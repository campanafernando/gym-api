from app.entities.base import Base
from app.entities.audits import Audits
from sqlalchemy.dialects import postgresql
import sqlalchemy as sa


class User(Base, Audits):
    id = sa.Column(
        postgresql.UUID(as_uuid=True),
        primary_key=True,
        server_default=sa.text("gen_random_uuid()"),
    )
    name = sa.Column(sa.String(255), nullable=False)
    status = sa.Column(sa.Boolean, nullable=False, default=True)
    email = sa.Column(sa.String(255), nullable=True)
    cpf = sa.Column(sa.String(255), nullable=False, index=True)
    birth_date = sa.Column(sa.Date(), nullable=False)
    phone = sa.Column(sa.String(255), nullable=True)
    height = sa.Column(sa.DECIMAL, nullable=True)
    weight = sa.Column(sa.DECIMAL, nullable=True)
