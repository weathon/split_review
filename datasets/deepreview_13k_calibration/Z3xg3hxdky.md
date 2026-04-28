# DSP: Dynamic Sequence Parallelism for Multi-Dimensional Transformers

- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 6, 3, 6, 6

## Abstract
Scaling multi-dimensional transformers to long sequences is indispensable across various domains. However, the challenges of large memory requirements and slow speeds of such sequences necessitate sequence parallelism. All existing approaches fall under the category of embedded sequence parallelism, which are limited to shard along a single sequence dimension, thereby introducing significant communication overhead. However, the nature of multi-dimensional transformers involves independent calculations across multiple sequence dimensions. To this end, we propose Dynamic Sequence Parallelism (DSP) as a novel abstraction of sequence parallelism. DSP dynamically switches the parallel dimension among all sequences according to the computation stage with efficient resharding strategy. DSP offers significant reductions in communication costs, adaptability across modules, and ease of implementation with minimal constraints. Experimental evaluations demonstrate DSP's superiority over state-of-the-art embedded sequence parallelism methods by remarkable throughput improvements ranging from 32.2\% to 10x, with at least 50\% communication volume reduction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes to improve the efficiency of multi-dimensional transformers for long sequences via dynamic sequence parallelism (DSP). Unlike the conventional data parallelism, model parallelism, pipeline parallelism, etc. which are designed only within a single dimension and have limited flexibility, DSP can adaptively switch between dimensions and therefore, can minimize the communication overhead. The evaluation results show that DSP can improve the E2E throughput by 10x and at least 50\% communication. The authors also make DSP a user-friendly API that can be easily integrated into the existing transformer training/inference frameworks.

### Strengths
+ This paper targets an important topic -- the low efficiency of transformers on long sequences, and proposes effective solution that yields significant end-to-end throughput improvement;
+ Well written paper with clear logic, the illustration and presentation are helpful for understanding the paper's idea.

### Weaknesses
- The evaluation section can be further elaborated. I assume that authors are evaluating the inference tasks only. If yes, this should be explicitly pointed out. Also, the discussions for DSP on training phase are missing. For example, will DSP affect accuracy or the training convergence cycles? Specifically, how does the dynamic switching between parallelism dimensions impact the gradient aggregation and the overall training stability? The paper lacks a detailed analysis of the potential overhead introduced by the dynamic switching mechanism itself, such as the time spent in decision making and the cost of reconfiguring the parallel execution environment.
- Extending the experiments on more configurations could be beneficial. See questions for details. For example, the paper should explore the performance of DSP with varying model sizes and sequence lengths, and how the performance scales with different numbers of GPUs. It is also important to understand the sensitivity of DSP to different hardware environments, such as different types of GPUs or network interconnects.

### Questions
- How does DSP impact training phase? Will it take longer to converge with DSP?
- How does DSP perform on the larger models with more parameters?
- If the experimental environment changes, for example, with less or more GPUs, how will DSP perform over the other works?
- Will DSP perform better or worse for relatively shorter sequence length?

### Soundness
3

### Presentation
3

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
The paper presents Dynamic Sequence Parallelism (DSP), a novel method to scale multi dimensional transformers with long sequence length efficiently. The proposed solution dynamically switches the parallel computation dimension and minimizes communication costs and enhances adaptability. The experimental results show that communication reduction, and throughput improvement compared to state-of-the-art embedded sequence parallelism methods.

### Strengths
1. The paper is well organized and easy to follow.
2. The illustration with the tensor shape helps the understanding of the proposed solution.
3. Applicability to the emerging ND transformer.
4. Easy to use API design.

### Weaknesses
1. Can you please show the breakdown for communication overhead/actual computation etc?
2. Can you please show the performance with a larger parameter/multi axis model?

### Questions
Please see the weakness section.

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
4

### Summary
This paper presents a method for parallelising the inference computation of multi-dimensional transformers, i.e., transformers that operate on multi-dimensional data such as video streams. In a Multi-GPU setup, the authors argue that it is sufficient to exploit the inter-sequence (e.g., inter-column and inter-row) parallelism available in multi-dimensional data instead of embarking on more advanced methods that can parallelize the processing of a single sequence across several GPUs  (referred to as embedded sequence parallelism in the paper).  The approach proposed by the authors requires all-to-all communication to reshuffle the data across GPUs after processing each dimension. The main argument is that because there is substantial inter-sequence parallelism in multi-dimensional data, there is no need to exploit intra-sequence parallelism, which leads to fewer communication rounds than the approaches that support intra-sequence parallelism.

### Strengths
The experiments demonstrate that exploiting inter-sequence parallelism instead of intra-sequence parallelism leads to significant performance advantages when parallelising multi-dimensional transformers.

### Weaknesses
1) The technical contribution is quite limited. The main contribution of the solution presented appears to be insertion of all-to-all communication rounds to re-arrange the data before switching to a different dimension. This mechanism is similar to 2D FFT processing, where transformations are applied row-wise and column-wise with transpositions in between.
2) The theoretical and the practical comparisons with the methods that focus on intra-sequence parallelism (Megatron-SP, RingAttention, and DeepSpeed-Ulysses) are not fair because:
- These comparison points are not designed to support multi-dimensional data. They are designed to support large single-dimensional sequences. This submission does not necessarily offer better solutions for supporting large single-dimensional sequences, which should be better clarified in the paper.
- The comparison points focus on both training and inference and involve optimisations for reducing the activation memory usage during training. This submission appears to be covering only the inference part without covering any activation memory minimisation techniques, which should be acknowledged in the paper, perhaps in a limitations or discussions section.
- RingAttention can be efficiently implemented on simple ring-like topologies without requiring all-to-all interconnects. It is not fair to assume an all-to-all interconnect and then compare the communication complexity per link (or per device) with a solution that assumes a ring topology, which uses fewer links. It would be great if the authors could clarify their assumptions about the network topology and justify their choice of comparison methods.
- The authors build on some assumptions made in DeepSpeed-Ulysses, which this reviewer believes to be problematic: there is no significant difference between the complexity of all-reduce and all-to-all operations when the underlying topology is all-to-all. Because this submission makes the same assumptions made by DeepSpeed-Ulysses, the communication complexity comparisons given in Table III of this submission are also questionable. In particular, the authors appear to be reporting the total communication volume for Megatron-SP and RingAttention while reporting per-device communication volume for DeepSpeed-Ulysses and their work (DSP).

Furthermore, the results presented do not demonstrate a clear advantage of the proposed method when the spatial sequence length is large. The authors have not provided end-to-end performance measurements for large sequences, making it difficult to assess the practical benefits of their approach. The quadratic complexity of attention mechanisms with respect to sequence length will dominate the execution time for large sequences, and it is unclear if the proposed method can effectively address this issue. The authors also need to clarify that they are evaluating only the inference performance in all their experiments, not just in Figure 7 and Figure 8.

### Questions
Why do the authors compare their work only with the techniques that exploit intra-sequence parallelism? Are there no other techniques for parallelising multi-dimensional transformers? Are there no other techniques for exploiting inter-sequence parallelism? A more comprehensive literature review and comparisons would be very useful. If such techniques do not exist, it would be valuable for the authors to explicitly state this and discuss why their approach is novel in this context.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Dynamic Sequence Parallelism (DSP), a novel approach to sequence parallelism in multi-dimensional transformers. Unlike existing methods that shard along a single sequence dimension, DSP dynamically switches the parallel dimension based on the computation stage, utilizing an efficient resharding strategy that minimizes communication overhead. DSP’s adaptable and easy-to-implement design allows it to operate across various modules without specialized modifications. Experimental results demonstrate DSP's performance advantages over state-of-the-art methods, achieving throughput improvements of 32.2% to 10x and reducing communication volume by at least 50%. The paper’s contributions include a formal definition of DSP, a comprehensive analysis of its communication and memory efficiency, and experimental validations that highlight its scalability and ease of integration with existing distributed frameworks.

### Strengths
Dynamic Sequence Parallelism (DSP) is a novel approach that overcomes limitations of existing sequence parallelism by dynamically switching dimensions based on computation stages, enhancing efficiency in multi-dimensional transformers. The technical foundations are solid, with thorough mathematical definitions and a comprehensive communication and memory analysis that demonstrate DSP’s advantages over state-of-the-art methods. The clarity of the paper is bolstered by well-structured figures, tables, and logical organization, making complex concepts accessible. DSP’s adaptability and scalability in high-dimensional transformer applications make it a significant contribution, with broad relevance for scaling long sequences across various transformer architectures and distributed deep learning systems.

### Weaknesses
The paper could benefit from broader evaluation across additional transformer architectures, including single-dimensional applications, to strengthen its generalizability claims. A deeper analysis of DSP’s computational overhead, particularly with frequent resharding on large-scale setups, would clarify if its efficiency holds consistently as dimensions and devices scale. Specifically, the paper lacks a detailed breakdown of the time spent in resharding operations versus actual computation, making it difficult to assess the practical overhead of dynamic switching. Practical limitations, such as handling global operations involving all sequence dimensions, are briefly mentioned but would benefit from expanded discussion or mitigation strategies. For instance, the paper does not elaborate on how DSP handles operations that require gathering data across all sequence dimensions, which could introduce bottlenecks. More detailed examples of the API and implementation details, especially for integration with popular frameworks, would improve usability for practitioners. The current API description is too high-level and lacks concrete examples of how to implement the `split`, `dynamic_switch`, and `gather` operations within existing deep learning frameworks. Additionally, weak scaling experiments indicate challenges in inter-node communication as GPU counts increase; exploring optimized strategies for inter-node setups could further enhance DSP’s scalability. The paper does not provide sufficient detail on the specific communication patterns and bottlenecks encountered in inter-node scenarios, making it hard to evaluate the practical scalability of DSP in large distributed environments.

### Questions
How does the resharding process impact performance in practice, especially as the number of GPUs or sequence dimensions increases? Quantifying the computational or memory overhead of these operations would clarify DSP’s efficiency as scales grow and reveal any potential trade-offs.

Appendix A.4 briefly introduces the API, but more detailed examples, including guidance for integrating DSP with popular frameworks like TensorFlow or JAX, would be helpful. Could you add further explanation on API usage and potential challenges in integrating DSP across different environments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The paper presents Dynamic Sequence Parallelism, a approach for scaling multi-dimensional transformers efficiently. DSP dynamically switches the parallel dimension between computation stages using a resharding strategy, which reduces communication overhead and simplifies implementation. DSP provides substantial performance improvements over existing sequence parallelism methods, such as Megatron-SP and DeepSpeed-Ulysses, achieving higher throughput (32.2% to 10x increase) and reducing communication volume by up to 75%.

### Strengths
++ The paper targets important problem for multi-dimensional transformers scalability.

++ The proposed approach effectively reduced communication overhead.

### Weaknesses
-- The overhead associated with resharding in DSP is not clear. Specifically, the computational cost of the resharding operation itself, including any necessary data movement or re-indexing, is not well-defined. Furthermore, the memory footprint implications of dynamically changing data layouts, such as potential memory fragmentation or increased memory usage due to temporary copies, are not sufficiently addressed. It is also unclear how the resharding overhead scales with increasing sequence lengths or a larger number of GPUs, which is crucial for the practical applicability of the method.

-- The paper mentions altering sequence parallelism between computation stages, but it is unclear under what specific circumstances or computations this alteration becomes necessary. The description lacks concrete examples of when and why switching between different sequence parallelism strategies is required. The paper does not provide a clear explanation of the criteria used to determine when a change in parallelism strategy is beneficial or necessary, making it difficult to assess the general applicability of the approach.

### Questions
DSP requires data resharding between stages, which means that the memory layout of data changes dynamically. This process can complicate memory management and may lead to increased memory fragmentation or inefficient memory use. How to solve this case in the proposed appraoch?

Could the authors provide more details on the computational and memory overhead associated with the resharding operation in DSP? How this overhead scales with an increasing number of GPUs or longer sequences?

The paper mentions altering sequence parallelism between computation stages, but it is unclear under what specific circumstances or computations this alteration becomes necessary. Could the authors clarify when and why it is necessary to change the sequence parallelism strategy between different stages of computation?

### Soundness
3

### Presentation
2

### Contribution
3
