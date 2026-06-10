## Summary
Frame-Voyager proposes learning to select informative frame combinations for Video-LLMs by training a lightweight reward model on combination-level rankings. The training data is generated automatically by exhaustively enumerating small (M,T) frame combinations, feeding them through a reference Video-LLM (VILA-8B), and ranking by prediction loss against ground-truth answers. At inference, the model scores each of M candidate frames (using features that incorporate inter-frame context from all M frames processed simultaneously through an LLM bottom layer) and picks the top T. Experiments on four VQA benchmarks show consistent improvements over uniform sampling and simple retrieval baselines, including outperforming LongVILA (128–256 frames) with only 8 frames.

## Strengths
1. **Combination-level supervision for frame selection is novel and effective.** The idea of using a reference Video-LLM's prediction loss to rank frame combinations and training a reward model on those rankings is a clever, human-free labeling pipeline. The training on combination-level data (pairwise ranking of full combinations) goes beyond typical frame-by-frame matching approaches.

2. **Strong empirical results.** Frame-Voyager with 8 frames outperforms LongVILA using 128–256 frames on extremely long videos (average 41 minutes). This is a striking result that directly supports the core thesis that frame quality matters more than frame quantity. On Video-MME (no subtitles), it improves VILA-8B by 3.0% (3.6% on long videos alone).

3. **Thorough ablation study (six RQs).** The paper systematically examines: comparison with other frame extraction methods (RQ1), data collection components (RQ2), frame count sensitivity (RQ3), architectural design choices (RQ4), performance by question type (RQ5), and qualitative analysis (RQ6). This is unusually thorough for a frame selection paper.

4. **Plug-and-play demonstrated across two architecturally distinct Video-LLMs.** VILA-8B uses SigLIP+Llama3-8B while VILA-40B uses InternViT-6B+Yi-34B. Consistent improvements on both suggest the method transfers across different visual encoders and LLM backbones.

## Weaknesses

### Fatal
None.

### Major
1. **Overclaiming "combinational" selection — inference reduces to individual top-T scoring.** The paper repeatedly claims to "consider the combination of frames as a whole" (Section 2, line 70) and perform selection "in a combinational manner" (Section 1, line 36). However, at inference (Section 3.3, line 157), the method simply computes a scalar reward for each frame independently and picks the top T — the same inference paradigm as the CLIP and VILA-Embedding baselines it criticizes for "ignoring frame-to-frame relationships." The model's per-frame features do incorporate inter-frame context (all M frames are processed simultaneously through the bottom LLM layer, line 127), which is a meaningful operational difference from pure independent scoring. But the paper frames the contribution as fundamentally combinational when the inference procedure is not. True combinational selection would evaluate subsets jointly. This gap between rhetoric and execution should be acknowledged and analyzed.

2. **Generalization across (M,T) regimes is asserted but never demonstrated.** The paper states that "models trained with smaller combinations exhibit generalization capabilities when larger values of M and T are used during inference" (lines 104–105), but provides zero systematic analysis. Training uses (M=16,T=2) and (M=32,T=4); inference uses (M=128,T=8) and (M=32,T=2). There is no experiment showing how performance varies when training on (16,2) and testing on (32,4), (64,8), (128,8), etc., nor analysis of what the model does differently at larger scales. This is the most important missing experiment for validating the method's practical utility.

3. **No comparison against learning-based frame selection methods.** The paper compares only against rule-based methods (Histogram, Edges Change Ratio, Motion) and simple embedding retrieval (CLIP, VILA-Embedding). The related work section cites learning-based methods (Wang et al. 2024, Yu et al. 2024, Liang et al. 2024) but these are not benchmarked against quantitatively. As a result, the advantage over the most relevant competitors is unclear.

### Minor
4. **Reference model fixed to VILA-8B; plug-and-play generality only tested on VILA variants.** The training data is generated using VILA-8B's losses, and evaluation is only on VILA-8B and VILA-40B (both from the same model family, albeit with different architectures). The paper claims plug-and-play generality but does not test on a genuinely different Video-LLM family (e.g., VideoLLaMA2, LLaVA-OneVision). Transfer of the ranking signal across model families remains unvalidated.

5. **Data filtering thresholds introduced without justification.** The thresholds for exclusion (average loss > 7, top 30%/10% by variance, line 174) are presented as if they are known good values. No ablation or sensitivity analysis is provided for these choices. Since filtering discards a large fraction of data, the impact of these thresholds on the final model could be significant.

6. **No runtime or efficiency comparison.** Frame-Voyager adds an extra pass through the visual encoder and one LLM layer for all M candidate frames. The overhead relative to uniform sampling or CLIP-based retrieval is not quantified, making it impossible to assess the practical cost of the accuracy gains.

### Trivial
None.

## Nice-to-Haves
- An analysis of ranking quality from the reference Video-LLM: e.g., human evaluation of top vs. bottom combinations, or agreement between different reference models, to validate that the loss-based ranking reflects genuine frame quality.
- Diversity/coverage metrics for the selected frames, in addition to VQA accuracy.
- An experiment combining Frame-Voyager with LongVILA's long-context approach to see if gains are complementary.
- Sensitivity analysis for the data filtering thresholds (average loss cutoff, variance percentiles).

## Removed Points
These points are flagged to be removed; treat them with caution:
- **Critic's strong version of "inference is not combinational"** — Retained and reframed as Major #1 (overclaiming). The critic's stronger version (equating the method to individual matching) is softened because the paper's frame features do incorporate all M frames' context through self-attention (line 127: "all M candidate frames are processed simultaneously"), which is a meaningful difference from CLIP-style independent scoring.
- **Critic's claim of "circular dependency"** — Demoted to Minor #4. The critic argued that using VILA-8B's losses creates a circular dependency. Testing on VILA-40B (different visual encoder and LLM) partially addresses this, making the strong "circular" framing overstated. The narrower concern (non-VILA models untested) is retained.
- **Strength Finder's claim #6 about generalization** — Removed because it directly conflicts with verified Major weakness #2. The paper asserts generalization (lines 104–105) but provides no evidence for it, making this an unsupported strength.
- **Critic's complaint about "no analysis of ranking quality"** — Moved to Nice-to-Haves. This is a worthwhile extension but not a core weakness.
- **Critic's complaint about ground-truth answers being required** — Removed. This is inherent to the supervised setup and the paper acknowledges it.
- **Critic's complaint about the two-stage downsampling (uniform then selection)** — Removed. The paper explicitly describes this design choice (Section 3, line 81); it is not a hidden limitation.
- **Critic's complaint about computational cost of data construction** — Removed. The paper mentions training costs (Section 4.1, line 188) and the data construction cost is implicit from the described pipeline. The critic's concern is about missing detail, not a substantive flaw.
- **Strength Finder's generic framing ("addressed an important problem")** — Not present in the actual Strength Finder output; all listed strengths are specific. No removal needed.

## Novel Insights
The most interesting observation emerging from the reviews is the tension between the paper's claim of "combinational" selection and its actual inference procedure. The paper's implicit defense — that per-frame rewards are computed from features that see all M frames simultaneously through self-attention — suggests an intermediate position between pure individual scoring and true subset evaluation that would benefit from precise characterization. Separately, the striking result that 8-frame Frame-Voyager beats 128–256 frame LongVILA on 41-minute videos raises a question about the "lost-in-the-middle" problem: perhaps the benefit of intelligent frame selection is not just relevance but avoiding the degradation that comes from packing many frames into the LLM context window. This suggests a potentially complementary relationship that the paper could explore.

## Suggestions
1. **Reframe the contribution honestly.** The method is a *per-frame scorer trained with combination-level supervision and context-aware features* — not "combinational frame selection." This reframing would be equally strong and far more defensible.
2. **Add a systematic (M,T) generalization experiment.** Train on (16,2) and test on (32,4), (64,8), (128,8), etc., with and without fine-tuning. This is the single most important missing analysis.
3. **Compare against at least one learning-based frame selection method** from the cited literature (e.g., KeyVideoLLM clustering, weakly-supervised selection from Wang et al. 2024).
4. **Report inference-time overhead** in wall-clock time and FLOPs relative to uniform sampling and CLIP-based selection.
5. **Test on at least one non-VILA Video-LLM** (e.g., VideoLLaMA2, LLaVA-OneVision) to substantiate the "plug-and-play" claim.
6. **Add sensitivity analysis for the data filtering thresholds** (average loss cutoff, variance percentile) to show robustness.

## Score and Decision

The paper addresses a real problem with a clever, well-executed approach. The core idea (combination-level supervision for frame scoring via a reference Video-LLM's prediction loss) is novel, and the empirical results are strong — particularly the LongVILA comparison. The six-RQ ablation is unusually thorough. However, the overclaimed "combinational" framing and the missing generalization analysis are significant issues that prevent this from being a top-tier paper in its current form. With honest reframing and the addition of the key missing experiments, this would be a strong paper. I lean toward acceptance because the contributions are real and the weaknesses are addressable.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>