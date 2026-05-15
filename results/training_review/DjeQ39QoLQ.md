Now I have a thorough understanding of the paper and all reviewer claims. Let me compose the final consolidated review.

## Summary
This paper proposes a "perturb-then-diagonalize" (PTD) methodology for initializing diagonal state-space models (SSMs) as an alternative to the S4D/S5 initialization that discards the low-rank part of HiPPO. The paper provides: (1) a theoretical analysis proving that while S4D's outputs converge to S4's pointwise on smooth inputs, they fail to converge uniformly — exhibiting constant-magnitude spikes in the transfer function at certain Fourier modes; (2) the PTD framework that approximately diagonalizes the HiPPO matrix via a small perturbation, with a transfer-function error bound linear in the perturbation size and only logarithmic in state dimension; (3) S4-PTD and S5-PTD models that demonstrate improved robustness to Fourier-mode noise and competitive LRA performance.

## Strengths
- **Fine-grained theoretical analysis of S4 vs. S4D convergence (Lemma 1, Theorems 1–2):** The paper derives an explicit formula for the transfer function difference G_DPLR - G_Diag and proves that convergence is only weak-* (pointwise for smooth inputs) but not uniform, with spikes of constant magnitude at frequencies Θ(n²). This goes well beyond prior empirical observations and provides a concrete mathematical explanation for why the diagonal initialization can be fragile, even when it works well on average.

- **PTD framework with rigorous error control (Theorem 4.1):** The paper bounds the transfer function error of the perturbed system as (2ln(n)+4)ε + O(√(log n) ε²) — linear in perturbation size and only logarithmic in state dimension. This gives a principled, theoretically grounded alternative to discarding the low-rank part. The connection to pseudospectral theory and backward-stable diagonalization is clean and generalizable beyond HiPPO.

- **Synthetic failure mode demonstration (Section 3.4, Figure 2):** The extrapolation experiment (training on frequencies [0,80], testing on [0,100]) cleanly reveals S4D's catastrophic failure (predicting *negative* amplitudes for signals with frequencies >80) while S4-PTD preserves correct behavior. This directly validates the theoretical prediction that S4D's transfer-function spikes cause measurable performance degradation.

- **Robustness to structured Fourier-mode noise (Section 5.2, Figures 3a–3b):** On sCIFAR, S4-PTD maintains ~75% accuracy on inputs contaminated with worst-case sinusoidal noise at S4D's spike frequencies, while S4D collapses to near chance. This provides concrete empirical validation that the PTD initialization avoids the specific fragility predicted by the theory.

- **Competitive LRA performance:** S4-PTD improves over S4D by +1.69% average accuracy (86.58 vs. 84.89), with particular gains on Path-X (+4.44%), Retrieval (+1.61%), and Text (+2.14%). S5-PTD matches or slightly exceeds S5 (87.61 vs. 87.46).

## Weaknesses

### Fatal
None.

### Major
- **LRA results reported without error bars or multiple seeds.** The accuracy improvements of S4-PTD over S4D (+1.69% avg) and especially S5-PTD over S5 (+0.15% avg) cannot be assessed for statistical significance. Given that the S4→S4D gap is larger than the S4-PTD improvement over S4D in several tasks, and that S5-PTD's gains are negligible, the claim that PTD "helps to improve the accuracy of deep learning models" is not convincingly supported by the LRA numbers alone. The paper needs either error bars over multiple seeds or a clear statement that the LRA results are single-run and should be interpreted indicatively. *(Verified: Table 1 reports single numbers per model/task with no variance or seed count.)*

### Minor
- **Robustness evaluation is limited to a single, worst-case noise scenario.** The paper is transparent that the CIFAR-10 experiment uses "worst-case noises intentionally made to fail the S4D model" (line 444), and the claims are specifically about "Fourier-mode noise-perturbed inputs" (line 14). Nevertheless, the practical significance of the robustness result is narrowed considerably by: (1) testing only one dataset (sCIFAR), (2) using only one type of noise (sinusoidal at S4D's spike frequencies), and (3) showing no results for more natural corruptions (e.g., Gaussian noise, missing pixels, sensor noise). A broader robustness evaluation — even adding one more noise type on sCIFAR — would substantially strengthen the practical relevance.

- **The PTD optimization (Eq. 13) is underspecified.** The paper proposes minimizing κ(Ṽ_H) + γ‖E‖ subject to A_H+E = Ṽ_H Λ̃ Ṽ_H⁻¹, states that gradient descent is used, and controls ‖E‖ through γ. However, it provides no details on algorithm initialization, convergence behavior, computational cost for different state sizes n, or sensitivity to the starting point. While the theoretical bounds (Theorems 4.2–4.3) guarantee existence of good perturbations, the practical recipe for finding them is left as a black box. *(Verified: Lines 378–383 state the objective and mention gradient descent but give no further algorithmic details.)*

- **S5-PTD gains over S5 are negligible on LRA.** The average improvement is only +0.15% (87.61 vs. 87.46), with S5-PTD actually scoring lower than S5 on Image (−0.08%) and Path-X (−0.06%). This undercuts the claim that PTD broadly improves accuracy; the benefit appears architecture-dependent, with clearer gains for S4D-style SISO models than for S5-style MIMO models. The paper's own language ("S5-PTD matches the performance of the S5 model") is appropriately cautious, but the abstract's broader claim ("helps to improve the accuracy") should be tempered.

### Trivial
- The paper's claim that PTD "strongly converges to the HiPPO framework" could benefit from a brief explicit reminder that this refers to the input-output map (transfer function), which is conjugation-invariant, rather than the internal state representation. The paper does establish this connection (lines 90–91, 123–124), so this is purely a clarity nitpick.

## Nice-to-Haves
- **Run LRA tasks with at least 3 random seeds and report mean ± std.** This would make the accuracy claims properly testable.
- **Add one additional noise type (e.g., Gaussian or random masking) on sCIFAR** to show that PTD does not actively harm robustness to non-Fourier noise, even if the primary claim is about Fourier-mode robustness.
- **Provide a brief empirical characterization of the PTD optimization** — e.g., how many gradient steps are needed, how the objective value varies with n, and whether the reported perturbation matrices (‖E‖/‖A_H‖ ≈ 10⁻² to 10⁻¹) are reliably obtained.
- **A visual comparison of the transfer function |G_Pert| overlaid on |G_DPLR| and |G_Diag|** for several ε values would help readers intuitively verify that PTD smooths out the spikes.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

1. **Harsh Critic Point 4: "Core theoretical framing conflates different reference systems."** The critic argues that Theorem 3 bounds G_Pert − G_DPLR rather than G_Pert − G_HiPPO. However, the paper explicitly states (lines 90–91, 123–124) that the transfer function is conjugation-invariant, so G_DPLR = G_HiPPO (same I-O behavior). Bounding G_Pert against G_DPLR is therefore equivalent to bounding it against the original HiPPO system in the transfer-function sense. The "converges to the HiPPO framework" claim is explicitly about transfer functions (line 13: "Through theoretical analysis of the transfer functions..."). This criticism is factually incorrect and reflects a misunderstanding of conjugation invariance. **REMOVED.**

2. **Harsh Critic's request for realistic robustness benchmarks** (Gaussian noise, adversarial perturbations): The paper's claims are specifically about "Fourier-mode noise-perturbed inputs." Requesting experiments on Gaussian noise, missing inputs, or adversarial attacks asks the paper to address problems outside its stated scope. The paper is transparent that the noise experiment uses worst-case noise (line 444). The narrow scope is acknowledged, and expanding beyond it is a nice-to-have, not a weakness. **MOVED to Nice-to-Haves.**

3. **Criticism that the synthetic extrapolation task is "far from realistic":** The paper presents this as a diagnostic that isolates the theoretical phenomenon, not as a realistic benchmark. Its purpose is to validate the theory, which it does convincingly. The critic acknowledges this ("convincingly illustrates the theoretical spikes") but then faults it for being unrealistic — which is not a genuine weakness of a diagnostic experiment. **REMOVED (contradicts the critic's own acknowledgment).**

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself fails to make. The key synthesis is that the theoretical analysis is the paper's strongest contribution, while the experimental validation is adequate but not definitive — a gap the authors should address in future work.

## Suggestions
1. **Add error bars to LRA results** by running each configuration with at least 3 random seeds. Without this, the paper's accuracy claims remain unvalidated.
2. **Provide implementation details for the PTD optimization** (Eq. 13): how E is initialized, how gradient descent is applied to the non-convex objective κ(Ṽ_H) + γ‖E‖, typical number of iterations, and computational cost for relevant state sizes. This would address the current black-box nature of the method.
3. **Qualify the accuracy claim** in the abstract and conclusion to reflect that PTD's accuracy benefit is architecture-dependent: clear for S4D-style SISO models, marginal for S5-style MIMO models.
4. **Add one transfer-function overlay plot** (|G_Pert| vs. |G_DPLR| vs. |G_Diag| for a few ε values) to visually confirm that PTD smooths the spikes predicted in Section 3 — this would be a compelling visual summary of the paper's main idea.

## Score and Decision

The paper makes a genuine theoretical contribution: it provides the first fine-grained analysis of S4 vs. S4D convergence behavior, revealing non-uniform convergence that prior work only observed empirically. The PTD framework is principled, and the transfer-function error bound (linear in ε, logarithmic in n) is clean and useful. The experimental validation, while limited in scope (no error bars on LRA, single noise type for robustness), does support the theory's predictions in the cases tested. The paper's claims are scoped appropriately for the most part, though the accuracy claims would benefit from statistical grounding.

The paper should not be rejected — its theoretical contribution is solid and the experimental results are consistent with the theory, even if the experiments themselves are not exhaustive. But the paper would be substantially stronger with error bars on LRA and a more detailed specification of the PTD optimization. The overall quality is decent for a venue that values theoretical insight alongside empirical demonstration.

Score: 6.0 (good, but with room for improvement on experimental rigor).

Actually, let me reconsider. The paper has:
- Strong theoretical contribution (Lemmas 1, Theorems 1-3) — genuinely novel analysis
- A novel methodology (PTD) with theoretical guarantees
- Limited but supportive experiments
- Transparency about limitations (worst-case noise, S5-PTD marginal)

For a conference paper, this is a solid contribution. The theory alone is valuable. The experiments confirm the theory without being exhaustive. Let me give 6.5.

Actually, let me think about the scale more carefully. In ML conferences:
- 8-10: Breakthrough / exceptional
- 6-7: Good, solid contribution
- 4-5: Borderline
- 1-3: Weak

This paper has a clear novel theoretical contribution, a new method, and supporting experiments. The main issues are (1) no error bars on LRA, (2) limited robustness evaluation, (3) underspecified optimization. These are significant but not fatal. I'll go with 6.0.

Wait, I said I should round to .0 or .5. Let me go with 6.0. The paper is solid but the experimental gaps are real.

Decision: Accept. The theoretical contribution is significant enough to warrant acceptance even with the experimental shortcomings.

MY FINAL SCORE: 6.0
MY FINAL DECISION: Accept## Summary

This paper proposes a "perturb-then-diagonalize" (PTD) methodology for initializing diagonal state-space models (SSMs) as an alternative to the S4D/S5 initialization that discards the low-rank part of HiPPO. The paper provides: (1) a theoretical analysis proving that while S4D's outputs converge to S4's pointwise on smooth inputs, they fail to converge uniformly — exhibiting constant-magnitude spikes in the transfer function at certain Fourier modes; (2) the PTD framework that approximately diagonalizes the HiPPO matrix via a small perturbation, with a transfer-function error bound linear in the perturbation size and only logarithmic in state dimension; (3) S4-PTD and S5-PTD models that demonstrate improved robustness to Fourier-mode noise and competitive LRA performance.

## Strengths

- **Fine-grained theoretical analysis of S4 vs. S4D convergence (Lemma 1, Theorems 1–2):** The paper derives an explicit formula for the transfer function difference G_DPLR − G_Diag and proves that convergence is only weak-* (pointwise for smooth inputs) but not uniform, with spikes of constant magnitude at frequencies Θ(n²). This goes well beyond prior empirical observations and provides a concrete mathematical explanation for why the diagonal initialization can be fragile, even when it works well on average.

- **PTD framework with rigorous error control (Theorem 4.1):** The paper bounds the transfer function error of the perturbed system as (2ln(n)+4)ε + O(√(log n) ε²) — linear in perturbation size and only logarithmic in state dimension. This gives a principled, theoretically grounded alternative to discarding the low-rank part. The connection to pseudospectral theory and backward-stable diagonalization is clean and generalizable beyond HiPPO.

- **Synthetic failure mode demonstration (Section 3.4, Figure 2):** The extrapolation experiment (training on frequencies [0,80], testing on [0,100]) cleanly reveals S4D's catastrophic failure (predicting *negative* amplitudes for signals with frequencies >80) while S4-PTD preserves correct behavior. This directly validates the theoretical prediction that S4D's transfer-function spikes cause measurable performance degradation.

- **Robustness to structured Fourier-mode noise (Section 5.2, Figures 3a–3b):** On sCIFAR, S4-PTD maintains ~75% accuracy on inputs contaminated with worst-case sinusoidal noise at S4D's spike frequencies, while S4D collapses to near chance. This provides concrete empirical validation that the PTD initialization avoids the specific fragility predicted by the theory.

- **Competitive LRA performance:** S4-PTD improves over S4D by +1.69% average accuracy (86.58 vs. 84.89), with particular gains on Path-X (+4.44%), Retrieval (+1.61%), and Text (+2.14%). S5-PTD matches or slightly exceeds S5 (87.61 vs. 87.46).

## Weaknesses

### Fatal

None.

### Major

- **LRA results reported without error bars or multiple seeds.** The accuracy improvements of S4-PTD over S4D (+1.69% avg) and especially S5-PTD over S5 (+0.15% avg) cannot be assessed for statistical significance. Given that the S4→S4D gap is larger than the S4-PTD improvement over S4D in several tasks, and that S5-PTD's gains are negligible, the claim that PTD "helps to improve the accuracy of deep learning models" is not convincingly supported by the LRA numbers alone. The paper needs either error bars over multiple seeds or a clear statement that the LRA results are single-run and should be interpreted indicatively. *(Verified: Table 1 reports single numbers per model/task with no variance or seed count.)*

### Minor

- **Robustness evaluation is limited to a single, worst-case noise scenario.** The paper is transparent that the CIFAR-10 experiment uses "worst-case noises intentionally made to fail the S4D model" (line 444), and the claims are specifically about "Fourier-mode noise-perturbed inputs" (line 14). The practical significance is narrowed by: (1) testing only one dataset (sCIFAR), (2) using only one noise type (sinusoidal at S4D's spike frequencies), and (3) showing no results for more natural corruptions. A broader robustness evaluation — even adding one more noise type on sCIFAR — would substantially strengthen the practical relevance.

- **The PTD optimization (Eq. 13) is underspecified.** The paper proposes minimizing κ(Ṽ_H) + γ‖E‖ subject to A_H+E = Ṽ_H Λ̃ Ṽ_H⁻¹, states that gradient descent is used, and controls ‖E‖ through γ. However, it provides no details on algorithm initialization, convergence behavior, computational cost for different state sizes n, or sensitivity to the starting point. While Theorems 4.2–4.3 guarantee existence of good perturbations, the practical recipe for finding them is left as a black box. *(Verified: Lines 378–383 state the objective and mention gradient descent but give no further algorithmic details.)*

- **S5-PTD gains over S5 are negligible on LRA.** The average improvement is only +0.15% (87.61 vs. 87.46), with S5-PTD scoring lower than S5 on Image (−0.08%) and Path-X (−0.06%). This undercuts the claim that PTD broadly improves accuracy; the benefit appears architecture-dependent, with clearer gains for S4D-style SISO models than for S5-style MIMO models. The paper's own language ("S5-PTD matches the performance of the S5 model") is appropriately cautious, but the abstract's broader claim ("helps to improve the accuracy") should be tempered.

### Trivial

- The claim that PTD "strongly converges to the HiPPO framework" could benefit from an explicit reminder that this refers to the input-output map (transfer function), which is conjugation-invariant, rather than the internal state representation. The paper does establish this connection (lines 90–91, 123–124), so this is purely a clarity nitpick.

## Nice-to-Haves

- **Run LRA tasks with at least 3 random seeds and report mean ± std.** This would make the accuracy claims properly testable.
- **Add one additional noise type (e.g., Gaussian or random masking) on sCIFAR** to show that PTD does not actively harm robustness to non-Fourier noise, even if the primary claim is about Fourier-mode robustness.
- **Provide a brief empirical characterization of the PTD optimization** — e.g., how many gradient steps are needed, how the objective value varies with n, and whether the reported perturbation matrices (‖E‖/‖A_H‖ ≈ 10⁻² to 10⁻¹) are reliably obtained.
- **A visual comparison of the transfer function |G_Pert| overlaid on |G_DPLR| and |G_Diag|** for several ε values would help readers intuitively verify that PTD smooths out the spikes.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Harsh Critic Point 4: "Core theoretical framing conflates different reference systems."** The critic argues that Theorem 3 bounds G_Pert − G_DPLR rather than G_Pert − G_HiPPO. However, the paper explicitly states (lines 90–91, 123–124) that the transfer function is conjugation-invariant, so G_DPLR = G_HiPPO (same I-O behavior). Bounding G_Pert against G_DPLR is therefore equivalent to bounding it against the original HiPPO system in the transfer-function sense. The "converges to the HiPPO framework" claim is explicitly about transfer functions (line 13). This criticism is factually incorrect. **REMOVED.**

2. **Harsh Critic's request for realistic robustness benchmarks** (Gaussian noise, adversarial perturbations, missing inputs): The paper's claims are specifically about "Fourier-mode noise-perturbed inputs." Requesting experiments beyond this scope asks the paper to address problems it never claimed to solve. The paper is transparent that the noise is worst-case (line 444). Expanding to additional noise types is a nice-to-have, not a weakness. **MOVED to Nice-to-Haves.**

3. **Criticism that the synthetic extrapolation task is "far from realistic":** The paper presents this as a diagnostic that isolates the theoretical phenomenon, not as a realistic benchmark. Its purpose is to validate the theory, which it does convincingly. Faulting it for being unrealistic is not a genuine weakness of a diagnostic experiment intended to illustrate a mathematical point. **REMOVED.**

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself fails to make. The main takeaway from the review process is that the theoretical analysis is the paper's strongest and most distinctive contribution, while the experimental validation is adequate but not exhaustive — a gap the authors could close with additional runs and noise types.

## Suggestions

1. **Add error bars to LRA results** by running each configuration with at least 3 random seeds. Without this, the paper's accuracy claims remain unvalidated.
2. **Provide implementation details for the PTD optimization** (Eq. 13): how E is initialized, how gradient descent is applied to the non-convex objective κ(Ṽ_H) + γ‖E‖, typical number of iterations, and computational cost for relevant state sizes.
3. **Qualify the accuracy claim** in the abstract and conclusion to reflect that PTD's accuracy benefit is architecture-dependent: clear for S4D-style SISO models, marginal for S5-style MIMO models.
4. **Add one transfer-function overlay plot** (|G_Pert| vs. |G_DPLR| vs. |G_Diag| for a few ε values) to visually confirm that PTD smooths the spikes predicted in Section 3 — this would be a compelling visual summary of the paper's main idea.

## Score and Decision

The paper's theoretical contribution — the fine-grained analysis of S4 vs. S4D convergence with the explicit transfer-function formula and the non-uniform convergence proof — is genuinely novel and addresses a gap in the SSM literature. The PTD framework with its O((2ln(n)+4)ε) error bound is principled and potentially useful beyond HiPPO. The experiments validate the theory qualitatively but lack the statistical rigor (no error bars) needed to fully support the accuracy claims. The overall contribution is solid but not exceptional; the paper would be strengthened by more rigorous experimental reporting. I recommend acceptance on the strength of the theoretical contribution, with the expectation that the experimental gaps can be addressed in a camera-ready version.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>