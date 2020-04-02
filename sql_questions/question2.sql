
--postgresql
-- question 2

CREATE TABLE user_sales(
	userid int,
	saleid int
);

INSERT INTO user_sales(userid, saleid)
VALUES
		(1, 1),
		(1, 2),
		(1, 3),
		(2, 3),
		(2, 4),
		(3, 5),
		(3, 6),
		(3, 7),
		(4, 8);

CREATE TABLE sale_amount(
	saleid int,
	amount money
);

INSERT INTO sale_amount(saleid, amount)
VALUES
	(1, '$4.00'),
	(2, '$3.50'),
	(3, '$2.00'),
	(4, '$3.75'),
	(5, '$5.25'),
	(6, '$3.00');

-- query for question 2
select userid, sum(amount)
from user_sales inner join sale_amount on (user_sales.saleid = sale_amount.saleid)
group by userid
having (sum(amount) > '$4') and (sum(amount) < '$6');