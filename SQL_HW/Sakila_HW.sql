select first_name, last_name from actor;

select concat(first_name,' ', last_name) Actor_Name from actor;

select actor_id, first_name, last_name from actor
where first_name = "Joe";

select first_name, last_name from actor
where last_name like '%gen%';

select last_name, first_name from actor
where last_name like '%li%';

SELECT country_id, country FROM country 
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');


#4a

#4b

UPDATE actor SET first_name = 'HARPO' WHERE last_name = 'WILLIAMS';

UPDATE actor SET first_name = 'GROUCHO' WHERE last_name = 'WILLIAMS';


SHOW create table address;	

select first_name, last_name, address from staff 
inner join address on 
staff.address_id=address.address_id;

select * from payment;
select * from staff;

select first_name, last_name, sum(amount) from staff
inner join payment where staff.staff_id=payment.staff_id
group by first_name;





