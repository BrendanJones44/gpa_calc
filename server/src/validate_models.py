def add_error(errors, error_type, error):
    """
    add_error to appropriate place in errors hash

    :param errors: the hash of {error_type:[error]} 's
    :param error_type: the type of error
    :param error: the error to add
    :return: none. Adds error to errors
    """
    if error_type in errors.keys():
        errors[error_type].append(error)
    else:
        errors[error_type] = [error]
