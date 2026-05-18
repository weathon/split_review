Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces ReDial, a human-annotated benchmark of 1,216 parallel AAVE–Standardized English prompt pairs spanning four reasoning categories (algorithm, math, logic, comprehensive). Using ReDial, the authors evaluate 11 LLMs and find that (1) nearly all models exhibit statistically significant performance drops on AAVE inputs, (2) this brittleness is not fully explained by data skewness (as shown in a perplexity-matched noisy-text comparison), and (3) prompting models to standardize AAVE before answering does not close the gap and adds computational cost.

## Strengths

1. **First human-annotated AAVE–Standardized English parallel reasoning benchmark.** ReDial is constructed by hiring AAVE speakers (including CS experts for algorithm tasks) to rewrite seven established benchmarks. The annotation pipeline includes cross-validation for naturalness and manual correctness checks, avoiding the circularity of using LLMs as evaluators (Section 2, Figure 2). This fills a genuine gap — prior dialect benchmarks either used rule-based transformations or LLM-generated rewrites, both of which have known limitations.

2. **Systematic and statistically rigorous evaluation across models and tasks.** Table 1 shows consistent, statistically significant performance drops (tested via McNemar with Holm-Bonferroni correction) across 11 LLMs covering proprietary (GPT-4o/4/3.5), open-weight (LLaMA-3/3.1, Mistral/Mixtral), and specially trained (Phi-3) families. The drops are documented under both zero-shot and CoT prompting. Table 2 further disaggregates by reasoning category, revealing that comprehensive reasoning suffers nearly 50% relative degradation.

3. **Creative perplexity analysis probing the data-skewness hypothesis.** The experiment comparing model performance on AAVE versus character-level noisy text at matched perplexity levels (Figure 2) provides evidence that frequency alone does not explain the gap — larger models perform worse on human-written AAVE than on even less familiar (higher-perplexity) noisy text. This is a genuinely informative probe that goes beyond the typical "AAVE is underrepresented → gap exists" narrative.

4. **Practical finding about standardization prompting being insufficient and costly.** Figure 3 demonstrates that instructing models to rephrase AAVE queries in Standard English before answering does not close the performance gap — and even increases token costs. This has real-world implications for the quality of service dialect users receive.

5. **Analysis of scaling and training-data curation effects.** The paper shows that scaling (LLaMA-3-8B → 70B) widens the dialect gap, and that Phi-3 models trained on highly curated "textbook" data are particularly brittle. These findings align with prior work on how data cleaning can exacerbate minority-group unfairness (Section 3.2).

## Weaknesses

### Fatal
None.

### Major

1. **Lack of annotator reliability documentation for the core dataset.** ReDial is a central contribution, yet the paper provides no information about the number of annotators hired, how many rewrites each produced, or any measure of inter-annotator agreement. The annotation description (Section 2.2) mentions cross-checking ("annotators cross-check and edit each others' annotations") and the ethics section (Section 6) explains the privacy-driven decision not to collect personal information. However, reporting annotator counts and agreement metrics (e.g., on a held-out set of 50–100 instances rewritten by multiple annotators) is orthogonal to privacy and is standard practice for dataset papers. Without this information, it is difficult for the community to assess whether the AAVE in ReDial reflects a consistent dialect variety or is idiosyncratic to a small number of individuals. The paper would be significantly strengthened by adding this documentation.

### Minor

1. **The standardization experiment would benefit from the direct AAVE+standardize vs. Standard+standardize comparison.** The paper currently compares AAVE+standardize to vanilla (zero-shot) Standard English and finds the former cannot match the latter. This is a valid fairness claim (an AAVE user doing extra work gets worse service than a Standard English user doing none). However, the paper also claims this shows "standardization does not close the gap," and the cleaner attribution test would be AAVE+standardize vs. Standard+standardize — i.e., both conditions receiving the same extra instruction. The paper has the data for this (Figure 3 shows both bars) but does not compute or discuss this comparison. If the gap persists, the claim that dialect per se causes the remaining gap becomes stronger. If it disappears, the conclusion needs revision. Either outcome would sharpen the paper's message.

2. **The perplexity-matched noise experiment uses character-level typos, which differ qualitatively from AAVE's systematic grammatical/lexical/phonological features.** The paper interprets the finding that models perform worse on AAVE than on matched-perplexity noise as evidence that "data skewness does not explain the whole picture." However, character-level noise is what models are commonly trained to be robust to (via data augmentation), so the comparison may stack the deck against AAVE. Moreover, Phi-3-Mini shows the opposite pattern (better on AAVE than on matched-perplexity noise), which the paper notes but does not explore — this exception undercuts the generality of the conclusion. The paper's claims are appropriately cautious ("suggest," "may not diminish"), but the analysis would benefit from explicitly acknowledging these confounds.

3. **The LLaMA-3-8B exception (no statistically significant drop) is under-analyzed.** This small model shows essentially no dialect gap (Δ=0.009 zero-shot, Δ=0.016 CoT, both non-significant). The paper attributes this to its generally lower performance but does not examine whether the gap is masked by a floor effect or whether the model genuinely treats both varieties more equally. This counterexample could inform hypotheses about what drives dialect brittleness (e.g., capacity thresholds, instruction-tuning data composition) and deserves dedicated discussion.

### Trivial

- The qualitative error analysis (Section 4.3) is limited to GPT-4o on the math subset. The identified patterns (wrong rephrasing, distraction, incomplete execution) are instructive, but it is unclear how representative they are across models and other task categories. The paper acknowledges this scope choice, so it is not a flaw, but it limits the generalizability of the error taxonomy.

## Nice-to-Haves

- A direct test of the data-augmentation hypothesis: fine-tune a model on augmented AAVE data and measure whether the gap shrinks. The paper's negative claim ("data skewness does not explain the whole picture") is supported by the current analysis, but a positive demonstration would be more convincing.
- Error analysis across a broader set of models (e.g., Mistral-7B alongside GPT-4o) to show whether failure patterns are model-specific or general.
- Task-specific analysis controlling for annotator background: since CS-expert annotators handled algorithm tasks while others likely handled different tasks, the paper could discuss whether the performance gap varies by task in a way that might reflect annotator quality rather than dialect complexity.

## Removed Points

These points from the reviews were removed with justification:

- **"The paper should test more advanced prompting methods"** — The paper explicitly scopes itself to daily-usage prompting (Section 3.1), which is a defensible choice. The "minor inconsistency" about the standardization prompt being a more advanced instruction is a trivial scope nitpick.
- **"The causal language in the perplexity analysis should be softened"** — The paper already uses appropriately cautious language ("suggest," "does not explain the whole picture," "may not"). This criticism overstates the paper's claims.
- **"Error analysis should include other models and tasks"** — Moved to Nice-to-Haves; not a core weakness.
- **"Task-specific analysis by annotator background"** — Moved to Nice-to-Haves; the paper cannot produce this data without collecting personal information. The ethics section transparently acknowledges this limitation.
- **"Fine-tuning experiment on augmented AAVE data"** — Moved to Nice-to-Haves; the paper's claim is a negative one ("data skewness alone does not explain"), which the current analysis supports. A positive fine-tuning experiment would strengthen but is not required to validate the existing claim.
- **Strength Finder's generic strength about "addressing an important problem"** — The retained strengths all have specific, citeable evidence from the paper. Generic framing ("this paper addressed an important problem") was dropped.

## Novel Insights

The most interesting finding that emerges from combining the reviews and the paper is the tension between the scaling-is-harmful narrative and the LLaMA-3-8B exception. The paper shows that larger models (LLaMA-3-70B, GPT-4o) are both more capable and more dialect-brittle, while LLaMA-3-8B shows no significant gap. This suggests that dialect unfairness is not a simple function of model capacity or training data size but may arise from how instruction tuning and data curation interact with dialectal features. The Phi-3 results (highly curated data → most brittle) point in the same direction: the very processes that make models good at standardized benchmarks may make them worse for dialect speakers. The perplexity analysis adds a further twist: models are somehow worse at handling systematic linguistic variation (AAVE) than random noise, even when they are more "familiar" with the latter. This combination of findings — curated data hurts, scaling hurts, random noise hurts less than real variation — paints a picture where dialect unfairness is not a simple data-quantity problem but something deeper about the structure of representation learning.

## Suggestions

1. **Report annotator counts and inter-annotator agreement.** Provide the number of AAVE speakers hired (total and per task category), the number of rewrites per annotator, and agreement metrics on a held-out multi-annotator subset (e.g., lexical overlap or naturalness ratings on 50–100 doubly-annotated instances). This is the single highest-leverage improvement.

2. **Add the AAVE+standardize vs. Standard+standardize comparison.** The data is already collected (Figure 3). Compute whether the gap between these two conditions is statistically significant. This would cleanly attribute any remaining gap to dialect per se rather than to the extra instruction.

3. **Directly analyze the LLaMA-3-8B exception.** Check whether this model's non-significant drop is a floor effect (it performs poorly on both varieties) or genuine robustness. If the latter, examine what differs about its training data or instruction-tuning recipe.

4. **Acknowledge the confound in the perplexity analysis more explicitly.** Note that character-level noise is a form of perturbation models may be specifically trained to handle, whereas AAVE features are systematic and may not be covered by standard data augmentation.

## Score and Decision

### Overall Assessment

This paper tackles an important and understudied problem — LLM fairness toward dialect speakers in reasoning tasks. The ReDial dataset is a genuine contribution, and the evaluation is thorough, covering 11 models with appropriate statistical testing. The key findings (significant performance drops, insufficiency of standardization, the non-trivial relationship between data frequency and brittleness) are all supported by the data and are practically important.

The most significant weakness is the lack of annotation documentation (annotator count, inter-annotator agreement) for the core dataset. This is a meaningful gap for a resource meant to serve the community, but it does not invalidate the downstream findings, which are consistent across models and tasks and survive multiple robustness checks. The other issues (standardization comparison, perplexity confounds) are addressable with analyses the authors have the data for or with wording adjustments.

The paper's contributions are real, the methodology is generally sound, and the findings are compelling. With the annotation documentation added and the standardization comparison sharpened, this paper would be a strong contribution.

**Score: 7.0** — A solid paper with clear contributions and a few fixable weaknesses.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>