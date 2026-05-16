Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes SUMMER, a framework for Multimodal Emotion Recognition in Conversations (MERC) that combines three components: Sparse Dynamic Mixture of Experts (SDMoE) for local-to-global token-wise interaction, Hierarchical Cross-Modal Fusion (HCMF) with Global MoE for contextual understanding, and a novel "retrograde distillation" strategy (Interactive Knowledge Distillation, IKD) where a frozen unimodal (text) teacher guides a multimodal student. The method achieves strong results on IEMOCAP and MELD, with notable gains on minority and semantically similar emotion categories.

---

## Strengths

- **Strong empirical results on two standard benchmarks.** On IEMOCAP, SUMMER achieves a 2.61% w-ACC improvement over prior methods. On MELD, the student model shows a 15.5% relative gain on "Fear" over CORECT and distinct improvements on "Anger" (+3.5%) and "Disgust" (+5.81%) compared to SDT (Tables 1–2). These gains are demonstrated across both majority and minority emotion classes.

- **Ablation studies confirm the contribution of each component.** Table 4 shows that removing SDMoE (replacing with standard MoE), replacing HCMF with self-attention, or removing IKD all cause performance declines on both datasets. Figure 5 further shows that residual structures in HCMF improve training stability. This systematic ablation supports the architectural claims for SDMoE and HCMF.

- **t-SNE visualization provides qualitative support.** Figure 6 shows that SUMMER's learned features produce more distinct emotion category boundaries compared to raw features, with reduced overlap between semantically similar pairs (e.g., "happy" vs. "excited").

- **The paper addresses a relevant and well-motivated problem.** The running example (Figure 1a) clearly illustrates the issue of local-context overemphasis in MERC, and the motivation for dynamic expert selection (Figure 1b) is grounded in a real limitation of fixed Top-K MoE.

---

## Weaknesses

### Fatal
None.

### Major

- **The central claim about retrograde distillation is not properly ablated.** The paper's key novelty is the "retrograde" direction of distillation (unimodal teacher → multimodal student), motivated as addressing "fusion disorientation" and gradient conflicts that arise in self-distillation. However, the ablation in Table 4 only compares the full SUMMER (with IKD) against "w/o IKD" (no distillation at all). This conflates two questions: (a) whether *any* distillation helps, and (b) whether the *retrograde direction specifically* provides benefits over standard alternatives. A proper ablation would compare (i) no distillation, (ii) standard KD with a multimodal teacher → multimodal student, and (iii) the proposed unimodal teacher → multimodal student. Without (ii), the paper cannot support the claim that the retrograde direction is what helps, nor the claim that it mitigates gradient conflicts better than existing alternatives. Since this is listed as a core contribution, this gap is significant.

### Minor

- **The dynamic routing mechanism is under-specified, affecting reproducibility.** The Dynamic Routing Mechanism (Eqs 3–5) has several ambiguities. The hard threshold in Eq (3) checks whether gating weights \(W_g\) fall within \((\mu-2\sigma, \mu+2\sigma)\), but it is not specified whether \(\mu\) and \(\sigma\) are computed per sample, per batch, or globally over all experts, nor what \(W_g\) represents (raw logits before softmax?). Additionally, the relationship between Eq (3)'s hard threshold and Eq (4)'s Gumbel softmax is not reconciled: the hard threshold creates a non-differentiable step that the Gumbel softmax is supposed to address, but the paper does not specify whether the threshold is applied *before* the Gumbel softmax (operating on \(W_g\)), *after* (operating on \(\hat{G}_{dyn}\)), or in parallel. This makes faithful reimplementation difficult without guessing critical design choices.

- **No statistical significance or variance reporting.** Results in Tables 1 and 2 report single-run metrics without standard deviations or confidence intervals. For datasets of this size (IEMOCAP: ~12 hours of conversation), variance across random seeds or data splits can be non-negligible. Without this information, it is impossible to assess whether the claimed improvements (especially the smaller ones, e.g., 1.86% on "sadness") are statistically meaningful.

- **The teacher model's comparison against baselines is not apples-to-apples.** The paper notes that the text-only teacher model "outperforms prior approaches" and "surpasses all existing models" (Section 4.4). However, the teacher uses RoBERTa for text encoding, while many baselines (e.g., DialogueRNN, DialogueGCN) were originally published with older text features (GloVe, BERT). The relative advantage may partly reflect a stronger text backbone rather than anything specific to the proposed methodology. The student model's main results are the more important comparison, but the teacher comparison should be stated with appropriate qualification.

### Trivial
None.

---

## Nice-to-Haves

- **Comparison of computational cost.** The SDMoE and HCMF modules add parameters and inference overhead. Reporting FLOPs, parameter count, or runtime against baselines would help assess practical tradeoffs.
- **Gradient analysis.** The paper motivates IKD by saying it "mitigates gradient conflicts from modal heterogeneity" but provides no gradient-based analysis (e.g., gradient alignment metrics, loss landscape visualization) to substantiate this claim.
- **Hyperparameter sensitivity.** The method introduces several hyperparameters (temperature \(\tau\), the \(2\sigma\) threshold factor, adjustment factor \(\phi\), KD scalars \(\kappa_1\)–\(\kappa_4\)). An ablation or sensitivity study for these would strengthen the paper.
- **Confusion matrices.** The error analysis (Section 4.5) honestly acknowledges underperformance on "Sad" but would benefit from quantitative evidence such as confusion matrices.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not properly cite or discuss prior work on unimodal-to-multimodal distillation in other domains."** — Removed per hard rule: missing related work claims are not permitted without external verification of the cited literature.
- **"Eq (2) for Speaker Embeddings: notation uses a typographical symbol (†) that is not defined."** — Removed per hard rule: formatting/parsing artifacts are not author errors.
- **"Missing appendix, missing proofs in appendix"** — No such criticism was made, but references to Sections A.1 and A.2 exist in the paper; these sections were stripped by the parser and are presumed to exist in the original submission.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a key evaluation gap (unablated distillation direction) that the paper's own claims did not anticipate, but this is a weakness in the paper's experimental design rather than a novel observation about the problem domain.

---

## Suggestions

1. **Add a comparison against standard (non-retrograde) distillation**: train a multimodal teacher model using the same architecture and compare: (a) no distillation, (b) multimodal teacher → multimodal student, (c) unimodal teacher → multimodal student (proposed). This directly tests whether the retrograde direction is beneficial.
2. **Clarify the dynamic routing mechanism**: specify what \(\mu\) and \(\sigma\) are computed over (per-sample, per-batch, or global), what \(W_g\) represents, and how the hard threshold (Eq 3) interacts with the Gumbel softmax (Eq 4). Include pseudocode if needed.
3. **Report standard deviations** across at least 3–5 random seeds for all main results.
4. **Qualify the teacher model comparison**: note that the teacher uses a stronger text backbone (RoBERTa) than some baselines, and that this may contribute to its superior performance.

---

## Score and Decision

The paper proposes a plausible method with strong empirical results and ablation studies that validate SDMoE and HCMF. However, the evaluation of its central novelty—the retrograde distillation direction—is incomplete: the paper shows that distillation helps but does not show that the *retrograde direction* is what matters, which is the claimed contribution. This is a significant gap that requires additional experiments rather than simple clarification. Combined with under-specification of the dynamic routing mechanism and missing variance estimates, the paper in its current form does not convincingly support all its claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>