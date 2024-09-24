from enum import StrEnum
from types import MappingProxyType


class CSSTab(StrEnum):
    active: str = "text-blue-900 border-blue-900active dark:text-blue-900 dark:border-blue-900"
    deactive: str = "border-transparent hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300"


CSS_TABS = MappingProxyType(
    {
        "essays": {
            "tab": {
                "essays": CSSTab.active.value,
                "profile": CSSTab.deactive.value,
                "resume": CSSTab.deactive.value,
                "ai": CSSTab.deactive.value,
            }
        },
        "profile": {
            "tab": {
                "profile": CSSTab.active.value,
                "essays": CSSTab.deactive.value,
                "resume": CSSTab.deactive.value,
                "ai": CSSTab.deactive.value,
            }
        },
        "resume": {
            "tab": {
                "resume": CSSTab.active.value,
                "essays": CSSTab.deactive.value,
                "profile": CSSTab.deactive.value,
                "ai": CSSTab.deactive.value,
            }
        },
        "ai": {
            "tab": {
                "ai": CSSTab.active.value,
                "essays": CSSTab.deactive.value,
                "profile": CSSTab.deactive.value,
                "resume": CSSTab.deactive.value,
            }
        },
    }
)
