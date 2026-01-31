# Recipe Feature Engineering Pipeline

## AI & Business - Data Preprocessing & Feature Engineering Assignment

---

## Assignment Overview

In this assignment, you will apply data preprocessing and feature engineering techniques to a real-world recipe dataset containing **5,000 recipes** with various ingredients, nutritional information, and metadata. The dataset has been sourced from multiple cooking platforms and contains several data quality issues that you must identify and resolve.

**Learning Objectives:**

- Identify and handle missing data using appropriate imputation techniques
- Detect and treat outliers in numerical features
- Address data inconsistencies and formatting issues
- Create meaningful derived features through feature engineering
- Apply data transformation techniques (normalization, encoding)
- Handle class imbalance in categorical variables
- Document your data cleaning process and decisions

---

## Dataset Description

**File:** `recipes_raw_data.csv`  
**Total Records:** 5,000 recipes  
**Source:** Aggregated from multiple online recipe databases

### Columns:

| Column Name          | Data Type | Description                                             |
| -------------------- | --------- | ------------------------------------------------------- |
| recipe_id            | String    | Unique identifier for each recipe                       |
| recipe_name          | String    | Name of the recipe                                      |
| category             | String    | Recipe category (Breakfast, Lunch, Dinner, etc.)        |
| cuisine              | String    | Cuisine type (Italian, Mexican, Chinese, etc.)          |
| dietary_restrictions | String    | Dietary category (Vegetarian, Vegan, Gluten-Free, etc.) |
| difficulty           | String    | Difficulty level (Easy, Medium, Hard, Expert)           |
| prep_time_mins       | Integer   | Preparation time in minutes                             |
| cook_time_mins       | Integer   | Cooking time in minutes                                 |
| total_time_mins      | Integer   | Total time (prep + cook)                                |
| servings             | Integer   | Number of servings                                      |
| calories             | Integer   | Calories per serving                                    |
| protein_g            | Float     | Protein content in grams                                |
| carbs_g              | Float     | Carbohydrate content in grams                           |
| fat_g                | Float     | Fat content in grams                                    |
| rating               | Float     | Average user rating (1-5 scale)                         |
| num_reviews          | Integer   | Number of user reviews                                  |
| ingredients          | String    | Comma-separated list of ingredients                     |
| equipment_needed     | String    | Required kitchen equipment                              |
| author               | String    | Recipe author name                                      |
| date_added           | String    | Date recipe was added to database                       |

---

## Part 1: Data Quality Assessment (20 points)

### Task 1.1: Exploratory Data Analysis

Load the dataset and perform initial exploration:

**Your Tasks:**

1. Load the data into a Pandas DataFrame
2. Display basic statistics (shape, info, describe)
3. Identify columns with missing values and calculate missing percentages
4. Create a visualization showing missing data patterns
5. Identify potential duplicate records

**Questions to Answer:**

- How many missing values exist in each column?
- Which columns have the highest percentage of missing data?
- Are there any patterns in the missing data?
- How many duplicate recipes exist?

**Document your findings here:**

```
[Student writes findings]
```

---

### Task 1.2: Data Quality Issues Identification

Identify all data quality problems in the dataset:

**Your Tasks:**

1. Check for negative values in numerical columns (time, servings, calories, nutrients)
2. Identify unrealistic values (e.g., cooking times over 500 minutes, calories over 5000)
3. Find inconsistent formatting in text columns (author names, ingredients, dates)
4. Detect outliers using statistical methods (IQR, Z-score)
5. Check for rating values outside the 1-5 range

**Document issues found:**

```
Issue 1: [Describe issue]
Affected Columns: [List columns]
Number of Records: [Count]

Issue 2: [Describe issue]
...
```

---

## Part 2: Data Cleaning & Preprocessing (40 points)

### Task 2.1: Handling Missing Data

Apply appropriate strategies for each column with missing values:

**Your Tasks:**

1. **Numerical columns** (prep_time, cook_time, calories, nutrients):
   - Decide between mean, median, or mode imputation
   - Justify your choice based on data distribution
   - Consider creating a "missing indicator" flag

2. **Categorical columns** (ingredients, equipment, author):
   - Decide between imputation or deletion
   - Consider creating an "Unknown" category

3. **Date column**:
   - Handle inconsistent date formats
   - Impute missing dates if necessary

**Implementation Notes:**

```python
# Example approach for numerical imputation
# [Student implements here]
```

**Justification for your imputation choices:**

```
[Student explains reasoning]
```

---

### Task 2.2: Handling Invalid & Outlier Values

**Your Tasks:**

1. **Negative values**: Replace or remove negative values in:
   - prep_time_mins, cook_time_mins
   - servings, calories
   - protein_g, carbs_g, fat_g
   - rating, num_reviews

2. **Out-of-range values**:
   - Fix ratings outside 1-5 range
   - Cap or remove unrealistic cooking times (>500 mins)
   - Handle extreme calorie values (>5000 or <50)

3. **Outliers**:
   - Use IQR method or Z-score to detect outliers
   - Decide whether to cap, transform, or remove them
   - Document your threshold decisions

**Implementation Strategy:**

```python
# [Student implements outlier detection and handling]
```

---

### Task 2.3: Data Standardization & Formatting

**Your Tasks:**

1. **Text standardization**:
   - Standardize author names (handle case sensitivity)
   - Standardize ingredient separators (some use ';' instead of ',')
   - Clean equipment_needed formatting

2. **Date formatting**:
   - Convert all dates to consistent format (YYYY-MM-DD)
   - Handle multiple date formats in the dataset

3. **Categorical consistency**:
   - Ensure consistent capitalization in categories
   - Check for duplicate categories with different spellings

**Code Implementation:**

```python
# [Student implements standardization]
```

---

### Task 2.4: Duplicate Removal

**Your Tasks:**

1. Identify duplicate recipes based on:
   - Recipe name AND ingredients
   - Consider recipes as duplicates if both match
2. Decide on deduplication strategy (keep first, keep last, keep highest rated)
3. Remove duplicates and document how many were removed

**Implementation:**

```python
# [Student implements deduplication]
```

---

## Part 3: Feature Engineering (30 points)

### Task 3.1: Create Numerical Derived Features

**Your Tasks - Create the following new features:**

1. **time_per_serving**: Total cooking time divided by servings
2. **calories_per_minute**: Calories divided by total cooking time
3. **protein_ratio**: Protein grams as percentage of total macronutrients
4. **carbs_ratio**: Carbs as percentage of total macronutrients
5. **fat_ratio**: Fat as percentage of total macronutrients
6. **total_macros**: Sum of protein, carbs, and fat
7. **ingredient_count**: Number of ingredients (count items in ingredients list)
8. **equipment_count**: Number of equipment items needed
9. **complexity_score**: Create a composite score based on:
   - Number of ingredients
   - Difficulty level
   - Total cooking time
10. **popularity_score**: Create a score based on:
    - Rating
    - Number of reviews

**Implementation:**

```python
# [Student creates derived features]
```

**Explain your approach for complexity_score and popularity_score:**

```
[Student explanation]
```

---

### Task 3.2: Create Categorical Derived Features

**Your Tasks:**

1. **time_category**: Bin total_time_mins into categories:
   - Quick: 0-30 mins
   - Medium: 31-60 mins
   - Long: 61-120 mins
   - Very Long: >120 mins

2. **calorie_category**: Create health-conscious categories:
   - Low: <300 calories
   - Medium: 300-600 calories
   - High: >600 calories

3. **serving_size**: Categorize servings:
   - Individual: 1-2 servings
   - Small Group: 3-4 servings
   - Large Group: 5+ servings

4. **recipe_age_days**: Calculate days since recipe was added

5. **is_healthy**: Binary flag based on:
   - Calorie count
   - Protein ratio
   - Your defined criteria for "healthy"

**Implementation:**

```python
# [Student creates categorical features]
```

---

### Task 3.3: Text Feature Engineering

**Your Tasks:**

1. **Create binary ingredient flags** for common ingredients:
   - has_chicken, has_beef, has_pork, has_fish
   - has_cheese, has_milk
   - has_gluten (based on ingredients like flour, bread, pasta)

2. **Extract cuisine-specific patterns**:
   - is_asian_cuisine (Chinese, Japanese, Korean, Thai, Vietnamese)
   - is_european_cuisine (Italian, French, Greek, Spanish)

3. **Count ingredient categories**:
   - num_proteins (count protein ingredients)
   - num_vegetables (count vegetable ingredients)
   - num_spices (count spice ingredients)

**Implementation:**

```python
# [Student implements text feature extraction]
```

---

### Task 3.4: Feature Encoding

**Your Tasks:**

1. **One-hot encoding** for:
   - category
   - cuisine
   - difficulty
   - dietary_restrictions

2. **Label encoding** for:
   - time_category
   - calorie_category
   - serving_size (ordinal)

3. **Handle high-cardinality features**:
   - Consider grouping rare categories
   - Use frequency encoding for author if needed

**Implementation:**

```python
# [Student implements encoding]
```

---

### Task 3.5: Feature Scaling & Normalization

**Your Tasks:**

1. **Normalize** the following features to 0-1 range:
   - prep_time_mins, cook_time_mins
   - calories
   - All nutrient features (protein_g, carbs_g, fat_g)

2. **Standardize** (z-score) the following:
   - rating
   - num_reviews
   - All derived ratio features

3. **Explain your choice** of normalization vs standardization for each group

**Implementation:**

```python
# [Student implements scaling]
```

**Justification:**

```
[Student explains why different scaling methods were chosen]
```

---

## Part 4: Data Quality Validation (10 points)

### Task 4.1: Post-Processing Validation

**Your Tasks:**

1. Verify no missing values remain (or document why some remain)
2. Confirm all numerical values are within expected ranges
3. Verify all dates are in consistent format
4. Check that all categorical encodings are correct
5. Ensure no duplicate records remain
6. Validate that engineered features are calculated correctly (spot check)

**Validation Results:**

```python
# [Student implements validation checks]
```

**Final Data Quality Report:**

```
Total Records: [Count]
Missing Values: [Summary]
Duplicates Removed: [Count]
Outliers Handled: [Count]
Features Created: [Count]
Final Feature Count: [Count]
```

---

## Part 5: Documentation & Insights (Bonus 10 points)

### Task 5.1: Create Data Pipeline Summary

**Your Tasks:**

1. Create a visual diagram or flowchart showing your entire preprocessing pipeline
2. Document key decisions and their justifications
3. Provide recommendations for ML model use cases with this data

**Pipeline Documentation:**

```
[Student creates pipeline diagram or detailed description]
```

---

### Task 5.2: Generate Insights

**Your Tasks:**

Answer the following questions using your cleaned dataset:

1. What is the most common cuisine type?
2. What is the average cooking time by difficulty level?
3. Which dietary restriction has the highest average rating?
4. Is there a correlation between number of ingredients and recipe rating?
5. What percentage of recipes are "healthy" based on your criteria?

**Insights:**

```
[Student provides analysis and insights]
```

---

## Submission Requirements

### Required Files:

1. **Cleaned dataset**: `recipes_cleaned.csv`
2. **Python script**: `recipe_feature_engineering.py` (with all your code)
3. **This completed document**: `assignment_submission.md` or `.pdf`
4. **Optional**: Jupyter notebook with exploratory analysis

### Code Requirements:

- Well-commented code explaining each step
- Use of functions for reusable data cleaning operations
- Proper error handling
- Clear variable naming

### Documentation Requirements:

- Explanation of all major decisions
- Justification for imputation methods, outlier handling, and feature engineering choices
- Summary statistics before and after cleaning
- List of all created features with descriptions

---

## Grading Rubric

| Section                 | Points        | Criteria                                                        |
| ----------------------- | ------------- | --------------------------------------------------------------- |
| Data Quality Assessment | 20            | Thorough identification of all issues, clear documentation      |
| Data Cleaning           | 40            | Appropriate handling of missing data, outliers, inconsistencies |
| Feature Engineering     | 30            | Creative and meaningful derived features, proper encoding       |
| Validation              | 10            | Complete validation of cleaned data                             |
| **Bonus**               | 10            | Pipeline documentation and insights                             |
| **Total**               | **100 (+10)** |                                                                 |

### Grading Notes:

- **Excellent (90-100)**: All issues identified and resolved appropriately, creative feature engineering, well-documented
- **Good (80-89)**: Most issues handled correctly, standard feature engineering, adequate documentation
- **Satisfactory (70-79)**: Basic cleaning completed, minimal feature engineering, basic documentation
- **Needs Improvement (<70)**: Missing significant issues, incomplete feature engineering, poor documentation

---

## Tips for Success

1. **Start with EDA**: Understand your data before making changes
2. **Document as you go**: Don't wait until the end to document decisions
3. **Think about the end use**: Feature engineering should support ML model goals
4. **Validate frequently**: Check your work after each major transformation
5. **Use version control**: Save intermediate versions of your data
6. **Consider domain knowledge**: Think about what makes sense for recipes
7. **Be consistent**: Apply the same logic to similar problems
8. **Test edge cases**: What happens with missing values, zero values, etc.?

---

## Resources

### Recommended Python Libraries:

- `pandas`: Data manipulation
- `numpy`: Numerical operations
- `scikit-learn`: Preprocessing, scaling, encoding
- `matplotlib`/`seaborn`: Visualization
- `missingno`: Missing data visualization

### Reference Documentation:

- Pandas documentation: https://pandas.pydata.org/docs/
- Scikit-learn preprocessing: https://scikit-learn.org/stable/modules/preprocessing.html
- Study guide: https://fiveable.me/artificial-intelligence-in-business/unit-7/data-preprocessing-feature-engineering/study-guide/sxayo7SASUAWyFEG

---

## Academic Integrity

This is an individual assignment. You may:

- Use online documentation and tutorials
- Discuss general concepts with classmates
- Ask the instructor for clarification

You may NOT:

- Copy code from classmates
- Share your completed code with others
- Use AI tools to complete the assignment without understanding the code

By submitting this assignment, you affirm that this work is your own and that you have not given or received unauthorized assistance.

**Student Signature:** **********\_\_\_**********  
**Date:** **********\_\_\_**********

---

**Good luck! Remember: The goal is not just to clean the data, but to understand WHY you're making each decision and HOW it will impact downstream ML models.**
