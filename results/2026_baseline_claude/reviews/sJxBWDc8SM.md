Now I have read the complete paper. Let me write my review.

---

## Summary

This paper revisits empirical comparisons between Transformers and modern recurrent models (SSMs, specifically Mamba, Hyena, Mamba2, DeltaNet) on the multi-query associative recall (MQAR) and copying tasks. The central claim is that prior evaluations were confounded by optimization instability: SSMs have an extremely narrow optimal learning-rate window compared to Transformers, which are robust across orders of magnitude. With proper tuning, SSMs can solve MQAR in regimes where prior work deemed them incapable, including in single-layer settings. The paper further documents opposing scaling behaviors (width-favored for SSMs, depth-favored for Transformers), 1-layer training dynamics related to induction heads, ablations identifying the 1D convolution as a key enabler of Mamba's expressivity, and that DeltaNet achieves Transformer-level optimization stability.

---

## Strengths

- **Re-contextualizes a widely-cited prior result**: The paper directly challenges conclusions of Arora et al. (2023) / Zoology, demonstrating through careful learning-rate grid search (~3,000 runs, ~20,000 GPU hours) that Mamba can solve MQAR in the "hard" (long-sequence, small-width) regime previously attributed to expressivity limitations. This is practically significant given how influential those prior comparisons have been.

- **Opposing scaling behaviors (width vs. depth) are clearly demonstrated**: The systematic ablation over 1-layer vs. 2-layer, varying width and depth (Table 1, Figs. 3–4), provides a compelling and actionable finding: scaling SSMs along depth (to match Transformer parameter count) is misguided; width is what matters. The copy task (Table 1) illustrates this strikingly—a 24-layer Mamba at 150M parameters achieves only 16% accuracy, while a 12-layer wider Mamba at the same parameter count reaches 100%.

- **Mechanistic insight via convolution ablation**: The finding (Table 2) that removing the 1D convolution from 1-layer Mamba reduces accuracy to the same ~2% failure point as 1-layer Attention—and conversely, that adding convolution to Attention's QKV projection enables 99% accuracy—is a crisp, testable mechanistic insight with direct implications for architecture design.

- **Novel induction-head dynamics in 1-layer models**: The observation (Fig. 6) that a 1-layer Transformer exhibits a loss bump reminiscent of induction-head formation (previously documented only in 2-layer models) but without any accuracy gain is new to the best of my knowledge and adds a concrete empirical data point to the theory of induction heads.

- **DeltaNet as an architectural path to stability**: Grounding DeltaNet's robustness in the Householder-based update (which avoids the exponential decay in $A_k$) provides a hypothesis linking architecture to training stability, pointing to a concrete design principle for future SSM work.

---

## Weaknesses

### Fatal
None.

### Major

- **No theoretical explanation for the narrow LR window**: The paper provides a compelling empirical account of optimization brittleness in SSMs but offers no formal characterization of why their loss landscape differs from Transformers. The vanishing-gradient hypothesis (citing Trockman et al.) is mentioned once in passing for DeltaNet but is never connected to the LR-sensitivity results in Mamba or Hyena. Given that the title claims to identify "a fundamental mismatch in the loss landscape," the absence of even an informal loss-landscape analysis (e.g., Hessian sharpness, gradient norms during the narrow LR window) is a meaningful gap. Without it, the paper diagnoses a symptom without explaining the disease.

- **Findings are confined to synthetic benchmarks; real-language-model implications remain unvalidated**: The paper explicitly acknowledges this limitation in the discussion, but it is more than a caveat—it is a fundamental constraint on the scope of the claims. SSMs are tuned with practitioners using fixed learning-rate schedules in large-scale LLM training, not a grid search. The implication that "prior expressivity conclusions may be confounded by optimization" can only be fully evaluated if the authors show whether the narrow optimal LR also afflicts standard LLM training pipelines or whether, in practice, warm-up schedules and cosine decay happen to land in the good window. Without even a single language-modeling experiment, the connection to "language modeling performance" in the abstract is asserted rather than demonstrated.

### Minor

- **The optimization analysis is limited to learning rate**: Gradient clipping, weight decay, optimizer choice (Adam vs. others), and warm-up length all interact with the curvature of the loss landscape. Since the paper's thesis is about optimization stability, studying only the learning rate leaves open whether the brittleness persists under other optimizer variants or configurations commonly used in LLM pretraining.

- **Single-layer induction-head bump analysis is informal**: The claim that the 1-layer Transformer "attempts" to form induction heads (Section 6) is stated as a hypothesis and would benefit from additional mechanistic evidence—e.g., attention pattern visualization before and after the bump, or measuring induction-score (as in Olsson et al.) during training.

- **Coverage of newer SSMs is narrow**: Mamba2 and DeltaNet are evaluated (Fig. 7), but other prominent modern recurrent architectures (e.g., RWKV5/6, GLA, Hawk/Griffin) are not included, limiting the generality of stability conclusions about "modern recurrent models" beyond Mamba-family architectures.

### Trivial
None worth noting.

---

## Nice-to-Haves

- A gradient-norm or Hessian-spectrum analysis during training around the narrow LR window would make the "mismatch in loss landscape" claim substantially more concrete.
- Even a single small-scale language-modeling experiment (e.g., WikiText-103 or The Pile subset) demonstrating that properly-tuned Mamba closes some of the gap observed in Waleffe et al. would directly connect the synthetic findings to the paper's broader motivation.
- Reporting validation/test accuracy along with training accuracy would strengthen claims about generalization vs. memorization in the single-layer SSM setting.

---

## Novel Insights

The paper's most genuinely novel contribution beyond restating known SSM-Transformer differences is the identification of **optimization instability as the primary practical differentiator**, with concrete evidence that prior work's key negative results for Mamba on MQAR are artifacts of a too-sparse learning-rate grid. Equally novel is the mechanistic bridge: 1-layer Mamba without its 1D convolution ≈ 1-layer Attention in expressivity, and 1-layer Attention + convolution on QKV ≈ 1-layer Mamba in expressivity, providing a crisp architectural equivalence. The observation of an induction-head-like loss bump in 1-layer Transformers—without corresponding accuracy gain—is also new and hints at an intriguing gap between circuit formation and functional leverage that warrants follow-up.

---

## Suggestions

- Provide at least one analysis of gradient norms or sharpness across the learning rate range to mechanistically connect the narrow LR window to the loss landscape claim.
- Extend experiments to even one small-scale language modeling task to strengthen the claimed relevance to "language modeling performance."
- Add induction-score curves (following Olsson et al.) during single-layer training to ground the loss-bump hypothesis more rigorously.
- Examine whether standard cosine-LR schedules with warm-up as used in LLM pretraining happen to explore the narrow good window, or whether they miss it systematically.

---

## Score and Decision

The paper makes a genuine and practically important contribution: it shows that a widely-used benchmark comparison (Zoology/MQAR) is confounded by optimization artifacts, and that the gap between SSMs and Transformers is smaller than previously reported once tuning is done carefully. The scaling analysis and convolution ablation are concrete and actionable. The main weakness is the gap between the empirical evidence (confined to synthetic benchmarks) and the broader claims about "language modeling" and "loss landscape geometry," which remain unsupported by theoretical analysis or real-language experiments. This is a well-executed empirical study whose findings are significant for the SSM research community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>