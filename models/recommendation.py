import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from surprise import Dataset, Reader, SVD

class RecommendationModel:
    def __init__(self):
        self.model = SVD()

    def load_data(self, file_path):
        # Load dataset
        self.data = pd.read_csv(file_path)
        reader = Reader(rating_scale=(1, 5))
        self.dataset = Dataset.load_from_df(self.data[['user_id', 'item_id', 'rating']], reader)

    def train(self):
        # Train the model
        trainset = self.dataset.build_full_trainset()
        self.model.fit(trainset)

    def recommend(self, user_id, num_recommendations=5):
        # Generate recommendations
        user_items = self.data[self.data['user_id'] == user_id]['item_id'].tolist()
        all_items = self.data['item_id'].unique()
        items_to_predict = [item for item in all_items if item not in user_items]
        predictions = [self.model.predict(user_id, item) for item in items_to_predict]
        predictions.sort(key=lambda x: x.est, reverse=True)
        return predictions[:num_recommendations]
