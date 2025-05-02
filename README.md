Voici un fichier README_SQL.md en Markdown qui regroupe toutes les requêtes SQL utilisées dans mon projet, accompagnées d’explications claires pour chacune.

markdown
Copier
Modifier
# 📊 Requêtes SQL du projet TidianeFlix

Ce fichier contient l’ensemble des requêtes SQL utilisées dans le cadre du projet **TidianeFlix**, classées par type avec explications.

---

## 🔹 Requêtes de base

### 1. Lister tous les films avec leur durée et leur genre
```sql
SELECT titre, duree, genre FROM film;
Cette requête affiche le titre, la durée et le genre de tous les films présents dans la base.

2. Afficher les projections d’un film donné (ex. : Wakanda Forever)
sql
Copier
Modifier
SELECT * FROM projection WHERE id_film = (
    SELECT id_film FROM film WHERE titre = 'Wakanda Forever'
);
Elle récupère les projections du film "Wakanda Forever" en identifiant son id_film.

3. Lister les clients triés par nom
sql
Copier
Modifier
SELECT * FROM client ORDER BY nom;
Affiche tous les clients, triés par ordre alphabétique du nom.

4. Compter le nombre total de films projetés dans la semaine
sql
Copier
Modifier
SELECT COUNT(DISTINCT id_film) AS films_semaine 
FROM projection 
WHERE WEEK(date) = WEEK(CURDATE());
Compte les films uniques projetés pendant la semaine en cours.

🔸 Requêtes avec jointures
5. Détail des tickets achetés (film, date, client, prix)
sql
Copier
Modifier
SELECT ticket.id_ticket, film.titre, projection.date, client.nom, ticket.prix
FROM ticket
JOIN projection ON ticket.id_projection = projection.id_projection
JOIN film ON projection.id_film = film.id_film
JOIN client ON ticket.id_client = client.id_client;
Permet d’avoir un historique détaillé de chaque ticket vendu.

6. Liste des projections avec titre du film et nom de la salle
sql
Copier
Modifier
SELECT projection.date, film.titre, salle.nom_salle
FROM projection
JOIN film ON projection.id_film = film.id_film
JOIN salle ON projection.id_salle = salle.id_salle;
Fournit une vue complète des projections, avec les titres et les salles.

7. Afficher les notes et commentaires donnés pour chaque film
sql
Copier
Modifier
SELECT film.titre, avis.note, avis.commentaire
FROM avis
JOIN film ON avis.id_film = film.id_film;
Récupère les avis (note + commentaire) associés à chaque film.

8. Clients ayant assisté à plus de 3 projections
sql
Copier
Modifier
SELECT id_client, COUNT(*) AS nb_tickets
FROM ticket
GROUP BY id_client
HAVING nb_tickets > 3;
Identifie les clients réguliers ayant acheté plus de 3 tickets.

🔺 Requêtes avancées
9. Film le plus projeté ce mois-ci
sql
Copier
Modifier
SELECT film.titre, COUNT(*) AS nb_projections
FROM projection
JOIN film ON projection.id_film = film.id_film
WHERE MONTH(date) = MONTH(CURDATE())
GROUP BY film.id_film
ORDER BY nb_projections DESC
LIMIT 1;
Donne le film ayant le plus de projections ce mois.

10. Moyenne des notes par film
sql
Copier
Modifier
SELECT film.titre, AVG(avis.note) AS moyenne_note
FROM avis
JOIN film ON avis.id_film = film.id_film
GROUP BY film.id_film;
Calcule la note moyenne donnée à chaque film.

11. Salles les plus utilisées
sql
Copier
Modifier
SELECT salle.nom_salle, COUNT(*) AS nb_projections
FROM projection
JOIN salle ON projection.id_salle = salle.id_salle
GROUP BY salle.id_salle
ORDER BY nb_projections DESC;
Classe les salles selon leur nombre d’utilisations.

12. Clients qui ont donné un avis mais n’ont acheté aucun ticket
sql
Copier
Modifier
SELECT DISTINCT client.nom, client.prenom
FROM client
JOIN avis ON client.id_client = avis.id_client
WHERE client.id_client NOT IN (
    SELECT id_client FROM ticket
);
Liste les clients qui ont laissé un avis sans jamais acheter de ticket.

13. Total des revenus générés par jour
sql
Copier
Modifier
SELECT DATE(date_achat) AS jour, SUM(prix) AS revenu_journalier
FROM ticket
GROUP BY DATE(date_achat);
14. Total des revenus par semaine
sql
Copier
Modifier
SELECT WEEK(date_achat) AS semaine, SUM(prix) AS revenu_hebdo
FROM ticket
GROUP BY WEEK(date_achat);
Ces requêtes calculent les revenus selon les périodes.

15. Vue films_populaires
sql
Copier
Modifier
CREATE VIEW films_populaires AS
SELECT f.titre, COUNT(t.id_ticket) AS tickets_vendus, AVG(a.note) AS note_moyenne
FROM film f
LEFT JOIN projection p ON f.id_film = p.id_film
LEFT JOIN ticket t ON p.id_projection = t.id_projection
LEFT JOIN avis a ON f.id_film = a.id_film
GROUP BY f.id_film;
Vue utile pour consulter rapidement les films les plus populaires selon les ventes et les notes.

16. Fonction revenu_par_film(id_film)
sql
Copier
Modifier
DELIMITER //
CREATE FUNCTION revenu_par_film(film_id INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
  DECLARE total DECIMAL(10,2);
  SELECT SUM(t.prix)
  INTO total
  FROM ticket t
  JOIN projection p ON t.id_projection = p.id_projection
  WHERE p.id_film = film_id;
  RETURN IFNULL(total, 0.0);
END;
//
DELIMITER ;
Fonction SQL personnalisée pour retourner les revenus générés par un film donné.

🛠️ À propos
💾 SGBD : MySQL

👨‍💻 Auteur : Cheikh Niang

📧 Contact : cheikhniang159@gmail.com


