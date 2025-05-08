# Election Exit Poll and Voter Prediction Model 
**Problem Statement :** You are hired by one of the leading news channels CNBE who wants to analyze recent elections. This survey was conducted on 1525 voters with 9 variables. You have to build a model, to predict which party a voter will vote for on the basis of the given information, to create an exit poll that will help in predicting overall win and seats covered by a particular party.

## Data Dictionary for Dataset

| Feature                       | Description                                                                                                      | Interpretation                                                                                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **`vote`**                    | The political party the voter supports. Values: `"Labour"` or `"Conservative"`                                   | This is your **target variable** — what you're trying to predict using all other features.                             |
| **`age`**                     | Age of the voter in years.                                                                                       | A numeric feature. Older or younger voters may prefer different parties.                                               |
| **`economic.cond.national`**  | Rating of the **country’s economic condition** (1–5 scale).                                                      | Subjective opinion: **1 = very bad**, **5 = very good**. May influence party preference based on national performance. |
| **`economic.cond.household`** | Rating of **personal/household financial situation** (1–5 scale).                                                | Also subjective: how well-off the respondent feels economically. Important for voter behavior.                         |
| **`Blair`**                   | How the respondent rates **Tony Blair**, leader of the Labour Party at the time (1–5 scale).                     | **1 = dislike very much**, **5 = like very much**. A high score suggests voter favors Labour.                          |
| **`Hague`**                   | Rating of **William Hague**, leader of the Conservative Party (1–5 scale).                                       | Similarly, **higher scores** suggest **preference for the Conservatives**.                                             |
| **`Europe`**                  | 11-point scale on attitude toward **European integration**. Higher = **more Eurosceptic** (less support for EU). | Political alignment with EU-related issues. Can influence support for parties based on EU stance.                      |
| **`political.knowledge`**     | How well the respondent understands each party’s EU position (0–3 scale).                                        | **0 = no knowledge**, **3 = high knowledge**. May correlate with how confidently a person votes.                       |
| **`gender`**                  | Gender of the voter: `"male"` or `"female"`.                                                                     | Used to analyze demographic influence on vote preference.                                                              |


💡 Example Interpretation:
A person who:

Rates Blair = 5, Hague = 1

Thinks national economy = 4, household = 4

Has low Euroscepticism (Europe = 2)
... is likely to vote Labour, based on ideology and leadership preference.

## Steps Performed
1. Data Loading and Initial Exploration
2. Dropping Irrelevant Column (Serial Number)
3. Checking for Duplicates and Removing Partial Duplicates
4. Exploratory Data Analysis (EDA): Generated Automated EDA Report using ydata-profiling
5. Outlier Detection via Boxplots
6. Encoding Categorical Variables (Vote and Gender)
7. Feature Scaling for Numerical Columns
8. Data Splitting (70 (Train) :30 (Test) with Stratification)
9. Model Building and Evaluation:
    - Logistic Regression
    - Linear Discriminant Analysis (LDA)
    - k-Nearest Neighbors (kNN)
    - Naive Bayes
    - Random Forest (Bagging)
    - General Bagging
    - Boosting (Adaptive Boosting)
10. Evaluation Metrics: Accuracy, Confusion Matrix, Classification Report
11. Final Model Selection and Conclusion


## Vote Share and Exit Poll Insights
- ### Labour has strong support and Vote Share.
    ![image](https://github.com/user-attachments/assets/8e891cc6-9850-4d5a-b19f-331deff32089)

- ### Female voters are more active and politically engaged in this dataset.
    ![image](https://github.com/user-attachments/assets/02017038-c2a1-4355-a918-436eb6719e27)

- ### Age-wise visualization showed younger and middle-aged groups favor Labour more.
    ![image](https://github.com/user-attachments/assets/c39b2b7b-8fbe-4f3e-ab87-24f9598e18ed)

- ### These trends suggest the Labour party's campaign had wider appeal and engagement. Clear Win of Labour Party.
    ![image](https://github.com/user-attachments/assets/b53f32c6-fd60-48db-b32e-3f7651b9de88)


## Exploratory Data Analysis (EDA)
See `Election_EDA_Report.html` for Automated EDA Report and EDA revealed the following insights:

✅ **Labour Party :**

 - Both females and males voted predominantly for Labour.

 - *Females cast more votes than males for Labour*.

 - Labour shows stronger appeal across all genders, particularly female voters.

✅ **Conservative Party :**

 - Overall, fewer votes were cast for Conservatives compared to Labour.

 - *Females again outvoted males for Conservatives, though the gap is smaller than in Labour.*

✅ **Overall Gender Voting Trend :**

 - *Female voters are more active than male voters* in this dataset (consistent with the previous bar chart: 808 females vs. 709 males).

 - Female votes outnumber male votes across both political parties.

 - Labour maintains broader gender support, while Conservative support is more limited and shows a lower male participation.

#### 📊  Age Group-Based Voting Trends :

**Younger Age Groups (18–30 and 31–45) :**

 - Show strong support for Labour, suggesting that younger voters lean more progressive or are more influenced by Labour’s messaging.

 - Labour gains a significant portion of its votes from these age groups.

**Middle Age Group (46–60) :**

 - Slightly more balanced between the two parties but still shows Labour in the lead.

 - This group might reflect working-class concerns that resonate more with Labour policies.

**Older Age Group (61+) :**

 - Conservative support increases slightly here, but Labour still maintains a lead.

 - This could suggest some generational alignment with traditional conservative values but not enough to surpass Labour.

#### 🎯 Conclusion :
The Labour Party dominates across both gender and age groups, making it the most popular party in this dataset and **Clear Win of Labour Party**.

 - **Female voters are the most engaged, casting more votes than males in both parties.**

 - **Labour’s success is especially strong among young voters**, while **Conservatives perform relatively better among older demographics**, but not enough to close the gap.

These trends could reflect differences in political priorities, outreach strategies, or social engagement patterns across demographics.

<br>

## Model Comparison and Inference

| Model                                  | Training Accuracy | Test Accuracy | Notes                                                        |
| -------------------------------------- | ----------------- | ------------- | ------------------------------------------------------------ |
| **Logistic Regression**                | 0.836             | 0.840         | Solid baseline; balanced precision/recall.                   |
| **Linear Discriminant Analysis (LDA)** | 0.838             | 0.842         | Slightly better than logistic regression; well balanced.     |
| **k-Nearest Neighbors (kNN)**          | 0.852             | 0.836         | Highest training accuracy (risk of overfitting).             |
| **Naive Bayes**                        | 0.825             | 0.844         | Lowest training accuracy but good generalization.            |
| **Random Forest (n=1000)**             | —                 | 0.827         | Stable and robust, but slightly underperforms others.        |
| **Bagging (n=1000)**                   | —                 | 0.827         | Similar to Random Forest, consistent but not top-performing. |
| **Adaptive Boosting (n=1000)**                  | —                 | **0.849**     | ⭐ Best test accuracy; strong performance overall.            |


Among all models, Boosting delivered the highest test accuracy (84.9%), indicating that it is the best performing model for this dataset. 

 ### Inference
  -	Adaptive Boosting outperformed all other models in terms of test accuracy (84.9%), making it the best overall. It achieved a good balance of precision and recall.
  -	Naive Bayes surprised with a strong test performance despite a lower training score — indicating excellent generalization.
  -	LDA and Logistic Regression were also strong contenders with consistent and high accuracy, showing they are still competitive for linear separability.
  -	kNN had the highest training accuracy, suggesting it might be overfitting slightly — as its test accuracy dropped a bit.
  -	Random Forest and Bagging had solid but slightly lower performance, possibly due to parameter defaults or redundancy in tree-based ensembles for this dataset.
### Conclusion
  -	Best Performing Model: Boosting — **Adaptive Boosting** — due to its superior accuracy and f1-score.
  -	**Caution :** Models like kNN and Random Forest can overfit if hyperparameters aren’t tuned.
  -	Recommended Final Model: Boosting, with potential tuning for learning_rate and n_estimators=1000.

## Streamlit Deployment
A user-friendly Streamlit web application was created to allow users to input voter features and get real-time predictions using the trained AdaBoost model `voter_model.pkl`.

<br>

![image](https://github.com/user-attachments/assets/32244535-e50f-47f6-8424-fc7dc96670f1)

