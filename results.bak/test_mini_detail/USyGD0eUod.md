Now I have all the information I need. Let me produce the consolidated review.

---

## Summary

This paper tests whether commonly used SAE auto-interpretability metrics (fuzzing/detection AUROC) can distinguish trained transformers from randomly initialized ones across Pythia models spanning 70M to 6.9B parameters, with four randomization schemes. The central finding is that these aggregate metrics produce remarkably similar scores for trained and randomized models — both are far from the Gaussian-input control (chance), but nearly indistinguishable from each other. The paper recommends always including randomized baselines and developing targeted measures of feature "abstractness" like the proposed token distribution entropy.

## Strengths

1. **Important, timely negative finding.** The paper challenges a widespread assumption in SAE-based mechanistic interpretability — that high auto-interpretability scores indicate discovery of learned, computationally relevant features. Given the rapid adoption of auto-interpretability pipelines (Paulo et al., Bills et al.), this sanity check is both valuable and actionable. The results are clearly presented in Figures 1 and 2, showing trained and randomized variants clustered together and well above the control across dozens of settings.

2. **Broad experimental design.** The paper evaluates five Pythia model sizes (70M–6.9B), four randomization variants (re-randomized incl./excl. embeddings, Step-0, and a Gaussian-input control), and seven metrics (explained variance, cosine similarity, L1 norm, two AUROC variants, CE loss score, token entropy). This breadth rules out narrow explanations (e.g., "it only happens for one model size" or "only for one metric") and makes the finding substantially more robust than a single-model, single-metric study would be.

3. **Token distribution entropy as a distinguishing complementary metric.** The entropy analysis (last row of Figure 2) reveals that trained models show increasing entropy across layers (more abstract, less token-specific features), while randomized models stay flat and low. This provides a concrete proof-of-concept for the paper's recommendation to supplement aggregate metrics with targeted measures of feature abstractness, and suggests a path forward rather than merely critiquing existing methods.

4. **Toy model analysis providing mechanistic insight.** Section 4 demonstrates via controlled toy experiments that randomly initialized neural networks can preserve or amplify superposed structure in their inputs (Figures 3–5). This directly addresses the "why" behind the main finding, and the Pareto-frontier analysis showing that random MLP outputs are harder to distinguish from superposed inputs than Gaussian controls provides a concrete mechanistic rationale. The section is well-motivated and supports rather than distracts from the core claim.

5. **Clear writing and appropriate self-awareness of limitations.** The paper is well-structured and clearly written. The limitations section (Section 5) honestly acknowledges the scope (Pythia family, TopK SAE architecture, specific metrics) and explicitly states what the paper does *not* claim. This candor strengthens the paper's credibility.

## Weaknesses

### Fatal

None.

### Major

1. **Main figures lack error bars or statistical testing.** Figures 1 and 2 present single lines per variant with no confidence intervals, shaded regions, or measures of variability. The paper mentions "multiple random seeds" (Appendix E), but the main visual evidence — which must stand alone for review — does not incorporate this information. For a paper making a *negative claim* (metrics *do not distinguish*), the lack of uncertainty quantification is significant: the reader cannot assess whether the small differences between trained and randomized variants are within measurement noise or represent real (if small) distinctions. The paper would be substantially strengthened by adding error bars (e.g., standard error across SAE training seeds or random re-randomizations) and/or a simple statistical test (e.g., comparing per-latent AUROC distributions between trained and random variants).

### Minor

2. **Token distribution entropy is preliminary and unvalidated.** The paper correctly describes this metric as "preliminary" and "not a direct measure of abstractness," but it remains a weak reed for the claim that trained and random models produce qualitatively different features. The entropy measure has not been validated against human judgments of feature abstractness, and its relationship to polysemanticity or computational relevance is asserted rather than demonstrated. This does not undermine the paper's main claim (which rests on the AUROC results), but it does limit the strength of the positive prescription.

3. **The title is slightly broader than the experimental scope.** "Automated Interpretability Metrics Do Not Distinguish Trained and Random Transformers" implies a more exhaustive sweep (simulation scoring, other SAE architectures like Gated/JumpReLU, other model families) than the paper actually covers. A more precise phrasing — e.g., "Common SAE Auto-Interpretability Metrics Fail to Distinguish Trained from Random Transformers in Pythia Models" — would better match the evidence. The limitations section acknowledges the scope, so this is a framing issue rather than a scientific one.

### Trivial

None.

## Nice-to-Haves

- A small-scale verification using simulation scoring (Bills et al.) on a subset of latents would strengthen the claim that the failure to distinguish extends beyond the cheaper fuzzing/detection proxies.
- Testing on a second model family (e.g., GPT-2 or Llama-2-7B) would increase generality, but this is expectedly out of scope for a single paper and the practical barriers are high (SAE training cost).

## Removed Points

The following points from the reviews were checked against the paper and removed with justification:

1. **"Latent sampling procedure unclear"** — The paper explicitly states: "we randomly sampled 100 features to obtain auto-interpretability scores" (line 98). This is clear and answers the question. Removed as factually incorrect.

2. **"Toy model section is disconnected from the core claim"** — Section 4 directly addresses the question of *why* random networks might yield interpretable latents. Figures 3–5 show that random NNs preserve/amplify superposition, providing mechanistic support for the main result. Removed as inaccurate.

3. **"Missing simulation scoring"** — The paper explains that simulation scoring is expensive and that fuzzing has been shown to correlate with it (citing Paulo et al. 2024). This is a justified methodological choice, not a weakness.

4. **"Testing on a second model family"** — The paper acknowledges this as a limitation. Requesting experiments on additional model families beyond the already-broad Pythia suite is scope creep.

5. **"Figure 2 is too dense / line colors are similar"** — A formatting/presentation nitpick that does not affect the scientific content. Removed.

6. **"Related work contrast could be highlighted earlier/more directly"** — This is a presentational suggestion, not a weakness of the paper's scientific contribution.

7. **"Limitations paragraph does not mention error bars"** — The paper does discuss the scope limitations honestly. The absence of an explicit mention of error bars is a minor oversight, already covered under Weakness #1 above.

8. **Strength Finder: generic strengths about importance of problem** — Removed because they lack specificity and are not grounded in concrete evidence from the paper. E.g., "the paper identifies a real and important problem" is generic and conflicts with the weaker aspects of the evaluation.

## Novel Insights

The reviews do not surface any genuinely novel observation beyond the paper's own contributions. The harsh critic's framing of the error-bars issue is the most insightful criticism, but it is a standard methodological expectation rather than a novel perspective. The strength finder correctly identifies the core contributions without adding interpretive value.

## Suggestions

1. **Add error bars or confidence bands to Figures 1 and 2**, using variation across random seeds for SAE training and/or model re-randomization. Even a simplified treatment (e.g., reporting the range or standard error across seeds as shaded regions) would substantially strengthen the evidence.
2. **Perform and report a simple statistical comparison** between the per-latent AUROC distributions of trained and randomized variants (e.g., two-sample KS test) for a representative subset of settings. If the differences are not statistically significant, report this explicitly; if they are significant for some layers/model sizes, discuss what that means.
3. **Consider a more precise title** that signals the scope (Pythia models, SAE auto-interpretability metrics), e.g., "Common SAE Auto-Interpretability Metrics Fail to Distinguish Trained from Random Transformers."
4. **Validate the token distribution entropy** more thoroughly, even with a simple sanity check (e.g., correlation with percentage of activations on a single token ID, or with human-annotated feature abstractness on a small sample).

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries on "SAE auto-interpretability metrics sparse autoencoders transformers" with score bands (-1, 3.5), (3.5, 7.5), (7.5, 11).  

- Weak band anchors: scores 2.50–3.40 (chess SAE paper, hierarchical tracing, geometry of concepts, reward model SAE). These papers are significantly weaker — narrow scope, poor presentation, or unsubstantiated claims. Our paper is clearly above.  
- Middle band anchors: scores 4.00–7.00 (SAGE 4.00, Rethinking Evaluation 5.75, Residual Stream Analysis 6.50, Towards Principled Evaluations 7.00).  
- Strong band anchors: scores 7.75–9.00 (Scaling and evaluating SAEs 8.20, Sparse Feature Circuits 8.00, Knowledge Awareness 9.00). These are landmark papers — TopK SAE introduction, feature circuits, mechanistic interpretability breakthroughs. Our paper is clearly below.

→ **Round 1 bracket: [4.5, 7.5]**

**Round 2 (Narrowing):** Two queries targeting (4.5, 6.0) and (6.0, 8.0).  

- **"Rethinking Evaluation... Polysemous Words" (5.75, Accept Poster):** Proposes a new SAE evaluation metric focused on polysemous words. Received criticism for conceptual assumptions (SAE features should map to word meanings) and narrow scope. Our paper is broader (5 model sizes, 7 metrics, toy models) and its central claim is better supported. Our paper is stronger → above 5.75.  
- **"Everything, Everywhere" (7.0, Accept Poster):** A negative-result paper about non-identifiability in mechanistic interpretability, with a novel taxonomy. The reviews acknowledged its importance but noted the toy-model scope limits generality. Our paper is similarly a negative-result empirical study but tests on real transformers rather than toy models. Comparable quality, slightly less theoretical novelty. → comparable to slightly below 7.0.  
- **"Towards Principled Evaluations" (7.0, Accept Poster):** Proposes a framework for SAE evaluation using supervised dictionaries. Gets accepted but with criticism about single-task focus and presentation. Our paper has broader experiments but no methodological framework. → slightly below 7.0.  
- **"Measuring Information in Text Explanations" (6.5, Reject with split 5,5,8,8):** Information theory for text explanations. Split reviews reflect methodological concerns. Our paper is more coherent and its claims are better supported. → above 6.5.

**Final position:** The paper sits above the 5.75 anchor (Rethinking Evaluation) and below the 7.0 anchors (Towards Principled Evaluations, Everything Everywhere). The most comparable anchor is "Everything, Everywhere" — both are negative-result empirical studies with clear experimental design and appropriate caveats. Our paper is slightly weaker in novelty (no taxonomy contribution) but applies to real transformers rather than toy models.  

**Final score: 6.5** — A solid paper with clear contributions and addressable limitations.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>