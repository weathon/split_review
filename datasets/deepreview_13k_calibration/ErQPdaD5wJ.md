# AutoUAD: Hyper-parameter Optimization for Unsupervised Anomaly Detection

- Decision: Accept
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
Unsupervised anomaly detection (UAD) has important applications in diverse fields such as manufacturing industry and medical diagnosis. In the past decades, although numerous insightful and effective UAD methods have been proposed, it remains a huge challenge to tune the hyper-parameters of each method and select the most appropriate method among many candidates for a specific dataset, due to the absence of labeled anomalies in the training phase of UAD methods and the high diversity of real datasets. In this work, we aim to address this challenge, so as to make UAD more practical and reliable. We propose two internal evaluation metrics, \textit{relative-top-median} and \textit{expected-anomaly-gap}, and one semi-internal evaluation metric, \textit{normalized pseudo discrepancy} (NPD), as surrogate functions of the expected model performance on unseen test data. For instance, NPD measures the discrepancy between the anomaly scores of a validation set drawn from the training data and a validation set drawn from an isotropic Gaussian. NPD is simple and hyper-parameter-free and is able to compare different UAD methods, and its effectiveness is theoretically analyzed. We integrate the three metrics with Bayesian optimization to effectively optimize the hyper-parameters of UAD models. Extensive experiments on 38 datasets show the effectiveness of our methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Unsupervised anomaly detection (UAD) faces challenges in model selection and hyper-parameter tuning due to the lack of labeled anomalies and dataset variability. This work introduces three evaluation metrics—relative-top-median, expected-anomaly-gap, and normalized pseudo discrepancy (NPD)—to estimate model performance without labels. Using Bayesian optimization, these metrics streamline UAD tuning, showing effectiveness across 38 datasets.

### Strengths
- The paper is well-written.
- The focus on hyper-parameter optimization in UAD is important and well-motivated.
- The proposed method is novel.
- Extensive experiments effectively demonstrate the method’s effectiveness.

### Weaknesses
 - The details of AutoUAD are complex and difficult to understand.

### Questions
Please see Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims at improving hyperparameter optimization of unsupervised anomaly detection methods. To that end, it first proposes three different metrics that can be used to estimate the performance of UAD methods at testing. The metrics are used within a Bayesian optimization framework to estimate the hyperparameters of different UAD methods.

### Strengths
- The work addresses a relevant problem that requires further attention from the literature
- A large set of datasets are used for evaluationLarge set of datasets considered for evaluation.

### Weaknesses
 - The paper lacks clarity. As pointed in the questions section, there are multiple sentences that seem incomplete, which makes difficult to understand the concept being explained.
- There are some of the statements and claims that are contradictory across the paper. For example, the paper claims to be unsupervised and criticizes previous works that claim to be unsupervised but still require some form of supervision: this work aims at fixing this. Nonetheless, Definition 2 and remark 3.2 introduce labels for normal and abnormal points ($\mathcal{Y}$) and in the explanation of Definition 4 there seems to be the notion of supervision as there is the idea of true anomalies.
- Other claims lack a justification (see question 3 regarding assumption 2).
- The assumption of an isotropic Gaussian distribution for the generated dataset may be over-simple. Real-world datasets may have more complex dynamics. The paper does not adequately address how this simplification impacts the applicability of the proposed method to real-world scenarios where data distributions are far from Gaussian. The use of an isotropic Gaussian to define a hypersphere, while mathematically convenient, may not effectively capture the complex, non-linear boundaries often present in real-world anomaly detection problems. This oversimplification could lead to a model that performs well on synthetic data but fails to generalize to more realistic datasets with intricate data structures.

### Questions
**Questions:**:
1. In Eq 4, if the median (median(s))  is close to zero, the selected value of $\epsilon$ may induce some instability of V_rtm. How do you deal with those cases?
2. In definition 1, what is $\mathcal{D}'_1$? 
3. Assumption 2 lacks justification. What leads to conclude that 20% of the points on any given dataset are similar to true anomalies?
4. What is $\xi$ in Eq 5? 
5. "In many practical scenarios, such as medical diagnosis and mechanical fault detection, noisy or wrongly collected data constitute a small portion" -> Do you have evidence that backs this claim?
6. If Bayesian optimization, according to the claims, works on supervised setting, how can it be used in this setup that is AutoUAD?

**Comments:**
- The formulation of definition 1 has some flaws. If one says that N points were drawn from a distribution it means that they were effectively drawn. One cannot then say that N is unknown. Perhaps what is really meant is that points in $\mathcal{X}$ come from two different distributions, but it is not possible to determine which points come from which (D_0 or D_1). Please reformulate to the latter clearly stating where points come without the need of mentioning the quantities (N). Also, explain what is the difference between $\mathcal{D}_1$ and $\mathcal{D}'_1$.
- Assumption 1 seems to be missing something : "... will assign the majority of data points with low anomaly scores"  to what? same for the minority. Please complete/
- What is the point of Figure 2? it does not seem to match what is written in the text. What makes the difference between, for instance, fig 2 a and b?
- The observations from assumption 1 and Figure 2 are somehow trivial. This is the typical assumption in most anomaly detection setups.
- There is some text missing in definition 4 ("there exists and the variance.." -> there exists what?) that makes text incomprehensible. Please revise the sentence. 

**Minor comments:**
- "Histograms of training anomaly scores of models with low high testing AUCs" -> with low and high?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces different metrics for the optimization of hyperparameters in unsupervised anomaly detection. The authors formulate the problems of hyperparameter tuning and model selection as a maximization of the expected evaluation metric for a random dataset containing anomalies. They then propose three metrics that approximate this unknown expected value (up to some monotonically increasing function).
The key contributions of the paper are (i) the introduction of three evaluation metrics for hyperparameter optimization, (ii) theoretical analysis of the third metric and (iii) empirical experiments comparing the optimization based on the proposed evaluation metrics with other model selection methods.

### Strengths
The paper has a red line and the structure from internal to external evaluation metrics is comprehensible. The problem of hyperparameter optimization is well motivated, and extensive empirical experiments are provided.

The proposed metrics are, generally, clearly defined, and the approach is innovative. 

This paper could be a helpful contribution to unsupervised hyperparameter tuning.

### Weaknesses
The proposed metrics seem to work only under strong assumptions, no theoretical guarantees in terms of the expected false positive/negative rate are provided and the results of experiments seem to be overly optimistic with results being reported on the same data that was used for model selection and hyperparameter tuning.

Given the current shortcomings (see below), I recommend to reject the paper. I would be willing to increase the score, given that the below concerns are addressed.

---
UPDATE: Based on the additional results and explanations provided by the authors, I suggest to accept the paper.

### questions:
 Comments/Questions:
- Hyperparameter tuning is a challenge in other unsupervised learning tasks as well. Which relevant approaches are there, that are worth being added to the "Related Work" section?
- The internal evaluation metrics depend on hyperparameters themselves, which does not seem to be an advantage. How robust are they w.r.t. different choices of the hyperparameters?
- Definition 2: Are the true labels supposed to be in \{0, 1\}? Generally, the anomaly scores are not restricted to the interval $[0, 1]$. What should be passed to the evaluation metric $\mathcal{E}?$ The anomaly scores, or binary predictions based on them?
- L205: "While these tail points are part of the normal data, their distance from the majority
can make them resemble potential anomalies. They should be recognized by a good UAD model." -> Should a good UAD model recognize these points as anomalies or normal data? From my understanding, a *good* UAD model should not only perform well for data close to the majority, but also for data points at the boundary of "normal" behavior
- What is the intuition of using the mean and median to define RTM? It seems more natural to use the $mean(\{s_i|s_i < s_{top\tau\%}\})$ instead of the median (or the median in both cases).
- Can the RTM be interpreted so that an error of $\tau\%$ is accepted? Similar to the significance level of a statistical test?
- L249: What is the intuition behind the statement: "RTM may overlook a case in which all scores are uniformly distributed..."?
- L255: "Based on Assumption 1, there exists (?) and ..." -> What does exist?
- L257: What is $\xi$ in equation (4)? There seems to be something missing.
- What is the intuition of the definition of $AG(\xi, p(s))$? Why are the probabilities $w_0(k)$ and $w_1(k)$ used as weights? This seems to prefer values of $k$ such that $s_k$ is close to the median of the sample $s$.
- Definition 5: $AG(\xi)$ is not defined, only $AG(\xi; p(s))$ - and the latter not correctly
- Definition 5: Why is the conditional expectation needed? $\xi \ge s_{thr}$ by definition, so the conditional expectation reduces the the expectation, right?
- L288: If overfitting w.r.t. the training data is an issue, couldn't this simply be fixed by using a train-test-split or cross validation?
- Definition 6: Here the underlying assumption is that the "normal" data is approximately normal distributed with distribution $\mathcal{N}(\mu, diag(\sigma))$. This seems to be a very strong assumption, especially in applications with real data.
- Definition 6: Why are the coordinates assumed to be uncorrelated (as modeled with the diagonal matrix)? Why are covariances between the coordinates not considered? This assumption is **very** restrictive and even in the examples not met (see, e.g., Fig. 3)
- L372: Geometric interpretation: Why is the outline generally a hypersphere? That is, why is this the case if the variance across different coordinates varies?
- Figure 6: What does the y-axis represent? The correlation of $\nu$ with AUC? In this case, high values would be good, so the results for NPD/NDP seem ambiguous.
- Are the final results, e.g. in Table 1, calculated based on the validation data, i.e., the same data that was used for model selection and hyperparameter tuning? If so, the results are probably overly optimistic for the model selection methods.
- Some considered datasets contain unrealistic many anomalies. Can "anomalies" that occur more than 10-20\% of the time be considered as real anomalies?

Additional Feedback
- Definition 1: "normal distribution" (and the term "normal" in general) is ambiguous: clearly the distribution of normal data points is meant and not the normal distribution $\mathcal{N}(\mu, \sigma)$, but the terms "normal" (as typical) and "normal" (as Gaussian) should be distinguished better
- Definition 1: $p_0$ and $p_1$ are not defined - probably the density functions of $D_0$ and $D_1$?
- Definition 2 (L. 170-171): The joint distribution of $(\tilde{X}, \tilde{Y})$ could be specified instead of the vague "Let $\tilde{X}$ be a random unseen dataset containing both normal samples and anomalous samples"
- Definition 2: $\mathbb{E}$ should denote the expectation over the joint distribution of $(\tilde{X}, \tilde{Y})$
- Definition 3: The notation could be simplified by using the usual notation $s_{(i)}$ for sorted values (with $s_{(1)} \le \dots \le s_{(n)}$ and $s_{(\frac{\tau}{100} N)}$ instead of $s_{top\tau\%}$
- Definition 3: $\varepsilon$ could be avoided by the case distinction $med(s)=0$ and $med(s)\neq 0$
- Definition 4: "Let $p(s)$ be the distribution of the anomaly score $s$" -> Emphasize that $p(s)$ is the unknown, theoretical distribution, not the empirical distribution based on the observations in $s$
- Definition 5: From Def. 4 it is not clear what the role of $\xi$ is. If $\xi=k$, only integer-valued are allowed. In this case, the distribution is simply the discrete uniform distribution on indices $k$ with $s_k > s_{thr}$, right?
- Typo in Definition 6: "varaince vector" -> "variance vector"
- The abbreviation NPD/NDP is not used consistently (mostly NPD, in experiments NDP)

### Questions
Comments/Questions:
- Hyperparameter tuning is a challenge in other unsupervised learning tasks as well. Which relevant approaches are there, that are worth being added to the "Related Work" section?
- The internal evaluation metrics depend on hyperparameters themselves, which does not seem to be an advantage. How robust are they w.r.t. different choices of the hyperparameters?
- Definition 2: Are the true labels supposed to be in $\{0, 1\}$? Generally, the anomaly scores are not restricted to the interval $[0, 1]$. What should be passed to the evaluation metric $\mathcal{E}?$ The anomaly scores, or binary predictions based on them?
- L205: "While these tail points are part of the normal data, their distance from the majority
can make them resemble potential anomalies. They should be recognized by a good UAD model." -> Should a good UAD model recognize these points as anomalies or normal data? From my understanding, a *good* UAD model should not only perform well for data close to the majority, but also for data points at the boundary of "normal" behavior
- What is the intuition of using the mean and median to define RTM? It seems more natural to use the $mean(\{s_i|s_i < s_{top\tau\%}\})$ instead of the median (or the median in both cases).
- Can the RTM be interpreted so that an error of $\tau\%$ is accepted? Similar to the significance level of a statistical test?
- L249: What is the intuition behind the statement: "RTM may overlook a case in which all scores are uniformly distributed..."?
- L255: "Based on Assumption 1, there exists (?) and ..." -> What does exist?
- L257: What is $\xi$ in equation (4)? There seems to be something missing.
- What is the intuition of the definition of $AG(\xi, p(s))$? Why are the probabilities $w_0(k)$ and $w_1(k)$ used as weights? This seems to prefer values of $k$ such that $s_k$ is close to the median of the sample $s$.
- Definition 5: $AG(\xi)$ is not defined, only $AG(\xi; p(s))$ - and the latter not correctly
- Definition 5: Why is the conditional expectation needed? $\xi \ge s_{thr}$ by definition, so the conditional expectation reduces the the expectation, right?
- L288: If overfitting w.r.t. the training data is an issue, couldn't this simply be fixed by using a train-test-split or cross validation?
- Definition 6: Here the underlying assumption is that the "normal" data is approximately normal distributed with distribution $\mathcal{N}(\mu, diag(\sigma))$. This seems to be a very strong assumption, especially in applications with real data.
- Definition 6: Why are the coordinates assumed to be uncorrelated (as modeled with the diagonal matrix)? Why are covariances between the coordinates not considered? This assumption is **very** restrictive and even in the examples not met (see, e.g., Fig. 3)
- L372: Geometric interpretation: Why is the outline generally a hypersphere? That is, why is this the case if the variance across different coordinates varies?
- Figure 6: What does the y-axis represent? The correlation of $\nu$ with AUC? In this case, high values would be good, so the results for NPD/NDP seem ambiguous.
- Are the final results, e.g. in Table 1, calculated based on the validation data, i.e., the same data that was used for model selection and hyperparameter tuning? If so, the results are probably overly optimistic for the model selection methods.
- Some considered datasets contain unrealistic many anomalies. Can "anomalies" that occur more than 10-20\% of the time be considered as real anomalies?

Additional Feedback
- Definition 1: "normal distribution" (and the term "normal" in general) is ambiguous: clearly the distribution of normal data points is meant and not the normal distribution $\mathcal{N}(\mu, \sigma)$, but the terms "normal" (as typical) and "normal" (as Gaussian) should be distinguished better
- Definition 1: $p_0$ and $p_1$ are not defined - probably the density functions of $D_0$ and $D_1$?
- Definition 2 (L. 170-171): The joint distribution of $(\tilde{X}, \tilde{Y})$ could be specified instead of the vague "Let $\tilde{X}$ be a random unseen dataset containing both normal samples and anomalous samples"
- Definition 2: $\mathbb{E}$ should denote the expectation over the joint distribution of $(\tilde{X}, \tilde{Y})$
- Definition 3: The notation could be simplified by using the usual notation $s_{(i)}$ for sorted values (with $s_{(1)} \le \dots \le s_{(n)}$ and $s_{(\frac{\tau}{100} N)}$ instead of $s_{top\tau\%}$
- Definition 3: $\varepsilon$ could be avoided by the case distinction $med(s)=0$ and $med(s)\neq 0$
- Definition 4: "Let $p(s)$ be the distribution of the anomaly score $s$" -> Emphasize that $p(s)$ is the unknown, theoretical distribution, not the empirical distribution based on the observations in $s$
- Definition 5: From Def. 4 it is not clear what the role of $\xi$ is. If $\xi=k$, only integer-valued are allowed. In this case, the distribution is simply the discrete uniform distribution on indices $k$ with $s_k > s_{thr}$, right?
- Typo in Definition 6: "varaince vector" -> "variance vector"
- The abbreviation NPD/NDP is not used consistently (mostly NPD, in experiments NDP)

### Soundness
2

### Presentation
2

### Contribution
2
