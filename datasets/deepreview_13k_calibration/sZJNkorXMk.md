# Autocorrelation Matters: Understanding the Role of Initialization Schemes for State Space Models

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Current methods for initializing state space model (SSM) parameters primarily rely on the HiPPO framework \citep{gu2023how}, which is based on online function approximation with the SSM kernel basis. 
However, the HiPPO framework does not explicitly account for the effects of the temporal structures of input sequences on the optimization of SSMs.
In this paper, we take a further step to investigate the roles of SSM initialization schemes by considering the autocorrelation of input sequences. 
Specifically, we: (1) rigorously characterize the dependency of the SSM timescale on sequence length based on sequence autocorrelation; (2) find that with a proper timescale, allowing a zero real part for the eigenvalues of the SSM state matrix mitigates the curse of memory while still maintaining stability at initialization; (3) show that the imaginary part of the eigenvalues of the SSM state matrix determines the conditioning of SSM optimization problems, and uncover an approximation-estimation tradeoff when training SSMs with a specific class of target functions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies the initialization strategy used in SSM from various point of view, namely the time scale, the real and imaginary part of the state matrix. It demonstrates the dependency of the SSM timescale on sequence length based on sequence autocorrelation. Further it is shown that having a zero real part for the eigenvalues of the SSM state matrix mitigates the curse of memory. Finally, the paper demonstrates that the imaginary part of the eigenvalues of the SSM state matrix determine the conditioning of SSM optimization problems, and present a approximation-estimation tradeoff when training SSMs with a specific class of target functions.

### Strengths
1. The paper has presented some very novel an interesting insights into the initialization scheme for SSM.
2. The analysis is well grounded and thorough.
3. The experiments are well though out, extensive and results are convincing of the claims made in the paper.

### Weaknesses
While the experimental results are convincing on the datasets considered in the paper, how are the expected to hold in larger scale experiments? Can authors comment on that.

What do the authors think of extending these insights or draw parallel to setting(s) where the sequence length can be varied?

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
An analysis of the effects of some parameters of the so-called SSM layer is provided. Specifically, the authors analyze 1) the relation between the timescale $\Delta$ and the sequence length $L$, 2) the effect of the (zero) real part of the time evolution matrix, and 3) the effect of the imaginary part of the time evolution matrix, both theoretically and empirically.

### Strengths
- The claims are clear, and most of them are supported both theoretically and empirically.
- The topic is indeed important as the SSM-based models are increasingly used in various problems.
- Although the analyses may not be surprising per se in terms of dynamical systems theory, their implication especially in using SSM architecture sounds new and useful.

### Weaknesses
The empirical evaluation is limited to synthetic data or somewhat simple benchmark data. This fact does not much diminish the value of the paper, but reporting the applicability of the proposed theory to more real-world datasets would certainly be appreciated.

A thing remained a bit unclear to me is that how the discussions are necessarily relevant only to the initialization. Doesn't it make sense to constrain the parameter values (e.g., $\Re(W)$) as guided in the given theory, not only at the initialization but also during training iterations? As the paper's title emphasizes the role of *initialization*, a bit more discussion in this regard might be helpful.

### Questions
No questions that may change my evaluation.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides a theoretical analysis of a state-space model from three perspectives: discretisation size ($\Delta$), the real components of the diagonal weights, and their imaginary counterparts. It discusses the scaling laws of $\Delta$, highlights how zero real parts contribute to long memory, and introduces an approximation-estimation tradeoff influenced by the imaginary components.

### Strengths
**(I)** The analyses presented are rigorous, with clear explanations connecting the results to different initialization strategies, which is crucial for understanding SSMs.

**(II)** The paper is well-structured, with illustrative examples that help to clarify the theoretical concepts.

### Weaknesses
 **(I)** The paper primarily focuses on theoretical aspects, with limited empirical evaluation beyond basic synthetic examples. It would be beneficial to include practical applications that demonstrate the utility of the proposed methods. Specifically, the paper lacks experiments on real-world datasets or established benchmarks, making it difficult to assess the practical impact of the theoretical findings. The synthetic examples, while useful for illustrating the theory, do not adequately capture the complexities of real-world data, such as noise, non-stationarity, and high dimensionality. This limits the ability to validate the proposed initialization strategies in realistic scenarios.

**(II)** The explanation of the three theoretical components sounds a bit separated. While they all fall under the umbrella of initializations, a stronger connection would give the paper a more cohesive narrative. The paper presents the analysis of discretization size, real components, and imaginary components as distinct topics, without clearly articulating how they interact and collectively contribute to the overall performance of the state-space model. This lack of integration makes it challenging to understand the holistic impact of these components on the model's behavior. For instance, the paper could benefit from a discussion on how the choice of discretization size affects the optimal initialization of real and imaginary components, and vice-versa.

**(III)** Although the theoretical results are clearly presented, they are dense. More emphasis on distilling key messages and offering practical guidelines would enhance the paper's accessibility. The paper presents a series of theorems and proofs, which can be difficult for readers to fully grasp without a clear articulation of their practical implications. The paper would benefit from more intuitive explanations of the theoretical results, along with concrete examples of how these results can be used to guide the initialization of state-space models. For example, the paper could provide a step-by-step guide on how to select the appropriate discretization size, real components, and imaginary components for a given task.

### Questions
**(I)** The analysis focuses on the single-input single-output case. How would these results extend to the multiple-input multiple-output (S5) case? High-level insights would suffice.

**(II)** The paper assumes ZOH discretisation. How would the results differ with bilinear discretisation?

**(III)** Several questions regarding Theorem 4.1:

   (a) The upper bound applies to the expected output. Is there a corresponding probabilistic bound?

   (b) Can the upper bound be shown to be tight?

   (c) How does the real part of $w_j$ affect this bound? Specifically, how would increasing or decreasing it impact the upper bound?

   (d) The analysis focuses on the final output. How would the results change if the sum of outputs $\sum_{\ell = 1}^L y_\ell^2$  were considered instead? This pooling is adopted by many SSMs.

**(IV)** The paper explores various settings for how $\Delta$ should scale with $L$. Given a specific task, what method would you use to determine the appropriate $\Delta$?

**(V)** When the real part of $w$ is set to zero at initialization, is it still trained in practice? If so, do you enforce non-positivity? In this case, how do you handle reparameterization, especially since you can’t use the logarithm of it? Could you also show the behavior of the real part of $w$ after training? If it becomes negative, what is the benefit of zero initialization?

**(VI)** On line 376, the assumption is made that $c$ is real-valued. However, many SSM implementations use a complex $c$. What necessitates this assumption?

**(VII)** Given a specific task, how would you determine the appropriate balance between approximation and estimation tradeoff? Would this be driven by hyperparameter tuning or derived from theoretical insights?

### Soundness
3

### Presentation
3

### Contribution
3
