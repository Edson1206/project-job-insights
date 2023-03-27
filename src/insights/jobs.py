import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as file:
        jobs_list = []
        jobs_csv = csv.DictReader(file, delimiter=",", quotechar='"')
        for item in jobs_csv:
            jobs_list.append(item)
        return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_list = read(path)
    job_types = set()
    for listed_job in jobs_list:
        job_types.add(listed_job['job_type'])
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtered_jobs = []
    for listed_job in jobs:
        if listed_job["job_type"] == job_type:
            filtered_jobs.append(listed_job)
    return filtered_jobs
