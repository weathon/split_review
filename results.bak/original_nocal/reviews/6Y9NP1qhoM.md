Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me synthesize the final review.

---

## Summary

This paper addresses covert misinformation injection in LLM-based Multi-Agent Systems (MAS). It contributes two main artifacts: (1) **MISINFOTASK**, a dataset of 108 realistic tasks with paired fallacious arguments and ground truths designed for red-teaming misinformation in MAS, and (2) **ARGUS**, a training-free two-stage defense framework that adaptively localizes critical communication channels (using topological importance, semantic relevance, and frequency) and performs goal-aware Chain-of-Thought rectification. Experiments across 4 LLM families, 5 topologies, and 3 injection methods show ARGUS reduces MT by ~28% and improves TSR by ~10% on average over attack-only baselines.

## Strengths

- **Novel, purpose-built dataset for misinformation in MAS (Section 3.1).** MISINFOTASK fills a genuine gap — most existing work on MAS information injection focuses on overt jailbreaks, not covert misinformation. The dataset includes 108 tasks with 4–8 fallacious arguments and ground truths per task, constructed via LLM generation with human filtering, covering five reasoning categories.

- **Consistent empirical advantage across a broad experimental sweep.** Table 1 shows ARGUS achieves the best (highest) TSR in all 12 model×attack combinations, and the best (lowest) MT in 10 of 12 (one tie). This consistency across GPT-4o-mini, GPT-4o, DeepSeek-V3, and Gemini-2.0-flash, and across Prompt Injection, RAG Poisoning, and Tool Injection, provides substantive evidence that the framework generalizes beyond a single setting.

- **Principled, composable localization mechanism (Section 4.1).** The framework combines edge betweenness centrality (topological), sentence-level semantic relevance to inferred misinformation goals (semantic), and channel communication frequency (Section 4.1.2, Eqs. 5–9). Table 3's hyperparameter ablation confirms all three components contribute, with information relevance being the most critical.

- **Training-free and modular design.** ARGUS requires no fine-tuning or dedicated classifiers, making it practical to deploy on top of existing MAS. The ablation study (Table 2) isolates the contribution of dynamic localization, CoT revision, and multi-turn correction, with each component's removal degrading performance.

- **Generalization across MAS topologies (Figure 6).** ARGUS reduces MT under all five tested topologies (Chain, Full, Self-Determined, Circle, Star), demonstrating robustness to structural variation.

## Weaknesses

### Major

- **LLM-as-judge evaluation without human validation or calibration (Section 5.1, Eq. 1).** Both MT and TSR rely entirely on GPT-4o scoring semantic consistency. There is no human evaluation of a sample of outputs, no calibration study comparing the LLM judge's scores against human judgments or objective task success, and no analysis of the judge's reliability. While LLM judges are widely used, the lack of any validation against ground truth is a significant gap — especially given that (a) the MT metric measures alignment with an inferred "misinformation intent-driven goal" rather than objective correctness, and (b) the paper's central quantitative claims (28.17% MT reduction, 10.33% TSR improvement) rest entirely on this single unvalidated judge. The authors should at minimum report agreement statistics on a held-out human-annotated sample.

### Minor

- **No statistical significance testing for main comparisons (Table 1).** Several improvements, while directionally consistent, are modest in magnitude (e.g., DeepSeek-V3 under Prompt Injection: TSR improvement of +2.69 with SD of 2.69). Without confidence intervals, p-values, or effect-size reporting, the reader cannot assess whether these improvements are robust or within sampling noise. The standard deviations reported in Table 1 appear to be task-level (within-group) variance, which is not the information needed for significance testing of mean differences.

- **Goal-inference accuracy is moderate and downstream effects are unanalyzed (Figure 4, Section 4.2).** The corrective agent infers the misinformation's intent-driven goal with accuracy ranging from ~0.50 to ~0.80 depending on attack type. When this inference is wrong, adaptive re-localization (which depends on semantic similarity to the inferred goal) may direct monitoring toward irrelevant channels, and rectification may itself inject errors. The paper does not analyze how goal-inference errors cascade into localization failures or incorrect corrections. This is partially mitigated by the ablation showing ARGUS with dynamic localization outperforms the "w/o Dynamic Local." variant, but a direct analysis of the inference-to-defense failure chain would strengthen the paper.

- **Baseline coverage is limited (Section 5.1).** Only two baselines are compared: Self-Check (a simple prompt-level reflection) and G-Safeguard (GNN-based pruning). A consensus-based defense (e.g., multi-agent debate/voting) or a retrieval-augmented fact-checking baseline (querying a trusted external source) would establish a more meaningful bar. The paper's claim of being a "unified shield" is less supported without comparison to alternative defense paradigms.

- **Temporal analysis lacks key experimental detail (Figure 5).** The figure caption and surrounding text do not specify which core LLM was used for the round-by-round MT tracking, and no error bars or uncertainty estimates are provided. This limits the interpretability of the claim that ARGUS "reverses" the increasing MT trend.

### Trivial

- "w/o Multi-Turn Corr." in Table 2 is not explicitly defined in the ablation text; it is inferable from context (Section 4.2's multi-round rectification) but should be stated.

## Nice-to-Haves

- Quantify the computational overhead of ARGUS (extra LLM calls per round, latency, cost). The paper acknowledges this as a limitation (Section 7) but provides no numbers.
- Report false-positive/false-negative rates: how often does ARGUS incorrectly flag correct information or miss actual misinformation?
- Scale MISINFOTASK beyond 108 tasks to strengthen the empirical base.
- Provide qualitative case studies of successful and failed rectifications.

## Removed Points

These points from the reviewers were removed with justification:

1. **"Improvement is small/high-variance and cherry-picked"** — removed because the critic's specific example (Gemini-2.0-flash: "Self-Check yields lower MT than ARGUS") is **factually wrong**: ARGUS MT=3.60 < Self-Check MT=4.02 < G-Safeguard MT=3.89. The critic also misreads standard deviations (task-level variance) as run-level variance for significance claims. The improvements are directionally consistent across 12/12 TSR settings, which is the relevant evidence.

2. **"Injection methods inject explicit false statements — not more covert than typical attacks"** — removed because the paper's definition of covertness is about semantic framing (benign-sounding but factually wrong) versus overt malicious content, not about the injection method. The critic conflates the two.

3. **"108 tasks is very small"** — removed as a generic scope criticism that does not threaten the core claims. The dataset is specialized and task generation is costly; 108 tasks with 4-8 fallacious arguments each is reasonable for a first dataset in this niche.

4. **"Figure 5 without error bars and only for a single model (presumably?)"** — the lack of error bars is retained as a minor weakness. The "single model" speculation is removed because it's not verified from the paper and the critic adds "presumably" acknowledging uncertainty.

5. **"Self-reinforcing failure loop" concern about goal inference** — the critic's framing as a "structural" issue is too severe given that the ablation (Table 2) shows the full system (with this loop) outperforms "w/o Dynamic Local." (without it), suggesting the mechanism is net beneficial even with imperfect inference. Retained as a minor weakness about unanalyzed cascading effects.

6. **"Weaknesses that would, if true, invalidate the paper's core contribution"** — the substantive criticisms (LLM judge, baselines, significance) are retained at appropriate severity; none are fatal.

## Novel Insights

None beyond the paper's own contributions. The reviews surface standard areas-of-concern (evaluation validation, baseline coverage) but do not identify a weakness or strength not already acknowledged in the paper itself. The harsh critic's framing of the LLM judge issue as "circular" is partially novel but overstated: the judge (GPT-4o) is not the same model as the agents it evaluates (which include GPT-4o-mini, DeepSeek-V3, Gemini); the circularity concern would only apply to the GPT-4o-as-agent condition, which is one of four tested.

## Suggestions

1. **Validate the LLM judge on a human-annotated sample.** Annotate 50–100 outputs from the MISINFOTASK experiments with human judgments of MT and task success, report agreement (Cohen's κ or Spearman correlation), and use this to calibrate the threshold θ_m for TSR. This single addition would substantially strengthen the credibility of all quantitative claims.

2. **Add at least one stronger baseline.** A multi-agent debate/consensus baseline (e.g., Chern et al., 2024, which the paper cites in Related Work) or a simple "verify with web search tool" baseline would provide a more meaningful comparison point and better support the claim that ARGUS is a "unified shield."

3. **Report effect sizes and confidence intervals** for the main ARGUS vs. attack-only and ARGUS vs. best-baseline comparisons in Table 1, to clarify which improvements are robust.

4. **Analyze goal-inference cascading effects.** Show how localization accuracy and final MT/TSR vary with goal-inference correctness, to understand when and how the defense degrades.

5. **Specify the model used in Figure 5** and add error bars or confidence bands to the temporal trends.

## Score and Decision

The paper tackles a genuinely understudied problem (covert misinformation as distinct from jailbreaks), contributes a useful dataset and a principled, training-free defense framework, and evaluates it across a commendably broad set of conditions (4 LLMs, 5 topologies, 3 attack types, 3 injection methods). The main weakness — sole reliance on an unvalidated LLM judge — is significant but not fatal, as the task ground truths are human-curated and the pattern of results is consistent across diverse settings. With human validation of the judge, stronger baselines, and better statistical reporting, this would be a strong paper. In its current form, the contribution and evidence are solid enough to merit acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>