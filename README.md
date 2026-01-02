# RoalCode

RoalCode est un langage de programmation **interprété**, **typé** et **orienté performance**, conçu pour le développement d’applications lourdes nécessitant une gestion de mémoire maîtrisée, une syntaxe claire et une architecture moderne.

Il combine la lisibilité des langages de haut niveau avec une structure proche de C#/Java, tout en restant simple à apprendre et à utiliser.

## Caractéristiques principales

* Langage **interprété**
* **Typage statique obligatoire**
* Syntaxe claire et lisible
* Gestion robuste de la mémoire (avec le module `memoRoal`)
* Programmation orientée objet complète
* Gestion native des erreurs (exceptions)
* Système de modules extensible
* Conçu pour les **applications complexes et performantes**

## Exemple complet

```RoalCode
// ===== Variables typées =====
int a = 10
float b = 2.25
string text = "Texte à imprimer"
bool flag = true

console.print("Initialisation :", text + " ", string(a), " et ", string(b))

// ===== Listes et dictionnaires =====
int[] numbers = [1, 2, 3, 4]
string[] cities = ["Lyon", "Paris", "Marseille"]
map<string,int> ages = {"Alice":20, "Bob":25}

console.print("Premier nombre :", string(numbers[0]))
console.print("Age de Bob :", string(ages["Bob"]))

// ===== Saisie utilisateur =====
int nbr = console.scan("Entrez un nombre : ")

// ===== Conditions =====
if (nbr > 0) {
    console.print("Nombre positif")
} else if (nbr == 0) {
    console.print("Nombre nul")
} else {
    console.print("Nombre négatif")
}

// ===== Boucles =====
int sum = 0
for (int i = 0; i < 5; i = i + 1) {
    sum = sum + i
}
console.print("Somme :", string(sum))

// ===== Fonctions =====
int square(int x) {
    return x * x
}
console.print("Carré de 5 :", string(square(5)))

// ===== Classes =====
public class Person {
    string name
    int age

    void greet() {
        console.print("Bonjour, je suis " + name)
    }
}

Person p = new Person()
p.name = "Alice"
p.age = 20
p.greet()
```

## Syntaxe du langage

### Types primitifs

* `int`
* `float`
* `string`
* `bool`
* `void`

### Structures de données

* Listes typées : `int[]`, `string[]`, etc.
* Dictionnaires : `map<key,value>`

### Opérateurs logiques

* `and`
* `or`
* `not`

## Boucles

### Boucle for

```RoalCode
for (int i = 0; i < 10; i = i + 1) {
    console.print(i)
}
```

### Boucle for each

```RoalCode
for each city in cities {
    console.print(city)
}
```

## Programmation orientée objet

* Classes avec visibilité `public` et `private`
* Héritage avec `:`
* Méthodes typées
* Allocation dynamique avec `new`

```RoalCode
private class Animal : Person {
    public string species
}
```

## Gestion des erreurs

```RoalCode
try {
    int result = 10 / nbr
} catch (DivisionByZeroError e) {
    console.print("Division par zéro")
} catch (Exception e) {
    console.print(e.message)
} finally {
    console.print("Fin du traitement")
}
```

## Modules

Modules standards disponibles :

* `console` (inclus par défaut)
* `math`
* `string_utils`
* `file_io`
* `network`
* `sys`
* `os`
* `time`
* `random`
* `winUI`
* `memoRoal`
* `scoreedit`
* `future`

```RoalCode
import math
from file_io import File
```

## Chaînes multilignes

```Roalcode
string text = """Texte sur
plusieurs lignes
conservé tel quel"""
```

## Commentaires

```RoalCode
// Commentaire simple
/*
   Commentaire
   multilignes
*/
```

## Objectif du langage

RoalCode est conçu pour :

* le développement d’applications lourdes
* les outils professionnels
* les interfaces graphiques Windows
* les éditeurs spécialisés (ex: TEXTA score edit ou StudioX)
* les projets nécessitant lisibilité + performance

## Statut du projet

RoalCode est en développement actif. Bientôt l'interpréteur sera disponible.

---

**RoalCode — Simple à lire, puissant à exécuter.**
