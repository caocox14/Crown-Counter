-- pg_dump -U postgres -d plantas_db --clean --if-exists -f plantas_db.sql
-- PostgreSQL database dump
--

\restrict eBNksx4BPsQZdSGZjN1Gkfw3dnIc1JFqOSNKBlUAgh1XA6VjRBn5gTSkyKicCs0

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
    humedad real,
    temperatura real
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
4	Helianthus annuus	 Sunflower ,  Common sunflower ,  آفتابگردان 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153840158012080172.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-7.5
5	Rosa × odorata	 Tea rose ,  Spice Humes blush ,  Hybrid Tea Rose 	                                                                                                                                                      	0.65	-7.5
6	Bixa orellana	 Lipstick tree ,  Annatto ,  Achiote 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153454328214978569.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.8	19.5
7	Capsicum annuum	 Peppers ,  Chili ,  Bell Pepper 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/317731389827022848.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	7.5
8	Sesamum indicum	 Sesame ,  Beniseed ,  Benneseed 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154157526030483465.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	14.5
9	Ocimum tenuiflorum	 Tulasi ,  Tulsi ,  तुलसी 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/237989193055338496.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	7.5
10	Albuca bracteata	 False seaonion ,  False Sea-onion ,  Pregnant Onion 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153423215471886338.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-2
11	Gossypium hirsutum	 American cotton ,  Cotton ,  Bourbon cotton 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153898290394431517.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	28
12	Papaver rhoeas	 Common poppy ,  Field Poppy ,  Shirley poppy 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/347124084416872448.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-20
13	Circaea lutetiana	"Broadleaf Enchanter s-nightshade", "Enchanter s-nightshade", "Common Enchanter s Nightshade"	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/201173682576523264.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-17.5
14	Vaccinium corymbosum	 Blueberry ,  Highbush blueberry ,  American blueberry 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/214257325487718400.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-17.5
15	Bambusa vulgaris	 Bamboo ,  Common bamboo ,  Feather bamboo 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154246732501221418.png?x-oss-process=image/format,webp/resize,s_300&v=1.0       	0.65	7.5
16	Musa × paradisiaca	 Banana ,  Plantain ,  French plantain 	                                                                                                                                                      	0.5	12.5
17	Bougainvillea spectabilis	 Great bougainvillea ,  Bougainvillea ,  Paper flower 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154035914031497259.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	3
18	Saraca indica	 Asoka-tree ,  Ashok ,  Asoca 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/357128467703726080.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.8	30
19	Coffea arabica	 Coffee ,  Arabian coffee ,  Coffeetree 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/348107034927202304.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	15
20	Caladium bicolor	 Caladium ,  Heart of Jesus ,  Angel-wings 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154122277233885212.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	20
21	Kalanchoe laetivirens	 Mother of millions ,  Crenatodaigremontiana ,  Mother of Thousands 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/393494844857647104.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	24
22	Calendula stellata	 Calendulas ,  Pot Marigold ,  Star Calendula 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/351944519486767104.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-12.5
23	Camellia japonica	 Camellia ,  Japanese Camellia ,  Rose of Winter 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/348098389158035456.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-12.5
24	Cannabis sativa	 Cannabis ,  Marijuana ,  Ganja 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154052655814017039.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	24
25	Saccharum officinarum	 Sugarcane ,  Noble sugarcane , "Ka ñaruushi"	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154125318070730766.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.8	27.5
26	Cinnamomum verum	 Ceylon Cinnamon ,  Cinnamon ,  Sri Lanka Cinnamon 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/222362998223699968.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.8	27.5
27	Oxalis versicolor	 Peppermint rock oxalis 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/157642814681776132.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-2
28	Ficus elastica	 Rubberplant ,  فیکوس ,  فیکوس الاستیکا 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154078743445372950.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-12.5
29	Hibiscus rosa-sinensis	 Hawaiian hibiscus ,  Hibiscus ,  गुड़हल 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154120121160302616.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-12.5
30	Triticum aestivum	 Wheat ,  Common Wheat ,  Bread Wheat 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153464880949624853.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-12.5
31	Prunus cerasifera	 Cherry plum, myrobalan ,  Cherry Plum ,  Purple-leaf Plum 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/202644425407725568.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-17.5
32	Schefflera arboricola	 Dwarf umbrella-tree ,  شفلرا ,  Hawaiian-elf 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153444759027843082.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	20
34	Cyclospermum leptophyllum	 Celery ,  Marsh Parsley ,  Slender-celery 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154228216897208327.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	29
35	Dianthus caryophyllus	 Carnation ,  Clove pink ,  Divine-flower 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153723133038166047.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	-7.5
37	Chrysanthemum indicum	 Indian chrysanthemum ,  Chrysanthemum ,  চন্দ্রমল্লিকা 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153755942293340180.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-7.5
36	Cocos nucifera	 Coconut palm ,  Coconut ,  Copra 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/201174919527104512.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	20
38	Davallia canariensis	 Deer-foot fern ,  Rabbit foot fern ,  Hare-foot fern 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/605064083457900545.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	7.5
39	Dahlia pinnata	 Dahlia ,  Pinnate dahlia ,  کوکب 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154057612206276631.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	18
40	Taraxacum officinale	 Dandelion ,  Blowball ,  Common Dandelion 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153417717913747457.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-20
41	Asparagus officinalis	 Garden asparagus ,  Asparagus ,  Gemüsespargel 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/317695758778335232.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-7.5
42	Eucalyptus camaldulensis	 Eucalyptus ,  Murray red gum ,  Blue gum 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154508789930786816.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	-2
43	Ficus lyrata	 Fiddle-leaf fig ,  فیکوس لیراتا ,  Lyre-leaf figtree 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154144580999053326.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	12.5
44	Fittonia albivenis	 Nerveplant ,  Mosaic-plant ,  Angel Plant 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153868848393617419.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	21.5
45	Hoya carnosa	 Honeyplant ,  Hindu Rope ,  Waxplant 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/201212968642412544.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	3
46	Cicer arietinum	 Chickpea ,  Bengal gram ,  Garbanzo 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153990872709464092.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	22.5
47	Gardenia jasminoides	 Gardenia ,  Cape jasmine ,  Jasmin 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/201211542713270272.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	7.5
48	Juniperus communis	 Common juniper ,  Juniper ,  Malchangel 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153864076684951586.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-20
49	Phaseolus vulgaris	 Bean ,  Kidney bean ,  Common Bean 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153923896989450273.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	3
50	Osmanthus fragrans	 Sweet osmanthus ,  Tea Olive ,  Fragrant olive 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154079194416939026.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	-2
51	Hydrangea macrophylla	 Hydrangea ,  Hortensia ,  Bigleaf Hydrangea 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154128268713263129.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-12.5
52	Crassula ovata	 Jade plant ,  Money Tree ,  Ogre ears 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154223947699716110.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	3
53	Lavandula angustifolia	 English lavender ,  Common Lavender ,  Lavender 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/314436260852662272.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	-12.5
54	Lepidium sativum	 Garden cress ,  Pepperwort ,  Town cress 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153823111286882321.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	18
55	Iris × germanica	 Bearded Iris ,  Flags ,  German Iris 	                                                                                                                                                      	0.35	-17.5
56	Spathiphyllum wallisii	 Peace lily ,  اسپاتی فیلوم ,  Peach lily 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153421815312547857.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	12.5
57	Cordyline fruticosa	 Broadleaf palm-lily ,  Ti plant ,  Good-luck-plant 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154495260783804421.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	12.5
58	Plantago major	 Common plantain ,  Broadleaf Plantain ,  Plantain 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154155228222980096.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-20
59	Nymphaea candida	 White water lily ,  Shining water lily ,  Atlantic Waterlily 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/217204665190940672.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.8	18.5
60	Phalaenopsis spp.	 Orchid ,  Moth Orchid ,  Butterfly Orchid 	                                                                                                                                                      	0.7	22.5
61	Magnolia grandiflora	 Southern magnolia ,  Evergreen Magnolia ,  Magnolia little gem 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154026701326647299.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-12.5
62	Agave cupreata		https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153893815038509097.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	7.5
87	Camellia sinensis	 Black tea ,  Tea ,  Teabush 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153926388070481953.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0	0
63	Mangifera indica	 Mango ,  Mango Tree ,  आम 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/317750884683579392.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.675	27
64	Tripleurospermum inodorum	 Scentless Mayweed ,  False Chamomile ,  False Mayweed 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/202692215508828160.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	-12.5
66	Zea mays	 Corn ,  Sweet Corn ,  Maize 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153466251044192267.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	3
67	Mentha spicata	 Spearmint ,  Wild mint ,  Garden mint 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/317753689297223680.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.8	-20
68	Myrtus communis	 Myrtle ,  Common Myrtle ,  True myrtle 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/347113789380263936.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-7.5
69	Ilex aquifolium	 Holly ,  English holly ,  Common Holly 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/201213213455548416.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-7.5
72	Dysphania ambrosioides	 Jerusalem-tea ,  Epazote ,  Spanish-tea 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153743336564326429.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	22
70	Azadirachta indica	 Neem ,  Neem Tree ,  नीम 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153402616808734755.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.8	29.5
71	Plectranthus amboinicus	 Cuban-oregano ,  Indian-mint ,  Orégano brujo 	https://www.picturethisai.com/wiki-image/1080/153933693809852443.jpeg                                                                                 	0.5	22.5
74	Petroselinum crispum	 Parsley ,  Flat Leaf Parsley ,  Garden parsley 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/317759152495624192.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-17.5
75	Petunia × atkinsiana	 Common garden petunia ,  Petunia ,  Garden petunia 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154026151570833423.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	3
76	Pinus sylvestris	"Scot s Pine",  Scots Pine ,  Scotch pine 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/201221889289486336.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	-20
77	Dionaea muscipula	 Venus fly trap ,  Venus flytrap , "Venus  flytrap"	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/202701402443874304.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-2
78	Dracaena fragrans	 Corn plant ,  Fragrant dracaena ,  Dracaena 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154131794881413123.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	12.5
81	Salvia officinalis	 Sage ,  Common Sage ,  Garden Sage 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/317693121668415488.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-12.5
80	Ruta chalepensis	 Fringed rue ,  Rue ,  African rue 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/349667009998815232.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	-7.5
79	Artemisia californica	 California sagebrush ,  Coastal sagebrush ,  Cowboy cologne 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153810153370550294.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	25
83	Syngonium podophyllum	 Arrowhead vine ,  Nephthytis ,  White Butterfly 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/347090111225561088.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	15
82	Tagetes patula	 Marigold ,  French Marigold ,  Spreading marigold 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/351495317447213056.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	3
84	Glycine max	 Soybean ,  Soya ,  Soya-bean 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154025417131425801.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-2
88	Thymus herba-barona	 Caraway thyme ,  Corsican thyme 	https://apps.rhs.org.uk/plantselectorimages/detail/Thymusherbabarona2-2.jpg                                                                           	0.35	-12.5
86	Tamarindus indica	 Tamarind ,  Tamarind Tree ,  Kilytree 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154182183437729792.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	27.5
85	Nicotiana tabacum	 Tobacco ,  Cultivated Tobacco ,  Igwayi 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153992788264878083.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-7.5
89	Marsilea quadrifolia	 European water-clover ,  European waterclover ,  Common Water Clover 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/157090619326464009.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.8	-12.5
90	Verbena × hybrida	 Verbena ,  Hybrid Verbena 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/153785899690229793.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	12.5
91	Catharanthus roseus	 Periwinkle ,  Vinca ,  Sadabahar 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/202698610715131904.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	7.5
93	Zamioculcas zamiifolia	 ZZ Plant ,  Zanzibar Gem ,  Zeezee plant 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/348133526285484032.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.35	12.5
92	Viola odorata	 Sweet violet ,  Garden violet ,  English violet 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/202693061617385472.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-17.5
2	Aloe vera	 Aloe vera ,  Aloe ,  آلوورا 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/242358321552261120.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	7.5
33	Allium cepa	 Onion ,  Spring Onion ,  Green Onion 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/317839670247555072.png?x-oss-process=image/format,webp/resize,s_300&v=1.0       	0.65	-7.5
65	Leucanthemum vulgare	 Ox-Eye Daisy ,  Oxeye daisy ,  Dog Daisy 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/154193608050737182.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.5	-20
73	Peperomia obtusifolia	 American rubberplant ,  برگ قاشقی ,  Baby Rubberplant 	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/347093040393256960.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.65	12.5
94	Echinocactus grusonii	 Golden Barrel Cactus ,  Barrel cactus , "Mother-in-law s-seat"	https://www.picturethisai.com/image-handle/website_cmsname/image/1080/202701866300342272.jpeg?x-oss-process=image/format,webp/resize,s_300&v=1.0      	0.2	7.5
\.


--
-- Name: plantas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.plantas_id_seq', 94, true);


--
-- Name: plantas plantas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.plantas
    ADD CONSTRAINT plantas_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict eBNksx4BPsQZdSGZjN1Gkfw3dnIc1JFqOSNKBlUAgh1XA6VjRBn5gTSkyKicCs0

