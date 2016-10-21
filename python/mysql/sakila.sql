SELECT customer.first_name, customer.last_name, customer.email, customer.address 
FROM customer 
JOIN address 
ON customer.address_id = address.address_id
WHERE city_id = 312;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name 
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON category.category_id = film_category.category_id
WHERE category.category_id = 5;

SELECT film.title, film.description, film.release_year
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 5;

SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address 
ON customer.address_id = address.address_id
JOIN city 
ON address.city_id = city.city_id
WHERE customer.store_id = 1 AND (address.city_id = 1 OR address.city_id = 42 OR address.city_id = 312 OR address.city_id = 459);
        
SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE actor.actor_id = 15 AND film.rating = 'G' AND film.special_features LIKE '%Behind the Scenes%';

SELECT film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
FROM film
JOIN film_actor
ON film_actor.film_id = film.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category
ON film_category.film_id = film.film_id
JOIN category
ON category.category_id = film_category.category_id
WHERE film.rental_rate = 2.99;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, CONCAT(actor.first_name, " ", actor.last_name) AS actor_name
FROM film
JOIN film_category
ON film.film_id = film_category.film_id
JOIN category
ON film_category.category_id = category.category_id
JOIN film_actor
ON film.film_id = film_actor.film_id
JOIN actor
ON actor.actor_id = film_actor.actor_id
WHERE category.name LIKE 'Action' AND actor.first_name = 'Sandra' AND actor.last_name = 'Kilmer';