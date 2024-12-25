# AI-Popularity-Tracker
AI Model Popularity Tracker
A Python library for tracking and analyzing AI model ratings and popularity across different categories.
Features

Track AI models with names, categories, and ratings
Store model-specific parameters and specifications
Get highest-rated models across all categories
Find top models within specific categories (LLM, Image Generation, etc.)
Sort by rating with alphabetical tiebreaking

Usage
pythonCopyfrom ai_tracker import AIModel, AILibraryManagement

# Initialize library
library = AILibraryManagement()

# Add models
library.add_model(AIModel("GPT-4", "LLM", 4.8, {"parameters": "175B"}))
library.add_model(AIModel("DALL-E 3", "Image", 4.5))

# Get top models
top_models = library.get_highest_rated_models(3)

# Get category recommendation
top_llm = library.recommend_top_model_by_category("LLM")
Input Format
Each model entry requires:

Name (string)
Category (string)
Rating (float: 0.0-5.0)
Parameters (optional dict)

Testing
Run tests with:
bashCopypython ai_tracker_test.py
Contributing

Fork repository
Create feature branch
Commit changes
Push to branch
Create Pull Request

License
MIT License
