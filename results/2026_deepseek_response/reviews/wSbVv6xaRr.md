Now I have strong calibration anchors. Let me write the final consolidated review.

**Round 1 Bracketing:** The paper is clearly above the <3.5 band (FedADM, Compressed Decentralized Learning — weak papers with large gaps) and clearly below the >7.5 band (highly polished, well-evaluated papers). Bracketed range: 4.0–6.5.

**Round 2 Narrowing:** Compared within the (4.0, 6.0) and (5.5, 7.0) bands, the paper is stronger than BiCompFL (4.80, limited novelty) but weaker than DeComFL (6.25, cleaner presentation and larger-scale experiments). It is comparable to LASER (5.83, similar mix of solid theory + limited evaluation). The abstract error and algorithm inconsistency prevents it from reaching the Accept-level papers.

**Final score: 5.0**. The paper has a genuinely novel core idea and solid theory but is held back by a factual error in the abstract (O(1/K) vs O(1/√K)), an algorithm pseudocode inconsistency, and limited experimental scope.

---

## Summary

FedMPDD proposes a federated learning algorithm that reduces per-client uplink communication from O(d) to O(m) by encoding gradients through directional derivatives along m random Rademacher vectors, transmitting only the resulting scalars and a seed. The server reconstructs the gradient estimate via the same random vectors. The method provides inherent privacy against gradient inversion attacks through the nullspace of the low-rank projection. Theoretical convergence (O(1/√K)) and privacy bounds are provided, with experiments on MNIST and CIFAR-10 showing communication savings and privacy protection compared to baselines.

## Strengths

1. **Novel joint treatment of communication and privacy via projected directional derivatives.** The multi-projected directional derivative mechanism simultaneously compresses gradients (to O(m) scalars per client per round) and provides inherent privacy via rank-deficiency. Lemma 1 shows the expected relative gradient reconstruction error is (d-1)/m, independent of gradient magnitude — unlike LDP, where protection varies with gradient size (Remark 5). Tables 1 and 2 empirically confirm FedMPDD achieves low SSIM (<0.22) under gradient inversion attacks while staying within tight communication budgets, whereas compression-only baselines (QSGD, Top-k, lp-proj) leak substantial information (SSIM ≥0.74).

2. **Convergence rate matching FedSGD for non-convex objectives.** Theorem 2 establishes O(1/√K) convergence with m = O(log(d/δ)/ε²) projections, overcoming the dimension-dependent O(d/√K) convergence of the single-projection variant. The Johnson–Lindenstrauss Lemma provides the key norm-preservation bound.

3. **Consistent privacy independent of gradient magnitude.** Unlike LDP where relative reconstruction error is proportional to 1/‖g_i‖² (large gradients poorly protected, small gradients overwhelmed by noise), Lemma 1's bound (d-1)/m is gradient-magnitude-independent. Figure 1 shows SSIM stays below 0.04 across all training epochs, confirming stable practical privacy.

4. **Strong empirical results under constrained budgets.** On CIFAR-10 (Table 2), FedMPDD (m=600) achieves 40.8% test accuracy under a 0.9 GB budget while baselines range from 12.9%–38.1%. To reach 60% target accuracy, FedMPDD uses 1.32 GB (>356× reduction vs. FedSGD) with SSIM ≤0.14, while compression-only baselines require 1.8–2.3 GB and leak information (SSIM ≥0.74).

5. **Tunable privacy-communication-accuracy trade-off** controlled by m, supported by theoretical bounds (Lemmas 1, 2) and the multi-round composition bound (T·m < d, Remark 2).

## Weaknesses

### Fatal
None.

### Major

1. **Abstract overclaims convergence rate.** The abstract states FedMPDD "converges at a rate of O(1/K), matching the performance of FedSGD." However, Theorem 2 (Equation 5) proves O(1/√K) — the correct rate for non-convex SGD. The introduction's bullet points correctly state O(1/√K). This is a factual error in the abstract that overstates the convergence rate by an order of magnitude and must be corrected.

2. **Algorithm pseudocode contradicts the claimed efficient implementation.** Algorithm 2 (line 6) explicitly requires each client to "Compute local stochastic gradient g_i(x_k)" — the full O(d)-dimensional gradient — before the directional-derivative loop. A reader implementing Algorithm 2 verbatim incurs O(d) computation per round. Remark 1 discusses a JVP-based approach that avoids computing the full gradient, but this is presented as an alternative, not reflected in the pseudocode. This inconsistency undermines reproducibility and clarity about the actual computational profile.

3. **Limited experimental scope relative to claims.** The paper claims FedMPDD is "suitable for large-scale problems" but evaluates only MNIST (LeNet, ~62K params) and CIFAR-10 (simple CNN, ~300K params). No results on larger datasets (e.g., CIFAR-100, ImageNet) or architectures (e.g., ResNet-50) are provided. Additionally, no standard deviations or multiple-seed results are reported, making it impossible to assess the variance of the method given the stochasticity of random projections.

### Minor

1. **CIFAR-10 convergence curves not shown in main text.** For MNIST, Figure 3 provides full accuracy/loss curves vs. rounds and vs. bits. For CIFAR-10, results are only summarized in Table 2. Full convergence curves would help assess whether FedMPDD eventually matches the final accuracy of FedSGD or other baselines without communication limits.

2. **Non-IID results deferred to appendix.** The experimental setup mentions testing on non-IID data, but no non-IID results appear in the main text. Given that non-IID distributions are the norm in FL and can exacerbate variance issues for projection-based methods, this is a notable omission.

3. **Privacy guarantees are reconstruction-error bounds, not a formal DP guarantee, with unverified dependencies.** Lemmas 1 and 2 provide meaningful reconstruction-error bounds, but Lemma 2's bound depends on L_v(x), a Lipschitz constant that may be large for deep networks and is not controlled by the method. The paper would benefit from explicitly clarifying that the protection is against reconstruction attacks rather than a formal DP framework, to avoid potential misinterpretation.

4. **No experimental comparison with methods jointly addressing compression and DP.** The paper cites Agarwal et al. 2018 (CP-SGD) in related work and mentions methods combining DP with compression, but does not compare against them experimentally. Such comparisons would better contextualize FedMPDD's joint privacy-communication trade-off.

5. **Practical m vs. theoretical m gap.** The theory requires m = O(log(d)/ε²), but experiments use m=400–800 for LeNet (~62K params) where log(d) ≈ 11. The paper acknowledges m "grow[s] slightly with d" but does not discuss the gap between the theoretical logarithmic requirement and empirical choices.

### Trivial
None.

## Nice-to-Haves

- Systematic sweep of m (e.g., from 1 to 2d) on a small model to illustrate the privacy-accuracy-communication trade-off more completely.
- Reporting the number of rounds (not just bytes) needed to reach target accuracy, since round count affects latency.
- Including peak accuracy reached by each method without communication limits to confirm FedMPDD does not harm final performance.

## Removed Points

1. **"Static projection" characterization of sketched methods** (Harsh Critic): The critic claims the paper's characterization of sketched methods as using "static projection" is misleading because some redraw per round. However, Count-Sketch and most sketch-based FL methods use a fixed hash/sign matrix throughout training. The paper's characterization is substantively accurate. *Removed.*

2. **Lemma 2 bound "involves ‖g_i‖²" diminishing uniformity claim** (Harsh Critic): The critic claims this undermines the "uniform privacy" claim. However, the uniformity claim is about gradient reconstruction error (Lemma 1), not data reconstruction error (Lemma 2). Lemma 1's bound is indeed gradient-magnitude-independent. The critic conflates the two lemmas. *Removed.*

3. **Generic strength finder items** (e.g., "this paper addressed an important problem"): Removed as lacking specific evidence tied to the paper's content. *Removed.*

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the abstract's convergence rate** from O(1/K) to O(1/√K) to match Theorem 2.
2. **Revise Algorithm 2** to either use JVP-based directional derivatives directly (removing the "compute full gradient" step) or clearly separate the efficient variant as the primary method.
3. **Add error bars / multiple-seed results** to all experiments.
4. **Include CIFAR-10 convergence curves** (accuracy vs. rounds and vs. bits) in the main text.
5. **Add larger-scale experiments** (e.g., ResNet on CIFAR-100) to substantiate scalability claims.
6. **Include comparison with a joint compression+DP method** (e.g., CP-SGD) to better contextualize the privacy-communication trade-off.
7. **Clarify privacy framing**: explicitly state the protection is against reconstruction attacks, not a formal DP guarantee.

## Score and Decision

**Calibration Anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| FedComLoc (0jmFRA64Vw) | 3.00 | R1 (low) | Much weaker; limited novelty, poor experiments |
| Bidirectional CE (Jl0aEFrp11) | 2.75 | R1 (low) | Much weaker; poor presentation |
| BiCompFL (ogIFNo2bQw) | 4.80 | R1 (mid) | Weaker; limited novelty (extension of prior work), while current paper has genuinely novel idea |
| Improving Accel FL (9TSv6ZVhvN) | 4.67 | R1 (mid) | Comparable; theory-heavy, limited experiments like current paper, but fewer errors |
| Per-sample clipping (BdPvGRvoBC) | 6.00 | R1 (mid) | Stronger; cleaner presentation, accepted at ICLR |
| LASER (TCJbcjS0c2) | 5.83 | R2 (4-6) | Comparable; solid theory + limited experiments, mixed reviews |
| DeComFL (omrLHFzC37) | 6.25 | R2 (5.5-7) | Stronger; cleaner presentation, larger-scale experiments (OPT-1.3B) |
| FedSMU (ZU42Wrcqfm) | 5.75 | R2 (4-6) | Comparable; similar experimental scope, but fewer errors |
| Collaborative Compressors (J7hIz9GXKq) | 5.25 | R2 (4-6) | Comparable; more limited in scope |

**Round 1 Bracket:** [4.0, 6.5]. The paper is clearly stronger than weak 3-range papers but substantially weaker than 7+ papers.

**Round 2 Narrowing:** Compared to DeComFL (6.25), the most conceptually similar paper, the current paper has a more principled first-order approach but is held back by the abstract error, algorithm pseudocode inconsistency, and smaller-scale experiments. Compared to FedSMU (5.75) and LASER (5.83), the current paper has comparable quality but with a clear factual error that those papers lack.

**Final Score:** 5.0 — The paper proposes a genuinely novel approach with solid theoretical foundations, but the abstract's convergence-rate overclaim and the algorithm pseudocode inconsistency are significant issues that must be addressed, and the experimental evaluation needs broadening and tightening.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>