"""mensagem

Revision ID: 58ede61e6760
Revises: e51fd87cac46
Create Date: 2023-01-28 23:03:59.626502

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '58ede61e6760'
down_revision = 'e51fd87cac46'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    CREATE TABLE product_test_2 (
        name VARCHAR(255) NOT NULL,
        test INTEGER NOT NULL
    );
    """)


def downgrade() -> None:
    op.execute("DROP TABLE product;")
