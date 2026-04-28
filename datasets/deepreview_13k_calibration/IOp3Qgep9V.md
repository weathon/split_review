# Towards Adversarially Robust Condensed Dataset by Curvature Regularization

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 1, 3, 5

## Abstract
Dataset condensation is a recent technique designed to mitigate the rising computational demands of training deep neural networks. It does so by generating a significantly smaller, synthetic dataset derived from a larger one. While an abundance of research has aimed at improving the accuracy of models trained on synthetic datasets and enhancing the efficiency of synthesizing these datasets, there has been a noticeable gap in research focusing on analyzing and enhancing the robustness of these datasets against adversarial attacks. This is surprising considering the appealing hypothesis that condensed datasets might inherently promote models that are robust to adversarial attacks. In this study, we first challenge this intuitive assumption by empirically demonstrating that dataset condensation methods are not inherently robust. This empirical evidence propels us to explore methods aimed at enhancing the adversarial robustness of condensed datasets. Our investigation is underpinned by the hypothesis that the observed lack of robustness originates from the high curvature of the loss landscape in the input space. Based on our theoretical analysis, we propose a new method that aims to enhance robustness by incorporating curvature regularization into the condensation process. Our empirical study suggests that the new method is capable of generating robust synthetic datasets that can withstand various adversarial attacks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study how to compute a condensed dataset on which the trained models achieve good adversarial robustness. Specifically, the authors propose an algorithm GUARD, matching the gradients of the model trained on regularized loss, where the regularizer tries to punish large curvature. Finally the authors compare GUARD with other data condensation methods on MNIST, CIFAR10 and ImageNet under different levels of adversarial attacks.

### Strengths
The paper is written clearly and motivation is also clear. I personally think it is worth studying how to compute such condensed dataset which promotes adversarial robustness without adversarial training.

### Weaknesses
1. The theoretical part (section 5) is not sound enough.
2. The reference is not comprehensive. The main idea is to match the gradient which tends to have smaller curvature (sharpness). There are many existing literatures on how to reach flatter minima, e.g., sharpness aware minimization, implicit regularization. Though these works are not about condensaton, some of them might have relations to adversarial robustness (like arXiv:2305.05392). Also, there are other works also trying to give such adversarially robust condensation like arXiv:2211.10752, but they are neither mentioned and nor compared.

3. The definition of $h$ is missing in Proposition 1. 
4. Why is $\tilde \ell(x,v)$ convex in terms of $x$ in the appendix A given that $\ell(x)$ is convex? It's obvious that $\tilde\ell(x,\cdot)$ is convex but $\tilde\ell(\cdot,v)$ might not be convex. Say $\ell(x)=-x^3+3x^2$ and hence $\ell(x)$ is convex in $[0,1]$. The corresponding quadratic approximation $\tilde\ell(x,v)$ has second order derivative on $\frac{\partial^2\tilde\ell(x,v)}{\partial x^2}=-6x$ is non-positive in $[0,1]$, which implies that it is non-convex in $[0,1].$
5. I think eq(12) in the appendix A requires $h^{-1}(\cdot)$ to be a contraction map, why is that true? If it is true, then $\left\|h\left(x^{\prime}\right)-\mathbb{E}_{x \sim D_c}[h(x)]\right\| \leq \sigma$ basically implies that the distance between the $x'$ and the mean of training samples with label $c$ is no larger than $\sigma$. Is it a reasonable assumption?

### Questions
1. Is it $\phi$ or $\theta$ in "where $\phi$ is some neural network and D is a distance function in the parameter space" in page 4?
2. The definition of $h$ is missing in Proposition 1. 
3. Why is $\tilde \ell(x,v)$ convex in terms of $x$ in the appendix A given that $\ell(x)$ is convex? It's obvious that $\tilde\ell(x,\cdot)$ is convex but $\tilde\ell(\cdot,v)$ might not be convex. Say $\ell(x)=-x^3+3x^2$ and hence $\ell(x)$ is convex in $[0,1]$. The corresponding quadratic approximation $\tilde\ell(x,v)$ has second order derivative on $\frac{\partial^2\tilde\ell(x,v)}{\partial x^2}=-6x$ is non-positive in $[0,1]$, which implies that it is non-convex in $[0,1].$
4. I think eq(12) in the appendix A requires $h^{-1}(\cdot)$ to be a contraction map, why is that true? If it is true, then $\left\|h\left(x^{\prime}\right)-\mathbb{E}_{x \sim D_c}[h(x)]\right\| \leq \sigma$ basically implies that the distance between the $x'$ and the mean of training samples with label $c$ is no larger than $\sigma$. Is it a reasonable assumption?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the adversarial robustness property of a recent technique called Dataset Condensation (DC). DC learns to synthesize a smaller dataset such that models can still have good generalization performance if they are trained on this smaller dataset. The authors provided a negative answer to the hypothesis -- DC can generate datasets that can foster adversarially robust models by discarding non-observable features that often lead to adversarial vulnerability. Finally, the authors proposed a method called GUARD (Geometric regUlarization for Adversarial Robust Dataset) to improve adversarial robustness for DC methods by incorporating curvature regularization. The effectiveness of the proposed method is verified by some experiments on MNIST and CIFAR10 classification tasks.

### Strengths
+ The adversarial robustness property of DC methods has not been studied before. 

+ The authors first clarified that adversarial robustness is not held for DC and then proposed a method to improve such property.

### Weaknesses
 - Dataset Condensation (DC) was a recent technique that has not been recognized by many people. Whether it is promising to be used in the big data era is not clear. The authors proposed to study whether DC methods are adversarially robust. The motivation is very weak. I cannot see any significance in studying this topic. 

- Although overturned by the authors, the hypothesis "adversarial robustness might be inherently induced by the dataset condensation process" does not make much sense. It is not clear why DC can be linked with the previous work that suggested the adversarial vulnerability of models is often tied to these non-observable features since the authors did not study what type of features are discarded by DC methods. Also, the goal of DC seems to reduce training samples other than discarding non-observable features. The connection between these two types of work seems to be hallucinated without any evidence. 

- The novelty of the proposed method is not clear. Curvature Regularization has been considered by (Moosavi-Dezfooli et al. 2019). The technical novelty is limited.

- The experiment is weak. Only conduct on MNIST and CIFAR10.  Only evaluate ConvNet with 3 layers. 

- The authors only compare the adversarial robustness performance with several DC methods. The improvements are very marginal. For example, for l-inf attack, the performance of the proposed method is 0.7±0.2, which can not show any improvements. In other words, the proposed method also fails under this attack.

### Questions
What does Figure 1 mean?

What is the function of Figure 2?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article proposes improving the adversarial robustness of models trained on compressed training data using the dataset condensation technique to accelerate training. The author first empirically verifies that dataset condensation alone does not enhance the model's adversarial robustness. Then, through theoretical derivation, they suggest regularizing the curvature term when performing dataset condensation. Finally, the author conducts experiments to demonstrate the effectiveness of their approach.

### Strengths
The topic studied in this paper is valuable and indeed offers a new direction for improving the adversarial robustness of models. The writing of the paper is also well-done, providing a detailed introduction to previous work. The paper includes both theoretical analysis and complementary experiments to support its claims. Overall, the paper is quite comprehensive.

### Weaknesses
However, I have some concerns regarding both the method and the experimental results. Firstly, looking at the experimental section, I'm not quite sure what the improvement in adversarial robustness at the scale shown in Table 2 indicates, especially when considering the standard deviation. It seems to only weakly suggest that the proposed method may exhibit better consistency in terms of adversarial robustness. I find it difficult to consider this experimental result as strong support for the author's conclusions.

Regarding the method, the author uses Taylor expansion to find the relationship between adversarial samples and the first and second-order information of samples under the model. However, they only briefly mention that "previous work has shown that regularizing gradients gives a false sense of security about the robustness of neural networks" and then solely rely on the curvature term as a regularization term -- without further theoretical or experimental justification. I find this unacceptable. Furthermore, the approximation of the Hessian matrix is very rough, and there is no further exploration or explanation regarding the parameter $h$.

Overall, the research direction is indeed valuable, but the current version is too rough and would be difficult to be considered as a top conference paper.

### Questions
Apart from the concerns about the method and its experimental results, I have some other questions as well. 

Firstly, I am confused about the inequality sign in equation (2). If the adversarial samples are defined as maximizing the loss, then it seems that the inequality should be reversed. However, considering the higher-order terms, I am not entirely sure about the direction of this inequality. Please correct me if I misunderstood.

Secondly, I find the assumption in Proposition 1 regarding the convexity of $l(\cdot)$ confusing. Why can we make such an assumption?

Moving on to the experimental section, there is a significant decrease in performance on clean samples after applying this method (as shown in the appendix). I am unsure if this contradicts the statement mentioned in the paper that "in practice, it is important that the condensed data enable the model to perform well both in i.i.d test setting and under adversarial attacks" (currently, it seems contradictory). Additionally, these experimental results should be presented in the main body of the paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper highlights the vulnerability of existing dataset condensation methodologies to adversarial attacks and introduces a dataset condensation technique that takes adversarial robustness into account. The authors are motivated by the assertion that to ensure adversarial robustness, the data loss should exhibit a low curvature. Drawing inspiration from prior studies that enhanced adversarial robustness through curvature regularization, they bridge this approach with a gradient matching-based dataset condensation algorithm. As a result, they propose a methodology named "Geometric regUlarization for Adversarial Robust Dataset" (GUARD). The dataset produced using this methodology demonstrates superior adversarial robustness performance in various settings when compared to traditional techniques.

### Strengths
- The paper identifies the vulnerability of models trained using traditional data condensation methodologies to adversarial attacks, implying that condensed datasets might leverage spurious features and information.
- The authors point out that an adversarially trained model should possess a smooth loss landscape. They also highlight the challenges of adversarial training in dataset condensation, tackling the issue from a curvature perspective.
- By bridging two methodologies, gradient matching in data condensation and CURE in adversarial robustness, the paper introduces a robust data condensation method named GUARD. This proposed method integrates curvature considerations into the gradient matching process of condensed data via regularization.
- The results demonstrate that the proposed method achieves relatively higher robust accuracy compared to traditional methods. Furthermore, it displays superior performance and efficiency when compared with standard adversarial training techniques for dataset condensation.

### Weaknesses
 - Previous methodologies were conducted without considerations related to adversarial robustness. Achieving performance that doesn't significantly surpass these methods might not hold substantial meaning. Notably, the performance against strong attacks does not seem to indicate significant robustness. When proposing a methodology considering adversarial robustness, I believe that the proposed method should exhibit a performance better than random chance (10% for 10-class tasks) when subjected to strong attacks. The setting for strong attacks reflects the benchmark for invisible perturbations in the adversarial robustness research area. Approaches that fail to demonstrate significant performance improvements in this setting are arguably limited.
- Naturally, training methodologies considering adversarial robustness demand higher computational costs compared to standard training. Given that the proposed method appears to simultaneously utilize both the conventional method (gradient matching) and curvature regularization, it seems to require a relatively high computational cost (please correct me if I'm mistaken). However, the enhanced robustness performance doesn't seem to justify this computational overhead.
- The proposed method shows a decline in performance on regular data compared to traditional methods. While a trade-off between robustness and accuracy can be expected, the drop in clean accuracy doesn't seem to be adequately compensated by an increase in robust accuracy.

### Questions
- Has there been an analysis or experiment regarding the computational cost, specifically on the overhead introduced compared to traditional methodologies?
- Are there performance results under the general AutoAttack setting, which has the same epsilon upper bound as the strong attack?
- In the weaknesses section, drawbacks are highlighted using the standard strong attack as a reference. What are the author's thoughts on this? My knowledge in the dataset condensation field is limited; hence, I'm unaware if there have been studies focusing on adversarial robustness in this domain. Considering the methodologies compared in the paper, it appears there might not be. Therefore, it's challenging to judge the appropriateness of the paper's settings. Given that the model has been trained on limited data, I'd like to inquire whether it's suitable to compare the performances of methodologies under a weaker setting (epsilon=2), rather than the conventional adversarial settings employed in the vision domain.
- Are there any other cases where adding curvature regularization to methods other than gradient matching leads to an improvement (not marginal) in robustness performance?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
