-- What query would you run to get the total revenue for March of 2012?
SELECT SUM(billing.amount) AS total_revenue_march
FROM billing
WHERE billing.charged_datetime 
BETWEEN '2012-03-01 00:00:00.000' 
AND '2012-03-31 23:59:59.999';
-- What query would you run to get total revenue collected from the client with an id of 2?
SELECT SUM(billing.amount) AS total_revenue_collected
FROM billing
WHERE billing.client_id = 2;
-- What query would you run to get all the sites that client=10 owns?
SELECT sites.domain_name
FROM sites
WHERE client_id = 10;
-- What query would you run to get total 
-- # of sites created each month for the client with an id of 1? What about for client=20?
SELECT MONTH(sites.created_datetime) AS month, COUNT(sites.domain_name) AS number_of_sites, sites.client_id 
FROM sites
WHERE sites.client_id = 1 OR sites.client_id = 20
GROUP BY MONTH(sites.created_datetime);
-- What query would you run to get the total 
-- # of leads we've generated for each of our sites between January 1, 2011 to February 15, 2011?
SELECT sites.domain_name, COUNT(leads.site_id) AS number_of_leads, leads.registered_datetime
FROM leads
JOIN sites
ON leads.site_id = sites.site_id
WHERE leads.registered_datetime
BETWEEN '2011-01-01 00:00:00.000'
AND '2011-02-15 23:59:59.999'
GROUP BY leads.site_id;
-- What query would you run to get a list of client names and the total 
-- # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT clients.first_name, clients.last_name, COUNT(leads.registered_datetime) AS number_of_leads
FROM clients
JOIN sites
ON sites.client_id = clients.client_id
JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime
BETWEEN '2011-01-01 00:00:00.000'
AND '2011-12-31 23:59:59.999'
GROUP BY clients.client_id;
-- What query would you run to get a list of client name and the total 
-- # of leads we've generated for each client each month between month 1 - 6 of Year 2011?
SELECT clients.first_name, clients.last_name, MONTH(leads.registered_datetime) AS month
FROM clients
JOIN sites
ON sites.client_id = clients.client_id
JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime
BETWEEN '2011-01-01 00:00:00.000'
AND '2011-06-30 23:59:59.999'
GROUP BY leads.registered_datetime;
-- What query would you run to get a list of client name and the total 
-- # of leads we've generated for each of our client's sites between January 1, 2011 to December 31, 2011?
SELECT clients.first_name, clients.last_name, sites.domain_name, COUNT(sites.site_id) AS number_of_leads, MONTH(leads.registered_datetime) AS month
FROM clients
JOIN sites
ON sites.client_id = clients.client_id
JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime
BETWEEN '2011-01-01 00:00:00.000'
AND '2011-12-31 23:59:59.999'
GROUP BY sites.domain_name, clients.client_id
ORDER BY clients.client_id;
-- # Come up with a second query that shows all the clients, the site name(s), and the 
-- # total number of leads generated from each site for all time.
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS clients_name, sites.domain_name, COUNT(leads.site_id) AS number_of_leads
FROM clients
JOIN sites
ON sites.client_id = clients.client_id
JOIN leads
ON sites.site_id = leads.site_id
GROUP BY sites.domain_name
ORDER BY clients.client_id;
-- Write a single query that retrieves total revenue collected from each client each month of the year.
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS clients_name, 
	SUM(billing.amount) AS amount_billed, MONTH(billing.charged_datetime) AS month_billed, 
    YEAR(billing.charged_datetime) AS year_billed
FROM billing
JOIN clients
ON clients.client_id = billing.client_id
GROUP BY clients.client_id, month_billed, year_billed
ORDER BY clients.client_id, year_billed, month_billed;
-- Write a single query that retrieves all the sites that each client owns. 
-- Group the results so that each row shows a new client. Add a new field called 'sites' 
-- that has all the sites that the client owns. (HINT: use GROUP_CONCAT);
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS clients_name, GROUP_CONCAT(' ', sites.domain_name)
FROM clients
JOIN sites
ON clients.client_id = sites.client_id
GROUP BY clients_name
ORDER BY clients.client_id;