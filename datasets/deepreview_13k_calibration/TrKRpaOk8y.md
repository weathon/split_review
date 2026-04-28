# A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 8, 6

## Abstract
Training and serving long-context large language models (LLMs) incurs substantial overhead. 
To address this, two critical steps are often required: a pretrained LLM typically undergoes a separate stage for context \term{length extension} by training on long-context data, followed by architectural modifications to \term{reduce the overhead of KV cache} during serving. 
This paper argues that integrating length extension with a GPU-friendly KV cache reduction architecture not only reduces training overhead during length extension,
but also achieves better long-context performance. 
This leads to our proposed \name, which finetunes a pretrained LLM into an efficient architecture during length extension. 
\name builds on three key insights: 
(1) Sparse attention patterns, such as window attention (attending to recent tokens), attention sink (initial ones), and blockwise sparse attention (strided token blocks) are well-suited for building efficient long-context models, primarily due to their GPU-friendly memory access patterns, enabling efficiency gains not just theoretically but in practice as well. 
(2) It is essential for the model to have direct access to all tokens. 
A hybrid architecture with 1/3 full attention layers and 2/3 efficient ones achieves a balanced trade-off between efficiency and long-context performance.
(3) Lightweight training on 5B long-context data is sufficient to extend the hybrid model's context length from 4K to 128K.

We evaluate \name on both Llama-2 7B and Llama-2 70B, demonstrating its effectiveness across different scales. 
During training with 128K-long contexts, \name achieves 1.55x training speedup and reduces wall-clock time by 36\%, compared to a full-attention baseline. 
During inference, \name reduces KV cache memory by 62\%, achieving 1.67x prefilling speedup and 1.41x decoding speedup.
Compared to baselines that apply KV-cache reduction techniques to full-attention long-context LLMs, \name achieves substantially stronger performance not only on the Needle-in-a-Haystack retrieval task, but also on more challenging long-context reasoning tasks, including BABILong and RULER.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces LONGGEN, an efficient architecture designed to extend context length while minimizing computational and memory overhead during training and inference. The key contribution of LONGGEN is its innovative use of a combination of full attention and KV-reduced attention layers during the post-training phase of context length extension. This approach allows the model to adapt to sparse context scenarios, effectively addressing the poor performance observed with previous KV cache reduction methods on long-context tasks. Additionally, LONGGEN introduces static position access and block-wise context handling to mitigate issues related to position embeddings and idling threads. Empirical experiments demonstrate LONGGEN’s superior performance compared to other KV cache reduction methods, highlighting its effectiveness in managing extended contexts efficiently.

### Strengths
Originality
	1. hybrid architecture to long-context expanding. Instead of using a full attention mechanism across all layers, the proposed LONGGEN introduces a creative combination of sparse and full attention. This hybrid method allows model generalize well on long-context tasks without high computational overhead. 
	2. The work also introduces an optimized GPU-friendly KV cache management technique, which makes long-context processing feasible and efficient on hardware.

Quality
The paper write with a good formal quality in both methodological and experimental part. Extensive evaluations are presented on benchmarks, highlighting LONGGEN’s performance benefits over alternative KV cache reduction techniques and full-attention baselines. The experimental part also includes ablations analyses such as the position and number of full attention layers.

Clarity
The clarity of the paper is good, particularly in its well explanations of the  KV cache optimization methods and hybrid attention. There are some graphs support the narrative and help show the model’s efficiency benefits.  Clear section headings and figures guide the reader through the technical details, allowing for a smooth understanding of ideas.

Significance
This paper is significant as it addresses a critical challenge in LLM scalability which is efficiently extending the context length while preserving the model’s quality and saving computational cost on hardware. It suitable for some applications that require processing large contexts, such as document analysis and long-form dialogue.

### Weaknesses
1. This is not the first paper to propose post-training with a sparse attention mechanism; previous works, such as "Sparser is Faster and Less is More," have also introduced sparse attention methods during both training and inference stages.
2. Comparisons are limited to KV cache reduction methods that allocate KV budgets at the pre-filling stage. However, approaches like "Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference" use query-level sparsity to dynamically activate the KV cache and provide full context access. The paper does not address the potential benefits of dynamic sparsity in comparison to the static sparsity used in LONGGEN, particularly in scenarios where different parts of the context may have varying levels of importance.
3. Additional experiments are needed to strengthen the robustness of the idea that hybrid sparse attention performs best. For a more comprehensive comparison, LONGGEN could also use H2O, RazorAttention, and PyramidKV methods to extend context length during post-training. The current evaluation lacks a thorough exploration of the design space for hybrid attention, such as varying the number and placement of full attention layers, and the specific sparsity patterns applied in the sparse attention layers. This limits the understanding of the optimal configuration for different tasks and context lengths.

### Questions
1. How did you set up experiment parameters to ensure a fair comparison between LONGGEN and previous KV cache reduction methods, such as Attn Sink, H2O, and PyramidKV?
2. Does the sparse attention method remain consistent between training and inference?
3. When you mention savings in profiling and decoding time, is this in comparison to the full attention method? If so, could you also describe how LONGGEN's inference time compares to previous KV cache methods?

### Soundness
3

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
4

### Summary
This paper introduces LongGen, which improves both training and inference efficiency of long-context LLMs. The key insights in this paper are: 1) structured sparse attention patterns, with GPU-friendly memory access patterns, enable practical efficiency gains for long-context LLM; 2) a hybrid architecture with full attention layers and sparse ones provides efficiency merits while keeping the models’ performance; 3) context-extension training only requires a lightweight training dataset. Experiments show that LongGen reduces training wall-clock time by 36%. It also reduces KV cache memory by 62% during inference, achieving 1.67x prefilling speedup and 1.41x decoding speedup.

### Strengths
1) LongGen improves both training and inference efficiency for long-context LLMs, accelerating training by 1.55x and inference by 1.41-1.67x, without prominent accuracy loss.
2) LongGen identifies that keeping middle layers with full attention and applying sparse attention on the beginning and final layers achieves better performance. It also finds that keeping 1/3 layers with full attention achieves a balance between accuracy and efficiency.
3) LongGen integrates a triton-based attention kernel supporting structured sparsity for efficient inference and training.

### Weaknesses
1) The key insights proposed in this paper have been introduced in other papers. For instance, attention-sink and block-sparse attention are not new attention patterns (e.g., [1](https://arxiv.org/abs/2309.17453), [2](https://arxiv.org/abs/2407.02490)). Additionally, extending the model's context length can be achieved with light-weight training is also observed in existing literature (e.g., [3](https://arxiv.org/abs/2306.15595), [4](https://arxiv.org/abs/2307.03170), [5](https://arxiv.org/abs/2309.12307)). The novelty of this paper is limited.

2) The evaluation details of the efficiency benchmark should be further elaborated.

3) The models used for main evaluation is old. Results on Llama-3 series would be more persuasive.

### Questions
1) What is the specific evaluation setting for Figure 2 (Right)? Is it tested on 4 A100 GPUs with TP=4 with vLLM? On a single A100, vLLM (W8A8) requires less than 30ms to decode a token for Llama-2-7B (64K sequence length, batch size = 1). Since the complexity of decoding stage attention grows linearly with regard to the sequence length, decoding a token with 128K context sequence length should take no more than 60ms with a single A100. However, in Figure 2 (Right), it takes 60 seconds to decode 512 token (~117 ms/token) with 4 GPUs (dense baseline with 32 full layers). It would be helpful if the authors can provide more details about this evaluation.

2) What is the kernel-level speedup achieved with the sparsity pattern used in LongGen for the attention kernel? For instance, given the 1/64 sparsity (retain 2K tokens in 128K), what is the speed comparison between dense flash attention and the sparse attention kernel used in LongGen? Is it possible for LongGen to achieve measured speedups when serving (i.e., run inference with) sequences shorter than 128K?

3) How is the proposed method compare with other existing KV cache elimination methods (e.g., [6](https://arxiv.org/abs/2310.01801))?

### Soundness
2

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
4

### Summary
This paper presents LONGGEN, a method designed to enhance the efficiency of long-context training and inference in large language models (LLMs). LONGGEN employs a hybrid attention architecture to achieve an optimal balance between computational efficiency and performance in long-context tasks. The model architecture is segmented into three sections: the first and last thirds of the layers utilize sparse attention mechanisms, while the middle third maintains full attention.

### Strengths
1) Problem importance: LONGGEN addresses the critical problem of context window extension in LLMs, specifically targeting issues of performance degradation, high computational complexity, and excessive memory consumption as context length increases, which is an important challenge for enabling LLMs to handle long-form content efficiently in real-world applications.

2) Training and inference efficiency: The LONGGEN approach enhances both training and inference efficiency by reducing training FLOPs, KV cache memory size, prefilling speed, and decoding speed. By employing sparse attention in the outer layers and full attention in the middle, LONGGEN effectively manages computational load and memory usage. This design allows for context length extension up to 128K tokens with lightweight fine-tuning on long-context data, making it suitable for long-context applications. 

3) Results: LONGGEN demonstrates almost the same performance as the full-attention model across key benchmarks, including Needle-in-a-Haystack (NIAH), BABILong, RULER, MMLU, Math, and BigBenchHard (BBH). Additionally, it outperforms other KV cache eviction methods and long-context training approaches on the NIAH and BABILong tasks.

### Weaknesses
1) Results of the other models: The results of LONGGEN have only been demonstrated on Llama2-7B and Llama2-70B models, which limits understanding of its effectiveness on other model architectures and sizes (such as GPT models, Gemini, or other Llama models). Specifically, the performance of the proposed method on models with different attention mechanisms (e.g., different variants of multi-head attention or other sparse attention implementations) is not explored, making it difficult to assess the generalizability of the approach.

2) Results on the other tasks: LONGGEN introduces an hourglass architecture that keeps the middle layers in full attention mode, based on previous studies [1, 2, 3] showing that attention heads are crucial for retrieval and reasoning tasks. However, its performance on other long-context benchmarks has not been explored in this work (such as single/multi-document QA or Summarization). This is a significant limitation, as the effectiveness of the method may vary across different task types, and the current evaluation is not comprehensive enough to draw broad conclusions about its applicability.

3) Full attention layers:  The specific selection of the full attention layer has not been explored, which can differ from task to task (or model to model). Additionally, although the authors have conducted an ablation study to determine that 1/3 of the layers should use full attention, this proportion may vary across different models or different tasks and would require separate ablation studies for each. The lack of a systematic approach to determine the optimal placement and number of full attention layers is a concern, as the current approach may not be optimal for all scenarios.

### Questions
1) What are the results of LONGGEN  on other popular large language models, such as GPT models or Gemini?

2) How would the results of LONGGEN change if applied to tasks other than retrieval or reasoning ones?

3) Should the architecture, specifically the number and placement of full attention layers, be adjusted for different models or tasks?

4) Is there an algorithmic or automated method for determining the optimal number and placement of full-attention layers?

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
4

### Summary
This paper proposes LongGen, which integrates GPU-friendly KV cache reduction architecture to save both length extrapolation and serving cost. It is built on three observations, on sparse attention and the number of tokens needed. It achieves effective cost reduction in both training and serving cost.

### Strengths
1. The paper is well written: especially abstract and introduction is well structured and informative on what the paper is going to about. The figures are well made.
2. The performance is very good: e.g. NIAH result is much better than previous methods such as StreamingLLM.

### Weaknesses
There is no noticeable weaknesses that the reviewer hope the authors shall address (only some small clarification questions). Please see the question section.

### Questions
In the experiment setup, the author mentions that the tensor parallel size is set to 8 with 256 GPUs. Are the remaining GPUs used for data parallelism or pipeline parallelism? And what is the framework used to measured the speedup? And how many iterations to calculate the average training/inference time?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors finetunes a pretrained LLM into an hybrid architecture that consists 1/3 full attention layers and 2/3 sparse attention layers. By incorporating full attention layers, LongGen allows the model to access to certain positions directly, enhancing the performance on accurate retrieval tasks. Experimental results show that LongGen incurs no loss on the needle-in-a-haystack retrieval task and maintains model performance on tasks with short context, such as MMLU, demonstrating its effectiveness.

### Strengths
- The work highlights the importance of including full attention layers for models to achieve accurate retrieval.
- The paper is well-written.
- Experimental results indicate that LongGen accelerates both training and inference for long context while preserving model performance.

### Weaknesses
 - Since training on long context constitutes a small portion of pre-training, the training speedup of LongGen is limited during pre-training.
- LongGen with AtteSink and BlockSparse demonstrates similar performance, necessitating a detailed explanation for this observation.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
2
