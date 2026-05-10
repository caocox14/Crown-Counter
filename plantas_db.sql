--
-- PostgreSQL database dump
--

\restrict cuoDRwEfFfHypYIJWhYs4dSMltTbse9gfxqckungYvRLstdJtS5G3ydi293FAKJ

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE IF EXISTS ONLY public.plantas DROP CONSTRAINT IF EXISTS plantas_pkey;
ALTER TABLE IF EXISTS public.plantas ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE IF EXISTS public.plantas_id_seq;
DROP TABLE IF EXISTS public.plantas;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: plantas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.plantas (
    id integer NOT NULL,
    nombre_cientifico character varying(150) NOT NULL,
    nombres_comunes text NOT NULL,
    imagen character(150),
    humedad integer,
    temperatura integer
);


ALTER TABLE public.plantas OWNER TO postgres;

--
-- Name: plantas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.plantas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.plantas_id_seq OWNER TO postgres;

--
-- Name: plantas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.plantas_id_seq OWNED BY public.plantas.id;


--
-- Name: plantas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plantas ALTER COLUMN id SET DEFAULT nextval('public.plantas_id_seq'::regclass);


--
-- Data for Name: plantas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.plantas (id, nombre_cientifico, nombres_comunes, imagen, humedad, temperatura) FROM stdin;
1	Echinocactus grusonii	 Golden Barrel Cactus ,  Barrel cactus , "Mother-in-law s-seat"	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/202701866300342272.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0	0
2	Aloe vera	 Aloe vera ,  Aloe ,  آلوورا 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/242358321552261120.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0	0
\.


--
-- Name: plantas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.plantas_id_seq', 3, true);


--
-- Name: plantas plantas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plantas
    ADD CONSTRAINT plantas_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict cuoDRwEfFfHypYIJWhYs4dSMltTbse9gfxqckungYvRLstdJtS5G3ydi293FAKJ

