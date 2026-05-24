Now I have a solid understanding of the paper and the calibration landscape. Let me write the final consolidated review.

**My round-1 bracket:** Based on the initial calibration, this paper sits between the weak anchors (avg 1.5-3.0) and the strong anchors (avg 8.0-9.0), clearly in the middle band (3.5-7.5). The most topically similar anchors in this band are SegGen (6.0), SlotAdapt (6.25), Image Inpainting via Iteratively Decoupled (6.25), Paint by Inpaint (4.0), MoveAnything (4.5), and PAIR Diffusion (~4.8).

**Narrowing:** Comparing against these, the current paper has more extensive ablation studies than Paint by Inpaint or MoveAnything, but its evaluation methodology has more significant fairness issues than any of the 6.0+ anchors (SegGen, SlotAdapt, Image Inpainting). The unfair baseline comparison and the ambiguous "resplit from training set" evaluation on AHP are structural concerns that the 6.0+ anchors do not share. This places the paper below those. It is comparable to PAIR Diffusion (~4.8) and MoveAnything (4.5) in terms of the severity of its evaluation gaps.

**Final score:** 4.5 — below the acceptance threshold, with interesting ideas undermined by insufficiently rigorous evaluation.

---

## Summary

This paper proposes MaskComp, an iterative framework for visual object completion that alternates between a mask-conditioned generation stage (a fine-tuned ControlNet variant with time-variant gating) and a segmentation stage (SAM with majority voting). The key insight is that providing a more complete object mask as a generation condition leads to better object completion, and the mask can be progressively refined through multiple generation-and-segmentation rounds. Experiments on AHP and DYCE datasets show improved FID scores and user preference over ControlNet, Kandinsky, and Stable Diffusion baselines.

## Strengths

- **Well-motivated iterative refinement loop.** The paper identifies a genuine chicken-and-egg problem — better masks yield better generation, but the mask itself is what needs to be completed — and proposes a natural alternating solution. The ablation in Table 3a (FID improving from 24.7 at 1 IMD step to 16.9 at 5 steps, then 16.1 at 7 steps) directly validates that the iterative process drives improvement, independent of any baseline comparison.

- **Empirical confirmation that mask condition quality matters.** Table 2a shows FID-G of 16.9 with visible masks, 15.3 with noisy masks, and 12.7 with complete masks, all conditioned on the same partial object. This supports the paper's core observation (Section 1, Figure 2) and motivates why iterative mask refinement is worth pursuing.

- **Thorough ablation of design choices.** The paper separately ablates segmentation model choice (Table 4a: SAM yields 16.9 vs 22.5 for Mask2Former), voting strategy (Table 4b), occlusion type (Table 4d), number of IMD steps (Table 3a), number of sampled images (Table 3b), diffusion iterations (Table 3c), and time-variant gating (Table 3d: gating improves FID from 18.2 to 16.9). This level of dissection provides concrete evidence that the implementation decisions are well-motivated.

- **Honest failure case analysis.** Section 4.2 discusses how SAM filters extra limbs and mask voting suppresses errors, and acknowledges that robustness depends on SAM's ability to reject implausible outputs. This candor is valuable for understanding the method's limitations.

## Weaknesses

### Major

1. **Unfair baseline comparison.** The paper fine-tunes its Mask-denoising ControlNet on AHP + OpenImage (50/36 epochs respectively), while all baselines (ControlNet, Kandinsky, SD 1.5, SD 2.1) are evaluated with their publicly released pretrained weights and no domain-specific fine-tuning. The large FID gaps on AHP (e.g., ControlNet 40.2 vs MaskComp 16.9) likely reflect a combination of domain adaptation and the proposed iterative framework, conflating two separate advantages. A proper evaluation should at minimum fine-tune one of the baselines (e.g., ControlNet) on the same AHP training split to isolate the benefit of the iterative refinement loop. The amodal baseline in Table 4c (AISFormer+ControlNet, FID 29.4 vs MaskComp 16.9) partially mitigates this concern because it also uses a mask prediction pipeline with ControlNet, but AISFormer was not fine-tuned on AHP either.

2. **Ambiguous evaluation protocol for AHP.** The paper states "As the original test split is too small [56 images], we resplit 10,000 images from the training set for evaluation." This is the primary quantitative benchmark, and the paper also trains MaskComp on AHP. It is not explicitly stated whether these 10,000 images were held out from training or are simply drawn from the same pool used for training. The word "resplit" could mean a proper train/test partition, but the lack of a clear statement that these images were excluded from training is a significant omission that undermines confidence in the AHP results. The DYCE results are cleaner — DYCE has a separate held-out test set of 27,617 objects, and MaskComp was not trained on DYCE — so the DYCE numbers (FID-G 20.0 vs SD 2.1 at 30.0) are more trustworthy, but the paper's headline claims rest on AHP.

3. **Compute disparity not controlled.** MaskComp uses 5 IMD steps × 5 generated images per step = 25 diffusion passes (plus SAM segmentation per pass) per test example, while each baseline runs a single diffusion pass. The paper acknowledges the 15.5-second inference time per step but does not compare against a multi-sample baseline (e.g., generating 25 images with SD2.1 and selecting the best by some heuristic). While iterative refinement is the method's design, the comparison conflates the benefit of additional sampling with the benefit of the iterative framework.

### Minor

4. **FID-G and FID-S metrics may favor the method.** The paper computes FID-G within ground-truth object regions and FID-S within SAM-segmented foreground regions. Since MaskComp uses SAM internally for segmentation, its outputs may be systematically more aligned with SAM's segmentation boundaries than baselines' outputs, which could be penalized by SAM's mis-segmentations. A cleaner evaluation would use a held-out segmentation model not involved in the pipeline, or report unsegmented FID as a supplementary metric.

5. **User study lacks critical details.** The paper reports that "the participants are required to rank the generated object from different methods based on their completeness and quality" but provides no information about the number of participants, their expertise, whether images were shown paired or in random order, or inter-rater agreement. Without these details, the user study results (53% and 63% "Best" for MaskComp) cannot be independently assessed.

6. **Theoretical framing as Gibbs sampling is loose.** Section 3.3 describes the alternating procedure as "MCMC-like" and "more specifically Gibbs sampling-like," but Gibbs sampling requires that the conditional distributions p(I|M) and p(M|I) are compatible with the same joint distribution. Here, p(I|M) is a neural network trained on a specific occlusion distribution, and p(M|I) is SAM trained on completely different data. There is no guarantee that these conditionals correspond to the same joint, and no convergence or detailed-balance analysis is provided. The paper acknowledges this with hedging language, but the framing adds limited rigor.

### Trivial

7. The paper reports "We generated text prompts using BLIP for all experiments" but the inference section says "We give the class label as the text prompt to facilitate the ControlNet to effectively generate objects." These are contradictory — either BLIP is used or class labels are used.

## Nice-to-Haves

- A comparison where ControlNet (or SD) is given the same computational budget — e.g., generating 25 samples and selecting the best by some automatic criterion — would help disentangle the benefit of iterative refinement from the benefit of more sampling.
- A convergence analysis showing that mask change between iterations decreases would strengthen the iterative denoising analogy.
- Training-time details about the occlusion distribution (size, shape, position ranges) would improve reproducibility.

## Removed Points

- **"Object-shaped occlusions give counterintuitive worse FID" (Harsh Critic, Section-by-Section Notes):** The paper already explains in the appendix that "the occlusion with a more complicated object shape will impose more challenges on the proposed model." This is not a weakness — it is expected that more complex occlusion shapes are harder to complete.
- **"No theoretical guarantee that the mask improves monotonically" (Harsh Critic, Method):** The paper does not claim monotonic improvement; it presents empirical evidence (Table 3a) that FID improves with more steps. The failure case analysis explicitly discusses error tolerance. This is a reasonable empirical paper, not a theoretical one.
- **"Missing related works" (various):** Per instructions, I cannot verify the existence of missing citations and do not penalize for this.
- **"Formatting nitpicks":** Removed per instructions — these are parser artifacts, not author errors.
- **Strength Finder generic strengths ("addressed an important problem," "well-written"):** Dropped as generic/superficial without specific evidence.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely re-surfaced the paper's own claims and limitations without adding a genuinely new analytical perspective.

## Suggestions

1. **Fix the baseline comparison.** Either fine-tune ControlNet on the same AHP training data as MaskComp, or evaluate a zero-shot variant of MaskComp that uses the pretrained ControlNet (without the time-variant gating fine-tuning) with the same iterative loop. This would isolate the contribution of the iterative refinement from the contribution of domain-specific fine-tuning.
2. **Clarify the AHP evaluation protocol.** Explicitly state whether the 10,000 evaluation images were held out during training, and if so, describe the split procedure. Better yet, obtain results on the original 56-image test set (even with wide confidence intervals) or use cross-validation.
3. **Report user study details.** Add participant count, instructions, and optionally inter-rater agreement (e.g., Fleiss' kappa) to make the user study verifiable.
4. **Add a compute-controlled experiment.** Show that the iterative refinement, not just additional sampling, is what drives improvement by comparing against a ControlNet baseline that also generates multiple images and applies post-hoc selection.

## Score and Decision

**Calibration anchors used:**

| Paper (path) | Avg Score | Round | Comparison |
|---|---|---|---|
| RFJGFrMvYj (TCIG) | 1.50 | R1 bracketing | Much weaker — limited experiments, no compelling results |
| L1BXvqwsMv (Specializing SAM) | 2.50 | R1 bracketing | Weaker — narrow adaptation problem, limited scope |
| hkWHdI8ss5 (SITTO) | 2.33 | R1 bracketing | Weaker — less thorough evaluation |
| 2HdZPEQUig (Efficient Object-Centric) | 3.00 | R1 bracketing | Weaker — limited experimental validation |
| **J9Vwp7TiE5 (SegGen)** | **6.00** | **R1 middle / R2** | **More rigorous evaluation but novelty concerns; this paper has comparable experimentation but more fundamental evaluation fairness issues** |
| **bVBLqKoiJ1 (Paint by Inpaint)** | **4.00** | **R1 middle / R2** | **Similar level of evaluation gaps; this paper has stronger ablations but similar baseline fairness issues** |
| **rUf9G9k2im (Image Inpainting via Iteratively Decoupled)** | **6.25** | **R1 middle / R2** | **Stronger evaluation, accepted as spotlight; this paper's evaluation fairness issues are more severe** |
| **kZvor5aaz7 (SlotAdapt)** | **6.25** | **R1 middle / R2** | **More thorough, accepted as poster; this paper has weaker evaluation methodology** |
| IRcv4yFX6z (Hierarchical Image Segmentation) | 8.00 | R1 strong | Much stronger — rigorous evaluation, clear contribution |
| 3M0GXoUEzP (CrIBo) | 8.00 | R1 strong | Much stronger — thorough analysis |
| UyNXMqnN3c (DreamGaussian) | 8.50 | R1 strong | Much stronger — impressive results, oral acceptance |
| Ha6RTeWMd0 (SAM 2) | 9.00 | R1 strong | Foundation model work of much broader scope |
| Pq2yEKXOl7 (SlotSAM) | 4.50 | R2 narrowing | Similar level — mixed evaluation quality, rejected |
| tCYdsuQgZZ (Test-time Contrastive Concepts) | 5.67 | R2 narrowing | Stronger evaluation methodology |
| jvoK9rUl7W (MoveAnything) | 4.50 | R2 narrowing | Similar level — interesting idea with evaluation gaps |
| cI5j8tEPNU (PAIR Diffusion) | 4.80 | R2 narrowing | Similar level — ControlNet variant with evaluation gaps, rejected/withdrawn |
| bFMpmb8p3D (Multitask I2I Diffusion) | 4.75 | R2 narrowing | Similar level — multitask approach with evaluation limitations |

**Round 1 bracket:** 3.5–6.5 (middle band based on topical similarity)
**Round 2 narrowing:** 4.0–5.5 (comparable to Paint by Inpaint at 4.0, MoveAnything at 4.5, PAIR Diffusion at 4.8; weaker than SegGen at 6.0, SlotAdapt at 6.25)
**Final position:** Closer to the 4.5–4.8 anchors than to the 6.0+ anchors, because the evaluation fairness issues (unfair baseline comparison, ambiguous training-set evaluation) are real and structural.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>