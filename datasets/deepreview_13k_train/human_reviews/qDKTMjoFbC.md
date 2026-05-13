# BurstAttention: An Efficient Distributed Attention Framework for Extremely Long Sequences

- Decision: Reject
- Scores: 5, 6, 6, 5, 6

## Abstract
Effective attention modules have played a crucial role in the success of Transformer-based large language models 
(LLMs), but the quadratic time and memory complexities of these attention modules also pose a challenge when processing long sequences. 
One potential solution for the long sequence problem is to utilize distributed clusters to parallelize the computation of attention modules across multiple devices 
(e.g., GPUs). 
However, adopting a distributed approach inevitably introduces extra memory overheads to store local attention results and incurs additional communication costs to aggregate local results into global ones. 
In this paper, we propose a distributed attention framework named ``BurstAttention'' to optimize memory access and communication operations at both the global cluster and local device levels by partitioning attention along the sequence dimension across device.
Through our experiments, we compare BurstAttention with other competitive long-sequence distributed attention solutions. 
The experimental results under different lengths demonstrate that BurstAttention offers significant advantages for processing long sequences compared with these competitive baselines, especially tensor parallelism (Megatron-V3) with FlashAttention, reducing 40\% communication overheads and achieving 1.37 $\times$ speedup during training 128K sequence length on 32$\times$A100.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents BurstAttention, a method for partitioning the attention operation across multiple GPUs in order to process very long sequences. The method combines a global step, which computes attention using a ring-based method and online softmax, with a blocked local attention implementation to take advantage of on-chip cache. The memory, local I/O, and communication costs of BurstAttention are analyzed. Finally, BurstAttention is evaluated experimentally on LLaMA-2 7- and 13-billion parameter models for inference and training performance, where BurstAttention outperforms other methods such as RingAttention.

### Strengths
1. Long sequence lengths are a critical problem for LLMs, and sparse attention mechanisms may not always be sufficient to tackle them. This paper is helping to address this, both in inference and training, by providing a method to decompose the attention computation among multiple GPUs.
2. The combination of the global and local attention optimizations, plus online softmax, enable improved performance in the paper's benchmark results.
3. The benchmark results compare with several existing methods for high-performance attention computation, including FlashAttention and RingAttention.

### Weaknesses
1. The novelty of the paper is unclear. It seems to me that it is essentially a straightforward combination of three existing ideas: RingAttention (Li et al., 2022); online softmax (Milakov & Gimelshein, 2018); and FlashAttention (Dao et al., 2022). Further, the ring-based approach to attention seems essentially to be a variant on classic 1D distributed matrix-matrix multiplication algorithms or Cannon's algorithm with one dimension of the mesh trivial (see, e.g., Golub's "Matrix Computations" book, or the Cannon or Fox algorithm). One could imagine pipelining the distributed attention computation (it is unclear to me whether this paper does this), but then it still seems very similar to SUMMA (Van De Geijn & Watts, 1997).
2. The analysis section seems quite perfunctory. It adequately describes the characteristics of the particular implementation, but does not address optimality. E.g., there are lower bounds for distributed matrix-matrix multiplication (via pebbling and in communication-avoiding algorithms) that could be used. Similarly, FlashAttention includes a lower-bound analysis that might be leveraged here.
3. The experimental evaluation does not include any error bars or measures of variance. Especially since this includes cross-device communication, and BurstAttention introduces additional communication on top of existing methods (e.g., tensor or data parallelism) which may interfere, these are important to include.
4. The experimental section lacks any detailed analysis of the algorithm and includes only end-to-end results. For example, what percent of peak device flop was sustained? How much communication is performed? What is the breakdown in runtime of communication and computation? How well does the local attention optimization perform (e.g., reduction in cache misses)? These sorts of analyses would help inform how BatchAttention performs in different scenarios, what its bottlenecks are, and why, precisely, it is faster than existing methods. (Further, the paper states in Section 1 that BurstAttention "can fully optimize the input-output (I/O) and communication procedures in distributed clusters", yet does not back this claim up.)
5. The evaluation is conducted only up to 8 GPUs which are interconnected via PCIe. This is not especially large scale for training LLMs (although could be reasonable for fine-tuning), and it is not clear how the method will scale.

### Questions
1. Please clarify the novelty of the paper (see above).
2. Can you contextualize the analysis in Section 4 with lower bounds or otherwise provide an indication of how far BurstAttention is from optimal?
3. Please add error bars (or similar) to all experimental results.
4. Please expand the experimental analysis; see above for suggestions.
5. How does BurstAttention scale to larger numbers of GPUs or on different networks?
6. A related point, how does BurstAttention perform when combined with other standard parallelism techniques for training, e.g., data-parallelism/FSDP, pipelining, etc.? Does its additional communication cause interference?
7. In Section 5.3, why fix the batch size to 1 for training? This seems quite small.
8. In Section 5.4, why is a different sequence length used for scaling than is presented in the earlier results? This makes it hard to contextualize the scaling.

-----

In light of the authors' response addressing some of my concerns, I have raised my score. However, I still remain concerned about the novelty and depth of the experiments.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper contributes a new sequence parallelism scheme for attending over long sequences that uses GPU memory hierarchy and distributed ring communication to improve inference and training throughput. The authors show the effectiveness of this method on Llama2-7B for training and inference and Llama2-13B for inference, and show improvements over both TP+FlashAttention, which has lower memory footprint but lower throughput, and RingAttention, which has higher memory footprint and higher throughput. The authors also show that their formulation, which uses local and global attention optimization to improve memory footprint and global communication, maintains exact attention correctness while still bringing these performance improvements.

### Strengths
The paper analysis for training and inference time tradeoff with respect to memory and throughput is solid for causal decoder-only transformer models. The algorithm and communication and memory overhead analysis is also very detailed and thorough for both GAO and LAO.

### Weaknesses
The paper only evaluates two decoder-only models at inference time, and a single small model at training time. The scaling law along the sequence dimension is present but a scaling law along the model capacity dimension is also important given that the dimensionality of the Q/K/V will also increase with model size and therefore the communication and memory overhead as well.

For the tensor parallelism/TP+Flash Attention baselines, is the implementation being used the Megatron-LM implementation which parallelizes each head across devices (and therefore reduces the memory footprint/communication)?

For the time-to-first-token experiment is the sequence length equivalent to the prompt input length e.g. the model generates the first token conditioned on 4096/8192/.../262144 tokens?

### Questions
For the tensor parallelism/TP+Flash Attention baselines, is the implementation being used the Megatron-LM implementation which parallelizes each head across devices (and therefore reduces the memory footprint/communication)? 

For the time-to-first-token experiment is the sequence length equivalent to the prompt input length e.g. the model generates the first token conditioned on 4096/8192/.../262144 tokens?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper aims at processing extremely long sequences in attention under distributed settings. The proposed solution is to partition the computation of attention modules across multiple devices at the sequence dimension, which seems to be an improved version of the prior RingAttention method. Through the proposed global attention optimization using online softmax, the BurstAttention method can reduce the memory usage of intermediate results. In addition, BurstAttention can be integrated with FlashAttention, as the local attention optimization, to further reduce latency and support longer sequences.

### Strengths
- The paper is well-motivated at addressing the memory and communication challenges of processing extremely long sequences in multi-device settings.
- The proposed global attention optimization seems to be an effective extension to RingAttention in reducing memory usage.

### Weaknesses
While integrating two prior methods (RingAttention and FlashAttention) to be more efficient by itself could be a contribution, the paper could elaborate more on the new challenges, if any, and different method designs to establish its new contributions. In particular, the local attention optimization does not seem to bring any new insights than using FlashAttention in a distributed system. The paper does not clearly articulate the specific limitations of applying FlashAttention directly within a distributed context, nor does it detail the modifications or novel aspects introduced to make it suitable for the proposed framework. The description of the local attention optimization lacks the necessary depth to distinguish it from a straightforward application of FlashAttention. It is unclear how the proposed method addresses potential issues such as data synchronization or load balancing across devices when using FlashAttention in a distributed manner. Furthermore, the paper does not provide sufficient details on how the global and local attention mechanisms interact, and the specific challenges that arise from their integration.

### Questions
- Can you comment on the significance of the reduced latency of the first token? How is the implication on overall latency?
- What is the new contribution over FlashAttention? Or simply integrating it into the BurstAttention framework?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents BurstAttention, an efficient distributed attention for long context LLMs.

### Strengths
1. the method is well motivated, well presented and easy to understand.
2. the comparison is throughout and complete.

### Weaknesses
1. The comparison with Megatron is not up-to-date. For instance, Figure 2b does not use the most memory-efficient implementation. The baseline should be set up Megatron-v3 (a combination of tensor model parallelism and sequence parallelism).
2. The latency comparison against Megatron is not well analyzed, see questions below.
3. The argument with sparse attention is vague. There are no experiments.



### Questions
Why table 3 shows such a big improvement against Megatron, are they all resulted from the communication volume? In particular, can the author provides the ablation on the communication wall clock time? (1) the communication volume is less indicative, because of different distributed prototype has different throughput themself. For instance, Megatron uses all-gather, which is highly optimized in NCCL. If the system uses P2P (and is the system using P2P? Can the author provide more details?), even the communication volume is less, the wall clock time can be higher. (2) In the experiment, the objective is causal language modeling, where the system seems to have unbalanced workload, e.g. the machine hosting first query will be idle most of the time. However, in Megatron, the workload is balanced because they do not partition sequences. Does the system balance the workload? If not, the system should be 2x slower than Megatron due to the unbalanced workload?

The reviewer is happy to raise score, if these questions are addressed clearly.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
> **TL;DR:** The proposed BurstAttention algorithm reduces 40% of communication overheads and thus achieves 2x
 speedup during training 32K sequence length. However, the experiments due not include comparisons to some popular distributed algorithms (Data and Pipeline Parallelism). Addressing my concerns (especially W.1. and W.2.) and questions would improve my score.

The paper introduces BurstAttention, an efficient distributed attention framework designed to address the challenges associated with processing long sequences in Transformer-based large language models (LLMs). While attention modules have been essential for the success of LLMs, their quadratic time and memory complexities pose obstacles for long sequences. BurstAttention divides long sequences into partitions across distributed clusters and employs global and local attention optimization strategies to optimize memory access and communication operations. FlashAttention can be viewed as a specialization of BurstAttention on a single device. Experimental results reveal that BurstAttention reduces communication overheads by 40% and achieves a 2× speedup in training on sequences of 32K length with 8×A100 GPUs, outperforming existing competitive distributed attention solutions. BurstAttention is also shown to adapt well to various optimization strategies and offers greater scalability in comparison to other solutions.

### Strengths
* **S.1.** The proposed BurstAttention algorithm tackles an important problem in the computational costs of training and inference of LLMs. 
* **S.2.** The paper is well written, the illustrations are informative, and the algorithms are easy to follow.
* **S.3.** The experimental results show that the  BurstAttention algorithm outperforms existing algorithms, especially for long context windows.
* **S.4.** The experiments are conducted on several model sizes and include ablations for the speedup gains.

### Weaknesses
 * **W.1.** The paper provides comparison to several algorithm, but does not include the common DataParallel and Pipeline Parallelism due to sequence length limitations. As these algorithms are the most popular approaches it would help to show even a single experiments using them as a baseline. It is unclear why these methods could not be applied, as sequence parallelism could be used to overcome length limitations. The lack of this comparison makes it difficult to assess the true advantage of the proposed method.
* **W.2.** The experiments are conducted on a single hardware setup, providing experiments on different configurations would help. The absence of results on diverse hardware, including different GPU architectures (e.g., NVIDIA A100 vs H100) and varying interconnect speeds (e.g., NVLink vs PCIe Gen 4), limits the generalizability of the findings. The performance of distributed algorithms is highly sensitive to these factors, and the paper should explore these variations.
* **W.3.** The paper states that BurstAttention can be easily extended to other cross-attention modules, however, it does not provide any details. Providing additional details would help. The lack of specific details on how BurstAttention can be adapted to different cross-attention mechanisms makes it difficult to evaluate the practical applicability of the proposed method. For example, it is not clear how the partitioning and communication strategies would need to be modified for different attention variants.

### Questions
* **Q.1.** Which PCIe is used in the experiments and what is the bandwidth?
* **Q.2.** How would the experiments look if the communication bandwidth would be higher/lower?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
