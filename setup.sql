USE master;
GO

IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'EquitecTestDB')
BEGIN
    CREATE DATABASE EquitecTestDB;
END
GO

USE EquitecTestDB;
GO

IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'TradeOrders')
BEGIN
    CREATE TABLE TradeOrders (
        OrderId INT IDENTITY(1,1) PRIMARY KEY,
        ClientName NVARCHAR(100) NOT NULL,
        StockSymbol NVARCHAR(50) NOT NULL,
        Quantity INT NOT NULL,
        Price DECIMAL(18, 2) NOT NULL,
        OrderType NVARCHAR(10) NOT NULL CHECK (OrderType IN ('BUY', 'SELL'))
    );
    
    -- Insert a sample record
    INSERT INTO TradeOrders (ClientName, StockSymbol, Quantity, Price, OrderType)
    VALUES ('Demo Client', 'EQU.IT', 100, 150.50, 'BUY');
END
GO
