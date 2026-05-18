Now I have thoroughly read and cross-referenced the paper against all reviewer claims. Let me compose the final consolidated review.

---

## Summary

This paper introduces CoLa-DCE, a method that extends diffusion-based counterfactual explanation (built on LDCE, Farid et al. 2023) by constraining the counterfactual generation to a user-selected set of semantic concepts. Gradients are masked at an intermediate classifier layer so that only the top-\(k\) concept channels guide the diffusion process, optionally with spatial thresholding for further localization. The paper also proposes a classifier-internal near-miss target selection (using activations or LRP attributions) that improves flip ratios over WordNet-based label selection. Experiments on ImageNet with VGG16, ResNet18, and ViT classifiers evaluate minimality (FID, L1) and accuracy (flip ratio, confidence), with a validity test confirming that selected concepts align with actual attribution shifts.

## Strengths

- **Novel concept-guided counterfactual generation.** The idea of masking the external classifier's gradient at a chosen intermediate layer to restrict changes to specific concept channels is a genuine extension of LDCE that adds a degree of semantic control absent in prior diffusion-based counterfactual methods (DiME, ACE, DVCE, LDCE). Equation 4 provides a clean mathematical description of the gradient masking, and Algorithm 1 gives an end-to-end pseudocode specification.

- **Improved target selection via classifier-internal near-miss.** Replacing LDCE's WordNet-based label target with a near-miss selected from the classifier's own feature space (activations or LRP attributions) yields substantially improved flip ratios and confidence across all three architectures (e.g., VGG16bn flip ratio from 0.851 → 0.956 with LRP-based target). This is a clean, practical contribution that is well-tested in Table 1.

- **Validity test confirms concept–change alignment.** Figure 7 provides quantitative evidence that the attribution difference between original and counterfactual images concentrates on the selected concepts, with the selected-concept ratio consistently exceeding random-concept baselines. This supports the claim that the concept guidance is causally meaningful rather than arbitrary.

- **Systematic analysis of the number of concepts.** Figure 3 shows the tradeoff between minimality (FID) and accuracy (flip ratio) as \(k\) varies, demonstrating that even 10 concepts can achieve >75% flip ratio while improving FID over the LDCE baseline. The spatial conditioning analysis adds further evidence of localized control.

- **Model debugging demonstration.** The case study in Figure 8 shows how CoLa-DCE explanations can identify missing or misinterpreted concepts in a misclassification (Junco vs. Brambling), illustrating a practical application beyond standard counterfactual evaluation.

## Weaknesses

### Fatal
None.

### Major

- **Comprehensibility is claimed as a demonstrated benefit but is never directly evaluated.** The abstract states: "We demonstrate the advantages of our approach in minimality and **comprehensibility** across multiple image classification models and datasets." The introduction and conclusion reinforce that improved transparency and comprehensibility are primary contributions. However, the quantitative evaluation (Table 1, Figure 3) measures only FID, L1, flip ratio, and confidence — none of which quantify comprehensibility or human understanding. The validity test (Figure 7) shows concept-alignment fidelity, which is a prerequisite for comprehensibility but not evidence that a human finds the explanation more understandable. The qualitative examples (Figures 5, 6, 8) are suggestive but do not substitute for an objective assessment. Given that the paper's central motivation is that current counterfactuals "lack transparency" and that CoLa-DCE improves "comprehensibility," this evaluation gap is significant. A small-scale human judgment task (e.g., 3–5 raters judging whether concept visualizations match perceived changes in 20–30 samples) or a well-motivated automatic proxy would substantially strengthen the paper. As it stands, comprehensibility is asserted rather than demonstrated.

- **The target-selection experiment uses the LDCE baseline without concept-guidance, while CoLa-DCE rows in Table 1 show degraded flip ratios compared to LDCE+Act/Attr.** For VGG16bn, LDCE+Attr achieves a flip ratio of 0.956 while CoLa-DCE+Attr drops to 0.821; for ResNet18, LDCE+Act achieves 0.960 while CoLa-DCE drops to 0.846. The paper notes that concept-guidance is "competitive to the baseline" (line 254), but the flip ratio drops of 13–14 points are material. While this is understandable (the gradient signal is attenuated by masking), the paper should more explicitly characterize the accuracy–transparency tradeoff that users face, beyond the conceptual ablation in Figure 3. The qualitative claim that CoLa-DCE yields "much more transparent counterfactuals while still being competitive" (line 254) understates the empirical cost on the primary classification accuracy metric.

### Minor

- **Interaction between concept masking and LDCE's consensus alignment is not discussed.** The paper's Algorithm 1 passes the constrained classifier score to `ApplyLDCE()`, and Eq. 4 specifies the gradient masking. However, the paper does not discuss whether LDCE's implicit-classifier consensus mechanism (which aligns the external classifier gradient with the diffusion model's implicit gradient) needs any modification to operate correctly on a masked gradient. In practice, the masking can be applied first and then LDCE's consensus operates naturally on the resulting gradient, but stating this explicitly would resolve ambiguity. Since the method is reproducible from the described equations, this is a clarity issue, not a fatal gap.

- **Spatial conditioning threshold \(\eta\) is mentioned but not specified.** Line 194 states that gradients below threshold \(\eta\) are zeroed out, but the value of \(\eta\) and whether it is a fixed global threshold or adaptive per concept are not reported. This affects reproducibility of the spatial conditioning results.

- **Concept selection is fixed based on the original image's gradient, but the importance of concepts may shift during the diffusion process.** The paper acknowledges this (line 173: "conditions require precomputation and remain fixed"), but does not analyze how much this harms performance. A sensitivity analysis comparing fixed vs. dynamically re-selected concepts at intermediate steps would clarify the practical severity of this limitation.

- **Distribution of near-miss distances is not reported.** The paper uses 90% of ImageNet validation as a reference set and reports high flip ratios (0.80–0.96), but does not report the distribution of distances between the original sample and its selected near-miss target. This would help interpret whether the near-miss typically selects a target that is semantically very close or occasionally selects a distant one.

### Trivial
None.

## Nice-to-Haves

- **Comparison against ACE and DVCE baselines.** While comparing against the most directly related method (LDCE) is defensible, adding ACE or DVCE comparisons would contextualize the tradeoffs (e.g., does concept masking hurt flip ratio relative to non-concept SOTA diffusion counterfactuals?).

- **Direct comprehensibility proxy.** As noted under Major weaknesses, even a small-scale human judgment task (e.g., 3 raters, 20 samples) verifying that annotated concept changes match perceived visual differences would substantiate the core claim.

- **The choice of concept layer.** An ablation across different intermediate layers (rather than just one per model architecture) would help understand how the choice of concept layer affects the quality of guidance.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The paper provides no description of [how concept masking integrates with LDCE]"** — Removed as factually incorrect. Equation 4 (lines 176–187) precisely describes the gradient masking: \(\nabla_x p(x|y,\theta_1...\theta_k) = \delta(\nabla_{g(x)} h, \theta_1...\theta_k) \cdot \nabla_x g\) where \(\delta\) zeros out non-selected channels. The algorithmic loop in Algorithm 1 then feeds this constrained gradient into the LDCE framework. The description, while not exhaustive about LDCE's internal consensus, is sufficient for the method to be understood.

- **"Missing related work on concept-based counterfactuals from tabular/text domains"** — Removed per constraint on missing related works.

- **"Inherited parameters from LDCE not listed"** — Removed per constraint on reproducibility nitpicks. It is standard practice to reference hyperparameters from the method one builds upon. The paper acknowledges this limitation (lines 355–356: "multiple parameters...require fine-tuning").

- **"The validity test does not prove confinement to selected concepts"** — Weakened from the harsh critic's framing. The test in Figure 7 shows that selected concepts account for a disproportionate share of attribution differences, which is meaningful positive evidence. The test does not claim perfect confinement; the paper itself notes (line 329) that "redundancy of similar feature encodings...it is reasonable that the selected features do not perfectly align." What remains is a minor limitation about the strength of the claim.

## Novel Insights

Beyond the paper's own contributions, the key insight from triangulating the reviews is that **concept-guided gradient masking introduces a transparency-vs-accuracy tradeoff that the paper does not fully characterize**. The flip ratio drops of 13–14 points (Table 1) between LDCE+Attr (0.956) and CoLa-DCE (0.821) on VGG16bn are not incidental — they represent the cost of constraining the gradient to a sparse set of channels. The paper's Figure 3 shows this tradeoff as a function of \(k\), but the absolute costs at typical \(k\) values (e.g., \(k=20\)) are higher than the narrative suggests. A paper that more explicitly frames this as a tunable precision–recall tradeoff (rather than presenting it as a pure improvement) would better serve practitioners deciding whether to adopt concept guidance.

## Suggestions

1. **Add a direct comprehensibility evaluation.** Even a small-scale human judgment task (3 raters, ~20 samples) matching concept visualizations to perceived image changes would transform the paper's support for its primary claim. If a user study is impractical, a structured annotation proxy (e.g., do the concept visualizations align with concept localization maps?) would help.

2. **Discuss the interaction between gradient masking and LDCE's consensus mechanism explicitly.** A one-paragraph clarification stating that the masked external gradient is treated as the "external classifier gradient" within LDCE's existing consensus alignment, with no modification needed, would resolve the harsh critic's primary concern.

3. **Report the spatial conditioning threshold \(\eta\)** and state whether it is a global constant or per-concept adaptive value.

4. **Add a sensitivity analysis on fixed vs. dynamically re-selected concepts** at intermediate diffusion steps to quantify the practical impact of concept shifts during generation.

5. **Explicitly characterize the accuracy–transparency tradeoff** with a clear statement of flip ratio costs at different concept budgets, rather than describing the method as "competitive to the baseline" (which understates a 13–14 point drop).

## Score and Decision

This paper proposes a sensible, well-motivated extension to diffusion-based counterfactuals. The core methodological ideas (concept-guided gradient masking, near-miss target selection) are novel and supported by adequate quantitative evidence on standard metrics. The validity test in Figure 7 is the strongest evidence that the concept guidance works as intended.

However, the paper's primary stated contribution — improved comprehensibility — is not empirically validated by any metric or human study. This gap between claimed contribution and evaluated evidence is significant. Additionally, the flip ratio costs at the default concept budget are materially higher than the paper's framing suggests. These weaknesses are addressable but are not resolved in the current manuscript.

On balance: the methodological contributions are real, the experiments are competent on their own terms, and the approach is clearly a useful step forward. But the evaluation does not fully match the paper's own scope of claimed benefits.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>