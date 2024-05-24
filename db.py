from neo4j import GraphDatabase, basic_auth


class database:
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://44.204.196.216:7687",auth=basic_auth("neo4j", "hall-syntax-hose"))

    def close(self):
        self.driver.close()    
        
    def run_query(self, query,parameters=None):
        with self.driver.session() as session:
            result = list(session.run(query,parameters))
            return result
