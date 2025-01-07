from piccolo.engine import SQLiteEngine
from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry


DB = SQLiteEngine()

APP_REGISTRY = AppRegistry(
    apps=["home.piccolo_app", "piccolo_admin.piccolo_app"]
)
