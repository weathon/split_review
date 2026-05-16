Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes DeCom, a federated learning algorithm that achieves **O(1) per-round communication** (uplink and downlink) by exploiting zeroth-order optimization: clients transmit only gradient scalars and reconstruct model updates from shared random seeds. The paper provides convergence guarantees under standard assumptions (O(√d/√(mPKR))) and, under a low effective rank assumption, a dimension-free rate of O(√κ/√(mRP)). Empirical results on MNIST, Fashion-MNIST, and LLM fine-tuning (OPT-125M/1.3B) show communication savings of several orders of magnitude.

## Strengths

- **Novel algorithm achieving O(1) communication per round.** DeCom's core idea—decomposing ZO gradients into a scalar and a reconstructible perturbation via shared random seeds, combined with a revert step for downlink—is clever and well-motivated. The per-round communication cost is formally independent of model dimension d, a genuine advance over existing FL compression methods.

- **First dimension-free convergence guarantee in FL under low effective rank.** Theorem 4.2 (Theorem 2 in the paper) provides a convergence rate of O(√κ/√(mRP)) that depends on the effective rank κ rather than the model dimension d. The analysis also corrects a limitation in prior low-rank analyses (Malladi et al., 2023) by properly handling the smoothness parameter μ rather than assuming μ→0.

- **Orders-of-magnitude communication savings on billion-parameter models.** Table 2 shows that DeCom fine-tunes OPT-1.3B with ≈1 MB total communication per client, compared to FedZO's ~10³ TB—a factor exceeding 10⁶. The absolute transmitted data (~1 MB) is nearly identical across model sizes (125M vs. 1.3B), directly validating the dimension-free claim.

- **Comprehensive communication complexity comparison.** Table 1 systematically compares uplink, downlink, and total communication of FedAvg, FedZO, FedCom, and DeCom, clearly illustrating where the savings come from.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Missing experimental details for LLM fine-tuning experiments.** The LLM experiments (Table 2) do not report the number of communication rounds, local steps, learning rate schedules, or training epochs used for each method. The paper references a "Sec. 7" for parameter settings, but this content was not present in the available submission. Without these details, the reader cannot verify that FedZO and DeCom were compared under controlled conditions, and the impressive communication ratios cannot be independently reproduced. This is the most significant weakness in the paper.

- **Theory-algorithm gap on shared perturbations.** The convergence analysis (Theorems 1 and 2) derives variance reduction via the 1/m factor from client averaging, implicitly assuming independent randomness across clients. However, the algorithm uses identical random seeds for all participating clients (Section 3.2, line 144: "all clients agree on one common seed"), so perturbations are shared. The variance of the averaged gradient estimator under shared perturbations does not achieve the same 1/m reduction as under independent perturbations. While this nuance likely does not change the overall rate (the dominant variance comes from the data sampling, which remains independent), the paper does not acknowledge or address this mismatch. A brief discussion or ablation (shared vs. independent seeds) would strengthen the theoretical grounding.

- **Weak support for "comparable performance" on Fashion-MNIST.** On the Fashion dataset (Figure 2), DeCom achieves lower accuracy than FedAvg and FedCom when compared at equal communication vector length. The paper's claim of "comparable performance" is defensible only against Top-k, not against the stronger first-order baselines. This should be more carefully qualified.

- **Strong assumptions in the low-rank analysis.** The local κ-effective rank assumption (Assumption 4.4) requires the Hessian to be bounded by a matrix with effective rank κ over a ball of radius 2ηdG(x_r) that scales with d. This is inherited from Malladi et al. (2023) but its validity for very high-dimensional models in the FL setting is not discussed.

### Trivial

- Line 188 (Algorithm 1): A minor formatting issue — the line `$\x_{r+1} = \x_{r} - \eta \sum_{k=1}^K\cdot g^k_{r} \cdot \z^k_r$` has a stray `\cdot` after the sum that should be removed.

- Line 432: Broken cross-reference (`Sec~\ref{sec. This observation...}`) — the appendix reference is garbled in the extracted text.

## Nice-to-Haves

- An ablation experiment comparing shared vs. independent random seeds on MNIST would directly validate the theoretical handling of variance and address the theory-algorithm gap.
- Reporting the number of communication rounds and FLOPs for the LLM experiments would make the comparison more informative.
- A discussion of privacy implications of shared random seeds would be valuable — since all clients use the same perturbation, the server (or any client knowing the seed) can reconstruct the global update direction, which may be undesirable in privacy-sensitive FL settings.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh Critic's Critical Issue #1 ("dimension-free rate still contains dimension-dependent terms"):** The reviewer claims the μ² terms in Theorem 2 introduce dimension dependence. This is **mathematically incorrect**. With the chosen μ ≤ ⁴√κ/(⁴√(mRP)√((d+3)³)), we have μ² ∝ 1/(d+3)³ (not 1/d^{3/2} as the reviewer computed). Substituting into (1/2)μ²L²(d+3)³ gives (1/2)L²√κ/√(mRP), which is dimension-free. Substituting into 4μ²L⁴d³η gives O(1/R), which decays faster than the main O(1/√R) rate and is also dimension-free. The theorem's claim is correct.

2. **Harsh Critic's claim that FedZO communication numbers are "implausible":** 1937.15 TB for FedZO on OPT-1.3B corresponds to ≈186K rounds of full-model communication (≈10.4 GB/round per client for uplink+downlink), which is a plausible number of optimization steps for ZO fine-tuning. The numbers are not implausible; the real issue is the missing experimental details (addressed above as a minor weakness). The "implausible" framing is removed; the missing-details criticism is kept.

3. **Harsh Critic's complaint about variable downlink communication:** The paper explicitly discusses this (Section 5, lines 373-376) and correctly characterizes it as an average of 2MKP scalars per round. This is adequately addressed.

4. **Strength Finder's generic strengths:** Dropped generic phrasing like "addressed an important problem" — only concrete, evidenced strengths are kept.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **For the LLM experiments:** Report the exact number of communication rounds run for each method (FedZO and DeCom), along with the learning rate schedule and local steps. This one change would resolve the most significant reproducibility concern.

2. **Add an ablation comparing shared vs. independent seeds** on the MNIST task to verify that the variance consequences are benign in practice, which would close the theory-algorithm gap.

3. **Qualify the "comparable performance" claim** on Fashion-MNIST by explicitly noting which baselines DeCom matches and which it trails.

4. **Add a brief discussion** of the privacy implications of shared random seeds.

## Score and Decision

The paper presents a genuinely novel algorithm with a clever core idea, sound theoretical foundations (the dimension-free claim is correctly supported), and impressive empirical evidence of communication savings on billion-parameter models. The weaknesses are minor and addressable: missing experimental details for the LLM experiments and a nuanced theory-algorithm gap on perturbation independence. Neither undermines the core contribution. The paper makes a clear and valuable contribution to communication-efficient federated learning.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>