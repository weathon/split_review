# Doubly robust identification of treatment effects from multiple environments

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Practical and ethical constraints often dictate the use of observational data for causal inference, particularly in medicine and social sciences. Yet, observational datasets are prone to confounding, potentially compromising the validity of conclusions. While adjusting for all available covariates is a common corrective strategy, this approach can introduce bias, especially when post-treatment variables are present or some variables remain unobserved—a frequent scenario in practice. Avoiding this bias often requires detailed knowledge of the underlying causal graph, a challenging and often impractical prerequisite. In this work, we propose RAMEN, an algorithm that tackles this challenge by leveraging the heterogeneity of multiple data sources without the need to know the complete causal graph. Notably, RAMEN achieves *doubly robust identification*: we identify the treatment effect if either the causal parents of the treatment or those of the outcome are observed. Empirical evaluations across synthetic, semi-synthetic, and real-world datasets show that our approach significantly outperforms existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work addresses the bias arising from adjusting for bad controls in observational causal inference by leveraging invariance conditional properties of either the treatment or the outcome across multiple environments. The methodology includes two practical solutions and they are validated across synthetic, semi-synthetic, and real-world datasets.

### Strengths
1. The issue of bad controls is important in observational causal inference. The proposed approach of excluding them using multi-environment data appears to be a novel idea.
3. Comprehensive simulations are done to demonstrate the performance and robustness of the proposed algorithms.
4. The paper is well-written and clear.

### Weaknesses
1. The identification assumptions seem strong and the real-world applicability might be constrained. Are any parts of the assumptions testable using observed data, or can any robustness checks or sensitivity analyses be performed? Have you tested how violations of Assumption 4.1 impact the results?
2. To provide more convincing results regarding the method's usefulness in real-world applications, could you elaborate more on the selected controls by the algorithm in the birthweight dataset? Additionally, why is it difficult to exclude those potential bad controls or colliders based solely on domain knowledge?
3. Assumption 4.1 can be renamed since it's one of the identification assumptions.
4. The notations in the experiments are confusing and inconsistent, for example:
- In the problem setting and methodology sections, Z denotes the observed variables, d is the number of observed covariates, p is total number of variables. [d] is used to denote the indices of Z, but in Assumption 3.2, it refers to nodes.
- In the simulations, d is used inconsistently to denote the total number of nodes, the number of independent noises, and the association between the outcome and the descendant.
- Z is used to denote the descendant of T and Y in the appendix, corresponding to $X_c$ in Section 5.
- p is used as the subscript for the pre-treatment variable $X_p$ in Section 5, but it does not appear in the data generating process in the appendix.
- $\sigma$ is used to represent both a variance parameter and the sigmoid function in the data generating process.
- In the second row of Figure 9, the white space can be trimmed if the second RAMEN estimator is not used.
5. Could you explain how $\sigma^2$ in Appendix C.6 introduces environment heterogeneity and how Assumption 4.1 is violated? It only shifts the means and amplifies the variance of observed variables within the same environment.

### Questions
1. In figure 2a and 2c, if $X_c$ is only a descendant of $Y$, why does adjusting for both covariates lead to bias?
2. How are the standard errors calculated and why are they significantly higher for the proposed algorithm compared to the baselines in the application?
3. Can this approach be generalized to non-binary treatments and other estimands?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers a novel setting in which data is collected from heterogeneous environments, aiming to identify causal effects for each environment without prior knowledge of the causal graph. Under certain assumptions, the authors propose two algorithms to identify the target causal quantities. The effectiveness of this approach is demonstrated through extensive experiments.

### Strengths
1- The paper is well-written, and related work is thoroughly discussed. Additionally, the connection between the paper’s assumptions and previous work is clearly presented, for example, following Assumptions 3.3 and 4.1.

2- Various experiments have been conducted, demonstrating the significance of RAMEN.

### Weaknesses
1- The focus of the paper is solely on the identification of treatment effect; therefore, there is no analysis of sample complexity for the proposed algorithm.



### Questions
1- Could you discuss the point mentioned above?

2- What does “Descendant” mean in Figure 2?

3- Could you elaborate on Lines 264 and 278? They are not clear to me.

4- Regarding Theorem 1, we understand that the quantity is identifiable under certain assumptions. However, if some assumptions are not satisfied, can you demonstrate that the causal effect is not identifiable? This would be similar to the concept of completeness in the causal effect identification literature.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes RAMEN, a method that leverages multiple environments to achieve doubly robust identification of the ATE in the presence of post-treatment and unobserved variables. Empirical evaluations across synthetic, semi-synthetic, and real-world datasets show that the proposed method significantly outperforms existing methods.

### Strengths
1. This paper estimates causal effects in the presence of post-treatment and unobserved variables.
2. The paper introduces a novel double robustness property.
3. The authors demonstrate their method's effectiveness through extensive experiments on synthetic, semi-synthetic, and real-world datasets.

### Weaknesses
1. In the introduction, the explanation of valid and invalid adjustment sets lacks specific examples(such as in advertising recommendations or in the healthcare field), and it is difficult to understand the corresponding scenarios based only on the cause graph.
2. RAMEN should satisfy the positivity and ignoreability assumptions, which are not given in the problem setting of the paper.
3. There are many symbols and formulas in the paper. It may be better to list a symbol table.
4. The experimental evaluation metrics(such as PEHE[1] or ATE[1]) and comparison algorithms(such as[1]) are insufficient.

### Questions
1. What are the advantages of the proposed method compared with methods using neural networks, such as the method in the literature [1][2].
2. How is the number of samples in different environments determined in synthetic data experiments? To vary the number of samples per environment, it is recommended that sensitivity analysis experiments be added to synthetic datasets.

[1]Shalit U, Johansson F D, Sontag D. Estimating individual treatment effect: generalization bounds and algorithms[C].ICML’2017.

[2]Shi C, Blei D, Veitch V. Adapting neural networks for the estimation of treatment effects[C]. NIPS’2019.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides a new doubly robust identification framework given multiple data sources, in the sense that, it is able to identify the average treatment effect if in a causal DAG, the parent node of treatment or outcome is fully observed and conditional distribution of either treatment or outcome given their parents are the same across all data sources, without knowing which.

To identify the adjustment set, the paper proposed two losses based on the minimax problem outlined from the moment condition in the assumption above. 

On the sample level, the paper conduct simulations to examine the performance of their proposed RAMEN estimator.

### Strengths
The presentation of the paper is clear. The problem tackled seems interesting. I am not entirely familiar with the literature on this direction so if I believe the contributions of other literature that this paper listed, I think the idea is novel in the literature.

### Weaknesses
1. I think one of key ingredient of this paper is Assumption 4.1. I found this assumption somewhat questionable and hard to believe.
 a. Can you provide what it means under some concrete real-data examples? Maybe explain for your real-data application specifically?
 b. Can you comment the testability and falsifiability of the assumption? Can one touch slightly or comment on some sort of sensitivitiy analysis you can imagine?
 c. Intuitively, not only different data sources should be heterogeneous, but the magnitude matter, especially in estimation when you identified the S_opt. So in the simulation, maybe you can add a sensitivity parameter to represent the strength of heterogeneity of data sources , and then twist that parameter (from zero (Assumption 4.1 fails) to strong) and see what happens?


2. Apart from 1c above examining assumption 4.1, I think there are multiple angles the simulation can be strengthened, so that readers can better judge the value and contribution of this work.
For example, to examine assumption 3.3, can you check a fourth setting where both when both (a) and (b) fails. This is a common practice when evaluation classical doubly robust estimators. We expect RAMEN will fail under this setting, but it can help me to justify the difficulty of your simulations setting. For example, if RAMEN even performs reasonably well under the 4th setting, it means the simulation is too easy and failure of (a) or (b) creates not enough difficulty. I think a reasonably setting would be to combine the scenario when one of Assumption 3.3 (a) and Assumption 3.3 (b) fails in your simulation setting (b) and (c) into a case that Assumption 3.3 fails.

3. In Section 5.4, I found using 4 trimesters of birth as different environment doubtful. Are they just repeated measure of the same pregant women for 4 times? Can you comment on what Assumption 3.3 and 4.1 means in your real-world experiment?
 a. Clarify if these are indeed repeated measures or separate groups of women.
 b. Explain how Assumptions 3.3 and 4.1 are expected to hold in this specific context.
 c. Suggest alternative ways to define environments in this dataset if trimesters are not appropriate.




### Questions
Needs clarification:
1. You assumed no presence of observed mediators (Assumption 3.2) but keeps emphasizing that the paper allows post-treatment variables and unmeasured variables, so do you mean you allow either unmeasured confounders, unmeasured mediators, or colliders (can be either observed or unobserved);
2. In Assumption 3.1, you said that \eps is an exogeneous noise vector following the joint distribution P_\eps^e over p independent variables. But on Page 4 line 202, you said "our setting does not require independence of the noise variable", is this a contradiction?
3. Page 2 line 83: "We then provide the first, to our knowledge, doubly robust identification guarantees for treatment effect in the presence of both post-treatment and unobserved variables." This contribution is misleading to readers. This approach is not the first approach to handle both post-treatment and unobserved variables, but rather the first doubly robust one (if I understood correctly). For example, for the "valid adjustment set" approach, as long as practitioners know this set, it also allows both post-treatment and unobserved variables in the DAG.

Address a limitation:
1. In abstract "Notably, RAMEN achieves doubly robust identification: we identify the treatment effect if either the causal parents of the treatment or those of the outcome are observed. " This needs more clarification because the doubly robust assumption not only requires either parent is observed but homogeneity of condiitonal distributions across sources of bias.
2. Solving a minimax problem can be difficult and slow. Can you add comments on the latency (speed) of running your estimator?
 a. Please provide specific runtime measurements for your method on the datasets used in the paper.
 b. Compare these runtimes to those of the baseline methods.
 c. Discuss how the runtime scales with dataset size and number of covariates.

### Soundness
2

### Presentation
3

### Contribution
2
