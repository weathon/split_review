Now let me write the final consolidated review. Let me first organize my analysis of all the reviewer claims, cross-checked against the paper.

**Verification of key claims:**

1. **JL Lemma error**: Verified from the paper text (line 112). The paper claims that \(\frac{1}{m}U_{k,i}U_{k,i}^\top\) satisfies the JL lemma with \(m = O(\ln(d/\delta)/\epsilon^2)\). The classical JL lemma applies to maps from ℝ^d to ℝ^m, not to the reconstruction operator mapping back to ℝ^d. For Rademacher entries, \(\mathbb{E}[\|\frac{1}{m}UU^\top g\|^2] = \frac{d+m-1}{m}\|g\|^2\), which scales as \(d/m\) for \(m \ll d\). The claimed logarithmic dependence on \(d\) is therefore mathematically unsupported. The appendix (Lemma 6) is stripped, so I cannot verify whether there's additional nuance, but as stated in the main body, the claim is incorrect.

2. **Abstract inconsistency**: Verified. Abstract says "O(1/K)." Theorem 2 says "O(1/√K)." The rest of the paper consistently uses O(1/√K). This is a typo in the abstract.

3. **LDP comparison**: Verified. The paper adds Laplace noise with fixed variance (0.1, 0.5, 1, 10) directly to gradients without sensitivity calibration or ε reporting. This is not a proper DP mechanism. However, the paper explicitly distinguishes its approach from DP — its privacy claim is about reconstruction error, not DP.

4. **Empirical m vs log d**: For CNN with d~300K, log d ≈ 12.6, but m=600 is used. The paper claims this "further supports" the log d theory. This is not correct — 600 is much larger than 12.6. However, asymptotic O(log d) can hide large constants.

5. **FedPDD gradient notation**: The critic's claim about inconsistent notation between Eq (2) and Eq (1) — this is a minor presentation issue.

Now let me finalize.

For the score, I need to place this relative to anchors. My round 1 bracket was 5.0-7.0. Round 2 gave me: DeComFL at 6.25 (most similar), GRAIN at 5.60, nAs4LdaP9Y at 6.33, rsg1mvUahT at 6.50, giU9fYGTND at 7.00.

Compared to DeComFL (6.25): Our paper has a broader contribution (privacy + communication) and a more clever algorithm, but has a significant theoretical flaw. DeComFL has cleaner theory. I'd place our paper slightly below DeComFL.

Compared to GRAIN (5.60): GRAIN is an attack paper with a narrower scope. Our paper makes a constructive contribution to FL systems. I'd say our paper is at a similar quality level — perhaps slightly above because it's a defense/improvement rather than an attack.

Final score: **5.5**. This reflects: (a) a genuinely novel and useful algorithmic contribution, (b) strong empirical results with meaningful baselines, (c) a solid privacy analysis (Lemmas 1-2), but (d) a significant theoretical gap in the convergence analysis that needs revision, and (e) some weaknesses in the experimental comparisons (LDP calibration, missing joint baselines).

Now let me write the review.## Summary

This paper introduces FedMPDD, a federated learning algorithm that encodes high-dimensional client gradients by computing their directional derivatives along multiple random Rademacher vectors. Each client transmits only the scalar directional derivatives and a random seed, reducing uplink communication from O(d) to O(m) with m ≪ d. The server reconstructs a gradient estimate by projecting back onto the same random vectors. The rank deficiency of the projection (m ≪ d) provides inherent privacy against gradient inversion attacks, and the multi-projection averaging overcomes the dimension-dependent convergence limitations of single-projection variants. The paper provides theoretical convergence analysis, privacy bounds, and experiments on MNIST and CIFAR-10 demonstrating joint communication-privacy benefits.

## Strengths

- **Novel algorithmic contribution.** The use of multi-projected directional derivatives for federated learning is genuinely creative and, to my knowledge, not previously explored in FL. The core mechanism — encoding gradients as inner products with random vectors, transmitting scalars plus seeds, and reconstructing server-side — simultaneously addresses communication and privacy in a unified, elegant design (Algorithm 2, lines 6–11 and 14–19).

- **Rigorous privacy analysis via rank deficiency.** Lemmas 1 and 2 provide explicit, verifiable bounds: the expected relative squared gradient reconstruction error is (d−1)/m (Equation 6), and the private data reconstruction error inherits a lower bound scaling with d/m (Equation 7). Unlike the convergence argument, these derivations are correct and create a direct, quantifiable link between the projection parameter m and the privacy barrier. Figure 1 empirically corroborates this with SSIM scores remaining consistently below 0.04 across 100 training epochs.

- **Strong empirical demonstration of the joint communication-privacy trade-off.** Tables 1 and 2 show that FedMPDD is the only evaluated method that simultaneously stays within strict byte budgets and achieves low SSIM (≤0.22) while delivering meaningful test accuracy. On CIFAR-10, FedMPDD with m=600 reduces the bytes needed for 60% target accuracy by 356× relative to FedSGD while keeping SSIM at 0.14, whereas all baselines either exceed budgets or leak substantial information (SSIM > 0.7). The parameter m functions as an effective tunable knob across the privacy-communication-accuracy trade-off.

- **Well-chosen baselines covering diverse compression paradigms.** The paper compares against quantization (QSGD), sparsification (Top-k), sketching (lp-proj), and structured updates (SA-FedLora), plus LDP variants, providing a comprehensive benchmark landscape that substantiates the claim that existing methods trade off privacy for compression or vice versa.

## Weaknesses

### Major

- **The central convergence argument rests on a mathematically incorrect application of the Johnson–Lindenstrauss lemma.** Section 2 (line 112) claims that the reconstruction operator \(\frac{1}{m}U_{k,i}U_{k,i}^\top\) (a d×d matrix) satisfies the JL lemma with \(m = O(\ln(d/\delta)/\epsilon^2)\), yielding the norm bound \(\|\frac{1}{m}U_{k,i}U_{k,i}^\top g\| \leq (1+\epsilon)\|g\|\). The classical JL lemma applies to maps from ℝ^d to a lower-dimensional space ℝ^m and guarantees norm preservation of the *projected* vector. The operator here maps ℝ^d → ℝ^m (via U^⊤) and then lifts back to ℝ^d (via \(\frac{1}{m}U\)). For Rademacher entries, a direct variance computation gives \(\mathbb{E}[\|\frac{1}{m}UU^\top g\|^2] = \frac{d+m-1}{m}\|g\|^2\), which scales as d/m when m ≪ d, not as 1 + ε with m ∝ log d. Consequently, Theorem 2's claimed \(O(1/\sqrt{K})\) convergence rate under the stated \(m = O(\log d)\) condition is unsupported by the argument presented. This is not a matter of missing constants — the claimed logarithmic dependence on dimension is not achievable for this reconstruction operator. The paper would need a fundamentally different analysis (e.g., variance-based) to correctly characterize the m-d-convergence relationship.

- **The empirical m values do not support the logarithmic-growth claim, and the text overstates the alignment.** For the CNN model (d ~ 300K parameters), log d ≈ 12.6, while the smallest used m is 600. The paper states this "further supports the theoretical guarantees in Theorem 2, where m is required to grow logarithmically with the dimension d" (line 200). In reality, m = 600 is roughly 48 × log d, and while asymptotic notation can hide constants, the gap is large enough that the empirical evidence does not "support" the log-d claim — it merely shows that m can be a small fraction of d (0.2%–4%). This overstatement weakens an already fragile theoretical narrative.

### Minor

- **The LDP comparison lacks proper calibration.** The experiments add Laplace noise with fixed variances (0.1, 0.5, 1, 10) directly to gradients, without gradient clipping, sensitivity analysis, or reporting privacy budgets (ε, δ). This makes the "LDP" baseline an ad-hoc noise-injection scheme rather than a principled differentially private mechanism. The paper's core privacy claim is about reconstruction error (Lemmas 1–2), not formal DP, and the paper explicitly distinguishes itself from DP approaches — so this does not invalidate the contribution. However, claiming to outperform "LDP" while using an uncalibrated proxy weakens the comparison. A fair evaluation should either implement proper LDP with reported ε values or reframe the comparison as against "gradient noise" rather than LDP.

- **No baselines that jointly combine compression and formal privacy.** The paper positions itself as uniquely addressing both communication and privacy, but does not compare against methods like QSGD + calibrated DP noise (e.g., cpSGD, which is cited in the references) or compressive DP approaches from the related work discussion. Including at least one such joint baseline would substantially strengthen the empirical claim.

- **The abstract contains a factual error.** The abstract states convergence at rate "O(1/K)" while Theorem 2 and the rest of the paper consistently give O(1/√K). This is a clear typo but should be corrected to avoid misleading readers about the paper's theoretical contribution.

- **The empirical evaluation of m-scaling is limited.** The paper selects fixed m values for each experiment and claims they were chosen according to \(m = O(\ln(d/\delta)/\epsilon^2)\). A systematic experiment showing, for a fixed model, how accuracy and SSIM vary as m ranges from small to large (as a fraction of d) would much more convincingly characterize the trade-off than the current fixed-point comparisons. Table A.9 (in the stripped appendix) is mentioned but not visible for verification.

- **The convergence guarantee is presented as matching FedSGD without qualification.** Both the abstract and introduction claim FedMPDD "matches the performance of FedSGD," but Theorem 2 contains an additive \(\epsilon G^2 / \sqrt{K}\) term from the projection distortion. While this term can be made small by tuning m, it means the rate *matches up to an additive constant*, not that it is identical — a nuance worth stating explicitly.

### Trivial

- The gradient notation in Equation (2) has several typos/formatting issues in the decomposition diagram: the server-side projection terms are misaligned and the variable naming is inconsistent between the decomposition and the equation text. This does not affect understanding but could be cleaned up.

## Nice-to-Haves

- A variance-based convergence analysis replacing the JL argument would be valuable. The correct variance characterization (showing that the estimator has variance scaling as d/m) would still yield a meaningful trade-off — just not the log-d claim — and would put the theory on solid ground.
- Include a joint communication+privacy baseline (e.g., cpSGD or QSGD with calibrated Gaussian noise) to strengthen the claim that FedMPDD uniquely balances both objectives.
- The projected-forward JVP strategy mentioned in Remark 1 is appealing for resource-constrained settings; experimental validation, even on a single architecture, would substantiate the computational-efficiency claim.
- Discuss the server-side computational cost of regenerating m random d-dimensional vectors per client per round (O(Nβdm) per round), which may become the bottleneck for large N or d.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The LDP baseline is not a standard DP mechanism... this makes the comparison with privacy methods unfair."** → Retained but downgraded to Minor because the paper explicitly distinguishes its privacy approach from DP and the core privacy analysis (Lemmas 1–2) does not depend on LDP comparisons. The comparison is illustrative, not foundational.
- **"FedMPDD with m=600 reaches 40.8% test accuracy... 60% target accuracy for CIFAR-10 leaves open whether FedMPDD can reach higher accuracies."** → The strength finder's framing of 40.8% as strong evidence is contextual. The 60% target accuracy limitation is a reasonable observation but is more about scope than a flaw — the paper demonstrates it can reach the target at dramatically lower communication cost, which is the point. Kept as context but not elevated to a weakness.
- **"The computational cost remark (Remark 1) is stated without empirical support."** → The paper acknowledges this as a follow-up study (Section F of appendix) and provides complexity analysis; the claim is hedged appropriately. This is a nice-to-have, not a weakness.
- **Harsh critic's claim about "FedPDD gradient notation inconsistency between Eq (2) and Eq (1)"** → This was a parser-artifact misreading by the critic; the equations are consistent when read in the original context. Removed.
- **Harsh critic's claim about "server-side computation O(Nβdm) per round"** → This is a legitimate concern but fits better as a nice-to-have since the paper focuses on uplink communication and the server is assumed to have more resources. Moved to Nice-to-Haves.
- **Strength Finder: "Dimension-independent convergence guarantee"** → This strength is directly contradicted by the verified JL issue. The claimed dimension independence (logarithmic dependence) is unsupported. Removed.
- **Strength Finder: "Protocol design that minimizes uplink overhead"** → This is a restatement of the algorithm, not an independently verified strength. Removed as generic.
- **Strength Finder: "Effective privacy-communication-accuracy trade-off via m"** → This is genuinely supported by the experiments. Retained in modified form under strengths.

## Novel Insights

The paper's decomposition of the gradient encoding into (a) client-side inner products with random vectors and (b) server-side reconstruction from seeds reveals a remarkably simple mechanism that simultaneously yields communication compression and privacy. The insight that the privacy guarantee arises from the nullspace dimension (d−m) of the projection operator — giving a uniform, gradient-magnitude-independent reconstruction error of (d−1)/m — is genuinely novel and provides a clean alternative to the noise-vs-utility dilemma that plagues additive-noise privacy methods. This geometric perspective on privacy through rank deficiency could inspire future work beyond the specific FL setting.

## Suggestions

- Replace the JL-based convergence argument with a variance-based analysis. Show that the gradient estimator has bounded variance scaling as O(d/m + 1) and derive the resulting convergence rate. This would produce a correct (though less optimistic) theory that still demonstrates the benefit of multi-projection over single-projection (which has variance O(d)).
- Calibrate the Laplace noise baselines properly — report the gradient norm clipping threshold used and the resulting ε values — or relabel them as "Gaussian/Laplace noise" rather than "LDP" to avoid implying formal DP guarantees.
- Add at least one joint compression+DP baseline (e.g., QSGD + Gaussian noise with calibrated sensitivity) to Tables 1–2.
- Correct the abstract to say O(1/√K) instead of O(1/K).
- Add a systematic m-sweep experiment showing accuracy and SSIM as functions of m/d for a fixed model, which would provide a clearer empirical characterization of the trade-off than the current point comparisons.

## Score and Decision

**Calibration anchors across all rounds:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 0jmFRA64Vw (FedComLoc) | 3.00 | R1 | Weaker — narrower scope, less empirical validation |
| Jl0aEFrp11 (Bidirectional Comm-Efficient FL) | 2.75 | R1 | Weaker — rejected for theoretical gaps and limited experiments |
| Zh9gz3CaWm (FedMUD) | 3.75 | R1 | Weaker — limited theory, narrower experiments |
| cKGpe1792U (RGLA) | 5.67 | R2 | Similar quality tier; attack paper with solid empirical work |
| omrLHFzC37 (DeComFL) | 6.25 | R1/R2 | Most comparable; similar idea (scalar+seed encoding), stronger theory, narrower scope (no privacy) |
| nAs4LdaP9Y (FedOrth) | 6.33 | R2 | Stronger theory, more specialized problem |
| giU9fYGTND (FedImpro) | 7.00 | R2 | Clearly stronger — clean theory + comprehensive experiments |
| ZuazHmXTns (PAdaMFed) | 7.60 | R1 | Clearly stronger — rigorous theory, well-executed |

**Round 1 bracket:** 5.0 – 7.0  
**Round 2 narrowing:** DeComFL (6.25) is the closest comparator. FedMPDD has a broader contribution (privacy + communication vs. communication only), a more creative algorithm (first-order projection vs. zeroth-order downgrade), and more comprehensive baselines. However, DeComFL's theory is cleaner and its convergence analysis is correct as stated, whereas FedMPDD's JL-based argument is mathematically unsupported. On balance, FedMPDD is slightly weaker than DeComFL due to the theoretical gap. Against GRAIN (5.60), FedMPDD is comparable in empirical quality but makes a more constructive contribution (system improvement vs. attack). **Final score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>