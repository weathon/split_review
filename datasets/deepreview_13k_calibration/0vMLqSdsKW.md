# A Unified Causal Framework for Auditing Recommender Systems for Ethical Concerns

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
As recommender systems become widely deployed in different domains, 
they increasingly influence their users' beliefs and preferences. 
Auditing recommender systems is crucial as it not only ensures the continuous improvement of recommendation algorithms but also safeguards against potential \llreplace{pitfalls}{issues} like biases and ethical concerns. 
In this paper, we view recommender system auditing from a causal lens and 
provide a general recipe for defining auditing metrics.
Under this general causal auditing framework,
we categorize existing auditing metrics
and identify gaps in them---\vsedit{notably,} the lack of metrics for auditing user agency while accounting for the \vsedit{multi-step} dynamics of the recommendation process. 
We leverage our framework 
and propose two classes of such metrics:
future- and past-reacheability and stability\lldelete{
\sgcomment{add a sentence briefly explaining the metrics. Something like:}.}
\sgedit{\lldelete{We present two classes of metrics to quantify user agency: 
reacheability and stability}, that measure the ability of a user to influence their own and other users' recommendations, respectively.}
We provide both a gradient-based and a black-box approach
for computing these metrics, 
allowing the auditor to compute them
under different levels of access to the recommender system.
In our experiments, 
we demonstrate the efficacy of methods for computing the proposed metrics
and inspect the design of recommender systems through these proposed metrics.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a unified causal framework for auditing recommender systems with focus on user agency. The authors make three main contributions:
1. A general causal framework that formalizes interventional and counterfactual metrics for auditing recommender systems.
2. Two novel classes of metrics - reachability and stability, to measure user agency while accounting for recommendation dynamics.
3. Efficient computational methods for these metrics under different levels of access to the recommender system.

The framework is evaluated empirically using both matrix factorization and recurrent neural network based recommenders, showcasing interesting trade-offs between stability and reachability.

### Strengths
1. The technical claims and methodology are very well-supported. The causal framework is rigorously developed with clear mathematical formulations. The empirical evaluation is comprehensive, with well-designed ablation studies showing impact of various stochasticity levels, time horizon lengths and model architecture choices.

2. Novel formalization of reachability and stability metrics presented capture both immediate and long-term effects, handle multi-step recommendation dynamics and account for both user and adversary perspectives.

3. The paper is generally well-written and logically structured. The causal framework is presented clearly with helpful examples.

### Weaknesses
1. The assumption of static user/item embeddings during gradient computation could be better justified. Additional experiments showing impact of this simplification would be valuable.

2. The empirical evaluation focuses on movie recommendations - testing on other domains (e.g. social media, e-commerce, etc.) would strengthen the framework's generalizability claims.

3. The choice of distance metrics for stability measures (L2 distance) could be better justified. Adding discussion of metric sensitivity to adversarial perturbations and analysis of the relationship between local and global notions of reachability would be useful.

4. The paper presents limited discussion of computational complexity and scalability analysis, particularly for large-scale recommender systems. The paper could analyze how the methods scale with number of users, items and time horizon.

### Questions
1. How does the computational complexity scale with the number of users, items and time horizon? What are recommended approaches for large-scale recommender systems?

2. What are the practical implications of assuming static embeddings during gradient computation? How would the results change with full retraining?

3. Could the framework be extended to handle more complex recommendation scenarios like slate recommendations or contextual bandits?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a unified causal framework for auditing recommender systems, specifically to address ethical concerns such as user agency, stability, and reachability. It categorizes auditing metrics from a causal perspective and introduces two key metrics, past- and future-reachability, and stability, which measure a user’s ability to influence recommendations. The empirical studies evaluate the metrics on different recommender models, highlighting the trade-offs between user influence on recommendations and system stability.

### Strengths
The causal approach offers a novel way to address ethical issues, providing a structured method for defining and calculating user-centric metrics.

Offering both gradient-based and black-box methods for metric computation enables broader application

### Weaknesses
The framework’s reliance on specific causal assumptions and models,this may reduce its generalizability across diverse recommender systems.

The paper lacks a discussion about the differences between recommendation systems.

### Questions
What are the differences and impacts of applying this model to various recommendation models?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this work, authors pay attention to recommender system auditing from a causal perspective, and point out the lack of metrics for auditing user agency for the recommendation process. Therefore, two metrics are proposed, including future- and past-reachability and stability, which can measure the impact of users on their own and other users. To calculate these metrics, the authors also design a gradient-based and a black box approach.

### Strengths
S1- This paper provides comprehensive details on the background of the problem.

S2- The authors give detailed experiment settings which improves the reproducibility.

### Weaknesses
W1-The motivation of this paper is not quite clear. For example, what’s the actual relationship between user agency and ethical concerns? It is not immediately obvious how the proposed metrics directly address ethical issues. The paper needs to more explicitly connect the concept of user agency, as measured by their metrics, to specific ethical harms that can arise in recommender systems. For instance, how does a lack of reachability or stability directly lead to a violation of user rights or fairness?

W2-The experiments are only conducted on ML-1M, which are insufficient to explain the universality of the conclusions since the recommendation senarios are diverse. Experiments on at least one dataset from other recommendation senarios are needed. The ML-1M dataset is relatively old and small, and may not reflect the complexities of modern recommendation systems. The paper should include experiments on datasets with different characteristics, such as larger datasets, datasets with more diverse item types, or datasets with more complex user-item interaction patterns. This would help to demonstrate the robustness and generalizability of the proposed metrics.

W3- In Figure 3 for the distribution of past instability values, for MF, Past-5 shows lower proportion of 0.0 than Past-1, but for RRN, Past-5 presents higher proportion of 0.0 than Past-1. Could you please explain the reason for this contrary result?

### Questions
Please see them in the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work, the authors adopt a causal perspective on recommender system auditing and present a general method for defining auditing metrics. Within this overarching causal auditing framework, they categorize existing audit metrics. Leveraging their framework, they propose two types of metrics: future-/past-reachability and stability, which respectively measure a user's ability to influence recommendations for themselves and for other users. Additionally, they introduce a gradient-based method and a black-box method for calculating these metrics, allowing auditors to assess them at various levels of system access. Empirically, the authors demonstrate the effectiveness of their proposed metrics and use them to examine the design of recommender systems.

### Strengths
- Auditing recommender systems is a highly meaningful area of study, and the paper contributes valuable insights.
- The article is well-written and clearly articulated, making complex concepts accessible.
- It provides methods for auditing from both white-box and black-box perspectives, catering to different levels of system access.

### Weaknesses
 - **W1**: **Ambiguity in Definitions**: The definitions in the article lack detailed explanations, which may lead to ambiguity. For example:
  - **Q1-1**: In Definitions 4.1 and 4.2, the authors consider only the intervention on $O_{i,t}$ without accounting for its effect on $A_{i,t+1}$. Specifically, in Equation 1, the formulation only considers the effect of $do(O_{i,t+k-1} = f(A_{i,t+k-1}))$ on $A_{i,t+k}$, but it does not account for the effect of $do(O_{i,t+k-2} = f(A_{i,t+k-2}))$ on $A_{i,t+k-1}$. Why was this setting chosen?
  - **Q1-2**: Are Definitions 4.1 and 4.2 consistent? Specifically, does past-$k$ at time $t+k$ equal future-$k$ at time $t$? It would be helpful if the authors could address this question both intuitively and formally. It seems that future reachability considers the effect of interventions on future recommendations, while past reachability does not, but this distinction is not reflected in Equation 1. Furthermore, what is the practical significance of past reachability, especially when analyzing the expected reachability of an item under unchanging recommendations? What does this imply in real-world scenarios?

- **W2**: **Limited Analysis Scope**: The analysis in Section 5 is confined to $k=1$, representing only a special case of the broader definitions provided.
  - **Q2**: Please describe how the corresponding white-box and black-box methods would operate when $k > 1$. Specifically, would Equation 5 and the formulas in Section 5.2 need to be adjusted, or would this require retraining to evaluate the metrics? Please provide a detailed explanation.

- **W3**: **Practical Applicability Concerns**: There is a gap between the theoretical propositions and practical scenarios.
  - **Q3**: Proposition 5.1 requires fixing item embeddings, while Proposition 5.2 requires fixing user embeddings. Since these conditions are difficult to meet in real recommender systems, how does this gap affect practical auditing? While I understand that these assumptions simplify analysis, what is the significance of these assumptions on the practical auditing process? Previous works using similar assumptions do not necessarily imply that these assumptions will not affect the auditing process.

- **W4**: **Lack of Experimental Rationale**: Certain experimental setups lack clear justification.
  - **Q4-1**: Section 6.1 mentions different policies for future and past metrics. Why was this setup chosen? Please explain the rationale behind this decision.

- **W5**: **Incomplete Experimental Validation**:
  - **Q5-1**: The use of a single dataset limits the experimental scope and generalizability of the findings. The conclusions drawn in the experimental section, such as “As we increase $\beta$, or decrease the stochasticity of the system, user recommendations tend to become more stable,” are data-dependent. If consistent results cannot be achieved across multiple datasets, these conclusions will be hard to accept. I strongly encourage the authors to include results from additional datasets.
  - **Q5-2**: The current experiments focus on analyzing existing models within the proposed framework but do not clarify why this framework or these metrics are more valid than existing auditing methods. Additional experiments, such as straightforward case studies, are needed to further validate the framework.

### Questions
In addition to **Q1** to **Q5** mentioned in the Weaknesses, I have several other questions:

- **Q6**: What is the relationship between the proposed metrics and recommendation performance? Does a stronger recommendation model perform better according to these metrics?

- **Q7**: The metric comparisons in Figure 3 are described but lack corresponding explanations. For instance, why do some items show "a user’s recommended list is either heavily affected by the actions of an adversary or is minimally affected by them"?

- **Q8**: Is the time horizon parameter in the experimental parameters equivalent to $k$ in Definitions 4.1 and 4.2? If not, how is $k$ set in the experiments?

I am happy to engage in further discussion, and if these issues are addressed, I am willing to reconsider the score.

### Soundness
2

### Presentation
3

### Contribution
2
