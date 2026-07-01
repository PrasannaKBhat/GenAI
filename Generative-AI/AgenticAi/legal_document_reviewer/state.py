from typing import TypedDict


class ReviewState(TypedDict):
    file_path: str
    document: str

    summary: str
    risks: str
    compliance: str

    approval: str

    final_report: str