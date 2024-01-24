-- ereate a mysql board table schema with comments, reply functions, and file attachment functions, author, date, etc.
create table board (
    id int auto_increment comment 'board id',
    title varchar(50) not null comment 'board title',
    content text comment 'board content',
    author varchar(20) not null comment 'board author',
    date datetime not null comment 'board date',
    primary key (id)
) engine=InnoDB default charset=utf8 comment 'board table';

create table reply (
    id int auto_increment comment 'reply id',
    board_id int not null comment 'board id',
    content text comment 'reply content',
    primary key (id)
) engine=InnoDB default charset=utf8 comment 'reply table';

create table file (
    id int auto_increment comment 'file id',
    board_id int not null comment 'board id',
    file_name varchar(50) not null comment 'file name',
    file_path varchar(200) not null comment 'file path',
    primary key (id)
) engine = InnoDB default charset=utf8 comment 'file table';
