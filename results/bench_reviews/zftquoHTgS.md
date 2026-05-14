Now I have a thorough understanding of both the paper and all calibration anchors. Let me compile the final review.

---

## Summary

This paper identifies and quantifies "underthinking" — the tendency of Long Chain-of-Thought (LongCoT) LLMs to prematurely switch between reasoning thoughts without sufficient exploration — and proposes SmartSwitch, an inference-time framework that detects thought switches via linguistic cues, evaluates abandoned thoughts with an off-the-shelf Process Reward Model (PRM), and injects a deepen prompt to encourage further exploration of promising but prematurely discarded paths. The method is training-free and plug-and-play. Experiments across five model scales (1.5B–32B) on five math benchmarks show consistent accuracy gains (up to +23.3 points on AIME25) alongside reduced inference time and token usage.

## Strengths

- **Consistent and substantial accuracy gains across diverse models and benchmarks**: Table 1 shows SmartSwitch improves pass@1 accuracy for all five tested models (DeepSeek-R1-Distill-Qwen at 1.5B, 7B, 14B, 32B, and QwQ-32B) on all five benchmarks (AIME24, AIME25, AMC23, MATH-500, GaoKao2023en), with gains ranging from +0.6 to +23.3 percentage points. These are non-trivial improvements on established competition-level math benchmarks.

- **Inference efficiency improves despite intervention overhead**: Tables 2 and 3 demonstrate that SmartSwitch reduces both average response length (e.g., −14.2% tokens for the 32B model on AIME24) and wall-clock time per query (e.g., −35.3% for the 7B model on AIME24), even after accounting for PRM scoring and backtracking costs. This dual improvement (accuracy up, cost down) is a non-obvious and practically valuable outcome.

- **Training-free and model-agnostic design**: SmartSwitch requires no fine-tuning and is applied as a wrapper across two model families and five scales, from 1.5B to 32B parameters. This low barrier to adoption is a genuine practical strength.

- **Thorough ablation of design choices**: The paper ablates PRM selection (Table 4), process division strategy (Table 6), score-mapping strategy (Table 7), and score threshold (Table 8). The "Always Intervene" baseline (18.9% vs. 20.0% vanilla, Table 4) cleanly demonstrates that PRM-guided selective intervention is essential, not merely the act of injecting prompts.

## Weaknesses

### Fatal

None.

### Major

- **No validation split described; threshold sensitivity is sharp**: Section 5.1 states the PRM score threshold τ = 0.7 as a fixed setting without describing any validation procedure. Table 8 then shows accuracy as a function of threshold *on the test benchmarks themselves* (AIME24). The performance peak at exactly 0.70 is sharp: for DeepSeek-R1-Distill-Qwen-7B, accuracy drops from 66.7% at 0.70 to 43.3% at 0.71 — a 23.4-point swing across a 0.01 threshold change. This pattern holds across all five models and raises legitimate concerns about whether hyperparameters were selected using test-set feedback. The paper does not describe a held-out validation set, making it impossible for readers to assess to what degree the reported gains generalize beyond the specific threshold value. This undermines confidence in the main results.

- **The Underthinking Frequency (UF) metric is a heuristic proxy with no external validation**: Equation (1) defines UF_L as the count of thoughts shorter than L tokens. Short length does not necessarily indicate premature abandonment — a thought can be concise, correct, and complete. While the paper acknowledges this is "heuristic," the entire problem framing (Section 3) and all quantitative claims about prevalence, severity, and correlation with difficulty (Figures 1b, 2) rest on this unvalidated metric. The paper does not compare UF against any external measure of thought depth or human judgment of abandonment. Since the UF metric is used to motivate the method, its limitations weaken the conceptual foundation, even though the method's downstream accuracy results do not directly depend on it.

### Minor

- **No compute-matched baselines**: SmartSwitch introduces PRM calls and backtracking operations not present in vanilla inference. The only compared methods (vanilla inference, standard prompting, TIP) do not use comparable inference-time compute. While Tables 2–3 show SmartSwitch is actually *faster* overall (since it prunes wasteful exploration), a comparison against best-of-N sampling reranked by the same PRM, or against PRM-guided tree search with matched compute budget, would more cleanly attribute gains to the intervention logic rather than to the PRM signal itself. The paper's efficiency results partially address this, but a head-to-head compute-matched comparison would strengthen the causal claim.

- **No statistical significance or variance reported**: Pass@1 is estimated from 32 responses per problem on benchmarks with ~30 problems (AIME24, AIME25). Point estimates without confidence intervals or significance tests make it difficult to assess whether observed differences (e.g., the +7.0 gain for DeepSeek-R1-Distill-Qwen-14B on AIME24) are statistically reliable given the small number of test instances. This is common practice in the field but remains a limitation.

- **Conceptual limitation: PRM score signals plausibility, not incompleteness**: The intervention logic treats a high PRM score as evidence that a thought was "prematurely abandoned." However, a high PRM score indicates the step is plausible but says nothing about whether it is already complete. The method cannot distinguish "promising and unfinished" from "promising and finished." The "Always Intervene" ablation (Table 4) shows that selective intervention is better than indiscriminate intervention, but does not directly test whether interventions sometimes trigger on already-completed thoughts, which would waste compute on redundant deepening. This is not fatal given the net-positive results, but it limits the mechanistic interpretability of *why* the method works.

### Trivial

- The 200-token subdivision threshold (Section 5.1), the max-intervention cap of three, and the choice of L=100 for UF are stated without sensitivity analysis or justification. These are minor tuning details that do not affect core claims but would benefit from brief justification.

## Nice-to-Haves

- **Analysis of intervention outcomes**: Categorizing interventions into "deepening led to correct answer," "deepening was redundant," and "deepening led to error" would directly test whether the method recovers promising paths or merely perturbs generation. This would strengthen the mechanistic narrative.

- **Compute-matched baselines**: Best-of-N sampling reranked by the same PRM, with matched total inference budget, would isolate the contribution of the backtracking logic from the PRM signal.

- **Dynamic deepen prompts**: Instead of a single fixed prompt, generating context-sensitive hints referencing the specific content of the promising thought could improve intervention effectiveness and is a natural extension.

- **Threshold sensitivity on a validation set**: Plotting accuracy as a continuous function of threshold on a held-out set would demonstrate stability and justify the chosen value without test-set contamination concerns.

## Removed Points

These points are flagged to be removed from the main review; treat them with caution.

- **"Potential Score Threshold Tuned Directly on Test Benchmarks" as an accusation of deliberate cheating**: The harsh critic framed this as definitive evidence of test-set tuning. While the sharp threshold sensitivity and absence of a validation split are legitimate concerns (retained as a Major weakness above), the paper does not admit to test-set tuning and the threshold of 0.7 could potentially have been selected based on general PRM practice or pilot experiments. The concern is recharacterized as a methodological transparency issue rather than an accusation.

- **"The thought segmentation is performed by an LLM (DeepSeek-V3), which itself may be unreliable"**: The paper describes this as one segmentation strategy (v1 in Table 6) and compares it against simpler strategies. The adaptive paragraph strategy (v4) does not require an external LLM for segmentation and is the default. The criticism misreads the paper — the LLM-based segmentation is evaluated as an ablation, not used as the primary method.

- **"TIP's penalty hyperparameter is not tuned, and the method is deterministic"**: TIP is prior work (Wang et al., 2025). The paper compares against it as-is, which is standard practice. Criticizing the paper for not tuning a baseline's hyperparameters is not reasonable.

- **"The choice of L=100 tokens is arbitrary; no sensitivity analysis"**: The paper varies L continuously from 100 to 250 in Figure 1(b), showing that the underthinking prevalence pattern holds across thresholds. This *is* a sensitivity analysis. The choice of L=100 for detailed analysis is a fixed reference point, not an arbitrary claim.

- **"Figure 2b does not control for total response length"**: The paper reports UF as a count, not a rate, which indeed can be confounded by total length. However, the harsh critic's framing as a fatal flaw is overstated — the correlation between UF and incorrect answers is presented as an observation alongside other evidence, not as the sole proof of underthinking.

- **"No exploration of prompt variants" and "backtracking mechanism discards model state"**: These are scope-creep criticisms. A single fixed deepen prompt is a deliberate design choice for simplicity. Exploring prompt variants is future work, not a weakness.

- **Formatting/style nitpicks and typo complaints**: All removed per the hard rules. The original submission does not have these parser artifacts.

- **Missing appendix, proofs, or references**: Removed per hard rules — the parser strips these sections.

## Novel Insights

The finding that PRM-guided backtracking *simultaneously* improves accuracy and reduces inference cost (Tables 2–3) is genuinely interesting and counterintuitive. One might expect that injecting additional reasoning steps would increase cost; instead, SmartSwitch appears to prune wasteful thought-switching so effectively that it more than compensates for the overhead. This suggests that LongCoT models may spend a large fraction of their inference budget on shallow, unproductive exploration — an insight with implications beyond this specific method. The paper's observation that smaller models benefit disproportionately from SmartSwitch (e.g., 1.5B gains +16.7 on AIME25 vs. 32B gains +20.0) also hints that underthinking may be more severe in weaker models, suggesting a scaling relationship worth further study.

## Suggestions

- **Describe hyperparameter selection protocol**: Even if no formal validation split was used, describe how the threshold of 0.7 was chosen (prior work convention? small pilot? transferred from a different benchmark?). If a validation split was used, state it clearly and move the threshold sensitivity analysis to that split.
- **Add confidence intervals**: At minimum, report binomial confidence intervals for the main results in Table 1 given the ~30-problem benchmarks.
- **Add a compute-matched baseline**: A best-of-N baseline with the same PRM (using the same total PRM calls as SmartSwitch consumes on average) would strengthen the claim that the backtracking logic, not just the PRM signal, drives the gains.
- **Validate or replace the UF metric**: Either compare UF against human judgments of thought abandonment on a small sample, or acknowledge more prominently that UF is a rough proxy and reframe the Section 3 analysis as correlational rather than definitional.

## Score and Decision

### Anchor comparison

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `NFJK96X82a` (Rethinking Reward Models) | 6.00 | Stronger: more comprehensive multi-domain evaluation, theoretical analysis. Current paper is narrower in scope and has sharper methodological concerns. |
| `6QDFsYxtI1` (When More is Less) | 6.00 | Stronger: combines theory and empirics, cleaner experimental design with synthetic controls. Current paper has a novel method but less rigorous validation. |
| `qK4JKOu0Gx` (Scaling Reasoning Hop) | 5.50 | Comparable in ambition: identifies a phenomenon, proposes test-time intervention. That paper has stronger mechanistic analysis. Current paper has broader model coverage and larger gains. |
| `N5kWa3sRJt` (OptimalThinkingBench) | 5.33 | Different genre (benchmark paper). Current paper has a method contribution with empirical validation, comparable overall contribution level. |
| `aQZIpELFwp` (Are Reasoning LLMs Robust) | 4.50 | Similar: inference-time intervention study on reasoning models. That paper has cleaner experimental design. Current paper has a practical method with strong gains. |
| `YAhTj2VgBw` (InT) | 4.50 | Similar: method paper addressing reasoning failures. That paper has a cleaner conceptual framework but requires oracle access. Current paper is fully inference-time and plug-and-play. |
| `bXZCUh1MQp` (How Much Backtracking) | 4.00 | Weaker: limited to one model family and toy tasks. Current paper covers more models, real benchmarks, and shows stronger gains. |
| `hOF6s8Yfxs` (Hyperparameter Search on Test Set) | 2.67 | Much weaker: limited novelty, narrow domain. Current paper has a novel method with clear empirical contribution. |

The current paper's strengths — consistent accuracy gains across five model scales, simultaneous efficiency improvements, thorough ablations, and a genuinely training-free plug-and-play design — place it above the 4.0 anchors. The efficiency result (accuracy up AND cost down) is genuinely non-obvious and practically significant. However, the paper falls short of the 6.0 anchors due to (a) the sharp threshold sensitivity without documented validation, which undermines confidence in reported numbers, and (b) the UF metric being an unvalidated heuristic proxy that weakens the conceptual motivation. These are not fatal — the method works regardless of whether UF perfectly captures underthinking — but they prevent the paper from reaching the top tier. The paper is most comparable to the 5.0–5.5 range: a solid method contribution with strong empirical results and some methodological sloppiness that can be addressed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>