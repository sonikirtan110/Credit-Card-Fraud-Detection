CREATE TABLE fraud_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amt DECIMAL(10,2),
    city_pop INT,
    lat DECIMAL(9,6),
    `long` DECIMAL(9,6),
    merch_lat DECIMAL(9,6),
    merch_long DECIMAL(9,6),
    unix_time BIGINT,
    category VARCHAR(50),
    prediction VARCHAR(20),
    probability DECIMAL(5,2),
    recommendation VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
