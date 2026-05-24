Now I have a clear calibration picture. Let me finalize my analysis and write the review.

**Calibration Summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| UbLvSPMvMA | 1.67 | R1 | Much weaker — unclear contribution, poor execution |
| Wxl0JMgDoU | 2.50 | R1 | Weaker — narrow scope, poorly executed |
| sknUS8X9q0 | 4.00 | R1 | Weaker — confusing presentation, unclear novelty |
| F76bwRSLeK | 4.80 | R1 | Weaker — limited evaluation, high reconstruction loss |
| todLTYB1I7 | 5.00 | R2 | Slightly weaker — evaluation framework but less comprehensive |
| OeHSkJ58TG | 5.67 | R2 | Comparable but more limited scope |
| bXeSwrVgjN | 6.00 | R2 | Comparable in quality |
| **Ebt7JgMHv1** | **6.33** | R2 | **Most comparable** — negative finding about interpretability, toy+real experiments, accepted |
| Tj3xLVuE9f | 6.80 | R2 | Slightly stronger — more theoretical depth |
| **OZWHYyfPwY** | **7.00** | R2 | Slightly stronger — negative finding + theory, cleaner, rejected (!) |
| 1Njl73JKjB | 7.00 | R1 | Slightly stronger — principled framework, accepted |
| I4e82CIDxv | 8.00 | R1 | Stronger — major contribution |
| tcsZt9ZNKD | 8.20 | R1 | Much stronger — major multiple contributions |

The paper under review is closest to Ebt7JgMHv1 (6.33, accepted) — a well-executed negative finding about an interpretability method with both toy models and real experiments. Our paper has more comprehensive empirical coverage (5 model sizes, 5 variants, 7 metrics) but slightly less theoretical depth. I'd place it at **6.0**.

---

## Summary
This paper demonstrates that widely-used sparse autoencoder (SAE) evaluation metrics — including auto-interpretability AUROC, explained variance, and reconstruction metrics — fail to reliably distinguish features derived from trained Pythia transformers from those derived from randomly initialized ones. Over five model sizes (70M–6.9B), five model variants (trained, two re-randomization schemes, Step-0, and a Gaussian-embedding control), and seven evaluation metrics, the authors show consistent overlap between trained and randomized models. The token distribution entropy metric is introduced as a proof-of-concept that does distinguish them, revealing that randomized features tend to be token-specific rather than abstract. The paper argues that high aggregate auto-interpretability scores are insufficient evidence that SAEs have recovered learned computational features, and recommends routine use of randomized baselines.

## Strengths
- **Comprehensive experimental design with rigorous null models**: The paper compares five distinct model variants (trained, re-randomized incl. and excl. embeddings, Step-0, Gaussian-embedding control) across the full Pythia suite (70M–6.9B). The control condition (Gaussian token embeddings) convincingly validates that the pipeline can produce chance-level scores when features are truly absent, ruling out measurement artifacts (Figure 1, Figure 2).
- **Converging evidence from multiple evaluation metrics**: Beyond auto-interpretability AUROC (both fuzzing and detection), the paper reports explained variance (R²), cosine similarity, L1 norm, CE loss score, and token distribution entropy across layers and model sizes (Figure 2). The consistent overlap across these diverse metrics strengthens the negative finding considerably.
- **Token distribution entropy as a proof-of-concept alternative**: The entropy metric (Figure 2, last row) cleanly separates trained from randomized variants, showing that randomized features remain token-specific while trained features become more abstract in deeper layers. This directly demonstrates that current aggregate metrics miss an important dimension of feature quality and provides a constructive path forward.
- **Mechanistic plausibility via toy models**: Sections 4.1–4.3 provide a clear linear-algebraic demonstration that matrix multiplication preserves superposition and that random MLPs can amplify sparsity. The GloVe/Pythia embedding experiments (Figure 5) connect the toy analysis to real language representations, offering plausible mechanisms for why random transformers yield non-trivial SAE features.

## Weaknesses

### Fatal
None.

### Major
- **No statistical quantification of overlap in main text**: All main figures (Figures 1, 2) report only point estimates — no error bars, confidence intervals, or distributional overlap measures. The central claim that metrics "do not distinguish" trained from random requires showing that the distributions genuinely overlap, not just that point estimates are close. The paper references Appendix E for multiple random seeds, but the stripped appendix prevents verification, and the main text itself provides no quantitative support for the indistinguishability claim at the level of statistical rigor. The multi-model, multi-layer, multi-metric convergence provides some informal confidence, but a paper making a "do not distinguish" claim needs to demonstrate this directly.

### Minor
- **Random > trained inversion cases go unremarked**: In Figure 1 (Pythia-6.9b), the randomized variants achieve AUROC 0.87–0.88 while the trained variant scores 0.79. The paper frames these as "similar" or "overlapping," but randomized models actually *outperform* trained ones on this metric. This inversion is neither discussed nor analyzed — yet it actually strengthens the paper's argument (the metric is not merely uninformative but can be actively misleading). A brief qualitative analysis of what kinds of explanations produce these higher scores would deepen the contribution.
- **Toy model connection to transformers remains speculative**: Sections 4.1–4.3 provide plausible mechanisms but the gap between 2D/3D toy models and full Pythia transformers is not bridged empirically. The paper acknowledges this ("we leave the question…to future work"), so this is appropriately hedged — but the section reads more as motivated speculation than as rigorous explanation of the main empirical findings.
- **Single explainer model and data corpus**: Only Llama-3.1-70B-Instruct is used for explanation generation, and only RedPajama for SAE training. Both are correctly noted as limitations in Section 5, but a reader might wonder whether the similarity between trained and random scores is pipeline-specific.

### Trivial
- The abstract states metrics "do not distinguish" trained and random transformers, while the body uses more measured language ("surprisingly similar," "insufficient to guarantee"). Aligning the abstract to the body's more careful framing would improve precision.

## Nice-to-Haves
- Varying the explainer model (size, family) or the auto-interpretability prompt strategy would reveal whether the similarity between trained and random scores is pipeline-specific or fundamental.
- A brief qualitative analysis of cases where randomized models achieve higher AUROC than trained ones (Figure 1) would turn an overlooked pattern into additional supporting evidence.
- Reporting a rank-based or classifier-based measure of distributional overlap between trained and randomized variants (e.g., training a classifier to separate them from the metric values) would directly quantify the indistinguishability claim.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **Harsh critic: "SAE training details (number of epochs, learning rate, convergence diagnostics) are sparse"** → REMOVED. Per removal rules, undisclosed hyperparameters and trivial implementation details are not valid criticisms. The paper specifies architecture (TopK, expansion 64, k=32), training data volume (100M tokens), and references the implementation base (Belrose et al., 2025).
- **Harsh critic: "Robustness checks in the appendix... are referenced but not visible"** → REMOVED. The appendix is stripped by the parser; the paper's references to Appendix C/E are valid. Per hard rules, we do not criticize missing appendix content.
- **Harsh critic: "Ablating the auto-interpretability pipeline" (varying explainer model, prompt, scoring)** → MOVED to Nice-to-Haves. This is an extension, not a flaw in the presented work.
- **Harsh critic: "Discussion of polysemanticity vs. superposition adds marginal value"** → REMOVED. This is a subjective judgment about related work coverage; the paper uses this distinction to clarify its scope.
- **Strength Finder: "Robustness across SAE hyperparameters and data scales"** → RETAINED but noted as dependent on stripped appendix content.
- **Strength Finder: "Use of a strong, open-source auto-interpretability pipeline and large explainer model"** → REMOVED as a standalone strength. This is an implementation detail, not a contribution. It's table-stakes for the experiment, not a strength to highlight.

## Novel Insights
The paper's most genuinely novel observation is that randomized transformers actually yield SAE features with *higher* auto-interpretability scores than trained ones in some cases (Figure 1, randomized AUROC 0.87–0.88 vs trained 0.79), yet the paper itself does not explore this. Beyond what the paper already contributes, the reviews surface that the paper's finding connects to a broader pattern in interpretability research: multiple recent papers (OZWHYyfPwY on feature visualizations, Ebt7JgMHv1 on subspace patching) have independently discovered that popular interpretability methods can produce compelling-looking results that fail basic sanity checks. This paper's contribution is a well-executed instance of this pattern applied to SAE evaluation metrics.

## Suggestions
- **Add distributional overlap quantification**: Even a simple addition like ±1 SD bands around the point estimates in Figure 2, bootstrapped from the 100 latents per layer, would substantially strengthen the central claim. If Appendix E's multiple-seed results are solid, a summary panel in the main text would be ideal.
- **Discuss the random > trained inversion explicitly**: A paragraph addressing Figure 1's AUROC inversion — noting that this actually strengthens the argument by showing the metric can be actively misleading — would turn a silent pattern into supporting evidence and preempt reader confusion.
- **Tighten the abstract**: Replace "do not distinguish" with "often fail to distinguish" or "can produce similar scores for" to match the body's measured tone.

## Score and Decision

This is a well-executed negative-result paper that makes an important contribution to mechanistic interpretability: showing that common SAE evaluation metrics fail a basic null-model sanity check. The experimental design is comprehensive (5 variants × 5 model sizes × 7 metrics), the control condition validates the pipeline, and the token entropy metric provides a constructive alternative. The main weaknesses are the absence of statistical quantification in the main text and the undiscussed inversion cases where random outperforms trained — both are addressable and neither invalidates the core finding. Calibrated against comparable negative-finding interpretability papers (Ebt7JgMHv1 at 6.33, OZWHYyfPwY at 7.00), this paper sits at a similar level of contribution with more comprehensive empirical coverage but less theoretical depth.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>