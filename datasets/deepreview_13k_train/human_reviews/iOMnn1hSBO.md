# DECISION-FOCUSED UNCERTAINTY QUANTIFICATION

- Decision: Accept
- Scores: 6, 8, 8, 6, 6

## Abstract
There is increasing interest in ``decision-focused" machine learning methods which train models to account for how their predictions are used in downstream optimization problems. Doing so can often improve performance on subsequent decision problems. However, current methods for uncertainty quantification do not incorporate any information at all about downstream decisions. We develop a framework based on conformal prediction to produce prediction sets that account for a downstream decision loss function, making them more appropriate to inform high-stakes decision-making. Our approach harnesses the strengths of conformal methods—modularity, model-agnosticism, and statistical coverage guarantees—while incorporating downstream decisions and user-specified utility functions. We prove that our methods retain standard coverage guarantees.  Empirical evaluation across a range of datasets and utility metrics demonstrates that our methods achieve significantly lower decision loss compared to standard conformal methods. Additionally, we present a real-world use case in healthcare diagnosis, where our method effectively incorporates the hierarchical structure of dermatological diseases. It successfully generates sets with coherent diagnostic meaning, aiding the triage process during dermatology diagnosis and illustrating how our method can ground high-stakes decision-making on external domain knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel framework for decision-focused uncertainty quantification, integrating conformal prediction with downstream decision-making considerations. By introducing decision loss into the prediction process, the authors create a conformal method that offers both standard statistical coverage and improved utility for specific applications, such as healthcare diagnostics.

### Strengths
1. The setting of this paper is interesting that taking the decision loss in conformal prediction pipeline.
2. This paper effectively bridges conformal prediction and downstream decision making by incorporating user-specified utility functions, providing both theoretical guarantees and practical applicability. The authors comprehensively address both separable and non-separable decision losses.

### Weaknesses
1. The motivation for the study and its illustrative example could be more clearly developed. The authors present the example of the Fitzpatrick dataset to explain their approach, but the rationale for selecting a loss function that reflects the hierarchical homogeneity of dermatologic pathologies remains somewhat unclear. It would benefit the reader if the authors further explained why this hierarchical approach yields a more interpretable clinical result. In addition, I suggest moving this example to the introduction or background section to establish the relevance of the study more clearly.

2. The method relies on applications that require a decision loss function; however, the necessity and specific contexts for using a decision loss function should be more thoroughly explained. The authors claim that their method "outperforms existing approaches" in terms of decision loss; however, since the loss function is central to their conformal prediction adaptation, one would expect it to outperform basic conformal approaches that don't consider decision loss. An explanation of why certain applications requires such a loss function would clarify the broader applicability. For example, in Section 3.1, the authors present a medical example where penalties are associated with the cost and complexity of each test. However, the experimental datasets largely use homogeneity-focused loss functions, so it is unclear why this type of loss should apply to datasets such as CIFAR100. The authors might consider providing additional examples of potential applications and elaborating on appropriate loss functions for each.

### Questions
See weaknesses.

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
This paper presents a new framework that merges conformal prediction with decision-focused learning to create prediction sets that optimize decision-making while maintaining statistical coverage at various levels. The method addresses a gap in current techniques, which often ignore how predictions affect real-world decisions, especially in high-stakes areas like healthcare. The authors propose two algorithms: a penalty-based approach for separable losses and an optimization method for non-separable losses without hyperparameters. They provide theoretical and empirical evidence, including a healthcare case study, to show the effectiveness of their approach.

### Strengths
- Originality: Novel integration of decision-focused loss into conformal prediction, addressing a key gap in uncertainty quantification for high-stakes applications.
- Quality: Robust theoretical grounding and empirical results, demonstrating significant decision-loss reduction across multiple datasets.
- Clarity: The paper is well-structured, with a logical flow from motivation to problem formulation, methodology, and results. Also explains previous related concepts well
- Significance: Highly relevant for domains like healthcare, enhancing prediction sets to support actionable, utility-aligned decisions.

### Weaknesses
 - Lacks comparisons with alternative uncertainty methods like Bayesian inference, limiting context on the framework’s unique advantages.
- Tuning for separable loss is computationally intensive; more efficient tuning methods would improve usability.
- Focuses heavily on healthcare; additional applications in other high-stakes areas would demonstrate broader applicability.

### Questions
- For the penalty-based approach in separable losses, can you elaborate on the efficiency of grid-search tuning for large datasets? Are there faster alternatives?
- Could you clarify how the fixed order of adding elements to prediction sets affects performance for complex utility structures? Would alternative scoring or ordering strategies improve flexibility for non-separable losses?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper tackles a problem in AI decision-making and how to make AI predictions more useful for real-world decisions while maintaining reliability. Instead of just giving a set of possible predictions (like in conformal prediction methods), this work creates prediction sets that make practical sense for decision-makers. The paper suggests a solution that balances probability and cost using tunable parameters and another elegant solution that doesn't need to find this tunable parameter and automatically finds the best balance of likelihood and cost associated with the class.

### Strengths
- This is a strong and mathematically sound work that extends traditional conformal prediction work by generating sets of utility functions that capture the associated likelihoods and costs, which is crucial for decision-making.

### Weaknesses
 - The results section is limited regarding insights provided and evaluated only on 4 common datasets. It would also be a nice insight to see the prediction sets for the experiments as a qualitative analysis. 
- It will be interesting to see how this approach works for more challenging datasets with complex hierarchical structures. 
- Limited ablation studies
-There is no discussion on the loss functions choices and design beyond maximum distance and coverage

### Questions
- The greedy approach overall seems to be doing worse than the approach that uses a learnable $\lambda$ parameter. Could the authors please clarify the advantages of the greedy approach? 
- Can you provide theoretical bounds for the performance between greedy optimizer vs optimal solution for non-seperable losses ? 
- Is there a relationship between base model calibration and decision loss? 
- Did you consult medical experts about the clinical relevance of your prediction sets?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper aims to generate prediction sets that maximize a utility function while having coverage guarantees. It extends standard approaches in conformal predictions with novel conformity scores that integrate the utility of the prediction set. Several utility functions are considered, and the approaches differ depending on whether they are separable or inseparable. The marginal coverage guarantees of conformal prediction can be preserved in both cases. Experiments on three classification datasets and diverse utility functions show that the methods achieve higher utility than the conformal prediction approach that uses the standard non-conformity score.

My evaluation of the paper is mixed. On the one hand, I find the notion of utility of prediction sets very interesting and novel (to my knowledge). On the other hand, I find the paper confusing in some parts, especially in its framing as a "decision-focused" approach, which refers to a stream of literature that provides structured predictions by integrating a constrained optimization problem.

### Strengths
The main novelty of the paper is providing prediction sets that maximize a user-specified utility function. If the utility function is the size of the set, we recover the traditional conformal prediction setting. However, the approach is more general. It can consider for instance the hierarchy / categories of the labels in the prediction set. The example in Figure 1 works quite well to illustrate the value of the obtained sets, which are more informative for users.

From a methodological perspective, the algorithms and non-conformity score are quite simple (which is an advantage) and are shown to preserve the coverage guarantees of conformal predictions. The experiments also suggest that they provide good performance.

### Weaknesses
I have two main concerns.

First, I find the framing of the paper as a decision-focused approach misleading and confusing. This is for two reasons. It hides the novelty of the paper, which is its focus on prediction sets with utility. It also makes it seems that the paper is focusing on decision-making in the same vein as the cited works of  Mandi et al., 2020; Elmachtoub & Grigas, 2022; Wang et al., 2021, etc. However, this is not the case because (a) the loss function is completely independent of the true label (hence, there is no notion of accuracy / task loss / decision loss / regret of the prediction set) and (b) the prediction sets are unconstrained since the coverage guarantee is achieved by the conformalization procedure. Decision-focused learning typically deals with the challenges of having to output a decision that is both heavily constrained (linear or combinatorial constraints) and provides good task loss thanks to end-to-end training.

An interesting direction to make the problem task-focused / end-to-end would be to consider Equation (1) as the task and train the ML classifier in an end-to-end fashion to minimize this task loss.

I argue that the paper's main focus is conformal predictions with utility and does not have much to do with decision-focused learning. My second main concern is that the current analysis of the prediction sets is a bit light. The experiments do not show how large the prediction sets are (which is a common utility metric in conformal prediction) nor their achieved marginal and conditional coverage. There is likely to be a trade-off between these metrics (size vs. achieved coverage vs. user-specified utility) for having truly informative prediction sets. I would also expect to see benchmarks from the existing literature on conformal predictions, such as the adaptive approaches cited in the paper.

I also have a few minor comments:
- line 53 "*the work to date on decision-focused learning has largely neglected uncertainty quantification, concentrating instead on constructing models to optimize point predictions for specific decision tasks*". This is incorrect. Point forecasts are the focus when the task loss is linear in the predicted parameters. It is not always the case, see among others:
Qi et al. (2021). Integrated conditional estimation-optimization.
Chenreddy et al. (2022). Data-driven conditional robust optimization.
Kallu & Mao (2023). Stochastic optimization forests.
Sadana et al. (2024). A survey of contextual optimization methods for decision-making under uncertainty.
as well as the following papers, who all use conformal predictions:
Chenreddy et al. (2024). End-to-end conditional robust optimization.
Patel et al. (2024). Conformal contextual robust optimization.
Yeh et al. (2024). End-to-End Conformal Calibration for Optimization Under Uncertainty.
- line 171. The first property states a conditional coverage guarantee (“*for an instance*”), whereas the objective is marginal coverage (what conformal predictions guarantee and what I believe is shown in Figure 2). It could help to formally introduce the problem using Equation (1), which includes a marginal coverage guarantee.
- The short proofs of Proposition 3 and 4 should be moved to the paper body to clearly show that the coverage guarantee is achieved by the split procedure.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces new methods for uncertainty quantification in classification problems, focusing on conformal prediction techniques that optimize decision loss. Three methods are proposed to address different types of decision losses (separable and inseparable) and are with or without hyperparameters. These approaches retain the coverage guarantee of traditional conformal prediction while achieving significantly lower decision loss, as demonstrated through empirical evaluation on five datasets.

### Strengths
- The paper's goal is clear.
- The simplicity of this method, along with the effort to propose a method without introducing a new hyperparameter, will favor its adoption in practical applications.
- Empirical results show notable improvement over the standard conformal prediction method.
- The methods are theoretically well-supported.

### Weaknesses
 - The discussion of related work is insufficient, focusing exclusively on conformal prediction literature while neglecting other uncertainty quantification methods (quantile regression, Bayesian methods, ensemble methods...). As the goal of the paper is to "Incorporate the decision loss into uncertainty quantification", this omission makes it difficult to assess the significance of the paper beyond conformal prediction.

- Building on the previous point, the paper lacks comparisons with existing methods, even though relevant approaches in conformal prediction appear to address the authors' objectives [1]. Other methods outside of conformal prediction also exist [2], and while they may not offer the same theoretical guarantees, comparing their empirical performance would help assess the impact of the proposed methods. Additionally, traditional conformal prediction could be directly applied to classifiers that focus on minimizing decision loss [3].

- Some sections, such as Figure 2, require improved clarity for better readability.

- The experimental details required to reproduce the results are missing. Specifically, classifiers trained on these datasets can be sensitive to variations in training hyperparameters.

- The authors modify the conformal score by incorporating an additional term to account for decision loss. This modification, while aiming to minimize decision loss, could potentially make the conformal score less informative, leading to larger, less predictive conformal sets. The paper does not adequately address the trade-off between minimizing decision loss and maintaining the informativeness of the conformal sets. For certain loss functions, adding an extra element to the conformal set could directly reduce the decision loss, which raises concerns about the method's practical utility. The lack of analysis on the average size of the conformal sets further exacerbates this issue.

- The authors focus on split conformal prediction, but there are other conformal prediction methods available [1,2]. The paper does not discuss the applicability of the proposed modifications to these other methods, or whether they are specific to split conformal prediction. Furthermore, the lack of adaptiveness in split conformal prediction is a known issue [1]. The paper does not analyze how the proposed method affects conditional coverage, or whether the decision loss is minimized uniformly across all subgroups. Given the emphasis on medical applications, it is crucial to assess the method's performance on specific subgroups, which is currently missing.

### Questions
- The authors modify the conformal score by incorporating an additional term to account for decision loss. Wouldn't this make the conformal score less informative and potentially increase the size of the conformal sets? In general, doesn't attempting to minimize decision loss tend to result in larger sets which carry less predictive value? Furthermore, for certain losses, is it possible that adding an extra element to the conformal set could directly reduce the decision loss? To address these concerns, I recommend that the authors report the average size of the conformal sets in their experiments.

- The authors focus on split conformal prediction, but there are other conformal prediction methods available [1,2]. Can the proposed modifications be applied to these other methods, or are they specific to split conformal prediction?

- Following the previous point, the lack of adaptiveness in split conformal prediction is a known issue [1]. How does the proposed method affect conditional coverage? Is the decision loss minimized uniformly across all subgroups, or are there significant discrepancies? Since the authors emphasize medical applications, it seems essential to assess the method's performance on specific subgroups in such contexts.

[1] (2019) Conformalized Quantile Regression

[2] (2022) A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification

### Soundness
2

### Presentation
3

### Contribution
3
