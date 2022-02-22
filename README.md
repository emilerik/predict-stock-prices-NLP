# Evaluating Predictive Power of SEC 8-K Forms on Stock Prices
A project as part of the course "Text Mining" at Linköping University.

Files:
- `main.ipynb` - the bulk of the project
- `helper_functions.py` - some helper functions used in preprocessing
- `processed_df.csv` - all the data after preprocessing steps
- `models/` directory with the trained models and their histories. See `main.ipynb` for how they're loaded.

Abstract:

In the US, publicly listed companies must file a report called SEC 8-K
(or Form 8-K) to inform their investors of important events in the company, such
as bankruptcy or change of management. These forms follow a clear structure
and may contain information that affects the stock in the days following the
report, which has prompted researchers to explore processing the information
using NLP in order to forecast stock prices. In this project, a deep neural
network called LSTM was developed and used with GloVe word embeddings
to predict UP or DOWN signals for stock prices. Importantly, only textual
and no financial features were used for prediction. A unigram model with a
random forest classifier was used as baseline. Despite attempts at tuning the
LSTM model, it achieved 50.05% accuracy on test data, indicating that it was
not able to find a predictive signal in the textual data. The unigram model
achieved 52.98% accuracy, lending some weight to the usefulness of the textual
information, but the majority class classifier still achieved the highest accuracy
of 53.68%.
