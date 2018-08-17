create table allstops
(
  stop_id      varchar(12)     null,
  stop_name    varchar(100)    null,
  stop_lat     decimal(25, 20) null,
  stop_long    decimal(25, 20) null,
  true_stop_id int             null,
  busroute     varchar(15)     null
);

create table auth_group
(
  id   int auto_increment
    primary key,
  name varchar(80) not null,
  constraint name
  unique (name)
);

create table auth_user
(
  id           int auto_increment
    primary key,
  password     varchar(128) not null,
  last_login   datetime(6)  null,
  is_superuser tinyint(1)   not null,
  username     varchar(150) not null,
  first_name   varchar(30)  not null,
  last_name    varchar(150) not null,
  email        varchar(254) not null,
  is_staff     tinyint(1)   not null,
  is_active    tinyint(1)   not null,
  date_joined  datetime(6)  not null,
  constraint username
  unique (username)
);

create table auth_user_groups
(
  id       int auto_increment
    primary key,
  user_id  int not null,
  group_id int not null,
  constraint auth_user_groups_user_id_group_id_94350c0c_uniq
  unique (user_id, group_id),
  constraint auth_user_groups_group_id_97559544_fk_auth_group_id
  foreign key (group_id) references auth_group (id),
  constraint auth_user_groups_user_id_6a12ed8b_fk_auth_user_id
  foreign key (user_id) references auth_user (id)
);

create table column_sequence
(
  id    int(10)     not null
    primary key,
  `46a` varchar(45) null
);

create table core_usersettings
(
  id              int auto_increment
    primary key,
  routeid         varchar(20) charset latin1  not null,
  direction       varchar(200) charset latin1 not null,
  originstop      varchar(200) charset latin1 not null,
  destinationstop varchar(200) charset latin1 not null,
  journeyname     varchar(200) charset latin1 not null,
  userid_id       int                         not null,
  constraint core_usersettings_userid_id_5f0ed0a2_fk_auth_user_id
  foreign key (userid_id) references auth_user (id)
)
  charset = utf8mb4;

create table currentWeather
(
  dt                  int                                 not null
    primary key,
  timestamp           timestamp default CURRENT_TIMESTAMP not null,
  city_id             int                                 null,
  temp                decimal(5, 2)                       null,
  temp_min            decimal(5, 2)                       null,
  temp_max            decimal(5, 2)                       null,
  pressure            int                                 null,
  humidity            int                                 null,
  wind_speed          int                                 null,
  wind_deg            int                                 null,
  rain_1h             decimal(5, 2)                       null,
  rain_3h             decimal(5, 2)                       null,
  rain_24h            decimal(5, 2)                       null,
  rain_today          decimal(5, 2)                       null,
  snow_1h             decimal(5, 2)                       null,
  snow_3h             decimal(5, 2)                       null,
  snow_24h            decimal(5, 2)                       null,
  snow_today          decimal(5, 2)                       null,
  clouds_all          int                                 null,
  weather_id          int                                 null,
  weather_main        varchar(50)                         null,
  weather_description varchar(80)                         null,
  weather_icon        varchar(10)                         null,
  dt_iso              datetime                            null
);

create table django_content_type
(
  id        int auto_increment
    primary key,
  app_label varchar(100) not null,
  model     varchar(100) not null,
  constraint django_content_type_app_label_model_76bd3d3b_uniq
  unique (app_label, model)
);

create table auth_permission
(
  id              int auto_increment
    primary key,
  name            varchar(255) not null,
  content_type_id int          not null,
  codename        varchar(100) not null,
  constraint auth_permission_content_type_id_codename_01ab375a_uniq
  unique (content_type_id, codename),
  constraint auth_permission_content_type_id_2f476e4b_fk_django_co
  foreign key (content_type_id) references django_content_type (id)
);

create table auth_group_permissions
(
  id            int auto_increment
    primary key,
  group_id      int not null,
  permission_id int not null,
  constraint auth_group_permissions_group_id_permission_id_0cd325b0_uniq
  unique (group_id, permission_id),
  constraint auth_group_permissio_permission_id_84c5c92e_fk_auth_perm
  foreign key (permission_id) references auth_permission (id),
  constraint auth_group_permissions_group_id_b120cbf9_fk_auth_group_id
  foreign key (group_id) references auth_group (id)
);

create table auth_user_user_permissions
(
  id            int auto_increment
    primary key,
  user_id       int not null,
  permission_id int not null,
  constraint auth_user_user_permissions_user_id_permission_id_14a6b632_uniq
  unique (user_id, permission_id),
  constraint auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm
  foreign key (permission_id) references auth_permission (id),
  constraint auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id
  foreign key (user_id) references auth_user (id)
);

create table django_admin_log
(
  id              int auto_increment
    primary key,
  action_time     datetime(6)          not null,
  object_id       longtext             null,
  object_repr     varchar(200)         not null,
  action_flag     smallint(5) unsigned not null,
  change_message  longtext             not null,
  content_type_id int                  null,
  user_id         int                  not null,
  constraint django_admin_log_content_type_id_c4bce8eb_fk_django_co
  foreign key (content_type_id) references django_content_type (id),
  constraint django_admin_log_user_id_c564eba6_fk_auth_user_id
  foreign key (user_id) references auth_user (id)
);

create table django_migrations
(
  id      int auto_increment
    primary key,
  app     varchar(255) not null,
  name    varchar(255) not null,
  applied datetime(6)  not null
);

create table django_session
(
  session_key  varchar(40) not null
    primary key,
  session_data longtext    not null,
  expire_date  datetime(6) not null
);

create index django_session_expire_date_a5c62663
  on django_session (expire_date);

create table dublinBus_schedule_current
(
  pkey                int          not null
    primary key,
  trip_id             varchar(45)  null,
  arrival_time        varchar(45)  null,
  departure_time      varchar(45)  null,
  stop_id             varchar(45)  null,
  stop_sequence       varchar(200) null,
  stop_headsign       varchar(200) null,
  pickup_type         varchar(45)  null,
  drop_off_type       varchar(45)  null,
  shape_dist_traveled varchar(45)  null,
  route_id            varchar(45)  null,
  service_id          varchar(45)  null,
  shape_id            varchar(200) null,
  trip_headsign       varchar(200) null,
  direction_id        varchar(45)  null,
  line_id             varchar(45)  null
);

create table forecastWeather
(
  dt                  int                                 not null
    primary key,
  dt_txt              timestamp default CURRENT_TIMESTAMP not null
  on update CURRENT_TIMESTAMP,
  timestamp           timestamp default CURRENT_TIMESTAMP not null,
  temp                decimal(5, 2)                       null,
  temp_max            decimal(5, 2)                       null,
  temp_min            decimal(5, 2)                       null,
  humidity            int                                 null,
  wind_speed          int                                 null,
  wind_deg            int                                 null,
  clouds_all          int                                 null,
  weather_id          int                                 null,
  weather_main        varchar(50)                         null,
  weather_description varchar(80)                         null,
  weather_icon        varchar(10)                         null,
  pressure            int                                 null
);

create table holidays
(
  date      datetime    not null,
  type      varchar(15) null,
  timestamp int         null,
  constraint holidays_date_uindex
  unique (date)
);

alter table holidays
  add primary key (date);

create table leavetimes
(
  dayofservice    datetime    not null,
  tripid          int         not null,
  progrnumber     smallint(6) not null,
  stoppointid     smallint(6) null,
  plannedtime_arr int         null,
  plannedtime_dep int         null,
  actualtime_arr  int         null,
  actualtime_dep  int         null,
  suppressed      float       null,
  primary key (dayofservice, tripid, progrnumber)
);

create table locations66
(
  busroute     varchar(15)     not null,
  stopid       int             not null,
  true_stop_id int             null,
  stop_lat     decimal(25, 20) null,
  stop_long    decimal(25, 20) null
);

create table routes
(
  routes varchar(10) not null
    primary key
);

create table routes_stopid
(
  busroute varchar(15) not null,
  stopid   int         not null,
  primary key (busroute, stopid)
);

create table stopsStatic
(
  stop_id      varchar(12)     null,
  stop_name    varchar(100)    null,
  stop_lat     decimal(25, 20) null,
  stop_long    decimal(25, 20) null,
  true_stop_id int             null
);

create table trips
(
  dayofservice    datetime    not null,
  tripid          int         not null,
  lineid          varchar(10) null,
  routeid         varchar(20) null,
  direction       tinyint     null,
  plannedtime_arr int         null,
  plannedtime_dep int         null,
  actualtime_arr  int         null,
  actualtime_dep  int         null,
  supressed       float       null,
  primary key (dayofservice, tripid)
);