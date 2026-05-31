Now let me run calibration search to bracket the paper's score before writing the review.Now let me read one more anchor to finalize my calibration:Now I have enough data to write the final consolidated review. Let me compile my findings.

---

## Summary

ARSS introduces the first GPT-style decoder-only autoregressive transformer for novel view synthesis (NVS) from a single image, conditioned on a predefined camera trajectory. The method combines VidTok (a causal video tokenizer with FSQ) for temporally consistent visual token sequences, a geometry-constrained camera autoencoder that converts Plücker raymaps into 3D positional guidance tokens, and a hybrid token permutation strategy that randomly shuffles tokens within each frame while preserving inter-frame temporal order. Training and evaluation are performed on RealEstate10K, ACID, and DL3DV at 256×256 resolution.

---

## Strengths

- **Best LPIPS across all three benchmarks.** From Table 1: ARSS achieves 0.269 vs. 0.314 (LVSM) and 0.349 (SEVA) on Re10K; 0.265 vs. 0.308 (LVSM) and 0.326 (SEVA) on ACID; 0.347 vs. 0.400 (LVSM) on DL3DV. This is a consistent perceptual quality advantage across in-distribution and zero-shot settings.

- **Best FVD on Re10K and DL3DV.** From Table 1: 50.51 vs. 56.31 (LVSM) and 57.56 (SEVA) on Re10K; 91.25 vs. 96.83 (LVSM) on DL3DV. This supports the claim that the causal AR design and temporal tokenizer yield better sequence-level temporal consistency.

- **Hybrid spatial permutation ablation is clean and well-supported.** Table 2 shows a clear and monotonic improvement: raster (16.29 PSNR, 71.17 FID) → full spatial+temporal permutation (18.76, 62.58) → spatial-only permutation (19.22, 60.11). The design choice is well-motivated and quantitatively validated.

- **Video tokenizer substantially outperforms per-frame VQ tokenization.** Table 3 shows FVD dropping from 137.68 (VQ image tokenizer) to 52.56 (VidTok, FSQ), a ~62% improvement, along with PSNR gains (15.69→19.22) and LPIPS gains (0.498→0.294), demonstrating that temporal compression in the tokenizer is critical for multi-view consistency.

---

## Weaknesses

### Fatal
None.

### Major

- **SEVA is absent from the error accumulation analysis (Figure 6).** The paper's strongest claim about long-horizon behavior—"our method maintains consistently highest or near-highest PSNR/SSIM while exhibiting the lowest LPIPS at every timestep" (Section 4.2)—is made against LVSM, MotionCtrl, RayZer, and ViewCrafter. But SEVA is the only competitor that performs comparably in Table 1 (winning SSIM and FID on Re10K; winning SSIM, FID, and FVD on ACID). The comparison in Figure 6 is assembled entirely from methods ARSS beats decisively in Table 1. As a result, the per-frame trajectory analysis—which is potentially ARSS's most distinctive experimental contribution—does not demonstrate superiority over the method that actually matters. No justification is given for SEVA's exclusion from this figure.

- **The paper's primary motivation for the AR paradigm is not experimentally tested.** The introduction argues that AR models are advantageous because they "can incrementally extend and reuse existing generations when the trajectory changes" and operate "in a sequential and causal manner" (Section 1). These are specific, testable claims, distinct from general reconstruction quality. The experiments measure PSNR, SSIM, LPIPS, FID, and FVD—the same reconstruction metrics used by diffusion-based baselines. No experiment demonstrates trajectory extension beyond training length, incremental generation when the path changes mid-sequence, or any scenario where the causal property yields a qualitative advantage that a joint diffusion baseline cannot match. The paper ends up arguing for AR models on grounds it does not verify, then evaluates on metrics that are agnostic to those grounds.

### Minor

- **The tokenizer ablation (Table 3) conflates two independent variables.** The VQ vs. VidTok comparison simultaneously changes (a) the tokenizer architecture (image/spatial vs. video/spatiotemporal) and (b) the quantization scheme (VQ vs. FSQ). FSQ is known to improve training stability and reconstruction quality independently of temporal modeling. The paper attributes the full improvement to temporal consistency, but without a VQ-based video tokenizer as an intermediate condition, the contribution of temporal architecture alone cannot be isolated.

- **Ablation tables do not specify the evaluation dataset.** Tables 2 and 3 do not state whether results are on Re10K, ACID, a validation subset, or some combination. This makes the ablation numbers difficult to interpret relative to Table 1 and limits reproducibility of the design-choice analysis.

- **The 256×256 resolution constraint is underanalyzed.** Section 5 briefly acknowledges that ARSS is "trained from scratch using limited public datasets with relatively low resolution," but does not analyze how much of the SSIM and FID deficit relative to SEVA (e.g., ACID FID: 47.76 for ARSS vs. 33.16 for SEVA) is attributable to resolution rather than method. For the reader to evaluate the comparison fairly, some discussion of the resolution effect is needed.

### Trivial
None.

---

## Nice-to-Haves

- **Design an experiment that specifically tests the sequential, causal advantage of AR.** For instance: evaluate whether ARSS can extend a trajectory beyond the training horizon by iteratively conditioning on previously generated frames, and compare this to a diffusion model that must regenerate all frames jointly when the trajectory is extended. This would make the AR framing earn its stated motivation rather than serving only as a design choice that happens to produce competitive reconstruction metrics.

- **Include SEVA in Figure 6.** If ARSS degrades more slowly than SEVA on long trajectories, this is a compelling finding that would differentiate ARSS from its strongest competitor in a meaningful way. If not, reporting this honestly would still be informative.

- **Report inference time.** Given that the paper emphasizes training from scratch without heavy computational resources (Section 5), a brief comparison of inference cost versus SEVA would help readers calibrate the efficiency claim.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Exclusion of SEVA from DL3DV is unfair"**: The paper explicitly notes in Table 1's caption that "For SEVA, ViewCrafter, and RayZer results on DL3DV are not reported, since DL3DV was part of its training data." This is transparent and appropriate, not an omission. **Removed** because the paper addresses this directly.

- **"Comparison with SEVA is unfair because SEVA uses pre-trained models"**: Per the hard rule, if the asymmetry (SEVA uses large pre-training; ARSS does not) favors the baseline, the criticism should be removed. ARSS achieving competitive results against a much better-resourced baseline is actually evidence for the method, not against it. **Removed.**

- **Equation 7 truncation (missing right-hand argument to CE)**: Likely a parser artifact in text extraction. Equation 3 presents the full loss form, and the surrounding paragraph describes the full objective. **Removed** per the rule on parser/formatting artifacts.

- **Equation 5 notation error (d vs. m)**: The body text states "**d** is the normalized camera ray direction, **d** is the momentum term," where the second **d** should be **m**. However, the momentum is correctly defined as **m** = **o** × **d** in the same sentence. This appears to be a rendering artifact from the PDF parser, not a paper error. **Removed** per the rule on formatting artifacts.

- **"Claim that AR is the first to achieve NVS cannot be verified"**: The paper claims to be "the first that applies the GPT-style causal autoregressive model in novel view generation with camera control" (Section 1). This is a narrowly scoped novelty claim (GPT-style discrete AR, not AR diffusion or flow-based methods). **Removed** per the rule against questioning existence of cited claims without external verification.

- **Generic strength about "important problem"**: Removed from strengths per filtering discipline.

---

## Novel Insights

The most genuinely novel observation in this paper—supported by Table 2—is that preserving temporal order while randomizing spatial order within frames is strictly necessary for quality autoregressive NVS: both full temporal randomization and raster spatial ordering produce substantially worse results, and the hybrid wins across all four metrics. This validates that multi-view generation has an asymmetry that single-image AR methods do not face: spatial context within a frame is bidirectional, but the cross-frame causal dependency is strictly directed. The camera token, which provides 3D positional instruction at the per-token level, is what makes spatial randomization safe without losing positional context. This design pattern—temporal order preserved, spatial order randomized, 3D position encoded per-token—may generalize to other sequential visual tasks beyond NVS.

---

## Suggestions

1. Add SEVA to Figure 6. Re-run the per-frame PSNR/SSIM/LPIPS curves including SEVA and report honest results. If ARSS degrades more slowly, report it prominently; this would be the paper's most compelling result.
2. Add one targeted experiment demonstrating the claimed causal/sequential advantage over diffusion models—e.g., trajectory extension or on-the-fly trajectory adaptation—to validate the core motivation of the AR approach.
3. Report FID and FVD alongside PSNR/SSIM in the ablations and specify the evaluation dataset for Tables 2 and 3.
4. Add a brief analysis of resolution impact on metrics, even if only qualitative, to help readers calibrate the SSIM/FID gap vs. SEVA.

---

## Score and Decision

**Calibration summary:**

**Round 1 anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| CCM-DiT (15lk4nBXYb) | 3.00 | 1 (low) | Camera-controlled video diffusion via LoRA; clearly weaker scope and contribution than ARSS |
| ARVideo (hWlCc7Iksi) | 3.40 | 1 (low) | AR self-supervised video representation; rejected, no direct NVS connection |
| AR-1-to-3 (pOcGFvfgjS) | 5.00 | 1 (mid) | Most topically similar: AR from single image to 3D object views; weaker evaluation (1 synthetic dataset, less ablation) |
| Training-free Camera Control (KI1zldOFz9) | 5.80 | 1 (mid) | Training-free camera control for video diffusion; more elegant but different paradigm |
| ControlAR (BWuBDdXVnH) | 6.25 | 1 (mid) | Controllable image generation for AR models; strong results vs. ControlNet++; better-supported claims |
| Where Am I (NuHYh4YKNe) | 6.25 | 1 (mid) | AR for joint pose estimation + view prediction; controversial novelty claims; accepted despite disputes |
| LVSM (QQBPWtvtcn) | 7.67 | 1 (high) | Large view synthesis model; ARSS's baseline; much stronger scope and evaluation |

**Round 1 bracket: 4.5–6.0**

**Round 2 anchors:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| 3D-free NVS (VLuJL8cnGk) | 5.00 | 2 | NVS from single image combining 3D-free and 3D-based approaches; rejected, mixed scores; ARSS has stronger ablations |
| Zero-shot NVS via video diffusion (zDJf7fvdid) | 6.00 | 2 | Training-free NVS via video diffusion; accepted; more theoretically grounded; ARSS is more empirically robust but weaker on motivation-evaluation coherence |
| CameraCtrl (Z4evOUYrk7) | 6.50 | 2 | Camera control for text-to-video; accepted; comprehensive evaluation; ARSS compares unfavorably in coverage of baselines |
| Bridging AR and Masked (KUz8QXAgFV) | 5.50 | 2 | AR-masked hybrid for visual representation; rejected; moderate novelty; ARSS is slightly stronger in domain specificity |

**Round 2 narrowing:** ARSS sits clearly above AR-1-to-3 (5.0, Reject) in experimental rigor and domain relevance, but below Zero-shot NVS (6.0, Accept) due to the motivation-evaluation coherence gap and SEVA's absence from Figure 6. It is further below CameraCtrl (6.5, Accept), which has tighter claim-to-experiment alignment. The paper is a genuine first step in applying GPT-style AR to scene NVS and achieves competitive results, but the core stated advantage of the AR paradigm is unvalidated, and the most important per-frame comparison (vs. SEVA) is missing. This positions ARSS closer to the 5.0 anchor than the 6.0 anchor.

**Final score: 5.0 — Reject**

The paper opens a legitimate research direction but falls short of acceptance in its current form due to: (1) the motivation-to-experiment coherence gap (the stated advantage of causal AR is never tested), and (2) the absence of SEVA from the per-frame analysis that is the paper's strongest unique experimental contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>