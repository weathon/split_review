## Summary
The paper proposes SWAP, an entropic Wasserstein regression (EWR) formulation for one-shot network pruning that generalizes the sparse linear-regression (LR) formulation used by recent FIM-based pruners (LR is recovered as Π = diag(1/n), ε = 0). The authors argue that the implicit "neighborhood interpolation" induced by the OT plan averages gradients within neighborhoods while preserving covariance information, providing robustness to noisy gradients, and validate this on MLPNet/MNIST, ResNet20/50/CIFAR-10, and MobileNetV1/ImageNet under clean and noisy-gradient conditions.

## Strengths
- **Clean unification with prior LR pruners.** The observation that the LR formulation of Chen et al. (2022) / Benbaki et al. (2023) is exactly the ε = 0, Π = diag(1/n) special case of the EWR objective (eq. 10) is a genuinely useful reframing and immediately motivates the generalization.
- **Conceptually novel OT framing for pruning.** Casting FIM-based pruning as a sliced-Wasserstein problem on gradient projections ∇ℓᵢᵀw vs. ∇ℓᵢᵀw̄ is a fresh angle for the pruning literature.
- **Consistent empirical gains in the noisy-gradient regime vs. LR.** Tables 2–3 show that EWR reduces test loss against LR across multiple sparsity × noise settings (up to 8.13% on MobileNetV1 at 0.75 sparsity / 25% noisy data / 2σ), with 90% CIs reported over 10–25 runs — better statistical hygiene than is typical in pruning papers.
- **Strong high-sparsity accuracy relative to the methods reported.** On MobileNetV1 at sparsity ≥ 0.6 and ResNet20 at sparsity ≥ 0.8, EWR clearly dominates MP/WF/CBS where they are reported, and edges out LR by 1–3 pp at extreme sparsity (Table 1).

## Weaknesses

### Fatal
None. The core empirical contribution stands even if the theoretical argument is loose.

### Major
- **Theorem 1 ("Convex Hull Distance Equality") is not correct as stated, and the noise-reduction narrative leans on it.** The theorem asserts that for any probability measure ν on S, the point y' = ∫y dν satisfies ‖x − y'‖² = ∫‖x − y‖² dν. By the bias–variance identity, ∫‖x − y‖² dν = ‖x − E[y]‖² + Var(ν), so equality holds only when ν is a Dirac. The "Neighborhood Interpolation" derivation in Section 3 (the equalities defining yᵢ′ and xᵢ′ and the Kᵢ⁽¹⁾/Kᵢ⁽²⁾ decomposition in eq. 8/eq. 11) is built on this identity. The authors appear to mean a different statement — "for any ν there exists a measure ν' on Conv(S) such that the identity holds" — but the existence claim is not proved in the body and is not made precise. At minimum the theorem needs a corrected statement and an argument (or it should be presented as a bound, with the residual variance retained downstream).
- **The trace-variance argument treats the OT plan as data-independent.** Section 3 derives trace(Σᵢ′) = (Σⱼ νⱼ⁽ⁱ⁾²) trace(Σ) ≤ trace(Σ) by treating νⱼ⁽ⁱ⁾ as fixed convex coefficients. But νⱼ⁽ⁱ⁾ are determined by the Sinkhorn plan Π computed from the cost matrix on the noisy gradients themselves, so the variance computation omits the coupling between ν and ∇ℓ. The claimed "balance" between covariance preservation and noise reduction is therefore asserted, not demonstrated; there is no ε-sweep that quantifies the bias–variance trade-off in between the ε → 0 (LR) and ε → ∞ (uniform averaging) limits.
- **Headline abstract numbers overstate the measured gains.** The abstract advertises "6% improvement in accuracy and 8% improvement in testing loss for MobileNetV1 with less than one-fourth of the network parameters remaining." The 8% loss number matches Table 3 (MobileNetV1, 0.75 sparsity, 25% noisy data, EWR vs LR). The 6% accuracy number is not visible in Table 1 against any contemporary baseline: at sparsity 0.8 (closest to "one-fourth remaining") EWR=66.82 vs LR=65.72 (~1.1 pp), and vs CBS/WF/MP those baselines have already collapsed (16.38/0.24/0.11). The cleanest reading of Table 1 in the regimes the paper claims to win is that EWR beats LR by 1–3 pp; the abstract should be tightened accordingly.
- **The "outperforms SoTA at high sparsity" claim is really "outperforms LR at high sparsity."** In every sparsity row where the paper reports its biggest wins (ResNet20 ≥ 0.95, ResNet50, MobileNetV1 ≥ 0.9, and all noisy rows), the MP/WF/CBS columns are "–". The only live comparator there is LR, of which EWR is a strict superset (Π = diag(1/n)). The paper's strongest claims are therefore against a single baseline that the proposed method nests, which materially weakens the "SoTA" framing.
- **Motivating scenarios are not actually tested.** The introduction motivates the method with federated learning, analog-memory deployment, and adversarial data poisoning, but none of Tables 1–3 instantiate any of these: noise is injected directly on a fraction of data points at synthetic σ/2σ levels. The robustness contribution should either be evaluated under at least one of the motivating settings or the motivation should be scoped down.

### Minor
- **OT solver is missing from Algorithm 1.** Π appears in line 7's gradient but is never assigned in the pseudocode; Sinkhorn iteration count, stopping criterion, and how/when Π is recomputed across the outer SGD loop are not stated in the body. A two-line addition would fix this.
- **Noise model is under-specified.** "20% of data is with noise," "noise = σ vs 2σ," "10%/25% noisy data" are used without saying whether noise is on inputs, labels, or gradients, what distribution it is drawn from, and what σ is normalized against. The robustness story is the paper's central distinguishing claim and the protocol should be unambiguous in the body.
- **Sample-complexity paragraph is a one-liner.** The O(1/√n) vs. O(1/n^{1/4}) claim is asserted in a single sentence with no reference to a specific result or tie back to pruning; either expand or remove.
- **Table 1 protocol unclear.** Whether Table 1 numbers include fine-tuning, re-training, or are purely one-shot is not stated (Tables 2–3 are explicitly "no fine-tuning"). ResNet50 numbers on CIFAR-10 (~83% at 0.95) are notably below typical retrain-after-prune numbers in the literature for a network of this capacity, which is fine if intended but deserves a sentence of context.

### Trivial
None retained (formatting issues in the parsed text are not author errors).

## Nice-to-Haves
- An ε-sweep on at least one (network, sparsity) pair, plotting test loss/accuracy as ε varies between 0 and ∞, to make the "balance" claim concrete.
- A wall-clock comparison vs LR/CBS to substantiate the "marginal additional cost" claim quantitatively.
- One experiment matching a motivating setting (FL gradient skew, analog-memory weight noise, or label-poisoning) instead of generic per-sample noise.
- A corrected statement of Theorem 1 framed as existence on Conv(S), with the residual variance retained when the inequality direction is used downstream.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- *"Missing comparison to oBERT / M-FAC / SparseGPT / fast-OBC."* Removed per the no-external-references rule — I cannot verify which contemporary baselines are appropriate without external sources. The more general weakness (only LR is a live comparator in the high-sparsity regime) is retained above.
- *Generic strength: "the paper addresses an important problem of efficient pruning."* Dropped as non-specific.
- *Strength: "the theoretical analysis provides a clear, principled explanation of noise mitigation."* Conflicts with the verified Major weakness about Theorem 1 and the trace argument; per the rule "when a strength and weakness disagree, the weakness wins," this strength is dropped.

## Novel Insights
The genuinely novel observation is the algebraic identity LR-pruning = (ε=0, Π=diag(1/n)) EWR-pruning, which suggests a one-parameter family of FIM-based pruners interpolating between per-sample LR (no smoothing) and global-mean averaging (full smoothing) via Sinkhorn ε. This is a clean conceptual handle that could outlast the specific algorithm proposed here. Beyond that, the reviews do not surface insights independent of the paper's own contributions.

## Suggestions
- Re-state Theorem 1 as an existence result on Conv(S) and verify the resulting Kᵢ⁽¹⁾/Kᵢ⁽²⁾ decomposition; if only a Jensen bound is available, propagate the residual variance into the noise-reduction argument honestly.
- Add an ε-sweep ablation (e.g., ε ∈ {0, 1e-3, 1e-2, 1e-1, 1, 10}) on ResNet20/CIFAR-10 at sparsity 0.95 with and without noise.
- Specify Sinkhorn iteration count, stopping tolerance, and ε in Algorithm 1; state Π's assignment explicitly.
- Define the noise model precisely (where injected, distribution, σ normalization) in Section 5.
- Soften the abstract: replace "6% / 8%" framing with the specific comparisons (vs LR, at this sparsity and noise level), and replace "outperforms SoTA" at high sparsity with "outperforms LR; MP/WF/CBS do not produce usable models at these sparsities."
- Run at least one experiment under an FL-style gradient or label-noise setting to ground the motivation.

---

**Quality dimensions.** *Originality:* solid — the EWR/sliced-Wasserstein framing of FIM-pruning is fresh. *Importance:* moderate — robust high-sparsity pruning is genuinely useful. *Claim support:* mixed — empirical claims vs LR are well-supported with CIs, but the theoretical claims (Theorem 1, trace argument) and the "SoTA" framing in the abstract are not. *Soundness of experiments:* mostly adequate but with under-specified noise protocol and a thin comparator set in the headline regime. *Clarity:* generally clear, but the Section 3 derivation hinges on an identity that is not correctly justified. *Value:* the LR-as-special-case viewpoint and consistent noise-robustness gain over LR are a real contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>