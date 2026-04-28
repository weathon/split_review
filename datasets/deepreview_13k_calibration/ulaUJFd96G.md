# Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 3, 8

## Abstract
Large language models (LLMs) have shown remarkable performance in various natural language processing tasks. 
However, a primary constraint they face is the context limit, i.e., the maximum number of tokens they can process.
Previous works have explored architectural changes and modifications in positional encoding to relax the constraint, but they often require expensive training or do not address the computational demands of self-attention.
In this paper, we present \textit{Hierarchical cOntext MERging (HOMER)}, a new training-free scheme designed to overcome the limitations. \mname~uses a divide-and-conquer algorithm, dividing long inputs into manageable chunks. Each chunk is then processed collectively, employing a hierarchical strategy that merges adjacent chunks at progressive transformer layers. A token reduction technique precedes each merging, ensuring memory usage efficiency.
We also propose an optimized computational order reducing the memory requirement to logarithmically scale with respect to input length, making it especially favorable for environments with tight memory restrictions. 
Our experiments demonstrate the proposed method's superior performance and memory efficiency, enabling the broader use of LLMs in contexts requiring extended context.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a new approach to handle long context by LLMs without any training, by compressing and merging context chunks in a divide-and-conquer manner. Specifically, the long context is first split into chunks, and a LLM then encodes and compresses the chunk by pruning its tokens according to attention importance, finally concatenating adjacent chunks at each transformer layers. The proposed approach is shown achieving good performance on retrieval and QA tasks. Additionally, it can be viewed orthogonal to other techniques to extend LLM context length via scaling Rotary embeddings, and is shown state-of-the-art performance on QA when combing with other existing techniques together.

### Strengths
- The proposed approach brings a new perspective to handle long context by LLMs through context compression and merging, complementary to other popular techniques focusing on Rotary position embeddings.
  
- The approach is shown to surpass all baselines on Passkey Retrieval, extending to 8 times longer than the pretrained context length. For QA, it is shown to achieve the best performance combining with another long-context technique NTK.
  
- The proposed approach has the advantage of low GPU memory usage, compared with other baselines, due to the compression of context, leading to a reduced size of KV cache.

### Weaknesses
Though effective on the relatively easy Passkey Retrieval, the heavy compression and merging of context might hurt the reasoning capability of LLMs, as shown by Table 3 that the proposed approach alone underperforms other long-context techniques on QA. It is unknown whether this technique would remain useful on other tasks that also require reasoning. More experiments on other tasks could be conducted to demonstrate the advantages as well as the disadvantages of the proposed approach.

Specifically, the attention-based pruning, while efficient, could lead to the loss of crucial information, especially in tasks requiring complex reasoning chains. The merging process, by concatenating compressed chunks, might also disrupt the contextual understanding of the model, as the original positional relationships between tokens are altered. The experiments on QA, while showing some improvement when combined with other techniques, do not fully explore the limitations of the compression and merging strategy on tasks that require more sophisticated forms of reasoning, such as tasks involving logical inference or multi-hop reasoning.

### Questions
What if we only look at the attention importance at the final layer directly, and use the top-k positions as the final pruning decisions for every layer? How is this compared to the proposed approach?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new method called Hierarchical Context Merging to extend the context limit of LLMs all the way to 64K tokens. The method is training-free, and uses a divide-and-conquer methodology to segment inputs into smaller units. At each following Transformer layer, the segments are fused together through a token reduction technique to reduce the memory footprint. The authors also propose to optimize the computation order to further reduce the memory requirement by 70%. 

The proposed method is evaluated on three sets of tasks: Perplexity on 19 long documents from PG-19, passkey retrieval and question answering. The paper shows superior performance on all three benchmarks against RoPE-based baselines such as PI, NTK and YaRN.

### Strengths
The work shows several strengths:
1. The proposed method HOMER is the only method which has a reasonable Perplexity on 64K long documents. The performance gain on passkey retrieval at 32K tokens is impressive: 22.4% -> 80.4%.
2.  The memory reduction up to 70% is also quite impressive.

### Weaknesses
However, I do have several weaknesses regarding the work:
1. For Llama-2-13B, the gain on both perplexity and passkey retrieval is very marginal for all the context lengths below 32K. This raises concerns about the method's effectiveness in more common context ranges, as many practical applications may not require extremely long contexts. The lack of substantial improvement in these lower ranges suggests that the method's complexity might not be justified for general use cases.
2. The Accuracy on QA benchmark is very concerning (Table 3): HOMER alone is worse than the NTK method, not showing any performance advantage. This is a significant drawback, as question answering is a crucial task for evaluating the practical utility of language models. The fact that HOMER underperforms a baseline method in this area questions its general applicability and suggests that the proposed approach might not be as robust as claimed. 1&2 together raises the question of the generalization of the HOMER method, and the presented results are not comprehensive enough to convince the readers.
3. The biggest concern is the complexity of the method: compared to RoPE based methods, HOMER involves merging chunks, token reduction, embedding refinement as well as computational order reduction. All these techniques together make the proposed method very hard for wide adoption in the community, hence limiting the impact of the work. The multiple stages of processing introduce significant engineering overhead, and the need for careful parameter tuning for each stage could make it difficult to implement and integrate into existing systems.

### Questions
I do have a few questions that I need clarifications from the authors:

1. The inference time of HOMER was not discussed at all in the paper. Instead, memory is the major focus. While memory footprint is an important dimension, inference time is very important for LLM applications. Given the extensive manipulations of HOMER on context embeddings at each Transformer layer, I expect a significant overhead occurring due to such forward operations compared to RoPE methods.
2. The explanation of propagative refinement is confusing: token pruning is done through a forward pass, and the top-K token embeddings are tracked and obtained only at the top-layer after the entire forward pass. It is unclear to me how the refined embeddings are gathered at the low-level layers, and impact the computation results shown in the ablation in Table 4(b).
3. Minor point: the token pruning section didn’t explain how it is done – it is unclear how the top-K hyperparameter is selected, and the tradeoff between speed and K is made (e.g. keeping a large K at each layer will result in more steps of pruning).

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an approach to extend the context limit of large language models (LLMs). The key idea is to hierarchical context merging, progressively conducting token pruning from bottom to top layers. The token pruning method is simple and training-free, which prunes the tokens with minimal attention from the final token in each chunk, and conducts adjustments (e.g., attention and position bias) to make sure the model to work properly. The results show that it can work on 64k context length without perplexity explosion.

### Strengths
- A training-free method and can be easily adopted
- Some empirical results showing the feasibility of the token pruning method.

### Weaknesses
While this paper presents a seemingly promising approach to long context modeling, its major issue lies in the lack of clarity regarding its use case. According to the paper's description, HOMER first breaks down a long context (e.g., 64k) into N chunks, prunes tokens from each chunk, and finally merges them into a compressed and short context. If this is the case, this method is not suitable for streaming decoding scenarios (where the key-value cache of previously decoded tokens is not recalculated, only new decode tokens are computed).

The key question arises: if this work is not for streaming decoding, then there is no need for such a process. For a 64k length context, wouldn't it be sufficient to ignore the first 62k context and only use the last 2k context? According to the results in Figure 1 of the paper, using only 2k context, the perplexity (PPL) is less than 6 (around 5 point something), whereas after all the effort of merging with HOMER, the PPL is above 8.

Given this, I question the necessity of using HOMER. Using the last 2K context directly seems to yield better results, casting a large doubt on the value of the method proposed in this paper. If the setting of this paper is not for streaming decoding, then the performance of HOMER should at least be better than the PPL of the 2K context. However, this method requires recalculating the key-value pairs for the previous context, which doesn't seem to align with a streaming decoding setting, making it the most confusing aspect for me.

### Questions
See the weakness section

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Paper addresses long contexts (>4k tokens of a pre-trained model such as LLaMA) in LLMs which are challenging because of the nature of Transformer self-attention.
A technique called HOMER is introduced: contrarily to previous approaches that approximate the computation of self attention, or that use position interpolation at inference, authors propose a ‘compression’ method which decomposes the long input into manageable chunks; then a hierarchical merging strategy ensures the ‘communication’  between those chunks. One advantage of the approach is that it does not necessarily require fine-tuning. Perplexity experiments are done to assess the efficiency of the method as well as experiments on passkey retrieval and Q&A tasks. Finally it is shown that the approach proposed can be used successfully in addition to position interpolation techniques.

### Strengths
-a new approach to handling long contexts in LLMs that can be used additionally to position interpolation techniques proposed recently

-extensive experiments done with LLaMA2 (ppl and long-context tasks) and comparison with recent (2023) baselines such as YaRN

-convincing results on both ppl and tasks evaluations

-method is orthogonal to position interpolation methods

### Weaknesses
 -the parts related to propagative refinement (3.2) and efficiency improvement (3.3) should be clarified/improved

-for Q&A it is a pity that HOMER+YaRN results are not presented (+ YaRN seems to not be working well on this task, why?)

-for Q&A i’m wondering if the comparison with YaRN and NTK is really fair as for them, context documents are clipped whereas for HOMER, which is a compression technique, the full context document can be used.

-In 4.4 (ablation) it not 100% clear what the uncalibrated (as opposed to calibrated) pruning criteria is

### Questions
-It is unclear to me why PROPAGATIVE REFINEMENT OF LOWER-LAYER EMBEDDINGS is needed. During inference the final layer representation of the long input is computed so why do you actually need to refine the lower layer embeddings afterwards ? In other words, why do you need to have fixed-length embeddings for every layers afterwards ? I could not fully understand this part.

-Similarly section 3.3 is a bit to laconic to be fully understandable: how this binary-tree inspired computation is innovative ? What is described in Appendix/figure3 seems to me a straightforward way to efficiently compute the hierarchical merging process.

-for Q&A it is a pity that HOMER+YaRN results are not presented (+ YaRN seems to not be working well on this task, why?)

-for Q&A i’m wondering if the comparison with YaRN and NTK is really fair as for them, context documents are clipped whereas for HOMER, which is a compression technique, the full context document can be used.

-In 4.4 (ablation) it not 100% clear what the uncalibrated (as opposed to calibrated) pruning criteria is

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
