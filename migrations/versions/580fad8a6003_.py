"""empty message

Revision ID: 580fad8a6003
Revises: 77600c67e11a
Create Date: 2022-07-30 12:15:17.842029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '580fad8a6003'
down_revision = '77600c67e11a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_employees_email'), ['email'])

    with op.batch_alter_table('hypervisor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('custid', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_hypervisor_customers_id_customers', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_hypervisor_custid_customers'), 'customers', ['custid'], ['id'])
        batch_op.drop_column('customers_id')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_users_email'), ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_users_email'), type_='unique')

    with op.batch_alter_table('hypervisor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('customers_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_hypervisor_custid_customers'), type_='foreignkey')
        batch_op.create_foreign_key('fk_hypervisor_customers_id_customers', 'customers', ['customers_id'], ['id'])
        batch_op.drop_column('custid')

    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_employees_email'), type_='unique')

    # ### end Alembic commands ###
