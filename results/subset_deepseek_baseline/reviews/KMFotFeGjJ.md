## Summary

This paper proposes a method to detect data poisoning attacks on instruction-fine-tuned language models. The approach uses influence functions computed via the EK-FAC approximation, and applies a semantic transformation (sentiment inversion) to identify "critical poisons"—examples whose influence remains strong and polarity-unchanged after transformation. The method is evaluated on a sentiment classification attack (T5-small-1m-adapt) and a math reasoning attack (deepseek-coder-1.3b-instruct). The authors show that removing a small fraction of detected points recovers performance to near-clean levels.

## Strengths

- **Addresses an important and timely problem.** Detecting data poisoning in LLM fine-tuning, especially without prior knowledge of the attack, is a valuable capability for safe deployment.
- **Novel use of semantic transformation with influence functions.** The idea of comparing influence distributions before and after a label-relevant transformation to expose poisoned examples is creative.
- **Computational feasibility via EK-FAC.** The use of Anthropic’s efficient influence function approximation makes the method tractable on reasonably sized models and datasets, showing practical potential.
- **Demonstrates performance recovery.** Removing the detected points on both tasks leads to a reduction in attack success, suggesting the method has some signal.

## Weaknesses

### Major

1. **Very low detection recall.** On the sentiment classification task, only 23 out of 1000 actual poisons are correctly identified (2.3% recall) among 653 flagged examples. A true positive rate of 3.5% means the vast majority of flagged points are false positives. The paper does not report precision, recall, or F1, nor does it compare against a random removal baseline. The claimed "performance recovery" could simply be due to removing a set of benign examples that do not harm accuracy, rather than successfully targeting poisons.

2. **No rigorous baselines.** The comparison with existing defenses is superficial. The paper dismisses loss-based filtering with a single sentence and does not quantitatively compare against spectral signatures, activation clustering, or any other established poison detection method on the same attacks. Without such comparisons, the relative merit of the proposed method is unsubstantiated.

3. **Limited task and attack diversity.** The method is evaluated on only two tasks (sentiment and math reasoning) with a single trigger phrase ("James Bond") and a single model architecture per task. The semantic transformation is hand-crafted: sentiment inversion for classification, and "What is the opposite of..." for math. It is unclear how to generalize this to other tasks (e.g., code generation, summarization) or to attacks that do not have a natural semantic inversion (e.g., inserting irrelevant tokens). The claim of "no prior knowledge" is overstated because the design of the transformation implicitly assumes knowledge about the task.

4. **Weak math reasoning experiment.** The math model achieves only 7% accuracy even on the clean dataset, and the attack metric is not accuracy but "target output rate." Removing detected examples reduces the target output rate to 0, but this may be trivial given the model’s poor reasoning ability. Results on a more capable model are needed to demonstrate practical utility.

5. **Threshold selection and reproducibility.** The paper states it detects 653 "critical poisons" but does not specify how the threshold for "strong influence" and "unchanged polarity" is set. This makes the method hard to reproduce and suggests potential overfitting to the specific dataset.

### Minor

- The influence score computation is limited to a single layer of the model (configurable), and experiments use small models (T5-small, 1.3B). Scalability to larger models (e.g., 7B+) is not discussed.
- Figures (e.g., histograms) are low resolution and hard to read. The bar chart in Figure 4 lacks confidence intervals.
- The text in Table 1 contains highlighted entries whose meaning is not explained.

## Nice-to-Haves

- Provide full precision/recall curves and compare against a random removal baseline.
- Test on a diverse set of attacks (different triggers, label-flipping, backdoor) and on larger models (e.g., Llama-2-7B).
- Explore whether the transformation can be automated (e.g., using a separate LLM to generate an opposite) rather than hand-designed per task.
- Include a variant that uses fewer false positives, perhaps by combining influence scores with a secondary filter.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Report detection precision and recall, and compare against a baseline that removes the same number of random examples, to show that performance recovery is not an artifact of dataset size reduction.
- Evaluate on a more capable model (e.g., Llama-2-7B) and an attack that causes measurable accuracy degradation, to demonstrate that removal restores meaningful task performance.
- Provide a clearer algorithm for threshold selection, or show sensitivity to the chosen cutoff.
- Discuss limitations more openly: the method relies on a task-specific transformation and may fail for attacks without a natural semantic axis.

## Score and Decision

**Score:** 4

**Decision:** Reject

While the underlying idea is interesting, the empirical evaluation is too weak to support the paper’s claims. The extremely low recall (2.3%) and the absence of meaningful baselines make it unclear whether the method adds value over simple heuristics. The limited scope (two tasks, one attack pattern, small models) and the reliance on hand-crafted transformations further reduce the significance of the contribution. A substantially more thorough evaluation is needed.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>