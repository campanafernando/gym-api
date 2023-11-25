import sqlalchemy as sa


class Audits:
    date_created = sa.Column('date_created', sa.TIMESTAMP(True), server_default=sa.sql.func.now())
    date_updated = sa.Column('date_updated', sa.TIMESTAMP(True), server_default=sa.sql.func.now(), onupdate=sa.sql.func.now())