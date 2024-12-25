class AIModel:
    def __init__(self, name, category, rating, parameters=None):
        self.name = name
        self.category = category
        self.rating = rating
        self.parameters = parameters or {}

class AILibraryManagement:
    def __init__(self):
        self.inventory = []
    
    def add_model(self, model):
        self.inventory.append(model)
    
    def get_highest_rated_models(self, x):
        sorted_models = sorted(self.inventory, key=lambda m: (-m.rating, m.name))
        return sorted_models[:x]
    
    def recommend_top_model_by_category(self, category):
        category_models = [model for model in self.inventory if model.category == category]
        if not category_models:
            return None
        return max(category_models, key=lambda m: (m.rating, -ord(m.name[0])))
