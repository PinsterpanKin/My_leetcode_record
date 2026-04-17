#Without the application of the DENSE_RANK() function, the following SQL query can be used to calculate the rank of each score in the Scores table:

SELECT
    s1.score,
    (
        SELECT COUNT(DISTINCT s2.score)
        FROM Scores s2
        WHERE s2.score >= s1.score
    ) AS `rank`
FROM Scores s1
ORDER BY s1.score DESC;

#With DENSE_RANK() function, much more efficient:

SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores;