Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes FedMPDD, a federated learning algorithm that compresses each client's gradient by computing its directional derivatives along $m$ random Rademacher vectors and transmitting only the $m$ resulting scalars plus a seed (reducing communication from $O(d)$ to $O(m)$). The server reconstructs a gradient estimate by projecting these scalars back using the same random vectors reconstructed from the seeds. The paper provides convergence guarantees (Theorem 2: $O(1/\sqrt{K})$ rate matching FedSGD), privacy analysis via reconstruction error bounds (Lemmas 1–2), and experiments on MNIST and CIFAR-10 comparing against sparsification, quantization, sketching, and LoRA-based baselines.

## Strengths

1. **Clean theoretical convergence analysis.** Theorem 2 provides a high-probability convergence bound for the multi-projection estimator, with the distortion term $\epsilon G^2/\sqrt{K}$ controlled by $m = O(\log(d/\delta)/\epsilon^2)$ via the Johnson–Lindenstrauss lemma. The analysis correctly identifies that the multi-projection averaging resolves the $\sqrt{d}$ variance blowup that plagues single-projection estimators.

2. **Gradient reconstruction error is rigorously characterized.** Lemma 1 derives the exact expected relative reconstruction error $(\frac{d-1}{m})$ for the projected gradient estimator under Rademacher random vectors. This is a clean, quantitative link between the compression level $m$ and the information loss, and it is independent of gradient magnitude — a genuine advantage over additive-noise mechanisms.

3. **Communication savings are substantial and well-demonstrated.** Tables 1 and 2 show that FedMPDD achieves its target accuracy with 1.32 GB total uplink on CIFAR-10, versus 471.96 GB for FedSGD (>350× reduction). Under a fixed 0.9 GB budget, FedMPDD reaches 40.84% test accuracy, outperforming QSGD (12.97%), lp-proj (34.72%), Top‑k (38.11%), and SA-FedLora (35.84%).

## Weaknesses

### Fatal

None.

### Major

1. **Abstract claims $O(1/K)$ convergence, but Theorem 2 gives $O(1/\sqrt{K})$.** The abstract states "FedMPDD converges at a rate of $O(1/K)$, matching the performance of FedSGD." This is wrong on two counts: the theorem in the body proves $O(1/\sqrt{K})$, and FedSGD itself converges at $O(1/\sqrt{K})$ for non-convex objectives, not $O(1/K)$. This is a concrete, verifiable inconsistency between the abstract and the paper's own formal result.

2. **Algorithm 2 as written contradicts the claimed computational efficiency.** Algorithm 2 (line 6) explicitly computes the full gradient $\mathbf{g}_i(\mathbf{x}_k)$ before projecting it. This incurs $O(d + dm) = O(dm)$ cost per client. Remark 1 then discusses avoiding this by using Jacobian-vector products, but the pseudocode does not reflect that alternative. As presented, the algorithm's per-client computation is $m$ times more expensive than FedSGD, which undermines the claim that it is computationally favorable in resource-constrained settings. The JVP-based variant described in Remark 1 could resolve this, but it is not the algorithm being evaluated.

3. **Privacy claims are materially overstated.** The paper repeatedly uses terms like "inherent privacy" and "fundamentally different from differential privacy approaches." However:
   - Lemma 2's lower bound on data reconstruction error depends on an unspecified Lipschitz constant $L_v(\mathbf{x})$, making the bound unverifiable and the claimed privacy guarantee effectively non-quantitative.
   - The privacy protection observed empirically (SSIM 0.14–0.22 in Table 2) is largely a consequence of information loss from aggressive compression. Competing compression methods (Top‑k, lp-proj) also degrade SSIM (0.74–0.91) but are labeled as "fail[ing] on privacy," while FedMPDD's similar (albeit stronger) compression is labeled as providing "inherent privacy." The paper does not provide a side-by-side comparison that isolates the privacy benefit per communication bit, making the claim of fundamentally superior privacy unsubstantiated.
   - The paper does not compare against any formal privacy framework (e.g., DP) combined with compression, leaving the privacy claims in a conceptual vacuum.

4. **No error bars or variance reporting in main experimental tables.** Tables 1 and 2 report single-point accuracy and SSIM numbers with no indication of variability across runs. In the presence of stochasticity from client sampling, mini-batch selection, and random projections, the absence of error bars or multiple-seed reporting makes it impossible to assess whether the reported differences (e.g., 40.84% vs. 38.11% for Top‑k) are statistically significant.

### Minor

1. **Missing ablation: fixed vs. dynamic projection.** The paper argues that "dynamic" per-client-per-round random projection is a key differentiator from "fixed subspace" methods, but does not include a baseline that reuses the *same* random projection across rounds. Such an ablation would directly test whether the claimed benefit is from the subspace randomness or from the averaging mechanism itself.

2. **Novelty over previous random-projection FL methods is overstated.** The core mechanism — computing $(u^\top g)u$ with seed-based reconstruction — is a standard JL-style random projection. The paper states it is "fundamentally distinct from structured and sketched updates," but several cited works (Park & Choi 2023, Guo et al. 2024) also use random projections that can be re-sampled per round. The paper's differentiation would benefit from a precise comparison.

3. **Multi-round privacy bound (Remark 2) is of limited practical use.** The bound $T \times m < d$ ensures privacy only under a static-gradient worst-case assumption. For the CIFAR‑10 experiment with $d \approx 300k$, $m=600$, this allows at most 500 rounds — a limit many FL deployments exceed. The bound's practical relevance is unclear.

4. **The claim about "smaller m yielding faster convergence" is unsupported.** The conclusion states that smaller $m$ "sometimes yielded faster convergence with stronger privacy," citing Appendix Fig. A.9, but Theorem 2 predicts that smaller $m$ increases the distortion $\epsilon$, which should strictly worsen convergence. This claim contradicts the paper's own theory and is not convincingly established.

### Trivial

None.

## Nice-to-Haves

- Include a direct comparison with a variant that uses the same random projection at every round, to isolate the benefit of the "dynamic" strategy.
- Add a comparison against a combined LDP+compression baseline (e.g., Amiri et al. 2021) under the same communication budget.
- Include confidence intervals or multiple-seed results for all main experiments.

## Removed Points

- **"Algorithm–claim inconsistency called 'mutually exclusive' by harsh critic"** — Remark 1 describes a JVP-based optimization that *could* replace line 6, not a claim that Algorithm 2 already does so. It is a presentation gap (the algorithm and the efficiency claim are about two different implementations), not a contradiction. Downgraded from Critical to Major.

- **"Proofs deferred to appendix"** — This is standard practice across ML venues; not a weakness per se.

- **"Not situating privacy within formal DP framework"** — The paper explicitly situates its contribution as an alternative to DP rather than a DP mechanism; this is a design choice, not an error. The criticism has been reframed as the specific overstatement in item 3 above.

- **"Notation confusion in Eq. (2)"** — Minor and not central to evaluation.

- **"Lemma 1/2 proofs not shown"** — These are standard calculations for random projections; the paper states them clearly. Removed as not substantive.

- **"Characterization of fixed subspace as inaccurate"** — Some of the cited methods may indeed use fixed subspaces; this depends on the specific references and cannot be verified without external sources.

- **"SSIM values may just reflect poor gradient approximation"** — Speculative; the paper does show that FedMPDD achieves competitive accuracy alongside low SSIM, so poor approximation is not the sole explanation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Fix the abstract to state $O(1/\sqrt{K})$ and "matching FedSGD's rate" (which is also $O(1/\sqrt{K})$ for non-convex objectives).
2. Either update Algorithm 2 to reflect the JVP-based variant that avoids materializing the full gradient, or acknowledge that the presented algorithm computes the full gradient and re-evaluate the computational claims accordingly.
3. Tone down privacy claims: replace "inherent privacy" with "obfuscation via information loss" and provide a direct quantitative comparison with other compression methods at identical communication budgets.
4. Report all experimental results with confidence intervals over at least 3 random seeds.
5. Add an ablation comparing dynamic projections against fixed-projection (same subspace reused across rounds).

## Score and Decision

### Calibration Report

**Round 1 — Bracketing.** Searched three bands for papers on federated learning, gradient compression, random projection, and privacy.

| Band | Avg scores | Representative anchors |
|------|-----------|----------------------|
| Weak (≤3.5) | 3.00 | FL privacy papers with fundamental flaws; rejected unanimously |
| Middle (3.5–7.5) | 4.67–5.83 | LASER (5.83), FeDLRT (5.50), Collab. Compressors (5.25), MAPA (5.00), Ferret (4.67) |
| Strong (≥7.5) | 7.60–8.00 | Strong FL/optimization theory papers with thorough evaluation; accepted |

**Initial bracket:** Between 4.5 and 6.0.

**Round 2 — Narrowing.** Queried inside (4.0, 6.0) with topic-specific searches. Read 4 anchors in full.

- **Ferret (4.67)** — Random-projection FL with seed sharing. Dinged for overclaimed novelty relative to FetchSGD, presentation issues, weak comparison. The current paper has more theory but similar presentation and novelty issues. Comparable.
- **MAPA (5.00)** — Model-agnostic projection adaptation. Dinged for overclaimed model-agnosticism, limited experiments. Similar profile to this paper.
- **Collab. Compressors (5.25)** — Rigorous theory for collaborative DME, but weak experiments. This paper has broader evaluation but less rigorous theory baseline comparison.
- **FeDLRT (5.50)** — Low-rank FL with convergence guarantees. Stronger theory presentation but limited novelty. This paper's theory is comparable but has the abstract inconsistency.

**Final score:** 5.0. The paper has a reasonable core idea and some solid theoretical components (Lemma 1, Theorem 2), but is held back by a concrete abstract/body inconsistency, overclaimed privacy framing, an algorithm that does not match its own efficiency claims, and experiments lacking statistical rigor. It sits slightly below LASER (5.83) and FeDLRT (5.50) due to these structural presentation issues, and is directly comparable to MAPA (5.00) and Ferret (4.67).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>