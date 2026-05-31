Now let me run calibration searches across score bands to anchor the paper's quality.Now I have sufficient calibration data to write the final review.

**Round 1 bracket**: 4.5–6.5
**Round 2 anchors**: CtrLoRA (6.00, accepted), DyDiT (5.50, accepted), LinFusion (6.25, rejected)

PKA sits below CtrLoRA (clean ablations, no training-regime confound) and DyDiT (broader datasets, identical pre-training baseline) due to the quality comparison methodology problem and missing ablation quality metrics, but above the weak rejection papers (≤3.5) given its principled efficiency contributions.

---

## Summary

This paper proposes Patch-Wise and Keyword-Aware Attention (PKA), an efficient attention framework for multi-condition Diffusion Transformers. The core idea is to decompose full "concatenate-and-attend" attention into two specialized modules: Position-Aligned Attention (PAA) for spatial-aligned conditions (O(N) complexity via one-to-one patch correspondence) and Keyword-Scoped Attention (KSA) for subject-driven conditions (masking by keyword-activated image regions), complemented by a condition KV-cache and a novel early-timestep sampling strategy. Quantitative experiments on FLUX.1-based LoRA models report up to 10× latency and 5.12× VRAM reduction versus a full-attention baseline at 16 conditions, alongside competitive FID, SSIM, and consistency metrics on three multi-condition tasks.

---

## Strengths

- **PAA's O(N²)→O(N) complexity reduction is principled and verified.** The diagonal attention pattern of spatial conditions is empirically confirmed in Figure 2 (attention matrix nearly exactly diagonal for edge-map conditions), and the ablation in Figure 9 shows PAA operating at 13.63 s / 237 MB versus the full-attention baseline at 15.38 s / 308 MB, with visually indistinguishable output quality.

- **Early-timestep sampling insight is genuine and cleanly evidenced.** Figure 5 provides a quantitative perturbation experiment (SSIM of generated images vs. number of steps perturbed high-to-low vs. low-to-high), unambiguously showing that condition influence is concentrated in the early denoising stages (high t). Figure 11 demonstrates that biasing toward early timesteps (μ=0.5, δ=1.5) visibly accelerates convergence compared to standard or late-biased sampling.

- **Condition KV-caching eliminates redundant computation across denoising steps.** By restricting condition tokens to self-attention (Figure 4b), K and V projections are computed only once and reused, directly contributing to the efficiency gains in Figures 7–8.

- **Efficiency scalability is well-demonstrated.** Figures 7–8 show that PKA's latency and VRAM scale near-linearly while full-attention (UniCombine) scales quadratically, with verified speedup factors of 3.90×, 6.46×, and 10.0× at 4, 8, and 16 conditions, respectively.

---

## Weaknesses

### Fatal
None.

### Major

- **Quality comparison conflates the attention mechanism with training-regime differences.** The proposed model is fine-tuned with LoRA for 20K iterations on a curated subset of Subject200K where captions contain descriptive keywords (Section 4.1). The test set is drawn from the same curated distribution. The baselines OminiControl2 and UniCombine are pre-existing models trained on different datasets and regimes. Table 1 therefore pits PKA on in-distribution data against baselines on an out-of-distribution evaluation. A convincing quality claim would require training one model with full attention and one with PKA on the same data, same optimizer, same iterations—holding all variables except the attention structure constant. Without this controlled ablation, it is impossible to attribute the FID/SSIM/CLIP-I improvements to the attention mechanism rather than to training-data curation, the choice of LoRA fine-tuning, or simply favorable distribution match.

- **The headline 10× speedup applies to 16 conditions, but all quality experiments evaluate exactly 2 conditions.** Section 4.2.1 reports efficiency numbers for 1–16 conditions, while Section 4.2.3 evaluates three 2-condition tasks. From Figure 7, the speedup curve shows ~1–2× at 2 conditions. The paper presents the efficiency result and the quality result as jointly validating PKA, but the settings are disjoint. A reader cannot determine whether the method is, say, 1.5× faster in the setting where quality was actually compared. Reporting the latency gap at the 2-condition quality-evaluation setting alongside the scaling plot would unify the evidence.

### Minor

- **A 25% relative Canny F1 gap is mischaracterized as "narrow."** Table 1 shows Subject-Canny F1: UniCombine 0.551, PKA 0.414 — a 25% relative deficit on the primary controllability metric for that task. Section 4.2.3 describes this as "a minor exception of a narrow margin," which is inaccurate. The paper provides no analysis of which component (PAA, KSA, or their interaction) is responsible, nor whether it reflects a systematic failure mode of PAA for edge conditions in the presence of a simultaneous subject condition.

- **Ablation tables (Figures 9 and 10) report only latency, VRAM, and visual examples—no quantitative quality metrics.** For a paper whose central joint claim is efficiency-without-quality-loss, knowing that PAA and KSA each individually preserve quality at the same level as full attention is essential. Even a single column (e.g., SSIM or F1) added to these tables would substantially strengthen the ablation.

- **KSA's dependence on keyword-identifiable prompts is not acknowledged as a limitation.** Section 4.1 explicitly states the training set was curated "ensuring each image caption contains a descriptive keyword." KSA requires identifiable keyword tokens (Section 3.2.2). For free-form prompts without a clear subject keyword, the mask in Equation 3 may activate irrelevant regions silently. This should be stated as a scope limitation rather than left implicit.

### Trivial
None worth raising.

---

## Nice-to-Haves

- Report the specific latency and VRAM numbers at 2 conditions (the setting actually used in Table 1) in Figure 7/8 or the main text, so efficiency and quality are assessed in a unified picture.
- Add a failure analysis: one or two generated examples where the diagonal attention assumption breaks down (e.g., a depth map with non-local structure, or conditions at different resolutions) would clarify the practical scope of PAA.
- A brief decomposition of how much speedup comes from the condition KV-cache alone versus PAA+KSA structural changes would help readers understand the contribution of each component.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **PAA's spatial alignment assumption at different resolutions (harsh critic, Section 3.2.1):** The critic suggests PAA may fail when image and condition grids don't align. For the standard FLUX.1 setup where inputs are patchified at the same resolution, this is a non-issue. There is no evidence in the paper of misalignment, and the paper's scope is FLUX.1 at standard resolutions. Removed as speculative.

- **Condition cache contribution not separately decomposed (harsh critic, Section 4.2.1):** The condition cache is a component of PKA's total speedup, but demanding a breakdown of cache vs. attention structure contribution is a nice-to-have, not a methodological flaw. Demoted to Nice-to-Have.

- **Early-timestep sampling tested only on single condition (harsh critic, Section 3.3):** The critic suggests Figure 5's perturbation analysis may not generalize to multi-condition training. However, the experiment is presented as motivational, and the final training results in Figure 11 are shown under the actual multi-condition fine-tuning setting. This concern is speculative.

- **KSA efficiency gains modest compared to PAA:** The critic correctly notes 16.99→15.33 s (~10%) for KSA versus 15.38→13.63 s for PAA. This is true and informative, but it is not a flaw; KSA is presented as providing both efficiency and subject controllability. The paper does not overclaim KSA's efficiency contribution.

- **Strength: "Comprehensive quantitative evaluation shows state-of-the-art quality" (Strength Finder):** This strength conflicts with the verified major weakness that the comparison is confounded by training regime. A model evaluated on its own training distribution compared against models trained elsewhere does not cleanly demonstrate quality superiority. Removed.

- **Framing of diagonal attention as surprising finding:** The critic notes the diagonal structure follows intuitively from the nature of spatial conditions. This is accurate but is a presentation comment, not a methodological flaw. Removed per pure-nitpick filter.

---

## Novel Insights

The perturbation experiment in Figure 5 is the paper's most standalone contribution: it provides a clean quantitative demonstration that condition influence in flow-matching models is concentrated in early (high-noise) timesteps, motivating a shifted logit-normal sampling distribution during fine-tuning. This insight is generalizable beyond the specific PKA architecture and could inform timestep sampling strategies for any conditional fine-tuning of flow-matching DiTs.

---

## Suggestions

1. **Within-system quality ablation (highest priority):** Train one FLUX.1-LoRA with full attention and one with PKA on identical data/optimizer/iterations, and compare Table 1 metrics. This single experiment would transform the quality claim from "circumstantial" to "causal."
2. **Report 2-condition efficiency numbers** explicitly in Figure 7/8 or the text, to let readers calibrate efficiency vs. quality in the same evaluation setting.
3. **Address the Canny F1 gap honestly:** Analyze whether the 0.414 vs. 0.551 difference comes from PAA's diagonal constraint failing to capture edge-structure globally, or from KSA masking suppressing edge-relevant query positions, and state this as a known limitation.
4. **Add quantitative quality metrics (SSIM or F1/MSE) to Figures 9 and 10** to validate that each module independently preserves quality.
5. **Add a limitations section** covering: (a) KSA's dependence on keyword-identifiable prompts; (b) PAA's assumption of spatial alignment between image and condition grids.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison to PKA |
|---|---|---|---|
| Jt1gGIumJo (Highlight Diffusion) | 3.00 | R1 weak | Lower quality, training-free acceleration with vague evaluation — PKA is clearly stronger |
| iG7qH9Kdao (DiT scaling) | 5.00 | R1 mid | Empirical scaling study, similar scope; PKA has cleaner methodological motivation but comparable evaluation depth |
| D2as3jDmRA (LinFusion) | 6.25 | R1 mid | Linear attention for high-res SD, tested on multiple architectures; more comprehensive but similar in scope — PKA is slightly weaker due to confound |
| qmXedvwrT1 (LEGO bricks) | 6.67 | R1 mid | Efficient DiT backbone, accepted; stronger experimental coverage and cleaner ablations than PKA |
| gU58d5QeGv (Würstchen) | 8.00 | R1 strong | Full architecture redesign with user studies; far more comprehensive than PKA |
| 3Gga05Jdmj (CtrLoRA) | 6.00 | R2 narrow | Controllable gen with LoRA, clean ablations, comparable scope — PKA is weaker due to quality comparison confound |
| taHwqSrbrb (DyDiT) | 5.50 | R2 narrow | DiT efficiency via timestep+spatial redundancy, broader evaluation, cleaner comparison (same pre-trained model) — PKA is comparable but narrower |
| BWuBDdXVnH (ControlAR) | 6.25 | R2 narrow | Controllable gen for AR models, clean methodology — PKA is weaker due to unfair comparison methodology |

**Round 1 bracket:** 4.5–6.5.

**Round 2 narrowing:** The closest comparators are DyDiT (5.50) and CtrLoRA (6.00). DyDiT has cleaner evidence because it ablates on the same pre-trained model with no training-distribution confound. CtrLoRA has comprehensive coverage across conditions. PKA is comparable to DyDiT in motivation quality and execution but falls below it on experimental rigor: the training-regime confound in Table 1 is more serious than any single weakness in DyDiT, and the Canny F1 gap is left unexplained. PKA lands between DyDiT (5.50) and the lower end of the bracket, closer to 5.0.

**Axis assessment:**
- *Originality:* Moderate — PAA and KSA exploit well-understood structural priors (diagonal spatial attention, subject locality), but the combination and the early-timestep insight are a novel system contribution.
- *Importance:* Clear practical relevance — multi-condition DiT control is a real bottleneck as condition counts grow.
- *Claims supported:* Partially — efficiency claims are well-supported; quality claims are confounded by training setup.
- *Soundness of experiments:* Mixed — efficiency experiments are solid; quality comparison is methodologically weak.
- *Clarity:* Good. The paper is readable and well-organized.
- *Value to community:* Moderate — the early-timestep insight and condition-caching design are useful; the quality comparison leaves open whether PKA truly trades off nothing for speed.

**Final score: 5.0 (Reject)** — PKA's efficiency contributions are principled and its early-timestep insight is genuine, but the paper's central joint claim (efficiency without quality loss) is not cleanly supported. The quality comparison is confounded by training regime, the headline speedup is decoupled from the quality evaluation setting, and a key controllability gap is mischaracterized. These are addressable weaknesses, but as submitted they prevent confident acceptance. The paper is comparable to DyDiT in ambition but falls short on experimental rigor.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>