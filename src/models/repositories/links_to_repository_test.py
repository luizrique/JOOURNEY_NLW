import pytest 
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .links_to_repository_test import LinksToRepository

db_connection_handler.connect()
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao  com o banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_to_repository = LinksToRepository(conn)

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
    liks_to_repository = LinksToRepository(conn)

    response = liks_to_repository.find_links_from_trip(trip_id)
    assert isinstance(response, list)
    assert isinstance(response[0], tuple)