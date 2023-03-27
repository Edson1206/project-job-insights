from src.insights.jobs import read
from typing import List, Dict


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_list = read(path)
    industries = list()

    for job in jobs_list:
        industry = job["industry"].strip()
        if industry not in industries and industry != "":
            industries.append(industry)
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    jobs_filtered = []
    for job_listed in jobs:
        if job_listed["industry"] == industry:
            jobs_filtered.append(job_listed)
    return jobs_filtered
