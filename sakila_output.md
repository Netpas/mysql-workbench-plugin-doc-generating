# sakila



Automatically generate documents. The latest form of document changes by 2010-09-14 11:00:00

## **<a id='actor'></a>actor**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| `actor_id` | SMALLINT | <a id='actor-actor-id'></a>PRIMARY, Auto increments, Not null |   |   |
| `first_name` | VARCHAR(45) | Not null |   |   |
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
| `address_id` | SMALLINT | <a id='address-address-id'></a>PRIMARY, Auto increments, Not null |   |   |
| `address` | VARCHAR(50) | Not null |   |   |
| `address2` | VARCHAR(50) |  | `NULL` |   |
| `district` | VARCHAR(20) | Not null |   |   |
| `city_id` | SMALLINT | Not null |   |  [**foreign key** ](#city-city-id)  `to column city_id` on table `city`. |
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
| `category_id` | TINYINT | <a id='category-category-id'></a>PRIMARY, Auto increments, Not null |   |   |
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
| `city_id` | SMALLINT | <a id='city-city-id'></a>PRIMARY, Auto increments, Not null |   |   |
| `city` | VARCHAR(50) | Not null |   |   |
| `country_id` | SMALLINT | Not null |   |  [**foreign key** ](#country-country-id)  `to column country_id` on table `country`. |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `city_id` | PRIMARY |   |
| idx_fk_country_id | `country_id` | INDEX |   |


## **<a id='country'></a>country**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| `country_id` | SMALLINT | <a id='country-country-id'></a>PRIMARY, Auto increments, Not null |   |   |
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
| `customer_id` | SMALLINT | <a id='customer-customer-id'></a>PRIMARY, Auto increments, Not null |   |   |
| `store_id` | TINYINT | Not null |   |  [**foreign key** ](#store-store-id)  `to column store_id` on table `store`. |
| `first_name` | VARCHAR(45) | Not null |   |   |
| `last_name` | VARCHAR(45) | Not null |   |   |
| `email` | VARCHAR(50) |  | `NULL` |   |
| `address_id` | SMALLINT | Not null |   |  [**foreign key** ](#address-address-id)  `to column address_id` on table `address`. |
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
| `film_id` | SMALLINT | <a id='film-film-id'></a>PRIMARY, Auto increments, Not null |   |   |
| `title` | VARCHAR(255) | Not null |   |   |
| `description` | TEXT |  |   |   |
| `release_year` | YEAR |  |   |   |
| `language_id` | TINYINT | Not null |   |  [**foreign key** ](#language-language-id)  `to column language_id` on table `language`. |
| `original_language_id` | TINYINT |  | `NULL` |  [**foreign key** ](#language-language-id)  `to column language_id` on table `language`. |
| `rental_duration` | TINYINT | Not null | `3` |   |
| `rental_rate` | DECIMAL | Not null | `4.99` |   |
| `length` | SMALLINT |  | `NULL` |   |
| `replacement_cost` | DECIMAL | Not null | `19.99` |   |
| `rating` | ENUM |  | `'G'` |   |
| `special_features` | SET |  |   |   |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| idx_title | `title` | INDEX |   |
| idx_fk_language_id | `language_id` | INDEX |   |
| idx_fk_original_language_id | `original_language_id` | INDEX |   |
| PRIMARY | `film_id` | PRIMARY |   |


## **<a id='film_actor'></a>film_actor**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| `actor_id` | SMALLINT | <a id='film-actor-actor-id'></a>PRIMARY, Not null |   |  [**foreign key** ](#actor-actor-id)  `to column actor_id` on table `actor`. |
| `film_id` | SMALLINT | <a id='film-actor-actor-id'></a>PRIMARY, Not null |   |  [**foreign key** ](#film-film-id)  `to column film_id` on table `film`. |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `actor_id`, `film_id` | PRIMARY |   |
| idx_fk_film_id | `film_id` | INDEX |   |
| fk_film_actor_actor_idx | `actor_id` | INDEX |   |


## **<a id='film_category'></a>film_category**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| `film_id` | SMALLINT | <a id='film-category-film-id'></a>PRIMARY, Not null |   |  [**foreign key** ](#film-film-id)  `to column film_id` on table `film`. |
| `category_id` | TINYINT | <a id='film-category-film-id'></a>PRIMARY, Not null |   |  [**foreign key** ](#category-category-id)  `to column category_id` on table `category`. |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `film_id`, `category_id` | PRIMARY |   |
| fk_film_category_category_idx | `category_id` | INDEX |   |
| fk_film_category_film_idx | `film_id` | INDEX |   |


## **<a id='film_text'></a>film_text**

---

### *Description:*



### *Columns:*

| Column | Data type | Attributes | Default | Description |
| --- | --- | --- | --- | ---  |
| `film_id` | SMALLINT | <a id='film-text-film-id'></a>PRIMARY, Not null |   |  [**foreign key** ](#inventory-film-id)  `to column film_id` on table `inventory`. |
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
| `inventory_id` | MEDIUMINT | <a id='inventory-inventory-id'></a>PRIMARY, Auto increments, Not null |   |   |
| `film_id` | SMALLINT | Not null |   |  [**foreign key** ](#film-film-id)  `to column film_id` on table `film`. |
| `store_id` | TINYINT | Not null |   |  [**foreign key** ](#store-store-id)  `to column store_id` on table `store`. |
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
| `language_id` | TINYINT | <a id='language-language-id'></a>PRIMARY, Auto increments, Not null |   |   |
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
| `payment_id` | SMALLINT | <a id='payment-payment-id'></a>PRIMARY, Auto increments, Not null |   |   |
| `customer_id` | SMALLINT | Not null |   |  [**foreign key** ](#customer-customer-id)  `to column customer_id` on table `customer`. |
| `staff_id` | TINYINT | Not null |   |  [**foreign key** ](#staff-staff-id)  `to column staff_id` on table `staff`. |
| `rental_id` | INT |  | `NULL` |  [**foreign key** ](#rental-rental-id)  `to column rental_id` on table `rental`. |
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
| `rental_id` | INT | <a id='rental-rental-id'></a>PRIMARY, Auto increments, Not null |   |   |
| `rental_date` | DATETIME | Not null, Unique |   |   |
| `inventory_id` | MEDIUMINT | Not null, Unique |   |  [**foreign key** ](#inventory-inventory-id)  `to column inventory_id` on table `inventory`. |
| `customer_id` | SMALLINT | Not null, Unique |   |  [**foreign key** ](#customer-customer-id)  `to column customer_id` on table `customer`. |
| `return_date` | DATETIME |  |   |   |
| `staff_id` | TINYINT | Not null |   |  [**foreign key** ](#staff-staff-id)  `to column staff_id` on table `staff`. |
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
| `staff_id` | TINYINT | <a id='staff-staff-id'></a>PRIMARY, Auto increments, Not null |   |   |
| `first_name` | VARCHAR(45) | Not null |   |   |
| `last_name` | VARCHAR(45) | Not null |   |   |
| `address_id` | SMALLINT | Not null |   |  [**foreign key** ](#address-address-id)  `to column address_id` on table `address`. |
| `picture` | BLOB |  |   |   |
| `email` | VARCHAR(50) |  | `NULL` |   |
| `store_id` | TINYINT | Not null |   |  [**foreign key** ](#store-store-id)  `to column store_id` on table `store`. |
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
| `store_id` | TINYINT | <a id='store-store-id'></a>PRIMARY, Auto increments, Not null |   |   |
| `manager_staff_id` | TINYINT | Not null, Unique |   |  [**foreign key** ](#staff-staff-id)  `to column staff_id` on table `staff`. |
| `address_id` | SMALLINT | Not null |   |  [**foreign key** ](#address-address-id)  `to column address_id` on table `address`. |
| `last_update` | TIMESTAMP | Not null | `CURRENT_TIMESTAMP` |   |


### *Indices:*

| Name | Columns | Type | Description |
| --- | --- | --- | --- |
| PRIMARY | `store_id` | PRIMARY |   |
| idx_unique_manager | `manager_staff_id` | UNIQUE |   |
| idx_fk_address_id | `address_id` | INDEX |   |


