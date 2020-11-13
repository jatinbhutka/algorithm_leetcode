'''
Query for % contribution of individual channels and combunation of pairs of channels
'''

SELECT 
	cpc,
	organic,
	affiliate,
	social,
	COUNT(DISTINCT userid) AS total_signups,
	COUNT(DISTINCT userid)/(SELECT COUNT(*) FROM user_signup_data) AS percent_of_total
FROM user_signup_data
GROUP BY 1,2,3,4
ORDER BY 6 DESC;




'''
Below Query returns avg. number of account signups on the days when TV campaign was run = 68.75
'''

WITH cte_avg_signups_TvCampaign AS
(
	SELECT
		c.date,
	 	COUNT(u.userid) AS total_signups 
	FROM 
		tv_campaigns c LEFT JOIN user_signup_data u ON c.date = u.signup_date 
	GROUP BY c.date
)
SELECT 
	AVG(c.total_signups) AS avg_campaign_signups 
FROM cte_avg_signups_TvCampaign c;




	
'''
Below Query returns avg. number of account signups on the days when TV campaign was NOT run = 53.61
'''	

with cte_avg_signups_Non_TvCampaign AS
(
	SELECT 
		u.signup_date AS date,
		COUNT(u.user_id) AS total_signups
	FROM user_signup_data u
	WHERE 
		u.signup_date NOT IN (SELECT date FROM tv_campaigns)
	GROUP BY u.signup_date
)
SELECT 
	AVG(c.total_signups) AS avg_non_campaign_signups 
FROM cte_avg_signups_Non_TvCampaign c;


'''
We see 28% lift in the avg. account signups on the days TV campaign was run.
'''
