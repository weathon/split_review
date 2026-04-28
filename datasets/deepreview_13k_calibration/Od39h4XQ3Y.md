# Efficient Sharpness-Aware Minimization for Molecular Graph Transformer Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Sharpness-aware minimization (SAM) has received increasing attention in computer vision since it can effectively eliminate the sharp local minima from the training trajectory and mitigate generalization degradation. However, SAM requires two sequential gradient computations during the optimization of each step: one to obtain the perturbation gradient and the other to obtain the updating gradient. Compared with the base optimizer (e.g., Adam), SAM doubles the time overhead due to the additional perturbation gradient. By dissecting the theory of SAM and observing the training gradient of the molecular graph transformer, we propose a new algorithm named GraphSAM,  which reduces the training cost of SAM and improves the generalization performance of graph transformer models. There are two key factors that contribute to this result: (i) \textit{gradient approximation}: we use the updating gradient of the previous step to approximate the perturbation gradient at the intermediate steps smoothly (\textbf{increases efficiency}); (ii) \textit{loss landscape approximation}: we theoretically prove that the loss landscape of GraphSAM is limited to a small range centered on the expected loss of SAM (\textbf{guarantees generalization performance}). The extensive experiments on six datasets with different tasks demonstrate the superiority of GraphSAM, especially in optimizing the model update process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study Sharpness Aware Minimization (SAM), an effective training objective in the image domain to avoid "sharp minima", in the context of graph transformers for molecular data. The proposed efficient SAM-alternative, termed GraphSAM, empirically performs on par with SAM while being more efficient.

### Strengths
1. More efficient approach for SAM (roughly 30%-50% faster training)
1. GraphSAM consistently improves the performance of the base model
1. Approach is ablated and rich explanations are provided
1. The paper is well organized and it is easy to follow.

### Weaknesses
1. The relation to graph machine learning is a bit obscure: is GraphSAM only a good approximation for graph transformers? After all, GraphSAM does not rely on anything graph-related besides the observations made with SAN + graph transformers. Although it is fine to focus on molecular data, the paper would benefit significantly from a holistic discussion (and some rudimentary experiments) demonstrating its applicability, or lack thereof, to other graph-based models and tasks beyond molecular property prediction. The current scope is too narrow to fully assess the generalizability of the proposed method.

2. The theoretical statements could be better motivated and more decisively embedded into the story. It remains a bit vague what the actual implications are. For example, the conclusion of Theorem 1 is speculative "by replacing the inner maximum of LG(θ + εˆS) with the maximum of LG(θ + εˆG), we tend to smooth the worse neighborhood loss in the loss landscape. In other words, if one could minimize the upper bound given by LG(θ + εˆG), the final loss landscape is as smooth as that obtained from SAM." Alternatively, the wording may be improved. It is not clear why optimizing the upper bound necessarily results in a "loss landscape is as smooth as that obtained from SAM". The connection between minimizing the upper bound and achieving a smoother loss landscape needs more rigorous justification.

3. Proof of Theorem 1 relies on empirical observations and (from my perspective) strong assumptions. However, the authors do sufficiently not discuss this in the main part and, thus, the current presentation is misleading. In other words, these assumptions, etc. should be made explicit in a rather prominent way in the main part (e.g. "and after ||ω0 ||2 experimental analysis, the updating gradient ω ≫ ε " is not stated clearly in main part). I think it would be better to drop the term "Theorem" and rather give some intuitive, mathematically motivated explanation.

Minor:
1. Missing space in the first line of page 2
2. The bold highlighting in Table 1 is counter-intuitive. Perhaps add an additional marker to highlight the best model per task.

### Questions
1. Is GraphSAM only a good approximation for graph transformers? How is GraphSAM working, e.g., in the image domain?
1. Are there any observations of how the behavior of the graph transformer changes if trained with GraphSAM? For example, do the attention scores then align better with the graph connectivity, or do they become smoother (higher entropy)?
1. Is it possible to compare GraphSAM with other efficient SAM derivates besides SAM-k (e.g., see related work section)?
1. Is The proportionality in Theorem 2 not merely caused by the first-order Taylor approximation (Eq 6 in A1.1)? How do the authors know that the linear term is a sufficient approximation?

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
The study introduces Sharpness-aware minimization (SAM) in computer vision, a technique effective in eliminating sharp local minima in training trajectories and countering generalization degradation. However, its dual gradient computations during optimization increases time costs. To address this, a novel algorithm named GraphSAM is proposed. It lowers the training expenses of SAM while enhancing the generalization performance of graph transformer models. The approach is underpinned by two main strategies: gradient approximation and loss landscape approximation. Empirical tests across six datasets validate GraphSAM's superiority, particularly in refining the model update process. Anonymized code is also provided for further reference.

### Strengths
(1) The paper is exceptionally coherent in its writing. The content is presented seamlessly, and the expression is clear.

(2) This paper is both conceptually and technically innovative. It uniquely reutilizes the updating gradient from the previous step, approximating the perturbation gradient in an efficient manner.

(3) The experimental design of this study is well-conceived. It systematically validates the representational capabilities of GraphSAM. Additionally, the appendix offers an extensive set of supplementary experiments.

### Weaknesses
 (1) In Observation 1, the author notes the differing changes of the perturbation gradient and the updating gradient throughout the training process. I wonder, is this a general phenomenon? Could more case studies be provided to illustrate this further?

(2) The results presented in Table 1 seem to show limited improvement on certain datasets. I suggest the author consider incorporating an efficiency aspect into the table. Efficiency is a crucial contribution, yet it hasn't been emphasized adequately in the experimental section, which seems inconsistent.

### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes GraphSAM to reduce the training cost of sharpness-aware minimization (SAM) and improve the generalization performance of graph transformer models. GraphSAM uses the updating gradient of the previous step to approximate the perturbation gradient at the intermediate steps smoothly and theoretically proves that the loss landscape of GraphSAM is limited to a small range centered on the expected loss of SAM. Extensive experiments on six datasets with different tasks demonstrate the effectiveness and efficiency of GraphSAM.

### Strengths
- **Motivation is clear**: SAM is a powerful optimizer but doubles the computational cost compared with the base optimizer. Thus, **improving its efficiency** (the focus of this paper) is an important problem
- GraphSAM improves the efficiency of SAM by **approximating the perturbation gradient** $\epsilon_{t+1}$ as the moving average of $\epsilon_t$ and $\omega_{t}$ based on two observations: (i) $\epsilon_t$ is close to $\epsilon_{t+1}$ (Figure 3(a)) and (ii) $\epsilon_{t+1}$ is close to $\omega_t$ (Figure 3(c))
- By approximating the perturbation gradient, GraphSAM almost **does not need to compute the perturbation gradient** (only once per epoch). Thus, GraphSAM is efficient
- Experimental results on the graph dataset show that GraphSAM is comparable with SAM (Tables 1 and 2) and is more efficient (Table 2)

### Weaknesses
 - **writing**:
  - The colors in Figure 1 are inconsistent with the observations: "compared to the base optimizer of Adam (the blue bar)", but the blue is LookSAM? also, SAM (cyan)?
  - Figure 1, it is better to include the proposed GraphSAM as well
  - Related works: "most of the work still ignores the fact of SAM’s double overhead (Damian et al., 2021; Kwon et al., 2021;Wang et al., 2022)." I think some methods have attempted to mitigate this issue, e.g., AE-SAM, SS-SAM, better to discuss them here
  - Section 3, "SAM consumes double overhead due to the extra computation of perturbation gradient compared with the base optimizer." existing methods (AE-SAM, SS-SAM) have tried to mitigate this issue, better to discuss them here, and why they cannot be used for graph datasets, this is also the motivation for the proposed GraphSAM
  - Figure 3, sub-caption for each subfigure
  - Table 1: also compare with GROVER+AE-SAM/SS-SAM
  - "AE-SAM and RST periodically compute the update gradient by different strategies": AE-SAM is an adaptive strategy, not a periodic strategy
- it seems that the proposed GraphSAM is general, not limited to graph transformers, and can also be used in computer vision. Thus, it is better to conduct some experiments on computer vision.
- ablation study for hyperparameters $\gamma, \lambda, \beta$
- Theorem 2, based on the proof, the proportion ratio depends on the $\theta$ (Eq(7)), it is trivial. if we assume the loss is Lipschitz, then the constant can be independent of $\theta$.

### Questions
see the questions in weakness.

======

I have read the rebuttal and other reviews. Most of my concerns are resolved, so I maintain my score of 6.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper designs a computation efficient variant of sharpness aware minimization (SAM) for molecular graph transformers.

### Strengths
S1. This paper observes that flat minima generalize better for molecular graph transformers. This extends the boundary of sharpness awareness to a new domain.

S2. To overcome the computational burden, this paper leverages domain specific knowledge to design GraphSAM. Supporting theories are derived to explain the reasons behind design.

S3. GraphSAM improves throughput with comparable performance with SAM. Compared to other variants of computation efficient SAM, GraphSAM performs better in the considered setting.

### Weaknesses
W1. Can the authors elaborate more on equation (3)? In particular, are there any specific reasons for choosing $\epsilon_t$ as the moving average of $w_t/\|w_t \|$? What will happen if $\epsilon_t$ becomes moving average of $w_t$?

W2. What are the specific reasons behind the choice of StepLR for the $\rho$-schedulers? Does other approaches, such as cosine schedulers or inverse square root schedulers help?

Q1. Table 1 does not fit into the paper properly.

Q2. Some of the expressions are unnecessarily complicated. For example, in equation (2) and (3), $sign(\epsilon_t)|\epsilon_t|$ can be replaced by $\epsilon_t$.

Q3. Missing references on SAM variants. 

[1] Du, Jiawei, Daquan Zhou, Jiashi Feng, Vincent YF Tan, and Joey Tianyi Zhou. "Sharpness-Aware Training for Free." arXiv preprint arXiv:2205.14083 (2022).

[2] Li, Bingcong, and Georgios B. Giannakis. "Enhancing Sharpness-Aware Optimization Through Variance Suppression." arXiv preprint arXiv:2309.15639 (2023).

### Questions
Q1. Table 1 does not fit into the paper properly.

Q2. Some of the expressions are unnecessarily complicated. For example, in equation (2) and (3), $sign(\epsilon_t)|\epsilon_t|$ can be replaced by $\epsilon_t$.

Q3. Missing references on SAM variants. 

[1] Du, Jiawei, Daquan Zhou, Jiashi Feng, Vincent YF Tan, and Joey Tianyi Zhou. "Sharpness-Aware Training for Free." arXiv preprint arXiv:2205.14083 (2022).

[2] Li, Bingcong, and Georgios B. Giannakis. "Enhancing Sharpness-Aware Optimization Through Variance Suppression." arXiv preprint arXiv:2309.15639 (2023).

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
