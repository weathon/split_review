## Summary
This paper investigates four visual encoders (CLIP, DINOv2, MAE, DeiT) as visual branches in MLLMs and finds that shallow CLIP features and DINOv2 features capture fine-grained information beneficial for grounding tasks. Based on these analyses, the authors propose COMM, which fuses multi-level CLIP features with deep DINOv2 features (with an MLP for alignment) and demonstrates strong performance on REC, REG, POPE, VQA, and captioning benchmarks.

## Strengths
- Systematic per-layer probing across four vision pretraining paradigms (CLIP, DINOv2, MAE, DeiT) in the MLLM setting (Sec. 3, Fig. 3, Tab. 7); the finding that shallow CLIP layers favor REC while deeper layers favor POPE/REG is concrete and reproducible.
- The observation that vision-only DINOv2 — when given a 2-layer MLP for alignment — can match or exceed CLIP on fine-grained REC tasks (Table 1: DINOv2 w/ MFM 72.8 vs. CLIP w/ MFM 70.0 avg REC) is a non-obvious finding for the MLLM community.
- COMM achieves strong, consistent gains on REC (e.g., 91.73 on RefCOCO val vs. Qwen-VL-7B-Chat 88.55), REG (+16.5 CIDEr over Shikra on RefCOCOg), POPE, and VQA (Tables 2-5).
- The MFM design (LLN-Layerscale) and the MLP alignment recipe are simple, ablated against several alternatives (Fig. 4), and reported in enough detail to reimplement.

## Weaknesses

### Fatal
None.

### Major
- **Training-regime confound between the analysis and the headline model.** The per-layer/MFM analyses (Sec. 3, Fig. 2-3, Tab. 1) use 9,400 iterations at batch 16 on 4 GPUs, while the final COMM model uses 100K iterations at batch 64 plus a second instruction-tuning stage. The "Shikra*" curve used as the anchor in Fig. 3 is therefore far below the published Shikra. The paper never tests whether the layer-wise orderings (shallow CLIP > deep CLIP for REC; DINOv2 shallow features hurt) survive when each encoder gets a full-scale training budget. The design choices in COMM rest on the under-trained study.
- **Resolution / token-budget confound for the headline comparisons.** COMM is trained at 336×336 (the paper explicitly motivates this choice to "promote fine-grained perception"), while Shikra/Kosmos-2/BLIP-2 baselines are at their native, smaller resolutions, and the architecture concatenates patch tokens from both CLIP and DINOv2 — roughly doubling the visual sequence length at the LLM. No CLIP-only or DINO-only control is trained at 336×336 with matched token budget and the full 100K-step recipe, so the attribution of the gains in Tables 2-5 to *fusion* (rather than resolution + tokens + scale) is not isolated. Within the paper's own evidence (Tab. 1), CLIP w/ MFM and COMM differ by only ~1.5 CIDEr on COCO and ~0.9 on Flickr, while the gaps over prior MLLMs in Tables 2-5 are much larger — suggesting non-fusion factors dominate.
- **Severe MLP-depth instability is dismissed in one sentence (Tab. 6).** Going from 2 → 4 → 8 MLP layers collapses RefCOCO+ test-A from 77.5 → 53.7 → 8.2, and POPE collapses similarly. This 70-point swing from a single hyperparameter is described only as "increasing the number beyond 2 suffers degraded performance." Either the alignment recipe is brittle or there is an optimization pathology; either way, this is not adequately diagnosed for what the authors propose as a core design choice.
- **Numerical inconsistency between Tab. 1 and Tab. 5 for COMM (e.g., COCO CIDEr 127.3 vs. 132.7; the same encoder/method labeled identically).** The paper does not reconcile this. If Tab. 1 reflects the analysis regime (under-trained) while Tab. 5 reflects the full recipe, this should be stated, and the comparison in Tab. 1 then cannot directly support "fusion > single encoder" at the regime that produces the reported SOTA.

### Minor
- The abstract's claim that "DINO surpasses CLIP in fine-grained related perception tasks" is supported by REC only in Tab. 1; on POPE, captioning, MME-PS, OK-VQA, and VQAv2, CLIP w/ MFM is comparable to or beats DINOv2 w/ MFM. The framing is selective.
- The MAE/DeiT comparison in Tab. 7 uses single-layer features without the MLP alignment that DINOv2 is given; the "DeiT supervised training is too strong" verdict is therefore speculative.
- No variance/seeds for any central comparison; many differences in Tab. 1 are within plausible run-to-run noise for ~9.4K-iteration training runs.
- The compute/parameter and visual-token-count cost of adding the DINOv2 branch + per-layer Linear-LN modules is not quantified relative to baselines.

### Trivial
- "First to extensively investigate" overclaims a bit; "first within the MLLM setting" would be more accurate.

## Nice-to-Haves
- A resolution-matched, token-budget-matched CLIP-only and DINOv2-only control trained with the full 100K-step recipe — this is the single experiment that would directly support the causal claim.
- Diagnostic analysis of the MLP-depth collapse (gradient norms, initialization, learning rate sensitivity, robustness across seeds).
- Drop COMM into a more recent base (e.g., LLaVA-1.5) to show the gains are not entangled with the Shikra-specific pipeline.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Reviewer claim that "first to investigate" overstates novelty because of concurrent works comparing CLIP/DINO/MAE for grounding.** Removed because the rule prohibits citing missing related work that I cannot verify externally. Kept a softer version as a Trivial note about the scope of the claim, which is internally checkable.
- **Strength: "The paper addresses an important problem."** Generic; removed per filtering rules.
- **Strength: COMM is "principled."** Marketing language without specific evidence; removed.
- **Reviewer claim that POPE gains are "modest (~1.4%)" and POPE is "saturating" — no significance reported.** Single-run evaluation is standard for these benchmarks; mentioning is fair but not a major issue and isn't a structural flaw. Kept as a Minor under variance.

## Novel Insights
None beyond the paper's own contributions. The per-layer ordering (shallow CLIP favors REC, deep CLIP favors POPE/REG) and the MLP-alignment trick for DINOv2 in MLLMs are the paper's own findings, and they are useful, but they are not augmented by additional novel insight in the reviews.

## Suggestions
- Add resolution-matched, token-count-matched CLIP-only and DINOv2-only controls at the full 100K-step recipe.
- Reconcile the Tab. 1 vs. Tab. 5 COMM numbers and clearly state which training regime each table reflects.
- Diagnose the MLP-depth collapse with at least an ablation across seeds, LR, and initialization.
- Replicate the MFM and DINOv2-MLP recipe on a non-Shikra base (e.g., LLaVA-1.5) to decouple from the Shikra training pipeline.
- Soften the abstract's "DINO surpasses CLIP in fine-grained tasks" framing to reflect that this holds on REC but not uniformly.

## Evaluation by Axis
- **Originality:** Moderate. The systematic intra-MLLM probing and the MLP-alignment-for-DINOv2 observation are useful; the fusion architecture itself is a straightforward concat with layerscale.
- **Importance:** The question of what visual encoder to use for MLLMs is genuinely important to the community.
- **Claim support:** Mixed. The strongest causal claim — that fusion is what produces the SOTA gaps over Shikra/Qwen — is not isolated from resolution and token-budget confounds. The narrower analytical claims are reasonably supported by the probing study, modulo the under-trained regime.
- **Soundness of experiments:** Adequate breadth (5 task families) but missing resolution-matched/token-matched controls, no seed variance, and an unresolved MLP-depth instability.
- **Clarity:** Generally clear; the Tab. 1 vs. Tab. 5 numerical mismatch and the regime-vs-headline distinction need explicit notes.
- **Value to community:** The probing artifact and DINOv2-MLP recipe are usable findings; the headline numbers should be interpreted with caution until controls are added.

## Score and Decision

Anchors retrieved (all from `/home/wg25r/split_review/datasets/deepreview_13k_calibration/`):
- `vqgDq1uycO.md` (MERV, multi-encoder fusion for VideoLLMs), avg 6.00 — closest topical match; fuses multiple visual encoders, accept-band but rejected; this paper is similar in spirit but has a clearer single-decision target (CLIP+DINOv2) and a more thorough per-layer analysis, though weaker controls.
- `2jEiFTLRwX.md` (VisionFuse, training-free MLLM fusion), avg 5.00 — very similar concept (combining multiple vision encoders for MLLM perception), reject; closest match in framing.
- `0yTf37PXcH.md` (Arcana, boosting MLLM vision), avg 5.40 — directly comparable: also aggregates intermediate CLIP features and adds a vision-side module; mid-band reject. Very close in spirit and scope.
- `FlvtjAB0gl.md` (unified language-vision pretraining), avg 6.25 — accept; more ambitious unification, broader contribution than this paper.
- `5E6VOD7W0z.md` (erroneous CLIP agreements), avg 4.50 — analysis paper on CLIP in MLLMs, weaker contribution.
- `fqtaADSGEe.md` (revisiting REC evaluation), avg 3.67 — REC-focused critique paper, lower than this work.
- `hLIlN0f4ix.md` (do better LMs have crisper vision), avg 5.00 — analytical study, mid-band.
- `xYzOkOGD96.md` (grounded video captions), avg 3.83 — less relevant, low-band reference.
- `Jwgw3znxT3.md` (token merging in ViT), avg 5.75 — tangential.
- `BI1N3lTWtn.md` (multi-level transformer training), avg 5.75 — tangential.
- `vJ0axKTh7t.md`, `k5VHHgsRbi.md`, `9OevMUdods.md` — high-band MLLM-related anchors (6.25–6.80); each is a more clearly scoped benchmark/analysis contribution than this paper.
- `0A6f1b66pE.md` (Mamba MLLM), avg 4.60; `ZAx5DxAucB.md` (LM4LV), avg 5.00; `h5UdvNFHee.md` (REVIP), avg 5.00 — mid-band MLLM papers.
- `s5T9A9tXTX.md` avg 4.00; `DiRJUdmZoK.md` avg 4.00; `pLvh9DTyoE.md` avg 2.50 — low-band MLLM-adjacent works, weaker than this paper.

This paper sits closest to Arcana (5.4), VisionFuse (5.0), and MERV (6.0): comparable scope (boost MLLM via better visual features), substantive experiments and a real finding (DINOv2 alignment, shallow-layer behavior), but real attribution/control gaps that prevent the headline claim from being fully isolated from confounds. It is stronger than the 4.0–4.6 band (more empirical breadth and a clearer finding) but does not reach the 6+ band, where contributions are either more novel or more carefully controlled.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>