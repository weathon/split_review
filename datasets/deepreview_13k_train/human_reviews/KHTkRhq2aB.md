# PAFT: A Parallel Training Paradigm for Effective LLM Fine-Tuning

- Decision: Reject
- Scores: 5, 3, 8, 8

## Abstract
Large language models (LLMs) have shown remarkable abilities in diverse natural language processing (NLP) tasks. The LLMs generally undergo supervised fine-tuning (SFT) followed by preference alignment to be usable in downstream applications. However, this sequential training pipeline leads to alignment tax that degrades the LLM performance.

This paper introduces PAFT, a new \textbf{PA}rallel training paradigm for effective LLM \textbf{F}ine-\textbf{T}uning, which independently performs SFT and preference alignment (e.g., DPO and ORPO, etc.) with the same pre-trained model on respective datasets. The model produced by SFT and the model from preference alignment are then merged into a final model by parameter fusing for use in downstream applications. This work reveals important findings that preference alignment like DPO naturally results in a sparse model while SFT leads to a natural dense model which needs to be sparsified for effective model merging. This paper introduces an effective interference resolution which reduces the redundancy by sparsifying the delta parameters. The LLM resulted from the new training paradigm achieved Rank \#1 on the HuggingFace Open LLM Leaderboard\footnote{\url{https://huggingface.co/spaces/HuggingFaceH4/open\_llm\_leaderboard}}. Comprehensive evaluation shows the effectiveness of the parallel training paradigm.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel training approach to perform parallel training of SFT and preference alignment (like PPO, DPO). Their approach aims at solving the problem (e.g., catastrophic forgetting) induced by the traditional sequential training approach (first SFT and then preference alignment).

### Strengths
1. The idea of this paper is interesting and worth being investigated.
2. The proposed method seems to be effective according to the provided results.

### Weaknesses
1. **Unclear motivation towards the inclusion of adapters in the proposed method.**
- The authors should explain why adapters are needed to address the sequential training problem of SFT and preference alignment.
2. **Vague properties abut the proposed approach.** 
- Deeper analysis about the following items should have been included in the paper.
    - The method design
    - Why the proposed method works
    - Improvements over catastrophic forgetting
3. **Limited novelty of the proposed method.**
- The sparse merging actually rely on existing methods.
- The contributions will increase if a customized merging approach is proposed for bridging SFT and preference alignment.
4. Poor formatting of Table 1 and Table 2 (can be fixed).

### Questions
1. How was sparsity discoverd to affect merging process?
2. What do "Ein-70B" and "TextBase-7B" represent in Table 2?
3. The authors performed PAFT on the Neurotic-7B 4 and MoMo-70B models. However, Table 3 does not include the original scores of Neurotic-7B 4 and MoMo-70B before PAFT. Is there a reason behind this?
4. Can the proposed approach work without adapters?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Large language models (LLMs) often go through a sequential training pipeline before deployment, i.e., supervised finetuning (SFT) followed by preference alignment, such as DPO. However, the alignment could lead to performance reduction on some capabilities acquired during pretraining and SFT, namely the alignment tax. This paper addresses this problem by replacing the sequential pipeline with a parallel training pipeline, namely PAFT: it performs SFT and DPO independently based on the same pretrained base model, and then merges them as the final model. The authors observed that increasing sparsity to SFT leads to improved PAFT performance. Through experiments with Mistral and LLama, the authors show that PAFT outperforms sequential training, and achieves top results in Huggingface Open LLM leaderboard.

### Strengths
* PAFT represents a new and interesting post-training paradigm, that performs SFT and DPO independently and gets the final model by merging them;
* PAFT shows improved performance compared to individual SFT/DPO and sequential training;
* Experiments are based on two different LLM families;

### Weaknesses
 * Lack of explanation why pretrained model can be directly used for alignment and leads to excellent performance;
* Experimental setup doesn’t support alignment tax, but SFT tax;
* Evaluation on alignment performance is weak but important;
* Statements are not always supportive and require more experiments

### Questions
1. While independent DPO and SFT sounds interesting, it’s unclear why a pretrained model could be directly used for DPO or alignment. In the literature and in practice, SFT is often used before alignment to make sure the model could produce reasonable responses. More explanation should be given.
2. In Table 1, it’s surprising that DPO alone outperforms SFT and base model by a large margin, which means the alignment doesn’t suffer from tax but improves downstream tasks consistently. This is counter-intuitive and the authors need to provide more convincing analysis.
3. Besides, Table 1 shows that SFT hurts downstream performance. The authors may need to consider changing their experimental setup. Or give the readers more explanations.
4. Major experiments are based on performance on six downstream tasks, which however has little to do with human preferences. It’s unclear how the proposed method affects preference alignment compared to the baselines given in Table 1. Table 3 is the right evaluation direction but no comparisons with the baselines.
5. In the paper, the authors argue that sparsity is an important factor but didn’t show further ablations. What if applying L1 norm to DPO? Would it lead to better performance? What if reducing \lambda in Equation (1) to produce SFT models at different levels of sparsity? Would higher sparsity really lead to better results?
6. In Table 1, SFT-alone and DPO-alone achieve an average score of 60.65 and 63.33 respectively, but the merged model achieves a score of 65.24. Could you provide a simple interpretation where the improvements come from?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose PAFT (Parallel Fine-Tuning for LLMs), a novel training paradigm that fine-tunes large language models (LLMs) by concurrently applying supervised fine-tuning (SFT) and preference alignment rather than sequentially. This parallel approach minimizes the "alignment tax"—the degradation of previously fine-tuned knowledge when preference alignment follows fine-tuning. PAFT further introduces sparsification of the SFT delta parameters using L1 regularization, enhancing the compatibility of both fine-tuning phases during parameter merging. Experimental results show that PAFT outperforms sequential methods, achieving high rankings on benchmarks like the HuggingFace Open LLM Leaderboard and AlpacaEval.

### Strengths
Effective Mitigation of Alignment Tax: PAFT introduces a parallel training paradigm that addresses catastrophic forgetting often caused by sequential fine-tuning. The approach preserves fine-tuning and alignment benefits without performance compromise.
Innovative Sparsification Technique: By applying L1 regularization to the SFT delta parameters, PAFT effectively reduces parameter interference during model merging, resulting in a more efficient and robust model.
Comprehensive Benchmarking: The authors demonstrate the effectiveness of PAFT across multiple datasets and merging methods, establishing its robustness and achieving top performance across multiple tasks.
State-of-the-Art Results: PAFT achieved Rank #1 for specific model sizes on the HuggingFace Leaderboard, demonstrating practical impact and the potential for real-world deployment.

### Weaknesses
Sparse Experimental Analysis on Broader Tasks: While PAFT’s strengths are demonstrated for tasks in NLP benchmarks, additional experiments on diverse domains would enhance the generalizability claims. The current evaluation is limited to NLP tasks and benchmarks; the method's performance on tasks such as vision, speech, or multi-modal data is not explored, which limits the scope of the conclusions. The paper would benefit from an analysis of whether the observed improvements in NLP tasks translate to other modalities or data types.
Limited Baseline Comparison: The study primarily compares PAFT to sequential and standalone training, with minimal inclusion of alternative parallel training strategies. Introducing comparisons with other recent sparse training or parallel tuning techniques could contextualize PAFT's advantages. The paper lacks a thorough comparison with other methods that also aim to mitigate the alignment tax or improve parameter merging, such as methods that use different regularization techniques or parameter update strategies. This makes it difficult to assess the relative novelty and effectiveness of PAFT.
Potential Overhead in Parallel Execution: Implementing parallel SFT and preference alignment could introduce additional computational overhead. An analysis of training efficiency, including any potential increased resource requirements, would be beneficial. The paper does not provide a detailed breakdown of the computational costs associated with the parallel training paradigm, such as memory usage, training time, and energy consumption. This analysis is crucial for assessing the practical feasibility of PAFT, especially for resource-constrained environments.
In-depth Ablation of Sparsity Levels: Additional analysis on different L1 regularization strengths would further clarify the trade-offs between sparsity and performance. The paper only presents results for a limited number of L1 regularization strengths, and it does not explore the full spectrum of possible values. A more detailed ablation study would help to identify the optimal regularization strength and provide a deeper understanding of the relationship between sparsity and performance.

### Questions
Does the parallel structure of PAFT introduce any latency or computational overhead, particularly in real-time or low-latency applications?
What are the effects of varying L1 regularization strengths on downstream performance and model sparsity? A more detailed ablation study could provide insights into optimal settings.
How does PAFT generalize to tasks beyond NLP, such as vision or multi-modal tasks?
Can other forms of preference alignment, such as ORPO, provide similar improvements? Additional benchmarks using ORPO alongside DPO would strengthen PAFT’s applicability.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
1.It shows that parallel training of SFT (Supervised Fine-Tuning) and preference alignment outperforms sequential training, significantly reducing the alignment tax.
2.The paper emphasizes the importance of sparse model integration to prevent model conflict while maintaining the full functionality of each model. It demonstrates that the L1-norm is superior to DARE (Deep Attentional Reinforcement Learning for Exploration) as a more effective and higher-quality method for promoting sparsity in model training across various model merging techniques.
3.The paper provides an extensive evaluation of PAFT (Preference Alignment Fine-Tuning) on renowned public benchmarks, such as the Open LLM Leaderboard and AlpacaEval. The PAFT-optimized 7B model secured the #1 rank in the 7B/8B model category on the Open LLM Leaderboard, and the PAFT-optimized 70B model led the global Leaderboard.

### Strengths
The paper is well-written, providing a new parallel training paradigm called PAFT for fine-tuning large language models, which to some extent offsets the alignment tax caused by sequential training. The large language model produced by this new training paradigm performs excellently, ranking first in the 7B/8B model category.

### Weaknesses
1. There is a lack of brief introductions to the various model merging methods used in the experimental section.
2. Pay attention to the layout, some tables exceed the width limit, such as Table 1, Table 2, and Table 4.

### Questions
1. In Table 1, regardless of whether it is Mistral-7B or Llama-3-8B, the average score of PAFT using the Linear merging method is slightly lower than that of Parallel SFT+DPO, and a similar phenomenon is observed in Table 4. What could be the possible reasons for this?
2. Why does PAFT show such a significant improvement over Parallel SFT+DPO in the TIES and DARE TIES merging methods, while the improvement is not as noticeable in other model merging methods?

### Soundness
3

### Presentation
3

### Contribution
3
