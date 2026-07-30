# Statistics

Statistics is the **science of collecting, organizing, summarizing, analyzing, and interpreting data**.

It helps us identify **patterns, trends, and relationships** in data so that we can make informed decisions.

---

# Types of Statistics

## 1. Descriptive Statistics

Descriptive statistics summarize and describe the main features of a dataset.

It helps us understand the data using measures such as mean, median, mode, charts, and graphs.

---

## 2. Inferential Statistics

Inferential statistics use **sample data** to make predictions or draw conclusions about a larger population.

It helps predict what may happen in the future or estimate unknown information about a population.

---

# Basic Statistical Terms

## Population

A **population** is the complete collection of individuals or items being studied.

---

## Sample

A **sample** is a smaller group selected from the population for analysis.

---

## Variable

A **variable** is any characteristic or value that can change from one observation to another.

Examples include age, height, salary, and marks.

---

## Data

- **Datum** – A single value or observation.
- **Data** – A collection of observations.

---

## Experiment

An experiment is a process performed to collect data or test a hypothesis.

---

## Parameter

A **parameter** is a numerical value that describes a population.

Examples include population mean and population standard deviation.

---

## Statistic

A **statistic** is a numerical value calculated from a sample.

It is used to estimate the corresponding population parameter.

---

# Types of Data

## 1. Categorical (Qualitative) Data

Categorical data represents characteristics or categories rather than numerical values.

### Nominal Data

Nominal data consists of categories with **no specific order**.

Examples:

- Seasons
- Colours
- Gender
- Blood Group

---

### Ordinal Data

Ordinal data consists of categories that **have a meaningful order or ranking**.

Examples:

- Class rankings
- Customer satisfaction (Poor, Good, Excellent)
- Education levels

---

## 2. Numerical (Quantitative) Data

Numerical data consists of values that can be measured or counted.

---

### Discrete Data

Discrete data consists of **countable values**.

Examples:

- Number of students
- Number of cars
- Number of books

---

### Continuous Data

Continuous data consists of **measurable values**.

Examples:

- Height
- Weight
- Temperature
- Distance

---

# Levels of Quantitative Data

## Interval Scale

Interval data has equal intervals between values but **does not have a true zero**.

Examples:

- Temperature in Celsius
- Temperature in Fahrenheit

---

## Ratio Scale

Ratio data has equal intervals and **a true zero value**.

Examples:

- Age
- Income
- Weight
- Height
- Number of children

---

# Measures of Central Tendency

Measures of central tendency describe the **center or typical value** of a dataset.

---

## Mean

The **mean** is the average of all observations.

It is calculated by adding all values and dividing by the number of observations.

**Note:** Mean is affected by **outliers**, so it can be easily influenced by extremely large or small values.

---

## Median

The **median** is the middle value after arranging the data in ascending order.

If the dataset contains an even number of observations, the median is the average of the two middle values.

Median is **less affected by outliers**, making it a safer measure when extreme values are present.

---

## Mode

The **mode** is the value that occurs **most frequently** in a dataset.

A dataset may have:

- One mode (Unimodal)
- Two modes (Bimodal)
- More than two modes (Multimodal)

---

# Measures of Dispersion

Measures of dispersion describe **how spread out the data values are**.

They indicate how much the observations vary from the center.

Common measures include:

- Range
- Variance
- Standard Deviation
- Interquartile Range (IQR)

---

# Standard Deviation

Standard deviation measures **how far the data values are from the mean**.

- Small standard deviation → Data is close to the mean.
- Large standard deviation → Data is widely spread.

---

# Distribution

A distribution describes **how data values are spread**.

---

## Symmetrical Distribution

In a symmetrical distribution:

- Mean = Median = Mode

The graph forms a **bell-shaped curve**.

The skewness is **zero**.

---

## Left-Skewed Distribution (Negative Skew)

The tail of the distribution extends towards the **left**.

Most observations are concentrated on the right side.

Generally:

**Mean < Median < Mode**

---

## Right-Skewed Distribution (Positive Skew)

The tail of the distribution extends towards the **right**.

Most observations are concentrated on the left side.

Generally:

**Mean > Median > Mode**

---

# Quartiles

Quartiles divide the data into **four equal parts**.

- Q1 → 25%
- Q2 → 50% (Median)
- Q3 → 75%
- Q4 → 100%

---

# Interquartile Range (IQR)

The Interquartile Range measures the spread of the **middle 50%** of the data.

Formula:

```text
IQR = Q3 − Q1
```

---

# Lower Bound

Used to identify lower outliers.

Formula:

```text
Lower Bound = Q1 − (1.5 × IQR)
```

---

# Upper Bound

Used to identify upper outliers.

Formula:

```text
Upper Bound = Q3 + (1.5 × IQR)
```

---

# Z-Score (Standard Score)

A Z-score tells **how many standard deviations a value is from the mean**.

Formula:

```text
Z = (X − Mean) / Standard Deviation
```

Where:

- X = Data value
- Mean = Average
- Standard Deviation = Spread of data

---

# Outlier Treatment

## Capping

Capping replaces extremely high or low values with predefined maximum or minimum limits.

It reduces the effect of outliers without removing data.

---

## Binning

Binning groups continuous data into intervals (bins).

Instead of analysing individual values, analysis is performed on the groups.

---

# Probability Distribution

A probability distribution describes **how probabilities are assigned to different possible values of a random variable**.

---

## Probability Density Function (PDF)

A Probability Density Function (PDF) describes the probability distribution of a **continuous random variable**.

The total area under the curve is always equal to **1**.

---

# Types of Probability Distribution

## Bernoulli Distribution

Bernoulli distribution represents an experiment with **only two possible outcomes**.

Examples:

- Success or Failure
- Yes or No
- True or False

---

## Binomial Distribution

Binomial distribution describes the probability of obtaining a fixed number of successes in a fixed number of independent Bernoulli trials.

---

## Poisson Distribution

Poisson distribution measures the probability of a given number of events occurring within a fixed interval of time or space.

---

## Uniform Distribution

Uniform distribution is a distribution where **every outcome has an equal probability**.

---

# Central Limit Theorem (CLT)

The Central Limit Theorem states that **when the sample size is sufficiently large, the sampling distribution of the sample mean approaches a normal distribution**, regardless of the population's original distribution.

It is one of the most important concepts in statistics.

---

# Hypothesis Testing

Hypothesis testing is a statistical method used to determine whether there is enough evidence to support or reject a claim about a population.

---

# Z-Test

A Z-test is used to compare sample data with a population when:

- The population standard deviation is known.
- The sample size is generally large (n ≥ 30).

---

# T-Test

A T-test is used to compare means when:

- The population standard deviation is unknown.
- The sample size is relatively small.

---

# Independent T-Test

An Independent T-Test compares the means of **two independent groups** to determine whether they are significantly different.

---

# Variance

Variance measures **how far each data value is from the mean**.

It is the average of the squared differences from the mean.

Standard deviation is calculated using variance.

---

# Relationship Between Variance and Standard Deviation

- Variance measures the spread using squared units.
- Standard deviation is the square root of variance.
- Standard deviation is easier to interpret because it is in the same units as the original data.

---

# Data Analysis

Data analysis is the process of:

- Collecting data
- Cleaning data
- Organizing data
- Analysing patterns
- Drawing conclusions
- Making informed decisions

It helps transform raw data into meaningful information.
