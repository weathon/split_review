Now I have all the calibration data I need. Let me synthesize the final review.

**Round 1 bracket:** Based on initial calibration, I placed the paper between ~5.5 and ~7.5. The weak anchors (avg 3.0-3.25) were clearly worse papers, while the strong anchors (avg 7.75-8.2) were method papers with different contributions. The most analogous papers were in the 5.6-7.0 range.

**Round 2 narrowing:** Comparing against `OZWHYyfPwY` ("Don't Trust Your Eyes," 7.0, Reject), `todLTYB1I7` ("Principled Evaluation Framework," 5.0, Reject), `Hf17y6u9BC` ("Activation Patching Best Practices," 6.67, Accept), and `v675Iyu0ta` ("Interpretability Illusions," 5.6, Reject), the current paper is stronger than the 5.0-5.6 papers (more comprehensive, real LLMs) and comparable to the 6.67-7.0 papers. It sits slightly below "Don't Trust Your Eyes" due to the fuzzing-vs-simulation gap which limits the strength of the central claim.

**Final score: 6.5**

---

## Summary

This paper applies the "randomized baseline" sanity check (Adebayo et al., 2020) to sparse autoencoder (SAE) evaluation metrics. Across five Pythia model sizes (70M–6.9B) and multiple randomization schemes, it shows that aggregate auto-interpretability AUROC scores (fuzzing protocol) and several reconstruction metrics for trained transformers are similar to those for randomly initialized transformers, while a Gaussian-embedding control correctly scores at chance. The paper also introduces token distribution entropy as a metric that *does* reveal differences, and provides toy-model analysis suggesting why random networks preserve sparse structure.

## Strengths

1. **Systematic empirical evidence across model scales and randomization schemes.** The paper tests five Pythia model sizes (70M to 6.9B), four randomized variants (Step-0, re-randomized incl. and excl. embeddings, Gaussian control), and seven evaluation metrics in a 7×5 grid (Figure 2). This breadth convincingly establishes that the failure of aggregate auto-interpretability AUROC to distinguish trained from random transformers is not a fluke of one model size or random seed. The control condition (Gaussian embeddings) correctly scores at chance (AUC=0.50), confirming the metrics are not simply insensitive but specifically fail to differentiate trained from structurally plausible random alternatives.

2. **Token distribution entropy as a proof-of-concept metric that succeeds.** The paper proposes a simple, targeted measure—entropy of latent activations over token IDs—and shows it reveals qualitative differences that aggregate scores miss (Figure 2, last row). For trained models, entropy increases with layer depth (indicating more abstract, less token-specific features), while for randomized variants it stays low. This provides a concrete, actionable starting point for developing better SAE evaluation, not just a critique.

3. **Appropriate caution in interpretation and clear limitations section.** The paper does not claim SAEs fail to learn meaningful features—only that the common aggregate metrics are insufficient to certify that they have. The limitations section is explicit about the scope (Pythia models, TopK SAEs, RedPajama dataset), and the conclusion is measured and constructive.

## Weaknesses

### Major

1. **The central claim rests on fuzzing AUROC without validation against simulation scoring — an evidential gap.** The paper relies on the "fuzzing" auto-interpretability protocol (Paulo et al., 2024) as its primary interpretability measure, citing its correlation with simulation scoring (Bills et al., 2023). However, correlation in ordinary settings does not guarantee both metrics behave identically on random models. It is possible that simulation scoring *does* distinguish trained from random (as prior work by Bricken et al. suggests for one-layer transformers). The paper acknowledges this as a limitation (line 98: "this measure has been demonstrated to correlate with simulation scoring") but does not test it, even on a small subset. The reader cannot determine whether the failure is a property of automated metrics in general or of fuzzing specifically. This gap weakens the headline claim that "automated interpretability metrics" in general fail — the evidence directly supports only the fuzzing variant.

2. **Title and framing overstate the breadth of the finding.** The title — "Automated Interpretability Metrics Do Not Distinguish Trained and Random Transformers" — implies a universal failure. The paper's own results show a more nuanced picture: (a) cross-entropy loss recovery *cannot be applied at all* to random variants, which is itself a form of distinguishing; (b) token distribution entropy *does* systematically distinguish trained from random; (c) for some metrics (e.g., explained variance, cosine similarity), the picture is mixed across layers and model sizes. The abstract and conclusion are more measured ("in many settings," "under certain conditions"), but the title misleads casual readers. A more precise framing would be "Aggregate Auto-Interpretability Scores Do Not Reliably Distinguish Trained from Random Transformers."

### Minor

3. **The observation that randomized variants sometimes achieve *higher* AUROC than trained (Figure 1: trained AUC 0.79 vs. randomized 0.87–0.88 for Pythia-6.9b) is not discussed in the main text.** This is arguably the most striking and informative aspect of the result — it suggests random models can appear *more* interpretable by this metric. The figure caption reports the values, but the body text only says the curves "overlap" or are "similar" without noting the direction. Discussing this would strengthen the paper's argument.

4. **No statistical testing or uncertainty quantification on AUROC comparisons.** The paper samples 100 latents per SAE, enabling statistical comparisons (e.g., Mann-Whitney U test, effect sizes) between trained and random variants. Currently, "similar" is used qualitatively. Reporting confidence intervals or significance tests would quantify when differences are genuinely negligible vs. small but detectable.

5. **The toy model section (Section 4) is suggestive but does not directly connect to the transformer results.** The section shows that random MLPs can preserve/amplify superposition in toy data and that word embeddings exhibit structure recoverable by SAEs. However, no direct measurement is made of whether the superposition or sparsity levels in *random transformer activations* predict the similarity in auto-interpretability scores. The connection remains a plausible hypothesis rather than evidence for the mechanism. This doesn't weaken the empirical finding, but the toy section could be condensed or repositioned as speculation without affecting the main result.

### Trivial

6. The term "AUROC (Pruned)" in Figure 2 is not defined in the main text; clarification of the post-processing step would help.

## Nice-to-Haves

- Validating simulation scoring on a subset (e.g., Pythia-160m, layers 0 and 4, trained vs. Step-0) would substantially strengthen the central claim.
- A brief discussion of whether other SAE architectures (Gated, JumpReLU) might behave differently would be helpful context.
- The 1B-token training robustness check mentioned in the appendix could be elevated to the main paper.

## Removed Points

- *"Missing related work"* — removed per instructions (cannot verify existence of missing references).
- *"Reproducibility concerns about undisclosed hyperparameters"* — removed; hyperparameters are specified (k=32, expansion factor=64, 100M tokens, TopK SAE).
- *"Formatting/presentation nitpicks"* — removed per instructions (parser artifacts).
- *"Weaknesses about the toy model being 'mathematically trivial'"* — removed; the mathematical point about linear transformations preserving superposition is simple but correctly contextualized as a starting point for intuition, not the paper's main contribution.
- *"The toy model mechanism should be different from what is claimed"* — moved here; the paper's framing ("preserve or amplify") is consistent with the actual finding that random NNs homogenize sparsity structure; the distinction is minor.
- *"Should test more architectures beyond Pythia"* — removed as scope creep; testing five model sizes in one family with extensive randomization schemes is already comprehensive for a single paper.
- Generic strengths from Strength Finder about "important problem" — removed as superficial; only concrete, evidence-grounded strengths are retained.

## Novel Insights

The most interesting insight from the combined reviews is that **the paper's strongest evidence is also its least discussed**: the fact that randomized variants sometimes produce *higher* auto-interpretability AUROC than trained models (Figure 1, Pythia-6.9b). This inverts the usual logic — it is not just that metrics fail to distinguish, but that a random model can systematically appear *more* interpretable. This points toward a deeper issue: whatever statistical regularities the fuzzing protocol picks up may be partially *destroyed* by training (which introduces more complex, less token-id-correlated features), rather than created by it. This is a genuinely valuable observation that deserves more prominence in the paper.

## Suggestions

1. **Test simulation scoring on a small subset** (e.g., one model size, one layer, ~50 latents) to validate that the fuzzing result extends to the more expensive protocol. This single experiment would resolve the main evidential gap.
2. **Revise the title** to something more precise, e.g., "Aggregate Auto-Interpretability Scores Do Not Reliably Distinguish Trained from Random Transformers."
3. **Add statistical comparisons** (e.g., confidence intervals or effect sizes) for the AUROC differences between trained and random variants across layers.
4. **Elevate the discussion of the direction of AUROC differences** — the fact that randomized variants *exceed* trained in AUROC for large models is an important finding that the paper should analyze rather than mention only in the figure caption.

## Score and Decision

**Anchors consulted (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| wwO8qS9tQl (ALMANACS) | 3.00 | 1 | Worse — narrower scope, different focus |
| RBqvU12SHz (Structural Probing) | 3.25 | 1 | Worse — less comprehensive |
| bXeSwrVgjN (Benchmarking Deletion Metrics) | 6.00 | 1 & 2 | Slightly worse — narrower metric focus, no model scaling |
| v675Iyu0ta (Interpretability Illusions) | 5.60 | 1 | Worse — single Dyck language case study vs. real LLMs |
| syThiTmWWm (Cheating Auto Benchmarks) | 7.75 | 1 | Better — cleaner/surprising result with direct implications |
| tcsZt9ZNKD (Scaling SAEs) | 8.20 | 1 | Better — different category (method paper with scaling laws) |
| I4e82CIDxv (Sparse Feature Circuits) | 8.00 | 1 | Better — different category (method paper) |
| PdaPky8MUn (Never Train from Scratch) | 8.00 | 1 | Better — different topic |
| todLTYB1I7 (Principled Eval Framework) | 5.00 | 2 | Worse — narrower, vision-only, less comprehensive |
| OZWHYyfPwY (Don't Trust Your Eyes) | 7.00 | 2 | Comparable — similar critique of interpretability tools; current paper more comprehensive but lacks theoretical component |
| Hf17y6u9BC (Activation Patching Best Practices) | 6.67 | 2 | Comparable — similar empirical-critique genre; current paper has broader model scaling |
| X0r4BN50Dv (F-Fidelity) | 6.67 | 2 | Slightly better — more novel methodological contribution |

**Round 1 bracket:** 5.5–7.5

**Narrowing:** Comparison with round-2 anchors, particularly "Don't Trust Your Eyes" (7.0, similar critique paper), "Activation Patching Best Practices" (6.67, similar empirical standardization), and "Principled Eval Framework" (5.0, narrower scope) places the paper at 6.5. It is stronger than 5.0–5.6 papers due to comprehensive real-LLM experiments, and comparable to 6.67–7.0 papers but slightly below due to the fuzzing-vs-simulation evidential gap and title overclaim.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>