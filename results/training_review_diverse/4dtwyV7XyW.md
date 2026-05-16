## Summary

This paper proposes Knowledge Tracing Set Transformers (KTSTs), a transformer-based model class for knowledge tracing that replaces the commonly used but flawed "expanded representation" with principled, permutation-invariant set representations of student interactions. The model also introduces a learnable variant of ALiBi for positional attention. Evaluated on 8 benchmark datasets against 22 baselines, KTST achieves new SOTA AUC/accuracy on 7 of 8 datasets while being conceptually simpler than prior domain-inspired approaches.

## Strengths

- **New state-of-the-art performance on seven of eight benchmark datasets.** Tables 1 and 2 show KTST (mean) achieves the highest AUC and accuracy on all datasets except Statics2011, with most improvements statistically significant at the 0.01 level via paired t-tests against reproduced baselines. This directly and convincingly supports the paper's central empirical claim.

- **Principled, permutation-invariant set representations with rigorous motivation.** Section 3 clearly identifies how the "expanded representation" used in prior work (Ghosh et al., 2020; Liu et al., 2022; 2023b; Yin et al., 2023) introduces label leakage and a training–inference distribution shift. Section 4.3 defines permutation invariance formally and proposes three aggregation functions (mean, unique set, MHSA) that satisfy it while remaining domain-agnostic. The contrast with complex, domain-inspired alternatives (Rasch embeddings, memory-augmented networks) is well-drawn.

- **Large-scale, reproducible empirical evaluation.** The paper evaluates on 8 datasets with 22 baselines, all reproduced within the pykt framework under consistent preprocessing, data splits, and hyperparameter tuning protocols. Statistical significance testing is applied throughout. This is a high standard of empirical rigor for the knowledge tracing field.

- **Ablation study validating key architectural choices.** Table 3 systematically compares 4 attention mechanisms × 2 cross-attention designs (q=k vs. q≠k) × 2 architectures (encoder-decoder vs. decoder-only), identifying the best configuration (learnable ALiBi, q=k, encoder-decoder) with statistical support. This provides direct evidence for the design decisions behind KTST.

- **Synthetic experiments probing representation capacity.** Section 5.3 uses MIRT-generated data to systematically vary KC-per-question ratio and sample size. The results show that MHSA embeddings excel in high-capacity settings while mean embeddings generalize reliably, consistent with real-world benchmark patterns and the paper's conjectures about overfitting.

## Weaknesses

### Fatal
None.

### Major

- **No controlled experiment isolating the effect of the representation choice.** The paper argues in Section 3 that the expanded representation is flawed (label leakage, distribution shift) and that set representations are the principled alternative. However, the empirical evidence for this causal claim relies entirely on cross-model comparisons (KTST with set representations vs. baselines that happen to use the expanded representation, which differ in architecture, hyperparameters, and other design choices). A controlled experiment — training KTST with the expanded representation (with proper masking per Liu et al., 2022) and comparing to KTST with set representations under identical architecture/hyperparameters — would directly isolate whether the representation drives improvements. Without it, the paper's strongest narrative claim (that *principled representations* drive the gains) remains plausible but not definitively proven. This is a gap between the paper's motivating critique and its evidence base; it does not invalidate the core contribution (the model still achieves SOTA), but it limits the strength of the attribution.

### Minor

- **Ablation study (Table 3) conducted on only one dataset (ASSISTments2009).** Key architectural decisions — learnable ALiBi, q=k, encoder-decoder — are validated on a single dataset. Given that datasets vary substantially in KC-per-question ratio (Ednet: 2.30, Statics2011: 1.0) and size, it is unclear whether these design preferences generalize. Extending the ablation to at least 2–3 more datasets (e.g., Ednet for high ratio, Algebra2005 for moderate ratio) would substantially strengthen confidence in the architectural recommendations.

- **Computational cost not quantified.** The paper notes that MHSA embeddings "add computational cost" (Section 4.3) but does not report training/inference times, parameter counts, or FLOPs for any of the three embedding variants. This omission makes it difficult for practitioners to assess the practical trade-off between mean embeddings (simpler, used for SOTA results) and MHSA embeddings (higher capacity, more expensive).

### Trivial
None.

## Nice-to-Haves

- Quantifying the severity of the distribution shift introduced by the expanded representation (Section 3) would strengthen the motivation further.
- The synthetic experiments use MIRT as the sole generative model; validating the capacity conclusions under an alternative generative assumption would be useful but is not essential given their supporting role.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about the phrase "flawed evaluation" being too strong (Harsh Critic, Section-by-Section Notes).** This is a stylistic/phrasing preference, not a substantive weakness. The paper substantiates the label leakage and distribution shift claims precisely in Section 3. *Reason: Removed as a phrasing nitpick / subjective tone concern.*
- **Criticism that "the paper could acknowledge that simplicity is relative" (Harsh Critic, Section 4.1 note).** The paper already contextualizes simplicity by comparing to domain-inspired alternatives (Rasch embeddings, memory-augmented networks, GNNs) in Sections 4.1 and 4.3. *Reason: Already addressed reasonably in the paper.*
- **Criticism about synthetic experiment generalizability (Harsh Critic, Section 5.3 note).** The synthetic experiments are explicitly scoped as supporting evidence for capacity conjectures, not primary validation. The paper's language ("support this conjecture") is appropriately cautious. *Reason: Misplaced expectation — the experiments serve their stated purpose.*
- **Criticism about MHSA embeddings' "thin" real-world evidence (Harsh Critic, Section 4.3 note).** The paper honestly concedes that MHSA embeddings overfit on simpler datasets and are primarily competitive on Ednet. This is an acknowledged empirical finding, not a weakness. *Reason: The paper already acknowledges the limitation.*

## Novel Insights

None beyond the paper's own contributions. The review process surfaces one useful framing: the paper convincingly shows that *KTST as a whole* achieves SOTA, but does not empirically isolate whether set representations *per se* are the causal driver of improvement — the gains could partially arise from other architectural choices (Learnable ALiBi, encoder-decoder with q=k). This is a methodological gap that clarifies what the paper proves vs. what it motivates, but it does not undermine the paper's value as a strong new method.

## Suggestions

- **Add a controlled experiment**: train KTST with the expanded representation (with proper masking per Liu et al., 2022) and compare to KTST with set representations under identical architecture/hyperparameters. This would substantiate (or bound) the paper's strongest narrative claim and significantly strengthen the paper.
- **Extend the ablation study** (Table 3) to at least 2–3 more datasets covering different KC-per-question ratios (e.g., Ednet, Algebra2005) to verify whether architectural preferences generalize beyond ASSISTments2009.
- **Report computational cost** (training/inference times, parameter counts) for the three embedding variants to help practitioners assess the practical trade-offs.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>