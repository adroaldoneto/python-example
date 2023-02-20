"""test

Revision ID: e51fd87cac46
Revises: 
Create Date: 2023-01-27 19:26:27.801322

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'e51fd87cac46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.execute(open('migration/versions/001_create_product_table.sql', 'r').read())
    op.execute("""
    CREATE TABLE alembic_version_history (
        version_num VARCHAR(32),
        inserted_at TIMESTAMP,
        message TEXT
    );
    
    CREATE TABLE product (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price INTEGER NOT NULL
    );
    """)


def downgrade() -> None:
    op.execute("DROP TABLE product;")
