# sakila



Automatically generate documents. The latest form of document changes by *2018-05-17 16:34:00*

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
| `address` | VARCHAR(50) CHARACTER SET latin1 COLLATE latin1_bin | Not null |   |   |
| `address2` | VARCHAR(50) CHARACTER SET koi8r COLLATE koi8r_bin |  | `NULL` |   |
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


