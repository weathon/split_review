Now I have a comprehensive understanding of the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary

FedMPDD proposes a federated learning algorithm that compresses each client's gradient into \(m \ll d\) scalars by computing directional derivatives along \(m\) random projection vectors. The server reconstructs an aggregated gradient estimate by projecting these scalars back onto the same random vectors (regenerated from transmitted seeds). The authors claim two benefits: (1) communication efficiency via \(O(m)\) uplink cost, and (2) inherent privacy against gradient inversion attacks from the rank-deficient projection. A Johnson–Lindenstrauss argument is used to claim \(O(1/\sqrt{K})\) convergence with \(m = O(\log d)\).

## Strengths

- **Novel compression mechanism with practical design**: The use of multiple random projected directional derivatives — each client transmits \(m\) scalars plus a seed — is genuinely novel for FL. The Rademacher distribution choice for lower variance (Lemma 3) and the seed-based server-side reconstruction are well-motivated and practical.

- **Strong communication efficiency demonstrated empirically**: Under fixed bit budgets and target-accuracy constraints (Tables 1–2, Figure 3), FedMPDD achieves dramatic uplink savings — e.g., reaching 60% accuracy on CIFAR-10 using 1.32 GB vs. FedSGD's 471.96 GB (\(>350\times\) reduction) — while outperforming QSGD, Top-k, lp-proj, and SA-FedLora in the low-budget regime. The bit-vs-accuracy curves are convincing.

- **Comprehensive experimental evaluation**: Experiments cover three datasets (MNIST, FMNIST, CIFAR-10), four model architectures, IID and non-IID splits, and multiple client participation rates (10%, 50%, 100%). The ablation over \(m\) values (Appendix A.9) demonstrates the tunable trade-off.

- **Clear algorithm specification**: Algorithms 1–2 are presented with sufficient detail, and the encoding/decoding strategy using seeds for server-side reconstruction is practical and well-described.

## Weaknesses

### Fatal

None.

### Major

- **Convergence proof contains a genuine technical gap at the JL-to-expectation transition (Theorem 2)**. The proof at Eq. (32)–(33) attempts to bound \(\mathbb{E}[\|\hat{\mathbf{g}}_i(\mathbf{x}_k)\|^2] - \mathbb{E}[\|\mathbf{g}_i(\mathbf{x}_k)\|^2]\) by applying the JL high-probability bound (\(\|\frac{1}{m}UU^\top\mathbf{g}\|^2 \leq (1+\epsilon)^2\|\mathbf{g}\|^2\) w.p. \(\geq 1-\delta\)) and then wrapping it in an expectation without accounting for the failure probability. This is problematic because Lemma 1 independently establishes \(\mathbb{E}[\|\hat{\mathbf{g}}_i - \mathbf{g}_i\|^2] / \|\mathbf{g}_i\|^2 = (d-1)/m\), which for \(m = O(\log d)\) gives a relative error of \(\approx d/\log d\) — far from \(\epsilon^2\). The JL high-probability event cannot be directly converted into an expectation bound without bounding the contribution of the \(\delta\)-probability failure events, where the norm inflation can be substantial for Rademacher matrices. This means the claimed \(O(1/\sqrt{K})\) rate with \(m = O(\log d)\) is not properly justified by the current proof. The empirical results are unaffected, but the central theoretical claim is unsupported as stated.

- **Privacy claims are overstated relative to what is actually shown**. The paper describes FedMPDD as providing "inherent privacy," "uniform privacy protection," and a "privacy guarantee" (e.g., Section 2, Remarks 2 and 5, Abstract). What is actually established is: (i) Lemma 1 bounds the expected *gradient* reconstruction error (not data reconstruction error), and (ii) Lemma 2 lower-bounds data reconstruction error under a Lipschitz condition whose constant may be large in practice. The rank-deficiency argument (\(\text{rank} < d\) prevents unique gradient recovery) is a genuine mechanism that makes GIA harder, but it does not constitute a formal privacy guarantee — the attacker knows the exact projection matrix \(\mathbf{U}\) (from seeds) and can optimize in input space using the observed scalar projections directly. The comparison with LDP in Remark 5 frames FedMPDD as having "consistent relative reconstruction error" independent of gradient magnitude, but this is comparing an expected error over random projections (which the adversary observes exactly each round) against LDP's noise-based error. These are fundamentally different quantities. The paper would be on stronger ground framing FedMPDD as an empirical defense against GIAs rather than claiming "privacy guarantees."

### Minor

- **LDP baselines are not properly calibrated**. The experiments compare against FedSGD + Laplace noise with fixed variances (0.1, 0.5, 1, 10). No (\(\epsilon, \delta\))-DP budget is reported, and the noise levels are not calibrated to a standard privacy definition. This weakens the claim that FedMPDD "outperforms" privacy-preserving methods. However, the comparison still serves its purpose of showing that naive noise injection either fails to protect privacy or destroys accuracy, while FedMPDD provides a middle ground. The paper does not claim these baselines represent formal LDP with specific (\(\epsilon, \delta\)) budgets, so this is a presentation issue rather than a fatal flaw.

- **Gradient inversion attack evaluation could be more thorough**. The privacy evaluation uses two attack methods (DLG and Yu et al. 2025) and reports SSIM. It is not demonstrated whether these attacks are properly tuned for the projected setting (e.g., whether the attacker exploits the known projection matrix \(\mathbf{U}\) by projecting dummy gradients before comparison). A negative result with poorly-tuned attacks does not constitute strong evidence of privacy. That said, the SSIM values are consistently low across training (Figure 1), which provides reasonable empirical support.

### Trivial

- The paper's conversion between its notation for the projected directional derivative and the standard gradient notation contains some redundancy (e.g., Eq. (3) is repeated with different formatting at lines 301–303 and 315–321), likely a PDF-parser artifact in the version reviewed but worth cleaning up.

## Nice-to-Haves

- It would strengthen the paper to compare against a method that combines compression with formal DP (e.g., CP-SGD, DP-SignSGD, or a quantized+DP scheme with a declared (\(\epsilon, \delta\)) budget), to properly contextualize the privacy-communication trade-off.
- An investigation of whether adding calibrated noise to the scalar projections could yield a formal LDP guarantee at lower per-dimension cost than full-vector LDP would be a natural and compelling extension.
- Time-to-accuracy plots (wall-clock) would complement the bit-vs-accuracy curves and address concerns about per-round computational overhead of \(O(dm)\) at the server.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *Harsh Critic claim: "The bound \(T \times m < d\) for multi-round privacy (Remark 2) is presented as a fundamental guarantee, but it only speaks to unique gradient recovery under a static-gradient assumption, which is both unrealistic and not equivalent to data privacy."* → **Removed.** Remark 2 explicitly states "in a worst-case scenario (e.g., a static gradient)" — the paper is transparent about the assumption. Presenting a worst-case bound under stated assumptions is standard practice. The paper also notes that "the natural evolution of gradients during training provides stronger practical protection."

- *Harsh Critic claim: "Lemma 2's lower bound derivation contains algebraic errors (e.g., the step where the projection error is subtracted from the Lipschitz bound without proper justification for the inequality direction)."* → **Removed.** The derivation uses reverse triangle inequality (\(\|a-b\| \geq |\|a\| - \|b\||\)) which is standard and correct. The critic's specific objection is not substantiated upon inspection.

- *Harsh Critic claim: "The server must regenerate all random directions, which incurs \(O(dm)\) computation per client per round at the server."* → **Removed.** The paper explicitly acknowledges this in Remark 1 and discusses computational costs in Appendix F, including strategies to mitigate overhead (projected-forward approach). This is not a hidden cost.

- *Strength Finder claim: "Comprehensive evaluation... rigorous privacy analysis."* → **Removed from strengths.** The privacy analysis is not rigorous — it provides expected-error bounds, not formal privacy guarantees. While the experimental evaluation is broad, the privacy framing is overstated (see Major Weakness).

- *Strength Finder claim: "Careful analysis of distribution choice... convergence proofs are complete and well-structured."* → **Partially removed.** The Rademacher variance analysis (Lemma 3) is valid and correctly credited. However, "convergence proofs are complete" conflicts with the verified major weakness about the JL-to-expectation gap. The proof structure is clear, but completeness is compromised.

## Novel Insights

The most genuinely novel observation from this reviewing process is the tension between Lemma 1's expectation bound and the JL high-probability bound. Lemma 1 shows \(\mathbb{E}[\|\hat{\mathbf{g}} - \mathbf{g}\|^2]/\|\mathbf{g}\|^2 = (d-1)/m\), which requires \(m = \Omega(d/\epsilon^2)\) to achieve relative error \(\epsilon^2\). The JL lemma suggests only \(m = O(\log d/\epsilon^2)\) suffices for norm preservation with high probability. The resolution is that the JL failure events (probability \(\delta\)) contribute disproportionately to the expectation, meaning the high-probability convergence analysis cannot be trivially converted to an expectation bound without additional work — a subtlety worth highlighting for future work on JL-based compression in optimization.

## Suggestions

- **Fix the convergence proof**: Either (a) derive a high-probability convergence guarantee that explicitly carries \(\delta\) through and shows it can be made arbitrarily small without harming the rate, or (b) bound \(\mathbb{E}[\|\frac{1}{m}UU^\top\mathbf{g}\|^2]\) directly using the exact expectation (which follows from Lemma 1) and accept that \(m = \Omega(d/\epsilon^2)\) is needed for the current proof structure, then find alternative arguments to improve the dependence. The second approach would be more honest but would weaken the claimed rate.

- **Recalibrate privacy claims**: Frame FedMPDD as providing "empirical defense against gradient inversion attacks" rather than "privacy guarantees." Remove language like "uniform privacy protection" that implies a formal guarantee. The rank-deficiency argument is a genuine defense mechanism; present it as such without overclaiming.

- **Strengthen the attack evaluation**: Either (a) design a stronger attack that explicitly leverages the known projection matrix \(\mathbf{U}\) (projecting dummy gradients before comparison), or (b) explicitly argue why existing GIA formulations already account for this. Report attack hyperparameters (iterations, learning rates) to demonstrate fair evaluation.

## Score and Decision

### Anchor Comparison

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/jAYHFBdQ0M.md` (JL Transforms) | 3.50 | Similar JL-based compression for distributed optimization. FedMPDD has a more novel algorithm, stronger experiments, and broader evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/fSRmZ7P1kb.md` (Log-Bit) | 4.00 | Also compresses to scalars via projections. FedMPDD has much stronger experiments (non-convex DNNs vs. convex only), better practical applicability, and no unrealistic persistent-excitation assumptions. |
| `/home/wg25r/review_agent/human_reviews_2026/Y6lVVJHiwN.md` (FedSGM) | 4.40 | Unified compression framework with strong theory. FedMPDD has better empirical results but weaker theory due to the proof gap. Overall comparable contribution level. |
| `/home/wg25r/review_agent/human_reviews_2026/Hude2v2AEX.md` (Discrepancy-aware) | 5.00 | Solid communication compression paper with clear contribution. FedMPDD has similar empirical strength and adds privacy as a side benefit, though the privacy framing is less rigorous. |
| `/home/wg25r/review_agent/human_reviews_2026/PSmakC4sw5.md` (Composite EF) | 6.00 | Strong theoretical contribution resolving a fundamental gap. FedMPDD's theoretical contribution is weaker due to the unresolved proof gap. |
| `/home/wg25r/review_agent/human_reviews_2026/xzJrPSlMS4.md` (Diminishing Noise DP) | 2.00 | Privacy-focused FL paper with weak contribution. FedMPDD is substantially stronger in both novelty and empirical validation. |

FedMPDD introduces a genuinely novel compression mechanism with strong empirical results. However, the main convergence theorem has a verifiable proof gap and the privacy claims are overstated. These issues are fixable in revision (tightening the proof, recalibrating privacy language). Relative to the anchor papers: it clearly outperforms the 3.50–4.00 tier in novelty and experimental quality, is comparable to the 4.40–5.00 tier but with a weaker theoretical foundation than the 6.00 paper. A score of **5.0** reflects solid contributions with significant but addressable weaknesses.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>