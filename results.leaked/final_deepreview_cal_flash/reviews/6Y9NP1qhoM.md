Now let me compose the final consolidated review.

## Summary

This paper tackles the problem of misinformation injection in LLM-based multi-agent systems (MAS) — where factually incorrect but semantically benign statements can evade conventional detection and derail collaborative tasks. The authors contribute (1) MISINFOTASK, a 108-task dataset spanning five reasoning categories, each with 4–8 plausible fallacious arguments and ground truth; and (2) ARGUS, a training-free defense framework that adaptively localizes suspicious communication channels via topological, semantic, and frequency signals, then deploys a goal-aware corrective agent using CoT-based reasoning. Experiments across 4 LLMs, 3 injection methods, and 5 topologies show that ARGUS reduces misinformation toxicity by ~28% and improves task success rates by ~10%, consistently outperforming two existing defenses.

## Strengths

1. **MISINFOTASK fills a genuine gap in misinformation-specific MAS evaluation.** The dataset is the first designed explicitly for studying misinformation (not overtly malicious content) injection in multi-agent systems. With 108 realistic tasks, 4–8 fallacious arguments per task, and five distinct categories (Conceptual Reasoning, Factual Verification, Procedural Application, Formal Language Interpretation, Logic Analysis), it addresses the identified gap that prior work relied on "simplistic question-answering tasks" and focused on jailbreak-style inputs (Section 3.1). The construction methodology (seed examples → LLM sampling → manual filtering) is sound.

2. **ARGUS delivers substantial and consistent gains across diverse attacks and LLMs.** On MISINFOTASK, ARGUS achieves on average a ~28% reduction in Misinformation Toxicity (MT) and a ~10% improvement in Task Success Rate (TSR) relative to attack-only baselines (Table 1). It outperforms both Self-Check and G-Safeguard in nearly every setting — for instance, with GPT-4o-mini under Tool Injection, ARGUS raises TSR from 68.75% (attack-only) to 89.66%, whereas G-Safeguard reaches only 70.46%. These results are aggregated over 4 core LLMs (GPT-4o-mini, GPT-4o, DeepSeek-V3, Gemini-2.0-flash), 3 injection methods, and 5 operational rounds.

3. **Adaptive localization effectively identifies misinformation channels.** The two-stage pipeline (topology-based initialization + dynamic re-localization using semantic relevance and frequency) achieves high accuracy in inferring the attacker's misleading goal: for Prompt Injection, the corrective agent's goal-identification accuracy reaches ~0.75–0.80 across categories (Figure 4). This enables targeted rather than blanket monitoring.

4. **Temporal analysis confirms ARGUS curtails misinformation propagation over rounds.** Figure 5 shows that without defense, MT increases steadily across rounds (e.g., ~4.5→~5.2 for Prompt Injection), whereas with ARGUS it declines (e.g., ~4.5→~3.2). This demonstrates the framework actively interrupts propagation rather than merely masking symptoms.

5. **Ablation studies verify the contribution of each core component.** Removing dynamic localization, CoT-based revision, or multi-turn correction each degrades performance (Table 2). ARGUS is also shown to transfer effectively across five distinct topologies (Chain, Full, Self-Determined, Circle, Star) in Figure 6, and is training-free.

## Weaknesses

### Fatal
None.

### Major

1. **Missing explicit definition of the weighted-score formula used in adaptive re-localization (α, β, γ).** The method section (Section 4.1.2) states that the comprehensive score Score^r(e) is "calculated as a weighted sum" of Score_topo(e), Score_rel(e), and Score_freq(e), but never provides the actual formula. The ablation study (Table 3) then references weights α, β, and γ without specifying which symbol corresponds to which score component. The rows "w/o α", "w/o β", "w/o γ" are therefore ambiguous — the reader cannot determine which ablation removes which factor. The text later notes that "information relevance is the most critical factor," but without the mapping, even this qualitative conclusion cannot be verified against the numbers. This is a basic methodological omission that renders Table 3 partially uninterpretable.

2. **Numerical claims in the abstract and introduction reference the same quantity differently without explanation.** The abstract states ARGUS achieves "an average reduction in misinformation toxicity of approximately 28.17%," while the introduction claims "reducing misinformation toxicity by approximately 38.24% across various core LLMs." Both numbers describe MT reduction but compute different things: 28.17% is the simple relative reduction from the attack-only baseline (average of per-attack-type reductions: 28.18%, 20.38%, 35.95%), while 38.24% measures the percentage of the attack-induced MT increase (from the vanilla baseline of 1.28) that ARGUS recovers. Neither calculation is wrong, but the paper never explains this distinction, creating an apparent contradiction that erodes trust in the quantitative claims. These two figures should be reconciled and their different bases explained.

3. **Table 1 subscripts are undefined.** Every non-attack-only cell in Table 1 carries a subscript (e.g., "3.73₁.₂₁" for GPT-4o-mini ARGUS under Prompt Injection). These are never explained in the caption or main text. They appear to be absolute differences from the Attack-only row (e.g., 4.94 − 3.73 = 1.21), not standard deviations — an unconventional choice. Without explicit labeling, a reader could mistake them for variance estimates, which are entirely absent from the table. The paper should either label these clearly as "Δ from Attack-only" or replace them with proper standard deviations (the caption of Figure 2 mentions three experimental trials).

### Minor

4. **Limited baseline comparison.** The paper compares ARGUS against only two defenses: Self-Check (a simple prompt-based method) and G-Safeguard (a graph-based method that sometimes *degrades* performance relative to attack-only — e.g., GPT-4o G-Safeguard under Prompt Injection achieves TSR 55.31% vs. Attack-only 56.25%). The paper would be substantially strengthened by including at least one additional baseline, such as a standalone verification agent or a fact-checking method, to isolate the benefit of the graph-based localization component from the benefit of having any corrective agent at all.

5. **Potential evaluation bias from LLM judge family overlap.** Both the MT and TSR metrics are scored by GPT-4o-2024-08-06, which belongs to the same model family as two of the four evaluated core LLMs (GPT-4o and GPT-4o-mini). The paper does not discuss whether this could systematically favor outputs produced by models from the same family, nor does it provide any calibration (e.g., human evaluation on a subsample, or a judge from a different model family) to validate the scoring. Given that the MT metric measures "semantic consistency" with a reference, using the same model family for both judge and core LLMs raises a plausible confound.

6. **No per-category breakdown of the MISINFOTASK dataset.** The paper claims the dataset covers five categories (Conceptual Reasoning, Factual Verification, Procedural Application, Formal Language Interpretation, Logic Analysis), but never reports how many tasks belong to each category. This makes the coverage claim unverifiable and prevents readers from assessing whether certain categories are over- or under-represented, which could affect the reported aggregate results.

7. **Corrective agent's own robustness is not examined.** ARGUS depends on a corrective agent (a_cor) that reads communication logs and performs CoT-based reasoning to detect and rectify misinformation. The paper does not analyze what happens if the attacker can compromise the logs that a_cor reads, or feed it misinformation that matches its own knowledge gaps. This is an important threat vector that should at least be discussed, given that the defense introduces a new point of failure.

### Trivial
None.

## Nice-to-Haves

- **Report key hyperparameter values in the main text.** The number of monitored edges *k* (Equations 4, 9), the similarity threshold θ_sim (Equation 6), and the TSR threshold θ_m (Equation 1) are important for reproducibility. If they appear in the appendix, a cross-reference would help.
- **Provide a cost/latency analysis.** ARGUS runs an LLM-based corrective agent on multiple channels over multiple rounds; a token count or wall-time comparison with baselines would help readers assess practicality.
- **Add human evaluation on a subsample.** Even 20–30 samples rated by humans would strengthen confidence that MT and TSR scores reflect genuine task outcomes rather than judge agreement patterns.

## Removed Points

- **"Missing critical hyperparameters (k, θ_sim, θ_m)":** These may be reported in the appendix (which was stripped by the parser); the hard rule on missing appendix content applies. Moved to Nice-to-Haves.
- **"Figure 2 is confusing / shows one point per method":** The figure caption explicitly states "data points represent the outcomes from three independent experimental trials," and multiple points per method are visible in the scatter plot. The reviewer appears to have misread the figure.
- **"Dataset size (108 tasks) is small":** For a specialized, manually curated dataset of misinformation injection scenarios, 108 tasks is a reasonable scale. This is a generic criticism without a concrete standard for comparison.
- **"Threat model is narrow (single agent compromise, injection only at start)":** The paper explicitly scopes its threat model in Section 3.3; the limitations section acknowledges this. This is a scope choice rather than a flaw.
- **"Paper claims 'pioneering evaluation' – overstated":** This is a judgment call about framing; the paper does cite prior work and positions its contribution relative to existing gaps. Not a substantive weakness.
- **Various formatting/style nitpicks (font sizes, figure readability, typos):** These are likely parser artifacts and are removed per the hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension well: the paper proposes a genuinely useful dataset and defense framework for an underexplored threat (covert misinformation in MAS), and its evaluation is reasonably broad across LLMs, attacks, and topologies. The main insight from the reviews is that the paper's credibility is undermined not by flawed methodology but by inconsistent and incomplete reporting — the numerical discrepancy between abstract and introduction, the undefined ablation weights, and the unexplained table notation. These are presentation issues, not fatal methodology errors, but they are severe enough that a reader cannot fully trust or replicate the results in the current form.

## Suggestions

1. **Reconcile the 28.17% and 38.24% numbers** by adding a sentence explaining that 38.24% measures the fraction of the attack-induced MT increase (relative to the vanilla baseline) that ARGUS eliminates, while 28.17% measures the simple relative reduction from the attack-only MT. Keeping both is fine, but the distinction must be explicit.
2. **Provide the exact formula for Score^r(e)** with α, β, γ explicitly mapped to Score_topo, Score_rel, and Score_freq (e.g., Score^r(e) = α·Score_topo(e) + β·Score_rel(e) + γ·Score_freq(e)). Also state the default values used.
3. **Rename the Table 1 subscripts** (e.g., "Δ" instead of an unlabeled subscript) and add a footnote: "Subscript values indicate the absolute difference from the corresponding Attack-only row." Better yet, replace them with standard deviations across the three experimental trials mentioned in Figure 2.
4. **Add at least one stronger baseline** — a simple fact-checking agent that queries the core LLM's knowledge without graph-based localization — to isolate the benefit of the spatial localization component.
5. **Acknowledge and discuss the LLM judge family overlap**, or supplement with a small human evaluation or a judge from a different model family to validate the scoring trends.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Human Score | Round | Comparison |
|--------|----------------|-------|------------|
| acDwoHrwZ8 — MAS with Social Hierarchy | 3.00 | R1 | Much weaker; narrower scope, less rigorous evaluation |
| cSnbM9SIJJ — Very Large-Scale MAS Simulation | 3.00 | R1 | Different topic (infrastructure, not security); weaker contribution |
| E2CR6hmV1I — Multi-Agent Learning (CollabUIAgents) | 3.00 | R1 | Different topic; weaker evaluation |
| Bp2axGAs18 — Resilience of MAS with Malicious Agents | 5.20 | R1,R2 | Most similar anchor. Current paper has a dedicated dataset + more sophisticated defense + broader evaluation. Marginally stronger. |
| NAbqM2cMjD — Prompt Infection | 5.20 | R1,R2 | Also closely related. Current paper has stronger method contribution (dataset + defense vs. attack-only) and broader LLM coverage. Slightly stronger. |
| EP6n8LCEK6 — Prejudice in D2C MAS | 5.50 | R2 | Different topic (social bias); comparable execution quality |
| gKM8wwsTOg — AgentMonitor | 4.80 | R2 | Simpler method (XGBoost-based), less novel. Current paper is clearly stronger in methodological contribution. |
| V4y0CpX4hK — Agent Security Bench | 6.25 | R2 | More comprehensive in scope (10 scenarios, 400+ tools, 90K tests) and more polished. Current paper is weaker along these dimensions. |
| YauQYh2k1g — Adversarial Robustness of Multimodal Agents | 6.25 | R2 | Different domain (web agents); comparable rigor but more polished presentation |

**Round 1 bracket:** The paper sits between the weak (~3.0) and strong (~8.0) anchors. The most topically relevant anchors in the middle band (5.0–5.5) provide the best comparison.

**Round 2 narrowing:** The paper is clearly stronger than AgentMonitor (4.80) and the 5.20 anchors (Resilience of MAS, Prompt Infection) due to its dedicated dataset, more sophisticated defense, and broader evaluation across 4 LLMs. It is weaker than Agent Security Bench (6.25) which is more comprehensive and polished. The paper's core contributions are solid, but the reporting issues (unresolved numerical inconsistency, undefined αβγ mapping, unexplained table notation) prevent it from reaching the 6+ level.

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>