# Residual Kernel Policy Network: Enhancing Stability and Robustness in RKHS-Based Reinforcement Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 8, 3

## Abstract
Achieving optimal performance in reinforcement learning requires robust policies supported by training processes that ensure both sample efficiency and stability. Modeling the policy in reproducing kernel Hilbert space (RKHS) enables efficient exploration of local optimal solutions. However, the stability of existing RKHS-based methods is hindered by significant variance in gradients, while the robustness of the learned policies is often compromised due to the sensitivity of hyperparameters. In this work, we conduct a comprehensive analysis of the significant instability in RKHS policies and reveal that the variance of the policy gradient increases substantially when a wide-bandwidth kernel is employed. To address these challenges, we propose a novel RKHS policy learning method integrated with representation learning to dynamically process observations in complex environments, enhancing the robustness of RKHS policies. Furthermore, inspired by the advantage functions, we introduce a residual layer that further stabilizes the training process by significantly reducing gradient variance in RKHS. Our novel algorithm, the Residual Kernel Policy Network (ResKPN), demonstrates state-of-the-art performance, achieving a 30% improvement in episodic rewards across complex environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper applies Reproducing Kernel Hilbert Space (RKHS) methods to policy gradient to enhance sample efficiency and stability in training. Additionally, it introduces a variance reduction technique inspired by residual networks, further improving the stability and effectiveness of the policy training process.

### Strengths
1. This paper introduce a new RKHS policy learning algorithm.
2. This paper introduces a variance reduction technique by designing a residual layer for the RKHS policy
3. The numerical results demonstrate the validity of the proposed method

### Weaknesses
1. While applying RKHS to reinforcement learning (RL) is not novel, this paper lacks a discussion of existing methods. Relevant references include: 
[1] Mazoure, Bogdan, et al. "Representation of reinforcement learning policies in reproducing kernel Hilbert spaces." arXiv preprint arXiv:2002.02863 (2020). 
[2] Wang, Yiwen, and Jose C. Principe. "Reinforcement learning in reproducing kernel Hilbert spaces." IEEE Signal Processing Magazine 38.4 (2021): 34-45. 
Additionally, some kernel-based methods, although not specifically RKHS-based, are also relevant to consider. 
2. Existing work, such as reference [2], introduces variance reduction techniques. A comparison or discussion of these approaches with the methods in this paper would provide valuable insights. Although RKHS is rarely applied to RL, there is extensive work on integrating RKHS with general machine learning problems. 
3. The idea of applying RKHS to RL appears straightforward, and the key distinctions from previous approaches remain unclear.

### Questions
1. Based on the numerical results, it appears that the main improvement stems from the residual design. However, the comparison models are baseline models without any variance reduction techniques, raising questions about the fairness of the comparison. Additionally, variance reduction methods introduced in previous works should be considered.
2. There is existing literature on combining RKHS with residual networks, and a discussion of these studies would add valuable context.
3. The numerical section would benefit from testing in more complex environments to strengthen the evaluation.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper, titled "Residual Kernel Policy Network: Enhancing Stability and Robustness in RKHS-Based Reinforcement Learning," addresses the instability and sensitivity in RKHS-based reinforcement learning policies. The authors show significant gradient variance and hyperparameter sensitivity and propose the Residual Kernel Policy Network (ResKPN). This network incorporates representation learning to adaptively align observations with the kernel's structure. The Authors also employ a residual architecture to further stabilize training. Experiments on MuJoCo tasks demonstrate ResKPN's performance, reportedly surpassing baseline algorithms like PPO and DPO by up to 30% in episodic rewards.

### Strengths
The technical claims are well-founded, and the experimental results are robustly supported by rigorous methodology. The integration of residual layers with RKHS gradients appears to reduce gradient variance, as confirmed by extensive empirical evidence on MuJoCo environments. The variance analysis is theoretically grounded, and experimental setups align well with the claims, ensuring soundness across technical aspects.

The presentation is clear overall, though there are instances where dense technical language or unclear phrasing makes comprehension difficult, especially in theoretical sections. Improved structuring or additional context around complex derivations could enhance readability.

This work contributes meaningfully to reinforcement learning research by empirically identifying a weakness in a common reinforcement learning approach. It attempts to solve this by introducing a model with enhanced stability and robustness through representation learning and a residual layer. The originality lies in effectively merging RKHS gradient variance reduction with neural network-based feature extraction, a strategy not previously well-addressed. The approach is promising for applications requiring adaptive, high-dimensional policy learning. However, just adding a residual neural network to an existing method has limited originality.

- Significance: Tackling gradient variance in RKHS-based reinforcement learning is critical for real-world applications, and the results demonstrate potential for improved robustness.
- Experimental Rigor: Extensive tests across six MuJoCo tasks validate ResKPN’s efficacy and its edge over comparable baselines in terms of episodic rewards and convergence rates.
- Practical Impact: The adaptability of ResKPN to complex, high-dimensional environments shows promise for real-world reinforcement learning scenarios.

### Weaknesses
Complexity of Variance Analysis: While theoretically thorough, the variance analysis may benefit from simplification or additional visual explanations. This complexity could present a barrier for researchers less familiar with RKHS. The current presentation relies heavily on mathematical derivations without providing sufficient intuitive explanations or illustrative examples, making it difficult to grasp the core concepts and practical implications of the variance reduction. Specifically, the introduction of notations like \(\Gamma_A\), \(\Gamma_V\), and \(\Gamma_{h,\mu}\) without sufficient context or motivation can be confusing for readers not deeply versed in RKHS theory.

Computational Cost: Given the use of RKHS, the method may face scalability limitations in more extensive settings or when applied to multi-agent environments. The computational overhead associated with kernel methods, particularly the need to compute and invert kernel matrices, can be prohibitive in large-scale or real-time applications. The paper does not adequately address the practical implications of this computational burden, such as the increased training time and memory requirements, which could limit the applicability of the proposed method in resource-constrained settings.

Limited Discussion on Alternative Kernels: While Gaussian kernels are utilized effectively, the paper could explore the feasibility of other kernels or adaptive kernel selection strategies to further broaden the model's applicability. The exclusive use of Gaussian kernels limits the generalizability of the findings, as different kernels may be more suitable for specific types of data or tasks. The paper lacks a comprehensive discussion on the potential benefits and drawbacks of alternative kernels, such as Laplacian, polynomial, or sigmoid kernels, and does not explore the possibility of dynamically adapting the kernel based on the characteristics of the environment or the learning process.

### Questions
Could the authors expand on how ResKPN might handle multi-agent or cooperative environments? Given the scalability challenges, it would be valuable to understand the model's limitations in such settings. How would the approach adapt to environments where action spaces vary significantly in scale or complexity? Neural networks often succeed in settings with large amount of training data, would such a setting be appropriate for a non-parametric method such like RKHS? 106: h is a functional (function -> values), but notation h(s) is used, s is a state, not a function so why do we call h a functional?

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
3

### Summary
This paper sets out to make a new SOTA in RL policy gradient algorithms, by modifying a method from reproducing kernel Hilbert space (RKHS) reinforcement learning, where policies are represented as Gaussians in a RKHS.  This allows policies to be learned in a space that captures relationships and correlations in large-dimensional action spaces.

The paper argues that previous RKHS RL approaches have suffered for two reasons.  First, the selection of the kernel is important and difficult, and an improper kernel choice leads to underperformance.  Second, RKHS RL is particularly vulnerable to high variance in the gradients, leading to unstable learning.

The paper addresses these issues by introducing ResKPN. This policy algorithm addresses the representation problem by applying the kernel to a learned representation of the state rather than to the state itself, and the high variance problem by introducing a residual layer in the representation to empirically decrease this variance.

The paper shows that policies learned via ResKPN outperform or compete closely with benchmark algorithms like PPO on a variety of standard RL problems.

### Strengths
- The problem is clearly explained.  It is clear what problems with RKHS RL the authors are setting out to fix, and how those problems motivate the produced algorithm.
- The mathematics and notation are professionally done, and are easy enough to follow (though I didn't go through the derivations in the appendices).
- The writing is clear.
- The experiments in the experimental section are comprehensive and convincing.
- A more effective RL baseline is significant... if it's usable (see weaknesses/questions).

### Weaknesses
 - An important argument of the paper is that representation and variance problems cause RKHS RL to fail.  Accordingly, something like the illustrations of the representation and variance problems (Figure 1) are probably necessary, but I do not find these particular illustrations very effective.  They show that on one problem, some Gaussian kernels are ineffective, and that on another (single) problem, high variance can be seen.  I don't think they reinforce the strong causal relationship that the authors intend to convey, particularly when the high variance is itself dependent on the kernel selection.  Representation problems are certainly easy enough to believe, but the fact that the fully connected layer is effective *because it diminishes variance*, rather than (for example), just because it augments the representation, is not so clearly argued.
- How slow is this? Seems like it might be very slow... Is it slow enough to be near-unusable?  I think this should be addressed with a table of training times in the appendix.

**Minor things**
- The system being trained in this algorithm is complex, with lots of different sets of parameters ($\theta, \iota, \delta...$).  I think Figure 6 is important enough that it should probably be promoted to the regular paper, as the explanation is not clear enough to stand on its own without it.  The critic network should also be integrated into this figure.
- On line 96, $U(w)$ should be $U(\pi_w)$.
- On line 191, should be $\sigma^2=0.3, 0.5, 0.7,$ and 0.9.
- Wording on lines 262-263 is not correct.
- On line 299, "The key idea of residual layer" should be "They key idea of the residual layer" (or "motivating the residual").

### Questions
- How slow is this?  Please provide some training time comparisons with PPO.
- Do you have any further explanation or intuition for the variance-kills-RKHS-methods argument?  Would minibatches mitigate this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the challenges of achieving optimal performance in RL using policies modeled in reproducing RKHS. While RKHS-based methods offer efficient exploration of local optima, they suffer from significant instability due to high variance in policy gradients and sensitivity to hyperparameters. The authors analyze the causes of instability, particularly highlighting the increased gradient variance with wide-bandwidth kernels. To resolve these issues, they propose the ResKPN, a novel approach that integrates representation learning to process complex observations and introduces a residual layer inspired by advantage functions. This residual layer reduces gradient variance, thereby improving training stability and policy robustness. The ResKPN algorithm achieves state-of-the-art performance, with a 30% increase in episodic rewards across multiple complex environments.

### Strengths
The paper presents a clear and well-defined contribution by addressing the instability and sensitivity issues in RKHS-based reinforcement learning methods. The introduction of the ResKPN and the integration of representation learning and a residual layer provide a novel solution to these challenges. The contribution is clearly articulated, with a strong emphasis on how the proposed method improves stability and performance in complex environments. The significant 30% improvement in episodic rewards further highlights the effectiveness of the approach.

### Weaknesses
A notable weakness of the paper is the absence of available code for the proposed ResKPN. The lack of code limits reproducibility and hinders other researchers from validating the results or building upon the work. Providing access to the implementation would significantly enhance the paper's impact and facilitate further exploration of the proposed methods.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
3
