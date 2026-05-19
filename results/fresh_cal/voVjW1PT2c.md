Now I have a thorough understanding of the paper. Let me write my consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now produce the final review.

---

After careful analysis, here is my assessment. The paper proposes ProMix, using mixup to diversify the auxiliary outlier set for OOD detection, with theoretical analysis and empirical results. Let me verify the key claims systematically.

**Verification of the numerical discrepancy claim:**

The paper text (line 216) states: "compared to the best baseline, ProMix achieves a reduction in terms of FPR95 of 0.36% and 4.77% on CIFAR-10 and CIFAR-100... relative error reductions of 14.2% and 31.5%."

For CIFAR-10: 0.36/14.2% = 2.54. This matches OE at ~2.55 from the critic's reading. ✓
For CIFAR-100: 4.77/31.5% = 15.14. The critic claims POEM is 14.14 and ProMix is 10.34 (diff=3.80, rel=26.9%).

The table is an image, so I cannot independently verify. The paper's stated numbers (4.77 reduction, 31.5% relative) imply the best baseline has FPR95 ≈ 15.14 and ProMix ≈ 10.37. If POEM is at 14.14 as the critic claims, then POEM is NOT the "best baseline" here, and there must be another method at ~15.14 that is the best baseline. Or the critic misread the table. Since I cannot verify, I flag this as a potential concern rather than a confirmed error.

**Verification of the ℋ*_div ⊆ ℋ*_aux claim:**

Line 100: "Because 𝒳_aux ⊂ 𝒳_div holds, the hypotheses performing well on 𝒫_{𝒳_div} also perform well on 𝒫_{𝒳_aux}, giving rise to ℋ*_div ⊂ ℋ*_aux."

I confirm this is indeed unsubstantiated. The fact that a hypothesis minimizes the total loss on the diverse distribution (ID + more OOD classes) does NOT guarantee it minimizes the sub-loss on the original distribution (ID + fewer OOD classes). A hypothesis could have slightly higher loss on the original sub-distribution but compensate with much lower loss on the new OOD classes. This is a genuine logical gap. The over-parameterized justification on line 66 is only given for ℋ*_ood ⊆ ℋ*_aux, not for this claim.

**Verification of missing hyperparameters:**

ω is mentioned in the training objective (line 176) but its value is never specified. ✓ Confirmed missing.
γ is the threshold for detection — determined by the FPR95 evaluation criterion, not a hyperparameter. So this is not missing.

Now let me write the final review.## Summary

This paper proposes ProMix, a method that applies mixup to auxiliary outlier sets used during OOD detection training, combined with informative (greedy) sampling, to improve OOD detection performance. The paper provides a theoretical generalization bound arguing that more diverse auxiliary outliers reduce the OOD detection error bound, and that mixup enhances diversity. Experiments on CIFAR-10 and CIFAR-100 with six OOD test datasets show competitive results against several baselines.

## Strengths

- **Novel and well-motivated core idea**: The paper identifies diversity of auxiliary outliers as a key factor in OOD detection generalization and proposes mixup as a practical method to increase it. This connection between mixup and OOD detection theory is novel. The intuition that semantic diversity matters more than sample size is well-supported by controlled experiments (Figure 2, Section 5.2), which directly manipulate outlier class count while holding sample size constant.

- **Strong ablations isolating mechanism of improvement**: Table 3 (Section 5.2) shows that augmentations preserving semantics (noise, cutout) fail to improve or degrade performance, while mixup succeeds — confirming that semantic change, not mere perturbation, drives the improvement. Table 2 (labeled "Table 5" in text) demonstrates synergy between mixup and greedy sampling, showing the two components are complementary.

- **Informative controlled experiments validating the diversity hypothesis**: Figure 2 (Section 5.2) directly tests the paper's central thesis by varying outlier class diversity and sample size independently. The monotonic improvement with diversity and limited effect of sample size provide the strongest empirical support for the paper's core claim. These experiments go beyond typical end-to-end comparisons.

## Weaknesses

### Major

- **Unsubstantiated step in the theoretical analysis (ℋ*_div ⊆ ℋ*_aux)** (Section 3.3, line 100). The paper claims: "Because 𝒳_aux ⊂ 𝒳_div holds, the hypotheses performing well on 𝒫_{𝒳_div} also perform well on 𝒫_{𝒳_aux}, giving rise to ℋ*_div ⊂ ℋ*_aux." This is a logical leap that is not generally true. ℋ*_div is defined as the set of minimizers of the total loss on the diverse training distribution (ID data + more diverse OOD data). A hypothesis that minimizes this total loss need not be a minimizer on the original sub-distribution (ID + fewer OOD classes). It could achieve lower total loss by performing better on new OOD classes while performing slightly worse on the original set. The paper provides no justification (e.g., realizability, separability of loss contributions) for this subset relation. The over-parameterized justification on line 66 only applies to ℋ*_ood ⊆ ℋ*_aux, not to this claim. Because this step is the only link between diversity and reduced coverage error (Theorem 2, Theorem 3), the paper's central theoretical guarantee is not established. This is compounded by strong claims in the title ("Guaranteed") and method name ("Provable") that are not fully supported by the analysis as presented.

- **Missing hyperparameter ω and lack of sensitivity analysis for key design choices**: The regularization weight ω in the training objective (Eq. 13, line 176) is never specified, and its selection procedure is not described. The mixup ratio σ=0.5 (Algorithm 1, line 190) determines what fraction of the candidate set consists of truly mixed samples vs. original outliers, but this parameter is neither justified nor ablated. The greedy selection threshold μN=100,000 (for N=400,000) is also not ablated. These parameters likely affect performance, and the paper provides no guidance on how to set them.

### Minor

- **Potential numerical inconsistency in headline claims**: The paper states absolute FPR95 reductions of 4.77% and relative reductions of 31.5% on CIFAR-100 (line 216). This implies the best baseline has FPR95 ≈ 15.14 and ProMix ≈ 10.37. However, the paper does not explicitly state which method is the "best baseline" for each dataset, making it impossible to verify whether the stated reductions match the table values. The CIFAR-10 reduction (0.36 absolute, 14.2% relative) implies a best baseline at ~2.54, which is consistent with typical OE values. The authors should explicitly state which baseline is being compared for each dataset and verify the numbers are consistent.

- **Unspecified computational cost**: The method samples N=400,000 outliers per epoch, applies mixup, computes OOD scores for all candidates, sorts them, and selects 100,000. No runtime comparison with baselines is provided, making it unclear whether the gains come at a significant computational premium.

### Trivial

- None beyond the above.

## Nice-to-Haves

- Empirical validation of Assumption 1: Showing that mixed outliers indeed occupy new semantic regions (e.g., via feature-space visualization or a separate OOD detector) would strengthen the paper's justification for why mixup works beyond simple perturbation.
- Ablation of α (Beta distribution parameter for mixup) to show sensitivity to the mixup interpolation strength.
- Ablation on ω (regularization weight) to show how it affects the trade-off between ID accuracy and OOD detection.

## Removed Points

These points from the reviewers are flagged to be removed. Treat them with caution:
- **"Misreported primary quantitative results (evidential)"** — The harsh critic claims POEM is at 14.14 and ProMix at 10.34 on CIFAR-100, yielding 3.80 absolute and 26.9% relative improvement. However, the table is an image in the PDF and cannot be independently verified from the text. The paper's stated numbers (4.77 absolute, 31.5% relative) are mathematically self-consistent and imply a best baseline at ~15.14. Without being able to read the table, this cannot be confirmed as an error. Demoted to Minor (potential inconsistency).
- **"The bound is a standard domain adaptation bound"** — This is a characterization, not a weakness. Applying domain adaptation theory to OOD detection with auxiliary outliers and connecting it to diversity is a novel contribution.
- **"Inconsistency between hard labels and soft scores"** — The theory uses hard-label hypotheses for the analysis while the method uses soft scores. This theory-practice gap is common in ML papers and does not invalidate either component.
- **Missing related works** — Cannot be evaluated without comprehensive knowledge of all related literature.
- **Reproducibility nitpicks** (undisclosed hyperparameters like training details that are standard) — Removed per hard rules.
- **Generic strawman criticisms** that misunderstand the paper or claim the paper didn't address something it did.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the theoretical gap**: Either provide a rigorous proof of ℋ*_div ⊆ ℋ*_aux (likely requiring additional assumptions) or, more practically, drop the formal theorem claim and present the diversity argument as a well-motivated inductive bias supported by the strong empirical evidence in Figure 2. The paper's empirical contribution (ProMix method + Figure 2 + ablations) is strong enough to stand on its own without an overclaimed theoretical guarantee.
2. **Clarify the numerical claims**: Explicitly state which method is the "best baseline" for each dataset, report exact FPR95 values from Table 1 in the text, and include standard deviations.
3. **Report ω, ablate σ and μ**: Add the regularization weight ω to the experimental setup, and include sensitivity analysis for σ (mixup ratio) and μ (informative fraction).
4. **Add runtime comparison**: Report training time per epoch or total training time vs. baselines to contextualize the computational overhead.

## Score and Decision

Based on my assessment: the paper presents a novel and well-motivated idea with generally solid empirical work (particularly Figure 2 and the ablations). However, the theoretical analysis contains a genuine gap that undermines the "Guaranteed"/"Provable" framing, and several experimental details are missing. The paper would benefit from major revisions to address these issues but has meaningful empirical contributions.

**Score: 5.0**

**Decision: Reject** (but the paper is close to the acceptance threshold; a corrected version addressing the theoretical overclaiming and missing experimental details could merit acceptance)

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>