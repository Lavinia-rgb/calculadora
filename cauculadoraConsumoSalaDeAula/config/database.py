from peewee import SqliteDatabase

# Define the database
database = SqliteDatabase('database-v5.db')

def startup_db():
    database.connect()
    # Import models inside the function to avoid circular import issues
    from models.bandeira import BandeiraDB
    from models.dependencia import DependenciaDB
    from models.dispositivo import DispositivoDB
    from models.tipo_consumidor import TipoConsumidorDB
    from models.tipo_dispositivo import TipoDispositivoDB
    from models.unidade_consumidora import UnidadeConsumidoraDB
    # Create tables
    database.create_tables([
        UnidadeConsumidoraDB,
        BandeiraDB,
        DependenciaDB,
        DispositivoDB,
        TipoConsumidorDB,
        TipoDispositivoDB,
    ])

def shutdown_db():
    database.close()
