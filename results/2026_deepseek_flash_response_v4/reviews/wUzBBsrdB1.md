## Summary

This paper studies the effect of the L0 hyperparameter (average number of firing latents per token) on sparse autoencoder (SAE) quality. Using toy models with known ground-truth features, it demonstrates that setting L0 too low causes SAEs to mix correlated features (feature hedging), improving MSE reconstruction at the cost of latent monosemanticity. The paper shows that a ground-truth SAE scores *worse* on reconstruction than a corrupted SAE at low L0 (MSE 4.88 vs 2.73), directly proving that MSE loss incentivizes incorrect feature learning when L0 is misspecified. It proposes `c_dec` (decoder pairwise cosine similarity) as a diagnostic whose "elbow" near low L0 values coincides with peak sparse probing performance on Gemma-2-2b and Llama-3.2-1b, and argues that most commonly used SAEs have too low an L0.

## Strengths

- **Clean toy-model demonstration with ground truth (Sections 3.1–3.3):** Because the paper constructs synthetic data with known orthogonal features and controlled correlations, it can directly compare trained SAEs against a hand-constructed ground-truth SAE. The finding that a low-L0 trained SAE achieves MSE=2.73 while the ground-truth SAE achieves 4.88 (Section 3.3) is direct, causal evidence that the MSE loss *actively incentivizes* feature mixing when L0 is too low. This experimental design cleanly separates L0 misspecification from confounds present in real LLMs.

- **Sparsity-reconstruction plots shown to mis-rank the correct SAE (Section 3.4, Figure 4):** Figure 4 demonstrates that at every L0 below the true value, a trained (corrupted) SAE achieves higher variance explained than the ground-truth correct SAE. This is a concrete counterexample to a standard evaluation methodology—if a training method produced a perfect SAE, the sparsity-reconstruction plot would rank it *worse* than an incorrect one. This is a valuable caution for the field.

- **c_dec elbow aligns with peak sparse probing performance on two LLMs (Section 4, Figure 8):** On both Gemma-2-2b (layer 5) and Llama-3.2-1b (layer 7), the sharp increase in c_dec at low L0 coincides with peak k=16 sparse probing F1 scores (Kantamneni et al., 2025 benchmark, 100+ tasks). This grounds the toy-model-derived metric in an independent downstream task.

- **Replication across BatchTopK and JumpReLU architectures (Sections 3.6, 4.1):** The L0-mixing effect appears in both architectures, ruling out architecture-specific artifacts. The JumpReLU "stickiness" observation (Figure 7, left) independently corroborates the existence of a preferred L0.

## Weaknesses

### Fatal
None.

### Major
- **The claim that "most commonly used SAEs have an L0 that is too low" is not well-supported by the presented evidence.** The LLM experiments examine only 2 models (Gemma-2-2b, Llama-3.2-1b) × 2 primary layers (layers 5 and 7 for the main c_dec analysis, plus layer 12 for the BatchTopK vs JumpReLU comparison). The Neuronpedia survey is referenced to Appendix A.13 (not evaluable from the main text). The sparse probing F1 differences across the entire L0 range are modest (~0.04, from ~0.78 to ~0.82), and the paper does not report whether these differences are statistically significant. A sweeping claim about "most SAEs used by researchers today" needs substantially broader evidence across more models, layers, SAE variants, and ideally a demonstration that the L0≈200 elbow corresponds to meaningfully better *interpretability*, not just a small probing-score improvement.

- **The gap between the clean toy model and the messy LLM evidence is under-acknowledged.** In the toy model, features are perfectly orthogonal with known correlations, and a single "true L0" exists by construction. In LLMs, the paper's own results show complex c_dec behavior: the Gemma-2-2b layer 5 curve (Figure 8, top-left) has a long flat region where the global minimum lies in the flat zone, making the "elbow" detection a qualitative heuristic rather than a principled estimator. The paper's central framing (title "SPARSE BUT WRONG," definitive language about "incorrect features") implies a stronger LLM conclusion than the correlational evidence supports. The paper shows that c_dec co-occurs with sparse probing performance, but does not *causally* demonstrate that LLM SAE latents at low L0 mix correlated features in the same way as the toy model.

### Minor
- **The c_dec metric has limited practical utility as presented.** It requires training a costly sweep of SAEs across L0 values (32768-wide SAEs on 500M tokens each per L0 value). Its interpretation varies by architecture (JumpReLU vs BatchTopK c_dec curves diverge notably at high L0, Figure 9), and the practical recommendation is to visually identify the "elbow"—a qualitative judgment. The paper acknowledges these limitations in Section 6 but does not fully reckon with how much they reduce the metric's everyday usefulness. The metric is most useful as a sanity check for clearly-too-low L0, but not as a precise estimator of the "optimal" L0.

- **Limited statistical rigor for LLM results.** The paper reports 3 seeds per L0 for sparse probing (Figure 8) but does not provide significance tests or confidence intervals for the F1 differences. Given the ~0.04 effect size, it is unclear whether the peak F1 is meaningfully different from the low-L0 F1.

### Trivial
None.

## Nice-to-Haves
- A quantitative elbow-detection heuristic (e.g., derivative-based, or "the L0 where c_dec is within 1 stdev of its minimum") would be more actionable than visual inspection.
- Investigation of the L0-width interaction: does a wider SAE (more latents) mitigate the low-L0 feature-mixing problem?
- Direct per-latent analysis of LLM SAEs trained at different L0s to show mixing patterns (similar to the toy-model heatmaps), rather than relying solely on the aggregate c_dec metric.

## Removed Points
These points were flagged by reviewers but removed for the following reasons:
- **Critique that the paper's condemnation of sparsity-reconstruction plots is overstated and self-contradictory:** The harsh critic claimed the paper "uses these plots to compare JumpReLU and BatchTopK SAEs (Figure 9)." This is factually incorrect—Figure 9 shows c_dec and sparse probing plots, not standard MSE-vs-L0 sparsity-reconstruction tradeoff plots. The paper's critique of sparsity-reconstruction plots is well-supported by Figure 4's concrete counterexample and is not contradicted by the paper's own experiments.
- **Critique about "single correct L0" not translating from toy models:** The paper explicitly acknowledges this complexity (Section 4.2: "there is likely a range of L0s where some latents are firing more than they ideally should while other latents are firing less"). The critic's framing that this "undermines" the central claim overstates the paper's position—the claim is that L0 matters and must be set correctly, not that a single precise value exists in LLMs.
- **Generic area-of-concern speculation** (e.g., "could the metric be measuring a proxy?") removed per filtering discipline.
- **Missing appendix content** removed per hard rules (appendix stripping is a parser artifact—the original submission contains these sections).
- **Formatting/style nitpicks and complaints about reproducibility of implementation details** removed per hard rules.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Tone down the "most commonly used SAEs" claim** unless the Neuronpedia survey is expanded into the main text with clear statistics. Qualify the LLM conclusions as applying to the specific models and layers tested.
2. **Add significance tests** (or at least error bars) for the sparse probing F1 differences across L0 values.
3. **Provide a quantitative elbow-detection heuristic** for c_dec to reduce reliance on visual inspection.
4. **Add a more direct causal analysis** in LLMs—for example, show that individual LLM latents from low-L0 SAEs mix correlated features (analogous to the toy-model heatmaps in Figures 2–3) rather than relying solely on the aggregate c_dec metric.
5. **Clarify the practical recommendation:** state explicitly that c_dec is a sanity check for clearly-too-low L0, not a precise optimal-L0 estimator, and that its interpretation differs across SAE architectures.

---

## Calibration Details

### Round 1 — Bracketing

**Low anchors (avg < 3.5):**
- *tcsZt9ZNKD.md* — "Scaling and evaluating sparse autoencoders" (avg 1.75). Not comparable—most reviewers panned this paper.
- *89wVrywsIy.md* — "Automatically Identifying and Interpreting Sparse Circuits" (avg 3.40). Reject.

**Middle anchors (3.5 < avg < 7.5):**
- *ghH6YYDs15.md* — "Compute Optimal Inference and Provable Amortisation Gap in SAEs" (avg 4.67, Reject). Similar type of critical SAE paper with theory-toy-model gap. Our paper has cleaner empirical demonstration and more practical relevance.
- *F76bwRSLeK.md* — "Sparse Autoencoders Find Highly Interpretable Features in Language Models" (avg 4.80, Accept). Foundational SAE paper. Our paper is a critical follow-up with comparable empirical quality but narrower scope.
- *ZtvRqm6oBu.md* — "Applying SAEs to Unlearn Knowledge" (avg 5.25, Reject). Our paper has a stronger core finding.
- *5lIXRf8Lnw.md* — "Automatically Interpreting Millions of Features" (avg 5.50, Reject). Our paper has cleaner experimental validation.

**High anchors (avg > 7.5):**
- *9ca9eHNrdH.md* — "Sparse Autoencoders Do Not Find Canonical Units of Analysis" (avg 7.00, Accept). Stronger methodological contribution (stitching, meta-SAEs, BatchTopK). Our paper is less novel methodologically.
- *1Njl73JKjB.md* — "Towards Principled Evaluations of Sparse Autoencoders" (avg 7.00, Accept). More rigorous evaluation framework. Our paper has weaker LLM evidence.
- *LC2KxRwC3n.md* — "A is for Absorption" (avg 7.50, Reject). Very similar critical SAE paper, but rejected due to single-model/single-task scope. Our paper is slightly broader (2 models, 2 architectures) with cleaner toy-model evidence.

**Initial bracket:** Between 4.0 and 6.5.

### Round 2 — Narrowing

Anchors queried inside (4.5, 6.5) and (6.0, 8.0):
- *MDvecs7EvO.md* — "Mechanistic Permutability" (avg 6.50, Accept). Cleaner method paper, more extensive experiments.
- *XAjfjizaKs.md* — "Residual Stream Analysis with Multi-Layer SAEs" (avg 6.50, Accept). Broader scope.
- *imT03YXlG2.md* — "Sparse autoencoders reveal selective remapping of visual concepts" (avg 6.50, Accept).

**Final score:** 5.5. The paper's core insight (low L0 causes feature mixing in a way that sparsity-reconstruction plots miss) is well-demonstrated in toy models and clearly important for SAE practitioners. But the overclaim about "most SAEs" and the gap between toy-model causality and LLM correlation prevent this from reaching the 6.5–7.0 tier. The paper sits above papers with limited experimental support (4.67, 4.80) and below papers with stronger methodological contributions or broader empirical coverage (7.00).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>