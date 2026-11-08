"""Catalog formatting and filtering."""

def trim_names(names):
    output = []
    for name in names:
        output.append(name.strip())
    return output


def names_trimmed(names):
    return [name.strip() for name in names]


def trim_nonempty_names(names):
    output = []
    for name in names:
        if name.strip():
            output.append(name.strip())
    return output


def unique_names(names):
    output = []
    for name in names:
        if name not in output:
            output.append(name)
    return output


def names_as_set(names):
    return list(set(names))


def first_three(names):
    return names[:3]


def first_four(names):
    return names[:4]
