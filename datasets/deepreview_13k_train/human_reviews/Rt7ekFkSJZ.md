# Fair Feature Importance Scores for Interpreting Tree-Based Methods and Surrogates

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Across various sectors such as healthcare, criminal justice, national security, finance, and technology, large-scale machine learning (ML) and artificial intelligence (AI) systems are being deployed to make critical data-driven decisions. Many have asked if we can and should trust these ML systems to be making these decisions.  Two critical components are prerequisites for trust in ML systems: interpretability, or the ability to understand why the ML system makes the decisions it does, and fairness, which ensures that ML systems do not exhibit bias against certain individuals or groups. Both interpretability and fairness are important and have separately received abundant attention in the ML literature, but so far, there have been very few methods developed to directly interpret models with regard to their fairness. In this paper, we focus on arguably the most popular type of ML interpretation: feature importance scores. Inspired by the use of decision trees in knowledge distillation, we propose to leverage trees as interpretable surrogates for complex black-box ML models. Specifically, we develop a novel fair feature importance score for trees that can be used to interpret how each feature contributes to fairness or bias in trees, tree-based ensembles, or tree-based surrogates of any complex ML system.  Like the popular mean decrease in impurity for trees, our {\it Fair Feature Importance Score} is defined based on the mean decrease (or increase) in group bias.  Through simulations as well as real examples on benchmark fairness datasets, we demonstrate that our Fair Feature Importance Score offers valid interpretations for both tree-based ensembles and tree-based surrogates of other ML systems. 
Keywords: Interpretability, fairness, interpretable surrogates, knowledge distillation, decision trees, group fairness

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on the problem of explaining the unfairness of ML models. The proposed metric works for tree based models only. They key idea is to slightly alter the node splitting procedure to compute the unfairness score of a feature.

### Strengths
1. The paper correctly notes that using explanations to understand the unfairness of a model is an important desideratum in applications of ML.

2. The proposed procedure is simple and easy to understand.

### Weaknesses
While it focuses on an interesting and timely problem, I think the paper still has some key issues which should be addresses before its ready for publication.

1. **Framing:** The paper claims to be the first to consider fairness and explainability of ML models. For instance, the paper notes that "we have no current way of understanding how a feature affects the fairness of the model’s predictions". However, there is already non-negligibly amount of work that focuses on fairness and explainability both. Consider for example [this blogpost](Explaining Measures of Fairness) showing how to use SHAP to understand model unfairness. On a more academic side, I would suggest that the paper factors papers 1-4 (and related references therein) in the related work section so that the readers can better frame its contributions.

2. **Motivation:** The paper needs to motivate the design choices in a better way. I am not sure that "trees have a popular and easy-to-compute intrinsic feature importance score known as mean decrease in impurity" is the most important reason to focus on trees. There exist plenty of methods like SHAP, LIME and Integrated Gradients for explaining all kinds of other ML models. Similarly, why consider the mean decrease in impurity (MDI) score? There are other methods like TreeSHAP which seem to offer better theoretical properties. Also, the proposed FairFIS metric has a rather interesting choice in comparing a parent and the child node. The paper explains why the the computation of the style of Eq. 1 was not considered, but does not mention what are the pros and cons of the computation of FairFIS? How can we ascertain that this choice corresponds to how humans would expect model explanations to behave?

3. **Evaluation:** The evaluation, while considering multiple datasets, is quite high level and relies on the parallels between FIS and FairFIS. I would suggest performing a more systematic analysis and consider quantitative evaluations metrics (e.g., those considered [here](https://arxiv.org/abs/1705.07874) and [here](https://arxiv.org/abs/1912.09405)).

4. **Writing:** I think the writing should also be improved before the paper is ready for publication. Currently, the paper tends to simply provide information without first giving motivation and reasoning. Consider for instance the experiment in Section 3.1, where the paper directly dives into the details of the experiment without explaining why it was set up in this way, what metrics should the users watch out for, and what kind of values of should they expect to see.

### Questions
Please see points 1-3 in the "Weaknesses" section.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors proposed a new feature importance score to investigate whether bias exists in the machine learning models. This score is adapted from the classical feature importance score over tree-based models by considering the difference between the bias of the nodes and their children. Through some experiments in the simulated settings, the authors can demonstrate that the proposed metric can provide reasonable explanations of why bias occurs in the predictions of the machine learning models.

### Strengths
+ The problem of interpreting why and how bias occurs in machine learning systems is an important problem to study
+ The authors proposed a simple and generic solution to solve this problem
+ The authors tried to provide extensive experiments to empirically demonstrate the benefits of the proposed solution.

### Weaknesses
+ I have some concerns about the motivations of this paper. The authors claim that they want to interpret how a feature influences the prediction bias of one model. However, I feel that this problem could be solved by performing counterfactuals over the features that we want to explain and evaluating how the prediction bias gets changed. For example, if we want to understand how the feature "sex" influences the prediction bias, we can generate counterfactuals by flipping the sex from male to female and female to male and check how the prediction bias changes. The authors need to provide more justifications for why this strategy is not satisfactory.
+ Related to the above point, the baseline comparison in the experiments is very simple and lacks many critical baseline methods, in particular, the state-of-the-art feature importance score over general models. As mentioned above, we adapt such baseline methods by measuring how perturbing the target feature impacts the prediction bias. For example, we can adapt the permutation feature importance score to the bias scenario by randomly permuting the target feature and measuring how much the prediction bias gets changed. It would be essential to consider the adaptations of such a baseline and perform an empirical comparison.
+ Interpreting the influence of a feature over the model prediction bias through the decision tree surrogate is also problematic. I am not sure whether the feature that causes the most significant prediction bias for the surrogate model can really cause the same amount of bias in the original model. The authors need to verify this somehow, say through performing counterfactuals over the target features on the original models. For example, if the surrogate model suggests that "sex" is the most important feature, we can perform counterfactuals over "sex" on the original model and measure how much the prediction bias gets changed. If the change is also significant, then it can verify that the surrogate model is a good proxy for the original model in terms of feature importance for bias.
+ I am also worried about the novelty of the proposed solution. In my mind, it is still like simply replacing the loss function in FIS score with bias metrics, which seems to be straightforward to me. More discussion on why the proposed metric is non-trivial is needed. For example, the authors can discuss whether there are any theoretical guarantees for the proposed metric, or whether there are any unique challenges when adapting the FIS score to the bias scenario.

### Questions
See above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors introduced the limited prior work on the understanding of how a feature affects the fairness of the model's predictions. The authors then proposed FairFIS, a surrogate model to interpret tree-based model which assigned the fairness score to each of the features, providing the protected atrribute are provided. The authors demonstrated in simulation and real data that FairFIS is capable of capturing the important features that increase/ decrease the bias w.r.t the protected variables in their definition.

### Strengths
The question the authors attempted to answer is novel and important: Given a protected feature, what are the contribution of other features with respect to minimizing  the contribution of the protected feature. This is a great approach to understanding the fluctuation of feature contribution w.r.t. a particular feature that is not of interests.

### Weaknesses
1. The paper's approach to addressing fairness through the proposed algorithm is not adequately substantiated. The algorithm requires users to define a set of "protected" features, then computes bias based on this selection. This methodology rests on the assumption that the chosen protected features are inherently unbiased—a claim not demonstrated in the paper. The authors need to provide a rigorous formal definition of what constitutes a "protected feature" in various contexts. For instance, are features like income, country of origin, or religion universally considered protected, or does their status depend on the specific prediction task?  Without a clear framework for identifying protected features, the practical applicability of FairFIS is questionable. Furthermore, the authors should clarify how the selection of different sets of protected features impacts the computed bias and the resulting FairFIS scores. A sensitivity analysis demonstrating the robustness of FairFIS to variations in the protected feature set would significantly strengthen the paper's claims.

2. The generative model used in the simulation doesn't fully align with the authors' objective of understanding feature contributions to fairness. The proposed model, represented as z --> x --> y, implies that the protected attribute z is the root cause of the outcome y. This raises a fundamental question: if z is indeed the primary driver of y, why is it designated as "protected"?  Consider a scenario where z represents race and y represents a health outcome. If race (z) directly influences the health outcome (y) through a causal pathway, is it appropriate to label race as a protected attribute, or should it be considered a legitimate predictor? The authors need to address this apparent contradiction. Moreover, the paper should explore alternative generative models where the relationship between z, x, and y is more complex, such as models with latent confounders or feedback loops. This would provide a more realistic assessment of FairFIS's performance in diverse scenarios.

### Questions
How should one select the protected features? Who should decide the fairness of the selection of protected features? Are income, country, religion considered as protected features?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an approach for measuring the contribution of features to fairness metrics, namely equalized odds and demographic parity, in decision trees. This metric, called "Fair Feature Importance Score" (FairFIS), measures the change in group bias for a feature, akin to the traditional mean decrease in impurity. Through simulations and real-world tests on benchmark fairness datasets, the paper demonstrates the efficacy of FairFIS in providing valid interpretations for tree-based ensemble models and as surrogates for other ML systems.

### Strengths
The paper proposes a novel metric for quantifying the contributions to the overall feature measure based on the model features used in decision trees. Fairness is an important topic and the proposed metric uses equalized odds and demographic parity, which are two of the most commonly used metrics, making it appealing.

### Weaknesses
I think that the paper is fairly verbose and the presentation could be more concise. I had to go back and forth between pages to make sure that my understanding of the mathematical notation was correct. Nonetheless, the paper lacks two important discussions:
* How should practitioner use the proposed metric? A discussion is needed on this. 
* Similarly to FIS, when features are correlated some may receive low FairFIS values even though they matter for fairness purposes. 

In addition, I think that the method should be compared to other baselines. I can think of at least two:

* First, in all the datasets that the authors employed, the number of features is small. Thus, it’d be easy to fit p models where p is the number of features and each model is missing one feature, and then analyze how fairness metrics vary across models.  This idea is similar to leave-one-covariate-out (LOCO) inference, see https://www.stat.cmu.edu/~ryantibs/talks/loco-2018.pdf.
* Second, one could fit two different models to the data and compare the disparities of the models with the tree-based method proposed by https://arxiv.org/pdf/1707.00046.pdf. The authors could analyze FairFIS for each model and see if they reach similar conclusions about which features contribute towards disparities as they would with the method from that paper. 

Other minor details:
* What are the error bars in Figure 2? Are they confidence intervals? What are the groups? The legend should be improved because it is mentioned that they are G1, G2 etc only on page 7. 
* It seems that the authors are considering $\Sigma=I$ in the main paper, and $\Sigma\neq I$ in the Appendix. Is this correct?
* Proposition 1 could be shortened. It’s taking up a lot of space and it’s pretty clear how these metrics need to be computed. 
* There are a couple of typos.

### Questions
Mentioned above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
