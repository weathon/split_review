Now I have verified the paper content against the reviewer claims. Let me synthesize the final consolidated review.

## Summary

This paper presents a systematic empirical study investigating whether diffusion-based video generation models can discover classical physical laws purely from visual data. Using a controlled 2D simulation testbed (Box2D) and scaling experiments across model sizes (22M–456M parameters) and dataset sizes (30K–6M videos), the authors evaluate three types of generalization: in-distribution (ID), out-of-distribution (OOD), and combinatorial. The core findings are that (1) scaling yields near-perfect ID and measurable combinatorial generalization improvements, but OOD generalization does not improve with scaling; (2) models rely on case-based retrieval rather than rule abstraction; and (3) a prioritization hierarchy (color > size > velocity > shape) governs how models match test inputs to training examples.

---

## Strengths

- **Controlled deterministic testbed enables quantitative physics evaluation.** The paper develops a 2D simulation (Box2D) where videos are deterministically governed by classical mechanics, alongside a parsing tool to extract object states from generated pixels. This allows continuous velocity error metrics (Section 3) and systematic manipulation of latent variables (velocity, size, color) across ID/OOD/combinatorial splits — a capability that prior world-model evaluations using real-world or non-deterministic videos cannot achieve.

- **Scaling is insufficient for OOD generalization but improves combinatorial generalization with coverage.** The paper provides direct quantitative evidence across three tasks (uniform motion, elastic collision, parabolic motion) that increasing model size (22M→310M) and data (30K→3M) does not reduce OOD velocity error, while ID error approaches the system noise floor (Fig. 3). Conversely, for combinatorial generalization (Table 1), scaling the number of templates from 6 to 60 reduces the human-judged abnormal rate from 67% to 10% (DiT-XL), revealing a clear dissociation between how scaling affects different generalization types.

- **Discovery of a case-based generalization mechanism and a concrete attribute prioritization hierarchy.** Controlled experiments (e.g., training on red balls + blue squares, testing on red squares, Section 5.3) show that the model shifts toward the matched training example by color rather than shape, with quantitative evidence ("no exceptions on 1,400 test cases"). The systematic pairwise comparisons yield the ranking color > size > velocity > shape, providing a testable, mechanistic insight into why video models struggle with object consistency.

- **Geometric characterization of OOD extrapolation via convex hull.** In the collision task (Fig. 7), the paper shows that OOD velocity points inside the convex hull of the training set produce low error comparable to ID, while points outside produce high error. This precisely distinguishes interpolation from true extrapolation and is a clean, actionable result.

- **Identification of attribute, spatial, and temporal combinatorial patterns (Section 5.4).** The paper shows that when training data contains separable physical events, the model can combine them across attributes, space, or time to generate physically coherent sequences, providing a positive counterpoint to the OOD failure and suggesting which forms of composition the model can handle.

---

## Weaknesses

### Fatal
None.

### Major
None. The paper's central claims are supported by the evidence, and no single issue invalidates the core results.

### Minor

- **The OOD velocity error metric may partially conflate model error with parsing error.** The paper reports a GT baseline (parsing error on ground-truth video) of 0.010 for ID conditions, and model ID error approaches this (0.012). However, the parsing error for OOD conditions is not reported. If parsing is less accurate for out-of-range velocities (e.g., fewer frames with the ball fully in view due to faster motion), some fraction of the 0.427 OOD error could be artefactual rather than model failure. The overall conclusion that scaling does not close the OOD gap is almost certainly robust (the gap is 40× the ID error, far larger than any plausible parsing increase), but the claim that scaling has "little or negative impact" should acknowledge this confound.

- **The memorization experiment (Section 5.2) lacks quantification.** The paper reports that the Set-2 model "occasionally produces" reverse-direction videos for low-speed balls and shows a single example. No quantitative measure is given: what fraction of low-speed test cases exhibit this behavior? How does it vary with model size or dataset composition? The paper's case-based generalization thesis rests on multiple pillars (interpolation/extrapolation in 5.1, attribute prioritization in 5.3), so this does not undermine the overall claim, but the direct memorization evidence is weaker than it should be.

- **Human evaluation for combinatorial generalization lacks methodological detail.** The abnormal ratio is the most direct measure of physics fidelity, but the paper does not report the number of videos evaluated, number of annotators, inter-annotator agreement, or the instructions given to human judges. For a binary "normal/abnormal" judgment on simple physical scenes this is unlikely to reverse the 67%→10% trend, but the reliability of the metric is not fully established.

- **The attribute prioritization hierarchy is slightly overclaimed.** The pairwise tests thoroughly establish color > shape, size > shape, velocity > shape, and color > velocity. However, the evidence for size > velocity is described as a "slight preference" (Section 5.3, line 348). The full chain color > size > velocity > shape is presented as settled (line 351, abstract, conclusion), but the weakest link (size > velocity) is supported by observational preference rather than a clean experimental outcome. The hierarchy is still informative, but the certainty is disproportionate to the evidence on this one pair.

- **Key scaling results are reported without variance or seed-dependence.** Figures 3 shows single error values per condition. Given the paper's own observation that OOD errors are "highly random" across data sizes (line 194), reporting variance across random seeds would strengthen confidence that the null OOD scaling result is not a fluke of a particular run.

- **The ambiguity analysis (Section 5.5) is illustrative but not quantified.** The paper shows examples where pixel-level ambiguity causes incorrect physics predictions but does not measure how frequently such ambiguity occurs or how much it affects overall results across the test sets.

### Trivial
- **OOD test composition in main text could be more specific.** The paper states "various types of OOD setting, e.g., velocity/radius-only or both OOD" and defers to the appendix (line 158). While the appendix presumably contains the details, the main text's figure legend simply says "OOD" without indicating whether the reported results aggregate over multiple OOD types or use a specific one.

---

## Nice-to-Haves

- **Compare to a simple non-diffusion baseline** (e.g., a neural network that directly predicts latent states from initial conditions, or even a linear regression for uniform motion). This would help disentangle whether the observed OOD limitations are specific to the video generation paradigm or are general properties of neural networks trained on the same data.

- **Ablate the OOD distance.** How far outside the training range must the test data be before the model fails? Is the failure gradual or abrupt? This would clarify whether the model exhibits any extrapolation ability at all over short distances.

- **Test the attribute prioritization hierarchy in the combinatorial (multi-object interaction) setting** to see whether the same ranking holds when the model must simultaneously handle interacting objects.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The paper should check whether position trajectories are physically consistent in other ways (e.g., conservation of momentum)."** — For the simple scenarios tested (uniform motion, elastic collision, parabolic motion), velocity error is the direct and appropriate metric for physics adherence. Post-collision velocities in elastic collisions are fully determined by conservation laws, so velocity error already tests those laws. This criticism misunderstands the metric.

2. **"OOD test set composition is underspecified in the main text."** — The main text (lines 157–158) clearly states that OOD videos use radius and velocity values outside the training range and lists examples of OOD types (velocity-only, radius-only, or both), with details deferred to the appendix. This is standard practice.

3. **"The paper does not use methods the reviewer prefers."** — The demand for non-diffusion baselines and additional physics-specific metrics are scope-creep suggestions that would make this a different paper. Moved to Nice-to-Haves.

---

## Novel Insights

Beyond the paper's own contributions, the reviews surface one noteworthy synthesis: the paper reveals a sharp *disconnect* between the types of generalization that benefit from scaling. Scaling works for ID and combinatorial generalization but fails entirely for OOD — and the failure is not merely flat but "highly random." This randomness itself is an under-analyzed finding: unlike supervised learning where scaling typically produces monotonic improvements or plateaus, OOD error here fluctuates non-monotonically with data size (e.g., DiT-B on uniform motion: 0.433, 0.328, 0.358). This non-monotonicity suggests that larger datasets may introduce more "deceptive" nearest neighbors that the model can latch onto, which is consistent with the case-based retrieval hypothesis but deserves deeper investigation as a phenomenon in its own right.

---

## Suggestions

1. **Report the parsing error (GT baseline) for OOD conditions** to fully validate the velocity error metric, or use a complementary metric less dependent on parsing.
2. **Quantify the memorization experiment** (Section 5.2): report the fraction of low-speed test samples showing direction reversal, and compare to a baseline model trained on the full velocity range.
3. **Add variance information** to the scaling results (Fig. 3) — even 2-3 seeds per condition would substantially increase confidence in the null OOD scaling result.
4. **Report human evaluation details** (number of annotators, inter-rater agreement, number of videos judged) for the abnormal ratio.
5. **Qualify the attribute hierarchy** to acknowledge that the size > velocity link is the weakest and based on "slight preference" rather than a decisive experimental outcome.

---

## Score and Decision

**Originality:** 7/10 — The three-way generalization framework (ID/OOD/combinatorial) applied to video generation physics learning is novel, as is the attribute prioritization hierarchy.

**Importance of research question:** 9/10 — Whether scaling video generation yields world models that understand physics is a timely and high-impact question.

**Claims supported by evidence:** 7/10 — Core claims are well-supported. Minor overclaim on the attribute hierarchy and the memorization mechanism weakens precision but not validity.

**Soundness of experiments:** 7/10 — Experimental design is thoughtful and thorough. Minor weaknesses around parsing confound, missing variance, and human evaluation details reduce the score slightly.

**Clarity of writing:** 8/10 — Well-structured and clear. The categorization of generalization types is explained well.

**Value to the community:** 8/10 — The findings challenge optimistic narratives about video generation as world simulation and provide concrete directions for improvement.

**Overall assessment:** This is a solid empirical study that addresses an important question with well-designed experiments. The core findings — that scaling alone does not yield OOD generalization and that models rely on case-based retrieval — are compelling and appropriately caveated. The weaknesses (parsing confound, missing quantification in one experiment, incomplete human eval details) are bounded and do not undermine the main claims. With the suggested revisions, the paper would be notably stronger.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>