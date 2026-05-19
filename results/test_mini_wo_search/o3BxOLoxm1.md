Here is my consolidated review.

---

## Summary

This paper proposes Manifold Preserving Guided Diffusion (MPGD), a training-free framework for conditional generation using pretrained diffusion models. The core idea is to constrain guidance updates to the tangent space of the data manifold, preventing the off-manifold drift that degrades sample quality in prior methods (DPS, FreeDoM, LGD-MC). The paper derives a "shortcut" update rule that avoids backpropagation through the diffusion model, and proposes two autoencoder-based projection methods (MPGD-AE, MPGD-Z) to enforce manifold constraints. Evaluated on linear inverse problems, FaceID-guided face generation, and style-guided text-to-image generation, the method shows competitive quality with reduced inference time and memory usage.

## Strengths

- **Training-free conditional generation with meaningful speed-ups and lower memory**: MPGD requires no extra training and uses off-the-shelf loss functions. Table 1 shows MPGD achieves 5.82s inference on FaceID guidance vs. 10.65s (FreeDoM) and 14.64s (LGD-MC) — a 1.8–2.5× speed-up. Table 2 further shows MPGD-LDM uses 15.53 GB VRAM vs. 31.65 GB (LGD-MC) and 17.30 GB (FreeDoM), making it the only method that fits in a 16 GB GPU at 100 DDIM steps.

- **Generalization across multiple tasks and both pixel/latent domains**: The framework is evaluated on three distinct conditional generation tasks (noisy linear inverse problems, FaceID-guided face gen, style-guided text-to-image with Stable Diffusion) and demonstrates applicability in both pixel-space and latent-space diffusion models without task-specific tuning.

- **Theoretical diagnosis of the manifold divergence problem in prior methods**: Section 3 explicitly identifies that existing training-free guidance methods (DPS, FreeDoM) optimize in ambient-space neighborhoods that can push samples off the data manifold. This diagnosis motivates the MPGD framework and is a useful conceptual contribution regardless of the method's limitations.

- **Derivation of a shortcut that avoids backpropagation through the denoiser**: Theorem 1 provides a simplified update rule (Eq. 8–9) that updates the clean estimate \(x_{0|t}\) directly, bypassing gradient computation through \(\epsilon_\theta\). This is the algorithmic basis for the observed speed and memory improvements, and the reasoning from tangent-space optimization to the shortcut is a clean conceptual link.

- **Memory efficiency enabling deployment on consumer hardware**: Table 2 reports MPGD-LDM at 15.53 GB VRAM vs. 31.65 GB for LGD-MC, which is a practically meaningful difference — it fits in a 16 GB consumer GPU while the strongest baseline does not.

## Weaknesses

### Fatal
None.

### Major

- **The "up to 3.8× speed-up" claim in the abstract/intro is not explicitly grounded to a specific experimental setting in the paper text.** The reported tables show speed-ups of 1.8–2.5× (FaceID: 5.82s vs 14.64s → 2.5×; Style: 19.83s vs 37.43s → 1.9×; vs FreeDoM 26.50s → 1.3×). The paper states "up to 3.8×" in both the abstract and introduction (lines 9, 52) and Figure 4 (ffhq_sr) may show this value at very low step counts, but there is no explicit sentence linking the 3.8× figure to a concrete experimental condition. An empirical claim of this magnitude should be traceable to a specific setting (task, step count, baseline). This is a framing/verifiability issue: the claim may be true but cannot be verified from the text as written.

- **No statistical uncertainty is reported for any metric.** All tables show single point estimates for KID, FaceID loss, style loss, and timing. With 1000 samples per evaluation, bootstrapped confidence intervals or standard errors would be straightforward to compute and would substantially strengthen the credibility of comparative claims, especially where differences are small (e.g., KID 0.0445 vs 0.0452 between MPGD-Z and FreeDoM in Table 1 — these may or may not be significant).

### Minor

- **No ablation study isolating the shortcut from the manifold projection.** The paper presents MPGD w/o Proj. (shortcut only), MPGD-AE (shortcut + AE projection), and MPGD-Z (latent manipulation). But there is no "projection-only" variant where an ambient-space gradient update is followed by a VQGAN encode-decode step. Such an ablation would clarify whether the projection or the shortcut drives the improvements, and whether the shortcut alone (without projection) actively harms fidelity (as suggested by MPGD w/o Proj. KID of 0.0473 vs DDIM's 0.0442 in Table 1).

- **Hyperparameter schedules (\(\rho_t\), \(c_t\)) are not specified.** The step-size parameters are described only as "time-dependent" (lines 87, 174) and no schedules are given. As the paper itself notes that prior methods require "detailed fine-tuning of step size scheduling" (line 135), providing the schedules used for MPGD is essential for reproducibility and for fair comparison.

- **The FaceID experiment uses only 50 DDIM steps.** This is a low-step regime that particularly favors methods avoiding per-step gradient computation through the diffusion model. Testing at higher step counts (100+) would clarify whether the speed and quality advantages persist, or whether baselines close the gap with more steps.

- **The claim that the shortcut is "naturally manifold preserving" for latent diffusion models** (line 49, line 279: "the decoded latent guidance \(D(\nabla_{z_{0|t}} L(D(z_{0|t});y))\) is on the tangent spaces of the data manifold") is stated without proof or rigorous argument. The general condition (gradient must lie in the tangent space) is non-trivial and is not established for arbitrary style/ID losses applied through the decoder. While the claim may hold in practice, the paper does not provide evidence for it beyond the LDM architecture's properties.

### Trivial

- Algorithm 2 (line 237) has a typo: `L((D(z_{0|t});y)` has an unmatched parenthesis.

## Nice-to-Haves

- Adding DPS with repainting as a baseline would address a natural competitor, though the paper does acknowledge repainting as an existing technique (lines 135, 284).
- Providing total FLOPs or GPU-hours in addition to wall-clock time would help disentangle hardware effects from algorithmic efficiency.
- A limitations section discussing when MPGD might fail (e.g., when VQGAN reconstruction error is large, or when the manifold hypothesis is strongly violated) would improve the paper's completeness.

## Removed Points

These points from the inputs are removed (with justification):

1. **"Disconnect between theoretical assumptions and practical implementation"** — The paper explicitly acknowledges that the linear subspace manifold hypothesis and perfect autoencoder are idealizations (Assumptions 3.2, 4.1) and states that "in practice, we find that well-trained imperfect autoencoders such as VQGAN also have similar effects" (line 269), pointing to Figure 2 as empirical support. The figure exists in the original submission. The paper is transparent about the gap; this criticism overstates the problem.

2. **"The shortcut MPGD w/o Proj. is not convincingly manifold-preserving"** — The paper explicitly states the condition required (∇L must lie in the tangent space, line 179) and names the method "MPGD w/o Proj." to acknowledge it lacks explicit projection. It also honestly reports its worse KID (0.0473 vs 0.0442) in Table 1. This is not a flaw; it is transparent reporting.

3. **"Proposition 1 is only given informally"** — The paper labels it "Informal" (line 127), which is by design. The formal statement was in the appendix (which is stripped during parsing).

4. **"The derivation from tangent-space objective to shortcut is opaque"** — The formal Theorem 1 and its proof are in the appendix (stripped during parsing). The main text provides the intuition and resulting update equations.

5. **"Missing baseline: DPS with repainting"** — Repainting is discussed in the paper (lines 135, 284) as a related technique. The paper's baseline set (DPS, LGD-MC, MCG, FreeDoM) is standard for this line of work. Demanding every possible variant is scope creep.

6. **"Figure 6 not visible"** — The figure (referenced as Figure 2 in the paper, `fig:inner_product`) exists in the original submission. Parsing artifacts do not make it absent.

7. **Strength Finder strengths that are generic/delusional** — Dropped generic strengths such as "addressed an important problem" which lack paper-specific evidence. Only concrete, evidence-grounded strengths are retained above.

## Novel Insights

The most interesting observation from this review process is the tension between the paper's strong conceptual framing (manifold-preserving guidance via tangent-space projection) and the evidence actually provided. The "shortcut" that avoids backpropagation through the denoiser appears to be the primary practical contributor to speed-ups, while the "manifold preservation" — the paper's chief theoretical selling point — rests on autoencoder-based projections whose manifold-preserving properties are claimed but not rigorously validated beyond a single reference figure. The practical value of the method (speed, memory) may be independent of whether the theory perfectly holds, suggesting the paper's framing as a manifold-preserving theory is stronger than the evidence supports, but the algorithmic heuristic itself is useful and competitive.

## Suggestions

1. Ground the "up to 3.8×" speed-up claim explicitly: "At 20 DDIM steps for FFHQ 4× super-resolution, MPGD achieves a 3.8× wall-clock speed-up over LGD-MC."
2. Add bootstrapped confidence intervals or standard errors to all metric tables.
3. Include an ablation: "projection-only" variant (ambient gradient + VQGAN encode-decode) vs. "shortcut-only" vs. "shortcut + projection" to disentangle the contributions.
4. Provide the \(\rho_t\) and \(c_t\) schedules used in all experiments (e.g., as a table or formula).
5. Add at least one experiment at higher step counts (e.g., 100-200 steps) for FaceID guidance to test whether the speed/quality advantages persist.
6. Fix the typo in Algorithm 2 (line 237).

## Score and Decision

The paper presents a well-motivated, training-free framework with practical speed and memory benefits validated across multiple tasks. The major weaknesses are that (a) the headline speed-up claim is not explicitly grounded to an experiment in the text, and (b) no statistical uncertainty is reported, which weakens comparative claims. These are addressable in a revision. The core contributions — the shortcut update rule and empirical demonstration of competitive quality with lower cost — are sound and valuable. The paper does not have fatal flaws, but the evidence is somewhat uneven: strong on practical utility, weaker on validating the manifold-preservation theory that motivates the method.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>