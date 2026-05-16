Now I have sufficient information to compose the final review. Let me synthesize everything.

---

## Summary

This paper proposes to regularize the energy (from energy-based models) among training samples to improve out-of-distribution (OOD) generalization. It first shows empirically (Figure 2) and theoretically (Section 3.2) that long-tail recognition methods (reweighting and margin control) can be understood as implicitly regularizing the energy distribution across classes. It then extends this perspective to general OOD scenarios (subpopulation shift, domain generalization) by introducing Influence Aware Energy Regularization (IAER), which uses influence functions to determine per-sample energy regularization coefficients. Experiments span CIFAR-LT, ImageNet-LT, iNaturalist, SubpopBench datasets, and DomainBed benchmarks.

## Strengths

1. **Novel perspective on energy disparity among in-distribution samples.** Prior work (Liu et al. 2020; Grathwohl et al. 2020) uses energy for OOD detection or generation but focuses on the gap between IID and OOD data. This paper is the first to systematically investigate and regularize energy differences among training samples themselves — a genuine and underexplored direction. (Abstract, §1)

2. **Theoretical unification of long-tail methods as implicit energy regularization.** The derivation in §3.2 (Eqs. 5–6) shows that adding an energy regularization term decomposes into two gradient effects — sample reweighting and margin adjustment — which correspond to two major branches of long-tail methods. This provides a principled unifying lens absent in prior work, supported by the empirical finding (Figure 2) that LDAM produces nearly uniform class-wise energy while ERM does not.

3. **IAER extends energy regularization beyond long-tail to general OOD scenarios via influence functions.** Using influence functions to determine per-sample regularization coefficients (§4.1, Eqs. 8–11) is a principled way to handle implicit distribution shifts where no prior knowledge (like class frequencies) is available. The method is evaluated across three distinct OOD categories (long-tail, subpopulation shift, domain generalization) — broader than most papers in this space.

4. **Orthogonality to risk-based methods is formally shown.** Remark 4.1 proves that energy can be arbitrarily changed without altering predicted class probabilities, demonstrating that energy regularization is complementary to invariant risk minimization — a distinction overlooked in prior work.

5. **Empirical insights into influence values.** Figure 3 (influence positively correlated with class count, R = 0.70) and Figure 4 (influence uncorrelated with training loss, R = −0.04) provide useful diagnostics about what the method is doing and why it targets different samples than loss-based approaches.

## Weaknesses

### Fatal
None.

### Major

1. **Missing control for continued training without regularization in long-tail experiments.** In Table 2, the paper takes models pre-trained with ERM or LDAM-DRW and fine-tunes with IAER for 5 epochs. The comparison is against the original pre-trained model, not against continued fine-tuning with standard cross-entropy for the same 5 epochs. Without this control, part of the observed gains (e.g., 5.47% error reduction on CIFAR10-LT) could be due to additional training rather than the energy regularization term. The same issue affects the ImageNet-LT and iNaturalist experiments (Table 3), where IAER is applied during classifier retraining. This is the single most important missing piece for establishing causal attribution. (Section 4.2.1)

2. **Subpopulation shift experiments lack comparison with established methods.** Table 4 compares IAER only against ERM, despite the SubpopBench testbed including many standard algorithms (e.g., group DRO, JTT, LfF). Since subpopulation shift is one of the three main evaluation scenarios, the absence of these baselines makes it difficult to gauge whether IAER adds value beyond standard practice or is competitive. (Section 4.2.2)

### Minor

1. **Theoretical "unification" is more suggestive than rigorous.** The derivation in §3.2 shows that *adding energy regularization* combines reweighting and margin control effects, which is clean. However, the claim that existing methods (reweighting, LDAM) "could be unified as implicit energy regularization" is not fully substantiated: there is no mapping from a given reweighting scheme to a specific per-sample β_x, and the margin effect in LDAM operates on logits before softmax whereas the derivation here changes a gradient coefficient. The empirical evidence (Figure 2) is correlational, not causal. The conceptual framing is valuable, but the paper should be more precise about what is being "unified" and what is shown.

2. **Domain generalization improvements are small and lack statistical characterization.** In Table 5, improvements over ERM are often <1%, and no standard deviations or confidence intervals are reported despite the paper stating "5 trials" were conducted. On some test conditions, IAER can underperform ERM. Without variance estimates, the significance of these marginal gains is unclear.

3. **No validation of the influence function approximation quality.** The influence function assumes convexity and infinitesimal perturbations — conditions violated by neural networks. The paper acknowledges this limitation (§6) but does not empirically evaluate whether the computed influences correlate with the actual effect of a finite energy penalty. A small-scale validation (e.g., comparing predicted influence against actual change in validation loss for a subset of points) would substantially strengthen the method's credibility.

4. **Influence-based β assignment is heuristic.** Setting β proportional to the negative normalized influence (scaled by γ) is reasonable but not derived from any optimality principle. There is no analysis of whether the sign of the influence reliably predicts the benefit of regularization for OOD generalization, or how robust the coefficients are to the choice of validation subset.

5. **No ablation of the key hyperparameter γ** (Eq. 10). The paper sets 0 < γ < 1 but does not report sensitivity to its value or how it was chosen across experiments.

### Trivial

1. The description of the "margin" effect in §3.2 (line 100) uses non-standard terminology: the gradient coefficient (p̄(y|x) − 1/(1−β̂_x)) is described as a "margin," whereas margin conventionally refers to logit differences (f(x)[y] − max_{j≠y} f(x)[j]). While the algebraic connection is clear, this could confuse readers.

2. The paper could strengthen the causal evidence in Figure 2 by also showing the energy distribution after applying reweighting methods, not just LDAM, to more fully support the "implicit regularization" claim.

## Nice-to-Haves

- Add a "fine-tune with cross-entropy" control for the long-tail experiments (Table 2, 3). This is the single most impactful addition.
- Compare against a simpler uniform energy regularization baseline (fixed β for all samples) to isolate whether the per-sample weighting from influence functions is beneficial relative to a simpler approach.
- For domain generalization (Table 5), test combining IAER with IRM or other risk-based methods to empirically verify the claimed orthogonality (Remark 4.1).
- Report standard deviations for all main results.
- Provide a sensitivity analysis for γ.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"First to call" claim is overstated (Harsh Critic).** The paper says "to the best of our knowledge, we are the first to call for attention to the energy difference between in-distribution data samples." Prior OOD detection work focuses on IID-vs-OOD energy thresholds, not regularizing energy *among* training samples. This is a genuine distinction; the claim is appropriately qualified. **Removed** — the criticism misreads the paper's contribution.
- **Influence sign convention contradiction (Harsh Critic).** The critic states the text says "increase energy on points with positive influence" but the formula β = −γ·Z_val/Z_max "contradicts." This is incorrect: when Z_val > 0, β < 0, and L_ce + β·E_θ = L_ce − |β|·E_θ, which encourages higher energy — exactly matching the text. **Removed** — factually wrong.
- **"Unsubstantiated speculation" about overfitting (Harsh Critic).** The paper explicitly says "we conjecture" (line 279), which is appropriate for speculation. **Removed** — not presented as a claim.
- **Figure 2 does not establish causation (Harsh Critic).** The paper presents it as empirical evidence ("empirically indicate"), not as a proof. **Removed** — standard correlational evidence, not misrepresented.
- **Time complexity criticism (Harsh Critic).** The critic notes the overhead is "honestly reported" and "substantial but may be acceptable." This is not a weakness. **Removed**.
- **Generic/weak strengths from Strength Finder.** The strength finder's point about "Comprehensive empirical validation" is partially retained as Strength #3 because the breadth of evaluation is genuinely noteworthy, though weaknesses temper this.

## Novel Insights

The most interesting observation emerging from the reviews — beyond the paper's own contributions — is that the influence of energy regularization is uncorrelated with training loss (R = −0.04, Figure 4). This counterintuitive finding, together with the result that influence correlates with class frequency (Figure 3), suggests that energy regularization operates on a fundamentally different axis from loss-based interventions. The paper's observation that energy is "arbitrary" with respect to class predictions (Remark 4.1) further underscores this. This decoupling of energy from both loss and accuracy could open a research direction where energy regularization is used as an orthogonal knob for controlling model confidence and generalization, testable in conjunction with existing methods.

## Suggestions

1. **Add a simple control experiment for every fine-tuning setup:** fine-tune the same pre-trained model with standard cross-entropy for the same number of epochs and report the result alongside IAER. This directly addresses the most critical attribution gap.
2. **Expand subpopulation shift baselines** to include at least group DRO and one other standard method (e.g., JTT) to contextualize IAER's improvements.
3. **Validate the influence approximation** on a small subset: compare predicted influence against actual change in validation loss after a small energy penalty step, and report the correlation.
4. **Report standard deviations** for all main tables, especially where gains are marginal (<1%).

## Score and Decision

The paper introduces a genuinely novel perspective (energy regularization among training samples) with a theoretically grounded method (IAER) and evaluates it across diverse OOD scenarios. The core contribution is clear and interesting. However, the experimental validation has notable gaps — most critically the missing fine-tuning control for long-tail experiments and the limited baselines in subpopulation shift — that prevent full confidence in the reported improvements. These are addressable in revision but nontrivial in scope.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>