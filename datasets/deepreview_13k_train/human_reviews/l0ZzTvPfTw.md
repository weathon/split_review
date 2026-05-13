# FlashRNN: I/O-Aware Optimization of Traditional RNNs on modern hardware

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
While Transformers and other sequence-parallelizable neural network architectures seem like the current state of the art in sequence modeling, they specifically lack state-tracking capabilities. These are important for time-series tasks and logical reasoning. Traditional RNNs like LSTMs and GRUs, as well as modern variants like sLSTM do have these capabilities at the cost of strictly sequential processing. While this is often seen as a strong limitation, we show how fast these networks can get with our hardware-optimization FlashRNN in Triton and CUDA, optimizing kernels to the register level on modern GPUs. We extend traditional RNNs with a parallelization variant that processes multiple RNNs of smaller hidden state in parallel, similar to the head-wise processing in Transformers. To enable flexibility on different GPU variants, we introduce a new optimization framework for hardware-internal cache sizes, memory and compute handling. It models the hardware in a setting using polyhedral-like constraints, including the notion of divisibility. This speeds up the solution process in our ConstrINT library for general integer constraint satisfaction problems (integer CSPs).
We show that our kernels can achieve 50x speed-ups over a vanilla PyTorch implementation and allow 40x larger hidden sizes compared to our Triton implementation. We will open-source our kernels and the optimization library to boost research in the direction of state-tracking enabled RNNs and sequence modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces FlashRNN, which optimizes traditional RNNs on modern GPUs. It divides RNNs into smaller pieces and parallelize over it to increase efficiency on GPUs. The model auto-adjusts its internal cache settings using a constraint satisfaction problem solver, enabling further performance optimization based on hardware. The experimental results show that the proposed solution is 50x faster than a vanilla PyTorch implementation.

### Strengths
- The paper is easy to follow and well organized.
- Hardware aware fine tuning
- Comprehensive benchmarking

### Weaknesses
 - The paper emphasizes the register level CUDA optimization. It'd be great if the authors can show how the implementation is close to the roofline through profiling.
- I believe comparing to pytorch is not fair as pytorch has overhead to launch its internal CUDA kernel.
- Several fusion can be achieved through compilation. How is it different? Also, not using compilation seems to be unfair comparison.
- Why FlashAttention2 matters in the RNN?

### Questions
Please see the weakness section above.

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
While Transformers are state-of-the-art in sequence modeling, they lack state-tracking abilities. RNN families, like LSTMs and GRUs, can perform state tracking but at the expense of sequential processing. To address this, this paper introduces FlashRNN, which optimizes kernel operations to leverage GPU registers and SRAM. Additionally, it incorporates ConstrINT, an auto-tuning optimization tool that operates under hardware constraints, such as cache and memory limits, by solving an integer constraint satisfaction problem. Experimental results demonstrate the effectiveness and efficiency of FlashRNN.

### Strengths
+ Hardware-aware optimization for accelerating RNN model training and inference is promising.
+ It claims that FlashRNN will be open-sourced, which helps further research in this direction.

### Weaknesses
 - Certain critical procedures are somewhat unclear and would benefit from further clarification.
- The experimental section could be strengthened with additional details and improvements.
- The interaction between ConstrINT and other components in FlashRNN is somewhat unclear. Providing an overall architecture or workflow for FlashRNN would be helpful.
- Algorithm 5.1 outlines the kernel fusion procedure but lacks a detailed explanation. A further illustration of this algorithm would be beneficial.
- In Algorithm 5.1, line 242 mentions “Load RtbgsR_{tbgs}Rtbgs​, BtgB_{tg}Btg​ to registers and SRAM.” How many registers and how much SRAM can be used for storing these values? Utilizing all available registers and SRAM may not be ideal, as they may also be needed for storing intermediate results during computation. If this strategy is used, it could impact performance. Detailed clarification is needed.
- Line 299 states that multiple heads are computed in parallel in different programs without synchronization. Could this lack of synchronization impact accuracy?
- Lines 301 to 303 indicate that custom caching strategies cannot be applied due to restrictions on GPU register access in Triton. Is there a significant gap between the intended design in Algorithm 5.1 and the Triton implementation? How large is this gap?
- Line 310 mentions that FlashRNN pads with zeros to support small batch sizes, at the cost of efficiency. How much efficiency is lost due to this padding?
- The evaluation setup is somewhat confusing. Are all four backends (CUDA fused, CUDA alternating, Triton fused, and Vanilla PyTorch) being compared with the two baselines, FlashAttention2 and nn.LSTM? If so, it appears that FlashRNN’s performance is lower than the baselines in most configurations shown in Figures 1 to 4. Additionally, why is FlashRNN compared with FlashAttention2?
- In the experiments, lines 467 to 468 mention replacing attention blocks with FlashRNN LSTM for speed comparisons. Does this substitution provide a meaningful comparison?
- None of the experiments include accuracy comparisons, which appears to be a limitation.

### Questions
1. The interaction between ConstrINT and other components in FlashRNN is somewhat unclear. Providing an overall architecture or workflow for FlashRNN would be helpful.
2. Algorithm 5.1 outlines the kernel fusion procedure but lacks a detailed explanation. A further illustration of this algorithm would be beneficial.
3. In Algorithm 5.1, line 242 mentions “Load RtbgsR_{tbgs}Rtbgs​, BtgB_{tg}Btg​ to registers and SRAM.” How many registers and how much SRAM can be used for storing these values? Utilizing all available registers and SRAM may not be ideal, as they may also be needed for storing intermediate results during computation. If this strategy is used, it could impact performance. Detailed clarification is needed.
4. Line 299 states that multiple heads are computed in parallel in different programs without synchronization. Could this lack of synchronization impact accuracy?
5. Lines 301 to 303 indicate that custom caching strategies cannot be applied due to restrictions on GPU register access in Triton. Is there a significant gap between the intended design in Algorithm 5.1 and the Triton implementation? How large is this gap?
6. Line 310 mentions that FlashRNN pads with zeros to support small batch sizes, at the cost of efficiency. How much efficiency is lost due to this padding?
7. The evaluation setup is somewhat confusing. Are all four backends (CUDA fused, CUDA alternating, Triton fused, and Vanilla PyTorch) being compared with the two baselines, FlashAttention2 and nn.LSTM? If so, it appears that FlashRNN’s performance is lower than the baselines in most configurations shown in Figures 1 to 4. Additionally, why is FlashRNN compared with FlashAttention2?
8. In the experiments, lines 467 to 468 mention replacing attention blocks with FlashRNN LSTM for speed comparisons. Does this substitution provide a meaningful comparison?
9. None of the experiments include accuracy comparisons, which appears to be a limitation.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper optimizes traditional RNNs on GPUs. They introduce optimized kernels and an optimization framework. One challenge for efficient and scalable implementations that the authors tackle is the requirement of strict sequential processing of RNNs. They introduce a parallelization variant that processes multiple RNNs of smaller hidden state in parallel, inspired by the head-wise processing in transformers. They implement two variants, an alternating version switching between point-wise and matrix-multiplication kernels and a fused implementation, optimizing memory transfers while using hardware-optimized matrix-multiplication. The second leads to a further 3-4x speed-up over the alternating option for small batch sizes. Their kernels can achieve 50x speed-ups over a vanilla PyTorch implementation and allow 40x larger hidden sizes compared to their Triton implementation. 
To enable flexibility on different GPU variants, they also introduce an optimization framework for hardware-internal cache sizes, memory and compute handling.

### Strengths
- The paper is overall well-written, uses clear language and structure. 
- it tackles an important problem of overcoming a fundamental limitation important for further scaling rnns. This would enable state-intensive tasks where state continuity and stepwise dependency matter, which might be less naturally handled by Transformers
- They compare to relevant Backends (e.g., cuDNN)

### Weaknesses
They mention the HASTE library and that they overcome their limitations. However, I think they don't benchmark directly against HASTE which would be relevant.

### Questions
Can you elaborate on the similarities and differences of the HASTE implementation and your approach. Did you benchmark against HASTE? If not, why not?

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
FlashRNN is a hardware-optimized library that significantly accelerates traditional RNNs, like LSTMs and GRUs, using optimized kernels for GPUs. The paper introduces kernel-level optimizations that fuse matrix multiplications and activation functions, achieving up to 50x speed-ups compared to standard implementations. FlashRNN also supports parallel processing through a "multi-head" approach and uses the ConstrINT framework to model hardware constraints. This library enables faster and more efficient RNN performance, particularly in state-tracking tasks.

### Strengths
FlashRNN offers performance improvements by focusing on kernel fusion techniques that optimize LSTM and GRU operations on modern GPUs. The library’s focus on fusing matrix multiplication and activation functions into a single operation significantly reduces memory access overhead, a critical bottleneck in memory-bound computations. The integration of the ConstrINT framework for hardware-aware optimization ensures that the method adapts well to various GPU architectures. Additionally, the open-source nature of FlashRNN encourages further exploration and development in state-tracking tasks, where RNNs still excel. The paper’s effort to justify LSTM optimization versus Transformers provides valuable insight into the relevance of RNNs in certain domains.

### Weaknesses
FlashRNN has some limitations, particularly in its use cases, as its advantages are more pronounced for state-tracking tasks and less clear for applications where parallelizable models like Transformers excel, which may limit its broader appeal. Additionally, its focus on GPU-based optimizations reduces its applicability for users working with other hardware, such as TPUs or CPUs. Despite performance improvements, RNNs still face inherent scalability issues due to sequential processing, and FlashRNN doesn't fully address the parallelization advantage held by Transformers. Lastly, the paper notes numerical precision differences in training compared to implementations like PyTorch's cuDNN, which may need further investigation. The performance gains are primarily demonstrated on training tasks, and it is not clear how well these optimizations translate to inference scenarios, particularly given the different memory access patterns and computational requirements between training and inference. Furthermore, the paper does not fully explore the limitations of the proposed approach when dealing with very long sequences, which are known to be problematic for traditional RNNs due to vanishing gradients and memory constraints.

### Questions
A few questions and feedback:

Was the profiling conducted with torch.compile optimizations? Have you considered trying TVM auto-tuning for further optimization?

Since LSTM's arithmetic intensity is mostly memory-bound, the proposed method seems to focus primarily on fusion operations. It’s unclear if other techniques to tackle bandwidth bottlenecks for inference were explored. Given that Transformers were specifically designed to overcome LSTM limitations, this aspect could use more clarification.  The paper would benefit from a more detailed comparison of computational complexity scaling between FlashRNN and Transformers, particularly how each scales with respect to input size and hidden states.

While it’s good that the paper addresses why LSTM optimization remains relevant compared to Transformers, it is not fully convincing why FlashRNN would outperform FlashAttention or how FlashRNN differs fundamentally from applying FlashAttention-like methods to RNNs. 

Has the method been tested on GPUs with less SRAM? It would be valuable to understand how FlashRNN performs in environments with different hardware constraints. What are the options if the weight matrix (W) cannot be cached? Addressing this scenario would help clarify how the method adapts to different hardware limitations.

### Soundness
3

### Presentation
2

### Contribution
2
