Now let me write the consolidated review.

## Summary

This paper studies differentially private PCA for vertically partitioned data, where columns of a dataset are distributed across multiple clients without a trusted third party. The authors propose SPCA, which combines independent Skellam noise contributions from each client (aggregated via the BGW secure multiparty computation protocol) to achieve two levels of differential privacy: server-observed DP (protecting records from the server) and client-observed DP (protecting other clients' data partitions). The paper claims through theoretical analysis that SPCA matches the privacy-utility trade-off of the optimal centralized DP-PCA baseline, and provides experiments on four datasets showing near-identical utility.

## Strengths

- **Novel algorithmic design for a hard threat model**: SPCA is the first DP PCA algorithm for vertical federated learning that simultaneously protects against both the server and adversarial clients without requiring any trusted third party. The combination of distributed Skellam noise injection with the BGW MPC protocol is a principled approach that addresses the non-linearity challenges unique to VFL (as opposed to HFL where linear aggregation suffices). The paper clearly motivates why existing solutions (trusting a client or third party for noise injection) are insufficient.

- **Rigorous dual-privacy problem formulation**: Section 3.2 carefully defines two distinct DP definitions (server-observed and client-observed) with formal justification of why they are both necessary. Propositions 1 and 2 construct explicit counterexamples showing that protecting one level does not imply the other, which clarifies a subtle but important point often overlooked in the VFL literature.

- **Empirical results show promise**: The experiments on four datasets (KDDCUP, ACSIncome, CiteSeer, Gene) with varying dimensions demonstrate that SPCA can achieve utility close to the centralized DP baseline, significantly outperforming the naive distributed baseline. This suggests the overall approach has practical potential.

## Weaknesses

### Major

- **Internal inconsistency between the claimed error rate and the stated sensitivity bounds**. Lemma 2 defines the sensitivity parameters as Δ₂ = γ² + n and Δ₁ = min((γ²+n)², √n(γ²+n)). Lemma 3 states γ = O(n) and claims an error bound of O(k√n √μ_{ε,δ}) with √μ_{ε,δ} = c√(log(1/δ))/ε — independent of γ and n, matching the centralized baseline. However, when γ = O(n), Δ₂ = O(n²), so the RDP bound's leading term gives τ ≈ αΔ₂²/(4μ) = αO(n⁴)/(4μ). To achieve a fixed (ε,δ)-DP target, μ must therefore be at least Ω(Δ₂²) = Ω(n⁴), yielding an error bound of O(k√n √μ) = O(k n^{2.5}) — far worse than the claimed O(k√n) rate. The paper does not resolve this tension or explain a regime where it is avoided. This undermines the paper's central theoretical claim that SPCA matches the optimal centralized baseline in privacy-utility trade-off. The experiments may suggest that the implemented method works well in practice, but the theoretical justification as written does not support the headline result.

- **Missing experimental detail: the mapping from (ε,δ) to the Skellam noise parameter μ is not specified**. The experiments report utility for various ε values (with δ = 10⁻⁵) but never state how the Skellam parameter μ was derived from the privacy budget. This mapping depends on Δ₂, Δ₁, γ, and the RDP-to-(ε,δ) conversion. Without knowing the actual μ values used, the privacy guarantees of the experimental outputs are unverifiable — the paper claims its method achieves a given ε but provides no evidence that the noise scale was correctly calibrated. This is a critical reproducibility gap, as the central comparison ("SPCA matches centralized") is meaningless if SPCA's noise was calibrated to a different effective privacy level than claimed.

### Minor

- **Client-observed DP is defined and analyzed theoretically but not evaluated experimentally**. The paper introduces client-observed DP as a key contribution and provides RDP bounds in Lemma 2, yet all experiments evaluate only server-observed DP. The client-observed bound scales with N²/(N-1)², and the practical utility degradation under this stricter form of privacy is never demonstrated. Since the paper claims to be "the first solution in the literature that simultaneously enforces two levels of DP," the lack of any experimental validation for the client-level guarantee weakens the significance of this claimed contribution.

- **The algorithm's handling of intra-client column pairs and the full covariance computation is underspecified**. Section 4 focuses the description on pairs (i,j) where the two columns belong to different clients, noting "for now" but never returning to explain how intra-client pairs (both columns on the same client) are handled. For such pairs, the computation is local to that client, yet DP noise must still be added. The paper does not discuss whether the same noise-accumulation process applies or whether client-observed DP guarantees degrade for intra-client pairs.

- **Practical communication and computation costs of the MPC protocol are not discussed**. Computing the full covariance matrix of size O(n²) using MPC (BGW with Shamir secret sharing) requires O(n²) secure multiplications, each involving communication among all N clients. For high-dimensional datasets such as Gene (n=20531), this overhead would be prohibitive in a real deployment. The experiments are almost certainly simulation-based (computing the perturbed covariance directly rather than through actual MPC), which should be stated explicitly. This limits the practical claims of the paper.

### Trivial

- Lemma 3 uses the notation "√μ_{ε,δ}" in a way that is initially confusing — it defines the square root of μ as a function of ε and δ, rather than defining μ itself. This makes the expression hard to parse on first reading.

## Nice-to-Haves

- **Resolve the γ-sensitivity-error tension**: Provide a complete derivation of Δ₂ and Δ₁ and identify regimes of γ (e.g., γ = O(1)) where the error rate matches the centralized baseline while discretization error remains controlled. Alternatively, if the bounds are loose in practice, state this explicitly and characterize the gap.
- **Provide the full (ε,δ)-to-μ mapping used in experiments**: Include a table or figure showing μ for each (ε,δ,γ) configuration.
- **Evaluate client-observed DP utility**: Even a small-scale simulation showing how utility degrades as N varies for fixed client-observed (ε,δ) would substantially strengthen the contribution.
- **Discuss the practical feasibility of MPC for the reported dimensions**: A complexity analysis (cost per covariance entry, total communication) and a statement about whether experiments used real MPC or a simulation would help readers assess the method's deployability.

## Removed Points

The following criticisms from the original reviews were removed for the reasons stated:

1. **"The comparison baseline is a strawman"** — The paper's distributed baseline (Sec. 3.3) is a natural first-principles approach to the setting. The paper never claims it is a strong baseline; it is presented to illustrate the gap that SPCA closes. Criticizing this as a strawman is unfair given the paper's honest presentation.

2. **"Centralized baseline sensitivity not specified; may be incorrectly calibrated"** — The centralized baseline follows Dwork et al. (2014), whose calibration is well-established. The critic's concern about per-entry composition is not clearly a mistake; the standard approach for the vectorized symmetric covariance matrix with ℓ₂ row-norm bound 1 uses O(1)-scale noise per entry, which is correct under the standard Gaussian mechanism analysis for functions with bounded ℓ₂ sensitivity. This criticism is speculative.

3. **"Standard deviation of 0.001 implausibly small"** — The magnitude of ‖DṼ_k‖²_F depends on the dataset and k; for large datasets this quantity can be very large, making an SD of 0.001 plausible. The critic provides no evidence that this is anomalous.

4. **"Missing discussion of server-client collusion"** — The paper explicitly assumes the semi-honest model (Section 3). Collusion is outside scope, and criticizing its absence is scope creep.

5. **"Related works not cited"** / **"Missing appendix content"** — The parser strips appendix content; these criticisms reflect extraction artifacts, not paper flaws.

6. **"Figure labels garbled"** — Parser artifact, not an author error.

7. **Strength "Error rate matches the optimal centralized baseline"** — This claimed strength conflicts with the verified major weakness (theoretical inconsistency). Per the filtering rules, when strength and weakness disagree, the weakness wins.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation about the paper that the authors themselves do not already state.

## Suggestions

1. **Fix the theoretical analysis**: Either (a) identify a regime of γ (e.g., γ = O(1)) where Δ₂ = O(1) and the error rate becomes O(k√n), while showing discretization error is controlled, or (b) provide a tighter sensitivity analysis that avoids the O(n⁴) scaling, or (c) be transparent about the fact that the theoretical bound is O(k n^{2.5}) rather than O(k√n), and justify why the method still works in practice.

2. **Provide full experimental transparency**: Add a table showing the exact μ values used for each (ε,δ,γ) configuration, along with the RDP conversion formula. This is essential for the privacy claims to be verifiable.

3. **Acknowledge the scope of experimental validation**: State clearly that the experiments only validate server-observed DP, and explicitly scope the client-observed DP claim to the theoretical analysis.

4. **Clarify the intra-client pair handling**: Either extend the algorithm description to cover all pairs uniformly, or explain any modifications needed for intra-client pairs.

5. **Add a complexity and feasibility discussion**: Include the communication/computation cost of MPC for the reported dataset dimensions and clarify whether experiments used real MPC or simulation.

## Score and Decision

The paper addresses a genuinely important problem (DP PCA in VFL without a trusted third party) and the core algorithmic design (distributed Skellam noise + MPC) is clever and well-motivated. The problem formulation with dual DP definitions is a careful contribution.

However, the paper has two major weaknesses that prevent acceptance in its current form. First, the central theoretical claim — that SPCA matches the optimal centralized privacy-utility trade-off — is internally inconsistent with the paper's own sensitivity analysis, which predicts a much worse error rate when γ = O(n). Second, the experimental evaluation lacks the key detail of how the privacy budget (ε,δ) maps to the noise parameter μ, making the privacy guarantees of the experiments unverifiable. Together, these issues mean that neither the theoretical nor the experimental case for the paper's main claim is convincing as written.

The algorithmic idea has merit and could potentially be substantiated with a corrected analysis and fuller experimental reporting. But in its present form, the contribution is not adequately supported.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>