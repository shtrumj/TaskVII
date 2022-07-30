"""empty message

Revision ID: 77600c67e11a
Revises: 148e6b524551
Create Date: 2022-07-30 11:41:26.925327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77600c67e11a'
down_revision = '148e6b524551'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hypervisor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('customers_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'customers', ['customers_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hypervisor', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('customers_id')

    # ### end Alembic commands ###
