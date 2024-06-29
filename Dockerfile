# A prepared image with python3.10, java 11, ir_datasets, tira, and PyTerrier installed 
FROM webis/ir-lab-wise-2023:0.0.4

# Update the tira command to use the latest version
RUN pip3 uninstall -y tira \
	&& pip3 install tira

# Install nltk, spaCy, and pygls
RUN pip3 install nltk spacy pygls \
    && python3 -m spacy download en_core_web_sm

# Download NLTK stopwords
RUN python3 -c "import nltk; nltk.download('stopwords')"

# importing RandomForestRegressor 
RUN python3 -c "from sklearn.ensemble import RandomForestRegressor"

ADD . /app

