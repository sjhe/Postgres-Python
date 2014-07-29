--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: campaign; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE campaign (
    name character(30) NOT NULL,
    starttime character(10),
    endtime character(10)
);


ALTER TABLE public.campaign OWNER TO c370_s19;

--
-- Name: cost; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE cost (
    subject character(30) NOT NULL,
    amount integer,
    campaign character(30) NOT NULL
);


ALTER TABLE public.cost OWNER TO c370_s19;

--
-- Name: employee; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE employee (
    sin integer NOT NULL,
    name character(30),
    gender character(6),
    age integer,
    salary integer,
    "position" character(30)
);


ALTER TABLE public.employee OWNER TO c370_s19;

--
-- Name: event; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE event (
    campaign character(30) NOT NULL,
    name character(30) NOT NULL,
    note character(100)
);


ALTER TABLE public.event OWNER TO c370_s19;

--
-- Name: funds; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE funds (
    supporter integer,
    campaign character(30)
);


ALTER TABLE public.funds OWNER TO c370_s19;

--
-- Name: hostin; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE hostin (
    location character(30),
    campaign character(30)
);


ALTER TABLE public.hostin OWNER TO c370_s19;

--
-- Name: location; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE location (
    address character(30) NOT NULL
);


ALTER TABLE public.location OWNER TO c370_s19;

--
-- Name: member; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE member (
    sin integer NOT NULL,
    name character(30),
    gender character(6),
    age integer,
    memberid integer,
    donation integer DEFAULT 1000 NOT NULL,
    duration character(20) DEFAULT '8 months'::bpchar NOT NULL,
    annotation character(50)
);


ALTER TABLE public.member OWNER TO c370_s19;

--
-- Name: organize; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE organize (
    volunteer integer,
    campaign character(30)
);


ALTER TABLE public.organize OWNER TO c370_s19;

--
-- Name: supporter; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE supporter (
    sin integer NOT NULL,
    name character(30),
    gender character(6),
    age integer,
    donation integer
);


ALTER TABLE public.supporter OWNER TO c370_s19;

--
-- Name: supports; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE supports (
    member integer,
    campaign character(30),
    date character(30) DEFAULT '2011/01/01'::bpchar NOT NULL
);


ALTER TABLE public.supports OWNER TO c370_s19;

--
-- Name: works; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE works (
    employee integer,
    campaign character(30)
);


ALTER TABLE public.works OWNER TO c370_s19;

--
-- Name: view1; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view1 AS
 SELECT employee.name
   FROM employee,
    works
  WHERE ((works.campaign = 'Let it be'::bpchar) AND (works.employee = employee.sin));


ALTER TABLE public.view1 OWNER TO c370_s19;

--
-- Name: view11; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view11 AS
 SELECT cost.campaign,
    sum(cost.amount) AS sum
   FROM cost
  GROUP BY cost.campaign;


ALTER TABLE public.view11 OWNER TO c370_s19;

--
-- Name: view12; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view12 AS
 SELECT hostin.location,
    hostin.campaign
   FROM hostin
  WHERE (hostin.campaign = 'Let it be'::bpchar);


ALTER TABLE public.view12 OWNER TO c370_s19;

--
-- Name: view10; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view10 AS
 SELECT view11.campaign,
    view11.sum,
    view12.location
   FROM (view11
   JOIN view12 ON ((view11.campaign = view12.campaign)));


ALTER TABLE public.view10 OWNER TO c370_s19;

--
-- Name: volunteer; Type: TABLE; Schema: public; Owner: c370_s19; Tablespace: 
--

CREATE TABLE volunteer (
    sin integer NOT NULL,
    name character(30),
    gender character(6),
    age integer,
    numberofparticipation integer,
    tier integer NOT NULL
);


ALTER TABLE public.volunteer OWNER TO c370_s19;

--
-- Name: view2; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view2 AS
 SELECT volunteer.name
   FROM volunteer
  WHERE (volunteer.tier = 2);


ALTER TABLE public.view2 OWNER TO c370_s19;

--
-- Name: view3; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view3 AS
 SELECT volunteer.name
   FROM volunteer,
    ( SELECT organize.volunteer
           FROM organize
          WHERE (organize.campaign = 'In My Life'::bpchar)) ov
  WHERE ((volunteer.sin = ov.volunteer) AND (volunteer.tier = 2));


ALTER TABLE public.view3 OWNER TO c370_s19;

--
-- Name: view4; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view4 AS
 SELECT s1.name
   FROM supporter s1
  WHERE (NOT (EXISTS ( SELECT supporter.sin,
            supporter.name,
            supporter.gender,
            supporter.age,
            supporter.donation
           FROM supporter
          WHERE ((supporter.name <> s1.name) AND (supporter.donation > s1.donation)))));


ALTER TABLE public.view4 OWNER TO c370_s19;

--
-- Name: view5; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view5 AS
 SELECT member.name
   FROM member,
    ( SELECT supports.member
           FROM supports
          WHERE (supports.campaign = 'Let it be'::bpchar)) sm
  WHERE ((member.memberid = sm.member) AND (member.age < 25));


ALTER TABLE public.view5 OWNER TO c370_s19;

--
-- Name: view6; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view6 AS
 SELECT employee."position"
   FROM employee
  WHERE (employee.salary = ( SELECT min(employee_1.salary) AS min
           FROM employee employee_1));


ALTER TABLE public.view6 OWNER TO c370_s19;

--
-- Name: view7; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view7 AS
 SELECT supporter.donation
   FROM supporter
  WHERE (supporter.donation >= ALL ( SELECT supporter_1.donation
           FROM supporter supporter_1));


ALTER TABLE public.view7 OWNER TO c370_s19;

--
-- Name: view8; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view8 AS
 SELECT member.name
   FROM (member
   JOIN supports ON ((member.memberid = supports.member)))
  WHERE (member.gender = 'male'::bpchar);


ALTER TABLE public.view8 OWNER TO c370_s19;

--
-- Name: view9; Type: VIEW; Schema: public; Owner: c370_s19
--

CREATE VIEW view9 AS
 SELECT avg(volunteer.age) AS avg
   FROM (         SELECT volunteer_1.sin
                   FROM volunteer volunteer_1
        INTERSECT
                 SELECT organize.volunteer
                   FROM organize
                  WHERE (organize.campaign = 'Let it be'::bpchar)) s,
    volunteer
  WHERE (volunteer.sin = s.sin);


ALTER TABLE public.view9 OWNER TO c370_s19;

--
-- Data for Name: campaign; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY campaign (name, starttime, endtime) FROM stdin;
A Day In The Life             	2010/08/01	2010/10/10
Strawberry fields forever     	2010/09/01	2010/11/10
Abbey Road                    	2011/01/05	2011/01/19
Let it be                     	2011/04/20	2011/05/10
In My Life                    	2012/03/22	2012/04/18
hellow world                  	2014/12/25	2015/01/25
\.


--
-- Data for Name: cost; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY cost (subject, amount, campaign) FROM stdin;
Rent for the location         	1000	A Day In The Life             
Rent for the location         	1400	Strawberry fields forever     
Rent for the location         	2000	Abbey Road                    
Rent for the location         	2400	Let it be                     
Rent for the location         	3000	In My Life                    
poster                        	100	In My Life                    
poster                        	98	A Day In The Life             
poster                        	258	Strawberry fields forever     
poster                        	1000	Let it be                     
\.


--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY employee (sin, name, gender, age, salary, "position") FROM stdin;
101	John He                       	male  	27	50000	President                     
102	Jenny Li                      	female	25	30000	Human Resource                
103	Ken Ho                        	male  	26	40000	Director                      
\.


--
-- Data for Name: event; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY event (campaign, name, note) FROM stdin;
Let it be                     	The Start Event               	Time: 8:00AM to 12:00PM, Every Wednesday!                                                           
Let it be                     	Hello World                   	May 2nd, 8:00PM to 12:00AM                                                                          
\.


--
-- Data for Name: funds; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY funds (supporter, campaign) FROM stdin;
401	Let it be                     
402	Let it be                     
403	Let it be                     
401	A Day In The Life             
404	A Day In The Life             
405	A Day In The Life             
401	Abbey Road                    
405	Abbey Road                    
403	Abbey Road                    
402	In My Life                    
404	In My Life                    
405	Strawberry fields forever     
\.


--
-- Data for Name: hostin; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY hostin (location, campaign) FROM stdin;
2993 Oakbay Ave, Victoria, BC 	A Day In The Life             
3001 Sannich Rd, Victoria, BC 	Strawberry fields forever     
583 Johnson St, Victoria, BC  	Abbey Road                    
919 RoyalOak Ave, Victoria, BC	Let it be                     
105 Bay Street, Victoria, BC  	In My Life                    
1024 Cook Street, Victoria, BC	In My Life                    
\.


--
-- Data for Name: location; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY location (address) FROM stdin;
2993 Oakbay Ave, Victoria, BC 
3001 Sannich Rd, Victoria, BC 
583 Johnson St, Victoria, BC  
919 RoyalOak Ave, Victoria, BC
105 Bay Street, Victoria, BC  
1024 Cook Street, Victoria, BC
\.


--
-- Data for Name: member; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY member (sin, name, gender, age, memberid, donation, duration, annotation) FROM stdin;
201	Caitlin A                     	female	26	1001	1000	8 months            	\N
202	Kaitlyn A                     	female	26	1002	1000	8 months            	\N
203	Kaitlin A                     	female	26	1003	1000	8 months            	\N
204	Katelyn A                     	female	26	1004	1000	8 months            	\N
205	Katelin A                     	female	26	1005	1000	8 months            	\N
206	Catelin A                     	female	26	1006	1000	8 months            	\N
207	Catelyn A                     	female	26	1007	1000	8 months            	\N
208	John H                        	male  	20	1008	1000	8 months            	\N
209	Jason M                       	male  	15	1009	1000	8 months            	\N
200	Caitlyn A                     	female	26	1000	1000	8 months            	Awesome                                           
\.


--
-- Data for Name: organize; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY organize (volunteer, campaign) FROM stdin;
301	A Day In The Life             
303	A Day In The Life             
304	A Day In The Life             
305	A Day In The Life             
302	Let it be                     
306	Let it be                     
307	Let it be                     
308	Let it be                     
308	In My Life                    
301	In My Life                    
312	Abbey Road                    
301	In My Life                    
\.


--
-- Data for Name: supporter; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY supporter (sin, name, gender, age, donation) FROM stdin;
405	Walter W                      	male  	35	500000
401	Mike A                        	male  	35	1000
402	Mike B                        	male  	35	500
403	Mike B                        	male  	35	5000
404	James A                       	male  	35	55000
\.


--
-- Data for Name: supports; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY supports (member, campaign, date) FROM stdin;
1000	Let it be                     	2011/01/01                    
1008	Let it be                     	2011/01/01                    
1001	In My Life                    	2011/01/01                    
1003	In My Life                    	2011/01/01                    
1005	In My Life                    	2011/01/01                    
1007	In My Life                    	2011/01/01                    
1009	In My Life                    	2011/01/01                    
\.


--
-- Data for Name: volunteer; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY volunteer (sin, name, gender, age, numberofparticipation, tier) FROM stdin;
301	Johnson B                     	male  	21	2	1
302	Jacob C                       	male  	29	5	2
309	Mike Z                        	male  	29	1	1
304	Joanna E                      	female	55	50	2
305	Mandy F                       	female	25	3	2
306	Linda G                       	female	25	4	2
307	Lucian H                      	male  	20	9	2
308	Lucian H                      	male  	20	9	2
303	Jacky D                       	male  	26	1	1
310	Ken H                         	male  	30	5	2
311	Jen H                         	female	25	5	2
312	Harley H                      	male  	25	2	1
\.


--
-- Data for Name: works; Type: TABLE DATA; Schema: public; Owner: c370_s19
--

COPY works (employee, campaign) FROM stdin;
101	A Day In The Life             
101	Strawberry fields forever     
101	Abbey Road                    
101	Let it be                     
101	In My Life                    
102	In My Life                    
103	Let it be                     
103	Abbey Road                    
102	Strawberry fields forever     
\.


--
-- Name: campaign_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s19; Tablespace: 
--

ALTER TABLE ONLY campaign
    ADD CONSTRAINT campaign_pkey PRIMARY KEY (name);


--
-- Name: cost_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s19; Tablespace: 
--

ALTER TABLE ONLY cost
    ADD CONSTRAINT cost_pkey PRIMARY KEY (subject, campaign);


--
-- Name: employee_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s19; Tablespace: 
--

ALTER TABLE ONLY employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (sin);


--
-- Name: event_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s19; Tablespace: 
--

ALTER TABLE ONLY event
    ADD CONSTRAINT event_pkey PRIMARY KEY (campaign, name);


--
-- Name: location_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s19; Tablespace: 
--

ALTER TABLE ONLY location
    ADD CONSTRAINT location_pkey PRIMARY KEY (address);


--
-- Name: member_memberid_key; Type: CONSTRAINT; Schema: public; Owner: c370_s19; Tablespace: 
--

ALTER TABLE ONLY member
    ADD CONSTRAINT member_memberid_key UNIQUE (memberid);


--
-- Name: member_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s19; Tablespace: 
--

ALTER TABLE ONLY member
    ADD CONSTRAINT member_pkey PRIMARY KEY (sin);


--
-- Name: supporter_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s19; Tablespace: 
--

ALTER TABLE ONLY supporter
    ADD CONSTRAINT supporter_pkey PRIMARY KEY (sin);


--
-- Name: volunteer_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s19; Tablespace: 
--

ALTER TABLE ONLY volunteer
    ADD CONSTRAINT volunteer_pkey PRIMARY KEY (sin);


--
-- Name: cost_campaign_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY cost
    ADD CONSTRAINT cost_campaign_fkey FOREIGN KEY (campaign) REFERENCES campaign(name);


--
-- Name: event_campaign_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY event
    ADD CONSTRAINT event_campaign_fkey FOREIGN KEY (campaign) REFERENCES campaign(name);


--
-- Name: funds_campaign_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY funds
    ADD CONSTRAINT funds_campaign_fkey FOREIGN KEY (campaign) REFERENCES campaign(name);


--
-- Name: funds_supporter_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY funds
    ADD CONSTRAINT funds_supporter_fkey FOREIGN KEY (supporter) REFERENCES supporter(sin);


--
-- Name: hostin_campaign_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY hostin
    ADD CONSTRAINT hostin_campaign_fkey FOREIGN KEY (campaign) REFERENCES campaign(name);


--
-- Name: hostin_location_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY hostin
    ADD CONSTRAINT hostin_location_fkey FOREIGN KEY (location) REFERENCES location(address);


--
-- Name: organzie_campaign_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY organize
    ADD CONSTRAINT organzie_campaign_fkey FOREIGN KEY (campaign) REFERENCES campaign(name);


--
-- Name: organzie_volunteer_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY organize
    ADD CONSTRAINT organzie_volunteer_fkey FOREIGN KEY (volunteer) REFERENCES volunteer(sin);


--
-- Name: supports_campaign_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY supports
    ADD CONSTRAINT supports_campaign_fkey FOREIGN KEY (campaign) REFERENCES campaign(name);


--
-- Name: supports_member_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY supports
    ADD CONSTRAINT supports_member_fkey FOREIGN KEY (member) REFERENCES member(memberid);


--
-- Name: works_campaign_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY works
    ADD CONSTRAINT works_campaign_fkey FOREIGN KEY (campaign) REFERENCES campaign(name);


--
-- Name: works_employee_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s19
--

ALTER TABLE ONLY works
    ADD CONSTRAINT works_employee_fkey FOREIGN KEY (employee) REFERENCES employee(sin);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

