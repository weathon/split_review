Now I have a good calibration picture. Let me synthesize the final review.

**Round 1 bracket analysis:**
- Weak band (avg 1.5-3.0): Papers like "Pixel-Aware Accelerated Reverse Diffusion" (3.0), "TCIG" (1.5), "Self-distillation for diffusion models" (3.0). IterRef is clearly much stronger than these.
- Middle band (avg 3.5-7.5): DPMC (4.75), Momentum-driven Noise-free Guidance (5.33), DDPP (6.25), Unlocking Guidance (6.50), DAS (7.25). IterRef is comparable to these.
- Strong band (avg 7.5+): Interpolating AR and Discrete (8.0), Learning to Discretize (8.0), Learning to Permute (8.0). IterRef is weaker than these.

**Round 2 narrowing:**
Comparing with the most relevant anchors in the 5-7 range:
- **DDPP (6.25)**: Steering masked discrete diffusion via posterior prediction. Requires training a secondary model. IterRef is training-free (inference-time only), which is an advantage. DDPP has more extensive experiments (wet-lab validation). IterRef's experiments are clean and systematic but narrower.
- **Unlocking Guidance (6.50)**: General guidance framework for discrete diffusion/flow. Similar to IterRef in addressing discrete-specific challenges. Has theoretical derivation of guided rate matrices. IterRef's MTM-based approach is more novel mechanism-wise.
- **DAS / Alignment without Over-optimization (7.25)**: Training-free SMC-based alignment for continuous diffusion. Very clean and comprehensive. IterRef is specific to discrete diffusion, which is a harder problem setting, but the DAS paper is cleaner overall with more thorough experiments.
- **Simple Controllable UDLM (5.25)**: Classical guidance for discrete diffusion. Good contributions but limited scope (small vocab). IterRef is stronger.

The IterRef paper has:
- A clear, novel contribution (MTM-based iterative refinement for discrete diffusion)
- Theoretical grounding (Proposition 1)
- Multiple model backbones and tasks
- Informative ablations (timing, k vs N)
- Some documentation gaps (𝒰 not specified for main results, s-t not specified, no error bars)

The main weaknesses are real but not fatal — they are documentation/analysis gaps rather than fundamental flaws in the method.

Comparing against the anchors: IterRef is better than DPMC (4.75) and similar to DDPP (6.25) in contribution quality. It's slightly weaker than Unlocking Guidance (6.50) and DAS (7.25) in comprehensiveness. I'd place it around 6.0-6.5. Let me settle on 6.0.

Actually, let me think more carefully. The harsh critic raised a legitimate concern about the comparison fairness. Let me re-examine this.

Looking at the paper: The paper compares IterRef with baselines under the same NFE budget. This is the standard protocol. However, the harsh critic's point is that baselines apply guidance at every denoising step while IterRef applies it selectively (at 𝒰). The critic says this conflates the benefit of the MTM kernel with the benefit of spending compute selectively.

But this is actually a feature of IterRef, not a bug. The method is *designed* to be selective about where it applies compute. The comparison at equal NFE is standard. Moreover, Table 2 (the "Evenly" row) shows the results when IterRef is applied at every step at the same total cost. On 3 out of 4 tasks, Evenly actually outperforms the best single-step application, suggesting that the method works even without selective application.

So this criticism is partially valid but not fatal. It would still be good practice to include a controlled comparison where baselines are also restricted to 𝒰, but the current protocol is standard and the results are credible.

Let me finalize my assessment. The paper is a solid contribution to a timely problem. It has systematic experiments, a principled method, and informative ablations. The main weaknesses are documentation gaps and lack of error bars. I'd score this at 6.0.

Now let me write the final review.Now I have a clear calibration picture. Let me synthesize the final review.

---

## Summary

This paper introduces IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with noising-denoising transition kernels to iteratively refine intermediate diffusion states toward reward-aligned distributions. The method is evaluated across text (MDLM, LLaDA-8B) and image (MaskGIT) domains with multiple reward functions, showing consistent improvements over baselines under equal NFE budgets. Informative ablations isolate when refinement matters (later stages) and whether iteration or particle count drives gains (iteration wins).

## Strengths

- **Principled theoretical grounding via MTM**: Proposition 1 establishes that the refinement chain at a single fixed timestep satisfies detailed balance and converges to the optimal intermediate distribution p^*(x_t) as k → ∞. This goes beyond purely heuristic iterative refinement methods common in related work, providing an explicit convergence guarantee for the per-step kernel.

- **Consistent empirical advantage across models, modalities, and reward functions**: Figure 2 shows IterRef outperforming FK, SVDD, SoP, and BoN across 4 language tasks with 2 discrete diffusion backbones (MDLM, LLaDA-8B). Table 1 extends this to image generation with MaskGIT, showing improvements at every compute budget. The breadth of settings provides credible evidence that the method is not tailored to a single favorable configuration.

- **Informative ablation isolating iteration count vs. particle count**: Table 3 holds the product k×N constant and shows that increasing iterations (k) consistently outperforms increasing particles (N). This provides direct evidence that the iterative refinement mechanism itself drives gains, not merely the increased sample count.

- **Empirical finding about refinement timing**: Table 2 tests refinement at specific diffusion steps (0.9T through 0.1T) and finds that later-stage refinement is substantially more effective. This contrasts with continuous diffusion where early steps dominate, and provides a principled basis for where to allocate compute.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Gap between theoretical guarantee and full-algorithm claim**: Proposition 1 guarantees convergence of the MTM chain at a *single fixed timestep* to p^*(x_t). The abstract and introduction, however, claim "convergence to the reward-aligned distribution" for the overall sampling procedure. The full algorithm (Algorithm 2) iterates over denoising steps, composing MTM refinement (at some steps) with the base denoising kernel p_θ(x_{t-1}|x_t). Even if each MTM block converges to p^*(x_t) individually, the paper offers no analysis of whether the composition converges to p^*(x_0). The contribution statement (bullet 3) appropriately qualifies this ("provides an explanation of its effectiveness under certain assumptions"), but the abstract oversells it. This is a scope-of-guarantee mismatch, not an error in the proof itself.

- **Unspecified noising horizon s−t**: The transition kernel K depends on a noising step x_s with s > t (Equation 2, line 109). Section 3.3 mentions that each proposal requires N(s−t) diffusion-model calls, but the paper never states what value of s−t is used in practice. This affects both proposal quality (how far the state is noised) and computational cost. Without this detail the method is not fully reproducible from the main text. (The appendix is stripped, so the information may exist there but is inaccessible.)

- **Effective timestep set 𝒰 not stated for main results**: Table 2 shows that choosing different timesteps for refinement yields dramatically different results (e.g., CoLA: 23.3 at 0.9T vs. 87.0 at 0.1T). The paper does not state which 𝒰 was used for the main experiments in Figures 2, Table 1, or Figure 5. Without this, the reader cannot assess whether the reported results use a per-task optimized set, a fixed global configuration, or the "Evenly" setting. Since the method's flexibility to choose 𝒰 is presented as an advantage (Section 3.2), the actual choice must be disclosed for fair evaluation.

- **Intermediate reward approximation not analyzed theoretically**: The paper states (line 117) that intermediate rewards r(x_t) can be approximated by evaluating the reward on the model's predicted x_0, which is the standard approach. However, the theoretical convergence proof (Proposition 1) assumes access to the true r(x_t). The paper does not discuss whether or how this approximation affects detailed balance or whether the chain still targets the correct distribution under the approximation.

- **No error bars or variance estimates**: All figures and tables report point estimates without standard deviations, confidence intervals, or error bars. Given the stochasticity of MCMC sampling and the modest evaluation size (15 prompts, 20 samples each for language tasks), variance estimates would meaningfully strengthen the main claims. This is a presentation gap, not a fatal one — single-run evaluations are common in large-scale benchmarks, but the experiments here are not at prohibitive scale.

### Trivial

- The qualitative image samples (Figure 3) appear selected; including random samples would strengthen the visual evidence.
- The detoxification examples (Figure 5) show a tendency to frame outputs as quotations, which is interesting but the paper does not discuss potential reward over-optimization or gaming behaviors.

## Nice-to-Haves

- State the specific 𝒖 used for all main experiments in the main text (not just in an ablation table).
- State the noising horizon s−t used in practice and include an ablation showing its effect on performance and cost.
- Add a controlled experiment where each baseline is restricted to the same timestep set 𝒰 as IterRef, to isolate the benefit of the MTM kernel from the benefit of selective compute allocation.
- Discuss the impact of the r(x_t) ≈ r(ˆx_0) approximation on the theoretical guarantees.
- Report error bars or confidence intervals for the main quantitative results (at least the core Figure 2 experiments).

## Removed Points

These points were raised by reviewers but are removed from the main weaknesses:

- **"Unfair comparison invalidates 8× faster narrative"** (harsh critic): The NFE-based comparison is standard and fair. The method's ability to apply compute only where it helps is a *feature* of IterRef, not a confounding variable. Table 2 shows "Evenly" (apply at all steps) actually outperforms selective application on most tasks, suggesting the method works even without the selective-application advantage. The concern is moved to a nice-to-have controlled experiment suggestion.

- **"SoP adaptation to discrete domain is ambiguous / weak baseline"**: Speculative. The paper states baselines are configured following their original papers.

- **"Overstated novelty / underexplored claim"**: Subjective framing criticism. The paper cites relevant concurrent work (Wang et al. 2025, Dang et al. 2025, Jain et al. 2025) in Related Work.

- **"Missing related work comparison"**: The paper discusses relevant work explicitly. Per policy, missing related-work criticisms are removed.

- **"CLIPScore improvements are modest / not perceptually meaningful"**: Improvements are consistent across all budgets (e.g., +1.6 at 2×, +1.0 at 16×). Given the figure caption notes the MaskGIT resolution, these are within expected ranges for discrete image diffusion.

- **"Derivations deferred to appendix"**: The appendix is stripped from the review copy; this is not a valid criticism.

- **Strength Finder generic strengths** (e.g., "important problem"): Removed as generic/non-specific.

## Novel Insights

None beyond the paper's own contributions. The key empirical insight — that later-stage refinement is more effective than early-stage for discrete diffusion, opposite to continuous diffusion — is already well documented by the authors in Table 2.

## Suggestions

- Clarify in the abstract and introduction that the convergence guarantee applies per refinement stage at individual timesteps, not automatically for the full multi-step trajectory.
- Specify the noising horizon s−t used in all experiments in the main text.
- Disclose the effective timestep set 𝒰 used for each main result.
- Include error bars or confidence intervals for the primary quantitative results.
- Add a brief discussion of how the r(x_t) ≈ r(ˆx_0) approximation interacts with the theoretical guarantees.
- Consider including a controlled experiment where baselines are applied at the same selective timesteps as IterRef, to further strengthen attribution.

---

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:**

| Band | Anchor Paper | Avg Score | How It Compares |
|------|-------------|-----------|-----------------|
| Weak (≤3.5) | Pixel-Aware Accelerated Reverse Diffusion | 3.00 | Much weaker contribution; unclear methodology |
| Weak (≤3.5) | TCIG | 1.50 | Much weaker; limited scope |
| Weak (≤3.5) | Self-distillation for diffusion models | 3.00 | Weaker; less principled |
| Middle (3.5–7.5) | DPMC (MCMC for inverse problems) | 4.75 | Comparable novelty, weaker experiments |
| Middle (3.5–7.5) | Momentum-driven Noise-free Guidance | 5.33 | Similar scope, less principled theory |
| Strong (≥7.5) | Interpolating AR and Discrete Diffusion LM | 8.00 | Stronger; broader architectural contribution |
| Strong (≥7.5) | Learning to Permute with Discrete Diffusion | 8.00 | Stronger; novel formalism |

**Round 2 — Narrowing (5.0–7.0):**

| Anchor Paper | Avg Score | How It Compares |
|-------------|-----------|-----------------|
| DDPP: Steering Masked Discrete Diffusion | 6.25 | Similar quality. DDPP requires training secondary model, IterRef is inference-time. DDPP has wet-lab validation, IterRef has broader text+image evaluation. Comparable overall. |
| Unlocking Guidance for Discrete Diffusion | 6.50 | Similar quality. This paper derives guidance for CTMCs; IterRef uses MTM with noising-denoising kernels. IterRef provides stronger ablation analysis. |
| DRAKES: Fine-tuning Discrete Diffusion | 6.00 | IterRef is stronger — training-free, more comprehensive experiments, cleaner theoretical link. |
| DAS: Alignment without Over-optimization | 7.25 | Stronger overall — more polished, cleaner evaluation pipeline, but focuses on *continuous* diffusion. IterRef tackles the harder discrete setting. |
| Simple Controllable UDLM | 5.25 | Weaker; limited to small-vocabulary settings. IterRef is more generally applicable. |

**Round 1 bracket:** 3.5 – 7.5 (clearly in the middle band).

**Final score determination:** IterRef is most comparable to DDPP (6.25) and Unlocking Guidance (6.50). It is slightly stronger than DRAKES (6.00) due to broader experimentation and training-free operation. It is weaker than DAS (7.25) in polish and comprehensiveness but addresses the harder discrete-diffusion setting. The method is novel, the theory is principled, and the experiments (6 model×task combinations, 2 modalities, 4 ablations) are solid. The main weaknesses are documentation gaps (𝒰 not specified, s−t not specified) and lack of error bars — these are real but not fundamental. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>