library(readxl)
View(Iris)                               
I = Iris
I$Species = NULL
View(I)
R = kmeans(I,3)
R$size
R$cluster
table(Iris$Species, R$cluster)
plot(I$SepalLengthCm,I$SepalWidthCm, col = R$cluster)
plot(Iris$SepalLengthCm, Iris$SepalWidthCm, col = iris$Species)