Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper presents a three-stage paradigm — generate, predict, manipulate — for studying human perceptual variability using images sampled from ANN decision boundaries. The authors (1) generate ambiguous handwritten digits via diffusion models with uncertainty/controversial guidance, (2) collect human judgments from 246+ participants to build the varMNIST dataset, (3) fine-tune models to predict individual responses (showing Spearman correlation with human entropy rising from ρ=0.08 to ρ=0.74 after group-level fine-tuning), and (4) generate personalized controversial stimuli that steer different participants toward opposite percepts. The core contributions are a novel generative method for producing naturalistic boundary images, a large publicly-released behavioral dataset, and a demonstration that subject-specific fine-tuning aligns ANN perceptual variability with human perceptual variability.

## Strengths

- **Novel generative method that successfully evokes human perceptual variability from ANN decision boundaries**: The varMNIST dataset shows that over half of generated images have entropy significantly greater than zero (Figure A.10), and the average sum of success+bias rates across all guidance conditions approaches 80% (Figure 3b). This directly supports the central hypothesis that images at ANN perceptual boundaries produce diverse human percepts, and the use of diffusion priors + a human digit-judgment surrogate addresses the known problem of generated images being unrecognizable (cf. Feather et al. metamers).

- **Subject-specific fine-tuning substantially aligns model and human perceptual variability**: For VGG, group fine-tuning increases the Spearman rank correlation between model and human entropy from ρ=0.08 to ρ=0.74 (Figure 4c). GroupNet and IndivNet outperform BaseNet by ~20% on varMNIST (Figure 4a), and IndivNet achieves an additional ~5% improvement on individual-specific subsets. Accuracy improved for 241 of 246 participants after individual fine-tuning. These results demonstrate a meaningful and measurable alignment between ANN and human perceptual variability.

- **Large-scale, well-validated behavioral dataset**: The paper collects data from 246 participants across 116,715 trials for varMNIST, plus 276 participants for the digit-judgment task and 18 participants in an in-lab manipulation experiment. This provides substantial statistical power for the reported analyses and represents a valuable resource for the community studying human perceptual variability.

- **Methodological innovation combining diffusion priors, counterfactual guidance, and human surrogate models**: By training a digit-judgment surrogate on human responses and incorporating it into the generation loss, the method ensures generated images remain recognizable as digits. This addresses a known limitation of prior work where boundary images were often unrecognizable to humans.

## Weaknesses

### Fatal
None.

### Major

- **The manipulation experiment has a confound that weakens the central claim of "selectively manipulating individual behaviors."** The comparison in Figure 5b/c contrasts Round 1 stimuli (varMNIST images generated using group-level classifiers) with Round 2 stimuli (generated using individually fine-tuned models). These two conditions differ not only in the individualization of the models but also in the specific images shown, the number of trials (500 vs. ~360 per participant), and the effects of task familiarity/practice from Round 1 to Round 2. The observed improvements — +3% success rate (p<0.001) and +12% targeted ratio (p<0.001) — cannot be cleanly attributed to individual fine-tuning alone. This does not invalidate the paper, but the manipulation claim needs to be tempered: the results are preliminary evidence, not a controlled demonstration. A proper control would present group-model-generated images alongside individually-generated images in Round 2, using the same participants and trial structure. The claim as currently stated ("selectively manipulate individual behaviors," "amplify perceptual differences") overstates what the evidence supports.

### Minor

- **The thresholds defining guidance outcomes (success/bias/failure) are not justified or tested for robustness.** The 80% sum threshold and 10% min threshold in Section 3.3.2 are used throughout all quantitative comparisons (Figure 3b, Figure A.12) to rank guidance strategies, classifiers, and digit pairs, yet no sensitivity analysis is provided. The paper would be strengthened by showing that the main conclusions (e.g., controversial > uncertainty, CORNet > LRM) hold under reasonable threshold variations, or by supplementing with a continuous metric (e.g., response entropy).

- **The details of the "balanced" sample selection for the manipulation experiment (Section 5.1) are underspecified.** The paper states that "around 500 balanced samples" were selected from varMNIST for Round 1, but does not explain what "balanced" means (balanced across digit pairs? across participants? across entropy levels?). This omission matters because any selection bias in Round 1 sampling could affect the Round 1 vs. Round 2 comparison.

- **Sentinel trial exclusion rates are high (38.5% for the recognition experiment) and the sentinel procedure is not described in the main text.** The paper states that participants were excluded based on "Sentinel trials" but never explains what these are. Given that 154 out of 400 participants were removed, a brief description of the criterion in the main text is warranted.

- **Data-mixing ratios for individual fine-tuning (2:1:1 for varMNIST-i:varMNIST:MNIST) appear arbitrary and are not ablated.** No justification or sensitivity analysis is provided for these ratios, which could affect the accuracy and alignment results in Figure 4.

- **Baseline success/failure rates for the varMNIST condition in the manipulation experiment are not explicitly stated in the text.** The paper reports percentage changes (+3% success, +1% bias, −4% failure) but does not state the absolute baseline rates, making it difficult for the reader to assess effect sizes without carefully reading Figure 5b.

### Trivial

- The entropy correlation after fine-tuning is illustrated with VGG (ρ=0.08→0.74) in the main text, while results for other classifiers are deferred to Figure A.14. The main text should include at least a brief summary of whether the improvement is consistent across architectures. (The paper explicitly references the appendix figure, so this is a presentation choice, not an omission.)

- Some comparisons lack error bars or confidence intervals (e.g., Figures 3b, 4b, 4d), relying on qualitative description rather than quantified uncertainty.

## Nice-to-Haves

- Add a controlled condition in the manipulation experiment where group-model-generated images are also presented in Round 2 alongside individually-generated images, to isolate the effect of individualization.
- Validate the 80%/10% threshold definitions with a sensitivity analysis or switch to a continuous metric (e.g., response entropy of the two target classes).
- Ablate the 2:1:1 and 1:1 mixing ratios and report whether the results in Figure 4 are robust to different ratios.

## Removed Points

These points are flagged to be removed — treat them with caution:

- The harsh critic's concern about "circular reinforcement" in the digit judgment surrogate (Section 3.2). The reviewer acknowledges this "is not a flaw," and it is a standard design choice — the surrogate ensures images look like digits to humans, which is the intended function. This does not constitute a weakness.
- The harsh critic's characterization of the manipulation confound as "structural" and as invalidating the claim entirely. The within-subject design (same participants in both rounds) provides partial control, and the 12% improvement in targeted ratio is not easily explained by practice effects alone. The weakness is real but not fatal; it has been downgraded to Major above.
- The harsh critic's criticism about the abstract overclaiming ("paves the way for AI models with personalized perceptual capabilities"). This is standard rhetorical framing in introductions and does not affect the technical contribution.
- The harsh critic's suggestion that the paper should compare against a "purely model-based naturalness criterion." This is a wishlist item that would broaden the paper's scope rather than strengthen its core claims.

## Novel Insights

The harsh critic's identification of the manipulation confound highlights a genuine limitation that the paper's own framing does not adequately acknowledge: the within-subject Round 1 vs. Round 2 comparison conflates individualization of the generative model with a host of other procedural differences. However, the strength finder correctly identifies that the +12% improvement in targeted ratio is harder to dismiss as a pure confound than the +3% success-rate improvement — directional guidance (getting participant A to see "3" and participant B to see "5" specifically, rather than just different digits) is a more precise behavioral signature that practice effects alone would not produce. Bringing these two observations together: the manipulation result is suggestive and worth reporting, but it requires a controlled replication before the authors can claim "selective manipulation."

## Suggestions

1. **Temper the manipulation claims** — reframe the manipulation section as a preliminary proof-of-concept that individually fine-tuned models can predict which images will be controversial for specific participant pairs, rather than claiming controlled "selective manipulation." Explicitly acknowledge the confound between individualization and other procedural differences.
2. **Add a sensitivity analysis for the 80%/10% guidance thresholds** — show that the ranking of classifiers and strategies in Figure 3b is stable under threshold variation (e.g., 70%/5% and 90%/15%), or adopt a continuous metric.
3. **Define "balanced" sampling** in Section 5.1 and describe the sentinel trial procedure briefly in the main text.
4. **Report absolute baseline values** in the manipulation results text, not just in the figures.
5. **Add either error bars or bootstrapped confidence intervals** to the key comparison figures (3b, 4b, 4d) to support the qualitative claims.

## Score and Decision

This paper presents a novel and well-executed paradigm for studying human perceptual variability. The generative method is an advance over prior work (it produces naturalistic boundary images that humans recognize), the varMNIST dataset is a large-scale resource, and the alignment results (ρ=0.08→0.74) are impressive. The manipulation experiment is the weakest link — it supports the paper's thesis directionally but suffers from a confound between individualization and procedural differences. The paper's first two contributions are strong enough to carry it, provided the manipulation claims are appropriately tempered and the methodological gaps (threshold justification, underspecified sampling, sentinel criteria) are addressed. I recommend acceptance with major revisions focused on the manipulation section.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>