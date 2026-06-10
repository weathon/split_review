Here is my final consolidated review.

---

## Summary

This paper trains Sparse Autoencoders (SAEs) on the residual streams of Maia-2, a human-like chess model that adapts its play to different skill levels. The authors identify SAE features correlating with a "square no longer attacked" concept (whether a threatened square is secured by the model's predicted move), then show that boosting these features via mediated intervention improves Maia-2's move quality on a curated set of 4,750 positions where the model previously made threat-related mistakes. The paper claims this demonstrates SAEs' utility for understanding and manipulating skill adaptation in transformer models.

## Strengths

- **CC-AUC as an active training criterion, not just post-hoc evaluation**: Karvonen et al. (2024) used chess-concept AUC only to evaluate SAE quality; this paper goes further by incorporating CC-AUC into hyperparameter selection (combined with normalized -L) and as an early-stopping criterion (Section 4.3, patience of 10 tracked every 500 iterations). This is a genuine methodological addition over prior work.

- **Mediated intervention with a random-feature control**: The intervention framework (Section 5.2.2) compares the effect of boosting the best-correlated SAE feature against a random-feature perturbation of the same magnitude (Figure 4). This distinguishes specific causal effects from general activation noise, which is a proper experimental design choice.

- **Reconstruction fidelity evaluated across skill levels**: The paper measures move-prediction agreement between original and SAE-reconstructed Maia-2 across multiple skill levels (Figure 2, right panel), not just a single forward pass. This is directly relevant to the claim that the SAEs preserve skill-sensitive information.

- **Curated transitional-position dataset**: The refinement of Tang et al.'s (2024) transitional positions with two filtering criteria (centipawn loss >30 at lower Elo, and failure to address a specific threatened square) yields a clean testbed for isolating threat-response failure modes (Section 5.2.1).

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative results reported in the text — the paper relies entirely on figures.** The entire Results section (Section 5) describes figures without reporting any numerical values for the central intervention experiment. There are no tables or text-reported numbers for: best-move prediction rates at each skill level after intervention, the magnitude of transition point shifts, the CC-AUC scores for the 64 selected features (only two example squares are given: e3 at 0.88 and 0.90), the separation between targeted and random intervention at specific strengths, or any confidence intervals or variability measures. A reader cannot assess effect sizes, reliability, or practical significance from figures alone. At ICLR standards, this is a significant evidential gap.

2. **Narrow scope relative to the "skill adaptation" framing.** The paper studies one chess concept — "square no longer attacked" (defensive threat response) — on one layer (last layer), using one filtered dataset. Yet the title, abstract, and conclusion make broad claims about "understanding skill adaptation in transformers" and "how skill-specific information is encoded within the model." Threat response is one tactical sub-skill; the paper provides no evidence that the identified features encode *skill level* (e.g., by showing the feature activates differentially across skill inputs on the same positions, or that intervening shifts behavior along a broader skill continuum beyond the narrow filtered dataset). The limitations section (6.1) acknowledges this partially, but the framing throughout the paper is disproportionately broad relative to the evidence presented.

3. **Claim of "eliciting both higher skill and lower skill play" is not supported.** The abstract claims the intervention elicits "both higher skill and lower skill play" and the conclusion mentions "adding and subtracting feature vectors." However, the intervention defined in Section 5.2.2 only adds a positive boost (s ∈ [0.1, 10]) to the SAE feature activation. No experiment demonstrates that subtracting/suppressing a feature elicits lower-skill play. This claim in the abstract and conclusion is unsupported.

4. **No comparison to direct skill-level manipulation.** The most natural baseline — simply running Maia-2 at a higher skill level and measuring the improvement — is absent. Without this comparison, it is unclear whether the SAE intervention is manipulating skill-relevant internal representations or simply patching in a tactical correction that the model already knows at higher skill levels. Comparing the SAE intervention's effect to the effect of raising the model's skill input would directly test whether the features mediate the model's skill modulation mechanism.

### Minor

5. **CC-AUC metric selection inflates apparent concept mastery.** The CC-AUC takes, for each concept, the *maximum* AUC across all 2,048 SAE features, then averages across concepts. With 2,048 features, some spuriously high AUC values are expected. Additionally, the concept set includes 32 "presences of pieces at the initial position" and 32 "presences of arbitrary pieces at random squares" — trivial concepts that inflate the overall CC-AUC. Since CC-AUC is used for hyperparameter selection and early stopping rather than the main result, this is a methodological concern rather than a fatal one.

6. **Feature monosemanticity is not analyzed.** For the 64 selected features (one per square), the paper does not examine whether these features also correlate with unrelated concepts. An interpretability paper that claims features encode "threat response" should verify that the selected features are not simultaneously encoding other board-state properties.

7. **Only one SAE configuration evaluated in the intervention.** Despite performing a grid search, only the 2048-dim, α=1e-5 SAE is used for the intervention experiments. Testing whether worse-performing SAEs (by CC-AUC) yield weaker intervention effects would strengthen the causal claim.

### Trivial
None.

## Nice-to-Haves
- Testing whether the identified features activate differentially across skill inputs on a fixed set of positions would directly test the skill-level encoding hypothesis.
- Evaluating the intervention on the full (unfiltered) transitional dataset would demonstrate generalization beyond the narrowly curated 4,750 positions.
- Testing additional skill-relevant chess concepts (e.g., king safety, pawn structure, piece activity) would broaden the paper from a single-case demonstration to a more systematic study.

## Removed Points
Weaknesses flagged by reviewers but removed after verification against the paper:

- **"The core intervention experiment is nearly tautological due to dataset construction"** — Removed. The experiment tests whether boosting a selected feature causes a change in model behavior in the predicted direction. This is a non-trivial hypothesis; the intervention could have failed. The dataset filtering is an intentional design choice to isolate the phenomenon, not a logical circularity. The random-feature control further validates specificity of the effect.

- **"Random-feature baseline is a straw-man comparison"** — Removed. A random-feature control is a standard minimal sanity check in causal intervention studies. It tests whether any arbitrary feature perturbation produces the same effect, which is the correct null hypothesis.

- **Claims about missing implementation details or formatting artifacts** — Removed per meta-reviewer instructions. These are either parser artifacts or standard expectations that are not valid criticisms of the submission.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a table reporting numerical results: best-move prediction rates at each skill level for original, intervened, and random-feature control with standard errors or confidence intervals.
2. Add an experiment with feature suppression (subtraction) to substantiate the "lower skill play" claim, or remove the claim from the abstract and conclusion.
3. Add a comparison to the baseline of directly increasing Maia-2's skill level to disentangle skill-level encoding from tactical correction.
4. Report CC-AUC scores for all 64 selected features, not just two examples.
5. Temper the broad claim that the paper explains "how skill-specific information is encoded" — the paper demonstrates that SAE features can manipulate threat-response behavior in a specific tactical context, which is an interesting but narrower contribution.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>