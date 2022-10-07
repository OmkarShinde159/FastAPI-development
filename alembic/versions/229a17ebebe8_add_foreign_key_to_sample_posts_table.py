"""add foreign-key to sample_posts table

Revision ID: 229a17ebebe8
Revises: 36fc9de22bf2
Create Date: 2022-09-25 21:07:00.688477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '229a17ebebe8'
down_revision = '36fc9de22bf2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('sample_posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('sample_posts_users_fk',source_table="sample_posts",
            referent_table="users",local_cols=["owner_id"],remote_cols=["id"],ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('sample_posts_users_fk',table_name='sample_posts')
    op.drop_column('sample_posts','owner_id')
    pass
