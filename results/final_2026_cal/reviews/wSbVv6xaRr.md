## Summary

This paper introduces FedMPDD, a federated learning algorithm that encodes each client's gradient as $m$ directional derivatives along random Rademacher vectors (communicating only $m+1$ scalars per client per round), then decodes on the server via a low-rank projection $\frac{1}{m}U_{k,i}U_{k,i}^\top$. The central insight is that averaging $m$ projections overcomes the dimension-dependent convergence failure of a single projection: Theorem 2 proves an $O(1/\sqrt{K})$ convergence rate matching FedSGD when $m$ grows only logarithmically in $d$. Empirical results on MNIST and CIFAR-10 show substantial communication savings (e.g., 356× less than FedSGD to reach 60% accuracy on CIFAR-10) while maintaining low SSIM scores against gradient inversion attacks.

## Strengths

- **Novel algorithmic idea with clean theoretical backing.** The multi-projected directional derivative encoding is a genuine departure from fixed-subspace methods (low-rank, sketching, Count-Sketch) that all rely on a static projection shared across clients and rounds. FedMPDD's per-client, per-round random projections are dynamic and independently sampled, and the paper shows this preserves unbiasedness while overcoming the $\sqrt{d}$ variance blowup of a single projection. Theorem 2's convergence bound explicitly isolates the compression penalty as $O(\epsilon G^2/\sqrt{K})$, tying it to the JL distortion parameter $\epsilon$.

- **Convergence theory with logarithmic dimension dependence.** Theorem 2 proves that $m = O(\log(d/\delta)/\epsilon^2)$ suffices to match FedSGD's $O(1/\sqrt{K})$ rate — the same logarithmic growth as the JL Lemma. This is a nontrivial extension of single-projection analysis (which would give $O(d/\sqrt{K})$) and directly validates the paper's core algorithmic claim.

- **Empirical demonstration of joint improvement.** Tables 1–2 show FedMPDD achieving competitive accuracy under tight communication budgets (0.09 GB / 0.9 GB) while holding SSIM below 0.22 against two gradient inversion attacks (Yu et al., 2025; Zhu et al., 2019). The fixed-budget experiment (Table 2) is a realistic operational scenario, and FedMPDD outperforms all compression-only baselines (QSGD, lp-proj, Top-k, SA-FedLora) on accuracy while simultaneously keeping SSIM an order of magnitude lower.

- **Meaningful privacy lower bounds (Lemmas 1–2).** Lemma 1 gives the expected relative gradient reconstruction error as $(d-1)/m$, and Lemma 2 translates this into a lower bound on data reconstruction error that depends on $d$, $m$, and the gradient Lipschitz constant. These are more than what most compression-only methods provide, and the derivation is mathematically sound (verified: for Rademacher vectors, $\mathbb{E}[\|(1/m)UU^\top g - g\|^2]/\|g\|^2 = (d-1)/m$ follows from elementary variance calculations on the off-diagonal terms).

## Weaknesses

### Major

- **Privacy claims are materially overstated relative to what is established.** The paper titles itself "Communication-Efficient and Private Federated Learning," and the abstract claims "inherent privacy against gradient inversion attacks" and "strong privacy protection." However:
  - Lemmas 1–2 provide lower bounds on *gradient* reconstruction error and *data* reconstruction error under a *specific attack formulation* (minimizing the projected-gradient discrepancy). These do not constitute a formal privacy definition (no $\epsilon$-DP, no mutual information bounds, no RDP guarantee). The analysis does not rule out attribute inference, membership inference, or partial leakage of label information — adversaries may infer sensitive properties even when full-image reconstruction is impossible.
  - The comparison to LDP (FedSGD+Laplace) is framed as a privacy evaluation, but LDP at least provides a formal $(\epsilon,\delta)$ guarantee; FedMPDD provides an informal obfuscation property that is not quantitatively comparable. The paper should either (a) provide a formal DP analysis (e.g., by bounding the sensitivity of $\frac{1}{m}UU^\top g$ and adding calibrated noise) or (b) explicitly downgrade its privacy claims to "resistance to exact gradient reconstruction" and acknowledge that no guarantee against broader inference is made.
  - The multi-round composition bound (Remark 2: $T \times m < d$) is worst-case for a static gradient and says nothing about information accumulation under realistic gradient evolution. The paper acknowledges this ("natural evolution of gradients provides stronger practical protection") but the caveat is insufficient given the strength of the headline privacy claims.  

  **Why this is major, not fatal:** The core algorithmic contribution (communication-efficient FL with convergence guarantees) does not depend on the privacy framing. The privacy lower bounds (Lemmas 1–2) are real and nontrivial — they establish that FedMPDD provides more than accidental obfuscation. The problem is the *framing gap*: the paper sells privacy as a first-class contribution comparable to formal DP methods, but the evidence supports a weaker claim. This is fixable by recalibrating the language and adding limitations.

- **Abstract contains a numerical discrepancy that undermines first impressions.** The abstract states the convergence rate as $O(1/K)$, while Theorem 2 (the actual theorem) proves $O(1/\sqrt{K})$. These are different rates. The theorem is the correct one; the abstract appears to have a typographical error ($1/K$ instead of $1/\sqrt{K}$). This should be corrected before publication.

- **No variance or uncertainty reporting in experimental tables.** Tables 1–2 report test accuracy and SSIM as single numbers with no standard deviations, confidence intervals, or repetition across random seeds. Given that the method injects randomness through projection vectors, client sampling, and data splits, reporting variability is essential to assess stability and reproducibility. This is not a fatal flaw (many FL papers share this limitation), but it is a significant gap for a paper that makes quantitative comparisons.

### Minor

- **Privacy evaluation is narrow.** Only two specific gradient inversion attacks are tested, and the sole metric is SSIM of full-image reconstruction. This does not exhaust the threat space: a determined adversary could combine information across rounds, leverage multiple observed projections, or apply different optimization objectives. The paper should at minimum discuss these limitations rather than extrapolating to a general "privacy protection" claim.

- **Client computation cost is not empirically verified in the main paper.** Remark 1 claims that the $O(dm)$ encoding cost can be offset by Jacobian-vector products (avoiding explicit gradient computation), but the only runtime reference points to a "follow-up study" and an appendix table. For a method that adds per-client computation beyond standard FedSGD, wall-clock time experiments or explicit complexity measurements in the main evaluation section would substantially strengthen the practical feasibility claim.

- **No formal DP adversary bound or sensitivity analysis.** Even a simple relaxation — e.g., bounding $\|\frac{1}{m}UU^\top g\| \leq \|g\|$ (which follows from the JL bound) and computing the sensitivity of the projected gradient to a single data point — would add rigor without requiring a full DP mechanism. The absence of such analysis makes the privacy comparison to LDP fundamentally apples-to-oranges.

### Trivial

- **Lemma 1's formula $(d-1)/m$ is stated without derivation in the main text.** The formula is correct (verified via elementary variance calculation for Rademacher vectors), but a brief justification or explicit reference to the appendix derivation would help readers who may find the $(d-1)/d \approx 1$ residual at $m=d$ counterintuitive (it arises because $m=d$ random $\pm1$ vectors still have off-diagonal noise in $(1/d)UU^\top$).

## Nice-to-Haves

- Replace or supplement the LDP privacy baselines with methods that combine formal DP with compression (e.g., the approach of Amiri et al. 2021, mentioned in related work but not compared). This would clarify whether FedMPDD's obfuscation is complementary to, or competitive with, formal DP at equivalent communication cost.
- Report the empirical distortion $\epsilon$ achieved at the chosen $m$ values (i.e., verify that $m = O(\log(d)/\epsilon^2)$ holds with a concrete $\epsilon$) to connect the theory more directly to the experiments.
- Include wall-clock runtime comparisons for client-side computation, even for a single representative setup.

## Removed Points

- *"The convergence analysis relies on a high-probability bound that is not reflected in the practical choices of $m$; $m \ll \log d$"* — **Removed (factually incorrect).** The JL condition is $m = O(\log(d)/\epsilon^2)$, not $m = O(\log d)$. With $m=600$ and $\log d \approx 12$ (for $d\approx 160k$), the implied distortion is $\epsilon \approx \sqrt{12/600}\approx 0.14$, which is entirely reasonable. The critic compared $m$ to $\log d$ directly while ignoring the $1/\epsilon^2$ factor.
- *"Lemma 1's formula $(d-1)/m$ seems implausibly large when $m=d$"* — **Removed (strawman).** The formula is mathematically correct for random $\pm 1$ vectors: even with $m=d$ projections, $(1/d)UU^\top$ is not the identity — its off-diagonal entries have variance $1/d$, producing a residual squared error of $(d-1)/d$ in expectation. This is a well-known property of random projections, not an error in the paper.
- *"No discussion of how to set $\delta$ for the high-probability bound over $K$ rounds"* — **Removed (addressed in paper).** The paper states it selects $m = O(\log(d/\delta)/\epsilon^2)$ for sufficiently small $\delta,\epsilon$, and provides empirical validation across $m$ values in Appendix A. The high-probability guarantee is per-round, and a union bound over $K$ rounds is standard but not a missing requirement for the paper's claims.
- Various formatting/style nitpicks and speculation about missing appendix content — **Removed (parser artifacts / no content to verify).**

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about Lemma 1's formula being counterintuitive at $m=d$ is resolved by noting that random $\pm 1$ vectors do not form an orthonormal basis even at full rank, so the residual is real — but this is a feature of the analysis, not a flaw. The strength finder's observation that the privacy guarantee is "magnitude-independent" captures a genuine advantage over LDP that is worth highlighting in the paper's discussion.

## Suggestions

1. **Recalibrate the privacy framing.** Replace "private federated learning" and "inherent privacy" with more precise language: "resistance to exact gradient reconstruction via rank-deficient projection" or "obfuscation against gradient inversion attacks." Add a limitations paragraph explaining what the Lemmas 1–2 guarantees do and do not cover (e.g., no guarantee against attribute inference, membership inference, or cross-round information aggregation). If the authors wish to retain a formal privacy claim, add a sensitivity analysis of the projected gradient and couple it with a standard DP mechanism (Gaussian or Laplace) on the compressed message.

2. **Fix the abstract convergence rate.** Change $O(1/K)$ to $O(1/\sqrt{K})$ to match Theorem 2.

3. **Add error bars.** Report means and standard deviations over at least 3 random seeds for all main experimental tables.

4. **Provide client-side runtime measurements.** Even a single table showing wall-clock time per round for FedMPDD vs. FedSGD vs. baselines on one representative setup would significantly strengthen the practicality claims in Remark 1.

## Score and Decision

### Calibration Protocol

**Round 1 — Bracketing.** Queried for papers on "federated learning communication efficient privacy gradient compression random projection" in three bands:
- Weak band (avg ≤ 3.5): Retrieved anchors with scores 2.0–3.33 (random projection privacy, federated continual learning, CUR decomposition). These papers had fundamental flaws — unclear methodology, insufficient evidence, or weak contributions.
- Middle band (3.5 < avg ≤ 7.5): Retrieved MAPO (4.0), DP-GRAPE (5.0), SGMM (4.0), Log-Bit (4.0), ADI (4.67). These papers have solid core contributions but clear limitations.
- Strong band (avg > 7.5): Retrieved papers on kernel functions, matrix sign methods, multilevel control functionals — topically irrelevant to this paper.

**Initial bracket:** 4.0–6.0 (FedMPDD is clearly stronger than the weakest band papers and topically different from the strong band).

**Round 2 — Narrowing.** Queried within (3.5, 6.0) for communication-efficient FL and within (4.0, 7.0) for gradient inversion defense:
- MAPO (4.0): Communication-efficient projection method. Rejected. Novel but with limited novelty, weak theory, and insufficient baselines. FedMPDD has stronger theory (convergence proof for multi-projection, JL-based analysis) and more comprehensive evaluation.
- GradientHide (4.5): Defense against gradient inversion attacks. Rejected on limited novelty and insufficient experiments. FedMPDD's privacy evaluation is comparable (both test against GIAs with SSIM), but FedMPDD has the additional contribution of communication efficiency with convergence guarantees.
- DP-GRAPE (5.0): DP + random projection for memory efficiency. Rejected with scores 4,4,6,6. Similar approach (random projections) but different setting (centralized DP training vs. FL). Comparable theoretical rigor. FedMPDD is slightly weaker on privacy (no formal DP) but stronger on communication efficiency (new algorithmic paradigm).
- SGMM (4.0): Private federated LoRA. Rejected. Limited experiments, incremental contribution. FedMPDD is clearly stronger.
- ADI (4.67): Communicative compression + weighting. Accepted as poster (scores 6,4,4). Comparable novelty and theory, but limited to convex analysis. FedMPDD has non-convex guarantees which is more relevant for deep learning.

**Final calibration:** FedMPDD sits above MAPO (4.0), GradientHide (4.5), and SGMM (4.0) due to stronger theory, more novel algorithm, and broader evaluation. It is comparable to DP-GRAPE (5.0) and ADI (4.67) in rigor but has the distinct weakness of oversold privacy claims, which the compared anchors do not share. Weighting this, FedMPDD lands at 5.0 — a solid paper with a real contribution held back by a significant framing gap that a revision could address.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>