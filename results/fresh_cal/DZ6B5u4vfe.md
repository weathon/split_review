I have thoroughly read and verified the paper's content against both reviewer inputs. Let me now produce the consolidated review.

---

## Summary

This paper investigates how instruction-tuning affects the alignment of LLM representations with human brain activity and behavior. It evaluates 25 models (17 instruction-tuned and 8 vanilla) from the T5 and LLaMA families across three fMRI datasets and one reading-time dataset. The main findings are: (1) instruction-tuning improves brain alignment by ~6.2% on average, (2) world knowledge (MMLU, r=0.81) and model size (log parameters, r=0.95) are strongly correlated with brain alignment, and (3) instruction-tuning does not similarly improve behavioral alignment to human reading times. A controlled ablation experiment (Figure 1D) further shows that instruction-following ability contributes to brain alignment beyond additional training data alone.

## Strengths

- **Controlled ablation experiment isolating instruction-following from added training data (Figure 1D).** The paper fine-tunes LLaMA-7B on the Alpaca dataset and, critically, also trains a control model on the same data but with instructions removed. The instruction-tuned model achieves higher brain alignment than the ablated counterpart, providing causal evidence that the instruction-following component itself drives part of the improvement (Section 4.1, line 76). This goes beyond a simple pre/post comparison.

- **Comprehensive evaluation across model families, scales, and neural datasets.** The study spans 25 models from 77M to 33B parameters across two architectures (T5 encoder-decoder and LLaMA decoder-only), tested on three independent fMRI datasets (PEREIRA2018, BLANK2014, WEHBE2014). This breadth strengthens the generalizability of the instruction-tuning effect beyond any single model or dataset (Sections 3–4).

- **Demonstration of a dissociation between brain alignment and behavioral alignment.** Section 5 and Figure 3 show that while instruction-tuning improves internal representational similarity to brain activity, it does not improve behavioral alignment to human reading times, and behavioral alignment is not significantly correlated with model size, world knowledge, or next-word prediction loss. This non-obvious negative result is a useful finding for the community, suggesting that improvements in internal representations do not automatically translate to more human-like behavioral outputs on this specific measure.

- **Use of instruction-tuned models to conduct fine-grained correlation analysis across knowledge domains (Table 2).** Because instruction-tuned models can follow the question-answer format of MMLU and BBH, the paper is able to compute correlations between brain alignment and specific knowledge categories (STEM, Humanities, Social Sciences, etc.) and reasoning types (algorithmic, world knowledge, multilingual). This methodological affordance enables a richer analysis than prior work that was limited to vanilla LMs.

## Weaknesses

### Fatal
None.

### Major

- **The "world knowledge" claim is confounded with model size, and no analysis separates their contributions.** The paper reports r=0.81 between brain alignment and MMLU overall score, and r=0.95 between brain alignment and log parameter count. These two predictors are themselves almost certainly strongly correlated (larger models achieve higher MMLU scores), yet the paper does not report their intercorrelation, perform a partial correlation, or conduct any variance decomposition to isolate the unique contribution of world knowledge from model size. The conclusion that "world knowledge is a key factor underlying LLM-brain alignment" (Section 4.2, line 91) is therefore not well-supported by the evidence presented. The observed MMLU correlation could be largely or entirely driven by the confound that larger models have more capacity and also happen to score higher on knowledge benchmarks. The paper partially mitigates this by showing that smaller instruction-tuned models can outperform larger vanilla models (e.g., Vicuna-13B > LLaMA-33B, line 97), which does suggest size is not the whole story, but this does not substitute for a proper disentanglement in the core correlation analysis. Without addressing this, the paper's most novel claim remains substantially weakened.

### Minor

- **The main finding that instruction-tuning improves brain alignment (6.2%) lacks a formal statistical test.** The paper reports an average improvement and shows all 8 paired points above the identity line in Figure 1B, which is visually compelling. However, no paired statistical test (e.g., Wilcoxon signed-rank or permutation test across the 8 vanilla/instruction-tuned pairs) is conducted to assess whether this improvement is statistically significant. The error bars represent median absolute deviation over human participants, not variability across model pairs. The longitudinal ablation on LLaMA-7B (Figure 1D) provides supporting evidence for a single model family but does not substitute for a significance test across all 8 comparisons.

- **The behavioral alignment analysis is underpowered, making the "no effect" conclusion tentative.** Section 5 reports that instruction-tuning "generally does not improve behavioral alignment," but the sample is small (8 paired comparisons), the figure shows a mix of increases and decreases, and no formal test is reported. The null correlations with MMLU (r=0.08, p=0.76) and model size (r=0.26, p=0.31) may reflect low statistical power rather than a true absence of relationship. To the paper's credit, the language is appropriately hedged ("generally indicates," line 114) and Section 6.2 discusses the need for broader behavioral benchmarks. However, the strength of the conclusion as stated in the abstract and introduction still somewhat overstates what the data can support.

### Trivial
None.

## Nice-to-Haves

- Report the intercorrelation between model size and MMLU performance explicitly. This single number would allow readers to gauge how much of the r=0.81 correlation may be spurious, and would strengthen the paper's analytical transparency.
- Conduct a partial correlation or linear regression predicting brain alignment from MMLU score while controlling for model size (and vice versa). If the MMLU partial correlation remains significant, the world knowledge claim would be substantially strengthened.
- For the behavioral alignment analysis, report effect sizes and confidence intervals alongside p-values, so readers can assess whether the null results are genuinely informative or merely underpowered.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"BLANK2014 results should be treated as unreliable"* — The paper already acknowledges the small participant count (N=5) and explicitly discusses this as a limitation (line 99). Including BLANK2014 in the average with this caveat is standard practice.
- *"The paper does not discuss whether instruction-tuned models differ in training data size/quality"* — The paper describes the different instruction-tuning datasets (FLAN, Alpaca, GPT4ALL, Vicuna) in Section 3 and acknowledges format variability as a limitation in Section 6.3. This point amounts to scope creep beyond what a single study can control.
- *"Best layer per model may inflate alignment and favor larger models"* — Selecting the best-performing layer is standard practice in Brain-Score work (following Schrimpf et al., 2018). If the critic believes this is problematic, they should cite a specific reference showing it introduces a systematic bias, not merely speculate.
- *"Brain alignment metric is limited to linear mapping"* — Using a linear mapping from LLM representations to fMRI voxels is the standard approach in this literature. Every method has limitations, and this one is applied uniformly across all models, so it does not differentially disadvantage any comparison.
- *"Instruction format varies across FLAN/Alpaca/Vicuna without analyzing variability"* — The paper acknowledges this as a limitation (Section 6.3) and restricts the study to two model families to mitigate it. Demanding a full analysis of instruction-format effects is a reasonable extension but not a flaw in the current paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the confounding issue directly.** Add a partial correlation analysis or a simple linear regression that predicts brain alignment from MMLU while controlling for log parameter count (and vice versa). This would either substantially strengthen or appropriately constrain the world knowledge claim, and it requires no new experiments or data—only re-analysis of existing results.
2. **Add a paired statistical test for the 6.2% improvement.** A Wilcoxon signed-rank test across the 8 vanilla/instruction-tuned pairs, or even a bootstrap confidence interval on the improvement, would formalize the main empirical claim. Given that all 8 pairs lie above the identity line, the result is almost certainly significant—reporting the test would close this gap cleanly.
3. **Rephrase the behavioral alignment conclusions** to more clearly acknowledge the low statistical power. Phrases like "we did not detect an effect" rather than "does not improve" would more accurately reflect what the data can support, especially given the small sample.

## Score and Decision

This paper makes a solid empirical contribution by systematically evaluating the effect of instruction-tuning on brain alignment across 25 models, with a well-designed ablation experiment. The 6.2% improvement finding is plausible and well-supported visually, though it lacks a formal significance test. The more ambitious claim that world knowledge is a key factor is weakened by the confounding with model size—a gap that could be closed with additional analysis but is not addressed in the current manuscript. The behavioral alignment analysis is appropriately tentative but underpowered. Overall, the paper is a reasonable contribution to an active area, with clear avenues for strengthening its core claims.

**MY FINAL SCORE:** <score>6.5</score>
**MY FINAL DECISION:** <decision>Accept</decision>