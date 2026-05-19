- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 5, 3, 3, 8
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper investigates whether three broad families of LLM-steering techniques — in-context learning (ICL), fine-tuning, and activation editing — can improve the faithfulness of chain-of-thought reasoning. Across three datasets (AQuA, LogiQA, TruthfulQA) and three models (Llama-3-8B, GPT-3.5, GPT-4), the authors report that none of the tested strategies consistently improve faithfulness without sacrificing accuracy. The paper contributes a systematic negative result, a probing analysis showing faithfulness is localized in specific attention heads, and a refinement of the early-answering faithfulness metric to the per-example level using probability scores.

## Strengths

- **Systematic comparison across three intervention families**: The paper tests ICL (4 sampling strategies), fine-tuning (4 analogous strategies), and activation editing (top-K probe-based translation) on a consistent set of 3 models × 3 datasets. This breadth is the paper's primary contribution — it is the first evaluation to compare all three approaches on the same faithfulness benchmark. The consistent pattern across Figures 2–7 that no configuration simultaneously achieves high accuracy and high faithfulness is the study's central empirical result.

- **Observation that larger, more accurate models are less faithful**: Section 4.2.1 reports that GPT-4 achieves higher accuracy than GPT-3.5 and Llama-3 across all three datasets but exhibits poorer faithfulness (e.g., on TruthfulQA, the accuracy difference between CoT and non-CoT prompting is zero for GPT-4). This connects the hardness result to model scale and training objectives (RLHF), a nontrivial finding that goes beyond stating the negative result.

- **Probing analysis revealing localized encoding of faithfulness**: Figure 1 shows that certain attention heads have substantially higher probing accuracy for faithfulness than others (e.g., ~0.85 vs. ~0.55 on LogiQA). This demonstrates that faithfulness information is concentrated in specific model components — a concrete insight into model internals that supports the claim that faithfulness is a property the model encodes but not one current interventions can reliably amplify.

- **Novel application of activation editing to faithfulness**: The paper introduces a minimally invasive intervention (Equation 1) that translates attention-head activations along the learned probe direction, scaled by the standard deviation of projections. While based on prior activation-editing work (Li et al. 2024), applying it to target faithfulness specifically is novel.

- **Refined faithfulness metric using probability scores**: The paper extends the Lanham et al. (2023) early-answering metric from binary correctness to per-example probability scores (Section 2), enabling the fine-grained analysis shown in Figures 2–7.

## Weaknesses

### Fatal
None.

### Major
- **No quantitative summary tables**: The entire Results section (Section 4.2) relies exclusively on scatter plots. There are no tables reporting mean faithfulness scores, accuracy values, standard deviations, or effect sizes for any (model, dataset, strategy) combination. For a paper whose primary claim is a *negative result*, the absence of numerical evidence is a significant gap — the reader cannot assess whether a reported "improvement" is 0.01 or 0.1 in AOC score. The paper states concrete numbers once (activation editing baseline: AQuA accuracy 0.49, faithfulness 0.627) but omits them for all ICL and fine-tuning conditions. Scatter plots convey trends but do not replace summary statistics needed for cross-study comparison.

- **Single faithfulness metric used without critical discussion**: All experiments rely solely on the early-answering AOC metric from Lanham et al. (2023). The paper acknowledges the difficulty of operationalizing faithfulness (Section 2, line 71: "operationalizing this definition... is non-trivial") but never discusses the metric's known limitations — e.g., it measures a proxy (answer consistency under truncation) rather than causal faithfulness, and it may conflate faithfulness with answer stability. If the metric itself is insensitive to real improvements, the negative findings about improving it may not generalize to the construct of faithfulness the community cares about. The paper should at minimum acknowledge this limitation.

### Minor
- **No statistical significance or error bars**: For a negative-result study, the reader needs to know whether the observed lack of improvement is within noise. No confidence intervals, standard deviations, or significance tests are reported for any experiment. The paper does not specify the number of runs (single-run evaluation appears to be the norm in the paper's figures).

- **No sensitivity analysis for binarization threshold in probing**: Section 3.3 binarizes the continuous faithfulness scores using the median as a threshold for training linear probes, with no investigation of whether results are sensitive to this choice. Different thresholds might yield different probe directions and different editing outcomes.

- **GTA baseline description is ambiguous**: The Ground Truth Answers baseline is described as "a random set of ground truth question and answer pairs" (Section 4.1), but it is unclear whether these pairs include CoT rationales or just Q-A pairs. The results later treat GTA as comparable to other strategies, so the content of the examples matters for interpretation.

- **Claim scope in title slightly overbroad**: The title "On the Hardness of Faithful Chain-of-Thought Reasoning" suggests a general hardness result, whereas the paper tests specific instantiations of three approaches (4 ICL strategies, 4 fine-tuning strategies, 1 activation-editing design with top-K heads). The body text is appropriately measured — the abstract says "current array of approaches may not be sufficient" — but the title over-advertises the scope. This is a framing issue, not a substantive flaw.

### Trivial
None.

## Nice-to-Haves
- Diagnostic analysis of *why* strategies fail (e.g., does ICL faithfulness correlate with in-context example similarity? Do fine-tuned models overfit to selection bias? Do probe directions correspond to faithfulness or to something correlated like confidence?)
- A limitations section explicitly discussing (a) single-metric reliance, (b) narrow exploration of each approach, (c) the fine-tuning coverage gap for GPT-4, and (d) potential data leakage in selection (same dataset used for selecting faithful examples and evaluating).

## Removed Points
*These points were identified in reviews but removed after verification against the paper:*

- **"Activation editing only tested on two datasets (LogiQA relegated to appendix)"** — REMOVED because the paper explicitly references LogiQA activation editing results in the appendix (Figure 5 caption: "~\ref{app:intervention} for \logiqa dataset"). The parser strips appendix sections, but they exist in the original submission. Per rules, appendix content is assumed present.
- **"Superscript c notation never formally defined"** — REMOVED because it IS defined at line 103: "use a superscript $^c$ notation to indicate that only $(Q, E, A)$ triplets with correct answers are used."
- **"Equation ambiguous about whether translation applies before or after softmax"** — REMOVED because Equation 1 clearly shows addition after the softmax(QQ^T)V product: $\text{softmax}(\ldots) \mathbf{V'} + \alpha \theta \sigma$. The equation is unambiguous.
- **"Fine-tuning hyperparameters unspecified"** — REMOVED per rules about reproducibility nitpicks. LoRA rank, epochs, etc. are implementation details standard for the community.
- **"Missing related work"** — REMOVED per rules: do not mention missing related works without external confirmation.
- **"Related work discussion of prior positive findings (Turpin et al.)"** — REMOVED per rules: do not mention missing related works.
- **General area-of-concern sweeps** ("could the metric be measuring a proxy?", "are confounders controlled?") — REMOVED as they lack concrete anchors in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews do not synthesize a novel observation that is not already present in the paper's own analysis (e.g., the inverse relationship between model scale and faithfulness, or the localized encoding of faithfulness in specific attention heads).

## Suggestions

1. **Add summary tables**: For each experiment (ICL, fine-tuning, activation editing), provide a table with columns: Model, Dataset, Strategy, Mean Faithfulness (AOC), Mean Accuracy, and ideally standard deviation or confidence intervals. This single change would dramatically strengthen the evidentiary value of the paper.

2. **Acknowledge metric limitations**: Add a brief discussion of the early-answering metric's known limitations (proxy measurement, conflation with answer consistency). If possible, show results on a second faithfulness metric to demonstrate robustness.

3. **Tighten title scope**: Consider a title that reflects the specific strategies tested rather than implying a general hardness result (e.g., "On the Limited Efficacy of Selected Steering Strategies for Faithful Chain-of-Thought Reasoning").

4. **Add diagnostic analysis**: Even a simple analysis of when/why strategies fail would deepen the contribution beyond reporting failure (e.g., does faithfulness correlate with example similarity in ICL? Do probe directions for faithfulness align with other known properties?).

---
