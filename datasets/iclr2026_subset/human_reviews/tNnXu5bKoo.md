## Human Reviewer 1

### Summary
The paper introduces FuseGPT, a structured pruning paradigm that reframes block removal as "prune-and-fuse" knowledge redistribution. The method uses a Macro Influence (MI) metric to identify absorbable blocks and a learnable low-rank fusion mechanism to inject their knowledge into neighbors.

### Strengths
1. The "prune-and-fuse" paradigm is a creative conceptual departure from standard "prune-and-retrain" approaches, as it attempts to recycle, rather than discard, the knowledge within pruned blocks.

2. The implementation of knowledge transfer via learnable low-rank matrices to fuse weights into neighboring layers is a technically sound and clearly described mechanism.

### Weaknesses
1. Computational Cost of Compression: The iterative "prune-one-by-one" approach, which requires re-computing importance scores (MI) and performing local adaptation for each block being removed , is acknowledged as computationally intensive. This high one-off cost to compress the model is a significant drawback compared to one-shot pruning methods.

2. Local Fusion Heuristic: The fusion mechanism is restricted to a local partial group of neighboring blocks (size $G=7$), based on an assumption of functional similarity between adjacent blocks. This heuristic may be sub-optimal if a block's knowledge is more relevant to a functionally similar but distant block, a possibility the paper does not explore.

3. "Fusion-Aware" Metric: The paper claims the MI metric is "fusion-aware" and identifies blocks by their "capacity to be effectively absorbed". However, the metric itself is calculated by measuring the impact of removal (cosine similarity on final hidden states), which primarily identifies redundancy. The link between low redundancy and high "fusibility" is an inference, not a direct measurement provided by the metric.

4. While FuseGPT marginally outperforms other pruning methods, it still incurs a catastrophic >11-point drop in zero-shot performance on LLaMA-2-7B at 25% sparsity. This severe degradation in capability makes its 1.33x speedup  an unacceptable trade-off, raising doubts about its practical utility.

### Questions
1. Compression Cost: Could you quantify the total computational cost (e.g., in GPU-hours) required to compress LLaMA-2-7B to 25% sparsity using FuseGPT? How does this one-off cost compare to the cost of one-shot methods like SLEB or SliceGPT, combined with a standard (non-local) fine-tuning run needed to achieve their reported results?

2. Iterative vs. One-Shot Fusion: The iterative process is a clear bottleneck. Have you experimented with a "one-shot" version of FuseGPT, where the $N$ blocks with the lowest-MI scores are identified once, and then all fusions are performed simultaneously (or sequentially without re-scoring)? How much performance is lost in this more efficient scenario?

3. Local vs. Global Fusion: To test the local fusion assumption, have you considered an alternative? For example, identifying the $G$ most similar blocks (e.g., by feature or weight similarity) in the entire network as fusion targets, rather than just the immediate neighbors? This would test the hypothesis that adjacent blocks are indeed the optimal recipients.

4. Group Size Sensitivity: The partial group size was fixed at $G=7$. How sensitive is the final model's performance to this hyperparameter? What is the trade-off between a larger $G$ (more computational/memory cost during adaptation) and the quality of the fused model?

5. Rationale for Updating $W_{i,j}$: During the fusion fine-tuning (Eq. 4), the pruned block's weights $W_{p,j}$ are frozen, but the neighboring block's weights $W_{i,j}$ and the coefficient $C$ are updated. What is the rationale for updating $W_{i,j}$ (via LoRA )? Does this not risk degrading the neighbor block's original knowledge? What happens if you only train the fusion coefficients $C$ and keep all original weights ($W_{i,j}$ and $W_{p,j}$) frozen?

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

---

## Human Reviewer 2

### Summary
The paper suggests a new block-wise compression approach for LLMs which iterates on block/layer dropping. 
Specifically, the authors propose a new "MI" metric for layer dropping, and combine it with a "fusion" approach by which a removed block is "fused" into its neighbors by retraining. 
Experiments on fairly standard datasets are provided, suggesting that FuseGPT works better than prior dropping methods such as ShortGPT, and various ablations on components of the method.

### Strengths
- The paper provides a new solution to a standard efficiency problem.

### Weaknesses
- The solution is a fairly complex heuristic. 
- The speedups are quite small for the amount of accuracy that is dropped. 
- Some of the choices made, for instance in the metric choice, appear questionable.

### Questions
There are two major shortcomings to the work, in my view.

1. The first is that its assumptions regarding the metric appear to be invalid. Specifically, one basic assumption behind the work is that compression can be done iteratively, by ranking via the MI metric, followed by removal and fusion. This assumes that there exists a monotone metric hat can be applied to blocks, with the property that minimizing the metric upon removal would minimize the accuracy loss. 
However, to my understanding, the EvoPress, work (https://arxiv.org/abs/2410.14649) shows that the assumption of monotonicity is _invalid_ for DNN pruning, there exist configurations where pruning more leads to _lower_ accuracy loss (possibly due to redundancy, co-dependence, or other phenomena that we don't understand). As such, the authors argue that search is the correct approach, and that no monotone metric is "correct" given that it's based on an invalid assumption. Moreover, the authors provide quite good results for layer dropping, which seem to be SOTA.
Can the authors position their work relative to EvoPress, and explain why this isn't cited? 

2. The second significant weakness is that the accuracy drops are really major, especially for such a complex method. From a deployment perspective, the models would be unusable. (E.g. a 2-point PPL increase for 33% speedup improvement.) 
Can the authors explain why one would use their method on a recent model family (e.g. Qwen3) rather than just pick the next smallest model from the model family? Their technique does not appear to be Pareto-competitive in terms of size-vs-accuracy.

### Soundness
1

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
In my understanding, FuseGPT proposes a structured pruning approach for large language models that merges redundant transformer blocks rather than simply discarding them. The method works in three steps: (1) identify the least important block using a "Macro Influence" (MI) metric that measures how much removing a block perturbs the final hidden states. (2) For each block, fuse that block's parameters into neighboring blocks using learnable low-rank coefficients. (3) Perform lightweight fine-tuning on a partial group of blocks around the removed one using KL divergence loss. This specific cycle will repeat iteratively until reaching the target compression rate. The core insight is that redundant blocks still contain valuable knowledge that can be redistributed to neighbors before removal.

### Strengths
Clarity in presentation and motivation: The paper is well-written and easy to follow. The motivation for knowledge redistribution over simple deletion is intuitive and well articulated. The progression from problem statement through methodology to results flows logically.


Figures and tables: Figure 1 provides an excellent visual comparison showing how FuseGPT differs from unstructured, channel-wise, and block pruning. Figure 2 clearly illustrates the partial group update mechanism. Tables are comprehensive and self-explanatory, with consistent formatting that facilitates cross-method comparison.


Problem significance: Post-training compression of large language models is critically important for deployment today in our resource-constrained environments. Methods that preserve performance while reducing computational requirements have substantial practical value, especially as models continue to scale. Additionally, the fact that this method is not training is super critical.

### Weaknesses
W1: Novelty

W1A: MKA
The paper completely omits "Pruning via Merging: Compressing LLMs via Manifold Alignment Based Layer Merging" (Liu et al., arXiv:2406.16330, EMNLP 2024, June 2024). This is a major issue because: (a) MKA predates FuseGPT by and implements layer fusion/merging as its core mechanism, (b) In the paper, MKA reports better results than FuseGPT (43.75% compression on Llama3-8B with only 2.82% MMLU drop versus FuseGPT's 25% compression). The novelty claimed for this work is significantly undermined without addressing MKA. Authors must  provide head-to-head comparison, and explicitly articulate what FuseGPT contributes beyond MKA's approach(both experimentally and in theory).


W1B: Layer Merging in Other methods
Even with cited work like LaCo, the paper doesn't adequately explain how FuseGPT's low-rank coefficient fusion differs from or improves upon existing layer merging approaches (such as LaCo's RDSC). The technical distinctions remain unclear.


W2: Evaluation on older/outdated architectures. 

Experiments focus on LLaMA-2 (2023), LLaMA-3 (early 2024), and LLaVA-1.5, while recent pruning papers evaluate on LLaMA-3.1, Mistral NeMo, Phi-3.5, and Qwen models. This is not sufficient an ICLR 2026 submission; including more recent architectures strengthen generalization claims.


W3: Wall clock/GMacs

The paper claims "lightweight" fine-tuning but provides no wall-clock time comparisons or even GMacs. For a pruning/compression paper, it is super important.

### Questions
Q1: How does FuseGPT compare to MKA on the same setup?

Q2: What is the computational overhead versus MKA's progressive merging or one-shot methods?

Q3: Can you provide results on LLaMA-3.1 or other recent (2024) architectures?

### Soundness
2

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
3