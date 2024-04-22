from google.cloud import datastore
import traceback

DS_CLIENT = datastore.Client()

class DatastoreService:
    kind = "Facts"

    def add(self, question):
        print(f"Adding question: {question} to Datastore")
        try:
            new_entity = datastore.Entity(DS_CLIENT.key(self.kind))
            new_entity["question"] = question
            new_entity["status"] = "processing"
            DS_CLIENT.put(new_entity)

            return True, f"Successully added {question} to DS"
        except Exception:
            print(traceback.format_exc())
            return False, "Unable to add data to store!"
        
    def update(self, answer):
        print(f"Updating Datastore")
        try:
            query = DS_CLIENT.query(kind=self.kind)
            entity = list(query.fetch())

            if entity:
                entity= entity[0] 
            else:
                return False, "No entities found"
            
            question = entity["question"]
            entity["facts"] = answer
            entity["status"] = "done"
            DS_CLIENT.put(entity)

            return True, f"Successully updated {question} to DS"
        except Exception:
            print(traceback.format_exc())
            return False, "Unable to update DS!"
        
    def get(self):
        print(f"Retrieving from Datastore")
        try:
            query = DS_CLIENT.query(kind=self.kind)
            entity = list(query.fetch())

            entity = entity[0] if entity else None
            return True, entity
        except Exception:
            print(traceback.format_exc())
            return False, "Unable to retrieve entity!"
        
    def deleteEntity(self):
        print(f"Deleteing all entities from Datastore")
        try:
            query = DS_CLIENT.query(kind=self.kind)
            entities = list(query.fetch())
            
            # Delete the fetched entities in a batch
            keys = [entity.key for entity in entities]
            DS_CLIENT.delete_multi(keys)

            return True, "Successfully deleted entities"
        except Exception:
            print(traceback.format_exc())
            return False, "Unable to delete entity!"
        
    