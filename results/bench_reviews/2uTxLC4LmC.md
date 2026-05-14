Now I have all the information I need. Let me write the final review.

## Summary

This paper identifies and addresses the problem of unsafe intermediate reasoning in Large Reasoning Models (LRMs), showing that existing safety alignment methods leave harmful content in chain-of-thought reasoning even when final responses appear safe. The authors systematically analyze safety dynamics during reasoning—identifying "safety triggers" (critical steps that consolidate safe reasoning) and "compliance cues" (steps that strongly correlate with unsafe continuations)—and propose **Intervened Preference Optimization (IPO)**, which replaces compliance cues with sampled safety triggers to construct preference pairs and applies partial DPO from the divergence point. Evaluated on three LRMs across jailbreak and adversarial safety benchmarks, IPO achieves consistent improvements in reasoning safety (e.g., DS-8B reasoning harmfulness on WildJailbreak drops from 82.4% to 23.4%) while preserving reasoning capabilities and demonstrating substantial efficiency gains over RL-based alternatives like GRPO.

## Strengths

- **Clear problem identification with compelling evidence.** Section 2.2 systematically demonstrates that existing SFT-aligned LRMs (RealSafe, STAR) still exhibit high harmful ratios in reasoning (e.g., RealSafe-7B: 52.2% reasoning harmfulness vs. 2.4% response harmfulness on WildJailbreak, Figure 2). The paper further shows that safe reasoning strongly correlates with safe responses (only 0.1%–0.6% of cases have safe reasoning but unsafe responses, Figure 3), establishing reasoning-level safety as a distinct and practically important alignment target.

- **Principled diagnosis of why RL-based process supervision fails.** The analysis of GRPO rollout diversity (Figure 4) shows that ~36% of harmful prompts yield zero safe trajectories, and ~50% yield few or none, providing a clear mechanistic explanation for why rewarding safe reasoning directly is insufficient. This diagnosis directly motivates the IPO intervention strategy.

- **Consistent and substantial safety improvements across models and benchmarks.** IPO achieves the lowest average reasoning harmfulness on DS-8B (15.3%), DS-7B (18.4%), and Qwen3-8B (13.9%), outperforming SFT-based methods (STAR: 22.6% on DS-8B) and GRPO (18.5% on DS-8B). The gains hold across diverse adversarial benchmarks (JailbreakBench, StrongReject, WildJailbreak) with three distinct model families, demonstrating robustness.

- **Preservation of reasoning capabilities.** IPO achieves the highest average reasoning accuracy across AIME, MATH, GPQA, and HumanEval for DS-8B (68.5%) and DS-7B (71.5%), surpassing both base models and all safety baselines. The KL divergence analysis (Figure 7) confirms targeted changes only at safety-critical tokens rather than broad distributional shift.

- **Efficiency advantage over RL-based alignment.** IPO requires at most 14 generations per prompt vs. GRPO's 40+, and training completes in ~40 minutes vs. 2+ hours, while achieving better safety. This is a practical advantage for real-world deployment.

- **Ablation studies validate key design choices.** Experiments confirm robustness to compliance cue detector choice (Table 3), and show that partial DPO from divergence points outperforms both SFT and full-trajectory DPO—directly supporting the paper's reward-shaping analogy.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by evidence.

### Minor

- **Figure 6 reports identical harmful ratios across three different safety triggers.** The table (lines 178–185) shows exactly the same values (100, 60, 40, 25, 18, 15) for all three trigger sentences across all five intervention iterations. While it is plausible that different safety triggers produce broadly similar steering effects (all are from the same pool of effective triggers), exact identity at every iteration is suspicious and suggests either a presentation artifact (e.g., the trigger-specific columns mistakenly duplicating the average column) or aggregation that obscures per-trigger variation. The paper should clarify whether these are actual per-trigger results or a formatting issue. Note that even if the numbers are rounded, this does not undermine the paper's core claim—the intervention clearly reduces harmfulness regardless—but the lack of clarity should be corrected.

- **Safety dynamics analysis (Sections 3.1–3.2) is based on only 30 prompts.** The identification of safety triggers, compliance cues, and their correlation (Pearson R=0.85) is conducted on a small sample from JailbreakBench. While the paper extends the analysis qualitatively to Qwen3-8B (Figure 10 in the appendix), the sample size limits the generality of the claimed patterns. A larger-scale validation (e.g., 100+ prompts across multiple benchmarks) would strengthen the empirical foundation for the method's motivation.

- **No confidence intervals or significance tests for main results (Table 2).** The paper reports point estimates without variance, making it difficult to assess whether improvements are statistically reliable, especially for close comparisons (e.g., IPO vs. STAR on DS-8B reasoning safety: 15.3% vs. 22.6%, or IPO vs. GRPO reasoning accuracy on DS-8B: 68.5% vs. 68.3%). This is a common limitation in safety evaluation papers, but reporting bootstrapped confidence intervals would improve evidential strength.

- **The training dataset for Qwen3-8B is notably small (520 examples).** The paper notes varying dataset sizes and should discuss whether this affects the results, as smaller datasets may limit generalization.

### Trivial

- The text description of the line graph in Figure 6 mentions "three different trigger" lines, but the table reports every column as identical. The mismatch between the visual description (three lines differing somewhat) and the tabular data (identical) needs editorial alignment.
- The GRPO exploration in Table 1 is only shown for DS-8B. While understandable as a diagnostic, noting this scope limitation early would help.

## Nice-to-Haves

- **Larger-scale validation of safety dynamics (Sections 3.1–3.2).** Repeating the CSR/compliance cue analysis on 100+ prompts across different benchmarks would confirm the generality of the identified patterns and strengthen the paper's motivation.
- **Confidence intervals or bootstrap estimates for Table 2 results.** This would help assess the reliability of close comparisons.
- **Qualitative examples of IPO-generated reasoning traces** showing before/after intervention would help readers build intuition for the method's effect.

## Removed Points

- *"Suspiciously identical intervention results as a potential evidential issue that undermines the core empirical motivation for IPO"* — This overstates the severity. Even if the numbers are genuinely identical across triggers, the paper's core claim is that intervention *works*, not that different triggers produce differential effects. Identical performance across triggers could indicate robustness. The issue is one of clarity/transparency, not a fatal evidential flaw.
- *"The GRPO results in Table 1 are only for DS-8B"* — Minor completeness point noted in Trivial. Table 2 already includes GRPO results for all three models as baselines. The exploratory analysis in Table 1 is naturally scoped.
- *"Missing parts about multi-turn and agentic scenarios"* — The paper explicitly scopes these as future work in the conclusion. Criticizing their absence is scope creep.
- *Any formatting, typo, or missing appendix complaints* — These are parser artifacts, not author errors.

## Novel Insights

Beyond the paper's own contributions, the most interesting cross-review observation is that the paper's core identification of safety triggers and compliance cues aligns with and extends a growing body of work showing that LRM safety is concentrated in specific reasoning steps rather than distributed uniformly (cf. concurrent findings on "refusal cliffs" and "self-jailbreaking" mechanisms). The paper's insight that compliance cues can be surgically replaced with safety triggers—and that this yields effective training signals—offers a methodological twist on standard preference optimization that goes beyond simply labeling whole trajectories as safe/unsafe. The partial DPO formulation (training only from the divergence point) is a clean operationalization of the reward-shaping insight that may have broader applicability beyond safety.

## Suggestions

1. **Clarify Figure 6.** Provide per-trigger results (even if similar) rather than duplicating the average column, or explain if this is a formatting error. A simple variance bar or annotation explaining that all three triggers produce comparable results (with actual per-trigger values) would resolve the concern.
2. **Expand the safety dynamics analysis to a larger prompt set** (100+ prompts) in a revised version, or at minimum provide a clear caveat about the sample size.
3. **Consider adding bootstrapped confidence intervals** for the key comparisons in Table 2 to strengthen the reliability of the reported improvements.
4. **Include one or two full qualitative examples** of IPO-corrected reasoning traces in the main paper—this would significantly improve reader understanding of the method's behavior.

## Score and Decision

### Calibration Anchors (Batch Retrieval Results)

| Paper | Avg Score | Comparison |
|---|---|---|
| SafeRBench (m4VAwxLMqt) | 3.50 | Benchmark paper without novel methodology; much weaker than current paper |
| Beyond Safe Answers (3azDaaAYzb) | 3.50 | Diagnostic benchmark paper with limited actionable method; weaker |
| Bag of Tricks (DjKPlFEnCk) | 3.50 | Attack-focused paper; narrower contribution |
| Self-Jailbreaking (akbtPEZnDZ) | 5.50 | Phenomenon discovery with simple SFT mitigation; similar topic but less complete solution; current paper has stronger method and evaluation |
| AdvChain (mIe17L3kWn) | 5.00 | Similar type (LRM safety method), but analysis controversial per reviewer concerns; current paper stronger on evidence |
| SaFeR-VLM (8fswQTV8Dp) | 5.00 | Multimodal safety method with comparable ambition but rejected; current paper has more rigorous evaluation |
| When Thinking Backfires (GpL66XgjjF) | 6.67 | Mechanistic analysis with no mitigation method; different contribution type, similar quality tier |
| Output Supervision Can Obfuscate (JTX0iqxBjk) | 7.00 | Theoretical analysis of CoT monitoring; narrower scope, higher theoretical depth |
| SafeDPO (PJdw4VBsXD) | 6.50 | Simpler constrained-DPO method with theoretical guarantees; comparable acceptance tier |
| Superficial Safety Alignment (9yS40pO1RF) | 4.50 | Hypothesis paper with limited evaluation; weaker than current paper |

The paper is clearly above the 4–5 score band (reject/withdrawn papers). It compares favorably with accepted LRM safety papers at the 5.5–6.5 level: it has a more complete methodological contribution than Self-Jailbreaking (5.50), stronger empirical evaluation than AdvChain (5.00), and more practical impact than When Thinking Backfires (6.67—which only diagnoses but does not mitigate). The main issues (Figure 6 clarity, 30-prompt sample, no confidence intervals) are minor presentation and scope limitations, not threats to validity. The paper sits comfortably at the level of accepted poster papers with clear practical contributions.

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**