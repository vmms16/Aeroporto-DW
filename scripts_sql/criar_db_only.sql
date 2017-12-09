-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema airport
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema airport
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `airport` DEFAULT CHARACTER SET utf8 ;
USE `airport` ;

-- -----------------------------------------------------
-- Table `airport`.`estacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `airport`.`estacao` (
  `id` VARCHAR(45) NOT NULL,
  `cidade` VARCHAR(45) NULL DEFAULT NULL,
  `estado` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `airport`.`aeroporto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `airport`.`aeroporto` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `sigla` VARCHAR(45) NULL DEFAULT NULL,
  `local` VARCHAR(45) NULL DEFAULT NULL,
  `id_estacao` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `sigla_UNIQUE` (`sigla` ASC),
  INDEX `fk_Aeroporto_1_idx` (`id_estacao` ASC),
  CONSTRAINT `fk_Aeroporto_1`
    FOREIGN KEY (`id_estacao`)
    REFERENCES `airport`.`estacao` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

-- -----------------------------------------------------
-- Table `airport`.`dados_meteorologicos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `airport`.`dados_meteorologicos` (
  `id_est` VARCHAR(45) NOT NULL,
  `data` VARCHAR(45) NOT NULL,
  `pressao` INT(11) NULL DEFAULT NULL,
  `temperatura` INT(11) NULL DEFAULT NULL,
  `umidade` INT(11) NULL DEFAULT NULL,
  `vento` INT(11) NULL DEFAULT NULL,
  `precipitacao` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id_est`, `data`),
  CONSTRAINT `fk_Dados_Meteorologicos_1`
    FOREIGN KEY (`id_est`)
    REFERENCES `airport`.`estacao` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `airport`.`empresa_aerea`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `airport`.`empresa_aerea` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(300) NULL DEFAULT NULL,
  `sigla` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `sigla_UNIQUE` (`sigla` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `airport`.`justificativas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `airport`.`justificativas` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `sigla` VARCHAR(45) NULL DEFAULT NULL,
  `descricao` VARCHAR(300) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `airport`.`Situacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `airport`.`Situacao` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `airport`.`voo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `airport`.`voo` (
  `id_voo` INT(11) NOT NULL AUTO_INCREMENT,
  `numero_voo` INT(11) NULL DEFAULT NULL,
  `hora_partida_realizada` VARCHAR(45) NULL DEFAULT NULL,
  `hora_partida_prevista` VARCHAR(45) NULL DEFAULT NULL,
  `hora_chegada_realizada` VARCHAR(45) NULL DEFAULT NULL,
  `hora_chegada_prevista` VARCHAR(45) NULL DEFAULT NULL,
  `data_partida_realizada` VARCHAR(45) NULL DEFAULT NULL,
  `data_partida_prevista` VARCHAR(45) NULL DEFAULT NULL,
  `data_chegada_realizada` VARCHAR(45) NULL DEFAULT NULL,
  `data_chegada_prevista` VARCHAR(45) NULL DEFAULT NULL,
  `empresa_aerea` INT(11) NULL DEFAULT NULL,
  `justificativa` INT(11) NULL DEFAULT NULL,
  `id_situacao` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_voo`),
  INDEX `fk_Voo_1_idx` (`empresa_aerea` ASC),
  INDEX `fk_Voo_2_idx` (`justificativa` ASC),
  INDEX `fk_Voo_3_idx` (`id_situacao` ASC),
  CONSTRAINT `fk_Voo_1`
    FOREIGN KEY (`empresa_aerea`)
    REFERENCES `airport`.`empresa_aerea` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Voo_2`
    FOREIGN KEY (`justificativa`)
    REFERENCES `airport`.`justificativas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Voo_3`
    FOREIGN KEY (`id_situacao`)
    REFERENCES `airport`.`Situacao` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `airport`.`voo_aeroporto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `airport`.`voo_aeroporto` (
  `id_voo_fk` INT(11) NOT NULL,
  `id_aeroporto_origem` INT(11) NOT NULL,
  `id_aeroporto_destino` INT(11) NOT NULL,
  PRIMARY KEY (`id_voo_fk`, `id_aeroporto_origem`, `id_aeroporto_destino`),
  INDEX `fk_Voo_Aeroport_2_idx` (`id_aeroporto_origem` ASC),
  INDEX `fk_Voo_Aeroport_3_idx` (`id_aeroporto_destino` ASC),
  CONSTRAINT `fk_Voo_Aeroport_1`
    FOREIGN KEY (`id_voo_fk`)
    REFERENCES `airport`.`voo` (`id_voo`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Voo_Aeroport_2`
    FOREIGN KEY (`id_aeroporto_origem`)
    REFERENCES `airport`.`aeroporto` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Voo_Aeroport_3`
    FOREIGN KEY (`id_aeroporto_destino`)
    REFERENCES `airport`.`aeroporto` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
