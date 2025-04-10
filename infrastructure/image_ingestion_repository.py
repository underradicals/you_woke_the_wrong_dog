import sqlite3
from typing import Any, Generator


def get_distinct(connection: sqlite3.Connection, sql: str) -> Generator[Any, Any, None]:
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        yield row


def iter_gen(generator, column_name: str, resource_list: list) -> None:
    for item in generator:
        resource_list.append(item[column_name])


def fetch_all_icons(connection: sqlite3.Connection) -> Generator[Any, Any, None]:
    sql = """select distinct icon_url from Weapons;"""
    yield from get_distinct(connection, sql)


def fetch_all_watermarks(connection: sqlite3.Connection) -> Generator[Any, Any, None]:
    sql = """select distinct watermark_url from Weapons;"""
    yield from get_distinct(connection, sql)


def fetch_all_screenshots(connection: sqlite3.Connection) -> Generator[Any, Any, None]:
    sql = """select distinct screenshot_url from Weapons;"""
    yield from get_distinct(connection, sql)


def fetch_all_damage_types(connection: sqlite3.Connection) -> Generator[Any, Any, None]:
    sql = """select distinct damage_type_url from Weapons;"""
    yield from get_distinct(connection, sql)


def fetch_images(chunks: list[list[Any]]):
    for chunk in chunks:
        yield chunk
        
if __name__ == "__main__":
  pass