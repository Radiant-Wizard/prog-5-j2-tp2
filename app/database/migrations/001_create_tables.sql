CREATE TYPE renter_type AS ENUM(
'PERSONAL', 'ENTREPRISE'
);

CREATE TABLE IF NOT EXISTS renter(
  id SERIAL PRIMARY KEY,
  name varchar(50),
  type renter_type
);

CREATE TABLE IF NOT EXISTS car(
  id SERIAL PRIMARY KEY,
  carReference varchar(10) UNIQUE,
  dailyPrice NUMERIC(100, 2)
);


CREATE TABLE IF NOT EXISTS carRent(
  id SERIAL PRIMARY KEY,
  rentDurationInDay int,
  carId INT REFERENCES car(id),
  renterId INT REFERENCES renter(id)
);

CREATE TABLE IF NOT EXISTS moneyRent(
  id SERIAL PRIMARY KEY,
  amount NUMERIC(100, 2),
  interest NUMERIC(10, 2),
  renterId INT REFERENCES renter(id)
);
