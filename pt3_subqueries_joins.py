# Part 3: Subqueries & Joins


def top_postcodes_for_chain_stores():
    """
    From the businesses table, select the top 10 most popular postal_code.
    They should be filtered to only count the restaurants owned by people/entities that own 5 or more restaurants.
    The result should:
    * return a row (postal_code, frequency) for each 10 selection
    * sort by descending order to get the most relevant zip codes
    :return: a string representing the SQL query
    :rtype: str
    """

    return "SELECT postal_code, COUNT(postal_code) as count FROM businesses as b WHERE b.owner_name in \
    (SELECT owner_name FROM businesses GROUP BY owner_name HAVING COUNT(business_id) >= 5) \
    GROUP BY postal_code ORDER BY count DESC LIMIT 10"


def inspection_scores_in_94103():
    """
    First let's get an idea about the inspection score our competition has.
    Based on multiple inspections, find out the minimum Score (as "min_score"),
    average Score (as "avg_score") and maximum Score (as "max_score") for all restaurant in post code "94103".
    The average score should be rounded to one decimal.
    :return: a string representing the SQL query
    :rtype: str
    """

    return "SELECT MIN(Score) AS min_score, ROUND(AVG(Score), 1) AS avg_score, MAX(Score) AS max_score \
    FROM businesses AS b JOIN inspections AS i ON b.business_id = i.business_id WHERE postal_code == '94103'"


def risk_categories_in_94103():
    """
    Now lets get more serious, and look at how many times restaurants with postal code 94103
    (that's Market street) has committed health violations and group them based on their risk category.
    The output should be (risk_category, count as frequency) and sorted in descending order by frequency
    :return: a string representing the SQL query
    :rtype: str
    """

    return "SELECT risk_category, COUNT(*) AS frequency \
    FROM businesses AS b JOIN violations as v ON b.business_id = v.business_id \
    WHERE postal_code == '94103' GROUP BY risk_category ORDER BY frequency DESC"
