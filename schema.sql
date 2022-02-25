CREATE TABLE users (	
	id SERIAL PRIMARY KEY, 
	username VARCHAR(144) NOT NULL UNIQUE,
	password VARCHAR(144),
	is_admin BOOLEAN
);

CREATE TABLE recommendations (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER REFERENCES users,
    media INTEGER, 
    header TEXT, 
    author TEXT,
    description TEXT, 
    url_link TEXT,
    ISBN TEXT
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY, 
    recommendations_id INTEGER REFERENCES recommendations,
    tag TEXT
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY, 
    recommendations_id INTEGER REFERENCES recommendations,
    course_header TEXT,
    course_id TEXT
);

CREATE TABLE favorites (
    id SERIAL PRIMARY KEY, 
    user_id INTEGER REFERENCES users,
    recommendations_id INTEGER REFERENCES recommendations,
    done_reading BOOLEAN
);

CREATE TABLE likes (
    result INTEGER,
	creation_time TIMESTAMP,
    recommendations_id INTEGER REFERENCES recommendations, 
    user_id INTEGER REFERENCES users
);
