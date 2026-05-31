Now I have a thorough understanding of the paper. Let me write the review.

---

## Summary

FedMPDD proposes a framework for Federated Learning that simultaneously reduces uplink communication cost and protects against Gradient Inversion Attacks (GIAs) by compressing each client's gradient into *m* scalars—the directional derivatives along *m* independent random Rademacher vectors—which are decoded on the server via the same seeds. The core insight is that averaging *m* rank-1 projections produces an unbiased gradient estimator that (a) satisfies a Johnson-Lindenstrauss norm-preservation property with only logarithmic dependence on dimension *d*, and (b) leaves a (d–m)-dimensional nullspace that fundamentally limits adversarial gradient reconstruction. The paper provides convergence guarantees (O(1/√K) for nonconvex objectives), formal lower bounds on GIA reconstruction error (Lemmas 1–2), and experiments on MNIST/CIFAR-10 with multiple architectures.

---

## Strengths

- **Novel joint mechanism:** The paper introduces a compelling "encode as projections, decode by re-seeding" paradigm that achieves communication reduction *and* a provable privacy barrier through a single geometric construction rather than bolting on additive noise after the fact. The unbiasedness of the projected directional derivative (E[u(uᵀg)] = g for zero-mean, unit-variance u) is carefully established and distinguishes this from biased sketched approaches.

- **Rigorous JL-based convergence:** Theorem 2 cleanly connects the JL operator-norm bound (Lemma 6) to the choice m = O(ln(d/δ)/ε²) and derives an O(1/√K) convergence rate matching FedSGD. The three-term decomposition of the bound (initialization, client sampling, projection distortion) is interpretable and well-motivated.

- **Quantified privacy barrier (Lemmas 1–2):** Lemma 1 gives a closed-form relative squared gradient reconstruction error of (d–1)/m, and Lemma 2 converts this into a lower bound on adversarial data-recovery error. This direct link between the tunable parameter *m* and privacy is more interpretable than standard DP noise calibration and is empirically confirmed (SSIM < 0.04 in Figure 1, stable across training epochs).

- **Comprehensive experiments:** The evaluation spans MNIST, CIFAR-10, multiple architectures (LeNet, CNN, ResNet), IID and non-IID splits, three participation rates, two GIA families (Yu et al. 2025; Zhu et al. 2019), and five baseline methods (QSGD, Top-k, lp-proj, SA-FedLora, FedSGD ± LDP). Table 2 shows a compelling >144× communication reduction vs. FedSGD at the same accuracy while keeping SSIM < 0.22.

- **Practical JVP angle (Remark 1):** The observation that each scalar sᵢʲ = uʲᵀgᵢ can be computed as a Jacobian-vector product without materialising the full gradient is practically important; the reduction in client-side computation when m < hpT/(h+p) connects to the broader forward-mode autodiff literature.

---

## Weaknesses

### Fatal
*None that invalidate the core claims.*

### Major

1. **Abstract–body convergence discrepancy.** The abstract explicitly states FedMPDD "converges at a rate of O(1/K), matching the performance of FedSGD," whereas Theorem 2 states O(1/√K) (with step size η = 1/(L√K)) and the contribution bullets also state O(1/√K). For a nonconvex objective, O(1/K) would require convexity or strong convexity assumptions absent here. This inconsistency undermines confidence in the theoretical presentation and should be corrected.

2. **Multi-round privacy guarantee is practically vacuous for real FL runs.** Remark 2 states privacy holds as long as T × m < d. For the CIFAR-10/CNN experiments (d ≈ 300 K, m = 600), this allows T < 500 rounds. Yet Table 2 shows FedMPDD requires ~1.32 GB to reach 60% accuracy; with 10% participation of ~10 clients at m = 600 scalars per client, each round costs ≈14.4 KB, so 1.32 GB ≈ 96 000 rounds, giving T × m ≈ 5.8 × 10⁷ >> d. The paper deflects this by noting "the natural evolution of gradients provides stronger practical protection," but this is an empirical claim, not a formal one. The gap between the stated formal guarantee and the actual training regime should be prominently acknowledged, not buried in a remark, since it significantly weakens the paper's privacy claims.

3. **Privacy is not formalised in any standard framework.** The reconstruction-error lower bound in Lemma 2 assumes the adversary uses a specific gradient-matching objective L(v̂). A more capable adversary can perform inference directly from the *m* observed scalars {u_{k,i}^{(j)ᵀ} g_i} plus the seeds, without attempting full gradient reconstruction. No mutual information, Rényi divergence, or (ε,δ)-DP bound is provided, so the paper cannot claim that FedMPDD is "private" in any standard sense beyond resistance to this specific attack class. The contrast with LDP is therefore partly unfair: LDP carries formal guarantees against any adversary, while FedMPDD's guarantees apply only to gradient-matching GIAs.

### Minor

1. **Server-side computational cost deserves explicit discussion.** Decoding requires the server to regenerate and sum N_active × m Rademacher vectors of length d per round: O(d m βN) operations. For d = 300 K, m = 2000, βN = 100, this is ~6 × 10¹⁰ operations per round. This is likely dominated by bandwidth in practice, but no analysis is provided for large-scale deployments.

2. **Relationship to seeded random sketches is understated.** Transmitting *m* projections + a seed is mechanically identical to a seeded Rademacher sketch. The claimed distinction ("dynamic vs. fixed projection") is real but not exclusive to FedMPDD; Count-Sketch and Gaussian sketch methods can also use fresh randomness per round. The privacy argument and JL-based convergence analysis are the genuine novelties over prior sketching work; the paper overstates the algorithmic distinction.

3. **Fixed-budget experimental design creates a very harsh baseline for FedSGD.** At 0.09 GB, FedSGD achieves only 11.45% on MNIST (essentially random). This arises because full-gradient FL cannot complete even one round within the budget when there are many participating clients. While this is a valid communication-constrained regime, its extreme nature should be stated explicitly, and a medium-budget comparison (where FedSGD completes at least a few rounds) would make the comparison less cherry-picked.

### Trivial

- None beyond what is already captured above.

---

## Nice-to-Haves

- A formal DP analysis (even a loose one) showing how the projection-induced noise interacts with standard Gaussian mechanism arguments would significantly strengthen the privacy claim.
- Adding FedSketch (Haddadpour et al.) as a baseline—a method that also claims joint communication and privacy—would better position FedMPDD in the landscape.
- Reporting Δ₁ = communication compression ratio at the point where FedMPDD's accuracy matches each baseline's best accuracy (rather than at a common budget) would give a cleaner communication-efficiency comparison.

---

## Novel Insights

The most genuinely novel insight is that the *rank deficiency* of the multi-projected directional derivative operator (1/m)UUᵀ serves a dual purpose: it is the very property that causes slow convergence in the single-projection variant (FedPDD), and simultaneously it is the property that prevents adversarial gradient recovery. The paper then shows that increasing *m* (and hence rank) via the JL lemma recovers FedSGD-level convergence while only logarithmically increasing communication cost—implying that the privacy-convergence tension can be resolved at an O(log d) cost rather than the O(d) cost paid by LDP to achieve comparable gradient obfuscation. The closed-form relative reconstruction error (d–1)/m, which is independent of gradient magnitude, is a clean result that explains why LDP is fragile (small gradients drowned by noise, large gradients weakly protected) while this method is not.

---

## Suggestions

1. Correct the abstract's convergence claim from O(1/K) to O(1/√K) and reconcile with the text.
2. Add an explicit discussion of when the multi-round privacy guarantee (T·m < d) is satisfied versus violated in each reported experiment, and quantify the empirical SSIM gap between the formal regime and the actual training regime.
3. Provide even an informal argument for why practical privacy holds beyond T·m = d (e.g., bounding the information in *m* scalar projections about the original data via Fisher information or mutual information).
4. State explicitly in the main text that the privacy guarantee targets GIA-class attacks only, and discuss what stronger guarantees would require.

---

## Score and Decision

The paper presents a technically sound and experimentally well-supported approach to a relevant FL challenge. The JL-based convergence framework and the geometric privacy argument are genuinely novel. The primary weakness is that the formal multi-round privacy guarantee is effectively inapplicable to the very experiments that demonstrate the method's utility, and the abstract contains an incorrect convergence claim. Neither issue invalidates the core contribution, but both represent significant gaps that should be resolved.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>