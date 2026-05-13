Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes PLNL, a method for complementary label learning (CLL) that decomposes the learning problem into two subtasks: positive label guessing (PLG) for highly-confident instances and negative label enhancement (NLE) for moderately/under-confident instances. PLG assigns pseudo-labels to instances whose predictions are stable and high-confidence across two augmented views, while NLE uses k-nearest-neighbor label frequency voting in the output space to progressively augment the negative label sets of less certain instances. The paper presents theoretical bounds on generalization error and PLG/NLE error rates, and reports strong empirical results, most notably a 20.29% accuracy improvement on STL-10 over prior CLL methods.

## Strengths

- **Novel decomposition of CLL into PLG and NLE** is conceptually clean and well-motivated. Unlike prior URE-based and FL-based CLL methods, the paper leverages output space information to recover both positive and negative labels. The insight that moderately-confident and under-confident instances can contribute supervision through negative label enhancement (rather than being discarded) is genuinely novel for CLL (Section 3).

- **Instance-aware self-adaptive threshold** (Eq. 8) is a principled mechanism that initializes at 1/K and adapts via momentum-averaged historical confidence, addressing confirmation bias more carefully than fixed global thresholds (Section 3.1).

- **Strong empirical results across multiple datasets and both single/multiple CLL settings** with consistent improvements over prior CLL methods. The 6.45% improvement on CIFAR-100 (MCLL) is particularly notable given the difficulty of that benchmark. Figure 2 provides useful dynamic analysis showing PLG maintains high precision alongside growing selected ratio, and NLE precision stays above 0.99 throughout training (Section 6).

- **Unified framework connecting pseudo-labeling to negative label recovery** (Section 4) provides a useful conceptual lens for comparing methods via selected ratio η and average enhanced negative label set size s̄, with empirical validation in Figure 3.

## Weaknesses

### Fatal
None

### Major

- **The Remark following Theorem 1 overstates what the theorem proves about consistency.** The Remark claims that "as N→∞, ε₁→0, ε₂→0, the empirical risk minimizer converges to the true risk minimizer with high probability." However, examining the bound in Eq. (20), as N→∞ the Rademacher and finite-sample terms vanish, but the residual term 2(1−(1−ε)/(K−s̄))B remains. As ε₁,ε₂→0 (so ε→0), this becomes 2(1−1/(K−s̄))B, which vanishes only if s̄→K−1 (i.e., nearly all labels are recovered as negative). The paper never proves that training dynamics drive s̄→K−1; it only observes this empirically in Figure 2c for one dataset. The Remark should state that convergence requires both ε→0 and s̄→K−1, or the consistency claim should be properly qualified. This is a major issue because the abstract and introduction both claim the method can "construct a classifier consistent with that learned by clean full labels" — a central claim that the theorem does not fully establish.

- **No ablation study isolating PLG and NLE components, or separating warm-up contributions.** PLNL uses SCL-LOG for 20 epochs of warm-up (Section 3.1), and the two-view augmentation architecture is a non-trivial design choice. The paper reports no ablation of PLG-only vs. NLE-only vs. PLG+NLE, nor any experiment showing PLNL without warm-up vs. SCL-LOG with warm-up+two-view architecture but without PLG/NLE. Without these ablations, it is impossible to determine how much of the empirical gains come from the proposed PLG/NLE methodology versus from the initialization and architectural choices. This is especially concerning for the 20.29% STL-10 improvement, which is unusually large and demands attribution clarity.

### Minor

- **Theorem 2 provides an extremely loose bound.** ε₁ ≤ (K−1−sᵢ)ψ where ψ ∈ (0, 1/(K−1−sᵢ)) guarantees only ε₁ < 1, which is trivially true for any error rate. While this does technically constitute an "upper bound," it provides no meaningful quantitative information about the actual PLG error. The theorem would benefit from tightened assumptions or at minimum an acknowledgment of the looseness.

- **Assumption 1 is central to NLE but never validated empirically.** The assumption requires αₖ (probability the true label appears in neighbors' CL sets) to be small and βₖ (probability a negative label appears in neighbors' CL sets) to be large. Theorem 3's bound depends entirely on these quantities. No experiment estimates αₖ and βₖ on any benchmark dataset, and Theorem 3's bound is never numerically evaluated, making it impossible to assess whether the bound is tight or vacuous in practice.

- **The comparison with FixMatch and FreeMatch** (Figure 3) is of limited relevance because these SSL methods are not designed to exploit complementary label information — they operate under a different learning paradigm. The comparison is interesting as a reference point but should not be framed as a head-to-head evaluation.

### Trivial

- The τᵢ formulas for sets U and M (Section 3.3) contain apparent extraction artifacts that make the exact expressions hard to parse.

## Nice-to-Haves

- Sensitivity analysis for the hyperparameter α in the self-adaptive threshold (Eq. 8) and the divisor 10 / linear growth schedule in τᵢ formulas would strengthen confidence in robustness.
- Per-class error analysis (confusion matrices) of PLG and NLE would illuminate failure modes.
- An explanation for why STL-10 shows a dramatically larger improvement (20.29%) than other datasets (2–3% on CIFAR-10) would clarify the conditions under which PLNL is most effective.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Theorem 2 is vacuous" (Harsh Critic Critical Issue 1):** While Theorem 2 is extremely loose, calling it "vacuous" overstates the case. It is a valid but trivial bound. Downgraded to Minor rather than Fatal.

- **"Theorem 1 does not yield consistency" (Harsh Critic Critical Issue 1):** This is partially correct — the bound does not go to zero without s̄→K−1. However, the Harsh Critic's claim that "the Remark's assertion...is false as stated" is too strong; the Remark is incomplete/oversimplified rather than outright false, since the convergence can occur if both ε→0 and s̄→K−1 simultaneously. The real issue is the overstatement, not that the theory is fundamentally wrong. Upgraded from Fatal to Major.

- **"Memory bank overhead not discussed" (Harsh Critic §3.1):** This is a minor implementation detail concern, not a substantive issue. Removed as nitpick about reproducibility/implementation details.

- **"O(N²) cost of k-NN computation" (Harsh Critic §3.3):** k-NN on outputs is cheap (only K-dimensional outputs), so O(N²) is manageable and standard in practice. Weakened to trivial.

- **"3 seeds is minimal for reliable variance estimation" (Harsh Critic §6):** Standard practice in this field; not a substantive weakness.

- **"Unified framework is a trivial observation" (Harsh Critic §4):** This is an opinion; the reframing provides useful metrics (η, s̄) and is empirically validated in Figure 3. Removed.

- **Strength Finder's "Theoretical consistency guarantees" strength**: The theoretical contribution is undermined by the looseness of Theorem 2 and the gap between Theorem 1 and the Remark's consistency claim. Moved to a qualified mention rather than a standalone strength.

- **Strength Finder's "Three-tier confidence-based instance selection" as a standalone strength**: The selection criteria are reasonable but the three-tier split and two-view architecture are design choices whose individual contributions are not ablated. Weakened.

## Novel Insights

The most insightful observation across the reviews is the precise gap in the consistency argument: Theorem 1's bound in Eq. (20) reveals that convergence to the clean-label classifier requires not only that pseudo-labeling errors ε→0, but also that the average enhanced negative label set size s̄→K−1. The paper implicitly assumes this happens through training dynamics but never proves it, creating a disconnect between the theoretical framework and the stated claims. The empirical evidence in Figure 2c suggests s̄ does grow substantially during training, but this is observed only for CIFAR-100 MCLL and is not established as a general property. Closing this gap — either by proving s̄→K−1 under certain conditions or by properly qualifying the consistency statement — would substantially strengthen the paper's theoretical contribution.

## Suggestions

- **Qualify the consistency claim**: Revise the abstract and Remark to state that consistency requires both ε→0 and s̄→K−1, and note that s̄→K−1 is observed empirically but not proven theoretically.
- **Add component ablations**: Report PLG-only, NLE-only, and PLG+NLE results. Also compare PLNL with and without the SCL-LOG warm-up to isolate warm-up contribution.
- **Validate Assumption 1**: Estimate αₖ and βₖ from the trained model's k-NN output space on each dataset and report whether the required ordering holds.

## Score and Decision

The paper makes a genuine and novel contribution by decomposing CLL into PLG and NLE, a conceptually clean framework that leverages output-space information in a way prior methods do not. Empirical results are consistently strong across five benchmarks. However, the theoretical claims about consistency are overstated relative to what the theorems deliver (the Remark omits a necessary condition), Theorem 2 provides only a trivial bound, and the absence of ablation studies makes it difficult to attribute empirical gains to the proposed PLG/NLE methodology specifically. These issues, while not fatal, significantly weaken the paper's ability to support its central claims about why the method works and whether its theoretical guarantees are meaningful.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>