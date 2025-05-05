CREATE TABLE store (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(255)
);

CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

CREATE TABLE price (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    store_id INT NOT NULL,
    value DECIMAL(10, 2) NOT NULL,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (store_id) REFERENCES store(id),
    UNIQUE (product_id, store_id, start_datetime)
);

CREATE TABLE promotion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    discount_percent DECIMAL(5,2) NOT NULL CHECK (discount_percent >= 0 AND discount_percent <= 100),
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME NOT NULL
);

CREATE TABLE promotion_product_store (
    id INT AUTO_INCREMENT PRIMARY KEY,
    promotion_id INT NOT NULL,
    product_id INT NOT NULL,
    store_id INT NOT NULL,
    FOREIGN KEY (promotion_id) REFERENCES promotion(id),
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (store_id) REFERENCES store(id)
);
