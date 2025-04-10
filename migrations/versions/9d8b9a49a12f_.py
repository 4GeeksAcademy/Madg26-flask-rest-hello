"""empty message

Revision ID: 9d8b9a49a12f
Revises: aff796361fbb
Create Date: 2025-04-10 00:49:39.426314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d8b9a49a12f'
down_revision = 'aff796361fbb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('instagram_media', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'instagram_post', ['post_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('instagram_media', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('post_id')

    # ### end Alembic commands ###
