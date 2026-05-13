# Direct Preference Optimization Using Sparse Feature-level Constraints

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
The alignment of large language models (LLMs) with human preferences remains a key challenge. While post-training techniques like Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) have achieved notable success, they often experience computational inefficiencies and training instability. In this paper, we propose \textbf{F}eature-level constrained \textbf{P}reference \textbf{O}ptimization (FPO), a novel method designed to simplify the alignment process while ensuring stability. FPO leverages pre-trained Sparse Autoencoders (SAEs) and introduces feature-level constraints, allowing for efficient, sparsity-enforced alignment. Our approach enjoys efficiency by using sparse features activated in a well-trained sparse autoencoder and the quality of sequential KL divergence by using the feature-level offline reference. Experimental results on benchmark datasets demonstrate that FPO achieves an above 5\% absolute improvement in win rate with much lower computational cost compared to state-of-the-art baselines, making it a promising solution for efficient and controllable LLM alignments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces feature-level constraints aimed at  improving the stability of alignment training process and reducing memory usage. However, the improvements are marginal, at the cost of increased complexity. And the paper lacks justification for some crucial design decisions and fails to provide analysis on hyperparameter tuning, especially for the KL divergence coefficient.

### Strengths
1. This paper incorporates feature-level constraints into DPO and use sparse autoencoders to identify the features used for constructing the constraints, which is novel to my knowledge. 

2. The paper is well-written and easy-to-follow.

### Weaknesses
1. This paper essentially builds upon SimPO by introducing feature-level constraints to improve the stability of alignment training. However, it does not discuss the advantages of the proposed constraints over the widely used forward KL divergence. Additionally, SimPO+KL should be included as a baseline in the experimental section.

2. As claimed by the authors, the proposed feature-level constraint offers efficiency advantages over the token-level KL divergence constraint. However, while the proposed method reduces memory usage by 5G, it significantly increases the algorithm's complexity by introducing at least two additional hyperparameters, the target layer and SAE type, both of which are challenging to tune in practice and can vary across different network architectures and sizes.

3. According to Table 2, the improvement achieved by the proposed method is marginal. For instance, on the Gemma-2-2B model and the benchmark AlpacaEval-2 (805 questions), the proposed method yields better responses than SimPO in only up to eight samples, while significantly increasing the algorithm's complexity. On the Gemma-2-9B model, the number of superior samples does not even exceed three samples compared to SimPO. Furthermore, as shown in Figure 3, the proposed method reduces the KL divergence on positive samples, raising doubts on its effectiveness.

4. By introducing Sparse Autoencoders, the authors achieve a 5-8G reduction in memory usage compared to TDPO. However, based on my experience, this reduction could be accomplished using engineering techniques, such as offline storage or off-load, without introducing additional modules that increase algorithmic complexity. Could the authors elaborate more on this?

5. The algorithm lacks in-depth clarification and analysis of some design choices. e.g.,

5.1. Why the 2-norm is used in the proposed loss function instead of other distance metrics? Could the authors provide a deeper insight, potentially from the theoretical perspective?

5.2. Why sparse encoding is applied only to a single layer’s hidden state l  as shown in Eq (12-13) rather than certain layers of the network? And how to choose this layer?

6. It is not discussed whether the proposed method can be generalized across different model architectures. 

7. The comparison methods in this paper involve many hyperparameters, especially the KL divergence coefficient. How did the authors tune these parameters? Could the authors present and compare the performance of the methods under different KL divergence coefficients?

### Questions
Please refer to "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a method, Feature-level constrained Preference Optimization (FPO) for human preference alignment.  FPO replaces the KL divergence regularization with l2 regularzaion in  Token-Level Direct Preference Optimization (TDPO) and uses a sparse autoencoders (SAEs) for efficiency and stability. The length control trick is also applied. Numerical results on Gemma-2-2B and Gemma-2-9B are presented.

### Strengths
This paper addresses an important problem in LLM post-training, focusing on improving efficiency and stability in alignment with human preferences.

### Weaknesses
1. The sample code is not provided, which limits the reviewers' ability to verify reproducibility.

2. Could the authors elaborate on why results are provided only for Gemma models? What about results for Llama models?

3. Based on the current presentation, I would consider it as a relatively simple extension of DTPO, as both methods incorporate token-level knowledge and use regularization to integrate it back into DPO. A more detailed discussion clarifying the differences would be beneficial.

### Questions
Please see the weaknesses part.

At this stage, I tend to recommend rejection. However, I am open to reevaluating this work based the furture discussions.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper try to address the challenge of aligning large language models (LLMs) with human preferences, which is a critical task. It acknowledges the limitations of post-training techniques like RLHF and DPO, which, despite their success, can be computationally inefficient and unstable. To address this, the authors propose Feature-level constrained Preference Optimization (FPO), a novel method that aims to simplify the alignment process while maintaining stability. FPO uses pre-trained Sparse Autoencoders (SAEs) and incorporates feature-level constraints to enable efficient and sparsity-enforced alignment. The approach benefits from the use of sparse features activated within a well-trained sparse autoencoder and leverages the quality of sequential KL divergence through feature-level offline reference. The experimental results on benchmark datasets show that FPO achieves a 5.08% absolute improvement in win rate with a significantly lower computational cost than state-of-the-art methods, suggesting it as a promising solution for efficient and controllable LLM alignments.

### Strengths
1.	The paper introduces an innovative Feature-level Constrained Preference Optimization (FPO) methodology, aimed at addressing the alignment challenge between Large Language Models (LLM) and human preferences—a pivotal issue in ongoing research endeavors.
2.	The FPO approach harnesses pre-trained sparse autoencoders (SAEs) and feature-level constraints, thereby offering a novel perspective on an efficient and robust alignment process.
3.	The experimental outcomes reveal a significant absolute victory rate enhancement on the benchmark dataset, while the computational expense is beneath that of the current state-of-the-art benchmarks. This indicates that the methodology holds promise in terms of efficiency and manageability.

### Weaknesses
1.	I continue to harbor confusion regarding the "feature" in the context of Feature-level Constrained Direct Preference Optimization. Could you elucidate the specific characteristics of the extracted features from the text? Furthermore, what distinguishes the essence of feature-level from token-level, fundamentally; and why are they juxtaposed for comparison? 
2.	I find myself deeply perplexed by Figure 3 and middle figure of Figure 4. What the authors intend to convey? How does achieving the minimum KL divergence in FPO's margin manifest "Enhanced Controllability"? Could the author provide further elucidation on Figure 3 and middle figure of Figure 4 ?
3.	In the right panel of Figure 4, there are a total of twenty points, with six situated below the "Tie Line" (representing 30%). This does evoke a measure of skepticism regarding the efficacy of the method in question. Furthermore, as indicated by the data presented in Table 3, the performance of FPO failed to surpass that of TDPO-2, according to the authors' findings. Although FPO does exhibit greater efficiency in terms of GPU utilization, this discrepancy appears to be of somewhat negligible significance (given our graphics cards typically operate at 80GB). 
4.	The author offers a meager synthesis of offline preference alignment methodologies, with the present article notably lacking a comprehensive summary and description of pertinent prior work. This deficiency hinders the understanding of the broader offline preference alignment field by other researchers. I suggest the author supplement this with a more extensive synthesis in the form of a review and consider the citation of following literatures:

[1]	Wang Z, Bi B, Pentyala S K, et al. A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More[J]. arXiv preprint arXiv:2407.16216, 2024.

[2]	Shen T, Jin R, Huang Y, et al. Large language model alignment: A survey[J]. arXiv preprint arXiv:2309.15025, 2023.

[3]	Azar M G, Guo Z D, Piot B, et al. A general theoretical paradigm to understand learning from human preferences[C]//International Conference on Artificial Intelligence and Statistics. PMLR, 2024: 4447-4455.

[4]	Wang C, Jiang Y, Yang C, et al. Beyond reverse kl: Generalizing direct preference optimization with diverse divergence constraints[J]. arXiv preprint arXiv:2309.16240, 2023

[5]	Sun H, Zheng Y, Zhao Y, et al. Generalizing Offline Alignment Theoretical Paradigm with Diverse Divergence Constraints[C]//ICML 2024 Workshop on Models of Human Feedback for AI Alignment. 2024.

[6]	Chen H, Zhao H, Lam H, et al. Mallows-DPO: Fine-Tune Your LLM with Preference Dispersions[J]. arXiv preprint arXiv:2405.14953, 2024.

[7]	Rafailov R, Hejna J, Park R, et al. From $ r $ to $ Q^* $: Your Language Model is Secretly a Q-Function[J]. arXiv preprint arXiv:2404.12358, 2024.

Generally speaking, the paper's proposed methodology is innovative, presenting an intriguing perspective; however, the author should elucidate the issues surrounding the 'weakness' aspect. Should the author address my concerns, I would be inclined to enhance my rating.

### Questions
See 'Weaknesses' Part.

### Soundness
3

### Presentation
3

### Contribution
3
