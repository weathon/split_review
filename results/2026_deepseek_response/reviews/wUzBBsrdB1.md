## Summary

This paper studies how the L0 hyperparameter (average number of active latents per token) affects feature quality in Sparse Autoencoders (SAEs). Using toy models with ground-truth features, it demonstrates that setting L0 too low causes the SAE to mix correlated features into latents to improve MSE reconstruction — producing demonstrably incorrect features that nonetheless look "good" on standard sparsity-reconstruction tradeoff plots. The paper proposes decoder pairwise cosine similarity (c_dec) as a practical diagnostic metric whose minimum (or elbow) identifies the correct L0, and validates this on Gemma-2-2b and Llama-3.2-1b SAEs, where the c_dec elbow aligns with peak k-sparse probing performance. It also compares BatchTopK and JumpReLU SAE behavior at high L0.

---

## Strengths

1. **Mechanistic demonstration of feature mixing at low L0 (Section 3.1, Figures 2–3).** Using toy models with known ground-truth features and controlled correlations, the paper directly visualizes how SAEs with L0 below the true L0 mix positive components of positively correlated features and negative components of negatively correlated features. This provides a clean, mechanistic explanation for why low-L0 SAEs underperform on downstream tasks — not just smooth degradation, but systematic corruption of every latent.

2. **Shows sparsity-reconstruction tradeoff can favor incorrect solutions (Section 3.4, Figure 4).** The paper constructs a ground-truth SAE with correct features and compares its reconstruction to a trained SAE at the same L0. The trained SAE (with corrupted latents) achieves *better* reconstruction than the ground-truth SAE at low L0. This is a concrete, one-figure refutation of the implicit assumption that better reconstruction at a given sparsity means a better SAE.

3. **Proposes c_dec as a practical diagnostic metric and validates it in toy models and LLMs (Sections 3.5, 4, Figures 6, 8).** c_dec is minimized at the true L0 in toy models with 5 seeds, and its "elbow" (the point just before it jumps due to low L0) aligns with peak k-sparse probing F1 across 100+ tasks on both Gemma-2-2b and Llama-3.2-1b. The metric is simple to compute, has theoretical grounding (Appendix A.6), and provides a practical heuristic for L0 selection that does not require ground-truth features.

4. **Validates findings across architectures (Section 3.6, Figure 7; Section 4.1, Figure 9).** The c_dec pattern holds for both BatchTopK and JumpReLU SAEs, and the paper documents meaningful differences in how the two architectures behave at high L0.

---

## Weaknesses

### Fatal
None.

### Major

1. **The claim that "most commonly used SAEs have an L0 that is too low" goes beyond the evidence.** The abstract asserts this as a finding, and the Discussion (Section 6) supports it only with "a cursory search of open source SAEs on Neuronpedia" relegated to Appendix A.13. The paper's own experiments cover two models (Gemma-2-2b, Llama-3.2-1b) at a limited set of layers. The core contribution — that incorrect L0 corrupts features — is well-established by the toy and LLM experiments. But the prevalence claim about "most commonly used SAEs" is a separate, unsupported extrapolation that should be softened to an observation about the specific SAEs surveyed.

### Minor

2. **c_dec's sensitivity to non-orthogonal features is not discussed.** The metric's motivation relies on the Linear Representation Hypothesis (near-orthogonal features). The toy model enforces orthogonal features, so c_dec minimization aligns perfectly with ground truth. However, recent work (Engels et al., 2025, cited by the paper) suggests some LLM features may be non-linear or non-orthogonal. The paper acknowledges c_dec is "not a perfect guide" (Section 6) but does not explore how non-orthogonal ground-truth features would affect it. A brief discussion of when c_dec may fail would strengthen the paper.

3. **The Section 4.2 analysis of "L0 simultaneously too low and too high" is suggestive but not quantitatively supported.** The decoder projection histograms (Figure 9, right) are an interesting visualization, and the paper uses appropriately cautious language ("we suspect," "likely"). However, the claim that at L0=750 some latents are monosemantic while others mix features would be strengthened by a quantitative decomposition (e.g., clustering latents by firing frequency or decoder norm). As presented, this remains acknowledged speculation.

4. **Limited statistical reporting for the LLM experiments.** The paper reports 3 seeds per L0 for Figure 8 but does not present mean and standard deviation values for sparse probing F1 scores in a table. The error bars in the figures appear small, but the absence of explicit quantification makes it harder to assess reliability, particularly in the Gemma layer 5 results where the c_dec curve is relatively flat.

### Trivial

5. The statement "we are particularly excited about the possibility that we can learn more about the underlying correlational structure between underlying features by studying correlations in the SAE decoder" (Section 6) is vague and does not add substance.

---

## Nice-to-Haves

- **Mechanism analysis for JumpReLU vs. BatchTopK differences at high L0.** The paper hypothesizes that JumpReLU's per-latent thresholds allow it to maintain lower c_dec at high L0 (Section 4.1). A concrete comparison of learned threshold distributions or firing rate profiles would make this more than a plausible speculation, but the observation as presented is still valid.
- **Explicit description of the sparse probing benchmark tasks and how F1 is averaged across them** to improve reproducibility.
- **A brief note on dead latents and their potential effect on c_dec.**

---

## Removed Points

These points were considered and removed from the main weaknesses with justification:

- **"The sparsity-reconstruction critique is overstated":** The paper demonstrates on a toy model that a trained SAE outperforms the ground-truth SAE on reconstruction at low L0. The claim that "sparsity-reconstruction tradeoff plots are not a sound method of evaluating SAE architectures" follows directly from this demonstration. The concern about "overcorrection" is a framing preference, not a valid weakness.
- **"JumpReLU vs. BatchTopK comparison lacks mechanism analysis":** The paper uses "we suspect" language, making the speculative nature clear. Deeper analysis is a nice-to-have, not a weakness.
- **Missing appendix content, proofs in appendix, absent references:** The parser strips these sections from all papers; they exist in the original submission.
- **Criticism about "statistical rigor" demanding confidence intervals beyond what is standard in the SAE field:** Visual error bars with 3 seeds are standard for large-scale SAE training.
- **Pure formatting/style nitpicks:** These are parser artifacts, not author errors.
- **Strength Finder's generic praises about "addressing an important problem":** These are content-free and lack specific evidence; they do not constitute evidence-backed strengths.

---

## Novel Insights

Beyond "low L0 is bad," the paper's key insight is that low L0 is *actively incentivized* by the MSE loss, creating a perverse incentive where the SAE can achieve better reconstruction by mixing correlated features than by learning the correct sparse decomposition. This means that sparsity-reconstruction tradeoff plots — the standard evaluation tool — can be *negatively correlated* with feature correctness. The c_dec metric offers a practical workaround that does not require ground-truth features, making this insight actionable.

---

## Suggestions

1. **Soften the "most commonly used SAEs" claim** in the abstract and introduction to match the evidence.
2. **Add a brief discussion** of when c_dec might fail (non-orthogonal features, dead latents).
3. **Add quantitative decomposition** to the Section 4.2 analysis (e.g., cluster latents by firing frequency to confirm the mixed-behavior hypothesis).
4. **Include a small table** of mean ± std for sparse probing F1 at each L0 for the two LLM layers.

---

### Calibration Details

**Round 1 — Bracketing:** Three queries on `sparse autoencoder L0 / feature quality / interpretability` across score bands. Low band (<3.5): retrieved anchors with avg scores 1.67, 2.50, 3.00 — all clearly weaker. Middle band (3.5–7.5): retrieved Cunningham (4.80), "Compute Optimal Inference" (4.67), "Towards Principled Evaluations" (7.00), "Canonical Units" (7.00). High band (>7.5): retrieved "Sparse Feature Circuits" (8.00), "A is for Absorption" (7.50). **Initial bracket: 4.5–7.5.**

**Round 2 — Narrowing:** Two queries inside the bracket. Mid anchors (4.0–6.0): Cunningham (4.80), "Compute Optimal Inference" (4.67), "Unlearning with SAEs" (5.25), "Automatically Interpreting Millions" (5.50). Upper anchors (6.0–8.0): "Principled Evaluations" (7.00), "A is for Absorption" (7.50), "Canonical Units" (7.00), "Multi-Layer SAEs" (6.50). Read in full: Cunningham (4.80), "Principled Evaluations" (7.00), "Canonical Units" (7.00), "A is for Absorption" (7.50).

**Comparison vs. specific anchors:**
- **vs. Cunningham (4.80):** Current paper is clearly stronger — more rigorous toy model experiments, a practical metric, validation on modern LLMs with multi-task benchmarks.
- **vs. "Principled Evaluations" (7.00):** Weaker in evaluation framework completeness; that paper proposes a full suite of evaluation axes. Current paper has a more focused contribution.
- **vs. "A is for Absorption" (7.50):** Similar in structure (identify pathology → controlled study → LLM validation). Current paper has broader model/task validation but has a prevalence overclaim that "A is for Absorption" avoids.
- **vs. "Canonical Units" (7.00):** Weaker in scope of technical contribution (two novel techniques + new architecture). Current paper is more narrowly focused on L0.

**Final score: 6.5.** The paper is clearly above mid-range anchors (4.8–5.5) in evidence quality, and comparable to upper-range anchors (7.0–7.5) but pulled slightly down by the unsupported prevalence claim and the speculative Section 4.2 analysis. The core contribution is solid, well-evidenced, and practically useful.

---

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>