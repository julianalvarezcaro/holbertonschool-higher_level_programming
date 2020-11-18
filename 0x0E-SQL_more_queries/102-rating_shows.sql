-- Lists all genres that are not of the show Dexter
-- Display: tv_genres.name
SELECT title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
INNER JOIN tv_show_ratings ON id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC
