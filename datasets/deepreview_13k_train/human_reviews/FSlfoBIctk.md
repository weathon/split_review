# LOGO --- Long cOntext aliGnment via efficient preference Optimization

- Decision: Reject
- Scores: 6, 6, 3, 6

## Abstract
Long-context models~(LCMs) have shown great potential in processing long input sequences~(even more than 100M tokens) conveniently and effectively.
With significant progress, recent research has pointed out that LCMs can accurately locate token-level salient information within the context.
Yet, the generation performance of these LCMs is far from satisfactory and might result in misaligned responses, such as hallucinations.
To enhance the generation capability of LCMs, existing works have investigated the effects of data size and quality for both pre-training and instruction tuning.
Though achieving meaningful improvement, previous methods fall short in either effectiveness or efficiency.
In this paper, we introduce LOGO~(Long cOntext aliGnment via efficient preference Optimization), a training strategy that first introduces preference optimization for long-context alignment.
To overcome the GPU memory-bound issue caused by the long sequence, LOGO employs a reference-free preference optimization strategy and adopts a position synthesis method to construct the training data.
By training with only 0.3B data on a single 8$\times$A800 GPU machine for 16 hours, LOGO allows the Llama-3-8B-Instruct-80K model to achieve comparable performance with GPT-4 in real-world long-context tasks while preserving the model's original capabilities on other tasks, e.g., language modeling and MMLU.
Moreover, LOGO can extend the model's context window size while enhancing its generation performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces LOGO, a preference optimization training strategy to improve long-context alignment in language models. LOGO uses a reference-free preference objective and a position synthesis method to address memory constraints and efficiently train LCMs. With only 0.3B tokens on limited GPUs, LOGO achieves notable performance comparable to GPT-4 on real-world long-context tasks while preserving other model capabilities.

### Strengths
1. This work is the first to study long-context alignment. The topic and methods are both novel.

2. LOGO can extend the context window of short-context models, allowing for flexible adaptation across various LCM architectures.

3. Experiments on various benchmarks including needle in the hay-stack is promising.

4. The LOGO strategy effectively optimizes LCMs using limited data and resources, achieving comparable results with larger models.

### Weaknesses
1. If we use flash-attention (ring-attention) & deepspeed zero3 cpu offload, it is all right to train Llama-3-8B on 80k context (I already tested it). I think this should be a baseline to compare with the proposed Positional Indices Synthesis. The comparison should include both GPU memory, training hours and accuracy.

2. Would you please try longer context for evaluation? It seems that the longest context is commonly 80k in the paper, which might not be enough this year. For example, qwen2 models is commonly pre-trained as 128k context. It is able to train about 256k context with ring-attention (and the proposed Positional Indices Synthesis).

### Questions
What is the potential for scaling LOGO to models trained on diverse, multi-modal data? For example, long video VLM. I know that this might be hard to resolve in the rebuttal. This is just a discussion.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach to long-context language modeling, leveraging a combination of attention mechanisms and position encoding to improve performance on long-range dependencies. The method shows promising results in improving long-context understanding while maintaining computational efficiency.

### Strengths
-The paper proposes a new attention mechanism that combines the strengths of existing methods. This results in improved performance on long-range dependencies. It also enables efficient handling of long-context training with limited computational resources.

-The authors thoroughly evaluate their method on multiple benchmark datasets. They demonstrate its effectiveness in various settings and show a clear improvement over baseline methods.

### Weaknesses
 -The core idea of using preference optimization for long-context alignment seems like a straightforward extension of existing methods such as DPO and SLiC. The position synthesis method shows similarities to existing techniques like ALiBi and RoPE. The paper's main contribution appears incremental rather than transformative.

-The preference optimization objective (Equation 3) is similar to DPO without significant modification. The position synthesis method lacks theoretical justification for its effectiveness. The training procedure fails to address the fundamental challenges of long-context understanding.

-Experimental Limitations: While the authors compare their method to several existing approaches, the comparison is not exhaustive, and some relevant methods are not considered.

### Questions
1.How does LOGO fundamentally differ from DPO in handling long-context scenarios?

2.What theoretical guarantees can be provided for the position synthesis method?

3.How does the method scale with increasing context lengths beyond 32k tokens?

4.Can you provide detailed analysis of failure cases?

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
4

### Summary
This paper introduces LOGO, a novel training strategy that addresses the challenge of improving long context language models' (LCMs) generation capabilities while maintaining efficiency. While existing LCMs can effectively locate important information in long contexts, they often struggle with generating appropriate responses, leading to hallucinations and misaligned outputs. LOGO tackles this through a reference-free preference optimization approach that teaches models to distinguish between preferred and dis-preferred outputs, combined with an efficient data construction pipeline utilizing positional indices synthesis. The method's key advantage is its resource efficiency - requiring only 0.3B tokens of training data and 16 hours on a single 8×A800 GPU machine - while achieving comparable performance to GPT-4 on long-context tasks and maintaining performance on traditional benchmarks. The authors demonstrate LOGO's effectiveness across various tasks and its ability to extend context windows of existing models while enhancing their generation quality.

### Strengths
Combining preference optimization with long-context alignment addresses a gap in current LCM training methods.
Develops a creative data construction pipeline that effectively creates preference/dis-preference pairs without requiring extensive human annotation
Clear experimental methodology with detailed ablation studies that validate design choices
Well-structured presentation with clear problem motivation and solution development

### Weaknesses
Lack of rigorous evaluation methods for detecting misaligned outputs and hallucinations, which affects the quality assessment of preference/dis-preference pairs
While the paper provides implementation details, the quality of training data could significantly impact results, and the paper uses relatively simple datasets
The theoretical justification for why preference optimization works better than traditional methods in long-context scenarios could be stronger

### Questions
How does LOGO compare with recent baselines such as [1], and methods included in your related work?
Please add comparsion with pipeline using long context and preference optimization, for example LongRoPE[2]&SimPO[3].
Since your contribution focus on long context alignment, please eval it on corresponding benchmark, LongAlign[3].
Could you provide more theoretical analysis such as error bounds for LOGO and analyze its convergence properties?

[1] Zhao, Hao, et al. "Long Is More for Alignment: A Simple but Tough-to-Beat Baseline for Instruction Fine-Tuning." Forty-first International Conference on Machine Learning.
[2] Ding, Yiran, et al. "LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens." Forty-first International Conference on Machine Learning.
[3]Meng, Yu, Mengzhou Xia, and Danqi Chen. "Simpo: Simple preference optimization with a reference-free reward." arXiv preprint arXiv:2405.14734 (2024).
[4] Bai, Yushi, et al. "Longalign: A recipe for long context alignment of large language models." arXiv preprint arXiv:2401.18058 (2024).

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a novel preference alignment method for long-text models, combining position encoding expansion with human preference alignment techniques. For position encoding expansion, the authors propose splitting ultra-long contexts into multiple chunks, applying continuous position encoding within each chunk, and using a jump-based position encoding between chunks to achieve extended position encoding. In terms of preference alignment, the authors generate responses of varying quality by providing different qualities of context, treating higher-quality responses as preferred and lower-quality ones as non-preferred. These are then fed into SimPO for preference learning. Beyond SimPO loss, the authors also incorporate a weighted language modeling loss into the total loss.

Thanks to this unique position encoding expansion approach, the language modeling loss corresponding to strongly relevant contexts is not overly smoothed, thus improving optimization efficiency while reducing issues such as hallucination. On the other hand, the introduction of the powerful SimPO further strengthens the model’s instruction-following ability.

### Strengths
1. Innovative Training Strategy The introduction of LOGO, a long-context alignment method combined with preference optimization, improves the generation capabilities of LCMs.

2. Efficient Training LOGO adopts a position index synthesis method, allowing training to be completed with limited data and resources (8×A800 GPUs on a single machine in 16 hours), significantly improving training efficiency.

3. Significant Performance Improvement In real-world tasks, the Llama-3-8B-LOGO model significantly outperforms GPT-3.5-Turbo and approaches the performance of some top-tier closed-source models like GPT-4, while maintaining strong performance in short-context tasks as well.

### Weaknesses
More controlled experiments should be conducted, comparing the performance of models under the same experimental conditions: (1) using only instruction tuning, (2) using instruction tuning + SimPO (with SimPO’s positive and negative samples that already exist in the training corpus, rather than those generated by policy models or other LLMs), and (3) using the full LOGO method. These comparisons would clarify that the effectiveness of LOGO is not solely attributable to either instruction tuning alone or to the straightforward combination of instruction tuning and SimPO.

Specifically, the paper lacks a clear ablation study that isolates the impact of each component of LOGO. It is unclear how much performance gain is due to the novel position encoding expansion versus the preference alignment with SimPO. The current experiments do not sufficiently demonstrate that the combination of these two techniques is necessary for the reported performance improvements. For example, the paper should include a baseline where only the position encoding expansion is used, without any preference alignment, and another baseline where only SimPO is used with standard position encoding. This would help to quantify the contribution of each component to the overall performance.

### Questions
1.	In the Preference and Dis-preference Data Synthesis section, you mentioned generating preferred data using πθ. Then, in the experimental section, you stated that you used long-llm-data as the training data. As far as I know, long-llm-data already includes standard answers. Did you generate additional answers using πθ beyond these standard answers? If so, what specific model was used as πθ—was it the policy model itself?

2.	You mentioned using long-llm-data as training corpus. To my understanding, this corpus, especially for the single-detail QA, multi-detail QA, and summarization datasets, was already instruction-tuning dataset. So, why do you mention at the end of the Evaluation Settings part that 12,000 data samples from LongAlpaca were used as instruction training data?

3.	Compared to using standard instruction tuning on long-llm-data, how much additional performance improvement does the SimPO loss provide? As far as I know, simple instruction tuning on long-llm-data already yields strong performance on LongBench.

### Soundness
2

### Presentation
3

### Contribution
3
