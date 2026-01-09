import logging
from abc import ABC, abstractmethod
from sklearn.ensemble import RandomForestClassifier

class ModelBuildingStrategy(ABC):
    @abstractmethod
    def build_and_train_model(self, X_train, y_train):
        pass
class RandomForestStrategy(ModelBuildingStrategy):
    def build_and_train_model(self, X_train, y_train):
        logging.info("Building and training Random Forest model for disease classification")
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model
