Now I have all the information I need. Let me construct the final review.

## Summary

The paper proposes OC-STORM, an object-centric model-based RL pipeline that integrates a frozen pre-trained video object segmentation model (Cutie) into the STORM world model. Object features are extracted via few-shot annotated masks (6-12 per environment), encoded through a categorical VAE, and fed alongside raw visual observations into a spatial-temporal transformer for dynamics prediction and policy learning. The method is evaluated on the Atari 100k benchmark (26 games) and on Hollow Knight boss fights.

## Strengths

1. **Clear motivation and well-designed pipeline.** The paper articulates a genuine limitation of reconstruction-based MBRL (L₂ loss dominated by large background areas) and proposes a practical remedy: feed compact object feature vectors from a frozen foundation model into the world model. The four-step pipeline (annotate → extract → incorporate → train) is cleanly described, and Figure 2 provides a helpful architectural overview.

2. **Consistent improvement over STORM across diverse domains.** On Atari 100k, OC-STORM achieves 134.8% mean HNS vs STORM* at 114.2% (and vs original STORM at 122%), winning on 18 of 26 games (Table 1). On Hollow Knight bosses, the improvements are substantial — notably Mage Lord (return 28.0 vs 19.6, win rate 48% vs 5%) and Pure Vessel (15.7 vs 8.9) (Table 3). These results demonstrate that the object-centric design provides a meaningful advantage over the non-object-centric baseline.

3. **Careful categorization and analysis of when object-centricity helps.** Table 2 splits Atari games into "object-representable" vs. "not," showing a large improvement in the former (142.8% vs 116.5%) and comparable performance in the latter (124.0% vs 130.0%). This honest breakdown helps characterize the method's capabilities and limitations.

4. **Informative ablation study.** Figure 4 compares vector+visual, mask+visual, visual-only, and vector-only configurations across five environments, showing that the compact vector representation from Cutie outperforms raw mask inputs — a non-trivial and practically useful finding that justifies the design choice.

5. **Few-shot annotation with frozen foundation model.** The method requires only 6-12 annotation masks per environment and uses a frozen Cutie, avoiding the need for extensive labels or internal game state access that prior object-centric RL work required. The reconstruction experiment (Figure 3) validates that the 2048-d feature vectors retain sufficient spatial and state information.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline configuration ambiguity weakens the primary comparison.** The paper compares OC-STORM against STORM*, which uses "a more lightweight configuration for faster training and decision-making on Hollow Knight" (Table 1 caption). While STORM* and OC-STORM share the same config (controlling for the config variable), the paper never specifies what was changed, nor does it justify that the lighter config does not systematically disadvantage STORM more than OC-STORM. Since the object module provides additional representational capacity, it could plausibly compensate for a reduced visual backbone in a way that the baseline cannot. This ambiguity undermines confidence that the reported gains are purely attributable to object-centricity. The original STORM scores (122% HNS) are listed as reference, but they are obtained under different (unknown) conditions and thus cannot serve as a controlled baseline either. **Why it matters**: the paper's central empirical claim is that OC-STORM improves over STORM; the reader cannot verify whether this improvement is robust to the configuration choice without either (a) a specification of the config change, or (b) a confirmatory experiment using the original STORM config on a subset of games.

### Minor

2. **No variance reporting for main Atari results (Table 1).** Only mean HNS across 5 seeds is reported, with no standard deviations, confidence intervals, or significance tests. The ablation study (Figure 4) shows that variance information exists. Without it, the reader cannot assess whether reported improvements (e.g., 134.8% vs 114.2% overall, or the 124% vs 130% gap in the non-object category) are statistically reliable. This is standard practice for many Atari 100k papers, but including variance would significantly strengthen the paper.

3. **Hollow Knight evaluation lacks non-STORM baselines.** The paper acknowledges that direct comparison with other methods is "impractical" due to differing settings (line 250), but does not attempt to run DreamerV3 or DIAMOND under the same conditions. Since DIAMOND outperforms OC-STORM on Atari (146% vs 134.8%), it is plausible it would also be competitive on Hollow Knight. The claim of "best-known sample efficiency on several Hollow Knight bosses" is therefore unsupported. This limits the significance of the Hollow Knight results to a single ablation (OC-STORM vs STORM) rather than a demonstration against the broader field.

4. **Non-object category underperformance is not analyzed.** On the 11 games where "not all key information can be represented as objects," OC-STORM achieves 124.0% HNS vs STORM* at 130.0% — a real deficit that the paper describes as "on par." No analysis is provided for why performance drops in specific games (e.g., duplicate instances in MsPacman, missing background in Gopher), even though the limitations section identifies these failure modes. A focused analysis on 2-3 representative games would sharpen the paper's understanding of its own method's boundaries.

### Trivial
None.

## Nice-to-Haves

- **Report standard deviations for Table 1.** Even a supplementary table with per-game std devs would substantially increase the credibility of the results.
- **Run at least one additional baseline on Hollow Knight.** DreamerV3 is open-source and could be configured to match the OC-STORM training setup. Even a rough comparison would contextualize the results.
- **Specify the lightweight configuration changes** from original STORM to STORM* (network sizes, batch sizes, etc.).

## Removed Points

These points were flagged for removal. Treat them with caution.

- *Harsh Critic Critical Issue 1 (reworded part)*: "If the configuration is suboptimal for STORM... any improvement could simply reflect that the baseline is weakened." — The paper states STORM* and OC-STORM share an *identical* configuration, so the comparison is controlled. The concern that lighter configs might asymmetrically affect the two methods is a reasonable speculation but not a proven flaw; it is kept in weakened form as Major Weakness #1 above rather than as "fatal."
- *Harsh Critic: "Missing appendix details"* (hyperparameters, model sizes, etc.) — The parser strips appendices; these exist in the original submission.
- *Harsh Critic: "Computational overhead of Cutie inference"* — Not a core claim of the paper; nice-to-have but not a weakness.
- *Harsh Critic: "Hollow Knight environment under-described"* (wrapper, reward function, action space details) — Likely in the stripped appendix.
- *Strength Finder: Generic/superficial strengths* ("the method is plausible," "the paper is well-written," "the problem is important") — Removed for lack of concrete specificity; the retained strengths above are all grounded in specific evidence from the paper.

## Novel Insights

The reviews surface an interesting tension not fully addressed by the paper. The method's core strength — the compact object feature vector from Cutie — is also its key limitation. Cutie's object-level features are effective precisely when the environment has clearly delineated, non-duplicated objects of interest, but this excludes many real-world scenes with repetitive patterns, amorphous obstacles, or continuous terrain. The paper's split into "object-representable" vs. "not" games (Table 2) is a step toward understanding this boundary, but the absence of analysis for the underperforming category leaves the actual failure modes uncharacterized. A second tension concerns the role of the raw visual stream: the method never fully commits to the object-centric representation (it always keeps visual input), which raises the question of whether the improvement comes from the object features specifically, or simply from having a larger/better model (two streams instead of one). The ablation (Figure 4) partially addresses this by showing that "Vector + Visual" outperforms "Visual (STORM)" and "Vector only," but the paper would benefit from a more direct apples-to-apples comparison of model capacity vs. representational quality.

## Suggestions

1. **Clarify the baseline configuration.** Describe what was changed from original STORM to STORM*. Better yet, run both STORM (original config) and OC-STORM (original config) on a representative subset of Atari games (e.g., 5-6 games from each category in Table 2) to demonstrate that the improvement holds regardless of the config choice.

2. **Add variance to Table 1.** Include standard deviations or interquartile ranges for the 5-seed Atari results. This is a low-effort addition with high impact.

3. **Analyze 2-3 underperforming non-object games.** For e.g., Hero, Frostbite, and Gopher, show qualitative examples of what Cutie segments and what it misses, and discuss how this relates to the performance gap. This would turn a weakness into a strength by providing actionable insight.

4. **Run DreamerV3 on Hollow Knight.** It is open-source and can be configured to match OC-STORM's sample limit. Even a single boss (e.g., Hornet Protector or Mage Lord) would contextualize the Hollow Knight results against a non-STORM baseline.

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Small Features Matter | Qr9TjKYzjl.md | 3.00 | R1 | Clearly weaker paper — lacking novelty, limited evaluation. OC-STORM is stronger. |
| Transformers+slot encoding | 2H6KhX1kJr.md | 3.00 | R1 | Weaker — similar domain but less thorough evaluation. |
| SOLD (obj-centric latent dyn) | iqdqRmqUsD.md | 4.00 | R1 | Weaker — missing baselines, limited task scope. OC-STORM has broader evaluation. |
| OCAtari | 4PzxLPEGRn.md | 4.50 | R1 | Benchmark paper, not directly comparable. Similar score band. |
| Harmony World Models | RN7RzMxwjC.md | 5.00 | R2 | Weaker — limited baselines, missing ablations. OC-STORM is more thorough. |
| SGF (Simple Good Fast) | yFGR36PLDJ.md | 5.75 | R2 | Comparable quality. SGF accepted as poster; OC-STORM has stronger contribution but similar evaluation rigor. Slightly below OC-STORM. |
| OOCDM | 7VVGO0kuuY.md | 5.80 | R1 | Comparable score band. OOCDM had stronger theory but weaker evaluation domains. |
| SafeDreamer | tsE5HLYtYg.md | 6.50 | R2 | Stronger paper — broader evaluation, cleaner comparisons. OC-STORM is below this. |
| EC-Diffuser | o3pJU5QCtv.md | 6.25 | R2 | Stronger — more thorough evaluation on manipulation tasks, ablations. |

**Round 1 bracket**: 4.0 – 7.5. The paper is clearly above the 3.0-level papers (which had fundamental issues with novelty/rigor) and below the 8.0-level papers.

**Round 2 narrowing**: Within the 4.5–7.5 bracket, I compared OC-STORM to SGF (5.75, accepted poster), HarmonyWM (5.0, reject), OOCDM (5.8, reject), and EC-Diffuser (6.25, accepted poster). OC-STORM is stronger than HarmonyWM and comparable to SGF (slightly stronger contribution, slightly weaker evaluation). It is weaker than EC-Diffuser (which has more thorough ablations and baselines). The paper sits between 5.75 and 6.25 — I place it at 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>