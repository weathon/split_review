# Attention-Only Transformers via Unrolled Subspace Denoising

- Decision: Reject
- Scores: 6, 5, 3, 6

## Abstract
Despite the great success of transformers in practice, their architectures have been empirically designed, hence lack of mathematical justification and interpretability. Moreover, many empirical studies have indicated that some components of the transformer architectures may be redundant and can be removed or replaced without compromising overall performance. Hence to derive a compact and interpretable transformer architecture, we contend that the goal of representation learning is to compress a set of noisy initial token representations towards a mixture of low-dimensional subspaces. Based on the existing literature, the associated denoising operation naturally takes the form of a multi-subspace self-attention (MSSA). By unrolling such iterative denoising operations as a deep network, we arrive at a highly compact architecture that consists of only an MSSA operator with skip connections at each layer, without MLP. We rigorously prove that each layer of the proposed transformer performs so highly efficient denoising that it improves the signal-to-noise ratio of token representations {\em at a linear rate} with respect to the number of layers. Despite its simplicity, extensive experiments on language and vision tasks demonstrate that such a minimalistic attention-only transformer can achieve performance close to conventional transformers, such as GPT-2 and CRATE.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach to transformer architecture by proposing an attention-only model that utilizes multi-subspace self-attention (MSSA) for efficient denoising of token representations. The authors demonstrate that their unrolled optimization framework simplifies transformer architectures significantly, achieving performance comparable to traditional models while enhancing interpretability. Rigorous theoretical analysis supports the denoising capabilities of their architecture, showing improvements in signal-to-noise ratio across layers. Extensive empirical evaluations across language and vision tasks validate the practical effectiveness of their proposed design.

### Strengths
The use of unrolled optimization to design a simplified transformer architecture presents a fresh perspective on transformer design, focusing on interpretability and efficiency.

The paper rigorously proves the denoising effectiveness of the proposed architecture, providing a solid mathematical foundation for its claims.

The authors conduct comprehensive experiments across diverse tasks, supporting the practical viability of their approach and demonstrating competitive performance.

### Weaknesses
One notable weakness of this study is the lack of validation on state-of-the-art transformer architectures, such as Llama, and benchmark tasks, including MMLU. It would strengthen the paper significantly to include evaluations on these platforms to better assess the proposed method's performance in comparison to leading models in the field.

The paper could benefit from more detailed comparisons to the latest transformer variants such as mamba and linear transformers, which may also claim reduced complexity or improved performance.

### Questions
See the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Paper proposes an attention only transformer with guarantees that each subsequent layer improves the SNR of the signal. they provide theoretical insights in to how such a system is beneficial and also run some baseline experiments on how this holds up against traditional transformer networks.

### Strengths
The approach is very good and sound. builds on strong pre-existing work and adds an important piece to it. The flow of the paper is good and adds theoretical justifications on attention only transformers.

### Weaknesses
The paper doesn't offer any practical analysis on the theory. The results on language and vision are good, but using the paper's own arguments, the training dynamic of such systems and modern frameworks can reach convergence outside of this papers contributions. The key piece missing is an approach to understanding how the proofs of the theory play out in actual training. Specifically, while the paper provides a theoretical framework for improved signal-to-noise ratio (SNR) in attention-only transformers (AoT), it lacks empirical validation of this improvement in trained models. The paper needs to demonstrate that the theoretical SNR gains are observable in practice, not just as a theoretical construct. The current experiments show that the models perform well, but not that the SNR improves layer by layer as the theory suggests. This is a critical gap in the analysis.



### Questions
How does the reformulation in the paper for AoT converge?
How can we observe better SNR in these models?

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
5

### Summary
This paper introduces a class of interpretable attention-only transformers that compresses noisy initial token representations into a mixture of low-dimensional subspaces, primarily building on the multi-head subspace self-attention introduced in [1]. The authors provide theoretical guarantees on the model's denoising performance, demonstrating that the signal-to-noise ratio improves with each layer. Experimental results in both language and vision tasks illustrate the advantages of the proposed transformer.

### Strengths
1. The paper provides a good review of the multi-head subspace self-attention from [1].

2. The paper is well-written with illustrative figures.

### Weaknesses
1. The proposed attention-only transformer is just a simple extension by unrolling Eqn. 3 in the paper, which is the multi-head subspace self-attention in [1]. Most heavy-lifting work has been done in [1], and unrolling Eqn. 3 is just an incremental contribution.

2. The motivation behind the proposed unrolling transformers is to denoise the noisy initial token representations towards a mixture of low-dimensional subspaces. However, it is not clear why denoising token representations should help improve the performance of the model. Also, there is no empirical evidence showing that the tokens are drawn from a mixture of noisy low-rank Gaussian distributions as assumed in Definition 1.

3. The experimental results are unconvincing.

* First, in Table 1, test perplexity should be used to evaluate the models rather than just validation loss and zero-shot accuracy. Also, in Table 1, the proposed models need many more parameters compared to the baseline GPT-2 while still worse than the baseline GPT-2 in most cases. 

* Second, in Table 2, the performance of the proposed model, AoT, on ImageNet-1K is much worse than the baseline CRATE-\alpha model. For example, AoT-Huge has more parameters (86M) than the baseline CRATE-\alpha-B/16 but is 2% worse than the baseline in top-1 accuracy. 

* Third, even though the authors claim that their proposed transformer is interpretable in the abstract and introduction, there are no experiments to show the interpretability. Similarly, one of the contributions mentioned in the introduction is to understand the role of self-attention and MLP layers, this is not really empirically discussed in the paper.

4. I highly doubt the efficiency of the proposed method. From Table 1 and Table 2, it is clear that the proposed model requires more parameters than the baseline transformer models. Also, the multi-head subspace self-attention in Eqn. 3 requires more computations compared to the baseline self-attention.

### Questions
1. Why shared-QKV subspace self-attention mechanisms, as mentioned in line 299? 

2. Please provide the efficiency analysis, i.e., real-time running and memory usage, of the proposed transformer vs. the baseline transformer.

**References**

[1] Yaodong Yu, Sam Buchanan, Druv Pai, Tianzhe Chu, Ziyang Wu, Shengbang Tong, Hao Bai, Yuex- iang Zhai, Benjamin D Haeffele, and Yi Ma. White-box transformers via sparse rate reduction: Compression is all there is? arXiv preprint arXiv:2311.13110, 2023a.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a multi-subspace self-attention (MSSA) to replace Transformers. By unrolling such iterative denoising operations as a deep network, the proposed technique arrives at a highly compact architecture that consists of only an MSSA operator with skip connections at each layer, without MLP. They also rigorously prove that each layer of the proposed transformer performs so highly efficient denoising that it improves the signal-to-noise ratio of token representations at a linear rate with respect to the number of layers.

### Strengths
1. The motivation is based on the existing linear representation hypothesis and the superposition hypothesis, which states that the token representations lie on a union of (possibly many) low-dimensional subspaces. 

2. The empirical performance is good. On zero-shot language tasks and fine-tuning ViT, the method achieves comparable results.

### Weaknesses
1. A lot of linear hypothesis works can be used to do some interpretability tests of the LMMs. I am wondering if this new architecture might naturally fit the interpretability tests. I would suggest that the authors try GPT's auto-interpretability and might do some circuit analysis as done in [1].

2. Can the author do some experiments about training ViTs from scratch? That would be more convincing to show the effectiveness.

3. Can authors visualize some of the attention masks in ViTs for a few input images? That might help if each $U$ can correspond to different regions

### Questions
Please see the weaknesses.

My main interest is to see if this architecture has better interpretability. The authors emphasize the interpretability in the intro but do not really validate it in the experiments. I am curious to see the results.

### Soundness
3

### Presentation
3

### Contribution
3
