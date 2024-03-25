-- Criar o banco de dados INSS
CREATE DATABASE INSS;

-- Usar o banco de dados INSS
\c INSS;

-- Criar a tabela Beneficios
CREATE TABLE Beneficios (
    Competencia DATE,
    Especie VARCHAR(100),
    COD VARCHAR(20),
    CID VARCHAR(100),
    Despacho VARCHAR(100),
    DataNascimento DATE,
    Sexo CHAR(1),
    MunicipioResidencia VARCHAR(100),
    Dependentes VARCHAR(100),
    Filiação VARCHAR(200),
    UF CHAR(2)
);
