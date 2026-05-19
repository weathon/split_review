- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 3, 5, 5, 5
Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

This paper introduces "Scale Shift Domain Generalization" for crowd localization, establishing that differences in head scale distributions between training and test domains cause dramatic performance degradation. It contributes ScaleBench (17,138 images, 1.5M manually annotated bounding boxes, partitioned into four scale-separated domains), evaluates 20 DG algorithms, provides a theoretical analysis framing scale shift as a mixed diversity-and-correlation shift, and proposes Semantic Hook as a case-study mitigation method. The paper's main empirical findings (Q1–Q4) — that adding more in-distribution data provides marginal benefit, that scale-aware sampling achieves "less is more," that interpolation offers limited help, and that enhancing semantic (rather than scale) association is effective — are genuinely novel and actionable.

## Strengths

- **First dedicated benchmark for scale shift in crowd localization.** ScaleBench is carefully constructed: 1.5M new bounding box annotations on 2,700 images from SHHA/SHHB/QNRF, combined with three already-annotated datasets, then partitioned into four domains (Tiny/Small/Normal/Big) using a principled 2D mixed-Gaussian patch-splitting procedure followed by Gaussian sampling to enhance inter-domain separation (Eqs. 2–5). The leave-one-out evaluation across four domains is appropriate and provides a controlled testbed that did not previously exist.

- **Empirical insights from Q1–Q4 are novel and actionable.** (i) Table 3 shows that adding the Big domain to training for target Small improves performance only from 77.92% (TN→S) to 77.94% (TNB→S), quantitatively demonstrating diminishing returns from scale-mismatched data. (ii) Figure 4's "less is more" finding — IID sampling by scale achieves comparable performance with only 30% of data — is non-obvious and supports the claim that scale distribution is a primary attribute. (iii) Table 5's ablation showing semantic perturbation substantially outperforms scale perturbation (+4.88 points OOD F1) directly validates the core design principle.

- **Large-scale reproduction of 20 DG algorithms exposes an under-explored challenge.** Table 2 reports F1 scores for 20 algorithms across three backbones (ResNet18, HRNetW-48, ViTBase), showing many advanced methods performing at or below the ERM baseline. This is a genuine empirical signal that existing DG techniques do not readily handle scale shift.

- **The paper acknowledges its own limitations honestly.** The authors explicitly state that SemanticHook shows "only marginal improvement" (line 242) and position it as "a case study" and an "effective tool for analyzing the scale shift issue" rather than a SOTA claim (line 244). This candor is commendable.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 1 is asserted rather than proven.** The theorem claims that when scale distributions differ (p₁(c|z) ≠ p₂(c|z)), both diversity shift (Div_div > 0) and correlation shift (Div_cor > 0) are present. The diversity shift claim follows straightforwardly from p₁(c) ≠ p₂(c). The correlation shift claim, however, requires showing that p₁(y|c) ≠ p₂(y|c) — i.e., the label distribution conditioned on scale differs between domains. The paper does not provide this proof; it simply writes down the definition from Ye et al. (2022) and asserts positivity. Equation 6 is a general decomposition of p(y|x) that does not specifically implicate scale shift. This weakens the paper's claimed theoretical contribution. The paper would be stronger if this were reframed as an empirically motivated hypothesis or heuristic decomposition rather than a formal theorem.

- **Hyperparameter tuning for the 20 reproduced DG algorithms is not described, undermining the central empirical claim.** The paper states it "follow[s] DomainBed (Gulrajani & Lopez-Paz, 2021)" only for train/validation splitting (line 173), but DomainBed's core methodological lesson is that DG algorithm rankings are highly sensitive to hyperparameter tuning — many methods match or underperform ERM when tuning is suboptimal. The paper does not describe what hyperparameter search was performed, the search spaces, the selection criterion, or whether task-specific tuning was done for each of the 20 algorithms. Without this information, readers cannot distinguish between a genuine failure of DG methods on scale shift and an artifact of poor adaptation. This is the most significant omission, as the paper's framing relies on this comparison to motivate the under-explored nature of the problem.

### Minor

- **Semantic Hook's mechanism is not well-justified.** The "Intuitive Remark" (line 162) states that Gaussian noise ε "primarily influences the semantic information," but Gaussian noise applied at the pixel level affects edges, textures, colors, and all low-level features — not selectively semantic information. The paper provides no evidence that the residual embedding f_E(x+ε) − γ f_E(x) selectively removes scale-related information while preserving semantics. The method would benefit from a clearer formal statement about what properties of ε ensure this selectivity.

- **Missing control ablation for the hooking mechanism.** Table 5 ablates semantic vs. scale perturbation but does not include the obvious control: training with Gaussian noise augmentation alone (without the residual hooking operation and without the second loss term). Without this, the contribution of the hooking mechanism itself (as opposed to noise augmentation) is unclear.

- **Missing variance/confidence information.** Table 2 reports single F1 values for each algorithm×domain combination with no standard deviations or multiple-seed runs. Given that many comparisons show small differences (e.g., ERM 66.79 vs. DANN 66.96 on ResNet18), readers cannot assess whether differences are meaningful.

- **Some implementation details are underspecified.** The noise distribution ε ∼ 𝒩(λ, 𝐈) leaves λ unspecified (line 151). The annealing schedule for γ is described only in qualitative terms (lines 274–280). The heuristic search for σ_m in Eq. 5 is mentioned but not detailed. These affect reproducibility.

### Trivial

- The potential biases introduced by the patch-splitting filtering criteria (3-σ rule, minimum patch height) and the artificial nature of the four domains relative to real-world scale shifts are not discussed as limitations.
- The paper does not discuss whether the patch-splitting procedure destroys contextual information useful for localization.

## Nice-to-Haves

- Including a baseline where the model is trained with the same Gaussian noise augmentation but without the residual hooking (i.e., just training with f_E(x+ε) and no second loss) to isolate the hooking mechanism's effect.
- Reporting standard deviations across multiple random seeds for the main results (Table 2).
- Deepening the "less is more" analysis: testing whether the IID sampling result is robust across different backbones and whether uniform random sampling (not scale-aware IID) produces the same pattern.
- Specifying λ for ε ∼ 𝒩(λ, 𝐈) and formalizing the γ annealing schedule.

## Removed Points

- **Prior work acknowledgment (Harsh Critic, Sec. 1):** The critic claimed the paper should "acknowledge prior work on scale-aware training… more precisely." The paper already does this (line 26: cites Han et al., 2023; Wang et al., 2023a; Ma et al., 2021, explicitly distinguishing domain generalization from domain adaptation). The criticism is factually incorrect given what is on the page.

- **First-study claim qualification (Harsh Critic):** The critic suggested the "FIRST study" claim should be qualified. The paper already qualifies it with "as far as we know" (line 28) and explicitly distinguishes its setting (DG with unseen target, maintaining source performance) from prior work. This is appropriately nuanced.

- **Strength Finder's "rigorous theoretical proof":** The claim that Theorem 1 "rigorously shows scale shift involves both diversity shift and correlation shift" conflicts with the verified weakness that the theorem is not properly proven (the correlation shift part is asserted without proof). Since the weakness wins, this overstated strength is removed.

- **"Evaluation lacks rigor" framing (Harsh Critic):** The critic's general framing that the evaluation "lacks rigor" is too broad. The specific, anchored concern (missing hyperparameter tuning protocol) is kept; the dismissive framing is removed.

- **Nitpick about appendix/absent references:** Any implication that missing sections in the parsed PDF reflect missing content in the original submission is disregarded.

## Novel Insights

None beyond the paper's own contributions. The reviews do not contribute observations that meaningfully extend or reinterpret the paper's findings.

## Suggestions

1. **Reframe Theorem 1 as an empirically motivated hypothesis or decomposition,** not a formal theorem. Remove the claim of proof and instead present the two terms as a useful lens for interpreting the experimental results. The paper's empirical contributions (Q1–Q4) are stronger than its theory, and the paper would benefit from leaning into this.

2. **Provide the hyperparameter tuning protocol** for all 20 reproduced DG algorithms: search spaces, selection criterion, number of trials, and whether validation was done on the source-domain validation sets per DomainBed conventions. If the authors used default hyperparameters without tuning, state this clearly and temper the corresponding claim (e.g., "off-the-shelf implementations without task-specific tuning").

3. **Add the missing control ablation** for Semantic Hook: training with noise augmentation alone (without the hooking loss) to isolate the effect of the residual hooking mechanism.

4. **Specify λ** in ε ∼ 𝒩(λ, 𝐈) and the γ annealing schedule, and ideally add a formal description of what property of ε makes the residual embedding approximately scale-invariant.

5. **Add standard deviations** (or multiple-seed runs) to the main results table, or explicitly note their absence as a limitation.
