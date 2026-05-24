Now I have enough information for calibration. Let me write the consolidated review.

## Summary

The paper proposes FedMPDD, a federated learning algorithm that encodes each client's gradient by computing its directional derivatives along multiple random Rademacher vectors (m ≪ d). This compresses uplink communication from O(d) to O(m) scalars per client per round. The server reconstructs a gradient estimate using the same random vectors, and the rank deficiency of the low-rank projection provides inherent protection against gradient inversion attacks. The paper claims an O(1/√K) convergence rate matching FedSGD with m = O(log d) projections, and provides empirical results showing up to 356× communication reduction with SSIM consistently below 0.22 under gradient inversion attacks.

## Strengths

- **Large measured communication reduction (356×) with preserved accuracy on real benchmarks**: Table 2 shows that on CIFAR-10 (IID), FedMPDD with m=600 (0.2% of d) requires only 1.32 GB of total uplink to reach 60% test accuracy, versus 471.96 GB for FedSGD — a 356× reduction. FedSGD and its Laplace-noise variants exceed the 0.9 GB budget in the first iteration, while FedMPDD stays within budget and achieves competitive accuracy (40.84% vs 38.11% for Top-k, 34.72% for lp-proj).

- **Simultaneous communication reduction and privacy protection validated across multiple attack methods**: Table 2 shows SSIM ≤ 0.22 for FedMPDD, whereas compression-only baselines (lp-proj, Top-k, SA-FedLora) all show SSIM ≥ 0.74, indicating substantial data leakage. Figure 1 shows SSIM consistently below 0.04 over 100 epochs on LeNet. Two different attack methods (Yu et al., 2025 and DLG) are tested, and the privacy-communication trade-off is systematically varied via the parameter m.

- **Core algorithmic idea is novel and well-motivated**: Using multi-projected directional derivatives where each client independently samples new i.i.d. Rademacher vectors every round (as opposed to fixed-subspace sketches) yields an unbiased gradient estimator (E[ĝ_i] = g_i). The paper explicitly identifies and characterizes the dimension-dependent convergence problem of the single-projection variant (FedPDD), which has convergence rate O(d/√K), and proposes multi-projection averaging as a principled fix.

- **Formal reconstruction error bound with clear trade-off**: Lemma 1 provides a clean expression for the expected relative gradient reconstruction error: (d-1)/m. This is independent of gradient magnitude, unlike LDP-based approaches where protection depends on ||g_i||². Remark 2 gives a multi-round composition bound (T × m < d) guaranteeing that unique gradient recovery is impossible.

## Weaknesses

### Major

- **The convergence analysis conflates a high-probability JL norm-preservation bound with the variance bound required for SGD convergence — the central theoretical claim is unsupported.** Lemma 1 gives the expected relative squared error as (d-1)/m, implying the variance of the estimator scales as O(d/m)·||g||². Theorem 2 claims O(1/√K) convergence with m = O(log(d/δ)/ε²) and an error term O(εG²/√K). However, the expected squared norm of the estimator (which is what enters standard SGD convergence bounds) is (1 + (d-1)/m)||g||² — for m = O(log d), this is O(d/log d), far larger than (1+ε)²||g||² for any reasonable ε. The JL lemma applied to the operator (1/m)UU^T gives a high-probability bound on the norm of the estimate for a single draw, but the *expected squared norm* that governs SGD convergence is not controlled by this bound. The paper never explains how the JL norm-preservation guarantee (which governs a single draw's norm with probability 1-δ) bridges to the expectation bound that the convergence analysis requires. Furthermore, the "operator-norm JL lemma" (Matoušek, 2008) cited by the paper requires m = Ω(d/ε²) for operator-norm bounds, not m = O(log d/ε²) as claimed. A convergence rate of O(1/√K) with m = O(log d) is inconsistent with the paper's own Lemma 1. This is a structural error that undermines the paper's primary theoretical contribution.

- **The privacy analysis, while providing reconstruction error lower bounds, does not establish a formal privacy guarantee and overclaims in several places.** Lemma 2's lower bound on data reconstruction error depends on the Lipschitz constant L_v(x), which is problem-specific and not quantified in the paper. The claim of "uniform privacy" (Remark 3, referenced in the introduction) — that protection is independent of gradient magnitude — holds for the *relative* reconstruction error but does not constitute a formal privacy definition comparable to differential privacy. The multi-round composition bound (Remark 2, T × m < d) is a condition on gradient recovery, not data recovery, and its derivation from the earlier lemmas is not shown. The paper uses the term "inherent privacy" without formally defining what it means, and the empirical SSIM results, while suggestive, do not constitute a rigorous privacy guarantee. A comparison against standard DP baselines under equivalent privacy budgets would substantially strengthen the evaluation.

- **The empirical comparison omits methods that jointly address communication efficiency and privacy.** The paper compares against lp-proj, Top-k, SA-FedLora, and QSGD — all compression-only methods not designed for privacy — and unsurprisingly finds they have high SSIM. It also compares against LDP (Laplace noise), but only at a few fixed noise levels without tuning to match a desired privacy budget. A proper evaluation would include methods that simultaneously target compression and privacy (e.g., Amiri et al., 2021 — compressive differentially private FL, or Agarwal et al., 2018 — CPSGD, which the paper cites in related work) and present a Pareto frontier of accuracy vs. communication vs. privacy (e.g., SSIM or ε-DP budget) across a range of operating points for all methods.

### Minor

- **The abstract claims "convergence at a rate of O(1/K)" while Theorem 2 states O(1/√K).** These are inconsistent (one suggests linear convergence, the other sublinear). While O(1/√K) is what the theorem actually states and is standard for non-convex smooth SGD, the abstract's stronger claim should be corrected.

- **Wall-clock computation time is not reported.** Remark 1 argues that the O(dm) encoding cost can be offset via Jacobian-vector products and claims the time is "negligible" (citing Table A.10 in the appendix), but the main text provides no actual runtime measurements. Given that FL deployment scenarios involve resource-constrained clients, this is a relevant omission.

### Trivial

- The pseudo-code in Algorithm 2 has a minor notation inconsistency: line 8 uses subscript `k,i` while line 9 uses superscript `k` and subscript `i` differently.
- Some figure references (e.g., "Fig. A.9") point to the stripped appendix and cannot be verified from the main text.

## Nice-to-Haves

- A properly derived convergence rate in terms of d, m, and K, with the conditions under which it matches FedSGD clearly stated. If the rate is O(d/(m√K)) rather than O(1/√K) with logarithmic m, the contribution should be reframed accordingly.
- Accuracy vs. SSIM Pareto curves for a range of m values without artificial budget constraints, to more clearly show the three-way trade-off.
- Error bars or multiple-seed results for the experimental tables.

## Removed Points

Points removed from the Harsh Critic and Strength Finder inputs, treated with caution:

- **"The convergence proof is missing from the main text, and the appendix is not available"** — Removed per hard rules: the parser strips appendices from all papers; these exist in the original submission.
- **"Hyperparameter details for the baselines... are not provided in the main text"** — Removed per hard rules: these are in the appendix (which was stripped) and the paper states this explicitly.
- **"The paper lacks a formal privacy guarantee such as ε-differential privacy"** — Partially removed as over-extended: the paper explicitly frames its privacy as "inherent" (reconstruction-based, not DP). This is a legitimate framing even if the guarantees are weaker than DP. The criticism about overclaiming is retained in Major weakness #2.
- **Strength Finder strength about "Provable privacy independent of gradient magnitude"** — Kept but contextualized: the (d-1)/m bound is indeed gradient-magnitude-independent, which is a genuine property. However, the privacy claims are qualified in the weakness above.
- **"The LDP comparison uses only a single noise level... without tuning to match a desired privacy level"** — Retained in reduced form (merged into Major weakness #3 about missing joint methods).
- **"FedSGD and its variants are shown to exceed the communication budget, but this is a trivial observation"** — Removed: exceeding the budget is not trivial — it demonstrates that these methods are simply infeasible under the stated constraints, which is a meaningful comparison point.
- **"The extra term in Theorem 2's convergence bound depends on ε, and since ε can be made small with m = O(log d/ε²), the theory is sound"** — This claimed strength from Strength Finder is contradicted by the verified weakness about the JL lemma application, and is removed.
- **"The convergence rate matching standard FedSGD under a logarithmically growing number of projections"** — Removed because this is the specific claim that is unsupported (see Major weakness #1).

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses do not surface a genuinely novel observation that the paper itself does not already make.

## Suggestions

1. **Fix the convergence analysis.** Derive the actual convergence rate in terms of d, m, and K. State the conditions under which the rate matches FedSGD (likely requiring m = Ω(d) if the analysis follows standard SGD variance bounds, or clarify if a different analytical approach is being used). If the JL lemma is being invoked in a non-standard way, explain the precise relationship between the high-probability norm bound and the expectation bound in the convergence analysis, and state the correct m requirement.

2. **Re-frame the privacy contribution.** Provide either (a) a formal differential privacy guarantee under a specific definition (even if non-standard), or (b) clearly qualify the guarantees as reconstruction-error lower bounds rather than "inherent privacy." Include comparisons against DP baselines under matched privacy budgets.

3. **Expand the empirical comparison.** Include methods that jointly target compression and privacy (e.g., Amiri et al., 2021 or CPSGD / Agarwal et al., 2018). Present accuracy vs. communication vs. SSIM Pareto plots across a range of m values for all methods.

4. **Report wall-clock times** for client-side computation in the main text, not just the appendix, to substantiate the claim that the O(dm) cost is "negligible."

## Score and Decision

**Calibration details:**

*Round 1 — Bracketing:* Searched for "federated learning gradient compression random projection convergence analysis" across three bands.
- Low band (<3.5): Anchors at 1.67 (compressed decentralized learning with error feedback — rejected for weak experiments), 3.00 (FedADM, FedComLoc — rejected for limited scope).
- Middle band (3.5-7.5): Anchors at 4.67 (compression+importance sampling FL — rejected for convex-only theory and weak experiments), 5.75 (FedProx extrapolation analysis — rejected for restricted scope), 5.83 (LASER — rejected for insufficient novelty despite sound theory and good experiments), 5.50 (FeDLRT — rejected for missing baselines and presentation issues but strong theory and experiments).
- High band (>7.5): Anchors at 7.60–8.00 (all accepted; topics are DRO, optimization bounds — structurally different paper types).

*Bracket:* Between 3.5 and 6.0. The paper has real experimental evidence and a novel idea, placing it above the 1.67–3.00 range, but the theoretical flaw is more fundamental than the issues in middle-band papers like LASER (5.83, criticized for low novelty) or FeDLRT (5.50, criticized for missing baselines).

*Round 2 — Narrowing:* Focused on gradient compression theory and privacy papers in the (3.5, 6.5) range.
- SAFL (4.50, scores 3,6,3,6): Criticized for strong assumptions but accepted that theory was sound under those assumptions. Experiments were moderately convincing.
- FedExProx tighter analysis (4.67, scores 3,6,5): Solid analysis but limited to quadratic/synthetic problems.
- Gradient inversion and privacy papers (4.75–5.67): Focused on attack/defense, not directly comparable.

*Comparison:* The current paper's theory flaw is more severe than SAFL's strong-assumptions issue or FedExProx's scope limitation — SAFL's convergence analysis was internally consistent given its assumptions, while this paper's Theorem 2 appears inconsistent with its own Lemma 1. However, the empirical results here (356× compression, low SSIM) are stronger than those in SAFL or FedExProx. The paper sits between SAFL (4.50) and FeDLRT (5.50) but closer to 4.50 due to the fundamental theory issue.

*Final calibration:* The paper has a genuinely interesting idea and strong empirical evidence for communication reduction and privacy protection, but a major unresolved issue in its core theoretical claim. The score reflects that the contribution is not fatally invalidated — the empirical results stand on their own — but the theoretical framing as presented is misleading.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>