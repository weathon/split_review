Now let me compile my final consolidated review after thoroughly checking the paper against all reviewer claims.

---

## Summary

This paper studies fairness in AI-assisted decision-making when human decision-makers have heterogeneous expertise. It shows that existing calibration criteria (calibration and human-alignment) can produce unfair utility across groups with different expertise, introduces *inter-group-alignment* as a new criterion, proves an upper bound on utility disparity depending on both human-alignment and inter-group-alignment, and proposes *group-level multicalibration* as a method to achieve both properties simultaneously. Experiments on four tasks with real human data show that group-level multicalibration reduces utility disparity while maintaining or improving overall utility.

---

## Strengths

1. **First theoretical demonstration that human-alignment alone cannot guarantee fair utility under expertise heterogeneity.** Theorem 3.4 formally proves that perfectly human-aligned AI confidence still yields nonzero utility disparity when groups have different expertise, revealing a genuine limitation of prior work (Corvelo Benz & Rodriguez, 2023).

2. **Formalization of inter-group-alignment as a novel fairness criterion for AI-assisted decision-making.** Definition 3.5 defines inter-group-alignment, and Theorem 3.6 establishes a tight upper bound on utility disparity that depends jointly on human-alignment and inter-group-alignment, providing a concrete target for calibration design.

3. **Group-level multicalibration as a sufficient condition for both alignment goals.** Theorem 4.4 proves that α/2-multicalibration within each human group simultaneously yields α-human-alignment and α-inter-group-alignment, giving a clear algorithmic route to fair utility.

4. **Consistent empirical validation across four real-world tasks with human data.** Figure 2 shows that group-level multicalibration reduces utility disparity (e.g., from ~0.04 to near 0 on the Art task) while improving overall utility, outperforming both uncalibrated confidence and standard multicalibration. An important finding is that standard multicalibration sometimes *increases* disparity.

5. **Novel fairness perspective focused on decision-makers rather than decision subjects.** The paper identifies and formalizes a fairness problem distinct from mainstream algorithmic fairness (which targets individuals being decided upon), opening a new direction in AI-assisted decision-making research.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The experimental validation does not confirm that the chosen grouping (gender) actually exhibits expertise heterogeneity as formally defined.** The paper defines ED = P(Y=1|a, h, s₁) – P(Y=1|a, h, s₀) and states that groups are "expertise-heterogeneous if ED ≠ 0." However, the experiments split participants by gender and provide no analysis showing that, for the same human confidence h and AI advice a, the two gender groups differ in P(Y=1). If the observed utility disparity stems from other factors correlated with gender (e.g., different decision policies) rather than from expertise differences, the experiments validate the method for *some* group disparity but not specifically for the expertise-driven scenario that motivates the paper. The theoretical framework is unaffected, but the connection between motivation and evidence is weaker than claimed.

2. **The decision policy π(h,a) is learned on original (uncalibrated) AI confidence and applied to calibrated values without analyzing distribution shift.** The paper trains an MLP on data where human decisions were made in response to the original AI confidence, then feeds calibrated confidence values into this policy (Section 5.1). If calibrated values deviate substantially from the original distribution, the learned policy may extrapolate in unrealistic ways. The paper does not discuss how much the calibrated a values differ from the original a, nor test robustness to the choice of policy model. (This limitation is shared with prior work by Corvelo Benz & Rodriguez, 2023.)

3. **The asymmetry in the utility disparity bound coefficient is not explained.** Theorem 3.6's bound contains a term (3α_g − α_g²) with coefficient 3 on α_g, which is larger than the corresponding coefficient on α_h. The paper notes (Corollary 4.1) that minimizing α_g minimizes the bound, so the qualitative conclusion is unaffected. However, readers may reasonably wonder whether the asymmetry is exact or an artifact of the proof derivation; the paper provides no discussion. This is a missing explanation rather than a flaw in the result.

4. **The evaluation relies on a single crowdsourcing dataset.** All four tasks come from the same study (Vodrahalli et al., 2022a) with the same participant pool and experimental setting. While the tasks cover multiple modalities (image, text, tabular), generalizability to high-stakes settings (e.g., medical, legal) with different decision dynamics is not demonstrated. The paper does not acknowledge this limitation.

### Trivial

- The MLP-based decision policy model is described only by architecture (one hidden layer, 20 nodes, ReLU); training procedure, loss function, and feature construction are not reported. This is a minor reproducibility gap.
- The monotonicity assumption (Assumption 2.1) is central to the theory, but the learned MLP policy's monotonicity is not verified. If the learned policy is non-monotone, the theoretical framework does not strictly apply to the evaluation.

---

## Nice-to-Haves

- **Validate expertise heterogeneity directly.** Compute P(Y=1 | h, a) for each gender group using the *original* (uncalibrated) AI confidence and show that for the same h and a, the groups have different P(Y=1). If the data cannot support this, the experiments should be described as evaluating the method under *some* group disparity rather than specifically expertise-driven disparity.
- **Analyze the distribution of calibrated a values.** Show whether calibrated confidence values lie within the range seen during policy training. If they do, the extrapolation concern is mitigated; if not, a caveat is warranted.
- **Add sensitivity analysis for λ and ᾶ.** The main results use fixed values (λ=0.125, ᾶ=0.0001); demonstrating that conclusions hold over a range would strengthen robustness claims.
- **Statistical tests for Table 1 alignment metrics** to contextualize whether differences at the third decimal place are meaningful.

---

## Removed Points

These points were flagged but removed with justification:

- *"Missing proof sketch (appendix)"* — Parser strips appendices from all papers; the proofs exist in the original submission. REMOVED per hard rule.
- *"α/2 factor is not explained"* — The paper explains (end of Section 4) that the condition ᾶ+λ ≤ α/2 ensures the final discretized function satisfies α-alignment. The explanation is present, though terse. REMOVED as not factually correct.
- *"The paper should note there is work on algorithmic fairness for decision subjects"* — The paper already does this in Section 6.1. REMOVED as strawman.
- *"Whether f_A takes s as input or produces separate functions"* — The paper clearly defines f_A: Z → [0,1] with Z = {X, H, S} and describes updating bins per group. The design choice is transparent. REMOVED as the paper already makes this clear.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely overlap in their assessment: the theoretical contribution and method are sound, the experiments are well-designed, and the main limitations (unvalidated expertise-gender link, learned policy extrapolation, single-dataset source) are correctly identified by both the harsh critic and the strength finder but do not threaten the paper's core claims.

---

## Suggestions

1. Add an analysis showing whether the gender groups used in experiments actually exhibit expertise disparity (ED ≠ 0) under the paper's formal definition, using the original uncalibrated AI confidence. This would close the gap between the motivating story and the experimental evidence.
2. Include a brief analysis of how much the calibrated confidence values shift relative to the original training distribution, and discuss whether the learned decision policy is being applied in-distribution.
3. Clarify in the main text (not just the algorithm) why the bound in Theorem 3.6 contains the coefficient 3 on α_g, or note whether this is an artifact of the proof technique.
4. Acknowledge the single-dataset limitation explicitly in the paper.

---

## Score and Decision

The paper addresses an underexplored and practically important problem with a clean theoretical framework, a novel criterion (inter-group-alignment), and a well-motivated method (group-level multicalibration). The experiments are consistent across four tasks and convincingly demonstrate the method's effectiveness. The weaknesses are real but limited in scope — they concern the *connection* between the motivating story and the experimental instantiation, not the validity of the theoretical results or the core method. No fatal flaw exists. The contribution is solid and represents a clear step forward in a meaningful direction.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>