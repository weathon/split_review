Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

The paper introduces Scalable Ensemble Diversification (SED), a method that trains diverse model ensembles for ImageNet-scale tasks without requiring a separate OOD dataset. SED replaces external OOD disagreement data with dynamically weighted hard training samples, uses stochastic pair selection to reduce computational complexity from O(M²) to O(1), and introduces the Predictive Diversity Score (PDS) for OOD detection. Experiments demonstrate benefits in both OOD generalization (prediction ensembles, model soups) and OOD detection across ImageNet-A/R/C, OpenImages, and iNaturalist.

## Strengths

1. **First demonstration of disagreement-based ensemble diversification at ImageNet scale.** Prior methods (A2D, DivDis) were limited to small-scale settings. Table 1 shows SED achieves dramatic diversity gains (#unique predictions 5.00 vs. ~1.04–1.15 for baselines on IN-C-1), and Table 2 shows real OOD generalization improvements (e.g., prediction ensemble on IN-R: 48.7% with SED vs. 45.2% with A2D, M=5). This is the paper's central contribution and is well-supported.

2. **Predictive Diversity Score (PDS) provides a principled and effective OOD detector.** PDS directly exploits ensemble diversity rather than averaging it out like BMA. Table 3 shows SED-A2D with PDS achieves the highest AUROC on all four OOD datasets evaluated (e.g., OpenImages: 0.941 vs. best BMA baseline 0.923; IN-C-1: 0.681 vs. 0.642). Figure 2 further shows the causal link between diversification strength (λ) and improved OOD detection.

3. **Computational innovations make large-scale diversification practical.** The stochastic pair selection (reducing pairwise computations from O(M²) to O(1) per batch) and dynamic hard-sample weighting (eliminating the need for external OOD data collections) are genuinely useful algorithmic contributions. The O(1) complexity claim is theoretically grounded.

4. **Thorough evaluation across multiple aggregation and detection settings.** The paper tests three aggregation strategies (oracle, prediction ensemble, uniform soup) and two detection scores (BMA, PDS) across both covariate and semantic OOD shifts. The breadth of evaluation provides a complete picture of where SED helps and where it does not.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the evidence presented. The issues below are addressable in revision.

### Minor

1. **ID accuracy trade-off is acknowledged but under-analyzed.** For M=50 (Table 2), SED-A2D's ImageNet validation accuracy drops to 82.6–83.6% vs. 85.4–85.5% for deep ensembles — a ~2–3 point loss. For OOD detection, the PDS-based covariate-shift detector reports 1.0% IN-Val accuracy (Table 3). The paper acknowledges this cost for OOD detection (line 374) but does not discuss it for OOD generalization. A practitioner needs to see this trade-off quantified, ideally as a Pareto frontier (ID accuracy vs. OOD metric across λ values). The paper has λ sweeps (Figure 2) but does not overlay ID accuracy on the same plot.

2. **Scalability advantage asserted but not measured.** The paper claims computational superiority over A2D/DivDis via O(1) stochastic pair selection and shallow fine-tuning, but provides no wall-time or FLOPs comparison across methods. The text reports "2 to 12 hours per experiment" but not how this breaks down per method. Since the baselines also use shallow fine-tuning (line 221–222), the incremental cost of exhaustive pairwise disagreement vs. stochastic pairs is unclear without measurements. A simple table of training hours for M=5 and M=10 under SED vs. A2D would substantiate the scalability claim.

3. **The "1.0" IN-Val accuracy in Table 3 (SED-A2D, PDS, Covariate detector) requires clarification.** The paper reports 1.0% accuracy for the covariate-shift detector ensemble. This is an extreme degradation — barely above random (0.1%). If this is driven by an extreme λ choice, the paper should explain and show the λ value used. If it is a formatting/typographical error (possibly intended as 85.1 matching the BMA row), it must be corrected. The paper acknowledges this value in text (line 374) but does not explain its provenance.

4. **Potential distributional overlap in baseline evaluation.** A2D and DivDis baselines use ImageNet-R images (unlabeled) as their OOD disagreement data during training, and are then evaluated on ImageNet-R for OOD generalization (Table 2). While the disagreement objective does not use labels, the models are exposed to the IN-R image distribution during training. The paper notes (line 225) that the choice of OOD dataset has little influence (referencing Table 9 in appendix), but the main text should discuss this design choice explicitly. The cleanest comparison would use a held-out OOD source (e.g., a subset of Places365) for the baselines' disagreement data.

5. **The squared denominator in Eq. (5) and stop_grad on α_n are unmotivated design choices.** The normalization makes α_B = 1/avg_CE (line 152–154), which is sensible, but the paper does not explain why the denominator is squared rather than linear. Similarly, stop_grad on α_n means the sample weights do not backpropagate into the main loss — a potentially important interaction that is noted (line 161) but not analyzed or ablated. These are minor design decisions but an ablation would clarify their necessity.

### Trivial
- The paper would benefit from analyzing what "hard samples" look like qualitatively (e.g., a t-SNE projection or loss distribution analysis), beyond the IN-R examples in Figure 1 which are OOD test images, not training samples.
- Table 1 and 3 use the notion of "Covariate/Semantic detector types" which is not intuitive at first read; the caption explains it but the notation could be streamlined.

## Nice-to-Haves
- Wall-time training comparison across SED, A2D, and deep ensembles for M=5 and M=10.
- Ablation of the squared denominator in Eq. (5) (replace with linear denominator or no normalization).
- Ablation comparing SED with full A2D loss (all pairs) vs. stochastic pair selection to isolate the contribution of each.
- Analysis of whether the benefit comes from the hard-sample weighting or simply from applying disagreement to all training samples with any weighting.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about "the core motivation lacking conceptual justification"** — The paper is an empirical contribution and explicitly acknowledges in its Limitations section (line 450–452) that theoretical justification requires future work. The method is described with two clear desiderata (lines 141–142) and a mechanism (lines 144–154). The request for deeper theoretical analysis is beyond scope for an empirical methods paper; the existing justification is adequate for this paper class.
- **Criticism about "oracle selection being problematic"** — The reviewer acknowledges this is standard practice in the diversification literature (cites A2D, Damien1). The paper presents oracle as one of three aggregation strategies and does not over-claim its practical relevance. The meaningful results (prediction ensemble, uniform soup) show clear SED gains. This is standard practice, not a flaw.
- **Criticism about "computational efficiency conflating algorithmic innovation with engineering choice"** — The reviewer acknowledges the comparison is internally consistent (all methods use the same shallow fine-tuning setup). The three innovations (dynamic sample selection, stochastic pairs, layer-wise updating) are clearly delineated in the paper (lines 54–56). The conflation claim overstates the issue.
- **Criticism about "claim omits prior work at moderate scale"** — The paper mentions scimeca2023 (synthetic OOD) and the claim that prior work is limited to "small-scale artificial settings" is substantively correct for the ImageNet scale targeted here.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful points about the ID accuracy trade-off and missing runtime measurements, but these are actionable critique rather than novel synthesis.

## Suggestions

1. **Add a figure showing ID accuracy vs. OOD metric (AUROC or accuracy) as λ varies.** The paper already has λ sweeps in Figure 2; adding an ID accuracy curve would directly address the trade-off concern.
2. **Include a runtime comparison table** with wall-clock training hours for SED, A2D, and deep ensembles at M=5 and M=10.
3. **Clarify the "1.0" IN-Val value in Table 3** — either correct it if a typo, or explain the λ and behavior that produces this extreme degradation.
4. **Add an explicit discussion** of the distributional overlap between the baselines' OOD disagreement data (IN-R) and their evaluation on IN-R, along with the evidence from Table 9 that the choice of disagreement data does not materially affect results.
5. **Ablate the squared denominator** in Eq. (5) by comparing against a linear denominator variant.

## Score and Decision

This paper makes a clear empirical contribution: it demonstrates that disagreement-based ensemble diversification can work at ImageNet scale by replacing external OOD data with dynamically weighted hard training samples, and it introduces PDS as an effective OOD detector. The evidence in Tables 1–3 is consistent and supports the main claims. The weaknesses are about depth of analysis (under-explored trade-offs, missing runtime measurements, unmotivated design choices) rather than any invalidation of the core results. The paper honestly acknowledges its limitations. With the suggested additions, it would be a strong publication.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>