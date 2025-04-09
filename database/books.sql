CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    year_published INTEGER,
    status TEXT CHECK(status IN ('Available', 'Borrowed')) NOT NULL
);
