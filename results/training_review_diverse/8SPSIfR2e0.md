I now have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces "selective pruning," a machine unlearning method for transformers that prunes neurons based on the ratio of their activation importance on a forget dataset versus a retain dataset. The method requires only a small representative dataset and runs on a single consumer GPU. The paper evaluates across five model families (OPT, Galactica, Pythia, RoBERTa, ViT) up to 7B parameters, on tasks including code removal, Python removal, class removal from CIFAR-100, and toxicity reduction. A secondary contribution is analyzing whether feed-forward or attention neurons are more "specialized" for specific tasks.

## Strengths

- **Compute- and data-efficient unlearning for LLMs**: The method requires only a small representative dataset and runs on a single NVIDIA RTX 4090, even for 6.7B parameter models (Section 5, first paragraph; Section 6, paragraph 4). This is in contrast to Hessian-based pruning methods or fine-tuning approaches that are far more expensive for large models.

- **Cross-model and cross-task breadth**: The paper evaluates across five model architectures (OPT, Galactica, Pythia, RoBERTa, ViT) from 125M to 7B parameters, and on both language and vision tasks (code removal, Python removal, class unlearning, toxicity reduction). This breadth strengthens the claim that the approach generalizes (Table 1; Figures 1–3).

- **Empirical observation about feed-forward neuron specialization**: For models trained with feed-forward dropout (OPT, Galactica, RoBERTa), pruning feed-forward neurons via the importance ratio systematically yields a larger differential accuracy drop (forget vs. retain) than pruning attention neurons (Table 2: e.g., 59.6 vs 28.4 for OPT-1.3B, 52.4 vs 41.7 for Galactica-1.3B). The paper also identifies that Pythia (trained without dropout) does not show this effect, and hypothesizes that dropout drives task-specialization (Section 5.2, paragraph on dropout). This insight goes beyond evaluating a method to contributing a testable hypothesis about model design.

- **Strong forget accuracy with competitive retain accuracy on CIFAR-100**: Selective pruning achieves 0% accuracy on the forget class while retaining high retain accuracy (89.4% for "rocket," 89.5% for "mushroom"), outperforming Finetune, UNSIR, Amnesiac, and SSD in retain accuracy and matching the best methods on forget accuracy (Table 3).

## Weaknesses

### Fatal
None.

### Major

- **Missing random pruning results despite acknowledging the baseline**: The paper states at line 153 that "As a baseline we also randomly pruned layers" but presents zero results from this baseline in any figure or table. The central claim of Section 5.1 is "Selective Pruning is Effective," and the paper relies on the x=y line as an implicit baseline. While the x=y line does demonstrate asymmetric damage (more to forget than retain), it does not isolate whether the *scoring function* adds value over blind random pruning at the same pruning fraction. Showing random pruning curves alongside the selective ones for at least the Code vs. Pile experiments is necessary to support the claim that the scoring function itself is driving selectivity, rather than aggressive pruning of any kind.

- **CIFAR-100 MIA comparison is not discussed despite showing worse results**: In Table 3, selective pruning achieves MIA scores of 3.8 (rocket) and 2.8 (mushroom), which are noticeably *worse* (higher) than SSD (0.8 and 0.0) and Teacher (0.0 and 0.0). Since MIA is a standard unlearning privacy metric, higher MIA indicates that forget-class data points are more identifiable — i.e., worse unlearning from a privacy perspective. The paper presents the table without any discussion of this trade-off, and the concluding statement that selective pruning is "competitive" is undermined by these numbers. At minimum, the paper should acknowledge and discuss this limitation.

- **Toxicity experiment baselines are thin**: The toxicity comparison uses only a single quoted baseline (task arithmetic fine-tuning). For GPT-2-Large, attention neurons are pruned without explanation of why FF pruning (shown to be more effective in the main experiments) was not used. For LLaMA 2, no comparison method is provided at all. The retain dataset for LLaMA 2 is not specified (the GPT-2 experiment uses WikiText perplexity as the retain metric, implicitly clarifying the retain set). The reader cannot assess whether similar results could be achieved with random pruning or a simpler baseline.

### Minor

- **No uncertainty quantification across runs**: All experiments appear to be single runs without error bars or confidence intervals. For a method involving dataset sampling, iterative pruning, and threshold-based decisions, variability across random seeds or data splits is unknown. The CIFAR-100 comparison (Table 3) quotes results from other works without error bars for selective pruning. While the cross-model consistency partially mitigates this concern, the absence of any uncertainty estimates makes it impossible to assess whether the reported differences (e.g., 46.2 vs. 46.6 for FF vs attention in Pythia) are meaningful. **However**, I downgrade this from Major because: (1) smoothed curves over 50 pruning steps reduce noise, (2) the trends are consistent across multiple model families and task pairs, and (3) single-run evaluation is common in this class of work.

- **FF vs. attention claim is somewhat stronger than the evidence supports across all models**: The paper claims "feed-forward neurons are more specialized than attention neurons" (line 344), but for Pythia-1.4B the maximum difference is essentially tied (46.2 FF vs. 46.6 attention, Table 2). The paper does acknowledge this at line 391 ("pruning Pythia FF neurons is only marginally more effective"), but the broader claim in the abstract and discussion could be read as universally true. The claim should be explicitly scoped to models trained with feed-forward dropout, as the data supports.

- **No comparison of iterative vs. one-shot pruning**: The paper uses 50 steps of 2% pruning throughout but never compares to one-step pruning of the same total fraction. The "backup neuron" rationale (line 120–121) is plausible but untested. This makes it unclear whether the iterative procedure is actually beneficial or whether the main results could be obtained with a single pruning step.

- **The "stopping criterion" is not evaluated**: The paper uses "all neurons pruned" as the stopping criterion for analysis (line 151), but notes that in practice one would stop earlier based on retain accuracy thresholds. No sensitivity analysis is provided for how results depend on this threshold.

- **Scoring function behavior when importance(retain) is near zero is not discussed**: The scoring function uses an epsilon to prevent division by zero (line 114), but the paper does not discuss how this interacts with pruning choices, especially in early iterations when some neurons may be nearly silent on the retain set. This could cause neurons with near-zero retain importance (and small forget importance) to be incorrectly prioritized.

### Trivial

- **Incomplete sentence at line 77**: Observation 2) reads "For attention neurons" followed by a blank line, suggesting truncated content. (If this is a parser artifact, ignore; otherwise it should be completed.)

- **Unsourced claim in Broader Impacts**: The statement at line 517 that the method "is unlikely to generate systems that are more harmful than the base model" is stated without evidence or argument. Pruning can create brittle models that fail unpredictably, so this claim should be justified or removed.

## Nice-to-Haves

- An ablation of the number of pruning steps (e.g., 1 step of 100% vs. 10 steps of 10% vs. 50 steps of 2%) to validate the iterative procedure.
- A sensitivity analysis for the retain-accuracy stopping threshold.
- For the toxicity experiment, a comparison with FF pruning (not just attention) and a random pruning baseline.
- A brief discussion of failure cases or task pairs where selective pruning performed notably worse than the average.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that "the x=y line is not a meaningful comparator"**: I partially disagree with the harsh critic here. The x=y line *is* meaningful: it shows equal drop on both tasks, and the method's curves systematically lie above it, demonstrating asymmetric damage. This does not replace a random pruning baseline but is not meaningless. I have kept this in the Major weakness above but with more measured framing.

- **"The paper's claim about 'unlikely to generate systems that are more harmful' is unsupported"**: Kept in Trivial rather than elevated — it's a single sentence in Broader Impacts and not central to the paper. The reviewer's concern about brittle models is valid but speculative.

- **Harsh critic's point about "For attention neurons" followed by nothing**: This IS present in the paper (line 77-78). I kept it in Trivial. If it's a parser artifact, it should be removed entirely.

- **Strength Finder's strength about "Competitive unlearning performance on standard benchmarks"**: Modified to note the MIA trade-off rather than presenting it as unqualified strength.

## Novel Insights

The harsh critic's most valuable observation is the identification that the paper's central claim ("Selective Pruning is Effective") cannot be properly evaluated without a random pruning comparison. This is not about questioning the method's validity — the x=y line does show asymmetric damage — but about isolating whether the scoring function's *selectivity* adds value over mass pruning. The critic's framing that this is "not a minor omission" is too harsh, but the underlying point is substantive and constructive. The reviewer's observation about the CIFAR-100 MIA scores being worse than SSD/Teacher without discussion is also an insightful catch that the authors should address in revision.

## Suggestions

1. **Add random pruning curves** to the main figures (Code vs. Pile, Python vs. Code) showing the forget-vs-retain accuracy trade-off for random pruning at matching pruning fractions. This is the single highest-leverage improvement for the paper.

2. **Discuss the CIFAR-100 MIA trade-off** explicitly. Selective pruning achieves better retain accuracy than SSD but worse MIA; this is a meaningful privacy-utility trade-off that should be acknowledged and discussed rather than presented as unqualified competitiveness.

3. **Run at least 3 seeds** for the core Code vs. Pile experiment on the 1.3B-scale models (OPT, Galactica, Pythia) and report mean ± std for the max-difference metric. This would clarify whether the FF vs. attention differences (especially the tied Pythia result) are reliable.

4. **Scope the FF vs. attention claim** more precisely to "models trained with feed-forward dropout," since Pythia (no dropout) does not show the effect.

5. **Clarify the retain dataset** used in the LLaMA 2 toxicity experiment and specify why attention pruning was used for GPT-2 rather than the more effective FF pruning.

6. **Compare iterative vs. one-shot pruning** for at least one model/task pair to validate the iterative procedure's benefit.

## Score and Decision

**Originality**: Good — the scoring function (ratio of forget-to-retain activation importance) is simple but novel as an unlearning method for LLMs. The finding about dropout and specialization is insightful.

**Quality of research question**: Important — machine unlearning for LLMs is timely, and understanding neuron-level specialization has implications for both safety and interpretability.

**Claims support**: Mixed — the central claim about selectivity is partially supported (x=y line) but weakened by the missing random baseline. The FF vs. attention claim is well-supported for dropout-trained models but overclaimed as general. The CIFAR-100 comparison claims competitiveness without discussing the MIA trade-off.

**Soundness of experiments**: Broad but has gaps — no uncertainty quantification, no random pruning baseline, limited comparison methods for toxicity.

**Clarity**: Good overall, with clear methodology description and well-structured results section. Minor gaps in incomplete sentence and unspecified retain datasets.

**Value to community**: Moderate — the method provides a cheap, accessible baseline for LLM unlearning that others can build on. The hypothesis about dropout and specialization is testable and interesting.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>