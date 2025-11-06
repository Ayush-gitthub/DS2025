# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# R Reference Script for Data Science Students - University of Trier
# This script covers concepts from Chapters 1-5 of "Statistical Programming with R"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# =============================================================================
# Chapter 1: Some History and Getting Started
# =============================================================================

# R can be used as a scientific calculator for basic arithmetic operations.
10 + 5          # Addition
10 - 5          # Subtraction
10 * 5          # Multiplication
10 / 5          # Division

# The '#' symbol is used for comments. Anything after it on the same line is ignored.
# Comments are crucial for making your code readable and understandable.

# Using the print() function to display output.
print("Hello, Trier University!")


# =============================================================================
# Chapter 2: Vectors, Matrices, and Arrays
# =============================================================================

### --- Vectors: The basic data structure ---

# Create a numeric vector using the c() function (c stands for combine).
my_numeric_vector <- c(10, 20, 30, 40, 50)
my_numeric_vector

# Create a sequence of numbers.
sequence_vector <- 1:5 # Creates integers from 1 to 5
sequence_vector

# R vectors are "atomic," meaning all elements must be of the same data type.
# If you mix types, R will coerce them to the most flexible type.
mixed_vector <- c(1, "hello", TRUE) # All elements become characters.
mixed_vector
class(mixed_vector) # Check the data type of the vector

# Indexing vectors: Accessing elements using square brackets [].
my_numeric_vector[3]      # Get the 3rd element.
my_numeric_vector[c(1, 4)] # Get the 1st and 4th elements.
my_numeric_vector[-2]     # Get all elements EXCEPT the 2nd.


### --- Matrices: A two-dimensional data structure ---

# Create a matrix with 3 rows and 2 columns.
# By default, matrices are filled by column.
my_matrix <- matrix(data = 1:6, nrow = 3, ncol = 2)
my_matrix

# Create a matrix filled by row by setting byrow = TRUE.
my_matrix_byrow <- matrix(data = 1:6, nrow = 3, ncol = 2, byrow = TRUE)
my_matrix_byrow

# Indexing matrices: [row, column]
my_matrix[2, 1]  # Element at the 2nd row, 1st column.
my_matrix[3, ]   # The entire 3rd row.
my_matrix[, 2]   # The entire 2nd column.


### --- Arrays: Multi-dimensional data structures ---

# Create a 3-dimensional array (2 rows, 3 columns, 2 layers).
my_array <- array(data = 1:12, dim = c(2, 3, 2))
my_array

# Indexing arrays: [row, column, dimension]
my_array[1, 2, 2] # Element at 1st row, 2nd column of the 2nd layer.
?t()
t <-t(my_matrix)
t
?inverse.gaussian
# =============================================================================
# Chapter 3: Lists and Data Frames
# =============================================================================

### --- Lists: Flexible containers for different data types ---

# A list can hold elements of different types and structures.
my_list <- list(
  name = "Florian",
  student_id = 12345,
  grades = c(95, 88, 92),
  course_matrix = my_matrix
)
my_list

# Indexing lists:
# Using single brackets [] returns a sub-list.
my_list[1]

# Using double brackets [[]] or the $ sign extracts a single element.
my_list[[3]]
my_list$grades

# Applying functions to list elements
# lapply returns a list
lapply(my_list$grades, function(x) x + 5)

# sapply tries to simplify the result to a vector or matrix
sapply(my_list$grades, function(x) x + 5)


### --- Data Frames: The most common structure for datasets ---

# A data frame is a special list where all elements are vectors of the same length.
my_df <- data.frame(
  Name = c("Florian", "Jan", "Ralf"),
  Age = c(21, 30, 45),
  Major = c("Data Science", "Statistics", "Economics"),
  IsStudent = c(TRUE, TRUE, FALSE)
)
my_df
?data.frame
# Indexing data frames:
# Access columns like a list.
my_df$Age
my_df[["Name"]]

# Access elements like a matrix.
my_df[1, 3] # 1st row, 3rd column
my_df[2, ]  # 2nd row, all columns

# Factors: A special data type for categorical variables.
# Let's create an 'AgeGroup' factor from the 'Age' column using cut().
my_df$AgeGroup <- cut(
  my_df$Age,
  breaks = c(0, 25, 40, 100),
  labels = c("Young", "Middle", "Senior")
)
str(my_df) # The structure now shows that AgeGroup is a Factor.


# =============================================================================
# Chapter 4: Packages
# =============================================================================

# Packages extend R's functionality. CRAN is the main repository.

# To install a package, use install.packages().
# We comment this out so it doesn't run every time.
install.packages("fortunes")

# To use a package's functions, you must load it into your R session.
library(fortunes)

# Now you can use functions from the 'fortunes' package.
fortune(10) # Display a random R fortune.

# To use a function without loading the whole package, use the :: operator.
# This is useful to avoid conflicts when two packages have a function with the same name.
fortunes::fortune(15)
?fortune
fortune()
# =============================================================================
# Chapter 5: Visualisation
# =============================================================================

# R has three main plotting systems: base graphics, lattice, and ggplot2.

### --- Base Graphics (`graphics` package) ---

# Use the built-in 'iris' dataset for these examples.
data(iris)
head(iris)
?head
# High-level plotting: Create a new plot.
# Scatter plot of Sepal.Length vs. Petal.Length.
plot(
  x = iris$Sepal.Length,
  y = iris$Petal.Length,
  main = "Iris Sepal vs. Petal Length", # Title
  xlab = "Sepal Length (cm)",         # X-axis label
  ylab = "Petal Length (cm)",         # Y-axis label
  pch = 19,                          # Plotting character (solid circle)
  col = "blue"                       # Color of the points
)

# Low-level plotting: Add elements to the current plot.
# Add a horizontal line at the mean of Petal.Length.
abline(h = mean(iris$Petal.Length), col = "red", lwd = 2) # lwd is line width

# Add a legend to the plot.
legend(
  "topleft",
  legend = "Mean Petal Length",
  col = "red",
  lty = 1, # Line type
  lwd = 2
)

# Other plot types in base graphics:
# Histogram
hist(iris$Sepal.Width, main = "Histogram of Sepal Width", xlab = "Sepal Width (cm)")

# Boxplot
boxplot(Sepal.Length ~ Species, data = iris, main = "Sepal Length by Species")


### --- Lattice Graphics (`lattice` package) ---
install.packages("lattice") # Uncomment to install
library(lattice)

# Create a conditional scatterplot (trellis graph).
# This shows the relationship between Petal.Length and Sepal.Length,
# conditioned on the Species.
xyplot(
  Petal.Length ~ Sepal.Length | Species,
  data = iris,
  main = "Petal vs. Sepal Length by Species (Lattice)"
)


### --- ggplot2 Graphics (`ggplot2` package) ---
install.packages("ggplot2") # Uncomment to install
library(ggplot2)

# ggplot2 builds plots in layers based on the "grammar of graphics".
# 1. Start with ggplot(), defining the data and aesthetic mappings.
# 2. Add layers (geoms) to determine how the data is displayed.

# Simple scatterplot
ggplot(data = iris, mapping = aes(x = Sepal.Length, y = Petal.Length)) +
  geom_point() # Add a layer of points

# Add another aesthetic: map the 'Species' variable to the 'color' aesthetic.
ggplot(data = iris, mapping = aes(x = Sepal.Length, y = Petal.Length, color = Species)) +
  geom_point() +
  labs(
    title = "Iris Petal vs. Sepal Length (ggplot2)",
    x = "Sepal Length (cm)",
    y = "Petal Length (cm)"
  )

# Combine multiple geoms: add points and a smoothed line.
ggplot(data = iris, mapping = aes(x = Sepal.Length, y = Petal.Length, color = Species)) +
  geom_point() +
  geom_smooth(method = "lm") # Add a linear model smoothing line

# Faceted graphs: create subplots for each category (similar to lattice).
ggplot(data = iris, mapping = aes(x = Sepal.Length, y = Petal.Length)) +
  geom_point() +
  facet_wrap(~ Species) # Create a separate plot for each species
