Now let me run the calibration search to properly score this paper.Round 1 bracket: **4.5 – 6.0**. MaskComp has a real novel mechanism with ablations, but weak baselines and metric issues put it clearly below IterComp (6.8). Let me narrow within the bracket.Now I have enough to write the final review. Let me synthesize everything.

**Round 1 bracket: 4.5 – 6.0**
- MaskComp's novel IMD mechanism and solid ablations put it above the 1.5–3.0 weak anchors
- Missing task-specific baselines and metric limitations put it below EmerDiff (6.0) and IterComp (6.8)

**Round 2 narrowing:**
- Closer to Diffree (4.75, Reject) and G4Seg (5.4, Reject) than to EmerDiff (6.0, Accept)
- MaskComp has more novel mechanism than Diffree but shares the "fine-tuned vs. zero-shot" baseline problem
- The amodal baseline (Table d) partially mitigates the "no task-specific comparison" concern
- Final score: **5.0**

---

## Summary

MaskComp addresses the object completion task — reconstructing a fully visible object from its occluded partial view — by introducing an Iterative Mask Denoising (IMD) process. The key idea is to treat the partial object mask as a noisy version of the complete mask, then iteratively refine it via alternating generation (a trained CompNet built on ControlNet) and segmentation (SAM) stages. A mask voting mechanism aggregates N generated samples per step to produce a progressively more complete mask condition, which in turn improves generation quality. The method includes a time-variant gating operation and an auxiliary mask prediction loss.

---

## Strengths

- **Novel IMD formulation with clear motivation**: The core observation — that conditioning generation on more complete masks yields more complete objects — is directly verified in Table (conditioned mask), showing FID improvement from 16.9 (partial mask) to 15.3 (intermediate mask) to 12.7 (complete mask). The iterative mechanism that follows from this is logical and coherent.

- **Thorough ablation of all design components**: Tables 1 and more-ablation systematically isolate the contribution of (a) segmentation network choice (SAM vs. CLIPSeg vs. SEEM: FID 16.9 vs. 19.9 vs. 18.1), (b) number of IMD steps (T=1: 24.7 → T=5: 16.9 → T=7: 16.1), (c) number of sampled images (N=4: 17.4 vs. N=5: 16.9), (d) condition gating (16.9 with vs. 18.2 without), (e) mask loss (16.9 with vs. 17.7 without), and (f) voting strategy (logits voting best at 16.9). This level of ablation is thorough and justifies each design choice.

- **Robustness to segmentation errors demonstrated**: Table (robust) shows that introducing 15% area random mask noise slows convergence but still reaches FID 16.5 after 9 iterations vs. 15.9 without noise — demonstrating that errors are not amplified through the loop.

- **Amodal segmentation baseline comparison**: Table (ablation, d) compares against a two-stage pipeline (AISFormer amodal masks + ControlNet generation) achieving FID 29.4 vs. MaskComp 16.9. This provides some evidence that the joint iterative generation–segmentation loop outperforms a decoupled two-stage approach, partially addressing concerns about task-specific comparison.

- **Operates without complete object supervision**: Table (more ablation, c) shows MaskComp degrades from 16.9 to 19.4 FID when trained without complete object annotations — still competitive — demonstrating practical applicability to in-the-wild scenarios.

---

## Weaknesses

### Fatal
*None.*

### Major

- **Baselines in the main comparison are not designed for object completion**: Table (main results) compares MaskComp — fine-tuned for 50 epochs on AHP and 36 epochs on OpenImage — against ControlNet, Kandinsky 2.1, SD 1.5, and SD 2.1 used off-the-shelf without any task-specific adaptation. These models are generic text-driven image synthesizers. The reported FID gap (MaskComp: 16.9 vs. baselines: 30.0–43.9 on AHP) therefore reflects task-specific training at least as much as architectural advantage. The paper acknowledges the amodal comparison (Table d), where the amodal baseline uses ControlNet without fine-tuning, but this is also not a fully fair comparison. Without a single specialized object-completion or amodal-completion model fine-tuned under comparable conditions, the paper cannot establish whether IMD represents a principled advance over prior completion approaches or simply benefits from supervised training on a task-specific dataset.

- **FID does not measure instance-level completion quality, and the user study is underspecified**: The paper explicitly acknowledges that "FID cannot reflect object completeness" (Section 4.1), yet no completeness-specific per-instance metric is introduced. Per-instance mask IoU against ground-truth complete masks, or per-instance LPIPS/SSIM restricted to the completed region, would directly validate whether IMD closes the gap to the true complete shape. The user study provides partial instance-level signal, but the number of participants, number of images evaluated, and statistical significance are not reported. A "Best" rate of 0.53 is a striking result that warrants a significance test.

### Minor

- **Inference time ambiguity**: Table (ablation, c) reports "Gen: 14.3s | Segm: 1.2s | Total: 15.5s" for "one IMD step." However, with N=5 images sampled per step and T=5 steps, the actual cost is at minimum 5×14.3×5=357.5s for the generation component alone (assuming sequential generation), before the final completion pass. The table makes 15.5s appear to be the total per-completion cost. The paper does mention a speed-up approximation (reducing diffusion steps in early iterations), but the baseline cost is never stated clearly, which makes the throughput comparison difficult to assess.

- **Threshold τ=0.5 for mask voting is not ablated**: The voting rule (Eq. 3) directly determines where the refined mask boundary falls, yet only voting *strategy* (logits vs. mask) is ablated in Table (more ablation, d). The threshold τ=0.5 is fixed without justification or sensitivity analysis.

- **Gibbs sampling analogy asserted without formal justification**: Section 3.4 presents IMD as a "Gibbs sampling-like" process and claims it samples the joint distribution p(I, M). Standard Gibbs sampling convergence requires the chain to be ergodic with respect to the target distribution — a property that depends on characteristics of CompNet and SAM that are never characterized. The paper appropriately hedges with "like," but the theoretical section raises expectations that it does not satisfy. The empirical evidence (FID decreasing with iteration count) is more convincing than the theory and should be the primary argument.

- **FID-S evaluation may favor MaskComp**: FID-S uses SAM-segmented foreground regions for FID computation. Since MaskComp's own outputs go through SAM during the IMD process, SAM may segment MaskComp outputs more cleanly than the baselines, potentially inflating the FID-S advantage. FID-G (using GT masks) is less susceptible to this bias and is the metric to trust; reviewers and readers should weigh FID-G more heavily.

### Trivial
*None beyond the above.*

---

## Nice-to-Haves

- A quantitative mask IoU trajectory across IMD steps (iteration 1 → T) against ground-truth complete masks would be the most direct evidence for the mask-denoising claim. Figure 5 shows visual improvement, but reporting "mask IoU converges toward GT complete mask" as a number across iterations would make the core mechanism airtight.
- A single-shot baseline (CompNet with partial mask, no iteration, no IMD) compared against T=1,3,5 IMD steps would isolate IMD's incremental contribution; currently T=1 already includes the full mask-voting machinery.
- Surfacing the "no complete object annotation" setting (Table more ablation, c: FID 19.4) more prominently in the abstract or introduction would strengthen practical significance — it directly speaks to in-the-wild deployment.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: Missing related work on amodal/object completion literature** — Removed per hard rule (cannot verify existence of specific papers; do not mention missing related works).
- **Harsh critic: "Structural problem, not patchable with more experiments"** — Retained as a Major weakness but demoted from "structural/fatal" framing since the paper does include an amodal baseline (Table d), partially mitigating this concern. The amodal baseline is still not ideal (ControlNet not fine-tuned), so the concern remains Major, not Fatal.
- **Strength finder: "Quantitative superiority over strong baselines"** — Removed as stated. ControlNet, Kandinsky 2.1, and Stable Diffusion variants are not "strong" baselines for this task; they are generic models without task-specific adaptation. This strength conflicts with the verified Major weakness about baseline selection.

---

## Novel Insights

The Gibbs-sampling interpretation of alternating generation and segmentation stages as joint distribution sampling over (image, mask) pairs is a suggestive theoretical framing. Even if the formal convergence is not guaranteed, viewing mask voting as approximating $p(M|I)$ and CompNet generation as approximating $p(I|M)$ gives a principled vocabulary for understanding why iterative refinement helps and when it should converge. The empirical evidence that mask errors are not propagated (Table robust), and that even 15% area noise still converges to near-optimal FID in 9 iterations, is consistent with this interpretation and constitutes a non-obvious finding about the robustness of the iterative denoising loop.

---

## Suggestions

1. **Add a task-specific fine-tuned baseline**: Train ControlNet or an equivalent on the same AHP/OpenImage data with identical hyperparameters, then run it through one forward pass (no IMD). This directly isolates whether IMD adds value beyond supervised training.
2. **Report mask IoU per IMD step**: Compute IoU against ground-truth complete masks at T=1, 3, 5, 7 to provide quantitative evidence of mask convergence.
3. **Specify user study methodology**: Report participant count, number of evaluated images per method, and a significance test (e.g., Wilcoxon signed-rank) for the Best and Rank statistics.
4. **Clarify per-completion inference cost**: Explicitly state total wall-clock time for T=5, N=5 (not per-step time) and provide the fast mode as the default reported number.
5. **Ablate threshold τ**: Test τ ∈ {0.4, 0.5, 0.6} on AHP to show robustness (or identify the optimal setting).

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Human Score | Round | Comparison |
|------|----------------|-------|-----------|
| RFJGFrMvYj.md (TCIG two-stage controlled generation) | 1.50 | R1 | Far weaker — minimal contribution, no novel mechanism |
| MqvQUP7ZuZ.md (DC3DO) | 3.00 | R1 | Weaker — straightforward adaptation with limited novelty |
| dAavOuxZvo.md (VIPaint inpainting w/ diffusion) | 3.00 | R1 | Weaker — methodologically less complete |
| 4w99NAikOE.md (IterComp iterative feedback) | 6.80 | R1 | Stronger — has theoretical proofs, more task-relevant baselines |
| a7gOjgFswH.md (G4Seg generation+segmentation loop) | 5.40 | R1/R2 | Similar profile — iterative gen+seg, rejected |
| YqyTXmF8Y2.md (EmerDiff semantic knowledge in diffusion) | 6.00 | R1/R2 | Stronger — cleaner evaluation and broader baselines |
| JT53iXH7eO.md (Diffree object inpainting w/ SD) | 4.75 | R2 | Similar — fine-tuned vs. generic baselines problem, similar scope |
| h7fZvaU93L.md (Video inpainting w/ conditional diffusion) | 5.50 | R2 | Roughly comparable scope and rigor |
| DuyuAHBk1t.md (AIR zero-shot adaptation iterative refinement) | 5.50 | R2 | Comparable — iterative refinement paper, borderline |

**Round 1 bracket:** 4.5–6.0.

**Round 2 narrowing:** MaskComp sits closer to G4Seg (5.4, Reject) and Diffree (4.75, Reject) than to EmerDiff (6.0, Accept). Like Diffree, MaskComp compares a trained task-specific model against zero-shot generic models. Like G4Seg, it pairs generation and segmentation iteratively. MaskComp has more thorough ablations than either, and its IMD mechanism is more principled than G4Seg's discrepancy-based refinement. The amodal baseline (Table d) partially differentiates it. On balance, MaskComp is between the 4.75 and 5.4 anchors, with the more complete ablation suite pulling it slightly above G4Seg.

**Originality:** Moderate-high. The IMD framing and Gibbs-sampling analogy are novel for object completion.  
**Research question importance:** Moderate. Object completion from occlusion is a real problem, though the paper doesn't situate it strongly within the completion literature.  
**Claim support:** Moderate. Claims are directionally supported by ablations, but the main comparison is against weak baselines.  
**Experimental soundness:** Moderate. Ablations are sound; main comparison is not.  
**Clarity:** Good. The method is clearly described and the IMD process is well illustrated.  
**Value to community:** Moderate. The iterative generation–segmentation loop could generalize to other tasks, but the paper doesn't develop this.

**Final score: 5.0 — Reject (borderline)**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>