-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT ts.title
FROM tv_shows ts
    LEFT JOIN tv_genres tg ON ts.genre_id = tg.id
    AND tg.name = 'Comedy'
WHERE tg.id IS NULL
ORDER BY ts.title ASC;