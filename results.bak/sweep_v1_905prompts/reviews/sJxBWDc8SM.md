Now I have everything I need. Let me write the final consolidated review.

## Summary

This paper conducts an extensive empirical study of optimization dynamics in modern recurrent models (Mamba, Hyena, Mamba2, DeltaNet) versus Transformers on the multi-query associative recall (MQAR) and copying tasks. Through over 3,000 runs, the authors demonstrate that SSMs succeed only within a narrow learning-rate window, while Transformers are robust across orders of magnitude — re-contextualizing prior expressivity comparisons that used fixed hyperparameters. The paper also reveals opposing scaling strategies (SSMs benefit from width, Transformers from depth), identifies the 1D convolution as the key component enabling Mamba's single-layer MQAR performance, and shows that DeltaNet achieves Transformer-like LR stability.

## Strengths

- **Clear demonstration of optimization instability as a confound (Figure 1).** The paper shows that Mamba and Hyena achieve high MQAR accuracy only within a narrow LR window, while Attention maintains high accuracy across orders of magnitude. The dashed vertical lines from prior work (Arora et al., 2023) fall outside these windows for SSMs, directly supporting the claim that prior expressivity conclusions were confounded by suboptimal tuning. This is the paper's strongest and most actionable finding.

- **Contrasting scaling behaviors revealed through controlled experiments (Figures 3–4, Table 1).** Table 1 is particularly effective: a 12-layer Mamba with width 1408 (150M params) solves copying (100%), while a 24-layer Mamba with the same parameter count but narrower width fails (16%). This provides concrete evidence that parameter-matched comparisons can mislead by ignoring each architecture's preferred scaling axis.

- **Causal identification of architectural drivers via ablations (Table 2).** Removing the 1D convolution from 1-layer Mamba drops accuracy from 99% to 2% (matching a 1-layer Transformer), while adding a convolution to 1-layer Attention raises it to 99%. This mechanistic decomposition is stronger than merely correlating performance with model class.

- **Discovery of a 1-layer training dynamics phenomenon (Figure 6).** The finding that a 1-layer Transformer exhibits a loss bump resembling induction-head formation yet fails to improve accuracy is novel and deepens understanding of induction-head mechanisms.

- **Evaluation of DeltaNet as a stability-improving architecture (Figure 7).** DeltaNet maintains high MQAR accuracy across a wide LR range, unlike Mamba/Mamba2. The paper connects this to the absence of a decay term in its recurrence, offering a concrete design insight.

- **Thorough empirical methodology.** The paper reports over 3,000 runs and ~20,000 GPU hours, uses 5 seeds with max-min error bars for most figures, and carefully replicates prior work with proper tuning.

## Weaknesses

### Major

- **Inconsistency between Figure 3 (1-layer heatmap) and Section 6 findings.** Figure 3 shows 1-layer Mamba with uniformly low accuracy across all model dimensions (64–2048) and sequence lengths. Yet Section 6 (and the abstract) states that "well-tuned Mamba and other SSMs can learn to recall with one layer," and Figure 6 shows Mamba(width=64) achieving near-perfect accuracy. The learning rate used to produce the Figure 3 heatmap is not stated in the main text, making it unclear whether suboptimal LRs were used. This undermines the clean narrative of the scaling section and should be resolved — either by annotating Figure 3 with the LR used, or by clarifying that the heatmap uses a fixed LR that is suboptimal for 1-layer Mamba.

### Minor

- **Central thesis slightly overstates the evidence.** The sentence "Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics" (Section 3) is stronger than what the experiments concretely show. The paper demonstrates that optimization is a *major* differentiator and that many prior conclusions were confounded, but it also acknowledges that "a sizable gap with Transformers can still be observed at low widths (e.g. Hyena)" and that theoretical expressivity limitations exist (finite hidden state). The abstract and conclusion are appropriately nuanced ("a crucial differentiator lies not just in their theoretical expressivity, but in their fundamental learnability"); the strong central thesis sentence should be softened to match.

- **Missing copying task parameters in the main text.** Table 1 and Figure 5 present copying task results without specifying the sequence length, vocabulary size, copy length, or LR grid details in the main text. While these are referenced to the appendix (standard practice), the copying task is central to the paper's claims and would benefit from at least a sentence stating the key parameters (e.g., "following Jelassi et al. (2024), sequences of length X with Y copies and vocabulary size Z").

- **Table 1 lacks error bars.** The copying task results in Table 1 report only a single accuracy value per configuration, while most other figures report mean and max-min errors across 5 seeds. Given the small number of seeds, reporting variance would strengthen the reliability of these important results.

- **"Induction head attempt" claim is speculative.** The interpretation that the 1-layer Transformer loss bump "resembles the formation of an induction head circuit" and that the model "attempts" to form induction heads is a plausible hypothesis but is not supported by direct evidence (e.g., attention map visualizations or head analyses). The paper does acknowledge this as a hypothesis ("we hypothesize," "suggests an attempt"), which is appropriate, but the claim is still presented with more confidence than the evidence warrants.

- **Mechanistic link to gradient issues is inferred, not measured.** The paper attributes SSM instability to "vanishing and exploding gradient issues inherited from classical RNNs" but does not directly measure gradient norms, eigenvalues, or loss landscape curvature. This is reasonable for an empirical paper but should be more clearly flagged as an indirect inference.

### Trivial

- In the captions, "Figure 2" and "Figure 3" appear to be repeated from the image alt-text rather than cleanly formatted.

## Nice-to-Haves

- Test DeltaNet on the copying task (not just MQAR) to verify that its stability benefits generalize beyond a single benchmark.
- Add attention-map visualizations for the 1-layer Transformer at the loss-bump step to directly test the "induction head attempt" hypothesis.
- Quantify the "narrow window" numerically (e.g., ratio of LR range with ≥90% accuracy to full search range) for a more precise comparison.
- Include direct gradient norm or effective rank measurements across the LR sweep to provide causal evidence for the "brittle optimization" claim.

## Removed Points

These points were flagged in the input reviews but are removed or demoted after verification:

- **"Abstract overclaims" framed as fatal / severely misleading.** While the central thesis sentence is slightly overclaimed, the abstract itself is well-calibrated ("not just...but..." structure). This is a minor wording issue in one sentence, not a fundamental misrepresentation. → Demoted to Minor.
- **"Heatmap contradiction might use suboptimal LRs" speculation.** This is a real concern but well-supported by the evidence — the paper later shows that 1-layer Mamba *can* succeed with proper tuning, so the concern is legitimate, not speculative. → Kept as Major.
- **"Fair comparison" complaint about asymmetric evaluation.** The asymmetry (favoring baselines) is deliberate and valid; not a weakness. → Removed.
- **Missing related work mentions.** Cannot verify without external sources. → Removed.
- **Style/formatting nitpicks about figure presentation.** Parser artifacts. → Removed.
- **"No user studies" or "no theoretical proofs."** Not appropriate for an empirical systems paper. → Removed.
- **Reproducibility concerns about undisclosed hyperparameters.** These are in the appendix. → Removed.
- **Strength: "addressed an important problem."** Generic and unspecific. → Removed from strengths.
- **Strength: "large-scale systematic study" (3,000+ runs).** This is concrete and well-supported; the number is explicitly stated. → Kept.

## Novel Insights

None beyond the paper's own contributions. The observation that the 1D convolution is the critical architectural component enabling single-layer MQAR (with the S6 mixer alone performing identically to a Transformer) is a genuinely novel mechanistic insight that cuts through the architectural complexity. Similarly, the finding that DeltaNet's Householder updates eliminate the narrow-LR problem but that this benefit is limited by practical implementation constraints (max dimension 256) is an honest empirical contribution that points toward a concrete design direction.

## Suggestions

1. **Resolve the Figure 3 / Section 6 inconsistency.** Either annotate the heatmap with the learning rate used, or explicitly state that a fixed (suboptimal for 1-layer Mamba) LR was used. Better yet, produce a version of the heatmap using the optimal LR for each configuration.

2. **Soft the central thesis sentence** in Section 3 from "not...but mainly" to "not only...but also" or similar, to match the more careful wording in the abstract and conclusion.

3. **Move a few key copying task parameters** (sequence length, vocabulary, copy count) into the main text alongside Table 1.

4. **Add error bars to Table 1** using the same max-min convention used elsewhere.

## Score and Decision

### Calibration

**Round 1 bracket:** 3.5–7.5 (middle band). The paper is clearly well above the weak-band anchors (2.0–3.0) and below the strong-band anchors (7.6–8.0) which represent papers with more thorough validation across multiple scales or formal theoretical contributions.

**Round 2 anchors used for narrowing:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| *State Space Models are Provably Comparable to Transformers in Dynamic Token Selection* (QFgbJOYJSE) | 5.75 | R2 | Weaker than our paper — theoretical paper with limited experiments and no optimization analysis; our paper provides stronger empirical evidence |
| *Understanding Bottlenecks of SSMs through Recency and Over-smoothing* (pymXpl4qvi) | 6.00 | R2 | Similar in style (empirical analysis of SSM limitations) but our paper has more actionable positive findings (convolution role, DeltaNet stability) |
| *Zoology* (LY3ukUANko) | 6.33 | R2 | Directly comparable (MQAR task, SSM vs Attention); Zoology had mixed reviews (8,3,8) with one reviewer citing writing/rigor issues; our paper is better written and more focused |
| *Scaling Optimal LR Across Token Horizons* (WYL4eFLcxG) | 6.00 | R2 | Systematic empirical study of LR scaling; our paper covers a broader scope (multiple architectures, two tasks, architectural ablations) |
| *The Optimization Landscape of SGD Across the Feature Learning Strength* (iEfdvDTcZg) | 6.25 | R2 | Rigorous empirical study but different topic; similar level of thoroughness |
| *Understanding Factual Recall in Transformers via Associative Memories* (hwSmPOAmhk) | 7.33 | R3 | Stronger theoretical contributions but narrower scope (shallow models, synthetic data); our paper has broader architectural coverage and more actionable findings |

Our paper sits above the 6.0–6.33 anchors (SSM Bottlenecks, Zoology) because it provides more actionable insights (convolution ablation, DeltaNet stability) and a more complete analysis across two tasks. It is below the 7.33 anchor, which had strong theoretical contributions alongside experiments. The main weaknesses (Figure 3 inconsistency, slightly overclaimed thesis, missing error bars on one table) are fixable and do not threaten the core findings.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>