-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : sam. 25 mai 2024 à 14:43
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `supervision_onduleurs`
--

-- --------------------------------------------------------

--
-- Structure de la table `alarm`
--

CREATE TABLE `alarm` (
  `id` int(11) NOT NULL,
  `id_onduleur` varchar(50) DEFAULT NULL,
  `type_alarm` varchar(20) DEFAULT NULL,
  `date_alarm` datetime DEFAULT NULL,
  `etat_alarm` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `consomation`
--

CREATE TABLE `consomation` (
  `id` int(11) NOT NULL,
  `consomation` double DEFAULT NULL,
  `date_de_consomation` datetime DEFAULT NULL,
  `intervalle` varchar(30) DEFAULT NULL,
  `id_onduleur` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `consomation`
--

INSERT INTO `consomation` (`id`, `consomation`, `date_de_consomation`, `intervalle`, `id_onduleur`) VALUES
(3, 3000, '2024-05-25 13:38:20', '24h', '192.168.12.113'),
(4, 3000, '2024-05-25 13:39:31', 'week', '192.168.12.113'),
(5, 3000, '2024-05-25 13:39:46', 'month', '192.168.12.113');

-- --------------------------------------------------------

--
-- Structure de la table `onduleurs`
--

CREATE TABLE `onduleurs` (
  `id_onduleur` varchar(50) NOT NULL,
  `nom_onduleur` varchar(20) DEFAULT NULL,
  `numero_de_serie` varchar(50) DEFAULT NULL,
  `modele` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `onduleurs`
--

INSERT INTO `onduleurs` (`id_onduleur`, `nom_onduleur`, `numero_de_serie`, `modele`) VALUES
('192.168.12.113', 'EATON', NULL, NULL);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `alarm`
--
ALTER TABLE `alarm`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_id_onduleur_2` (`id_onduleur`);

--
-- Index pour la table `consomation`
--
ALTER TABLE `consomation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_id_onduleur_1` (`id_onduleur`);

--
-- Index pour la table `onduleurs`
--
ALTER TABLE `onduleurs`
  ADD PRIMARY KEY (`id_onduleur`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `alarm`
--
ALTER TABLE `alarm`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `consomation`
--
ALTER TABLE `consomation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `alarm`
--
ALTER TABLE `alarm`
  ADD CONSTRAINT `fk_id_onduleur_2` FOREIGN KEY (`id_onduleur`) REFERENCES `onduleurs` (`id_onduleur`);

--
-- Contraintes pour la table `consomation`
--
ALTER TABLE `consomation`
  ADD CONSTRAINT `fk_id_onduleur` FOREIGN KEY (`id_onduleur`) REFERENCES `onduleurs` (`id_onduleur`),
  ADD CONSTRAINT `fk_id_onduleur_1` FOREIGN KEY (`id_onduleur`) REFERENCES `onduleurs` (`id_onduleur`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
