
# # Classification Demo 
# import pandas as pd
# from optimalflow.autoCV import dynaClassifier,evaluate_model,dynaClassifier
# import joblib

# tr_features = pd.read_csv('./data/classification/train_features.csv')
# tr_labels = pd.read_csv('./data/classification/train_labels.csv')
# val_features = pd.read_csv('./data/classification/val_features.csv')
# val_labels = pd.read_csv('./data/classification/val_labels.csv')
# te_features = pd.read_csv('./data/classification/test_features.csv')
# te_labels = pd.read_csv('./data/classification/test_labels.csv')

# custom_ml = ['lgr','svm','mlp','rf','ada','gb','xgb','lsvc','sgd','hgboost','rgcv']

# clf_cv_demo = dynaClassifier(custom_estimators = custom_ml,random_state = 13,cv_num = 5)

# clf_cv_demo.fit(tr_features,tr_labels)

# models = {}

# for mdl in ['lsvc','sgd','hgboost','rgcv']:
#     models[mdl] = joblib.load('./pkl/{}_clf_model.pkl'.format(mdl))

# for name, mdl in models.items():
#     try:
#         ml_evl = evaluate_model(model_type = "cls")
#         ml_evl.fit(name, mdl, val_features, val_labels)
#     except:
#         print(f"Failed to load the {mdl}.")
    
# # fast Classification Demo 
# import pandas as pd
# from optimalflow.autoCV import dynaClassifier,evaluate_model,fastClassifier
# import joblib

# tr_features = pd.read_csv('./data/classification/train_features.csv')
# tr_labels = pd.read_csv('./data/classification/train_labels.csv')
# val_features = pd.read_csv('./data/classification/val_features.csv')
# val_labels = pd.read_csv('./data/classification/val_labels.csv')
# te_features = pd.read_csv('./data/classification/test_features.csv')
# te_labels = pd.read_csv('./data/classification/test_labels.csv')

# custom_ml = ['lgr','svm','mlp','rf','ada','gb','xgb','lsvc','sgd','hgboost','rgcv']

# clf_cv_demo = fastClassifier(custom_estimators = custom_ml,random_state = 13,cv_num = 5,n_comb = 20)

# clf_cv_demo.fit(tr_features,tr_labels)

# models = {}

# for mdl in ['lsvc','sgd','hgboost','rgcv']:
#     models[mdl] = joblib.load('./pkl/{}_clf_model.pkl'.format(mdl))

# for name, mdl in models.items():
#     try:
#         ml_evl = evaluate_model(model_type = "cls")
#         ml_evl.fit(name, mdl, val_features, val_labels)
#     except:
#         print(f"Failed to load the {mdl}.")
# # Regression Demo 1
# import pandas as pd
# from optimalflow.autoCV import evaluate_model,dynaClassifier,dynaRegressor
# import joblib

# tr_features = pd.read_csv('./data/regression/train_features.csv')
# tr_labels = pd.read_csv('./data/regression/train_labels.csv')
# val_features = pd.read_csv('./data/regression/val_features.csv')
# val_labels = pd.read_csv('./data/regression/val_labels.csv')
# te_features = pd.read_csv('./data/regression/test_features.csv')
# te_labels = pd.read_csv('./data/regression/test_labels.csv')

# reg_cv_demo = dynaRegressor(random_state=13,cv_num = 5)

# reg_cv_demo.fit(tr_features,tr_labels)

# models = {}

# for mdl in ['lr','knn','tree','svm','mlp','rf','gb','ada','xgb']:
#     models[mdl] = joblib.load('./pkl/{}_reg_model.pkl'.format(mdl))

# for name, mdl in models.items():
#     try:
#         ml_evl = evaluate_model(model_type = "reg")
#         ml_evl.fit(name, mdl, val_features, val_labels)
#     except:
#         print(f"Failed to load the {mdl}.")

# # # Regression Demo 2
# import pandas as pd
# from optimalflow.autoCV import evaluate_model,dynaClassifier,dynaRegressor
# import joblib

# from optimalflow.utilis_func import pipeline_splitting_rule, update_parameters,reset_parameters
# reset_parameters()

# tr_features = pd.read_csv('./data/regression/train_features.csv')
# tr_labels = pd.read_csv('./data/regression/train_labels.csv')
# val_features = pd.read_csv('./data/regression/val_features.csv')
# val_labels = pd.read_csv('./data/regression/val_labels.csv')
# te_features = pd.read_csv('./data/regression/test_features.csv')
# te_labels = pd.read_csv('./data/regression/test_labels.csv')

# reg_cv_demo = dynaRegressor(random_state=13,cv_num = 5)

# reg_cv_demo.fit(tr_features,tr_labels)

# models = {}

# for mdl in ['lr','knn','tree','svm','mlp','rf','gb','ada','xgb','hgboost','huber','rgcv','cvlasso','sgd']:
#     models[mdl] = joblib.load('./pkl/{}_reg_model.pkl'.format(mdl))

# for name, mdl in models.items():
#     try:
#         ml_evl = evaluate_model(model_type = "reg")
#         ml_evl.fit(name, mdl, val_features, val_labels)
#     except:
#         print(f"Failed to load the {mdl}.")

# # Fast Regression Demo 2
import pandas as pd
from optimalflow.autoCV import evaluate_model,dynaClassifier,fastRegressor
import joblib

from optimalflow.utilis_func import pipeline_splitting_rule, update_parameters,reset_parameters
reset_parameters()



tr_features = pd.read_csv('./data/regression/train_features.csv')
tr_labels = pd.read_csv('./data/regression/train_labels.csv')
val_features = pd.read_csv('./data/regression/val_features.csv')
val_labels = pd.read_csv('./data/regression/val_labels.csv')
te_features = pd.read_csv('./data/regression/test_features.csv')
te_labels = pd.read_csv('./data/regression/test_labels.csv')

custom_ml = ['lr','knn','tree','svm','mlp','rf','gb','ada','xgb','hgboost','huber','rgcv','cvlasso','sgd']

reg_cv_demo = fastRegressor(custom_estimators = custom_ml,random_state = 13,cv_num = 5,n_comb = 12)

reg_cv_demo.fit(tr_features,tr_labels)

models = {}

for mdl in ['lr','knn','tree','svm','mlp','rf']:
    models[mdl] = joblib.load('./pkl/{}_reg_model.pkl'.format(mdl))

for name, mdl in models.items():
    try:
        ml_evl = evaluate_model(model_type = "reg")
        ml_evl.fit(name, mdl, val_features, val_labels)
    except:
        print(f"Failed to load the {mdl}.")

# # EstimatorCV Test Demo - classification
# import pandas as pd
# from optimalflow.estimatorCV import clf_cv,reg_cv

# tr_features = pd.read_csv('./data/classification/train_features.csv')
# tr_labels = pd.read_csv('./data/classification/train_labels.csv')
# # val_features = pd.read_csv('../data/val_features.csv')
# # val_labels = pd.read_csv('../data/val_labels.csv')
# # te_features = pd.read_csv('../data/test_features.csv')
# # te_labels = pd.read_csv('../data/test_labels.csv')

# clf_demo = clf_cv(cv_val = 5,random_state = 13)
# clf_demo = clf_demo.lgr()
# result = clf_demo.fit(tr_features,tr_labels)
# print(result.best_estimator_)


'''
# EstimatorCV Test Demo - Regression
# import pandas as pd

# tr_features = pd.read_csv('../data/regression/train_features.csv')
# tr_labels = pd.read_csv('../data/regression/train_labels.csv')
# # val_features = pd.read_csv('../data/val_features.csv')
# # val_labels = pd.read_csv('../data/val_labels.csv')
# # te_features = pd.read_csv('../data/test_features.csv')
# # te_labels = pd.read_csv('../data/test_labels.csv')

# tr_labels = tr_labels.values.ravel()
# reg_demo = reg_cv(cv_val = 5,random_state = 13)
# reg_demo = reg_demo.gb()
# result = reg_demo.fit(tr_features,tr_labels)
# print(result.best_estimator_)
'''