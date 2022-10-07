"""create posts table

Revision ID: bb05cddbe69d
Revises: 
Create Date: 2022-09-25 20:10:17.569521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb05cddbe69d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('sample_posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                                sa.Column('title',sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_table('sample_posts')
    