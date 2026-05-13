# GLoRA: Geometric Adaptive Ranks for Efficient LoRA Fine-Tuning

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
Fine-tuning large language models is computationally intensive because it requires updating all parameters. Low-Rank Adaptation (LoRA) improves efficiency by modifying only a subset of weights but introduces a trade-off between expressivity and computational cost: lower ranks reduce resources but limit expressiveness, while higher ranks enhance expressivity at increased cost. Despite recent advances in adaptive LoRA techniques, existing methods fail to provide a theoretical basis for optimizing the trade-off between model performance and efficiency. We propose Geometric Low-Rank Adaptation (GLoRA), a novel framework that computes the intrinsic dimensionality of hidden state representations to adaptively select LoRA ranks. We demonstrate that the intrinsic dimension provides a lower bound for the optimal rank of LoRA matrices, allowing for a principled selection that balances efficiency and expressivity. GLoRA dynamically adjusts the rank for each layer based on the intrinsic dimensionality of its input and output representations, recognizing that not all model parameters equally impact fine-tuning. Empirical validation on multiple tasks shows that GLoRA consistently outperforms recent baselines within the same parameter budget.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes GLoRA, a geometric-adaptive LoRA method that is able to adjust each LoRA component's rank throughout the training process. By presenting a series of theoretical analysis, the authors establish the connection between the rank of transformer blocks and the intrinsic dimension. The experiments show that GLoRA is able to achieve better generalization performance with less computational cost.

### Strengths
1. This submission presents sufficient rigorous theoretical justification. The definitions, theorems, and corollaries are somewhat stated clearly in Section 3, which solidly supports the algorithm. 
2. The experimental results shown so far (Table 1) exhibit huge potential of GLoRA to outperform other LoRA baselines (LoRA, SLoRA) in the scenarios where the computational resources are the bottleneck.

### Weaknesses
1. **Missing the main algorithm.** I don't know if it's just me missing this important part, but in the paper, I haven't found any description about the main algorithm of GLoRA. After the theory (Section 3), it directly jumps into the experimental results. If the authors do have this (but buries it in somewhere else), I highly suggest to present it as a separate chapter. It would be also great if they can reiterate the main algorithm during the rebuttal. 
2. **Limited scope of empirical verification.** The experiments are conducted only on one LM architecture (DeBERTaV3, proposed in 2021), which is a bit outdated and of limited scope. Especially now the decoder-only LLMs are considered the strongest and are widely used. It would be good to include the experimental results on other LLM architectures. 
3. **Not enough baselines.** In the related work, the authors mention a few other baseline adaptive LoRAs (including AdaLoRA, ALoRA, SaLoRA). I wonder why the comparison is only conducted on the naive LoRA and SLoRA, where only one adaptive LoRA baseline is used? 
4. **Gap between the theory and the algorithm.** If I understand it correctly, the number of the parameters (rank(T)) needed for a Transformer block to represent a data distribution is not equivalent to the rank of LoRA. How do the authors bridge the gap between this discrepancy during training, as there is no concrete illustration of the algorithm?

### Questions
1. Estimating the intrinsic dimension of transformer blocks should be non-trivial and time-consuming. How does GLoRA achieve this with even faster training speed compared to naive LoRA? Is it because of its lower rank? 
2. See weekness 4. 
3. I understand the use of the AutoML tool for hyper-parameter tuning. I want to know if there are additional hyperparameters introduced by GLoRA, and what is the sensitivity of them if there is any? 
4. Missing critical citation of intrinsic dimension: Li, Chunyuan, et al. "Measuring the intrinsic dimension of objective landscapes." arXiv preprint arXiv:1804.08838 (2018) 

Most of my concerns and my questions stem from the lack of the main algorithm. I would happily increase my score once it is resolved.

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
This paper introduces GLoRA, a variant of LoRA that leverages the geometric properties of both the dataset and model parameters to adaptively adjust the rank.

### Strengths
The paper introduces a theoretical framework that justifies the intuition that the intrinsic dimension is smaller than the embedding dimension and tends to decrease during fine-tuning.

Additionally, the paper proposes an adaptive rank approach to enhance the performance of LoRA across a variety of natural language understanding tasks.

### Weaknesses
There are two major weaknesses in this paper:

1. There is a significant gap between the theoretical analysis and the experiments.
    - The connection between the theory (or the intuition behind it) and the method itself is not well-articulated. Specifically, how the theoretical insights are applied in the method is unclear, and there is no discussion on how to utilize existing intrinsic dimension estimation tools effectively during training.

2. The experimental results require further explanation.
    - For instance, in Table 2 on page 8, the "Mean Rank" is given as either an integer (1 or 2), rather than a real number.
    - The authors evaluated their method on only 6 of the 8 tasks from the original LoRA paper, leaving some tasks untested.
    - Additionally, while the proposed method performs significantly better than LoRA with ranks of 1 or 2, the mean rank across all datasets remains either 1 or 2, which raises questions about the method’s effectiveness and the representativeness of the reported results.

### Questions
As introduced in the identified weaknesses, here are specific questions:

Q1: How is the theoretical analysis connected to the model? How is the adaptive dimension calculated, and how does the rank change during fine-tuning?

Q2: Why are the Mean Ranks reported as integers?

Q3: Why were the remaining two datasets from the original LoRA paper not tested?

Q4: Why does the proposed method outperform LoRA with ranks of 1 or 2, even though the Mean Rank is consistently 1 or 2 across datasets?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel framework called Geometric Low-Rank Adaptation (GLoRA) for the efficient fine-tuning of large language models (LLMs). The key innovation of GLoRA is in its approach to Low-Rank Adaptation (LoRA), a method that updates only a subset of model weights to reduce computational costs. GLoRA computes the intrinsic dimensionality of hidden state representations to adaptively select LoRA ranks, providing a theoretical basis for optimizing the trade-off between model performance and efficiency. The framework dynamically adjusts the rank for each layer based on the intrinsic dimensionality of its input and output representations, recognizing the varying impact of model parameters on fine-tuning. Empirical results on multiple tasks show that GLoRA outperforms recent baselines within the same parameter budget.

### Strengths
- The paper provides a solid theoretical framework that connects the intrinsic dimensionalities of data representation manifolds with the ranks of weight updates in transformer blocks. 
- The paper backs up its claims with extensive empirical validation across multiple tasks, demonstrating that GLoRA consistently outperforms existing baselines while maintaining the same parameter budget.

### Weaknesses
 - Although the theoretical analysis part (section 3) is very solid, it lacks some takeaways to clearly describe the main body of the theoretical analysis. Specifically, the paper does not clearly articulate how the derived lower bound on the rank is actually used in practice, and how it relates to the selection of the LoRA rank for each layer. The connection between the theoretical findings and the practical implementation is not explicitly stated, leaving the reader to infer the connection.
- There is a lack of an overall summary description of the GLoRA method. An algorithm description or pseudo code can be added. The paper does not provide a clear step-by-step explanation of how the intrinsic dimensionality is estimated, and how this estimate is then used to set the LoRA rank. A more detailed algorithmic description would be beneficial for reproducibility and understanding.
- The experiment is a bit thin and lacks some supplementary experiments, such as studying the application position of GLoRA in the transformer model. It's unclear whether GLoRA is applied to all layers, or only a subset, and if the latter, how this selection is made. Furthermore, the paper lacks experiments exploring the sensitivity of the method to different choices of the intrinsic dimension estimator, and how this choice impacts the overall performance.

### Questions
- Why is there a lack of testing for MNLI and QQP tasks for the GLUE benchmark?
- In section 4.1, the authors mentioned that they wanted to compare Adalora. Why are there no experiments on Adalora in the following experiments?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies the trade-off between model performance and LoRA rank in the efficient fine-tuning scenario. Specifically, the authors propose GLoRA to adaptively select LoRA ranks by evaluating the lower bound of the optimal LoRA rank using the intrinsic dimension of the hidden representations. The author evaluate the performance of GLoRA on finetuning BERT-like classification models on the GLUE benchmark.

### Strengths
1. This paper studies the lower bound of the optimal LoRA fine-tuning rank, which bridge between the geometry of hidden representations and model parameter manifold.
2. This paper evaluate the performance of GLoRA in fine-tuning on GLUE dataset.

### Weaknesses
 1. The authors did not provide a formal definition or introduction of the proposed GLoRA algorithm. 
 2. From my understanding, according to Theorem 3.1 and Theorem 3.2, the authors proposed to set the amount of tunable parameters as $\max(d_{i}-d_{i-1},0)$, where $d_i$ is lower bounded by the rank of the Fisher information matrix of the $i$-th transformer block. However, the lower bounding $d_i$ and $d_{i-1}$ is not sufficient to establish an informative estimation of $d_i-d_{i-1}$. 
 3. The lower bound of the so-called 'optimal rank' in Theorem 3.1 and Theorem 3.2 seems to be loose, as it can takes the value $0$, which is the trivial lower bound.
 4. The established lower bound does not reflect how the LoRA rank can be adaptively adjusted based on data representations that might change during the fine-tuning process. The authors did not clarify in what sense the GLoRA ranks are considered "adaptive."
 5. The authors did not provide compare their method against AdaLoRA, SaLoRA, and ALoRA in Table 1 and Table 3. The empirical experiments are confined on the DeBERTaV3 architecture and GLUE dataset.
 6. Although this paper aims to study the optimal parameter rank through the lens of Riemannian geometry theory, the solidness of the notations and the derivations in this paper is compromised by some typo and undefined notations. Therefore, the paper is not easy to follow.
   1) What is the notation $\mathrm{dim} \mathfrak{J}mf$ in Page 3, line 157?
   2) The subscription $\phi$ might be missed in the FIM in Page 4, lines 181-184.
   3) The Riemannian metric is a (2,0)-tensor which measure the distance between two inputs (tangent vectors). For clarity, the FIM euqation might be $\mathcal{I}(\phi_1,\phi_2)=\mathbb{E}[\partial_{\phi_1}\log \mathbb{P}\cdot \partial_{\phi_2}\log \mathbb{P}^\top]$.
   4) For self-containess and rigority, can the authors add the formal mathematical definition of 'intrinsic dimension' in lines 240-242, and the 'estimated intrinsic dimension' $\mathrm{idim}(\cdot)$ in Theorem 3.1?

### Questions
1. How does the Conjecture 3.1 helps estimating the lower bound of $N_{i-1}$ or improving the rank selection process (e.g. which rank to choose) in LoRA during the training process? 
2. What is the algorithmic complexity of the rank estimation process in GLoRA?
3. Does GLoRA use a fixed rank across the training process? If not, how does GLoRA adapt the number of rank? What is the rank increasing and decreasing policy? Otherwise, what is the resulting rank pattern of GLoRA?

### Soundness
1

### Presentation
1

### Contribution
2
