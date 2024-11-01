CREATE TABLE tbltheme_configuration(
	theme VARCHAR(100) NOT NULL,
	background_color CHAR(6) NOT NULL,
	font_color CHAR(6) NOT NULL,
	screen_size VARCHAR(20) NOT NULL DEFAULT '800x600',
	active TINYINT NOT NULL DEFAULT 0
);

INSERT INTO tblsoftware_configuration(theme, background_color, font_color, screen_size, active)
VALUES('Light', 'FFFFFF', '1d1d1d', '800x600', 0),
('Dark', '000000', 'FFFFFF', '800x600', 1);

CREATE TABLE tbltarefa(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	titulo VARCHAR(100) NOT NULL,
	descricao VARCHAR(255)
);

CREATE TABLE tblhorarios(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	id_tarefa INTEGER NOT NULL,
	everyxtimeenable TINYINT NOT NULL DEFAULT 0,
	everyxtime TIME NOT NULL DEFAULT '00:00:00',
	defaulttime TIME NOT NULL DEFAULT '00:00:00',
	typenotification TEXT CHECK(typenotification IN('PC', 'SMS', 'WPP', 'TGM')) NOT NULL DEFAULT 'PC',
	diassemana VARCHAR(100),
	FOREIGN KEY(id_tarefa) REFERENCES tbltarefa(id)
);

create table tblconfig(
	version VARCHAR(20) NOT NULL,
);