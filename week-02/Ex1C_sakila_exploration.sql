/*
a) Information about actors.
b) Informations about films and their rental logs.
c) film_actor
d) Table includes rental processing informations. It is hard to read because we can able to so just id numbers. This looks awful for basic interfaces.
e) Same issues happens in here too. We can able to see only numbers. 
f) We have to use film table together with inventory and rental tables. This helps to readbilty a lot.
*/

USE sakila;
SELECT rental_date, inventory_id FROM rental ;
SELECT inventory_id, film_id FROM inventory ;
SELECT film_id, title FROM film ; 
