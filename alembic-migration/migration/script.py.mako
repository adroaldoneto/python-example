"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade() -> None:
    ${upgrades if upgrades else "pass"}
    op.execute("INSERT INTO alembic_version_history (version_num, inserted_at, message) VALUES ('${up_revision}' ,NOW(), '${message}')")



def downgrade() -> None:
    ${downgrades if downgrades else "pass"}
