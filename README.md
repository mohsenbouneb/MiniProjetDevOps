# Mini Projet DevOps

Ce projet implémente un pipeline CI/CD pour une application Python de calcul. Il utilise GitHub Actions pour automatiser le processus de build, de test et de déploiement sur Azure.

## Objectif

L'objectif de ce projet est de créer un pipeline automatisé qui construit une image Docker pour une application Python, effectue une analyse de code avec SonarQube, puis déploie l'application sur Azure.

## Fonctionnalités

- **Build Docker Image** : Construction d'une image Docker à partir du code source.
- **Analyse SonarQube** : Analyse du code source pour détecter les vulnérabilités et améliorer la qualité du code.
- **Déploiement sur Azure** : Déploiement de l'application sur une Azure Web App.

## Prérequis

- Docker
- SonarQube
- Azure Web App
- GitHub Actions

## Workflow GitHub Actions

1. **Checkout du code** : Récupération du code source depuis GitHub.
2. **Installation des dépendances** : Installation de Java pour SonarScanner et de SonarScanner lui-même.
3. **Exécution de l'analyse SonarQube** : Analyse du code avec SonarQube.
4. **Connexion à Docker Hub** : Connexion à Docker Hub pour pousser l'image Docker.
5. **Build de l'image Docker** : Construction de l'image Docker.
6. **Push de l'image Docker** : Pousser l'image Docker sur Docker Hub.
7. **Déploiement sur Azure** : Déploiement de l'image Docker sur une Azure Web App.

## Instructions pour Exécuter le Projet

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/Manel-Trabelsi/MiniProjetDevOps.git
