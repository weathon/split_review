## Summary

This paper investigates whether multimodal foundation models (GPT-4o, Gemini 1.5 Pro, and two open-weights models) benefit from in-context learning at scale — from few-shot (<100 examples) up to ~2,000 demonstrating examples. The authors benchmark across 14 datasets spanning image classification, VQA, and object localization, finding that Gemini 1.5 Pro's performance generally improves log-linearly with more examples while GPT-4o exhibits less stable (V-shaped) scaling. The paper also explores query batching to reduce per-query cost and latency, and introduces an "ICL data efficiency" metric to compare how quickly models learn from additional demonstrations.

## Strengths

- **Comprehensive, multi-domain benchmark with 14 datasets across 4 domains and 3 task types.** The paper goes beyond classification-only benchmarks to include VQA (RSVQA, VQA-RAD) and object localization (DIOR, DeepLesion) — a genuine extension beyond prior text-only many-shot ICL work (Li et al. 2023, Agarwal et al. 2024). This breadth directly supports the claim that many-shot ICL generalizes across diverse multimodal settings.

- **Well-executed mechanistic ablation of zero-shot batching improvements.** The decomposition into domain calibration (+3.0% on TerraIncognita), class calibration (+3.5%), and self-ICL (+5.5%) on two datasets (Section 5.2, Figure 4) goes beyond reporting the phenomenon to explaining *why* batching helps. This is the most insightful analysis in the paper.

- **Prompt-robustness verification.** The paper explicitly tests sensitivity to different prompt wordings on two datasets and confirms the log-linear improvement trend is consistent (Section 4), addressing a well-known fragility concern in ICL research.

- **Concrete cost/latency analysis with real API pricing.** Section 5.3 reports measured latency and dollar costs using actual Gemini 1.5 Pro preview pricing, showing practical feasibility (35× latency reduction on HAM10000, 45× cost reduction on TerraIncognita with batching).

- **Controlled experimental design.** Class-stratified sampling for demo and test sets, temperature=0 with reruns on abstention, bootstrapped error bars with 1,000 replicates — these methodological choices strengthen confidence in the scaling curves.

## Weaknesses

### Fatal
None.

### Major

- **The ICL data efficiency metric is computed via a log-linear regression that is inappropriate for GPT-4o's V-shaped scaling curves, and the cross-model comparison is confounded by different shot ranges.** The paper observes that GPT-4o "performance drops sharply at first and then improves significantly" (V-shaped curves) on multiple datasets (Section 4, line 147). Fitting a log-linear regression through the zero-shot point on V-shaped data produces a slope estimate that is highly sensitive to which shot counts are included and can be negative (Oxford Pets: -3.72) — the paper acknowledges this negative value but still uses the metric for cross-model comparison. Furthermore, GPT-4o was tested over a shorter shot range than Gemini 1.5 Pro (limited by context windows and timeouts), so the efficiency slopes are computed over different x-ranges. The headline claim that "Gemini 1.5 Pro exhibits higher ICL data efficiency than GPT-4o on most datasets" rests on comparing slopes where the assumed functional form is violated for one model. The paper would be stronger if it reported maximum relative improvement over zero-shot (already present) or area under the scaling curve as a complementary, assumption-free metric.

### Minor

- **The open-weights analysis reports an important negative result but provides no analysis of *why* these models fail.** The paper states that Llama 3.2-Vision and InternLM-XComposer2.5 "do not benefit from the demonstrating examples" but does not investigate whether this is due to context-length ceilings, architectural limitations, training-data issues, or something else. The specific shot counts tested for open models are also not reported. As a result, the finding is a descriptive observation rather than an actionable insight for the open-weights community. The conclusion "highlighting a significant gap" is warranted, but the analysis is thin.

- **The efficiency metric and detailed quantitative comparison only cover 10 of the 14 datasets.** The VQA (RSVQA, VQA-RAD) and object localization (DIOR, DeepLesion) datasets are included in the figures and discussed qualitatively in the text (e.g., "Gemini 1.5 Pro performance continues to improve up to the highest number of demonstrating examples on... VQA-RAD, DIOR and DeepLesion"), but they are absent from the efficiency table and the quantitative efficiency comparison. This creates a gap between the advertised scope (14 datasets) and the scope of the paper's central quantitative comparison.

- **The batched zero-shot ablation study is conducted only on Gemini 1.5 Pro and only on two datasets (TerraIncognita and UCMerced).** While the decomposition is insightful, the paper acknowledges this limitation (Section 6, line 215) but does not test whether the same three factors generalize to GPT-4o or to other datasets. This limits the generalizability of what is otherwise the strongest analytical contribution.

### Trivial

- Prompt templates are not shown in the paper, which slightly hinders reproducibility — particularly for the VQA and localization tasks where prompt formatting can matter.
- The cited tool link is truncated in the PDF (parser artifact).

## Nice-to-Haves

- A fine-tuning comparison on one or two datasets (even a small model) would ground the practical claims about many-shot ICL potentially "remov[ing] the need for fine-tuning" — though the paper explicitly identifies this as future work.
- Error bars or confidence intervals on the efficiency metric slopes would clarify whether cross-model differences are statistically meaningful.
- An analysis of whether later queries in a batched request benefit from seeing earlier responses (positional analysis) would strengthen the batching section.

## Removed Points

These points were flagged by the reviewers but removed after verification against the paper:

- **"Missing quantitative results for 4 of 14 datasets":** REMOVED. The paper presents scaling curves for these datasets in Figure 3 (caption states "on all three categories of tasks") and discusses them in the text (line 145 explicitly names VQA-RAD, DIOR, DeepLesion). The efficiency table covers only 10 datasets, but the results are not "missing" — they are presented in figures and text.
- **"Data contamination defense is insufficient":** REMOVED. The paper explicitly acknowledges this limitation ("we cannot determine that with certainty") and provides a reasonable argument. The critic mischaracterized the paper's hedging as dismissal.
- **"Comparison to fine-tuning is missing":** REMOVED. The paper explicitly states "it remains to be seen how traditional fine-tuning... compares to many-shot ICL... so future work should explore this." The paper scopes this out appropriately.
- **"Temperature=0 with single seed is insufficient":** REMOVED. Temperature=0 is already deterministic by definition. Bootstrapping (1,000 replicates) captures the main source of variance (data sampling), which is standard for this type of work.
- **"Only 2 open models tested":** REMOVED. Testing two open models (at different size points: 7B and 11B) is a reasonable sample for a study whose primary focus is the closed-model comparison.
- **"No positional analysis for batched queries":** REMOVED. The paper's ablation study on zero-shot batching explicitly decomposes the contributions and addresses this concern.

## Novel Insights

The primary novel empirical observation is that **the relationship between shot count and performance qualitatively differs between model families**: Gemini 1.5 Pro shows stable log-linear improvement across nearly all datasets, while GPT-4o often degrades before improving (V-shaped). This suggests that the internal mechanism for incorporating many demonstrations differs between architectures or training procedures — an observation that could motivate further mechanistic analysis. The decomposition of zero-shot batching gains into domain calibration, class calibration, and self-ICL is a secondary but well-supported insight that goes beyond prior batch-prompting work.

## Suggestions

1. **Revise or supplement the efficiency metric.** Replace or augment the log-linear slope with a metric that does not assume a monotonic functional form — e.g., max relative improvement over zero-shot (already reported) or area under the scaling curve. At minimum, caveat the cross-model comparison by noting the different shot ranges and the V-shaped violation.
2. **Provide the efficiency numbers for the VQA and localization datasets**, or clearly state that the efficiency metric is restricted to classification tasks.
3. **Add a brief analysis of why open-weights models fail.** Even a short paragraph examining context-length limits or architectural differences would substantially strengthen this finding.
4. **Include prompt templates** in the appendix or supplementary material.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>