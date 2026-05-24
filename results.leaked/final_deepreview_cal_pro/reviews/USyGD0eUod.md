Now I have a thorough picture. Let me synthesize everything into the final review.

## Summary

This paper performs a sanity check on sparse autoencoder (SAE) evaluation: it trains SAEs on activations from both fully trained and randomly initialized Pythia transformers, then evaluates them using standard metrics including auto-interpretability AUROC ("fuzzing"). The central finding is that aggregate auto-interpretability scores and reconstruction metrics are surprisingly similar between trained and randomized models — particularly for larger models — meaning these metrics alone cannot distinguish learned computations from artifacts of architecture or data structure. The paper introduces token distribution entropy as an alternative metric that does capture meaningful differences (trained models show increasing abstractness across layers; randomized ones show consistently low entropy). A toy-model section (Section 4) provides intuition for why random networks might preserve or amplify superposition structure present in input data.

## Strengths

- **Timely and well-motivated sanity check.** The paper addresses a concrete, important question for the mechanistic interpretability community: whether commonly used metrics actually distinguish learned features from artifacts. The null-model approach (following Adebayo et al., 2020) is appropriately rigorous and the two framing hypotheses about superposition (preservation vs. amplification) give the investigation clear conceptual grounding.

- **Systematic empirical sweep across model scales and randomization conditions.** Figure 2 evaluates seven metrics across five Pythia model sizes (70M to 6.9B) under four different randomization variants plus a Gaussian-input control. The consistency of the pattern — randomized variants tracking trained models while the control separates cleanly — provides converging evidence that the finding is not an artifact of a particular scale or setup. The inclusion of the Step-0 variant (weights at initialization, before any training) alongside the norm-preserving re-randomization variants is a particularly thoughtful control.

- **Token distribution entropy provides a constructive counterpoint.** Rather than merely identifying a failure mode, the paper offers a proof-of-concept metric (entropy of latent activations over token IDs, bottom row of Figure 2) that does distinguish trained from randomized models: trained models show increasing entropy with depth (consistent with increasingly abstract features), while randomized variants show consistently low entropy (single-token features). This strengthens the argument that the problem lies with aggregate metrics specifically, not with SAEs themselves.

- **Toy-model rationale offers plausible mechanistic intuition.** Section 4 demonstrates that random matrix multiplications preserve the parametric form of superposition, and that random MLPs can even amplify sparsity structure in their inputs (Figures 3–5). The GloVe/Pythia embedding analysis (Section 4.3) connects this to language data specifically. The paper appropriately hedges that these are plausibility arguments, not definitive mechanism identification.

- **Careful experimental design with appropriate controls.** The randomization protocols preserve parameter norms and separately control for the role of pre-trained embeddings (re-randomized excl./incl. embeddings). Hyperparameter robustness is checked with different expansion factors and sparsities (Appendix C, Figure 18). The Gaussian-input control correctly establishes a chance-level baseline.

## Weaknesses

### Fatal

None.

### Major

None. The core claim — that aggregate auto-interpretability scores can be similar between trained and randomized transformers and are thus insufficient on their own — is well-supported by the evidence presented.

### Minor

- **No statistical quantification of the similarity claim.** Figures 1 and 2 show point estimates without error bars, confidence intervals, or distributional information. While the pattern is consistent across many layers and model sizes, reporting bootstrap confidence intervals over the 100 sampled latents (or showing the full per-latent distribution) would transform the visual argument into a quantitatively credible one. This is addressable with existing data and does not undermine the core finding, but it would strengthen the paper substantially.

- **Title and abstract overstate the scope of metrics tested.** The title says "Automated Interpretability Metrics" (plural) and the abstract refers to "auto-interpretability scores," but the main evaluation centers on a single scoring scheme (fuzzing) implemented with a single LLM (Llama-3.1-70B-Instruct). Detection scoring appears in an appendix (stripped in the reviewer copy), and simulation scoring (the original Bills et al. method) is not tested. The paper notes that fuzzing correlates with simulation scoring (Paulo et al., 2024), which provides some justification, but the framing should be tightened to match what was actually evaluated. This is a presentation issue rather than an evidential one.

- **Limited model family and explanation-generator diversity.** Only the Pythia model family is tested, and only Llama-3.1-70B-Instruct is used for explanation generation and fuzzing evaluation. The paper acknowledges these limitations in Section 5, and the Pythia family is a reasonable and widely-used choice. However, the generality of the finding across transformer architectures and explanation-generator LLMs remains an open question.

- **Toy-model section sits somewhat apart from the main empirical narrative.** Section 4 provides interesting intuition, but its connection to the transformer-scale results remains speculative, as the paper itself acknowledges ("we leave the question of which predominates... to future work"). The section could be tightened or partially moved to an appendix without weakening the central contribution.

### Trivial

- The computation of token distribution entropy ("total latent activation per token across the set of maximally activating examples") is described only in prose and could benefit from a precise mathematical definition for replicability.
- The CE loss score row in Figure 2 is plotted for the trained variant only (which is correct, since randomized models have poor loss regardless), but the grid layout could be visually misleading; a clearer separation or annotation would help.

## Nice-to-Haves

- A short, concrete recommendation for what a "routine randomized baseline" should look like (e.g., "train an SAE on a randomly initialized version of the target model and compare the distribution of AUROC scores") would give practitioners an actionable takeaway beyond the general admonition.
- A brief discussion of the relationship between auto-interpretability scores and causal feature importance (e.g., noting that a high-scoring feature from either a trained or random model might still be causally inert) would add useful nuance.
- A small qualitative study showing example explanations for high-scoring random-model latents alongside their maximally activating examples would make the abstract claim concrete and persuasive for readers less familiar with the metrics.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "The paper's core empirical claim... is presented without any quantification of statistical variability" — KEPT but downgraded to Minor.** The concern is valid (no error bars), but the claim is supported by consistency across many layers and model sizes, making the lack of error bars a presentation weakness rather than an evidential gap. The harsh critic's suggestion that this might "weaken the 'do not distinguish' conclusion" is speculative — the consistent pattern across dozens of data points makes it unlikely that all trained-randomized differences would vanish under proper uncertainty quantification.

- **Harsh Critic: "The breadth of the claim relative to the evidence... the evaluation centers on a single scoring scheme (fuzzing)" — KEPT but downgraded to Minor.** The paper does test detection scoring in Appendix B and cites correlation with simulation scoring. The title overclaim is a presentation issue. The harsh critic's characterization as "not yet supported for the entire class of methods" is partially addressed by the appendix and the cited correlation.

- **Harsh Critic: "The entropy analysis... would benefit from even a small validation (e.g., showing that human raters judge high-entropy features as more abstract)" — MOVED to Nice-to-Haves.** This is scope creep: the paper presents entropy as a proof-of-concept, not a validated diagnostic. Demanding human validation for a proof-of-concept metric is disproportionate.

- **Strength Finder: "A toy-model rationale for why random networks produce interpretable SAE latents" — KEPT but softened.** The toy model is useful intuition but, as the paper acknowledges, does not definitively establish mechanism. The strength is valid but should be presented with the caveat that this section is speculative.

- **Harsh Critic: "the cross-entropy loss score is plotted for the trained variant only... a clearer visual separation would help" — MOVED to Trivial.** The paper explicitly explains this choice ("the CE loss score only makes sense for the trained variant"), so this is purely a presentation nitpick.

- **Harsh Critic: "Acknowledging that a high-scoring feature might still be causally inert... would add nuance" — MOVED to Nice-to-Haves.** This is outside the paper's stated scope; adding it would be nice but its absence is not a weakness.

## Novel Insights

The paper's most distinctive insight is the combination of its null-model methodology with the token entropy metric: by showing that aggregate metrics fail while a simple distributional measure succeeds, it pinpoints *what* is missing from current evaluation — namely, any notion of feature abstractness or complexity that increases across layers. The toy-model connection between random matrix multiplication and superposition preservation, while speculative, offers a concrete mechanistic hypothesis for *why* random networks produce apparently interpretable features, moving beyond mere observation toward explanation. This pairing of empirical diagnosis with mechanistic hypothesis is more constructive than a typical "metrics are broken" paper.

## Suggestions

- Add bootstrap confidence intervals (e.g., 95% CI over the 100 sampled latents) to Figures 1 and 2, and report a simple summary statistic such as the maximum mean AUROC difference between trained and randomized variants across all layers. This would turn the qualitative similarity observation into a reproducible quantitative claim.
- Tighten the title and abstract to specify that the primary finding concerns fuzzing-based auto-interpretability AUROC (with detection results in appendix), rather than implying all automated interpretability metrics were tested. Consider "Fuzzing-Based Auto-Interpretability Scores Do Not Distinguish Trained and Random Transformers" or similar.
- Provide a precise mathematical definition of the token distribution entropy computation for replicability.
- Consider condensing Section 4 or moving parts of it to an appendix to keep the main text focused on the empirical results, which are the paper's strongest contribution.

## Score and Decision

### Calibration anchors retrieved:

**Round 1 (bracketing):**
- `Wxl0JMgDoU` — avg 2.50: SAE + chess skill analysis, rejected. Much weaker than our paper.
- `89wVrywsIy` — avg 3.40: SAE circuit analysis with hierarchical tracing, rejected. Weaker.
- `F76bwRSLeK` — avg 4.80: "SAEs Find Highly Interpretable Features in LMs," foundational paper. Our paper is a critical evaluation building on this work; more focused but narrower.
- `1Njl73JKjB` — avg 7.00: "Towards Principled Evaluations of SAEs," proposes supervised dictionary evaluation framework. Similar critical-evaluation spirit; our paper is less technically novel but broader in empirical sweep.
- `9ca9eHNrdH` — avg 7.00: "SAEs Do Not Find Canonical Units of Analysis," critical evaluation with novel techniques (stitching, meta-SAEs). Our paper is comparable in critical spirit but less methodologically innovative.
- `tcsZt9ZNKD` — avg 8.20: "Scaling and evaluating sparse autoencoders," major contribution (TopK SAEs, scaling laws, GPT-4). Much stronger than our paper.
- `syThiTmWWm` — avg 7.75: "Cheating Automatic LLM Benchmarks," null-model sanity check for LLM benchmarks. Very similar spirit; that paper is more comprehensive and surprising.

**Round 2 (narrowing):**
- `Ebt7JgMHv1` — avg 6.33: "Is This the Subspace You Are Looking For?", interpretability illusion in activation patching. Comparable critical-evaluation paper; our paper is similarly well-executed but more empirical and less theoretical.
- `v675Iyu0ta` — avg 5.60: "Interpretability Illusions in the Generalization of Simplified Models," single case study. Our paper is broader and more systematic.
- `XAjfjizaKs` — avg 6.50: "Residual Stream Analysis with Multi-Layer SAEs," solid SAE contribution. Our paper is comparable in quality.

**Initial bracket from Round 1:** 5.5–7.5

**Round 2 narrowing:** The paper sits between the 6.33 anchor (Ebt7JgMHv1, similar "interpretability illusion" paper) and the 7.0 anchors (more methodologically innovative SAE evaluation papers). Our paper is more empirically thorough than Ebt7JgMHv1 (5 model sizes vs. 2 tasks) but less theoretically sophisticated than the 7.0 anchors. The paper's contribution is real and well-executed but incremental — it confirms a suspicion many in the community may already hold, with systematic evidence. Score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>