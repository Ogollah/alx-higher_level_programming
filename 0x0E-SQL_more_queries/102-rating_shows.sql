-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT CONCAT(ts.title, ' ', IFNULL(SUM(tr.rating), 0)) AS `tv_show_rating_sum`
FROM tv_shows ts
    LEFT JOIN tv_shows_rate tr ON ts.id = tr.show_id
GROUP BY ts.id,
    ts.title
ORDER BY SUM(tr.rating) DESC;