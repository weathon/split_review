# On the Optimization and Generalization of Two-layer Transformers with Sign Gradient Descent

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
The Adam optimizer is widely used for transformer optimization in practice, which makes understanding the underlying optimization mechanisms an important problem.
    However, due to the Adam's complexity, theoretical analysis of how it optimizes transformers remains a challenging task. 
    Fortunately, Sign Gradient Descent (SignGD) serves as an effective surrogate for Adam.
    Despite its simplicity, theoretical understanding of how SignGD optimizes transformers still lags behind.
    In this work, we study how SignGD optimizes a two-layer transformer -- consisting of a softmax attention layer with trainable query-key parameterization followed by a linear layer -- on 
    a linearly separable noisy dataset.
    We identify four stages in the training dynamics, each exhibiting intriguing behaviors.
    Based on the training dynamics, we prove the fast convergence but poor generalization of the learned transformer on the noisy dataset.
    We also show that Adam behaves similarly to SignGD in terms of both optimization and generalization in this setting.
    Additionally, we find that the poor generalization of SignGD is not solely due to data noise,
    suggesting that both SignGD and Adam requires high-quality data for real-world tasks.
    Finally, experiments on synthetic and real-world datasets empirically support our theoretical results.

    \iffalse
    {\bf [Deprecated]} The Adam optimizer has achieved great success in transformer optimization, but gradient descent performs poorly in this setting.
    However, our theoretical understanding of how Adam optimizes and generalizes in transformers is limited. 
    In this work, we give an end-to-end theory of learning two-layer transformers by sign gradient descent, which recent works suggests is a good surrogate of Adam. 
    We provide a theoretical characterization of the whole optimization dynamics, from random initialization to final convergence, and identify four stages exhibiting unique behaviors, primarily caused by attention mechanisms and softmax nonlinearity.
    We demonstrate the exponential convergence of training loss with respect to a given precision,
    and show that the trained transformer given by sign gradient descent have at least constant generalization error. 
    \jianfei{rephrase to make the main message (it trains fast but generalizes poorly) more clear. currently it is not immediately clear}
    \bingrui{This also a current problem, will we stress this point out or modify the statement? The main reason is fast training doesnt lead to poor generalization. Generalization is partly due to the low signal-to-ratio data. Also see section 4.2.}
    This fast convergence, but harmful generalization result, which we refer to as \textit{destructive convergence}, provides an intriguing counterexample to the common wisdom that faster training leads to better generalization. \jianfei{is there really such common wisdom?}
    We verify our theoretical results by experimental simulation.
    \bingrui{No, this common wisdom is wrong, as mentiond in Section 4.2.}
    \zhanpeng{Seemingly, you first say Adam is good in practice. But in your analysis, you find a critical issue about Adam. Your theoretical findings contrasts with our common understanding. Do you have any experiments to show that such issue indeed occurs in real-world scenario?}
    \bingrui{This is a good question, here are two points. 1. do we mention Adam in this paper with a mass of text? Currently, I think the discussion about Adam should be concise. Instead, we mainly focus on signGD.
    2. The real-world data experiments. AC also mentioned this point. do you think a simple model (eg one layer VIT) on noisy MNIST is enough? For example, see the data in the Appendix F. in~\citet{CCBG22}. Well, if that experiment works for signGD, I think it can also work for Adam.
    }\fi

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper studies the learning dynamics of two-layer transformers optimized with SignGD. It introduces a theoretical framework that categorizes the learning process into four distinct stages, providing an analytical tool to study these dynamics. The study demonstrates that while SignGD achieves fast convergence of the transformer model, it leads to poor generalization on noisy datasets.

### Strengths
1. The paper offers a comprehensive four-stage analysis of transformer training dynamics, which is a promising contribution to understanding the behavior of transformers. 

2. The demonstration of fast convergence but poor generalization with SignGD on noisy data is important. These findings are beneficial for practical applications as they guide the selection of optimizers and the preparation of datasets in real-world tasks.

3. The theoretical approach is novel.

### Weaknesses
1) The paper claims that both SignGD and Adam require high-quality data to perform well. However, an apparent contradiction arises in Figure 2(d), where the model with less noisy data (SNR=1.0) performs worse than that with noisier data (SNR=0.5). This discrepancy challenges the theoretical claims and needs to be addressed or explained to validate the model’s consistency across different noise levels. This is particularly concerning because the expectation is that with a higher signal-to-noise ratio, the model should generalize better, not worse. The fact that the test loss increases with cleaner data suggests a potential flaw in the experimental setup or an unaddressed factor influencing the results, which undermines the paper's conclusions about the impact of noise on SignGD. It is crucial to understand whether this behavior is due to overfitting on the cleaner dataset, or if there is a more fundamental issue with the optimization process under these conditions.

2)  The description of the training dynamics in Section 3.1 lacks clarity, making it difficult to follow through the stages. It would be beneficial to explicitly map the training steps of the analysis to each stage in the diagrams (e.g., steps 1-2 corresponding to Stage 1). Additionally, providing data plots before and after switching steps of different stages, such as providing the mean noise values before and after the transition steps for 1st stage and 2nd stage in Fig 1(a), would greatly enhance understanding. The current presentation focuses mainly on the dynamics within each stage, but the transitions between stages, which are critical for understanding the overall learning process, are not well-illustrated. For example, showing the change in key noise and query noise at the transition from Stage I to Stage II would provide a clearer picture of how the model's internal representations evolve.

3) In many real-world applications of Adam in transformer, such as those used in vision and language tasks, often exhibit robustness to noise in practical applications, which is contrary to the findings presented. Understanding whether this discrepancy is due to lower real-world noise levels or other factors that contradict the assumptions made in the study is essential for aligning theoretical insights with empirical observations. The paper does not adequately address the gap between the simplified noise model used in the analysis and the complex, often structured, noise present in real-world datasets. This raises concerns about the applicability of the theoretical findings to practical scenarios, especially given the widespread use of Adam in noisy real-world settings. It is important to investigate whether the i.i.d. Gaussian noise assumption is a limiting factor in the analysis and how the results might change with more realistic noise models.

### Questions
1. In Figure 2(d), the test loss for the less noisy case (SNR=1.0) is higher than for the noisier case (SNR=0.5) when using SignGD, which contradicts theoretical expectations about the benefits of higher-quality data. Could you provide an analysis of the noise characteristics or data distribution across different SNR levels that might explain this behavior? Additional experiments or analyses could also be valuable in investigating this phenomenon further. For instance, it’s possible that entirely clean data may reduce generalization performance compared to slightly noisy data, though too much noise also significantly hinders generalization.

2. Clarity and Detail in Training Dynamics Analysis (Section 3.1): Could you offer a clearer mapping between training steps and each stage of the training dynamics? More detailed explanations of the transitions between each of the four stages would be helpful. Additionally, including data plots that capture the state of relevant variables before and after critical transition points would improve clarity (rather than focusing solely on within-stage details, like in Figure 1(a)).

3. Real-world applications of Transformers, such as language modeling, demonstrate robustness to noise. How do the noise levels assumed in your theoretical model compare to those typically encountered in practical Transformer applications? Could you discuss any factors or experiments that might explain the gap between your theoretical findings and the observed robustness of Transformers to noise in real-world scenarios?

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
3

### Summary
The paper investigates the optimization and generalization properties of Sign Gradient Descent (SignGD) for transformers, focusing on binary classification tasks involving noisy, linearly separable data. The authors claim that SignGD is an effective surrogate for the Adam optimizer. They identify four stages in the training dynamics of SignGD and observe that it achieves fast convergence in training loss but generalizes poorly, especially on noisy data.

### Strengths
The paper provides a multi-stage framework to analyze the transformer training using SignGD, making this complex behaviour into small interpretable stages.

By establishing that SignGD is a proxy for Adam, the paper is capable of offering new perspectives on the reasons why Adam present some generalization problems.

The combination of theoretical proofs and experimental validation strengthens the proposed analysis and its overall message.

### Weaknesses
The main weakness of the method is its limited applicability to real-world scenarios. The reliance on assumptions such as linearly separable data and the use of only two-layer transformers restricts its effectiveness when dealing with more complex datasets and modern, state-of-the-art transformer architectures. Specifically, the analysis is confined to a simplified two-layer transformer model, which lacks the depth and complexity of contemporary architectures that often employ dozens of layers and intricate attention mechanisms. This simplification makes it difficult to extrapolate the findings to practical applications, where transformers are typically much deeper and incorporate multi-head attention, layer normalization, and residual connections. Furthermore, the assumption of linearly separable data, while useful for theoretical analysis, is rarely met in real-world datasets, which often exhibit complex, non-linear decision boundaries. This discrepancy limits the practical relevance of the theoretical results, as the observed training dynamics may not generalize to more realistic scenarios.

### Questions
Can the framework be extended to deeper transformers or multi-head attention mechanisms? I ask that because no method is currently using two layers transformer, so its extension to SOTA networks could provide broader applicability. 

From the current work what strategies could the authors envision can be used to improve generalization of SignGD and consequently Adam in data noisy settings? Identifying such strategies would be valuable for increasing robustness in real-world applications, where noise is often unavoidable.

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
4

### Summary
This manuscript provides a deep theoretical analysis of the training dynamics of a simplified two-layer transformer using signSGD on a synthetic dataset. It explicitly identifies four complex but distinct stages in the training dynamics. Furthermore, it empirically uncovers that Adam exhibits similar behavior under the same conditions as signSGD. The analysis demonstrates that while signSGD typically converges quickly, it generalizes poorly and requires high-quality data compared to SGD.

### Strengths
To the best of my knowledge, this manuscript is the first to theoretically analyze the detailed training dynamics of the transformer and softmax attention layer with trainable query-key parameterization using signSGD. It breaks down the process into four stages, capturing the complex and subtle behaviors, which deepens our theoretical understanding of the optimization process for Transformers.

### Weaknesses
 - Some assumptions in the analysis are overly strong and unrealistic. For example, the manuscript assumes that the data dimension satisfies  $ d = \Omega(\text{poly}(n)) $, and that the variance of noise satisfies $\sigma_p = \Omega(d^{\frac{1}{4}} n^3)$, where $ n $ is the number of data samples, which is typically much larger in practice. The requirement that $d$ scales polynomially with $n$ is a significant constraint, limiting the applicability of the theoretical results to practical scenarios where data dimensionality is often fixed or much smaller than the number of samples. Similarly, the noise variance assumption seems excessively large, potentially overshadowing the signal and making the analysis less relevant to real-world data with lower noise levels. These assumptions need further justification or exploration of their impact on the derived conclusions.

- Although the manuscript attempts to analyze the complex softmax attention with trainable query-key parameterization, it simplifies the attention block to a single-head variant rather than using the original multi-head version. This simplification significantly reduces the complexity of the analysis but also limits the generalizability of the findings. The behavior of multi-head attention, with its parallel processing of different feature subspaces, might exhibit different dynamics than the single-head version. Additionally, the formulation of $ v $ is somewhat unusual, defined as $v = \bar{w} _{v,1} - \bar{w} _{v,-1}$ which undermines the theoretical insights in relation to real-world scenarios. This definition of $v$ as a difference between averaged parameters seems artificial and lacks a clear connection to how value parameters are typically used in transformer models, potentially limiting the practical relevance of the analysis.

- While the empirical results validate the theoretical analyses for training a two-layer transformer using signSGD, it would be valuable to investigate whether the empirical training dynamics of a multi-layer transformer, or even the original transformer, align with the theoretical findings from the simplified two-layer model.  I would like to see whether the results  can extend to deeper transformers, or implement more experiments to test if the key behaviors you identified persist in more complex models. The absence of experiments on deeper or more realistic transformer architectures raises concerns about the practical applicability of the theoretical findings. The dynamics observed in a two-layer model may not directly translate to the more complex behavior of deeper networks with multiple attention and feedforward layers.

**Minor Issues**  
- At Line 168, the variable $ i $ in the equation is not explicitly defined, though it can be inferred that $ i$ represents the index of data samples.

- In Figure 2, the manuscript suggests distinct differences between the training dynamics of signSGD and Adam, yet does not provide sufficient explanations. For instance, in (a) and (b), it is noted that the negative term $\langle w_{Q,s}, y_i \epsilon_{i} \rangle$ for signSGD ultimately becomes positive, while for Adam, it remains consistently negative. In (c), signSGD converges at a linear rate, whereas Adam converges at a sublinear rate. I think it needs to provide more detailed explanations for these differences, and to discuss their implications for understanding Adam's behavior in practice.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
