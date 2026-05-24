Now let me write the final consolidated review.

## Summary

This paper proposes PKA (Patch-Wise and Keyword-Aware Attention), a decomposed attention mechanism for multi-condition Diffusion Transformers. It replaces the costly "concatenate-and-attend" paradigm with two specialized modules: Position-Aligned Attention (PAA) for spatial conditions (one-to-one token alignment) and Keyword-Scoped Attention (KSA) for subject conditions (masked attention scoped to keyword-relevant regions). The system is built on FLUX.1 with LoRA fine-tuning, and includes a Condition Cache (KV reuse across denoising steps) and an early-timestep sampling strategy that skews training toward the high-noise regime where visual conditions exert strongest influence. Experiments report up to 10× inference speedup and 5.12× VRAM reduction over full-attention baselines, with competitive or better FID, SSIM, CLIP-I, and DINOv2 scores across three multi-condition tasks.

## Strengths

1. **Well-motivated architectural decomposition grounded in attention sparsity analysis.** Figures 2-3 empirically demonstrate that spatial-condition attention is diagonally concentrated and subject-condition attention is localized to keyword-relevant regions. This evidence directly justifies PAA's one-to-one alignment and KSA's mask-based pruning, distinguishing the approach from generic token-pruning or layer-removal methods.

2. **Substantial and clearly demonstrated efficiency gains.** Figures 7-8 show that PKA achieves a 3.90×–10× speedup and 2.46×–5.12× VRAM reduction across 1–16 conditions on an RTX 6000 Ada GPU, with clean scaling trends. The Condition Cache mechanism (KV computed once per condition, reused for all denoising steps) is a simple but effective complement. These efficiency claims are architecture-intrinsic and not confounded by training configuration.

3. **Ablations confirm the design choices.** PAA is shown (Figure 9) to outperform sliding-window attention at every window size in both latency and VRAM (13.63s/237MB vs. 14.00s/276MB for SWA-1). KSA's threshold ε (Figure 10) provides a graceful, tunable efficiency–fidelity trade-off. The PAA vs. SWA comparison is a clean, controlled experiment that validates the one-to-one alignment design.

## Weaknesses

### Major

1. **Baseline quality comparison may be confounded by training configuration.** The paper states it "fine-tunes FLUX.1 using LoRA" for the proposed method but does not specify whether the baselines (OminiControl2, UniCombine) were fine-tuned under identical conditions (same dataset subset, same LoRA rank, same 20k iterations, same optimizer). The caption says "We employ OminiControl2 and UniCombine as baselines for our comparative analysis" without describing any additional fine-tuning of these baselines. Since Table 1 is the main evidence for the claim that PKA "maintains or improves generative quality," the risk that quality differences stem from different training recipes rather than the attention mechanism itself is a significant confound. The efficiency comparisons (Figures 7–8) are architecture-intrinsic and unaffected, but the quality claim needs clarification. The authors should either (a) confirm that baselines were fine-tuned identically, (b) justify why off-the-shelf checkpoints are directly comparable, or (c) retrain baselines under matched conditions.

2. **High absolute FID values go undiscussed.** The reported FID scores range from 52.99 to 80.20 across tasks. These are unusually high even for conditional generation on challenging datasets. The paper should explain whether this is due to small reference set size, low resolution, extreme task difficulty, or another factor. Without context, the absolute numbers undermine confidence in the evaluation protocol, even if the relative ordering is consistent.

### Minor

3. **Early-timestep sampling lacks quantitative validation.** Figure 11 provides visual convergence evidence for one example (alarm clock) showing that μ=0.5, δ=1.5 produces recognizable structure faster than standard or late-biased sampling. However, no quantitative metrics (FID, subject consistency scores, or CLIP-T) are reported for the full test set comparing the proposed early-timestep sampling against the standard logit-normal distribution. The visual evidence, while suggestive, is insufficient to support the claim that the strategy "enhances final control fidelity." Additionally, the paper states "μ > 0, δ > 1" as the condition and shows μ=0.5, δ=1.5 in Figure 11, but does not state which values were used in the main experiments (Table 1, Figures 7–8).

4. **KSA mask update schedule is underspecified.** Equation 3 generates a binary mask M^t at timestep t, and Equation 4 reuses it at timestep t+1. The paper invokes "temporal consistency" but does not state whether the mask is recomputed at every step, recomputed periodically every k steps, or computed once at step 0 and frozen for all remaining steps. If the mask is frozen, there is no empirical evidence (e.g., mask overlap between distant steps) that it remains valid throughout denoising, especially in later stages where fine details emerge. This matters because an invalid mask could silently degrade subject fidelity.

5. **Keyword selection for KSA is not specified.** The paper says "the keyword set 𝕂 typically contains just 1 to 2 tokens" and notes the dataset is curated so "each image caption contains a descriptive keyword." This suggests keywords are known a priori from dataset construction. For practical deployment, automatic keyword extraction would be needed, and failure cases (ambiguous keywords, multiple subjects, no keyword in caption) are not discussed. The paper should at least acknowledge this limitation and describe whether keywords were manually annotated or extracted automatically.

6. **LoRA rank and adapted layers are not reported.** The paper states LoRA is used for fine-tuning but provides no details about rank, which modules/layers were adapted, or how many additional parameters were introduced. This is a standard reporting expectation for reproducibility.

### Trivial

- The paper reports "w/o KSA" latency as 16.99s (Figure 10) but "w/o PAA" latency as 15.38s (Figure 9). These numbers describe different configurations (full attention for subject vs. full attention for spatial), but the discrepancy is not explained and could confuse readers.
- The paper uses "condition" loosely to mean both a modality type and one instance of it; clarifying in §4.2.1 would help.
- Dataset split sizes (training/testing) for the Subject200K subset are not reported.

## Nice-to-Haves

- **Quantitative ablation for early-timestep sampling.** Reporting FID and subject consistency on the full test set for the standard vs. shifted logit-normal distribution, even in the appendix, would substantially strengthen the paper.
- **End-to-end VRAM and latency** (not just attention-module), since total savings may be diluted by non-attention components (embeddings, MLPs, etc.).
- **Failure case discussion.** When does PAA break (non-aligned conditions)? When does KSA degrade (ambiguous keywords, multiple subjects)? This would increase the paper's realism and practical value.

## Removed Points

- *"PAA assumes perfect spatial alignment and does not discuss non-pixel-aligned conditions."* — For the spatial conditions used (Canny edges, depth maps), pixel alignment with the output image is inherent by construction; this is not a meaningful weakness.
- *"The Condition Cache is a standard KV-cache trick."* — This is not a weakness; it is a design choice. The paper's contribution is PAA/KSA, not the cache itself, and the cache is clearly described as complementary.
- *"OminiControl2 might not have been fine-tuned on the Subject200K subset at all."* — This speculation goes beyond what can be verified from the paper. The weakness about baseline fairness (Weakness 1 above) captures the valid concern without speculation.
- *"The KSA w/o KSA vs PAA w/o PAA latency discrepancy should be explained."* — Moved to Trivial.
- Several generic formatting/style nitpicks (not listed individually as they are parser artifacts).
- Generic strength claims about "the paper addresses an important problem" — moved here as superficial.

## Novel Insights

The key insight that spatial-condition and subject-condition attention in multi-condition DiTs exhibit fundamentally different sparsity patterns (diagonal-localized vs. keyword-scoped) is well-supported and leads to a clean architectural decomposition. The PAA idea of replacing full cross-attention with per-position one-to-one attention is the most novel contribution — it is surprisingly simple yet effective, and the ablation showing it beats sliding-window attention at all window sizes validates that the sparsity is truly diagonal, not just locally banded. This is a conceptually crisp finding.

## Suggestions

1. **Most important**: Clarify the baseline training protocol for Table 1. State explicitly whether OminiControl2 and UniCombine were fine-tuned under the same conditions as PKA (same data subset, same LoRA setup, same iterations). If they were not, retrain or provide a careful justification.
2. **Report full quantitative results** for the early-timestep sampling ablation on the test set (e.g., FID, subject consistency, CLIP-T) and specify the μ, δ values used in the main experiments.
3. **Specify the KSA mask update schedule** (recompute frequency) and provide evidence of mask validity across steps.
4. **Add a brief discussion** of the high absolute FID values.
5. **Report LoRA rank** and adapted modules.

## Score and Decision

### Calibration

**Round 1 bracket:** Between 3.5 and 7.5.

**Round 1 anchors explored:**
- wGVOxplEbf (SaRA, avg 6.20, Accept) — An efficient diffusion model fine-tuning method with extensive experiments; accepted. PKA has stronger architectural novelty but weaker baseline controls.
- 3kADTLbKmm (SparseDM, avg 4.00, Reject) — Sparse masks for diffusion models; rejected for incremental contribution. PKA has clearer motivation and stronger efficiency results.
- vNZIePda08 (Sparse-to-Sparse, avg 4.75, Reject) — Sparse-to-sparse training of diffusion models; rejected as incremental. PKA has more novel architectural insight.

**Round 2 narrowing:** Bracket refined to 5.0–6.5.

**Round 2 anchors explored:**
- taHwqSrbrb (DyDiT, avg 5.50, Accept) — Dynamic computation in DiT along timestep and spatial dimensions; accepted despite implementation-detail concerns. PKA has stronger efficiency numbers and comparable methodological novelty.
- D2as3jDmRA (LinFusion, avg 6.25, Reject) — Linear attention for diffusion; rejected despite high scores. PKA has similar concerns about experimental comparison fairness.
- wGVOxplEbf (SaRA, avg 6.20, Accept) — Repeated from round 1 for direct comparison.

**Comparison summary:** The paper is stronger than SparseDM (4.00) and Sparse-to-Sparse (4.75) in both motivation and method novelty. It is weaker than SaRA (6.20) and LinFusion (6.25) in experimental rigor due to the baseline comparison gap. It is comparable to DyDiT (5.50) in overall quality — both have genuine contributions alongside experimental gaps that are addressable in rebuttal. The paper sits above reject-level papers (3–5) due to a well-supported core efficiency claim and clean architectural insight, but below clearly strong papers (7+) due to the unaddressed confound in the quality comparison. I calibrate the score to 5.5.

**All retrieved anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Jt1gGIumJo | 3.00 | R1 | Much weaker; lacks method and evaluation |
| vK8C37eHXM | 3.20 | R1 | Much weaker; different topic |
| W4djmqKZC6 | 3.00 | R1 | Much weaker |
| IqGVIU4rvM | 2.50 | R1 | Much weaker |
| 3kADTLbKmm | 4.00 | R1 | Weaker; less clear motivation, modest gains |
| vNZIePda08 | 4.75 | R1 | Weaker; incremental sparse training application |
| wGVOxplEbf | 6.20 | R1/R2 | Stronger; cleaner experiments despite lower novelty |
| DDxLsxiZR8 | 4.00 | R1 | Weaker; token pruning with modest results |
| fV0t65OBUu | 8.00 | R1 | Much stronger; top-tier paper |
| OvoCm1gGhN | 8.00 | R1 | Much stronger; top-tier paper |
| gU58d5QeGv | 8.00 | R1 | Much stronger |
| OfjIlbelrT | 8.00 | R1 | Much stronger |
| taHwqSrbrb | 5.50 | R2 | Comparable; accepted, similar experimental depth |
| w6YS9A78fq | 5.00 | R2 | Slightly weaker |
| wiYV0KDAE6 | 5.75 | R2 | Comparable (different domain) |
| D2as3jDmRA | 6.25 | R2 | Comparable strength but rejected; similar baseline concerns |
| UmMa3UNDAz | 6.50 | R2 | Stronger |
| 3BhZCfJ73Y | 6.25 | R2 | Stronger |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>