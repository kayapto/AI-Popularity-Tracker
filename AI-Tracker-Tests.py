import unittest
from datetime import datetime
from ai_tracker import AIModel, AILibraryManagement

class TestAIModelTracker(unittest.TestCase):
    def setUp(self):
        self.library = AILibraryManagement()
        
        # Pre-populate with diverse test data
        self.models = [
            AIModel("GPT-4", "LLM", 4.8, {
                "parameters": "175B",
                "release_date": "2023-03-14",
                "company": "OpenAI"
            }),
            AIModel("Claude 2", "LLM", 4.7, {
                "parameters": "150B",
                "release_date": "2023-07-11",
                "company": "Anthropic"
            }),
            AIModel("DALL-E 3", "Image", 4.5, {
                "release_date": "2023-10-11",
                "company": "OpenAI"
            }),
            AIModel("Stable Diffusion XL", "Image", 4.3, {
                "release_date": "2023-07-26",
                "company": "Stability AI"
            }),
            AIModel("Llama 2", "LLM", 4.6, {
                "parameters": "70B",
                "release_date": "2023-07-18",
                "company": "Meta"
            })
        ]
        
        for model in self.models:
            self.library.add_model(model)

    def test_add_model(self):
        """Test adding new models"""
        new_model = AIModel("Gemini Pro", "LLM", 4.9)
        self.library.add_model(new_model)
        self.assertIn(new_model, self.library.inventory)
        self.assertEqual(len(self.library.inventory), 6)

    def test_highest_rated_models(self):
        """Test getting top rated models"""
        top_3 = self.library.get_highest_rated_models(3)
        self.assertEqual(len(top_3), 3)
        self.assertEqual(top_3[0].name, "GPT-4")
        self.assertEqual(top_3[1].name, "Claude 2")
        self.assertEqual(top_3[2].name, "Llama 2")

    def test_category_recommendation(self):
        """Test category-specific recommendations"""
        top_llm = self.library.recommend_top_model_by_category("LLM")
        top_image = self.library.recommend_top_model_by_category("Image")
        
        self.assertEqual(top_llm.name, "GPT-4")
        self.assertEqual(top_image.name, "DALL-E 3")

    def test_empty_category(self):
        """Test behavior with non-existent category"""
        result = self.library.recommend_top_model_by_category("Audio")
        self.assertIsNone(result)

    def test_rating_boundaries(self):
        """Test edge cases for ratings"""
        # Test minimum rating
        min_model = AIModel("TestMin", "LLM", 0.0)
        self.library.add_model(min_model)
        
        # Test maximum rating
        max_model = AIModel("TestMax", "LLM", 5.0)
        self.library.add_model(max_model)
        
        top_all = self.library.get_highest_rated_models(10)
        self.assertEqual(top_all[0].name, "TestMax")
        self.assertEqual(top_all[-1].name, "TestMin")

    def test_same_rating_ordering(self):
        """Test alphabetical ordering for same ratings"""
        self.library.add_model(AIModel("ZModel", "LLM", 4.8))
        self.library.add_model(AIModel("AModel", "LLM", 4.8))
        
        top_models = self.library.get_highest_rated_models(3)
        same_rating_models = [m for m in top_models if m.rating == 4.8]
        self.assertTrue(
            all(same_rating_models[i].name <= same_rating_models[i+1].name 
                for i in range(len(same_rating_models)-1))
        )

    def test_model_parameters(self):
        """Test model parameters storage and retrieval"""
        gpt4 = next(m for m in self.library.inventory if m.name == "GPT-4")
        self.assertEqual(gpt4.parameters["parameters"], "175B")
        self.assertEqual(gpt4.parameters["company"], "OpenAI")
        self.assertTrue("release_date" in gpt4.parameters)

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAIModelTracker)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    run_tests()
