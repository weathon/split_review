Now let me synthesize everything into the final consolidated review.

## Summary

This paper proposes the Language Confusion Gate (LCG), a lightweight MLP that operates at decoding time to mask tokens from disallowed language families, trained via norm-adjusted self-distillation using the base model's own debiased predictions. The key contributions are: (1) a mechanistic analysis showing that token embedding norm bias contributes to language confusion, (2) a practical plug-in intervention that intervenes on <0.4% of tokens with negligible latency overhead, and (3) strong empirical results across Qwen3, Llama3.1, Gemma3, and GPT-OSS showing substantial confusion reduction (e.g., CJ confusion from 1.0%→0.0%, Latin confusion from 4.4%→0.4% on Qwen3-30B) while maintaining task performance.

## Strengths

- **Order-of-magnitude confusion reduction across multiple model families and sizes.** Table 3 shows LCG reduces CJ and Latin confusion substantially across Qwen3-8B, Qwen3-30B, Llama3.1-8B, Gemma3-12B, and GPT-OSS. The reductions are consistent across both standard (no-think) and reasoning (thinking) modes (Tables 3, 4), spanning translation, QA, and code generation tasks.

- **Norm-adjusted self-distillation ablation cleanly validates the mechanistic insight.** The comparison between LCG-unadjusted and LCG-adjusted (Table 3) directly shows that training with norm-debiased pseudo-targets produces better gates, e.g., Llama3.1-8B Latin confusion drops from 5.7% to 2.9%. This is a controlled ablation that supports the core technical claim of Section 3.2.

- **Extremely low computational overhead in a production setting.** Section 6 reports that LCG adds only 0.4% to per-step generation time (15.95ms vs 15.99ms), making it practical for deployment. The intervention rate of 0.33–0.38% of tokens confirms the sparse intervention design.

- **Analysis-driven design grounded in concrete observations.** The paper motivates the approach with three findings (Section 3): confusion is rare, correct tokens appear in top-3 99.29% of the time, and token embedding norms are biased toward high-resource languages (Table 1: Low-Res tokens are only 0.14% of top-norm tokens in Qwen3-8B). These observations directly inform the gate design and training targets.

- **Code-switching preservation is explicitly evaluated.** The token-level evaluation (86.7% of human-validated code-switch points preserved) and the FLORES-WITH-LATIN analysis (Table 5) show the paper directly addresses the tension between suppressing confusion and preserving legitimate mixing.

## Weaknesses

### Fatal
None.

### Major
None. All identified issues are addressable and do not threaten the paper's core claims.

### Minor

1. **"Order of magnitude" claim overstates reductions for some models.** While the claim holds for Qwen3-30B (1.0%→0.0%, 4.4%→0.4%) and Qwen3-8B, it is less accurate for Gemma3-12B where CJ confusion goes from 0.2%→0.1% (2×) and Latin from 1.0%→0.5% (2×). The paper should qualify this claim by model.

2. **Latin confusion metric has a known but unquantified blind spot.** The FLORES-NO-LATIN subset flags any Latin character as erroneous. The paper acknowledges this design choice and provides FLORES-WITH-LATIN analysis as a counterbalance. However, the headline reduction numbers—especially the 4.4%→0.4% and 12.1%→2.0% figures—are stated without caveat about potential false positives from legitimate technical terms (e.g., "Python", "iPhone") that a model might naturally introduce where the ground-truth reference does not. The separate code-switch preservation analysis partially addresses this, but the core metric is not tightened to exclude this concern.

3. **ORPO baseline lacks sufficient implementation detail for a fair comparison.** The paper reports ORPO results (Figure 3) as a key training-based baseline but provides no hyperparameters (β, learning rate, epochs), validation strategy, or evidence of hyperparameter search. The statement "synthesize samples with language confusion as rejected samples similar as Lee et al. (2025)" is too vague. While this does not undermine LCG's overall case (which is supported by multiple baselines including ICL and greedy), the ORPO comparison specifically is not yet rigorous enough to support the claim that LCG "outperforms training-based methods."

4. **Code-switch preservation analysis lacks annotation rigor.** The 86.7% figure is based on human annotation, but the paper reports no details: number of annotators, inter-annotator agreement, number of examples annotated, or whether annotation was blind. "Natural, appropriate code-switch" is inherently subjective, and without these details the reliability of the figure is unclear.

5. **Intervention rule thresholds lack sensitivity analysis.** The safety thresholds in Rule (2) (top-k=5, top-p=0.999; top-k=20, top-p=0.95) are presented without justification or ablation. A Pareto-style analysis showing how varying these thresholds affects the trade-off between confusion reduction and code-switch preservation would strengthen the paper.

6. **FLORES-NO-LATIN split ratio not reported.** The paper partitions FLORES+ into two subsets but does not state how many examples fall into each. If FLORES-NO-LATIN is small, the confusion rate estimates could be noisy. This is a straightforward reporting gap.

7. **"Not much lower than the ground-truth answer rate" is a stretch for some models.** The paper states that post-intervention code-switch rates (e.g., Qwen3-8B: 25.90%) are "not much lower" than the ground-truth answer rate (38.36%). A 12-percentage-point gap is substantial; the framing should be more measured.

### Trivial
None.

## Nice-to-Haves

- **Broader evaluation benchmarks.** Testing on general-purpose benchmarks (e.g., multilingual MMLU, reasoning tasks with non-English prompts) would strengthen the "no degradation" claim, though the paper already covers translation, QA, and code generation domains where LCG is designed to intervene.

- **Quantify the fraction of confusion attributable to norm bias.** The paper shows norm-adjusted training helps (Section 3.2, ablation) but does not decompose confusion events into those caused vs. not caused by norm bias. This would contextualize the benefit of the norm adjustment component.

- **Results on the Language Confusion Benchmark (LCB).** The paper provides a reasoned justification for not using LCB (code-switching contamination, detector accuracy). However, even with caveats, reporting filtered LCB results would improve comparability with prior work. The current self-constructed subsets of FLORES and INCLUDE are reasonable but create an evaluation that is not directly comparable to existing literature.

- **Per-language breakdown of confusion rates.** The results aggregate target languages (Arabic, Hebrew, Korean, Thai, Chinese). Showing per-language confusion rates would reveal whether LCG works uniformly across languages.

- **Qualitative failure case analysis.** The paper shows only success cases. Examples where LCG incorrectly masks valid code-switching (false positives) or misses confusion (false negatives) would provide useful insight for practitioners.

## Removed Points

- **LCB absence as a core weakness** — The paper explicitly explains why LCB was not used (code-switching contamination and detector unreliability). This is a design choice with a stated rationale, not a gap. Removed as already addressed.

- **Pseudo-target quality concern ("oracle experiment would strengthen")** — The ablation of LCG-unadjusted vs LCG-adjusted is precisely the experiment that validates the pseudo-target quality. Removed as already addressed by existing evidence.

- **"No negative impact on task performance" is narrow** — The paper's claim is contextualized within the tasks evaluated (translation, QA, code generation). The benchmarks tested are directly relevant to where LCG intervenes. The request for MMLU/GSM8K is reasonable as a nice-to-have but over-weighted as a weakness.

- **General-purpose benchmark gap as "serious"** — Same as above; downgraded to Nice-to-Have.

## Novel Insights

The reviews surface an important tension that the paper acknowledges but does not fully resolve: LCG operates at the script-family level (CJ, Latin, Symbols, Low-Res), which means it cannot distinguish between, e.g., English and Spanish within the Latin family. The paper correctly frames this as a limitation. More subtly, the norm analysis reveals that the *same* mechanism (embedding norm bias) that causes high-resource confusion also creates a partial signal for debiasing—the norm-adjusted logits re-rank tokens toward correct-language candidates. This dual nature of the norm bias (cause of confusion *and* source of training signal) is an interesting observation that the norm-adjusted self-distillation cleverly exploits, but the paper does not explore how far this self-correction can be pushed before the pseudo-targets degrade. A deeper insight is that the gate's 0.33–0.38% intervention rate implies that language confusion is a sparse phenomenon even in confused models, which raises the question of whether the remaining 99.6% of un-intervened tokens could still carry latent confusion that happens to not surface due to tokenizer/decoding artifacts.

## Suggestions

1. Add a sensitivity analysis for the intervention rule thresholds (top-k, top-p values in Rule 2) with a Pareto curve showing the confusion-vs-code-switching trade-off.
2. Report FLORES-NO-LATIN/FLORES-WITH-LATIN split sizes and confidence intervals or bootstrap estimates for confusion rates.
3. Provide ORPO hyperparameters and validation details; alternatively, compare against a published ORPO checkpoint.
4. Add per-language confusion breakdowns and qualitative failure examples.
5. Include annotator details (count, agreement, procedure) for the human evaluation supporting the 86.7% figure.
6. Soften the "order of magnitude" and "not much lower" claims to match the actual per-model numbers.

## Score and Decision

**Calibration anchors (all from retrieval batch):**

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fSbPwHjdDG.md` (avg 3.00) — "Llamas think in English": poorly organized, controversial intervention methodology, single narrow task. The current paper is substantially stronger (cleaner method, more evaluation, practical contribution).

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KBixkDNE8p.md` (avg 3.00) — "Mind Scramble": gimmicky psychology-based approach with weak methodology. Current paper is far more rigorous.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4y3GDTFv70.md` (avg 3.25) — "Latent Space Theory": theoretical paper with limited empirical validation. Current paper has stronger empirical grounding.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uOnElfFuey.md` (avg 3.00) — "Recovering Knowledge": very narrow scope (regular languages). Current paper addresses a broader, more practical problem.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eznTVIM3bs.md` (avg 5.25) — "Babel Tower": interesting hypothesis about multilingual evolution in code LLMs, but limited to programming languages and has unclear methodology. Current paper has clearer empirical methodology and broader model coverage.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BCyAlMoyx5.md` (avg 5.67) — "Crosslingual Capabilities": solid analysis of crosslingual knowledge barriers but limited language diversity and somewhat expected findings. Current paper has stronger novelty (practical method + mechanistic insight).

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NCrFA7dq8T.md` (avg 6.60) — "The Same but Different": clean mechanistic interpretability, strong execution, but limited to 2 languages and 2 tasks. Current paper has broader practical scope and model coverage, though slightly less polished execution.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/HMa8mIiBT8.md` (avg 6.00) — "Knowledge Cross-Lingually Consistent": solid analysis paper on cross-lingual consistency with some methodological concerns. Comparable in quality to the current paper.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7xCSK9BLPy.md` (avg 7.33) — "Better Instruction-Following Through MBR": strong, well-executed decoding paper with clean evaluation. The current paper has a similar practical-engineering flavor but slightly rougher evaluation edges.

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uZ5K4HeNwd.md` (avg 7.00) — "Beyond Auto-Regression": strong diffusion distillation paper with thorough ablations. Current paper is comparable in contribution level but has more minor evaluation gaps.

**Overall assessment:** The paper makes a real contribution: a practical, lightweight, analysis-motivated solution to a problem that affects deployed multilingual systems. The norm-adjusted self-distillation training is a genuine technical contribution, and the evaluation spans an appropriate range of models and tasks. The weaknesses are all in reporting detail and evaluation polish, not in the validity of the core method. The paper is clearly above the acceptance threshold.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>