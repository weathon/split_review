## Summary
The paper investigates which visual encoder is best for MLLMs, systematically probing CLIP, DINOv2, MAE, and DeiT layer-by-layer on REC/REG/POPE. It reports two empirical findings — shallow CLIP layers help fine-grained grounding, and vision-only DINOv2 (with a non-linear MLP for alignment) is competitive as an MLLM visual branch — and proposes COMM, which fuses multi-level CLIP and deep DINOv2 features. COMM-7B reports SOTA on RefCOCO/+/g REC, REG, POPE, and several VQA/captioning benchmarks.

## Strengths
- **Layer-wise probing methodology is concrete and useful.** §3 / Fig. 3 sweeps the encoder layer index and evaluates REC/POPE/REG separately, yielding the specific observations that CLIP REC accuracy peaks around layer 12 while POPE improves with depth, and that REG CIDEr peaks around layer 16. This is a clean protocol future work can build on.
- **Surprising and well-supported empirical claim about DINOv2.** Table 1 shows DINOv2 + MFM + MLP reaches 72.8 avg REC vs. CLIP's 47.3 baseline (last-layer), which is genuinely informative against the prevailing assumption that text-image pretraining is required for the MLLM visual branch.
- **Systematic MFM strategy ablation.** Fig. 4 contrasts Mean(half), Mean(all), Layerscale, and LLN-Layerscale on both CLIP and DINOv2 and shows a coherent picture: shallow features help for CLIP but degrade DINOv2 (Mean(19–24) > Mean(all)), which is the specific evidence motivating the architecture in Eq. (1).
- **Hallucination gains are non-trivial.** COMM improves POPE Popular/Adversarial over Shikra by ~2–3 points, which is meaningful for the hallucination question and consistent with the fine-grained-features hypothesis.

## Weaknesses

### Fatal
None.

### Major
- **Headline SOTA comparisons confound the proposed fusion with a resolution jump and a doubled visual backbone.** §5.1 explicitly states COMM trains at 336×336 while Shikra uses 224×224, and COMM uses two ViT-L encoders versus baselines' one. REC/REG are very resolution-sensitive, so the 3–5 point gains over Shikra-13B / Qwen-VL-7B-Chat in Table 2 cannot be cleanly attributed to "fusing CLIP and DINOv2 with MFM." No matched-resolution or parameter-matched comparison is provided. This directly threatens the central architectural claim — the very thing COMM is selling.
- **The full-scale ablation that would isolate the DINOv2 contribution is missing.** Table 1 is the only direct CLIP-w/-MFM vs. COMM comparison and is run at 9.4k iterations / batch 16 (the §3 analysis recipe), not the 100k-step / batch-64 / 336-resolution recipe used for Tables 2–5. At analysis scale the CLIP-w/-MFM avg REC is already 70.0 vs. COMM's 72.8 (Δ=2.8). Whether DINOv2 still adds value at full training scale is therefore not demonstrated — and this is the core claim of the paper.

### Minor
- **MLP-depth and DeiT collapses look like training failures and are over-interpreted.** Table 4 (MLP) shows DINOv2 with 2-MLP → 77.5 test-A, 4-MLP → 53.7, 8-MLP → 8.2; Table 5 shows DeiT REC test-A at 18–25. These are catastrophic, not graceful, degradations under one fixed recipe and learning rate. The paper draws strong qualitative conclusions ("supervised training too strong, hard to align with word embedding space"; deeper MLPs categorically hurt) without LR sweeps or loss curves. The conclusions may well be right, but the present evidence does not exclude an optimization failure.
- **Selection of LLN-Layerscale is on the same set used downstream.** Five MFM strategies are introduced in §3, only three appear in Fig. 4 (Conv-Layerscale results aren't shown for both encoders), and the chosen variant is picked on REC/POPE — the same evaluations later used to argue for COMM. A held-out selection set would strengthen the argument.
- **Asymmetric DINOv2 layer range is fixed without ablation.** Eq. (1) uses all 24 CLIP layers but only DINOv2 layers 19–24. The paper justifies this informally ("shallow DINOv2 lacks semantic information," Fig. 4c–d), but no sweep is reported (e.g., 13–24, 16–24) — and the paper's central narrative emphasizes shallow features for grounding, so the cut-off deserves explicit testing on REC.
- **POPE and VQA baseline sets are thin.** Table 6 (POPE) compares only against Shikra-7B / InstructBLIP / MiniGPT-4 / LLaVA / mPLUG-Owl / MM-GPT; Qwen-VL is absent. Table 7 has multiple blank LLaVA-1.5 cells, and "SOTA over LLaVA-1.5-13B" rests on a single VQAv2-dev cell. This is presentational, not fatal, but it makes the SOTA claims softer than the table headlines suggest.
- **"First to extensively investigate visual encoders for MLLMs" is overstated** as a contribution. Reframe as "first to systematically probe layer-wise contributions across four encoder families in the Shikra recipe," which is what the experiments actually support.
- **Reproduced Shikra-7B REG numbers diverge dramatically from the paper's own.** Table 3 reports Shikra at 44.26 CIDEr on RefCOCO test-A from the official checkpoint, while paired RefCOCO test-B is 104.83 — the within-row spread suggests a possible eval-protocol mismatch that should be sanity-checked.

### Trivial
- "Less training data than Qwen (3.6M vs. 1.4B)" is a rhetorical comparison across very different corpus types (curated VQA/grounding vs. noisy web image-text). The point would be stronger if framed as training-data composition rather than absolute count.

## Nice-to-Haves
- Report the learned LayerScale weights α_i, β_j at convergence for COMM. This would directly verify that the "shallow CLIP helps grounding" probe finding survives full-scale training, and would tie §3 to §4 quantitatively.
- Provide one evaluation that controls for resolution (e.g., COMM at 224 vs. Shikra at 224, or one fixed-resolution grounding suite).
- Add seeds or at least a sensitivity bar on the §3 analysis-scale runs, since those curves drive the architectural choices.

## Removed Points
*These points were raised by the harsh critic but flagged here to be removed; treat them with caution.*
- "Equation (1) using only DINOv2 19–24 contradicts the paper's main message." Partially a misread — the paper's narrative is that shallow features help **for CLIP**, while it explicitly shows (Fig. 4c–d) that DINOv2 shallow features hurt. The asymmetric cut is consistent with the paper's argument, even if the specific cut-off layer is unablated (kept as a minor weakness above).
- Concerns about MAE/DeiT being "unsuitable" — kept above as a minor methodological caveat, but the harsh critic's framing as a structural flaw is too strong: the paper's broader narrative does not hinge on these encoders being categorically unusable.
- "Missing concurrent/prior work on probing CLIP layers." Dropped per review policy (cannot independently verify external references).
- Strength about LLN-Layerscale being a "thorough ablation of merging strategies" — kept, but with the caveat that selection happens on the eval set.

## Novel Insights
None beyond the paper's own contributions. The probing-by-layer-index methodology and the observation that vision-only DINOv2 + MLP rivals CLIP as an MLLM backbone are genuinely the paper's own.

## Suggestions
- Run, at minimum, **CLIP+MFM at 100k steps, 336 resolution, same data, same Vicuna-7B**, and compare directly to COMM. This is the single experiment that turns the contribution from suggestive to demonstrated.
- Add a 224-vs-336 row for COMM (or a 336 row for Shikra reproduced) to disentangle resolution from fusion.
- Sweep the DINOv2 layer range (e.g., {13–24, 16–24, 19–24, all}) on REC; this is cheap and directly addresses a load-bearing design choice.
- For the MLP-depth / DeiT collapses, report LR sweeps or loss curves; absent that, soften the categorical language ("unsuitable") in §3 and §5.
- Fill out Table 7 (LLaVA-1.5 cells) and add Qwen-VL to the POPE table; the SOTA framing currently rests on a thin baseline set.

## Axis Evaluation
- **Originality:** Moderate. The layer-wise probe is a fresh angle and the DINOv2-as-MLLM-backbone result is novel, but multi-encoder fusion itself is well-trodden.
- **Importance:** High. Which visual encoder to use is a load-bearing question for MLLMs.
- **Support for claims:** Mixed. Probing claims (§3) are reasonably supported; the central architectural claim (COMM > CLIP-w/-MFM) is supported only at small training scale, while the SOTA numbers are confounded by resolution and parameter count.
- **Soundness of experiments:** Adequate at the probing level; weak at the headline-comparison level.
- **Clarity:** Reasonably clear; figures and tables are readable.
- **Value to the community:** Moderate. The probing methodology and the DINOv2 finding are useful even if the COMM-vs-baselines comparison does not yet conclusively isolate the proposed fusion.

## Score and Decision
The paper makes two genuinely useful empirical contributions (layer-wise probing, DINOv2 as a viable MLLM backbone), but the headline architectural claim — that COMM's fusion specifically is what drives the gains — is not cleanly isolated from a 224→336 resolution increase and a doubled visual backbone, and the one direct ablation against CLIP-w/-MFM is only run at small scale. These are major but not fatal issues; the contribution is real but the strongest claims are not yet earned.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>