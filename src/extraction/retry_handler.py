from tenacity import retry, stop_after_attempt, wait_fixed


def retry_llm_call(func):
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(1),
        reraise=True,
    )
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
