---

## Summary
This paper proposes a framework for self-improving language models through **generator-verifier (GV) games**, where a single base model is instantiated in two roles—generating candidate solutions and evaluating their quality—to construct preference pairs for DPO fine-tuning. The core technical contribution is *thresholded majority voting* for filtering noisy self-verification signals. Two main variants are studied: **SimpleGV** (single-turn judge) and **RevisionGV** (multi-turn iterative feedback). Extensions including iterative training and curriculum learning are also explored. The paper demonstrates improvements on Knights and Knaves (KK) logical reasoning and mathematical benchmarks (GSM8K, MATH, TabMWP), and identifies *easy-to-hard generalization* as an emergent property of the approach.

---

## Strengths

- **Systematic framework with careful ablations**: The GV game is cleanly formalized (Section 2), and the paper methodically ablates over model sizes (1B–12B), data sizes (5K–40K), thresholds, and the number of generator/verifier passes. Using 4 random seeds with standard deviations throughout is rigorous.
- **RevisionGV nearly matches oracle on KK**: Gemma-3-12B with RevisionGV reaches 52.8% average accuracy vs. 53.6% for oracle ground-truth filtering—a remarkable result given that no external supervision is used. This strongly supports the central claim that self-feedback can be nearly as informative as ground-truth labels.
- **Easy-to-hard generalization is a concrete and non-trivial finding**: Models trained exclusively on 2–3 person KK instances generalize substantially to 4–8 person instances (40.7%→44.1% across iterative rounds, versus 31.0% for the base model). This is practical and well-documented.
- **No external environments or labels required**: Unlike Absolute Zero (which needs code execution) or GRPO (which needs ground-truth rewards), the approach operates entirely on free-form natural language with offline optimization—a genuine advantage for low-resource or unstructured domains.
- **Honest treatment of scaling limits**: The paper clearly reports that SimpleGV fails for 1B models (accuracy can drop below baseline), attributing it to noisy verifier judgments at small capacity. This intellectual honesty strengthens the paper's credibility.

---

## Weaknesses

### Fatal
None.

### Major
- **Mathematical reasoning gains are modest**: On the five-benchmark evaluation in Table 1, the gains for Gemma-3-4B are small: GSM8K decreases by 0.2pp, MATH500 improves by 1.6pp, MATHHard by 1.4pp, TabMWP by 2.9pp, and KK by 2.2pp. For Qwen-2.5-7B, the picture is similar (1–2.5pp on MATH benchmarks, and KK *decreases* by 0.5pp). The headline results from the abstract (31.0%→44.8% on KK) are the main source of drama, and they apply only to one benchmark with one model family.

- **Suspicious baseline comparison**: In Table 1, Absolute Zero (AZR) and AZR-Coder applied to Qwen-2.5-7B perform dramatically *below* the base model on KK (5.1% and 8.5% vs. 18.1%). If correct, this needs explanation; if it reflects a suboptimal implementation, it makes the comparison misleading. Similarly, AZR underperforms the base on GSM8K (84.0% vs. 90.2%), which is surprising for a method that uses code execution as verification. These anomalies undermine confidence in the comparative conclusions.

- **Incremental conceptual contribution**: The method is a combination of established components: LLM-as-judge (well-established), majority voting for robust aggregation (used in Self-Consistency, STaR, TTRL), and DPO training on self-generated preference pairs (explored in Self-Reward, SPIN, iterative DPO). The thresholded majority voting is a clean insight but modest in novelty. RevisionGV is closer to a natural extension. The paper would benefit from a clearer articulation of what the GV framework enables that prior methods fundamentally do not.

### Minor
- **Threshold sensitivity in practice**: Different iterations and different tasks use different thresholds to achieve best performance (e.g., Table 2 mixes τ=0.5, 0.6 across rounds). While the paper claims 0.6–0.7 is robust, the tables show non-monotonic behavior that requires per-task tuning.

- **Data size analysis shows diminishing returns**: Figure 4 reveals that performance can regress when going from 20K to 40K samples on TabMWP and KK. The paper attributes this to redundancy and verifier noise, but no mitigation is proposed.

- **RevisionGV vs. SimpleGV gap is small**: While RevisionGV is presented as the stronger method, the gain over the best SimpleGV threshold for the 4B model is only 1.5pp (42.2% vs. 40.7%), and the computational cost is substantially higher. The paper does not fully quantify the cost overhead of RevisionGV relative to its gains.

### Trivial
- Table 2 has a typo: "gamma-34b-it" appears to be "gemma-3-4b-it."

---

## Nice-to-Haves
- An analysis of *when* the self-verifier is right vs. wrong (e.g., conditioned on task difficulty or answer type) would help practitioners understand where the method is reliable.
- A comparison to a distillation baseline where preference pairs are labeled by a larger external model (e.g., Gemma-27B) would contextualize how much value is genuinely added by self-verification vs. simply benefiting from any preference signal.
- Applying RevisionGV to the math benchmarks (not just KK) would clarify whether multi-turn gains generalize beyond the structured logic domain.

---

## Novel Insights
The most genuinely novel observation is the **emergent easy-to-hard generalization** under curriculum learning in the KK setting: models trained exclusively on 2–3 person puzzles transfer effectively to 4–8 person puzzles where the combinatorial search space is orders of magnitude larger. This is not an obvious consequence of DPO on self-generated data and suggests that GV training induces more general reasoning patterns rather than task-specific memorization. The finding that RevisionGV nearly closes the gap to oracle supervision (52.8% vs. 53.6% for 12B) is also noteworthy: it implies that a model's own feedback, when structured as iterative revision rather than binary judgment, can approximate ground-truth labels with high fidelity.

---

## Suggestions
- Report total inference cost (in FLOPs or GPU-hours) for generating the preference datasets at various configurations, so readers can assess practical viability.
- Add a condition in Table 1 that uses a larger external judge (e.g., Gemma-27B as verifier) on the same data to isolate the benefit of *self*-verification vs. any verification at all.
- Investigate the 1B failure case more deeply: does the verifier fail because it cannot parse the solution, because it lacks logical reasoning ability, or because of output formatting issues? Understanding this would guide future work on extending self-evolution to small models.
- Provide a brief theoretical analysis of why thresholded majority voting improves precision—e.g., connecting it to confidence intervals over a binomial proportion—to strengthen the methodological foundation.

---

## Score and Decision

The paper presents a well-executed empirical study of self-improvement via generator-verifier games. Its main value is practical: a clean, reproducible framework, a useful thresholding technique, and a compelling easy-to-hard generalization finding. However, the conceptual novelty is incremental (combining LLM-as-judge with thresholded majority voting and DPO), the gains on mathematical reasoning benchmarks are modest, and some baseline comparisons raise questions. The KK results are the most compelling but are limited to one benchmark. Overall, the paper makes a positive contribution to an active and important research area, warranting a borderline acceptance.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>