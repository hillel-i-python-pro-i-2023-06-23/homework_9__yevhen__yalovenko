from typing import NamedTuple
from collections.abc import Iterator

from app.loggers.loggers import get_core_logger
from app.services.faker import faker


class User(NamedTuple):
    username: str
    email: str

    def get_dict(self) -> dict:
        return self._asdict()

    @classmethod
    def get_fieldnames(cls) -> list[str]:
        return list(cls._fields)

    @classmethod
    def from_raw_dict(cls, raw_data: dict) -> "User":
        return cls(
            username=raw_data["username"],
            email=raw_data["email"],
        )


def generate_user() -> User:
    return User(
        username=faker.first_name(),
        email=faker.email(),
    )


def generate_users(amount: int) -> Iterator[User]:
    logger = get_core_logger()

    logger.debug(msg="generate_users.start")

    for index in range(1, amount + 1):
        logger.debug(f"generate_users.iteration.{index}/{amount}")
        yield generate_user()

    logger.debug("generate_users.end")



