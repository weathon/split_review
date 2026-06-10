Now let me produce the final review in the required format.

## Summary
This paper proposes a Markov chain framework to model correlated client participation in federated learning under a minimum separation constraint (each client must wait R rounds between participations). It characterizes the asymptotic bias of vanilla FedAvg under correlated non-uniform participation, proves that increasing R reduces this bias under certain conditions, and proposes a lightweight debiasing algorithm that provably removes the bias. The Markov chain modeling is the paper's strongest contribution, providing a principled language for a practical FL scenario that prior theory largely assumed away.

## Strengths
1. **Novel Markov chain modeling of minimum-separation client participation** (Definition 1, Proposition 1, Lemma 1): The R-order Markov chain formally captures correlated participation induced by the minimum separation constraint — a standard FL practice for DP amplification. The framework encompasses independent non-uniform (R=0) and cyclic participation (R=M-1) as special cases, and the irreducibility/aperiodicity results provide a rigorous foundation for convergence analysis.

2. **Clean characterization of FedAvg's asymptotic bias** (Theorem 1): The convergence bound decomposes error into an optimization term Õ(τ_mix/√T) and an unavoidable bias term O(‖π_R − (1/N)1_N‖₁²) that depends solely on how far the stationary sampling distribution deviates from uniform — a formal result that distinguishes this from prior FedAvg analyses assuming unbiased sampling.

3. **Empirical evidence that increasing minimum separation reduces bias** (Figure 1): A clear monotonic decrease in the l1-distance between π_R and the uniform distribution as R grows (N=500, B=1, random p_i's), supporting the practical claim that the DP-motivated minimum separation has a beneficial side effect on convergence.

4. **Lightweight, provably convergent debiasing algorithm** (Algorithm 1, Theorem 3): Each client maintains just two scalars tracking empirical sampling frequency, scaling the local learning rate by 1/(π_Rⁱ N). Theorem 3 proves convergence to an unbiased solution at rate Õ(τ_mix/√T) without the bias term, without requiring the bounded-gradient assumption needed in Theorem 1. The bound does not grow with N, unlike prior cyclic-participation bounds.

5. **Generality to heterogeneous R_i and higher-order chains**: Section 5 notes extension to clients with individual R_i values. The convergence results generalize beyond first-order Markov chain SGD to higher-order chains with local updates (K > 1) and debiasing — a genuine extension of the Markov-sampling SGD literature (Beznosikov et al. 2024, Even et al. 2023).

## Weaknesses

### Fatal
None.

### Major
1. **Theorem 2's conditions are restrictive and the paper's framing overstates the theoretical contribution.** The theorem assumes that all size-B subsets drawn from the N−B non-minimal-p clients have nearly equal total probability (δ_j ≤ δ̄). For B=1, this requires p₂ ≈ p₃ ≈ … ≈ p_N — essentially assuming away most non-uniformity it claims to analyze. The paper acknowledges this only in passing (line 192: "when the availability probabilities p_i's of clients are not too far away from each other"), while the abstract states the claim as a general theoretical proof ("We theoretically prove … that increasing minimum separation reduces the bias"). The actual theorem covers a special case; the general claim rests on the single empirical plot in Figure 1. This mismatch between framing and technical content is a significant concern.

2. **Experimental evaluation is far too thin for a top venue.**
   - Only two settings: one synthetic dataset and MNIST with a small 3-layer fully-connected network. No CIFAR-10/100, no language or recommendation task.
   - No error bars, no multiple seeds, no variance reporting — single trajectories are presented for inherently stochastic convergence. This is not acceptable for empirical claims about convergence behavior.
   - The experimental protocol uses a group-based simplification (partitioning N clients into M fixed groups, selecting one group per round) that is a special case of the general per-client sampling model described in Sections 2–3. The experiments do not exercise the full generality of the claimed setting.
   - The "oracle uniform" baseline shown as a red horizontal line is not explained (how it is generated, under what protocol).

### Minor
1. **Convergence rates depend on an uncharacterized mixing time of an astronomically large state space.** The bounds in Theorems 1 and 3 and Lemma 1 all depend on τ_mix — the mixing time of a Markov chain whose state space d(M,R) = ∏_{k=0}^{R-1} σ(B(M−k), B) grows super-exponentially. No bounds on τ_mix in terms of N, B, R, or the p_i's are provided, nor any empirical estimates. This is a common limitation in Markov-chain SGD analyses (Beznosikov et al. 2024, Even et al. 2023 also leave τ_mix uncharacterized), but it means the rates are formal rather than practically grounded.

2. **Estimator convergence rate to π_R requires more careful justification.** Lemma 1 claims 𝔼[‖ν̃_t‖_∞²] = O(τ_mix/t), but λ_tⁱ = t_i/((t+1)B) is only updated when client i is sampled. For clients with small π_Rⁱ (inevitable in large-N systems), the effective number of informative updates is far smaller than t, making the stated worst-case O(τ_mix/t) rate suspect without a per-client argument that accounts for sampling sparsity.

3. **No discussion of estimator burn-in instability.** λ_tⁱ starts at 0, so ν_tⁱ = 1/(λ_tⁱ N) can be enormous early on (division by near-zero), potentially causing instability. The algorithm description does not address this practical concern or any safeguards.

### Trivial
- The FedVARP baseline comparison (Figure 3c) is not particularly informative: FedVARP is a variance-reduction method for uniform sampling, so showing it does not handle non-uniform bias is an expected negative result that does not sharpen the contribution.

## Nice-to-Haves
- Provide bounds or empirical estimates of τ_mix to ground the convergence rates in a tractable quantity.
- Expand experiments: add a vision benchmark beyond MNIST (e.g., CIFAR-10), report error bars over multiple seeds, and include a comparison against at least one debiasing method for non-uniform independent sampling (Wang et al. 2022 ArbiCLi) to contextualize the benefit of handling correlation.
- Discuss the burn-in phase of the estimator and practical mitigations (e.g., clipping ν_tⁱ, using a warm-up period, or a burn-in threshold before applying debiasing weights).

## Removed Points
The following points from the input reviews were removed with justification:

1. *"Incomplete baselines — the paper dodges comparison with methods designed for precisely the setting studied here"* — Removed because Wang et al. 2022 (ArbiCLi), Cho et al. 2022, Wang et al. 2023 (lightweight), and Ribero et al. 2022 address non-uniform but *independent* client participation, not the correlated setting studied here. They are cited as related work addressing a different problem variant, not as missing baselines for the same setting.

2. *"Lemma 1's proof is deferred to the appendix, which was not made available in the parsed text, so I cannot verify it"* — Removed per policy: the parser strips appendices from all papers; the proof exists in the original submission. The substantive concern about per-client sampling sparsity is retained as a Minor weakness.

3. *"The convergence rate matches Markov-sampling SGD and generalizes..."* (Strength Finder item 7, listed as a major strength) — Retained but listed among strengths, not as a separate category. No removal needed.

4. *"Generality to heterogeneous minimum separation values"* (Strength Finder supporting strength 1) — Retained but noted as briefly mentioned without formal analysis, thus not a core strength.

5. Pure formatting nitpicks and speculation about what might be in a missing appendix were removed throughout.

## Novel Insights
Beyond the paper's own contributions, the reviews highlight a productive tension: the Markov chain framework is the paper's most novel contribution, providing rigorous language for analyzing correlated participation. Yet this same rigor exposes a gap — the state-space explosion that makes the model precise also makes its mixing time intractable, and the main structural theorem (Theorem 2) requires conditions that largely assume away the non-uniformity it claims to explain. The debiasing algorithm is elegant precisely because it sidesteps this complexity (empirical estimation of π_R rather than analytical computation), but its convergence guarantees inherit the same mixing-time dependence, creating a net where the simplest solution depends on the least tractable parameter. This suggests a direction for future work: can the mixing time be bounded or estimated efficiently for this specific Markov chain structure, or can debiasing be achieved without τ_mix-dependent rates?

## Suggestions
1. Revise the abstract and introduction to accurately reflect Theorem 2's restrictiveness — explicitly state that the theoretical result requires near-uniformity of p_i among most clients, and that the general claim (R monotonically reducing bias for arbitrary p_i) is empirically supported but not yet theoretically proven.
2. Add error bars over multiple random seeds to all experiments; include at least one non-trivial benchmark (CIFAR-10) to demonstrate scalability beyond MNIST.
3. Run the evaluation under the general per-client sampling model (not the group simplification) to match the paper's own problem formulation.
4. Provide some characterization of τ_mix — either theoretical bounds for special cases, or empirical estimates from simulating the Markov chain — to contextualize the convergence rates.
5. Discuss the burn-in phase for the estimator and any practical safeguards against early-round instability from near-zero denominators in ν_tⁱ.

## Score and Decision
MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>