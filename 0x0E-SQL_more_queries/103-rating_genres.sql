-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT CONCAT(tg.name, ' ', IFNULL(SUM(tr.rating), 0)) AS `genre_rating_sum`
FROM tv_genres tg
    LEFT JOIN tv_shows ts ON tg.id = ts.genre_id
    LEFT JOIN tv_shows_rate tr ON ts.id = tr.show_id
GROUP BY tg.id,
    tg.name
ORDER BY SUM(tr.rating) DESC;