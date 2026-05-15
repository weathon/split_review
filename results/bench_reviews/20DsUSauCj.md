## Summary

The paper introduces an automated pipeline for extracting *persona vectors*—linear directions in activation space—from natural-language trait descriptions, and demonstrates their utility across four applications: (1) monitoring prompt-induced personality shifts via activation projection, (2) steering behavior at inference time, (3) a novel *preventative steering* method that adds undesired persona directions during finetuning to prevent drift, and (4) pre-finetuning data screening by projecting training data onto persona vectors. Experiments on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct across three traits (evil, sycophancy, hallucination) show strong correlations between persona-vector-projected activation shifts and post-finetuning trait expression (r=0.76–0.97), and demonstrate that preventative steering preserves general capabilities better than inference-time steering.

## Strengths

- **Automated, practical extraction pipeline.** Given only a trait name and description, the pipeline (Section 2) generates contrastive prompts, evaluation questions, and rubrics via Claude 3.7 Sonnet, then extracts a usable persona vector with no manual curation. This lowers the barrier to applying activation-engineering methods to new traits.

- **Finetuning shift correlations are the paper's strongest result.** Figure 4 shows r=0.76–0.97 (p<0.001) between the projection of finetuning-induced activation shifts onto persona vectors and post-finetuning trait expression, across two models and three traits. Cross-trait baselines are lower (r=0.34–0.86), confirming trait-specificity. This provides a mechanistic account of *when* and *how* finetuning changes behavior.

- **Preventative steering is a genuinely novel idea with compelling evidence.** Steering *toward* an undesirable persona direction during training, then removing the intervention at inference, reduces trait expression while preserving MMLU accuracy and new-fact recall far better than inference-time steering (Figures 5 and 6). The fact-acquisition case study (Section 5.2) is particularly clean: preventative steering suppresses hallucination to baseline while degrading new-fact accuracy only slightly, whereas inference-time steering degrades both.

- **Cross-trait and cross-model generality.** Experiments cover three negative traits on two architecturally distinct models (Qwen, Llama). Additional results (Appendix I) extend to four more traits including positive ones (optimism, humor), supporting generality beyond the narrow set shown in the main text.

- **Dataset-level data screening correlations are strong.** Figure 7 reports r=0.88–0.95 (p<0.001) between the projection difference metric computed *before* finetuning and the observed post-finetuning trait expression, suggesting the metric is a useful pre-training signal.

## Weaknesses

### Fatal
None.

### Major

- **Data screening lacks causal validation in the main text.** Section 6 shows that (a) the projection difference metric correlates with post-finetuning outcomes at the dataset level (Figure 7), and (b) trait-inducing and control samples are separable (Figure 8). However, the paper never performs the obvious intervention: actually filter training data by projection threshold, finetune on the filtered set, and measure whether post-finetuning trait expression decreases. The claim that persona vectors "enable fine-grained data filtering" (Section 6.2) is supported only by correlational evidence in the main text. While Appendix N is referenced for validation on real-world datasets, the main text would benefit from at least one direct filtering experiment to substantiate the causal claim.

- **Figure 4 correlations are reported for all datasets combined, not separately for EM-like datasets.** The scatter plots in Figure 4 include explicitly trait-eliciting datasets (Evil II, Sycophancy II, Hallucination II) alongside emergent-misalignment–like datasets (Medical, Code, GSM8K, MATH, Opinions). The paper's central motivation—that persona vectors capture *unintended* shifts—depends on the method working for EM-like datasets that do not explicitly teach the target trait. The paper does not report correlation coefficients restricted to EM-like datasets. If the correlation collapses or weakens substantially without the explicit datasets, the claim about capturing unintended shifts would be unsupported. This analysis must be shown.

### Minor

- **The judge validation is referenced but deferred entirely to the appendix.** The paper states "we validate it by checking agreement between our LLM judge and human evaluators... (see Appendix D)" (Section 2.1), but the main text provides no agreement rates, confusion matrices, or any quantitative indication of judge reliability. Given that every quantitative result depends on this judge, a brief summary in the main text (e.g., "Pearson r=0.XX with human raters") would substantially increase reader confidence. The appendix validation exists in the original submission but is not summarized.

- **The data screening claim is slightly overclaimed in the abstract.** The abstract states "persona vectors can be used to *flag training data* that will produce undesirable personality changes," which is supported by the correlational evidence. However, the term "flag" combined with the broader context implies a validated screening tool, whereas the causal link (does removing flagged data actually prevent unwanted shifts?) remains untested in the main text.

### Trivial
- None of substance.

## Nice-to-Haves

- **Separate EM-only correlation for Figure 4.** A small table reporting r values for the five EM-like datasets only (Medical, Code, GSM8K, MATH, Opinions) for each trait-model combination would directly address whether the method captures unintended shifts.
- **One direct filtering experiment.** Finetuning after removing high-projection (or keeping low-projection) samples and measuring trait expression would complete the data screening story.
- **A brief main-text summary of the LLM judge validation.** A single sentence with an agreement statistic would substantially strengthen the paper's evidential foundation.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Asymmetrical comparison between preventative and inference-time steering"** (Harsh Critic Critical Issue 4): Removed. The critic claims the comparison is unfair because inference-time steering is applied during MMLU evaluation while preventative steering is not. However, this is the intended and meaningful comparison: two end-to-end strategies (intervene at inference vs. intervene during training so inference intervention is unnecessary). Measuring MMLU of the preventatively-steered model *without* inference steering is the correct comparison because that is the practical benefit claimed.

- **"LLM judge validation is missing / deferred entirely"** as a structural flaw: Removed per instructions (parser strips appendices; paper explicitly states validation is in Appendix D). However, noted as a Minor weakness that a summary statistic in the main text would help.

- **"Figure 5 gray dashed line is confusing"**: Removed. The figure description is from a parser-extracted image caption; the actual figure may be clearer. Even if the line is a single reference value, this is at most a visualization nitpick.

- **Within-prompt-type correlations being modest** (raised by critic as a limitation): Not listed as a weakness because the paper itself honestly acknowledges this limitation (Section 3.3: "more modest correlations when controlling for prompt type... may be less reliable for more subtle behavioral changes"), which is transparent reporting rather than a flaw.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a direct filtering experiment.** A simple bar-chart experiment comparing post-finetuning trait expression for: (a) full dataset, (b) dataset filtered to remove high-projection samples, and (c) dataset filtered by an LLM judge baseline. This would directly substantiate the "filtering" claim in Section 6.

2. **Report EM-only correlations for Figure 4.** Create a small table or annotation showing the r-values restricted to the five EM-like datasets (Medical, Code, GSM8K, MATH, Opinions) for each trait-model combination. This would resolve the most serious empirical concern about whether the method captures *unintended* shifts.

3. **Include a main-text summary of judge validation.** Even one sentence (e.g., "GPT-4.1-mini achieves Pearson r=0.XX with human raters on 200 samples") would greatly increase trust in all downstream results.

## Score and Decision

**Calibration anchors** (all from ICLR 2026 human reviews):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `QZvGqaNBlU.md` (PERSONA: activation-space personality control) | 5.00 | Similar topic and methodology but narrower scope (inference-time only); this paper is more comprehensive (finetuning, preventative steering, data screening) and has stronger validation → this paper is stronger |
| `yjrVOxjkDR.md` (Persona Features Control Emergent Misalignment) | 7.50 | Stronger mechanistic analysis via SAEs and clearer causal mediation, but on a narrower phenomenon (emergent misalignment) with proprietary models; this paper has broader practical applications but weaker mechanistic depth → this paper is slightly weaker |
| `q5AawZ5UuQ.md` (Emergent Misalignment is Easy, Narrow Misalignment is Hard) | 5.33 | Comparable breadth and rigor; this paper covers more application areas (monitoring, data screening, preventative steering) → comparable |
| `VsEkWh3mXu.md` (SteeringSafety: steering evaluation framework) | 6.00 | Systematic evaluation framework with less novel methodology; this paper has clearer novel contributions (preventative steering, data screening) → comparable |
| `iD8uUeCBy5.md` (Steering Vector Transfer via Orthonormal Transformations) | 2.50 | Weak evaluation (cosine similarity only, no behavioral validation); this paper has much stronger empirical evidence → this paper is much stronger |
| `cN1QlgqORs.md` (Impatient Users Confuse AI Agents) | 3.50 | Narrower scope, weaker baselines, similar activation-steering methodology; this paper has better experiments and broader validation → this paper is stronger |
| `X5YiG1YXVT.md` (Accidental Vulnerability: Fine-Tuning Safety) | 2.00 | Weak methodology, unclear claims; this paper is substantially better in all dimensions → this paper is much stronger |

**Score reasoning**: The paper contributes an automated pipeline for extracting persona vectors, demonstrates strong correlations between activation shifts and finetuning-induced trait changes (r=0.76–0.97), and introduces the novel preventative steering method with clean evidence. The main weaknesses are (a) the data screening application is correlational rather than causally validated in the main text, and (b) correlation results are not broken down by dataset type to verify the method captures unintended shifts. These are addressable limitations, not fundamental flaws. Relative to the calibration set, the paper sits above purely inference-time activation steering papers (PERSONA, avg 5.0) but below deeply mechanistic work on emergent misalignment (avg 7.5). The contributions are substantial, the experiments are thorough, and the weaknesses are clearly scoped.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>