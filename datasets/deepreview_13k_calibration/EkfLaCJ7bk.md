# TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Large language models (LLMs) have driven significant advancements across diverse NLP tasks, with long-context models gaining prominence for handling extended inputs. However, the expanding key-value (KV) cache size required by Transformer architectures intensifies the memory constraints, particularly during the decoding phase, creating a significant bottleneck. 
Existing sparse attention mechanisms designed to address this bottleneck have two limitations: (1) they often fail to reliably identify the most relevant tokens for attention, and (2) they overlook the spatial coherence of token selection across consecutive Transformer layers, which can lead to performance degradation and substantial overhead in token selection. 
This paper introduces \Sys, a simple yet effective algorithm and system for fast and accurate LLM decoding through position persistent sparse attention. \Sys leverages the spatial coherence of tokens selected by existing sparse attention methods and introduces a few token selection layers that perform full attention to identify the tokens with the highest attention scores, while all other layers perform sparse attention with the pre-selected tokens. 
This design enables \Sys to substantially reduce the overhead of token selection for sparse
attention without sacrificing the quality of the generated results.
Evaluation on a diverse set of LLMs and tasks shows that \Sys{} closely matches the generative performance of full attention methods while reducing the LLM decoding latency by up to $2.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces TidalAttention, which uses a layer-wise selection approach to choose the top-k keys and values needed in top-k attention, thereby reducing the amount of KV cache requiring I/O.

### Strengths
The advantages of this paper are as follows:

1) The logic is very clear, and the writing is well-structured. The figures and captions are precise, making it easy for readers to quickly understand.


2) The focus of the paper is excellent, and I completely agree with it. Particularly with group query attention, KV cache storage is no longer a major issue; instead, the I/O for the KV cache in attention deserves attention. And I really like the mechanism cache correction.


3) Most of the experiments are solid, although there is room for improvement. And the cuda kernel is good.

### Weaknesses
I think the paper has the following limitations or raises some questions for me:

1) I believe there may be an issue with the dataset selection in the experiments. Since the authors’ method retains the full KV cache as opposed to KV cache eviction, it would be best to evaluate on datasets with longer outputs. If the dataset only outputs one token, as in NIAH, there should be no difference between eviction-based and selection-based sparse methods, which doesn't highlight the importance of maintaining the full KV cache. Additionally, some QA datasets in LongBench also have this issue. I recommend that the authors supplement more summarization datasets from LongBench (such as gov_report) and code completion datasets (like LCC and repo-bench).


2) The authors claim that their kernel stores dot product instead of attn score, so I just wondering how this method works for group query attention. How can the authors decrease the IO of gqa if the queries in the same group with different top-k?


3) The authors’ description of Quest is not very clear, and it would be beneficial to add citations for previous baselines in the tables.

### Questions
see cons.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduce a decoding method for sparse attention with pre-selected tokens. The method essentially performs full attention at lower layers and sparse selective attention at the upper layers to obtain the selected tokens, and then full-attention on reduced sets of tokens in the highest layers. The paper presents experiments to show that TidalDecode is competitive to full attention decoding while reducing latency.

### Strengths
- The paper presents an optimization strategy to improve speed and latency by recognizing that the selected tokens in sparse attention remain consistent across layers, so that the selection process may only need to happen in lower layers.
- The paper presents evaluation to show the method is competitive to some baselines on latency evaluation

### Weaknesses
 - The writing and presentation of the paper significantly need improvement. There are too much unnecessary underlined texts.
- The motivation and introduction are written unclearly, with too much irrelevant introductional texts.
- The preliminary and methodology are written in confusing ways. There is a need to put clearer definition and better writing. 

### Questions
NA

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
This article introduces a new sparse attention mechanism, TidalDecode, which is an efficient selection-based attention computing mechanism for the second stage of LLM inference, specifically the decoding stage. The authors discovered through empirical experiments that there is a significant overlap among the Top-K tokens in the attention scores between consecutive Transformer layers. Thus, they propose performing full attention computation only in the initial and intermediate layers, while the other layers select the most relevant KV-cache to compute attention, achieving an efficient sparse attention mechanism. Experimental results across diverse LLMs and tasks demonstrate significant improvements in both decoding latency and the quality of generated results. The optimal choice of the token re-selection layer is consistent across different tasks if the model belongs to the same model family.

### Strengths
1.The article is written in a clear and comprehensible way, with strong consistency across empirical experiments, motivation, methodology, and the effectiveness of the proposed method.
2.The method is simple yet effective, supported by extensive experimental and theoretical validations. A wide range of diverse experiments, including multiple LLMs and tasks, demonstrates the excellent performance of the proposed method.

### Weaknesses
1.The chosen token across different tasks for the same model family is almost consistent; however, the dramatic variation in performance between L12 and L13 in Table 7 presents a significant challenge for the method's generalization across different models and datasets. This variability, specifically the sensitivity to a single layer difference, raises concerns about the robustness of the method and its potential for catastrophic failure when applied to unseen data or model architectures. The lack of a clear understanding of why this specific layer is optimal, and the potential for this to shift with different data distributions, makes the method's practical application risky. 
2.Regarding Figure 2a, the overlap results, while present, do not appear substantial enough to justify the claim of significant redundancy in attention patterns across layers. The visual representation suggests a modest overlap, and without a more detailed quantitative analysis of the attention weights and their contribution to the final output, it is difficult to assess the true impact of this overlap. The lack of consideration for the magnitude of attention scores associated with the overlapping tokens further weakens the claim. A more rigorous analysis, beyond simple token overlap, is needed to validate the core motivation of the method.

### Questions
1.Building on Weakness 1, an adaptive layer selection strategy seems necessary. Did the authors explore any strategies in this regard?
2.I am quite curious about the actual application effects of KV Cache Correction. Were corresponding experimental validations conducted?
3.In Table 3, it is interesting to note that on certain datasets like HotQA, the sparse attention mechanism sometimes outperforms the full attention mechanism. Is there a relevant explanation for this, or an empirical rationale behind it?

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
The paper presents TidalDecode to enhance the efficiency and accuracy of large language models (LLMs) through position persistent sparse attention. TidalDecode introduces token selection layers to identify and retain the most relevant tokens, with other layers using sparse attention to manage memory and reduce computational demands. Empirical evaluations indicate that TidalDecode can achieve up to a 2.1× reduction in latency while maintaining comparable generative performance to full attention mechanisms.

### Strengths
The proposed method is effective, maintaining the advantages of both eviction and selection-based sparse attention methods according to experiments.
The paper presents robust evaluations across various LLMs and tasks, including LongBench and Needle-in-the-Haystack tests. Results indicate that TidalDecode consistently performs well compared to state-of-the-art methods.

### Weaknesses
1. Definition of `spatial coherence`. The spatial coherence seems just come from nowhere. I can mostly understand it refers to the consecutive layers have significant attention overlaps. But there is not a `scientific definition` in this paper.
2. Complexity of Implementation: TidalDecode's reliance on custom GPU kernels and specific layer configurations could limit its accessibility and adoption. Please provide pseudo code or GPU consumption data, it could make the results more clear.
3. The proposed method can be considered as a kind of hierarchical attention, more related baselines can be included. such as [1,2]
4. KV-cache correction seems to be crucial, no ablation study (or I just missed). Please provide the results without KV-cache correction.
5. training details, e.g, learning rate, training tokens, GPU hours, etc. It would help the reproduction.
6. Does `L` matter in different models? How to determine the optimal hyper-parameters. It would be appreciated if automatic prediction of `L` or a guideline for `L` selection across different model size, model architecture, etc.
7. There might be some conflicts in the packages used in latex.

### Questions
Please see weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
