-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 21 mai 2024 à 11:57
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
  `id_onduleur` int(11) NOT NULL,
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
  `intervalle` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `consomation`
--

INSERT INTO `consomation` (`id`, `consomation`, `date_de_consomation`, `intervalle`) VALUES
(3, 66.66666666666666, '2024-05-16 15:12:15', '24h'),
(4, 66.66666666666666, '2024-05-16 15:12:21', 'week'),
(5, 66.66666666666666, '2024-05-16 15:12:28', 'month'),
(6, 66.66666666666666, '2024-05-16 15:13:21', 'month'),
(7, 66.66666666666666, '2024-05-17 13:50:32', '5min');

-- --------------------------------------------------------

--
-- Structure de la table `onduleurs`
--

CREATE TABLE `onduleurs` (
  `id_onduleur` int(11) NOT NULL,
  `nom_onduleur` varchar(20) DEFAULT NULL,
  `numero_de_serie` varchar(50) DEFAULT NULL,
  `modele` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `alarm`
--
ALTER TABLE `alarm`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_onduleur` (`id_onduleur`);

--
-- Index pour la table `consomation`
--
ALTER TABLE `consomation`
  ADD PRIMARY KEY (`id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `onduleurs`
--
ALTER TABLE `onduleurs`
  MODIFY `id_onduleur` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `alarm`
--
ALTER TABLE `alarm`
  ADD CONSTRAINT `alarm_ibfk_1` FOREIGN KEY (`id_onduleur`) REFERENCES `onduleurs` (`id_onduleur`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
