import sqlite3 as sql

try:
    from src.db.config import ROOT_PATH
except ModuleNotFoundError:
    from config import ROOT_PATH


def get_db(language: str) -> list[tuple[str]]:
    """Get language database

    Args:
        language (str): Selected language

    Returns:
        list[tuple[str]]: list of texts
    """
    db_path = ROOT_PATH / "db" / language / "text.db"
    if not db_path.exists():
        print(f"Language <{language}> not found")
        return
    db = sql.connect(str(db_path))
    cursor = db.cursor()
    result = cursor.execute("SELECT text FROM text")
    return result.fetchall()
