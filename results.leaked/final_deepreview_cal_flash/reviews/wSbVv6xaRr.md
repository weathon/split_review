Now I have enough information to write the consolidated review. Let me compose it.

## Summary

The paper introduces FedMPDD, a federated learning algorithm that compresses client gradients via multi-projected directional derivatives — each client computes inner products of its gradient with m random Rademacher vectors (uploading m scalars plus a seed) and the server reconstructs a gradient estimate. The approach aims to jointly reduce uplink communication (from O(d) to O(m)) and provide privacy against gradient inversion attacks through the rank deficiency of the projection.

## Strengths

- **Genuine communication savings validated experimentally.** The paper demonstrates that FedMPDD drastically reduces total uplink communication compared to baselines — e.g., 356× reduction over FedSGD on CIFAR-10 to reach 60% accuracy (Table 2). The fixed-budget experiments show FedMPDD achieving reasonable accuracy where FedSGD cannot even complete a single round.

- **Interesting algorithmic idea.** Using projected directional derivatives (inner products with random vectors) as a gradient encoding mechanism in FL is novel, and the multi-projection averaging to reduce single-projection variance is a sensible design. The dynamic (per-client, per-round) random projection strategy is cleanly different from fixed-subspace approaches.

- **Comprehensive empirical setup.** The experiments span MNIST and CIFAR-10 with multiple architectures (LeNet, CNN), multiple baselines (FedSGD, LDP, QSGD, Top-k, lp-proj, SA-FedLora), both IID and non-IID settings, and two attack families (Yu et al. 2025, DLG). The SSIM-based privacy evaluation consistently shows FedMPDD achieving SSIM < 0.22.

- **Tunable three-way trade-off.** The parameter m simultaneously controls communication cost, gradient reconstruction accuracy, and privacy level, with explicit quantification via Lemma 1.

## Weaknesses

### Fatal

1. **Incorrect application of the Johnson-Lindenstrauss lemma (Section 2, Eq. (4)).** The paper claims that for the estimator $\hat{\mathbf{g}}_i = \frac{1}{m} U_{k,i}U_{k,i}^\top \mathbf{g}_i$, the JL lemma yields $\|\hat{\mathbf{g}}_i\| \le (1+\epsilon)\|\mathbf{g}_i\|$ with $m = O(\log(d/\delta)/\epsilon^2)$. This is mathematically incorrect. The JL lemma bounds $\|\frac{1}{\sqrt{m}} U^\top \mathbf{g}\| \approx \|\mathbf{g}\|$ (embedding into $\mathbb{R}^m$), not $\|\frac{1}{m} UU^\top \mathbf{g}\|$. For Rademacher entries (variance 1), the operator $\frac{1}{m}UU^\top$ has expected squared norm $\frac{d}{m}\|\mathbf{g}\|^2$, so the norm scales as $\sqrt{d/m}\,\|\mathbf{g}\|$ — far larger than $(1+\epsilon)\|\mathbf{g}\|$ when $m \ll d$. This error invalidates the central theoretical justification for choosing $m$ logarithmically in $d$.

2. **Internal contradiction between Lemma 1 and Theorem 2.** Lemma 1 correctly gives the estimator variance as $(d-1)/m$ times the gradient norm squared. The convergence bound in Theorem 2, however, contains only an $O(\epsilon G^2/\sqrt{K})$ term attributed to the multi-projection distortion — it does not incorporate the dominant $(d-1)/m \cdot G^2/\sqrt{K}$ variance term. The paper never explains how an estimator with variance $\Theta(d/m)$ can achieve the claimed $O(1/\sqrt{K})$ rate with logarithmic $m$. The convergence analysis as presented is therefore inconsistent with the paper's own variance calculation.

These two errors are verifiable from the main text. They undermine the paper's core theoretical claim — that FedMPDD matches FedSGD convergence with $m = O(\log d)$ projections — and cannot be resolved without a substantially revised analysis.

### Major

3. **Overstated privacy claims.** The paper repeatedly asserts "inherent privacy" and "uniform privacy protection" but provides no formal privacy definition (e.g., differential privacy or an information-theoretic measure). Lemma 2's lower bound on data reconstruction error depends on an unknown Lipschitz constant $L_v(\mathbf{x})$, making it non-operational. Remark 2's multi-round composition guarantee ($T \times m < d$) prevents *exact* gradient recovery but does not bound approximation error — an attacker can still obtain a good least-squares approximation. The empirical SSIM evaluation, while useful, evaluates only two specific attack families and is not a rigorous privacy guarantee.

4. **Missing comparison with methods that jointly address compression and privacy.** The paper claims a "joint" improvement in communication and privacy but does not empirically compare against techniques that combine gradient compression with differential privacy (e.g., Amiri et al. 2021; Lyu 2021), which are cited in the related work. Without such baselines, the claimed advantage over the joint state of the art is not substantiated.

5. **Inconsistency between abstract and theorem.** The abstract claims convergence at rate $O(1/K)$, while Theorem 2 gives $O(1/\sqrt{K})$. These are different rates (the former would require strong convexity, which is not assumed). This error undermines confidence in the presentation.

### Minor

6. **Privacy evaluation scope.** The empirical privacy evaluation relies on two gradient inversion attacks (Yu et al. 2025, DLG). The paper should discuss whether stronger attacks could achieve higher SSIM and acknowledge that SSIM from a specific attack family is not a formal privacy measure.

7. **The selection of $m$ in experiments is not tied to the claimed theoretical formula.** The paper states $m = O(\ln(d/\delta)/\epsilon^2)$ was used with "sufficiently small" $\delta,\epsilon$, but the specific values of $\delta,\epsilon$ are never reported. A direct validation of the relationship between $m$ and convergence (e.g., plotting convergence vs. $m$ for fixed $d$ to test the logarithmic scaling) would strengthen the empirical story.

### Trivial

- The abstract states $O(1/K)$ while the theorem states $O(1/\sqrt{K})$ — one of these is wrong (likely the abstract, given the non-convex setting).

## Nice-to-Haves

- A corrected convergence analysis that incorporates the $(d-1)/m$ variance from Lemma 1, even if it yields a dimension-dependent rate, would make the paper's actual trade-off transparent and could be paired with an empirical argument that real gradients have low effective rank.
- Formalizing privacy via a well-accepted framework (differential privacy or at least an information-theoretic notion) would substantially strengthen the paper.
- A sensitivity analysis of $m$ across different model sizes to empirically verify whether $m$ can remain sublinear in $d$ without degrading accuracy.
- Empirical comparison with Amiri et al. 2021 and Lyu 2021 (methods that jointly compress and add DP noise).

## Removed Points

- *Criticism that the fixed-budget comparison against FedSGD is uninformative* — This is a valid experimental design choice that demonstrates the method's communication efficiency under realistic constraints. FedSGD cannot operate within the budget, which is precisely the point the comparison makes.
- *Claim that the privacy lower bound (Lemma 2) depends on the Lipschitz constant and thus is "not operational"* — This is a common structure for such lower bounds; it is a genuine limitation but the harsh critic overstates the severity. Retained in weaker form (Major #3).
- *Request for more models/datasets* — The existing evaluation scope (MNIST, CIFAR-10, four architectures) is adequate for a conference submission.
- *Criticism about computational cost of $O(dm)$ encoding* — The paper addresses this via Remark 1 and the JVP approach, which is a reasonable addressal.
- *Criticism about missing appendix content* — The appendix is stripped by the PDF parser; per instructions, weaknesses about missing appendix content are removed.

## Novel Insights

**None beyond the paper's own contributions.** The core observation connecting the harsh critic and strength finder reviews is that the empirical results (strong communication savings and low SSIM) may be robust to the theoretical flaw — the method works in practice for reasons the current analysis does not correctly capture (possibly because real gradient matrices have low effective rank, making the worst-case $d/m$ variance pessimistic). This gap between flawed theory and strong empirics is itself an interesting observation, but it arises from the reviewers' meta-analysis, not from the paper itself.

## Suggestions

1. **Fix the JL lemma argument.** Replace the incorrect JL-based norm bound with a correct variance analysis built on Lemma 1. Acknowledge that the convergence rate depends on $d/m$ and discuss when this is acceptable (e.g., gradients are effectively low-rank, or client averaging provides sufficient variance reduction).
2. **Align the abstract's convergence claim with Theorem 2** ($O(1/\sqrt{K})$, not $O(1/K)$).
3. **Add baselines that jointly compress and add DP noise** (Amiri et al. 2021; Lyu 2021) to substantiate the "joint improvement" claim.
4. **Temper the privacy language**: replace "inherent privacy" with precise statements about gradient reconstruction error and SSIM under specific attacks. If differential privacy guarantees are desired, derive them or explicitly state their absence as a limitation.
5. **Validate the $m$ vs. $d$ scaling empirically** with a sweep over $m$ at different model sizes, plotting convergence against the theoretical prediction.

## Score and Decision

**Round 1 — Bracketing.** Three queries anchored on topics similar to the paper:
- Weak band (avg score < 3.5): FedComLoc (3.00), DECENT (1.67), FedADM (3.00), etc. — papers with incremental contributions or narrow scope.
- Middle band (3.5–7.5): FL Generalization Study (5.00, rejected), Private Blind Model Averaging (3.60, rejected), FedSMU (5.75, rejected), Improving LoRA (5.50, accepted).
- Strong band (> 7.5): Problem-Parameter Free FL (7.60), DP Few-Shot (8.00) — accepted papers with solid contributions.

**Initial bracket: 3.0 – 4.5.** The paper has stronger empirics than the weakest band but a fatal theoretical error that prevents it from reaching the middle band.

**Round 2 — Narrowing.** Two queries inside (2.0–4.5) and (4.0–6.5):
- CORE (3.67): shares the random-projection-for-compression theme but without the JL error; rejected for limited novelty and limited experiments. *The current paper has better experiments but a worse theory flaw → slightly weaker.*
- FedLoRU (4.00): low-rank FL updates with some theory but no convergence guarantees; rejected. *Comparable empirical quality; current paper's theory flaw is more severe → slightly weaker.*
- BiCompFL (4.80), FedSMU (5.75): stronger empirical/theoretical packages than the current paper.

**Final calibration relative to anchors:** FedLoRU (4.00) had limited novelty and no convergence theory but no fatal error. The current paper has a fatal theoretical error (JL misapplication) that is more serious than FedLoRU's absence of convergence guarantees. CORE (3.67) had a correct but limited theory with weak empirics. The current paper has stronger empirics but a wrong theory, making it roughly comparable or slightly weaker. Placing it at 3.5 reflects that the empirical contribution is real but the theoretical flaw is fatal.

**Score: 3.5** — The paper presents an interesting algorithmic idea and compelling empirical results, but its core theoretical justification is founded on an incorrect application of the JL lemma, and the convergence analysis is inconsistent with the paper's own variance calculation. This error undermines the paper's central claim that FedMPDD matches FedSGD convergence with logarithmically many projections. Substantial revisions to the theoretical analysis are needed before the work can be reconsidered.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>