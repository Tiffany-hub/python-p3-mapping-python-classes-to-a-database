from config import CONN, CURSOR

class Song:
    """
    Represents a song and provides methods to interact with a database table for storing songs.
    """

    def __init__(self, name: str, album: str):
        """
        Initializes a song instance with a name and album.

        Args:
            name (str): The name of the song.
            album (str): The album of the song.
        """
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        """
        Creates a table for songs if it does not exist.
        """
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)

    def save(self):
        """
        Saves the song instance to the table.
        """
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))

        # Get the last inserted row ID and assign it to self.id
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name: str, album: str) -> 'Song':
        """
        Creates a song instance, saves it to the table, and returns it.

        Args:
            name (str): The name of the song.
            album (str): The album of the song.

        Returns:
            Song: The created song instance.
        """
        song = cls(name, album)
        song.save()
        return song
