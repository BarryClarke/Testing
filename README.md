# Fisher's Iris Data set
![The Iris Family](/Images/iris-machinelearning.png)
## Scope
To summarize and present analysis of Fisher's Iris data set. Programming and Scripting Module project 2019
[See here for instructions](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)
## Table of Contents
1. Background
    - Ronald Fisher
    - Fisher's Iris data set
2. Data set Summary
    - Averages
    - Max lengths
    - Max widths
    - Distribution
3. Running the Code
4. Final Thoughts
5. References

## 1. Background
### Ronald Fisher 
![Ronald Fisher](/Images/Ronald.Fisher.jpg)  
[Ronald Fisher](http://leansixsigmadefinition.com/glossary/ronald-fisher/)  
* British Biologist and statistician (17th February 1890 - 29th July 1962)
* Widely considered to be "the single most important figure in 20th century statistics" *[2]*
* First to propose the Design of Experiments (The Design of Experiments (1935))
* Credited with initiating methods which led to Six Sigma and Lean Manufacturing [Lean Manufacturing and Six Sigma](http://leansixsigmadefinition.com/glossary/six-sigma/)
* Responsible for many other statistcal techniques such as [Analysis of Variance](http://leansixsigmadefinition.com/glossary/anova/), [P-value](https://en.wikipedia.org/wiki/P-value), and [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)

### Fisher's Iris dataset
* Linear Discriminant Analysis (LDA) is a statistiacl technique used in many applications including machine learning, image recognition and genetics. It focuses on maximising the seperability between two groups among known categories in order to differentiate the two groups and hence allow decisions to be made regarding the categories. 
* A good example of the application of LDA would be deciding which patients, with a particular illness, should be treated with a specific drug and which should not. LDA is a statistical technique that can use genetics to determine this with high statistical accuracy. See the following video: [Statquest: Linear Discriminant Analysis](https://www.youtube.com/watch?v=azXCzI57Yfc). *[5]*
* Fisher's Iris data set is a multivariate data set introduced by Ronald Fisher in his 1936 paper *[The use of multiple measurements in taxonomic problems](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)* *[3]* as an example of Linear discriminant analysis.

## 2. Data set Summary
* The Iris data set contains a total of 150 records - 50 records per specie, for 3 species of Iris: Iris Setosa, Iris Versicolor, and Iris Virginica. Within each record there are 5 attributes: the Sepal length, the Sepal width, the Petal length, the Petal width, and the specie.*[1]* The raw data colected can be seen [here](/Data/iris.csv). *[6]*
* Two of the three species (Setosa and Versicolor) were collected in Gaspé Peninsula, all from the same pasture, picked on the same day and measured at the same time by the same person with the same apparatus.*[4]*
* This data set and subsequent analysis has proven very valuable in many area's, including machine learning, because of the interesting statistical properties containied within the data set: From the data, the Setosa and Versicolor are difficult to seperate from each other, however the Virginica are easy to seperate from the other two.

## 3. Analysing the data set
### 3.1 Individual analysis of each specie
As can be ssen in the header picture, each Iris specie has Sepal and a petal. From the measuremants of the lengths and widths of both the Sepal and the Petal, we have calculated a few basic statistics for each specie. Please see the results for the Minimum, maximum, and average lengths and widths of sepal and petal for each specie, along with the scatter (Max - min) and the standard deviation for each attribute in [statistics 09-04-2019](statistics 09-04-2019.CSV) above. To obtain these statistics, please run statistics.py, which will produce was used to produce and present the statistics in the above csv file.

### 3.2 Comparison of species for individual attributes
In order to compare and contrast each specie, please see [comparison of Iris species for individual attributes](/Images/Comparison of Iris species for individual attributes.png). These plots were produced by running summary.py and the resulting plots saved to the images folder in this directory. From these plots, we can make a number of observations:
1. The sepal lengths and sepal widths for all 3 species are pretty similar in dimensions, whereas there appears to be a difference in the petal length and petal widths across the 3 species.
2. The Setosa petal seems to vary from the Versicolor and Virginica petals. It has a smaller petal. Its is quite easy to differentiate the Setosa from the other two species on the basis of the petal dimensions
3. It is more diffiscult to differentiate the Versicolor and the Virginica. As the plots show, perhaps the Versicolor petal is slightly smaller, in both length and width, than the Virginica, however there is still some crossover in the data for the Versicolor and Virginica petal. This means that, given a random petal, it would be difficult to decide whether it was a Versicolor or a Virginica.
The above gives us a good idea of the motivation of Fisher in his 1936 paper relating to the iris data set: Given a set of data from 3 species of a flower, use Linear Discriminant Analysis to be able to seperate or differentiate one for another 


## 4. Final Thoughts

## 5. References
*1.* http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP394/WholeStory-Iris.html  
*2.* http://leansixsigmadefinition.com/glossary/ronald-fisher/  
*3.* R.A. Fisher (1936). ["The use of multiple measurements in taxonomic problems"](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x). Annals of Eugenics. **7**(2): 179-188  
*4.* https://en.wikipedia.org/wiki/Iris_flower_data_set  
*5.* https://www.youtube.com/watch?v=azXCzI57Yfc  
*6.* https://gist.github.com/curran/a08a1080b88344b0c8a7

Summary.py: https://matplotlib.org/gallery/subplots_axes_and_figures/subplot.html







