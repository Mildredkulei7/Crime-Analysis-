import streamlit as st

#Create the horizontal sections of our app
header = st.container()
desc = st.container()
plot = st.container()
prediction = st.container()
model = st.container()

#The first section
with header:
    st.title('Crime Analysis')
    st.write("""
    # Text Classification
    """)
    st.write('This is an application that classifies crime related text into various subcategories')
    col1, col2 = st.columns(2)
with model:
    st.title('Classification Algorithms')
    models = st.sidebar.selectbox('Select Classification Model', ('Naive Bayes','KNN'))
    dataset = st.sidebar.selectbox('Select dataset', ("crime-vectorised.csv"))
    st.write('Classification model : ',models)
    st.write('Dataset : ',dataset)

#Loading the dataset
def get_data(dataset_name):
        data = pd.read_csv('/content/crime-vectorised.csv')
        X = data['clean_text']
        y = data['label']
        return X,y
        X,y
        st.write('Number of tweets : ', len(X))
        st.write('Dataset classes : ', y.unique().tolist())


# Adding model parameters
def model_params(clf_name):
        params = dict()
        if models == 'KNN':
            from sklearn.neighbors import KNeighborsClassifier
            cl_gs = KNeighborsClassifier(n_neighbors=9)
            cl_gs.fit(X_train_tfidf, y_train)
            k = st.sidebar.slider('Number of K-folds', 1, 10)
            params['K'] = k
        elif models == 'Naive Bayes':
            model_params(models)
# Second section of the app
with desc:
    st.title('Overview')
    st.write('This is the overview of the app')


