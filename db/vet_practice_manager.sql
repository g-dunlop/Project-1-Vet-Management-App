
DROP TABLE appointments;
DROP TABLE treatments;
DROP TABLE animals;
DROP TABLE owners;
DROP TABLE vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255)
    
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255),
    phone_number VARCHAR(255),
    email_address VARCHAR(255),
    address VARCHAR(255),
    registered BOOLEAN
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date_of_birth VARCHAR(255),
    type VARCHAR(255),
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE,
    treatment_notes VARCHAR(255)
    -- treatment notes will eventually be reference to appointment_id
);

CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    price FLOAT
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    animal_id INT REFERENCES animals(id) ON DELETE CASCADE,
    appointment_date DATE,
    appointment_time TIME,
    reason VARCHAR(255),
    treatment_id INT REFERENCES treatments(id) ON DELETE CASCADE
);

-- SELECT * FROM animals INNER JOIN vets ON animals.vet_id = vets.id;

-- SELECT * FROM animals INNER JOIN owners ON animals.owner_id = owners.id;

