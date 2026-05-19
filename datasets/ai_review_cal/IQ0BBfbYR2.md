- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3
I now have all the information needed to compile the final consolidated review. Let me organize my findings.

## Final Consolidated Review

---

## Summary

This paper proposes CoLa-DCE, which extends Latent Diffusion Counterfactual Explanations (LDCE) by constraining the classifier gradient to a small set of semantically interpretable concept channels and adding spatial localization. The method has three components: (1) local near-miss target selection based on the classifier's internal representation, (2) concept selection and conditioning that masks the gradient to only the top-k concept channels, and (3) spatial conditioning that further restricts changes to localized regions. The paper evaluates on ImageNet across multiple architectures (VGG16, ResNet18, ViT).

## Strengths

- **Concept conditioning with spatial constraints is a well-motivated and novel extension of diffusion-based counterfactuals.** The idea of replacing pixel-level minimality with concept-level minimality is clearly argued (Sec 4.3–4.4). Qualitative examples (Figures 4, 11) show that CoLa-DCE produces qualitatively sparser explanations than LDCE, and Table 1 shows FID improvements (e.g., VGG16bn: 44.43 vs LDCE Base 55.46), demonstrating that concept guidance can improve distributional realism.

- **The validity test quantitatively confirms that selected concepts drive the counterfactual change.** Section 5.5 (Figure 13) computes the ratio of attribution difference for selected vs. random concepts. The clear separation between the two conditions provides evidence that the concept selection mechanism captures channels that genuinely change, and is not a spurious artifact of gradient magnitude.

- **The local near-miss target selection (Sec 4.1) is a sensible improvement over the WordNet-based targets used in the original LDCE.** Table 1 shows that switching from the LDCE Base target to the attribution-based near-miss target (LDCE+Attr) consistently improves flip ratio (e.g., VGG16bn: 0.851→0.956) and confidence while reducing L1. Although this component is not unique to CoLa-DCE, it is a well-justified contribution that improves counterfactual quality across the board.

- **The trade-off analysis between number of concepts and accuracy (Figure 12/Fig. 2) provides useful practical guidance.** The paper honestly shows that reducing concepts to as few as 10 yields flip ratios above 75% while improving FID over the LDCE baseline, giving users a concrete knob to balance minimality and validity.

## Weaknesses

### Major

- **The paper's central claim — improved *transparency* and *comprehensibility* — is not directly evaluated.** The abstract, contributions list, and conclusion frame CoLa-DCE's main advantage as making counterfactuals "more transparent and more comprehensible" by revealing "where changed what" (lines 10–11, 47–48, 364–365). However, all reported metrics (FID, L1/L2, flip ratio, confidence) measure counterfactual quality (realism, minimality, accuracy), not transparency or comprehensibility. The validity test (Sec 5.5) is a useful sanity check that selected concepts correlate with attribution changes, but it does not measure whether a human user better understands the counterfactual. No user study, no proxy task (e.g., concept recall), and no human-grounded experiment is conducted. Given that the paper's own framing centers on improving transparency, this is the most significant evidential gap.

- **The minimality evidence is contradictory and the framing is inconsistent.** CoLa-DCE consistently has *higher* L1 norms than LDCE+Attr across all models (e.g., VGG16bn: LDCE Attr L1=12443 vs CoLa-DCE L1=13915; ResNet18: 12465 vs 13933 — Table 1). Yet the abstract claims "increased granularity through minimal feature changes" (line 10). The paper acknowledges the trade-off in passing (line 254: "damping the gradient signal") but continues to frame CoLa-DCE as improving minimality. If "minimal feature changes" refers to *semantic* minimality (fewer concepts changed), this is a reasonable redefinition — but the paper never clearly distinguishes semantic minimality from pixel-level minimality, and the only pixel-level metric (L1) contradicts the claim.

- **The Limitations section (Sec 6) omits key shortcomings.** It only mentions reliance on diffusion model quality and parameter tuning. It does not acknowledge: (a) the missing direct evaluation of transparency/comprehensibility, (b) the L1 trade-off, or (c) the absence of comparisons to methods beyond LDCE. A limitations section that omits these items gives an incomplete picture of the work's boundaries.

### Minor

- **Comparisons to other counterfactual generation methods (DiME, ACE, DVCE, SVCE) are absent.** The paper discusses these methods in Related Work (Sec 3.1) and notes their differing constraints (e.g., DiME requires robust classifiers, ACE is a two-step process). However, no explicit justification is given for their exclusion from experiments, and no attempt is made to compare on overlapping metrics (e.g., FID, flip ratio) where conditions permit. While the LDCE baseline comparisons are appropriate for showing the additive contribution, readers cannot assess how CoLa-DCE compares to the broader landscape.

- **The single debugging example (Figure 14/Fig. 5) is anecdotal.** Section 5.4 presents one misclassification case (brambling misclassified as junco) as evidence that CoLa-DCE "helps in model debugging." A systematic evaluation — e.g., counting how often concept visualizations match actual model failure modes across multiple cases — would be needed to support this claim.

- **The spatial threshold η is not specified, and no sensitivity analysis is provided.** Section 4.4 introduces a threshold η for binary spatial masking (line 194) but never reports its value or tests sensitivity to it. This affects reproducibility.

- **The effect of layer choice for concept extraction is not ablated.** Only one layer per model is tested (feat.37/feat.40 for VGG16, 4.1.c1 for ResNet18, encoder for ViT). The paper does not discuss how the choice of layer affects concept selection or counterfactual quality.

- **The exact value of k (number of concepts) is stated only in the Table 1 caption (k=20), not in the method section.** The paper mentions k ∈ [10, 140] in the trade-off study (Fig. 12) but should state the default value used for main results in the method section.

### Trivial

- What k=0 means in Figure 12 (concept trade-off) is not defined. It presumably corresponds to the LDCE baseline but should be labeled clearly.
- The notation in Eq. (4) uses θ₁...θₖ as index sets but introduces them as "binary constraints," which is a minor inconsistency.

## Nice-to-Haves

- Reporting standard deviations or confidence intervals (e.g., across multiple seeds) would strengthen all quantitative claims in Table 1 and Figures 12–13.
- An ablation of the "suspend conditioning for last 50 steps" design choice (Sec 5, line 211) would be informative.
- Testing on datasets beyond ImageNet (where the method's reliance on a large reference dataset may be less practical) would improve generalizability claims.

## Removed Points

*These points were flagged in the inputs but are removed with justification:*

- **"LRP aggregation not specified"** (Harsh Critic): The paper states that model perception can be derived via activation or LRP (line 140). The aggregation mechanism (summing over spatial dimensions) is the same as for gradients — this is reasonably inferable from context. Removed as overly granular.

- **"Strength: Validity test shows ratio near 1.0"** (Strength Finder): The paper's own text (line 329–330) discusses imperfect alignment due to feature redundancy, stating the ratio is not 1.0. The claim of "near 1.0" is unsupported by the paper and appears to misread the figure. Removed as factually inaccurate.

- **"Strength: Demonstrably useful for model debugging"** (Strength Finder): Based on a single anecdotal example (Figure 14). A single case study does not constitute a demonstrated strength. Removed as insufficiently supported.

- **"Missing related works"** (implicit in Harsh Critic's missing-baselines point): Do not mention missing related works per the rules (cannot verify external sources). Kept the *comparison gap* but not the "missing works" framing.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective not already present in the paper.

## Suggestions

1. **Either evaluate transparency or reframe the contribution.** Conduct a user study (even a small one) where participants compare CoLa-DCE explanations to LDCE explanations and answer questions about what changed. Alternatively, reframe the contribution away from "transparency and comprehensibility" and toward "controllable semantic-level minimality via concept selection," which the current evidence supports.

2. **Clarify the minimality framing.** Explicitly distinguish between *semantic minimality* (number of concepts changed) and *pixel-level minimality* (L1 norm). The paper currently conflates the two; the evidence supports the former but partially contradicts the latter.

3. **Acknowledge the L1 trade-off in the Limitations section and add a brief discussion of why concept conditioning increases pixel-level changes even as it improves FID** (e.g., gradient signal attenuation forces the diffusion process to rely more on stochasticity to reach the target class).

4. **Specify the spatial threshold η** and add a sensitivity analysis (or at minimum, state the fixed value used).

5. **Add at least one ablation on layer choice** to show whether concept selection quality is robust to this design decision.
