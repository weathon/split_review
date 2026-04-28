# Enabling Fine-Tuning of Direct Feedback Alignment via Feedback-Weight Matching

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
In this paper, we introduce feedback-weight matching, a new method that facilitates reliable fine-tuning of fully connected neural networks using Direct Feedback Alignment (DFA). Although DFA has demonstrated potential by enabling efficient and parallel updates of weight parameters through direct propagation of the network's output error, its usage has been primarily restricted to training networks from scratch. We provide the first analysis showing that existing standard DFA struggles to fine-tune networks pre-trained via back-propagation. Through an analysis of weight alignment (WA) and gradient alignment (GA), we show that the proposed feedback-weight matching enhances DFA's ability and stability in fine-tuning pre-trained networks, providing insights into DFA's behavior and characteristics when applied to fine-tuning. In addition, we find that feedback-weight matching, when combined with weight decay, not only mitigates over-fitting but also further reduces the network output error, leading to improved learning performance during DFA-based fine-tuning. Our experimental results show that, for the first time, feedback-weight matching enables reliable and superior fine-tuning across various fine-tuning tasks compared to existing standard DFA, e.g., achieving 7.97\% accuracy improvement on image classification tasks (i.e., 82.67\% vs. 74.70\%) and 0.66 higher correlation score on NLP tasks (i.e., 0.76 vs. 0.10). The code implementation is available at an anonymous GitHub repository.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this work, the authors analyzed the direct feedback alignment (DFA) for fine-tuning network pertained via backpropagation and identified its limitations compared. Accordingly, the feedback-weight matching is proposed to enhance the ability and stability of DFA in fine-tuning and combined it with weight decay to further reduce the network output error. Experiments are conducted on various datasets.

### Strengths
1. *Originality*: It is novel to recognize and scrutinize that the strong weight alignment condition for DFA in the case of fine-tuning is unlikely to satisfy. In order to address this issue, the feedback-weight matching and weight decay for it are originally proposed to enhance the fine-tuning performance.

2. *Significance*: Fine-tuning non-fully connected networks has been an actively studied topic in the recent years, especially after the debut of ChatGPT. This work is of significance to analyze DFA for fine-tuning and propose the solutions: feedback-weight matching.

### Weaknesses
1. *Quality*: It would largely improve the quality of this work to articulate the proof of propositions in mathematically standard manners. Usually propositions are presented in the main content and their mathematical proofs are rigorously detailed in appendices. The current presentation of the proofs within the main text disrupts the flow and makes it difficult to follow the core arguments. The mathematical derivations lack sufficient detail, making it challenging to verify the correctness and understand the underlying assumptions. For instance, the derivation of the feedback-weight matching should include a step-by-step breakdown with clear justifications for each transformation. The absence of this level of detail makes it difficult to assess the validity of the proposed method.

2. *Clarity*: Please also have a careful double check on the boldface numbers in Tables 1 and 2. It looks confusing and misleading to highlight the performance of the proposed method instead of the best performance. The experimental results should also be further analyzed. Please see **Questions** for details. The current highlighting gives a false impression that the proposed method always achieves the best results, which is not the case. A more transparent approach would be to highlight the best performing method in each case, regardless of whether it is the proposed method or a baseline. Furthermore, the experimental analysis lacks depth. For example, the authors should provide a more detailed discussion on the performance differences across different datasets and network architectures. It is not sufficient to simply present the numbers; a thorough analysis of why the proposed method performs better or worse in specific scenarios is needed.

### Questions
1. Would the authors clarify the statement "Equation (3) is referred to as weak weight alignment (WA) (Refinetti et al.,
2021), representing the state where no particular relationship exists between $\mathbf{W}_{1< l< L}^t$ and $\mathbf{F}_{l}\mathbf{A}_{l}^{t} \mathbf{F}_{l-1}^{\top}$, and between $\mathbf{W}_{L}^t$ and $\mathbf{A}_{L}^t \mathbf{F}_{L-1}^\top$? It seems that from Equation (3), $\mathbf{W}_{1< l< L}^t = \mathbf{F}_{l}\mathbf{A}_{l}^t\mathbf{F}_{l-1}^\top$, and $\mathbf{W}_{L}^{t}$ and $\mathbf{W}_{1< l< L}^t = \mathbf{A}_{L}^{t} \mathbf{F}_{L-1}^{\top}$.

2. In Table 2, the performance of DFA for training from scratch is the best among all three compared methods. It seems to be inconsistent to the performance on CIFAR-100. Could the authors explain the possible reasons? 

3. Why is the dataset STL more difficult to fine-tune on?

### Soundness
2

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
2

### Summary
This paper proposes feedback-weight matching to improve the reliability of fin-tuning for fully connected networks using direct feedback alignmeng.

### Strengths
+ It is quite interesting to investigate feasibility of using DFA for fine-tuning rather than training from scratch.
+ The proposed approach uses weight decay on top of feedback-weight matching to improve stability of fine-tuning, which makes sense. 
+ It has been shown that the proposed approach can work on transformer models for NLP tasks, which is more challenging.

### Weaknesses
 - It is not clear why the proposed approach hasn't been tested for other transformer models like ViT?
- The proposed approach has been evaluated on a limited number of datasets. Can it work on models trained, or do fine-tuning on imagenet?
- Some part of the paper is a bit difficult to follow.

### Questions
* Can this approach work for other vision models, not only just the fully connected ones?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the author presents a feedback-weight matching strategy that amalgamates Direct Feedback Alignment (DFA) (Nøkland, 2016) and back-propagation gradients to refine the pretrained classification models. The proposed approach attains superior performance compared to DFA, yet falls short of the performance exhibited by back-propagation based techniques. The author offers an in-depth theoretical analysis and validates the proposed method using basic network architectures.

### Strengths
1) The author offers a comprehensive theoretical analysis.
2) The proposed method attains superior performance compared to the original Direct Feedback Alignment.

### Weaknesses
1) The suggested approach appears to be ineffective. It yields inferior results compared to back-propagation based methods. The suggested strategy aligns the Direct Feedback weight with the back-propagation weight, resulting in enhanced performance. In my view, the improvement in results primarily stems from the back-propagation optimization.

2) The proposed method achieves lower performance than back-propagation methods.

### Questions
It appears that the enhanced efficacy still stems from the back-propagation optimization. Can the author elucidate on this?

### Soundness
2

### Presentation
2

### Contribution
2
