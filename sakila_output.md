# sakila



Automatically generate documents. The latest form of document changes by *2010-09-14 11:00:00*

![Database Structure](./sakila.db.png)

## **<a id='actor'></a>actor**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='actor-actor-id'></a>`actor_id` | SMALLINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `first_name` | VARCHAR(45) CHARACTER SET latin1 COLLATE latin1_general_ci | Not null |   |   |
| `last_name` | VARCHAR(45) | Not null |   |   |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `actor_id` | PRIMARY |   |
| idx_actor_last_name | `last_name` | INDEX |   |


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
| `city_id` | SMALLINT UNSIGNED | Not null |   |  foreign key to column [**city_id**](#city-city-id) on table [**city**](#city) |
| `postal_code` | VARCHAR(10) |  | `NULL` |   |
| `phone` | VARCHAR(20) | Not null |   |   |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `address_id` | PRIMARY |   |
| idx_fk_city_id | `city_id` | INDEX |   |


## **<a id='category'></a>category**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='category-category-id'></a>`category_id` | TINYINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `name` | VARCHAR(25) | Not null |   |   |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `category_id` | PRIMARY |   |


## **<a id='city'></a>city**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='city-city-id'></a>`city_id` | INT | PRIMARY, Not null |   |   |
| `city` | FLOAT | Not null |   |   |
| `country_id` | SMALLINT UNSIGNED | Not null |   |  foreign key to column [**country_id**](#country-country-id) on table [**country**](#country)  ON UPDATE:CASCADE |
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
| `store_id` | TINYINT UNSIGNED | Not null |   |  foreign key to column [**store_id**](#store-store-id) on table [**store**](#store)  ON UPDATE:CASCADE |
| `first_name` | VARCHAR(45) | Not null |   |   |
| `last_name` | VARCHAR(45) | Not null |   |   |
| `email` | VARCHAR(50) |  | `NULL` |   |
| `address_id` | SMALLINT UNSIGNED | Not null |   |  foreign key to column [**address_id**](#address-address-id) on table [**address**](#address)  ON UPDATE:CASCADE |
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
| `language_id` | TINYINT UNSIGNED | Not null |   |  foreign key to column [**language_id**](#language-language-id) on table [**language**](#language)  ON UPDATE:CASCADE |
| `original_language_id` | TINYINT UNSIGNED |  | `NULL` |  foreign key to column [**language_id**](#language-language-id) on table [**language**](#language)  ON UPDATE:CASCADE |
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
| <a id='film-actor-actor-id'></a>`actor_id` | SMALLINT UNSIGNED | PRIMARY, Not null |   |  foreign key to column [**actor_id**](#actor-actor-id) on table [**actor**](#actor)  ON UPDATE:CASCADE |
| <a id='film-actor-actor-id'></a>`film_id` | SMALLINT UNSIGNED | PRIMARY, Not null |   |  foreign key to column [**film_id**](#film-film-id) on table [**film**](#film)  ON UPDATE:CASCADE |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `actor_id`, `film_id` | PRIMARY |   |
| idx_fk_film_id | `film_id` | INDEX |   |
| fk_film_actor_actor_idx | `actor_id` | INDEX |   |


## **<a id='film-category'></a>film_category**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='film-category-film-id'></a>`film_id` | SMALLINT UNSIGNED | PRIMARY, Not null |   |  foreign key to column [**film_id**](#film-film-id) on table [**film**](#film)  ON UPDATE:CASCADE |
| <a id='film-category-film-id'></a>`category_id` | TINYINT UNSIGNED | PRIMARY, Not null |   |  foreign key to column [**category_id**](#category-category-id) on table [**category**](#category)  ON UPDATE:CASCADE |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `film_id`, `category_id` | PRIMARY |   |
| fk_film_category_category_idx | `category_id` | INDEX |   |
| fk_film_category_film_idx | `film_id` | INDEX |   |


## **<a id='film-text'></a>film_text**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='film-text-film-id'></a>`film_id` | SMALLINT UNSIGNED | PRIMARY, Not null |   |  foreign key to column [**film_id**](#inventory-film-id) on table [**inventory**](#inventory)  ON UPDATE:NO ACTION  ON DELETE: NO ACTION |
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
| `film_id` | SMALLINT UNSIGNED | Not null |   |  foreign key to column [**film_id**](#film-film-id) on table [**film**](#film)  ON UPDATE:CASCADE |
| `store_id` | TINYINT UNSIGNED | Not null |   |  foreign key to column [**store_id**](#store-store-id) on table [**store**](#store)  ON UPDATE:CASCADE |
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
| `customer_id` | SMALLINT UNSIGNED | Not null |   |  foreign key to column [**customer_id**](#customer-customer-id) on table [**customer**](#customer)  ON UPDATE:CASCADE |
| `staff_id` | TINYINT UNSIGNED | Not null |   |  foreign key to column [**staff_id**](#staff-staff-id) on table [**staff**](#staff)  ON UPDATE:CASCADE |
| `rental_id` | INT |  | `NULL` |  foreign key to column [**rental_id**](#rental-rental-id) on table [**rental**](#rental)  ON UPDATE:CASCADE  ON DELETE: SET NULL |
| `amount` | DECIMAL | Not null |   |   |
| `payment_date` | DATETIME | Not null |   |   |
| `last_update` | TIMESTAMP |  | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `payment_id` | PRIMARY |   |
| idx_fk_staff_id | `staff_id` | INDEX |   |
| idx_fk_customer_id | `customer_id` | INDEX |   |
| fk_payment_rental_idx | `rental_id` | INDEX |   |


## **<a id='rental'></a>rental**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='rental-rental-id'></a>`rental_id` | INT | PRIMARY, Auto increments, Not null |   |   |
| `rental_date` | DATETIME | Not null, Unique |   |   |
| `inventory_id` | MEDIUMINT UNSIGNED | Not null, Unique |   |  foreign key to column [**inventory_id**](#inventory-inventory-id) on table [**inventory**](#inventory)  ON UPDATE:CASCADE |
| `customer_id` | SMALLINT UNSIGNED | Not null, Unique |   |  foreign key to column [**customer_id**](#customer-customer-id) on table [**customer**](#customer)  ON UPDATE:CASCADE |
| `return_date` | DATETIME |  |   |   |
| `staff_id` | TINYINT UNSIGNED | Not null |   |  foreign key to column [**staff_id**](#staff-staff-id) on table [**staff**](#staff)  ON UPDATE:CASCADE |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `rental_id` | PRIMARY |   |
| idx_rental | `rental_date`, `inventory_id`, `customer_id` | UNIQUE |   |
| idx_fk_inventory_id | `inventory_id` | INDEX |   |
| idx_fk_customer_id | `customer_id` | INDEX |   |
| idx_fk_staff_id | `staff_id` | INDEX |   |


## **<a id='staff'></a>staff**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| <a id='staff-staff-id'></a>`staff_id` | TINYINT UNSIGNED | PRIMARY, Auto increments, Not null |   |   |
| `first_name` | VARCHAR(45) | Not null |   |   |
| `last_name` | VARCHAR(45) | Not null |   |   |
| `address_id` | SMALLINT UNSIGNED | Not null |   |  foreign key to column [**address_id**](#address-address-id) on table [**address**](#address)  ON UPDATE:CASCADE |
| `picture` | BLOB |  |   |   |
| `email` | VARCHAR(50) |  | `NULL` |   |
| `store_id` | TINYINT UNSIGNED | Not null |   |  foreign key to column [**store_id**](#store-store-id) on table [**store**](#store)  ON UPDATE:CASCADE |
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
| `manager_staff_id` | TINYINT UNSIGNED | Not null, Unique |   |  foreign key to column [**staff_id**](#staff-staff-id) on table [**staff**](#staff)  ON UPDATE:CASCADE |
| `address_id` | SMALLINT UNSIGNED | Not null |   |  foreign key to column [**address_id**](#address-address-id) on table [**address**](#address)  ON UPDATE:CASCADE |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `store_id` | PRIMARY |   |
| idx_unique_manager | `manager_staff_id` | UNIQUE |   |
| idx_fk_address_id | `address_id` | INDEX |   |


