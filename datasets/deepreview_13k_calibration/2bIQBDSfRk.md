# DenseAttention: No-Compromise Exact All $N \times N$  Interactions Algorithm with $O(N)$ Space and Time Complexity

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
The ubiquitous Transformer architecture suffers from two main bottlenecks: 1) low computational and memory efficiency, leading to suboptimal hardware utilization, and 2) quadratic time complexity with respect to sequence length $N$, making it slow and costly for large data contexts. We propose a novel DenseAttention Network architecture, a straightforward simplification of the standard Transformer block that addresses these issues and serves as a drop-in replacement for language modeling tasks. We eliminate memory-bound components in DenseAttention, including Softmax, masking, one skip connection, and both LayerNorms, as well as key, value, and output projection matrices, as they become redundant. Despite these removals, it maintains exact $N \times N$ pairwise interactions between tokens. By exploiting the associativity of matrix multiplications, DenseAttention can be computed with $O(N^2d)$ or $O(Nd^2)$ time and space complexity, depending on the context. To handle the absence of Softmax and prevent numerical instability, we introduce MaxNormActivation at both ends of the Transformer block. We also devise Cosine Relative Positional Embeddings as a computationally efficient replacement for RoPE, and simple LocalAttention variations of the block to help the model focus on details in extremely long contexts. 

DenseAttention competes with FlashAttention in speed on small sequences and outperforms it by orders of magnitude on large contexts. We pre-train encoder language models on sequences up to 16K in length, which perform similarly or better than baseline BERT-large, while significantly improving speed and efficiency.  Finally, we achieve state-of-the-art on the LRA benchmark among the Transformer-based architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors propose a new architecture, DenseAttention Network, which could potentially replace Transformer. The motivation of this new design is to alleviate the quadratic time complexity in sequence length as well as the memory-bound operations in the vanilla Transformer (e.g. softmax and layer normalization). Specifically, they propose to linearize the original multi-head attention layer with naive matrix multiplications. To stabilize the forward pass, the inputs of each layer are scaled to have the same $\ell_\infty$ norm. The authors further propose a replacement for the rotary embedding and sliding window that is compatible with their approach.

**Strengths**
1. Given the popularity of Transformer models, the topic of their efficiency becomes more and more important. The proposed solution is also well-motivated.
2. The paper is well-written and easy to follow.

**Weaknesses**
1. The major flaw of this paper is the thin experiments.
2. The paper lacks several important previous papers.

In summary, this paper proposes a potential solution to accelerate Transformer models. However, the experiments are not convincing enough. Therefore, I would recommend a clear rejection unless there is further evidence.

### Strengths
1. Given the popularity of Transformer models, the topic of their efficiency becomes more and more important. The proposed solution is also well-motivated.
2. The paper is well-written and easy to follow.

### Weaknesses
1. The major flaw of this paper is the thin experiments. The Transformer model is known to perform well on a wide range of tasks. In addition, it also demonstrates a promising scaling effect. On the other hand, this paper only contains limited experiments: (1) the testbeds are limited. Currently, the only benchmark is Long Range Arena (for causal LMs); (2) the baselines are limited. There is only one Transformer model that serves as the baseline without specifying how the model is trained; (3) the scaling effect is not studied. The authors do not analyze how the parameter number affects the results. It is unclear if the method could be scaled to larger-scale applications.
2. The paper lacks several important previous papers. In fact, linearizing attention has been heavily studied before [1, 2, 3]. This paper has no comparisons or discussions.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a DenseAttention Network (DANet), which addresses inefficiencies in the Transformer architecture, especially its high memory and computational cost - O(N^2), with respect to sequence length - N. DANet uses a new MaxNormActivation and Cosine Relative Positional Embeddings, capturing N x N interactions at O(N) space and time complexity. Experimental results demonstrate that DANet outperforms FlashAttention on long sequences on the Long Range Arena benchmark.

### Strengths
1) The paper proposes an interesting approach to eliminate projection matrices in attention, considering that the multiplication $W_QW_K^{\top}$ can be replaced with a single parameter, which I don't think exists in previous literature.
2) The paper also proposes using local attention in conjunction with the proposed attention function.

### Weaknesses
1) The paper lacks comparison against mamba in experiments. Mamba-I and Mamba-II are fast approaches for long range sequence modeling.
2) This is not the first paper which captures NXN correlations with O(N) complexity. Linear attention [1] uses linear approximations of attention. A fair comparison with this paper would be great.
3) The mathematical writing in this paper is inconsistent. Here are some instances:


Better Notation:
1. Standard operators max, var should be mentioned in times new roman using \DeclareMathOperator
2. Defined operators such as MaxNormActivation can be put in \text{MaxNormActivation}, as done in 200-204. 
3. Line 240: has a typo open bracket.
4. Line 284: << should be \ll.
5. Line 246: why is fp16 and bf16 bolded?

Major readability issues:
1. Inconsistent definition of $X_i$ in line 247, 300 and 311.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel neural network architecture called DenseAttention Network as alternative to Transformer networks with Self-Attention. 
The core innovation of DANet is the novel DenseAttention mechanism, which removes Softmax and projection layers from original Self-Attention.
Additionally the authors modify the surrounding network block: They replace Layernorm or RMS with their novel “MaxNormActivation”, they remove some skip connections and modify the Rotary Positional Embeddings. 
The paper performs experiments on the Long Range Arena Benchmark and masked language modeling with BERT-large sized models. 

The paper claims to outperform a BERT baseline on masked language modeling. 
It claims to set a new SOTA on “Transformer-based” models on LRA and to outperform 4 of 6 State Space model baselines.

### Strengths
- The usage of MaxNormActivation seems to be well motivated by a theoretical variance analysis. However, this could also be supported with experiments empirically too.
- Code provided.

### Weaknesses
In general I believe this paper is not ready for publication as there are several weaknesses in terms of the new architecture, the experiments and the presentation in the paper. My main concerns are summarized below: 

- A related work section is missing in which the authors put DANet in relation to other Linear Attention variants (e.g. GLA https://arxiv.org/abs/2312.06635 ), State space models (e.g. Mamba https://arxiv.org/abs/2405.21060) or other RNNs variants (e.g. xLSTM (https://arxiv.org/abs/2405.04517 ) or RWKV (https://arxiv.org/abs/2305.13048 )). Also a relation to embedding models other than BERT is missing, e.g. Monarch Mixer (https://arxiv.org/abs/2310.12109).
- Since DANet seems to be a hybrid architecture (Section 3.3), also a relation to hybrid architectures (e.g. https://arxiv.org/abs/2402.19427, https://arxiv.org/abs/2406.07522) is interesting.
- There are so many architecture changes (e.g. Layernorm, Positional Encoding, Block structure, Attention mechanism, Block order / hybrid variants) that leave the reader unclear of what brings performance gains. A careful ablation study could help here.
- While the paper demonstrates large throughput benefits in the long context regime compared to Transformers, it has not been shown in the paper that DANet performs well in the long context regime.
- Regarding Cosine RelPE: It is not clear why the authors made the modification to the original Rotary Positional Embedding. It seems to be motivated by efficiency gains, but this claim is not supported sufficiently. An experiment on this could help.
- A conclusion is missing.

### Questions
- Why do you still consider DANet as Transformer-based? The only part of transformers that is left, is the Feeforward layers which is now inside the block.
- You train your model with 4 stages, but the original BERT was trained on 2 stages. Could you also train the baseline in the same way?
- On page 10, line 494 (key highlights) you hint at the fact that DANet outperforms the baseline due to a soft-capping of output logits that you use. Why did you not try this for the baseline as well? 
- L.400: The authors find that local attention is effective. Do you use the Transformer Self-Attention here? An ablation on this would be interesting.
- Why do you use float16 in the experiments?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a new architecture which they call DenseAttention Network, which is a variation of the standard transformer architecture which is specifically tuned to perform well on long sequences. The changes include:
1) Take the softmax away in the attention block, writing $QK^{\top}V$ instead of $\mathrm{softmax}(QK^{\top})V$, and using associativity to compute the matrix product in linear time. (They name this as DenseAttention mechanism/block.)
2) Use a MaxNormActivation block instead of LayerNorm, which scales each token feature by its maximum absolute value.
3) Use a novel positional embedding called Cosine RelPE, which is claimed to perform similarly but more efficiently computable than RoPE.
4) For very long contexts, use a hand-rolled local attention implementation suited for DenseAttention.
They show that this architecture has general improvements over a basic transformer + RoPE implementation in Long Range Arena, both in performance (across a few tasks) and efficiency (more broadly, as the usual attention mechanism does not have linear-in-$N$ time complexity). It also shows improvements against S4-V1 in Long Range Arena, and BERT in terms of Masked Language Modeling.

### Strengths
- The MaxNormActivation block is potentially useful as a method to stabilize LLM training.
- The empirical results in tables 1-3 show that DenseAttention has some promise empirically on long-context sequence modeling tasks as compared to the standard transformer, S4-V1, and BERT.
- The efficiency results in table 4 show that it's possible to get out-of-the-box performance increases at long context compared to the usual BERT model. Specifically, all changes seem to be architectural, and no specialized kernels are needed to get better performance, as a result of using `torch.compile` and potentially fusing linear operations together.

### Weaknesses
 - The main mechanism behind DenseAttention, i.e., removing the softmax and using associativity to compute the product in linear-in-$N$ time, has been studied before; see for example [1]. It is acknowledged that the paper cites [1], but the paper suggests that the mechanism in [1] has poor efficiency; however DenseAttention is strictly a special case of the mechanism in [1] (using the notation of [1], set $\phi$ as the identity mapping). So this claim does not make sense, and the novelty of DenseAttention seems limited.

- The reasoning behind using MaxNormActivation seems lacking. In particular, since all norms are equivalent (i.e., bounded by each other up to multiplicative constants, possibly dependent on dimension) in finite-dimensional vector space, the boundedness of the maximum norm is equivalent to the boundedness of the $\ell^{2}$ norm. So if the argument in the paper goes through, it should mean that $\ell^{2}$ normalization should also work (then why not LayerNorm? But LayerNorm doesn't work, as reported in the paper, so something else is going on.). Although the MaxNormActivation is an interesting and potentially useful contribution, it may not work for the reason explained in the paper. Also there's a potential typo in the equation defining MaxNormActivation: it should be $\frac{X_{i}}{\max_{j}|X_{ij}| + \epsilon}$ on the RHS (note the absolute value).

- Not much motivation is given for the two other modifications, e.g., CosineRelPE and the local attention proposal - they seem to have a flavor of "we tried it and it works," potentially with some ablation, and without context of why such an approach may or may not make sense or generalize to other architectures.

- The results in Long Range Arena are promising insofar as they match up against a standard transformer and an SSM, but this may not be a fair comparison. Given that the authors start with a regular transformer and apply modifications to show improvement on long-context, they could also compare against more recent models specialized for long context. For example, the authors omit comparison with S5, whose numbers are publicly available on [PapersWithCode](https://paperswithcode.com/dataset/lra), as well as S4 V2 and a long list of other models benchmarked on Long Range Arena but not necessarily added there.

- The result on efficiency compared to BERT also may seem to not be a fair comparison. BERT is trained with an encoder-only architecture, while DenseAttention Network is trained with a decoder-only architecture. A fairer comparison would pit DenseAttention Network against a regular decoder-only transformer (as well as BERT if desired, along with, say, an SSM), under the same experimental setting, and allow readers to observe trends in the different approaches as different scaling parameters vary.

### Questions
- What is the specific motivation of designing CosineRelPE? 

- Is there anything that suggests that any new block (DenseAttention, CosineRelPE, MaxNormActivation) can generalize to other architectures and improve either performance or efficiency (while not degrading the other)?

### Soundness
2

### Presentation
2

### Contribution
2
