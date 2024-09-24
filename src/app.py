import markdown
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.responses import RedirectResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.schema import CSS_TABS
from src.utils import async_file_loader, load_essays_data

N_PAGE = 5

TEMPLATES = Jinja2Templates(directory="templates")


async def index(request):
    return RedirectResponse(url="/essays")


async def essays(request):
    page = int(request.query_params.get("page", 1))

    about_md = markdown.markdown(await async_file_loader("static/pages/README.md"), tab_length=2)

    essays = await load_essays_data()

    essays_total = len(essays)
    essays = essays[(page - 1) * N_PAGE : page * N_PAGE]
    has_more_essays = essays_total > page * N_PAGE

    return TEMPLATES.TemplateResponse(
        request,
        "pages/essays.html",
        {
            "about_md": about_md,
            "essays": essays,
            "page": page,
            "previous": page - 1 if page - 1 > 0 else 0,
            "next": page + 1 if has_more_essays else 0,
            "css": CSS_TABS.get("essays"),
        },
    )


async def essay(request):
    essay_id = int(request.path_params.get("essay", 1))
    essay = next(essay for essay in await load_essays_data() if essay.get("id") == essay_id)
    content = markdown.markdown(await async_file_loader(f"static/pages/essays/{essay_id}/README.md"), tab_length=2)

    return TEMPLATES.TemplateResponse(
        request,
        "pages/essay.html",
        {"essay": essay, "content": content, "css": CSS_TABS.get("essays")},
    )


async def profile(request):
    profile = markdown.markdown(await async_file_loader("static/pages/profile/README.md"), tab_length=2)

    return TEMPLATES.TemplateResponse(
        request,
        "pages/profile.html",
        {"profile": profile, "css": CSS_TABS.get("profile")},
    )


async def resume(request):
    resume = markdown.markdown(await async_file_loader("static/pages/resume/README.md"), tab_length=2)

    return TEMPLATES.TemplateResponse(
        request,
        "pages/resume.html",
        {"resume": resume, "css": CSS_TABS.get("resume")},
    )


routes = [
    Route("/", endpoint=index),
    Route("/essays", endpoint=essays),
    Route("/essay/{essay}", endpoint=essay),
    Route("/profile", endpoint=profile),
    Route("/resume", endpoint=resume),
    Mount("/static", StaticFiles(directory="static"), name="static"),
]

middleware = [Middleware(GZipMiddleware, minimum_size=600, compresslevel=9)]
app = Starlette(debug=False, routes=routes, middleware=middleware)
