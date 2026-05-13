# Block-Attention for Efficient RAG

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
We introduce Block-Attention, an attention mechanism designed to address the increased inference latency and cost in Retrieval-Augmented Generation (RAG) scenarios. 
Traditional approaches often encode the entire context.
Instead, Block-Attention divides retrieved documents into discrete blocks, with each block independently calculating key-value (KV) states except for the final block.
In RAG scenarios, by defining each passage as a block, Block-Attention enables us to reuse the KV states of passages that have been seen before, thereby significantly reducing the latency and the computation overhead during inference.
The implementation of Block-Attention involves block segmentation, position re-encoding, and fine-tuning the LLM to adapt to the Block-Attention mechanism. 
Experiments on four RAG benchmarks demonstrate that after block fine-tuning, the Block-Attention model achieves performance comparable to self-attention models (68.4\% vs 67.9\% on Llama3) or even superior performance (62.8\% vs 59.6\% on Mistral).
Notably, Block-Attention significantly reduces the time to first token (TTFT) and floating point operations (FLOPs) to a very low level. It only takes 45 ms to output the first token for an input sequence with a total length of 32K. Compared to the self-attention models, the time consumption and corresponding FLOPs are reduced by 98.7\% and 99.8\%, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the Block-Attention method, an efficient approach tailored for RAG scenarios that enhances inference efficiency while preserving performance through fine-tuning. Block-Attention operates by dividing the input sequence into multiple independent blocks, each calculating its key-value (KV) states separately via self-attention. Only the final block can attend to previous blocks, allowing the user query to reference all prior retrieved documents. Evaluations on four RAG benchmarks reveal that Block-Attention, after fine-tuning, maintains comparable accuracy to traditional self-attention models (e.g., 68.4% vs. 67.9% on Llama3) and even slightly outperforms in some cases (e.g., 62.3% vs. 59.6% on Mistral). The efficiency benefits, measured in TTFT and FLOPs, grow with input length; at 32K input length, Block-Attention’s TTFT and FLOPs reach just 1.3% and 0.2%, respectively, of those in standard self-attention models.

### Strengths
- Novel and practical idea
- easy to follow
- Simplicity: The solution is relatively simple to implement and can be integrated into existing LLM architectures.
- Impressive performance: this method reduces Time to First Token (TTFT) by up to 98.7% and FLOPs by up to 99.8%.

### Weaknesses
### Needs for finetuning:  
The method requires additional fine-tuning, which might be resource-intensive for larger models. It would be better to explore a training-free approach with the proposed method.

### Questions
Only tested on relatively small models (7B-8B parameters) - would it work as well on larger models?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes Block Attention for retrieval augmented generation (RAG). The idea is to confine attention within each retrieved document (a.k.a. block) and only let the query attend to all documents. In this way, the KVs for each document can be cached and reused if the document re-appears in multiple queries. The method also proposes to explicitly correct RoPE positional encoding before reusing the cached KVs. After fine-tuning, this technique can retain the accuracy of the baseline while speeding up the inference due to smaller attention span and avoiding the KV recomputation thanks to the block caching.

### Strengths
- The method is simple and easy to implement: It only involves limiting the attention computation within each document in RAG scenarios and caching the KVs for each block for document re-use as proposed in PromptCache [Gim et. al, 2024]. The newly introduced RoPE rotation correction is also straightforward to implement.
- Local attention and prompt caching are sound techniques and suitable for RAG applications.
- The paper is clear and easy to follow.

### Weaknesses
My primary concern is regarding the paper's contribution compared to the existing works and the need for a better experimental analysis to understand where this method stands among previous methods that share very similar ideas or how it improves them. The authors can find more detailed comments and suggestions below.

- Contribution and limitations compared to existing works

To me the main contributions of the paper to improve the efficiency of RAG can be summarized as 1) limiting the attention within each document 2) caching the KVs of the documents to reuse them 3) Adjusting the rotation in the RoPE position encoding based on the position of the reappearing cached document. Points 1 and 2 have been already proposed in prior works. E.g. PromptCache [Gim et. al. 2024] proposed the same techniques to speed up the RAG applications. This makes contribution 3, the main new addition to the existing works. However, according to the experiments reported in the submission, the RoPE position correction does not lead to any improvement over PromptCache (lines 353-356). To my understanding this makes fine-tuning the only source of improvement over PromptCache, which is an expected gain which comes with known challenges of such a fine-tuning.

I want to also point the authors to [1] below that is a closely relevant prior art which is currently missing from the draft. [1] also addresses the three aforementioned points above. Namely, it proposes limiting attention to attention blocks, caching the KVs for the documents to re-use them, and addresses the position encoding problems by overlaying the documents as parallel edges without requiring any fine-tuning. I would suggest the authors add a discussion on the advantages of the proposed method compared to [1] and also add controlled experimental comparisons to better highlight the contributions.

[1] Superposition Prompting: Improving and Accelerating Retrieval-Augmented Generation, Merth et. al.

* Experimental Results

The experimental section needs to be revised to clearly highlight the main sources of improvements and contributions between the proposed method and existing prior methods (under same settings, e.g. with or without fine-tuning). Based on the submission, comparisons with similar approaches are missing (see [1] above), additional speed up on top of PromptCache (if any) is not verified, and it is not clear to me if anything other than the fine-tuning is the source of accuracy improvement over PromptCache. The authors can find more detailed comments and questions regarding the experiments in the following section.

### Questions
- Additional questions and comments:

1) To my understanding, the main technical contribution of the method compared to the previous approaches is the proposal to explicitly re-adjust the positional encodings. What is the practical advantage of the proposed RoPE encoding adjustment? Does it lead to any improvement on the final RAG task quality metrics over PromptCache? From the current manuscript I did not find an ablation showing its importance to improve prior arts. 

2) What is the comparison between the proposed method and PromptCache in terms of efficiency? How much does the proposed method improve PromptCache in terms of wall-time?

3) How does the method compare with respect to the Superposition Prompting paper above [1] both in terms of accuracy and efficiency?

4) The paper mentions fine-tuning on RAG-specific datasets necessary for the proposed approach. Expectedly, fine-tuning can improve the accuracy on the specific tasks at hand, but it is also important to maintain the generalizability of the pre-trained models. This can be difficult especially when the training recipes are not available, or they are instruction fine-tuned on non-available data. How does the performance of the reported models change on common benchmarks such as MMLU and HumanEval after the suggested fine-tuning?

5) The positional encoding re-adjustment is only discussed for RoPE. As a suggestion for further improvement, it would be nice to have a more thorough analysis on different positional encoding approaches.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the efficiency challenges in RAG. The key observation is that different paragraphs retrieved in RAG are independent to each other. Therefore, it is possible to perform independent self-attention within each paragraph, and only allow the final question query to attend to all previous passages. This will dramatically improve TTFT in long-context RAG. The authors identify two important steps to recover accuracy after converting traditional self-attention to block attention (proposed in this paper): positional re-encoding and fine-tuning. Their final results show no loss of accuracy and significant speedup in long-context RAG applications.

### Strengths
1. The idea is simple and reasonable: different retrieved passages are not necessarily related to each other so the attention mask can be sparsified.
2. Positional re-encoding is an elegant way to solve inconsistencies in positional encodings.
3. Finetuning results show no loss of accuracy and significant speedup over self-attention baselines.

### Weaknesses
1. The method requires fine-tuning, which limits its scalability.
2. The evaluation seems to be a bit weak. 
- For example, the method trains on TQA/2Wiki's training set and evaluates on their validation sets. The results on these two benchmarks are not zero-shot and are not very representative. 
3. It's unclear what is the overhead associated with positional re-encoding.
4. Can you construct some examples where different retrieved passages are related to each other? In this case, will the proposed method fail? For example, you might retrieve several chapters in a textbook, where later chapters are dependent on earlier chapters.

### Questions
Please respond to my questions in "Weaknesses".

===

Post rebuttal: my concerns have been resolved and I will keep my score.

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
4

### Summary
This paper presents the Block-Attention mechanism aimed at optimizing inference efficiency in retrieval-augmented generation (RAG) scenarios. The authors assert that by modifying the attention calculation to process tokens in independent blocks, they can significantly enhance both accuracy and computational efficiency compared to traditional self-attention. The proposed method is evaluated against well-known RAG benchmarks, and the authors claim notable improvements in inference speed and resource consumption.

While the topic is pertinent, the contributions of the paper raise several concerns. The approach, although presented as innovative, relies on established principles of attention mechanisms without sufficiently distinguishing itself from previous work. Additionally, the experimental results, while promising, lack depth in exploring the nuances of the proposed method's effectiveness across varying conditions.

### Strengths
1. The paper is generally well-organized, with clear explanations of the Block-Attention mechanism and its proposed advantages.
2. The investigation into improving inference efficiency in LLMs through Block-Attention is timely.
3. The reported gains in inference speed and reduced computational load are compelling.

### Weaknesses
1. The concept of segmenting attention into blocks is not entirely novel and has been explored in various forms in the literature. The paper does not convincingly articulate how Block-Attention offers distinct advantages over similar approaches, such as sparse attention methods or hierarchical attention mechanisms. Specifically, the paper lacks a detailed comparison to methods that also aim to reduce computational cost by limiting attention scope, such as those using locality-sensitive hashing or other approximation techniques. The claim that Block-Attention is fundamentally different needs more rigorous justification, especially considering the existing body of work on efficient attention mechanisms.

2. The paper presents empirical results without adequately establishing the theoretical underpinnings of the Block-Attention mechanism. For example, the claim that "tokens in all blocks except the last are restricted to attending only to information within their own block" (Section 3.4) needs further elaboration on how this restriction impacts the model's representational capacity compared to full self-attention. The authors should provide a more formal analysis of the information flow and potential bottlenecks introduced by this block-wise attention, including a discussion on how the model maintains global coherence when information is processed in isolated blocks. A theoretical analysis of the computational complexity and memory footprint would also be beneficial.

3.  The experimental section would benefit from a broader set of benchmarks and comparison against state-of-the-art methods beyond just self-attention. The current evaluation is limited and does not fully demonstrate the robustness of the proposed method across diverse RAG scenarios. A more comprehensive evaluation should include comparisons with other efficient RAG techniques, such as those employing vector databases or knowledge graphs, to provide a clearer picture of the relative benefits of Block-Attention. The absence of such comparisons makes it difficult to assess the true impact of the proposed method.

4. The authors should discuss how the model performs under different conditions, such as varying levels of noise in the retrieved passages or the diversity of user queries. The current evaluation lacks an analysis of the sensitivity of Block-Attention to the quality of retrieved documents and the complexity of user queries. It is crucial to understand how the model behaves under less-than-ideal conditions, as this is often the reality in practical RAG applications. A discussion of the limitations and potential failure modes of the method is also necessary.

### Questions
1. How do the authors justify the choice of block size in the Block-Attention mechanism, and what implications does this have for different types of queries?
2. Can the authors elaborate on how the performance of Block-Attention varies with input length and retrieval volume? Are there any thresholds beyond which the performance might degrade?
3. Given the reliance on fine-tuning, how do the authors plan to address potential overfitting issues, particularly in diverse RAG settings?

### Soundness
3

### Presentation
3

### Contribution
3
