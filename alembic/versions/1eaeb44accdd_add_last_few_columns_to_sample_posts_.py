"""add last few columns to sample_posts table

Revision ID: 1eaeb44accdd
Revises: 229a17ebebe8
Create Date: 2022-09-25 21:28:48.444859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1eaeb44accdd'
down_revision = '229a17ebebe8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('sample_posts',sa.Column(
        'published',sa.Boolean(),nullable=False,server_default='TRUE'),)
    op.add_column('sample_posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()'),))
    
    pass


def downgrade() -> None:
    op.drop_column('sample_posts','published')
    op.drop_column('sample_posts','created_at')
    pass
