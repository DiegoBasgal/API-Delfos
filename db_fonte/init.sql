--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3 (Debian 16.3-1.pgdg120+1)
-- Dumped by pg_dump version 16.3 (Debian 16.3-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: data; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.data (
    "timestamp" timestamp without time zone NOT NULL,
    wind_speed numeric,
    power numeric,
    ambient_temperature numeric
);


ALTER TABLE public.data OWNER TO admin;

--
-- Data for Name: data; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.data ("timestamp", wind_speed, power, ambient_temperature) FROM stdin;
\.


--
-- Name: data data_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.data
    ADD CONSTRAINT data_pkey PRIMARY KEY ("timestamp");


--
-- PostgreSQL database dump complete
--

