# Simplified Abstract Syntax Tree Based Semantic Features Learning for Software Change Prediction
This repository includes the code and experimental data in our paper entitled "Simplified Abstract Syntax Tree Based Semantic Features Learning for Software Change Prediction". In this paper, we propose a Simplified AST-based Neural Network (SASTNN) model for software change prediction. We first parse the code to get the abstract syntax tree(AST), then simplify the AST and extract the semantic features of the code. Finally, a deep neural network is used to further model the naturalness of code and perform software change prediction.

### Requirements
+ python 3.8<br>
+ pandas 1.2.0<br>
+ gensim 3.5.0<br>
+ scikit-learn 0.24.0<br>
+ pytorch 1.7.1<br>
+ pycparser 2.20<br>
+ javalang 0.11.0<br>
+ RAM 16GB or more<br>
+ GPU with CUDA support<br>

### How to install
Install all the dependent packages via pip:

	$ pip install pandas==1.2.0 gensim==3.5.0 scikit-learn==0.24.0 pycparser==2.20 javalang==0.11.0

Please install pytorch according to your environment, refer to https://pytorch.org/

### Dataset
Our data set can be found under the path "one_version/classifier/data" .<br> The ast-whole folder contains the data of all projects; it is a "pkl" file, which is easy to read using the pandas library. Each file contains three columns, namely, file id, code, and label. <br>The tr folder contains traditional features of all projects.

### Change Prediction

#### use traditional classifier
1. cd one_version/classifier
2. run python pipeline_ast_whole.py to generate preprocessed data.
3. run methods_whole.py to get result.

#### use neural network
1. cd one_version/deep/ast_whole_nn
2. run python pipeline_ast_whole_cross.py to generate preprocessed data.
3. run train_whole_cross.py for training and evaluation.
