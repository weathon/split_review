Below is my final consolidated review.

---

## Summary

This paper proposes ReaL-TG, a reinforcement learning framework that fine-tunes LLMs (using GRPO with an F1-based outcome reward) to perform explainable link forecasting on real-world temporal graphs. The framework uses a temporal random-walk subgraph selector (T-CGS) to construct context graphs, verbalizes them as text prompts, and lets the LLM self-explore reasoning strategies. The paper also introduces a new evaluation protocol combining pMRR (to penalize over-generation) and an LLM-as-a-Judge system that assesses faithfulness, logical consistency, and answer-explanation alignment. Experiments show that the fine-tuned 4B model (ReaL-TG-4B) outperforms much larger LLMs (GPT-5 mini, Llama 3.3 70B) on ranking metrics while producing human-validated reasoning traces.

## Strengths

- **ReaL-TG-4B outperforms substantially larger frontier LLMs on link forecasting accuracy.** Table 2 shows ReaL-TG-4B achieves the highest combined MRR (0.552) and pMRR (0.508) across all six datasets, beating GPT-5 mini (0.456/0.351) and Llama 3.3 70B (0.521/0.423). The gains are especially large on unseen graphs (e.g., tgbl-uci MRR 0.607 vs. next best 0.422). The comparison across LLMs uses the same filtered evaluation data and prompts, so this finding is well-supported.

- **Human evaluation confirms both the quality of ReaL-TG-4B's reasoning traces and the reliability of the LLM-as-a-Judge system.** Section 5.2 reports that five human annotators assign scores of 0.885 (faithfulness), 0.872 (logical consistency), and 0.839 (answer-explanation alignment) on a random 50-sample subset—closely aligned with the automated judge. The same annotators rate the judging quality itself at 1.71–1.88 out of 2, validating the automated evaluation framework. This is a genuine methodological contribution for a community that has lacked systematic reasoning quality assessment.

- **The RL-based fine-tuning framework (GRPO with F1 outcome reward) is well-motivated, technically sound, and clearly improves over the base model.** Qwen3-4B goes from MRR 0.375 to 0.552 after ReaL-TG fine-tuning (Table 2), and reasoning quality traces improve across all three criteria (Table 3: δ_f 0.683→0.885, δ_c 0.700→0.880, δ_a 0.653→0.732). The non-parametric outcome reward avoids training a separate reward model and is a clean design choice.

- **The paper includes human evaluation of both reasoning traces and the judge system itself**, providing direct evidence that the automated scores correlate with human judgment—this is rare in the LLM+graph literature and increases confidence in the evaluation methodology.

## Weaknesses

### Fatal
None.

### Major

- **The evaluation test set systematically excludes hard queries, and the paper does not adequately discuss this limitation or its impact.** Both training and test data are filtered to retain only queries where all ground-truth answer nodes appear in the T-CGS context graph. From Table 1, this removes roughly 29% of queries overall—and over 50% on two datasets (tgbl-coin: 543/1000 removed; tgbl-flight: 512/1000 removed). Queries where answer nodes have no or few historical interactions are systematically discarded, making the evaluation unrepresentative of the full link forecasting task. The paper does not report per-dataset filtering rates or evaluate performance on the unfiltered set. While the filtering is understandable (LLMs cannot predict answer nodes they cannot see), the paper's framing as "real-world" evaluation is overstated without acknowledging this bias.

- **The claim of outperforming "strong traditional methods" (Table 4) is not cleanly supported because the paper does not clarify whether TGNNs are evaluated on the same filtered evaluation set or on the full TGB test set.** The Experimental Setup section describes the filtered 4,246-query evaluation data, and the TGNN comparison appears in the same section, suggesting the same data is used. However, the TGNN paragraph states that models are evaluated "using MRR" without specifying the test set, and the computational-cost discussion (timeouts) is more consistent with full-set evaluation. The paper needs to (a) explicitly state whether TGNNs use the same filtered queries, (b) if they do not, re-evaluate them on the filtered set or (c) if they do, acknowledge that TGNN results are also affected by the filtering and qualify the comparison claims accordingly. On tgbl-wiki, DyGFormer (0.847) actually outperforms ReaL-TG-4B (0.824), so the claim of universal outperformance is imprecise even setting aside the ambiguity.

### Minor

- **The pMRR metric uses an arbitrary penalty value of 1.1.** The paper notes "can be any number > 1," but the choice affects the magnitude of the penalty and thus the metric's sensitivity to over-generation behavior. No analysis or justification for the specific value is provided.

- **No sensitivity analysis is provided for the T-CGS hyperparameters (α, β, number of selected nodes).** The random-walk-based subgraph selection has tunable parameters (α=0.3, β=0.6, |𝒩_q|=100, max 2 steps). The paper does not ablate these choices or show how performance varies with them, leaving open how robust the overall pipeline is to these design decisions.

- **The reward hacking observed for ReaL-TG-0.6B (claiming the answer "has already been seen in the graph context") is not analyzed for ReaL-TG-4B.** The paper detects this shallow shortcut in the smaller model but does not audit whether the 4B model engages in similar (but harder-to-detect) pattern-matching behavior. Since the F1-based reward is the same for both models, a manual audit of ReaL-TG-4B's reasoning traces (even on a small sample) would strengthen the claim that the model genuinely reasons.

- **No confidence intervals or statistical significance are reported for any metric.** Given the moderate evaluation size (4,246 queries across 6 datasets) and the fact that some datasets have only ~450 queries after filtering, variance could be non-negligible. Reporting standard errors or running evaluations with multiple seeds would strengthen the results.

### Trivial
None.

## Nice-to-Haves

- Evaluate on the unfiltered test set, even if the model must output a default "unknown" token when answer nodes are absent from the context, to quantify the real-world performance gap introduced by filtering.
- Provide per-dataset filtering statistics (how many queries were excluded and why) to increase transparency.
- Apply ReaL-TG to a larger base model (e.g., Qwen3-8B) to test whether the framework scales with model capacity—the paper already identifies this as a promising direction but does not execute it.
- Include explicit reasoning trace examples comparing ReaL-TG-4B with its base model (Qwen3-4B) to illustrate how RL changes the reasoning behavior (the paper mentions this is in the now-stripped Appendix J).

## Removed Points

*These points were flagged but removed with brief justification.*

- **"Data leakage potential from filtered evaluation"** (Harsh Critic #3): The critic speculates that filtering may cause LLMs to "memorize patterns" rather than reason. All LLMs are evaluated on the same filtered data, so relative rankings remain meaningful. The paper also explicitly demonstrates reward hacking detection as evidence it is monitoring for such behavior. There is no concrete evidence of memorization in the 4B model, making this speculation rather than a verified weakness.
- **"LLM-as-a-Judge introduces model-specific bias; sample size only 50"**: The paper already acknowledges the potential family-bias issue (it excludes GPT-5 mini from reasoning evaluation for exactly this reason) and the human evaluation on 50 samples shows strong correlation. For a sanity-check validation, 50 samples with 5 annotators is reasonable. The critic's call for inter-annotator agreement (Cohen's κ) is a nice-to-have, not a weakness.
- **"No statistical significance"**: Single-run evaluation is standard practice for LLM benchmarks at this scale. Not a genuine weakness in this community context.
- Several formatting/style nitpicks from the harsh critic (e.g., about "1.1" being arbitrary, which the paper already acknowledges as a design choice that can be any value > 1).
- Strength Finder generic/superficial claims about "addressing an important problem" or "targeting an interesting question"—these are not specific enough to retain as actionable strengths.

## Novel Insights

None beyond the paper's own contributions. The cross-validation of the harsh critic and strength finder surfaces a tension that is worth highlighting: the paper's two headline claims ("outperforms much larger frontier LLMs" and "outperforms strong traditional methods") rest on different evidentiary footing. The LLM-vs-LLM comparison is clean (same prompts, same filtered data), well-supported, and is the paper's primary contribution. The TGNN comparison, while plausible, is weakened by ambiguity about the evaluation test set. Separating these claims and calibrating their strength accordingly—as the paper already partially does by listing only the LLM outperformance as a contribution—is the right framing, but the TGNN-comparison text currently overstates the evidence. The most novel methodological contribution is arguably the combination of (a) the GRPO-with-F1-reward approach to temporal graph reasoning and (b) the three-criterion LLM-as-a-Judge with human validation, both of which lay groundwork for a new evaluation paradigm in this subfield.

## Suggestions

1. **Clarify the TGNN evaluation protocol in Table 4.** Explicitly state whether TGNNs are evaluated on the same filtered 4,246-query set or on the full TGB test set. If the former, note that filtering also affects the TGNN numbers. If the latter, re-evaluate TGNNs on the filtered set or remove the direct comparison claim and instead frame it as indicative.
2. **Acknowledge and quantify the evaluation filtering limitation openly.** Report per-dataset filtering rates, discuss the types of queries excluded, and add a caveat that the results apply to queries where answer nodes are historically observed.
3. **Ablate T-CGS hyperparameters** (α, β, |𝒩_q|) to show robustness of the pipeline.
4. **Audit a random sample of ReaL-TG-4B's reasoning traces** for reward-hacking patterns similar to those detected in the 0.6B model.
5. **Tone down the "outperforms strong traditional methods" claim** to reflect the ambiguity in the comparison, e.g., "shows promising performance compared to TGNNs on the filtered evaluation set while additionally providing explanations."

## Score and Decision

**Originality:** High — RL-based fine-tuning (GRPO + F1 reward) for LLM-based temporal graph reasoning is novel.
**Importance of research question:** High — explainable link forecasting on temporal graphs is an important and underexplored area.
**Claims well supported:** Moderate — the main claim (outperforming larger LLMs) is well-supported; the TGNN comparison is less clean.
**Soundness of experiments:** Moderate — good human evaluation and careful reasoning quality assessment, but the filtering bias and TGNN evaluation ambiguity weaken the experimental setup.
**Clarity of writing:** High — well-structured and clearly written.
**Value to the research community:** High — the framework and evaluation protocol provide a foundation for future work on LLM-based temporal graph reasoning.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>