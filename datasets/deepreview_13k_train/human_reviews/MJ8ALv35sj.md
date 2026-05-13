# How Does Cross-Layer Correlation in Deep Neural Networks Influence Generalization and Adversarial Robustness?

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
\textit{Generalization} and \textit{adversarial robustness} are two critical concepts in machine learning. Understanding the key factors that affect the trade-off between these concepts is essential for guiding architectural design and developing training strategies, such as adversarial training, especially for deep neural networks. In this paper, we investigate the impact of cross-layer correlations in weight matrices on both generalization and adversarial robustness. We provide a theoretical analysis demonstrating that increasing cross-layer correlations leads to a monotonic increase in the generalization gap. Furthermore, we establish a connection between adversarial risk and natural risk. Leveraging this connection, we show that in linear models, higher cross-layer correlations also degrade adversarial robustness. Finally, we validate our theoretical findings through experiments conducted on MLPs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies the impact of cross-layer correlation on the generalization and adversarial robustness of deep neural networks. The authors present a theoretical analysis demonstrating that higher cross-layer correlation leads to a larger generalization gap and reduced adversarial robustness in linear models. Finally, empirical studies on MLPs are included to support these findings.

### Strengths
**Originality:** This paper investigates the effect of weight correlation on model generalization and adversarial robustness, with a specific focus on cross-layer weight correlation.

**Quality:** The analysis combines both theoretical and empirical perspectives.

**Significance:** This work contributes to understanding how architectural design influences model generalization and robustness, offering insights valuable for future network design.

### Weaknesses
Theoretic analysis: The claim that cross-layer correlation worsens the generalization gap appears trivial and resembles findings by Jin et al. In particular, the comparison in Lines 306–309 suggests that this work may simply serve as a specific example of the weight correlation explored in Jin et al.

In Theorem 4.2, the assumption of the same correlation coefficient between pairs of elements across adjacent weights seems quite strong and unrealistic. How crucial is this assumption in achieving the monotonically increasing result?

Empirical analysis: The fact that two of the ReLU-activated MLPs do not align with the trend described in the analysis (showing the lowest correlation but not the smallest gap) is concerning. The authors’ brief explanation, attributing this to limited learning capacity, is insufficient.

Additionally, the studies in Figures 1 and 2 are very restrictive as they only focus on TRADES. How were the $\beta$ values selected, and why is this training method the only one examined?

The discussion of Figure 2 also lacks detail. Could the authors clarify the specific phase transition being referenced?



### Questions
In discussing the trade-off between robustness and generalization, Fawzi et al., 2018 is cited both in support of and against this claim, i.e., Ln43 vs Ln46 and Ln99 vs Ln105. Could the author clarify the position of the paper on the trade-off?

The second contribution claims that the trade-off is "fundamental to the nature". Could the author provide a more precise definition or explanation of what they mean by this?

Ln100: Could the authors clarify what is meant by 'robust in tasks involving small distinguishability'?

Ln169: The phenomenom was first noticed by Szegedy et al. in Intriguing properties of neural networks.

Ln 214: Could the authors explain why it is reasonable to assert that the generalization gap is significantly influenced by the KL term when $\gamma$ is not too large? 

In Eq12, does $|l-s|<1$ mean $l=s$?

Ln448: "with 40 iterations" repeated.

Ln453: "The cross-layer correlation was averaged across layers". Do we consider all possible combinations of cross-layer correlations when averaging the results? I suggest the authors to provide a detailed explanation of how they calculated the average cross-layer correlation, including which layer combinations were considered and how they were weighted in the average.

### Soundness
3

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
2

### Summary
This study theoretically investigates the impact of cross-layer correlation on both the generalization gap and adversarial risk. The authors reveal that an increase in layer correlation worsens both the generalization gap and the difference between natural risk and adversarial risk, referred to as the adversarial gap.

### Strengths
The novelty of this research is that it clearly demonstrates, both theoretically and experimentally, the negative impact of cross-layer correlation on the generalisation gap and adversarial robustness of neural networks. The paper provides new insights by connecting the issues of generalisation and adversarial robustness, which have tended to be treated separately in the past, through the common factor of cross-layer correlation. In particular, the fact that the generalisation ability of the network decreases and the adversarial risk increases when the correlation between the weights of the layers is high provides new suggestions for more robust neural network design.

### Weaknesses
See Questions.

1. Why is the generalisation gap smaller for the larger $\bar{\tau}$ in the linear and relu6 cases with Depth=4,2 in Table 1? Does this mean that the theory is too conservative and the bounds are meaningless?
2. Does Eq.13 work for larger networks? For example, if you increase the size of the network, does the correlation between layers decrease, and does the upper limit of the generalisation gap decrease, etc? Are these phenomena observed experimentally?
3. The author says that the correlation between the output layers in Figure 2 increases towards the end of training, and that this represents a phase transition in learning. What does this mean?
4. Please clarify the limitations of this analysis. This paper theoretically demonstrates the intuitive result that generalization performance declines when the correlation between layers increases. While I think that this kind of research is very meaningful, I also think that clearly demonstrating the limitations of the theory is important for subsequent researchers.

### Questions
1. Why is the generalisation gap smaller for the larger $\bar{\tau}$ in the linear and relu6 cases with Depth=4,2 in Table 1? Does this mean that the theory is too conservative and the bounds are meaningless?
2. Does Eq.13 work for larger networks? For example, if you increase the size of the network, does the correlation between layers decrease, and does the upper limit of the generalisation gap decrease, etc? Are these phenomena observed experimentally?
3. The author says that the correlation between the output layers in Figure 2 increases towards the end of training, and that this represents a phase transition in learning. What does this mean?
4. Please clarify the limitations of this analysis. This paper theoretically demonstrates the intuitive result that generalization performance declines when the correlation between layers increases. While I think that this kind of research is very meaningful, I also think that clearly demonstrating the limitations of the theory is important for subsequent researchers.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies the effect of cross-layer correlations in neural networks on generalization and robustness. Both theoretical and empirical results show that larger cross-layer correlations increase the generalization gap and degrade robustness.

### Strengths
- The paper investigates how cross-layer correlations affect both adversarial robustness and generalization, which is novel in the community.
- The theoretical work is supported by comprehensive empirical evidence, covering both shallow and deep neural networks.

### Weaknesses
 - The statement of the theoretical results is unclear with a lot of undefined and confusing notation.
    - In line 130: '\bm{x}' should not denote the input domain, as it typically represents a single input instance. The authors should clarify whether they are referring to the entire input space or a specific input.
    - In equation 3, why is W not bolded while sometimes the vector or matrix is bolded? Also, the dimension of W is not mentioned. This makes it difficult to understand the mathematical operations and the scope of the analysis. It is crucial to define whether W is a matrix or a vector, and to specify its dimensions (e.g., $N_l \times N_{l-1}$).
    - In line 226, $N_l$ and $N_{l-1}$ are not defined. The authors should explicitly state what these variables represent (e.g., the number of neurons in layer $l$ and $l-1$, respectively) and where they are used in the context of the neural network architecture.
    - The notation ''$Cov_\pi$ and $Cov_\rho$' in equation 12 are confusing, why is there a subscript in the covariance? also the '0' should be bolded because it is an all zero matrix. It is unclear what the subscripts $\pi$ and $\rho$ represent in the context of covariance. The authors should clarify if these refer to different distributions or measures from which the weights are sampled. Additionally, the zero matrix should be denoted in boldface to distinguish it from a scalar zero.
    - The $\sigma_l$ in line 239 is defined as a covariance matrix, but since it is a scalar, it should be the variance. The authors should be consistent with the definition of $\sigma_l$ and clarify whether it is a scalar variance or a covariance matrix.
    - In line 488, ``with iteration number of 40, with 40 iterations'' is repetitive.

- Why does equation 13 study the lower bound of the KL term? According to equation 11, only the upper bound of the KL term makes sense. The authors need to justify why a lower bound of the KL divergence is relevant when the generalization bound is expressed in terms of an upper bound. The connection between the lower bound of the KL divergence and the upper bound of the generalization gap is not clear.

- In line 344, there is no trade-off between adversarial risk and natural risk, according to equation 23, the adversarial risk increases monotonically with natural risk. with natural risk. The authors should clarify the relationship between adversarial and natural risk, and if there is a trade-off, it should be explained more clearly. The current interpretation of equation 23 suggests a monotonic relationship, which contradicts the claim of a trade-off.

### Questions
- In line 211, what is the 'slight difference'? What is the difference in the technical proof? Why there is a 2$\gamma$ term instead of $\gamma$?
- In line 302, why does Theorem 4.2 suggest that layers in a neural network should be as uncorrelated as possible?  
- [1] has shown that the generalization gap will increase as the weight correlation increases, so what is the contribution in section 4 when compared to [1]?

Ref

[1] Gaojie Jin, Xinping Yi, Liang Zhang, Lijun Zhang, Sven Schewe, and Xiaowei Huang. How does
weight correlation affect generalisation ability of deep neural networks? Advances in Neural
Information Processing Systems, 33:21346–21356, 2020.

### Soundness
2

### Presentation
2

### Contribution
2
