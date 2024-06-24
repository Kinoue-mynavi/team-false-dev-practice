USE mujiqlo_ticket;

CREATE TABLE mst_review (
    review_id INT PRIMARY KEY,
    event_id INT NOT NULL,
    customer_id INT NOT NULL,
    review_score VARCHAR(1),
    review_title VARCHAR(30),
    review_comment VARCHAR(500),
    FOREIGN KEY(event_id) REFERENCES mst_event(event_id),
    FOREIGN KEY(customer_id) REFERENCES mst_customer(customer_id)
);