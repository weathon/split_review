# Quantum AdaBoost with Supervised Learning Guarantee

- Decision: Reject
- Scores: 3, 5, 5, 3

## Abstract
Although quantum algorithms based on parameterized quantum circuits  promise to achieve quantum advantages, in the noisy intermediate-scale quantum (NISQ) era, their capabilities are greatly constrained due to  limited number of qubits and depth of quantum circuits. Therefore, we may view these quantum algorithms as weak learners in supervised learning. Ensemble methods are a general technique in machine learning for combining weak learners to construct a more accurate one. In this paper, we theoretically prove and numerically verify a learning guarantee for quantum adaptive boosting (AdaBoost). To be specific, we theoretically depict how the prediction error of quantum AdaBoost on binary classification decreases with the increase of the number of boosting rounds and sample size.  By employing quantum convolutional neural networks, we further demonstrate that quantum AdaBoost can not only achieve much higher accuracy in generalization and prediction, but also help mitigate the impact of noise. Our work indicates that in the current NISQ era, introducing appropriate ensemble methods is particularly valuable in improving the performance of quantum machine learning algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to apply AdaBoost to ensemble models of parameterized quantum circuits for binary or multi-class classification of quantum states. An additional variant of the AdaBoost algorithm is proposed which is tailored for binary classification. Theoretical bounds and numerical demonstrations are presented in the paper.

### Strengths
The paper is well-presented. The algorithms and theorems are easy to follow.

### Weaknesses
The proposed method, named quantum AdaBoost, does not exploit the underlying quantum information. Effectively, it treats the PQCs as arbitrary weak classifiers that can take quantum states as input, and use AdaBoost to ensemble them. The novelty of this work is not thoroughly justified by the evidence presented. Besides, it is confusing to claim that multiple quantum AdaBoost algorithms have already been proposed in the literature while naming the proposed framework as quantum AdaBoost. The comparison between these algorithms and frameworks is also not explained.

The main theorem of the paper seems to be a combination of previously known results, with an additional bound on the Rademacher complexity of PQCs. The ideas justifying its novelty are not illustrated.

The experiments have not considered other ensemble methods and only compare the proposed framework with the base models. The experiments where noises are present do not suffice to justify that the proposed method is robust to the noises.

### Questions
What are the differences between your quantum AdaBoost and other previously proposed quantum AdaBoost algorithms?

How does your framework compare to other ensemble methods for quantum classifiers?

Why does your framework mitigate the effects of noises in PQCs?

### Soundness
2 fair

### Presentation
3 good

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
This paper considers quantum ensemble learning when the quantum classification models are used as weaker learners. The generalization error bound is given for this type of ensemble learning. The authors also give empirical evidence of improved accuracy by quantum ensemble learning.

### Strengths
*Quality*

- The analysis of ensemble learning when the weak learners are quantum models are provided with rigor.  This analysis follows the standard routine for ensemble learning, and is technically sound to the best of my knowledge.

- The experimental settings make sense to me. 

*Clarity*

- This paper is in general well written.

### Weaknesses
 *Novelty*

- Limited novelty in theoretical analysis. The proof seems a straightforward combination of the standard analysis for ensemble learning and well-established lemmas for quantum models. Thus, the novelty of the theoretical analysis in this paper is limited. Specifically, the generalization bound derived appears to be a direct application of existing results on Rademacher complexity for quantum models, combined with standard boosting analysis. The paper does not introduce any new proof techniques or insights into the interplay between quantum models and ensemble methods. The analysis lacks a deeper exploration of how the specific properties of quantum classifiers, such as their representation power or entanglement capabilities, influence the ensemble's performance.

- Limited novelty in the findings. The finding that ensemble learning can improve upon weak learners is not new to most ML audience. Thus, the key findings in this paper are not novel. The paper essentially demonstrates that a standard ensemble method, AdaBoost, can be applied to quantum classifiers and achieve improved performance, which is an expected outcome. There is no surprising or counter-intuitive result that would significantly advance the field.

*Significance*

- Due to the limited novelty, this work seems of limited significance in both theoretical machine learning and quantum machine learning. The lack of novel theoretical contributions and the incremental nature of the findings weaken the overall significance of the paper. The work does not open up new avenues of research or provide a fundamental understanding of quantum ensemble learning.

*Reproductivity*

- As there is no code for this work, it is unclear whether the empirical results are reproductible.

### Questions
*Question 1: Theoretical novelty*

The analysis in this paper seems a direct combination of existing tools for ensemble learning and quantum classifiers. What are the non-trivial theoretical points in this work?

*Question 2: Difference with related work*

What are the main differences between this work and existing works for ensemble learning and quantum machine learning? Please respond precisely.

*Question 3: New findings*

What are the main differences in experiments between the quantum weak learners and weak (classical) classifiers?

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work mainly proposes a quantum counterpart of AdaBoost algorithm, giving the theoretical analysis of prediction error on the binary classification problem and numerically providing the proof-of-principle experiments.

### Strengths
The manuscript is well-written and clearly introduces the quantum AdaBoost under the framework of the variational quantum algorithm. From theoretical and numerical perspectives, it demonstrates the feasibility of improving the performance of a quantum learning model by combining a few weaker ones.

### Weaknesses
1. With the limitation of the system size and circuit depth, the study aims to combine a few weaker quantum classifiers to improve the performance. The manuscript does not show the quantum advantages of the proposed model compared to classical ones from neither theoretical nor numerical. For instance, giving some tasks that are challenging for classical algorithms but can be surpassed by quantum learning models. Specifically, the manuscript lacks a clear demonstration of a problem where the quantum AdaBoost approach outperforms its classical counterpart in terms of computational complexity or achievable accuracy. The numerical experiments should include a comparison with classical AdaBoost on a dataset where quantum methods are expected to show an advantage, such as a problem with high dimensionality or complex non-linear decision boundaries. 
2. The technical and conceptual contributions are not significant enough. The proposed quantum adaptation of AdaBoost, while novel, does not introduce a fundamentally new quantum learning paradigm. The theoretical analysis, while sound, does not reveal any surprising or breakthrough results. The paper would benefit from a more in-depth discussion of the limitations of the proposed approach and potential avenues for future research that could lead to more significant advancements. The current contribution seems to be a straightforward application of AdaBoost principles to a quantum setting, without addressing the core challenges of quantum machine learning.
3. In numerics, it only provides a single run which is insufficient. The lack of statistical significance in the numerical results makes it difficult to draw any strong conclusions about the performance of the proposed algorithm. The experiments should include multiple runs with different random initializations and a proper statistical analysis of the results, including error bars and confidence intervals. The current presentation of results as a single run is not convincing and does not allow for a robust evaluation of the method.

### Questions
1. The algorithm 2 points out the error of the base classifier should be small. However, under the limitation of circuit depth, how to guarantee the classifier $h_t$ has a small test error meanwhile with shallow circuit depth.
2. In theorem 3.1, it points out that the generalization error is bounded by the number of training samples $n$ and independent trainable gates $K$. Since we can increase the number of $K$ to improve the model and decrease the error, however, why do we increase $K$, the bound is getting worse, which is not reasonable. 
3. The quantum advantages are not quite clear, is there any evidence that the proposed method gives quantum advantages?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work exploits a quantum Adaboost method to enhance the generalization capability of quantum neural networks, where related theoretical analysis is provided. The work also demonstrates the ensemble architecture of quantum neural networks is promising on NISQ devices.

### Strengths
1. Using the Adaboost method for Quantum Neural Networks is interesting. 

2. The theoretical bounds for the quantum Adaboost algorithm are a necessary contribution.

### Weaknesses
1. In section 2.1, using multi-qubit quantum gates for the parametric quantum circuits is not optimal, as real multi-qubit quantum gates have to suffer from more serious quantum noise and are harder to deal with the Barren Plateau problem. Why not use single quantum parametric gates?

2. The Eq. (5) associated with the analysis of empirical risk minimizer is incorrect for the quantum neural network (QNN). The output of  QNN relies on the measurement, resulting in an additional optimization bias that is related to the expectation of observables. The authors can refer to the Reference as:

Ref. Jun Qi, Chao-Han Huck Yang, Pin-Yu Chen*, Min-Hsiu Hsieh*, "Theoretical Error Performance Analysis for Variational Quantum Circuit Based Functional Regression," Nature Publishing Group, npj Quantum Information, Vol. 9, no. 4, 2023

3. Accordingly, the theoretical upper bound on Eq. (9) is not complete. An additional optimization bias corresponding to the optimization bias needs to be considered.

4. The quantum Adaboost algorithm in Algorithm 2 is basically identical to the classical Adaboost one. So, what are the quantum advantages of quantum neural networks against classical neural networks? Since the performance of the classical neural networks can be also boosted to better performance, it is not clear why the authors highlight the quantum Adaboost counterpart.

5. The authors do not provide a deeper discussion for the simulations as shown in Figure 4 and 5, why more Rounds are beneficial to the performance boost for the quantum Adaboost system? and why does the quantum Adboost method even attains worse results at the very beginning?

### Questions
1. Why more rounds T can be beneficial to the proposed Adaboost method? 

2. Why not provide the classical neural networks to compare the Adaboost performance? 

3. If using the same Adaboost algorithm, what are the quantum advantages of using quantum neural networks?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
