# ADAM Optimization with Adaptive Batch Selection

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Adam is a widely used optimizer in neural network training due to its adaptive learning rate. However, because different data samples influence model updates to varying degrees, treating them equally can lead to inefficient convergence. To address this, a prior work proposed adapting the sampling distribution using a bandit framework to select samples adaptively. While promising, both the original Adam and its bandit-based variant suffer from flawed theoretical guarantees. In this paper, we introduce Adam with Combinatorial Bandit Sampling (AdamCB), which integrates combinatorial bandit techniques into Adam to resolve these issues. AdamCB is able to fully utilize feedback from multiple actions at once, enhancing both theoretical guarantees and practical performance. Our rigorous regret analysis shows that AdamCB achieves faster convergence than both the original Adam and its variants. Numerical experiments demonstrate that AdamCB consistently outperforms existing Adam-based methods, making it the first to offer both provable guarantees and practical efficiency for Adam with adaptive batch selection.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces the AdamCB algorithm, aiming to address inefficiencies in the Adam optimizer by improving data sampling. AdamCB integrates combinatorial bandit techniques, enabling adaptive batch selection to focus on informative samples. The authors claim enhanced theoretical guarantees, providing a rigorously analyzed regret bound that surpasses those of standard Adam and its bandit-based variant, AdamBS, which are identified here as having flawed guarantees. Experimental results across diverse datasets demonstrate the practical benefits of AdamCB, indicating faster convergence and greater efficiency.

### Strengths
1. This paper rigorously addresses and corrects the theoretical flaws in convergence guarantees for both Adam and AdamBS, presenting refined proofs that offer independent value to the community.
2. The proposed AdamCB algorithm is shown to be both theoretically robust and empirically effective, with rigorous analysis and extensive experimental validation.
3. The paper presents the method and supporting claims clearly, facilitating reader comprehension and enhancing accessibility of the technical content.
4. Through a fair and thorough comparison, this paper evaluates AdamCB alongside Adam and AdamBS, incorporating corrected theoretical guarantees to provide a balanced assessment.

### Weaknesses
1. The paper's motivation could benefit from further clarification and depth. In the abstract and introduction, the authors state that uniform sampling leads to inefficiencies in Adam, but they should specify the type of inefficiency (e.g., memory, computational, time, or convergence efficiency; presumably the latter). Additionally, the authors should provide evidence or discussion showing that alternative sampling methods indeed improve Adam's efficiency, strengthening the case for the proposed approach. Specifically, the authors should clarify whether the inefficiency refers to the convergence rate, the quality of the solution found, or some other aspect. Furthermore, the paper should include a more detailed discussion of why uniform sampling is inherently suboptimal for Adam, perhaps by showing cases where it leads to slow convergence or poor generalization, and how alternative sampling methods address these issues.
2. Algorithm 3 requires prior knowledge of $L$ for the weight update rule, which may be limiting in practical applications. It would be valuable to discuss potential ways to relax this requirement or clarify how the authors manage this constraint in practice. The paper should address the practical challenges of estimating or choosing an appropriate value for $L$. If $L$ is too small, the algorithm may not converge, and if it is too large, the convergence may be slow. The authors should also discuss how sensitive the algorithm is to the choice of $L$ and provide guidelines for selecting a suitable value in different scenarios.

### Questions
1. In the weight adjustment section, it is unclear why AdamCB requires the sum of probabilities to equal $K$ instead of 1. This choice appears to necessitate an additional operation in the sampling strategy, specifically the introduction of a threshold $\tau$. Clarification on the rationale behind this requirement would be beneficial.
2. The paper could further explain why increasing the sample size $n$ leads to faster convergence in AdamCB. A theoretical or intuitive justification for this relationship would strengthen the understanding of the algorithm’s convergence behavior.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a variant of the Adam optimizer with a combinatorial bandit approach (AdamCB) for adaptively selecting batches to train on.  Using a combinatorial bandit to select a batch of examples addresses the limitation of a prior approach called Adam with Bandit Sampling (AdamBS) which failed to improve performance with larger batch size due to myopic approach of selecting a single sample at a time with replacement.  Another core contribution of the paper is new theoretical analysis of Adam, AdamBS, and the proposed AdamCB that relaxes prior assumptions as well as fixes errors in the prior proofs.  These convergence guarantees show AdamCB to have faster convergence than Adam and AdamBS and faster convergence with increasing batch size.  Experimental studies show AdamCB to outperform Adam and AdamBS on small scale MLP and CNN tasks.

### Strengths
The primary strengths of this paper are as follows:
- The writing is clear and easy to understand.  
- The assumptions required for the convergence analysis is more general than previous work and the theory also covers Adam and AdamBS.  
- The paper identifies and addresses incorrect assumptions made in the analysis of AdamBS.

### Weaknesses
 - The experiments are fairly limited in scale and not very reflective of practical settings that we are in these days with large models and large datasets.
- The benefits of adaptive selection will likely be limited in settings with large model dimensionality since then the $d\sqrt{T}$ term will dominate the $\sqrt{d}/n^{3/4}T^{3/4}$ term controlled by adaptive selection.  The potentially marginal improvement of adaptive selection is not discussed as far as I can tell in the main paper (it is discussed in the AdamBS paper).
- It is unclear how useful bandit selection will be in settings where we see the entire dataset just a few times as with LLM pretraining.
- It seems like the theoretical analysis has a lot of overlap with Tran et al. 2019 but this is mainly mentioned in the Appendix and not stated in the main text.  It also detracts from the novelty of the theoretical analysis.

### Questions
The convergence rate of Adam, Adam with Bandit Selection, and the proposed Adam with Combinatorial Bandits are all dominated by the $d\sqrt{T}$ term.  In practice, what is the expected speedup of using combinatorial bandit in training settings with >100 million parameters?

In the LLM setting, not only are models over 100 billion parameters in some cases, we also rarely loop through the full dataset if at all during pretraining.  What benefits if any do you expect adaptive batch selection to provide in this setting?

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
This paper proposes an extension of the Adam optimizer by integrating adaptive batch selection. It also identifies a flaw in the proof presented in previous papers. Based on extensive theoretical analysis and some experiments, the proposed method demonstrates better convergence and improved performance.

### Strengths
1. This paper clearly points out the flaw in the proof of previous papers.
2. This paper provides a new convergence rate of Adam/AdamBS in the new perspective.
3. The results on some simple datasets are better than baselines.

### Weaknesses
I appreciate the theoretical contribution, and my major concern is the applicability of this method in real-world applications. Since the optimizer is one of the most fundamental components of the entire machine learning process, I wonder if this method can be directly integrated into existing practices. Additionally, I question whether the performance remains robust given the extra effort required to assign sampling bias towards certain samples during batch construction. Please see the question part for more details.

### Questions
1. **Semi-supervised learning**: Semi-supervised learning is a popular machine learning task where the testing dataset is given without labels. In this context, I wonder if the adaptive sampling method can still assign weights to both training and unlabeled testing samples.

2. **Extra regularizations**: Many regularization techniques are sample-agnostic, such as weight decay and dropout. Sometimes, regularization is only related to the output instead of the input, for example, using a total-variation loss to encourage smoothness in image generation. How does the adaptive sampling method work in these cases?

3. **Adversarial samples/noises**: The paper mentions that "samples with a low gradient norm are assigned a low weight, whereas samples with larger gradient norms are more likely to be chosen in future iterations." What if there is noise in the dataset, which is common in real-world datasets? Is it beneficial for the model to learn more from noisy samples that are difficult to fit?

4. **Data augmentation**. Does this method compatible with data augmentation? The augmented data will share strong similarity among samples. What should be considered when using data augmentation? Will the training be biased in an unexpected manner?

5. **Comparison with other methods for data sampling**: Given the popularity of large language models (LLMs), it is important to fine-tune/pretrain LLMs with a wise combination of data. Is there any potential to demonstrate this method in such a setting? How does this method compare with currently adopted reinforcement learning-based methods for sampling, such as "DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining, NeurIPS 2023"?

### Soundness
3

### Presentation
3

### Contribution
3
