Now I have enough calibration data. Let me construct the final review.

## Summary

This paper introduces VideoJudge, a bootstrapping framework that generates training data for MLLM-based video understanding evaluators without human annotation. The method uses a generator–evaluator pipeline to produce candidate responses across a 1–5 rating scale, iteratively refining them until the evaluator's rating aligns with the target score. The resulting data is used to fine-tune Qwen2.5-VL-3B and 7B models for both pointwise and pairwise evaluation. The paper further introduces instance-specific rubric generation at test time and constructs new meta-evaluation benchmarks. Experiments show that the trained small models achieve competitive pairwise accuracy on human-annotated benchmarks compared to much larger models like Qwen2.5-VL-72B.

## Strengths

1. **Bootstrapping pipeline is a practical contribution to data generation for video judges**: The generator–evaluator loop produces over 100K training examples with automatic quality control. Human evaluation (§5.2) shows 94.8% annotator agreement (Cohen's κ=0.895) and >92% agreement with the gold preference on the hardest 2-vs-3 rating pairs, confirming the data is reliable without manual annotation.

2. **Pairwise results on independent human-annotated benchmarks are strong**: On VideoAutoArena (human ground truth), VideoJudge-7B achieves 85.49 — competitive with Qwen2.5-VL-72B (89.80). On VideoJudge-Pairwise-H (human-annotated 2-vs-3 pairs), VideoJudge-7B reaches 93.67 vs. 72B's 94.51. These benchmarks are independent of the bootstrapping pipeline and demonstrate genuine generalization.

3. **Instance-specific rubric generation works well**: VideoJudgeR-3B achieves Pearson 73.96 and Spearman 74.16, comparable to Qwen2.5-VL-72B (78.10/78.61) while being 24× smaller. Human judges prefer VideoJudgeR-3B's rubrics over GPT-4o-mini (53.4% win rate) and Qwen-72B (63.9% win rate) in Figure 3.

4. **Temperature robustness is convincingly demonstrated**: Figure 4 shows VideoJudge's Spearman correlation stays stable or improves from 0.66 (T=0.0) to 0.73 (T=1.0), while the base model drops from 0.56 to 0.42. This is practically important for reliable evaluation.

5. **Data quality validation via automatic metrics**: Figure 2 shows monotonic degradation of BERTScore (91.1→86.9) and BLEU (11.0→3.0) as the rating gap widens, confirming the generator reliably produces progressively lower-quality responses aligned with the intended rating scale.

## Weaknesses

### Fatal
None.

### Major

1. **Overestimation bias and poor calibration undermine pointwise reliability**: The paper's own error analysis (§6.2) reveals that VideoJudge overestimates scores by ≥2 points in 14.8% of cases (vs. 1.5% underestimation), only 36.9% of rating-3 responses get the correct score, and 81.3% of rating-4 responses are inflated to 5. For a model whose primary function is to evaluate quality, this systematic bias is a significant practical limitation. The paper acknowledges this in Limitations but offers no mitigation or analysis of whether pairwise judgments are robust to it. This does not invalidate the core contribution (the bootstrapping method works as a recipe), but it substantially limits the practical utility of the trained judge for absolute scoring.

2. **Closed-loop meta-evaluation benchmarks partly inflate the performance claims**: The two main pointwise benchmarks (VideoJudgeLLaVA, VideoJudgeVCG) are constructed using the same generator–evaluator pipeline that produced the training data (§4.2: "generating additional responses via our bootstrapping pipeline (Algorithm 1) with threshold 0"). The independent human-annotated benchmarks (VateX, LongVideoBench, VideoAutoArena) tell a more nuanced story — VideoJudge is competitive but does not clearly "outperform" models 10× larger. The paper acknowledges this in §7, and the claims in the abstract are cautiously worded ("outperforms or is on par with"), but the title and contributions section (contribution 3: "match or outperform much larger models") do not sufficiently caveat the benchmark dependence. This is the primary weakness affecting how the paper's contributions should be assessed.

### Minor

1. **Generator and evaluator model identities are not specified**: The methodology (§3) defines G (generator) and E (evaluator) abstractly but never states which specific models they are. This is critical for reproducibility. The appendix reference (§A.2) addresses video descriptions, not G/E. This should be a single sentence in the main paper.

2. **No comparison with fine-tuned baselines**: All large models are evaluated zero-shot. While this is standard practice for judge papers, a comparison with Qwen2.5-VL-7B fine-tuned on the same bootstrapped data (vs. from-scratch training) would help isolate whether the gains come from the bootstrapping data or simply from task-specific fine-tuning. The paper only ablates "with/without feedback" in the pairwise setting, not the data source.

3. **Human evaluation covers only one rating boundary**: The human evaluation (§5.2) is restricted to 250 samples of 2-vs-3 rating pairs. While the high agreement is reassuring, generalizability to other rating boundaries (e.g., 3-vs-4, 4-vs-5) is not shown. This is a minor limitation given the cost of human annotation.

4. **Threshold α for training not specified**: The acceptance criterion α is set to 0 for meta-evaluation benchmarks (§4.2) but its value during training data generation is unclear. The algorithm description (§3.1) defines it but doesn't state the chosen value for the final dataset.

### Trivial
None.

## Nice-to-Haves

- **Train with more frames**: The maxframes analysis (§6.2, Figure 20a) shows training benefits up to ~240 frames, yet the main models are trained with 60 frames. Retraining with more frames would likely improve results.
- **Ablate bootstrapping components**: Comparing training on (a) gold responses only, (b) randomly degraded responses, (c) responses without the acceptance criterion, and (d) full bootstrapped data would isolate the contribution of the iterative refinement loop.
- **Report computational cost**: The bootstrapping pipeline requires many generator/evaluator calls. A rough estimate of API calls or GPU hours would help assess scalability.

## Removed Points

These points were flagged for removal; treat them with caution.

- **Closed-loop being treated as "fatal"**: The harsh critic framed this as a fatal structural issue that invalidates the paper's core claims. However, the paper evaluates on independent human-annotated benchmarks (VateX, LongVideoBench, VideoAutoArena), acknowledges the issue in §7, and the pairwise results on truly independent benchmarks are strong. The closed-loop issue is real but major, not fatal.
- **Missing related works not mentioned** per instructions.
- **Formatting nitpicks and typo concerns** per instructions (parser artifacts).
- **"No comparison with fine-tuned baselines" framed as structural weakness**: This is a standard limitation but not a fatal one. The zero-shot comparison is the norm in judge-model papers and is informative on its own.
- **Strength Finder's generic strengths** (e.g., "addresses an important problem") — removed per instructions as non-specific.

## Novel Insights

The synthesis of the reviews does not produce insights beyond the paper's own contributions. The key tension — that the bootstrapping pipeline produces useful training data while also creating evaluation benchmarks that risk closed-loop effects — is already acknowledged by the authors in §7. The overestimation bias finding is also self-reported. No reviewer raised a pattern not visible in the paper itself.

## Suggestions

1. **Specify G and E models** in §3.1 with a single sentence (e.g., "We use Qwen2.5-VL-72B as both G and E" or whichever models were actually used).
2. **Add a calibration analysis for pairwise judgments**: Show that the overestimation bias does not affect pairwise accuracy, e.g., by analyzing pairwise accuracy stratified by the rating gap.
3. **Retrain with higher maxframes** (e.g., 240) to present the best possible version of the method, or justify why 60 frames was chosen despite the analysis showing benefits up to 240.
4. **Add an ablation on bootstrapping components** to demonstrate that the iterative refinement (not just the expanded data volume) drives the gains.
5. **Relegate closed-loop benchmarks to supplementary** or add a correlation analysis showing they rank models similarly to independent human-annotated benchmarks.

## Score and Decision

**Bracketing (Round 1)**: Low anchors (avg ≤ 3.5) included HumanVideo-MME (2.50), NOAH (3.00), SurveillanceVQA (3.00) — all rejected/withdrawn video benchmark papers. Mid anchors (3.5–7.5) included TIR-Judge (5.50, accepted), CompassJudger-2 (5.00, rejected), Shelf Life of Judges (4.50, accepted), IV-Bench (6.00, accepted), VideoMind (6.50, accepted). High anchors (7.5+) included Generative Universal Verifier (8.00, oral). Initial bracket: **4.5–7.0**.

**Narrowing (Round 2)**: Three additional queries targeted judge-model and video understanding papers:
- TIR-Judge (5.50, accepted poster): Similar contribution type (training small judge models), slightly cleaner evaluation but less novel training method. VideoJudge is comparable or slightly stronger in domain difficulty (video vs. text).
- CompassJudger-2 (5.00, rejected): Similar paper (training judge models), rejected due to domain generalization concerns and marginal novelty. VideoJudge is clearly stronger — cleaner contribution, better evaluation on independent benchmarks, more honest limitation discussion.
- Shelf Life of Judges (4.50, accepted poster): Empirical study rather than method paper. VideoJudge has stronger methodological contribution.
- VideoMind (6.50, accepted poster): Different contribution type (video agent). Comparable evaluation scope and thoroughness.

**Final calibration**: Compared to the most relevant anchor — TIR-Judge (5.50) — VideoJudge tackles a harder domain (video), has comparable evaluation rigor (human eval, temperature robustness, maxframes analysis), but has two notable weaknesses: the closed-loop benchmark concern and the overestimation bias. The core contribution (bootstrapping pipeline) is novel and well-executed. The pairwise results on independent human-annotated benchmarks are genuinely strong. This places the paper above the 5.0–5.5 range but below the 6.5+ range where papers like VideoMind (cleaner evaluation with fewer confounding issues) sit.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>