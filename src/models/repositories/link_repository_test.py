import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
from .link_repository import LinkRepository

db_connection_handler.connect()
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao  com o banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_to_repository = LinkRepository(conn)

    link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "google.com",
        "title": "Google"
    }

    link_to_repository.registry_links(link_infos)

@pytest.mark.skip(reason="interacao  com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    liks_to_repository = LinkRepository(conn)

    response = liks_to_repository.find_links_from_trip(trip_id)
    assert isinstance(response, list)
    assert isinstance(response[0], tuple)