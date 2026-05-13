# Tree Attention: Topology-Aware Decoding for Long-Context Attention

- Decision: Reject
- Scores: 6, 6, 5, 5, 3

## Abstract
Self-attention is the core mathematical operation of modern transformer architectures and is also a significant computational bottleneck due to its quadratic complexity in the sequence length. 
In this work, we derive the scalar energy function whose gradient computes the self-attention block, thus elucidating the theoretical underpinnings of self-attention. 
Our formulation reveals that the reduction across the sequence axis can be efficiently computed in parallel through a tree reduction. 
Our algorithm, called Tree Attention, for parallelizing exact attention computation across multiple GPUs enables cross-device decoding to be performed symptotically faster (up to 8x faster in our experiments) than state-of-the-art approaches such as Ring Attention, while also requiring significantly less communication volume and incurring 2x less peak memory. 
We demonstrate that Tree Attention speeds up decoding up to 4x on Llama 3.1-8B and can be applied to a variety of hardware and networking setups such as H100 DGX nodes, AMD MI300x nodes, and PCIe connected NVIDIA RTX 4090s.
Our code is publicly available here: https://anonymous.4open.science/r/tree_attention-7C32

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript "Tree Attention: Topology-Aware Decoding for Long-Context Attention" proposes a novel strategy for computing self-attention coefficients in Transformers, the fundamental operation behind the functioning of this highly celebrated generative model. The method is based on two fundamental ideas. The first is theoretical, inspired by statistical mechanics: at each step of the data generation process, self-attention can be computed as the gradient of a function that resembles the free energy of a multi-particle system at thermodynamic equilibrium. The second idea, on the other hand, concerns hardware: an ensemble of GPUs can be employed to compute the energy function along a tree-like scheme. Consequently, self-attention is computed in such a way that inter-node communication is avoided, unlike in recent architectures presented in the literature.
The main result of the paper is an algorithm for computing self-attention that is faster, as it scales logarithmically with the number of GPU nodes used in the process; requires less memory for storing useful variables before usage; and reduces inter-node communication volume for shorter execution times.

### Strengths
The main strength of this work lies in the elegant simplicity of the energy-driven theoretical argument, which enables a simplification of the architecture used to compute self-attention coefficients. The paper is well-written and pedagogical, even for readers who are not experts in physics or in the technical aspects of executing self-attention computation on this type of machine.

### Weaknesses
I believe that the authors should make a stronger effort in validating the theoretical predictions about the improvement in the computational cost of self-attention proposed by the Tree Attention method, which is also their main scientific question. The scaling of the execution time $T$ with respect to variables $N$ and $p$ is reported in figure (3), without any proper experimental analysis of the results, which would effectively validate the theoretical predictions and convince possible future users. While their report only shows that Tree Attention is faster than Ring Attention, a deeper analysis of the experiments would be definitely needed: e.g. one might start from a linear fit of $T$ Vs. $N$ in linear scale and a linear fit of $T$ Vs. $p$ in log scale; a proper expected scaling (to be confirmed by the plots) of Ring Attention is never provided, while the condition $T_{ring} > T_{tree}$ might give useful bounds on the choice of the parameters of the system.  
Moreover, while the paper emphasizes a strong connection with modern Hopfield models (which are even mentioned in the abstract), this aspect is never properly addressed in the manuscript. As a matter of fact, the only—yet fundamental, for the sake of the results—physics-inspired part of the work consists in deriving self-attention by applying the logsumexp function, which satisfies the associative property. On the other hand, self-attention has emerged in previous papers (see: Hoover et al. 2023, Kozachkov et al. 2023, D’Amico et al. 2024) due to its analogy with the gradient descent dynamics over the energy function of the modern Hopfield model. Since both the dynamic aspect/analogy part and the thermodynamic one, which involves considerations about minimization of a free-energy function, are only briefly discussed, I would consider sacrificing some of the discussion about Hopfield models to give more room to a broader test of the analytical predictions.


Major issues:

1) From Theorem (1), the computational complexity of self-attention, for a single query, is $O( \frac{N}{p} + \log p )$  where $N$ is the full length of the sequence and $p$ is the number of processors. The total complexity is thus quadratic in $N$. There are examples of methods that simplify the total complexity to $O(N)$ (e.g. BigBird, Longformer) or $O(N \log N)$ (e.g. Reformer) which, by the way, do not rely on a modification of the processors disposition and are not necessarily exact. If we assume the number of GPUs to scale as $p = \alpha N$ where $\alpha > 0$, then the complexity per query would scale as $O(\log N )$, hence the total complexity as $O(N\log N)$ which equals the one obtained by Reformer. Nevertheless, even if this scenario appears difficult to reproduce, since $N$ is large by definition, this limit is mentioned in the text (row 269). Could the authors comment on this? 

2) Regarding the experiments reported in Section 5.1. Physical limitations seem to impose that $p = O(1)$, and $p \ll N$. As a consequence, the effective behaviour of the execution time $T$ with respect to $N$ is $T \simeq \frac{N}{p}$, hence it is linear in $N$. On the other hand, when $N$ is fixed, we have $T \simeq  \frac{N}{p} + log(p)$, it should then scale logarithmically with $p$ for large $p$. Can the authors show these trends more clearly from figure (3) e.g. increasing the number of points (in the intermediate range, i.e. between the current minimum and maximum values on the x-axis) and performing a proper fit of the data-points? Moreover: what is the expected scaling of the computational cost of Ring Attention as a function of $(N,p)$ ? It seems from figure (3,b) that the behaviour of $T_{ring}$ as a function of $p$ is linear, while in principle it should be constant and remain $T_{ring} \gg \log p$. If not, please provide for a theoretical argument to explain this behaviour.

3)May the authors show that the formulation of $o$ in line (2) of Algorithm (3) already normalized by $lse$ is equivalent to implementing the formulation from line (4) in Algo (2)? Expanding the mathematical passages in Algo (3) might useful to visualize this aspect.  

4) The difference between the memory costs of Ring and Tree attentions is $\delta_{M} = Mem_{ring} - Mem_{tree} = 2b(\frac{N}{p}\cdot d - n_{h})$. Could the authors check for the scaling of this quantity with respect to $(N,p)$ to satisfy $\delta_{M} \propto \frac{N}{p}$ ? I believe this would make the analysis more rigorous and reliable. 

5) I propose to the authors to add the most recent attempt to map the self-attention mechanism into a energy-based model, i.e. D’Amico et al. 2024, to the Related Work appendix. Nevertheless, i would spend much more space in the same paragraph to mention previous works in the matter of the computational complexity of computing self-attention, even the cases where multiple processors were not employed. A useful review about this problem can be found in Keles et al. 2023.  

Minor Issues:

6) I suggest the authors to substitute the Wikipedia reference for the definition of Helmholtz free-energy with a more reliable and solid scientific source, among the thousand great statistical mechanics books. One example is  Landau, Lifshitz, "Statistical Physics". 

7) The index A in the second formula in section 2 (i suggest to add numbers to all formulas) seem to be redundant, including the subsequent comment "The capital Latin indices (𝐴) span the hidden dimension $𝑑_ℎ$". I would simply substitute the letter "d" on top of the sum with $d_h$. 

8) What is the difference between "Absolute" and "Relative" execution time in Section 5.1?  

9) Can the authors add a definition for the batches $b$ in Section 5.2 ?

Typos:

10) Row 144: Cumulant.
11) Row 505: Its communication.

### Questions
I will now present some comments and questions to the authors, aimed exclusively at improving their interesting work about a more effective computation of self-attention in transformers. Comments and questions are listed here below, divided in Major issues, Minor issues and Typos.

Major issues:

1) From Theorem (1), the computational complexity of self-attention, for a single query, is $O( \frac{N}{p} + \log p )$  where $N$ is the full length of the sequence and $p$ is the number of processors. The total complexity is thus quadratic in $N$. There are examples of methods that simplify the total complexity to $O(N)$ (e.g. BigBird, Longformer) or $O(N \log N)$ (e.g. Reformer) which, by the way, do not rely on a modification of the processors disposition and are not necessarily exact. If we assume the number of GPUs to scale as $p = \alpha N$ where $\alpha > 0$, then the complexity per query would scale as $O(\log N )$, hence the total complexity as $O(N\log N)$ which equals the one obtained by Reformer. Nevertheless, even if this scenario appears difficult to reproduce, since $N$ is large by definition, this limit is mentioned in the text (row 269). Could the authors comment on this? 

2) Regarding the experiments reported in Section 5.1. Physical limitations seem to impose that $p = O(1)$, and $p \ll N$. As a consequence, the effective behaviour of the execution time $T$ with respect to $N$ is $T \simeq \frac{N}{p}$, hence it is linear in $N$. On the other hand, when $N$ is fixed, we have $T \simeq  \frac{N}{p} + log(p)$, it should then scale logarithmically with $p$ for large $p$. Can the authors show these trends more clearly from figure (3) e.g. increasing the number of points (in the intermediate range, i.e. between the current minimum and maximum values on the x-axis) and performing a proper fit of the data-points? Moreover: what is the expected scaling of the computational cost of Ring Attention as a function of $(N,p)$ ? It seems from figure (3,b) that the behaviour of $T_{ring}$ as a function of $p$ is linear, while in principle it should be constant and remain $T_{ring} \gg \log p$. If not, please provide for a theoretical argument to explain this behaviour.

3)May the authors show that the formulation of $o$ in line (2) of Algorithm (3) already normalized by $lse$ is equivalent to implementing the formulation from line (4) in Algo (2)? Expanding the mathematical passages in Algo (3) might useful to visualize this aspect.  

4) The difference between the memory costs of Ring and Tree attentions is $\delta_{M} = Mem_{ring} - Mem_{tree} = 2b(\frac{N}{p}\cdot d - n_{h})$. Could the authors check for the scaling of this quantity with respect to $(N,p)$ to satisfy $\delta_{M} \propto \frac{N}{p}$ ? I believe this would make the analysis more rigorous and reliable. 

5) I propose to the authors to add the most recent attempt to map the self-attention mechanism into a energy-based model, i.e. D’Amico et al. 2024, to the Related Work appendix. Nevertheless, i would spend much more space in the same paragraph to mention previous works in the matter of the computational complexity of computing self-attention, even the cases where multiple processors were not employed. A useful review about this problem can be found in Keles et al. 2023.  

Minor Issues:

6) I suggest the authors to substitute the Wikipedia reference for the definition of Helmholtz free-energy with a more reliable and solid scientific source, among the thousand great statistical mechanics books. One example is  Landau, Lifshitz, "Statistical Physics". 

7) The index A in the second formula in section 2 (i suggest to add numbers to all formulas) seem to be redundant, including the subsequent comment "The capital Latin indices (𝐴) span the hidden dimension $𝑑_ℎ$". I would simply substitute the letter "d" on top of the sum with $d_h$. 

8) What is the difference between "Absolute" and "Relative" execution time in Section 5.1?  

9) Can the authors add a definition for the batches $b$ in Section 5.2 ?

Typos:

10) Row 144: Cumulant.
11) Row 505: Its communication.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Tree Attention, an algorithm for parallel self-attention computation across multiple GPUs to reduce communication volume and memory usage. It derives a scalar energy function for self-attention which leads to a Bayesian interpretation and a tree reduction approach for computing self-attention that is asymptotically faster due to parallelization. Experiments show close to 8× speedups on sequences of 5.12 million tokens using 128 GPUs.

### Strengths
1. The proposed algorithm is a novel take on self-attention and the derivation of the energy function and the associated Bayesian interpretation has the potential to contribute to a better theoretical understanding of the efficacy of self-attention in the future.

2. The tree attention algorithm cleverly exploits associativity of $\log\sum\exp$ and $\max$ to create a tree structure for attention computation in decoding that achieves logarithmic complexity as opposed to the linear complexity of prior approaches like ring attention which leads to clear latency improvements in experiments.

### Weaknesses
The details of the derivation of the energy function (for e.g. with the Taylor expansion in (10)) as well as the Bayesian interpretation in 3.2 seem unnecessary and may confuse the reader. If the main goal is to introduce the tree attention algorithm and its advantages, I would recommend making Section 3 more compact and moving things like the Bayesian interpretation to the discussion at the end of the paper.

What is $d_h$ in line 101? Also there seems to be some notation abuse in the expression since it both sums over $A$ and also is apparently performed for all $A$. I think one of those should be 'a'.

How exactly does tree attention save inter node communications and exploit the two-level network topology? Is it by reducing the number of inter-node communications or the data volume of inter-node communications or both?

Why must $k_{\hat{a}'}$ , $v_{\hat{a}'} $ from neighboring devices be stored in ring attention (Page 9, lines 451-454)? Since a copy of $q$ is available at all nodes, won't it be possible to perform ring attention by just computing the flash attention computations at each node to its neighbors which can then rescale and update their attention values? This would reduce both the memory overhead as well as the communication volume ('$t$' factor in (28)) of ring attention

### Questions
1. What is $d_h$ in line 101? Also there seems to be some notation abuse in the expression since it both sums over $A$ and also is apparently performed for all $A$. I think one of those should be 'a'.

2. How exactly does tree attention save inter node communications and exploit the two-level network topology? Is it by reducing the number of inter-node communications or the data volume of inter-node communications or both?

3. Why must $k_{\hat{a}'}$ , $v_{\hat{a}'} $ from neighboring devices be stored in ring attention (Page 9, lines 451-454)? Since a copy of $q$ is available at all nodes, won't it be possible to perform ring attention by just computing the flash attention computations at each node to its neighbors which can then rescale and update their attention values? This would reduce both the memory overhead as well as the communication volume ('$t$' factor in (28)) of ring attention

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
3

### Summary
This paper proposes a new method for improving the performance of self-attention mechanisms used in transformers, especially for long-context sequences. The authors introduce a tree-based method for computing attention, which uses the internal parallelism in the attention operation. This method reduces communication overhead and memory usage across multi-GPU clusters, as compared to existing methods like Ring Attention. The paper establishes a theoretical basis for their approach by deriving an energy function for self-attention and showing how it can be efficiently computed using parallel reductions. Experimental results indicate that Tree Attention achieves up to 8× speedups in long-sequence attention tasks while also halving peak memory usage.

### Strengths
1. The proposed method can effectively scale with the number of GPUs and scales logarithmically.

2. The memory usage of the proposed method can significantly reduce the memory usage.

3. The paper innovatively improve self-attention mechanism by using other related field's knowledge, which is interesting.

### Weaknesses
1. While the paper demonstrates high theoretical and experimental results, it did not provide any real-world deployment or compare with existing frameworks.

2. The system only tests on DGX H100 system, limiting the generalizability to other systems.

3. The paper only compare with self-implemented ring attention, it would be beneficial to compare with more other attention mechanisms like Linformer, Longformer, or performer.

### Questions
Overall, I think this paper proposed a novel self-attention mechanism that scales logarithmically and reduces memory footprints. I have a few comments and questions as follow.

In section 3, the derivation of energy function for self-attention is interesting. What will be comparative analysis between tree attention's use of energy function and other attention mechanism would use this energy function?

As stated in the cons, the paper showed an impressive result compare to ring-based attention. What would be the testing results compare to other different attention mechanism with more aspects like (different hidden sizes, varying GPU numbers)? Also, what will be the memory usage compare to other methods? 

For large distributed clusters (cloud-based GPUs), communication latency is a major concern, and overlapping communication and computation can be tricky. More insights on how Tree Attention manages or mitigates these latencies would provide better clarity for real-world implementations.

The analysis of communication volume is informative, but more practical scenarios could be discussed. For example, how does the communication overhead change when increasing not only the number of GPUs but also the number of nodes?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper addresses the challenge of efficiently computing self-attention in transformer models, which traditionally incurs quadratic complexity in sequence length. The authors propose an approach for parallelizing attention computation using Tree Attention, which leverages the gradient of an energy function. By implementing a tree reduction communication strategy, the proposed approach enables faster parallel decoding and reportedly achieves up to 8x faster performance than Ring Attention, with reduced communication volume and half the memory needed.

### Strengths
The Tree Attention approach accounts for two-level network topology awareness within GPU clusters, which is a practical and well-considered enhancement for real-world distributed computing environments.

### Weaknesses
 - The paper does not clearly explain why using the gradient of the energy function is advantageous for self-attention. This aspect feels insufficiently motivated, making it unclear on the potential contribution. The authors could have strengthened their argument by explaining how this approach uniquely benefits attention computation compared to existing methods.
- The paper claims significant performance improvements over Ring Attention, but it lacks clarity on what specific limitations in Ring Attention are addressed by Tree Attention. Without a clear comparison, it is challenging to understand if Tree Attention fills an existing gap or if it simply provides an alternative approach. 
- The details of the Tree Attention approach are challenging to follow, potentially impacting its accessibility and reproducibility. The method relies on parallel decoding and a tree reduction for attention computation, but the details of these operations are not well explained. Clearer explanations or diagrams could be helpful.

### Questions
- What design aspects of Tree Attention allow it to remain exact, despite the use of parallelized operations? Does the tree reduction introduce any approximations, or is it truly an exact method? This clarification would be valuable for understanding its applicability in tasks where exact attention computation is critical.
- The paper reports an 8x speedup compared to Ring Attention. Could the authors break down what aspects of Tree Attention contribute to this speedup? For example, how much of the improvement is due to, e.g., reduced communication volume by tree reduction?
- Given that Ring Attention is already a sequence parallel method for multi-GPU attention parallelism, what specific limitations does Tree Attention address that Ring Attention?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a new attention mechanism called tree attention. By leveraging tree reduction, it enables high parallelization of the decoding stage during LLM inference, especially for extremely long contexts.

### Strengths
1. This paper includes a microbenchmark of latency and bandwidth between inter-node and intra-node H100 GPUs, highlighting the communication bottleneck.

2. The paper introduces a new approach to designing improved attention mechanisms by considering the system topologies.

### Weaknesses
1. Although this work is called "tree attention," it is not general enough to handle common attention operations. It can only be used when the query has a single token, which limits its usefulness during training and the prefill stage.

2. The implementation of the ring attention baseline might be incorrect. The authors directly use the ring_fwd function from the flash_attn_jax library, which assumes the query, key, and value matrices are already partitioned [1]. Consequently, the actual calculation in this paper's implementation [2] involves a query matrix with P tokens, where P represents the number of workers. This leads to redundant computations, as each worker repeats the same attention calculation on the same query with different key/value partitions, instead of accumulating partial results.

3. Ring attention is not an appropriate baseline for the scenario considered in this work. The purpose of ring attention is to address long-context training, where the query, key, and value matrices are partitioned across workers. To calculate the complete attention map, these matrices need to be communicated, and ring attention provides a better scheduling mechanism to overlap communication and computation. However, in the scenario discussed here—during the decoding stage—the query has only one token and is copied to all workers. Therefore, only the last row of the attention map needs to be calculated, making ring attention unnecessary and inefficient due to redundant computation and communication of the full KV matrices instead of partial results. A more appropriate baseline would involve directly reducing the partial results of attention computation.

4. The idea and algorithm presented are straightforward, but the authors appear to complicate the explanation, which adds confusion rather than clarity.

5. The evaluation only demonstrates a single attention module and lacks end-to-end evaluation on a real-world large language model (LLM), which could weaken the authors’ claims about the algorithm’s effectiveness.

6. The algorithm and code do not utilize a tree topology. If they merely rely on the NCCL library, this approach may lack generalizability, reducing this work's contribution. Furthermore, the reported time complexity in Table 1 appears inconsistent, with O(log n) scaling on H100 and O(n) scaling on MI300X, regardless of the attention mechanism used. This discrepancy needs further explanation and profiling.

### Questions
Please address the issues mentioned in the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2
