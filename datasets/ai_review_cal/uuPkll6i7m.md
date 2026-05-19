- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 8, 5
Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the consolidated review.

## Summary

This paper introduces the notion of "certified calibration" — worst-case bounds on calibration metrics (Brier score and expected calibration error) under adversarial perturbations for models that already provide certified predictions. The contributions are: (1) a closed-form tight upper bound for the certified Brier score (CBS), (2) a mixed-integer programming reformulation to approximate the certified calibration error (CCE → ACCE) with an ADMM solver, (3) empirical demonstrations that calibration can be severely harmed even when accuracy is protected, and (4) adversarial calibration training (ACT) that fine-tunes models to improve certified calibration metrics.

## Strengths

- **Closed-form tight bound for certified Brier score (Theorem 1):** The paper provides an analytic, tight upper bound on the top-label Brier score under adversarial perturbations, using only per-sample confidence certificates (C2). This is clean, well-motivated, and correctly derived. It is used directly in experiments (Figure 1, Table 3) and serves as one flavour of ACT.

- **Novel MIP reformulation for the certified calibration error (Theorem 2):** The paper expresses the CCE as a mixed-integer program over bin assignments and perturbed confidences (Eq. 14–18), enabling a numerical approach to what would otherwise be an intractable non-convex, non-differentiable optimization. The ADMM solver converges within 3000 steps in all experiments.

- **Clear empirical demonstration that calibration attacks harm even robust models (Table 1):** A simple \( (\eta,\omega) \)-ACE attack on a ResNet-50 (ImageNet) increases AdaECE from 3.70% to 47.23% at \( \epsilon=2/255 \), and even on an adversarially trained model the ECE rises from 9.03% to 13.54%. This provides strong motivation for certified calibration.

- **Adversarial calibration training (ACT) improves both ACCE and CBS (Table 3):** Fine-tuning with Brier-ACT or ACCE-ACT reduces the ACCE (e.g., at radius 1.0 on CIFAR-10, from 56.36% to 47.08%) while preserving or improving certified accuracy. Critically, CBS — which is independent of the MIP formulation — also improves substantially (from 36.25% to 24.87% at radius 1.0), providing corroborating evidence that ACT genuinely improves calibration under attack.

- **Rigorous comparison of ACCE approximation methods (Figure 2):** The ADMM solver uniformly yields larger (tighter) ACCE bounds than the dECE and Brier-confidence baselines across all radii, demonstrating its effectiveness as an approximation method.

- **Computational cost analysis:** The paper quantifies the overhead of ACCE attacks relative to standard SmoothAdv (3.4% slower on CIFAR-10, 2.6% on ImageNet), showing that the additional ADMM updates are cheap compared to backpropagation through the network.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The equivalence claim in Theorem 2 lacks rigorous justification:** The paper states that "maximising (15) over (a,z) is equivalent to solving (12)" under the stated constraints, but does not provide a formal proof of equivalence. Specifically, the certificate C2 guarantees confidence bounds \( l_n \leq z(x_n+\gamma_n) \leq u_n \) but does not guarantee that *every* value within those bounds is attainable by some perturbation within the radius. The MIP assumes full controllability over the confidence within the certificate bounds, which makes the ACCE a *valid upper bound* (conservative certificate) rather than an exact solution to the CCE. This is a standard and acceptable limitation in the certification literature, and the paper honestly calls it an "approximate certificate" — but Theorem 2's wording implies exact equivalence. The paper would benefit from acknowledging this gap explicitly rather than claiming equivalence.

- **ACCE is both the training objective and the primary evaluation metric for ACCE-ACT:** While ACCE-ACT trains against a MIP-based adversary and is evaluated on ACCE, this creates a partial closed loop. The concern is partially mitigated because (a) the CBS metric — which is independent of the MIP — also shows substantial improvement (from 36.25% to 24.87% at radius 1.0), and (b) the paper reports ACT's effect on certified accuracy as well. However, the paper does not directly measure the actual (non-certified) ECE under an attack that respects the single-confidence constraint, which would help calibrate confidence in ACCE as a proxy.

- **No confidence intervals or variance estimates for key metrics:** Reported values (ECE, ACCE, CBS) are given as point estimates without standard errors or bootstrap intervals. Given varying dataset sizes (2000 samples for CIFAR-10, 500 for ImageNet), this limits the reader's ability to assess the reliability of reported improvements. This is common practice in the certification literature but would strengthen the paper if addressed.

- **dECE baseline is referenced but not defined:** The dECE method from Bohdal et al. (2023) is used as a baseline in Figure 2, but the paper provides no description of how it works. A brief explanation in the text or appendix would improve self-containedness.

- **The "Standard" and "CDF" certificates are used but not explained:** The paper relies on confidence certificates from Kumar et al. (2020) throughout, but does not describe how these bounds are computed or their properties. Since the ACCE/ACCE values depend on the tightness of these certificates, a brief description would help the reader interpret the results.

### Trivial

- Table 1 would benefit from noting whether the standard errors over the validation set are small enough to trust the observed differences.

## Nice-to-Haves

- An additional small-scale experiment where the true CCE is computed by brute-force search over discretized confidences (e.g., 200 samples, few bins) to directly measure the gap between ACCE and the true worst-case ECE. This would calibrate confidence in the ACCE metric.
- Wall-clock times for ADMM convergence vs. overall training iteration cost, to further substantiate the claim that ACCE attacks are "comparable" to SmoothAdv in cost.
- A more detailed ablation showing which components of the MIP (bin-specific confidences, valid assignment constraint, etc.) contribute most to the improvement over baselines.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"The MIP formulation overestimates the true worst-case ECE (structural flaw)"** — REMOVED. This point is factually incorrect. The MIP constrains each sample to exactly one bin (C^T a = 1_N), so only one z value per sample is active in the objective. The z_{n,m} across different bins are *alternative possibilities* for the optimization to choose among, not simultaneously assigned values. The Confidence Constraint ensures z_{n,m} ∈ [l_n, u_n] ∩ [l_m^B, u_m^B] whenever a_{n,m}=1, so any feasible solution corresponds to a realizable scenario (choose perturbation yielding confidence = z_{n,m} for the assigned bin m). The critic's claim that the formulation allows "different confidence values depending on which bin the point is assigned to" misunderstands that each sample *is* assigned to exactly one bin. The only real limitation is that the certificate bounds don't guarantee all values within them are attainable — but this is the standard limitation of certificate-based approaches, not a structural flaw unique to this MIP.

2. **Suggested ACT "closed loop" as a fatal/major flaw** — DEMOTED TO MINOR (see above). The critic's framing as a near-fatal concern is disproportionate given that CBS (an independent closed-form bound) also improves substantially.

3. **"ADMM convergence is not guaranteed to find a global optimum"** — REMOVED. This is true of essentially any non-convex optimization. The paper is transparent about using ADMM as an approximate solver and reports that it converges empirically within 3000 steps. This is standard practice.

4. **All formatting, typo, and style nitpicks** — REMOVED per instructions (PDF extraction artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the ACCE's status in Theorem 2:** Replace the claim of "equivalence" between the MIP and the CCE with a clear statement that the MIP formulation yields a *valid upper bound* on the CCE (i.e., the ACCE is a conservative certificate). Explicitly note that the certificate C2 only guarantees confidence within bounds, not attainability of every value, so the MIP solves a relaxed problem whose optimum upper-bounds the true CCE.

2. **Add an "ECEs under realistic attacks" experiment:** For a subset of samples, attack the model using the MIP adversary (from ACCE-ACT) and measure the actual (non-certified) ECE of the perturbed outputs, comparing it to the ACCE. This would demonstrate how tight the ACCE bound is in practice and directly address the closed-loop concern.

3. **Provide confidence intervals** for the key metrics (ACCE, CBS) in Table 3, at least through bootstrapping over the 2000 CIFAR-10 samples.

4. **Briefly describe the dECE method and the Standard/CDF certificates** in the main text or appendix to improve readability for readers unfamiliar with these baselines.
