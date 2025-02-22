import os
from dotenv import load_dotenv
from sqlmesh.core.config import (
    Config,
    ModelDefaultsConfig,
    GatewayConfig,
    FabricSQLConnectionConfig
)

load_dotenv()

HOST=os.getenv('FABRIC__ENDPOINT', '')
USER=f"{os.getenv('FABRIC__CLIENT_ID')}@{os.getenv('FABRIC__TENANT_ID')}"
PASSWORD=os.getenv('FABRIC__CLIENT_SECRET')
DATABASE=os.getenv('FABRIC__DATABASE')

config = Config(
    project="sqlmesh-fabric",
    gateways={
            "fabric": GatewayConfig(
                connection=FabricSQLConnectionConfig(
                    host=HOST,
                    authentication="ActiveDirectoryServicePrincipal",
                    user=USER,
                    password=PASSWORD,
                    database=DATABASE,
                    driver="pyodbc"
                )
            ),
        },
    default_gateway="fabric",
    model_defaults=ModelDefaultsConfig(
        dialect="tsql",
        start="2025-01-01",
        cron="*/5 * * * *"
    )
)