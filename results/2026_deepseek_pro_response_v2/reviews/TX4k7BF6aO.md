Now I have a clear picture. Let me finalize the review.

**Calibration summary:**

Round 1 bracketing placed ARPO between EAST (4.75) and REFUEL (6.50). Round 2 narrowed to:

| Anchor | Score | Decision | Comparison |
|--------|-------|----------|------------|
| StepTool (PNHjoWcQje) | 5.50 | Reject | Step-grained RL for tool learning. Less novel (standard RL + reward shaping), weaker results. ARPO is clearly stronger. |
| TPO (O0sQ9CPzai) | 6.33 | Accept | Multi-branch preference optimization for reasoning trees. Similar framing of multi-branch exploration. ARPO has broader benchmarks (13 vs 4), better motivating analysis, but more overclaiming. Comparable quality. |
| REFUEL (cVyELMpMRS) | 6.50 | Accept | Multi-turn RLHF with elegant algorithm. Stronger theory, cleaner contribution. ARPO has broader empirical validation but weaker theoretical framing. |

ARPO sits between StepTool (5.50) and TPO (6.33). Its empirical breadth and novel rollout mechanism put it above StepTool; its overclaiming on advantage attribution and GPG theorem, plus the missing entropy-specific ablation, keep it below TPO and REFUEL. **Score: 6.0, Accept.**

---

## Summary

ARPO proposes an RL algorithm for training multi-turn LLM-based tool-using agents. The core idea is an entropy-based adaptive rollout mechanism: the model branches additional partial trajectories at tool-call steps where token entropy spikes, rather than relying solely on trajectory-level sampling as in standard GRPO. The method is motivated by a pilot study showing that LLM token entropy reliably increases after tool calls (Figures 2, 4). ARPO couples this rollout scheme with advantage attribution estimation and is evaluated across 13 benchmarks spanning mathematical reasoning, knowledge-intensive QA, and deep search, consistently outperforming GRPO, REINFORCE++, and DAPO.

## Strengths

- **Well-motivated by empirical entropy analysis (§2):** The pilot study quantifies token entropy across tool-call boundaries using two agent types (search engine and Python interpreter), showing a consistent spike in the first 10–50 tokens after tool calls. This provides a principled, data-driven motivation for branching at tool-call steps rather than treating all steps uniformly.

- **Consistent empirical gains across diverse benchmarks (Tables 1, 2):** ARPO outperforms GRPO, REINFORCE++, and DAPO on the average across 10 mathematical and knowledge-intensive reasoning tasks on both Llama3.1-8B (55.3 vs. 51.1) and Qwen2.5-7B (58.3 vs. 56.5). On deep search tasks, ARPO-trained Qwen3-14B achieves 43.7% on GAIA and 10.0% on HLE with only 1k RL training samples, substantially outperforming GRPO-trained counterparts and prompting-based agent baselines.

- **Demonstrated tool-call efficiency (Figure 7a):** During RL training, ARPO stabilizes at roughly 250–300 tool calls per step vs. 400–450 for GRPO, while achieving higher accuracy. This is a practically meaningful reduction in a cost-sensitive domain.

- **Quantitative rollout diversity analysis (Figure 7b):** Using BGE-M3 embeddings, PCA, and DBSCAN clustering on 7.6k trajectories, ARPO produces 54 distinct clusters vs. 48 for GRPO with better intra-cluster compactness and inter-cluster separation, providing objective evidence that the branching mechanism broadens exploration.

- **Useful ablation comparing hard vs. soft advantage estimation (Figure 5):** The soft variant yields consistently higher and more stable rewards, and the paper adopts it as default. This provides actionable guidance for practitioners.

- **Pass@K scaling demonstrates inference-time benefits (Figure 6):** ARPO's benefits compound with more sampling budget — e.g., Qwen3-14B + ARPO reaches Pass@5 of 63.2% on GAIA and 24.0% on HLE — indicating that richer exploration during training translates to a more exploitable policy at inference.

## Weaknesses

### Fatal

None.

### Major

- **No ablation isolates whether entropy-guided branching specifically drives the gains.** The paper never compares ARPO against variants that branch using a non-informative signal (e.g., random branching at tool-call steps, branching at every tool-call step, or allocating the full budget to trajectory-level sampling with matched total tool calls). Without such ablations, the reader cannot determine whether the entropy signal specifically is causal, or whether any scheme that adds partial-rollout exploration at intermediate tool-call steps would yield similar results. The diversity analysis (54 vs. 48 clusters, Figure 7b) is suggestive but does not resolve this causal question. This is the most important missing experiment for establishing the paper's central claim.

- **The advantage attribution component is overstated as a separate contribution.** The "soft" variant is explicitly acknowledged to retain the original GRPO loss formulation (line 142). Equation 4 observes that shared-prefix trajectories have identical importance sampling ratios — a property inherent to any GRPO implementation when trajectories happen to share prefixes. The hard variant performs worse (Figure 5). The actual algorithmic contribution is the entropy-guided rollout scheme; the advantage attribution discussion (both hard and soft) should be reframed as a design choice within standard GRPO rather than presented as a second novel component.

- **The GPG Theorem (§3.3) is a notational restatement of the policy gradient theorem.** Equation 6 groups consecutive output tokens into "macro actions" and applies the standard policy gradient. This is a reparameterization — any policy gradient method applied to autoregressive LLMs already treats the full output sequence as the action. The paper claims this "provides a robust theoretical foundation" (line 170), but the theorem provides no constraint or insight that guides the method's design; ARPO would be identical without it. The framing as a novel theoretical contribution is unwarranted.

### Minor

- **The "half the tool-call budget" claim partially conflates structure with evidence.** ARPO's partial trajectories are inherently shorter than full trajectories, so using fewer total tool calls per step is partially structural rather than purely an empirical finding. A comparison where GRPO is run with a larger rollout budget that matches ARPO's total tool-call count would strengthen the efficiency claim. That said, Figure 7a does demonstrate that ARPO achieves higher accuracy while using fewer tool calls, which is a valid practical result.

- **No confidence intervals or variance reported in result tables.** For small benchmarks like AIME (30 questions), a 3.3 percentage point difference represents a single question and could fall within sampling noise. Reporting standard deviations across seeds or bootstrap confidence intervals would strengthen the reliability of the empirical claims.

### Trivial

- The entropy normalization procedure (summing ΔH values and dividing by vocabulary size V, lines 96–106) is unusual — dividing by the number of tokens k would be more natural. This likely does not affect results (since τ can be tuned to any scaling) but merits clarification.

## Nice-to-Haves

- A comparison controlling for total computation (e.g., running GRPO with a larger rollout budget that matches ARPO's total tool-call count) would make the efficiency claim more rigorous.
- Discussion of how the entropy-guided branching interacts with the KL penalty in GRPO — shared-prefix tokens receive duplicate gradient contributions, which could effectively up-weight early tokens relative to later ones.
- Extension or discussion of whether entropy-guided branching interacts differently with process rewards or denser reward signals, which are increasingly common in agentic RL.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic claim that "ARPO reduces to GRPO with a different rollout scheme" and is "vacuous":** Too strong. The rollout mechanism is genuinely novel and well-motivated. The retained Major weakness about the advantage attribution captures the overclaiming without dismissing the real contribution. Partially incorporated.

- **Harsh Critic concern about DBSCAN hyperparameters not reported:** True but minor — a nitpick that doesn't threaten any core claim. The qualitative conclusion (ARPO produces more diverse rollouts) is visible from the clustering visualization.

- **Harsh Critic concern about branching termination dynamics not being analyzed:** Speculative about edge cases; the paper acknowledges the termination condition and this doesn't affect the core contribution.

- **Strength Finder strengths about "this paper addressed an important problem" or generic statements:** Removed as too generic — not concrete, verifiable strengths grounded in specific paper content.

## Novel Insights

The most interesting observation from synthesizing these reviews is the tension between a genuinely useful heuristic (entropy-guided branching at tool-call boundaries) and overclaiming around its theoretical and algorithmic framing. The entropy signal as a guide for exploration in multi-turn agent training is a simple, practical idea that the empirical results suggest works well. The paper would be stronger if it embraced its identity as an empirical methods paper with a well-motivated heuristic, rather than attempting to package the contribution as containing a novel optimizer, a novel theoretical framework, and a novel credit assignment mechanism — when the actual novel component is the branching scheme. The entropy analysis in §2 is the paper's most distinctive contribution and provides a template for how to motivate exploration mechanisms through careful measurement of model behavior.

## Suggestions

- **Add the entropy-vs-alternatives ablation:** Compare ARPO against (a) random branching at tool-call steps (same budget, no entropy threshold), (b) branching at every tool-call step (no entropy threshold), and (c) budget-matched GRPO. This is the single most important experiment for establishing the causal role of the entropy signal and would substantially strengthen the paper.

- **Reframe the contribution:** Center the entropy-based adaptive rollout as the sole algorithmic novelty. Present advantage attribution as a design choice (GRPO as the optimizer) rather than a separate contribution. Downgrade or remove the GPG Theorem as a claimed contribution.

- **Report hyperparameter values and sensitivity:** At minimum, report the values of M, N, k, α, β, τ, and Z used in experiments, with a brief note on robustness.

- **Add confidence intervals:** Report standard deviations across seeds or bootstrap confidence intervals, particularly for small benchmarks like AIME.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>