SELECT twitter;
CREATE TABLE TweetsEurovision2023 (
	ObservationNumber INT PRIMARY KEY,
	PostingDate DATE,
	TweetContent VARCHAR(500),
	SentimentLabel VARCHAR(45),
	p_positive FLOAT,
	p_negative FLOAT
)
SELECT * FROM tweetseurovision2023V2;
SELECT COUNT(date) FROM tweetseurovision2023V2 GROUP BY date LIKE '2023-05-14%'; 
-- or date LIKE '2023-05-13%'--
SELECT COUNT(date) AS dia13 FROM tweetseurovision2023V2 WHERE date LIKE '2023-05-13%';
