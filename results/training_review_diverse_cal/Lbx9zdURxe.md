I have verified all claims against the paper. Let me now construct the final consolidated review.

---

## Summary

This paper proposes to regularize the energy (derived from classifier logits) among training samples rather than between in-distribution and OOD samples, as done in prior OOD detection work. It makes three main contributions: (1) calling attention to energy differences among in-distribution samples, (2) theoretically unifying data re-weighting and margin control for long-tail recognition as implicit energy regularization via a clean gradient derivation (Section 3.2, Eq. 5-6), and (3) proposing Influence Aware Energy Regularization (IAER) that uses influence functions to determine per-sample energy regularization coefficients for general OOD generalization scenarios. Experiments span long-tail classification (CIFAR-LT, ImageNet-LT, iNaturalist), subpopulation shift (SubpopBench), and domain generalization (DomainBed).

## Strengths

- **Theoretical unification of reweighting and margin control.** The derivation in Section 3.2 (Eq. 5-6) is sound: adding an energy regularization term with coefficient β_x produces gradient adjustments that simultaneously act as data reweighting (by factor 1-β_x) and margin control (shifting the coefficient of ∂f/∂θ from p(y|x)-1 to p(y|x)-1/(1-β_x)). This provides a clean, unified perspective on two major branches of long-tail methods that were previously seen as separate, and the result is non-trivial — it shows both effects emerge from a single source.

- **Empirical demonstration of energy bias in long-tail models.** Figure 2 is compelling: under ERM, average energy per class shows a strong negative correlation with class frequency (Pearson R = -0.74 on CIFAR10-LT, -0.60 on CIFAR100-LT), which nearly vanishes under LDAM (R = -0.26 and 0.16). This directly supports the paper's central thesis that standard training induces energy disparities and that long-tail methods implicitly level them.

- **Broad experimental scope across three OOD settings.** The paper evaluates across long-tail, subpopulation shift, and domain generalization — a wider range than many papers in this space. The most notable result is on CIFAR10-LT (imbalance 100), where IAER reduces ERM error from 29.64% to 24.17% (a 5.47% improvement). Subpopulation shift results (Table 4) show consistent improvements in both mean and worst-group accuracy.

## Weaknesses

### Major

- **IAER's core mechanism — the influence function — has acknowledged but unaddressed theoretical fragility for neural networks.** The paper assumes twice-differentiable, strictly convex loss to derive the influence function (Section 4.1), then acknowledges in Section 6 that "the influence function may not reflect the actual influence for neural networks." This is not a minor limitation: it means the method's central mechanism for determining per-sample energy regularization coefficients lacks a principled theoretical foundation for the setting in which it is applied. While using influence functions for neural networks is common practice (following Koh & Liang 2017), the gap between the convexity assumption and the non-convex reality is material here because the entire IAER method rests on the accuracy of these coefficients. The experimental results provide some empirical justification, but the paper does not include any diagnostic analysis (e.g., does the ranking of influence values correlate with actual impact of energy regularization when measured directly?) to bridge this gap.

- **The IAER method shows scenario-dependent and often marginal gains relative to its high computational cost.** On CIFAR100, improvements over baselines are often <1% and the paper acknowledges that performance can be sensitive to validation set size (attributing the small gains to few images per class). On domain generalization (Table 5), improvements over ERM are marginal on standard benchmarks: +0.1% on PACS, +0.5% on VLCS. On ImageNet-LT, IAER[Few] improves few-shot accuracy but the overall gain is modest (e.g., +0.8% for LWS+IAER[Few]) and the method requires choosing which validation subset to use — effectively three separate sets of results with no principled selection criterion. Meanwhile, the influence function approximation takes 718 seconds on CIFAR10 ResNet-32 alone (Table 6), and the paper provides no ablation on the approximation hyperparameters (iteration count, stochastic estimation variance) or stability analysis across random seeds. This combination of theoretical fragility, modest and inconsistent gains, and high cost makes it unclear whether the method is practically useful as presented.

### Minor

- **The "unification" claim is slightly overstated.** The derivation (Eq. 5-6) shows that *if you add an energy regularization term*, the resulting gradient combines reweighting and margin effects. This is a genuine and interesting connection — energy regularization *provides a unified perspective* on the two families. However, the paper's phrasing that long-tail methods "could be unified as implicit energy regularization" (contributions list) and that energy regularization "unifies" them (Section 3.2) implies a stronger two-way equivalence than is established. The derivation does not show that existing reweighting or margin methods are equivalent to energy regularization — only that energy regularization *induces* both effects simultaneously. The empirical evidence (Figure 2) supports the claim for LDAM, but the theoretical claim remains one-directional. This does not undermine the contribution but more precise phrasing would strengthen the paper.

- **The connection between Section 3 (unification framework) and Section 4 (IAER method) is weak.** Section 3 establishes that energy regularization produces reweighting+margin effects, and Section 4 proposes IAER to determine β coefficients via influence functions. But IAER does not leverage the specific derivation from Section 3.2 in any direct way — it simply adds an energy regularization term and uses influence functions to set β. The unified framework from Section 3 suggests that simpler heuristics (e.g., setting β proportional to class frequency for long-tail, or inversely proportional to domain size for DG) might work as well, but this is not tested. The paper would be stronger if it either built IAER directly on the framework or tested whether simple heuristics match IAER's performance.

- **No ablation or stability analysis of the influence function approximation.** Despite this being the computational bottleneck and a source of potential instability (stochastic estimation with 5000 iterations, 10 trials), the paper provides no analysis of how the approximation quality varies with iteration count, validation set size, or random seed.

### Trivial

- The paper does not provide numerical results for larger domain generalization benchmarks (e.g., TerraIncognita, OfficeHome) that are standard in DomainBed.
- Remark 4.1 (Arbitrary Energy) states a well-known property of the softmax — adding a constant to all logits shifts energy but not probabilities. This is not incorrect but adds little new insight.

## Nice-to-Haves

- A simpler baseline for setting β coefficients (e.g., proportional to inverse class frequency for long-tail, inversely proportional to domain counts for DG) would help disentangle whether the value of the paper is in the *concept* of energy regularization or in the *influence-function machinery*. If simple heuristics match IAER, the contribution is the framing; if not, IAER's complexity is justified.
- Comparisons to state-of-the-art methods on domain generalization benchmarks (beyond ERM) would strengthen the claim that IAER provides additive gains on top of existing approaches.
- An analysis showing that IAER actually changes the energy distribution across domains/subpopulations (analogous to Figure 2 for LDAM on long-tail) would directly support the paper's motivation for the generalization settings.

## Removed Points

The following points from the reviews were evaluated against the paper and removed:

1. **"No comparison to SOTA domain generalization methods"** — The paper explicitly states that it "take[s] the algorithms implemented in DomainBed as baselines" (line 253), which includes many DG methods (CORAL, MixStyle, etc.). The reviewer's claim is inaccurate.
2. **"First to call for attention overstates novelty"** — The paper qualifies this with "to the best of our knowledge," which is standard. Moreover, the paper itself shows that prior long-tail methods deal with energy implicitly but not *explicitly* — making the framing claim reasonable. Generic novelty-nitpicking removed.
3. **"Remark 4.1 does not add new insight"** — While not groundbreaking, this remark is included for completeness and does not harm the paper. Removing as a presentational nitpick.
4. **"The paper should also cover Y / additional tasks" (TerraIncognita, OfficeHome)** — These are reasonable extensions but the paper already covers three DG benchmarks (CMNIST, PACS, VLCS) and the DomainBed protocol. Demanding more benchmarks is scope creep; mentioned in Trivial/Nice-to-Haves instead.
5. **Complaint about "baseline is only ERM" for subpopulation shift** — The paper states it follows SubpopBench (which includes multiple standard baselines). The table is an image, and the claim cannot be cleanly verified from the text, so this is downgraded.

## Novel Insights

The most interesting finding from the reviews is the structural disconnect between the paper's two main technical contributions: the unification framework (Section 3) and the IAER method (Section 4). The unification framework genuinely adds theoretical value by showing that energy regularization subsumes both reweighting and margin effects — this is a contribution that stands independently of IAER. The IAER method, meanwhile, essentially reinvents the β-coefficient determination problem rather than leveraging the insight that in known-shift settings (long-tail), the β coefficients could be set by simple class-frequency heuristics. A stronger paper could have tested whether the unification framework itself suggests practical guidelines for setting β, rather than introducing a separate (and theoretically fragile) influence-function machinery. This suggests the paper's core value may be in the theoretical framing more than in the particular method proposed.

## Suggestions

- **Replace or simplify the influence-function mechanism.** Given its theoretical fragility and computational cost, a simpler approach — even a heuristic based on the insights from Section 3 — would make the paper's contributions cleaner and more practically useful. If the influence function is kept, at minimum add ablation studies on its approximation quality, stability across seeds, and sensitivity to validation set composition.
- **Add diagnostic evidence connecting IAER to energy distribution changes.** For the domain generalization and subpopulation shift experiments, show that IAER produces more uniform energy across domains/subpopulations (analogous to Figure 2 for LDAM), directly supporting the paper's core motivation.
- **Tighten the "unification" language.** Rephrase the claim to state that energy regularization *provides a unified perspective on* or *subsumes* both reweighting and margin control, rather than implying that existing methods are equivalent to energy regularization.

## Score and Decision

**Originality:** 6/10 — The energy-regularization perspective on training samples is relatively novel, though the derivation itself is straightforward gradient manipulation.

**Importance of Research Question:** 6/10 — Understanding why certain training dynamics help OOD generalization is an important question, and the energy lens is a useful addition.

**Claims Support:** 4/10 — The unification claim is moderately well-supported (derivation + Figure 2), but the IAER method's evidence is mixed and the central mechanism has acknowledged theoretical gaps.

**Soundness/Experiments:** 5/10 — Experiments cover appropriate settings but are often compared against limited baselines (ERM in several cases), improvements are modest, and the computational cost is high.

**Clarity:** 6/10 — Generally clear, though the relationship between Sections 3 and 4 could be better motivated.

**Value to Community:** 5/10 — The energy perspective on training samples and the unification of reweighting/margin control are valuable insights. The IAER method as presented is unlikely to be widely adopted in its current form due to cost and mixed results.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>