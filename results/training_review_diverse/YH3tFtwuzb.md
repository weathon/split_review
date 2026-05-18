Now I have enough information to write the consolidated review. Let me synthesize everything carefully.

---

## Summary

This paper proposes DP-BiTFiT, a differentially private fine-tuning method that optimizes only the bias terms of pre-trained neural networks. The key insight is that bias gradients do not require storing the per-sample input activations needed for weight gradient computation, which eliminates the dominant memory and time bottlenecks of DP training. The paper provides a systematic complexity analysis of DP PEFT methods (a missing piece in prior work), extensive accuracy evaluations across language and vision tasks, and scalability benchmarks showing 2–30× speedups and 2–8× memory savings over DP full fine-tuning while maintaining competitive accuracy.

## Strengths

1. **Serious computational efficiency advantage rigorously demonstrated.** The paper's complexity analysis (Tables 5/6 in the paper's numbering) shows that DP-BiTFiT's DP overhead is independent of the feature dimension $T$, unlike every weight-based method (full, LoRA, Adapter, Compacter) whose DP overhead scales as $O(T)$ or $O(T^2)$. This is validated empirically: on RoBERTa-base with SST2 (sequence length 512), DP-BiTFiT uses ≈6 GB GPU memory vs. ≈20 GB for DP full fine-tuning, and this gap widens dramatically with input dimensionality (Figure 2). The analysis also shows DP-BiTFiT is 1.5× faster than *non-private* full fine-tuning and 2× faster than DP full fine-tuning.

2. **Competitive accuracy across diverse tasks and model architectures** despite training only ≈0.1% of parameters. On RoBERTa-large (ε=8), DP-BiTFiT achieves 94.5% on SST2 (DP LoRA: 95.3%), 91.1% on QNLI (ties DP full), and 88.3% on MNLI-m (best among all DP methods). On GPT2-large E2E, DP-BiTFiT achieves BLEU 65.21, outperforming DP full fine-tuning's 64.64. On CIFAR10 with ViT-large (ε=2), it achieves 99.0% (DP full: 98.9%). The performance gap between BiTFiT and full fine-tuning consistently shrinks as model size increases (Remark 1, line 321).

3. **First systematic complexity analysis of DP parameter-efficient fine-tuning.** The paper provides a per-layer breakdown of time and space complexity for DP full, LoRA, Adapter, and bias training — an analysis explicitly identified as missing in prior DP and non-DP PEFT literature. This framework rigorously explains *why* DP-BiTFiT's efficiency advantage grows with input dimensionality and model size.

4. **Model-agnostic and trivial to implement.** DP-BiTFiT works on BERT, RoBERTa, GPT2, ViT, and ResNet without architectural modifications. The implementation requires effectively one line of PyTorch code to freeze all non-bias parameters. It does not require forward hooks for activation caching, unlike all existing DP codebases.

5. **Scalability stress-tested under realistic constraints.** The maximum-batch-size throughput experiments (Figures 5/6) convincingly show DP-BiTFiT achieving the highest throughput on both large language models (GPT2-large: max batch size ≈90 vs. ≈10 for DP full) and high-resolution vision models (ResNet-152 with 512² images).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Novelty framing moderately oversold; paper would benefit from reframing as a study.** The core algorithmic operation in Algorithm 1 is standard DP-SGD restricted to bias parameters. The paper's "Novelty" paragraph (p.3, lines 77-84) anticipates this criticism and argues the contribution lies in exploiting the simpler computation graph of bias gradients. While the complexity analysis and implementation insights are genuine contributions, labeling DP-BiTFiT as a "new algorithm" rather than "a practical study/efficient implementation of DP bias tuning" overstates the algorithmic distinction. The paper's value — the empirical validation, complexity analysis, and practical efficiency — stands on its own without this framing.

2. **Missing theoretical intuition for why bias-only tuning preserves accuracy under DP.** The paper shows empirically that DP-BiTFiT is competitive, but offers no discussion of *why* bias parameters can absorb task-specific information under DP constraints. Possible hypotheses (low intrinsic dimensionality of bias gradient space, smaller effective parameter count reducing DP noise, implicit regularization from the frozen weights) are not explored. Even brief empirical analysis (e.g., gradient norm distributions, effective rank of bias gradient matrices) would strengthen the paper.

3. **No error bars or confidence intervals on accuracy results.** Given the stochasticity of DP-SGD and variation across runs, reporting standard deviations would help assess whether the small accuracy gaps between methods (often <1%) are meaningful or noise. This is standard practice for empirical DP papers.

4. **Hyperparameter sensitivity not analyzed.** The paper notes that BiTFiT requires higher learning rates than full fine-tuning (line 315) but provides no analysis of sensitivity to the clipping threshold $R$, noise multiplier $\sigma$, or learning rate for DP-BiTFiT. Understanding how robust the method is to these choices would strengthen practical guidance.

### Trivial

1. **"Activation-free forward pass" terminology is slightly imprecise, though clarified in a footnote.** The paper's footnote (line 74) clarifies that "activation-free means memory-saving." Activations are still computed during the forward pass for the backward propagation; the savings come from not *storing/caching* activations via forward hooks. The distinction is subtle but the paper does address it.

2. **SOTA accuracy language could be more precise.** The abstract says "matches the state-of-the-art accuracy" — which is accurate. However, a few instances (e.g., "achieving state-of-the-art 99.0% accuracy on CIFAR10," line 396) claim outright SOTA on specific benchmarks where the paper genuinely is best. This is justified on a per-dataset basis but could cause confusion when generalized.

3. **Linear probing results for language tasks are mentioned only in the table caption (line 246) rather than in the main table.** Including them directly in the comparison table (as is done for vision tasks in Table 4) would make cross-method comparison easier.

## Nice-to-Haves

- **Privacy-accuracy-efficiency Pareto plots** (accuracy vs. time, accuracy vs. memory at fixed ε) would concretely answer "given a fixed compute budget, which DP method should I use?" — going beyond the current separate accuracy/efficiency tables.
- **Longer-sequence language experiments** (e.g., document-level classification with T > 1024) would showcase the decisive advantage of DP-BiTFiT's $T$-independent overhead, which the paper currently only extrapolates to.
- **Ablation on the effect of training bias terms in different layer types** (attention vs. feed-forward, early vs. late layers) could reveal whether certain biases matter more for DP accuracy.
- **DP-BiTFiT-Add** (for bias-free architectures) is a thoughtful extension; a broader evaluation (beyond ResNet18) would strengthen its validation.

## Removed Points

- **Claim that the paper's SOTA claim is unqualified in the main text/conclusion.** The paper consistently uses qualified language ("matches SOTA," "on par with SOTA," or ties SOTA to a specific benchmark where it genuinely achieves the best result). The reviewer's criticism overstates the issue.
- **Claim about missing linear probing baselines for language tasks.** The paper does include linear probing results for RoBERTa-base in the table caption (line 246: "87.2% on SST2 and 77.3% on QNLI"). The reviewer appears to have missed this.
- **Claim that prior codebases "could not" do what DP-BiTFiT does.** The paper never claims prior codebases *could not* do this — it notes that "no analysis has established that only BiTFiT can be activation-free" and that prior codebases did not remove forward hooks. This is an observation about prior engineering choices, not a capability claim.
- **Criticism that DP-BiTFiT's forward pass isn't truly "activation-free."** The paper's footnote (line 74) explicitly clarifies: "activation-free means memory-saving." The technical distinction is already addressed.
- **Strength Finder item about "matches or exceeds state-of-the-art DP accuracy"** — kept but qualified. The numbers show DP-BiTFiT is competitive, sometimes best, sometimes slightly behind. The strengthening is in the efficiency dimension, not blanket accuracy superiority.

## Novel Insights

The most interesting insight from the reviewer cross-analysis is that the paper's strongest contribution is *not* the method itself (which is a straightforward application of DP-SGD to bias parameters) but the *complexity-theoretic analysis* of why bias training fundamentally avoids the bottlenecks that plague all weight-based DP methods, including other PEFT approaches. Prior DP PEFT work (e.g., Yu et al., 2021) reported empirical speedups without explaining *why* the overhead pattern differs across methods. The paper's Table 2 provides the first rigorous explanation: the feature dimension $T$ appears in the DP overhead term for *every* weight-based method (including LoRA and Adapter) but not for bias training, because the bias gradient's computation involves only the output gradient (a $B \times T \times p$ tensor) collapsed via a ones-vector rather than the activation tensor (a $B \times T \times d$ tensor) that requires expensive outer products. This $T$-independence is the structural reason DP-BiTFiT's advantage grows on long sequences and high-resolution images, and it represents a genuinely useful analytical contribution beyond the paper's empirical results.

## Suggestions

1. Reframe the paper slightly to emphasize it as a **comprehensive empirical and analytical study of DP bias tuning** rather than a novel algorithm. This removes the novelty controversy and lets the real strengths (complexity analysis, scalability benchmarks, extensive accuracy comparisons) stand on their own.
2. Add a brief **theoretical or analytical discussion** (even empirical analysis of gradient norms / effective rank) of why bias parameters can absorb task information under DP.
3. Provide **error bars** (at least 3 runs) for the main accuracy tables.
4. Consider **Pareto-style joint plots** of accuracy vs. time and accuracy vs. memory for practical decision-making.

## Score and Decision

**Originality**: 6/10 — the core idea (DP-SGD on bias parameters) is simple, but the complexity analysis and the study itself fill a gap.  
**Importance**: 8/10 — efficiency in DP fine-tuning is a practically critical problem, and the paper's speedups are substantial.  
**Claims support**: 7/10 — accuracy claims are well-supported; efficiency claims are very well-supported. Some overclaiming in novelty framing.  
**Soundness**: 7/10 — experiments are well-designed and comprehensive; missing error bars and hyperparameter sensitivity analysis.  
**Clarity**: 7/10 — generally well-written; the "activation-free" terminology could be clearer but is explained.  
**Value**: 8/10 — practical method with clear deployment guidance; the complexity analysis is a reusable reference.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>