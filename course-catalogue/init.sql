CREATE TABLE IF NOT EXISTS courses (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    credits INT
);

INSERT INTO courses (code, name, description, credits)
VALUES
('COMP601', 'Introduction to Programming', 'Learn the basics of modern programming using Python.', 15),
('COMP602', 'Data Structures', 'Covers arrays, lists, stacks, queues, trees, and graphs that make up programming languages.', 15),
('COMP603', 'Databases', 'Introduction to relational database design and SQL.', 15),
('COMP604', 'Web Development', 'Learn how to build modern web applications.', 15)
ON CONFLICT (code) DO NOTHING;
