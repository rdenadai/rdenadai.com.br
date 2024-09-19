from enum import StrEnum

import markdown
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.responses import RedirectResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.utils import async_file_loader, load_essays_data

N_PAGE = 5

TEMPLATES = Jinja2Templates(directory="templates")


class CSSTab(StrEnum):
    active: str = "text-blue-900 border-blue-900active dark:text-blue-900 dark:border-blue-900"
    deactive: str = "border-transparent hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300"


async def homepage(request):
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
            "css": {
                "tab": {
                    "essays": CSSTab.active.value,
                    "profile": CSSTab.deactive.value,
                    "resume": CSSTab.deactive.value,
                }
            },
        },
    )


async def essay(request):
    essay_id = int(request.path_params.get("essay", 1))
    essay = next(essay for essay in await load_essays_data() if essay.get("id") == essay_id)
    content = markdown.markdown(await async_file_loader(f"static/pages/essays/{essay_id}/README.md"), tab_length=2)

    return TEMPLATES.TemplateResponse(
        request,
        "pages/essay.html",
        {
            "essay": essay,
            "content": content,
            "css": {
                "tab": {
                    "essays": CSSTab.active.value,
                    "profile": CSSTab.deactive.value,
                    "resume": CSSTab.deactive.value,
                }
            },
        },
    )


async def profile(request):
    profile = markdown.markdown(await async_file_loader("static/pages/profile/README.md"), tab_length=2)

    return TEMPLATES.TemplateResponse(
        request,
        "pages/profile.html",
        {
            "profile": profile,
            "css": {
                "tab": {
                    "essays": CSSTab.deactive.value,
                    "profile": CSSTab.active.value,
                    "resume": CSSTab.deactive.value,
                }
            },
        },
    )


async def resume(request):
    resume = markdown.markdown(await async_file_loader("static/pages/resume/README.md"), tab_length=2)

    return TEMPLATES.TemplateResponse(
        request,
        "pages/resume.html",
        {
            "resume": resume,
            "css": {
                "tab": {
                    "essays": CSSTab.deactive.value,
                    "profile": CSSTab.deactive.value,
                    "resume": CSSTab.active.value,
                }
            },
        },
    )


routes = [
    Route("/", endpoint=homepage),
    Route("/essays", endpoint=essays),
    Route("/essay/{essay}", endpoint=essay),
    Route("/profile", endpoint=profile),
    Route("/resume", endpoint=resume),
    Mount("/static", StaticFiles(directory="static"), name="static"),
]

middleware = [Middleware(GZipMiddleware, minimum_size=600, compresslevel=9)]
app = Starlette(debug=False, routes=routes, middleware=middleware)
