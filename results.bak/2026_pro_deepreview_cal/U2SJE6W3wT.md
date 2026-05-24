Now I have enough calibration data. Let me analyze the comparisons and write the final review.

**Calibration Summary:**

| Anchor Paper | Avg Score | Round | Comparison to AdcVSR |
|---|---|---|---|
| Self-distillation for diffusion (QKqWnNkwPL) | 3.00 | R1 Low | AdcVSR far stronger — comprehensive experiments, novel architecture, clear gains |
| AddSR (BpKbKeY0La) | 5.00 | R1 Mid | AdcVSR stronger — more thorough evaluation, video capability, dual-head novelty |
| Does Diffusion Beat GAN (46mbA3vu25) | 5.75 | R2 | AdcVSR stronger — more constructive contribution (builds vs analyzes), broader scope |
| AugKD (AC3713Fmhx) | 6.00 | R2 | AdcVSR stronger — video domain is harder, dual contributions, more comprehensive |
| T2V-Turbo-v2 (BZwXMqu4zG) | 6.00 | R2 | AdcVSR stronger — more novel architectural contribution, better ablation depth |
| Video Inverse Problems (TRWxFUzK9K) | 6.50 | R2 | AdcVSR comparable/slightly stronger — blind setting is more practical, broader evaluation |
| InstaFlow (1k4yZbbDqX) | 7.00 | R2 | Comparable — both have clear novel methods with thorough experiments |
| Shortcut Models (OlzB6LnXcS) | 8.00 | R2 | Shortcut Models stronger — broader applicability, cleaner conceptual contribution |
| FRB (MEbNz44926) | 8.00 | R1 High | FRB is more specialized but extremely well-executed; AdcVSR slightly below this tier |

**Bracket:** Round 1 placed it between 5.0 and 8.0. Round 2 narrowed to 6.5-7.5. The paper is clearly stronger than the 6.0-6.5 anchors and comparable to InstaFlow (7.00), but not quite at the 8.00 level of Shortcut Models or FRB.

Now let me write the consolidated review.

---

## Summary

This paper proposes AdcVSR, an improved adversarial diffusion compression method for real-world video super-resolution. It distills a large 3D DiT teacher (DOVE) into a compact "2D + 1D" student that augments a pruned 2D Stable Diffusion backbone with lightweight 1D temporal convolutions, and introduces a dual-head, dual-discriminator adversarial scheme that disentangles detail and consistency optimization. The resulting model achieves a 95% parameter reduction and 8× speedup over its teacher while maintaining competitive video quality and achieving the best temporal consistency among all compared methods.

## Strengths

- **The "2D + 1D" architecture is an elegant and well-validated design choice.** Table 2 and Figure 5 show that the 2D-only backbone fails catastrophically (\(E_{\text{warp}}^* = 4.43\), DISTS = 0.2418), while adding 1D temporal convolutions closes the DISTS gap to a pruned 3D DiT to just 0.0014 (0.2112 vs. 0.2098) and achieves the best warping error (\(E_{\text{warp}}^* = 1.67\)) — all at 0.55B parameters vs. 8.36B for the 3D model. This directly validates the core hypothesis that lightweight 1D temporal convolutions suffice for temporal consistency in the Real-VSR setting.

- **The dual-head, dual-discriminator adversarial scheme is novel and demonstrably effective.** Table 3 provides clean evidence: the single-head variant achieves decent CLIP-IQA (0.6745) but catastrophic warping error (6.32), the single-domain variant improves consistency (3.59) but sacrifices perceptual quality (0.6421), while the proposed dual-head, dual-domain design achieves the best of both (CLIP-IQA 0.6861, \(E_{\text{warp}}^* = 2.22\)). The five-type data curation for independent detail/consistency labels (Eq. 5) is a thoughtful and well-justified solution to the detail-consistency conflict identified in prior work.

- **Comprehensive and fair experimental evaluation.** The paper compares against 10 baselines spanning non-generative, multi-step diffusion, one-step diffusion, and Real-ISR methods across 6 test datasets (3 synthetic, 3 real-world). The efficiency gains are substantial and well-documented (Table 1, Figure 4). The ablation studies (Tables 2-4) systematically isolate the effect of each design choice: network architecture, discriminator design, and teacher/adversarial setup.

- **Practical significance.** The 95% parameter reduction (10.55B → 0.57B) and 8× inference speedup (4.42s → 0.55s) while maintaining competitive video quality represents a meaningful step toward deployable diffusion-based video super-resolution.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No analysis of what the 1D temporal convolutions actually learn.** The paper makes a plausible argument that 1D convolutions suffice for temporal consistency, and the ablation results support this. However, without any analysis of the learned temporal dynamics (e.g., effective receptive field, filter response patterns, or whether the convolutions simply average adjacent frames), the design rationale remains a plausible hypothesis rather than an experimentally grounded insight. This does not threaten the paper's contribution but would deepen understanding of why the "2D + 1D" design works.

- **The claim that dual-head discriminators provide "separate weight gradients for both" objectives (Sec. 3.3, final paragraph) is not directly verified.** The end-to-end metric improvements in Table 3 demonstrate the effect, but there is no gradient-level evidence (e.g., gradient norm or cosine similarity between heads) showing that the optimization is actually decoupled. This leaves a gap between the mechanistic claim and the empirical support.

### Trivial

- No explicit limitations paragraph in the main text (e.g., reliance on a powerful teacher like DOVE, potential sensitivity to extreme motion beyond training distribution). The appendix is referenced as containing further discussion (line 246).

## Nice-to-Haves

- Reporting variance/confidence intervals for the key metrics in Table 1 (even if only in the appendix) would strengthen confidence in the reported results, though single-run evaluation is standard in large-scale video SR benchmarks.
- A brief profiling breakdown of inference time (2D backbone vs. 1D convolutions) would help readers understand where the efficiency gains come from given that efficiency is a primary contribution.
- An analysis of the temporal receptive field or filter responses of the 1D convolutions would transform the architectural hypothesis into an experimentally grounded insight.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Could briefly clarify whether the augmented SD UNet used as the feature-domain discriminator backbone is identical to the student's own augmented UNet"** — The paper already states this explicitly on line 141: "the feature-domain discriminator exploits the same pretrained augmented SD UNet from the first stage (also frozen)." The concern about "data leakage" is speculative and unsupported by any evidence in the paper. REMOVED.

- **"No measure of variance for the metrics"** — Moved to Nice-to-Haves. Single-run evaluation is standard in large-scale video SR benchmarks; this is not a weakness by community norms.

- **"Inference breakdown is not discussed"** — Moved to Nice-to-Haves. This is a presentation enhancement, not a substantive weakness.

## Novel Insights

The paper's most distinctive contribution is the demonstration that a five-type curated data scheme with independent detail/consistency labels for dual-head discriminators can effectively resolve the optimization conflict between spatial detail and temporal consistency in video super-resolution. This goes beyond the standard GAN discriminator paradigm by restructuring adversarial supervision into a multi-attribute form, producing fine-grained and disentangled signals. The insight that real images (repeated as static pseudo-videos) provide "real" labels for both heads, while temporally shuffled videos provide "fake" consistency labels, is an elegant and generalizable data curation strategy that could inform future work on multi-objective adversarial training for video generation.

## Suggestions

- Include a brief analysis of the 1D temporal convolutions' learned behavior (e.g., effective receptive field, filter visualization on synthetic motion patterns). This would turn the "2D + 1D" hypothesis from a plausible assumption into an experimentally grounded insight without requiring new baselines or datasets.
- Add a short limitations paragraph to the main text (current line 246 references the appendix, but a one-sentence pointer to key limitations would improve transparency).
- Consider computing gradient cosine similarity between the detail and consistency heads during training to provide direct mechanistic evidence for the disentanglement claim.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>