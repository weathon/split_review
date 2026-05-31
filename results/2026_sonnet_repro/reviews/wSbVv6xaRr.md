Now let me run the calibration searches to anchor the score.Now I have enough to write the final review. Let me compile it.

---

## Summary

FedMPDD introduces a communication-efficient and privacy-aware federated learning framework based on *multi-projected directional derivatives*. Each client compresses its high-dimensional gradient into $m$ scalar projections along random Rademacher vectors, reducing uplink communication from $\mathcal{O}(d)$ to $\mathcal{O}(m)$ per round ($m \ll d$). The multi-projection averaging overcomes the $\mathcal{O}(d/\sqrt{K})$ dimension-dependent convergence of single-projection FedPDD, achieving $\mathcal{O}(1/\sqrt{K})$ convergence (Theorem 2), while the rank-$(d-m)$ nullspace of the projection inherently limits gradient reconstruction. Experiments on MNIST/LeNet and CIFAR-10/CNN show strong communication reductions (e.g., 356× less bytes than FedSGD for the same target accuracy) alongside low SSIM scores under gradient inversion attacks.

---

## Strengths

- **Unbiased, dimension-free gradient estimator:** The multi-projected directional derivative estimator is unbiased (proved from $\mathbb{E}[U_{k,i}U_{k,i}^\top] = mI_d$), and via the Johnson–Lindenstrauss Lemma, achieving near-identity behavior requires only $m = \mathcal{O}(\ln(d/\delta)/\epsilon^2)$ directions—growing logarithmically, not linearly, with $d$. This overcomes the $\mathcal{O}(d/\sqrt{K})$ convergence of single-projection FedPDD in a principled way.

- **Quantified gradient reconstruction error (Lemma 1):** The paper derives a closed-form relative squared error: $\mathbb{E}_U[\|\hat{g}_i - g_i\|^2]/\|g_i\|^2 = (d-1)/m$. This is an explicit, non-asymptotic result that is independent of gradient magnitude—a genuine theoretical strength that contrasts with LDP, whose reconstruction difficulty varies with gradient norm (Remark 5).

- **Simultaneous communication and privacy gains empirically verified:** Table 2 documents that competing compression methods (lp-proj, Top-k, SA-FedLora, QSGD) achieve communication reductions but all fail on privacy (SSIM $\geq 0.74$), while FedMPDD achieves SSIM $\leq 0.22$ and the best communication efficiency (1.32 GB vs. 471.96 GB for FedSGD at 60% accuracy)—supporting the dual benefit claim.

- **Consistent privacy level across training epochs:** Figure 1 shows SSIM remains below 0.04 over 100 epochs for LeNet, empirically validating that the privacy guarantee is independent of training stage and gradient magnitude—consistent with Lemma 1.

---

## Weaknesses

### Fatal
None.

### Major

- **Abstract claims $\mathcal{O}(1/K)$ convergence; Theorem 2 proves $\mathcal{O}(1/\sqrt{K})$**. The abstract states: "establishing that FedMPDD converges at a rate of $\mathcal{O}(1/K)$, matching the performance of FedSGD." Theorem 2 and the contributions bullet both correctly state $\mathcal{O}(1/\sqrt{K})$, which is the standard rate for nonconvex SGD. Standard FedSGD also achieves $\mathcal{O}(1/\sqrt{K})$—not $\mathcal{O}(1/K)$—for nonconvex objectives. This misstatement affects the paper's central performance claim at first contact and must be corrected.

- **Privacy framing overstates the formal guarantee.** Lemma 2's lower bound on data reconstruction error is $\frac{d-1}{m \cdot L_v(\mathbf{x})^2}\|g_i\|^2$, where $L_v(\mathbf{x})$ is the Lipschitz constant of the gradient with respect to the input. This constant is neither bounded nor estimated anywhere in the paper. For a typical neural network, $L_v$ can be large, driving the bound toward zero. More fundamentally, the paper compares this result directly with LDP's $(\epsilon, \delta)$-DP guarantee—a category error, since DP is composable, adversary-agnostic, and provides worst-case guarantees, while Lemma 2 applies only to a gradient-matching adversary without side information or semantic priors. The claim in Section 2 that FedMPDD offers "a formal defense against GIAs" comparable to LDP is overstated; the paper can legitimately claim empirical resistance to the tested attacks, but the formal machinery to claim DP-comparable protection is absent.

- **Multi-round privacy composition expires within the training horizon for some experiments.** Remark 2 states: "privacy is guaranteed if $T \times m < d$." For the MNIST/LeNet experiments ($d \approx 60{,}000$, $m = 400$), this gives $T < 150$ rounds. Figure 3 runs 160 rounds, slightly exceeding the static-gradient worst-case bound. The paper notes that "the natural evolution of gradients provides stronger practical protection," but this is an informal argument without analysis. A figure or quantification of how quickly the effective nullspace erodes with gradient evolution would substantially strengthen this claim.

### Minor

- **QSGD anomalously poor result in Table 2 (12.97% on CIFAR-10 under 0.9 GB budget).** QSGD with 8-bit quantization achieves a 4× compression over 32-bit; for a ~300K-parameter CNN it should fit within the 0.9 GB budget for many rounds. The result at near-random-chance accuracy is not explained. The paper states "QSGD... exceeds the budget" is not explicitly asserted for QSGD (only for FedSGD and Laplace variants), yet the result implies it does. The paper should clarify QSGD's per-round byte cost and how many rounds it actually completes within the budget, to distinguish an algorithmic failure from a budget artifact.

- **"Defendability" column (Tables 1, 2) is binary with no defined threshold.** The ✓/✗ designation is assigned without a formal definition or SSIM threshold. It appears ad hoc and introduces subjectivity into the comparison.

- **The persistent bias term in Theorem 2.** The bound (Eq. 5) contains a term $\mathcal{O}(\epsilon G^2 / \sqrt{K})$ that does not vanish with $K$—it is an irreducible residual bias from the finite-$m$ approximation. The paper implicitly acknowledges this but claims convergence "comparable to FedSGD"; in truth, FedMPDD converges to a neighborhood whose radius depends on $\epsilon$ (and hence $m$), which is not the same as matching FedSGD in the limit.

### Trivial

- The contributions section has an inconsistency: one bullet correctly says $\mathcal{O}(1/\sqrt{K})$ while the abstract says $\mathcal{O}(1/K)$.

---

## Nice-to-Haves

- Connecting the nullspace argument to a formal privacy notion—such as mutual information bounds or a $(k, \epsilon)$-anonymity-style guarantee—would allow the privacy claim to stand on formal ground rather than relying solely on the gradient-matching adversary framing.
- A figure plotting, for each experimental setting, both the convergence round and the privacy bound expiration point $d/m$ would let readers see precisely when the worst-case guarantee holds vs. when it relies on gradient dynamics.
- Including joint privacy+communication baselines such as cpSGD (Agarwal et al., 2018) or the DP+quantization approach of Amiri et al. (2021) in the main tables would directly test whether FedMPDD improves over existing joint solutions, which is the paper's core claim.
- Reporting variance or standard deviation over multiple runs would address the inherent stochasticity of the random projection directions.

---

## Removed Points

*These points are flagged to be removed—treat them with caution.*

- **Harsh critic: "JVP implementation changes the statistical behavior of $g_i$."** The paper explicitly flags that fixing a single mini-batch across $m$ directions is an approximation addressed in a "follow-up study" (Section F). This is appropriately scoped to an appendix. The concern is legitimate as a theoretical observation, but it is not unacknowledged—remove from main weaknesses.

- **Strength Finder: "Effective tunable trade-off in Appendix A.9."** This is a genuine result but the strength is generic (every parameterized method has a trade-off). Demoted.

- **Harsh critic: "Missing comparison to FedSketch/cpSGD in experimental tables."** While a valid nice-to-have, the rule against criticizing missing baselines that would favor the author's method (and the authors do discuss these in related work) keeps this as a nice-to-have rather than a major weakness.

---

## Novel Insights

The most genuinely novel observation here is that random projection for *communication* purposes also creates a formal nullspace obstruction for gradient inversion, without any additive noise. The dual exploitation of the rank-$(d-m)$ structure—simultaneously for compression and privacy—is a non-obvious connection that goes beyond the standard DP or compression literature. The resulting privacy level being *independent of gradient magnitude* (unlike LDP) is a qualitatively different regime: for LDP, large gradients are weakly protected; for FedMPDD, protection is magnitude-invariant. This could motivate formal information-theoretic frameworks for characterizing "compression-induced privacy" as a distinct privacy primitive, distinct from both DP and $k$-anonymity.

---

## Suggestions

1. Fix the abstract: replace "$\mathcal{O}(1/K)$" with "$\mathcal{O}(1/\sqrt{K})$" and remove the "matching FedSGD" claim since FedSGD itself is $\mathcal{O}(1/\sqrt{K})$, and FedMPDD converges to a neighborhood (not to the same stationary point).
2. Tighten the privacy claim: either add a bound on $L_v$ for the experimental architectures, or explicitly restrict the claim to "gradient-matching adversaries without side information" and remove any DP comparison.
3. Add to Remark 2: for each experiment, compute $d/m$ (the static-gradient privacy expiration round) and compare it to the actual training horizon; report it in a table or figure.
4. Clarify the QSGD result in Table 2: state the per-round bytes for QSGD 8-bit and confirm whether it exceeds or fits within the 0.9 GB budget, and how many rounds it completes.
5. Define the "Defendability" threshold quantitatively (e.g., SSIM < 0.3).

---

## Score Calibration

**Round 1 Bracket (3.5 / 3.5–7.5 / 7.5+):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| zqXANcFO9T (Compressed Decentralized, err-feedback) | 1.67 | R1-weak | Weaker: much narrower contribution, no privacy, rejected |
| Jl0aEFrp11 (Bidirectional FL, lazy aggregation) | 2.75 | R1-weak | Weaker: loose analysis, no privacy, rejected |
| 0jmFRA64Vw (FedComLoc) | 3.00 | R1-weak | Weaker: standard compression without privacy angle |
| IsHWcsk4Fz (FedADM) | 3.00 | R1-weak | Weaker: proximal FL, no significant novelty |
| Zh9gz3CaWm (Model Update Distillation) | 3.75 | R1-mid | Weaker: knowledge distillation approach, rejected |
| Pv6fwGPgrA (Sparse Training FL) | 4.20 | R1-mid | Weaker: no privacy component |
| rhfOzJzsKN (MAPA, Model-Agnostic Projection) | 5.00 | R1-mid | Similar: random projection for FL communication reduction, rejected; FedMPDD adds privacy and cleaner theory |
| omrLHFzC37 (Dimension-Free FL via ZO) | 6.25 | R1-mid | Close comparison: conceptually very similar (scalar + seed transmission); DeComFL has larger-scale experiments (LLMs) but no privacy angle; one reviewer even raised the question of projecting first-order gradients—which is what FedMPDD does |
| ZuazHmXTns (PAdaMFed, parameter-free FL) | 7.60 | R1-strong | Stronger: clean adaptive method, well-executed, accepted |

**Initial bracket: 4.5–6.0**

**Round 2 Narrowing (4.5–6.0):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| rhfOzJzsKN (MAPA) | 5.00 | R2 | FedMPDD is better: more principled theory, unbiasedness proved, genuine privacy angle not present in MAPA |
| FQc7gi8XvS (FedProx+Extrapolation) | 5.75 | R2 | That paper is purely theoretical with tight analysis; FedMPDD is mixed theory+empirical but with a meaningful abstract error |
| 9TSv6ZVhvN (Accelerated FL + Compression) | 4.67 | R2 | FedMPDD is stronger: cleaner approach, dual contribution, better experiments |
| J7hIz9GXKq (Collaborative Compressors) | 5.25 | R2 | Comparable: both are theory+experiments on FL communication; FedMPDD adds the privacy angle |
| omrLHFzC37 (Dimension-Free FL via ZO) | 6.25 | R2 | FedMPDD is somewhat weaker: smaller experimental scale, abstract error, privacy claims slightly overstated |

**Position relative to round-2 anchors:** FedMPDD sits between 5.25 (J7hIz9GXKq, slightly below) and 5.75 (FedProx paper). It is clearly stronger than MAPA (5.0) due to the privacy contribution and unbiasedness proof. It is weaker than DeComFL (6.25) due to smaller experimental scope, the abstract error, and overclaimed privacy framing. The abstract error, the overstated privacy comparison with LDP, and the multi-round composition concern together weigh against a clean accept at 5.5–6.0. The paper falls comfortably at 5.0.

## Score and Decision

**Originality:** Moderate-to-good. The use of multi-projected directional derivatives in FL is novel, the dual communication+privacy insight is genuinely new, and the nullspace privacy argument is non-obvious.
**Importance:** Moderate. The joint compression+privacy problem is practically relevant; the magnitude-invariant privacy guarantee is a qualitatively new property.
**Claim support:** Partially adequate. Convergence theory is solid; privacy claims are backed only by a specific adversary model without formal DP connection; abstract overstates the rate.
**Experimental soundness:** Fair. Main trends are clearly demonstrated; QSGD anomaly in Table 2 is unexplained; no variance over runs; experimental design heavily favors compression-heavy methods.
**Clarity:** Good overall. Algorithm 2 is clearly presented; Remark 2 on multi-round privacy is honest but underanalyzed.
**Value to community:** Real but needs revision. The privacy framing revision and abstract correction are necessary before publication.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>