## Summary
The paper proposes NVDP (Nonparametric Variational Differential Privacy), a method for sharing privacy-preserving transformer embeddings by inserting an NVIB (Nonparametric Variational Information Bottleneck) layer into a BERT-based architecture. Sampled embeddings are measured for privacy via Rényi Divergence (RD) and its Bayesian Differential Privacy (BDP) conversion. The paper empirically demonstrates that NVDP achieves a better privacy–utility trade-off than a VIB-based ablation (VTDP) across several GLUE tasks.

---

## Strengths

- **Novel architectural integration of NVIB with privacy measurement**: The paper proposes a concrete design (Figure 1, Section 3.1) that removes the residual skip connection around the denoising attention block to prevent un-sanitized embeddings from bypassing the stochastic bottleneck. This is a specific and principled design choice, not a generic adapter.

- **Derivation of a computable RD bound for the NVIB posterior**: Equation 7 (Section 3.3) derives a closed-form upper bound on the Rényi divergence between two NVIB sampling distributions by decomposing the DP posterior via its factored representation (Eq. 6) and aligning token positions. This enables privacy measurement without Monte Carlo approximation.

- **Empirical evidence for NVIB's advantage over VIB**: Table 1 consistently shows NVDP improving on VTDP in both utility and privacy. On MRPC, NVDP achieves 83.0% accuracy with BDP 10.70 and RD 0.34, vs. VTDP's 81.1% accuracy with BDP 11.50 and RD 1.20. Figure 2 further shows the full trade-off curves across all GLUE tasks favor NVDP.

- **Dual-perspective privacy evaluation**: Reporting both worst-case RD and the BDP conversion (which marginalizes over alternative inputs) gives both a strict upper bound and a more practically interpretable guarantee. The distinction is clearly motivated in Section 3.2.

---

## Weaknesses

### Fatal
*None that are unambiguously verifiable from the text alone.*

### Major

- **Privacy measurements are empirical test-set statistics, not formal guarantees over all inputs.** Section 4.1 explicitly states: *"we report the worst-case divergence across all test set pairs."* A differential privacy guarantee must hold for *all* possible pairs of inputs, not those that appear in the GLUE test corpus. The paper does derive a mathematical upper bound (Eq. 7) that in principle could yield per-input bounds, but this bound is evaluated only on the test corpus rather than maximized over all inputs (e.g., by optimizing over the model's parameter space or proving a universal bound). This means every number in Table 1 is an empirical lower bound on the true worst case, not a DP guarantee. For a paper whose core selling point is privacy protection, this gap between the mathematical machinery (Eq. 7) and how it is actually deployed in evaluation is a substantive problem.

- **No adjacency relation is defined, making the RDP guarantee non-standard.** Section 3.2 explicitly states: *"We do not assume any specific notion of adjacency between examples."* Standard RDP requires a defined adjacency relation specifying which pairs of inputs must produce indistinguishable outputs. Without it, Definition 2.2 is not instantiated, and the reported RD values conflate privacy protection with a generic semantic-similarity measurement (a medical text and a sports text should have high divergence, but this reflects semantics, not a privacy failure). The BDP framing is more defensible because it marginalizes over the data distribution, but the RD column in Table 1 is then uninterpretable as an RDP guarantee.

- **No comparison to any method that actually provides differential privacy.** All baselines — vanilla BERT and BERT+Dropout+WD — offer zero DP protection. There is no comparison to DP-SGD (Abadi et al., 2016) or any existing privatized-embedding method. Without a DP-aware baseline, neither the privacy numbers nor the utility numbers can be interpreted in the context of the broader DP-for-NLP literature. The paper cannot support its claim of "effective tradeoff" without at least one such reference point.

- **BDP ε values of 10–22 are large and the claim of "strong privacy guarantees" is unsupported.** Reported BDP(ε_μ) values range from 10.70 (MRPC) to 22.20 (STS-B) in Table 1. While BDP is a different and arguably weaker notion than standard DP, the paper does not provide any argument for why these values constitute meaningful privacy protection. The abstract and conclusion both assert "strong privacy guarantees" and "strong, practical privacy budgets" (Section 5), but these claims require contextualization: at what ε does BDP become practically useful, and how does BDP ε relate to standard DP ε for typical NLP threat models? This contextualization is absent.

### Minor

- **Unexplained reversal between RD and BDP rankings for QQP.** In Table 1, for QQP, NVDP has a *worse* worst-case RD (1.14) than VTDP (0.85), yet a *better* BDP (13.01 vs. 15.52). Since BDP is derived from the aggregated RD via Theorem 2 of Triastcyn & Faltings (2020), this reversal is not obviously expected. The paper does not comment on it. The likely explanation is that NVDP and VTDP are at different operating points on their λ_D/λ_G trade-off curve, but this makes the single-row comparison in Table 1 potentially misleading for QQP.

- **"Best of five runs" selection inflates utility.** Section 4.1 states: *"we perform five independent runs and select the best-performing run on the validation set."* Reporting the maximum of five runs on the test set inflates utility estimates, and these elevated utility numbers are reported alongside privacy measures computed at those same checkpoints. This is not standard evaluation practice in GLUE benchmarking.

- **No guidance on choosing λ_D and λ_G to hit a target privacy budget.** The paper shows privacy–utility curves in Figure 2 but provides no procedure for a practitioner who wants to achieve ε ≤ X. This limits practical deployability.

### Trivial

- Footnote 3 states that padding tokens are assigned (μ=0, σ=1, α=0) and that this gives a meaningful privacy measure, but does not verify that these assignments yield an upper bound rather than a lower bound on the RD — since α=0 padding terms contribute to the sum in Eq. 7 and their sign is not verified in the text.

---

## Nice-to-Haves

- The paper motivates NVDP with GAN-based and inversion-based reconstruction attacks (Section 1), yet never evaluates whether privatized embeddings resist such attacks. An empirical attack evaluation (e.g., measuring input reconstruction quality from shared NVDP embeddings) would directly validate the threat model and make the privacy claim more concrete.
- The NVIB parameters at inference time (μ, σ, α) already contain enough information to compute a per-input RD upper bound from Eq. 7. Reporting the maximum of these per-input bounds over a large training corpus would yield a proper privacy guarantee without requiring a change in architecture.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength Finder: "Dual-perspective evaluation gives both strict and average-case guarantee"** — Partially retained in Strengths, but the strict guarantee qualification is softened because, as identified above, the RD numbers are empirical statistics and not formal guarantees over all inputs.

- **Harsh Critic: "Formatting/style issues"** — No formatting criticisms were made by the harsh critic; not applicable.

- **Harsh Critic: "The bound in Eq. 7 may not hold for α=0 padding tokens"** — Retained as Trivial, but demoted from the structural concern the critic implied, since the paper acknowledges this in footnote 3 and treats it as future work.

- **Harsh Critic claim that the QQP inconsistency is "inconsistent unless the two models are at different operating points"** — The explanation (different operating points on the λ_D/λ_G curve) is likely correct; retained as a Minor presentation gap rather than a data integrity concern.

---

## Novel Insights

The main genuinely novel insight is that calibrating noise to the task via a nonparametric (Dirichlet Process) prior — which can allocate zero pseudo-count to uninformative positions, effectively dropping them — provides a better privacy-utility trade-off than isotropic Gaussian noise applied uniformly per-token. This is empirically demonstrated in Figure 2 and Table 1. The derivation in Eq. 7 that extends Rényi divergence to ordered sequences of weighted vectors sampled from a DP posterior is also technically original, though its role as a privacy *guarantee* (as opposed to an empirical privacy *statistic*) remains unestablished in the paper's current form.

---

## Suggestions

1. **Replace test-set empirical divergence with a formal per-input bound**: Eq. 7 already provides the machinery. Compute the RD upper bound for each training or validation example using its output parameters (μ, σ, α), and report the maximum as the privacy guarantee. This transforms an empirical measurement into a formal one and is a straightforward engineering change.

2. **Define an explicit adjacency relation**: Even a simple one (e.g., texts differing by at most one sentence, or all texts in the same domain) would ground the RDP guarantee and make Definition 2.2 instantiated. The BDP framing already implicitly uses the data distribution as the adjacency relation — making this explicit would improve rigor.

3. **Add a DP-SGD baseline**: Run existing open-source DP-SGD code on BERT fine-tuning for each GLUE task and report the resulting utility at various ε values. This anchors NVDP's BDP numbers in the framework the community already uses.

4. **Contextualize BDP ε values**: Provide either (a) an argument for what BDP ε ≈ 11 means in terms of adversary advantage, or (b) a conversion to a comparable standard DP or RDP guarantee. Without this, the claim of "strong privacy" cannot be assessed.

5. **Provide a tuning procedure for λ_D and λ_G**: Give practitioners a principled recipe for reaching a target privacy budget (e.g., a bisection strategy on the trade-off curve).

---

## Score and Decision

**Axes:**
- **Originality**: Moderate — NVIB exists; applying it to privacy measurement with Rényi Divergence is new, but the novelty is incremental.
- **Importance**: Moderate-to-high — Private embedding sharing is a real problem.
- **Claims supported**: Weak — The comparison to VTDP is well-supported; the claim of "strong DP guarantees" is not, due to the empirical-vs-formal issue and the large ε values.
- **Soundness**: Below average — The privacy framework has the adjacency and empirical-guarantee problems described above.
- **Clarity**: Adequate — The paper is clearly written, but key distinctions (formal vs. empirical guarantee, RDP vs. BDP rankings) are not addressed.
- **Community value**: Low-to-moderate without the missing DP-SGD baseline; the trade-off curves vs. VTDP are informative but not actionable without that anchor.

The paper presents a real and technically interesting contribution, but the core claim — providing formal differential privacy guarantees — is not upheld under scrutiny. The privacy numbers are test-set statistics, no adjacency is defined, ε values are large and uncritically claimed to be "strong," and the method cannot be placed in the broader DP landscape without a DP-SGD comparison. These are substantive issues for a venue like ICLR, which would expect a privacy paper to deliver on formal guarantees.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>2</community_value>
</subscores>