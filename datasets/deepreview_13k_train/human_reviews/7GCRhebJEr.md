# Robustness via learned Bregman divergence

- Decision: Reject
- Scores: 8, 6, 3, 3

## Abstract
We exploit the Bregman divergence to generate functions that are trained to measure the semantic similarity between images under corruptions and use these functions as alternatives to the $L^p$ norms to define robustness threat models. Then we replace the projected gradient descent (PGD) by semantic attacks, which are instantiations of the mirror descent, the optimization framework associated with the Bregman divergence. Adversarial training under these settings yield classification models that are more robust to common image corruptions. Particularly, for the contrast corruption that was found problematic in prior work we achieve an accuracy that exceeds the $L^p$- and the LPIPS-based adversarially trained neural networks by a margin of 29\% on the CIFAR-10-C corruption dataset.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an interesting learned similarity metric between images based on Bregman divergence and shows that this metric allows for the training of classifiers more robust against image corruption. L_p distances are widely used to assess the robustness of discriminative models because of mathematical convenience, not because they capture a principled notion of invariance in the data domain. The proposed Bregman divergence is demonstrated to be a promising alternative, contributing both to the literature on metric learning out-of-distribution robustness.

### Strengths
* The paper presents a mathematically elegant formulation for metric learning (via self-supervised Bregman divergence learning) and adversarial training (based on mirror descent).
* The authors show preliminary evidence that their method learns a “geometry of image corruptions.”
* From a brief literature review (and bolstered by the paper’s thorough review of related work) I believe the proposed training procedure is indeed novel.
* The comparison to the LPIPS divergence metric shows that the proposed Bregman divergence is an effective metric for learning robust models.
* The methods are very well presented and approachable.

Minor comments:
* I found Table 1 to be very helpful in making the work approachable.
* Algorithm 1 nicely documents the settings for hyperparameters.

### Weaknesses
 * The experiments are only conducted on CIFAR10-C, which is a single, simplistic dataset. I would like to believe that the results would hold on a more complex dataset like ImageNet-C, but this is not demonstrated in the paper. The Conclusions seem to acknowledge that scaling to larger convex architectures for the base function could be challenging.
* One of the issues of using Bregman divergences to measure image similarity is that these divergences are not necessarily symmetric. Many image augmentations are symmetric. While the authors mention the possibility of using a symmetrized version of the Bregman divergence, they do not explore this option thoroughly, and it is unclear how this would affect the learned metric and the robustness of the model.
* Lemma 1 is not important to include in the main text. The alternative approach in A.2 is a much simpler method to draw samples, which does not require the complicated statement of the Lemma; in fact the experiments use the simpler version in A.2! Moreover, due to typicality, sampling from a normal distribution in high dimension will essentially sample from the surface of a hypersphere.
* The computation of the $\Gamma$ function should be tractable, and not require approximation. It is not clear why the authors are approximating this function, and this could introduce inaccuracies in the computation of the Bregman divergence.
* The experiments are not particularly strong. The proposed approach does not perform best on the zoom blur corruption. Furthermore, the paper lacks a thorough analysis of the learned metric's properties, such as its sensitivity to different types of image corruptions and its ability to capture meaningful semantic relationships between images. This makes it difficult to assess the true potential of the proposed approach.

Small issues:
* I believe that the paper’s contribution on defining a new method for metric learning should be highlighted in the abstract.
* It feels like Equation 3 is out of place. Perhaps it should be in the next section on Mirror descent? I think it should also be admitted up front that while this projection is unique, it is not available in closed-form for neural networks (Table 1), thus you use a line search heuristic. The lack of a closed-form solution for the projection onto the Bregman ball is a significant limitation, and the authors should discuss the implications of using a heuristic approach.
* In Table 1, the mirror map for KL divergence is missing a +1 term.
* In the Mirror Descent paragraph in Section 2, I think it should say “mapping $z^{t+1}$ back to the **primal** space”.
* $\tau$ is used before definition in Equation 7 (def isn’t until Section 3.3).
* The caption of Figure 2 should be re-written. I had to read it a couple of times to understand what the plot is showing.

Small typos:
* “settings yield**s**” should be plural in the abstract.
* In the 1st sentence, the phrase “the way” is awkward.
* “AT was found to **improve also**” should be “also improve”.
* In 3.2 you use a \citet when it should be a \citep for Fenchel.
* In the first paragraph of Section 5, Hendrycks should be a \citet.
* Adversarial Training paragraph page 8: “use it”
* Last sentence: “cope” should be “scope”.

### Questions
1. Did you assess the L_p adversarial robustness of your models trained with the Bregman notion of robustness? Do you have any idea whether your robust models exhibit any of the beneficial characteristics (e.g. perceptual gradients) observed in robust models trained with adversarial training?
2. When you are training the Inverse Map (Eq. 7), do you use a `detach` operation in practice, i.e. to train the inverse map to emulate the base function without optimizing over the parameters of the base function? As written, this loss would seem to indicate that the base function is optimized to emulate the inverse map.
3. Do you have any metrics of the fit of the inverse map on the test data? Isn’t it also true that the inverse map could be fine-tuned during test time on the test points (i.e. the learned inverse map is a form of amortization).
4. How are corruptions $\tau$ sampled during training? Do you draw a single pair $\tau, d$ for each training image as an augmentation?
5. Since the projection $\Pi_K$ is not available in closed form for a learned base function, the paper uses a binary search heuristic. Can you show that this procedure would lead to convergence in the limit $\eta \rightarrow 0$?
6. Do you have any observations or conjectures about the right modes in the divergence plots (Figure 2)?
7. What is your choice for distance $d$ in Figure 3?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the corruption robustness of classifiers, and proposes a variant of adversarial training with perturbations sought according to a similarity measure, which is learned using corruption models. The similarity measure is defined as Bregman divergence, with a learned base function, and mirror descent is employed for seeking perturbations. The experimental results show that the approach outperforms $\ell_2$ and LPIPS based adversarial training towards corruption robustness.

### Strengths
- The paper is well written and the overall approach to employ Bregman divergences and mirror descent is well-motivated
- The discussion of the learned base functions for Bregman divergence for different corruptions provides interesting insights towards less artificial threat models.
- The experimental results show good performance on CIFAR-10-C, compared to $\ell_2$ adversarial training and RLAT.

### Weaknesses
 - The idea of learning similarity measures and generating suitable adversarial examples is interesting. However, since the work aims to increase the robustness of classifiers it needs to be discussed to what extend the corruption model can be practically known. Specifically, while CIFAR-10-C provides a set of simulated corruptions, the practical applicability of these models to real-world scenarios needs further justification. The paper should address whether the learned similarity measures generalize to unseen, real-world corruptions, or if they are overfit to the specific corruption models used during training.
- The method is compared to $\ell_2$ adversarial and RLAT method in the experiments, but in-distribution performance and data augmentation baselines seem to be missing. The absence of in-distribution performance makes it difficult to assess whether the proposed method sacrifices clean accuracy for robustness. Furthermore, comparing against data augmentation techniques, which are commonly used for improving robustness, is crucial to understand the relative benefits of the proposed adversarial training approach. Specifically, it is unclear how the proposed method compares to simple data augmentation strategies that might also incorporate the corruption models used for training the similarity measure.

### Questions
- Could the authors provide some more information on the in-distribution performance and on the performance of data augmentation baselines (which might also use the corruption model $\tau(x)$)?
- In Table 3 the corruption robustness accuracy is shown for the different models and on different corruptions. Do the authors have any insights on why the model trained on contrast (via learning the similarity measure) performs well on both contrast and fog, whereas the model trained on fog performs worse in both categories?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The study examines the use of Bregman divergence as an alternative to the $L^p$ norm for measuring the distance between benign and corrupted samples. It also explores the application of mirror descent, based on Bregman divergence, to identify corruptions for adversarial training. This is accomplished by constructing two convex neural networks that approximate the gradient of the distance-generating function and its inverse. Training the networks involves utilizing a Bregman loss. Additionally, a semantic attack is proposed using Bregman divergence to generate corrupted examples, which are then employed in adversarial training to enhance corruption robustness.

### Strengths
1. The organization of this paper is clear and logical. The motivation and procedures of the proposed method are well-described.
2. The proposed method is novel, and the experimental results demonstrate its superior performance compared to the baseline methods across different corruption severities.

### Weaknesses
1. The assertion that $(\nabla\phi)^{-1}=\nabla\bar{\phi}$ relies on the assumption of ICNN being of the Legendre type, which is not rigorously proven. The numerical method proposed for approximating the inverse $(\nabla\phi)^{-1}$ seems to deviate from Fenchel's (1949) result. While Equation (7) suggests that minimizing $\min_f \Vert f(\nabla\phi(x)) - x\Vert_2$ should yield $f=(\nabla\phi)^{-1}$, the optimality of using the L2 distance is not justified. A more thorough analysis of the choice of the L2 norm and its implications on the approximation accuracy is needed.

2. The evaluation in this paper has limitations. For instance, it remains unclear how the Bregman divergence training converges. Additionally, it is uncertain whether the method can scale to larger images, such as ImageNet. How does the choice of sampling numbers impact the approximation? Providing convergence analysis and demonstrating scalability to larger datasets would strengthen the paper.

3. The Bregman-based attack seeks the projection point $x'$ in the intersection of $D$, which is defined as the intersection of $B_{\phi}$ and $B$. The algorithm suggests projecting onto $B$ first, and then onto $B_{\phi}$. However, this procedure does not guarantee that the resulting projected point will reside within the intersection. A more rigorous explanation or modification of the projection method is required to ensure the projected point lies in the intersection.

4. Although Lemma 1 indicates that $d$ lies in the range $(0, 1)$, the rationale behind generating Figure 1 with $d=1$ is not clearly explained. Clarifying the choice of $d$ in Figure 1 and its relation to Lemma 1 would enhance the understanding of the visualization.

5. In the experiment, the fraction of $\Gamma$ functions is defined as $1/\sqrt{n}$. The purpose of introducing $\mu$ as the fraction of Gamma functions in Lemma 1 is not clear. A more detailed explanation of the role of $\mu$ and its connection to the experimental setup would be beneficial.

6. Based on my understanding, each iteration of mirror descent involves one forward pass and one backward pass for the input $x^t$. It is unclear how the computation cost of Bregman divergence training is determined. Providing a detailed breakdown of the computational cost, including the number of forward and backward passes required, would clarify the efficiency of the proposed method.

7. The notations in the equations lack consistency, such as the font used for variables like $\tilde{x}$ and $u$. Ensuring consistent notation throughout the paper would improve readability.

### Questions
See weaknesses

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper uses Bregman divergence for adversarial learning, which the authors argue to be more robust and can be more accurate.

### Strengths
The exposition is nice and the manuscript is easy to follow.

### Weaknesses
Adversarial learning is a fast-growing field. That being said, I failed to see the technical novelty of the proposed approach: the results appear to be straightforward and the technical contributions are limited. There is only one lemma and an algorithm in the current manuscript, making the paper more like in an engineering manner. The use of Bregman divergence, while offering some theoretical advantages, does not seem to translate to a significant practical improvement over existing adversarial training methods. Specifically, the paper lacks a thorough comparison to state-of-the-art adversarial training techniques, making it difficult to assess the true value of the proposed approach. The presented lemma, while mathematically sound, does not provide a substantial theoretical contribution that advances the field beyond known results. The algorithm itself is a direct application of Bregman divergence within an adversarial learning framework, lacking any unique or innovative algorithmic components.

### Questions
See my comments in the limitations.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
