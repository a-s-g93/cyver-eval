from typing import List

def get_cypher_queries() -> List[str]:
       return [
              
"""MATCH (:Collection {name: 'Chocolate cake'})<-[:COLLECTION]-(recipe)
RETURN recipe.id, recipe.name, recipe.description;""",


"""MATCH (r:Recipe {id:'97123'})-[:CONTAINS_INGREDIENT]->(i:Ingredient)<-[:CONTAINS_INGREDIENT]-(rec:Recipe)
RETURN rec.id, rec.name, collect(i.name) AS commonIngredients
ORDER BY size(commonIngredients) DESC
LIMIT 10;""",



"""MATCH (rec:Recipe)<-[:WROTE]-(a:Author)-[:WROTE]->(r:Recipe {name:'Seriously rich chocolate cake'})
RETURN rec.id, rec.name, rec.description
LIMIT 10;""",



"""MATCH (r:Recipe)
WHERE all(i in ['chilli', 'prawn'] WHERE exists(
    (r)-[:CONTAINS_INGREDIENT]->(:Ingredient {name: i})))
RETURN r.name AS recipe,
        [(r)-[:CONTAINS_INGREDIENT]->(i) | i.name]
        AS ingredients
ORDER BY size(ingredients)
LIMIT 20;""",


"""MATCH (r:Recipe)
WHERE all(i in ['coconut milk', 'rice'] WHERE exists(
    (r)-[:CONTAINS_INGREDIENT]->(:Ingredient {name: i})))
AND none(i in ['egg', 'milk'] WHERE exists(
    (r)-[:CONTAINS_INGREDIENT]->(:Ingredient {name: i})))
RETURN r.name AS recipe,
        [(r)-[:CONTAINS_INGREDIENT]->(i) | i.name]
        AS ingredients
ORDER BY size(ingredients)
LIMIT 20;""",



"""MATCH (a:Author)-[:WROTE]->(r:Recipe)
WHERE a.name = "Tony Tobin"
RETURN r.name
LIMIT 10;""",



"""MATCH (r:Recipe)
WHERE EXISTS {
    (r)-[:DIET_TYPE]->(dt:DietType {name: "Vegetarian"})
}
AND EXISTS {
    (r)-[:DIET_TYPE]->(dt:DietType {name: "Gluten-free"})
}
RETURN r.name
LIMIT 20;""",



"""MATCH (r:Recipe)
WHERE r.skillLevel = "Easy"
    AND (r.cookingTimeMinutes + r.preparationTimeMinutes) < 20
RETURN r.name as name, r.cookingTimeMinutes as cookingTimeMinutes, r.preparationTimeMinutes as preparationTimeMinutes, r.cookingTimeMinutes + r.preparationTimeMinutes as totalTime
ORDER BY totalTime
LIMIT 20;""",



"""MATCH (r:Recipe)
WHERE (r.cookingTimeMinutes + r.preparationTimeMinutes) < 30
RETURN r.name as name, r.cookingTimeMinutes + r.preparationTimeMinutes as totalTime
ORDER BY totalTime
LIMIT 20;""",



"""MATCH (r:Recipe)-[:KEYWORD]->(k:Keyword)
WHERE k.name = "Chocolate"
RETURN r.name
LIMIT 10;""",


"""MATCH (r:Recipe)-[:CONTAINS_INGREDIENT]->(i:Ingredient)
WHERE i.name = "couscous"
RETURN r.name
LIMIT 10;""",

"""MATCH (r:Recipe)-[:COLLECTION]->(c:Collection)
WHERE c.name = "Spicy chicken"
RETURN r.name
ORDER BY rand()
LIMIT 1;"""
       ]