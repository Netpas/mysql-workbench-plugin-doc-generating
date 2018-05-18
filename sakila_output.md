# sakila



Automatically generate documents. The latest form of document changes by *2018-05-17 11:05:00*

![Database Structure](./sakila.db.png)

## **<a id='actor'></a>actor**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='actor-actor-id'></a>`actor_id` | INT | PRIMARY, Not null |   |   |
| `first_name` | VARCHAR(45) |  |   |   |
| `last_name` | VARCHAR(45) |  |   |   |
| `last_update` | VARCHAR(45) |  |   |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `actor_id` | PRIMARY |   |


## **<a id='address'></a>address**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='address-address-id'></a>`address_id` | SMALLINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `address` | VARCHAR(50) BINARY | Not null |   |   |
| `address2` | VARCHAR(50) BINARY |  | `NULL` |   |
| `district` | VARCHAR(20) | Not null |   |   |
| `city_id` | SMALLINT UNSIGNED | Not null |   |  REFERENCES  [**city**](#city) ([**city_id**](#city-city-id)) |
| `postal_code` | VARCHAR(10) |  | `NULL` |   |
| `phone` | VARCHAR(20) | Not null |   |   |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `address_id` | PRIMARY |   |
| idx_fk_city_id | `city_id` | INDEX |   |


## **<a id='city'></a>city**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='city-city-id'></a>`city_id` | INT | PRIMARY, Not null |   |   |
| `city` | FLOAT | Not null |   |   |
| `country_id` | SMALLINT UNSIGNED | Not null |   |  REFERENCES  [**country**](#country) ([**country_id**](#country-country-id))  ON UPDATE CASCADE |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| idx_fk_country_id | `country_id` | INDEX |   |
| PRIMARY | `city_id` | PRIMARY |   |


## **<a id='country'></a>country**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='country-country-id'></a>`country_id` | SMALLINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `country` | VARCHAR(50) | Not null |   |   |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `country_id` | PRIMARY |   |


## **<a id='customer'></a>customer**

---

### *Description:*

Table storing all customers. Holds foreign keys to the address table and the store table where this customer is registered.

Basic information about the customer like first and last name are stored in the table itself. Same for the date the record was created and when the information was last updated.

### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='customer-customer-id'></a>`customer_id` | SMALLINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `store_id` | TINYINT UNSIGNED | Not null |   |  REFERENCES  [**store**](#store) ([**store_id**](#store-store-id))  ON UPDATE CASCADE |
| `first_name` | VARCHAR(45) | Not null |   |   |
| `last_name` | VARCHAR(45) | Not null |   |   |
| `email` | VARCHAR(50) |  | `NULL` |   |
| `address_id` | SMALLINT UNSIGNED | Not null |   |  REFERENCES  [**address**](#address) ([**address_id**](#address-address-id))  ON UPDATE CASCADE |
| `active` |  | Not null | `TRUE` |   |
| `create_date` | DATETIME | Not null |   |   |
| `last_update` | TIMESTAMP |  | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `customer_id` | PRIMARY |   |
| idx_fk_store_id | `store_id` | INDEX |   |
| idx_fk_address_id | `address_id` | INDEX |   |
| idx_last_name | `last_name` | INDEX |   |


## **<a id='film'></a>film**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='film-film-id'></a>`film_id` | SMALLINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `title` | VARCHAR(255) | Not null |   |   |
| `description` | TEXT |  |   |   |
| `release_year` | YEAR |  |   |   |
| `language_id` | TINYINT UNSIGNED | Not null |   |  REFERENCES  [**language**](#language) ([**language_id**](#language-language-id))  ON UPDATE CASCADE |
| `original_language_id` | TINYINT UNSIGNED |  | `NULL` |  REFERENCES  [**language**](#language) ([**language_id**](#language-language-id))  ON UPDATE CASCADE |
| `rental_duration` | TINYINT UNSIGNED | Not null | `3` |   |
| `rental_rate` | DECIMAL | Not null | `4.99` |   |
| `length` | SMALLINT UNSIGNED |  | `NULL` |   |
| `replacement_cost` | DECIMAL | Not null | `19.99` |   |
| `rating` | ENUM |  | `'G'` |  `('G','PG','PG-13','R','NC-17')` |
| `special_features` | SET |  |   |  `('Trailers','Commentaries','Deleted Scenes','Behind the Scenes')` |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| idx_title | `title` | INDEX |   |
| idx_fk_language_id | `language_id` | INDEX |   |
| idx_fk_original_language_id | `original_language_id` | INDEX |   |
| PRIMARY | `film_id` | PRIMARY |   |


## **<a id='film-actor'></a>film_actor**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='film-actor-actor-id'></a>`actor_id` | SMALLINT UNSIGNED | PRIMARY, Not null |   |   |
| <a id='film-actor-actor-id'></a>`film_id` | SMALLINT UNSIGNED | PRIMARY, Not null |   |  REFERENCES  [**film**](#film) ([**film_id**](#film-film-id))  ON UPDATE CASCADE |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `actor_id`, `film_id` | PRIMARY |   |
| idx_fk_film_id | `film_id` | INDEX |   |


## **<a id='film-category'></a>film_category**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='film-category-film-id'></a>`film_id` | SMALLINT UNSIGNED | PRIMARY, Not null |   |  REFERENCES  [**film**](#film) ([**film_id**](#film-film-id))  ON UPDATE CASCADE |
| <a id='film-category-film-id'></a>`category_id` | TINYINT UNSIGNED | PRIMARY, Not null |   |   |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `film_id`, `category_id` | PRIMARY |   |
| fk_film_category_film_idx | `film_id` | INDEX |   |


## **<a id='film-text'></a>film_text**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='film-text-film-id'></a>`film_id` | SMALLINT UNSIGNED | PRIMARY, Not null |   |  REFERENCES  [**inventory**](#inventory) ([**film_id**](#inventory-film-id))  ON UPDATE NO ACTION  ON DELETE NO ACTION |
| `title` | VARCHAR(255) | Not null |   |   |
| `description` | TEXT |  |   |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `film_id` | PRIMARY |   |
| idx_title_description | `title`, `description` | FULLTEXT |   |
| fk_film_text_idx | `film_id` | INDEX |   |


## **<a id='inventory'></a>inventory**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='inventory-inventory-id'></a>`inventory_id` | MEDIUMINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `film_id` | SMALLINT UNSIGNED | Not null |   |  REFERENCES  [**film**](#film) ([**film_id**](#film-film-id))  ON UPDATE CASCADE |
| `store_id` | TINYINT UNSIGNED | Not null |   |  REFERENCES  [**store**](#store) ([**store_id**](#store-store-id))  ON UPDATE CASCADE |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `inventory_id` | PRIMARY |   |
| idx_fk_film_id | `film_id` | INDEX |   |
| idx_store_id_film_id | `store_id`, `film_id` | INDEX |   |
| fk_inventory_store_idx | `store_id` | INDEX |   |


## **<a id='language'></a>language**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='language-language-id'></a>`language_id` | TINYINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `name` | CHAR(20) | Not null |   |   |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `language_id` | PRIMARY |   |


## **<a id='payment'></a>payment**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='payment-payment-id'></a>`payment_id` | SMALLINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `customer_id` | SMALLINT UNSIGNED | Not null |   |  REFERENCES  [**customer**](#customer) ([**customer_id**](#customer-customer-id))  ON UPDATE CASCADE |
| `staff_id` | TINYINT UNSIGNED | Not null |   |  REFERENCES  [**staff**](#staff) ([**staff_id**](#staff-staff-id))  ON UPDATE CASCADE |
| `rental_id` | INT |  | `NULL` |   |
| `amount` | DECIMAL | Not null |   |   |
| `payment_date` | DATETIME | Not null |   |   |
| `last_update` | TIMESTAMP |  | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `payment_id` | PRIMARY |   |
| idx_fk_staff_id | `staff_id` | INDEX |   |
| idx_fk_customer_id | `customer_id` | INDEX |   |


## **<a id='staff'></a>staff**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='staff-staff-id'></a>`staff_id` | TINYINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `first_name` | VARCHAR(45) | Not null |   |   |
| `last_name` | VARCHAR(45) | Not null |   |   |
| `address_id` | SMALLINT UNSIGNED | Not null |   |  REFERENCES  [**address**](#address) ([**address_id**](#address-address-id))  ON UPDATE CASCADE |
| `picture` | BLOB |  |   |   |
| `email` | VARCHAR(50) |  | `NULL` |   |
| `store_id` | TINYINT UNSIGNED | Not null |   |  REFERENCES  [**store**](#store) ([**store_id**](#store-store-id))  ON UPDATE CASCADE |
| `active` |  | Not null | `TRUE` |   |
| `username` | VARCHAR(16) | Not null |   |   |
| `password` | VARCHAR(40) |  | `NULL` |   |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `staff_id` | PRIMARY |   |
| idx_fk_store_id | `store_id` | INDEX |   |
| idx_fk_address_id | `address_id` | INDEX |   |


## **<a id='store'></a>store**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='store-store-id'></a>`store_id` | TINYINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `manager_staff_id` | TINYINT UNSIGNED | Not null, Unique |   |  REFERENCES  [**staff**](#staff) ([**staff_id**](#staff-staff-id))  ON UPDATE CASCADE |
| `address_id` | SMALLINT UNSIGNED | Not null |   |  REFERENCES  [**address**](#address) ([**address_id**](#address-address-id))  ON UPDATE CASCADE |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `store_id` | PRIMARY |   |
| idx_unique_manager | `manager_staff_id` | UNIQUE |   |
| idx_fk_address_id | `address_id` | INDEX |   |


# *Views*

## **<a id='actor-info'></a>actor_info**

---

### *Description:*

This is a view for actor table.

### *Sql:*

```sql
--
-- View structure for view `actor_info`
--

CREATE DEFINER=CURRENT_USER SQL SECURITY INVOKER VIEW actor_info 
AS
SELECT 
a.actor_id,
a.first_name,
a.last_name,
GROUP_CONCAT(DISTINCT CONCAT(c.name, ': ',
		(SELECT GROUP_CONCAT(f.title ORDER BY f.title SEPARATOR ', ')
                    FROM sakila.film f
                    INNER JOIN sakila.film_category fc
                      ON f.film_id = fc.film_id
                    INNER JOIN sakila.film_actor fa
                      ON f.film_id = fa.film_id
                    WHERE fc.category_id = c.category_id
                    AND fa.actor_id = a.actor_id
                 )
             )
             ORDER BY c.name SEPARATOR '; ')
AS film_info
FROM sakila.actor a
LEFT JOIN sakila.film_actor fa
  ON a.actor_id = fa.actor_id
LEFT JOIN sakila.film_category fc
  ON fa.film_id = fc.film_id
LEFT JOIN sakila.category c
  ON fc.category_id = c.category_id
GROUP BY a.actor_id, a.first_name, a.last_name
```
## **<a id='customer-list'></a>customer_list**

---

### *Description:*



### *Sql:*

```sql
--
-- View structure for view `customer_list`
--

CREATE VIEW customer_list 
AS 
SELECT cu.customer_id AS ID, CONCAT(cu.first_name, _utf8' ', cu.last_name) AS name, a.address AS address, a.postal_code AS `zip code`,
	a.phone AS phone, city.city AS city, country.country AS country, IF(cu.active, _utf8'active',_utf8'') AS notes, cu.store_id AS SID 
FROM customer AS cu JOIN address AS a ON cu.address_id = a.address_id JOIN city ON a.city_id = city.city_id 
	JOIN country ON city.country_id = country.country_id
```
## **<a id='film-list'></a>film_list**

---

### *Description:*



### *Sql:*

```sql
--
-- View structure for view `film_list`
--

CREATE VIEW film_list 
AS 
SELECT film.film_id AS FID, film.title AS title, film.description AS description, category.name AS category, film.rental_rate AS price,
	film.length AS length, film.rating AS rating, GROUP_CONCAT(CONCAT(actor.first_name, _utf8' ', actor.last_name) SEPARATOR ', ') AS actors 
FROM category LEFT JOIN film_category ON category.category_id = film_category.category_id LEFT JOIN film ON film_category.film_id = film.film_id
        JOIN film_actor ON film.film_id = film_actor.film_id 
	JOIN actor ON film_actor.actor_id = actor.actor_id 
GROUP BY film.film_id, category.name
```
## **<a id='sales-by-store'></a>sales_by_store**

---

### *Description:*



### *Sql:*

```sql
--
-- View structure for view `sales_by_store`
--

CREATE VIEW sales_by_store
AS 
SELECT 
CONCAT(c.city, _utf8',', cy.country) AS store
, CONCAT(m.first_name, _utf8' ', m.last_name) AS manager
, SUM(p.amount) AS total_sales
FROM payment AS p
INNER JOIN rental AS r ON p.rental_id = r.rental_id
INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
INNER JOIN store AS s ON i.store_id = s.store_id
INNER JOIN address AS a ON s.address_id = a.address_id
INNER JOIN city AS c ON a.city_id = c.city_id
INNER JOIN country AS cy ON c.country_id = cy.country_id
INNER JOIN staff AS m ON s.manager_staff_id = m.staff_id
GROUP BY s.store_id
ORDER BY cy.country, c.city
```
## **<a id='sales-by-film-category'></a>sales_by_film_category**

---

### *Description:*



### *Sql:*

```sql
--
-- View structure for view `sales_by_film_category`
--
-- Note that total sales will add up to >100% because
-- some titles belong to more than 1 category
--

CREATE VIEW sales_by_film_category
AS 
SELECT 
c.name AS category
, SUM(p.amount) AS total_sales
FROM payment AS p
INNER JOIN rental AS r ON p.rental_id = r.rental_id
INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
INNER JOIN film AS f ON i.film_id = f.film_id
INNER JOIN film_category AS fc ON f.film_id = fc.film_id
INNER JOIN category AS c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY total_sales DESC
```
## **<a id='staff-list'></a>staff_list**

---

### *Description:*



### *Sql:*

```sql
--
-- View structure for view `staff_list`
--

CREATE VIEW staff_list 
AS 
SELECT s.staff_id AS ID, CONCAT(s.first_name, _utf8' ', s.last_name) AS name, a.address AS address, a.postal_code AS `zip code`, a.phone AS phone,
	city.city AS city, country.country AS country, s.store_id AS SID 
FROM staff AS s JOIN address AS a ON s.address_id = a.address_id JOIN city ON a.city_id = city.city_id 
	JOIN country ON city.country_id = country.country_id
```
## **<a id='nicer-but-slower-film-list'></a>nicer_but_slower_film_list**

---

### *Description:*



### *Sql:*

```sql
--
-- View structure for view `nicer_but_slower_film_list`
--

CREATE VIEW nicer_but_slower_film_list 
AS 
SELECT film.film_id AS FID, film.title AS title, film.description AS description, category.name AS category, film.rental_rate AS price, 
	film.length AS length, film.rating AS rating, GROUP_CONCAT(CONCAT(CONCAT(UCASE(SUBSTR(actor.first_name,1,1)),
	LCASE(SUBSTR(actor.first_name,2,LENGTH(actor.first_name))),_utf8' ',CONCAT(UCASE(SUBSTR(actor.last_name,1,1)),
	LCASE(SUBSTR(actor.last_name,2,LENGTH(actor.last_name)))))) SEPARATOR ', ') AS actors 
FROM category LEFT JOIN film_category ON category.category_id = film_category.category_id LEFT JOIN film ON film_category.film_id = film.film_id
        JOIN film_actor ON film.film_id = film_actor.film_id
	JOIN actor ON film_actor.actor_id = actor.actor_id 
GROUP BY film.film_id, category.name
```
