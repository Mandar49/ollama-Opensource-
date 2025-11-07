from common import vn

# The DDL for the tables in the ad_ai_testdb database
ddl = """
CREATE TABLE IF NOT EXISTS ad_campaigns (
    campaign_id INT AUTO_INCREMENT PRIMARY KEY,
    campaign_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS ad_performance (
    performance_id INT AUTO_INCREMENT PRIMARY KEY,
    campaign_id INT,
    report_date DATE,
    impressions INT,
    clicks INT,
    spend DECIMAL(10, 2),
    FOREIGN KEY (campaign_id) REFERENCES ad_campaigns(campaign_id)
);
"""
vn.train(ddl=ddl)

# Documentation for the business logic and definitions
vn.train(documentation="Impressions are the number of times an ad is shown.")
vn.train(documentation="Clicks are the number of times an ad is clicked.")
vn.train(documentation="Spend is the amount of money spent on a campaign.")

# Complex Question-SQL pairs to train the model on specific queries
vn.train(
    question="What is the total spend for the 'Summer Sale' campaign?",
    sql="""
    SELECT SUM(p.spend)
    FROM ad_performance p
    JOIN ad_campaigns c ON p.campaign_id = c.campaign_id
    WHERE c.campaign_name = 'Summer Sale'
    """
)
vn.train(
    question="How many impressions did we get for the 'Back to School' campaign?",
    sql="""
    SELECT SUM(p.impressions)
    FROM ad_performance p
    JOIN ad_campaigns c ON p.campaign_id = c.campaign_id
    WHERE c.campaign_name = 'Back to School'
    """
)

print("Training complete. The chroma.sqlite3 vector store has been created.")
