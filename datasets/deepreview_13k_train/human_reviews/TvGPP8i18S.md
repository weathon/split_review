# MELODI: Exploring Memory Compression for Long Contexts

- Decision: Accept
- Scores: 5, 8, 6, 6

## Abstract
We present \melodi, a novel memory architecture designed to efficiently process long documents using short context windows. The key principle behind \melodi{} is to represent short-term and long-term memory as a hierarchical compression scheme across both network layers and context windows. Specifically, the short-term memory is achieved through recurrent compression of context windows across multiple layers, ensuring smooth transitions between windows. In contrast, the long-term memory performs further compression within a single middle layer and aggregates information across context windows, effectively consolidating crucial information from the entire history. Compared to a strong baseline - the Memorizing Transformer employing dense attention over a large long-term memory (64K key-value pairs) - our method demonstrates superior performance on various long-context datasets while remarkably reducing the memory footprint by a factor of 8.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a new context compression neural network for the long context in today's LLMs. With a hierarchical structure, it achieved a decent performance by reducing the memory footprint by a factor of 8.

### Strengths
1. The methodology seems novel and makes a lot of sense in dividing the tasks into long term and short term memory in the compression.
2. The empirical results seem promising.

### Weaknesses
1. Without prior knowledge, it's not clear that how the memory network works with the LLMs and this is also not reported as preliminary knowledge.
2. The results only show the efficiency part and do not show the effect of memory network on the performance of LLM.
3. Codes are not shared for checking the implementation.

### Questions
1. A preliminary session about the history of recent advances about memory compression would be much appreciated.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
MELODI is a novel memory architecture designed to efficiently process long documents using short context windows. MELODI is a hierarchical compression scheme for both short-term and long-term memory.

The Short-Term Memory uses a Multi-Layer Recurrent Compression Scheme which is distributed across multiple short-term layers, this mechanism progressively compresses context tokens and prior memory at each layer. It is asserted that this ensures smooth transitions between context windows and aggregates information across them. Each short-term layer: (1) Transforms context tokens via a transformer block and (2) Recurrently compresses the current context window into short-term memory *tokens*. Summary tokens are introduced to facilitate inter-layer communication within the short-term memory. Distinct linear token mixers are used to generate separate summary tokens for the next layer and short-term memory tokens for the next window, enabling divergent compression flows.

The Long-Term Memory is a Single-Layer Module which Memorizes Compressed Key-Value Pairs. It uses a single network layer and maintains a record of the entire history by further compressing each context window and stacking them. The claim is that this addresses the forgetting issue inherent in short-term memory due to limited capacity. Key-value (KV) pairs of long-term tokens are stored in a FIFO queue, ensuring the retention of a substantial portion of the recent history. The long-term layer introduces a long-term memory component and enables cross-attention between current context/summary tokens and the long-term memory. It employs a gating mechanism to combine self-attention and cross-attention results. It uses a linear token mixer to generate compressed KV pairs for the current window, which are then appended to the long-term memory.

The overall MELODI Architecture utilizes a "sandwich" structure with a long-term compression layer inserted between multiple recurrent short-term compression layers. It appears to demonstrate strong performance on various long-context datasets while significantly reducing memory usage compared to baselines like the Memorizing Transformer. Ablation studies appear to confirm the complementary roles of short-term and long-term memory, highlighting their synergistic contribution to an efficient and effective memory architecture.

Compared to LSTMs, which operate at the token level, MELODI focuses on memory management at the context window level. Unlike Transformer XL, which relies on caching KV pairs from the preceding window, MELODI employs a multi-layer recurrent compression for short-term memory. While similar to the Memorizing Transformer in using a dedicated memory layer, MELODI stores compressed KV pairs, leading to a substantial reduction in memory size.

### Strengths
Originality
This paper combines and extends ideas from previous works on memory mechanisms for language models. It integrates both short-term and long-term memory into a unified architecture, leveraging compression techniques inspired by LSTMs, Transformer XL, and Memorizing Transformer. The paper introduces a new hierarchical compression scheme for representing short-term and long-term memory. This scheme differentiates MELODI from previous approaches by employing recurrent compression across multiple layers for short-term memory and further compression within a single middle layer for long-term memory. The paper introduces a summary branching mechanism that uses linear token mixers to generate separate summary tokens for different purposes (next layer and next window). This contributes to the originality of the approach by enabling distinct compression flows within the short-term memory.

Quality
The paper presents comprehensive experimental results on three long-context datasets, demonstrating that MELODI outperforms several strong baselines (Transformer XL, Block Recurrent Transformer, and Memorizing Transformer) in terms of perplexity while significantly reducing memory usage. The paper conducts detailed ablation studies to analyze the impact of various design choices, including the sizes of short-term and long-term memory, long-term memory coverage, context window size, the number of short-term and long-term layers, and summary branching. These studies provide good evidence supporting the effectiveness and efficiency of MELODI's architectural choices.

Clarity
The paper is well-written and easy to follow. The authors present the motivation, architecture, and experimental results in a clear and concise manner. The paper uses several figures to effectively illustrate the key concepts and architectural components of MELODI. These figures significantly aid in understanding the hierarchical compression scheme and the flow of information within the model.  The authors provide detailed explanations of the various components of MELODI, such as the short-term and long-term layers, summary branching, and the gating mechanism used in the long-term layer. 

Significance
The paper tackles the important problem of efficiently processing long documents with transformer language models. This is a significant challenge because the quadratic complexity of attention mechanisms makes it computationally expensive to handle long sequences directly.
The proposed method has practical implications for various real-world applications that involve processing long texts, such as document summarization, question answering, and machine translation. MELODI's efficiency and effectiveness in handling long contexts could lead to improved performance and reduced computational costs in these areas. The paper does point to some new avenues for future research in memory architectures for language models. The hierarchical compression scheme and the use of summary branching could inspire further investigations into efficient and effective ways to manage information over extended sequences. Additionally, the authors acknowledge the limitation of their current work in addressing the fine-tuning of pre-trained models and suggest exploring adaptation techniques like LoRA fine-tuning in future work.

### Weaknesses
(1) The paper has only a limited exploration of longer context window size
The primary focus and the majority of the experiments revolve around a context window size of 512 tokens. This emphasis on relatively short context windows might limit the applicability of the method to tasks requiring significantly longer contexts, such as those involving very long documents or those benefiting from processing larger chunks of information simultaneously. The paper could be strengthened by conducting more extensive experiments with larger context window sizes, particularly those exceeding 2048 tokens or, ideally experiments in the 10k token regime. This would provide a better understanding of MELODI's performance and scalability in handling truly long contexts. Exploring how the model's memory capacity and compression mechanisms need to be adjusted for optimal performance with varying context lengths would be valuable. Figure 5 could be highlighted, discussed and presented more clearly and explicitly in terms of the long context issue. It seems this experiment does give perplexity numbers for 192x64=12k token context windows, but it is a bit hidden amongst the rest of the experiments given the importance of these longer regimes.

(2) There appears to be a lack of fine-tuning experiments
MELODI and the baselines, seem to have been trained from scratch. The paper doesn't explore the performance of MELODI when fine-tuned on a pre-trained language model. While most LLMs are derived from a larger pre-trained model, this is only a minor limitation given the amount of resources needed to train a SOTA grade LLM.  Investigating the adaptability of MELODI to be applied in fine-tuning scenarios would be beneficial. This could involve exploring techniques like LoRA (Low-Rank Adaptation) to integrate the short-term and long-term memory mechanisms into pre-trained models without significantly increasing the number of trainable parameters. Evaluating the performance of fine-tuned MELODI models on downstream tasks would provide insights into its effectiveness in practical applications. This is mentioned as possible future work.

(3) Limited Analysis of Computational Efficiency
More analysis and discussion of Memory Usage and Computational Time or computational complexity would be helpful. The paper could potentially benefit from discussions and comparisons of training and inference times for MELODI and the baselines

(4) Experiments are almost exclusively performed providing test set perplexity results. While there are many downstream tasks that could benefit from models yielding better perplexity, it would be more compelling to see the impact on other kinds of tasks and metrics where long range information is important.

### Questions
Suggestion: Could you provide some more experimental results in the 2k and larger token context regime?
Questions: Could you elaborate on any particular challenges and potential solutions for scaling MELODI to handle even larger context windows, such as 4096 or 8192 tokens, which are becoming increasingly common in language modelling? 
Is the key issue "just" the size of the GPUs / TPUs that you/one has access to, or could you provide more (concise) insights on this point?

Could you provide a discussion and/or analysis of MELODI's computational efficiency, including complexity analysis or measurements and comparisons of training and inference times compared to baseline models? Latency is an issue in real world situations and it would be useful for the reader to understand the inference time implications here.

The paper highlights the potential of MELODI for various natural language processing applications, such as document summarization, question answering, and machine translation. Have you considered conducting preliminary experiments on any of these downstream tasks to demonstrate the practical benefits of MELODI in specific applications?  With those kinds of experiments and answers to the questions above I could potentially score this paper higher.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel Transformer-based architecture, MELODI, which combines multiple short-term context window (recurrent + chunk-wise) Transformer layers with a single long-term compression layer. Experimental results show that MELODI achieves the lowest perplexity compared to similar memory-based Transformer variants. In addition, the paper presents ablation studies exploring various combinations of architectural components.

### Strengths
* The integration of long and short memories is a straightforward yet effective strategy. The paper clearly illustrates the concept through well-written explanations and clear visualizations.

### Weaknesses
 * The experiments mainly focus on perplexity comparisons, rather than evaluating the performance on long-context benchmarks such as LongBench or Needle-in-a-Haystack (NIH).
* The paper lacks discussion regarding the challenges in training the model; the recurrent nature of the model may impede efficient parallel training. Can you provide more detailed explanations?
* Although the model is Decoder-only, it is unclear how the chunk-wise approach affects token-wise generation behavior (a key mechanism in GPT-like LLMs). Does summary-generating action occur only after completing each chunk during the generation phase?
* The model appears to be relatively small, raising questions about the scalability of the architecture. Details regarding the model size (e.g., 1B, 2B?) and the model’s potential for scaling up would enhance the paper’s value.

### Questions
* It would be beneficial to provide the upper bound, such as a very long-context Transformer model (ex: 256K or more) for readers to get a sense of the performance gap.
* Suggestion: It would be interesting to compare MELODI with YOCO [1], which employs a similar long-short strategy. I understand that [1] is a very recent paper and you do not need to compare the work; it would be valuable to share your thoughts on the similarities and differences. [1] You Only Cache Once: Decoder-Decoder Architectures for Language Models, 2024.

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
2

### Summary
This paper presents MELODI, a memory architecture for efficient long document processing. It utilizes a hierarchical compression scheme, where the short-term memory performs recurrent compression of context windows, and long-term memory aggregates information from the entire history. Experimental results indicate superior performance along with a reduction in memory footprint.

### Strengths
1. The writing is clear and fluent.
2. Experimental results are promising, demonstrating an improvement in performance while simultaneously reducing memory usage.

### Weaknesses
1. The baselines are old. Some related methods are not discussed or compared.
2. Some experimental details are not provided. For example, how to choose the M, and how to evaluate the memory footprint.
3. For Figure 8, with the number of long-term memory layers increasing, the perplexity is reduced. So a single layer may not be sufficient.

### Questions
1. Could you add some latest methods, e.g. [1], to related works and baselines?  
2. Could you provide more details about the experiments, e.g. how to choose the M, and how to evaluate the memory footprint?
3. There is only one long-term layer in the proposed method, which may not be sufficient to model long-term memory. As shown in Figure 8, could you conduct experiments with more long-term memory layers?

[1] Wang, Weizhi, et al. "Augmenting language models with long-term memory." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
3

### Presentation
3

### Contribution
2
