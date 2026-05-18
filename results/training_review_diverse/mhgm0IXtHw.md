Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes Noise Map Guidance (NMG), an inversion method for real-image editing with text-guided diffusion models. Instead of using a one-dimensional null-text embedding (as in NTI and NPI), NMG directly conditions the reverse process on *noise maps* — the spatially-indexed latent variables from DDIM inversion — to preserve spatial context. The method reformulates the reverse process with dual conditioning (noise maps + text) through energy guidance, requiring no iterative optimization per timestep. Experiments across Prompt-to-Prompt, MasaCtrl, and pix2pix-zero show NMG preserves spatial structure better than NTI, NPI, and ProxNPI while achieving a ~20× speedup over NTI in reconstruction.

## Strengths

1. **Spatial-context preservation through noise-map conditioning is well motivated and effective.** Unlike NTI and NPI (which rely on a 1D null-text embedding that inherently lacks spatial information), NMG uses noise maps that share spatial dimensions with the input image. Qualitative results (Figs. 3–4) consistently show NMG retaining spatial layout, object positions, and scene structure that competing methods lose. This is the paper's core contribution and is convincingly demonstrated.

2. **Dual conditioning via energy guidance is principled and gives independent control.** The formulation (Eqs. 8–13) incorporating both noise maps and text through an energy function derived from L1 distance to the inversion trajectory is technically sound. The ablation (Fig. 5a) validates that \(s_N\) and \(s_T\) provide separable control over spatial preservation vs. text-driven editing — a capability absent in prior inversion methods.

3. **Broad compatibility with multiple editing frameworks.** NMG integrates successfully with Prompt-to-Prompt, MasaCtrl, and pix2pix-zero (Figs. 3–4), demonstrating that its spatial-context benefits apply across local edits, global style transfer, non-rigid manipulation (pose, viewpoint), and zero-shot image-to-image translation.

4. **Robustness to DDIM inversion variants.** When paired with pix2pix-zero's modified DDIM inversion (which adds a regularization term to the inversion process), NMG still produces spatially coherent results, whereas NTI and NPI degrade (Fig. 4b, Sec. 4.2).

5. **Quantitative and human evaluation superiority.** NMG consistently outperforms NTI, NPI, and ProxNPI on CLIPScore and TIFA across 4 local + 4 global + 2 non-rigid tasks (Table 1), and was the most preferred method in a 40-participant user study.

## Weaknesses

### Fatal
None.

### Major

1. **The \(z^{NM}_t \approx z^{NM}_{t-1}\) approximation is undefined and unvalidated.** The variable \(z^{NM}_t\) is never introduced before it appears in the approximation (line 113: "Empirically, we find that we can approximate \(\vz^{NM}_t \approx \vz^{NM}_{t-1}\)"). The only previously defined variable is \(z^{NM}_{t-1}\) (Eq. 7). The paper then uses \(z^{NM}_t\) in Eqs. 8–9 as input to the text-conditioning step. The intended meaning appears to be that after computing the noise-map-conditioned result \(z^{NM}_{t-1}\), it is treated *as if* it were at timestep \(t\) so that the text-conditioned step can operate with the correct timestep index. But this re-indexing is never explained, the approximation is offered without any empirical evidence, and the resulting notation is confusing enough to undermine reproducibility. The authors should replace this with a clear two-step sequential description (e.g., "compute \(\vz^{\text{nm}}_{t-1}\) with noise-map guidance, then compute \(\vz_{t-1}\) from \(\vz^{\text{nm}}_{t-1}\) with text guidance") and remove the unjustified approximation.

2. **Numerical values of the three guidance hyperparameters (\(s_g\), \(s_N\), \(s_T\)) are never reported.** The paper mentions these three scales in the method (Eqs. 5, 6, 8) and runs an ablation study showing they affect output quality (Fig. 5). The text states "we maintain a consistent guidance scale across all experiments" (Sec. 4.4) — but never says what those values are. Without the chosen numerical values, the experiments cannot be reproduced or fairly compared against. The authors should report the specific values used, describe how they were selected (e.g., grid search on a validation set), and ideally provide a sensitivity analysis.

### Minor

1. **"Optimization-free" terminology needs qualification.** The paper repeatedly calls NMG "optimization-free" (abstract, contributions, conclusion, related work). However, NMG computes \(\nabla_{\vz_t} \|z'_{t-1} - z^*_{t-1}\|_1\) at each timestep (Eq. 5), which involves backpropagation through the denoising network — a gradient computation. The paper correctly contrasts NMG's single backward pass with NTI's *iterative* per-timestep optimization, but the unqualified phrase "optimization-free" could mislead readers into thinking no gradient computation is involved. Clarifying this distinction (e.g., "no iterative parameter optimization" vs. "gradient-free") would improve precision without diminishing the contribution.

2. **No automatic metric for content preservation in unedited regions during editing.** The editing evaluation uses CLIPScore and TIFA (both measure alignment with the target prompt) and a user study asking for "highest fidelity." However, there is no automatic metric (e.g., LPIPS or PSNR on masked unchanged regions, when masks are available) that directly quantifies how well the original image's content is preserved in areas not targeted by the edit. LPIPS is used only for reconstruction (Table 2). Adding such a metric would strengthen the claim that NMG preserves spatial context during editing specifically.

3. **Total editing time (not just reconstruction) is not reported.** The ~20× speedup factor is for the reconstruction path only. Since the full editing pipeline includes attention-based editing (which is common across methods once inversion is done), the total wall-clock time for editing may tell a different story. Reporting end-to-end editing time would give a complete picture of the computational advantage.

4. **Computational overhead of the extra unconditional forward pass is not acknowledged.** The energy gradient in Eq. 5 uses \(z'_{t-1}\) computed with the unconditional \(\epsilon_\theta(z_t, \emptyset)\). This requires an additional unconditional forward pass through the network at each timestep before computing the gradient. This overhead should be explicitly stated and quantified.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing NMG against a variant that applies noise-map guidance to *both* reconstruction and editing paths (analogous to ProxNPI's behavior) would directly test the paper's central argument that constraining the editing path is harmful.
- Pseudocode or an algorithmic listing of the forward pass would resolve the notation confusion and improve reproducibility.
- Broader experimental comparison with EDICT, ReNoise, or other recent inversion-free methods would further contextualize the contribution (EDICT is already cited in related work, so this is about experimental breadth, not missing citations).

## Removed Points

- **Criticism that user study percentages are "not visible in the extracted text":** This is a parser/extraction artifact; the numbers exist in the original submission's table. Removed per parser-artifact rule.
- **Criticism that the paper does not compare with EDICT/ReNoise as missing methods:** EDICT (wallace2023edict) is cited in the related work (line 40). The comparison set (DDIM, NTI, NPI, ProxNPI) covers the most directly relevant baselines for an optimization-free inversion method. Broader comparison is moved to Nice-to-Haves.
- **Generic/overlapping strength from Strength Finder:** The strength "Optimization-free inversion that preserves spatial context" uses the same "optimization-free" language flagged as imprecise in Weakness Minor #1. The strength is retained because the *spatial context* claim is well-supported; only the label needs fixing.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same assessment: the core idea is solid and well-demonstrated, but the paper needs to fix its confusing notation for the dual-conditioning pipeline and report missing hyperparameter values before it can be reliably reproduced.

## Suggestions

1. Rewrite the dual-conditioning derivation (Sec. 3.2) to eliminate the \(z^{NM}_t \approx z^{NM}_{t-1}\) approximation. Present the two conditioning steps as a clear, sequential process with properly indexed intermediate variables.
2. Report the numerical values of \(s_g\), \(s_N\), and \(s_T\) used in all experiments, along with how they were selected (e.g., validation set, grid range).
3. Qualify the "optimization-free" claim to make clear that it refers to the absence of *iterative* parameter optimization, not the absence of any gradient computation.
4. Add a content-preservation metric (e.g., LPIPS on background/unchanged regions) to the editing evaluation.

## Score and Decision

The paper introduces a practically useful inversion method with a clear and well-motivated idea. The experimental evidence (qualitative, quantitative, user study) supports the core claims. The two major weaknesses — the confusing notation for the dual-conditioning pipeline and the missing hyperparameter values — are fixable in revision and do not invalidate the contribution. However, they must be resolved before the paper is publication-ready.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>