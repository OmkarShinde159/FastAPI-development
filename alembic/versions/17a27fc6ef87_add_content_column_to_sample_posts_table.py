"""add content column to sample_posts table

Revision ID: 17a27fc6ef87
Revises: bb05cddbe69d
Create Date: 2022-09-25 20:36:51.494079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17a27fc6ef87'
down_revision = 'bb05cddbe69d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('sample_posts',sa.Column('content',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('sample_posts','content')
    pass
