create database cadastro
default character set utf8
default collate utf8_general_ci;

use cadastro;

create table cliente(
	id int auto_increment not null,
    nome varchar(20) not null,
    email varchar(30) not null unique,
    senha varchar(10) not null,
    preferencia enum("Drama","Terror","Animação","Romance","Ação"),
    primary key(id)
)default charset = utf8;

insert into cliente values
(Default,"Thomas","thomaspirescorreia@gmail.com","25179616","Ação"),
(Default,"Carlos","CarlosEduardo@gmail.com","25179616","Drama"),
(Default,"Larissa","LarissaCavalcante@gmail.com","25179616","Terror"),
(Default,"Matheus","MatheusBorba@gmail.com","25179616","Ação"),
(Default,"Fernando","FernandoGustavo@gmail.com","25179616","Ação"),
(Default,"Maria","MariaBertolani@gmail.com","25179616","Romance");
