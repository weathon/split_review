# Provable Post-Deployment Deterioration Monitoring

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
Data distribution often changes when deploying a machine learning model into a new environment, but not all shifts degrade model performance, making interventions like retraining unnecessary. This paper addresses model post-deployment deterioration (PDD)  monitoring in the context of unlabeled deployment distributions. We formalize unsupervised PDD monitoring within the model disagreement framework where deterioration is detected if an auxiliary model, performing well on training data, shows significant prediction disagreement with the deployed model on test data. We propose D-PDDM, a principled monitoring algorithm achieving low false positive rates under non-deteriorating shifts and provide sample complexity bounds for high true positive rates under deteriorating shifts. Empirical results on both standard benchmark and a real-world large-scale healthcare dataset demonstrate the effectiveness of the framework in addition to its viability as an alert mechanism for existing high-stakes ML pipelines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes D-PDDM, a new unsupervised algorithm designed to detect post-deployment deterioration in machine learning models. D-PDDM monitors prediction disagreements between the deployed model and auxiliary models using test data, without requiring labeled testing data or training data. Experimental results on both synthetic and real clinical datasets demonstrate that the proposed method outperforms existing baselines.

### Strengths
1. The paper tackles the critical problem of monitoring distribution shifts after deployment, which is essential for the reliable application of AI models in real-world scenarios.

2. The authors provide theoretical backing for the proposed method, contributing to a more rigorous understanding of its behavior.

### Weaknesses
1. The theoretical analysis has significant limitations: It is restricted to noiseless binary classification settings where the ground-truth labeling function is deterministic. This assumption is overly stringent and does not apply to many real-world classification problems. Moreover, according to Lemma 2.1, the method is only applicable under the assumption of covariate shift, which is a restrictive condition that does not generally hold in practice.

2. The literature review is not comprehensive. The authors overlook important work in source-free and test-time adaptation, areas that feature methods for detecting and adapting to distribution shifts, such as entropy minimization and uncertainty quantification. The lack of comparison with these methods significantly limits the technical contribution of the paper.

3. The discussion of auxiliary models in the problem setting section lacks sufficient detail. There is no clear explanation of the basic requirements or conditions for selecting or configuring auxiliary models. This leaves readers unclear about how these models are chosen or how they relate to the proposed method. Additionally, a high-level overview of the unsupervised baselines used for comparison would help provide better context for understanding the unique contributions of D-PDDM.

4. The experimental section does not address the robustness of D-PDDM with respect to the number and efficiency of auxiliary classifiers. While D-PDDM does not require training data during deployment, it does introduce additional auxiliary classifiers. However, the authors do not discuss the extra storage and inference costs associated with these models. This oversight undermines the claimed advantage of the method, as the practical impact of these overheads on deployment efficiency remains unclear.

5. The experimental design lacks critical information. There are no data statistics provided for the synthetic and real-world clinical datasets. The hyperparameter tuning and model selection processes are not described, raising concerns about the fairness and generalizability of the benchmark.

6. No code or data is provided for reproducibility. Although the authors include a link to their code repository, it leads to an empty repository, making it impossible to replicate the results presented in the paper.

### Questions
Please see Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The accuracy of ML models predictions can deteriorate after deployment due to changes in the distribution of the feature distribution. The paper proposes that this deterioration can be detected indirectly without using labeled deployment data. It offers a method built of two steps: a) identify, in addition to the chosen model, a reference set of high-performing prediction models at training time; and b) check the maximal discrepancy, in terms of predictions on deployment data, between the reference models and the chosen model.
The paper provides a theorem to show conditions under which prediction disagreement with other good models is “equivalent” to predictions deteriorating compared to the training-set. It then proposes a method to calibrate a deterioration test from final samples, together with theoretical results regarding the rates by which the detection rates converge when deterioration occurs and when it does not. Experiments are shown comparing the FPR and TPR to other methods on a synthetic and two real datasets.

### Strengths
Significance: The problem of detecting changes in the performance of  prediction algorithms across environments is a fundamental challenge in machine learning, and algorithms that would detect such changes before observing the true labels are attractive because often obtaining such labels requres deliberate allocation of resources. The paper outlines an approach to tackling the problem using "critic" models as surrogates for the ground truth, and develops some theory for when we would expect the approach to be successful. At current state, the algorithm is more a proof of concept than ready-made (some considerations such as choice of critic models, performance when prediction error is non-negligible, are not fully discussed or developed) 

Originality: The disagreement approach suggested by the paper is somewhat new in the context discussed:
identifying a critic function that agrees on the training set but diverges at deployment. 
I should note however that the results are quite similar in flavour to the ideas in Rosenfeld and Garg 2023, using the relations (and similar mathematical arguments) found in that paper - an upper bound on prediction after distribution shift - but in reverse. 

[Also - If indeed the authors agree that the fundamental results used are based closely on the relations described in RG2023, perhaps they should have made a more explicit attribution]. 

Quality: The paper puts together several ideas in an easy to follow way. The theoretical explanation are illustrative. I later point areas in the theoretical results which may have small issues (or perhaps are unclear to me). 

Clarity: The paper is well written and easy to follow.
I think some of the use of the statistical naming conventions is half-hearted, adding to the confusion. 
As the main example, the terms "significance" (and "alpha") are not used explicitly in a statistical 
context, and so I was left to wonder until quite late whether indeed the FPR is kept at alpha etc. (If I am not mistaken it is, but 
I think being explicit would have helped).

### Weaknesses
Some of the discussion of weaknesses is already there in the description of the strengths: 
- The algorithm is more of a sketch, for example in how to choose Hp. 
- The paper has novelty, but the results are not a far extension of RG2023.
- It is not clear if it is useful if we don't have a very accurate model. 

Other than that, I have some questions detailed in the next section:

1. Isn’t it too good to be to be true to assume that g the ground truth function is in H? 
At first seemed to me a techicality, but when I look at the proof fo Lemma 2.1 (in the supplementary), PDD->DPDD, 
it hedges on g being the that function. But is g achievable in practice? and if not, what are implications? 

2. I don't quite understand what is the probabilitic statement hiding here
"With high probability, PDD is equivalent to D-PDD". 
This is I think a similar probability  model as here
"As this equivalence happens in probability, Def. 2 allows for certain false positive errors w.r.t. to Def. 1"
and here 
"We need to demonstrate h = g with high probability" (in proof of the Equivalence condition, Lemma A.1). 

But to me It seems that expressions such as "err(f, Qg)"  and "err(f,Pg)" are not supposed to be probabilistic statements, 
because f and g are fixed functions and this is an expected statements.

### Questions
1. Isn’t it too good to be to be true to assume that g the ground truth function is in H? 
At first seemed to me a techicality, but when I look at the proof fo Lemma 2.1 (in the supplementary), PDD->DPDD, 
it hedges on g being the that function. But is g achievable in practice? and if not, what are implications? 

2. I don't quite understand what is the probabilitic statement hiding here
"With high probability, PDD is equivalent to D-PDD". 
This is I think a similar probability  model as here
"As this equivalence happens in probability, Def. 2 allows for certain false positive errors w.r.t. to Def. 1"
and here 
"We need to demonstrate h = g with high probability" (in proof of the Equivalence condition, Lemma A.1). 

But to me It seems that expressions such as "err(f, Qg)"  and "err(f,Pg)" are not supposed to be probabilistic statements, 
because f and g are fixed functions and this is an expected statements.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors explore the impact of data distribution shifts on model performance after models are deployed in new environments, focusing specifically on shifts that do not lead to performance degradation, thus avoiding unnecessary retraining. The paper proposes a monitoring algorithm called D-PDDM (Disagreement-based Post-Deployment Deterioration Monitoring) to detect performance deterioration (PDD) in the unlabeled deployment distribution. This algorithm is based on a model inconsistency framework: if an auxiliary model performs well on the training data but exhibits significant predictive inconsistency with the deployed model on the test data, performance deterioration is detected.

### Strengths
- The method proposed by the authors to address this problem is quite interesting; specifically, to avoid accessing the original dataset and to evaluate the performance of the trained model, an auxiliary model is used to "memorize" information about the original distribution and performance differences.
- The paper is well-organized, making it clear and easy to understand.
- The theory presented seems to be largely sound.

### Weaknesses
 - I'm not sure if it's my mistake, but it seems the authors did not upload the code required to reproduce this work (the anonymous link does not seem to include the code).
- The experimental section lacks an introduction to the comparison methods, which may make it unclear for non-experts in this field whether the comparisons are reasonable or if they include the latest methods in this domain, as the proposed method only appears to be compared with several distribution divergence-based detection methods.
- The algorithm proposed in the paper may require substantial computational resources, especially during the pre-training phase. This could limit its practicality in resource-constrained environments, and the authors do not seem to mention an appropriate size for the sub-hypothesis space.

### Questions
- To address the issues mentioned in this paper, could continual learning or online learning serve as a final solution?
- For a large-scale model $f$, does the auxiliary model $h$ necessarily need to have the same structure as $f$?
- Is the proposed method highly dependent on the auxiliary model $h$'s ability to effectively fit the output of $f$?
- When the model's performance declines despite no significant distribution shift, could this be attributed to overfitting? Would this method still be effective in such cases?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes an unsupervised algorithm, D-PDDM, based on model disagreement for monitoring performance deterioration of machine learning models after deployment. The method detects performance degradation by measuring the prediction discrepancies between a well-performing auxiliary model and the deployed model in an unlabeled deployment environment, without requiring training data during deployment, thereby ensuring privacy and scalability. Theoretical analysis demonstrates that the algorithm maintains a low false positive rate under non-deteriorating data shifts and effectively detects deteriorating shifts. Experimental results show that it outperforms existing methods across various datasets.

### Strengths
1.	The approach of leveraging model disagreement for unsupervised PDD is a solution to the problem of monitoring performance without access to labels. It innovatively combines existing ideas from distribution shift literature and disagreement frameworks.
2.	The paper provides a solid theoretical foundation for the proposed method. The mathematical analysis is detailed, covering both deteriorating and non-deteriorating shifts. Additionally, the authors anticipate potential failure scenarios and propose strategies to mitigate them.
3.	The paper is well-structured, with clear definitions and thorough explanations of the proposed method. The inclusion of empirical results across diverse datasets enhances the comprehensibility of the theoretical guarantees.
4.	The work addresses a critical gap in real-world machine learning deployment, where acquiring labels is often impractical or costly. The proposed method's ability to operate without training data makes it particularly relevant for privacy-sensitive domains like healthcare.

### Weaknesses
1.	While the paper emphasizes not requiring training data during deployment, the approach's reliance on pre-trained auxiliary models raises questions about generalizability. If the auxiliary model does not generalize well to the deployment environment, D-PDDM's effectiveness could be compromised. Specifically, the choice of architecture, training data, and hyperparameters for the auxiliary model are not discussed in detail, potentially leading to a significant performance bottleneck if the auxiliary model's predictions are not reliable in the deployment setting. The paper needs to address how the auxiliary model is selected and validated to ensure it is robust to the target domain.
2.	The method's reliance on hypothesis spaces and sampling might face challenges in complex, high-dimensional settings. The scalability claims, though theoretically sound, might need further empirical validation, especially in more intricate real-world scenarios. The paper does not provide sufficient detail on how the sampling is performed in practice, and how the size of the hypothesis space affects the computational cost and the performance of the method. It would be beneficial to see experiments with larger datasets and more complex models to validate the scalability claims.
3.	Assumptions in Theoretical Analysis: The theoretical guarantees hinge on assumptions such as small total variation distances between distributions. These assumptions might not always hold in practice, especially in environments with drastic changes, potentially limiting the method's applicability. The paper should discuss the limitations of these assumptions and how the method might perform when these assumptions are violated. For example, how would the method behave if the data distribution changes abruptly or if the total variation distance is large?

### Questions
1.	How does the choice of auxiliary model affect the performance of D-PDDM? Would certain types of models or training procedures make the method more robust?
2.	Can the authors provide more insights or empirical results on how the algorithm scales when dealing with complex, high-dimensional data? Are there particular datasets where D-PDDM might struggle?
3.	The threshold for determining significant disagreement is crucial for the performance of D-PDDM. How sensitive is the method to this threshold, and are there automated ways to set it optimally?
4.	The paper suggests robustness to non-deteriorating shifts, but how does the method handle abrupt, substantial changes in the data distribution, which might not be gradual? Would the disagreement framework still provide reliable monitoring in such scenarios?

### Soundness
3

### Presentation
2

### Contribution
3
