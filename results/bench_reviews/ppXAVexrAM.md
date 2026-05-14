Now I have sufficient calibration data. Let me synthesize everything into the final review.

---

## Summary

ARSS proposes the first decoder-only autoregressive (GPT-style) transformer for scene-level novel view synthesis from a single image, conditioned on a predefined camera trajectory. The framework combines three components: a causal video tokenizer (VidTok with FSQ) for temporally coherent latent tokens, a camera autoencoder that compresses Plücker raymaps into 3D positional guidance tokens, and a hybrid token permutation strategy that randomly shuffles spatial token order within each frame while preserving temporal causality across frames. The paper evaluates on RealEstate10K, ACID, and DL3DV, and provides ablations isolating each design choice.

## Strengths

- **First decoder-only AR paradigm for scene NVS with camera control**: The paper is genuinely the first to apply a GPT-style causal transformer to scene-level novel view synthesis from a single image, with explicit camera trajectory conditioning. This opens a new direction distinct from the dominant diffusion-based approaches (Section 3, confirmed throughout the method section).

- **Effective and well-ablated hybrid token permutation**: The proposed ordering (random spatial shuffle within frames, temporal order preserved) yields a +2.93 dB PSNR gain over raster order (Table 2: 19.22 vs 16.29) and substantially better qualitative fidelity than both raster and full-permutation schemes (Figure 7). The ablation cleanly isolates this contribution.

- **Video tokenizer dramatically improves temporal consistency**: Replacing per-frame VQ with VidTok reduces FVD by 62% (137.68 → 52.56, Table 3), while also improving PSNR, SSIM, and LPIPS. This is a clear, well-motivated design choice supported by evidence.

- **Superior long-trajectory stability**: The per-frame error accumulation analysis (Figure 6) shows ARSS maintains higher PSNR/SSIM and lower LPIPS at every frame index, with flatter degradation slopes than baselines — indicating slower error accumulation over 17-frame trajectories.

- **Convincing zero-shot generalization**: On the unseen DL3DV benchmark, ARSS produces geometrically consistent views (Figure 4, Table 1) and generalizes to out-of-distribution AI-generated images (Figure 5), demonstrating robustness beyond the training distribution.

## Weaknesses

### Fatal

None.

### Major

- **SOTA claims are overstated relative to absolute performance**: The paper claims the method "outperforms current state-of-the-art methods" (Section 1, Section 5), but the absolute PSNR of 19.22 dB on RealEstate10K (Table 2) is modest even for the challenging 17-frame trajectory task. The paper's own Discussion (Section 5) acknowledges that quality is limited by the tokenizer and that training is from scratch on limited data — a concession that sits in tension with the SOTA framing. The abstract uses more measured language ("overall comparable to state-of-the-art"), suggesting the authors recognize this, but the stronger claims in the introduction and conclusion should be tempered to match the evidence. This is a presentation issue that, if left uncorrected, undermines credibility, but it does not invalidate the paper's genuine methodological contribution.

- **Causal accumulation advantage is motivated but never empirically validated**: The introduction motivates AR models by their ability to "incrementally extend and reuse existing generations when the trajectory changes" (Section 1) — a key claimed advantage over joint diffusion generation. No experiment tests this. The error accumulation analysis (Figure 6) shows ARSS degrades more slowly, but this only demonstrates stability, not the ability to extend a sequence by conditioning on previously generated views. An experiment where the model generates additional frames beyond the training length, or conditions on its own previous outputs, would be needed to substantiate this motivation. Without it, the paper's core argument for preferring AR over diffusion in world-modeling scenarios remains a promissory note.

### Minor

- **No ablation of the camera autoencoder against simpler alternatives**: The camera autoencoder (Section 3.2.2) compresses Plücker raymaps into latent tokens with a dedicated geometry-aware loss (Eq. 5). No experiment compares this design to a simpler baseline (e.g., projecting Plücker coordinates through a shallow MLP to the same latent dimension). The contribution of the geometry-consistency loss terms to final view synthesis quality is therefore unverified. This does not threaten the core contribution, but it leaves one component untested.

- **Baseline adaptation protocol is insufficiently described**: The paper evaluates methods like MotionCtrl, ViewCrafter, and Genwarp — which were not originally designed for single-image, 17-frame trajectory NVS — without describing how they were adapted to this protocol (e.g., how frames were allocated, whether their native resolution or frame counts were adjusted). Several baseline numbers are low (e.g., ViewCrafter at 12.67 PSNR, RayZer at 12.97), and while this may reflect genuine difficulty of the task rather than misconfiguration, the lack of detail prevents readers from assessing the fairness of the comparison.

- **Missing comparison to strongest single-image NVS methods**: The paper does not compare against recent methods known to achieve strong results on RealEstate10K for single-image NVS (e.g., geometry-conditioned diffusion models in the 25+ dB range for single-target-view settings). While the 17-frame trajectory task is harder than single-view prediction, comparing against these methods — even if only on a per-frame basis — would better contextualize ARSS's performance. The paper acknowledges in Section 5 that its method is trained from scratch without large-scale pretraining, which partly explains the gap, but the omission of stronger baselines makes it harder to assess where the method actually stands.

### Trivial

- The SOTA claim varies in strength across sections (abstract: "comparable to"; introduction/conclusion: "outperforms"). The language should be unified to match the evidence.

## Nice-to-Haves

- Pretraining the AR transformer on large-scale video data before fine-tuning on RE10K/ACID would likely close the gap with diffusion methods that benefit from massive pretrained checkpoints. The paper notes this as a limitation and future direction; providing even preliminary evidence would strengthen the argument for the AR paradigm.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic claim: "Unfair comparison and false claim of state-of-the-art performance — baselines are misconfigured... the entire experimental foundation collapses."** → **Downgraded to Major weakness about overstated claims and Minor about baseline description.** The critic asserts ViewCrafter "typically" achieves 26+ dB PSNR on RE10K for "the same task," but the paper's task (single image → 17 frames) is substantially harder than the single-target-view evaluation those published numbers refer to. The low baseline numbers may genuinely reflect adaptation difficulty rather than misconfiguration. The claim of fraudulent or fundamentally broken evaluation is not supported. However, the paper should better describe baseline adaptation and temper its SOTA language.

- **Harsh Critic claim: "The paper omits a large body of directly relevant work... single-view NeRF variants, geometry-conditioned diffusion models that achieve PSNRs around 28 dB on RE10K."** → **Removed.** Per instructions, missing related work critiques are excluded since I cannot independently verify their existence or relevance to this specific 17-frame task.

- **Harsh Critic claim about Figure 6: "per-frame error accumulation analysis only shows quality degrades more slowly than in some (misconfigured) baselines."** → **Downgraded.** The claim of misconfiguration is speculative. The error accumulation analysis is one of the paper's strengths — it provides per-frame metrics showing flatter degradation. The critique conflates a real concern (motivation not validated) with an unsupported accusation.

- **Strength Finder claim: "State-of-the-art quantitative results on multiple datasets (Table 1)."** → **Removed.** The absolute numbers are modest and the paper's own text (Section 5) acknowledges limitations. This strength conflicts with the verified weakness about overclaiming.

- **Harsh Critic claim about "garbled table" and "missing rows."** → **Removed.** This is a PDF parser artifact. The original submission's Table 1 is presumably complete. Per instructions, formatting artifacts are parser issues.

- **Harsh Critic claim: "The paper mentions that quality is limited by the tokenizer... This admission effectively concedes that the method is not state-of-the-art, creating a contradiction."** → **Removed as a separate weakness.** Acknowledging limitations is good scientific practice, not a contradiction. However, the tension with the SOTA claim is captured in the Major weakness above.

## Novel Insights

None beyond the paper's own contributions. The reviewing process did not surface novel observations that the paper itself does not already discuss (its limitations are self-acknowledged, and its strengths are evident from the experimental results).

## Suggestions

- **Temper the SOTA language.** Replace "outperforms current state-of-the-art methods" with "achieves competitive performance" or "outperforms the evaluated baselines on this specific task." The abstract already uses better language; unify throughout.
- **Add an incremental extension experiment.** Generate, say, frames 1–8, then condition on those outputs to generate frames 9–16, and compare against a baseline that generates all 16 at once. This would directly test the causal accumulation motivation.
- **Describe baseline adaptation.** For each baseline, specify: what resolution, how many frames were generated, how the single input image was provided, and whether any method-specific adjustments were made.
- **Ablate the camera autoencoder.** Compare against an MLP baseline that maps Plücker coordinates to the same latent dimension, with and without the geometry-consistency loss.

## Score and Decision

**Anchor comparisons:**

| Path | Paper | Avg Score | Decision | Comparison to ARSS |
|------|-------|-----------|----------|---------------------|
| `PZQHihJlfm` | ArchonView (AR for object NVS) | 5.00 | Reject | Most similar: also first AR for NVS. ARSS is stronger — handles scene-level multi-view sequences, has better ablations (token permutation, video tokenizer), and includes error accumulation + zero-shot generalization. ArchonView has scaling analysis and more benchmarks. |
| `pIyADlhQsp` | CausNVS (AR diffusion for NVS) | 3.50 | Reject | CausNVS was rejected for limited novelty (integration of existing techniques) and insufficient long-sequence evaluation. ARSS has clearly stronger novelty and experimental depth. |
| `NnSiKYA1Jk` | Pensieve (self-supervised NVS) | 5.50 | Reject | Comparable score band. Pensieve had stronger absolute results but evaluation was questioned for test-time optimization. ARSS has cleaner evaluation but more modest metrics. |
| `O66RinTZTR` | ReNoV (feature-warping NVS) | 3.50 | Reject | Significantly weaker than ARSS — missing baselines, incomplete training details, limited scalability. |
| `rJdGst0W8s` | ARPG (random-order AR image gen) | 6.50 | Accept (Poster) | Stronger than ARSS. ARPG has more thorough experiments on established benchmarks, clearer efficiency gains, and zero-shot task generalization. ARSS is in a harder domain (NVS vs. image generation) but the experimental validation is less complete. |
| `kI27Niy4xY` | VIST3A (text-to-3D stitching) | 8.00 | Accept (Oral) | Much stronger than ARSS. VIST3A has a clear, high-impact contribution with SOTA results and thorough validation. |

ARSS sits between ArchonView (5.00) and ARPG (6.50). It has stronger novelty and experimental depth than ArchonView but less thorough validation than ARPG. The paper makes a genuinely novel contribution — first decoder-only AR for scene NVS — with well-ablated components and reasonable results. However, the SOTA overclaiming, missing causal-accumulation validation, and modest absolute metrics prevent a clear accept recommendation. The score reflects a borderline paper that could become a solid poster with the suggested improvements.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>