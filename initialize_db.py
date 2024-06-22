import sqlite3

# Connect to the database
con = sqlite3.connect('FireExtinguisherDB.db')
cr = con.cursor()

# Create table if it doesn't exist
cr.execute('''
CREATE TABLE IF NOT EXISTS info (
    Id TEXT PRIMARY KEY,
    ExpiryDate TEXT,
    RefillingDate TEXT,
    LastRefilledDate TEXT,
    Location TEXT,
    NearbyStation TEXT
)
''')

# Insert sample data
sample_data = [
    ('FX001', '2024-07-01', '2023-07-01', '2023-01-01', 'Location A', 'Station A'),
    # Add the remaining sample data here...
]

cr.executemany('INSERT OR IGNORE INTO info (Id, ExpiryDate, RefillingDate, LastRefilledDate, Location, NearbyStation) VALUES (?, ?, ?, ?, ?, ?)', sample_data)
con.commit()

# Close the connection to the database
con.close()
