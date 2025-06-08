from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

from sklearn.model_selection import train_test_split

data = load_breast_cancer ()

x_train, x_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42
)

model = RandomForestClassifier()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)
y_pred_proba = model.predict_proba(x_test)[:,1]

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score (y_test, y_pred)

print(f"A métrica precision é: {precision:.2f}")
print(f"A métrica recall é: {precision:.2f}")
print(f"A métrica f1 é: {precision:.2f}")
print(f"A métrica auc é: {precision:.2f}")