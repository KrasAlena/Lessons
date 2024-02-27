import functools


def remove_trailing_spaces(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [arg.strip() if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {key: value.strip() if isinstance(value, str) else value for key, value in kwargs.items()}
        return func(*new_args, **new_kwargs)

    return wrapper


def spaces_to_underscores(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [arg.replace(' ', '_') if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {key: value.replace(' ', '_') if isinstance(value, str) else value for key, value in
                      kwargs.items()}
        return func(*new_args, **new_kwargs)

    return wrapper


def text_into_lowercase(func: callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new_args = [arg.lower() if isinstance(arg, str) else arg for arg in args]
        new_kwargs = {key: value.lower() if isinstance(value, str) else value for key, value in
                      kwargs.items()}
        return func(*new_args, **new_kwargs)

    return wrapper


@text_into_lowercase
@spaces_to_underscores
@remove_trailing_spaces
def prompt_user(text):
    return f'Result is {text}'


result = prompt_user('  John ate an Apple    ')
print(result)