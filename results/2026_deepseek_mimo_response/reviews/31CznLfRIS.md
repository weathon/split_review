## Summary
This paper introduces VideoJudge, a bootstrapped generator-evaluator pipeline for training 3B/7B MLLM-based judge models for video understanding evaluation. The framework synthesizes training data through iterative generation and quality control without human annotation, and additionally trains models to generate instance-specific rubrics at inference time. The paper claims that these small fine-tuned models match or surpass models up to 10× larger across meta-evaluation benchmarks.

## Strengths
- **Novel bootstrapping pipeline with validated data quality**: The generator-evaluator pipeline (§3.1, Algorithm 1) produces training data with monotonic quality degradation confirmed by BERTScore and BLEU metrics (Figure 2, §5.1), and human evaluation on the hardest 2-vs-3 pairs shows 94.8% inter-annotator agreement with Cohen's κ of 89.5 (§5.2). This provides concrete evidence that the bootstrapped supervision signal is reliable.
- **Instance-specific rubric generation is a genuinely novel capability**: VideoJudgeR-3B generates context-specific evaluation rubrics preferred by human annotators over those from models up to 72B parameters (63.9% win rate vs. Qwen-72B, 53.4% vs. GPT-4o-mini, Figure 3), representing a meaningful advance in interpretable evaluation.
- **Strong external benchmark result on LongVideoBench**: VideoJudge-7B achieves the best Δ(C-D) of 1.16, outperforming Qwen2.5-VL-32B (1.08) and 72B (1.06) on Table 1. This is a genuine win on an independently constructed benchmark.
- **Temperature robustness of trained models**: Figure 4 shows VideoJudge maintains or improves Spearman correlation (0.66→0.73) as temperature increases from 0 to 1, while the base Qwen2.5-VL-3B degrades from 0.56 to 0.42. This is a practically valuable property for deployment.
- **Honest error analysis**: The paper transparently reports overestimation bias (14.8% overestimate by ≥2 points vs. 1.5%) and poor mid-range calibration (36.9% accuracy on rating-3, §6.2).
- **Comprehensive evaluation suite**: 4 pointwise and 3 pairwise benchmarks, frame-budget ablation, temperature sensitivity analysis, comparison against both unimodal and multimodal baselines.

## Weaknesses

### Fatal
None.

### Major
- **Self-referential evaluation inflates headline results**: Two of four pointwise benchmarks (VideoJudgeLLaVA-MetaEval and VideoJudgeVCG-MetaEval) are constructed using the same bootstrapping pipeline (Algorithm 1, threshold 0, §4.2 line 106), and two of three pairwise benchmarks (VJ, VJ-H) use bootstrapped responses. On the genuinely external pairwise benchmark VideoAutoArena, Qwen2.5-VL-72B scores 89.80 vs. VideoJudge-7B's 85.49 (Table 3). On VATEX, while VideoJudge-3B achieves best RMSE (1.33) and ECE (0.63), Qwen2.5-VL-32B/72B substantially outperform on PSUP (0.73/0.71 vs. 0.61/0.66, Table 1), a preference consistency metric. The abstract's "three out of four meta-evaluation benchmarks" claim (line 9) counts self-referential benchmarks equivalently to external ones, overstating the evidence for generalization. The paper does acknowledge this "closed-loop" effect in §7, but briefly relative to the severity—the entire evaluation architecture is affected.

- **Generator and evaluator model identities not disclosed in main text**: The paper describes generator G and evaluator E (§3.1, lines 56-66) but never identifies what specific models fill these roles in the main text. Line 52 mentions "strong vision-language models (§A.2)" only for generating dense video descriptions. Without knowing whether G/E are proprietary (cost/reproducibility concerns), or the same Qwen2.5-VL models evaluated as baselines (direct circularity), readers cannot assess the framework's feasibility or the validity of comparisons. This information should be in §3.1, not hidden in an appendix.

### Minor
- **No statistical significance or variance reporting**: All results in Tables 1, 2, 3 are single point estimates. Key model differences are often 1-3 percentage points (e.g., VJ-H: 93.67 vs. 94.51, Table 3), and the pairwise training uses 50% random sampling (§4 line 90). Variance reporting would help determine whether observed differences are meaningful.

- **Rubric evaluation conflates fine-tuning with rubric generation**: Table 2 compares VideoJudgeR-3B (fine-tuned on rubric data) against zero-shot Qwen2.5-VL baselines. While all models "are prompted to produce rubrics together with reasoning and a score" (Table 2 caption), the comparison conflates the benefit of rubric-guided fine-tuning with the benefit of rubric generation per se. A fine-tuned baseline without rubric generation, under identical conditions, would isolate the contribution.

- **"Consistently outperform" wording overstated**: Line 218-219 claims "VideoJudge models consistently outperform their backbone baselines across all benchmarks." While technically true if "backbone baselines" means untrained Qwen2.5-VL-3B/7B, the surrounding text (line 234) claims they outperform "much larger models such as Qwen2.5-VL-32B and 72B in several cases"—the "several cases" are predominantly the self-referential benchmarks and LongVideoBench Δ(C-D), while on VAA and VATEX PSUP the larger models win.

### Trivial
- The abbreviation "FB" in Table 3 headers is defined in the caption but used without context in surrounding body text.

## Nice-to-Haves
- Ablating bootstrapping pipeline components (no feedback, different acceptance thresholds) evaluated on external benchmarks would isolate whether the bootstrapping process itself drives improvements.
- Clearly separating self-referential from external results in Tables 1 and 3 would improve transparency.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Formatting/nitpick issues raised by harsh critic — these are parser artifacts, not author errors.
- Concerns about appendix-stripped content — the appendix likely contains generator/evaluator model details; the core issue is main-text omission, which is captured in the Major weakness above.

## Novel Insights
The paper's most novel contribution is training models to generate instance-specific rubrics at inference time, validated by human preference over rubrics from models 20× larger. This goes beyond prior work that used fixed rubrics or distillation from proprietary judges. The finding that unimodal LLMs (Qwen3) consistently underperform multimodal models on video evaluation—even when given detailed video descriptions—also provides useful evidence for the field on the necessity of video inputs for judging video tasks.

## Suggestions
- Clearly separate self-referential from external benchmark results in Tables 1 and 3; reframe the "three out of four" claim to acknowledge which benchmarks are externally validated.
- Disclose generator and evaluator model identities in §3.1 (main text), not just appendix.
- Add variance estimates (e.g., 3 random seeds, or bootstrap CIs) for key comparisons where differences are small.
- Lean into genuine external wins (LongVideoBench Δ(C-D), VATEX RMSE/ECE) rather than diluting them with self-referential results.

## Calibration Anchors Retrieved
**Round 1 (bracketing):**
- BTr3PSlT0T (Video-LMM eval suite, 3.75) — weaker benchmark-only paper, less novelty
- xYzOkOGD96 (Grounded Video Captioning, 3.83) — different task, weaker contribution
- Z5nqeTH24j (VidEgoThink, 4.40) — benchmark paper with auto-generation pipeline
- wMRFTQwp1d (VideoEval, 4.00) — benchmark paper, rejected
- 87YOFayjcG (JudgeLM rejected, 5.25) — very similar concept (fine-tune LLM judges), less comprehensive
- L4nH3j7L94 (LLaVA-Critic, 4.75) — multimodal judge, rejected as mainly engineering
- xreOs2yjqf (EvalAlign, 4.75) — multimodal evaluation metric, rejected
- gtkFw6sZGS (Generative Judge, 5.33) — generative judge for alignment, accepted with low scores
- xsELpEPn4A (JudgeLM accepted, 7.50) — same concept, stronger results, accepted
- 7xCSK9BLPy (MBR Decoding, 7.33) — uses LLM judges for supervision, accepted
- X1OfiRYCLn (VLB Bootstrapping, 7.50) — vision-language bootstrapping for evaluation, accepted
- Im2neAMlre (T2I Evaluation, 7.33) — evaluation methodology paper, accepted

**Round 2 (narrowing):**
- I7uCwGxVnl (Self-Taught Evaluators, 5.40) — iterative self-improvement for judges, rejected; VideoJudge has more novelty and comprehensiveness
- SpTzsQjgxF (Rule-Based Rating, 5.75) — rule-based data selection, rejected
- m8yby1JfbU (Is Your VLM a Reliable Judge?, 6.50) — video judge reliability analysis, accepted; VideoJudge has a more complete system
- 2rWbKbmOuM (MEGA-Bench, 7.00) — multimodal evaluation benchmark, accepted

**Round 1 bracket**: 5.0–7.0
**Final score determination**: VideoJudge is clearly more novel and comprehensive than Self-Taught Evaluators (5.40, rejected) and LLaVA-Critic (4.75, rejected). It is comparable to "Is Your VLM a Reliable Judge?" (6.50, accepted) but with a more complete system and stronger methodological contributions (bootstrapping pipeline, rubric generation). It falls short of JudgeLM accepted (7.50) and VLB (7.50) due to the self-referential evaluation issue and mixed external benchmark results. Score: 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>