## Summary

This paper introduces MISINFOTASK, a dataset of 108 realistic tasks with curated misinformation scenarios for evaluating multi-agent system (MAS) vulnerability to covert misinformation injection, and ARGUS, a training-free defense framework that adaptively localizes and rectifies misinformation through goal-aware reasoning. ARGUS monitors critical communication edges using topological centrality, semantic relevance, and communication frequency, then deploys a corrective agent that uses chain-of-thought reasoning to identify and persuasively correct misinformation. Experiments across four LLMs, three injection methods, and five topologies show ARGUS consistently reduces misinformation toxicity and improves task success rates.

## Strengths

- **Targeted dataset contribution**: MISINFOTASK fills a genuine gap by providing 108 tasks with 4–8 plausible fallacious arguments per task and ground truths across five reasoning categories, specifically designed for evaluating covert misinformation injection in MAS (Section 3.1). This is a concrete resource for the community.

- **Comprehensive empirical evaluation**: The paper tests ARGUS across four distinct LLM backends (GPT-4o-mini, GPT-4o, DeepSeek-V3, Gemini-2.0-flash), three injection methods (Prompt Injection, RAG Poisoning, Tool Injection), and five topological configurations (Figure 6, Table 1). This breadth provides credible evidence for generalizability.

- **Insightful longitudinal analysis**: The per-round MT trends (Figure 5) empirically demonstrate that ARGUS does not merely block initial misinformation but actively curtails its propagation over successive rounds, illustrating a corrective rather than merely preventative effect.

- **Transparent ablation studies**: Tables 2–3 cleanly attribute performance to individual components (dynamic localization, CoT revision, multi-turn correction) and localization hyperparameters, with the ground-truth upper bound providing a useful reference point.

- **Novel adaptive localization mechanism**: The integration of topological betweenness centrality with dynamic semantic relevance and communication frequency (Section 4.1) is a concrete algorithmic contribution, validated by goal-inference accuracy measurements (Figure 4).

## Weaknesses

### Fatal

None.

### Major

- **Unvalidated LLM judge for primary metrics**: Both Misinformation Toxicity (MT) and Task Success Rate (TSR) are measured exclusively by an LLM judge (GPT-4o). No human evaluation, calibration study, or inter-annotator agreement is reported. The MT metric in particular requires the judge to score semantic consistency between system output and a misinformation goal — a subtle judgment that may be biased, especially when the defense rewrites or argues against the misinformation. While LLM-as-judge is common practice, relying on it for the paper's two core metrics without any validation weakens confidence in the numeric results. This is addressable with a human correlation study on a subset of tasks.

### Minor

- **No direct measurement of misinformation detection precision/recall**: The paper reports goal-inference accuracy of the corrective agent (Figure 4), but does not evaluate whether the localization step (Section 4.1) actually selects edges carrying contaminated messages, or whether the corrective agent correctly distinguishes misinformation from innocuous content at the sentence level. The ablation removing dynamic localization (Table 2) provides indirect evidence of its utility, but direct detection metrics would strengthen the mechanistic validation.

- **Limited baseline comparison**: The paper compares ARGUS against Self-Check and G-Safeguard — both reasonable MAS defenses — but does not include a simpler corrective-agent baseline (e.g., an agent that checks all messages without adaptive localization or goal-aware reasoning). The ablation of dynamic localization ("w/o Dynamic Local.") partially serves this role, but an external comparison to multi-agent debate approaches (which the paper itself cites, Chern et al., 2024) would better situate ARGUS within the defense landscape. This does not invalidate the results but limits the strength of the comparative claim.

- **Unusually small reported deviations for TSR**: Table 1 reports TSR standard deviations as low as 0.12% (GPT-4o-mini ARGUS, Prompt Injection). These values are suspiciously small for a metric computed over 108 tasks and warrant clarification — they may be standard errors or computed over a non-standard aggregation.

### Trivial

- The abstract claims "average reduction in misinformation toxicity of approximately 28.17%" while the introduction cites "approximately 38.24%." These numbers are computed across different aggregations (the former across all models, the latter across a potentially different set), creating minor confusion. Clarifying which aggregation each number refers to would help.

## Nice-to-Haves

- **Sensitivity analysis for LLM knowledge limitations**: The paper acknowledges (Section 7) that ARGUS addresses misinformation about knowledge resident in the agents' core LLMs and that time-sensitive external knowledge is out of scope. Testing ARGUS in a setting where the base LLM holds a false belief would quantify the practical risk of this scope limitation and strengthen the paper.

- **Cost and latency analysis**: Since ARGUS introduces additional computation (a corrective agent monitoring k edges and performing multi-stage CoT reasoning), even a coarse measurement of extra tokens and inference steps would inform practical adoption.

- **A concrete end-to-end example**: A walkthrough of the full pipeline — from an injected misinformation sentence through localization, the corrective agent's reasoning, the corrected message, and the final output — would make the method's behavior and failure modes more interpretable.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing details for reproducibility (Issue 3 from Harsh Critic)**: The paper explicitly defers parameter values (k, θ_sim, LLM temperature, complete prompts) to Appendices B and G. Per review policy, appendix-deferred content is assumed to exist in the original submission. The parser stripped the appendix; this is not an author error.

- **Method implicitly assumes the base LLM possesses correct world knowledge (Issue 5 from Harsh Critic)**: The paper explicitly defines misinformation as content contradicting the LLM's parametric knowledge (Section 2.3) and acknowledges the limitation regarding external/time-sensitive knowledge (Section 7). This is a stated scope, not a hidden assumption. Moved to Nice-to-Haves as a suggested extension rather than a weakness.

- **Strength Finder generic strengths**: Several Strength Finder items (e.g., "this paper addressed an important problem") were dropped as generic claims lacking specific evidence. The retained strengths above all include concrete citations to the paper.

## Novel Insights

The round-by-round MT analysis (Figure 5) provides a genuinely novel empirical observation: in attack-only settings, misinformation toxicity escalates monotonically across rounds, but under ARGUS, it decreases round by round. This demonstrates that ARGUS does not merely filter initial injections but actively reverses the contamination trend over time — a temporal corrective dynamic that distinguishes it from one-shot filtering defenses. This insight is valuable for understanding defense design in iterative multi-agent communication settings.

## Suggestions

- Add a human correlation study for the LLM judge on a representative subset of tasks (e.g., 20–30), reporting correlation coefficients and agreement rates for both MT and TSR. This would substantially strengthen the paper's evidential foundation at modest annotation cost.

- Include precision/recall metrics for the localization step by labeling which edges actually carried misinformation in a subset of test runs. This would validate the core mechanism.

- Clarify the TSR standard deviation computation in Table 1 and consider reporting standard deviations over tasks rather than (what appears to be) standard errors.

- Add a simple baseline where a corrective agent monitors all edges without adaptive localization or goal-aware reasoning, to isolate the contribution of ARGUS's specific design choices over a naive monitoring approach.

---

**Anchor comparisons:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| Bp2axGAs18 (MAS Resilience with Malicious Agents) | 5.20 | ARGUS is stronger: more focused contribution, cleaner experimental design, ablation studies, and a dataset contribution that Bp2axGAs18 lacks. |
| NAbqM2cMjD (Prompt Infection) | 5.20 | ARGUS is stronger: proposes a defense alongside attack analysis, whereas Prompt Infection primarily introduces an attack. |
| kgZFaAtzYi (Cracking the Collective Mind) | 3.50 | ARGUS is clearly stronger: comprehensive evaluations across models/topologies/attacks, a real defense contribution, and a dataset, vs. kgZFaAtzYi's limited two-agent setting and poor generalizability. |
| STpxO1Siaq (Defense via Debate) | 3.50 | ARGUS is clearly stronger: broader evaluation scope and more rigorous ablation. |
| D6zn6ozJs7 (MMFakeBench) | 6.60 | D6zn6ozJs7 has human evaluation of its benchmark and stronger metric validation. ARGUS has a defense contribution on top of its dataset but lacks human validation. ARGUS is slightly weaker. |
| leSbzBtofH (AutoAdvExBench) | 6.17 | Comparable in experimental rigor and contribution quality. leSbzBtofH has clearer metric definition (no LLM judge), ARGUS has a broader evaluation scope. Roughly equivalent. |
| 5kMwiMnUip (NEMESIS Jailbreaking) | 1.40 | ARGUS is vastly stronger across all dimensions. |

The paper sits above the 5.20-tier MAS papers due to its dataset contribution, systematic ablation, and longitudinal analysis, but below the 6.60 benchmark paper due to the unvalidated LLM judge and absence of direct detection metrics. Positioned closest to leSbzBtofH (6.17) in overall contribution quality.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>