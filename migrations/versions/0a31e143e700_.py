"""empty message

Revision ID: 0a31e143e700
Revises: 
Create Date: 2021-03-11 22:41:36.433686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a31e143e700'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('author', sa.String(length=80), nullable=False),
    sa.Column('suitable_ages', sa.String(length=120), nullable=False),
    sa.Column('pages', sa.String(length=100), nullable=True),
    sa.Column('book_description', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('connections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=False),
    sa.Column('village_supplier', sa.Integer(), nullable=True),
    sa.Column('info_reservation', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['info_reservation'], ['leandings.id'], ),
    sa.ForeignKeyConstraint(['village_supplier'], ['villages.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('leandings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('package_id', sa.Integer(), nullable=True),
    sa.Column('returning_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['package_id'], ['packages.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('packages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('books_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('package_tittle', sa.String(length=120), nullable=True),
    sa.Column('suitable_ages', sa.String(length=120), nullable=True),
    sa.Column('subject', sa.String(length=120), nullable=True),
    sa.Column('reserved_status', sa.Boolean(), nullable=False),
    sa.Column('date_reservation', sa.String(length=120), nullable=True),
    sa.Column('package_description', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['books_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('package_tittle')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('dni', sa.Integer(), nullable=False),
    sa.Column('village', sa.Integer(), nullable=True),
    sa.Column('connection_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['connection_id'], ['connections.id'], ),
    sa.ForeignKeyConstraint(['village'], ['villages.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dni'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('villages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('village_name', sa.String(length=125), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('village_name')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('writer_revies_id', sa.Integer(), nullable=True),
    sa.Column('book_reviewed_id', sa.Integer(), nullable=True),
    sa.Column('text_review', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['book_reviewed_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['writer_revies_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('villages')
    op.drop_table('users')
    op.drop_table('packages')
    op.drop_table('leandings')
    op.drop_table('connections')
    op.drop_table('books')
    # ### end Alembic commands ###
