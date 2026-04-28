# Not All Heads Matter: A Head-Level KV Cache Compression Method with Integrated Retrieval and Reasoning

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Key-Value (KV) caching is a common technique to enhance the computational efficiency of Large Language Models (LLMs), but its memory overhead grows rapidly with input length. Prior work has shown that not all tokens are equally important for text generation, proposing layer-level KV cache compression to selectively retain key information. Recognizing the distinct roles of attention heads in generation, we propose HeadKV, a head-level KV cache compression method, and HeadKV-R2, which leverages a novel contextual reasoning ability estimation for compression. Our approach operates at the level of individual heads, estimating their importance for contextual QA tasks that require both retrieval and reasoning capabilities. Extensive experiments across diverse benchmarks (LongBench, LooGLE), model architectures (e.g., Llama-3-8B-Instruct, Mistral-7B-Instruct), and long-context abilities tests demonstrate that our head-level KV cache compression significantly outperforms strong baselines, particularly in low-resource settings (KV size = 64 \& 128). Notably, our method retains just 1.5\% of the KV cache while achieving 97\% of the performance of the full KV cache on the contextual question answering benchmark

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed a head-level Key-Value cache compression algorithm, different from Ada-KV (also head-level), they don’t perform  allocation within a single layer during the budget allocation process but for all heads. 

They conduct experiments on LongBench and LooGLE, the performance is consistently better or comparable than the full KV baseline with a reasonable amount of KV cache size.

Also, they introduced the the retrieval-reasoning head to assign higher importance score for those heads with higher attentions on the correct answer. Such head seems useful based on the experiments, though not all of them, still makes reasonable improvements on certain datasets.

They also conduct thorough analysis on long-context retrieval, latency , memory usage, etc.

### Strengths
1. Reasoning head-level kV cache allocation and importance score estimation. 
2. Performance can be consistently better or comparable with the full KV setting.

### Weaknesses
1. We do not see much improvement on latency and memory as compared against Ada-KV, as I believe this work is based on Ada-KV.

### Questions
N.A.

### Soundness
4

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
4

### Summary
This paper proposes a head-level KV cache eviction method, and the authors use the retrieval capability of heads to score their importance, then less important heads evict more tokens. Based on previous retrieval-head criteria, the authors put forward two improvements: one is a more challenging retrieve-reasoning dataset, and the other is using attention weights to refine the score, making the scoring more accurate. By setting different KV cache budges for different heads, this method outperforms other baselines in various evaluation metrics while maintaining the same total KV cache size and inference latency.

### Strengths
1. The KV cache budget allocation strategy maintains the total amount of KV cache constant and keeps inference time unchanged.

2. Using top-k attention weights to refine the score can enhance the retrieval-head evaluation. 

3. The proposed retrieve-reasoning dataset may benefit future works.

### Weaknesses
1. How the S_h is normalized is not mentioned in this paper. In Equation (4), it seems that S_h should sum to one across all heads and all layers.

2. How the retrieval-reasoning dataset is generated is not mentioned in the paper.

3. The left subfigure in Figure 6 saids decoding times but line 512 mentioned that the decoding time includes prefilling time. This is quite confusing. In the figure, the prefill time of each method (when generating a length of 0) is squeezed into the same point on the image, making it impossible to discern their merits and demerits. Please rename the axis label, move the relevant explanation to the caption, or separate the prefill and decode into two figures.

4. The a_h in Equation (1) and (2) may need a superscript t.

5. Typo in Figure 1: The red text Prefilling Phrase should be Prefilling Phase.

6. Typo in Figure 5 and Figure 8: 'Neele-in-a-Haystack' should be 'Needle'.

7. Are those gaps between FullKV and HeadKV in the right subfigure of Figure 6 solely caused by KV cache?

8. Giving a pseudo code would be better.

### Questions
1. The a_h in Equation (1) and (2) may need a superscript t.

2. Typo in Figure 1: The red text Prefilling Phrase should be Prefilling Phase.

3. Typo in Figure 5 and Figure 8: 'Neele-in-a-Haystack' should be 'Needle'.

4. Are those gaps between FullKV and HeadKV in the right subfigure of Figure 6 solely caused by KV cache?

5. Giving a pseudo code would be better.

### Soundness
4

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
The paper proposes a new KV cache compression technique, HeadKV and HeadKV-R2, by selectively discarding or retaining the important KV cache based on different types of head. The proposed method consists of two main stages: retrieval-reasoning head identification and KV cache budget allocation based on the head's type. The paper proposes a new type of NIAH test and claim it can be used to identify heads that can both retrieve and reason about the tokens from the context based on the proposed retrieval-reasoning score estimation equation. After successfully identifying the R2-heads, the method dynamically allocate the KV cache budget to retain for each head based on its score from the previous step. The paper claims to maintain 97% performance, compared with baseline with full KV, even though only retaining 1.5% of total KV.

### Strengths
- The study presents a new way to compress KV cache based on different types of attention head is novel, even though there are concurrent works that also work on the same idea.
- The performance of the proposed method surpasses other baselines considered in the paper by a considerable margin at the extreme cases when retained KV size is small.

### Weaknesses
1. Even though the paper claims to successfully identify heads that can do both retrieval and reasoning for **long-context** task, which is better than the retrieval-only heads initially proposed in Wu et al. (2024), the NIAH experiment setting in the paper is not long enough (longest prompt = 8k). I believe 8k is considered to be not long enough nowadays. Can the author try longer NIAH test such as 64k or 128k to show the effectiveness of the identified R2-heads?
2. I believe there is a work called "Razorattention" [1] that is released in July which follows the same trajectory as this study, i.e. kv cache compression based on head type. Even though the paper addresses this work in their writing, I don't see any comparison in term of performance between the proposed method and that work, especially two works follow the same directory and Razorattention was released a few moths ago. It is unclear to notice the major contribution of the R2-heads from retrieval head only. Can the author benchmark and compare their performance in your experiment?
3. The estimation equation used to determine R2-head seems to be vague (or even incorrect).
- What is the first sigma, or the t-sigma, sum used for?
- The claim that this proposed estimation method can identify which head is responsible for reasoning is not convincing. Firstly, the study modifies the needle to include reasoning logics & incorrect answer, but do not consider them at all in the estimation equation. The estimation equation only considers the correct answer, c2, as the ground truth, which imo, the same as the original retrieval-identification test. What is the usage of the add-on logics and incorrect answer here if you don't consider it in the estimation?
4. I believe the paper would benefit more from ablation study showing and discussing the effect of different values of hyper-parameter alpha & beta on the performance of the methods.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a method for KV-cache compression for efficient language modeling. While previous work compresses the KV-cache at the global or layer level, this paper leverages the properties of multi-head attention and operates at individual heads, achieving a finer-grained computation allocation. The method weighs the importance of each head by considering their contribution to both the retrieval and reasoning processes, resulting in a better selection of past KV cache. With all strengths combined, the method outperforms the baseline methods in multiple tasks that require long-context retrieval or reasoning.

**post review**: I raised my score from 5 to 6.

### Strengths
1. This paper refines the method for head importance scoring proposed by Wu et al. (2024) and the authors justify their refinement with ablation studies.
2. This paper proposes a head-level allocation schema that can dynamically allocate memory across attention heads and layers. 
3. The performance of this method is better than baselines under the same memory budget.

### Weaknesses
1) The contribution of this paper is relatively marginal in terms of methodology. The modification to the method of Wu et al. (2024) is a shift from retrieval to reasoning and a relaxation of the weighting process, while the overall design of the scoring remains the same. From the KV-cache compression perspective, it improves the granularity of prior work from layer to head without changing the overall compression logic.

2) The application of the KV cache compression is limited to scenarios where retrieval is required. The compression/allocation is already done after reading the instruction part of the prompt, thus the attention of the generation will be constrained to the selection caches. For tasks such as Needle-in-the-Haystack or retrieval-based QA, this strategy might work, but for the rest of the tasks such as summarization or creative generation, it might fail.

This might be a general issue for all the work of KV cache selection, but this paper does not break this limitation.

3) This work might not be practically useful in terms of efficiency. Though the authors claim that their method can be as efficient as other methods and better than the full-KV baseline in section 4.5, the analysis is based on a 7B model. For larger models, the overhead on the KV cache and attention matrix is negligible.

Even for a 7B model, the analysis conducted in this paper shows that the decoding speed is improved only when the decoding sequence length reaches 1000 tokens. For memory usage, the difference is observable when the context length reaches 32k tokens. This might not be a typical case even for the datasets tested in this paper.

### Questions
1. What is the experiment condition for the memory usage diagram in Fig 6? The x-axis here is named "context length", so what is the generation length? Also, given the pre-filling phase has not changed, can the proposed method improve the memory usage for context encoding?
2. Finer-grained memory allocation usually means more fragmented memories. From my understanding, the method prunes caches from the token, layer, and head dimensions, will this result in fragmented KV caches? Will this affect the efficiency of parallel computation?
3. It would be great if the authors could discuss and compare this work to RAG methods.

It would be great if the authors discuss other efficiency-concerned papers. A few past work discusses the general compression of KV caches without considering the retrieval process:

- In-context Autoencoder for Context Compression in a Large Language Model. Ge et al, 2024. In ICLR.
- Dodo: Dynamic Contextual Compression for Decoder-only LMs. Qin et al, 2024. In ACL.
- VCC: Scaling Transformers to 128K Tokens or More by Prioritizing Important Tokens. Zeng et al., 2023. In NeurIPS.

### Soundness
3

### Presentation
4

### Contribution
3
