"""add user table

Revision ID: 36fc9de22bf2
Revises: 17a27fc6ef87
Create Date: 2022-09-25 20:48:06.248408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36fc9de22bf2'
down_revision = '17a27fc6ef87'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )

    pass


def downgrade() -> None:
    pass
