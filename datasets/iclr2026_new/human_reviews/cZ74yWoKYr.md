## Human Reviewer 1

### Summary
This paper proposes a plug-and-play method to enhance existing KV cache eviction strategies. Concretely, it heuristically sets a fraction factor α = 0.5: 50% of the KV budget is evicted using an existing method, and the remaining budget is selected based on A*|V|_1 to approximate output perturbation importance. Experiments on LongBench and Ruler show some improvements over baselines.

### Strengths
1. This paper is generally well-written.
2. The performance improvements over baseline methods on Longbench and Ruler are notable.

### Weaknesses
1) The paper claims that recent efforts are empirical and lack formal grounding, and that this work presents a formal study from the perspective of output perturbation. However, reasoning from output error is the most straightforward approach; the reason the field often avoids it is the high computational cost of evaluating A*V. The proposed “formal” method in practice is a heuristic: keep half of the budget with an existing method and allocate the rest via a relaxed A*|V|_1 criterion. Moreover, prior methods such as Quest and MagicPig also consider output-level effects. 

2) Let's go further from last point and discuss the soundness of the proposed method. Quest also uses an approximate A*V to select important tokens, but it is more justified because it makes on-the-fly decisions during inference, step-by-step, conditioned on each incremental output (I'm not asking the authors to compare Quest since its a selection method). By contrast, this paper’s formulation is built around the output of a single token at the end of prefilling. That is naturally aligned with single-turn QA settings like LongBench and ruler where most information resides in the prompt, but it is too narrow for real-world scenarios. In my view, such output-perturbation–based scoring is better suited for cache selection rather than eviction. The paper should include results on datasets like PG-19 and SCBench that feature multi-turn dialogue or long-horizon modeling.

3) Efficiency evaluation is unconvincing. The paper uses time-to-first-token (TTFT) in the prefill phase (including eviction) as the efficiency metric. Under the current evaluation setting, where full prefilling is followed by a one-shot eviction based on some metric, then decoding with the remaining KV, I think the TTFT does not make sense at all.  With one-shot removal, the complexity of the scoring method hardly matters; one could even use a full A*V and see little difference in TTFT compared to what is reported. What would be meaningful is: (a) chunk-wise acceleration during prefilling, or (b) on-the-fly acceleration during long-context decoding. At minimum, please quantify the latency/memory overhead per decoding step for the proposed approximate selection, since Quest found such approximations to be costly and thus opted for block-wise computation.

4) Clarity and presentation. The paper is not that easy to follow. The method is simple enough to be described clearly in a few paragraphs as the core idea is to introduce an approximate A*V to guide the first-step output perturbation for cache eviction. The mathematical proofs seem unnecessary.

5) Naming. The method needs a proper name. Referring to it as “ours” throughout the paper is unhelpful for readers and subsequent citations.

### Questions
Please see the above part.

### Soundness
1

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper presents a formal and theoretically grounded framework for identifying critical Key-Value (KV) cache entries during large language model (LLM) inference. Unlike prior empirical cache-eviction methods that depend solely on attention weights (e.g., H2O, SnapKV, AdaKV, HeadKV), the authors analyze the output perturbation caused by cache compression.
They derive an upper bound on the worst-case perturbation (Theorem 3.3), showing that both attention weights and projected value states (through $W_O$) are essential.
Based on this insight, they design a two-stage perturbation-constrained selection algorithm that can be plugged into existing eviction frameworks.
Experiments on Ruler (13 synthetic long-context tasks) and LongBench (16 real-world datasets) demonstrate consistent performance gains—reducing compression loss by more than half across three models (Llama-3.1-8B, Mistral-7B, Qwen2.5-32B) and three cache-eviction baselines.
The method adds negligible computational overhead.

### Strengths
1. The authors are the first to formalize KV cache criticality through output perturbation analysis. The derivation of an upper bound provides solid theoretical insight missing in prior work.
2. The algorithm integrates seamlessly with multiple state-of-the-art eviction methods (SnapKV, AdaKV, HeadKV) and consistently improves them without modifying their architectures.
3. Extensive experiments on 29 datasets across 3 model families (7B–32B scale) show robust improvements, with detailed ablations over cache sizes, layers, and heads.

### Weaknesses
1. Although Appendix B claims robustness to α, the main paper only presents results for α = 0.5. A sensitivity analysis in the main text would improve credibility.
2. The writing is mostly clear but sometimes verbose. Sections 3.4–3.6 mix implementation and theoretical statements, which could be reorganized for readability.

### Questions
How sensitive is the method to α across very small cache budgets (<10%)?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper first argues that many existing methods reduce the KV cache size by pruning or evicting KV entries that are considered to be less important, relying on attention weights. In contrast, this paper proposes a new perspective: the output perturbation should be the gold metric.  Based on this idea,  the paper aims to find a set of b KV entries, under a given cache budget B, to minimize the output disturbance. Theoretically, this paper shows that it is suboptimal to select key items only depending on attentions, and the influence of V and W^O must be considered at the same time. A two-stage greedy algorithm is proposed to find the critical KV, which is also a plug-and-play module, with negligible computational overhead.

### Strengths
1. Experiments confirm that the algorithm can effectively reduce the output disturbance and provide good performance under different cache sizes.

2. Good writing and illustrations.

3. Comprehensive experiments.

### Weaknesses
1. Some kV entries may be important to maintain long-distance dependency or semantic coherence, even if they contribute little to the l_1 loss of the current output. Could you provide some discussion about this point?

2. The greedy strategy does not guarantee finding the global optimal solution. Could you provide some output L1 result comparisons between the greedy strategy and exhaustive search? Is it possible?

3. The conclusion of the output difference relies on attention weight, V, and W^O is straightforward. However, this article has spent a lot of space proving this, which makes me puzzled.

4. Why must this paper use 50% of the budget to select the KV pair with maximum attention weights? Why not use the adjusted attention containing output differences directly (In Alg. 1)?

### Questions
Please see Weaknesses.

I think this paper is a good paper and the overal logic are self-motivated.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper studies KV cache eviction in LLM inference from an output perturbation perspective. To this end, the authors devised a perturbation-constrained objective to retain token caches that preserve the output distribution. In particular, given a total budget b, the authors divide b into two parts: the first part directly evicts caches with lower attention weights; the second part considers the L1 norm of value cache rows to identify important entries. Experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. The proposed method is plug-and-play and easy to use.  
2. The experimental results show clear improvements over baseline methods.

### Weaknesses
1. Some recent baselines are not compared [1, 2].  
2. I believe the authors' definition of perturbation is too narrow—it is defined only based on the output at the current step, and the proposed method is built on this foundation. However, cache eviction is static. Although the perturbation may be reduced at the current step, the KV cache pruned based on this step's perturbation might become important again in subsequent steps. Therefore, how should the perturbation in future steps be measured? Also, how does the proposed method perform in multi-turn dialogue or ultra-long sequence scenarios?  
3. The proposed method shares strong relevance to Quest [3]. Quest approximates attention computation based on the maximum and minimum KV values, while the proposed method uses the L2 norm for approximation. However, the authors do not provide any discussion or comparison with Quest, even though Quest employs a dynamic selection approach. 
4. The comparison of inference speed is not sufficient. There should be results on acceleration for both 128K pre-filling and inference, similar to the presentation in DuoAttention [1].

[1] DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads. In ICLR, 2025.  
[2] PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling. In Arxiv, 2024.  
[3] Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference. In ICML, 2024.

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4