## Summary

This paper presents a well-motivated sanity check for sparse autoencoder (SAE) evaluation in mechanistic interpretability. The authors train SAEs on both fully trained and randomly initialized Pythia transformers (across 5 model sizes and multiple randomization schemes) and evaluate them using standard metrics including auto-interpretability AUROC, explained variance, and cosine similarity. The central finding is that these metrics often fail to reliably distinguish between SAEs trained on trained vs. randomized transformers — only an uninformative Gaussian-embedding control is clearly separable. The paper also introduces token-distribution entropy as a proof-of-concept metric that does reveal differences (randomized SAE features remain token-specific while trained features become more abstract in later layers), demonstrating what aggregate metrics miss.

## Strengths

- **Systematic empirical demonstration across model scales and randomization regimes**: The paper compares SAEs on five Pythia model sizes (70M to 6.9B) under five carefully constructed variants (trained, re-randomized with/without embeddings, step‑0 initialization, and a Gaussian‑embedding control). Across a suite of metrics — explained variance, cosine similarity, L¹ norm, fuzzing AUROC, detection AUROC, and CE loss score — the randomized variants consistently overlap with the trained variant while the control is clearly separated (Figure 2). This breadth of evidence across models and conditions makes the core finding robust.

- **Token distribution entropy as a revealing counterexample**: The paper measures the entropy of a latent's activation distribution over token IDs and shows that (a) for trained models entropy increases with layer depth (reflecting more abstract, compositional features), while (b) randomized models exhibit consistently low entropy (indicating single‑token or simple-pattern latents). This is shown in Figure 2 (last row) and directly supports the paper's argument that standard aggregate metrics miss an important dimension of feature quality.

- **Appropriately cautious interpretation**: The paper explicitly states it does not claim SAEs fail to capture meaningful features — only that aggregate metrics alone are insufficient. The limitations section (Section 5) honestly acknowledges scope constraints (Pythia suite, single dataset, one explainer model). The randomization procedure discussion in Section 3 acknowledges and speculates about the parameter-norm preservation artifact rather than hiding it.

- **Plausibility analysis via toy models**: Section 4 provides mechanistic intuition for why random networks might yield high auto-interpretability scores — showing that matrix multiplications preserve superposition (Section 4.1) and that random MLPs can produce representations that SAEs reconstruct as if superposed (Figure 5). The authors appropriately hedge these claims as suggestive rather than explanatory.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No error bars or variability estimates in main figures**: Figures 1 and 2 display point estimates without confidence intervals or error bars. The paper samples 100 latents per SAE and references "Appendix E for multiple random seeds," but the main text does not convey how much the metrics vary across SAE training runs or latent samples. Since the core claim concerns *similarity* between conditions, reporting variability would substantially strengthen the evidence. The pattern is consistent enough across model sizes and metrics that this does not invalidate the findings, but it weakens the quantitative force of the overlap claims.

- **Title overstates the universality of the finding**: The title asserts metrics "Do Not Distinguish Trained and Random Transformers," but the paper's own text properly hedges this ("may not meaningfully distinguish," "in many settings," "under certain conditions"). The abstract and conclusion are appropriately nuanced; the title should match. The paper also shows that for Pythia‑70m the gap is visibly larger, which the title's categorical framing obscures.

- **Toy model connection to transformer results is loose**: Section 4 provides useful intuition but the link to the full-scale transformer results remains suggestive. The Pareto frontier differences between GloVe inputs/outputs and Gaussian controls (Figure 5b) are modest. This does not weaken the paper's empirical contribution, but the section's claims should be read as providing mechanistic plausibility rather than explanation.

### Trivial

- The paper uses only one SAE architecture (TopK, k=32, R=64) in the main results. Robustness to hyperparameters and SAE types is deferred to Appendix C and Figure 18 (stripped). A brief summary statement of the range of conditions tested would help readers assess generality without relying on inaccessible appendix material.

## Nice-to-Haves

- A scatter plot correlating token distribution entropy with AUROC across variants would turn the qualitative entropy observation into a quantitative argument that high AUROC for randomized models coincides with low entropy (trivial token-level features). This would directly quantify what aggregate metrics miss.

- Brief discussion of whether the explainer LLM (Llama-3.1-70B-Instruct) might contribute to inflated AUROC for randomized models by generating plausible-but-shallow token-level explanations. This is not a flaw requiring new experiments, but acknowledging the explainer's role would make the analysis more complete.

- A direct quantitative comparison between trained and randomized metric curves (e.g., mean absolute difference per metric per model size) would help readers assess exactly how similar the results are, beyond visual inspection of Figure 2.

## Removed Points

These points were flagged for removal; treat them with caution.

- **"The absence of any measure of variability across SAE training runs or latent sampling" was demoted from a potentially fatal concern to Minor.** The paper does sample 100 latents and references Appendix E for multiple random seeds. The visible consistency of the pattern across 5 model sizes, 5 variants, and 7 metric rows makes it unlikely that the overlap is an artifact of single-run noise. This is a presentation gap, not an evidential collapse.

- **"The randomization procedure deviates from the original initialization scheme" — REMOVED as a weakness.** The paper already acknowledges and discusses this in Section 3: "We speculate that this pattern arises because parameter norms may differ greatly between a trained model and its state at initialization. In contrast, our randomization procedure was specifically designed to preserve parameter norms." This is not a hidden flaw; the authors surface it transparently.

- **Claim that the paper says metrics "do not distinguish" in all circumstances — DEMOTED.** The paper's text uses appropriately hedged language ("may not meaningfully distinguish," "in many settings"). Only the title is categorical. The abstract and conclusion are properly qualified.

- **"Influence of the explainer LLM should be discussed" — moved to Nice-to-Haves.** This is a worthwhile discussion point but not a weakness in the paper's contribution. The paper's findings are about the insufficiency of aggregate metrics regardless of the explainer used.

- **"Clarify the degree of similarity with direct quantitative comparison" — moved to Nice-to-Haves.** Helpful but not essential; Figure 2 already provides visual comparison across all conditions.

- **"Missing related works" — REMOVED.** Per instructions, we do not flag missing references.

- **Formatting/style nitpicks — REMOVED.** Per instructions, these are parser artifacts, not paper problems.

## Novel Insights

The paper's use of token-distribution entropy to reveal what aggregate auto-interpretability metrics conceal is genuinely novel and instructive. Across all model sizes, randomized SAE latents show consistently low entropy (token-specific features) while trained SAE latents show increasing entropy with layer depth (more abstract, compositional features). This asymmetric pattern — overlapping AUROC but diverging entropy — cleanly demonstrates that high auto-interpretability scores can be achieved by learning trivial token-level features, and that current aggregate metrics are blind to this distinction. This insight points toward a concrete path for better metrics: measuring not just whether an explanation matches activation patterns, but whether those activation patterns reflect abstract, compositional computation rather than surface-level token identity.

## Suggestions

1. Add error bars or confidence intervals to the main figures (even if from the 100-latent sample within a single SAE training run). This would substantially strengthen the quantitative force of the overlap claims without requiring additional compute.

2. Soften the title to match the paper's own appropriately hedged conclusions (e.g., "Automated Interpretability Metrics Often Fail to Distinguish Trained and Random Transformers").

3. Consider adding a scatter plot of entropy vs. AUROC across all variants (perhaps as a compact panel in Figure 2 or a standalone figure). This would make the entropy argument quantitative rather than qualitative, directly showing that randomized models achieve high AUROC through low-entropy (token-specific) features.

4. Add a one-sentence summary in the main text of the robustness checks currently in Appendix C and Figure 18 (e.g., "These results hold across expansion factors 16–128, sparsities 16–32, and with 1B training tokens"), so readers can assess generality without depending on stripped appendix material.

## Score and Decision

**Calibration bracket (Round 1):** Initial retrieval placed this paper between the weak band (1.67–3.40, clearly weaker papers) and the strong band (7.00–8.20, papers with greater technical novelty and depth). Narrowed bracket: 5.0–7.0.

**Round 2 narrowing:** Compared against todLTYB1I7 (5.00, "Principled Evaluation Framework for Neuron Explanations" — proposes sanity checks but with less systematic execution and less clear contribution), 5lIXRf8Lnw (5.50, "Automatically Interpreting Millions of Features" — builds auto-interpretability pipeline but less focused contribution), 9ca9eHNrdH (7.00, "SAEs Do Not Find Canonical Units" — similar critical/limitation paper but with greater technical novelty via SAE stitching and meta-SAEs), and XAjfjizaKs (6.50, "Multi-Layer SAEs" — introduces new architecture with comparable execution quality).

This paper is clearly stronger than the 5.0–5.5 anchors (more systematic, sharper contribution, better execution) and somewhat weaker than the 7.0 anchors (which introduce new methods alongside empirical findings). It sits below XAjfjizaKs (6.50) which has comparable empirical quality but greater technical novelty via a new architecture. The paper's contribution — a well-executed sanity check with clear implications for evaluation practice — is solid and useful but narrow.

**Final score: 6.0.** The paper makes a clear, well-supported contribution that the community should see. The weaknesses (missing error bars in main figures, slightly overstated title, loosely connected toy model) are real but addressable and do not undermine the core empirical finding.

**Anchor papers retrieved across all rounds:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| 89wVrywsIy | 3.40 | 1 (weak) | Clearly weaker; less systematic, narrower contribution |
| Wxl0JMgDoU | 2.50 | 1 (weak) | Clearly weaker; less rigorous |
| 9L9j5bQPIY | 2.50 | 1 (weak) | Clearly weaker; different focus |
| UbLvSPMvMA | 1.67 | 1 (weak) | Clearly weaker |
| 1Njl73JKjB | 7.00 | 1 (mid) | Stronger; introduces evaluation framework with supervised dictionaries |
| ghH6YYDs15 | 4.67 | 1 (mid) | Our paper is stronger; more systematic empirical contribution |
| 9ca9eHNrdH | 7.00 | 1 (mid) / 2 (upper) | Stronger; similar critical stance but greater technical novelty |
| sknUS8X9q0 | 4.00 | 1 (mid) | Our paper is stronger; better execution and clearer contribution |
| tcsZt9ZNKD | 8.20 | 1 (strong) | Significantly stronger; introduced TopK SAEs and scaling laws |
| I4e82CIDxv | 8.00 | 1 (strong) | Stronger; introduced sparse feature circuits |
| k38Th3x4d9 | 8.00 | 1 (strong) | Not comparable; different domain |
| kbjJ9ZOakb | 8.00 | 1 (strong) | Not comparable; different domain |
| 5lIXRf8Lnw | 5.50 | 2 (lower) | Our paper is marginally stronger; sharper, more focused contribution |
| todLTYB1I7 | 5.00 | 2 (lower) | Our paper is stronger; more systematic and better executed |
| yR5QbFv4Xb | 5.33 | 2 (lower) | Not directly comparable; different focus |
| vc1i3a4O99 | 5.00 | 2 (lower) | Our paper is stronger; more systematic |
| XAjfjizaKs | 6.50 | 2 (upper) | Slightly stronger; comparable quality but greater technical novelty |
| imT03YXlG2 | 6.50 | 2 (upper) | Not directly comparable; vision domain |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>