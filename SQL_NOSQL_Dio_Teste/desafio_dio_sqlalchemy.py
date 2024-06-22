"""Desafio DIO, criar banco de dados com duas tabelas, Cliente e Conta, utilizando SQLAlchemy
"""
import sqlalchemy
import sqlalchemy.orm

Base = sqlalchemy.orm.declarative_base()

class Cliente(Base):
    """Classe para criação da tabela Cliente
    """
    __tablename__ = "contas_clientes"

    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    fullname = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.orm.relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente(id = {self.id}, name = {self.name}, fullname= {self.fullname})"

class Address(Base):
    """Classe para criação da tabela Address
    """
    __tablename__ = "address"
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    email_address = sqlalchemy.Column(sqlalchemy.String)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("contas_clientes.id")
                                )


    user = sqlalchemy.orm.relationship("Cliente", back_populates="address")

    def __repr__(self):
        return f"Address(id = {self.id}, email_address = {self.email_address}])"


print(Cliente.__tablename__)
print(Address.__tablename__)

engine = sqlalchemy.create_engine("sqlite://")

Base.metadata.create_all(engine)

inspector_engine = sqlalchemy.inspect(engine)

print(inspector_engine.has_table("contas_clientes"))
print(inspector_engine.get_table_names())
print(inspector_engine.default_schema_name)

with sqlalchemy.orm.Session(engine) as session:
    rodney = Cliente(
        name ='Rodney',
        fullname = 'Rodney Ribeiro',
        address = [Address(email_address = 'rodney@email.com')]
    )

    maria = Cliente(
        name = 'Maria',
        fullname = 'Maria Silva',
        address = [Address(email_address = 'maria@email.com')]
    )

    session.add_all([rodney,maria])
    session.commit()

teste_select_cliente = sqlalchemy.select(Cliente).where(Cliente.name.in_(['Rodney','Maria']))

print('\nExplorando as Tabelas\n')

for usuario in session.scalars(teste_select_cliente):
    print(usuario)

teste_select_address = sqlalchemy.select(Address).where(Address.user_id.in_([2]))

for address in session.scalars(teste_select_address):
    print (address)
# EOF

#TESTE
