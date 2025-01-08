import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class LeadScoringModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def load_data(self, file_path):
        # Load dataset
        self.data = pd.read_csv(file_path)

    def train(self):
        # Prepare data for training
        X = self.data.drop('converted', axis=1)
        y = self.data['converted']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model accuracy: {accuracy}")

    def score_lead(self, lead_data):
        # Score a new lead
        return self.model.predict([lead_data])
