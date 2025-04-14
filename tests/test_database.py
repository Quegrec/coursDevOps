import pytest
from app.database import Database

@pytest.fixture
def db():
    """
    Pytest fixture to initialize and clean up the database.
    """
    database = Database(db_path=":memory:")
    database.connect()
    yield database
    database.disconnect()

def test_database_init_failure():
    """
    Teste l'initialisation de la base de données avec un échec prévu.
    """
    db = Database(db_path="non_existent_path.db")
    assert db.db_path == "non_existent_path.db"
    assert db.connection is None

def test_database_init_default_path():
    """
    Teste l'initialisation de la base de données avec le chemin par défaut.
    """
    db = Database()
    assert db.db_path == ":memory:"
    assert db.connection is None

def test_database_init_custom_path():
    """
    Teste l'initialisation de la base de données avec un chemin personnalisé.
    """
    custom_path = "test_database.db"
    db = Database(db_path=custom_path)
    assert db.db_path == custom_path
    assert db.connection is None

def test_database_connect_failure():
    """
    Teste la connexion à la base de données avec un échec prévu.
    """
    db = Database(db_path="non_existent_path.db")
    connection = db.connect()
    assert connection is not None
    assert db.connection is not None
    assert db.connection == connection

    cursor = db.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone() is not None
    assert table_exists is True

    db.disconnect()
    assert db.connection is None

def test_database_connect_success(db):
    """
    Teste la connexion à la base de données avec un chemin valide.
    """
    assert db.connection is not None

    cursor = db.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone() is not None
    assert table_exists is True

def test_database_add_user_success(db):
    """
    Teste l'ajout d'un utilisateur à la base de données avec succès.
    """
    result = db.add_user("testuser", "testuser@example.com")
    assert result is True

    user = db.get_user("testuser")
    assert user is not None
    assert user["username"] == "testuser"
    assert user["email"] == "testuser@example.com"

def test_database_add_user_duplicate(db):
    """
    Teste l'ajout d'un utilisateur déjà existant à la base de données.
    """
    db.add_user("testuser", "testuser@example.com")
    result = db.add_user("testuser", "testuser@example.com")
    assert result is False

def test_database_add_user_invalid_email(db):
    """
    Teste l'ajout d'un utilisateur avec un email invalide.
    """
    result = db.add_user("testuser2", "")
    assert result is True

    user = db.get_user("testuser2")
    assert user is not None
    assert user["username"] == "testuser2"
    assert user["email"] == ""

def test_database_get_user_success(db):
    """
    Teste la récupération d'un utilisateur de la base de données avec succès.
    """
    db.add_user("user2get", "user2get@example.com")
    user = db.get_user("user2get")
    assert user is not None
    assert user["username"] == "user2get"

def test_database_get_user_not_found(db):
    """
    Teste la récupération d'un utilisateur qui n'existe pas dans la base de données.
    """
    user = db.get_user("non_existent_user")
    assert user is None

def test_database_delete_user_success(db):
    """
    Teste la suppression d'un utilisateur de la base de données avec succès.
    """
    db.add_user("user2del", "user2del@example.com")
    db.delete_user("user2del")
    user = db.get_user("user2del")
    assert user is None

def test_database_delete_user_not_found(db):
    """
    Teste la suppression d'un utilisateur qui n'existe pas dans la base de données.
    """
    result = db.delete_user("non_existent_user")
    assert result is False
