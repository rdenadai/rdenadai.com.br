from datetime import datetime

import xmltodict
from starlette.responses import Response

from src.utils import load_essays_data


async def generate_rss_feed():
    essays = await load_essays_data()
    rss_feed = {
        "rss": {
            "@version": "2.0",
            "channel": {
                "title": "Rodolfo De Nadai",
                "link": "https://rdenadai.com.br",
                "description": "Explore essays on technology, programming, and artificial intelligence.",
                "category": "Essays",
                "copyright": "",
                "language": "",
                "item": [
                    {
                        "title": essay.get("title"),
                        "link": f"https://rdenadai.com.br/essay/{essay.get('id')}",
                        "description": essay.get("description"),
                        "pubDate": datetime.fromisoformat(essay.get("created_at")).strftime("%a, %d %b %Y %H:%M:%S %z"),
                    }
                    for essay in essays
                ],
            },
        }
    }
    return xmltodict.unparse(rss_feed, pretty=True)


async def rss_endpoint(request):
    rss_xml = await generate_rss_feed()
    return Response(content=rss_xml, media_type="text/xml")
