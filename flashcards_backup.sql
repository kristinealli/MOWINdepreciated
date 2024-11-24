--
-- PostgreSQL database dump
--

-- Dumped from database version 14.14 (Homebrew)
-- Dumped by pg_dump version 14.14 (Homebrew)

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
-- Name: auth_group; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO kristinejohnson;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO kristinejohnson;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO kristinejohnson;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO kristinejohnson;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO kristinejohnson;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO kristinejohnson;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO kristinejohnson;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO kristinejohnson;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO kristinejohnson;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO kristinejohnson;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO kristinejohnson;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO kristinejohnson;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: cards_card; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.cards_card (
    id bigint NOT NULL,
    anishinaabemowin character varying(100) NOT NULL,
    english character varying(100) NOT NULL,
    pronunciation character varying(100) NOT NULL,
    subject character varying(100) NOT NULL,
    date_created timestamp with time zone NOT NULL,
    example_sentence text NOT NULL,
    audio_file character varying(100) NOT NULL,
    deck_id bigint NOT NULL
);


ALTER TABLE public.cards_card OWNER TO kristinejohnson;

--
-- Name: cards_card_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.cards_card_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cards_card_id_seq OWNER TO kristinejohnson;

--
-- Name: cards_card_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.cards_card_id_seq OWNED BY public.cards_card.id;


--
-- Name: cards_deck; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.cards_deck (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    description text NOT NULL,
    date_created timestamp with time zone NOT NULL,
    is_public boolean NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    owner_id integer
);


ALTER TABLE public.cards_deck OWNER TO kristinejohnson;

--
-- Name: cards_deck_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.cards_deck_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cards_deck_id_seq OWNER TO kristinejohnson;

--
-- Name: cards_deck_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.cards_deck_id_seq OWNED BY public.cards_deck.id;


--
-- Name: cards_deck_tags; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.cards_deck_tags (
    id bigint NOT NULL,
    deck_id bigint NOT NULL,
    tag_id bigint NOT NULL
);


ALTER TABLE public.cards_deck_tags OWNER TO kristinejohnson;

--
-- Name: cards_deck_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.cards_deck_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cards_deck_tags_id_seq OWNER TO kristinejohnson;

--
-- Name: cards_deck_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.cards_deck_tags_id_seq OWNED BY public.cards_deck_tags.id;


--
-- Name: cards_deckshare; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.cards_deckshare (
    id bigint NOT NULL,
    permissions character varying(10) NOT NULL,
    date_shared timestamp with time zone NOT NULL,
    active boolean NOT NULL,
    deck_id bigint NOT NULL,
    shared_by_id integer NOT NULL,
    shared_with_id integer NOT NULL
);


ALTER TABLE public.cards_deckshare OWNER TO kristinejohnson;

--
-- Name: cards_deckshare_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.cards_deckshare_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cards_deckshare_id_seq OWNER TO kristinejohnson;

--
-- Name: cards_deckshare_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.cards_deckshare_id_seq OWNED BY public.cards_deckshare.id;


--
-- Name: cards_profile; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.cards_profile (
    id bigint NOT NULL,
    study_streak integer NOT NULL,
    last_study_date date,
    total_cards_studied integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    preferred_name character varying(100),
    user_id integer NOT NULL,
    CONSTRAINT cards_profile_study_streak_check CHECK ((study_streak >= 0)),
    CONSTRAINT cards_profile_total_cards_studied_check CHECK ((total_cards_studied >= 0))
);


ALTER TABLE public.cards_profile OWNER TO kristinejohnson;

--
-- Name: cards_profile_chosen_decks; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.cards_profile_chosen_decks (
    id bigint NOT NULL,
    profile_id bigint NOT NULL,
    deck_id bigint NOT NULL
);


ALTER TABLE public.cards_profile_chosen_decks OWNER TO kristinejohnson;

--
-- Name: cards_profile_chosen_decks_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.cards_profile_chosen_decks_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cards_profile_chosen_decks_id_seq OWNER TO kristinejohnson;

--
-- Name: cards_profile_chosen_decks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.cards_profile_chosen_decks_id_seq OWNED BY public.cards_profile_chosen_decks.id;


--
-- Name: cards_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.cards_profile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cards_profile_id_seq OWNER TO kristinejohnson;

--
-- Name: cards_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.cards_profile_id_seq OWNED BY public.cards_profile.id;


--
-- Name: cards_tag; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.cards_tag (
    id bigint NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.cards_tag OWNER TO kristinejohnson;

--
-- Name: cards_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.cards_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cards_tag_id_seq OWNER TO kristinejohnson;

--
-- Name: cards_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.cards_tag_id_seq OWNED BY public.cards_tag.id;


--
-- Name: cards_usercardprogress; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.cards_usercardprogress (
    id bigint NOT NULL,
    box_level integer NOT NULL,
    last_reviewed timestamp with time zone NOT NULL,
    next_review_date timestamp with time zone NOT NULL,
    round_completed boolean NOT NULL,
    card_id bigint NOT NULL,
    user_id integer NOT NULL,
    last_review_result boolean NOT NULL
);


ALTER TABLE public.cards_usercardprogress OWNER TO kristinejohnson;

--
-- Name: cards_usercardprogress_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.cards_usercardprogress_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cards_usercardprogress_id_seq OWNER TO kristinejohnson;

--
-- Name: cards_usercardprogress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.cards_usercardprogress_id_seq OWNED BY public.cards_usercardprogress.id;


--
-- Name: cards_userdeck; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.cards_userdeck (
    id bigint NOT NULL,
    date_added timestamp with time zone NOT NULL,
    is_owner boolean NOT NULL,
    deck_id bigint NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.cards_userdeck OWNER TO kristinejohnson;

--
-- Name: cards_userdeck_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.cards_userdeck_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cards_userdeck_id_seq OWNER TO kristinejohnson;

--
-- Name: cards_userdeck_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.cards_userdeck_id_seq OWNED BY public.cards_userdeck.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO kristinejohnson;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO kristinejohnson;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO kristinejohnson;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO kristinejohnson;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO kristinejohnson;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO kristinejohnson;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO kristinejohnson;

--
-- Name: temp_json_import; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.temp_json_import (
    data jsonb
);


ALTER TABLE public.temp_json_import OWNER TO kristinejohnson;

--
-- Name: vocabulary; Type: TABLE; Schema: public; Owner: kristinejohnson
--

CREATE TABLE public.vocabulary (
    id integer NOT NULL,
    data jsonb NOT NULL
);


ALTER TABLE public.vocabulary OWNER TO kristinejohnson;

--
-- Name: vocabulary_id_seq; Type: SEQUENCE; Schema: public; Owner: kristinejohnson
--

CREATE SEQUENCE public.vocabulary_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.vocabulary_id_seq OWNER TO kristinejohnson;

--
-- Name: vocabulary_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kristinejohnson
--

ALTER SEQUENCE public.vocabulary_id_seq OWNED BY public.vocabulary.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: cards_card id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_card ALTER COLUMN id SET DEFAULT nextval('public.cards_card_id_seq'::regclass);


--
-- Name: cards_deck id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deck ALTER COLUMN id SET DEFAULT nextval('public.cards_deck_id_seq'::regclass);


--
-- Name: cards_deck_tags id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deck_tags ALTER COLUMN id SET DEFAULT nextval('public.cards_deck_tags_id_seq'::regclass);


--
-- Name: cards_deckshare id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deckshare ALTER COLUMN id SET DEFAULT nextval('public.cards_deckshare_id_seq'::regclass);


--
-- Name: cards_profile id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_profile ALTER COLUMN id SET DEFAULT nextval('public.cards_profile_id_seq'::regclass);


--
-- Name: cards_profile_chosen_decks id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_profile_chosen_decks ALTER COLUMN id SET DEFAULT nextval('public.cards_profile_chosen_decks_id_seq'::regclass);


--
-- Name: cards_tag id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_tag ALTER COLUMN id SET DEFAULT nextval('public.cards_tag_id_seq'::regclass);


--
-- Name: cards_usercardprogress id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_usercardprogress ALTER COLUMN id SET DEFAULT nextval('public.cards_usercardprogress_id_seq'::regclass);


--
-- Name: cards_userdeck id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_userdeck ALTER COLUMN id SET DEFAULT nextval('public.cards_userdeck_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: vocabulary id; Type: DEFAULT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.vocabulary ALTER COLUMN id SET DEFAULT nextval('public.vocabulary_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add card	7	add_card
26	Can change card	7	change_card
27	Can delete card	7	delete_card
28	Can view card	7	view_card
29	Can add deck	8	add_deck
30	Can change deck	8	change_deck
31	Can delete deck	8	delete_deck
32	Can view deck	8	view_deck
33	Can add tag	9	add_tag
34	Can change tag	9	change_tag
35	Can delete tag	9	delete_tag
36	Can view tag	9	view_tag
37	Can add user deck	10	add_userdeck
38	Can change user deck	10	change_userdeck
39	Can delete user deck	10	delete_userdeck
40	Can view user deck	10	view_userdeck
41	Can add user card progress	11	add_usercardprogress
42	Can change user card progress	11	change_usercardprogress
43	Can delete user card progress	11	delete_usercardprogress
44	Can view user card progress	11	view_usercardprogress
45	Can add profile	12	add_profile
46	Can change profile	12	change_profile
47	Can delete profile	12	delete_profile
48	Can view profile	12	view_profile
49	Can add deck share	13	add_deckshare
50	Can change deck share	13	change_deckshare
51	Can delete deck share	13	delete_deckshare
52	Can view deck share	13	view_deckshare
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$320000$iYJzySvmjmUzsfBuCxE9VJ$tSgJChvaS5dgfWyVUgVYidFTpeAV7gH5AvDFpvyqAIo=	2024-11-18 16:47:57.98046-05	f	kristinejohnson				f	t	2024-11-18 16:47:57.843879-05
3	pbkdf2_sha256$320000$90zsDz9lVYoI9UD0dZ0X0r$aozjzdaFn0r5HoddGEzw77m+AWvuOhwc19X9zfUMogo=	2024-11-18 17:51:58.547665-05	f	apollojohnson				f	t	2024-11-18 17:51:12.788466-05
4	pbkdf2_sha256$320000$epIYwzLcxaHhGuYEDCOAlL$q//dcN68bGDEK4eRUDiaTNa6GrjZDej9LusjuAGo+Mg=	2024-11-18 18:00:55.664041-05	f	Apollo				f	t	2024-11-18 18:00:55.535726-05
5	pbkdf2_sha256$320000$39fSlW6eKLJXlJX3BTrFou$S5uhJ7PgAFvhA66vT/jHNSD/DzOTkS8VTQR9eu5BFMs=	2024-11-18 21:20:05.878239-05	f	lolly				f	t	2024-11-18 21:20:05.743743-05
2	pbkdf2_sha256$320000$y6IHH6zAk7BIJpUA0NB3Tr$+sx7eHxqlIiaGbGZUe/QBbAa1TCUNKavbWyhq9OPq1E=	2024-11-18 22:39:25.299954-05	t	kristineallisonjohnson			kristineallisonjohnson@outlook.com	t	t	2024-11-18 17:49:30.593894-05
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: cards_card; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.cards_card (id, anishinaabemowin, english, pronunciation, subject, date_created, example_sentence, audio_file, deck_id) FROM stdin;
1	Gshkadin dbik giizis	Freeze Up Moon (November)	gsh-kah-din d-bihk gee-zis	November - Freeze-Up Moon	2024-11-18 17:07:12.704781-05			1
2	Jiibay wiikwandiwin	Ghost feast	jee-bay wee-kwan-dih-win	November - Freeze-Up Moon	2024-11-18 17:07:12.711768-05			1
3	Maawnjiwewin	A feast (Invite people together)	mawn-jee-weh-win	November - Freeze-Up Moon	2024-11-18 17:07:12.712796-05			1
4	Mshkawaakdin	Frozen solid	msh-kah-wahk-din	November - Freeze-Up Moon	2024-11-18 17:07:12.713626-05			1
5	Mkom	Ice	m-kohm	November - Freeze-Up Moon	2024-11-18 17:07:12.714562-05			1
6	Mkomiins	Icicle or ice cube	m-kohm-ee-ns	November - Freeze-Up Moon	2024-11-18 17:07:12.715422-05			1
7	N’biingech	I am cold	n-beeng-etch	November - Freeze-Up Moon	2024-11-18 17:07:12.716241-05			1
8	N’giizhoos	I am warm	n-gee-zhoos	November - Freeze-Up Moon	2024-11-18 17:07:12.717092-05			1
9	Gsinaa	It is cold outside	g-sih-nah	November - Freeze-Up Moon	2024-11-18 17:07:12.718225-05			1
10	Nchiiwat	Stormy weather	n-chee-waht	November - Freeze-Up Moon	2024-11-18 17:07:12.719042-05			1
11	Noodin	Windy	noh-din	November - Freeze-Up Moon	2024-11-18 17:07:12.719727-05			1
12	Gchi-Gsinaa	It is VERY cold outside	g-chee g-sih-nah	November - Freeze-Up Moon	2024-11-18 17:07:12.720403-05			1
13	Gchi-Nchiiwat	It is VERY stormy	g-chee n-chee-waht	November - Freeze-Up Moon	2024-11-18 17:07:12.720999-05			1
14	Gchi-Noodin	It is VERY windy	g-chee noh-din	November - Freeze-Up Moon	2024-11-18 17:07:12.721527-05			1
15	Goon	Snow on the ground	goh-n	November - Freeze-Up Moon	2024-11-18 17:07:12.722049-05			1
16	Goonkaa	A lot of snow on the ground	gohn-kah	November - Freeze-Up Moon	2024-11-18 17:07:12.722649-05			1
17	Boodwe	He/She Builds a fire	boo-dweh	November - Freeze-Up Moon	2024-11-18 17:07:12.723726-05			1
18	Giiwse	He/She Hunts	gee-w-seh	November - Freeze-Up Moon	2024-11-18 17:07:12.724608-05			1
19	N’Waawaashkeshi-giiwse	I am Deer hunting	n-wah-wahsh-keh-shee gee-w-seh	November - Freeze-Up Moon	2024-11-18 17:07:12.725445-05			1
20	N’Mizise-giiwse	I am Turkey hunting	n-mih-zih-seh gee-w-seh	November - Freeze-Up Moon	2024-11-18 17:07:12.726194-05			1
21	Dagwaagi	It is Fall	dah-gwah-gee	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.350984-05			2
22	Waabagaa	The leaves are turning color	wah-bah-gah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.353506-05			2
23	Waabagaa Giizis	The leaves turning color moon (September or October)	wah-bah-gah gee-zis	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.354288-05			2
24	Mtigwaakiing G’wii zhaami	We will go to the Forest	m-tih-gwah-kee-ing g-wih zah-mee	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.354929-05			2
25	G’wii oo giiwsemi nangwa	We will go hunting today	g-wih oh gee-w-seh-mee nang-wah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.355537-05			2
26	Zhashkwedoonyan n’da waabndaanan	I see Mushrooms	zhahsh-kweh-dohn-yahn n-dah wah-bn-dah-nahn	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.356124-05			2
27	N’daa miijinan na?	Should I eat them?	n-dah mee-jee-nahn nah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.356752-05			2
28	Enh! Nboobiing gwii toonan	Yes! You will want to put them in the soup	en! n-boh-beeng g-wih too-nahn	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.35733-05			2
29	Maaba Bine ge’ii gwa	This Partridge too!	mah-bah bih-neh geh-ee gwah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.357891-05			2
30	Gonda Binewag gewiinwaa	and these Partridges too	gohn-dah bih-neh-wahg geh-ween-wah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.358521-05			2
31	Manoomin miinwaa	Rice too	mah-noh-min meen-wah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.359028-05			2
32	Zhigaagwanzhiik N’mnopwaag	I like the taste of Onions	zhih-gah-gwahn-zheek n-mnoh-pwahg	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.359643-05			2
33	G’bishigenimaag na gegii?	Do you like them too?	g-bih-shih-geh-nee-mahg nah geh-gee	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.360156-05			2
34	Enh. Mnopogziwag	Yes. They taste good	en. m-noh-pohg-zee-wahg	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.360706-05			2
35	N’bishigendaan nboop	I like soup	n-bih-shih-gehn-dahn n-bohp	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.361263-05			2
36	Genii gwa	Me too!	geh-nee gwah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:21:45.361816-05			2
37	Dagwaagi	It is Fall	dah-gwah-gee	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.951869-05			2
38	Waabagaa	The leaves are turning color	wah-bah-gah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.953461-05			2
39	Waabagaa Giizis	The leaves turning color moon (September or October)	wah-bah-gah gee-zis	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.954159-05			2
40	Mtigwaakiing G’wii zhaami	We will go to the Forest	m-tih-gwah-kee-ing g-wih zah-mee	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.954813-05			2
41	G’wii oo giiwsemi nangwa	We will go hunting today	g-wih oh gee-w-seh-mee nang-wah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.955424-05			2
42	Zhashkwedoonyan n’da waabndaanan	I see Mushrooms	zhahsh-kweh-dohn-yahn n-dah wah-bn-dah-nahn	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.956078-05			2
43	N’daa miijinan na?	Should I eat them?	n-dah mee-jee-nahn nah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.956689-05			2
44	Enh! Nboobiing gwii toonan	Yes! You will want to put them in the soup	en! n-boh-beeng g-wih too-nahn	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.957242-05			2
45	Maaba Bine ge’ii gwa	This Partridge too!	mah-bah bih-neh geh-ee gwah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.957802-05			2
46	Gonda Binewag gewiinwaa	and these Partridges too	gohn-dah bih-neh-wahg geh-ween-wah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.958364-05			2
47	Manoomin miinwaa	Rice too	mah-noh-min meen-wah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.959007-05			2
48	Zhigaagwanzhiik N’mnopwaag	I like the taste of Onions	zhih-gah-gwahn-zheek n-mnoh-pwahg	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.959702-05			2
49	G’bishigenimaag na gegii?	Do you like them too?	g-bih-shih-geh-nee-mahg nah geh-gee	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.960345-05			2
50	Enh. Mnopogziwag	Yes. They taste good	en. m-noh-pohg-zee-wahg	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.96093-05			2
51	N’bishigendaan nboop	I like soup	n-bih-shih-gehn-dahn n-bohp	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.961799-05			2
52	Genii gwa	Me too!	geh-nee gwah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:29:24.96243-05			2
53	Dagwaagi	It is Fall	dah-gwah-gee	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.335783-05			2
54	Waabagaa	The leaves are turning color	wah-bah-gah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.337219-05			2
55	Waabagaa Giizis	The leaves turning color moon (September or October)	wah-bah-gah gee-zis	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.338251-05			2
56	Mtigwaakiing G’wii zhaami	We will go to the Forest	m-tih-gwah-kee-ing g-wih zah-mee	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.343368-05			2
57	G’wii oo giiwsemi nangwa	We will go hunting today	g-wih oh gee-w-seh-mee nang-wah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.344192-05			2
58	Zhashkwedoonyan n’da waabndaanan	I see Mushrooms	zhahsh-kweh-dohn-yahn n-dah wah-bn-dah-nahn	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.344951-05			2
59	N’daa miijinan na?	Should I eat them?	n-dah mee-jee-nahn nah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.345689-05			2
60	Enh! Nboobiing gwii toonan	Yes! You will want to put them in the soup	en! n-boh-beeng g-wih too-nahn	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.346513-05			2
61	Maaba Bine ge’ii gwa	This Partridge too!	mah-bah bih-neh geh-ee gwah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.347195-05			2
62	Gonda Binewag gewiinwaa	and these Partridges too	gohn-dah bih-neh-wahg geh-ween-wah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.347956-05			2
63	Manoomin miinwaa	Rice too	mah-noh-min meen-wah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.348632-05			2
64	Zhigaagwanzhiik N’mnopwaag	I like the taste of Onions	zhih-gah-gwahn-zheek n-mnoh-pwahg	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.349392-05			2
65	G’bishigenimaag na gegii?	Do you like them too?	g-bih-shih-geh-nee-mahg nah geh-gee	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.350052-05			2
66	Enh. Mnopogziwag	Yes. They taste good	en. m-noh-pohg-zee-wahg	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.351086-05			2
67	N’bishigendaan nboop	I like soup	n-bih-shih-gehn-dahn n-bohp	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.351895-05			2
68	Genii gwa	Me too!	geh-nee gwah	Dagwaagin - Autumn Vocabulary	2024-11-18 17:30:01.352387-05			2
69	Aaniin ________ !	Hey ________!	ah-neen ________	Going to the Fair Talk	2024-11-18 17:34:24.665038-05			3
70	Aaniin ________ ! Aaniish ezhiwebak?	Hey ________! What’s happening?	ah-neen ________ ah-neesh eh-zhee-weh-bahk	Going to the Fair Talk	2024-11-18 17:34:24.666567-05			3
71	N’wii zhaa odi Endzhi-waabnda’ding, Waabang.	I want to go over to the Fair tomorrow.	n-wee zah oh-deh en-jee wahb-nah-ding wah-bahng	Going to the Fair Talk	2024-11-18 17:34:24.667344-05			3
72	Gaawiin kii zhaasii na Jiinaagwa?	Didn’t you go yesterday?	gah-ween kee zah-see nah jee-nah-gwah	Going to the Fair Talk	2024-11-18 17:34:24.668023-05			3
73	Kaa. Gii gimiwon gbe-giizhik Jiinaagwa.	No. It rained all day yesterday.	kah gee gih-mih-won gbeh-gee-zheek jee-nah-gwah	Going to the Fair Talk	2024-11-18 17:34:24.668705-05			3
74	Gwii-wiijiiwin.	I want to go with you.	g-wih wee-jee-win	Going to the Fair Talk	2024-11-18 17:34:24.669407-05			3
75	Aahaaw dash! G’wii Minendaagozimi!	Alright then! We will have fun!	ah-how dash g-wih mih-nen-dah-go-zee-mee	Going to the Fair Talk	2024-11-18 17:34:24.670074-05			3
76	Wenesh waa waabndaaman?	What will you see?	weh-nesh wah wahb-nah-mahn	Going to the Fair Talk	2024-11-18 17:34:24.670694-05			3
77	Bezhigoogzhiik N’wii waabmaag!	I want to see the Horses.	beh-zhih-goog-zheek n-wee wahb-mahg	Going to the Fair Talk	2024-11-18 17:34:24.671262-05			3
78	Gchi-Gookoosh na ge’ii gwa.	The Big Pig too?	g-chee goo-kohsh nah geh-ee gwah	Going to the Fair Talk	2024-11-18 17:34:24.671823-05			3
79	Say! Gaawiin N’wii waabmaasiin wa gete-Gookoosh!	Yuck! I don’t want to see that old Pig!	say gah-ween n-wee wahb-mah-seen wah geh-teh goo-kohsh	Going to the Fair Talk	2024-11-18 17:34:24.672419-05			3
80	Enh. Maazhimaagozi.	Yeah. He smells bad.	en mah-zhee-mah-go-zee	Going to the Fair Talk	2024-11-18 17:34:24.67297-05			3
81	Naagish, N’daa shamaawson.	I could feed him a Hotdog.	nah-gish n-dah shah-maw-sohn	Going to the Fair Talk	2024-11-18 17:34:24.673413-05			3
82	Aashiij-maajii. Kiiwinaadis.	Good grief. You are crazy.	ah-shee-mah-jee kee-wee-nah-dis	Going to the Fair Talk	2024-11-18 17:34:24.673833-05			3
83	Niibin	It is Summer.	nee-bin	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.509555-05			4
84	Niibing	When it is Summer.	nee-bing	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.510632-05			4
85	Niibinong	Last Summer (During the Summer)	nee-bin-ohng	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.511122-05			4
86	Manoomin Giizis	August	mah-noh-min gee-zis	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.511605-05			4
87	Miin(an)	Berry, Berries	meen(ahn)	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.512055-05			4
88	Mskomin(ak)	Raspberry, Raspberries	muh-sko-min(ahk)	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.512695-05			4
89	Nangwa	Today	nahng-wah	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.513315-05			4
90	Jiinaagwa	Yesterday	jee-nah-gwah	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.513886-05			4
91	Waabang	Tomorrow	wah-bahng	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.514448-05			4
92	oZaawaa	Yellow	oh-zah-wah	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.514989-05			4
93	Mskwaa	Red	muh-skwah	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.515537-05			4
94	Mkadewaa	Black	muh-kah-deh-wah	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.516082-05			4
95	Waabshkaa	White	wahb-shkah	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.516632-05			4
96	Zhaawshkwaa	Green	zhahw-shkwah	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.517163-05			4
97	Waabanong	East	wah-bah-nohng	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.517738-05			4
98	Zhaawanong	South	zhah-wah-nohng	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.518342-05			4
99	Epngishmok	West	ep-ngish-mohk	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.518945-05			4
100	Giiwedinong	North	gee-weh-dih-nohng	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.519568-05			4
101	Niibin!! It’s Summer!!	It’s Summer!!	nee-bin	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.520208-05			4
102	Niibing, gwii-zhaami zaag’iganing.	This Summer, we will go to the Lake.	nee-bing g-wih zah-mee zahg-ih-gah-ning	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.520819-05			4
103	Niibinong, gaawiin ngii-zhaasii wiikwedong.	Last Summer, I didn’t go to the Bay.	nee-bin-ohng gah-ween n-gee zah-see wee-kweh-dohng	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.52201-05			4
104	Aambe Miinkedaa!	Let’s go berry picking!	ahm-beh meen-keh-dah	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.523027-05			4
105	N’minopidaanan Miinan.	I like the taste of Blueberries.	n-min-oh-pih-dah-nahn mee-nahn	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.523936-05			4
106	N’minopwaag Mskominak.	I like the taste of Raspberries.	n-min-oh-pwahg muh-sko-min-ahk	Niibin - Summertime Vocabulary	2024-11-18 17:37:33.524502-05			4
107	Wegnesh gaawaamdaman?	What did you see?	weh-nesh gah-wahm-dah-mahn	What Did You See or Hear?	2024-11-18 17:39:45.982533-05			5
108	Wegnesh ewaamdaman?	What do you see?	weh-nesh eh-wahm-dah-mahn	What Did You See or Hear?	2024-11-18 17:39:45.983359-05			5
109	Wegnesh gaanoondaman?	What did you hear?	weh-nesh gah-noon-dah-mahn	What Did You See or Hear?	2024-11-18 17:39:45.98401-05			5
110	Wegnesh enoondaman?	What do you hear?	weh-nesh eh-noon-dah-mahn	What Did You See or Hear?	2024-11-18 17:39:45.984588-05			5
111	Endzhi-waabnda’ding	At the Fair, public exhibition	en-jee wahb-nah-dah-ding	What Did You See or Hear?	2024-11-18 17:39:45.985168-05			5
112	Ookaan’gamigoong	In the (animal) Barn	oh-kahn-gah-mih-gohng	What Did You See or Hear?	2024-11-18 17:39:45.98573-05			5
113	Zag’iganing	At the Lake	zahg-ih-gah-ning	What Did You See or Hear?	2024-11-18 17:39:45.986348-05			5
114	Wiikwedong	At the Bay	week-weh-dohng	What Did You See or Hear?	2024-11-18 17:39:45.987319-05			5
115	Ziibiing	At the River	zee-bee-ing	What Did You See or Hear?	2024-11-18 17:39:45.987683-05			5
116	Oodenaang	In the City	oh-deh-nahng	What Did You See or Hear?	2024-11-18 17:39:45.988061-05			5
117	N’gii waamdaan.	I saw it. (inanimate)	n-gee wahm-dahn	What Did You See or Hear?	2024-11-18 17:39:45.98841-05			5
118	N’gii waabmaa.	I saw him/her/it. (animate)	n-gee wahb-mah	What Did You See or Hear?	2024-11-18 17:39:45.98878-05			5
119	N’gii noondaan.	I heard it. (inanimate)	n-gee noon-dahn	What Did You See or Hear?	2024-11-18 17:39:45.989351-05			5
120	N’gii noondwaa.	I heard him/her/them. (animate)	n-gee noon-dwah	What Did You See or Hear?	2024-11-18 17:39:45.989963-05			5
121	Niibiish(an), n’gii waamdaan(an).	The leave(s), I saw (them).	nee-beesh(ahn) n-gee wahm-dahn(ahn)	What Did You See or Hear?	2024-11-18 17:39:45.990497-05			5
122	Magkiik, N’gii waabmaag zag'iganing.	I saw frogs in the lake.	muhg-keek n-gee wahb-mahg zahg-ih-gah-ning	What Did You See or Hear?	2024-11-18 17:39:45.991049-05			5
123	Niibiishan N’waamdaanan ziibiing.	I see leaves in the river.	nee-beesh-ahn n-wahm-dah-nahn zee-bee-ing	What Did You See or Hear?	2024-11-18 17:39:45.991574-05			5
124	Niniwag N’noondwaag.	I hear the men.	nih-nih-wahg n-noon-dwahg	What Did You See or Hear?	2024-11-18 17:39:45.992113-05			5
125	N’niin	I myself	n-neen	What Did You See or Hear?	2024-11-18 17:39:45.992642-05			5
126	G’giin	You	g-geen	What Did You See or Hear?	2024-11-18 17:39:45.993153-05			5
127	Wiin	He/She/It	ween	What Did You See or Hear?	2024-11-18 17:39:45.993692-05			5
128	Asemaa	Tobacco	ah-seh-mah	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.466749-05			6
129	Manoomin	Rice	mah-noh-min	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.467793-05			6
130	Zaaga’igan	Lake	zah-gah-ee-gahn	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.46837-05			6
131	Ziibi	River	zee-bee	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.469058-05			6
132	Jiimaan	Canoe (boat)	jee-mahn	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.4698-05			6
133	Abwi	Paddle	ah-bwee	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.470525-05			6
134	Bimishkaa	Paddles along in a canoe	bih-mish-kah	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.471238-05			6
135	Gaandakii’ige	Push a canoe with a pole	gahn-dah-kee-ee-geh	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.471884-05			6
136	Gaandakii’igan	Push pole	gahn-dah-kee-ee-gahn	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.472647-05			6
137	Bawa’am	Knock Rice	bah-wah-uhm	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.473318-05			6
138	Bawa’iganaak(oon)	Rice knocker(s)	bah-wah-ee-gah-nahk(oon)	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.474099-05			6
139	Gaapizige	Roast (parch)	gah-pee-zih-geh	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.474742-05			6
140	Gaapizigan	Parched Rice	gah-pee-zih-gahn	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.475433-05			6
141	Kik	Kettle	keek	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.476066-05			6
142	Ishkode	Fire	ish-koh-deh	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.476732-05			6
143	Mimigoshkam	Thresh	mih-mih-gohsh-kahm	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.477357-05			6
144	Nanda Mkizinan biiskanan	Put on these Moccasins.	nahn-dah muh-kee-zih-nahn bees-kah-nahn	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.477994-05			6
145	Nooshkaachige	S/He Winnows	nohsh-kah-chee-geh	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.478629-05			6
146	Nooshkaachigaade	It is winnowed (by someone).	nohsh-kah-chee-gah-deh	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.479281-05			6
147	Nooshkaachigan	Winnowed Rice	nohsh-kah-chee-gahn	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.480111-05			6
148	Jiibaakwe	Cook	jee-bah-kweh	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.480796-05			6
149	Wiisni	Eat	wee-snih	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.481432-05			6
150	Biinichige	Clean things	bee-nih-chee-geh	Asemaa and Manoomin Vocabulary	2024-11-18 17:41:59.482141-05			6
151	N’gii dewe’igemi	We drummed.	n-gee deh-weh-ee-geh-mee	Making Simple Sentences (Plural)	2024-11-18 17:43:01.084515-05			7
152	G’ga nagam	You all will sing.	g-gah nah-gahm	Making Simple Sentences (Plural)	2024-11-18 17:43:01.085841-05			7
153	Wemibigwag	They are drinking.	weh-mih-big-wahg	Making Simple Sentences (Plural)	2024-11-18 17:43:01.086505-05			7
154	Wii wiisinwag	They want to eat. (They will eat.)	wee wee-seen-wahg	Making Simple Sentences (Plural)	2024-11-18 17:43:01.087136-05			7
155	G’nendamimi	We (inclusive) are hungry.	g-nen-dah-mih-mee	Making Simple Sentences (Plural)	2024-11-18 17:43:01.087758-05			7
156	Gii niimwag	They danced.	gee neem-wahg	Making Simple Sentences (Plural)	2024-11-18 17:43:01.088561-05			7
157	G’wii niim	You all will, or, want to dance.	g-wee neem	Making Simple Sentences (Plural)	2024-11-18 17:43:01.089198-05			7
158	G’gii niimwag	You all were dancing.	g-gee neem-wahg	Making Simple Sentences (Plural)	2024-11-18 17:43:01.089784-05			7
159	N’gii bmiptomi	We ran.	n-gee bmip-toh-mee	Making Simple Sentences (Plural)	2024-11-18 17:43:01.090259-05			7
160	Wemibigwag wiisinwag	They are drinking and eating.	weh-mih-big-wahg wee-seen-wahg	Making Simple Sentences (Plural)	2024-11-18 17:43:01.090847-05			7
161	Boozhoo	Hello	boozh-hoo	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.580198-05			8
162	Aaniin!	Hey! Hi!	ah-neen	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.581259-05			8
163	_________ ndi-zhinikaaz.	My name is ________.	_____ n-dee zhih-nih-kahz	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.582051-05			8
164	Giin dash, Aaniish e-zhinikaaz-yin?	And you, what is your name?	geen dash ah-neesh eh-zhih-nih-kahz-yin	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.583014-05			8
165	Aaniish ezhi-bimaadziyin?	How is your life?	ah-neesh eh-zhee bih-mahd-zih-yin	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.583655-05			8
166	nMino bimaadis.	I am fine.	n-mee-noh bih-mah-dees	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.584283-05			8
167	Aabiish enji-baayin?	Where are you from?	ah-beesh en-jee bah-yeen	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.58493-05			8
168	________ ndoo-njibaa.	I am from _________.	_____ n-doo n-jee-bah	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.585675-05			8
169	Aabiish endaayin?	Where do you live?	ah-beesh en-dah-yeen	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.586331-05			8
170	________ ndi daa.	I live in _________.	_____ n-dee dah	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.586941-05			8
171	Aabiish enji-nakiiyin?	Where do you work?	ah-beesh en-jee nah-kee-yeen	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.587545-05			8
172	________ ndoonjinakii.	I work at _________.	_____ n-doon-jih-nah-kee	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.588152-05			8
173	nGichi-nendam gii nkweshkwanaa.	I am very happy to have met you.	n-gee-chee nen-dahm gee n-kweh-shkweh-nah	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.588696-05			8
174	nGichi-nendam genii gii nkweshkwanaa.	I am also very happy to have met you.	n-gee-chee nen-dahm geh-nee gee n-kweh-shkweh-nah	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.589232-05			8
175	Gga waabmin miinwaa!	I’ll see you again!	gah wahb-min meen-wah	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.589813-05			8
176	Baa maa pii.	See you later.	bah mah pee	Shki-Nkweshkodaading - Getting Acquainted	2024-11-18 17:44:04.590361-05			8
\.


--
-- Data for Name: cards_deck; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.cards_deck (id, name, description, date_created, is_public, updated_at, owner_id) FROM stdin;
1	November - Freeze-Up Moon	Vocabulary related to November and winter activities in Anishinaabemowin.	2024-11-18 17:05:47.812545-05	t	2024-11-18 17:05:47.812787-05	\N
2	Dagwaagin - Autumn Vocabulary	Vocabulary related to autumn activities and observations in Anishinaabemowin.	2024-11-18 17:21:45.349631-05	t	2024-11-18 17:21:45.349654-05	\N
3	Going to the Fair Talk	Vocabulary related to conversations about going to the fair in Anishinaabemowin.	2024-11-18 17:34:24.663506-05	t	2024-11-18 17:34:24.663532-05	\N
4	Niibin - Summertime Vocabulary	Vocabulary related to summertime activities and observations in Anishinaabemowin.	2024-11-18 17:37:33.508059-05	t	2024-11-18 17:37:33.508086-05	\N
5	What Did You See or Hear?	Vocabulary and phrases for describing what you saw or heard in Anishinaabemowin.	2024-11-18 17:39:45.98157-05	t	2024-11-18 17:39:45.981583-05	\N
6	Asemaa and Manoomin Vocabulary	Vocabulary related to tobacco, rice, and traditional activities in Anishinaabemowin.	2024-11-18 17:41:59.465289-05	t	2024-11-18 17:41:59.46531-05	\N
7	Making Simple Sentences (Plural)	Vocabulary and phrases for creating plural sentences in Anishinaabemowin.	2024-11-18 17:43:01.083025-05	t	2024-11-18 17:43:01.083055-05	\N
8	Shki-Nkweshkodaading - Getting Acquainted	Vocabulary and phrases for getting acquainted in Anishinaabemowin.	2024-11-18 17:44:04.578809-05	t	2024-11-18 17:44:04.578833-05	\N
\.


--
-- Data for Name: cards_deck_tags; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.cards_deck_tags (id, deck_id, tag_id) FROM stdin;
\.


--
-- Data for Name: cards_deckshare; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.cards_deckshare (id, permissions, date_shared, active, deck_id, shared_by_id, shared_with_id) FROM stdin;
\.


--
-- Data for Name: cards_profile; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.cards_profile (id, study_streak, last_study_date, total_cards_studied, created_at, updated_at, preferred_name, user_id) FROM stdin;
1	0	\N	0	2024-11-18 16:47:57.972728-05	2024-11-18 16:47:57.98112-05	Kristine	1
3	0	\N	0	2024-11-18 17:51:12.916224-05	2024-11-18 17:51:58.54998-05	Apollo	3
4	0	\N	0	2024-11-18 18:00:55.657675-05	2024-11-18 18:00:55.66486-05	Jeff	4
5	0	\N	0	2024-11-18 21:20:05.871842-05	2024-11-18 21:35:59.873042-05	Molly	5
2	0	\N	0	2024-11-18 17:49:30.691189-05	2024-11-19 00:32:02.118263-05	Bob	2
\.


--
-- Data for Name: cards_profile_chosen_decks; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.cards_profile_chosen_decks (id, profile_id, deck_id) FROM stdin;
1	1	1
2	1	2
4	4	1
5	4	8
22	2	1
23	2	8
\.


--
-- Data for Name: cards_tag; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.cards_tag (id, name) FROM stdin;
\.


--
-- Data for Name: cards_usercardprogress; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.cards_usercardprogress (id, box_level, last_reviewed, next_review_date, round_completed, card_id, user_id, last_review_result) FROM stdin;
1	1	2024-11-18 17:08:36.669614-05	2024-11-18 17:08:36.668098-05	f	1	1	f
2	1	2024-11-18 17:08:36.669656-05	2024-11-18 17:08:36.668098-05	f	2	1	f
3	1	2024-11-18 17:08:36.669686-05	2024-11-18 17:08:36.668098-05	f	3	1	f
4	1	2024-11-18 17:08:36.669714-05	2024-11-18 17:08:36.668098-05	f	4	1	f
5	1	2024-11-18 17:08:36.669741-05	2024-11-18 17:08:36.668098-05	f	5	1	f
6	1	2024-11-18 17:08:36.669768-05	2024-11-18 17:08:36.668098-05	f	6	1	f
7	1	2024-11-18 17:08:36.669794-05	2024-11-18 17:08:36.668098-05	f	7	1	f
8	1	2024-11-18 17:08:36.66982-05	2024-11-18 17:08:36.668098-05	f	8	1	f
9	1	2024-11-18 17:08:36.669846-05	2024-11-18 17:08:36.668098-05	f	9	1	f
10	1	2024-11-18 17:08:36.669872-05	2024-11-18 17:08:36.668098-05	f	10	1	f
11	1	2024-11-18 17:08:36.669898-05	2024-11-18 17:08:36.668098-05	f	11	1	f
12	1	2024-11-18 17:08:36.669924-05	2024-11-18 17:08:36.668098-05	f	12	1	f
13	1	2024-11-18 17:08:36.669949-05	2024-11-18 17:08:36.668098-05	f	13	1	f
14	1	2024-11-18 17:08:36.669974-05	2024-11-18 17:08:36.668098-05	f	14	1	f
15	1	2024-11-18 17:08:36.67-05	2024-11-18 17:08:36.668098-05	f	15	1	f
16	1	2024-11-18 17:08:36.670025-05	2024-11-18 17:08:36.668098-05	f	16	1	f
17	1	2024-11-18 17:08:36.67005-05	2024-11-18 17:08:36.668098-05	f	17	1	f
18	1	2024-11-18 17:08:36.670076-05	2024-11-18 17:08:36.668098-05	f	18	1	f
19	1	2024-11-18 17:08:36.670102-05	2024-11-18 17:08:36.668098-05	f	19	1	f
20	1	2024-11-18 17:08:36.670127-05	2024-11-18 17:08:36.668098-05	f	20	1	f
21	1	2024-11-18 17:32:22.059673-05	2024-11-18 17:32:22.057043-05	f	21	1	f
22	1	2024-11-18 17:32:22.059721-05	2024-11-18 17:32:22.057043-05	f	22	1	f
23	1	2024-11-18 17:32:22.059751-05	2024-11-18 17:32:22.057043-05	f	23	1	f
24	1	2024-11-18 17:32:22.05978-05	2024-11-18 17:32:22.057043-05	f	24	1	f
25	1	2024-11-18 17:32:22.059808-05	2024-11-18 17:32:22.057043-05	f	25	1	f
26	1	2024-11-18 17:32:22.059835-05	2024-11-18 17:32:22.057043-05	f	26	1	f
27	1	2024-11-18 17:32:22.059862-05	2024-11-18 17:32:22.057043-05	f	27	1	f
28	1	2024-11-18 17:32:22.059888-05	2024-11-18 17:32:22.057043-05	f	28	1	f
29	1	2024-11-18 17:32:22.059915-05	2024-11-18 17:32:22.057043-05	f	29	1	f
30	1	2024-11-18 17:32:22.059942-05	2024-11-18 17:32:22.057043-05	f	30	1	f
31	1	2024-11-18 17:32:22.059969-05	2024-11-18 17:32:22.057043-05	f	31	1	f
32	1	2024-11-18 17:32:22.059996-05	2024-11-18 17:32:22.057043-05	f	32	1	f
33	1	2024-11-18 17:32:22.060021-05	2024-11-18 17:32:22.057043-05	f	33	1	f
34	1	2024-11-18 17:32:22.060047-05	2024-11-18 17:32:22.057043-05	f	34	1	f
35	1	2024-11-18 17:32:22.060072-05	2024-11-18 17:32:22.057043-05	f	35	1	f
36	1	2024-11-18 17:32:22.060099-05	2024-11-18 17:32:22.057043-05	f	36	1	f
37	1	2024-11-18 17:32:22.060124-05	2024-11-18 17:32:22.057043-05	f	37	1	f
38	1	2024-11-18 17:32:22.06015-05	2024-11-18 17:32:22.057043-05	f	38	1	f
39	1	2024-11-18 17:32:22.060175-05	2024-11-18 17:32:22.057043-05	f	39	1	f
40	1	2024-11-18 17:32:22.060201-05	2024-11-18 17:32:22.057043-05	f	40	1	f
41	1	2024-11-18 17:32:22.060227-05	2024-11-18 17:32:22.057043-05	f	41	1	f
42	1	2024-11-18 17:32:22.060253-05	2024-11-18 17:32:22.057043-05	f	42	1	f
43	1	2024-11-18 17:32:22.060279-05	2024-11-18 17:32:22.057043-05	f	43	1	f
44	1	2024-11-18 17:32:22.060305-05	2024-11-18 17:32:22.057043-05	f	44	1	f
45	1	2024-11-18 17:32:22.060331-05	2024-11-18 17:32:22.057043-05	f	45	1	f
46	1	2024-11-18 17:32:22.060358-05	2024-11-18 17:32:22.057043-05	f	46	1	f
47	1	2024-11-18 17:32:22.060384-05	2024-11-18 17:32:22.057043-05	f	47	1	f
48	1	2024-11-18 17:32:22.060411-05	2024-11-18 17:32:22.057043-05	f	48	1	f
49	1	2024-11-18 17:32:22.060437-05	2024-11-18 17:32:22.057043-05	f	49	1	f
50	1	2024-11-18 17:32:22.060463-05	2024-11-18 17:32:22.057043-05	f	50	1	f
51	1	2024-11-18 17:32:22.060489-05	2024-11-18 17:32:22.057043-05	f	51	1	f
52	1	2024-11-18 17:32:22.060515-05	2024-11-18 17:32:22.057043-05	f	52	1	f
53	1	2024-11-18 17:32:22.060906-05	2024-11-18 17:32:22.057043-05	f	53	1	f
54	1	2024-11-18 17:32:22.060941-05	2024-11-18 17:32:22.057043-05	f	54	1	f
55	1	2024-11-18 17:32:22.060968-05	2024-11-18 17:32:22.057043-05	f	55	1	f
56	1	2024-11-18 17:32:22.060993-05	2024-11-18 17:32:22.057043-05	f	56	1	f
57	1	2024-11-18 17:32:22.061019-05	2024-11-18 17:32:22.057043-05	f	57	1	f
58	1	2024-11-18 17:32:22.061045-05	2024-11-18 17:32:22.057043-05	f	58	1	f
59	1	2024-11-18 17:32:22.061071-05	2024-11-18 17:32:22.057043-05	f	59	1	f
60	1	2024-11-18 17:32:22.061096-05	2024-11-18 17:32:22.057043-05	f	60	1	f
61	1	2024-11-18 17:32:22.061122-05	2024-11-18 17:32:22.057043-05	f	61	1	f
62	1	2024-11-18 17:32:22.061149-05	2024-11-18 17:32:22.057043-05	f	62	1	f
63	1	2024-11-18 17:32:22.061174-05	2024-11-18 17:32:22.057043-05	f	63	1	f
64	1	2024-11-18 17:32:22.0612-05	2024-11-18 17:32:22.057043-05	f	64	1	f
65	1	2024-11-18 17:32:22.061225-05	2024-11-18 17:32:22.057043-05	f	65	1	f
66	1	2024-11-18 17:32:22.061251-05	2024-11-18 17:32:22.057043-05	f	66	1	f
67	1	2024-11-18 17:32:22.061276-05	2024-11-18 17:32:22.057043-05	f	67	1	f
68	1	2024-11-18 17:32:22.061301-05	2024-11-18 17:32:22.057043-05	f	68	1	f
79	1	2024-11-18 17:50:29.793858-05	2024-11-18 17:50:29.791209-05	f	11	2	f
80	1	2024-11-18 17:50:29.793885-05	2024-11-18 17:50:29.791209-05	f	12	2	f
81	1	2024-11-18 17:50:29.793913-05	2024-11-18 17:50:29.791209-05	f	13	2	f
82	1	2024-11-18 17:50:29.79394-05	2024-11-18 17:50:29.791209-05	f	14	2	f
83	1	2024-11-18 17:50:29.793968-05	2024-11-18 17:50:29.791209-05	f	15	2	f
84	1	2024-11-18 17:50:29.793996-05	2024-11-18 17:50:29.791209-05	f	16	2	f
85	1	2024-11-18 17:50:29.794023-05	2024-11-18 17:50:29.791209-05	f	17	2	f
86	1	2024-11-18 17:50:29.794051-05	2024-11-18 17:50:29.791209-05	f	18	2	f
87	1	2024-11-18 17:50:29.794079-05	2024-11-18 17:50:29.791209-05	f	19	2	f
88	1	2024-11-18 17:50:29.794107-05	2024-11-18 17:50:29.791209-05	f	20	2	f
70	2	2024-11-18 17:50:29.793563-05	2024-11-20 17:50:40.748245-05	f	2	2	f
71	1	2024-11-18 17:50:29.793602-05	2024-11-19 17:50:51.651222-05	f	3	2	f
72	2	2024-11-18 17:50:29.793639-05	2024-11-20 19:23:50.260832-05	f	4	2	f
73	2	2024-11-18 17:50:29.793676-05	2024-11-20 19:24:59.826276-05	f	5	2	f
74	2	2024-11-18 17:50:29.793715-05	2024-11-20 19:26:21.133952-05	f	6	2	f
75	2	2024-11-18 17:50:29.793749-05	2024-11-20 23:21:33.274001-05	f	7	2	f
76	1	2024-11-18 17:50:29.793775-05	2024-11-20 01:06:31.151785-05	f	8	2	f
77	1	2024-11-18 17:50:29.793803-05	2024-11-20 01:06:32.7136-05	f	9	2	f
78	1	2024-11-18 17:50:29.79383-05	2024-11-20 01:06:33.884772-05	f	10	2	f
69	2	2024-11-18 17:50:29.793503-05	2024-11-20 17:50:37.637935-05	f	1	2	f
106	1	2024-11-18 18:02:14.340808-05	2024-11-18 18:02:14.338128-05	f	18	4	f
107	1	2024-11-18 18:02:14.340834-05	2024-11-18 18:02:14.338128-05	f	19	4	f
108	1	2024-11-18 18:02:14.34086-05	2024-11-18 18:02:14.338128-05	f	20	4	f
109	1	2024-11-18 18:03:02.305787-05	2024-11-18 18:03:02.304451-05	f	161	4	f
110	1	2024-11-18 18:03:02.305824-05	2024-11-18 18:03:02.304451-05	f	162	4	f
111	1	2024-11-18 18:03:02.305854-05	2024-11-18 18:03:02.304451-05	f	163	4	f
112	1	2024-11-18 18:03:02.305882-05	2024-11-18 18:03:02.304451-05	f	164	4	f
113	1	2024-11-18 18:03:02.305912-05	2024-11-18 18:03:02.304451-05	f	165	4	f
114	1	2024-11-18 18:03:02.30594-05	2024-11-18 18:03:02.304451-05	f	166	4	f
115	1	2024-11-18 18:03:02.305968-05	2024-11-18 18:03:02.304451-05	f	167	4	f
116	1	2024-11-18 18:03:02.305996-05	2024-11-18 18:03:02.304451-05	f	168	4	f
117	1	2024-11-18 18:03:02.306024-05	2024-11-18 18:03:02.304451-05	f	169	4	f
118	1	2024-11-18 18:03:02.306055-05	2024-11-18 18:03:02.304451-05	f	170	4	f
119	1	2024-11-18 18:03:02.306083-05	2024-11-18 18:03:02.304451-05	f	171	4	f
120	1	2024-11-18 18:03:02.306111-05	2024-11-18 18:03:02.304451-05	f	172	4	f
121	1	2024-11-18 18:03:02.306139-05	2024-11-18 18:03:02.304451-05	f	173	4	f
122	1	2024-11-18 18:03:02.306167-05	2024-11-18 18:03:02.304451-05	f	174	4	f
123	1	2024-11-18 18:03:02.306195-05	2024-11-18 18:03:02.304451-05	f	175	4	f
124	1	2024-11-18 18:03:02.306223-05	2024-11-18 18:03:02.304451-05	f	176	4	f
89	1	2024-11-18 18:02:14.340344-05	2024-11-19 18:06:04.761071-05	f	1	4	f
90	1	2024-11-18 18:02:14.340382-05	2024-11-19 18:06:30.956205-05	f	2	4	f
91	2	2024-11-18 18:02:14.340412-05	2024-11-20 18:07:07.94746-05	f	3	4	f
92	1	2024-11-18 18:02:14.340439-05	2024-11-19 18:07:18.465851-05	f	4	4	f
93	2	2024-11-18 18:02:14.340466-05	2024-11-20 18:07:25.154066-05	f	5	4	f
94	2	2024-11-18 18:02:14.340493-05	2024-11-20 18:07:31.903416-05	f	6	4	f
95	1	2024-11-18 18:02:14.340519-05	2024-11-19 18:07:41.67495-05	f	7	4	f
96	1	2024-11-18 18:02:14.340545-05	2024-11-19 18:08:01.63043-05	f	8	4	f
97	1	2024-11-18 18:02:14.340572-05	2024-11-19 18:08:11.182864-05	f	9	4	f
98	1	2024-11-18 18:02:14.340599-05	2024-11-19 18:08:20.812561-05	f	10	4	f
99	1	2024-11-18 18:02:14.340625-05	2024-11-19 18:08:27.549534-05	f	11	4	f
100	2	2024-11-18 18:02:14.34065-05	2024-11-20 18:08:37.747487-05	f	12	4	f
101	1	2024-11-18 18:02:14.340676-05	2024-11-19 18:08:45.279824-05	f	13	4	f
102	2	2024-11-18 18:02:14.340702-05	2024-11-20 18:08:50.243925-05	f	14	4	f
103	2	2024-11-18 18:02:14.340728-05	2024-11-20 18:08:55.587322-05	f	15	4	f
104	2	2024-11-18 18:02:14.340754-05	2024-11-20 18:09:04.432606-05	f	16	4	f
105	1	2024-11-18 18:02:14.340781-05	2024-11-19 18:09:10.02312-05	f	17	4	f
133	1	2024-11-18 22:22:26.347441-05	2024-11-18 22:22:26.34481-05	f	169	2	f
134	1	2024-11-18 22:22:26.347468-05	2024-11-18 22:22:26.34481-05	f	170	2	f
135	1	2024-11-18 22:22:26.347494-05	2024-11-18 22:22:26.34481-05	f	171	2	f
136	1	2024-11-18 22:22:26.347519-05	2024-11-18 22:22:26.34481-05	f	172	2	f
137	1	2024-11-18 22:22:26.347546-05	2024-11-18 22:22:26.34481-05	f	173	2	f
138	1	2024-11-18 22:22:26.347571-05	2024-11-18 22:22:26.34481-05	f	174	2	f
139	1	2024-11-18 22:22:26.347597-05	2024-11-18 22:22:26.34481-05	f	175	2	f
140	1	2024-11-18 22:22:26.347623-05	2024-11-18 22:22:26.34481-05	f	176	2	f
141	1	2024-11-18 22:22:29.868034-05	2024-11-18 22:22:29.865286-05	f	128	2	f
142	1	2024-11-18 22:22:29.868088-05	2024-11-18 22:22:29.865286-05	f	129	2	f
143	1	2024-11-18 22:22:29.868126-05	2024-11-18 22:22:29.865286-05	f	130	2	f
144	1	2024-11-18 22:22:29.868218-05	2024-11-18 22:22:29.865286-05	f	131	2	f
145	1	2024-11-18 22:22:29.868318-05	2024-11-18 22:22:29.865286-05	f	132	2	f
146	1	2024-11-18 22:22:29.868358-05	2024-11-18 22:22:29.865286-05	f	133	2	f
147	1	2024-11-18 22:22:29.868396-05	2024-11-18 22:22:29.865286-05	f	134	2	f
148	1	2024-11-18 22:22:29.868434-05	2024-11-18 22:22:29.865286-05	f	135	2	f
149	1	2024-11-18 22:22:29.868471-05	2024-11-18 22:22:29.865286-05	f	136	2	f
150	1	2024-11-18 22:22:29.868509-05	2024-11-18 22:22:29.865286-05	f	137	2	f
151	1	2024-11-18 22:22:29.868547-05	2024-11-18 22:22:29.865286-05	f	138	2	f
152	1	2024-11-18 22:22:29.868583-05	2024-11-18 22:22:29.865286-05	f	139	2	f
153	1	2024-11-18 22:22:29.868611-05	2024-11-18 22:22:29.865286-05	f	140	2	f
154	1	2024-11-18 22:22:29.868639-05	2024-11-18 22:22:29.865286-05	f	141	2	f
155	1	2024-11-18 22:22:29.868666-05	2024-11-18 22:22:29.865286-05	f	142	2	f
156	1	2024-11-18 22:22:29.868743-05	2024-11-18 22:22:29.865286-05	f	143	2	f
157	1	2024-11-18 22:22:29.869371-05	2024-11-18 22:22:29.865286-05	f	144	2	f
158	1	2024-11-18 22:22:29.869419-05	2024-11-18 22:22:29.865286-05	f	145	2	f
125	2	2024-11-18 22:22:26.347211-05	2024-11-20 22:27:52.257659-05	f	161	2	f
126	1	2024-11-18 22:22:26.347254-05	2024-11-19 22:27:54.139309-05	f	162	2	f
127	2	2024-11-18 22:22:26.347284-05	2024-11-20 22:27:57.79301-05	f	163	2	f
128	2	2024-11-18 22:22:26.347312-05	2024-11-20 22:28:08.829259-05	f	164	2	f
129	1	2024-11-18 22:22:26.347338-05	2024-11-19 22:28:18.07167-05	f	165	2	f
130	2	2024-11-18 22:22:26.347365-05	2024-11-20 22:28:32.916276-05	f	166	2	f
131	1	2024-11-18 22:22:26.34739-05	2024-11-19 22:28:44.489553-05	f	167	2	f
132	2	2024-11-18 22:22:26.347416-05	2024-11-20 22:29:02.388664-05	f	168	2	f
159	1	2024-11-18 22:22:29.869447-05	2024-11-18 22:22:29.865286-05	f	146	2	f
160	1	2024-11-18 22:22:29.869473-05	2024-11-18 22:22:29.865286-05	f	147	2	f
161	1	2024-11-18 22:22:29.869499-05	2024-11-18 22:22:29.865286-05	f	148	2	f
162	1	2024-11-18 22:22:29.869524-05	2024-11-18 22:22:29.865286-05	f	149	2	f
163	1	2024-11-18 22:22:29.869549-05	2024-11-18 22:22:29.865286-05	f	150	2	f
164	1	2024-11-18 22:22:32.759214-05	2024-11-18 22:22:32.757079-05	f	83	2	f
165	1	2024-11-18 22:22:32.759253-05	2024-11-18 22:22:32.757079-05	f	84	2	f
166	1	2024-11-18 22:22:32.759283-05	2024-11-18 22:22:32.757079-05	f	85	2	f
167	1	2024-11-18 22:22:32.759312-05	2024-11-18 22:22:32.757079-05	f	86	2	f
168	1	2024-11-18 22:22:32.759341-05	2024-11-18 22:22:32.757079-05	f	87	2	f
169	1	2024-11-18 22:22:32.759368-05	2024-11-18 22:22:32.757079-05	f	88	2	f
170	1	2024-11-18 22:22:32.759394-05	2024-11-18 22:22:32.757079-05	f	89	2	f
171	1	2024-11-18 22:22:32.759421-05	2024-11-18 22:22:32.757079-05	f	90	2	f
172	1	2024-11-18 22:22:32.75946-05	2024-11-18 22:22:32.757079-05	f	91	2	f
173	1	2024-11-18 22:22:32.759488-05	2024-11-18 22:22:32.757079-05	f	92	2	f
174	1	2024-11-18 22:22:32.759513-05	2024-11-18 22:22:32.757079-05	f	93	2	f
175	1	2024-11-18 22:22:32.759539-05	2024-11-18 22:22:32.757079-05	f	94	2	f
176	1	2024-11-18 22:22:32.759564-05	2024-11-18 22:22:32.757079-05	f	95	2	f
177	1	2024-11-18 22:22:32.759589-05	2024-11-18 22:22:32.757079-05	f	96	2	f
178	1	2024-11-18 22:22:32.759614-05	2024-11-18 22:22:32.757079-05	f	97	2	f
179	1	2024-11-18 22:22:32.75964-05	2024-11-18 22:22:32.757079-05	f	98	2	f
180	1	2024-11-18 22:22:32.759665-05	2024-11-18 22:22:32.757079-05	f	99	2	f
181	1	2024-11-18 22:22:32.75969-05	2024-11-18 22:22:32.757079-05	f	100	2	f
182	1	2024-11-18 22:22:32.759715-05	2024-11-18 22:22:32.757079-05	f	101	2	f
183	1	2024-11-18 22:22:32.759741-05	2024-11-18 22:22:32.757079-05	f	102	2	f
184	1	2024-11-18 22:22:32.759766-05	2024-11-18 22:22:32.757079-05	f	103	2	f
185	1	2024-11-18 22:22:32.759791-05	2024-11-18 22:22:32.757079-05	f	104	2	f
186	1	2024-11-18 22:22:32.759816-05	2024-11-18 22:22:32.757079-05	f	105	2	f
187	1	2024-11-18 22:22:32.75984-05	2024-11-18 22:22:32.757079-05	f	106	2	f
202	1	2024-11-18 22:29:28.848237-05	2024-11-18 22:29:28.844315-05	f	107	2	f
203	1	2024-11-18 22:29:28.848305-05	2024-11-18 22:29:28.844315-05	f	108	2	f
204	1	2024-11-18 22:29:28.848342-05	2024-11-18 22:29:28.844315-05	f	109	2	f
205	1	2024-11-18 22:29:28.848379-05	2024-11-18 22:29:28.844315-05	f	110	2	f
206	1	2024-11-18 22:29:28.848415-05	2024-11-18 22:29:28.844315-05	f	111	2	f
207	1	2024-11-18 22:29:28.848454-05	2024-11-18 22:29:28.844315-05	f	112	2	f
208	1	2024-11-18 22:29:28.848497-05	2024-11-18 22:29:28.844315-05	f	113	2	f
209	1	2024-11-18 22:29:28.848535-05	2024-11-18 22:29:28.844315-05	f	114	2	f
210	1	2024-11-18 22:29:28.848573-05	2024-11-18 22:29:28.844315-05	f	115	2	f
211	1	2024-11-18 22:29:28.848631-05	2024-11-18 22:29:28.844315-05	f	116	2	f
212	1	2024-11-18 22:29:28.84867-05	2024-11-18 22:29:28.844315-05	f	117	2	f
213	1	2024-11-18 22:29:28.848708-05	2024-11-18 22:29:28.844315-05	f	118	2	f
214	1	2024-11-18 22:29:28.848746-05	2024-11-18 22:29:28.844315-05	f	119	2	f
215	1	2024-11-18 22:29:28.848786-05	2024-11-18 22:29:28.844315-05	f	120	2	f
216	1	2024-11-18 22:29:28.848823-05	2024-11-18 22:29:28.844315-05	f	121	2	f
217	1	2024-11-18 22:29:28.84886-05	2024-11-18 22:29:28.844315-05	f	122	2	f
218	1	2024-11-18 22:29:28.848897-05	2024-11-18 22:29:28.844315-05	f	123	2	f
219	1	2024-11-18 22:29:28.848946-05	2024-11-18 22:29:28.844315-05	f	124	2	f
220	1	2024-11-18 22:29:28.848995-05	2024-11-18 22:29:28.844315-05	f	125	2	f
221	1	2024-11-18 22:29:28.849042-05	2024-11-18 22:29:28.844315-05	f	126	2	f
222	1	2024-11-18 22:29:28.849081-05	2024-11-18 22:29:28.844315-05	f	127	2	f
223	1	2024-11-18 22:33:24.07786-05	2024-11-18 22:33:24.075505-05	f	128	2	f
224	1	2024-11-18 22:33:24.07792-05	2024-11-18 22:33:24.075505-05	f	129	2	f
225	1	2024-11-18 22:33:24.077957-05	2024-11-18 22:33:24.075505-05	f	130	2	f
226	1	2024-11-18 22:33:24.078009-05	2024-11-18 22:33:24.075505-05	f	131	2	f
227	1	2024-11-18 22:33:24.078046-05	2024-11-18 22:33:24.075505-05	f	132	2	f
228	1	2024-11-18 22:33:24.078088-05	2024-11-18 22:33:24.075505-05	f	133	2	f
229	1	2024-11-18 22:33:24.078127-05	2024-11-18 22:33:24.075505-05	f	134	2	f
230	1	2024-11-18 22:33:24.078164-05	2024-11-18 22:33:24.075505-05	f	135	2	f
231	1	2024-11-18 22:33:24.078202-05	2024-11-18 22:33:24.075505-05	f	136	2	f
232	1	2024-11-18 22:33:24.078242-05	2024-11-18 22:33:24.075505-05	f	137	2	f
233	1	2024-11-18 22:33:24.078283-05	2024-11-18 22:33:24.075505-05	f	138	2	f
234	1	2024-11-18 22:33:24.078322-05	2024-11-18 22:33:24.075505-05	f	139	2	f
235	1	2024-11-18 22:33:24.078382-05	2024-11-18 22:33:24.075505-05	f	140	2	f
236	1	2024-11-18 22:33:24.078449-05	2024-11-18 22:33:24.075505-05	f	141	2	f
237	1	2024-11-18 22:33:24.078527-05	2024-11-18 22:33:24.075505-05	f	142	2	f
238	1	2024-11-18 22:33:24.07857-05	2024-11-18 22:33:24.075505-05	f	143	2	f
239	1	2024-11-18 22:33:24.078619-05	2024-11-18 22:33:24.075505-05	f	144	2	f
240	1	2024-11-18 22:33:24.0787-05	2024-11-18 22:33:24.075505-05	f	145	2	f
241	1	2024-11-18 22:33:24.07875-05	2024-11-18 22:33:24.075505-05	f	146	2	f
242	1	2024-11-18 22:33:24.078803-05	2024-11-18 22:33:24.075505-05	f	147	2	f
243	1	2024-11-18 22:33:24.078851-05	2024-11-18 22:33:24.075505-05	f	148	2	f
244	1	2024-11-18 22:33:24.078888-05	2024-11-18 22:33:24.075505-05	f	149	2	f
245	1	2024-11-18 22:33:24.078925-05	2024-11-18 22:33:24.075505-05	f	150	2	f
246	1	2024-11-18 22:35:17.933423-05	2024-11-18 22:35:17.931011-05	f	161	2	f
189	2	2024-11-18 22:22:34.707711-05	2024-11-20 22:56:46.528898-05	f	70	2	f
190	1	2024-11-18 22:22:34.707749-05	2024-11-19 22:56:48.575138-05	f	71	2	f
191	2	2024-11-18 22:22:34.707788-05	2024-11-20 22:56:51.051421-05	f	72	2	f
192	2	2024-11-18 22:22:34.707831-05	2024-11-20 23:11:51.189531-05	f	73	2	f
193	2	2024-11-18 22:22:34.707873-05	2024-11-20 23:11:54.038837-05	f	74	2	f
194	2	2024-11-18 22:22:34.707912-05	2024-11-20 23:11:56.304541-05	f	75	2	f
195	2	2024-11-18 22:22:34.707951-05	2024-11-20 23:11:58.659493-05	f	76	2	f
196	2	2024-11-18 22:22:34.707987-05	2024-11-20 23:18:40.271352-05	f	77	2	f
197	2	2024-11-18 22:22:34.708028-05	2024-11-20 23:18:42.122827-05	f	78	2	f
198	2	2024-11-18 22:22:34.708075-05	2024-11-20 23:18:43.774196-05	f	79	2	f
199	2	2024-11-18 22:22:34.708114-05	2024-11-20 23:18:44.925779-05	f	80	2	f
200	2	2024-11-18 22:22:34.708153-05	2024-11-20 23:18:46.319224-05	f	81	2	f
201	2	2024-11-18 22:22:34.708194-05	2024-11-20 23:18:47.587027-05	f	82	2	f
247	1	2024-11-18 22:35:17.933481-05	2024-11-18 22:35:17.931011-05	f	162	2	f
248	1	2024-11-18 22:35:17.933566-05	2024-11-18 22:35:17.931011-05	f	163	2	f
249	1	2024-11-18 22:35:17.93365-05	2024-11-18 22:35:17.931011-05	f	164	2	f
250	1	2024-11-18 22:35:17.933691-05	2024-11-18 22:35:17.931011-05	f	165	2	f
251	1	2024-11-18 22:35:17.933729-05	2024-11-18 22:35:17.931011-05	f	166	2	f
252	1	2024-11-18 22:35:17.933768-05	2024-11-18 22:35:17.931011-05	f	167	2	f
253	1	2024-11-18 22:35:17.933806-05	2024-11-18 22:35:17.931011-05	f	168	2	f
254	1	2024-11-18 22:35:17.933857-05	2024-11-18 22:35:17.931011-05	f	169	2	f
255	1	2024-11-18 22:35:17.933911-05	2024-11-18 22:35:17.931011-05	f	170	2	f
256	1	2024-11-18 22:35:17.933981-05	2024-11-18 22:35:17.931011-05	f	171	2	f
257	1	2024-11-18 22:35:17.934024-05	2024-11-18 22:35:17.931011-05	f	172	2	f
258	1	2024-11-18 22:35:17.934063-05	2024-11-18 22:35:17.931011-05	f	173	2	f
259	1	2024-11-18 22:35:17.934101-05	2024-11-18 22:35:17.931011-05	f	174	2	f
260	1	2024-11-18 22:35:17.934138-05	2024-11-18 22:35:17.931011-05	f	175	2	f
261	1	2024-11-18 22:35:17.934175-05	2024-11-18 22:35:17.931011-05	f	176	2	f
262	1	2024-11-18 22:46:05.512368-05	2024-11-18 22:46:05.510085-05	f	161	2	f
263	1	2024-11-18 22:46:05.512453-05	2024-11-18 22:46:05.510085-05	f	162	2	f
264	1	2024-11-18 22:46:05.512504-05	2024-11-18 22:46:05.510085-05	f	163	2	f
265	1	2024-11-18 22:46:05.512543-05	2024-11-18 22:46:05.510085-05	f	164	2	f
266	1	2024-11-18 22:46:05.512581-05	2024-11-18 22:46:05.510085-05	f	165	2	f
267	1	2024-11-18 22:46:05.512619-05	2024-11-18 22:46:05.510085-05	f	166	2	f
268	1	2024-11-18 22:46:05.512657-05	2024-11-18 22:46:05.510085-05	f	167	2	f
269	1	2024-11-18 22:46:05.512695-05	2024-11-18 22:46:05.510085-05	f	168	2	f
270	1	2024-11-18 22:46:05.512759-05	2024-11-18 22:46:05.510085-05	f	169	2	f
271	1	2024-11-18 22:46:05.512895-05	2024-11-18 22:46:05.510085-05	f	170	2	f
272	1	2024-11-18 22:46:05.512941-05	2024-11-18 22:46:05.510085-05	f	171	2	f
273	1	2024-11-18 22:46:05.51298-05	2024-11-18 22:46:05.510085-05	f	172	2	f
274	1	2024-11-18 22:46:05.513018-05	2024-11-18 22:46:05.510085-05	f	173	2	f
275	1	2024-11-18 22:46:05.513056-05	2024-11-18 22:46:05.510085-05	f	174	2	f
276	1	2024-11-18 22:46:05.513099-05	2024-11-18 22:46:05.510085-05	f	175	2	f
277	1	2024-11-18 22:46:05.513137-05	2024-11-18 22:46:05.510085-05	f	176	2	f
188	1	2024-11-18 22:22:34.707653-05	2024-11-19 22:56:41.369642-05	f	69	2	f
292	1	2024-11-18 22:58:49.102167-05	2024-11-18 22:58:49.099141-05	f	161	2	f
293	1	2024-11-18 22:58:49.10223-05	2024-11-18 22:58:49.099141-05	f	162	2	f
294	1	2024-11-18 22:58:49.102267-05	2024-11-18 22:58:49.099141-05	f	163	2	f
295	1	2024-11-18 22:58:49.102304-05	2024-11-18 22:58:49.099141-05	f	164	2	f
296	1	2024-11-18 22:58:49.10234-05	2024-11-18 22:58:49.099141-05	f	165	2	f
297	1	2024-11-18 22:58:49.102376-05	2024-11-18 22:58:49.099141-05	f	166	2	f
298	1	2024-11-18 22:58:49.102411-05	2024-11-18 22:58:49.099141-05	f	167	2	f
299	1	2024-11-18 22:58:49.102446-05	2024-11-18 22:58:49.099141-05	f	168	2	f
300	1	2024-11-18 22:58:49.10248-05	2024-11-18 22:58:49.099141-05	f	169	2	f
301	1	2024-11-18 22:58:49.102527-05	2024-11-18 22:58:49.099141-05	f	170	2	f
302	1	2024-11-18 22:58:49.102574-05	2024-11-18 22:58:49.099141-05	f	171	2	f
303	1	2024-11-18 22:58:49.102618-05	2024-11-18 22:58:49.099141-05	f	172	2	f
304	1	2024-11-18 22:58:49.102655-05	2024-11-18 22:58:49.099141-05	f	173	2	f
305	1	2024-11-18 22:58:49.102693-05	2024-11-18 22:58:49.099141-05	f	174	2	f
306	1	2024-11-18 22:58:49.102729-05	2024-11-18 22:58:49.099141-05	f	175	2	f
307	1	2024-11-18 22:58:49.102765-05	2024-11-18 22:58:49.099141-05	f	176	2	f
308	1	2024-11-18 23:05:37.822044-05	2024-11-18 23:05:37.820232-05	f	161	2	f
309	1	2024-11-18 23:05:37.822104-05	2024-11-18 23:05:37.820232-05	f	162	2	f
310	1	2024-11-18 23:05:37.822137-05	2024-11-18 23:05:37.820232-05	f	163	2	f
311	1	2024-11-18 23:05:37.822169-05	2024-11-18 23:05:37.820232-05	f	164	2	f
312	1	2024-11-18 23:05:37.822215-05	2024-11-18 23:05:37.820232-05	f	165	2	f
313	1	2024-11-18 23:05:37.822252-05	2024-11-18 23:05:37.820232-05	f	166	2	f
314	1	2024-11-18 23:05:37.822287-05	2024-11-18 23:05:37.820232-05	f	167	2	f
315	1	2024-11-18 23:05:37.822321-05	2024-11-18 23:05:37.820232-05	f	168	2	f
316	1	2024-11-18 23:05:37.822356-05	2024-11-18 23:05:37.820232-05	f	169	2	f
317	1	2024-11-18 23:05:37.822391-05	2024-11-18 23:05:37.820232-05	f	170	2	f
318	1	2024-11-18 23:05:37.822434-05	2024-11-18 23:05:37.820232-05	f	171	2	f
319	1	2024-11-18 23:05:37.822469-05	2024-11-18 23:05:37.820232-05	f	172	2	f
320	1	2024-11-18 23:05:37.822505-05	2024-11-18 23:05:37.820232-05	f	173	2	f
321	1	2024-11-18 23:05:37.82254-05	2024-11-18 23:05:37.820232-05	f	174	2	f
322	1	2024-11-18 23:05:37.822578-05	2024-11-18 23:05:37.820232-05	f	175	2	f
323	1	2024-11-18 23:05:37.822612-05	2024-11-18 23:05:37.820232-05	f	176	2	f
324	1	2024-11-18 23:10:36.629333-05	2024-11-18 23:10:36.627325-05	f	161	2	f
325	1	2024-11-18 23:10:36.629393-05	2024-11-18 23:10:36.627325-05	f	162	2	f
326	1	2024-11-18 23:10:36.629432-05	2024-11-18 23:10:36.627325-05	f	163	2	f
327	1	2024-11-18 23:10:36.629469-05	2024-11-18 23:10:36.627325-05	f	164	2	f
328	1	2024-11-18 23:10:36.629505-05	2024-11-18 23:10:36.627325-05	f	165	2	f
329	1	2024-11-18 23:10:36.629548-05	2024-11-18 23:10:36.627325-05	f	166	2	f
330	1	2024-11-18 23:10:36.629597-05	2024-11-18 23:10:36.627325-05	f	167	2	f
331	1	2024-11-18 23:10:36.629647-05	2024-11-18 23:10:36.627325-05	f	168	2	f
332	1	2024-11-18 23:10:36.629698-05	2024-11-18 23:10:36.627325-05	f	169	2	f
333	1	2024-11-18 23:10:36.629748-05	2024-11-18 23:10:36.627325-05	f	170	2	f
279	2	2024-11-18 22:49:27.274669-05	2024-11-20 23:18:49.671813-05	f	70	2	f
280	2	2024-11-18 22:49:27.274699-05	2024-11-20 23:18:51.124879-05	f	71	2	f
281	2	2024-11-18 22:49:27.274726-05	2024-11-20 23:18:52.422956-05	f	72	2	f
282	2	2024-11-18 22:49:27.274753-05	2024-11-20 23:18:53.640197-05	f	73	2	f
283	2	2024-11-18 22:49:27.27478-05	2024-11-20 23:18:54.578144-05	f	74	2	f
284	2	2024-11-18 22:49:27.274806-05	2024-11-20 23:18:55.66242-05	f	75	2	f
285	2	2024-11-18 22:49:27.274833-05	2024-11-20 23:18:56.736366-05	f	76	2	f
286	2	2024-11-18 22:49:27.27486-05	2024-11-20 23:18:57.858285-05	f	77	2	f
287	2	2024-11-18 22:49:27.274887-05	2024-11-20 23:18:59.288889-05	f	78	2	f
288	2	2024-11-18 22:49:27.274914-05	2024-11-20 23:19:00.514102-05	f	79	2	f
289	1	2024-11-18 22:49:27.27494-05	2024-11-19 23:19:01.993943-05	f	80	2	f
290	1	2024-11-18 22:49:27.274967-05	2024-11-19 23:19:03.299142-05	f	81	2	f
291	1	2024-11-18 22:49:27.274993-05	2024-11-19 23:19:04.830158-05	f	82	2	f
334	1	2024-11-18 23:10:36.629799-05	2024-11-18 23:10:36.627325-05	f	171	2	f
335	1	2024-11-18 23:10:36.629849-05	2024-11-18 23:10:36.627325-05	f	172	2	f
336	1	2024-11-18 23:10:36.629898-05	2024-11-18 23:10:36.627325-05	f	173	2	f
337	1	2024-11-18 23:10:36.629948-05	2024-11-18 23:10:36.627325-05	f	174	2	f
338	1	2024-11-18 23:10:36.629998-05	2024-11-18 23:10:36.627325-05	f	175	2	f
339	1	2024-11-18 23:10:36.630055-05	2024-11-18 23:10:36.627325-05	f	176	2	f
278	2	2024-11-18 22:49:27.274627-05	2024-11-20 23:18:48.625576-05	f	69	2	f
340	1	2024-11-18 23:19:26.680739-05	2024-11-18 23:19:26.674918-05	f	21	2	f
341	1	2024-11-18 23:19:26.680788-05	2024-11-18 23:19:26.674918-05	f	22	2	f
342	1	2024-11-18 23:19:26.680818-05	2024-11-18 23:19:26.674918-05	f	23	2	f
343	1	2024-11-18 23:19:26.680847-05	2024-11-18 23:19:26.674918-05	f	24	2	f
344	1	2024-11-18 23:19:26.680876-05	2024-11-18 23:19:26.674918-05	f	25	2	f
345	1	2024-11-18 23:19:26.680904-05	2024-11-18 23:19:26.674918-05	f	26	2	f
346	1	2024-11-18 23:19:26.680934-05	2024-11-18 23:19:26.674918-05	f	27	2	f
347	1	2024-11-18 23:19:26.680963-05	2024-11-18 23:19:26.674918-05	f	28	2	f
348	1	2024-11-18 23:19:26.680992-05	2024-11-18 23:19:26.674918-05	f	29	2	f
349	1	2024-11-18 23:19:26.681021-05	2024-11-18 23:19:26.674918-05	f	30	2	f
350	1	2024-11-18 23:19:26.68105-05	2024-11-18 23:19:26.674918-05	f	31	2	f
351	1	2024-11-18 23:19:26.681079-05	2024-11-18 23:19:26.674918-05	f	32	2	f
352	1	2024-11-18 23:19:26.681108-05	2024-11-18 23:19:26.674918-05	f	33	2	f
353	1	2024-11-18 23:19:26.681136-05	2024-11-18 23:19:26.674918-05	f	34	2	f
354	1	2024-11-18 23:19:26.681164-05	2024-11-18 23:19:26.674918-05	f	35	2	f
355	1	2024-11-18 23:19:26.681192-05	2024-11-18 23:19:26.674918-05	f	36	2	f
356	1	2024-11-18 23:19:26.68122-05	2024-11-18 23:19:26.674918-05	f	37	2	f
357	1	2024-11-18 23:19:26.681249-05	2024-11-18 23:19:26.674918-05	f	38	2	f
358	1	2024-11-18 23:19:26.681277-05	2024-11-18 23:19:26.674918-05	f	39	2	f
359	1	2024-11-18 23:19:26.681307-05	2024-11-18 23:19:26.674918-05	f	40	2	f
360	1	2024-11-18 23:19:26.681371-05	2024-11-18 23:19:26.674918-05	f	41	2	f
361	1	2024-11-18 23:19:26.681401-05	2024-11-18 23:19:26.674918-05	f	42	2	f
362	1	2024-11-18 23:19:26.68143-05	2024-11-18 23:19:26.674918-05	f	43	2	f
363	1	2024-11-18 23:19:26.681458-05	2024-11-18 23:19:26.674918-05	f	44	2	f
364	1	2024-11-18 23:19:26.681488-05	2024-11-18 23:19:26.674918-05	f	45	2	f
365	1	2024-11-18 23:19:26.681517-05	2024-11-18 23:19:26.674918-05	f	46	2	f
366	1	2024-11-18 23:19:26.681545-05	2024-11-18 23:19:26.674918-05	f	47	2	f
367	1	2024-11-18 23:19:26.681574-05	2024-11-18 23:19:26.674918-05	f	48	2	f
368	1	2024-11-18 23:19:26.681602-05	2024-11-18 23:19:26.674918-05	f	49	2	f
369	1	2024-11-18 23:19:26.68163-05	2024-11-18 23:19:26.674918-05	f	50	2	f
370	1	2024-11-18 23:19:26.681659-05	2024-11-18 23:19:26.674918-05	f	51	2	f
371	1	2024-11-18 23:19:26.681688-05	2024-11-18 23:19:26.674918-05	f	52	2	f
372	1	2024-11-18 23:19:26.681718-05	2024-11-18 23:19:26.674918-05	f	53	2	f
373	1	2024-11-18 23:19:26.681748-05	2024-11-18 23:19:26.674918-05	f	54	2	f
374	1	2024-11-18 23:19:26.681777-05	2024-11-18 23:19:26.674918-05	f	55	2	f
375	1	2024-11-18 23:19:26.681808-05	2024-11-18 23:19:26.674918-05	f	56	2	f
376	1	2024-11-18 23:19:26.681838-05	2024-11-18 23:19:26.674918-05	f	57	2	f
377	1	2024-11-18 23:19:26.681866-05	2024-11-18 23:19:26.674918-05	f	58	2	f
378	1	2024-11-18 23:19:26.682354-05	2024-11-18 23:19:26.674918-05	f	59	2	f
379	1	2024-11-18 23:19:26.682401-05	2024-11-18 23:19:26.674918-05	f	60	2	f
380	1	2024-11-18 23:19:26.68244-05	2024-11-18 23:19:26.674918-05	f	61	2	f
381	1	2024-11-18 23:19:26.682479-05	2024-11-18 23:19:26.674918-05	f	62	2	f
382	1	2024-11-18 23:19:26.682516-05	2024-11-18 23:19:26.674918-05	f	63	2	f
383	1	2024-11-18 23:19:26.682553-05	2024-11-18 23:19:26.674918-05	f	64	2	f
384	1	2024-11-18 23:19:26.682591-05	2024-11-18 23:19:26.674918-05	f	65	2	f
385	1	2024-11-18 23:19:26.682628-05	2024-11-18 23:19:26.674918-05	f	66	2	f
386	1	2024-11-18 23:19:26.682666-05	2024-11-18 23:19:26.674918-05	f	67	2	f
387	1	2024-11-18 23:19:26.682705-05	2024-11-18 23:19:26.674918-05	f	68	2	f
\.


--
-- Data for Name: cards_userdeck; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.cards_userdeck (id, date_added, is_owner, deck_id, user_id) FROM stdin;
1	2024-11-18 17:08:38.232443-05	f	1	1
2	2024-11-18 17:50:31.578463-05	f	1	2
3	2024-11-18 18:02:32.603712-05	f	1	4
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	cards	card
8	cards	deck
9	cards	tag
10	cards	userdeck
11	cards	usercardprogress
12	cards	profile
13	cards	deckshare
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2024-11-18 16:43:01.57509-05
2	auth	0001_initial	2024-11-18 16:43:01.631636-05
3	admin	0001_initial	2024-11-18 16:43:01.641885-05
4	admin	0002_logentry_remove_auto_add	2024-11-18 16:43:01.65569-05
5	admin	0003_logentry_add_action_flag_choices	2024-11-18 16:43:01.69454-05
6	contenttypes	0002_remove_content_type_name	2024-11-18 16:43:01.708508-05
7	auth	0002_alter_permission_name_max_length	2024-11-18 16:43:01.713792-05
8	auth	0003_alter_user_email_max_length	2024-11-18 16:43:01.718492-05
9	auth	0004_alter_user_username_opts	2024-11-18 16:43:01.722553-05
10	auth	0005_alter_user_last_login_null	2024-11-18 16:43:01.726362-05
11	auth	0006_require_contenttypes_0002	2024-11-18 16:43:01.727926-05
12	auth	0007_alter_validators_add_error_messages	2024-11-18 16:43:01.732913-05
13	auth	0008_alter_user_username_max_length	2024-11-18 16:43:01.741474-05
14	auth	0009_alter_user_last_name_max_length	2024-11-18 16:43:01.745533-05
15	auth	0010_alter_group_name_max_length	2024-11-18 16:43:01.751288-05
16	auth	0011_update_proxy_permissions	2024-11-18 16:43:01.754854-05
17	auth	0012_alter_user_first_name_max_length	2024-11-18 16:43:01.758274-05
18	cards	0001_initial	2024-11-18 16:43:01.914008-05
19	cards	0002_remove_profile_decks_in_curriculum_and_more	2024-11-18 16:43:01.930937-05
20	cards	0003_alter_usercardprogress_options_and_more	2024-11-18 16:43:02.132591-05
21	cards	0004_usercardprogress_last_review_result	2024-11-18 16:43:02.138273-05
22	cards	0005_alter_card_deck	2024-11-18 16:43:02.144774-05
23	sessions	0001_initial	2024-11-18 16:43:02.154916-05
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
4zinpxlzan6qomcl5t0ci13ay25kxb96	.eJxVjEEOwiAQRe_C2hBpClNcuvcMZIZhWrSBpLQr491tky50-9_7760CbusUtpaWkFndlFWX340wvlI5AD-xjFXHWtYlkz4UfdKmH5XTfD_dv8CEbdrfAgAkBGBMTMkxWt8xRPKGDYgZBjDd1fUU0VnHsZeeBvFMYIUsgd-jkpe2hrmOuaib4NzS5wut0D_a:1tDE5n:LkxJ-oykvhYKyIph0jpVfl0yWjXIaUZYbw7C0fVTkeE	2024-12-02 21:35:51.714751-05
\.


--
-- Data for Name: temp_json_import; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.temp_json_import (data) FROM stdin;
\.


--
-- Data for Name: vocabulary; Type: TABLE DATA; Schema: public; Owner: kristinejohnson
--

COPY public.vocabulary (id, data) FROM stdin;
1	{"name": "November - Freeze-Up Moon", "cards": [{"english": "Freeze Up Moon (November)", "pronunciation": "gsh-kah-din d-bihk gee-zis", "anishinaabemowin": "Gshkadin dbik giizis"}, {"english": "Ghost feast", "pronunciation": "jee-bay wee-kwan-dih-win", "anishinaabemowin": "Jiibay wiikwandiwin"}, {"english": "A feast (Invite people together)", "pronunciation": "mawn-jee-weh-win", "anishinaabemowin": "Maawnjiwewin"}, {"english": "Frozen solid", "pronunciation": "msh-kah-wahk-din", "anishinaabemowin": "Mshkawaakdin"}, {"english": "Ice", "pronunciation": "m-kohm", "anishinaabemowin": "Mkom"}, {"english": "Icicle or ice cube", "pronunciation": "m-kohm-ee-ns", "anishinaabemowin": "Mkomiins"}, {"english": "I am cold", "pronunciation": "n-beeng-etch", "anishinaabemowin": "N’biingech"}, {"english": "I am warm", "pronunciation": "n-gee-zhoos", "anishinaabemowin": "N’giizhoos"}, {"english": "It is cold outside", "pronunciation": "g-sih-nah", "anishinaabemowin": "Gsinaa"}, {"english": "Stormy weather", "pronunciation": "n-chee-waht", "anishinaabemowin": "Nchiiwat"}, {"english": "Windy", "pronunciation": "noh-din", "anishinaabemowin": "Noodin"}, {"english": "It is VERY cold outside", "pronunciation": "g-chee g-sih-nah", "anishinaabemowin": "Gchi-Gsinaa"}, {"english": "It is VERY stormy", "pronunciation": "g-chee n-chee-waht", "anishinaabemowin": "Gchi-Nchiiwat"}, {"english": "It is VERY windy", "pronunciation": "g-chee noh-din", "anishinaabemowin": "Gchi-Noodin"}, {"english": "Snow on the ground", "pronunciation": "goh-n", "anishinaabemowin": "Goon"}, {"english": "A lot of snow on the ground", "pronunciation": "gohn-kah", "anishinaabemowin": "Goonkaa"}, {"english": "He/She Builds a fire", "pronunciation": "boo-dweh", "anishinaabemowin": "Boodwe"}, {"english": "He/She Hunts", "pronunciation": "gee-w-seh", "anishinaabemowin": "Giiwse"}, {"english": "I am Deer hunting", "pronunciation": "n-wah-wahsh-keh-shee gee-w-seh", "anishinaabemowin": "N’Waawaashkeshi-giiwse"}, {"english": "I am Turkey hunting", "pronunciation": "n-mih-zih-seh gee-w-seh", "anishinaabemowin": "N’Mizise-giiwse"}], "is_public": true, "description": "Vocabulary related to November and winter activities in Anishinaabemowin."}
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 52, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 5, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: cards_card_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.cards_card_id_seq', 176, true);


--
-- Name: cards_deck_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.cards_deck_id_seq', 8, true);


--
-- Name: cards_deck_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.cards_deck_tags_id_seq', 1, false);


--
-- Name: cards_deckshare_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.cards_deckshare_id_seq', 1, false);


--
-- Name: cards_profile_chosen_decks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.cards_profile_chosen_decks_id_seq', 23, true);


--
-- Name: cards_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.cards_profile_id_seq', 5, true);


--
-- Name: cards_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.cards_tag_id_seq', 1, false);


--
-- Name: cards_usercardprogress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.cards_usercardprogress_id_seq', 387, true);


--
-- Name: cards_userdeck_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.cards_userdeck_id_seq', 3, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 13, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 23, true);


--
-- Name: vocabulary_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kristinejohnson
--

SELECT pg_catalog.setval('public.vocabulary_id_seq', 1, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: cards_card cards_card_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_card
    ADD CONSTRAINT cards_card_pkey PRIMARY KEY (id);


--
-- Name: cards_deck cards_deck_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deck
    ADD CONSTRAINT cards_deck_pkey PRIMARY KEY (id);


--
-- Name: cards_deck_tags cards_deck_tags_deck_id_tag_id_0a407350_uniq; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deck_tags
    ADD CONSTRAINT cards_deck_tags_deck_id_tag_id_0a407350_uniq UNIQUE (deck_id, tag_id);


--
-- Name: cards_deck_tags cards_deck_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deck_tags
    ADD CONSTRAINT cards_deck_tags_pkey PRIMARY KEY (id);


--
-- Name: cards_deckshare cards_deckshare_deck_id_shared_with_id_9607d8b3_uniq; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deckshare
    ADD CONSTRAINT cards_deckshare_deck_id_shared_with_id_9607d8b3_uniq UNIQUE (deck_id, shared_with_id);


--
-- Name: cards_deckshare cards_deckshare_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deckshare
    ADD CONSTRAINT cards_deckshare_pkey PRIMARY KEY (id);


--
-- Name: cards_profile_chosen_decks cards_profile_chosen_decks_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_profile_chosen_decks
    ADD CONSTRAINT cards_profile_chosen_decks_pkey PRIMARY KEY (id);


--
-- Name: cards_profile_chosen_decks cards_profile_chosen_decks_profile_id_deck_id_291dd4e5_uniq; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_profile_chosen_decks
    ADD CONSTRAINT cards_profile_chosen_decks_profile_id_deck_id_291dd4e5_uniq UNIQUE (profile_id, deck_id);


--
-- Name: cards_profile cards_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_profile
    ADD CONSTRAINT cards_profile_pkey PRIMARY KEY (id);


--
-- Name: cards_profile cards_profile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_profile
    ADD CONSTRAINT cards_profile_user_id_key UNIQUE (user_id);


--
-- Name: cards_tag cards_tag_name_key; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_tag
    ADD CONSTRAINT cards_tag_name_key UNIQUE (name);


--
-- Name: cards_tag cards_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_tag
    ADD CONSTRAINT cards_tag_pkey PRIMARY KEY (id);


--
-- Name: cards_usercardprogress cards_usercardprogress_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_usercardprogress
    ADD CONSTRAINT cards_usercardprogress_pkey PRIMARY KEY (id);


--
-- Name: cards_userdeck cards_userdeck_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_userdeck
    ADD CONSTRAINT cards_userdeck_pkey PRIMARY KEY (id);


--
-- Name: cards_userdeck cards_userdeck_user_id_deck_id_a74c70a0_uniq; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_userdeck
    ADD CONSTRAINT cards_userdeck_user_id_deck_id_a74c70a0_uniq UNIQUE (user_id, deck_id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: vocabulary vocabulary_pkey; Type: CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.vocabulary
    ADD CONSTRAINT vocabulary_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: cards_card_deck_id_679b88fe; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_card_deck_id_679b88fe ON public.cards_card USING btree (deck_id);


--
-- Name: cards_deck_owner_id_1187f16f; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_deck_owner_id_1187f16f ON public.cards_deck USING btree (owner_id);


--
-- Name: cards_deck_tags_deck_id_788a8319; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_deck_tags_deck_id_788a8319 ON public.cards_deck_tags USING btree (deck_id);


--
-- Name: cards_deck_tags_tag_id_41991297; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_deck_tags_tag_id_41991297 ON public.cards_deck_tags USING btree (tag_id);


--
-- Name: cards_decks_deck_id_18488e_idx; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_decks_deck_id_18488e_idx ON public.cards_deckshare USING btree (deck_id, active);


--
-- Name: cards_decks_shared__e4493b_idx; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_decks_shared__e4493b_idx ON public.cards_deckshare USING btree (shared_with_id, active);


--
-- Name: cards_deckshare_deck_id_9a7c88e6; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_deckshare_deck_id_9a7c88e6 ON public.cards_deckshare USING btree (deck_id);


--
-- Name: cards_deckshare_shared_by_id_baf25f4b; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_deckshare_shared_by_id_baf25f4b ON public.cards_deckshare USING btree (shared_by_id);


--
-- Name: cards_deckshare_shared_with_id_85f45150; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_deckshare_shared_with_id_85f45150 ON public.cards_deckshare USING btree (shared_with_id);


--
-- Name: cards_profile_chosen_decks_deck_id_09f49c20; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_profile_chosen_decks_deck_id_09f49c20 ON public.cards_profile_chosen_decks USING btree (deck_id);


--
-- Name: cards_profile_chosen_decks_profile_id_7c8c1814; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_profile_chosen_decks_profile_id_7c8c1814 ON public.cards_profile_chosen_decks USING btree (profile_id);


--
-- Name: cards_tag_name_0a185c64_like; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_tag_name_0a185c64_like ON public.cards_tag USING btree (name varchar_pattern_ops);


--
-- Name: cards_usercardprogress_card_id_13d226d7; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_usercardprogress_card_id_13d226d7 ON public.cards_usercardprogress USING btree (card_id);


--
-- Name: cards_usercardprogress_user_id_d4e50c01; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_usercardprogress_user_id_d4e50c01 ON public.cards_usercardprogress USING btree (user_id);


--
-- Name: cards_userdeck_deck_id_963aabfa; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_userdeck_deck_id_963aabfa ON public.cards_userdeck USING btree (deck_id);


--
-- Name: cards_userdeck_user_id_256275fe; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX cards_userdeck_user_id_256275fe ON public.cards_userdeck USING btree (user_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: kristinejohnson
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_card cards_card_deck_id_679b88fe_fk_cards_deck_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_card
    ADD CONSTRAINT cards_card_deck_id_679b88fe_fk_cards_deck_id FOREIGN KEY (deck_id) REFERENCES public.cards_deck(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_deck cards_deck_owner_id_1187f16f_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deck
    ADD CONSTRAINT cards_deck_owner_id_1187f16f_fk_auth_user_id FOREIGN KEY (owner_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_deck_tags cards_deck_tags_deck_id_788a8319_fk_cards_deck_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deck_tags
    ADD CONSTRAINT cards_deck_tags_deck_id_788a8319_fk_cards_deck_id FOREIGN KEY (deck_id) REFERENCES public.cards_deck(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_deck_tags cards_deck_tags_tag_id_41991297_fk_cards_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deck_tags
    ADD CONSTRAINT cards_deck_tags_tag_id_41991297_fk_cards_tag_id FOREIGN KEY (tag_id) REFERENCES public.cards_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_deckshare cards_deckshare_deck_id_9a7c88e6_fk_cards_deck_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deckshare
    ADD CONSTRAINT cards_deckshare_deck_id_9a7c88e6_fk_cards_deck_id FOREIGN KEY (deck_id) REFERENCES public.cards_deck(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_deckshare cards_deckshare_shared_by_id_baf25f4b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deckshare
    ADD CONSTRAINT cards_deckshare_shared_by_id_baf25f4b_fk_auth_user_id FOREIGN KEY (shared_by_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_deckshare cards_deckshare_shared_with_id_85f45150_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_deckshare
    ADD CONSTRAINT cards_deckshare_shared_with_id_85f45150_fk_auth_user_id FOREIGN KEY (shared_with_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_profile_chosen_decks cards_profile_chosen_decks_deck_id_09f49c20_fk_cards_deck_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_profile_chosen_decks
    ADD CONSTRAINT cards_profile_chosen_decks_deck_id_09f49c20_fk_cards_deck_id FOREIGN KEY (deck_id) REFERENCES public.cards_deck(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_profile_chosen_decks cards_profile_chosen_profile_id_7c8c1814_fk_cards_pro; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_profile_chosen_decks
    ADD CONSTRAINT cards_profile_chosen_profile_id_7c8c1814_fk_cards_pro FOREIGN KEY (profile_id) REFERENCES public.cards_profile(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_profile cards_profile_user_id_454db9f1_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_profile
    ADD CONSTRAINT cards_profile_user_id_454db9f1_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_usercardprogress cards_usercardprogress_card_id_13d226d7_fk_cards_card_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_usercardprogress
    ADD CONSTRAINT cards_usercardprogress_card_id_13d226d7_fk_cards_card_id FOREIGN KEY (card_id) REFERENCES public.cards_card(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_usercardprogress cards_usercardprogress_user_id_d4e50c01_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_usercardprogress
    ADD CONSTRAINT cards_usercardprogress_user_id_d4e50c01_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_userdeck cards_userdeck_deck_id_963aabfa_fk_cards_deck_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_userdeck
    ADD CONSTRAINT cards_userdeck_deck_id_963aabfa_fk_cards_deck_id FOREIGN KEY (deck_id) REFERENCES public.cards_deck(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: cards_userdeck cards_userdeck_user_id_256275fe_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.cards_userdeck
    ADD CONSTRAINT cards_userdeck_user_id_256275fe_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: kristinejohnson
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

