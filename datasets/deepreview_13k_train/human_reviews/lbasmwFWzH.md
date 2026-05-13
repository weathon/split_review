# Riemannian Low-Rank Adaptation for Federated Fine-Tuning of Foundation Models

- Decision: Reject
- Scores: 3, 5, 3, 6

## Abstract
Rank-adaptive low-rank adaptation (LoRA), a parameter-efficient fine-tuning (PEFT) technology, has achieved state-of-the-art performance in fine-tuning foundation models (FM). Directly transplanting the rank-adaptive LoRA methods from centralized learning to federated learning raises two critical issues: client drift and rank drift. This paper presents a Riemannian LoRA algorithm with adaptive rank for federated fine-tuning of foundation models (FFT-FM), RAFFT, which solves the client-drift and rank-drift issues, and significantly improves the computational cost. First, by utilizing Riemannian Procrustes analysis, we propose a Riemannian parameter matching method to avoid the client-drift issue for ensuring the effectiveness of FFT-FM with rank-adaptive LoRA, and to reduce the cost of matrix decomposition by transforming the singular value decomposition (SVD) of high-dimensional full parameter matrices into the SVD of low-dimensional $r \times r$ matrices, where $r$ is the rank parameter in the LoRA. We theoretically derive the equivalence between our RAFFT algorithm with rank-adaptive LoRA for the FFT-FM and the standard FFT-FM on the full parameter matrices based on FedAvg and verify the bounded error introduced by approximation and numerical errors. Second, by leveraging Riemannian manifold theory, we develop a Riemannian gradient descent (RGD) method to guarantee the local full parameter matrices on clients in the form of low-rank ones with fixed rank optimized by the server in each FFT-FM round, for alleviating the rank-drift issue to speed up the convergence of RAFFT. We theoretically demonstrate that the RGD optimization on the Riemannian manifold ensures the rank invariance during the local update process and the RGD optimization can converge in the FFT-FM context.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposed Riemannian aggregation and update based on SVD parameterization of LoRA to address the client drift and rank drift issues of LoRA fine-tuning in federated learning.

### Strengths
I appreciate the extensive experiments on comparing the proposed methods to 13 baselines, and 30+ tables. The baselines include prompt tuning methods and LoRA methods. The Remannian aggregation and updates have certain theorems to show that they can work as intended.

### Weaknesses
However, I also find it a bit hard to interpret the results on why the proposed RAFFT methods are better, and the difference of the metrics (accuracy, loss and time). I hope the following comments can help improve the draft, and I am happy to discuss during the rebuttal period.

I kindly ask the authors to clarify “the client-drift issue” for LoRA. Feel free to use the definition in Sun et al. 2024a and Wang et al. 2024, but I would make my decision based on a self-contained explanation. Eq (1) is a fact, but it is not clear to me if it is an issue. In the [open review](https://openreview.net/forum?id=NLPzL6HWNl) of Sun et al. ICLR’24, reviewers also raised concerns about “The explanations and the analysis of LoRA are not convincing. The discussion … heavily focus on the nonlinear nature of LoRA, but deep neural networks suffer from more severe nonlinearity.”. In [Cho et al. 2024](https://arxiv.org/abs/2401.06432), the authors observed that reconstruction \Delta W before aggregation achieves worse performance in their experiments.  

Similarly, could the authors provide a self-contained definition of “rank-drift issue”?

The presentation of the paper can be improved. Specifically
- In section 3, the content seems to be a mix of derivation and algorithms. It is unclear what exactly needs to be done on both clients and the server. 
- It is unclear to me what the advantage of Riemann aggregation in section 3 is compared to aggregating the reconstructed \Delta W from every client. 
-  It is unclear how LoRA (SVD) parameters are determined. It is unclear whether adaptive ranks (what kind of adaptive?), or fixed rank are used. 
- How are the projected gradients in section 4 computed? Could the authors clarify the advantages compared to Zhang et al. 2023, conventional LoRA, and full model fine-tuning? This may be related to the definition of rank-drift issue, but I am not sure. 

Minor issue: 
Some references are duplicated, e.g.,
Qingru Zhang, Minshuo Chen, Alexander Bukharin, Pengcheng He, Yu Cheng, Weizhu Chen, and Tuo Zhao. Adaptive budget allocation for parameter-efficient fine-tuning. ICLR’23
Youbang Sun, Zitao Li, Yaliang Li, and Bolin Ding. Improving lora in privacy-preserving federated
Learning. ICLR’24

### Questions
I kindly ask the authors to clarify “the client-drift issue” for LoRA. Feel free to use the definition in Sun et al. 2024a and Wang et al. 2024, but I would make my decision based on a self-contained explanation. Eq (1) is a fact, but it is not clear to me if it is an issue. In the [open review](https://openreview.net/forum?id=NLPzL6HWNl) of Sun et al. ICLR’24, reviewers also raised concerns about “The explanations and the analysis of LoRA are not convincing. The discussion … heavily focus on the nonlinear nature of LoRA, but deep neural networks suffer from more severe nonlinearity.”. In [Cho et al. 2024](https://arxiv.org/abs/2401.06432), the authors observed that reconstruction \Delta W before aggregation achieves worse performance in their experiments.  

Similarly, could the authors provide a self-contained definition of “rank-drift issue”?

The presentation of the paper can be improved. Specifically
- In section 3, the content seems to be a mix of derivation and algorithms. It is unclear what exactly needs to be done on both clients and the server. 
- It is unclear to me what the advantage of Riemann aggregation in section 3 is compared to aggregating the reconstructed \Delta W from every client. 
-  It is unclear how LoRA (SVD) parameters are determined. It is unclear whether adaptive ranks (what kind of adaptive?), or fixed rank are used. 
- How are the projected gradients in section 4 computed? Could the authors clarify the advantages compared to Zhang et al. 2023, conventional LoRA, and full model fine-tuning? This may be related to the definition of rank-drift issue, but I am not sure. 

Minor issue: 
Some references are duplicated, e.g.,
Qingru Zhang, Minshuo Chen, Alexander Bukharin, Pengcheng He, Yu Cheng, Weizhu Chen, and Tuo Zhao. Adaptive budget allocation for parameter-efficient fine-tuning. ICLR’23
Youbang Sun, Zitao Li, Yaliang Li, and Bolin Ding. Improving lora in privacy-preserving federated
Learning. ICLR’24

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a Riemannian low-rank adaptation (LoRA) method with adaptive rank, tailored to federated fine-tuning of foundation models. The key ida is to utilize Riemannian Procustes analysis and Riemannian manifold theory to tackle the client drift issue and the rank drift issue, respectively. The authors demonstrate that the Riemannian gradient descent optimization on the Riemannian manifold ensures convergence. Experimental results on 3 different benchmark datasets show the advantage of the proposed algorithm.

### Strengths
1. The motivation of the paper is clear, and is well written.

2. Federated fine-tuning of foundation models using LoRA is an important topic.

3. The algorithm is developed with some theoretical insights, including Riemannian Procrustes analysis and Riemannian manifold theory. The paper also provides convergence analysis of the proposed RGD algorithm.

### Weaknesses
1. Many of the presentations of the paper are similar with the ones in the (Sun et al., 2024) paper. As an example, equation 1 in the authors's paper is also presented in equation 3 of (Sun et al., 2024). It is not clear which part is new to this work. I feel that the authors need to add more details regarding the difference with the previous work.

(Sun et al., 2024) "IMPROVING LORA IN PRIVACY-PRESERVING FEDERATED LEARNING", ICLR 2024.

2. Also, Reiemannian LoRA has been studied in a centralized setting in the following paper:

Riemannian Preconditioned LoRA for Fine-Tuning Foundation Models, ICML 2024.

The authors should also cite this paper, and describe the technical contributions compared to this work. For example, how is the authors' work different from combining the above two papers? What are the new challenges and technical contributions compared with the combination of these works?

### Questions
Please refer to the weakness above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper introduces RAFFT, a Riemannian LoRA algorithm with adaptive rank for federated fine-tuning of foundation models (FFT-FM). RAFFT effectively addresses the client-drift and rank-drift issues while significantly improving computational efficiency. To resolve the client-drift issue, the authors propose a Riemannian parameter matching method based on Riemannian Procrustes analysis to align local parameter matrices. To mitigate the rank-drift issue, they extend stochastic gradient descent (SGD) algorithms onto a Riemannian manifold.

### Strengths
1. The problem addressed is significant and appealing, focusing on a crucial aspect of LLM federated learning.
2. The paper applies a novel math technique to address the client-drift and rank-drift issues.

### Weaknesses
1. The writing quality is poor, with too many long sentences that are difficult to follow. Additionally, the paper includes many unexplained abbreviations, such as FedAvg, RAFFT, and RGD, which appear in the introduction without clarification.
2. The authors need to provide clear definitions of the client-drift and rank-drift issues. Referring readers to external works, as done with "Please refer to Sun et al. (2024a); Wang et al. (2024) for the definition of the specific client-drift issue in the FFT-FM," is inadequate. Readers need direct definitions within the paper to understand the problems being addressed.
3. The main text requires rigorous definitions of notations, as it is difficult to follow the proofs of the main results without them.
4. The paper lacks necessary lemmas that would aid in understanding the proof sketches.

### Questions
See weakness.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents RAFFT, a Riemannian LoRA algorithm with adaptive rank for federated fine-tuning of foundation models. The proposed method addresses the challenges of client drift and rank drift in federated LoRA by employing a Riemannian parameter matching technique. A Riemannian gradient descent algorithm is derived for rank consistency during local updates and to accelerate convergence.
The theoretical analysis shows rank invariance and convergence.

### Strengths
1. The use of Riemannian geometry to solve client-drift and rank-drift issues in federated fine-tuning is novel and effective, with well-defined methods like Riemannian Procrustes analysis and Riemannian gradient descent.
2. The paper provides rigorous proofs, including error bounds and convergence guarantees, which support the robustness of the RAFFT algorithm.

### Weaknesses
1. The efficiency of Riemannian operations is not fully quantified. A clearer breakdown of resource usage would help in assessing practical overhead.
2. Key parameters, like rank thresholds and learning rates, are not thoroughly analyzed. This could affect the method’s adaptability to various tasks and models.

### Questions
1. What are the specific computational trade-offs of Riemannian operations compared to simpler alternatives like FedAvg?
2. How does the proposed method perform under extreme non-IID data environments? Are there additional experiments or theoretical analyses that could demonstrate the stability and effectiveness of the RAFFT method across diverse data distribution scenarios?

### Soundness
3

### Presentation
3

### Contribution
3
