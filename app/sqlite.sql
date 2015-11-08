CREATE TABLE User(
user_id int primary key,
username varchar(30) not null,
type varchar(10) not null
);

CREATE TABLE Account(
account_number int primary key,
user_id int not null,
balance float not null,
type varchar(10) not null,
foreign key (user_id) references User(user_id) on delete cascade
);

CREATE TABLE Log(
user_id int not null,
account_number int not null,
log_content varchar(200) not null,
start_time timestamp,
end_time timestamp
foreign key (user_id) references User(user_id) on delete cascade,
foreign key (account_number) references Account(account_number) on delete cascade
);

