Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes k-CCP, a class-conditional conformal prediction method for imbalanced data that calibrates two thresholds per class: an inflated conformity score quantile and a calibrated rank threshold. By restricting candidate labels to the top-k predicted classes, k-CCP aims to produce smaller prediction sets than the standard class-conditional CP (CCP) while maintaining class-conditional coverage. The paper provides theoretical analysis (Theorem 1 for coverage, Theorem 2 for size reduction) and empirical evaluation on CIFAR-10, CIFAR-100, mini-ImageNet, and Food-101.

## Strengths

- **Novel double-calibration algorithm**: The k-CCP algorithm is a genuine algorithmic contribution — calibrating both a conformity score threshold and a rank threshold per class (Equation 9) to exploit the classifier's top-k accuracy is a natural and well-motivated idea that goes beyond prior CCP work. The algorithm design is clearly described and the reasoning for the two-threshold approach (lines 109–117) is sound.

- **Theorem 1 provides a meaningful coverage guarantee**: The condition in Theorem 1 (Equation 10) relating the inflated miscoverage rate α̃_y to the class-wise top-k error ε_y, calibration size n_y, and a confidence parameter δ is a real theoretical result. While the link to practice is imperfect (see weaknesses), the theorem itself gives a principled condition for achieving class-conditional coverage.

- **Strong empirical results on datasets with many classes**: On CIFAR-100, mini-ImageNet, and Food-101, k-CCP achieves 10–30% APSS reduction compared to CCP and cluster-CP while maintaining class-conditional coverage (Table 1, lines 188–190). The improvements are consistent across two imbalance ratios (ρ=0.5, 0.1) and three imbalance types (EXP, POLY, MAJ).

- **Diagnostic evidence supports the mechanism**: Figure 1 visualizes the trade-off condition σ_y, directly showing that σ_y ≪ 1 for the datasets where k-CCP is effective. This empirical validation provides insight into why the method works, independent of the theoretical issue with Theorem 2.

- **Sensitivity analysis on g**: Figure 2 demonstrates that k-CCP maintains lower APSS and UCR across a range of the hyperparameter g, showing practical robustness.

## Weaknesses

### Major

- **Theorem 2 is tautological and does not constitute a proof of size reduction.** Condition (12) and conclusion (13) are mathematically equivalent. Substituting the definition of σ_y into (12):
  - Left side = ∑_y P[V(X,y) ≤ Q̂_{1-α̃}^{class}(y), r_f(X,y) ≤ k̂(y)] = E[|Ĉ_{k-CCP}|]
  - Right side = ∑_y P[V(X,y) ≤ Q̂_{1-α}^{class}(y)] = E[|Ĉ_{CCP}|]
  
  Thus (12) is literally E[|Ĉ_{k-CCP}|] ≤ E[|Ĉ_{CCP}|], which is the same as conclusion (13). The theorem asserts "if k-CCP's expected size is smaller than CCP's, then it is smaller" — a restatement, not a proof. The paper's abstract and contributions section claim to "prove that k-CCP ... produces smaller prediction sets over the CCP method," but this theorem does not deliver that. The real evidence for size reduction is empirical (Figure 1's σ_y histograms), not theoretical. This overclaiming is a significant gap between the paper's rhetoric and its substance.

- **Gap between Theorem 1's theoretical guarantee and the practical implementation.** Theorem 1 (Equation 10) requires class-specific α̃_y satisfying α̃_y ≤ α − ε_{n_y} − δ − ε_y, depending on per-class calibration size n_y and top-k error ε_y. However, the experiments (line 177) use a **uniform** inflation g/√n applied identically to all baselines. No argument is given that this uniform scheme approximately satisfies the class-specific condition from Theorem 1, nor is there any discussion of how the validation-tuned g relates to the theoretical δ and ε_y terms. This creates a disconnect: the paper presents a "provable" method but the algorithm as implemented does not follow the provable recipe.

- **Inconsistent/incorrect claim about CIFAR-10 and σ_y.** The paper states (line 201): "k-CCP reduces to CCP on CIFAR-10, so σ_y=1 for all y and there is no trade-off." This is mathematically inconsistent. σ_y (Equation in line 147) uses the **inflated** coverage 1-α̃ in the numerator and the **original** coverage 1-α in the denominator. Even if k̂(y)=C (making the rank condition vacuous), σ_y = P[V ≤ Q̂_{1-α̃}^{class}] / P[V ≤ Q̂_{1-α}^{class}] ≠ 1 because α̃ < α (inflation). Furthermore, if the method truly "reduced to CCP," the APSS values would be identical — the paper itself appears to acknowledge differing APSS on CIFAR-10 in Table 1 (text says it "outperforms in most cases"). The explanation for behavior on small-C datasets is confused and should be corrected.

- **Evaluation uses balanced calibration sets.** The paper keeps calibration and test sets balanced (line 169). In real-world imbalanced data, calibration data is typically also imbalanced, meaning minority classes would have very few calibration samples — precisely where class-conditional coverage is hardest and where both CCP and k-CCP would suffer from unreliable quantile estimates. By using balanced calibration, the evaluation tests only the effect of the classifier's poor accuracy on minorities, not the effect of scarce calibration data. This is a significant limitation for a method promoted for "imbalanced data."

### Minor

- **Abstract overclaims for Proposition 1.** The abstract states that marginal CP "can perform arbitrarily poorly," but Proposition 1 (lines 76–86) only establishes a condition under which over- or under-coverage occurs for some classes. No quantification of "arbitrarily" (i.e., unboundedness of the coverage gap) is provided or proven.

- **"Double-calibration" terminology is imprecise.** The rank threshold k̂(y) (Equation 11) is set via an empirical error bound with a tuning parameter g, not via a conformal quantile procedure. Only the score threshold is calibrated in the CP sense. Calling both "calibrated" overpromises.

- **Incomplete results.** The paper states "We will add more results in final paper" (line 171) for conformalized training on CIFAR-100. A conference submission should be complete.

- **Imperfect comparison with cluster-CP.** Cluster-CP provides cluster-conditional rather than class-conditional coverage. While the paper controls UCR to be similar across methods, cluster-CP may require more inflation (yielding larger sets) to match class-conditional coverage, potentially disadvantaging it in APSS comparisons.

- **No pseudocode in the main text.** Algorithm 1 is mentioned but not displayed. While the prose description is largely sufficient, pseudocode would aid reproducibility.

### Trivial

- **Proposition 1's notation and conditions are dense and difficult to parse without careful study.** The ξ, ξ′ margins in Equation (7) are not given intuitive interpretation.

## Nice-to-Haves

- Evaluate with imbalanced calibration sets drawn from the same long-tail distribution as training data. This would test the method under the hardest realistic scenario.
- Reformulate Theorem 2 as a non-tautological statement: derive a bound on σ_y in terms of the classifier's top-k accuracy and calibration sizes, showing when σ_y < 1 provably holds under interpretable conditions.
- Provide pseudocode for the k-CCP calibration procedure.
- Clarify whether the inflation g/√n is applied class-wise (as Theorem 1 would suggest) or uniformly, and explain how the experimental g relates to the theoretical δ.
- Discuss diagnostic conditions under which k-CCP is not beneficial (few classes, low top-k accuracy).

## Removed Points

- Criticism about "does not discuss recent work on conformal prediction for balanced accuracy or set-size optimization" — removed per Rule 4 (missing related works).
- Criticism about "the proof (in appendix) is needed to see whether the gap can be arbitrarily large" about Proposition 1 — this is a strawman; Proposition 1 does not claim to show unboundedness, the abstract does. The core criticism (abstract overclaims) is kept in Minor; the appendix-as-evidence framing is removed.
- The reviewer's claim that "k-CCP often has worse APSS than CCP (Table 1: e.g., ρ=0.5 EXP: 1.85 vs 1.80)" — the paper's text (line 190) states "k-CCP still outperforms others in most cases even on CIFAR-10," so the reviewer's characterization is not verifiable from text and may constitute cherry-picking specific configurations. The valid criticism is about the inconsistent explanation of CIFAR-10 behavior, which is kept in Major.

## Novel Insights

The central tension revealed by the reviews is that k-CCP's actual strength is its cleverly constructed empirical calibration procedure (two-threshold trade-off), not its supporting theory, despite the paper framing theory as the headline. The σ_y diagnostic (Figure 1) is the paper's most insightful element — it directly visualizes the trade-off mechanism and shows that for datasets with many classes, the rank constraint is much more restrictive than the score threshold, yielding meaningful set-size reductions. The real scientific contribution is less "we proved k-CCP is better" and more "here is a diagnostic (σ_y) that reveals when restricting candidate labels by rank reduces set size, and here is how to exploit it." Reframing the paper around this diagnostic insight rather than the vacuous Theorem 2 would make the contribution both more honest and more useful to practitioners.

## Suggestions

1. Remove or significantly reframe Theorem 2. Acknowledge that it is not a substantive theorem but rather a definitional observation that σ_y < 1 is the condition for size reduction. Replace it with either (a) a non-trivial bound on σ_y derived from classifier properties, or (b) an honest empirical characterization of when σ_y < 1 holds, with the diagnostic figure as the main evidence.
2. Bridge the gap between Theorem 1 and practice: either modify the implementation to use class-specific inflation following Theorem 1, or provide a justification for why uniform inflation empirically satisfies the coverage condition (e.g., a bound showing that the uniform choice is a conservative approximation).
3. Correct the CIFAR-10 / σ_y explanation. The statement "k-CCP reduces to CCP" and "σ_y=1" are both incorrect under the paper's own definitions.
4. Add an experiment with imbalanced calibration sets (drawing calibration data from the same long-tailed distribution as training). This is the most impactful addition for strengthening the paper.
5. Include an algorithm pseudocode box in the main paper.
6. Tone down the "provable" language in the abstract and contributions, or deliver on it properly.

## Score and Decision

The paper identifies a meaningful problem and proposes a novel algorithmic solution with promising empirical results on datasets with many classes. However, the theoretical contribution is significantly overclaimed — Theorem 2 is tautological, and the gap between Theorem 1's guarantee and the implementation is unaddressed. The evaluation avoids the hardest realistic scenario (imbalanced calibration sets), and the CIFAR-10 analysis contains mathematical inconsistencies. The paper would benefit from honest reframing: acknowledging the heuristic nature of the size-reduction claim, correcting the technical errors, and strengthening the evaluation. In its current form, the paper does not deliver on its stated promises.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>