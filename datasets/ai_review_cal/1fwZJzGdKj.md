- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 8, 6, 3
Now I have a thorough understanding of the paper. Let me construct the final review.

## Summary

This paper proposes a multi-agent collaborative data selection framework for LLM pretraining. Three agents (quality, domain, topic) each score data points based on their perspective, and an "agent console" dynamically integrates their scores via reward-weighted updates computed using influence functions on reference tasks. Experiments on a 1.3B LLaMA-2 model trained on 30B tokens from SlimPajama show consistent improvements over a wide range of baselines, with ablations confirming the necessity of all three agents and the dynamic weighting mechanism.

## Strengths

1. **Clear empirical motivation**: The case study (Section 2, Figure 1) provides concrete statistics from SlimPajama showing conflicts among quality, diversity, domain, and influence — e.g., high-quality Book documents having 85% same topic, diverse C4 documents having low model influence. This directly motivates the collaborative framework.

2. **Consistent empirical gains across a broad baseline set**: Table 1 shows the multi-agent method (37.8 avg) outperforming every baseline across all three task categories (problem solving, commonsense reasoning, reading comprehension). The comparison includes 11 baselines spanning random sampling, perplexity filtering, classifier-based methods (QuRating, FineWeb-Edu, DSIR), domain mixing (DOGE, DoReMi, DMLaw, RegMix), and influence-function methods (MATES). Gains relative to MATES (7.1%), QuRating (6.2%), and Random 60B (4.7%) are all meaningful.

3. **Ablation rigorously validates the framework design**: Table 2 shows each agent contributes: removing quality drops 7.4%, removing topic drops MMLU by 4%, removing domain drops commonsense by 5%. The "without collaboration update" (fixed equal weights) drops 7.1% from 35.0 to 32.5, confirming that dynamic weighting is essential, not just having multiple signals.

4. **Computational efficiency is demonstrated with concrete numbers**: Offline labeling takes 180 GPU hours vs. QuRating's 2000 and MATES's 360 for four-stage update. The topic classifier pipeline (1.44B documents clustered → GPT-4o annotation → BERT fine-tuning) is a practical engineering contribution that enables the topic agent.

## Weaknesses

### Fatal
None.

### Major

1. **Reference tasks overlap in category with evaluation tasks**. The reward signal for updating agents is computed via influence functions on reference tasks (LAMBADA, SQuAD, Jeopardy, per line 72 citing DSDM). The evaluation benchmarks include reading comprehension (BoolQ, RACE) and knowledge-intensive tasks (MMLU). While these are different datasets from the reference tasks, they belong to the same task families (reading comprehension, factual knowledge). This creates a plausible channel through which the method receives a reward signal correlated with the evaluation distribution, whereas many baselines do not use influence functions keyed to these tasks at all. The paper acknowledges this limitation (line 72–73: "this approach heavily depends on the selection of the reference tasks") but does not experimentally isolate the effect. The method still outperforms MATES (which also uses influence functions on reference tasks), suggesting the multi-agent framework adds genuine value, but the concern would be substantially weakened by evaluating on tasks provably disjoint from the reference set (e.g., code generation, multilingual tasks).

### Minor

2. **Single-run results without variance reporting**. No multiple seeds or confidence intervals are reported for any experiment (end-to-end or ablation). The end-to-end training of a 1.3B model is expensive, but even the smaller-scale ablation (373M, 5000 steps) is run once. The 4.7% gain over Random 60B and 7.1% over MATES could be within run-to-run noise, which is known to be non-trivial in LLM pretraining.

3. **The "up to 10.5%" claim in the abstract is imprecisely framed**. The 10.5% is computed against Random 30B (the weakest baseline). The abstract says "compared to the state-of-the-art methods," but random sampling is not SOTA. The paper's text at line 291 properly breaks down the gains against each baseline group, so the full picture is available, but the abstract's phrasing is misleading. This should be corrected to state the comparison point explicitly.

4. **Ablation study at reduced scale**. The ablation (Table 2) trains 373M models for only 5000 steps (~20B tokens), while the end-to-end results use 1.3B models for 30B tokens. It is unclear whether the ablation conclusions (e.g., the 7.1% drop from removing dynamic collaboration) hold at the full scale. The authors should acknowledge this scaling caveat.

5. **Reference task specification is ambiguous**. Line 72 mentions LAMBADA, SQuAD, and Jeopardy with "e.g." and "in DSDM," which is not a definitive statement of which tasks were actually used in the experiments. Line 300 mentions LAMBADA as an example reference task. The paper should state the exact reference task set used in its experiments, as the entire reward signal depends on this choice.

6. **Computational cost accounting is incomplete for the topic classifier**. The paper reports 180 GPU hours for offline labeling but does not break down the cost of (a) clustering 1.44B CommonCrawl documents, (b) GPT-4o annotation, and (c) BERT fine-tuning. These are one-time preprocessing costs, but they should be reported for reproducibility and fair comparison.

### Trivial

- The policy gradient update (Eq. 5: `w ← w + η·R̄`) is not a standard policy gradient; it is reward-weighted averaging. The paper should rename this or clarify the connection.

## Nice-to-Haves

- **Learning optimal static weights as an ablation baseline**: The "without collaboration update" baseline uses fixed equal weights (uniform). A stronger baseline would be to learn optimal static weights on a held-out validation set before training. If the dynamic method still wins, the adaptivity claim is even stronger.
- **Tracking collaborative weights over training**: A figure showing how θ_quality, θ_domain, θ_topic evolve across training steps would directly demonstrate adaptivity and potentially reveal which agent dominates at which stage.
- **Varying the agent set**: The framework is presented as general but tested with exactly three fixed agents. An ablation adding a fourth agent (e.g., perplexity-based) would strengthen the claim of extensibility.

## Removed Points
These points are flagged to be removed; treat them with caution:

- **"Unclear baseline parity"** (Harsh Critic #2). The paper compares against published methods as-is. The suggestion to create modified versions of baselines (e.g., MATES with different update frequency) to match the method's machinery is not standard practice. The multi-agent method outperforms both offline and online (MATES) baselines; the comparison is fair.
- **"Case study is thin"** (Harsh Critic, Section-by-Section). The case study is presented as qualitative motivation, not as a rigorous empirical claim. Its purpose is to illustrate the existence of conflicts, which it does with concrete statistics. Criticizing it for being a single snapshot at one step applies a standard of evidence the paper never claims for it.
- **"Optimization is heuristic with no convergence guarantee"** (Harsh Critic, Section-by-Section). This applies to most applied ML methods and is not a specific weakness of this paper. The paper's reward-weighted update rules are transparent and reasonable.
- **"Agent console simply amplifies most rewarded signal"**. This misunderstands the mechanism: Eq. 8-9 update θ_A based on (R̄_A − R̄), meaning agents below average get *de-weighted*. It is a well-motivated credit assignment scheme.
- **"Three fixed agents is arbitrary"** (Harsh Critic, Section-by-Section). The paper tests all combinations of agents in the ablation, confirming each agent contributes. Extensibility to more agents is a nice-to-have, not a weakness.
- **"Related work missing Doremi"** — Doremi is already cited in the paper (line 263, 348).
- **"Missing limitations section"** — The paper discusses the reference task dependency explicitly (line 72–73). A separate limitations section is a formatting convention, not a content requirement.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Run the end-to-end 1.3B experiment with at least 2–3 seeds (or report confidence intervals from bootstrapping the evaluation).
2. Clarify the exact set of reference tasks used and ideally include at least one evaluation task family (e.g., code or math reasoning) that is provably unrelated to those reference tasks.
3. Report the topic classifier's accuracy on a held-out set and the GPU-hour breakdown of preprocessing steps.
4. Correct the abstract to say "up to 10.5% improvement over the weakest baseline (Random 30B)" or rephrase the "state-of-the-art" language.
