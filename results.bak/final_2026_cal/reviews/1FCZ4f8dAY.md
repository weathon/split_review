Now I have sufficient calibration. Let me compile the final review.

**Round 1 bracket**: Based on the anchor papers, this paper sits between the 5.5 paper (binary forms / tensor functions, Reject) and the 6.67-6.5 papers (accepted posters on equivariance topics). It is clearly stronger than the 5.5 anchor (more groups, more experiments, cleaner presentation). It is comparable or slightly stronger empirically than the 6.67 anchor but with a less "novel" theoretical problem framing (systematization vs. new phenomenon). **Initial bracket: 6.0 – 7.5**.

**Round 2 narrowing**: Reading the 6.67 anchor (symmetry increase, Accept Poster), this paper has more diverse experiments and clearer practical impact, but the theory is more of a systematization/extension rather than unveiling a new phenomenon. The paper is most comparable to ~7.0 papers. **Final score: 7.0**.

Now let me write the review.

Key decisions on weaknesses from the harsh critic:

**Overclaimed novelty**: The paper says "To the best of our knowledge this is the first work that provides a recipe for equivariant machine learning models for tensors at this level of generality." In context, the paper cites prior work on O(d) (Villar et al., Kunisky et al.) and the Related Work discusses them. The claim is about the *level of generality* — covering O(d), Lorentz, and Sp(d) — which is indeed new. I'll keep this as a minor weakness because the O(d)-specific part is a systematization, but the reviewer overstates this.

**Sparse vector narrative**: The reviewer's criticisms about SoS outperforming Ours in several settings need careful handling. The paper acknowledges that SoS does well when its assumptions are met (Identity covariance). The reviewer points out cases where SoS wins on Random covariance (Bernoulli-Gaussian) and the paper acknowledges this exception. The Corrected BG and Accept/Reject on Identity — these are cases where SoS assumptions ARE met. So the reviewer's criticism #2 and #3 are less valid. However, the point about the Diag variant outperforming the full model in some settings is valid and worth noting. Also the "Corrected Bernoulli-Gaussian" isn't explained in the main text. I'll keep this as a minor weakness.

**Complexity/scalability**: The paper gives the complexity formula and notes it's practical for small k'. The experiments use k'=2 (stress-strain, path signature) which is tractable. The reviewer's concern about n=100 for sparse vectors (k'=2) would give O(2! * 100^2 * ...) which is tractable. I think the paper adequately addresses this. I'll demote to minor.

**Table 2 metric**: The "d_F / d_F" is clearly a parser artifact. Per instructions, remove this.

**No e3nn comparison**: The paper discusses e3nn in Related Work. A comparison would strengthen but is not required. Move to nice-to-have.

**Parity/pseudovector discussion**: Trivial.

Let me now write the full review.## Summary

This paper provides a characterization of equivariant polynomial (and analytic) functions mapping tensors to tensors under the orthogonal group O(d), the indefinite orthogonal group O(s,d−s) (including the Lorentz group), and the symplectic group Sp(d). Using classical invariant theory, the authors show that all such functions can be expressed as linear combinations of tensor products of the inputs with group-specific isotropic tensors (Kronecker deltas, Levi-Civita symbols, and their analogs), whose scalar coefficients depend only on invariant inner products. This characterization is translated into practical, learnable architectures (Corollaries 1–3). The method is evaluated on three diverse problems: stress-strain tensor learning (materials science), path signature approximation (time series), and sparse vector estimation (theoretical computer science), where it consistently outperforms non-equivariant baselines and, in several settings, specialized prior methods.

## Strengths

- **Full characterization for three classical groups under a unified framework.** The paper provides explicit parameterizations for equivariant tensor-to-tensor functions under O(d), O(s,d−s), and Sp(d) (Theorems 1–2, Corollaries 1–3). This extends prior work that was largely restricted to O(3)/SO(3) or symmetric tensors, and the Lorentz/symplectic extensions are genuinely new architectural recipes. The unified treatment via invariant theory (Kronecker deltas → bilinear forms of each group) is clean and elegant.

- **Consistent and substantial empirical improvements across diverse applications.** On the stress-strain problem (Table 1), the equivariant model achieves test errors an order of magnitude lower than the best non-equivariant baseline (4.057e-6 vs. 2.020e-5 at n=5,000). On path signature estimation (Table 2), the method achieves error 0.002 vs. the next-best 0.007 under O(d) and 0.005 vs. 0.186 under Lorentz. The improvements are dramatic and hold across dataset sizes.

- **Practical parameterization that reduces to a concrete, implementable architecture.** Corollary 1 reduces the abstract equivariant characterization to a form that can be implemented with MLPs operating on pairwise inner products, with clear complexity bounds. The same recipe is extended to Lorentz and symplectic groups via Corollary 3. This makes the theory directly usable.

- **Learned models succeed where theoretical methods struggle.** In the sparse vector problem, the equivariant model substantially outperforms sum-of-squares methods in settings where the SoS assumptions (e.g., identity covariance) are violated — e.g., Accept/Reject with Random covariance (Ours 0.938 vs. SoS 0.610) and Corrected BG with Random covariance (Ours 0.935 vs. SoS 0.412), demonstrating the value of learned equivariant models beyond regimes with theoretical guarantees.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The sparse vector experiments have a mixed narrative that requires more nuance in the main text.** The paper states that SoS performs best when its assumptions are met but is outperformed by the learned model otherwise. This is broadly accurate, but several data points complicate the picture: (i) the Bernoulli-Gaussian case is correctly acknowledged as an exception, but (ii) the Diagonal-covariance results are mixed — the full model underperforms both SoS and the "Ours (Diag)" variant on several rows (e.g., Accept/Reject Diagonal: Diag 0.589, Ours 0.465, SoS 0.448; Corrected BG Diagonal: Diag 0.550, Ours 0.460, SoS 0.288). This suggests the full model may overfit due to the large number of pairwise inner-product terms (n=100 gives O(n²) inputs to the MLP). The main text does not discuss why the Diag variant sometimes outperforms the full model, nor does it clearly define the "Corrected Bernoulli-Gaussian" variant. These issues do not invalidate the overall contribution (the method still wins in several key settings), but a more careful discussion would strengthen the paper.

- **The novelty claim for the O(d) case is slightly overstated in the Discussion.** The paper states: "To the best of our knowledge this is the first work that provides a recipe for equivariant machine learning models for tensors at this level of generality." The Lorentz and symplectic extensions are genuinely new, but the O(d) vector-to-tensor characterization follows from known invariant theory (Weyl, Jeffreys, Roe Goodman) and is closely related to existing ML work (Villar et al. 2021 for vectors; Kunisky et al. 2024 for symmetric tensors). The paper cites these works and does not claim the O(d) result is entirely new in isolation, but the phrasing "at this level of generality" conflates the O(d) systematization with the genuinely novel Lorentz/Sp(d) extensions. The claim would be more accurate if it emphasized the Lorentz and symplectic extensions as the primary novelty while characterizing the O(d) case as a systematization of known results into ML-friendly form.

- **The complexity analysis in the main text uses the worst-case formula without the reductions noted in the appendix.** The stated complexity O(k′! n^{k′} (Q d n² + d^{k′})) uses the full k′! permutation count, but the text immediately notes that the permutation sum is smaller than S_{k′} when t>0 due to symmetries of δ^{⊗t} (discussed in Appendix D). A reader trying to assess scalability in the main text cannot determine how much smaller. The actual model sizes used in each experiment (number of terms after reductions) would help readers judge practical feasibility.

- **No discussion of output parity (p′) in the experiments.** The theory handles parity (pseudovectors) via the parity parameter, but all experiments use p=+1 for both input and output. A brief comment on when pseudovector outputs arise in practice (e.g., angular velocities, magnetic fields) and whether the method has been validated in such settings would strengthen the paper.

### Trivial

None.

## Nice-to-Haves

- A direct empirical comparison with e3nn on the O(d) experiments (stress-strain or path signature) would substantiate the claim in Related Work that the methods have comparable approximation power.
- A figure or table aggregating sparse-vector results across "SoS assumptions met" vs. "SoS assumptions violated" conditions would help readers see the trend at a glance.
- Reporting training errors alongside test errors for the sparse-vector experiment (Table 7 is in the appendix) would clarify whether the full model's weaker performance on some settings is due to overfitting.

## Removed Points

These points were flagged by the reviewers but are removed or demoted for the following reasons:

- **Table 2 metric "d_F / d_F" formatting error**: This is a PDF parsing artifact, not a paper error. Removed per hard rules.
- **Claim that SoS outperforms Ours on Accept/Reject Identity and Corrected BG Identity shows narrative is unsupported**: These are cases where the SoS assumptions are met (Identity covariance), so SoS winning is expected and consistent with the paper's narrative. The paper already acknowledges the Bernoulli-Gaussian exception. Removed.
- **Scalability concerns about n=100 in sparse vectors**: The output is k′=2 (d×d symmetric matrix), giving O(2!·100²·(...)) ≈ O(20,000·(...)) operations, which is tractable and the paper states k′∈{1,2,3,4} captures practical cases. The paper mentions appendix details. Demoted from major concern to minor.
- **Missing comparison to e3nn**: The Related Work discusses e3nn, and the paper's contribution is about extending beyond O(d) to Lorentz and Sp(d). A comparison would strengthen but is not a missing requirement. Moved to nice-to-have.
- **Complexity formula uses full k′! without reduction**: The paper explicitly mentions the permutation sum is "smaller than S_{k′} when t>0 as discussed in Appendix D." The formula is stated as worst-case, which is standard. Demoted to minor weakness about lack of concrete per-experiment model sizes.

## Novel Insights

The harsh critic's observation that the Diag variant (using only vector norms, ignoring cross terms) sometimes outperforms the full model on Diagonal-covariance settings is a genuinely useful insight. It suggests an interesting phenomenon: when the covariance structure is diagonal, the pairwise inner products are less informative and the additional parameters of the full model may lead to overfitting. This creates a potentially productive tension — the invariant-theoretic parameterization is complete (captures all polynomial equivariant functions) but may be *too expressive* for small-sample settings, and a simpler restriction to norm-only features regularizes more aggressively. The paper does not explore this, and it is worth investigating.

The paper's own most striking result — that on the stress-strain task the equivariant model achieves 4×10⁻⁶ error vs. 5×10⁻⁵ for a prior equivariant method (TFENN) — is noteworthy because both methods incorporate the same symmetry. This shows that the *form* of the equivariant parameterization matters beyond just enforcing equivariance, which is a contribution the paper understates.

## Suggestions

1. **Tighten the sparse-vector narrative**: Add a 2–3 sentence paragraph defining the SoS assumptions and which experimental settings satisfy them. Explain the "Corrected Bernoulli-Gaussian" variant briefly. Discuss why the Diag variant outperforms the full model in some settings (overfitting? uninformative cross terms?).
2. **Provide per-experiment model sizes**: For each experiment, state the actual number of terms and parameters used after the permutation reductions from Appendix D, so readers can assess practical scalability.
3. **Reframe the novelty claim**: Distinguish between the O(d) case (a systematization/transfer of known invariant theory into ML-friendly form) and the Lorentz/Sp(d) extensions (genuinely new architectures).
4. **Add a brief discussion of output parity** (p') and when pseudovector outputs would arise, even if not tested.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched three bands on topics related to equivariant tensor learning.
- Low band (avg < 3.5): anchors at 2.0–3.33 (e.g., "Invariant and equivariant architectures via learned polarization" avg 2.0, "An algebraic approach to approximately equivariant networks" avg 2.0). Clearly weaker than this paper.
- Middle band (avg 3.5–7.5): anchors at 5.0–6.67. Key comparables: "Learning equivariant tensor function representations via covariant algebra of binary forms" avg 5.50 (Reject); "Permutation Equivariant Neural Networks for Antisymmetric Tensors" avg 5.00 (Reject); "Reducing Symmetry Increase in Equivariant Neural Networks" avg 6.67 (Accept Poster); "Approximate Equivariance via Projection-Based Regularisation" avg 6.50 (Reject).
- High band (avg > 7.5): anchors at 8.0–8.5 but for less topically related papers (rotation estimation, permutation-equivariant geometry, quantum reservoir computing).

**Initial bracket: 6.0–7.5.** The paper is clearly stronger than the 5.0–5.5 anchors (more groups, more experiments, better presentation). It is comparable to the 6.5–6.67 anchors in theoretical rigor but has stronger/diverse empirical validation.

**Round 2 (Narrowing):** Read "Reducing Symmetry Increase in Equivariant Neural Networks" (avg 6.67, Accept Poster) in full. This paper has similar theoretical depth but only one real-world experiment (QM9) and more niche scope. The paper under review has three diverse applications with stronger results. However, the symmetry-increase paper identifies a fundamentally new phenomenon, whereas the O(d) part of this paper systematizes known theory. These offset. The most topically similar paper — "Learning equivariant tensor function representations via covariant algebra of binary forms" (avg 5.50, Reject) — is clearly weaker: it only covers SO(3), has only one experimental domain (turbulence), and has presentation issues.

**Final score: 7.0**. This paper makes a solid, well-supported contribution. The issues identified (nuanced sparse-vector narrative, slightly overstated O(d) novelty framing, incomplete complexity reporting) are minor and do not diminish the core contribution of clean theoretical characterizations for Lorentz/Sp(d) and strong empirical results across diverse domains.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>