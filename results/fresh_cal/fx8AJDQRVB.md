Now I have a complete picture of the paper. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me draft this carefully.

---

For the **Space MoE "capacity increase"** criticism: Let me re-read the paper carefully. Line 92-93 says for Sampling MoE: "Since only a single expert network is activated at each step, the scale and capacity of our model can expand with computational overhead remaining the same during inference." This is about Sampling MoE (not Space MoE), and it's correct — different experts at different timesteps genuinely increases capacity.

For Space MoE (line 96): "Similarly, we create MoE layers with N spatial experts... to scale the denoising UNet in diffusion-based SR." The averaging at inference means it's a form of structural reparameterization. The critic says "the framing as 'increasing capacity' is misleading" — but the paper also says "we propose to use Sample-Space Mixture of Experts (SS-MoE) to achieve more powerful latent-based SR, which steadily improves the capacity of the model without a significant increase in inference costs" (abstract). The SS-MoE includes both Sampling MoE (which genuinely increases capacity at inference) and Space MoE (which uses averaging). So the overall SS-MoE design does increase capacity — through Sampling MoE having different expert weights active at different timesteps. The Space MoE contributes through better training dynamics.

The critic's specific point is about Space MoE being described as "increasing capacity" — but this is somewhat addressed because the paper frames SS-MoE as a whole system, and the Sampling MoE part does genuinely increase capacity. The Space MoE averaging is a separate component. I'll keep a softened version of this criticism.

Actually, I need to be more careful. The abstract says "Sample-Space Mixture of Experts" — it's "Sampling-Space" not "Samples-in-Space." The paper's contribution is the combined SS-MoE. The Space MoE part (multi-FFN averaged at inference) is more like structural reparameterization. But the Sampling MoE part genuinely increases inference capacity. So the overall claim is valid. Let me remove this criticism entirely or keep a very softened version.

Actually, I'll keep a minor point about the Space MoE framing being slightly imprecise — it's worth noting that the Space MoE's benefit likely comes from training regularization rather than increased inference capacity, but this doesn't undermine the overall contribution. Let me include it as a minor point.Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper presents a latent diffusion model for image super-resolution with two main contributions: (1) a Sampling-Space Mixture of Experts (SS-MoE) that scales the denoising UNet without proportionally increasing inference FLOPs, and (2) a frequency-compensated decoder (FCD) that recovers high-frequency information lost during latent-space compression. The method is evaluated on 4× blind SR and 8× non-blind SR benchmarks, achieving state-of-the-art perceptual quality on 8× SR and competitive results on 4× SR.

## Strengths

- **SS-MoE scales model parameters with minimal FLOPs overhead, and this is directly measured.** Table 5 (computation cost) shows the method increases total parameters from 168.95M (LDM) to 605.30M while per-step FLOPs rise only 3.1% (0.1608T → 0.1658T). The Sampling MoE component genuinely increases inference-time capacity by using different expert weights at different timestep stages, while the Space MoE component adds training-time capacity through structural reparameterization.

- **Ablation studies confirm both sub-components contribute.** Table 2 (ablation on SS-MoE) shows that removing either Sampling MoE or Space MoE produces a measurable drop: LPIPS rises from 0.3031 to 0.3201 or 0.3134 on 4× SR. Table 4 (ablation on sampling steps) further shows SS-MoE at 50 steps achieves better perceptual quality than Space-MoE at 200 steps, demonstrating real efficiency gains from the staged-expert design.

- **State-of-the-art 8× SR perceptual results.** Table 3 (8× SR) reports the best LPIPS (0.2321), FID (44.49), and MUSIQ (64.17) on DIV2K Valid 8× SR among compared methods including RRDB, ESRGAN, SRFlow, FxSR-PD, and LDM, with clear margins (e.g., FID 44.49 vs. next-best 55.0 from FxSR-PD).

- **Frequency-compensated decoder produces measurable perceptual improvements.** Ablation Table 6 shows AFF+FFL improves LPIPS by 7.3% (0.3038 → 0.2815) and NIQE by 22.1% (5.6093 → 4.3675) over the baseline VQ decoder with all variants compared at the same checkpoint, providing clean causal evidence.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **FCD ablation performed at 25k steps instead of the final 50k checkpoint.** The paper states ablation experiments in Table 6 "have the same 25k training steps" (line 321), while the FCD training stage runs for 50k steps (line 144). Although all variants are compared at the same intermediate checkpoint — making the relative improvements internally valid — the absolute gains (e.g., 7.3% LPIPS reduction) may shift with longer training. Some benefits could amplify, others might diminish. Running the ablation at the final 50k checkpoint would strengthen the evidence.

2. **Table 1 (4× SR) presents two StableSR columns without a clean separation.** The table includes both an "StableSR" column (numbers from the original paper, using a different test set) and a "StableSR†" column (reproduced with the official model on the paper's test set). The text does acknowledge the difference ("Note that due to differences in making test sets…," line 196), but showing both side-by-side with no visual demarcation beyond the † symbol invites confusion: a reader may compare the proposed method against whichever column is more favorable, rather than only against the apples-to-apples reproduction. The table should either report only the reproduced numbers or separate the two columns more clearly.

3. **The Space MoE benefit is framed as "capacity increase" when its mechanism is closer to training regularization.** At inference, Space MoE averages all expert weights into a single FFN (Eq. 7), so the number of active parameters matches a standard single-FFN model. The improvement from Space MoE therefore stems from training dynamics (random token splitting incentivizes diverse feature representations, and weight averaging regularizes the final weights) rather than from increased inference-time capacity. This does not undermine the contribution — the technique works — but the framing would be more precise if it acknowledged the structural-reparameterization nature of this component and discussed how it differs from increasing inference capacity (which is what Sampling MoE legitimately provides).

4. **Uniform timestep division for Sampling MoE is stated without justification.** The paper divides timesteps uniformly into N stages (line 92) and uses N=4, but does not discuss whether adaptive allocation (e.g., more stages in the high-noise regime where denoising difficulty varies) could improve the design or whether N=4 was chosen empirically. A brief motivation or sensitivity study on N would strengthen the exposition.

### Trivial

- The frequency loss weight λ=10 is reported without sensitivity analysis.
- The paper notes missing FID/NIQE for StableSR on some real-world benchmarks without explanation.

## Nice-to-Haves

- **FCD ablation at the final 50k checkpoint** would turn the minor concern above into a settled point.
- **A head-to-head comparison against a baseline with matched inference FLOPs but without the MoE structure** would further isolate the SS-MoE training benefit (as the harsh critic suggested).
- **Frequency-domain visualizations** (FFT magnitude plots) of the decoder output would directly illustrate whether the AFF blocks restore the high-frequency content the baseline decoder loses.
- **Error bars or variance estimates** over multiple evaluation runs, though not standard for large-scale SR benchmarks, would strengthen confidence in small-margin improvements.

## Removed Points

These points were flagged by one or both reviewers but are removed after cross-checking against the paper:

- *Missing comparison to DiffBIR/ResShift* — Removed per instruction: the rule forbids mentioning missing related works (lack of external sources to verify existence or release status of every cited method).
- *"No analysis of convergence behavior for Space MoE random token splitting"* — Removed. The paper provides a convergence-motivated design (momentum update Eq. 4, momentum coefficient analysis for γ=0.999 vs. γ=0.9) and requiring formal convergence analysis is disproportionate for a design component whose effectiveness is validated empirically.
- *"GAN-based methods outperform on real-world benchmarks" critique* — Removed as partially inaccurate. The paper clearly qualifies: "our method achieves the lowest LPIPS score among diffusion-based methods on the two real-world benchmarks" (line 196). The critic's reading conflates the paper's claim of superiority "among diffusion methods" with an unqualified overall claim.
- *OpenImage dataset advantage concern* — Removed. The paper is transparent about the training data composition (line 141) and the ablation studies control for model architecture changes, not dataset composition. This is a scope-creep concern.
- *Computational overhead of AFF Fourier transforms not discussed* — Demoted to removed. The paper already reports total FLOPs and parameters for the full model including FCD (Table 5), and the overall method is substantially more efficient than StableSR (605.30M params, 0.1658T FLOPs vs. 1409.11M, 0.4162T). Requesting a breakdown of the AFF-specific overhead is reasonable as a nice-to-have but not a weakness.
- *"On RealSR/DRealSR, FID reported as missing for StableSR"* — Removed as trivial. The original StableSR paper likely did not report these numbers.
- *"No error bars or variance estimates"* — Removed as a field-standards issue. Single-run evaluation on large-scale benchmarks is standard practice in SR research. Moving to Removed Points for transparency.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting nuance: the SS-MoE design bundles two distinct mechanisms under one name — Sampling MoE (genuine inference-time capacity increase via staged expert routing) and Space MoE (training-time regularization via multi-expert structural reparameterization with weight averaging). Disentangling these mechanisms could be valuable for future work: the Sampling MoE insight (different noise levels benefit from different expert parameters) is more architecturally novel, while the Space MoE insight (multi-FFN training with momentum averaging regularizes diffusion UNets) is a practical engineering contribution that borrows from the discriminative-model literature. A paper that evaluated each mechanism's benefit independently against simpler baselines (e.g., dropout for Space MoE, or curriculum-based sampling for Sampling MoE) would further clarify the source of gains.

## Suggestions

1. In Table 1 (4× SR), either remove the original StableSR column and report only the reproduced numbers, or visually separate the two columns with a clear heading label (e.g., "StableSR (orig.)" and "StableSR (our repro.)") and add a footnote explaining why they differ.
2. Run the FCD ablation experiments (Table 6) at the final 50k-step checkpoint and report whether the relative ordering of ablations persists.
3. Add a sentence explaining the choice of N=4 for Sampling MoE stages and uniform vs. adaptive division. Even a brief note that "uniform division was chosen for simplicity and N=4 was validated by GPU memory constraints" would address the concern.
4. Clarify the Space MoE framing: explicitly state that it functions as a structural reparameterization technique that regularizes training rather than increasing inference-time parameter count.
5. Add a brief sensitivity study on the frequency loss weight λ to show that the chosen value (λ=10) is reasonable.

## Score and Decision

This paper makes two genuine contributions — SS-MoE and the frequency-augmented decoder — both supported by ablation evidence and competitive benchmark results. The 8× SR results are particularly strong. The main weaknesses are the FCD ablation at an intermediate training step (still internally valid but could be stronger) and the slightly confusing presentation of the StableSR comparison in Table 1. Neither issue threatens the core claims. The paper is well-motivated, the methodology is clearly described, and the experimental evaluation is thorough overall.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>