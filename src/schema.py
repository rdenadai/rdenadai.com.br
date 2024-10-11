from enum import StrEnum


class CSSTab(StrEnum):
    active: str = "text-blue-900 border-blue-900active dark:text-blue-900 dark:border-blue-900"
    deactive: str = "border-transparent hover:text-gray-600 hover:border-gray-300 dark:hover:text-gray-300"


CSS_TABS: dict[str, dict[str, dict]] = {
    "essays": {"tab": {}},
    "profile": {"tab": {}},
    "resume": {"tab": {}},
    "ai": {"tab": {}},
    "references": {"tab": {}},
}


for ref in ("essays", "profile", "resume", "ai", "references"):
    for xref in ("essays", "profile", "resume", "ai", "references"):
        CSS_TABS[ref]["tab"][xref] = CSSTab.active.value if ref == xref else CSSTab.deactive.value
