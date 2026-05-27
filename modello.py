from sklearn.linear_model import LogisticRegression

def model(X_train, y_train, X_test):
    # 1. Inizializziamo il modello
    # Utilizziamo il solver 'liblinear' che è ottimo per dataset piccoli
    model = LogisticRegression(solver='liblinear', random_state=42)

    # 2. Addestramento
    model.fit(X_train, y_train)

    # 3. Predizione
    y_pred = model.predict(X_test)

    return y_pred