## Summary

EmbodiedMAE proposes a multi-modal masked autoencoder that jointly learns representations across RGB, depth, and point clouds for robot manipulation. The authors construct DROID-3D, a large-scale supplement to the DROID dataset with ZED SDK-derived depth and point clouds (76K trajectories, 350 hours), and train a ViT-Giant multi-modal MAE on it, then distill to smaller variants. The paper evaluates across 70 simulation tasks (LIBERO, MetaWorld) and 20 real-world tasks on two robot platforms (SO100, xArm).

## Strengths

- **Addresses a genuine gap in 3D VFMs for embodied AI and demonstrates an architecture that avoids the 3D-degradation problem.** The paper correctly identifies that naively adding 3D channels to standard VFMs degrades performance. Table 1 provides clear evidence: DINOv2-RGBD drops from 70.7% to 54.4% on MetaWorld average (a 16.3-point regression), while EmbodiedMAE-RGBD *improves* over EmbodiedMAE-RGB (76.2% vs 73.0%). This asymmetry is the paper's strongest empirical finding and directly supports the claim that the multi-modal MAE design promotes effective 3D policy learning.

- **DROID-3D is a practical resource for the community.** Processing the full DROID dataset (76K trajectories, 350 hours) with ZED SDK — going well beyond SPA's ~1/15 subset using CrocoV2-Stereo — and providing metric depth and point clouds for every frame addresses a real bottleneck in 3D embodied research. The qualitative depth comparison (Figure 2) shows clear improvements over native depth from BridgeDataV2/RH20T and AI-estimated depth from SPA.

- **Broad evaluation scope with real-robot validation.** The paper evaluates across 70 simulation tasks (LIBERO 40 + MetaWorld 30) and 20 real-world tasks on two distinct robot platforms (low-cost SO100, high-performance xArm), which is more comprehensive than many VFM-for-robotics papers. The consistent improvement pattern — EmbodiedMAE variants outperform baselines across most settings, with particularly large margins in RBGD/PC configurations — provides converging evidence for the method's effectiveness.

- **Re-coloring experiment (Section 3.2) provides qualitative evidence of emergent object-level understanding.** The model propagates a color change from an altered patch to only the corresponding object while preserving the background and robot appearance, suggesting that multi-modal MAE pre-training induces implicit object-level segmentation despite no supervised training for it.

## Weaknesses

### Major

- **Headline claims are overstated relative to the evidence.** The abstract and conclusion claim EmbodiedMAE "consistently outperforms state-of-the-art vision foundation models." On MetaWorld RGB-only (Table 1), EmbodiedMAE-Large achieves 73.0% — identical to SPA (73.0%) — and SPA *outperforms* EmbodiedMAE on Medium difficulty (62.8% vs 60.4%). On xArm real-world tasks in the RGB-only setting, Figure 8's caption describes performance as "comparable to SOTA baselines." The abstract, introduction, and conclusion uniformly frame results as superior across the board, erasing these nuances. This damages the paper's credibility. The narrative would be *stronger* with honest framing (e.g., "competitive with SPA on RGB-only, with large gains from multi-modal inputs").

- **Real-world evaluation lacks statistical rigor.** Each real-world task is evaluated over only 10 trials (Figure 8 caption), with no confidence intervals, standard deviations, or error bars reported anywhere. For robot manipulation, task variance from initial conditions, hardware stochasticity, and policy noise can shift success rates by 10–20 percentage points. With this sample size, observed differences of ~5 points on several tasks are indistinguishable from noise. The claim of "SOTA performance in real-world manipulation" is not adequately supported.

- **Ablation studies do not validate core architectural design choices.** The ablations in Section 3.5 focus entirely on distillation hyperparameters (masking ratio, feature alignment points, loss ratio β). The central design questions — stochastic Dirichlet masking vs. fixed modality allocation, cross-attention decoder vs. simpler fusion (e.g., concatenation + linear decoder), shared vs. separate per-modality encoders — are never ablated. The paper acknowledges this is due to "prohibitive cost of ViT-Giant pre-training," but the consequence is that we do not know which design elements drive performance. An ablation at a smaller model scale (e.g., ViT-Base) would substantially strengthen the paper's method contribution.

- **DROID-3D dataset quality is asserted, not quantitatively validated.** The paper claims "high-quality" depth and point clouds for DROID-3D and contrasts them with "low-quality" alternatives from BridgeDataV2, RH20T, and CrocoV2-Stereo, but the only evidence is qualitative (Figure 2). No quantitative metrics (RMSE, absolute relative error, accuracy against any ground truth) are reported. For a dataset requiring ~500 hours of processing and positioned as a key contribution, the lack of quantitative validation is a significant gap.

- **Missing baseline: MultiMAE (Bachmann et al., 2022).** MultiMAE is the most directly comparable prior work — it processes RGB+depth through a multi-modal MAE with the same Dirichlet masking strategy (cited as the source). The paper never compares against it as a baseline. Without this comparison, it is unclear whether EmbodiedMAE's gains come from its specific design choices or simply from applying a multi-modal MAE to robot data rather than static images.

### Minor

- **No variance or confidence intervals reported anywhere in the paper.** Across all tables and figures (Table 1, Figure 6, Figure 8), not a single standard deviation, confidence interval, or error bar is reported. For a paper making comparative claims against five baselines across 90 tasks, this is a significant omission that makes it impossible to assess whether observed differences are meaningful.

- **Modality encodings in the decoder (Section 2.3) are underspecified.** The paper states that visible patches are "projected and enhanced with modality encodings" to form keys and values for cross-attention, but does not specify how these modality encodings are computed (learned embeddings? fixed codes?). This missing detail makes the architecture description incomplete.

- **100% masking ablation is unclearly described.** Section 3.5 tests "70%, 80%, and 100% ratios (100% representing training with only feature alignment loss)." It is unclear how the teacher model produces meaningful features for the student to align to when the student receives no visible patches at all.

- **The claim about bias terms implicitly encoding modality information (Section 2.2) is asserted without evidence.** Since the encoder shares parameters across modalities, it is not obvious that bias terms alone in the projection layers can disambiguate modalities. This should be verified or discussed.

### Trivial
- Inference FLOPs or wall-clock time for the VFM component are not reported, which would be useful for real-time robotics deployment.

## Nice-to-Haves
- Quantitative validation of DROID-3D depth quality (e.g., RMSE on held-out frames against a reliable reference).
- An ablation of the core architectural choices (stochastic vs. fixed masking, cross-attention decoder vs. simpler fusion) at ViT-Base scale.
- Statistical significance testing on real-world results (10 trials support binomial confidence intervals).
- Failure mode analysis for EmbodiedMAE's own mistakes (the paper only describes baseline failures).

## Removed Points
- **"Table 1 column headers are garbled"**: This is a parser artifact from the PDF extraction process; the original submission does not have this issue. Removed per "remove formatting artifacts" rule.
- **"ZED SDK may not generalize to all DROID camera hardware"**: Speculative concern about a potential limitation that is not a verified flaw in the paper as written. Removed.
- **"Section 1 conflates two separate issues about 3D VFMs"**: The criticism is about framing, not factual error. The introduction correctly cites Ze et al. and Zhu et al. for the claim that 3D representations can degrade policy performance. Removed.
- **"Related works should discuss VLA models more"**: The paper's scope is VFMs as backbones for embodied AI; it appropriately scopes itself. Removed.
- **Strength Finder's generic strengths** ("the paper addressed an important problem"): Removed as they are generic and lack specific evidence.

## Novel Insights

The most interesting cross-cutting observation is the empirical asymmetry: DINOv2's performance drops 16.3 points when depth is added (MetaWorld: 70.7% → 54.4%), while EmbodiedMAE improves (73.0% → 76.2%). Combined with the re-coloring experiment (Section 3.2) showing emergent object-level semantics, this suggests that multi-modal MAE pre-training on robot data learns cross-modal correspondences that standard vision-only VFMs lack entirely — making the representations immune (or even positively responsive) to the distributional shift introduced by 3D sensor inputs. This is the paper's strongest finding and warrants more emphasis than it receives.

## Suggestions
1. **Reframe the central claim.** The paper's genuine contribution — a 3D-aware VFM that avoids the degradation seen in other VFMs when adding depth — is strong enough that overclaiming RGB-only results only hurts credibility. State results honestly: "competitive with SPA on RGB-only, with large gains from multi-modal inputs."
2. **Report confidence intervals**, at minimum for the real-world results. With 10 trials, binomial confidence intervals are trivially computable.
3. **Add one core architectural ablation at ViT-Base scale**, even on a subset of tasks, to validate that the specific design choices (stochastic masking, cross-attention decoder) matter.
4. **Include quantitative depth metrics** for DROID-3D (RMSE, accuracy-threshold) against a held-out reference.
5. **Add MultiMAE as a baseline** adapted to the same policy learning setup.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Path | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| I0To0G5J7g.md | 3.20 | R1 | Much weaker paper (On the Surprising Efficacy of Online Self-Improvement...) |
| sXF5P4N7e8.md | 3.00 | R1 | Much weaker — narrow scope (Vision-Based Grasping through Goal-Conditioned Masking) |
| 9GKMCecZ7c.md | 3.40 | R1 | Weaker — simulation-only evaluation (Building Generalist Robot Policy) |
| 6TLdqAZgzn.md (SPA) | 6.50 | R1 | Stronger — 268 tasks, clearer claims, better ablation (SPA: 3D Spatial-Awareness) |
| Crsl3zbfvW.md | 4.40 | R1 | Comparable — similar issues with evidence (Single-View 3D Representations for RL) |
| IsGsv8qEHp.md | 5.00 | R1 | Similar — same overclaiming and missing CI issues (Human-oriented Rep Learning) |

**Round 2 — Narrowing:**
| Path | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| NxoFmGgWC9.md (GR-1) | 5.50 | R2 | Slightly stronger — clearer claims, accepted despite weak real experiments |
| vJwjWyt4Ed.md (ReViWo) | 5.40 | R2 | Comparable — accepted but had better ablations and narrower evaluation |
| izzYucQBji.md (DROP-CLIP) | 5.25 | R2 | Similar — same dataset validation and missing baselines issues, rejected |
| KTtEICH4TO.md (CORN) | 4.75 | R2 | Slightly weaker — narrower scope but cleaner execution, accepted |
| bw9bvwVwMH.md | 6.00 | R2 | Stronger — 3D self-supervised learning paper with better validation |

**Initial bracket (R1):** 4.0–5.5. **Narrowed assessment (R2):** The paper sits around 5.0, comparable to the 5.0–5.25 range anchors. It is weaker than SPA (6.5) and GR-1 (5.5) due to overclaiming, thin real-world evidence, and missing ablations. It is stronger than the 3.x papers (simulation-only, narrow scope). The contributions are genuine but insufficiently validated for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>