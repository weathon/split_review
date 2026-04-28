# From Search to Sampling: Generative Models for Robust Algorithmic Recourse

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Algorithmic Recourse provides recommendations to individuals who are adversely impacted by automated model decisions, on how to alter their profiles to achieve a favorable outcome. Effective recourse methods must balance three conflicting goals: proximity to the original profile to minimize cost, plausibility for realistic recourse, and validity to ensure the desired outcome. We show that existing methods train for these objectives separately and then search for recourse through a joint optimization over the recourse goals during inference, leading to poor recourse recommendations. We introduce GenRe, a generative recourse model designed to train the three recourse objectives jointly. Training such generative models is non-trivial due to lack of direct recourse supervision. We propose efficient ways to synthesize such supervision and further show that GenRe's training leads to a consistent estimator. Unlike most prior methods, that employ non-robust gradient descent based search during inference, GenRe simply performs a forward sampling over the generative model to produce minimum cost recourse, leading to superior performance across multiple metrics. We also demonstrate GenRe provides the best trade-off between cost, plausibility and validity, compared to state-of-art baselines. We release anonymized code at: https://anonymous.4open.science/r/GenRe-BD71

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors propose a generative model designed for algorithmic recourse, which transforms a negative sample $\mathbf{x}^-$ into a positive sample $\mathbf{x}^+$. The resulting positive sample must satisfy the following criteria:

- $\mathbf{x}^+$ is a high-quality sample that adheres to the underlying data distribution.
- $\mathbf{x}^+$ is classified with a high probability as belonging to the positive class by a pre-trained classifier.
- $\mathbf{x}^+$ should be close to $\mathbf{x}^-$ in the feature space.

The authors demonstrate that training a single model to simultaneously meet these objectives leads to improved overall performance compared to previous approaches.

### Strengths
Some strengths of this work include:

- The development of a single generative model that converts negative examples into positive samples suitable for addressing the algorithmic recourse problem.
- The model enhances the overall performance of recourse mechanisms.
- The authors have anonymously open-sourced their codebase, allowing others to reproduce their approach.

### Weaknesses
## Clarity
The notation, definitions, and equations should be carefully rechecked. In the current form of the paper, the following points severely reduce the paper's readability, and the reader has to guess what is most likely implied.

- Quantities are not properly defined.

     1. In Eq. (2), the cost function employed in this work is not defined. What is the cost? Did the authors provide clarifications regarding its final form?
     2. Line 251, $N^+$ is not defined.
     3. Eq (6) what is $\lambda$ values? 
     4. Algorithm 1, Line 290: what is $\mathbf{x}$
     5. Algorithm 2: Where is the projectCategoricals defined? What is $m_c$?
     2. Algorithm 2: Line 5, is $k$ sampled? If yes, how?

- Notation Consistency
     1. Are the bin scales the same as bin widths? If yes, please be consistent.
     2. Is $D_1$ the same as $N^+$
     3. Alg. 1: Line 290: $\mathbf{x}$ is not defined.
     3. Alg. 2: Step 1: $\mathbf{x}$ is not defined.
     4. Eq (7) and (8) seem to have different K.
     5. I suggest to limit the notation to $\mathbf{x}^+$ and $\mathbf{x}^-$ whenever possible.


- Are you using a random forest or an MLP for the classifier? If you use both, in which case do you use the first and the second? What is the accuracy of each classifier?

- For the baselines, how are the final checkpoints selected?

- Something is weird; why do you select variance equal to zero (line 376)? This choice makes step 2 of Algorithm 2 redundant.

## Experiments

### Efficiency analysis
- How does the proposed approach differ from prior work regarding the number of parameters, training time, and GPU/time requirements (during training/inference)?

### Ablations
- What is the benefit of using an autoregressive model for generation compared to other architectures? Did the author try a different setup? What is the models' performance for different generative architectures (non-autoregressive)?

## Minor
- Lines 557-560 double entry for the same paper.
- Steps can be added to Alg. 1 similarly to Alg. 2.
- Proofs can be moved to the appendix.

### Questions
1. What is the purpose of "TopK" in Line 290? What does "Top" refer to? Is this clarified in the main text? I was unable to find any explanation.  
2. How does the model determine which dimensions of $\mathbf{x}^-$ to freeze? Are these dimensions predefined by the dataset? How is the loss function formulated in practice?  
3. Have you started training the generative model from scratch, or are you using pre-trained weights?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces GenRe, a generative-based approach to algorithmic recourse that seeks to optimize three core recourse objectives via joint training, including validity, proximity, and plausibility. The authors claim that previous method fail to unify all objectives into the training and instead use a gradient-based inference time searching technique that could lead to unsatisfying performance. GenRe uses an auto-regressive generative model to sample recourse solutions directly, with a hand-craft training objective defined with the cost function and the vanilla data distribution. The authors validate GenRe's performance through comprehensive experiments on synthetic and real-world datasets.

### Strengths
- First of all, the paper is well-written and organized, making it easily followed. The problem definition and motivation are presented clearly, allowing readers to understand the contribution.
- Undoubtedly, the problem of recourse via AI is an important and open problem. It is also closely related to conditional generation, and consequently, the technical discussion (if useful) can be apply to a wide range of problems beyond.
- I appreciate that the authors analyze their proposed method on various tasks, helping us to understand the performance of GenRe.

### Weaknesses
I think the major weaknesses are a lack of careful motivation of the proposed method, as well as a more direct comparison with methods beyond the field of algorithmic recourse (but can be directly applied). Specifically,

- From the aspect of this specific problem (algorithmic recourse), if I understand correctly, the major improvement in the training process is the goal of Eq (4), which includes all properties that users care about (as well as the empirical distribution $Q(x^+|x)$ for sampling). However, to me, this task is different from sampling over $P(x|y=1)$ only because the additional cost function, $C(x,x')$ should be imposed. As a result, a very clear derivation is to sample from the distribution of $P(x|y=1)\exp^{-\lambda C(x,x')}$. The introduction of $V(x')$ seems to break the probabilistic explanation of the distribution, because $P(y=1|x)$ is naturally contained in $P(x|y=1)$ by the Bayesian law. In addition, the reason for choosing an auto-regressive model for sampling is also left unjustified, as sequential sampling is not a major concern in the problem. More justification (both intuitively and experimentally, and ideally, theoretically) of the technique selection is unavoidable. 
- From a more general sense of conditional generation, the problem of cost-aware sampling is not a novel problem and has been studied both in a general scenario and for specific generative models such as AR models or diffusion models. For instance, a direct method if to train a classifier-free diffusion model that allows sampling from $P(X,Y)$, and use a standard guidance technique (such that the $L_2$ norm like the CLIP score) to guide the diffusion process using $e^{-\lambda C(X, X')}$. The proposed training technique for unpair data (Sec 4.1) is, in fact, a very standard processing technique that has been widely used, and the choice of AR model seems to be more strange than another generative model such as VAE and diffusion. Therefore, while I admit that joint training is a new approach (in this field, maybe), the author should compare with the above alternatives to see if the proposed method can outperform existing baselines. One paper for reference: [Learning from Invalid Data: On Constraint Satisfaction in Generative Models]. In addition, [Classifier-Free Diffusion Guidance] is a straight-forward go-to method to compare with.

### Questions
No additional question beyond the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces **GenRe**, a generative model that provides actionable, realistic recourse for individuals affected by automated decisions. By jointly optimizing for **proximity** (low cost), **plausibility** (realistic changes), and **validity** (desired outcomes), GenRe outperforms traditional methods that address these goals separately. Rather than using gradient-based search, GenRe generates recommendations through efficient sampling, offering robust, balanced recourse. The model's code is publicly available to support further research and applications.

### Strengths
GenRe effectively integrates proximity, plausibility, and validity into a single generative model, addressing the core challenges of algorithmic recourse in a unified way. This contrasts with traditional methods that optimize these objectives separately, offering a more balanced solution.

By using forward sampling instead of gradient-based search, GenRe reduces computational costs during inference. This makes the model more scalable and applicable to real-world scenarios where speed is crucial.

The paper demonstrates that GenRe achieves better trade-offs between cost, plausibility, and validity compared to existing methods, providing evidence of its effectiveness across multiple datasets and scenarios.

The authors have made their code available, promoting transparency and enabling other researchers to build on their work, which helps advance the field of algorithmic recourse.

### Weaknesses
While GenRe shows improvements in the tested scenarios, its generalizability to highly diverse datasets or domains with different types of constraints might require additional adjustments or fine-tuning.

The paper acknowledges the challenge of synthesizing recourse supervision for training, which may introduce assumptions or heuristics that could impact the model's robustness in practice.

The success of GenRe heavily depends on the quality of the generative model and the training data. If the data is biased or limited, the recourse recommendations might be less effective or skewed.

### Questions
Are there particular large-scale use cases you envision as especially suited for GenRe's capabilities? Can you implement GenRe in a modern generative model, such as a pretrained one?

How does it handle biased or limited datasets? 

As GenRe integrates multiple complex objectives, how do you ensure interpretability in the generated recommendations?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses the problem of algorithmic recourse for individuals adversely impacted by automated model decisions. It proposes a generative model based method to finish recourse task by directly sampling without optimization at inference. The main goal is to balance three objectives: proximity to the original profile to minimize cost, plausibility to ensure realistic changes, and validity to achieve the desired result. Experimental results shows its effectiveness.

### Strengths
* This paper provides a thorough analysis of the limitations in current algorithmic recourse methods, highlighting the challenges of separately optimizing proximity, plausibility, and validity, which often leads to suboptimal results. This establishes a solid foundation and motivation for the proposed method.
* The GenRe method is intuitive and easy to implement and consistently providing more effective trade-offs among different factors.

### Weaknesses
1. **Advantage beyond Nearest neighbor**: The biggest issue is the neccessity of involving a complicated auto-regressive method. Essentially, this method uses a model to learn a smoothly-mixed version of nearest-neighbor search in positive samples. It lacks detailed analysis and ablation study for its advantage beyond simple KNN. Why should we bother to train a huge transformer instead of just finding the nearest valid sample and imitate it? I believe there are subtleties here because it requires some generalization stuff. But all these aspects are absent in the paper. Specifically, the paper does not explore how the method performs with varying sizes of the training dataset. It's possible that the advantage of the generative model diminishes with larger datasets where nearest neighbor search might suffice. Furthermore, the paper does not investigate the impact of different distance metrics on the nearest neighbor baseline, which could significantly affect its performance and potentially close the gap with the proposed method. A thorough comparison should include multiple distance metrics and analyze the sensitivity of the nearest neighbor approach to these choices. The paper should also provide a more rigorous analysis of the computational cost and time complexity of training the generative model compared to the simpler nearest neighbor approach. This is crucial for practical applications where computational resources might be limited.
2. **Interpretability Issue**: While GenRe is effective in balancing recourse objectives, the generative approach may lead to less interpretable outputs, especially for stakeholders who require clear, actionable insights. The model could benefit from an analysis of interpretability or user-friendliness of the generated recourse. The paper should explore methods to quantify the interpretability of the generated recourse, such as by measuring the complexity of the changes or the number of features modified. Additionally, it would be beneficial to include a user study to assess how easily stakeholders can understand and act upon the generated recourse. A comparison with simpler, more interpretable methods would also help to highlight the trade-offs between interpretability and performance.

### Questions
See weakness.

Also, after reading the original definition of LOF, it is higher when the data point is more abnormal (out of distribution). Why is there a upper arrow in table2?

### Soundness
3

### Presentation
3

### Contribution
2
