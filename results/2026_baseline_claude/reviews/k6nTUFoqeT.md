---

## Summary

FASTer is a unified framework for efficient autoregressive Vision-Language-Action (VLA) robot learning. It contributes two coupled components: **FASTerVQ**, a transformer-based residual vector-quantization (RVQ) tokenizer that encodes action chunks via 2D non-uniform patchification and joint temporal+frequency-domain reconstruction losses, achieving high compression with near-lossless reconstruction; and **FASTerVLA**, a VLA policy atop FASTerVQ that uses block-wise autoregressive (BAR) decoding and a lightweight action expert, yielding faster inference and stronger task performance. The framework is evaluated across nine benchmarks spanning five distinct embodiments in both simulation and the real world.

---

## Strengths

- **Strong and comprehensive empirical results**: FASTerVLA achieves 97.9% on LIBERO (top overall, exceeding prior AR models including π₀₅) and 87.9% on Simpler-Bridge (+12.9% over the second-best baseline). Evaluation spans nine benchmarks, five embodiments (single-arm, bimanual, whole-body), simulation and real hardware—an unusually broad validation for a method paper.

- **Practical inference speedup is substantial and well-documented**: In the single-arm setting, FASTerVLA runs in 112ms vs. 176–556ms for π₀/π₀-FAST (using the same PaliGemma backbone). For whole-body control (21-DoF, 32-step horizon), FASTerVLA completes in 237ms vs. 1,100–3,000ms for π₀-FAST—a speedup of 5–13× that makes the difference between operational and inoperable inference rates. Inference breakdown in Table 2 is transparent and informative.

- **Thoughtful 2D patchifier design**: Treating the action chunk as a 2D array (temporal × physical-group) and applying non-uniform grouping by physical semantics (EEF position, orientation, gripper state, base velocity) is a principled design choice grounded in the heterogeneous distribution problem. The analogy to audio-codec RVQ (shared traits: non-uniform information density, temporal correlations) is well-argued and leads to concrete architectural decisions.

- **Novel VRR metric** grounded in physical execution tolerances: the Valid Reconstruction Rate at tolerance σ is more directly interpretable than MSE/MAE, and the finding that codebook utilization (100% for FASTerVQ vs. 48–57% for FAST) correlates with downstream task performance is an empirically grounded insight linking tokenizer quality to policy quality.

- **Cross-embodiment and cross-backbone generalizability demonstrated**: FASTerVQ trained on single-arm delta-EEF data generalizes to joint-velocity, absolute joint-position, and delta joint-position actions from unseen embodiments (Droid, Galaxea, Aglex). Cross-backbone experiments (PaliGemma2-3B, Qwen2.5-3B, InternVL3.5-2B) show consistent gains, including a +17.3% absolute improvement for InternVL3.5-2B.

---

## Weaknesses

### Fatal
None.

### Major

1. **Comparison fairness on headline benchmarks is partially opaque.** The paper states models are initialized from "checkpoints pretrained on large-scale robotics data (e.g., from π₀-FAST)." It is unclear whether all compared models (notably π₀₅ from Physical Intelligence, which has proprietary scale) share the same pretraining corpus or have access to more data. The margin over π₀₅ on LIBERO is 1.1 percentage points, well within a range where training-data differences could account for the gap. The paper would be strengthened by explicitly controlling for or reporting the pretraining corpus size across baselines, or by at minimum reporting a fixed-backbone comparison where this ambiguity cannot arise.

2. **Statistical significance is absent throughout.** No standard deviations, confidence intervals, or number of evaluation trials are reported anywhere in the main results (Tables 1, 2, and Figures 4, 7, 9, 10). Given that success rates for several sub-tasks in Simpler-Bridge differ by only a few percentage points between methods, and real-world evaluations are inherently noisy, statistical significance is needed to confidently interpret the results.

3. **Stability claims are stated but not evidenced.** The paper asserts that "training a VLA on variable-length codes is substantially more challenging than on fixed-length representations" and that the coarse-to-fine RVQ structure "stabilizes both training and inference." These are quantitative empirical claims requiring quantitative support (e.g., training loss curves, variance across seeds, or failure-mode analysis). Neither training curves nor multi-seed variance are reported in the accessible portions of the paper.

### Minor

1. **BAR adds modest empirical gains over the non-BAR variant, and the theoretical justification for parallel decoding is informal.** The paper motivates parallel within-block prediction by noting action dimensions "often carry independent physical semantics," but the same physical correlation argument that motivates the 2D patchifier could equally imply dependencies between action dimensions. The average gain from BAR on LIBERO is ~2 points; on Simpler-Bridge it is actually negative in some sub-tasks (99.4% → 97.5% for the Spoon task). A more rigorous characterization of when/why BAR helps or hurts would strengthen the design argument.

2. **Spacing augmentation is introduced but not ablated.** This is a non-trivial training trick; its contribution to position-overfitting prevention should be quantified.

### Trivial
None beyond obvious parser artifacts in rendered figures (e.g., "#Lidar" in Figure 8).

---

## Nice-to-Haves

- Training curves (loss, codebook utilization vs. steps) for FASTerVQ and FASTerVLA would support the scaling and stability claims.
- An ablation of the DCT frequency-domain loss component vs. time-domain only, to quantify its contribution.
- Clarification of how proprioceptive state discretization (mentioned as "discretized into integers and tokenized as text") interacts with the VLM vocabulary, and whether this causes any vocabulary collision issues.

---

## Novel Insights

Beyond the paper's own stated contributions, there is a genuinely interesting structural insight: the two-dimensional heterogeneity of action sequences (temporal redundancy vs. cross-dimension semantic diversity) mirrors the structure of spectro-temporal audio representations, and the RVQ codec literature's solutions (non-uniform patching, RVQ coarse-to-fine quantization, combined time+frequency reconstruction) transfer directly to robot actions with measurable benefit. The finding that codebook utilization rate—an information-theoretic property of the tokenizer—is a reliable proxy predictor for downstream zero-shot generalization (100% utilization for FASTerVQ correlating with +12.9% Simpler-Bridge improvement) is an empirically grounded diagnostic link between tokenizer design and policy generalization that may guide future tokenizer development beyond this specific paper.

---

## Suggestions

1. Report per-condition success-rate standard deviations and number of evaluation trials in all tables.
2. Add an explicit table comparing pretraining dataset scale across all baselines.
3. Provide training loss curves and multi-seed statistics to support stability claims.
4. Ablate spacing augmentation and DCT loss independently.
5. Include a cleaner theoretical characterization of when block-wise parallel prediction preserves generative quality vs. when dependencies between action dimensions make it unsafe.

---

## Score and Decision

FASTer is a well-motivated, technically complete, and broadly validated framework that addresses a genuine bottleneck in autoregressive VLA inference. The results are strong across an unusually wide set of benchmarks, and the engineering and conceptual contributions (2D patchifier, RVQ tokenizer with physical grouping, BAR decoding, VRR metric) are individually solid and mutually reinforcing. The major weaknesses—comparison fairness ambiguity, absent statistical significance, and unsubstantiated stability claims—are real but do not undermine the core conclusions, particularly given the magnitude of the speedup on whole-body control and the consistent improvements across backbones and embodiments. This paper provides meaningful, reproducible contributions to the robotics and VLA community.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>