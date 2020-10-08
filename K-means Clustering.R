library(readxl)
View(iris)                               
y = iris[,-c(5)]
x = iris
y
View(y)
R = kmeans(y,3)
R$size
R$cluster
table(x$Species, R$cluster)
plot(y$Sepal.Length,y$Sepal.Width, col = R$cluster)
plot(x$Sepal.Length, x$Sepal.Width, col = x$Species)
plot(y$Petal.Length,y$Petal.Width, col = R$cluster)
plot(y$Petal.Length,y$Petal.Width, col = x$Species)

