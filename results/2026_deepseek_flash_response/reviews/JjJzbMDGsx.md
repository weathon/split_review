Now I have enough calibration info. Let me write the final review.

## Summary
This paper introduces Language Confusion Gate (LCG), a lightweight plug-in MLP that reduces language confusion in multilingual LLMs by predicting permissible language families at each decoding step and masking disallowed tokens. The key methodological contribution is norm-adjusted self-distillation, which leverages the discovery that output token embedding norms are systematically larger for high-resource languages (Table 1), creating a logit bias. LCG achieves substantial confusion reduction (e.g., Qwen3-30B CJ 1.0%→0.0%, Latin 4.4%→0.4%) with negligible overhead (0.4% latency increase, ~0.35% intervention rate) while preserving legitimate code-switching in most cases (86.7% token-level allowance).

## Strengths
- **Mechanistic discovery of output token embedding norm bias (Section 3.2, Table 1).** The paper identifies and quantifies that high-resource language tokens dominate the top 5% of embedding norms (e.g., CJ tokens at 10.74% vs. random expectation ~4% in Qwen3-8B), while low-resource tokens are severely underrepresented (0.14%). This geometric insight into *why* language confusion occurs is novel and goes beyond prior work, and it directly motivates the norm-adjusted self-distillation training procedure. This analysis stands independently as a contribution.

- **Order-of-magnitude confusion reduction with preserved task performance (Table 3).** On FLORES-NO-LATIN, LCG-adjusted reduces CJ confusion from 4.5%→0.1% (Qwen3-8B) and Latin confusion from 8.4%→2.9% (Llama3.1-8B), while BLEU scores remain stable. On INCLUDE, accuracy is maintained within ~1 point. No baseline method (ICL, greedy decoding, ORPO) achieves this combination of confusion reduction and task preservation — ORPO degrades INCLUDE accuracy by 4.1 points on Qwen3-8B (61.4→57.3).

- **Norm-adjusted ablation validates the core methodological claim (Table 3).** The controlled comparison between LCG-unadjusted and LCG-adjusted shows consistent improvement from norm adjustment across all model/language combinations (e.g., Llama3.1-8B Latin: 5.7%→2.9%), directly confirming that norm-debiasing the self-distillation targets produces a more accurate gate.

- **Extremely lightweight intervention with quantified efficiency (Section 5.3, Section 6).** LCG intervenes on only 0.33–0.38% of generated tokens and adds 0.4% per-step latency (15.95ms→15.99ms). These concrete efficiency numbers make a strong case for practical deployability.

- **Cross-architecture validation.** Evaluated on five model families (Qwen3-8B/30B, Llama3.1-8B, Gemma3-12B, GPT-OSS) in both "thinking" and "no-think" modes (Tables 3, 4), showing consistent effectiveness across diverse architectures.

## Weaknesses

### Major
- **Missing comparison against the most directly relevant plug-in baselines.** The paper discusses Nie et al. (2025) and Ji et al. (2025) in Related Work — both propose plug-in, no-retraining interventions for language confusion, which is *exactly* the category LCG claims to improve. Nie et al. suppresses language-switching neurons; Ji et al. applies post-hoc smoothing to suppress Chinese tokens in Korean generation. Neither is evaluated. The paper compares instead against ICL (a prompting method ill-suited to this task), greedy decoding, and ORPO (a retraining method). This means the paper's central claim — that LCG is an effective plug-in intervention relative to existing plug-in interventions — cannot be assessed. The reader cannot tell whether LCG improves over the state-of-the-art in its own category.

- **Complete absence of statistical reporting.** All confusion rates, BLEU scores, and accuracy figures are reported as point estimates with no confidence intervals, standard deviations, or significance tests (confirmed by grep). This is particularly consequential because many headline confusion rates are near zero (0.0%, 0.06%, 0.11%, 0.4%) — the difference between 0.06% and 0.00% (Table 4, GPT-OSS CJ%) or 0.1% and 0.0% (Table 3, Qwen3-30B CJ%) could easily fall within sampling noise, especially given how rare confusion events are. Without variance estimates, the reader cannot assess which differences are meaningful.

### Minor
- **Code-switch over-suppression is understated.** On FLORES-WITH-LATIN, LCG reduces code-switch rates substantially below the ground-truth answer rate (e.g., Qwen3-8B: 46.34%→25.90%, vs. answer rate 38.36% — a 12.5 percentage-point drop below the natural rate). The paper frames this as acceptable by comparing to Claude Sonnet 4 (23.29%), but Claude Sonnet 4 is an arbitrary reference, not a ground truth. The token-level analysis (86.7% allowance) evaluates only cases where the model *already* produced a natural code-switch, which is a best-case selection. A per-response analysis of how many responses lose all legitimate code-switches would be more informative.

- **"Order of magnitude" claim is overstated for some model/dataset combinations.** The Abstract claims confusion is reduced "often by an order of magnitude," but this does not hold uniformly. For Gemma3-12B, CJ confusion goes from 0.2%→0.1% (2×) and Latin from 1.0%→0.5% (2×). For Llama3.1-8B, Latin goes from 8.4%→2.9% (2.9×). The claim works for some cells (Qwen3-30B Latin 4.4%→0.4%, 11×) but should be qualified.

- **"LCG-adjusted consistently achieves better performance" is contradicted on INCLUDE accuracy.** On Qwen3-8B, LCG-unadjusted accuracy is 62.84 vs. LCG-adjusted 61.76; on Qwen3-30B, 71.55 vs. 70.83. While LCG-adjusted consistently improves *confusion rates*, the accuracy comparison shows LCG-unadjusted sometimes performs better, contradicting the broader phrasing.

- **The gate's own accuracy (precision/recall) is not analyzed.** The paper reports downstream confusion reduction but never measures whether gate errors are primarily false positives (masking correct tokens) or false negatives (missing confusion). This makes it harder to diagnose failure modes.

- **No per-language breakdown of confusion reduction.** The evaluation aggregates across Arabic, Hebrew, Korean, Thai, etc. Some languages may benefit substantially more than others, and reporting per-language results would reveal the method's boundaries.

### Trivial
- **Table 4 caption error.** The caption reads "Effectiveness of LCG Intervention on 'No-Think' Models measured on Humaneval-XL" but the table describes thinking-model results on Humaneval-XL. Clear copy-paste error.

## Nice-to-Haves
- Sensitivity analysis for the intervention rule parameters (top-k=5/top-p=0.999, etc.) would be useful, though the "No Rule" ablation already shows LCG works without them.
- Analysis of whether the Section 3.1 finding (correct-language token in top-3 99.29% of the time) holds for models beyond Qwen3-8B.
- Justification for why the same gate training data works for both thinking and no-think models.
- Specification of the k/p values used to generate self-distillation pseudo-targets.

## Removed Points
These points are flagged to be removed, treat them with caution:
- "GPT-OSS not being a standard identifier" — Removed per the hard rule: cited models/tools are assumed to exist.
- Criticism about reproducibility of cited models/references — Removed per hard rules.
- Various formatting/style nitpicks — Removed per hard rules about parser artifacts.
- "Section 3.1 statistic only for Qwen3-8B" — Weakened to nice-to-have since the paper is transparent about the model used; the finding is a motivation, not a claim of universality.
- "No sensitivity analysis for rule parameters" — Weakened to nice-to-have since "No Rule" ablation provides evidence of robustness.
- "Same training data for thinking and no-think" — Weakened to nice-to-have since it's a reasonable engineering choice.
- Various generic strength claims from Strength Finder (e.g., "this paper addresses an important problem") — Removed as generic/superficial.
- The criticism that the paper "cannot be independently verified" — Removed per hard rule.

## Novel Insights
None beyond the paper's own contributions. The calibration anchors reveal that the paper occupies a familiar position for multilingual LLM work: a cleanly motivated idea with a genuine insight (the norm bias analysis), but evaluation gaps — particularly missing the most relevant baselines and lacking statistical reporting — that prevent the paper from making a fully persuasive case at a top venue. This pattern is common in the 4.5–6.0 score range.

## Suggestions
1. **Implement and compare against Nie et al. (2025) and Ji et al. (2025)** as baselines. These are the directly competing plug-in methods and must be included to substantiate the claim of state-of-the-art plug-in intervention.
2. **Add bootstrapped confidence intervals** (e.g., 95% CI) for all confusion rates, especially the near-zero ones. This is critical for the reader to assess whether differences like 0.06%→0.00% are meaningful.
3. **Provide per-response code-switch analysis** to quantify what fraction of responses lose all legitimate code-switches under LCG, supplementing the existing token-level analysis.

## Score and Decision
**Calibration Details:**

**Round 1 — Bracketing.** Searched for papers on related topics (language confusion, multilingual LLM intervention, plug-in decoding) across three score bands.

*Low band (avg < 3.5):* Papers scoring 2.5–3.4 (EfficientSkip 2.5, Llama English intervention 3.0, DLP-LoRA 3.0, GTD-LLM 3.4). All rejected. These papers are substantially weaker — they lack clear mechanistic insights or have more fundamental methodological flaws. Our paper is clearly stronger.

*Middle band (3.5–7.5):* XTransplant (4.75, Reject), Babel Tower (5.25, Accept), Crosslingual Capabilities (5.67, Reject), TransLLM (6.25, Reject), Scaling Laws (5.25, Reject). Our paper fits here — it has genuine contributions but also significant evaluation gaps.

*High band (avg > 7.5):* Papers scoring 8.0 (DEPT, Combatting Dimensional Collapse, Self-Alignment, Interpolating Diffusion). These are pre-training/data/methodology papers with fundamentally different scope and rigor levels. Our paper is not in this band.

**Round 2 — Narrowing (4.5–7.5).** Read full reviews of Crosslingual Capabilities (5.67), TransLLM (6.25), Babel Tower (5.25), and XTransplant (4.75). Our paper is stronger than XTransplant (which had a methodological flaw of reporting upper-bound as main result) and comparable to Crosslingual Capabilities (both have evaluation limitations but genuine insights). It is weaker than TransLLM (6.25) in terms of evaluation completeness, though our paper has a novel mechanistic discovery that TransLLM lacks.

**Final Bracket:** 4.5–5.5 → Final Score: **5.0**

**Decision:** Reject

The paper has a genuine contribution in the norm bias analysis and a cleanly engineered method. However, the missing comparison against the most directly relevant plug-in baselines (Nie et al. 2025, Ji et al. 2025) and the complete absence of statistical reporting are significant evaluation gaps that prevent the central claims from being fully substantiated. A revised version addressing these issues could be a solid contribution.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>