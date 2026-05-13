# Stated Causal Language Modeling: Off-the-Shelf Enhancement of Context Memorization

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
We propose stated causal language modeling (stated-CLM), a novel method to enhance the memory capacity of large language models (LLMs) without modifying their architecture or parameters. Unlike existing context segmentation and sliding methods that discard low-weight tokens, stated-CLM compresses adjacent tokens, significantly reducing context information loss. We utilize the classic network pruning techniques with second-order derivatives to optimize the compressed token in the differentiable key-value space. Experiments on LLaMA, Mistral, and Gemma demonstrate that stated-CLM outperforms baselines on the LongBench benchmark by an average of 6.12\% (LLaMA3.1-8B) and 5.97\% (Mistral-v0.3-7B). On TopicRet, stated-CLM achieves accuracy levels comparable to full context models, while the baselines' accuracy is close to zero.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces "Stated Causal Language Modeling" (stated-CLM), a novel approach to enhance the memory capacity of large language models (LLMs) without modifying their architectures or parameters. The method aims to address limitations in LLMs' context length and computational complexity by compressing rather than discarding low-weight tokens. Using techniques inspired by network pruning, stated-CLM compresses adjacent tokens into a single token, preserving critical context information while maintaining memory efficiency.

### Strengths
1. Innovative Approach: The proposed token compression approach enhances memory without architecture changes, a clear advantage over existing context segmentation methods.
2. Efficiency in Context Compression: Stated-CLM reduces memory usage while preserving essential information, enabling longer context retention compared to traditional methods.
3. Strong Performance: Experimental results on multiple benchmarks, including LongBench and TopicRet, show a marked improvement over baselines in memory and retrieval tasks.
4. Applicability Across Models: The method was tested on LLaMA, Mistral, and Gemma architectures, illustrating versatility across different LLMs.

### Weaknesses
1. One potential weakness is the paper’s limited exploration of the trade-offs between compression rates and downstream performance across a wider variety of tasks. While the LongBench and TopicRet benchmarks cover important aspects of long-context retention, it would strengthen the paper to evaluate stated-CLM on additional tasks that may reveal specific limitations in high-compression settings, such as more complex QA or summarization tasks. 
2. The paper briefly mentions that low-weight tokens can still affect prediction outcomes, yet it does not quantitatively analyze the impact of compressing such tokens on information loss. To make this assessment more actionable, the paper could add metrics that measure the fidelity of compressed representations relative to uncompressed sequences. Additionally, examining token dependencies—particularly in sequences where tokens have subtle but cumulative importance—would reveal potential blind spots in the compression approach.

### Questions
1. How does stated-CLM handle information loss from compressed tokens, especially for tasks with subtle context dependencies? Can the authors provide more insight into the impact of compressing low-weight tokens on prediction accuracy?
2. What factors influenced the selection of specific hyperparameters (e.g., sink length and chunk length), and how adaptable are these parameters? It would be useful to understand why specific values were chosen for sink length, chunk length, and other hyperparameters, as well as any experiments the authors conducted to tune these parameters.

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
4

### Summary
The work explores the problem of long-range language modeling. The key idea is to compress adjacent pairs of tokens into single tokens, by which both the length of context and the information loss from compression are controlled. The authors derived a principle approach to estimate the tokens as compression of adjacent tokens. Experiments are conducted on LongBench and L-Eval with promising results. 

To the best of my knowledge, the proposed method is new in the research of long-range modeling. The empricial results, in terms of both efficacy (e.g., Table 1) and efficiency (e.g., Figure 3) are significant. In addition to these ``pros'', I have concerns as follows:

1. Though the authors provide empricial studies to show the advantage of the method in terms of efficiency, I think a formal and rigid complexity analysis is needed, as the method needs complicated extra computation in each layer and for each input sequence (correct me if I am wrong).  Without such analysis, it is confusing why the method can scale linearly with respect to context length in inference (cf., Figure 3). 

2. When do you perform compression? In each step of pre-training? or just in inference? More implementation details are needed.

3. The method is also related to LLMLingua (https://github.com/microsoft/LLMLingua) and Retrieval Pre-trained Transformer (https://arxiv.org/abs/2306.13421). The results could be more solid if these methods are involved in comparsion. 

4. Proof-reading is needed. Typos like "manuplate" in line 153 and grammar errors like "we the..." in line 197 are annoying.

### Strengths
1. New approach to long-range language modelling
2. Impressive empirical results on benchmarks.

### Weaknesses
1. Some necessary details are missing. 
2. Typos and grammar errors are annoying.

### Questions
1. Is the assumption of "cross parameter interactions are negligible (another typo in the draft...)" too strong for parameter estimation?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Stated-CLM, by compressing adjacent tokens, retains contextual information to enhance memory and supports long contexts without the need for additional training. Extensive experiments have demonstrated the advantages of Stated-CLM relative to baselines.

### Strengths
1. The writing is good.
2. The article validates the advantages of Stated-CLM over multiple baselines, providing extensive experimental results.
3. The author provides relatively detailed mathematical derivations for the proposed method.

### Weaknesses
1. This paper’s main weakness, in my view: The paper emphasizes its benefits in "**CONTEXT MEMORIZATION**," but the compared baselines (StreamingLLM and LongCache) lack memory capabilities, so the experimental results are bound to be better. There are many memory-capable methods that support long contexts without requiring training, such as THINK [1], StreamingDialogue [2], and SampleAttention [3]. The paper lacks both a performance comparison with these types of methods and a comparison of space and time complexity.
2. Stated-CLM seems to struggle with very long inputs. Assuming the context window is 2,048 tokens and the input is 10,000 tokens, it would require an initial stated-CLM run to compress the tokens down to 5,000, then another compression to 2,500, and this process would need to be repeated until it is reduced to within 2,048. This is costly and cumbersome.
3. Stated-CLM does not support streaming generation. Section 3.4 indicates that this method must pause after generating a certain number of tokens to perform a stated-CLM step.


**Reference**

[1] THINK: THINNER KEY CACHE BY QUERY-DRIVEN PRUNING

[2] StreamingDialogue: Prolonged Dialogue Learning via Long Context Compression with Minimal Losses

[3] SampleAttention: Near-Lossless Acceleration of Long Context LLM Inference with Adaptive Structured Sparse Attention

### Questions
More comparisons are needed to evaluate the effectiveness of stated-CLM.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces a novel training-free approach, Stated-CLM, to enhance the LLMs' capability to memorize contextual information and process long input sequences. The approach compresses the key and value representations of adjacent tokens that receive less attention. Optimal compressed representations, which maintain prediction consistency before and after compression, are calculated using second derivatives under certain assumptions inspired by prior network pruning techniques. Experiments conducted on both LongBench and TopicRet demonstrate the favorable performance of Stated-CLM over StreamingLLM and LongCache across several backbone LLMs.

### Strengths
1. The paper is clearly written and easy to follow.
2. The proposed approach is well-motivated, and supported by theoretical analysis based on specific assumptions.
3. The author did extensive experiments on six LLMs to validate the effectiveness of the proposed approach. The analysis indicates the superior performance of Stated-CLM over baselines under various compression ratios and shows the linear relationship between time cost and context length of compression methods.

### Weaknesses
The baselines utilized in this work are relatively weak. More competitive baselines, such as InfLLM[1] should be incorporated.

[1] InfLLM: Unveiling the Intrinsic Capacity of LLMs for Understanding Extremely Long Sequences with Training-Free Memory

### Questions
The author posits that “CLMs have seen samples similar to the current input during large-scale pre-training, their gradients gm, gm+1 tend to be zero”. Does this assumption potentially compromise the model's generalization ability in in-domain scenarios or with more recent data? More discussions are expected.

### Soundness
3

### Presentation
4

### Contribution
3
