 CREATE DATABASE IF NOT EXISTS marketdata;
 CREATE USER IF NOT EXISTS 'tradeuser'@'localhost' IDENTIFIED BY 'Trade123#';
 GRANT ALL ON marketdata.* TO 'tradeuser'@'localhost' IDENTIFIED BY 'Trade123#';
  GRANT ALL PRIVILEGES ON *.* TO 'tradeuser'@'localhost' IDENTIFIED BY 'Trade123#' WITH GRANT OPTION;


 use marketdata;

CREATE TABLE IF NOT EXISTS eoddata (
  ticker varchar(255) NOT NULL,
  TradeDate date NOT NULL,
  Open float NOT NULL,
  High float NOT NULL,
  Low float NOT NULL,
  Close float NOT NULL,
  VWAP float NOT NULL,
  Volume bigint(20) NOT NULL,
  Deliverable_Volume bigint(20) NOT NULL,
  Percentage_Deliverables float NOT NULL,
  PRIMARY KEY (ticker,TradeDate)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




CREATE TABLE IF NOT EXISTS intra_olh_trade (
  ticker varchar(255) NOT NULL,
  TradeDate date DEFAULT NULL,
  TradeTime datetime NOT NULL,
  Open float DEFAULT NULL,
  High float DEFAULT NULL,
  Low float DEFAULT NULL,
  Close float DEFAULT NULL,
  PClose float DEFAULT NULL,
  Atp  float DEFAULT NULL,
  Ipivot float DEFAULT NULL,
  NSE_Trade varchar(255) ,
  BSE_Trade varchar(255) ,
  Entry1 float DEFAULT NULL,
  Entry2 float DEFAULT NULL,
  Entry3 float DEFAULT NULL,
  SL float DEFAULT NULL,
  Target1 float DEFAULT NULL,
  Target2 float DEFAULT NULL,
  Target3 float DEFAULT NULL,
  Target4 float DEFAULT NULL,
  Target5 float DEFAULT NULL,
PRIMARY KEY (ticker,TradeTime)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


