from neo4j import GraphDatabase, Driver

local_driver: Driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "password"))

def get_local_neo4j_driver() -> Driver:
    return local_driver