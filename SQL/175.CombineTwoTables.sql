SELECT firstName, lastName, city, state 
FROM Person LEFT JOIN Address
ON Person.personId = Address.personId;
/*Because firstName, lastName, city and state are specific in all the variables in the two tables,
we don't have to specify the table name before the variable name.
*/
