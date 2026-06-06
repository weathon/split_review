Now I have a thorough understanding of the paper. Let me draft the review before calling calibration.Now I'll run Round 1 calibration bracketing.Let me read the most topically relevant anchors for better calibration.**Round 1 bracket: 5.0 – 6.5**. XTalker clearly beats weak 3.0 rejects, is roughly comparable to CaFe-Talk (6.0) but with noted evaluation framing problems, and falls below Loopy (8.0) which is a stronger, cleaner contribution. Let me narrow with Round 2.Now I have enough to score confidently. Let me finalize.

**Round 2 comparison:**
- XTalker vs. CaFe-Talk (6.0, accepted): CaFe-Talk achieves SotA lip sync while offering controllability; XTalker achieves real-time performance and best CSIM/LPIPS but has a 40% lip-sync gap vs. Float and evaluation framing issues. Roughly comparable; slight edge to CaFe-Talk.
- XTalker vs. EcoFace (6.5, accepted): EcoFace has more principled theoretical grounding for emotion-speech disentanglement. XTalker below.
- XTalker vs. AniHead (5.33, rejected): XTalker clearly stronger — better ablations, stronger results, more novel architecture.
- XTalker vs. AnyExpress (4.25, rejected): XTalker clearly stronger.

**Final bracket: 5.5 – 6.0.** The input asymmetry issue in Table 1 and the unexplained lip-sync gap keep XTalker from the 6.0 level of CaFe-Talk. I settle at **5.5**.

---

## Summary
XTalker is a flow-matching-based framework for audio-driven talking portrait animation that decomposes facial motion into three interpretable subspaces — lip-phoneme synchronization, emotional expression, and head pose — within the compact LivePortrait parameter space. A unified MM-DiT backbone jointly encodes portrait and audio signals, followed by three lightweight prediction heads conditioned on an audio envelope, emotion labels, and user-defined motion curves. The system achieves real-time performance (28.21 FPS on RTX 4090) while offering fine-grained controllability over facial expression and head motion.

## Strengths
- **Real-time performance, genuinely best in class**: Table 1 confirms 28.21 FPS on RTX 4090 and 33.14 FPS on A100 — more than 2× the next fastest real-time method and >30× faster than pixel-space diffusion baselines. This is an unambiguous, architecture-motivated advantage for interactive and deployment scenarios.
- **Best visual quality metrics**: XTalker achieves the best CSIM (0.9395) and LPIPS (0.0432) among all seven baselines by substantial margins, indicating strong identity preservation and perceptual fidelity.
- **Ablation validates every proposed component**: Table 2 shows clear degradation when DWA balancing is removed (Sync-C drops 0.7548→0.4809), when envelope conditioning is removed from the talking head (Sync-C 0.6790→0.2716), and when the segment noise initialization is degraded. The multi-head and training strategy contributions are individually supported.
- **Pose controllability quantitatively demonstrated**: Figure 7 shows nearly linear Pose-Variance growth with γ while cosine similarity peaks and stabilizes — providing quantitative, interpretable evidence of robust pose control.
- **Envelope noise initialization improves lip alignment**: Table 2 shows env_init raises Sync-C from 0.3786 to 0.4401 (N_seg=1 setting), confirming a concrete, independently measurable contribution.

## Weaknesses

### Fatal
None.

### Major

- **Input asymmetry in Table 1 for EmoACC and Pose-Variance** — XTalker's best-in-class EmoACC (0.6476) and Pose-Variance (21.2243) are achieved with explicit inputs (emotion label, user-defined motion curve) that none of the seven baselines receive; all baselines are audio-only. The paper presents these as evidence of "superior emotion and motion expressivity" (abstract, Section 4.2, contributions bullet 3) without disclosing this input asymmetry. As written, these numbers measure how well XTalker follows its own control signals — not that it is a more expressive generative model than its competitors. A paper positioning EmoACC and Pose-Variance as competitive results is misleading when the comparison is structurally unequal. This is a presentation/framing failure, not a methodological one, but it affects how the paper's central claims must be interpreted.

- **Lip-sync gap vs. Float is substantive and inadequately explained** — Float achieves Sync-C 1.0579 vs. XTalker's 0.7548 (approximately 40% lower). The paper attributes this to "limited scale of the training set" in Section 4.2 but provides no evidence for this claim — no data-scaling experiment, no ablation showing that more training data improves Sync-C. Since lip-sync accuracy is the foundational criterion for talking portrait animation, claiming "competitive lip-sync performance" while trailing the best baseline by this margin requires either a precise qualification or empirical investigation. If the data-scale hypothesis is correct, demonstrating it would be straightforward and would meaningfully strengthen the paper's position.

### Minor

- **Equation 7 circular notation**: The flow interpolant is written as `z_t^h = (1-tt)*z_0^h + tt*z_t^h`, which is self-referential (the target variable appears on both sides). The intended form is presumably `z_t^h = (1-tt)*z_0^h + tt*z_1^h`. This is a notation error in the manuscript.

- **Inference speed comparison partially conflates model efficiency with renderer efficiency**: Table 1's footnote reveals that XTalker's MM-DiT backbone takes only 0.48 ms per frame (2.2% of total), while the shared LivePortrait warping renderer accounts for 21.95 ms. The reported FPS primarily measures the LivePortrait renderer's speed, not XTalker's generative contribution. Pixel-space diffusion baselines (EchoMimic, Hallo3) are architecturally slower for unrelated reasons. The paper should clarify this distinction.

- **Disentanglement not quantitatively validated across heads**: The paper claims three-subspace "disentanglement" in the title and contributions, but provides no experiment measuring cross-head interference — e.g., whether adjusting emotion head output degrades Sync-C, or whether changing the pose head affects EmoACC. Without this, the disentanglement claim is an assertion rather than a demonstrated property.

- **20 synthetic GPT-5 test images without justification**: 20 of 100 test images are generated by GPT-5 (Section 4.1). No rationale is given. CSIM and LPIPS metrics on synthetic images are less interpretable because the distributional properties and identity specificity of synthetic portraits differ from real images.

### Trivial
- Circular index in Equation 7 (see Minor above; needs to be corrected in manuscript).

## Nice-to-Haves
- A data-scaling experiment (e.g., training XTalker on a larger dataset) to empirically evaluate whether the Sync-C gap vs. Float is data-driven or architectural. This would directly answer the most pressing open question about the method.
- Reframe Table 1 by explicitly labeling EmoACC and Pose-Variance as conditional controllability metrics (requiring control signals) rather than treating them as direct head-to-head comparisons with audio-only baselines. This doesn't weaken the contribution and makes the evaluation honest.
- A cross-head interference experiment (does emotion head modification corrupt Sync-C?) to formally validate the disentanglement claim.
- A user study measuring naturalness and expression fidelity when users specify their own emotion labels and curves, which is the intended use case, would better support the controllability contribution than the current asymmetric metric comparison.
- Clearer description of the LLM's role in the curve-pose synthesis module in the main text (Section 3.3); the current description leaves the LLM's actual function ambiguous.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **EmoACC circularity (removed)**: The harsh critic raised concern that EmoACC evaluation might be circular with the Emotion Expression Transformer's training pipeline. However, EmoACC uses an off-the-shelf external classifier (Muru, 2021) with no stated connection to the paper's supervision pipeline. The circularity claim is speculative; removed.
- **"Lip-envelope correlation is a known property" (removed)**: The harsh critic noted that audio-lip amplitude correlation is not a new observation. While correct in principle, the paper's specific contribution is confirming this in the LivePortrait implicit keypoint space. This is a legitimate new analysis in a specific representation, not just restating a known property.
- **46% angry accuracy is too low (removed)**: The harsh critic implied this needs more scrutiny. At 6-class classification, random chance is ~16.7%, so 46% is clearly and meaningfully above chance. The criticism is invalid.
- **Strength: "Important problem addressed" (removed as generic)**: Dropped as a generic importance-of-problem strength with no concrete paper-specific evidence.
- **LLM vagueness as a major flaw (removed)**: The main text is vague about the LLM's role, but detailed treatment is deferred to Appendix E.1. Per the hard rules about appendix content, this is not a structural flaw.

## Novel Insights
The paper's most practically novel contribution is the use of heterogeneous, automatically-constructable training targets to supervise three separate prediction heads within a single flow-matching backbone: audio envelope as a proxy lip-sync target (requiring no annotation), an Emotion Expression Transformer generating pseudo-labels (requiring only image-level emotion labels), and LLM-generated curve-to-pose mappings (requiring only text prompts). This combination effectively sidesteps the data bottleneck in annotating expression and pose for talking-portrait training. The envelope-driven noise initialization — injecting audio priors into the latent noise before flow-matching inference rather than only at inference time — is a clean and validated design choice for speech-driven generation. The dynamic weight averaging combined with homoscedastic uncertainty for multi-head flow-matching loss is a practically useful contribution to multi-task flow-matching optimization.

## Suggestions
- Correct the circular index in Equation 7 (`z_1^h`, not `z_t^h`, on the right-hand side).
- Reframe EmoACC and Pose-Variance in Table 1 as conditional controllability results: explicitly note in the caption that these metrics require emotion/curve inputs that baselines do not receive.
- Add a brief data-scaling ablation to test whether Sync-C improves on more training data — this is the most impactful single experiment to add.
- Quantify cross-head interference (e.g., EmoACC and Sync-C when only pose head is varied) to formally support the disentanglement claim.

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison to XTalker |
|---|---|---|---|
| `/deepreview_13k_calibration/15lk4nBXYb.md` (CCM-DiT) | 3.0 | R1 | Much weaker — incremental LoRA fine-tuning, no strong results |
| `/deepreview_13k_calibration/pWdkM9NNCA.md` (Fox-TTS) | 3.0 | R1 | Much weaker — TTS paper, limited novelty |
| `/deepreview_13k_calibration/9GNTtaIZh6.md` (Mask-Guided Video) | 3.0 | R1 | Much weaker — limited scope, simple method |
| `/deepreview_13k_calibration/S7cWJkWqOi.md` (CaFe-Talk) | 6.0 | R1+R2 | Very similar scope; CaFe-Talk has symmetric evaluation and SotA lip sync; XTalker has speed advantage but evaluation issues |
| `/deepreview_13k_calibration/vaEPihQsAA.md` (CyberHost) | 4.83 | R1 | Different scope (body animation); XTalker more directly impactful in its domain |
| `/deepreview_13k_calibration/sOmojPmnlL.md` (AnyExpress) | 4.25 | R1 | Rejected audio portrait method; XTalker clearly stronger |
| `/deepreview_13k_calibration/ATEawsFUj4.md` (GAIA) | 6.5 | R1+R2 | Stronger: large dataset contribution, scalable up to 2B; XTalker weaker |
| `/deepreview_13k_calibration/weM4YBicIP.md` (Loopy) | 8.0 | R1 | Much stronger: clean end-to-end, innovative temporal modeling |
| `/deepreview_13k_calibration/GstK7tITrE.md` (AniHead) | 5.33 | R2 | Rejected 3D avatar; XTalker stronger contribution |
| `/deepreview_13k_calibration/QmJoF47DIR.md` (3DGaussian Head) | 5.33 | R2 | Rejected 3D avatar; different domain but similar tier |
| `/deepreview_13k_calibration/oJA1GUqRww.md` (FaceShot) | 6.0 | R2 | Accepted portrait animation; training-free, different approach |
| `/deepreview_13k_calibration/aqlzXgXwWa.md` (Multiple Character) | 5.75 | R2 | Accepted controllable animation; comparable scope |
| `/deepreview_13k_calibration/iDcWYtYUwX.md` (EcoFace) | 6.5 | R2 | Accepted 3D talking face with emotion disentanglement; stronger theoretical grounding |
| `/deepreview_13k_calibration/AumOa10MKG.md` (DisPose) | 6.25 | R2 | Accepted controllable animation; comparable scope and quality |

**Round 1 bracket:** 5.0–6.5  
**Round 2 narrowing:** The closest topical anchors (CaFe-Talk at 6.0, EcoFace at 6.5, DisPose at 6.25) are all just above XTalker's quality due to the evaluation asymmetry issue, lip-sync gap, and comparatively limited training data. The 5.33 rejects are clearly below XTalker. XTalker sits at the bottom of the accepted cluster — comparable to the 5.75–6.0 accepted papers but with the evaluation framing problems pulling it down. The paper has genuine contributions (real-time speed, strong visual quality, clean ablation) but the headline claims are overstated relative to what the evaluation can support.

**Final score: 5.5** — The paper has real practical value and a coherent, well-ablated method, but the evaluation framing (input asymmetry in Table 1, overstated EmoACC/Pose-Variance claims) and unexplained lip-sync gap are substantive issues that require revision before the contribution can be assessed cleanly. This is a borderline-reject that could be revised to acceptance with targeted changes.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>