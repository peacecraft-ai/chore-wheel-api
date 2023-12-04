--nothing will be deleted from this file
--it will only grow downwards with commands that shape the database

create table tuser (
    user_id serial primary key,
    username varchar(32) not null,
    password varchar(255) not null
);
