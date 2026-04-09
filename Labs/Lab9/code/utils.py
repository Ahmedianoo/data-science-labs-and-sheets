import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
import seaborn as sns
from xgboost import XGBClassifier
from typing import Any, Dict, Optional, Union
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay


class Dataset:
    """
    Dataset wrapper for loading a CSV file and splitting it into
    training, validation, and test sets. The splits are accessible
    directly as class members.
    """

    def __init__(
        self,
        filepath: str,
        target_column: str,
        test_size: float = 0.2,
        val_size: float = 0.2,
        random_state: Optional[int] = 42,
    ):
        """
        Initialize and immediately load & split the dataset.

        Parameters
        ----------
        filepath : str
            Path to the CSV file.
        target_column : str
            Name of the target column.
        test_size : float, default=0.2
            Fraction of data for the test set.
        val_size : float, default=0.2
            Fraction of training data for the validation set.
        random_state : int, optional
            Random seed for reproducibility.
        """
        self.filepath = filepath
        self.target_column = target_column
        self.test_size = test_size
        self.val_size = val_size
        self.random_state = random_state

        # Placeholders for dataset and splits
        self.data: pd.DataFrame = None
        self.X_train: pd.DataFrame = None
        self.X_val: pd.DataFrame = None
        self.X_test: pd.DataFrame = None
        self.y_train: pd.Series = None
        self.y_val: pd.Series = None
        self.y_test: pd.Series = None

        # Load and split automatically
        self._load_data()
        self._split_data()

        self._print_imbalance()


    def _load_data(self) -> None:
        """Load CSV into a pandas DataFrame."""
        self.data = pd.read_csv(self.filepath)
        if self.target_column not in self.data.columns:
            raise ValueError(
                f"Target column '{self.target_column}' not found in dataset."
            )

    def _split_data(self) -> None:
        """Split dataset into train, validation, and test sets."""
        X = self.data.drop(columns=[self.target_column])
        y = self.data[self.target_column]

        # First split: train + test
        X_train_val, X_test, y_train_val, y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state
        )

        # Second split: train + validation
        val_fraction = self.val_size / (1 - self.test_size)
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_fraction, random_state=self.random_state
        )

        # Assign to members for direct use
        self.X_train, self.X_val, self.X_test = X_train, X_val, X_test
        self.y_train, self.y_val, self.y_test = y_train, y_val, y_test
    def imbalance_ratio(self) -> float:
        """
        Calculate the imbalance ratio (IR) of the target column.

        IR = (# samples in most frequent class) / (# samples in least frequent class)
        """
        counts = self.y_train.value_counts()
        ir = counts.max() / counts.min()
        return ir

    def _print_imbalance(self) -> None:
        """Print the imbalance ratio with a rule-of-thumb message in color."""
        ir = self.imbalance_ratio()

        # ANSI color codes
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        RED = "\033[91m"
        RESET = "\033[0m"

        print(f"Class Imbalance Ratio (IR): {ir:.2f}")

        if ir <= 3:
            print(f"{GREEN}Imbalance level: Mild (often OK with standard methods){RESET}")
        elif 3 < ir < 9:
            print(f"{YELLOW}Imbalance level: Moderate (needs attention){RESET}")
        elif 9 <= ir < 100:
            print(f"{RED}Imbalance level: Severe (requires specialized techniques){RESET}")
        else:
            print(f"{RED}Imbalance level: Extreme (consider anomaly detection methods){RESET}")



def plot_decision_boundary(model, X, y, feature_names, title, cmap='bwr'):
    """
    Plots the decision boundary of a trained sklearn classifier.

    Parameters
    ----------
    model       : trained sklearn estimator (has .predict())
    X           : np.ndarray of shape (n_samples, 2)
    y           : np.ndarray of shape (n_samples,)
    feature_names : list of two strings [x_label, y_label]
    title       : str
    cmap        : matplotlib colormap string
    """
    X = np.array(X)
    y = np.array(y)
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                         np.linspace(y_min, y_max, 300))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.2, cmap=cmap)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap, edgecolor='k', alpha=0.7)
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
    plt.title(title)
    plt.tight_layout()
    plt.show()


def evaluate(model, X, y, title="Evaluation"):
    """
    Prints classification report and plots confusion matrix.

    Parameters
    ----------
    model : trained sklearn estimator
    X     : features
    y     : true labels
    title : string label for the confusion matrix title
    """
    y_pred = model.predict(X)
    print(f"=== {title} ===")
    print(classification_report(y, y_pred))
    cm = confusion_matrix(y, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap='Blues')
    plt.title(title)
    plt.tight_layout()
    plt.show()
    return y_pred
