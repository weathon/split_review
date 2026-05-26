Now I have thoroughly read the paper and analyzed the reviewer claims. Let me construct the final consolidated review.

## Summary

This paper proposes Patch-wise and Keyword-Aware Attention (PKA), a framework that decomposes the expensive full-attention mechanism in multi-condition Diffusion Transformers into two specialized modules: Position-Aligned Attention (PAA) for spatial conditions (achieving O(N) complexity via one-to-one alignment) and Keyword-Scoped Attention (KSA) for subject conditions (using temporally-reused keyword masks). Complemented by a condition KV cache and an early-timestep training sampling strategy, PKA achieves up to **10× inference speedup and 5.12× VRAM reduction** versus the concatenate-and-attend baseline while maintaining competitive generative quality.

## Strengths

1. **Principled redundancy analysis that directly motivates architectural design (Figures 2 & 3).** The paper provides empirical attention-matrix visualizations showing diagonal dominance for spatial-aligned conditions and sparse keyword-correlated activation for subject-driven conditions. This categorization is not observational—it directly drives the two-module design (PAA and KSA), clearly distinguishing PKA from generic token-pruning or layer-skipping approaches in prior efficient DiT work (Section 2.2).

2. **PAA achieves provably O(N) complexity with practical efficiency gains over sliding-window attention (Eq. 2, Figure 9).** The ablation shows PAA at 13.63s/237MB versus the best sliding-window-attention variant at 14.00s/276MB, with qualitatively equivalent outputs. This demonstrates that the structural prior (spatial alignment) yields a strictly better efficiency–quality trade-off than generic sparsity patterns.

3. **KSA's mask-reuse mechanism cleanly decouples sparsity computation from attention (Eqs. 3–4, Figure 10).** Computing the keyword relevance mask once at timestep t and reusing it at t+1 avoids redundant per-step sparsity estimation. The threshold sweep (ε from 0 to 0.8) shows a graceful, controllable degradation from 368MB/16.99s (full) to 229MB/15.17s (ε=0.8), giving users an explicit efficiency–fidelity dial.

4. **Scalable efficiency across a wide range of condition counts (Figures 7 & 8).** While UniCombine exhibits polynomial explosion (~175s/~2000MB at 16 conditions), PKA scales near-linearly (~20s/~400MB). The measured speedups (3.90×–10.0×) and VRAM reductions (2.46×–5.12×) are directly measured on a single GPU and form the paper's strongest empirical contribution.

5. **Competitive quantitative quality alongside the efficiency gains (Table 1).** On three 2-condition tasks, PKA achieves the best FID across all tasks (e.g., 52.99 vs 61.03 on Subject-Canny), best SSIM (0.613 vs 0.508 on Canny-Depth), and best subject consistency (DINOv2 0.926 vs 0.901 on Subject-Canny), showing that the efficiency gains do not come at a catastrophic quality cost.

## Weaknesses

### Fatal

None.

### Major

1. **Ambiguity in the baseline comparison protocol undermines the quality/controllability claims.** The paper states, "To ensure a fair comparison, we fine-tune the FLUX.1 model using LoRA" (Section 4.1, Training Details), but it never explicitly states that OminiControl2 and UniCombine received the same LoRA fine-tuning on the same curated subset of Subject200K. If the baselines were used from pre-trained checkpoints while PKA received dataset-specific fine-tuning, then the quality differences in Table 1 could be partly attributable to the fine-tuning rather than to the attention mechanism itself. The efficiency results (Figures 7–8) are unaffected by this issue, but the claim that PKA "maintains or improves generative quality" is weakened. The authors should clarify whether all methods received equal fine-tuning and, if not, transparently discuss the limitation.

2. **Condition KV cache rests on an unverified architectural assumption.** The cache caches K/V projections of condition tokens after the first denoising step, implicitly assuming these representations are timestep-invariant. In DiT architectures such as FLUX, transformer blocks include timestep-conditioned components (e.g., modulation layers, shared normalization) that could alter condition-token representations across timesteps. The paper provides no empirical evidence (e.g., measuring L2 drift or cosine similarity of condition-token outputs across timesteps) to justify the cache. While the end-to-end qualitative results suggest the method works despite this, the lack of validation means the reader cannot assess how much of the measured speedup relies on a potentially invalid approximation, nor whether the approach would transfer to other DiT architectures.

3. **Generative quality is measured only at 2 conditions, while the headline efficiency numbers target up to 16 conditions.** Figures 7–8 show the scalability of time and memory up to 16 conditions (the regime where the 10× speedup is achieved), but every quality and controllability evaluation in Table 1 uses exactly 2 conditions. As conditions increase, interactions between multiple spatial and subject inputs could degrade fidelity in ways not captured by the 2-condition tests. Without evidence that quality survives at 4, 8, or 16 conditions, the practical significance of the largest claimed speedups is unclear.

### Minor

1. **F1 score on Subject-Canny contradicts the "maintains or improves controllability" claim.** PKA achieves F1=0.414 versus UniCombine's F1=0.551—a ~25% relative gap on a controllability metric. The paper characterizes this as a "narrow margin," but for edge-based controllability, this is a meaningful degradation. The claim of maintained/improved controllability should be qualified to reflect this gap.

2. **Ablation studies lack quantitative quality metrics.** The PAA ablation (Figure 9) and KSA threshold sweep (Figure 10) report only latency and VRAM, not FID, SSIM, subject consistency, or controllability scores. The reader cannot determine whether the efficiency gains from PAA/KSA come with a quality penalty that the full-attention baseline avoids. Similarly, the early-timestep sampling evaluation (Figure 11) is purely qualitative—no FID or convergence metrics are reported.

3. **Several experimental details needed for reproducibility are missing.** The LoRA rank, the exact μ and δ values for the shifted logit-normal sampling distribution, the procedure for extracting descriptive keywords from captions, and the architectural specification of how SP/SJ condition tokens are injected into FLUX layers are not provided.

4. **KSA's temporal-consistency assumption is not quantified.** KSA reuses a binary mask from timestep t at timestep t+1. The paper provides no measurement of mask overlap across timesteps (e.g., IoU or pixel overlap fractions), making it unclear how much approximation error the reuse introduces.

5. **FID usage in this multi-condition setting warrants justification.** FID is computed between generated images and ground-truth images, where the condition set includes a subject image that is not the same as the target image. This deviates from the standard FID evaluation protocol (comparing distributions of real vs. generated images of the same domain), and the paper does not discuss why FID is appropriate here.

### Trivial

- **Quantitative results in Table 1 lack error bars or confidence intervals.** Metrics like FID, CLIP-I, and DINOv2 can vary with random seed; reporting single-run values makes it difficult to assess the statistical robustness of the reported improvements.

## Nice-to-Haves

- The paper would benefit from a discussion of scenarios where the core assumptions break down (e.g., non-aligned spatial conditions, subject conditions without a clear keyword in the text prompt).
- Providing per-metric error bars (at least 3 runs) for Table 1 would strengthen confidence in the quality comparisons.
- Extending quality evaluation to higher condition counts (4, 8, 16) would directly connect the efficiency scaling results to quality preservation.

## Removed Points

These points were raised by the reviewers but are removed from the main review for the following reasons:

- **"Source of attention matrices not made explicit" (Section 1–2):** The paper specifies the analysis is on "existing multi-condition DiTs (Tan et al., 2024)" (line 21); the reference is clear enough for readers to check. This is closer to a citation-level detail than a substantive weakness.
- **"Mismatched resolution handling in PAA":** The paper's scope is conditions spatially aligned with the image (Canny, depth maps). Asking how non-aligned conditions would be handled stretches beyond the stated scope; the method is designed for the aligned case and this is made explicit.
- **"Generalizability of keyword requirement":** The Subject200K dataset was introduced by OminiControl for subject-driven generation; filtering for captions containing keywords is a standard curation step for this task. The concern is speculative and not anchored in a specific flaw in the paper.
- **"Stronger baseline equalization" from the Strengthening section:** While re-training baselines is ideal, it is not standard practice in this field (baselines have distinct architectures that are not plug-and-play with a single LoRA recipe). The reviewer's suggestion, though well-intentioned, demands a level of comparison that goes well beyond community norms and is more appropriate as a nice-to-have.
- **"Discussion of limitations" request:** The paper's conclusion is appropriately scoped. The absence of a dedicated limitations section is not a weakness—many papers at this level do not include one, and the relevant boundary conditions are implicitly conveyed by the experimental design.

## Novel Insights

The review process surfaces one insight beyond the paper's own contributions. The paper's core efficiency claims (10× speedup) come from a combination of (a) O(N) PAA, (b) sparsity from KSA, and (c) the condition KV cache. However, the cache assumption—that condition-token representations are timestep-invariant—is the least validated component, yet it contributes significantly to the wall-clock savings. A systematic ablation that disentangles how much of the speedup comes from each component (PAA alone, KSA alone, cache alone) under equal-quality conditions would substantially strengthen the paper. The current ablations measure efficiency but not quality, leaving this decomposition ambiguous.

## Suggestions

1. **Clarify the baseline comparison protocol.** State explicitly whether OminiControl2 and UniCombine received the same LoRA fine-tuning on the same data. If they did not, add a sentence acknowledging the limitation and arguing why the comparison remains informative (e.g., the baselines used their official pre-trained weights, which were also trained on the same domain).
2. **Validate the condition cache.** Measure the cosine similarity or relative L2 change of condition-token K/V between timesteps under the deployed architecture. If the change is negligible (<1%), report this to justify the cache. If it is non-negligible, discuss why the method still works despite the approximation.
3. **Report quality metrics at higher condition counts.** Even a single experiment with 4 or 8 conditions (mixing spatial and subject inputs) with FID and controllability metrics would bridge the gap between the efficiency scaling results and the quality evaluation.
4. **Add quantitative metrics to the ablation studies.** Report FID and at least one controllability metric for the PAA vs. full/SWA comparison and for at least two KSA threshold settings. This would allow readers to assess whether efficiency gains trade off quality.
5. **Provide missing experimental details** (LoRA rank, exact μ and δ values, keyword extraction procedure) either in the main text or supplementary material.

## Score and Decision

The paper makes a genuine contribution: the attention-redundancy analysis is well-motivated, the PAA and KSA modules are architecturally clean, and the efficiency scaling plots (up to 10× speedup, 5.12× VRAM reduction) are compelling. The core efficiency claims are well supported by direct measurement. The main weaknesses are (1) ambiguity in whether the quality comparison controlled for fine-tuning, (2) an unvalidated condition-cache assumption, and (3) quality evaluation limited to only 2 conditions despite speedup claims at 16. These are significant gaps but not fatal—they can be addressed with additional experiments and clarifications. The paper presents solid, timely work that would benefit from the suggested revisions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>