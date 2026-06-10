Now I have thoroughly read and verified the paper. Let me produce the final consolidated review.

---

## Summary

This paper systematically investigates fine-tuning LMs (rather than few-shot prompting them) for agentic tasks, proposing FireAct — a recipe for generating diverse agent trajectories from GPT-4 using multiple prompting methods (ReAct, CoT, Reflexion) and tasks, then fine-tuning smaller LMs on these trajectories. The main findings are: (1) fine-tuning consistently improves agent performance across Llama-2, CodeLlama, and GPT-3.5 (25–77% relative EM gains on HotpotQA), (2) fine-tuning yields 70% inference time reduction and improved robustness to noisy tool outputs, and (3) mixing data from multiple prompting methods can further help but the optimal mix varies by model. The paper is an empirical study with a practical distillation recipe.

## Strengths

1. **Systematic evidence across diverse LMs.** Table 1 (lines 156–164) reports HotpotQA EM gains for every LM tested — Llama-2-7B (+77%), Llama-2-13B (+62%), CodeLlama-7/13/34B, and GPT-3.5 (+25%) — showing the fine-tuning benefit generalizes beyond the single model family (PaLM) studied in prior work (Yao et al., 2022).

2. **Quantified robustness advantage under adversarial tool noise.** Fine-tuned agents lose only 5.1% (random noise) and 14.2% ("None" noise) of their EM score versus 28.0% and 33.8% for prompted agents (Table 2, lines 189–194). The paper provides a concrete explanation: the fine-tuning data includes GPT-4's recovery from noisy queries, so the model learns to handle failures.

3. **Non-trivial data scaling trends revealing qualitative LM differences.** GPT-3.5 reaches ~35 EM with only 100 samples then plateaus, while Llama models require ~500 samples before non-trivial performance "emerges" (Figure 1, lines 218–221). This gives practitioners concrete guidance on data budgets for different model choices.

4. **Oracle analysis quantifying headroom in method selection.** The gap between the best multi-method result (41.0 EM) and the oracle-per-instance baseline (52.0 EM) provides a precise, measurable upper bound on how much better method selection could be (Table 3, lines 252–263).

5. **Honest reporting of negative and non-monotonic results.** The paper explicitly documents cases where expected improvements do not hold: CoT+ReAct hurts CodeLlama models (line 287), CodeLlama-34B underperforms CodeLlama-13B in single-method fine-tuning (line 224), and all fine-tuned agents underperform naive IO prompting on MMLU (line 303).

## Weaknesses

### Major

- **The prompting vs. fine-tuning comparison conflates the fine-tuning procedure with data volume.** The prompted baselines receive 3–5 in-context examples, while the fine-tuned models receive 500–1,000 full trajectories (each containing multiple rounds). The resulting gap (e.g., 31.4→39.2 for GPT-3.5) is presented as evidence that "fine-tuning" is superior to "prompting," but this is equally explained by the orders-of-magnitude difference in supervision volume. The paper acknowledges "the benefit of learning from more samples" (line 171) in passing, but does not attempt to control for this asymmetry — e.g., by fine-tuning on very few examples (5 or 10) and comparing to few-shot prompting with those same examples, or by giving prompted models as many in-context examples as context allows. The central empirical framework consequently supports the claim that "more training data helps understanding" more strongly than it supports "fine-tuning as a learning procedure is intrinsically better than prompting." This matters because the paper's framing in the abstract and introduction presents the comparison as a method-level result ("language agents are consistently improved after fine-tuning their backbone LMs," line 8) rather than a data-volume result.

### Minor

- **No confidence intervals, standard errors, or significance tests for core EM comparisons.** With 500 HotpotQA test samples, the standard error of a binomial proportion near 40% is ~2.2%. Several claimed improvements are small — e.g., ReAct+CoT (41.0) vs. ReAct alone (39.4) is a 1.6-point difference well within one standard error. While single-run evaluation without error bars is standard in this field, the multi-method conclusions in Table 3 (lines 252–263) partly rest on differences this small, making their reliability unclear.

- **Multi-task fine-tuning results are underwhelming and presented somewhat optimistically.** Multi-task fine-tuning (HotpotQA + StrategyQA + MMLU) achieves 39.2 on HotpotQA (same as single-task), 55.5 on StrategyQA (well below prompting at 61.0), and 63.2 on MMLU (below IO prompting at 68.6). The paper frames "adding a task might not improve... but also does not hurt performances" (line 34) as a positive finding. However, the multi-task agent underperforms prompting on two of three tasks, and matching prompting on StrategyQA requires also adding CoT data. The claim that this "hints at the promise of fine-tuning one multi-task agent" (line 301) outruns the evidence.

- **Generalization experiments are limited.** The generalization finding (HotpotQA fine-tuning transfers to Bamboogle: 44.0 vs. 40.8) rests on only 125 test questions — well within the noise range given no error bars. The paper itself acknowledges that transfer to StrategyQA and MMLU fails (line 183), further limiting the strength of the generalization claim.

### Trivial

- None.

## Nice-to-Haves

- A controlled comparison where both the prompted and fine-tuned conditions receive the same demonstrations (e.g., 5, 10, or 20 examples, either in-context or as fine-tuning data) would isolate whether fine-tuning provides a fundamentally different learning mechanism or is simply benefiting from greater data volume. This would sharpen the paper's central empirical claim.

## Removed Points

- **Harsh Critic's "context length asymmetry confounds efficiency comparison":** The 70% inference time reduction is a genuine practical advantage of fine-tuning (shorter context). The paper frames this as a practical benefit, not a scientific finding about method superiority (line 178: "the advantage of having a much smaller context is clear"). **Removed** — correct as stated.

- **Harsh Critic's "robustness experiment confounded":** The paper explicitly explains the robustness gain comes from the fine-tuning data containing noise-handling examples (line 181–182). This IS the hypothesis being tested, not a confound. **Removed.**

- **Harsh Critic's "limited scope" (single task, single tool):** The paper explicitly acknowledges this limitation (line 320–321) and frames itself as "an initial step." **Removed** — this is scope-awareness, not an unacknowledged weakness.

- **Harsh Critic's "multi-method benefits oversold":** The abstract says mixing "can further improve" (line 10) — a hedged claim. The body explicitly acknowledges inconsistency (line 287: "mixing more methods does not always improve results"). The critic overstates the discrepancy. **Removed.**

- **Harsh Critic's "multi-task as negative result presented as positive":** The paper honestly reports the mixed results and frames the non-negative transfer as a finding. The presentation is fair. **Removed.**

## Novel Insights

The most interesting finding across the reviews is that the paper's strongest contributions are actually its nuanced or mixed findings — the non-monotonic data scaling (smaller LMs need a minimum data threshold before agent behavior "emerges"), the inconsistent multi-method benefits across model families, and the quantified oracle gap (52.0 vs. achieved 41.0). These findings are more novel and actionable than the headline "fine-tuning beats prompting" claim, which is largely predictable given the data asymmetry. The "emergence" threshold for open-source LMs (500+ trajectories before any non-trivial performance) is a practically important result that the paper does not emphasize enough. Similarly, the finding that adding CoT data helps GPT-3.5 and Llama-2 but hurts CodeLlama suggests an interaction between pre-training data distribution and fine-tuning data diversity that merits deeper investigation.

## Suggestions

1. **Re-frame the central contribution.** Present FireAct as a practical distillation recipe (generate diverse trajectories from GPT-4, fine-tune a student LM) rather than a comparative evaluation of "fine-tuning vs. prompting" as competing paradigms. This would align the framing more precisely with what the experiments actually show.

2. **Add a data-volume controlled experiment.** Fine-tune on very few examples (e.g., 5 or 10) and compare to few-shot prompting with those same examples. This would isolate whether fine-tuning provides a fundamentally different learning mechanism or is simply benefiting from greater data volume.

3. **Report confidence intervals** for the main EM comparisons, especially the multi-method results where small differences (e.g., 39.4 vs. 41.0) drive conclusions.

4. **Develop a testable hypothesis about when multi-method diversity helps.** The finding that CoT helps GPT-3.5 but hurts CodeLlama is intriguing and deserves analysis — does CodeLlama's code pre-training already internalize structured reasoning, making CoT-style trajectories redundant or even confusing?

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>