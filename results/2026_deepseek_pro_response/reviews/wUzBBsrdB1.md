Now I have a comprehensive set of anchors. Let me finalize the comparison:

- **`1Njl73JKjB.md`** (7.00, Accept) — IOI-only task evaluation framework, limited scope. Our paper is broader and more mechanistically grounded.
- **`9ca9eHNrdH.md`** (7.00, Accept) — Strong paper questioning SAE canonicality via novel methods. Our paper's toy model experiments are cleaner, and the sparsity-reconstruction critique is sharper.
- **`LC2KxRwC3n.md`** (7.50, Reject) — "A is for Absorption" — most comparable anchor. Both use controlled settings with ground truth to identify SAE failure modes. Our paper: broader scope (two LLMs, multiple layers, two architectures), a practical diagnostic metric (c_dec), and a direct critique of evaluation methodology. The "Absorption" paper was rejected primarily for limited scope and presentation — issues our paper handles better.
- **`d63a4AM4hb.md`** (7.00, Accept) — Different focus (non-linear features), less comparable.

Our paper is clearly stronger than the 7.00 anchors and comparable to or slightly stronger than the 7.50 anchor. The major weakness (under-supported "most SAEs" claim) tempers it from going higher. Final score: **7.5**.

---

## Summary

This paper demonstrates that the L0 sparsity hyperparameter in Sparse Autoencoders (SAEs) must be set correctly — not treated as a free parameter in a sparsity-reconstruction tradeoff — because insufficient L0 causes SAEs to mix correlated features together, achieving *better* reconstruction than a ground-truth SAE at the cost of feature quality. The core evidence comes from carefully controlled toy model experiments with known ground-truth features, showing that the standard sparsity-reconstruction evaluation paradigm would systematically reject correct SAEs in favor of corrupted ones. The authors propose a decoder pairwise cosine similarity metric (c_dec) as a practical diagnostic, validate it against sparse probing on real LLMs (Gemma-2-2b, Llama-3.2-1b), and provide architectural insights comparing BatchTopK and JumpReLU SAEs.

## Strengths

- **Clean, falsifying counterexample to sparsity-reconstruction evaluation**: Section 3.4 (Figures 4–5) provides the paper's most important contribution. A ground-truth SAE with exactly correct features achieves substantially worse variance explained than trained SAEs at every L0 below the true L0 (e.g., trained SAE at L0=5 achieves MSE 2.73 vs. ground-truth MSE 4.88). The trained SAEs at L0=1 and L0=5 outperform the ground-truth SAE on variance explained by over 2× despite having "horribly polysemantic latents bearing little resemblance to the underlying true features." This directly challenges the evaluation methodology used widely in SAE literature (Cunningham et al., 2024; Gao et al., 2024; Rajamanoharan et al., 2024).

- **Causal demonstration of the feature mixing mechanism in toy models**: Section 3.1 constructs a setup with known orthogonal feature directions, controlled firing probabilities, and a correlation matrix. When SAE L0 (1.8) is below the true L0 (2), decoder latents acquire off-diagonal cosine similarity components that mirror the feature correlation structure — positive components for positively correlated features (Figure 2) and negative components for anti-correlated features (Figure 3). Initializing to the ground-truth solution ensures the result comes from gradient pressure, not a local minimum — a strong experimental design choice.

- **Practical proxy metric validated against downstream task performance**: c_dec (Equation 4, Section 3.5) is motivated by a clear intuition — feature mixing increases inter-latent cosine similarity — and is validated on toy models (Figure 6, c_dec minimized exactly at true L0=11 across 5 seeds). On real LLMs (Figure 8), the "elbow" in c_dec just before the low-L0 jump coincides with peak k-sparse probing F1 scores on a >100-task benchmark, connecting the mechanism to practical SAE quality.

- **Architectural comparison yields actionable insights**: JumpReLU SAEs exhibit L0 "sticking" near the correct L0 across a wide range of sparsity coefficients (Section 3.6, Figure 7), and in LLM experiments (Section 4.1, Figure 9), JumpReLU SAEs maintain better sparse probing performance at high L0 than BatchTopK SAEs, with c_dec rising much less sharply. The decoder projection histogram analysis (Section 4.2) showing bimodal behavior at intermediate L0 provides converging evidence for the per-latent threshold hypothesis.

- **Honest self-assessment of limitations**: Section 6 explicitly acknowledges that c_dec "can sometimes remain nearly flat for a wide range of L0" and positions it as "a useful guide to avoid L0 that are clearly too low" rather than a perfect solution. This measured framing strengthens the credibility of the claims that are made.

## Weaknesses

### Fatal

None.

### Major

- **The "most SAEs have too low L0" claim is insufficiently supported**: This headline claim appears in the abstract ("We find that most commonly used SAEs have an L0 that is too low"), introduction, and discussion. However, the evidence consists of "a cursory search of open source SAEs on Neuronpedia" showing L0 < 100 is common, relegated to Appendix A.13. The paper does not establish what the correct L0 should be for those specific SAEs, so observing low L0 values does not demonstrate they are *too* low. The toy model and LLM results show there is some correct L0 per model/layer, but give no basis for claiming L0 < 100 is too low in absolute terms across different models and architectures. This claim should be substantially backed up or softened to a hypothesis.

### Minor

- **LLM evidence is correlational rather than causal**: The paper's strongest mechanistic claims (feature mixing at low L0, c_dec as a detector) are demonstrated cleanly in toy models where ground truth is known. In real LLMs, the evidence is correlational — c_dec patterns align with sparse probing performance — but feature mixing itself is not directly demonstrated. The paper acknowledges the inherent challenge (no ground truth in LLMs), but the title's strong claim ("Incorrect L0 Leads to Incorrect Features") rests more heavily on the toy model evidence than the LLM validation. The paper would benefit from more explicitly distinguishing the strength of evidence between the two settings.

- **c_dec is only partially validated as a practical guide**: As the authors acknowledge, c_dec can remain nearly flat across a wide L0 range (Gemma-2-2b layer 5 in Figure 8). The recommended "elbow" heuristic is post-hoc — it identifies the point just before the low-L0 jump, but if the curve had a different shape, the interpretation would change. The LLM validation covers only two model layers and two architectures, limiting confidence in the metric's generality.

### Trivial

- **Decoder projection histogram analysis (Section 4.2) is presented qualitatively**: The bimodal distribution observation at L0=750 is interesting but would benefit from quantification (e.g., distribution width metrics, KL divergence from a baseline) to make the analysis more reproducible and rigorous.

## Nice-to-Haves

- An experimental comparison to MDL SAEs or AFA SAEs for L0 selection would strengthen the paper's practical claims, since the paper positions itself in opposition to MDL's philosophy that there is no "correct" L0.
- The JumpReLU "sticking" phenomenon (Section 3.6) is noted in passing but could be analyzed more deeply — it suggests JumpReLU has an implicit inductive bias toward correct sparsity, which is practically important and currently undersold.
- A broader survey of c_dec curves across more layers, model sizes, and training distributions would give practitioners better guidance on when the metric is trustworthy.

## Removed Points

These points were flagged for removal; treat them with caution.

- **Harsh Critic: Introduction overstates literature position.** The harsh critic claimed the introduction's statement that sparsity-reconstruction plots imply "any sufficiently low L0 is equally valid" overstates how the literature treats L0. This is a reasonable characterization of the implicit assumption in the field — tradeoff plots do suggest picking any point on the curve — and the paper supports its critique persuasively with the ground-truth SAE counterexample.
- **Harsh Critic: Toy model initialization concern.** The harsh critic noted that initializing to ground-truth "leaves open the question of whether randomly initialized SAEs would converge to the same mixed solutions." This misunderstands the paper. Section 3.1's ground-truth initialization experiment is an *additional, stronger* demonstration (showing gradient pressure actively pushes away from correctness). The larger toy model experiments (Section 3.2–3.4) use random initialization and show the same feature mixing behavior at incorrect L0.
- **Harsh Critic: Error bars on MSE comparison.** Requesting error bars for the single MSE comparison (2.73 vs 4.88 in Section 3.3) is a nitpick — the gap is a factor of ~1.8× and the conclusion is robust. The paper includes error bars across seeds where they matter (Figure 6, Figure 8).
- **Strength Finder: Generic strengths about importance.** Removed generic framings about "addressing an important problem" that lacked concrete grounding.

## Novel Insights

The paper's most novel insight — beyond its own explicit contributions — is the demonstration that feature mixing at low L0 is *bidirectional* with respect to correlation sign: positively correlated features get positive components mixed in, while anti-correlated features get negative components mixed in (Sections 3.1, Figures 2–3). This symmetry means that low L0 corrupts essentially every latent in the SAE, not just those tracking correlated feature pairs. The practical implication — that negative correlations pervasive in language will produce nonsensical negative components in SAE latents — is a genuinely new way to understand why low-L0 SAEs underperform on downstream tasks, and it provides a mechanistic explanation for the empirical findings in Kantamneni et al. (2025) and Bussmann et al. (2025).

## Suggestions

- Soften the "most SAEs have too low L0" claim to a hypothesis (e.g., "our findings suggest that many widely-used SAEs may have L0 that is too low") or provide a systematic survey with L0 recommendations per model/layer rather than relying on a "cursory search" of Neuronpedia.
- Add explicit language in the abstract or introduction distinguishing the strength of evidence between toy model experiments (causal, with ground truth) and LLM validation (correlational, no ground truth).
- Quantify the decoder projection histogram analysis (e.g., report distribution width or variance) to make Section 4.2 more reproducible.

---

## Calibration Anchor Summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `tcsZt9ZNKD.md` (Scaling SAEs) | 1.75 | R1 | Much weaker — this paper's contribution is far more substantial |
| `89wVrywsIy.md` (Hierarchical Tracing) | 3.40 | R1 | Much weaker — methods and evaluation are less rigorous |
| `F76bwRSLeK.md` (Cunningham et al. SAEs) | 4.80 | R1 | Foundational but less novel; our paper critiques its evaluation paradigm |
| `1Njl73JKjB.md` (Principled Evaluations) | 7.00 | R1/R2 | Our paper is broader (two LLMs, toy models, metric) and more mechanistically grounded |
| `9ca9eHNrdH.md` (SAEs Not Canonical) | 7.00 | R1/R2 | Comparable quality; our toy model experiments are cleaner, critique is sharper |
| `LC2KxRwC3n.md` (A is for Absorption) | 7.50 | R2 | Most comparable; our paper has broader scope, practical metric, multi-model validation |
| `d63a4AM4hb.md` (Features Not Linear) | 7.00 | R2 | Different focus; less directly comparable |

**Round 1 bracket:** 7.0–8.0. **Round 2 narrowed to:** 7.0–7.5, with the paper landing at 7.5 — above the 7.00 anchors and comparable to the 7.50 anchor but with broader scope and clearer practical implications. The major weakness (under-supported "most SAEs" claim) prevents going higher, but this is addressable in rebuttal.

**Final score: 7.5, Accept.**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>