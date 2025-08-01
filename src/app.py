from uuid import UUID

import markdown
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.data import QUESTIONS_AI_DATA
from src.rss import rss_endpoint
from src.schema import CSS_TABS
from src.utils import async_file_loader, get_posted_at, load_essays_data

N_PAGE = 5

TEMPLATES = Jinja2Templates(directory="templates")

MARKDOWN_DEFAULT_CONFIG = {
    "extensions": [
        "markdown.extensions.fenced_code",
        "markdown.extensions.tables",
        "markdown.extensions.nl2br",
    ],
    "tab_length": 2,
}


async def load_default_route(request, html_page: str, markdown_file: str, tab: str):
    content = markdown.markdown(await async_file_loader(markdown_file), **MARKDOWN_DEFAULT_CONFIG)
    return TEMPLATES.TemplateResponse(
        request,
        html_page,
        {tab: content, "css": CSS_TABS.get(tab)},
    )


async def index(request):
    return await load_default_route(request, "pages/index.html", "static/pages/README.md", "index")


async def essays(request):
    page = int(request.query_params.get("page", 1))

    essays = await load_essays_data()
    total_essays = len(essays)
    essays = essays[(page - 1) * N_PAGE : page * N_PAGE]
    has_more_essays = total_essays > page * N_PAGE

    return TEMPLATES.TemplateResponse(
        request,
        "pages/essays.html",
        {
            "essays": essays,
            "page": page,
            "previous": page - 1 if page - 1 > 0 else 0,
            "next": page + 1 if has_more_essays else 0,
            "css": CSS_TABS.get("essays"),
        },
    )


async def essay(request):
    try:
        field = "alternate"
        essay_id = request.path_params.get("essay", "")
        if essay_id.isdigit():
            field = "id"
            essay_id = int(essay_id)

        essay = next(essay for essay in await load_essays_data() if essay.get(field) == essay_id)
        markdown_file = f"static/pages/essays/{essay.get('id')}/README.md"
        content = markdown.markdown(await async_file_loader(markdown_file), **MARKDOWN_DEFAULT_CONFIG)

        return TEMPLATES.TemplateResponse(
            request,
            "pages/essay.html",
            {
                "essay": essay,
                "posted_at": get_posted_at(essay.get("created_at")),
                "content": content,
                "css": CSS_TABS.get("essays"),
            },
        )
    except Exception:
        return RedirectResponse(url="/essays")


async def profile(request):
    return await load_default_route(request, "pages/profile.html", "static/pages/profile/README.md", "profile")


async def resume(request):
    return await load_default_route(request, "pages/resume.html", "static/pages/resume/README.md", "resume")


async def references(request):
    return await load_default_route(request, "pages/references.html", "static/pages/references/README.md", "references")


async def ai_hype_sanity_check(request):
    return TEMPLATES.TemplateResponse(
        request, "pages/ai-hype-sanity-check/index.html", {"data": QUESTIONS_AI_DATA, "css": CSS_TABS.get("ai")}
    )


async def ai_hype_sanity_check_result(request):
    try:
        profile_id = str(UUID(request.path_params.get("profile", "")))
        score = int(request.path_params.get("score", 0))

        return TEMPLATES.TemplateResponse(
            request,
            "pages/ai-hype-sanity-check/profile.html",
            {
                "profile": next(
                    filter(
                        lambda profile: profile.get("id") == profile_id
                        and score >= profile.get("min_score")
                        and score <= profile.get("max_score"),
                        QUESTIONS_AI_DATA.get("profiles", []),
                    )
                ),
                "score": score,
                "css": CSS_TABS.get("ai"),
            },
        )
    except Exception:
        return RedirectResponse(url="/ai-hype-sanity-check")


async def not_found(request: Request, exc: HTTPException):
    return TEMPLATES.TemplateResponse(request, "pages/error.html", {"css": CSS_TABS.get("essays")})


async def server_error(request: Request, exc: HTTPException):
    return TEMPLATES.TemplateResponse(request, "pages/error.html", {"css": CSS_TABS.get("essays")})


routes = [
    Route("/", endpoint=index),
    Route("/robots.txt", endpoint=RedirectResponse(url="/static/robots.txt")),
    Route("/essays", endpoint=essays),
    Route("/essay/{essay}", endpoint=essay),
    Route("/profile", endpoint=profile),
    Route("/resume", endpoint=resume),
    Route("/references", endpoint=references),
    Route("/ai-hype-sanity-check", endpoint=ai_hype_sanity_check),
    Route("/ai-hype-sanity-check/result/{profile}/{score}", endpoint=ai_hype_sanity_check_result),
    Route("/rss.xml", rss_endpoint),
    Mount("/static", StaticFiles(directory="static"), name="static"),
]

middleware = [Middleware(GZipMiddleware, minimum_size=600, compresslevel=9)]
app = Starlette(
    debug=False, routes=routes, middleware=middleware, exception_handlers={404: not_found, 500: server_error}
)
