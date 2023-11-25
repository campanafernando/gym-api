import re
from sqlalchemy.orm import as_declarative, declared_attr


def camel_case_to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


@as_declarative()
class Base:
    __name__: str

    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:  # pylint: disable=no-self-argument
        return camel_case_to_snake_case(cls.__name__)
