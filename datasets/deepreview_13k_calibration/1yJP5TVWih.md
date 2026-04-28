# Lambda-Skip Connections: the architectural component that prevents Rank Collapse

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 8, 5

## Abstract
Rank collapse, a phenomenon where embedding vectors in sequence models rapidly converge to a uniform token or equilibrium state, has recently gained attention in the deep learning literature. This phenomenon leads to reduced expressivity and potential training instabilities due to vanishing gradients. Empirical evidence suggests that architectural components like skip connections, LayerNorm, and MultiLayer Perceptrons (MLPs) play critical roles in mitigating rank collapse. While this issue is well-documented for transformers, alternative sequence models, such as State Space Models (SSMs), which have recently gained prominence, have not been thoroughly examined for similar vulnerabilities. This paper extends the theory of rank collapse from transformers to SSMs using a unifying framework that captures both architectures. We study how a parametrized version of the classic skip connection component, which we call \emph{lambda-skip connections}, provides guarantees for rank collapse prevention. Through analytical results, we present a sufficient condition to guarantee prevention of rank collapse across all the aforementioned architectures. We also study the necessity of this condition via ablation studies and analytical examples. To our knowledge, this is the first study that provides a general guarantee to prevent rank collapse, and that investigates rank collapse in the context of SSMs, offering valuable understanding for both theoreticians and practitioners. Finally, we validate our findings with experiments demonstrating the crucial role of architectural components such as skip connections and gating mechanisms in preventing rank collapse.\freefootnote{Preprint. Under Review.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Dao and Gu [https://arxiv.org/pdf/2405.21060] established a form of equivalence between transformers and continuous-time state-space models.  In a different development, Dong et al. [https://arxiv.org/abs/2103.03404] showed that self-attention layers without skip connections or MLPs suffer from "rank collapse" ― with increasing layers, the output matrix tends to rank-1, i.e., all token positions tend to the same representation.

The present submissions puts these together to show that rank collapse is a problem also for state-space models.  It shows that the skip connection provides vital protection against rank collapse, but that a weighted addition (with weight $\lambda$ which may be regarded as a hyperparameter, or perhaps trainable) with the skip connection is more flexible.

### Strengths
Reasons to accept:
* Identifies rank collapse problem in state-space models like MAMBA, similar to earlier discovery of this problem in transformer-type networks.
* Identifies skip strength parameter $\lambda$ as an important knob to limit the damage of rank collapse.

### Weaknesses
Reasons to reject:
* Given the two papers on which this paper builds, it might be argued that the present work is relatively incremental.  (That being said, I appreciate the candor while setting up the contributions of this paper, and I learnt something from it.)


*   Given the existing literature on rank collapse in transformers, the extension to state-space models, while novel, might be seen as a somewhat predictable outcome. The core mechanism of rank collapse, as demonstrated in self-attention layers, is the tendency for output representations to converge to a low-rank subspace, and it is not entirely surprising that a similar phenomenon would occur in other architectures lacking sufficient regularization or skip connections. The paper could benefit from a more detailed discussion of the specific nuances of rank collapse in state-space models compared to transformers, highlighting any unique challenges or characteristics that arise in this context.


*   The paper introduces a skip strength parameter $\lambda$ as a mechanism to mitigate rank collapse. While this is a practical approach, the paper does not provide a deep analysis of the optimal range or behavior of $\lambda$. It is unclear how sensitive the model is to the choice of $\lambda$, and whether there are specific conditions or architectures where certain values of $\lambda$ are more effective than others. A more thorough exploration of the parameter space and its implications would strengthen the paper's contribution.


*   The paper does not sufficiently address the practical implications of rank collapse in state-space models. While the theoretical analysis is valuable, it would be beneficial to see more concrete examples of how rank collapse affects the performance of these models in real-world tasks. For example, are there specific tasks or datasets where rank collapse is more pronounced, and how does the proposed $\lambda$-tuning method mitigate these issues in practice? The paper could also benefit from a discussion of the computational overhead associated with the proposed method, and whether it introduces any new challenges in terms of training or inference.


A few writing style and notation nits:

L156-L159 set up $X^{(k)}$ as layer input and $Y^{(k)}$ as layer output.  However, equation (1) introduces $O^{(k)}$ without explaining it will provide skipping ability in equation (2).

L174-L178 There seem to be some inconsistent subscripts and superscripts. On one side we see $A^{(k)}_t, B^{(k)}_t$ etc. But just after the displayed equation, for LTI systems we see the superscript $(k)$ disappear, without an explanation if this is because the LTI system is assumed to have one layer.

L888-L903 While setting up expressions and bounds with so many variables, it helps to afterward highlight the most import 1-2 variables, and give qualitative connections between their typical values in practice and the implications on the bounds.  E.g., how easy or difficult would be to choose an acceptable $\lambda$ in a typical LLM?  Also, some of the definitions like $S$ are very far from the proofs in the appendix.

### Questions
I have a reasonable estimate of creativity and technical depth, but it is difficult for me to assess impact.  I am not familiar with the area and my assessment has limited confidence. I would not, for example, know if rank collapse is widely appreciated within even the transformer "community" (if there is any such thing).  I have not seen MAMBA become that visible or widely used compared to standard transformer-based LLMs, but cannot speculate if rank collapse played a role.  $\lambda$-tuning for robustness seems quite useful, but again I do not know the area well enough to know if, in practice, $\lambda=1$ is frequently dangerous.  If the authors point to specific places in the paper where the above issues are discussed, or add some more motivating support, that would be helpful.

A few writing style and notation nits:

L156-L159 set up $X^{(k)}$ as layer input and $Y^{(k)}$ as layer output.  However, equation (1) introduces $O^{(k)}$ without explaining it will provide skipping ability in equation (2).

L174-L178 There seem to be some inconsistent subscripts and superscripts. On one side we see $A^{(k)}_t, B^{(k)}_t$ etc. But just after the displayed equation, for LTI systems we see the superscript $(k)$ disappear, without an explanation if this is because the LTI system is assumed to have one layer.

L888-L903 While setting up expressions and bounds with so many variables, it helps to afterward highlight the most import 1-2 variables, and give qualitative connections between their typical values in practice and the implications on the bounds.  E.g., how easy or difficult would be to choose an acceptable $\lambda$ in a typical LLM?  Also, some of the definitions like $S$ are very far from the proofs in the appendix.

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
This paper analyzes the rank collapse of SSM due to identical $\lambda$ skip connections. The authors provide a rigorous convergence rate for the rank collapse and offer sufficient guarantees to prevent it. Experimental results demonstrate the effectiveness of their analysis.

### Strengths
1. The lower boundary of the rank collapse of $\lambda$ skip connections is analytically derived. The results agree well with empirical analysis.
2. The paper presents the convergence rate in the absence of skip connections, contributing valuable insights.

### Weaknesses
1. The authors analyze the $\lambda$ skip connections. However, the skip strength $\lambda_k$ may vary on different layers.The paper should discuss how the findings hold up under these varying conditions. Additionally, many models implement skip connections selectively across layers rather than uniformly. A discussion on the generalizability of the results would enhance the paper.
2. Theorem 4.1 paves the way to choose suitable $\lambda$. However, in Figure 2, it appears that when $\lambda$ is sufficiently large, the rank collapse index shows little variation. Clarification on how to determine the optimal value of $\lambda$ would be beneficial.
3. Based on theorem 4.1, could the authors explore adding constraints to the parameters to optimize $C_M$, $S$ and $c$ for improved neural network performance?

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper examines the phenomenon of rank collapse in general sequence model architectures, including transformers and state space models. To mitigate this issue, the paper proposes a parameterized version of the skip connection that multiplies the residual stream by a constant factor. Theoretical analysis identifies the conditions on the parameter sufficient to prevent rank collapse, and an analytical example demonstrates that neither the absence of skip connections nor the standard implementation prevents rank collapse. Finally, empirical evaluations support the findings of theoretical analysis.

### Strengths
This paper addresses the significant issue of rank collapse in sequence model architectures. It offers both theoretical analysis and empirical evaluation to support the proposed architectural component aimed at resolving this problem. I like the remark that provides the parameters corresponding to the practical architectural settings.

Additionally, the theoretical development and overall presentation of the paper are commendably clear and well-structured.

### Weaknesses
The theory investigates the sufficient conditions for preventing rank collapse in the worst-case scenario. This could imply that the required conditions are overly stringent. The analysis focuses on a lower bound for the rank collapse metric, which may not be tight for typical input sequences. This raises concerns about the practical applicability of the derived conditions, as they might be more restrictive than necessary in common scenarios. Furthermore, the rank collapse metric is not normalized in the definition. It is unclear if lower bounding the unnormalized metric is sufficient, especially when the norm itself evolves across layers. This could potentially lead to misleading conclusions about the actual severity of rank collapse in different layers, as changes in the norm might overshadow changes in the rank itself.

### Questions
The rank collapse metric is not normalized in the definition. Would it be enough to lower bound the rank collapse metric, when the norm itself evolves across layers?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses rank collapse, a phenomenon where embedding vectors in deep learning models converge to a uniform state. Building on previous studies that focused on transformers, this paper extends the analysis to State Space Models (SSMs). The study employs theoretical and empirical analysis to demonstrate how lambda-skip connections, LayerNorm, and gating mechanisms contribute to both the stability and expressivity of transformers and SSMs.

### Strengths
S1. The paper tackles the problem of rank collapse, extending its analysis from transformers to SSMs.
S2. Through theoretical proofs, the paper demonstrates that lambda-skip connections prevent rank collapse, preserving model expressivity in both transformers and SSMs.
S3. Experimental results show that lambda-skip connections and other components enhance expressivity and stability across different model architectures.

### Weaknesses
W1. The definition of the residual term between Eq.(3) and Eq.(6) is inconsistent, with ambiguity around whether X or V serves as the residual term. This inconsistency impacts the theoretical derivations that follow and should be clarified to ensure precise interpretations. Additionally, certain symbols, such as D, are used in both the SSM and LayerNorm contexts but represent different meanings. Distinct notation would improve readability and reduce potential confusion.

W2. While the experiments generally align with the theoretical predictions, some disparities remain unaddressed. For example, the theoretical threshold for λ appears more conservative than the empirical results suggest, and additional clarification would help. Further, the appendix notes rank stability even without skip connections, which might challenge the presented theory.

W3. The paper primarily focuses on rank collapse within the model’s architecture but does not connect this phenomenon to downstream task performance. Adding experimental results that measure downstream task performance in relation to model depth and skip connection strength could provide a more comprehensive assessment.

### Questions
Q1. Between Eq. (3) and Eq. (6), there is ambiguity regarding the residual term, specifically whether X or V serves as the residual component. This inconsistency could impact the theoretical derivations that follow. Could the authors clarify this definition? Additionally, using the same symbol D for both SSM and LayerNorm contexts creates potential confusion. Distinct notations would enhance clarity.
Q2. The theoretical conditions for λ appear to be conservative compared to empirical findings. Could the authors explain this discrepancy? Furthermore, the appendix notes cases of rank stability without skip connections, which might challenge the theory. An analysis of these cases would be valuable.
Q3. Could the authors provide additional experiments showing the model’s downstream performance as a function of layer depth and skip strength? Also, would the inclusion of alternative metrics, such as effective rank, offer a more comprehensive assessment of rank collapse?

### Soundness
3

### Presentation
3

### Contribution
2
