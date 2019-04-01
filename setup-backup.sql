 DROP DATABASE histdata_test;
 CREATE DATABASE IF NOT EXISTS histdata_test;
 CREATE USER IF NOT EXISTS 'tradeuser_test'@'localhost' IDENTIFIED BY 'Trade123#';
 GRANT ALL ON histdata_test.* TO 'tradeuser_test'@'localhost' ;
  GRANT ALL PRIVILEGES ON *.* TO 'tradeuser_test'@'localhost' WITH GRANT OPTION;


 use histdata_test;

CREATE TABLE IF NOT EXISTS ieod_data_hour (
  id BIGINT NOT NULL AUTO_INCREMENT ,
  ticker varchar(255) NOT NULL,
  exchange varchar(10) NOT NULL,
  TradeDate date NOT NULL,
  TradeTime datetime NOT NULL,
  Open float DEFAULT NULL,
  High float DEFAULT NULL,
  Low float DEFAULT NULL,
  Close float DEFAULT NULL,
  Volume BIGINT DEFAULT NULL,
  PRIMARY KEY (id,ticker,exchange,TradeTime)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS ieod_data_5min (
  id BIGINT AUTO_INCREMENT,
  ticker varchar(255) NOT NULL,
  exchange varchar(10) NOT NULL,
  TradeDate date NOT NULL,
  TradeTime datetime NOT NULL,
  Open float DEFAULT NULL,
  High float DEFAULT NULL,
  Low float DEFAULT NULL,
  Close float DEFAULT NULL,
  Volume BIGINT DEFAULT NULL,
  PRIMARY KEY (id,ticker,exchange,TradeTime)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS ieod_data_30min (
  id BIGINT AUTO_INCREMENT,
  ticker varchar(255) NOT NULL,
  exchange varchar(10) NOT NULL,
  TradeDate date NOT NULL,
  TradeTime datetime NOT NULL,
  Open float DEFAULT NULL,
  High float DEFAULT NULL,
  Low float DEFAULT NULL,
  Close float DEFAULT NULL,
  Volume BIGINT DEFAULT NULL,
  PRIMARY KEY (id,ticker,exchange,TradeTime)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



CREATE TABLE IF NOT EXISTS ieod_data_10min (
  id BIGINT AUTO_INCREMENT,
  ticker varchar(255) NOT NULL,
  exchange varchar(10) NOT NULL,
  TradeDate date NOT NULL,
  TradeTime datetime NOT NULL,
  Open float DEFAULT NULL,
  High float DEFAULT NULL,
  Low float DEFAULT NULL,
  Close float DEFAULT NULL,
  Volume BIGINT DEFAULT NULL,
  PRIMARY KEY (id,ticker,exchange,TradeTime)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


