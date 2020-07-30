ternary_expression = (
    "Short String"
    if some_condition
    else (
        "This is a really long string that will eventually need to be split right here."
    )
)

ternary_expression = (
    "Short String"
    if some_condition
    else ("This is a really long string that will eventually need to be split right here.")
)


bad_split3 = (
    "What if we have inline comments on "  # First Comment
    "each line of a bad split? In that "  # Second Comment
    "case, we should just leave it alone."  # Third Comment
)

print(
    "This is a really long string inside of a print statement with no extra arguments"
    " attached at the end of it."
)

not_shareables = [
    # singletons
    True,
    False,
    NotImplemented, ...,
]

def foo3(list_a, list_b):
    # Standlone comment but weirdly placed.
    return User.query.filter(User.foo == "bar").filter(db.or_(
        User.field_a.astext.in_(list_a), User.field_b.astext.in_(list_b)
    )).filter(User.xyz.is_(None))

schema = {
    "mappings": {
        "test": {
            "properties": {
                "one_value": {
                    "type": "keyword",
                    "store": True,
                    "a": 1,
                    "b": 1,
                    "c": 1,
                    "d": 1,
                    "e": 1,
                }
            }
        }
    }
}

schema = {
    "mappings": {
        "test": {
            "properties": {
                "one_value": {
                    "type": "keyword",
                    "store": True,
                }
            }
        }
    }
}


# output
ternary_expression = (
    "Short String"
    if some_condition
    else (
        "This is a really long string that will eventually need to be split right here."
    )
)

ternary_expression = (
    "Short String"
    if some_condition
    else (
        "This is a really long string that will eventually need to be split right here."
    )
)


bad_split3 = (
    "What if we have inline comments on "  # First Comment
    "each line of a bad split? In that "  # Second Comment
    "case, we should just leave it alone."  # Third Comment
)

print(
    "This is a really long string inside of a print statement with no extra arguments"
    " attached at the end of it."
)

not_shareables = [
    # singletons
    True,
    False,
    NotImplemented,
    ...,
]


def foo3(list_a, list_b):
    # Standlone comment but weirdly placed.
    return (
        User
        .query
        .filter(User.foo == "bar")
        .filter(db.or_(
            User.field_a.astext.in_(list_a), User.field_b.astext.in_(list_b)
        ))
        .filter(User.xyz.is_(None))
    )


schema = {"mappings": {"test": {"properties": {"one_value": {
    "type": "keyword",
    "store": True,
    "a": 1,
    "b": 1,
    "c": 1,
    "d": 1,
    "e": 1,
}}}}}

schema = {"mappings": {"test": {"properties": {"one_value": {
    "type": "keyword",
    "store": True,
}}}}}
