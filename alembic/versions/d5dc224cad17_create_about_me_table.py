"""create about me table

Revision ID: d5dc224cad17
Revises: cc97233440c8
Create Date: 2026-09-19 14:00:24.459538

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5dc224cad17'
down_revision: Union[str, Sequence[str], None] = 'cc97233440c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "about_me",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=150), nullable=False),
        sa.Column("headline", sa.String(length=200), nullable=False),
        sa.Column("bio", sa.Text(), nullable=False),
        sa.Column("location", sa.String(length=150), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("github_url", sa.String(length=500), nullable=False),
        sa.Column("linkedin_url", sa.String(length=500), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

def downgrade() -> None:
    op.drop_table("about_me")
