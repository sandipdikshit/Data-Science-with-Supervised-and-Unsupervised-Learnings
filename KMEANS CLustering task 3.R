library(readxl)
> GRIP1 <- read_excel("Desktop/GRIP/GRIP1.xlsx")
> View(GRIP1)                              
> library(readxl)
> Iris <- read_excel("Desktop/GRIP/Iris.xlsx")
> View(Iris)                               
> I = Iris
> I$Species = NULL
> View(I)
> R = kmeans(I,3)
> R