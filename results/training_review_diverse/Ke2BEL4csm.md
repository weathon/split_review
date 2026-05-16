Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes NCL-SR, the first non-contrastive learning (NCL) framework for sequential recommendation (SR). It eliminates negative samples by learning from only positive pairs, and introduces a differential-privacy-based augmentation method that replaces items with synonyms via the exponential mechanism to generate diverse yet preference-preserving positive samples. The framework optimizes alignment and uniformity losses derived from matrix information theory. Experiments on six datasets show substantial improvements over existing SR and CL-based methods.

## Strengths

- **First NCL framework for SR with a novel DP-based augmentation design.** The paper identifies a genuine gap — NCL is underexplored in recommendation — and proposes a principled way to generate positive pairs via the exponential mechanism. The item-level complexity reduction (from O(k^l) to O(k·l), Section 4.1) makes the approach computationally practical.

- **Consistent and significant empirical gains across multiple datasets.** NCL-SR achieves average improvements of ~12% over SR baselines (Table 1) and ~12.5% over CL-based methods (Table 2), with gains reaching 33.2% on the sparsest dataset (Sports). These results hold across six diverse domains, demonstrating robustness.

- **Informative ablation study revealing that alignment may be more important than uniformity in SR.** Table 3 shows that removing alignment degrades performance more (6.1% Recall@10 drop) than removing uniformity (4.0% drop). This insight contrasts with typical CL assumptions and provides a useful direction for future SR research.

- **Thorough ablative decomposition.** The ablation (Table 3) systematically isolates the contributions of uniformity loss, alignment loss, DP augmentation, and the contrastive-vs-non-contrastive choice, providing clear evidence that each component contributes.

## Weaknesses

### Fatal
None.

### Major

**1. Disconnect between theoretical framing and actual implementation (representation-level vs. input-level augmentation).**  
Definition 1 and Theorem 1 are framed in terms of feeding an augmented user profile *x'* (an item sequence) into a recommendation mechanism *M*. However, the method (Eq. 6) produces a continuous weighted-sum representation *z<sub>X'</sub>* = Σ *P<sub>x'</sub>·f(x')* rather than a concrete augmented profile. The paper states (lines 109–110) that "expected output stability" allows generating an expected augmented profile, but it never explains how the preference-preservation guarantee transfers from the individual candidate profiles *x'* to the weighted combination *z<sub>X'</sub>*. Post-processing preserves DP, but preference preservation is not automatically inherited via post-processing. Since the theory and practice operate at different levels of representation, the core theoretical claim (that the augmentation "provably" preserves preferences for the actual method) is not established. The authors should either revise the theory to match the representation-level operation or explain the missing link.

**2. Theorem 1's margin condition is unverified and likely restrictive.**  
Theorem 1 requires that the expected score for the ground-truth item exceed the second-largest runner-up by a multiplicative factor of *e<sup>2ε</sup>*. This is a strong condition, especially for sparse recommendation data where score margins are often small. The paper provides no empirical check of whether this condition holds for a meaningful fraction of users in any dataset, nor does it discuss what happens when the condition is violated. The proof is simply referenced ("adapted from Wang et al.") without even a sketch. Since preference preservation is the paper's central motivation for using DP, the theoretical contribution remains a "if the condition holds" statement whose practical relevance is unverified.

**3. DP composition is not addressed.**  
The paper applies the exponential mechanism independently to each of *l* items in a user's history with privacy parameter ε (line 102: "re-define ... at item-level"). Under standard DP composition, the total privacy budget is at least (*l·ε*)-DP, not ε-DP. With typical sequence lengths of 10–20 items and ε moderate (e.g., 1), the composed budget can be large enough to weaken any meaningful privacy guarantee. The paper merely states it "remains DP" (line 109) without specifying the total budget or acknowledging composition. While the DP augmentation is used only as a training-time data augmentation (not for releasing a private model), the absence of any composition accounting is a technical gap in a method whose name and narrative center on differential privacy.

### Minor

**4. No efficiency measurements despite efficiency being a core motivation.**  
The introduction and abstract repeatedly motivate NCL by the "high computational costs" and "computational overhead" of negative samples in CL. Yet the paper never reports training time, memory usage, or any efficiency metric. The proposed DP augmentation itself has non-trivial overhead (computing synonym sets via all-item similarity, evaluating the exponential mechanism's scoring function). Without any empirical efficiency comparison against CL baselines, this motivational claim is asserted but unsupported.

**5. Non-standard evaluation protocol limits generalizability claims.**  
The paper uses a 2:2:6 train/validation/test split (only 20% training data), which the authors justify as a cold-start simulation with citations (Wu et al. 2024, Qian et al. 2020, Wang et al. 2022a, Lin et al. 2025). However, this deviates from standard SR protocols (leave-one-out, temporal splits), and the baselines may have been tuned for those standard setups. The paper does not report results under any standard protocol, making it unclear whether the large gains reflect an advantage specific to this extreme data-sparse regime or generalize to typical SR settings.

**6. No error bars or statistical significance.**  
All main results (Tables 1–2) are reported as point estimates without variance or significance tests. Given the very large claimed improvements, confidence intervals from multiple runs would substantially increase credibility.

**7. Key hyperparameters undisclosed.**  
The paper does not report the value of *k* (size of synonym sets), *γ* (in Eq. 10), or the exact *λ₁, λ₂* values used in the main experiments (the sensitivity analysis explores ranges but doesn't give the chosen settings). These are not trivial implementation details — they control the core behavior of the method.

**8. Ablation description is vague.**  
The ablation replaces DP augmentation with operations "randomly sampled from the CL-based baselines" (line 191) without specifying which operations (crop, mask, swap, substitution, insertion?) or at what strength. This makes the ablation difficult to interpret or reproduce.

**9. Sensitivity analysis lacks dataset labels.**  
Figure 2 does not specify which dataset's results are shown, and no conclusion is drawn beyond "different optimal configurations for different datasets."

**10. No limitations section.**  
The paper does not discuss any limitations of the proposed approach (e.g., synonym set staleness during training, the margin condition's restrictiveness, the composition issue).

### Trivial

- Definition 1 uses "expected" without formalizing the expectation; it is ambiguous whether this is over the randomness of the mechanism or the data distribution.
- The paper does not clarify whether synonym sets are recomputed as the recommender *f* changes during training; if not, they are based on an initial, potentially suboptimal encoder.

## Nice-to-Haves

- Additional results under a standard leave-one-out evaluation protocol to ground claims in the existing literature.
- Error bars (3+ runs) for the main results.
- Empirical verification of Theorem 1's margin condition on at least one dataset (distribution of score margins, fraction of users satisfying the condition).

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The paper does not discuss the existence of non-contrastive methods for recommendation that use alternative mechanisms."* — Per rule: Do NOT mention missing related works; the paper cites BYOL, SimSiam, Barlow Twins, and MEC, which is sufficient context for a new-method paper.
- *"The paper omits crucial hyperparameters ... training details."* — Partially addressed by the sensitivity analysis (Figure 2 explores λ₁, λ₂), and many training details are standard. The reviewer also groups this with generic reproducibility complaints. The remaining substantive missing parameters (*k*, *γ*) are kept in Minor #7 above.
- *"The paper does not specify how f(x) is computed (e.g., mean pooling, transformer pooling)."* — The paper states it uses E5 (e5-base-v2); the pooling mechanism for E5 is a standard implementation detail.
- *"The paper should also cover additional domains/tasks."* — Scope creep: the paper already covers six datasets across diverse domains.
- *Strength from Strength Finder about "theoretically grounded preference-preserving augmentation with provable guarantees."* — Conflicts with verified Major weaknesses #1 and #2 (theory–implementation disconnect and unverified margin condition), which undermine the provable-guarantee claim. Dropped per rule.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful critiques but do not identify novel technical insights missing from the paper itself.

## Suggestions

1. **Fix the theory–implementation gap.** Either re-frame Definition 1 and Theorem 1 to match the representation-level operation actually used, or (if there is an argument via post-processing) make that argument explicit and rigorous.
2. **Empirically verify Theorem 1's condition** on at least one dataset, showing the distribution of score margins. If the condition rarely holds, re-frame the DP augmentation as a well-motivated heuristic rather than a provable guarantee.
3. **Account for DP composition.** State the total privacy budget explicitly (even if large) and discuss whether the augmentation can meaningfully be called "differentially private" in this setting.
4. **Add efficiency measurements** (training time per epoch, peak memory) comparing NCL-SR against the strongest CL baseline.
5. **Report results on a standard leave-one-out split** to complement the cold-start protocol.
6. **Disclose missing hyperparameters** (*k*, *γ*, exact *λ₁/λ₂* values) and label the dataset in Figure 2.

## Score and Decision

This paper introduces a novel idea — combining DP-based augmentation with non-contrastive learning for SR — and demonstrates strong empirical results. However, it has a structural gap between its theoretical framing and its actual implementation (Major #1), an unverified theoretical condition that undermines the provable-guarantee claim (Major #2), and an unaddressed DP composition issue (Major #3). These are not fatal individually, but together they mean the paper's central claims are not adequately supported in the current form. The empirical results are promising, but the evaluation uses a non-standard protocol without error bars, and the computational motivation is unvalidated. A major revision addressing the theory–implementation mismatch and adding missing empirical analyses could make this a strong paper.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>