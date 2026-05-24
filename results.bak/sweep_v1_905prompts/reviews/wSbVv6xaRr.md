Now I have all the calibration data I need. Let me write the consolidated review.

## Summary

This paper introduces FedMPDD, a federated learning algorithm that compresses client gradients by projecting them onto multiple random Rademacher vectors and transmitting only the resulting scalars (plus a random seed), reducing uplink communication from O(d) to O(m) where m ≪ d. The server reconstructs an approximate gradient by projecting back. The paper claims that the rank-deficient projection provides "inherent privacy" against gradient inversion attacks, provides a convergence rate of O(1/√K) matching FedSGD, and demonstrates large communication savings (up to 356×) with competitive accuracy on MNIST and CIFAR-10 benchmarks.

## Strengths

- **Large, well-documented communication savings.** Table 2 shows FedMPDD (m=600) requires 1.32 GB total uplink to reach 60% accuracy on CIFAR-10, versus 471.96 GB for FedSGD and 117.98 GB for QSGD — a 356-fold and 89-fold reduction, respectively. These savings are directly attributable to the O(m) vs O(d) message size and are consistently demonstrated across two datasets and multiple m values.

- **Formal reconstruction error bounds.** Lemma 1 derives the expected relative gradient reconstruction error as (d−1)/m, and Lemma 2 lower-bounds data reconstruction error under a Lipschitz assumption. These are genuine mathematical statements about the compression mechanism, not just empirical observations.

- **Unbiased gradient estimator with JL-based norm preservation.** The multi-projection estimator is unbiased (E[ĝ] = ∇f), and Eq. (4) guarantees with high probability that ∥ĝ∥ ≤ (1+ε)∥g∥ when m = O(ln(d/δ)/ε²). The paper correctly identifies that single-projection (m=1) suffers from O(√d) variance scaling and demonstrates that increasing m mitigates this.

- **Interesting nullspace argument for consistent protection.** Unlike LDP where relative reconstruction error scales as 1/∥g∥² (poor protection for large gradients), FedMPDD's error (d−1)/m is gradient-magnitude-independent. The empirical SSIM plots (Figure 1) confirm stable, low SSIM across training, unlike LDP baselines.

## Weaknesses

### Major

- **Overclaimed "privacy" narrative without formal definition.** The paper repeatedly characterizes FedMPDD as providing "inherent privacy," a "privacy guarantee," and a "tunable privacy-utility trade-off," but *never defines privacy in any accepted formal framework* (no differential privacy, no information-theoretic metric, no clear threat model quantification beyond reconstruction error). Lemma 1 measures *compression-induced gradient reconstruction error*, which is a property of any lossy compressor — it is not a privacy metric. Lemma 2 gives a lower bound on data reconstruction error under a specific attack loss, but this depends on a Lipschitz constant that is not quantified and does not constitute a general privacy guarantee. The paper's comparison with LDP (Tables 1–2) is framed as FedMPDD ✓ vs LDP ✗ on "defendability," but LDP with appropriate noise provides a *formal* (ε,δ)-DP guarantee that FedMPDD does not offer or compete against at any equivalent privacy budget. The privacy claims need to be either (a) dropped in favor of a more measured characterization (e.g., "reconstruction error as an obfuscation mechanism") or (b) supplemented with a rigorous differential privacy analysis. This overclaiming affects the core thesis as stated in the title and abstract.

- **Convergence analysis has an unaddressed union-bound gap.** Theorem 2 states a per-round O(1/√K) convergence rate with probability at least 1−δ, relying on the JL Lemma bound (Eq. 4) which holds per-client per-round with probability 1−δ. To obtain a global guarantee over K rounds and βN clients per round, a union bound over ∼βN·K events is required, which would force δ to be extremely small (δ′ ≈ δ/(βNK)), driving m up correspondingly (m ∝ ln(βNK/δ)/ε²). The paper does not discuss this or show how m must scale with K to maintain the stated rate. Without addressing this, the claimed convergence result is not fully verified from what appears on the page.

- **Computational cost comparison against a non-standard baseline.** Remark 1 claims computational savings by comparing the JVP approach against "full forward-mode autodiff" costing O(h²pT²) — this is not how gradients are normally computed. The standard baseline is backpropagation, costing O(d). Since one JVP also costs O(d), computing m JVPs costs O(md), which exceeds O(d) for any m > 1. The paper's saving condition (m < hpT/(h+p)) may sometimes hold, but the framing of the comparison is misleading because it benchmarks against an unusually costly strawman rather than the standard approach.

### Minor

- **No statistical significance or error bars.** All reported results appear to be single-run. Given the stochasticity of both FL training and the random projections, reporting results over multiple seeds with error bars (or at minimum, stating how many runs were performed) is standard practice for a claims paper of this type.

- **Missing direct comparison to DP methods at equivalent privacy budgets.** The paper compares FedMPDD against poorly tuned LDP (var=0.1, 0.5, 1, 10) but does not include standard DP-FedAvg or DP-SGD with calibrated noise at a known (ε,δ) level. A comparison at matched privacy budgets would be necessary to support the claim that FedMPDD's approach is preferable to DP-based approaches.

- **Defendability threshold is inconsistently applied.** Table 1 uses SSIM << 0.03 for ✓, but Table 2 marks FedMPDD as ✓ despite SSIM values of 0.14–0.22, which clearly exceed 0.03. The paper should either define the threshold per-dataset or apply it consistently.

### Trivial

- The figure captions (especially Figure 2) appear garbled ("FedSGD + Lag (m=0.1)" etc.), likely from PDF extraction artifacts.

## Nice-to-Haves

- An ablation study systematically varying m across a wider range (beyond the 3–4 values per experiment) and reporting the effect on accuracy, communication, SSIM, and wall-clock time.
- Discussion of server-to-client communication cost, which remains O(d) per round and may be a bottleneck in some deployments.
- Extension to non-IID settings beyond what is mentioned in the experimental setup (no non-IID results appear in the main paper tables).

## Removed Points

The following points from the reviewers have been removed as invalid:

1. **Claimed contradiction about FedSGD+Laplace defendability** (Harsh Critic). The critic asserted that FedSGD+Laplace(var=0.5) is marked ✓ yet the paper "later claims it fails to protect." In fact, Table 1 shows var=0.5 on MNIST with ✓, while the text discusses var=0.1 on CIFAR-10 with ✗ — different variances on different datasets. No contradiction exists.

2. **Claimed inconsistency in Figure 2 caption** (Harsh Critic). The garbled labels ("FedSGD + Lag (m=0.1)") are PDF-parsing artifacts and do not reflect the original submission. The body text correctly discusses Laplace noise with variance 0.1.

3. **Claim about unfair comparison on FedSGD+Laplace(var=10)** (Harsh Critic). FedSGD+Laplace(var=10) has SSIM=0.23 (> 0.03) and fails to reach target accuracy, hence ✗. FedMPDD has SSIM=0.14 (≤ 0.03 threshold for CIFAR-10, as evidenced by the ✓ marking) and reaches the target. The metric is applied consistently.

4. **Criticism of table "*" notation** (Harsh Critic). The notation is clearly explained in the caption: "* indicates budget exceeded in the first iteration." The table reports the accuracy achieved in the single feasible iteration, which is standard.

5. **Claimed missing related works** — You cannot verify what is missing from the paper without external knowledge; all cited references are assumed to exist.

6. **Generic "weak experiments" complaints** that lack specific anchors — the experiments use standard benchmarks, proper baselines, and two attack methods.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely recapitulate points the paper already makes or raises concerns that are partially addressable; the most novel observation that emerges from synthesizing them is that the paper's "privacy" claims and convergence guarantees operate at different levels of rigor — the reconstruction error bounds (Lemmas 1–2) are mathematically sound statements about the *compressor's properties*, while the term "privacy guarantee" suggests a formal information-theoretic or DP-level assurance that the paper does not provide. This mismatch between what is formally proven (compression error) and what is claimed (privacy) is the central structural issue.

## Suggestions

1. Substantially revise the privacy narrative: replace "inherent privacy" / "privacy guarantee" with precise language about reconstruction error, obfuscation, or "protection via information loss." If privacy in a formal sense is desired, add a differential privacy analysis showing how the projection reduces sensitivity and what (ε,δ) levels are achievable.

2. Address the union-bound gap in the convergence proof: show how m must scale with K (the number of rounds) and N (number of clients) to maintain the stated O(1/√K) rate with high probability.

3. Clarify the computational cost analysis by comparing directly against backpropagation (the standard baseline) rather than full forward-mode autodiff. Provide concrete wall-clock measurements.

4. Report experiments with multiple random seeds and error bars.

5. Include a DP-based baseline (e.g., DP-FedAvg with Gaussian noise) at a matched privacy budget to support or qualify the privacy claims.

## Score and Decision

**Round 1 bracket:** I initially placed the paper between 3.5 and 7.5, with a narrower plausible range of 4–6 after comparing against anchors in the low and middle bands.

**Round 2 narrowing:** I compared FedMPDD against several anchors:
- **LASER (5.83)**: Solid compression work with formal theory, large-scale experiments; FedMPDD is weaker — it has unaddressed theory gaps and a more significant overclaiming problem.
- **FeDLRT (5.50)**: Good convergence guarantees, limited experiments; FedMPDD has stronger empirical communication results but weaker theoretical rigor.
- **MAPA (5.00)**: Similar projection-based FL compression; MAPA overclaims model-agnosticism, but FedMPDD's privacy overclaim is more central to its contribution. FedMPDD is comparable to slightly weaker than MAPA.
- **Ferret (4.67)**: Random projection for LLMs; criticized for limited novelty. FedMPDD has stronger empirical results but the privacy overclaim is a larger issue than Ferret's novelty concerns.
- **FedLoRU (4.00)**: Heuristic low-rank method with weak theory; FedMPDD is clearly stronger.

These anchors confirm the paper sits between 4.0 and 5.0, closer to MAPA/Ferret than to LASER/FeDLRT. The core compression contribution is real and well-demonstrated, but the privacy overclaiming and convergence theory gaps prevent it from reaching the 5+ range. Score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>