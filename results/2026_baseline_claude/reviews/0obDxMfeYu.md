Now I have read the full paper. Let me write my review.

---

## Summary

Medix is a two-stage OOD detection framework that exploits unlabeled "in-the-wild" data (a mixture of InD and OOD samples). In Stage 1, a greedy leave-one-out algorithm iteratively flags wild samples whose removal most reduces the L₂ distance between the element-wise median (EWM) of wild gradients and the mean InD gradient; the flagged samples become OOD candidates. In Stage 2, a binary OOD detector is trained on the InD labeled data and the flagged outliers. The paper provides theoretical bounds on inlier and outlier misclassification rates and demonstrates empirical improvements over 20 baselines on CIFAR-10 and CIFAR-100.

## Strengths

- **Empirically strong results**: On CIFAR-10, Medix reduces average FPR95 to 0.80% vs. WOODS's 3.40% — a 4× improvement. On CIFAR-100, the improvement over WOODS is smaller (5.42% vs. 6.74%) but consistent across all five OOD datasets. Results are averaged over five runs with reported standard deviations, adding credibility.

- **Well-motivated gradient-based intuition**: Figure 1 provides a clean, concrete empirical observation — as OOD samples are added to wild data, the EWM-to-InD-mean L₂ distance monotonically increases. This motivates the entire method and the stopping criterion, and the logic connecting motivation to algorithm is clear.

- **Two-sided theoretical guarantee**: Theorems 4.1 and 4.2 bound both inlier misclassification (InD samples flagged as OOD) and outlier misclassification (OOD samples retained as InD), providing a complete picture. The distinction between contamination, concentration, and separation effects is a useful decomposition.

- **Sub-Gaussian assumption is empirically validated**: The paper supports the key sub-Gaussian assumption with a gradient histogram (bell-shaped, light-tailed) and a Q-Q plot in Figure 4, which is good practice.

## Weaknesses

### Fatal
None.

### Major

1. **Theoretical bounds are vacuous at the experimental setting (π = 0.5)**. The default experimental contamination ratio is π = 0.5. At this value, Theorem 4.1's contamination term equals π / [2(1 − π)] = 0.5, meaning the inlier misclassification bound is ERR\_in ≤ 0.5 + (small concentration term) ≈ 0.5. Similarly, Theorem 4.2's contamination term is (1 − π) / (2π) = 0.5 at π = 0.5. Both bounds are thus near-vacuous (≈ 0.5 for binary classification) at precisely the regime tested empirically. The paper claims these bounds demonstrate Medix "achieves a low error rate," but the actual outlier extraction error of 12.5% (Figure 2) is far better than what the theory guarantees, indicating the theory is very loose. The theoretical contribution is significantly weakened by this gap between theory and practice at the chosen operating point.

2. **CONJ and DRL baselines are promised but absent from main results**. Section 5.1 explicitly states: "we included more recent baselines, including CONJ (Peng et al., 2024) and DRL (Zhang et al., 2024), to provide a more thorough evaluation." Neither appears in Table 1 or Table 2. The contribution count C3 claims "comparing its performance against 20 competitive baselines," yet only 13 baselines are visible in the main tables. It is impossible to verify whether Medix outperforms these recent methods without seeing their numbers.

3. **Algorithm 1 stopping criterion has a logical error**. Line 2 states `while t ≤ T or |δ_max| > ε`. With OR logic, the loop continues as long as *either* condition is true, meaning it always runs for at least T iterations regardless of convergence, and it never terminates early. The correct semantic for "run up to T iterations, stop early if convergence is reached" requires AND, not OR. This is a correctness issue in the pseudocode.

### Minor

1. **Computational complexity is underaddressed**. The paper acknowledges the leave-one-out approach is "computationally prohibitive" but defers analysis to Appendix A.6. The greedy algorithm as written requires O(|S|) EWM computations per iteration, each O(d·|S|), yielding O(d·|S|²) per round. For large wild datasets and high-dimensional gradients (penultimate layer of WideResNet-40-2), this is expensive. The main paper should quantify this.

2. **Data asymmetry in comparison**. Medix (and WOODS) train the InD classifier on 25,000 CIFAR samples, while all InD-only baselines use the full 50,000. The paper acknowledges this in a single sentence but does not assess how much of the gap between Medix and InD-only baselines is attributable to the outlier training vs. the data handicap.

3. **11 InD-OOD pairs claimed but only 10 described**. The abstract states "eleven InD-OOD pairs" (C3), but the tables show 5 OOD datasets × 2 InD datasets = 10 pairs.

### Trivial

- EWM is rotation-dependent (coordinate-wise median changes under rotation of the gradient space). This is not discussed.

## Nice-to-Haves

- Include CONJ and DRL results in the main tables (or clearly state they were moved to appendix and why).
- Report results at multiple π values (e.g., 0.1, 0.3, 0.5) in the main paper to demonstrate the method's behavior as the theoretical bounds tighten or loosen.
- A tighter theoretical analysis valid at π = 0.5 (or relying on the empirical observation that actual error is far lower than the bound) would strengthen the theory-practice story.

## Novel Insights

The use of element-wise median of gradients (computed at a model trained on InD data) as a robustness mechanism for separating InD and OOD data in a mixed unlabeled set is a genuinely new angle. Prior work (WOODS, Du et al. 2024a) used energy-based or threshold-based filtering; median-based filtering offers a different robustness property (breakdown point ≈ 50%) that is theoretically grounded even if the bounds are not tight at the operating point. The empirical observation that EWM gradient distance increases monotonically with OOD contamination (Figure 1) is clean and practically useful as a diagnostic.

## Suggestions

- Fix the stopping criterion in Algorithm 1 (change OR to AND).
- Either include CONJ/DRL in the main tables or explicitly state they are in the appendix with a clear reason.
- Explicitly note that the theoretical bounds are loose at π = 0.5 and discuss why the practical error rate is far better — this would demonstrate deeper understanding rather than obscure the gap.
- Add a small sensitivity study on π ∈ {0.1, 0.3, 0.5} in the main paper to show how performance degrades as OOD proportion decreases (and as the contamination term in Theorem 4.1 shrinks toward zero).

## Score and Decision

The method is novel and the empirical gains on CIFAR-10 are substantial. However, the theoretical guarantees — a central claimed contribution — are nearly vacuous at the experimentally-used π = 0.5, creating a significant gap between what the theory promises and what is actually demonstrated. The missing baselines that were explicitly promised in Section 5.1 raise fairness-of-comparison concerns. The algorithm pseudocode has a logical error in its stopping condition. These are issues that should be addressed before acceptance.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>