# AutoChunk: Automated Activation Chunk for Memory-Efficient Deep Learning Inference

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 5

## Abstract
Large deep learning models have achieved impressive performance across a range of applications. However, their large memory requirements, including parameter memory and activation memory, have become a significant challenge for their practical serving. While existing methods mainly address parameter memory, the importance of activation memory has been overlooked. Especially for long input sequences, activation memory is expected to experience a significant exponential growth as the length of sequences increases. In this approach, we propose AutoChunk, an automatic and adaptive compiler system that efficiently reduces activation memory for long sequence inference by chunk strategies. The proposed system generates chunk plans by optimizing through multiple stages. In each stage, the chunk search pass explores all possible chunk candidates and the chunk selection pass identifies the optimal one. At runtime, AutoChunk employs code generation to automatically apply chunk strategies. The experiments demonstrate that AutoChunk can reduce over 80% of activation memory while maintaining speed loss within 10%, extend max sequence length by 3.2x to 11.7x, and outperform state-of-the-art methods by a large margin.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers the memory consumption during inference of large deep neural networks on long input sequences. To reduce the activation memory, the paper proposes an adaptive compiler to automatically configure chunking strategies.

### Strengths
- The paper tackles an important issue that is becoming increasingly relevant as model sizes continue to grow.

- The empirical evaluation of the proposed method appears thorough.

### Weaknesses
 - The paper employs substantial jargon and undefined terms. For readers who are not deeply familiar with the topic, sections of the paper are somewhat difficult to comprehend. For instance, it is unclear what portion of activation memory is contained within a chunk. Specifically, the paper does not clearly define what constitutes a 'chunk' in the context of activation memory. Is it a fixed-size block of memory, or does its size vary depending on the layer or operation? Furthermore, the paper uses terms like 'splitting dimensions' without clearly explaining how this is implemented at the hardware level or how it interacts with the underlying computation graph. The lack of clarity around these core concepts makes it difficult to assess the practical implications of the proposed method.

- The ablation study is arguably somewhat restricted in scope. The paper does not explore the sensitivity of the proposed method to various hyper-parameters, such as the chunk size or the search space for the dynamic programming algorithm. It would be beneficial to see how the performance of the method varies under different configurations. Additionally, the ablation study should include a comparison with other chunking strategies, such as fixed-size chunking or heuristic-based chunking, to better understand the advantages and limitations of the proposed adaptive approach.

### Questions
How does the splitting across points inside a batch work?
How exactly does the dynamic programming approach work to solve Equation 11?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors define a formal model for breaking up neural net computations into chunks and sequentially executing them to save on memory footprint. They then formulate it as a search space optimization problem and provide an efficient search algorithm. They show that sequential execution of chunks on a limited set of ops is sufficient to provide good memory use gains while keeping overhead low.

### Strengths
- By formalizing the definition of legal chunk flows and providing a cost function, AutoChunk turns a programmer intuition ("certain computations can be sequentialized to save space") into an computational optimization problem. This breaks down of a lot of barriers to entry. Wrapping everything up into a single function call that statically optimizes a compute graph is a testament to just how end-to-end the authors have made their solution.
- Dimension slicing and tiling normally has a stupidly large optimization space. The authors provide several straightforward and effective means for reducing that space to a tractable size and then show that DP is sufficient to get good results.
- The observations on the need for sequential chunking across all operators (fig 4) is useful in understanding the intuition behind why overhead can be kept low. This is generally helpful beyond just its applicability to chunking (even if it has been observed before).
- I appreciated the measure of effectiveness in the presence of other memory optimization (i.e.- fused kernels). Often times, memory optimizations (sparsification, pruning, compression, etc.) partially or fully cannibalize each others benefits when used in conjunction. Good to see these play nicely together.

### Weaknesses
 - The paper uses a *lot* of bespoke jargon and sometimes uses terms before they are formally introduced. For reference, the following terms are used with the form "chunk ___": flow, region, dimension, size, search, space, setting, selection, formulation, strategy, plan, candidate. If I don't read the word "chunk" again for a while, I'll be happier for it.
- The benefits of AutoChunk vs. expert plans are a bit middling. This is less a weakness of AutoChunk's algorithm and more an observation that the expected benefits from AutoChunk will come from *unchunked* models rather than those already using a chunking strategy. In other words, AutoChunk is more useful when spreading the benefits of chunking to a broader set of models rather than improving on those that already use it. The paper's evaluation focuses on a single model (AlphaFold) that already employs a sophisticated chunking strategy, making it difficult to assess the true potential of AutoChunk in scenarios where no such strategy exists. This limits the impact of the results, as the most significant gains from AutoChunk are likely to be seen in models that currently do not use any form of memory optimization via chunking.

### Questions
- While activation memory is generally correlated with model complexity, chunkable activations seem heavily dependent on the model type. Obviously the models chosen for evaluation in the paper are amenable (which is not a strike against the work---these models are relevant and important). Can the authors give some intuition or generalizations on the classes of neural net architectures that fail to chunk nicely (vs those that do)?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
When serving large-scale deep learning models, their memory requirements are one of the major hurdles. Unlike the parameter memory, optimizations for the activation memory have not been much studied. Since the activation memory is variable depending on the context length, it is important to reduce the activation memory pressure for long context inference. In this research, the authors propose AutoChunk, an automatic compiler system that finds an efficient execution plan with low activation memory pressure. Their evaluation results show that AutoChunk can reduce 50~60% activation memory without speed loss, or 80% activation memory while maintaining speed loss within 10%.

### Strengths
- The paper suggests an important problem; optimizing the activation memory because the context length is rapidly increasing.
- Unlike the existence of DL compilers related to parallel execution, the paper presents a new type of DL compiler.

### Weaknesses
 - Little bit unclear how "activation memory" is measured. Unlike training, we can reuse memory in inference. For example, the MLP module of the Transformer layer has the following structure (not assuming gated linear).
  ```
  Y = UP_PROJ(X)
  Z = DOWN_PROJ(Y)
  ```
  In this case, X and Z can use the same memory region. Did the paper consider such a characteristic? It is confusing because Figure 4 shows the activation memory distribution of each node.
- More analysis for experiments will be helpful. For example, what is a chunking strategy that AutoChunk finds for the GPT model in Figure 5? For now, it is just a black-box compiler.
- For the GPT model, if AutoChunk can reduce the activation memory by half, we can allocate more memory for the key-value cache. It will lead to an end-to-end throughput increase. Are there any results about this? The first paragraph of Section 4 says that the prefill stage is assumed for the GPT case.

### Questions
- Could you explain the reason why AutoChunk can even accelerate inference for AlphaFold (B=4, S=512) and UNet (B=1, S=192) cases?
- Is batch dimension also considered as a candidate for chunking? If so, should we run the search algorithm for every execution? It might incur runtime overhead.
- How long does AutoChunk take to search chunking strategy?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
