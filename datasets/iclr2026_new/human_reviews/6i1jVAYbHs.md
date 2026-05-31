## Human Reviewer 1

### Summary
This paper proposes AtlasKV, a parametric knowledge augmentation method designed to integrate billion-scale Knowledge Graphs (KGs) into Large Language Models (LLMs) with extremely low VRAM cost (under 20GB). The core contributions are twofold: 1) KG2KV, a method for transforming KG triples into high-quality Query-Key-Value (Q-K-V) data, which aims to improve generalization by increasing query diversity compared to prior work. 2) HiKVP (Hierarchical Key-Value Pruning), a novel inference-time algorithm that organizes keys into a 3-layer hierarchy, enabling sub-linear ($\mathcal{O}(\sqrt[3]{M})$) time and memory complexity. This allows the model to scale to 1B triples while avoiding the linear cost growth seen in methods like KBLaM.

### Strengths
- Excellent Scalability: The primary strength of this paper is the HiKVP algorithm. It provides a credible path to scaling parametric knowledge augmentation to the billion-fact scale, a task that seems infeasible for prior methods like KBLaM. The experimental results in Figure 4, showing the ability to handle 1B triples with <20GB VRAM while KBLaM fails at 100K triples, are very impressive.

- Strong Generalization and Robustness: The KG2KV method effectively addresses the limited query diversity of template-based synthetic data used in prior work. This is validated by the strong results in Table 3, where AtlasKV (even with pruning) massively outperforms KBLaM on OOD datasets, especially complex ones like ATLAS-Pes20-QKV (e.g., 52.7% vs 5.5% on 10³ triples).

- Addresses a Critical Problem: Efficiently and scalably augmenting LLMs with vast, external factual knowledge is a fundamental goal in AI. This paper tackles this problem head-on with a novel parametric approach that avoids the high inference latency of RAG.

### Weaknesses
- Major Flaw in Experimental Validation: The paper's core premise is that scaling up KGs to 1B triples is valuable. However, the experiments fail to demonstrate this value. Table 3, the primary knowledge grounding experiment, only shows that as the number of "candidate triples" (i.e., noise) increases, performance decreases. This experiment proves "robustness to noise" but critically fails to prove the benefit of "knowledge coverage".
The paper is missing the most crucial experiment: a comparison between a small KG and the large KG on a set of questions where the answers only exist in the large KG. Without this, the motivation for the entire paper—scaling up—is left as an unsubstantiated assumption. As it stands, the experiments show that scaling up (the candidate pool) only hurts performance.

- Unaccounted LLM Cost & Unfair Comparison: The KG2KV method (Section 4.1, Appendix H) relies on external, powerful LLMs (GPT-4o-mini, and the authors state in Appendix I that Claude-4-sonnet was used for development) to transform KG relations into natural noun phrases. This introduces a significant, one-off (but potentially massive) computational and/or API cost for preprocessing the 1B+ triples. This cost is completely ignored in the paper's efficiency analysis. This makes the comparison to methods like KBLaM, which uses simple synthetic templates, an unfair, apples-to-oranges comparison. The scalability of AtlasKV is thus partially achieved by offloading significant complexity to an external, unmeasured LLM.

- Loss of Graph Structure: The KG2KV method inherently "flattens" the knowledge graph, treating each triple as an independent fact. This sacrifices all topological/structural information of the KG, limiting the method to one-hop retrieval and precluding multi-hop reasoning. This is a significant trade-off that should be more explicitly acknowledged and discussed as a limitation.

### Questions
- Could the authors provide an experiment that demonstrates the value of "knowledge coverage"? For example, by comparing a model trained on a 1M-triple KG vs. a 100M-triple KG on a set of questions where the answers only exist in the larger KG? This seems essential to justify the paper's core motivation.

- Can the authors quantify the computational cost (e.g., in GPU hours or total API costs) of the KG2KV preprocessing step for the 1B-triple ATLAS-Wiki dataset? How does this one-off cost compare to the training/inference costs, and how does it affect the overall efficiency claim?

- The performance of AtlasKV with HiKVP is notably lower than AtlasKV without HiKVP (e.g., Table 3, ATLAS-CC-QA, 10³ triples: 74.5% vs 96.4%). This suggests the hierarchical pruning is quite lossy. Have the authors explored strategies to mitigate this precision drop (e.g., different top-k values, as hinted at in Appendix B.2), or is this considered an acceptable trade-off for the achieved scalability?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes a relatively systematic optimization framework to address the high computational complexity of knowledge-augmented large language models (KG-augmented LLMs). It provides both theoretical and experimental analyses of the model’s time and space complexity as well as GPU memory consumption, showing a certain level of exploratory research value. The designs of the hierarchical knowledge base and Rectangular Attention modules are instructive. In addition, the authors present relatively complete complexity derivations and visualization results, which enhance the technical rigor of the work.

### Strengths
1. **Novel and principled framework:**

The transformation from KG triples to Q-K-V structures is conceptually elegant and theoretically aligned with transformer attention, effectively bridging symbolic and neural representations.

2. **Scalable design and sub-linear efficiency:**

The hierarchical pruning mechanism (HiKVP) achieves sub-linear time and memory complexity, making it feasible to integrate billion-scale KGs in limited VRAM environments.

3. **Strong empirical results:**

Extensive experiments demonstrate clear improvements in both knowledge grounding and generalization, with substantial reductions in memory cost compared to KBLaM and RAG.

### Weaknesses
1. The methodology section is difficult to follow. The main issue is that many symbols are not clearly defined. For example, the meaning of $S$ on Line 253 and the correspondence of variables in Eq. (3) and Eq. (13). In addition, the paper does not state the model’s optimization objective, which further increases the burden on readers trying to understand the work.

2. The paper’s primary contribution appears to be complexity optimization for KG-augmented LLMs. However, relying solely on time/space complexity analyses and VRAM accounting is not sufficient to fully assess this advantage. For instance, when performing top-k pruning over a hierarchical KB, switching among three levels of keys can induce frequent CPU–GPU I/O, which is a non-negligible hardware latency during real-world training/inference. I recommend discussing this overhead explicitly.

3. Missing parameter sensitivity analysis. To my knowledge, Rectangular Attention in KBLaM is not invoked at every LLM layer; it is typically applied every few layers. I could not find this setting in the main text (it might be in the appendix, which I may have overlooked). Moreover, the paper does not provide any rationale or analysis for such a setting.

4. Why three hierarchy levels? The choice of a 3-level hierarchical key-value cache is insufficiently justified. Please add more detailed theoretical or empirical support for this design choice.

5. Inter-level correlation in top-k selection is not clear. Are the top-k selections across different hierarchy levels correlated? Figure 6 only shows the variation of a single variable. Given that top-k pruning at an upper level can influence the quality of pruning at the next level, an experimental analysis of this inter-level dependency seems necessary.

6. I am curious about the appendix proof of equivalence for Rectangular Attention. It appears to be largely a distributive rearrangement of matrix operators that, in practice, does not change the computed result. Please provide a deeper explanation of its effectiveness. Alternatively, clarify whether this operator manipulation merely serves as an algebraic device to facilitate subsequent complexity analysis for hierarchical key-value computation.

### Questions
Please See weakness

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper proposes AtlasKV, a parametric method for integrating billion-scale KGs into LLMs without external retrievers, long contexts, or retraining.

It addresses limitations of non-parametric RAG (latency, retrieval bottlenecks) and traditional parametric methods (retraining costs, poor scalability)

Key innovations include KG2KV, which converts KG triples into query-key-value (Q-K-V) data aligned with LLM attention mechanisms, and HiKVP, a hierarchical pruning algorithm for sub-linear time/memory complexity during inference.

Experiments demonstrate superior empirical performance.

### Strengths
1. AtlasKV shifts from retrieval-heavy RAG to parametric KG injection, enabling training-free adaptation to new KGs. This idea is both novel and practical.

2. The method is well-motivated, with clear formalisms for KG2KV and HiKVP. Such formulation maintains generalization without fine-tuning.

3. Results show strong gains in knowledge-intensive tasks.

### Weaknesses
1. HiKVP's pruning is efficient, but lacks formal guarantees or error analysis. 

2. Lack comparison with GraphRAG algorithms, such as HippoRAG and Raptor. I understand the focus of this work is on large KGs, where existing graphRAG algorithms can struggle to handle especially for indexing latency and token consumption. But comparing with them on small datasets can benefit the understanding the pros and cons of these methods.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper introduces AtlasKV, a parametric knowledge integration framework for large language models (LLMs) that enables augmentation with billion-scale knowledge graphs (KGs) under modest GPU memory budgets (<20GB VRAM). The method converts KG triples into query–key–value (QKV) training data aligned with LLM attention structures. It also employs a hierarchical key–value pruning algorithm that reduces computational and memory overhead while preserving grounding accuracy. Extensive experiments on large-scale KG datasets (ATLAS family, Enron, etc.) demonstrate that AtlasKV outperforms both non-parametric RAG methods and parametric baselines (e.g., KBLaM) in terms of scalability, knowledge grounding, and generalization to out-of-distribution (OOD) queries.

### Strengths
- The combination of KG2KV and HiKVP is elegant, bridging symbolic KG structure with LLM attention in a natural way.

- The proposed method demonstrates integration of 1B triples with <20GB VRAM, a significant improvement over KBLaM (>40GB for 100K triples).

- Experiments across multiple datasets (ATLAS-CC, ATLAS-Pes2o, Enron) with ablations (entity vs. event masking, pruning strategies, encoders) show the effectiveness of the method.

### Weaknesses
- KG2KV requires relation rewriting (e.g., "because" -> "cause"), which relies on external LLMs. This introduces dependency on external models and may limit reproducibility.

- The baselines are strong (KBLaM, RAG), but newer lightweight RAG variants (e.g., caching-based or hybrid symbolic-neural methods) are not included.

- The claim that only 20K KG2KV samples suffice for generalization is intriguing, but more discussion is needed on why such small-scale training suffices for billion-scale integration.

### Questions
- How sensitive is AtlasKV to the quality of relation rewriting in KG2KV? Could noisy or ambiguous relations degrade performance?

- How does AtlasKV handle evolving KGs (e.g., streaming updates)? Is retraining or re-encoding required?

- Could AtlasKV be combined with lightweight retrieval (hybrid parametric + non-parametric) for further efficiency gains?

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