## Summary

ARPO (Agentic Reinforced Policy Optimization) is a reinforcement learning algorithm for training multi-turn LLM-based agents with tool use. Its core contribution is an entropy-based adaptive rollout mechanism that detects high-entropy moments following tool-call feedback and triggers branched sampling at those steps, combined with an advantage attribution scheme applied over the resulting mixed-prefix trajectories. The paper evaluates ARPO across 13 benchmarks spanning math, knowledge-intensive QA, and deep search, reporting consistent gains over trajectory-level baselines (GRPO, REINFORCE++, DAPO) while using roughly half the total tool-call budget.

---

## Strengths

- **Consistent empirical performance across 13 benchmarks and two model families.** Table 1 and Table 2 show ARPO outperforms trajectory-level baselines by an average of ~4% on 10 math/knowledge benchmarks and by ~6% on GAIA and WebwalkerQA for deep search. The breadth across Qwen and Llama architectures meaningfully reduces the likelihood of cherry-picked results.

- **Strong sample efficiency on deep search tasks.** ARPO trained on only 1k RL samples achieves 43.7% on GAIA and 10.0% on HLE with Qwen3-14B, competitive with or exceeding workflow-driven agents and much larger models (GPT-4o: 2.0% on HLE, DeepSeek-R1-671B: 8.6% on HLE). This is a concretely striking result.

- **Pass@K scaling analysis (Figure 6).** The paper documents monotonic improvement from Pass@1 → Pass@3 → Pass@5 for ARPO-aligned models (e.g., Qwen3-14B GAIA: 43.7% → 61.2%), demonstrating that ARPO improves the quality of the entire output distribution, not just greedy decoding.

- **Concrete ablation of soft vs. hard advantage (Figure 5).** The paper provides empirical justification for the design choice of soft advantage estimation, showing it yields consistently higher and more stable reward curves compared to hard advantage during training.

---

## Weaknesses

### Fatal
None.

### Major

- **No direct validation that entropy-guided branching outperforms uniform branching.** The paper's central thesis is that high-entropy steps after tool calls are the right places to branch. But the experiments never include a controlled comparison: ARPO with entropy-triggered branching vs. an ablation that branches uniformly at every tool-call step (or randomly). Without this, the entropy signal might be doing no selective work — ARPO's gains might be attributable entirely to *branched rollout structure* (step-level exploration at any tool-call step) rather than the entropy-guided *selection* of which steps to branch at. Figure 2 suggests entropy is broadly elevated after most tool calls, which makes the discrimination criterion potentially vacuous in practice. This is the single most important missing experiment.

- **Tool-call efficiency claim (Figure 7a) may confound shared-prefix reuse with genuine efficiency.** ARPO branches trajectories at intermediate steps, meaning branched paths *inherit* earlier tool-call results without re-executing them. GRPO samples M fully independent trajectories, each requiring all tool calls from scratch. Consequently, ARPO will have fewer total tool invocations by construction under the same number of sampled paths, irrespective of any entropy-based selection. The paper attributes the ~50% tool-call reduction to "ARPO's entropy-based adaptive rollout strategy" (§5.2), but this interpretation is only defensible if the comparison controls for prefix reuse — e.g., a budget-matched comparison where GRPO is given credit for hypothetically shared prefixes, or where the metric is wall-clock cost rather than raw tool invocations. As written, the efficiency claim may partially or largely reflect accounting differences in trajectory structure.

### Minor

- **The soft advantage contribution effectively reduces to GRPO on branched rollouts.** Section 3.2 explicitly states "we retain the original GRPO loss formulation" and demonstrates (Equation 4) that shared prefix tokens already receive aligned importance weights under GRPO's importance sampling ratio. This is a correct and useful insight, but it means the "soft advantage" is not a new loss function — it is the observation that GRPO implicitly handles the shared/individual token distinction when the rollout contains branched trajectories. The paper presents hard and soft advantage as co-equal algorithmic contributions, but the soft setting's novelty is largely in the rollout design, not in the update rule.

- **The Generalized Policy Gradient (GPG) Theorem (§3.3) is a trivial reformulation.** Treating a macro-action (contiguous token segment) as the atomic action under the standard policy gradient theorem yields the GPG result by substitution. The paper itself notes the theorem "encompasses the traditional Policy Gradient Theorem as a specific instance," which confirms that this is a re-parameterization rather than a new result. Labeling it a "theorem" and using it as "theoretical justification" for the method overstates its contribution. It provides naming convenience but no additional theoretical insight.

- **Core hyperparameters (α, β, τ, Z, N, M) are not analyzed in the main text.** These six parameters jointly control when branching fires and how many branches are spawned — they are central to the method's behavior. The paper defers sensitivity analysis to Appendix A.2. Given that τ and β together determine the branching frequency, their interaction with the "half tool-call budget" result and performance gains is a first-order concern for practical use.

### Trivial

- **DBSCAN clustering parameters (ε, minPts) are not reported for Figure 7b.** The 54-vs-48 cluster count comparison cannot be reproduced or evaluated without these. Given the relatively small difference (12.5%), the result's sensitivity to clustering parameters is non-trivial.

- **The abstract's claim to "pioneerly quantify token entropy variation of LLM during agentic reasoning"** overstates novelty. The paper's own related work cites prior entropy-based RL studies (Wang et al., 2025b/c; Cheng et al., 2025; Zheng et al., 2025b) that analyze entropy in LLM generation. The novel element is applying it to multi-turn tool-call feedback in an agentic RL setting — a worthwhile distinction, but not "pioneering" entropy measurement.

---

## Nice-to-Haves

- A direct ablation comparing ARPO vs. "random branching at every tool-call step (same total branch budget)" would be the highest-value experiment to add, directly validating whether the entropy selection criterion is doing useful work.
- Budget-equivalent comparison: measure total tool-invocation cost for GRPO and ARPO while holding constant either (a) number of unique trajectories or (b) wall-clock compute, to cleanly separate the structural prefix-reuse effect from the entropy-guided selection effect.
- Variance across multiple training seeds for at least one setting, especially for small-N benchmark splits (e.g., GAIA Level-3) where single-run comparisons may not be reliable.
- A main-text figure showing empirical branching frequency (how often P_t > τ triggers) across a representative dataset to validate that branching is selective and not universal.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: Word cloud analysis (Figure 2) uses generic tokens** — the criticism that tokens like "now," "information," "find" are high-entropy in any generative context is technically valid but too nitpicky. The word cloud is illustrative rather than evidentiary; the entropy *curves* (not word labels) are what motivate branching. This is a presentation caveat, not a methodological flaw.

- **Harsh critic: O(n log n) complexity claim** — The paper does include a footnote caveat about "neglecting entropy calculation overhead" and frames this as a range "between O(n log n) and O(n²)." The lower bound is context-dependent (branching at few steps). This is weak but not falsifiable given the paper's stated caveats. Demoted rather than retained as it anchors on an unstated assumption about branching rate.

- **Strength Finder: "Structured and diversified exploration space" (Figure 7b)** — Retained but downgraded: the 54 vs. 48 DBSCAN clusters is a weak signal with unreported hyperparameters. Not promoted as a standalone strength.

- **Strength Finder: "Theoretical grounding via GPG Theorem"** — Removed as a strength; the theorem is a trivial reformulation (retained as a Minor weakness instead).

- **Harsh critic: No variance/confidence intervals** — Removed as a standalone weakness since single-run evaluation is the norm at this scale in the agentic RL community.

---

## Novel Insights

The most genuinely novel observation is the combination of two things: (1) entropy reliably spikes in the first 10–50 tokens after tool-call feedback (validated across two tool types with distinct entropy profiles — search vs. Python interpreter), and (2) trajectory-level RL methods structurally ignore this signal by committing to complete rollout comparisons. The inference that this creates an exploitable seam for step-level exploration is intuitive and practically supported by the empirical results. What remains unverified is whether the entropy *magnitude* is doing any discriminative work beyond simply identifying tool-call boundaries — answering this would substantially sharpen the paper's theoretical story.

---

## Suggestions

1. **Add the random-branching ablation.** Run a version of ARPO that branches at every tool-call step (ignoring entropy) with the same total branch budget. If ARPO with entropy guidance beats this, the entropy selection is validated; if not, the contribution simplifies to "branched rollout structure for agentic RL," which is still a useful finding.

2. **Reframe the efficiency claim.** Clearly report whether Figure 7a counts each tool invocation once regardless of how many branched paths share it, or whether each branch that reuses a prior tool call is counted separately. Either choice is fine, but the current description leaves the efficiency interpretation ambiguous.

3. **Provide a main-text sensitivity figure** for τ (branching threshold) showing how performance changes across a range of values — this directly addresses the concern about hyperparameter sensitivity without requiring a full Appendix.

4. **Tone down the theoretical framing.** Rename the "GPG Theorem" to a "Proposition" or "Observation" in the main text to avoid overstating the theoretical contribution while retaining the conceptual utility of the macro-action framing.

---

**Axes Summary:**
- *Originality*: Moderate — entropy analysis in LLM reasoning is established; applying it to guide branching in multi-turn agentic RL training is the novel combination.
- *Importance*: High — agentic RL for tool-using LLMs is an active, high-stakes problem area.
- *Claims supported*: Moderate — empirical performance claims are well-supported; the mechanism attribution (entropy's selective role) is asserted but not isolated.
- *Soundness*: Moderate — broad benchmarking is convincing; key ablation (random branching baseline) is missing.
- *Clarity*: Good — the paper is well-organized and the algorithm is described clearly; some overclaiming in the abstract and §3.3.
- *Community value*: High — code is released; practical insights for agentic RL practitioners are concrete.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>