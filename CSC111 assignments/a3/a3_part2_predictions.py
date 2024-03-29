"""CSC111 Winter 2022 Assignment 3: Graphs, Recommender Systems, and Clustering (Part 2)

Instructions (READ THIS FIRST!)
===============================

This Python module contains classes responsible for making predictions of book review scores.
We've provided the abstract class and some example subclasses, and you'll complete one new
subclass and a new function to evaluate the different classes.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr, David Liu, and Isaac Waller.
"""
from __future__ import annotations
import csv
from typing import Union

import a3_part2_recommendations


class ReviewScorePredictor:
    """A graph-based entity that predicts scores for book reviews.

    This is an abstract class, and should be subclasses to implement different review
    prediction algorithms.

    Instance Attributes:
        - graph: The book review graph that this entity uses to make predictions.
    """
    graph: a3_part2_recommendations.WeightedGraph

    def __init__(self, graph: a3_part2_recommendations.WeightedGraph) -> None:
        """Initialize a new ReviewScorePredictor."""
        self.graph = graph

    def predict_review_score(self, user: str, book: str) -> int:
        """Predict the score (1-5) that the given user would give the given book.

        If there is already an edge between the given user and book in the graph,
        return that score. Otherwise, return a predicted score.

        Preconditions:
            - user in self.graph._vertices
            - book in self.graph._vertices
        """
        raise NotImplementedError


class FiveStarPredictor(ReviewScorePredictor):
    """A book review predictor that always predicts a five-star review,
    ignoring the actual book and user.
    """
    def predict_review_score(self, user: str, book: str) -> int:
        """Predict the score that the given user would give the given book.

        If there is already an edge between the given user and book in the graph,
        return that score. Otherwise, return 5 as the predicted score.

        Preconditions:
            - user in self.graph._vertices
            - book in self.graph._vertices
        """
        if self.graph.adjacent(user, book):
            return self.graph.get_weight(user, book)
        else:
            return 5


class BookAverageScorePredictor(ReviewScorePredictor):
    """A book review predictor that always predicts based on the book's average score,
    ignoring any user preferences.
    """
    def predict_review_score(self, user: str, book: str) -> int:
        """Predict the score that the given user would give the given book.

        If there is already an edge between the given user and book in the graph,
        return that score. Otherwise, return the book's average review score in
        the graph, rounded to the nearest integer (using the built-in `round` function).

        Preconditions:
            - user in self.graph._vertices
            - book in self.graph._vertices
            - the given book has at least one review
        """
        if self.graph.adjacent(user, book):
            return self.graph.get_weight(user, book)
        else:
            return round(self.graph.average_weight(book))


################################################################################
# Part 2, Q3
################################################################################
class SimilarUserPredictor(ReviewScorePredictor):
    """A book review predictor that makes a prediction based on how similar users rated the book.

    Representation Invariants:
        - self._score_type in {'unweighted', 'strict'}
    """
    # Private Instance Attributes:
    #   - _score_type: the type of similarity score to use when computing similarity score
    _score_type: str

    def __init__(self, graph: a3_part2_recommendations.WeightedGraph,
                 score_type: str = 'unweighted') -> None:
        """Initialize a new SimilarUserPredictor.

        You may want to review Section 10.4 of the Course Notes for a reminder on
        how to properly override a superclass initializer. To avoid a python_ta.contracts error,
        initialize self._score_type at the TOP of this method body.
        """
        self._score_type = score_type
        ReviewScorePredictor.__init__(self, graph)

    def predict_review_score(self, user: str, book: str) -> int:
        """Predict the score that the given user would give the given book.

        If there is already an edge between the given user and book in the graph,
        return that score. Otherwise, return the book's WEIGHTED review score among
        all users who have read the book, where the weight used is the similarity
        score of the reviewing user with the given user. self._score_type is used
        to determine which similarity score to use for the weights

        As usual, round this score using the built-in `round` function.

        For example, suppose there are three users A, B, C who have read the book,
        and one, D, who has not. We want to use the review scores of A, B, and C to predict
        the rating for D. The three user ratings and weighted similarity score with D
        are shown in this table:

            | User | Review score | Weighted similarity score with D |
            | ---- | ------------ | -------------------------------- |
            | A    | 3            | 0.4                              |
            | B    | 5            | 0.1                              |
            | C    | 2            | 0.3                              |

        Then the predicted review for D equals:

            (3 * 0.4 + 5 * 0.1 + 2 * 0.3) / (0.4 + 0.1 + 0.3) = 2.875

        and so this function would return 3.

        If the total similarity score from all of the book's reviewers is 0,
        then instead return the book's average review score (same as BookAverageScorePredictor).

        Preconditions:
            - user in self.graph._vertices
            - book in self.graph._vertices
        """
        if self.graph.adjacent(user, book):
            return self.graph.get_weight(user, book)
        else:
            n = 0
            d = 0
            for v in self.graph.get_neighbours(book):
                weight = self.graph.get_weight(v, book)
                similarity = self.graph.get_similarity_score(v, user, self._score_type)

                n += weight * similarity
                d += similarity

            if d == 0:
                return round(self.graph.average_weight(book))
            else:
                return round(n / d)


################################################################################
# Part 2, Q4
################################################################################
def evaluate_predictor(predictor: ReviewScorePredictor,
                       test_file: str, book_names_file: str) -> dict[str, Union[int, float]]:
    """Evaluate the given ReviewScorePredictor on the given test file.

    Read in each row of the given test_file (which contains a book, user, and
    review score). For each row, use the given predictor to make a prediction of the review
    score, and compare that prediction against the actual given review score from the file.

    Return a dictionary summarizing the performance of the predictor. This dictionary
    has the following keys:
        - 'num_reviews': the total number of predicted review scores (equal to the
            number of lines in the CSV file)
        - 'num_correct': the number of predicted review scores that exactly matched the
            actual review score
        - 'average_error': the average of the *absolute value difference* between
            predicted and actual review scores across all reviews in the test file

    Preconditions:
        - test_file is the path to a CSV file corresponding to the book review data
          format described on the assignment handout
        - book_names_file is the path to a CSV file corresponding to the book data
        - test_file has at least one row
        - all users and books in test_file are in predictor.graph
          format described on the assignment handout
    """
    num_reviews = 0
    num_correct = 0
    error = 0
    books = {}

    with open(book_names_file) as csv_file:
        reader = csv.reader(csv_file)

        for book_id, book_name in reader:
            books[book_id] = book_name

    with open(test_file) as csv_file:
        reader = csv.reader(csv_file)

        for user, book, score in reader:
            prediction = predictor.predict_review_score(user, books[book])
            num_reviews += 1
            error += abs(prediction - int(score))

            if prediction == int(score):
                num_correct += 1

    return {
        'num_reviews': num_reviews,
        'num_correct': num_correct,
        'average_error': error / num_reviews
    }


if __name__ == '__main__':
    # You can uncomment the following lines for code checking/debugging purposes.
    # However, we recommend commenting out these lines when working with the large
    # datasets, as checking representation invariants and preconditions greatly
    # increases the running time of the functions/methods.
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 1000,
        'disable': ['E1136'],
        'extra-imports': ['csv', 'a3_part2_recommendations'],
        'allowed-io': ['evaluate_predictor'],
        'max-nested-blocks': 4
    })
