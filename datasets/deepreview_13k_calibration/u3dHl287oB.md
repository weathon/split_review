# The Joint Effect of Task Similarity and Overparameterization on Catastrophic Forgetting — An Analytical Model

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 3, 6, 8, 8, 3

## Abstract
In continual learning, catastrophic forgetting is affected by multiple aspects of the tasks. 
Previous works have analyzed separately how forgetting is affected by either task similarity or overparameterization. In contrast, our paper examines how task similarity and overparameterization \emph{jointly} affect forgetting in an analyzable model. 
Specifically, we focus on two-task continual linear regression, where the second task is a random orthogonal transformation of an arbitrary first task (an abstraction of random permutation tasks). We derive an exact analytical expression for the expected forgetting --- and uncover a nuanced pattern. In highly overparameterized models, intermediate task similarity causes the most forgetting.  However, near the interpolation threshold, forgetting decreases monotonically with the expected task similarity. We validate our findings with linear regression on synthetic data, and with neural networks on established permutation task benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present an analytical upper bound for the expected amount of catastrophic forgetting during linear regression with gradient descent as a function of overparameterisation and overlap between tasks. In particular, they show that there exist two phenomenologically different learning regimes: In the overparameterised regime (i.e. $rank({\bf X}) / rank({\bf w})$ small) intermediate similarity between tasks leads to largest amount of forgetting (inverted U-shape) and monotonic behaviour is observed near the interpolation threshold ($rank({\bf X}) / rank({\bf w}) \approx 1$). To this end, the authors make the following assumptions: (1) The target values for both tasks $({\bf y})$ are identical, (2) both tasks are realisable (i.e. a zero-loss solution exists) (3) the second task is an orthogonal projection of the first task (c.f. permutation) and (4) the first task has successfully converged to the global, minimum-norm solution of task one before training on task two. By changing the subspace which the orthogonal operator transforms, the overlap between the tasks can be exactly controlled and its effect analytically studied.


**--------------------------------------**

**Unfortunately, I can not add official comments (anymore), thus I will add my comments to the author's comments here**

**Reply 1**
Weaknesses 1&2 and Questions 1,2,3: Thank you for the clarifications. As it is not obvious from section 2.1 why equation (3) is the closest point on the solution manifold when starting to train from the convergence point of task 1, I would like to suggest to include this derivation in the appendix.

Weakness 3: Thank you for the clarification.

Weakness 6: As there is no direct mapping from permuting MNIST to DOTS, I have mild concerns that the observed phenomena could be explained away by the fact that most information is in the center of the image and thus increasing the permuted area from the center to the outside may result in a non-linear transformation of the dimensional of the data-manifold. If the effect is non-linear, comparisons to phenomena observed when manipulating DOTS would be erroneous. However, I appreciate that the authors try to test their hypotheses on more complex data.

Weakness 4: The minimum-norm solutions studied by the authors are part of the "rich" learning regime. The lazy regime does exist in (multi-layer) linear networks. For example, in the regression model, weight values that lay in the null-space of the training data of the first task could be unequal zero. For example, when initialising the weight matrix from large random values, GD would still converge to a gloabl optimum, however, the convergence points would be unequal to equation (2) and (3). Thus, I would argue that the presented analytical results only apply to the rich learning regime.

Further, in an over-parametrized linear two-layer network, the first layer can be initialised, large and arbitrarily (and in theory even kept fixed). GD would still converge to a global optimum, however, as a consequence, the learned representations in the hidden layer would be "lazy". Again, I don't think that the analytical result apply to this regime and thus simulations that compare these two regimes (i.e. training from (very) small initial weights and training from large initial weights) would be useful. 

See also question: For Figures 6 & 7, how are the neural networks initialized? Do they operate in the rich or lazy regime?


**Reply 2**
I would like to thank the authors for addressing my questions.

Weakness 5: Thank you for adding these additional simulations.

Question: Can you give an intuitive explanation for why the expected forgetting is non-asymptotic for overparameterized regime and near interpolation threshold

Sorry, that question was not very well formulated. What I tried to ask is: Do you have an intuitive explanation for why in the overparametrized regime, the expected forgetting for increasing task dissimilarity if falling off, whereas near the interpolation threshold, it keeps increasing?

**The following points remain unaddressed:**

- **Weakness 7: Simulation details and / or code are not provided which makes interpretation of simulation results difficult and reproduction impossible.**
- **Weakness 10: The introduction to continual learning / catastrophic forgetting is, in my opinion, not referenced well enough**


As a result of the changes made by the authors I have increased my rating to a 6.

**--------------------------------------**

### Strengths
The authors tackle an important research question: What are the underlying mechanisms that govern catastrophic forgetting during the continuos acquisition of knowledge using gradient descent. Their analytical result fully describes phenomenologically distinct operating regimes during the continuous optimisation of a linear regression model using gradient descent. The authors validate their analytical result using simulation studies and test whether their results generalise to more complicated two-layer networks. Notation is consistent throughout the paper and explanations for variables, equations and derivations are provided. The paper and plots are generally well structured and accessible.

### Weaknesses
1. The model (i.e. single linear projection) and algorithm (gradient descent, full-batch gradient descent?!) are not stated in the introduction. Information about the regime to which the analytical result applies is scattered throughout the paper, which makes it difficult to contextualise the results. Specifically, the precise optimization algorithm (e.g., stochastic gradient descent with a specific batch size or full-batch gradient descent) and the learning rate schedule are not clearly defined in the introduction, making it hard to understand the scope of the analysis. The lack of clarity regarding the optimization procedure makes it difficult to assess the practical relevance of the theoretical findings.
2. It would be really helpful if all assumptions of the analytical result would be stated explicitly and collected within one section of the paper. For example, the ${\bf 0}$ initialisation and resulting convergence to the global, minimum-norm solution of the first task is hidden in Scheme 1 but crucial to understand the extent of the analytical result. The assumptions should be clearly stated in one place, including the zero initialization, the convergence to the minimum-norm solution, the realizability of both tasks, and the specific orthogonal transformation applied to the second task. This would significantly improve the clarity and accessibility of the theoretical framework.
3. I think the paper could benefit from making it more explicit that the analysis focuses on the dimensionality and overlap with respect to the manifold of the data distribution, which is often called overparametereised, but should not be confused with the overparameterisation deep networks (i.e. wide hidden layers). The paper should clearly distinguish between the overparameterization in linear models, which is related to the rank of the data matrix, and the overparameterization in deep networks, which is related to the number of neurons or layers. This distinction is crucial to avoid misinterpretations of the results.
(4. Resulting from 3., the model can not be used to make predictions about the underparameterised regime, e.g. bottlenecked networks.) This limitation should be explicitly stated. The analysis is restricted to scenarios where the number of parameters is greater than or equal to the rank of the data matrix, and therefore, it does not provide insights into the behavior of underparameterized models, such as those with bottleneck layers.
5. I think the paper should state explicitly that the analysis is limited to the rich learning regime. It does not provide any insights into the lazy learning regime. Comparisons and references from the paper’s “overparameterised regime” to e.g. the NTK regime are confusing and incorrect. The analysis is limited to the rich learning regime, where the weights are updated significantly during training. The paper should explicitly acknowledge that it does not apply to the lazy learning regime, where the weights change very little during training. The connection to the Neural Tangent Kernel (NTK) regime should be clarified, as the current analysis does not directly apply to it.
6. Simulation results in Figure 2. are limited to $d = 2$. There are no simulation results to validate the analytical result for edge-cases like p = d and large(r) d etc. The simulation results should be extended to include cases where the number of parameters is equal to the rank of the data matrix ($p=d$) and cases with large values of $d$ relative to $p$. This would provide a more comprehensive validation of the analytical results.
7. I am not entirely sure if the author’s version of permuted MNIST is suitable to study changes in task similarity that are comparable to DOTS, as vanilla MNIST data is on a very low dimensional data manifold and large parts of the information is centred on the middle of the picture. I think I would prefer a simulation study that uses artificial data as in Figure 4., with well controlled DOTS in two layer networks. The use of permuted MNIST to study task similarity might be problematic due to the low dimensionality of the data manifold and the concentration of information in the center of the images. It would be beneficial to include simulation studies with artificial data, similar to Figure 4, where the task similarity is more precisely controlled, especially in the context of two-layer networks.
8. Simulation details (initialisation scheme, learning rates etc.) and / or code are not provided.

Minor:
9. The notation in equations (2) and (3) is confusing. There are too many equal signs
10. The introduction to continual learning / catastrophic forgetting is, in my opinion, not referenced well enough
11. Using X_1 and X interchangeably is confusing and seems unnecessary

### Questions
- To what optimisation algorithm does the analytical result exactly apply?
- Could you please hint me at the Theorem in Gunasekar et al. (2018) from which equation (3) is derived?
- What assumptions are made on the size of batches and the size of the learning rate?
- Why does Theorem 3 have the assumption of p >= 5?
- Why can you assume that a randomly sampled data matrix X is identical to the worst case in Figure 2?
- The smallest expected forgetting in the interpolation regime (except for values close to 0 DOTS) is larger than the largest expected forgetting in the overparametereised regime. Why is that the case and how is it relevant to the analysis?
- Is there a benefit of using an informal illustration instead of slices from figure 3 in figure 1? The inverted U-shape seems to be slightly exaggerated as expected forgetting for large DOTS don’t fall off nearly as strongly as suggested by the illustration.
- Can you give an intuitive explanation of why the expected forgetting are (non-)asymptotic for overparameterised regime and near the interpolation threshold?
- Do the authors think that their results do generalise to learning more than two tasks? I think that would clearly contradict some of the assumptions and thus maybe should be listed as a limitation of the work?
- Is it maybe possible to use a log-scaled axis in Figure 3 instead of using subplots to represent the results?
- Is it possible that the x-axis of Figure 3, bottom right is labelled incorrectly? Values from 0 to 0.1 seem to be missing
- For figures 6. and 7., how are neural networks initialised? Do they operate in the rich or lazy regime?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to reveal the connection between the parametrization regime and forgetting. The authors start by analyzing the forgetting in a linear regression model and define their definition of their specific distribution shift for the second task. Moreover, the upper bound of the forgetting (derived as the loss of task 1 after learning task 2), is calculated and later used for different parameterization scenarios. The authors conclude that in an overparametrized regime, forgetting decreases as the task dissimilarity increases, however, in an underparametrized scenario, the trend is reversed (more forgetting for more dissimilar tasks). Finally, they evaluated the soundness of their derivations in a custom version of the permuted-NIST tasks.

### Strengths
I think the presentation in the paper is concise and to the point. The mathematical derivations in the given context are sound and clear. Maybe it would be better to show some of the derivations in eq 4 in the appendix but overall it is fine. 

The results within the linear regression and simple nist-type experiments look interesting and worth pursuing in future works.

### Weaknesses
 **Limited scope:** The main issue that I see in the paper is the limited scope of the provided analysis. I am fine with simple experiments in a theoretical paper but the upper bound of forgetting is very specific to the linear regression task. The derived bound relies heavily on the properties of linear models and the specific form of the distribution shift, making it unclear how these results generalize to more complex models or different task relationships. The analysis does not consider non-linearities or the hierarchical nature of representations learned in deep networks, which are crucial aspects of modern continual learning scenarios. 

**Overparametrization proxy:** The second issue is tightly related to the above, in theorem 3,  the proxy for overparametrization is defined as $1 - \frac{d}{p}$, where $d$ is the rank of the input data and $p$ is the data dimensionality. It makes sense in linear regression since the number of parameters is the same as the data dimension, i.e., $p$. This is true to some extent in the MLP layers (at least they are correlated). However, none of the derivations hold in the case of the convolutional layers where there are shared parameters and $p$ cannot be a surrogate for the number of parameters. The paper lacks a discussion on how the proposed overparameterization proxy relates to the actual number of parameters in deep learning models, particularly in convolutional layers where parameter sharing is prevalent. This makes the theoretical results difficult to interpret in the context of practical deep learning architectures. I encourage the authors to evaluate their upper bound in CNNs. 

**Task similarity definition:** Also, the definition of task similarity is very limited to the rotation of a subset of the data dimensions. All of the derivations are based on this initial assumption. I believe a good theoretical paper on this subject should expand this definition so that more real-world cases can be included in the analysis. The current definition is too narrow and does not capture the complexity of task relationships in real-world continual learning scenarios. My comment is the same for the permuted-NIST scenario. A simple permutation of a subset of pixels is not enough to back the main message in this more challenging scenario. The analysis would benefit from considering more complex task relationships, such as those involving semantic shifts or changes in the underlying data distribution beyond simple rotations or permutations.

### Questions
My question goes back to the previous comments:

**Q1:** Is the overparametrization proxy enough to provide a similar analysis in the CNN case? i.e., can we just substitute the $p$ with the number of parameters in a CNN layer?

**Q2:** Have the authors tried to evaluate their upper bound in more challenging scenarios?

**Q3:** Have the authors tried to test their upper bounds when the definition of the task similarity is different? i.e., more subtle semantic distribution shifts in the data. e.g. CIFAR-100 Superclass.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides a mathematical analysis of how task similarity and overparameterization jointly affect forgetting in continual learning. By proposing a pair of orthogonally transformed datasets, authors define their similarity measurement DOTS $\alpha$ and the level of overparameterization $\beta$. Theorem 3 provides the worst-case expected forgetting w.r.t $\alpha$ and $\beta$. Furthermore, synthetic and empirical experiments provide more support for the proposed analysis.

### Strengths
1. Writing is clear and easy to follow.
2. Their novel result provides a new perspective for forgetting analysis in continual learning.
3. The theoretical result is solid and consistent with empirical results.

### Weaknesses
1. The dataset assumption is strong, which only focuses on 2 datasets, and can be converted by orthogonal transformation. 
2. It is unclear how DOTS can compare with the notion of similarity in related works.

### Questions
1. Is the theory able to provide worst-case forgetting analysis with more general dataset assumption, or T>2 datasets?
2. It is still unclear that how DOTS relates to other notions of similarity, e.g. the principle angles in Evron et al. (2022). Is that possible to plot a figure that shows the relation between DOTS and $\theta$?
3. In Evron et al.(2022), Figure 3 shows the worst-case forgetting on T=2 tasks, where p=d-1(rank(X1)=rank(X2)=d-1), which in this paper, should corresponds to $\beta=1-\frac{d-1}{d}\approx 0$, which should fall into the very less overparameterization regime. However, there results still show the descent with a large angle. Can authors provide some explanation? (And this is also one of the reasons I hope to know how DOTS relates to $\theta$)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper considers the continual learning problem in the case of two linear regression tasks. The first task is arbitrary, while the second is assumed to be a random orthogonal transformation of the first one.

The main result of the paper is a precise expression of the normalized, expected forgetting (Theorem 3). The expression is related to the level of task similarity and overparameterization.

The paper proceeds to specialize the main theorem to the highly overparameterized regime and at the interpolation threshold, visualizing the amount of forgetting on synthetic data or the MNIST dataset.

### Strengths
The paper has several strengths:
- First, while the proof idea is straightforward (e.g., as shown in the proof sketch), it involves lengthy algebraic manipulations that the paper manages to excel in; this is commendable.
- Related to the first strength, even though the proof can be lengthy, the main paper is clearly written and easy to understand.
- The experiments numerically verify the correctness of the theorem and provide interesting insights into catastrophic forgetting. While some of the observations have been made in prior works, the paper suitably discussed that, and moreover provided different results in the highly overparameterized regime.

### Weaknesses
While I tend to vote for acceptance, I do have several questions or comments:

- At first glance it seems a little bit weird to have the same $y$ for two different tasks. I think it might be motivated by the case of permuted MNIST where permutations do not change the label. It would be great if the authors could comment on that in their revision.
- Certainly there is some gap between the theory and MNIST experiments. The authors are encouraged to discuss that gap. For example, the training loss in the theory vs test error in the experiments. The least-squares loss in the theory vs classification loss in the experiments (I suppose).
- Is there any deeper connection between the bound in the highly overparameterized regime, $\alpha^2(1-\alpha)^2$, and the corresponding bound in Lemma 9 of Evron et al. (2022) for the case $k=2$?
- While the main theorem is accomplished by algebraic calculations, I wonder whether there is a geometric proof that would achieve the same. For example, the two steps can be thought of as two projections (onto certain subspaces), and the forgetting can be bounded deterministically by some quantity related to the principal angles. With a random orthogonal transformation, the principal angles between the two subspaces would be in some sense random. Would it be easier if one analyzes the randomness of the principal angles, and could the algebraic proofs be replaced by geometric reasoning?

### Questions
See above.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In order to explore the common impact of task similarity and overparameterization on forgotten, the paper obtains a conclusion through formula derivation. The conclusion shows a non-monotonic behavior in task similarity when the model is suitably overparameterized, and a monotonic behavior when it is critically overparameterized. In addition, the paper verified the conclusion through a large number of experiments.

### Strengths
This paper obtained a precise and effective conclusion through a large number of formula derivations and experiments. This conclusion can help us better understand the forgetting problems of the model.

### Weaknesses
The experimental setting of the paper is very limited, and the scope of application of the conclusions is questionable. The reliance on pixel shuffling as the sole method for manipulating task dissimilarity is a significant limitation. This approach does not adequately capture the complexities of real-world task variations, where changes in semantic content, object relationships, or environmental conditions are more common. Furthermore, the exclusive use of the MNIST dataset raises concerns about the generalizability of the findings to more complex datasets with higher dimensionality and more intricate feature relationships. The paper's analysis, while mathematically rigorous, is primarily focused on linear models, and it remains unclear how these conclusions translate to non-linear neural networks, which are more commonly used in practice. The paper does not sufficiently address the potential impact of different activation functions, network architectures, or optimization algorithms on the observed forgetting behavior. The definition of overparameterization in the context of this paper also needs further clarification, especially its relationship to the model's effective learning capacity and its impact on the generalization performance.

### Questions
1.	Is the conclusion proved to be universal? If in a non-linear complex neural network, is the model forgetting the same as the conclusion?
2.	We can only mess up pixels as a standard of dissimilarity, which does not match the real scene. So it's hard to verify the conclusions on other data.
3.	Is overparameterization equivalent to the learning capacity of the model? Do the conclusions of the paper apply to other data and models?
4.	The formulas derived in this paper are rather complicated. Can you please explain Pseudoinverse Properties and Operator Norm Properties in detail?
5.	This paper only conducted experiments on the mnist dataset. Can the same conclusion be reached for other complex datasets?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies catastrophic forgetting in an analytical way. 
Specifically, they focus on two-task continual linear regression and uncover a pattern in overparameterized models 
where intermediate task similarity leads to the most forgetting.

### Strengths
1. The results under overparameterized models are interesting.

### Weaknesses
1. The writing needs improvement as it is difficult to grasp the central logical structure.
2. Format in assumption 1 seems not correct since there is a long blank.
3. The proof is difficult to follow, I can tell why the three terms in Lemma 6 can be replaced by the long formulas.
4. I think the paper 'Analysis of catastrophic forgetting for random orthogonal transformation tasks in the overparameterized regime' discusses a similar task. It is difficult to tell what the difference and improvement compared to that.

### Questions
1. I have tried to read all proof, but it is difficult to follow and check all the long expressions. 
I think it will be better to make the proof clearer to understand.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
