SELECT authid, count(*) as h_index
FROM
	(SELECT a.authid, c.outcitations, COUNT (c.pubid) AS citations_count, rank() over (partition by a.authid order by count(c.pubid) desc) as ranking
	FROM Authored a
	LEFT OUTER JOIN Citations c on a.pubid = c.outcitations
	GROUP BY a.authid, c.outcitations) t
WHERE ranking <= citations_count
GROUP BY authid;