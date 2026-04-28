# Taming Transformer Without Using Learning Rate Warmup

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Scaling Transformer to a large scale without using some technical tricks  such as learning rate warump and an obviously lower learning rate, is an extremely challenging task, and is increasingly gaining more attention. In this paper, we provide a theoretical analysis for training Transformer and reveal a key problem behind the model crash phenomenon in the training, \ie, the spectral energy concentration of $W_q^{\top} W_k$ (where $W_q$ and $W_k$ are the projection matrices for query and key in Transformer), which is the reason for a malignant entropy collapse. To remedy this problem, motivated by Weyl's Inequality, we present a novel optimization strategy---making weight updating in successive steps smooth, that is, if the ratio $\frac{\sigma_{1}(\nabla W_t)}{\sigma_{1}(W_{t-1})}$ is larger than a threshold, where $\nabla W_t$ is the updating quantity in step $t$, we will automatically bound the learning rate to a weighted multiply of $\frac{\sigma_{1}(W_{t-1})}{\sigma_{1}(\nabla W_t)}$. Our optimization strategy is able to prevent the rapid spectral energy concentration to only a few directions, and thus is able to avoid the malignant entropy collapse that will trigger the model crash. We conduct extensive experiments using ViT, Swin-Transformer and GPT, showing that our optimization strategy can effectively and stably train these (Transformer) models without using learning rate warmup.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper deals with the challenges of scaling Transformers without relying on techniques like learning rate warmup. It provides a theoretical analysis that identifies the concentration of spectral energy in weight matrices as a key factor behind model crashes, leading to entropy collapse. To resolve this issue, the authors propose a novel optimization strategy that smooths weight updates, preventing rapid concentration of spectral energy. Extensive experiments with various Transformer models, including ViT, Swin Transformer, and GPT, demonstrate that this approach effectively trains models.

### Strengths
This paper demonstrates strong originality, with the necessary mathematical definitions and proofs included as required. It is well-structured and organized clearly. The essential mathematical framework is presented both in the main text and supplementary material. Additionally, experiments have been conducted to verify the theoretical claims made in the paper.

### Weaknesses
This paper has several areas for improvement in terms of writing, particularly regarding the use of mathematical notations in the abstract without proper definitions. A similar issue is evident in the Introduction as well.

The experiments are inadequate; the paper should incorporate additional baseline models for comparison, as it currently only discusses or modifies three models. It would be advantageous to present empirical results using well-known recent models, such as those with linear complexity in attention, like Linformer or Flatten Transformers. The current selection of models does not provide a comprehensive view of the method's effectiveness across different architectures and attention mechanisms.

It would be preferable to provide proper references instead of linking to internet sources (such as Wikipedia) as seen on page 6 and elsewhere.

### Questions
I have a few questions and suggestions as follows.

1. In the abstract, there are mathematical notations that should either be predefined or the abstract should be written more clearly without them.

2. In the Introduction, some notations are defined later in the text, such as "$\delta vec(P)$" mentioned in the second contribution point, which should be defined earlier.

3. The paper claims that spectral energy concentration is a key issue behind model crashes. If attention is computed without using softmax (for example, in Linear attention models like Flatten or Vicinity Vision Transformer), will the same crash occur? Is the problem specifically due to softmax, which might cause sparsity or model instability?

4. The paper states that "the attention map is a sparse yet low-rank matrix" (in the third contribution point). Does this imply that "$A = softmax(\frac{P}{sqrt{d_q}})$" is sparse? If so, please provide a reference or proof for this assertion.

5. In the experimental results, please clarify the choice of using only pure encoder architectures (like ViT) or pure decoder architectures (like GPT). Is it possible to utilize an architecture that combines both encoder and decoder components?

6. It would be preferable to provide proper references instead of linking to internet sources (such as Wikipedia) as seen on page 6 and elsewhere.

7. Please include some recent variants of Transformers in the empirical results for comparison.

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
The paper analyzes a training instability associated with the self-attention layer of a Transformer by studying its training dynamics. Specifically, the paper identifies a ```Spectral Energy Concentration``` condition where-in the weights of the product of query transpose key matrix shows a rank collapse. The paper proposes to bound the base learning rate per step when the optimizer (AdamW specifically) proposes very large update vectors. The paper shows how the need to use learning rate warmup can be  relaxed for training Transformers. Empirical results are provided to support analysis and proposed algorithm.

### Strengths
- The analysis of the  query (transpose), key weight matrix product  is interesting. Specifically, using the singular values of this product matrix to show collapse is interesting
- Application of Weyl's inequality to the update equation for the optimizer to stabilize Transformer training is a nice development
- The biggest contribution of this paper is that the proposed algorithm built on analysis frees up a practitioner to use  learning rate warmup.

### Weaknesses
 - The paper contains limited empirical results. Specifically, the experimental setup used to study the algorithm is small and no results are provided with larger models (0.5B, 1B, 3B). This limits the contribution as its not clear how the proposed algorithm will work with larger models (albeit can still be considered ``small'') where training instabilities are more apparent

- Related to above, the QK layer norm paper by Deghani et al. (2023) show that training instabilities occur at 8B for vision transformers (ViTs). So, I wonder whether the new update along with no learning rate warmup will work as advertised

- The paper proposes ``Spectral Energy Concentration (SEC) '' to quantify collapse. Wouldn't a smooth rank measure also provide the similar  information while being easier to interpret? Furthermore, this contribution is not novel as large attention logits being a problem has been observed in literature below by Deghani et al (referred to in the paper) and by [Worstman et al.](https://arxiv.org/abs/2309.14322). The proposed SEC measure requires a hyperparameter 's' to be specified, which introduces a practical limitation compared to a smooth rank measure that would not require such tuning.

- The argument in Section 3.2 is not very clear. Especially the reader could use some help with understanding why the rank of X.T being small would imply the rank of X.T \otimes X.T is still small. The equation shows a square relationship. Firming up the arguments here would be very helpful to the reader

### Questions
- Would the proposed optimizer update work at reasonable scales like the ones considered by [Worstman et al.](https://arxiv.org/abs/2309.14322)?

- How different is the instability shown by analyzing weights of Q.T, K product different from logit norm growth shown previously in literature?

- (clarification request) The paper describes the product matrix in line 345 in general as a non-symmetric positive quasi-definite
square matrix. A reference to what these technical terms mean and/or definition in the appendix would help clarify what this means to the reader. The reviewer was unable to come up with a definition of quasi-definite for non-symmetric matrices but this maybe perhaps because I missed looking at an appropriate reference. 

The concerns raised in the review is that the work has limited novelty and also limited empirical support. Therefore, the initial decision for this paper is a reject.

### Soundness
3

### Presentation
2

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
The paper presents a method to eliminate learning rate warmup for training transformes. It begins by analyzing training dynamics, specifically observing the norm of certain parameters to understand behavior patterns when training is successful versus when it crashes. The authors note that, in the presence of warmup, the parameter norms tend to increase steadily, while they diverge in failed training runs. However, this analysis does not introduce new insights, as it’s known that parameter norms typically blow up when training crashes.
The authors argue that warmup can be bypassed by controlling the spectral energy concentration (SEC), which maintains the singular values of the product $W_q^TW_k$​ thus allowing successful training. To achieve this, they introduce a modified version of the AdamW optimizer using a power iteration-based step to estimate the largest singular values of the $W_q^TW_k$ matrix. Experiments with the proposed method show that it can perform similar to warmup.

### Strengths
1 .The authors propose an alternate method for transformer training that does not need learning rate warmup.

### Weaknesses
1. The choice of parameter norms for tracking training dynamics seems arbitrary. It’s already established in literature that parameter norms diverge when training fails, so this observation does not seem novel [1]. The paper could benefit from a deeper analysis or rationale for the specific parameters chosen, or alternatively, from an exploration of novel insights that could provide a more compelling argument. Specifically, the paper lacks a discussion of why the norms of $W_q$ and $W_k$ are tracked, rather than, for example, the norms of the attention output or the value matrix $W_v$. A more thorough justification for the chosen parameters is needed, especially given the existing literature on parameter norm divergence during training failure.

2. While the authors claim that the attention maps are sparse and low-rank, the plots are difficult to interpret. Hence it is impossible to make conclusions based on the provided plots. It might help to change the scaling of the plots to help visualization or simply estimate the rank of the attention maps. The plots lack clear visual cues to support the claim of sparsity and low-rank structure. The authors should provide a quantitative measure of rank, such as the effective rank, or a clearer visualization that highlights the sparsity pattern, perhaps by using a logarithmic scale or a thresholding technique.

3. My major concern is that in the proposed algorithm that controls the step size to ensure the SEC does not collapse, only ends up modifying the step size $\alpha$. It seems to me that this is another way of performing learning rate warmup and the analysis further justifies the use of warmup as it may help prevent SEC from collapsing. In order to disentangle these ideas, the authors might need to discuss how the modified $\alpha_t$ looks over time (does it resemble warmup, which seems to be the case). Experiments also suggest that the proposed method is in fact very similar to warmup and might be a different parameterization offering the same benefit as warmup. The paper needs to provide a more detailed analysis of how the adaptive step size evolves during training. It is crucial to show whether the proposed method is simply a re-parameterization of learning rate warmup, or if it offers a fundamentally different mechanism for controlling training dynamics. A comparison of the step size evolution with typical warmup schedules would be beneficial.

4. Further, while replacing warmup the authors introduce an additional power iteration step which is computationally more expensive and adds to each gradient update step, while learning rate warmup does not require this additional step. The computational overhead of the power iteration step is a significant concern. The authors should provide a detailed analysis of the computational cost of their method compared to standard training with warmup, including the time complexity and actual runtime measurements. This is important to justify the practicality of the proposed approach.

### Questions
See above.

### Soundness
3

### Presentation
3

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
This paper visualizes the training dynamics of transformer models in both successful and failing cases. Based on these visualizations, the authors observe that the rapid growth of the maximal singular value of the product of the query and key matrices,  W_q^T W_k , is a critical phenomenon associated with model crashes. They provide insights suggesting that when  W_q^T W_k  becomes concentrated along the directions of the top singular vectors, the attention probability matrix becomes sparse and low-rank. They also show crashed models typically exhibit significant spectral energy concentration. Finally, the authors propose a variant of AdamW that addresses this issue by clipping the learning rate to prevent the spectral norm of all parameters from increasing too quickly.

### Strengths
This paper provides insightful experiments demonstrating that the rapid growth of the spectral norm of the query-key product matrix (and other parameter matrices) is a crucial factor in model crashes. The study shows that in crashed models, the spectrum of the query-key product matrices often concentrates on the top eigenvalues. This provides novel insight on understanding transformer optimization.

### Weaknesses
- The theory part does not enhance the paper as effectively as it could.
    - In Theorem 1, the statement is somewhat vague. Terms like “malignant collapse” and “spectral energy concentration” are not formally defined, making the theorem unclear. Additionally, the proof of Theorem 1, which appears in Appendix D, lacks clarity and coherence. For example, the theorem aims to establish a sufficient condition for malignant collapse, yet the proof assumes the low rank of  W  due to malignant collapse. Furthermore, the proof relies heavily on the assumption of Gaussian distribution.
    - I would personally suggest rewriting Theorem 1 as a highlighted insight or intuition, supported by experimental results, such as Figure 1 and 4.
- In Figure 5, could you elaborate on how the concentrated and low-rank structure of  $\frac{\partial \text{vec}(P)}{\partial \text{vec}(W_q^T W_k)}$  leads  $W_q^T W_k$  to become low rank? It still requires reshaping the matrix, multiplying the activation gradient, and summing over data from  $\frac{\partial \text{vec}(P)}{\partial \text{vec}(W_q^T W_k)}$  to the update of  $W_q^T W_k$, so this implication is not straightforward.
- Could you clarify how one would generally set the parameter $\tau$ for an unseen model, and how $\tau$ might vary as the model scales up?
- Additionally, does benign collapse occur in real training tasks?

### Questions
See weakness above

### Soundness
2

### Presentation
3

### Contribution
3
