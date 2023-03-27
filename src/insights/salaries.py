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
    value = int(salary) if isinstance(salary, str) else salary

    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError("'min_salary' or 'max_salary' doesn't exist.")

    elif (type(job["min_salary"]) != int or type(job["max_salary"]) != int):
        raise ValueError("'min_salary' or 'max_salary' aren't valid integers.")

    elif (job["min_salary"] > job["max_salary"]):
        raise ValueError("'min_salary' is greater than 'max_salary'.")

    return True if job["min_salary"] <= value <= job["max_salary"] else False


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
    raise NotImplementedError
