# Generative Representational Instruction Tuning

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
All text-based language problems can be reduced to either generation or embedding. Current models only perform well at one or the other. We introduce generative representational instruction tuning (\method{}) whereby a large language model is trained to handle both generative and embedding tasks by distinguishing between them through instructions. Compared to other open models, our resulting \modelbase{} sets a new state of the art on the Massive Text Embedding Benchmark~(MTEB) and outperforms all models up to its size on a range of generative tasks. By scaling up further, \modelbig{} outperforms all open generative language models that we tried while still being among the best embedding models. Notably, we find that \method{} matches training on only generative or embedding data, thus we can unify both at no performance loss. Among other benefits, the unification via \method{} speeds up Retrieval-Augmented Generation (RAG) by >~60\% for long documents, by no longer requiring separate retrieval and generation models. Models, code, etc.
\begin{figure*}[htbp]
    \centering
    \begin{center}
        \includegraphics[width=0.96\textwidth]{figures/performance.pdf}
        \caption{\textbf{Performance of various models on text representation (embedding) and generation tasks.} \model{} is the first model to perform best-in-class at both types of tasks simultaneously.}
        \label{fig:performance}
    \end{center}
\end{figure*}

\begin{figure*}[htbp]
    \centering
    \begin{center}
        \includegraphics[width=\textwidth]{figures/octopus.pdf}
        \caption{\textbf{\method{}.} The same model handles both text representation and generation tasks based on the given instruction. For representation tasks, instructions ideally contain the target \colorbox{olive}{domain}, \colorbox{mikan}{intent}, and \colorbox{gold}{unit}~\cite{asai2022taskaware}. The representation is a tensor of numbers, while the generative output is text.} 
        \label{fig:octopus}
    \end{center}
\end{figure*}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents generative representational instruction tuning (GRIT), a unified model for embedding and generative tasks in text. GRIT learns embedding representations with a bidirectional attention followed by mean pooling and a instruction tuning with causal attention. The experiments show that GRITLM outperforms various prior open models on the MTEB benchmark and matches the performance of several instruction tuning models. Furthermore, the unified model speeds up retrieval augmented generation by 60%.

### Strengths
- The paper is very well written. It is easy to follow the main motivation of the paper. The related work positions the paper well. 
- The paper presents large-scale experiments. The model matches the performance of strong baselines on challenging benchmarks such as MTEB and instruction tuning datasets. 
- The caching mechanism reduces latency for RAG, especially longer sequences. 
- The GRITLM model will be useful for practitioners.

### Weaknesses
 **Mixed results**
The main contribution of the unified method is to reduce the latency for generating the output. However, Table 4 shows a tradeoff between performance and latency. In Doc-Query and Query-Doc experiments, we see that GRITLM speeds up RAG but at the cost of overall performance. Furthermore,  GRITLM does not show significant speed-ups on GPUs. Finally, I would be curious to see if a smaller embedding model (besides a smaller GRITLM) shows improved performance compared to the RAG performance in Table 4.

**Modularity.**
One of the main advantages of RAG is that it is modular. The separation of the embedding model and the generative model makes it easy to swap out either one of the components. With a unified embedding and generative model, the entire model has to be retrained which can be computationally expensive. 

**Include more recent work**
The authors have acknowledged that the more recent embedding models, such as NV-Embed, show improved performance over GRITLM. It would be awesome if the authors cited more recent work [a, b] and more.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
4

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
This paper introduces GritLM, a language model designed to excel at both text generation and embedding tasks.  Current large language models (LLMs) typically specialize in one or the other, requiring separate models for applications that need both functionalities. GritLM addresses this limitation by employing a joint training approach.

The model architecture leverages a standard autoregressive generation head for text generation, trained with a next-token prediction cross-entropy loss.  For embedding tasks, GritLM uses bidirectional encoding of the input prompt and mean pooling of the final hidden layer representations.  A contrastive loss with in-batch negatives is applied to these embedding representations. The overall training objective combines these two losses, allowing the model to learn both tasks concurrently.

Experimental results demonstrate that GritLM achieves competitive performance on both generation and embedding benchmarks, comparable to similarly-sized specialized models.  Furthermore, the authors explore the benefits of this unified architecture in two specific scenarios: (1) reranking, where GritLM improves its own generated text through its embedding capabilities, and (2) retrieval-augmented generation (RAG), where the unified model serves as both retriever and reader, significantly reducing inference costs.

### Strengths
* GritLM effectively demonstrates strong performance in both generation and embedding tasks within a single model.

* The paper presents a thorough experimental evaluation, including reranking and RAG scenarios, showcasing the practical advantages of the unified architecture.

### Weaknesses
The scalability of the proposed method raises some concerns. The practicality of training and deploying a single model for both retrieval and generation may be limited to certain model sizes. In real-world applications, employing a smaller, faster embedding model alongside a potentially much larger generation model is often preferred. A smaller embedding model typically suffices for retrieval, while larger generation models are crucial for high-quality text generation. The paper would benefit from a discussion addressing the impact of model scale on the effectiveness of the unified approach and whether it remains advantageous when using vastly different-sized models for retrieval and generation.  Specifically, quantifying the trade-off between performance and efficiency in such mixed-size scenarios would strengthen the paper's claims.

(An alternative approach for using different sizes of embedder and generator is to use the output of the N-th layer (where N is relatively small) for embeddings instead of the last layer.)

### Questions
N/A

### Soundness
3

### Presentation
3

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
This work introduces GRIT, a method to train a single large language model to excel at both generative and embedding tasks through differentiated instructions. They proposed GRITLM models achieve SOTA performance on the Massive Text Embedding Benchmark and surpass other models in generative tasks. GRIT unifies the two tasks without compromising performance, offering efficiency gains such as over 60% faster Retrieval-Augmented Generation for long documents. The unified model simplifies infrastructure by handling both embedding and generative tasks, reducing the need for separate models.

### Strengths
1. GRIT introduces a novel approach that enables a single large language model to excel at both generative and embedding tasks, traditionally handled separately.
2. By eliminating the need for separate retrieval and generation models, GRIT speeds up RAG by more than 60% for long documents, which is a substantial improvement in processing time and resource management

### Weaknesses
1. The unified model requires more training resource, while there is no comparison of the performance between separate generation models and embedding models under the same resource consumption as shown in Table 1 and Table 2.
2. The paper uses the Mistral model as the base model. I think it would also be necessary to conduct experiments on the LLaMA series models to verify the robustness of the method.

### Questions
Please refer to the above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a new framework called GRIT, which aims to unify text generation and embedding tasks within a single LLM, GRITLM. The model handles both tasks efficiently by distinguishing between them through instructions, which streamline use in multi-task applications like RAG. The authors demonstrate that GRITLM performs strongly on text representation and generation benchmarks, achieving competitive performance on the Massive Text Embedding Benchmark (MTEB) while also excelling in generative tasks. 

Contributions:
1. Unified Generative and Embedding Model: The GRIT framework combines generative and embedding tasks within a single LLM. By using instructional prompts to distinguish between tasks, GRIT allows both generation and embedding without sacrificing performance. GRIT also reduces the need for separate models and complex infrastructure setups. This unification could simplify real-world deployments, particularly for applications that traditionally require both retrieval and generation components, such as search engines, recommendation systems, and conversational AI.
2. Efficient RAG catching design: The paper proposes innovative caching techniques, like Doc-Query Caching, and Query-Doc Caching, that significantly speed up RAG processes by reducing the number of forward passes required for long document processing. This approach reduces computational load for RAG tasks, enhancing efficiency in applications that rely on fast, context-sensitive retrieval and generation.
3. Competitive Performance Across Generative and Embedding Benchmarks: GRITLM achieves strong results on both the MTEB and several generative tasks, outperforming other open models of comparable size. This dual-task proficiency demonstrates that GRIT can match or exceed task-specific models, marking a significant step toward a general-purpose language model that handles both types of tasks seamlessly.
4. Task-Specific Performance Optimization: GRIT introduces several improvements, such as bidirectional attention with mean pooling for embedding tasks and mixed token-sample level loss aggregation for generative tasks. These innovations contribute to the model's performance across diverse tasks and offer insights into optimizing large language models for multi-task functionality.

### Strengths
Originality: The GRIT framework presents an original approach by unifying generative and representational capabilities within a single model, GRITLM, that can seamlessly switch between tasks based on instructional prompts. This concept is innovative as it directly addresses a long-standing limitation in language models: the need for distinct models optimized separately for generation and embedding. Previous work has focused on either generation or embedding, often leading to complex infrastructures where multiple models must be managed, synchronized, and deployed separately. GRIT’s unified approach not only simplifies these workflows but also brings both task types under one architecture without compromising performance. Additionally, GRIT’s application of caching techniques to accelerate RAG showcases an innovative use of model design to enhance efficiency, a departure from traditional RAG approaches that rely on separate models.

Quality: The paper demonstrates a strong methodological foundation, supported by comprehensive experimentation and ablation studies. The authors provide detailed evaluations on major benchmarks, contrasting GRITLM’s performance with task-specific models to validate its efficacy as a multi-task solution. The robustness of the results is further confirmed through comparisons with proprietary models and current open-source alternatives, evidencing GRIT’s strong performance in both generative and embedding tasks. The use of ablations to explore trade-offs in task prioritization, loss aggregation, and memory efficiency contributes to the overall rigor, allowing readers to clearly understand how GRIT’s dual-objective structure was optimized. The paper’s experiments on efficiency gains with caching also underscore the quality of its findings, providing quantitative backing for its claims regarding speed improvements in RAG tasks.

Clarity: The paper is well-organized and clear in its presentation, guiding the reader through complex ideas with a logical flow. Key concepts, GRIT’s caching mechanisms, and instructional tuning, are introduced with adequate background and broken down into understandable segments. Figures effectively support comprehension, making the technical details more accessible. The thorough presentation of results, including detailed tables and ablation analyses, provides clarity around GRIT’s performance relative to baselines, demonstrating where it excels and where there may be trade-offs. Additionally, the inclusion of an in-depth Appendix suggests a commitment to transparency and accessibility, ensuring that interested readers have the resources to delve deeper into implementation specifics and experiment configurations. 

Significance: The significance of GRIT lies in its potential to impact the field of NLP by simplifying multi-task language model deployment and reducing reliance on separate models for embedding and generation tasks. Furthermore, GRIT’s caching innovations for RAG tasks significantly reduce computational overhead and latency, especially in long-document settings, which is valuable for any application that relies on fast, context-aware responses. Moreover, GRIT’s design choices and improvements, such as mean pooling for embeddings and loss aggregation, may inspire further research into architectural unification across other language model tasks.

### Weaknesses
 Storage Costs for Caching: The paper proposes innovative caching strategies to speed up RAG, but for example, Doc Caching, in particular, requires 30TB of storage for key-value states on GRITLM 7B. Such high storage demands are prohibitive in many real-world scenarios, limiting the practical usefulness of these techniques.

Instruction Dependence: The model’s reliance on instruction-based differentiation between tasks could lead to inconsistent performance if instructions are poorly structured or if the model misinterprets the intended task. Instruction-based models can sometimes be sensitive to variations in phrasing, and such dependency on clear, well-defined instructions might limit GRIT’s robustness in noisy or ambiguous real-world applications.

Complexity of Caching Mechanisms and Trade-offs: While the caching mechanisms offer significant speed-ups, they introduce substantial complexity to the model's architecture and inference workflow. The paper acknowledges that Query-Doc Caching can result in degraded performance due to mismatches in attention patterns. This complexity could make it challenging for practitioners to implement GRITLM optimally and may lead to inconsistent performance across different tasks and input types.

### Questions
Storage Costs for Caching: The caching techniques provide impressive speed improvements, but the storage requirements (e.g., 30TB for Doc Caching) are substantial. Can the authors discuss potential strategies to make these techniques more feasible for real-world use, particularly in terms of storage optimization?

Instruction Dependence: Including experimental results on GRITLM’s sensitivity to instruction phrasing and format would provide valuable insights into its robustness and areas for improvement.

### Soundness
4

### Presentation
4

### Contribution
4
