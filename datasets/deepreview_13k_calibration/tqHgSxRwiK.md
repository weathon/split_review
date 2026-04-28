# Test Relative Fairness in Human Decisions With Machine Learning

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
Fairness in decision-making has been a long-standing issue in our society. Compared to algorithmic fairness, fairness in human decisions is even more important since there are processes where humans make the final decisions and that machine learning models inherit bias from the human decisions they were trained on. However, the standard for fairness in human decisions are highly subjective and contextual. This leads to the difficulty for testing ``absolute'' fairness in human decisions. To bypass this issue, this work aims to test relative fairness in human decisions. That is, instead of defining what are ``absolute'' fair decisions, we check the relative fairness of one decision set against another. An example outcome can be: Decision Set A favors female over male more than Decision Set B. Such relative fairness has the following benefits: (1) it avoids the ambiguous and contradictory definition of ``absolute'' fair decisions; (2) it reveals the relative preference and bias between different human decisions; (3) if a reference set of decisions is provided, relative fairness of other decision sets against this reference set can reflect whether those decision sets are fair by the standard of that reference set. We define the relative fairness with statistical tests (null hypothesis and effect size tests) of the decision differences across each sensitive group. 
  Furthermore, we show that a machine learning model trained on the human decisions can inherit the bias/preference and therefore can be utilized to estimate the relative fairness between two decision sets made on different data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In fair classification, it is difficult or even ill-defined to have "true labels" for complex, subjective decision-making tasks. Hence, the paper proposes a relative notion of fairness. Operationally, for a pair of classifiers (people or algorithms), the paper tests for demographic parity (fraction of positives between two groups) between the two classifiers. The paper further considers a setting where the two classifiers make predictions (Y1 and Y2) on different datasets (X1 and X2). To apply the test, the paper trains a predictor on (X1, Y1), and use it to impute the first classifier's predictions on X2. The paper provides experimental results for the proposed methods on real datasets, in which the bias either exists in the data or is simulated.

### Strengths
1. In fairness research, it is important to think about the fairness notions carefully. The paper proposes a natural notion based on comparing a pair of classifiers in a relative sense, surpassing the need to define "true labels" which can be ambiguous or even infeasible in many applications.

2. The paper uses real data to evaluate the proposed method.

### Weaknesses
1. Methodology
Many data statistics have been used as the notion of fairness. Prior literature suggests that choosing which one to use requires careful thoughts. The paper should justify the choice of demographic parity, and ideally, provides comments on whether the proposed algorithms can generalize to other data statistics. The paper does not adequately address the limitations of demographic parity, particularly in scenarios where the sensitive attribute is correlated with factors that legitimately influence the outcome. This raises concerns about the practical applicability of the proposed methods in real-world settings where such correlations are common. Furthermore, the paper should discuss how the proposed framework could be adapted to other fairness metrics, such as equal opportunity or predictive parity, and what challenges might arise in doing so.

2. Novelty
Literature on individual fairness and label imputation should be overviewed:

(a) While the proposed relative comparison is natural, this idea of relative comparison is similar in spirit to individual fairness, in which "true labels" are also unnecessary. The paper needs to more clearly articulate how the proposed approach differs from existing individual fairness metrics, especially in terms of its underlying assumptions and practical implications. The connection to counterfactual fairness should also be explored, as it also deals with comparing outcomes under different conditions.

(b) I appreciate simplicity in general, but I struggle to see the two proposed algorithms as "novel" as the paper has claimed. Essentially the paper trains a predictor to impute missing labels. The paper does not sufficiently address the existing literature on label imputation, particularly methods that account for uncertainty in the imputed labels. The proposed algorithms appear to be a straightforward application of existing imputation techniques, and the paper needs to demonstrate a clear advantage over these methods.

To these ends, I fail to see a clear main contribution of the paper: the formulation and ideas are not entirely novel; the theoretical result (Prop 4.5) is very weak; and the experimental results also need improvement (detailed in "Experiments").

3. Mathematical formulation
I find the mathematical formulation presentation quite loose:

(a) Def 4.1 is based on "equality in distribution". What is the source of randomness? I suppose it's the distribution of data X, but it is not formally stated that X is random. The definition needs to be more precise about the underlying probability space and the random variables involved. It is unclear whether the equality in distribution is meant to hold for all possible values of the sensitive attribute, or only for some specific values. This lack of clarity makes it difficult to interpret the definition and its implications.

(b) I find Assumption 4.2 quite problematic and unjustified. The assumption is on a complicated quantity (Y_\Delta(A=a)), and I fail to understand what this assumption fundamentally means. I especially struggle with Eq. 6, where normality is claimed without having any assumption on the function f or the classifiers (Y0 and Y1). The assumption is not only unjustified but also seems overly restrictive. The paper needs to provide a theoretical justification for this assumption, or at least discuss the situations where it might be reasonable to assume. The claim of normality in Eq. 6 is particularly problematic, as it is not clear why the difference of two arbitrary classifiers should follow a normal distribution.

Is this the law of large numbers? Then the source of randomness needs to be defined. The assumption of large samples also in a certain sense defeats the purpose of label imputation in the "unbiased bridge" algorithm. One can just compute and compare the data statistics on (X1, Y1) and (X2, Y2) separately. The paper needs to clarify the role of the large sample assumption and explain why label imputation is still necessary in this setting. The connection between the large sample assumption and the proposed algorithms is not clear.

(c) I am confused about the correctness of Prop 4.5. In order to show equality in Def 4.1, under Assumption 4.2, should both equal mean and equal variance be required? Does RBT=RBD=0 only implies equal mean? Since the assumptions are very restrictive, this result somewhat feels like a tautology. The paper should clearly state whether the equality in distribution requires both equal mean and variance, and provide a rigorous proof of Prop 4.5. The current presentation is unclear and does not provide sufficient justification for the result.

(d) Minor
- In Def 4.3, the mean and variance should be called "empirical mean" and "empirical variance".
- It should be made clear early in Sec 4 that Y is binary {0, 1}.
- In Eq. 9, what is \overline{f}?

4. Experiments
(a) I find that there is a non-trivial gap between the experimental setup, and the setting that the algorithms are introduced in. The problem is motivated by bypassing the need to define "true labels". However, the experiment still simulates settings that have these true labels. This also happens in Step 0 in in the motivating example of Section 3. The experimental setup does not align with the core motivation of the paper, which is to avoid the need for true labels. The paper needs to provide a more compelling experimental setup that demonstrates the usefulness of the proposed methods in scenarios where true labels are not available. The current experiments are not convincing and do not adequately support the claims made in the paper.

(b) The experiment setup needs to be described in more detail. For example, I don't understand two equations for the injection procedure. What does \overline{Y}_1 = \overline{Y}_0 mean? How is the mean of the Gaussian computed, since there are values of \lambda (separately for sex and race). What z(a) means also needs to be explained. The description of the experimental setup is insufficient and lacks important details. The paper needs to provide a clear and precise explanation of the data generation process, including the meaning of all parameters and variables. The current description is confusing and makes it difficult to reproduce the experiments.

(c) Rigor: The paper needs to describe if multiple hypothesis testing is accounted.

(d) Presentation: The experimental results can be better presented by figures. The tables are very dense to parse.

5. Grammar:
- Title: "test" -> testing
- Abstract: "decisions sets"
- P2: "what are absolutely fair decisions" -> what absolutely fair decisions are
- P2: "present" -> presence
- P2: "Homan and others" -> refer to papers by the first author
- P7: "least beautify"

### Questions
Clarifications on Weaknesses 3(a, b, c), 4(a, b, c) would be the most helpful.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a different perspective of measuring fair decision-making by computing the fairness difference between decision sets made by various decision-makers. The authors evaluate the proposed approach on UCI-adult income and SCUT-FB500 face beauty datasets.

### Strengths
I like this perspective of measuring fair decision-making since there is potential to tap into often ignored aspects of decision-making: varied decision-maker biases and contextual differences.

### Weaknesses
While I liked the high-level idea, I think the problem modeling and presentation need some improvements. Below are the observed weaknesses (and respective suggestions) and some questions. 

- The examples and general presentation of the paper are not easy to follow. For example, the authors mention various non-complementary examples, which doesn't help drive the idea home. The annotator bias example points more towards the setting of different (ideologically/demographically) decision-makers and the same dataset (e.g., platform content) or different datasets (e.g., different sub-reddit data/ different parts of X). On the other hand, the motivating example looks at multiple experts (>2, as is in the methodology) who are similar (ideologically) on the same dataset (similar features selected by a hiring company.). In general, the examples don't support or complement the methodology. Authors should pick an intuitive running example that supports the main idea.  

- There is lots of inconsistency in writing. For example, the authors mention that they use different and same datasets in various parts of the write-up, which makes reading the paper hard. From my understanding, the authors use the same (exact) dataset and use part of the dataset as X_{0} (training set) and the other as X_{1} (validation set). Authors should aim for consistency in writing to improve readership. 

- Although I liked the idea, it does look like theory and empirical designs don't support the goal. The definition of relative fairness would have been more robust and intuitive if the definition had constraints specific to decision-makers and data distributions. I believe varied constraint values significantly change the problem. The authors use historical datasets with no information on how/who collected the datasets, which is critical to the suggested framework.  Although individuals might be different by A/B, they might be ideologically/demographically or contextually (biasedly) similar, which changes the idea of the relative fairness subject to "different" decision-makers. Additionally, the authors use a beauty dataset which is somewhat not ethically a great decision, and mention that the adult dataset comes from truth and is, therefore, 100% fair, which is unrealistic and unverified.  

  -  Authors should redefine (add constraints) relative fairness and respective terms and change datasets by using semi-synthetic datasets or conducting human subject studies to collect data. For example, authors could get content from different platforms or the same platform but different communities, and solicit for classifications from clearly different groups, e.g., 18-26 years and 27- 45 year-olds. 
  -  Lastly, the methodology seems flawed to me, since the ML model and X_{0} biases are propagated and possibly amplified to decisions on X_{1}. Currently, it looks like authors view {X_{0}, Y_{0}} as ground truth for desigining f(x) which is then used on {X_{1}, Y_{1}}. I think instead, there should be a benchmark, for example, assuming you have information {X, Y} on prospective students, and you want to measure relative fairness. Then curate a distinct group A to classify X to get Y_{A}, and another group B to classify X to get Y_{B}. Then measure the relative fairness of the two decision sets. 

- Although the authors cite some relevant literature, the literature review/related work section needs improvement. The section should be more cohesive and concise and clearly indicate the paper's strength and position in related works. 

- The way authors mention their contributions is not complementary to the idea and their work. The authors should restructure this section and make it stronger. Additionally, the authors mention that they show that a machine-learning model trained on human decisions can inherit bias/preference. This is not novel and is the motivation for most of the fairness in ML work. For example, several works on feedback loops and bail/justice systems show this. 

- Since authors define relative fairness as the statistical difference of the delta of two sets of decisions over a certain sensitive attribute, would it be reasonable to assume absolute fairness is particular to one decision set? Does it mean absolute fairness is a sub-routine of relative fairness?

### Questions
I like the idea but the paper presentation and methodology (theory and experiments) need some improvement. I have outlined some of these issues and made suggestions in the weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a method to compute the relative fairness between two sets of decisions. The paper presents a couple of metrics to compute the relative fairness of the decisions. If one of the decision sets is incomplete the paper proposes to leverage a ML model to regress the ground truth decisions onto the unlabeled set. The paper presents two approaches to perform the same using an unbiased and a biased bridge. Empirical results show that the proposed metrics are consistent with the ground truth scores.

### Strengths
1. The paper is fairly easy to follow.
2. The notion of relative fairness is novel.

### Weaknesses
1. The premise and contribution of the paper is unclear to me. Specifically, the utility and application of the proposed metrics need more clarification. As I understand relative fairness is useful when comparing two decision sets. But if both decision sets are biased and the relative fairness is near zero, what does that tell us? It seems like this could indicate a consistent bias, but the paper does not explore this implication. The practical value of this scenario is not clear.
2. Relative fairness as presented in the paper is simply the difference between statistical parity (with some normalization) of each decision set. Why can't we just rely on the absolute statistical parity? It provides a more granular and absolute measure of fairness. Why do we need relative fairness or what extra information does that provide us? The paper does not adequately justify the need for a relative measure over the absolute one, especially given the potential for both sets to be biased.
3. It is unclear to me why ML models are being used to approximate the decisions on an unlabeled set. If a small set of human decisions is available, why can't we just evaluate the absolute fairness of that set? The function f can be prone to a range of implicit biases of its own and the results of the proposed metrics can heavily rely on the parameterization of f. This introduces a significant source of uncertainty and potential for skewed results. The paper does not sufficiently address the sensitivity of the results to the choice of the ML model and its potential biases.
4. One of the use cases of relative fairness is when the fairness of the decisions suddenly changes over time. Even then it is unclear to me how relative fairness is useful over standard statistical parity. If fairness changes over time, wouldn't it be more informative to track the absolute statistical parity at different time points? The relative measure seems less informative in this context.

### Questions
1. Table 3 and 4 are quite hard to read. What do the values in brackets indicate? Are those the p-values?
2. Please respond to the comments in the weakness section as well.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
