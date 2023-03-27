from src.insights.jobs import read
from typing import Union, List, Dict


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    salaries = set()
    for job in jobs_list:
        if job['max_salary'].isnumeric():
            salaries.add(int(job['max_salary']))
    return max(salaries)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    salaries = set()
    for job in jobs_list:
        if job['min_salary'].isnumeric():
            salaries.add(int(job['min_salary']))
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])

        if callable(salary) or None in job.values() or min_salary > max_salary:
            raise ValueError
        return int(salary) in range(min_salary, max_salary)
    except TypeError:
        raise ValueError
    except KeyError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_filtered = []

    for jobs_list in jobs:
        try:
            verify_bool = matches_salary_range(jobs_list, salary)
        except ValueError:
            verify_bool = False
        if verify_bool:
            jobs_filtered.append(jobs_list)

    return jobs_filtered
