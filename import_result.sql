
DROP TABLE IF EXISTS Days_Stats;

CREATE TABLE Days_Stats
(
	Day int,
	Posts int,
	Votes int,
	Comments int
);

-- 57243;2016-03-31 19:55:33.127923-07;We Are Heroes;The next-gen MOBA+ RPG for mobile devices;443077;anh;1;0;http://www.producthunt.com/l/b3443c7ac79b50;http://www.producthunt.com/posts/we-are-heroes-2
-- 57242;2016-03-31 19:53:36.614695-07;Tesla Model 3;The mass market electric car by Tesla is here ⚡️🚘;16056;erictwillis;44;18;http://www.producthunt.com/l/3843d5a8440dc8;http://www.producthunt.com/posts/tesla-model-3-2

LOAD DATA LOCAL INFILE 'out.csv'
INTO TABLE Days_Stats
FIELDS TERMINATED BY ';'
    ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES -- Skip header
(Day, Posts, Votes, Comments);
SHOW warnings;
