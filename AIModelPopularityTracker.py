class AIModel:
    def __init__(self, name, category, rating, parameters=None):
        self.name = name
        self.category = category  # LLM, Image Generation, etc.
        self.rating = rating
        self.parameters = parameters or {}  # Model parameters/specs

class AILibraryManagement:
    def __init__(self):
        self.inventory = []
    
    def add_model(self, model):
        """Adds a new AI model to the inventory."""
        self.inventory.append(model)
    
    def get_highest_rated_models(self, x):
        """Returns the x highest-rated AI models."""
        sorted_models = sorted(self.inventory, key=lambda m: (-m.rating, m.name))
        return sorted_models[:x]
    
    def recommend_top_model_by_category(self, category):
        """Returns the top-rated model in a specific category."""
        category_models = [model for model in self.inventory if model.category == category]
        if not category_models:
            return None
        return max(category_models, key=lambda m: (m.rating, -ord(m.name[0])))

def main(path):
    fptr = open(path, 'w')
    
    num = int(input())
    library = AILibraryManagement()
    
    for _ in range(num):
        name, category, rating = input().split(',')
        library.add_model(AIModel(name, category, float(rating)))
    
    recommended_count = int(input())
    category = input()
    
    highest_rated_models = library.get_highest_rated_models(recommended_count)
    model_by_category = library.recommend_top_model_by_category(category)
    
    for model in highest_rated_models:
        fptr.write(f"Highest Rated AI Model: {model.name}, Rating: {model.rating}\n")
    
    if model_by_category:
        fptr.write(f"Top Recommended model in {category} Category: {model_by_category.name}, Rating: {model_by_category.rating}\n")
    else:
        fptr.write("No models found in the specified category.\n")
    
    fptr.close()

if __name__ == "__main__":
    import os
    path = os.environ.get("OUTPUT_PATH", "/dev/stdout")
    main(path)
