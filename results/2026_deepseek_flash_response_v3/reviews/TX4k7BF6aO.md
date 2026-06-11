Now let me write the final review.

**Calibration Anchors (all rounds):**
1. **EAST** (YCu7H0kFS3.md, avg 4.75, Reject) — entropy steering for LLM agents, but only evaluated on 2-arm bandits. ARPO is clearly stronger.
2. **DfPO** (6UQaXJm53B.md, avg 5.25, Reject) — action masking for RL fine-tuning. Mixed reviews (3,8,5,5), technical concerns. ARPO has cleaner methodology.
3. **Agent Q** (LuytzzohTa.md, avg 5.60, Reject) — MCTS+DPO for web agents. Strong results but poor presentation, missing ablations, limited evaluation (2 benchmarks).
4. **R-MCTS** (GBIUbwW9D8.md, avg 5.75, Accept) — MCTS + reflection for web agents. Accepted despite missing baselines. Had thorough ablations.
5. **MA-RLHF** (WWXjMYZxfH.md, avg 6.20, Accept) — macro-actions for RLHF. Clean execution with proper ablations.
6. **DqO** (k2q0rUX2lx.md, avg 3.50, Reject) — Q-function optimization for reasoning. Technical derivation concerns.
7. **GPO** (DpFeMH4l8Q.md, avg 5.67, Accept) — few-shot alignment framework.

ARPO is clearly stronger than 3.5–4.75 papers, comparable to 5.25–5.75 papers, but below 6.20 papers. Its missing step-level baselines and no variance reporting are significant gaps beyond what R-MCTS (5.75, accepted) had. Score: 5.0.

---

## Summary

ARPO proposes an entropy-based adaptive rollout mechanism for multi-turn LLM agent RL training. The key idea is to monitor token-level entropy after tool calls and branch additional rollouts at high-entropy decision points, enabling step-level exploration in regions where the model is uncertain. Combined with advantage attribution (using GRPO's objective as the default soft variant), the method is evaluated across 13 mathematical, knowledge-intensive, and deep search benchmarks on Llama3.1-8B, Qwen2.5-7B, and Qwen3-8B/14B backbones.

## Strengths

1. **Clear empirical motivation grounded in a concrete, reproducible observation.** The pilot study (Section 2, Figure 2) quantitatively documents that token-level entropy spikes sharply in the first 10–50 tokens after each tool call, with search feedback producing larger entropy increases than Python feedback (Ob.1–Ob.3). This gives a principled reason to focus exploration on post-tool-call steps specifically — a measurement that goes beyond prior single-turn entropy analyses.

2. **Consistent improvements over trajectory-level RL methods across two model families and 10 reasoning tasks (Table 1).** On Llama3.1-8B, ARPO achieves 55.3% average vs. 51.1% for GRPO/REINFORCE++ (+4.2%). On Qwen2.5-7B, 58.3% vs. 56.5% (+1.8%). The advantage is clearest on Llama3.1-8B and on deep search tasks (GAIA: 43.7% ARPO vs. 36.9% GRPO with Qwen3-14B, Table 2). These are the most directly relevant baselines (all trajectory-level RL), and ARPO wins consistently.

3. **Substantially lower tool-call budget during training.** Figure 7a shows ARPO uses ~250–350 tool calls per step versus GRPO's ~400–480 (a 37–48% reduction) while simultaneously achieving higher accuracy. This is a practical operational advantage that addresses a real cost concern in agentic RL at scale.

4. **Impressive sample efficiency on deep search tasks.** Using only 1k training samples, ARPO-tuned Qwen3-14B reaches strong performance on GAIA (43.7%) and HLE (10.0%), beating much larger models (DeepSeek-R1-671B: 8.6% on HLE). This suggests the entropy-guided branching enables efficient exploration even with limited data.

## Weaknesses

### Fatal
None.

### Major

1. **Missing baselines from the most relevant competitors — step-level/segment-level RL methods.** The paper's central thesis is that trajectory-level RL (GRPO, DAPO, REINFORCE++) provides insufficient granularity for multi-turn tool-use and that step-level credit assignment is needed. Yet the related work (Section 6) explicitly cites "segment-level RL objectives" from Guo et al. (2025), Li et al. (2025g), and Zheng et al. (2025a) — methods that already operate at a finer granularity than full trajectories. None are included in the experimental comparison. This is a significant gap: the chosen baselines are all trajectory-level, which makes ARPO's relative advantage partly by construction. Without comparison against existing step-level methods, the paper cannot support its central claim that ARPO's specific approach to step-level exploration (entropy-based adaptive branching) is superior to other step-level approaches.

2. **No statistical significance or variance reporting across any experiment.** Every result in Tables 1 and 2 is a single point estimate. No standard deviations, confidence intervals, or multi-seed runs are reported. This is a structural concern because several of the claimed advantages on Qwen2.5-7B are small or absent on individual benchmarks: ARPO is *worse* than GRPO on GSM8K (92.2 vs. 92.8) and HQA (58.8 vs. 59.0), tied on MATH (88.8) and 2Wiki (76.1). The average gain across all 10 tasks is only 1.8% (58.3 vs. 56.5). Without error bars, it is impossible to know whether these differences reflect genuine improvement or evaluation noise at temperature 0.6.

### Minor

1. **The "Generalized Policy Gradient Theorem" (§3.3) is not a novel theoretical contribution.** Equation 6 is the standard policy gradient theorem applied at the macro-action (token-segment) level. For any differentiable policy, the policy gradient theorem holds at any action granularity by a straightforward change of variable. The paper acknowledges this ("generalization encompasses the traditional Policy Gradient Theorem"). The theorem does not specifically constrain or justify ARPO's entropy-based adaptive branching — it would apply equally to any rollout strategy that segments token sequences. The paper should frame this as a standard result providing background justification, not as a novel theoretical contribution.

2. **The "Advantage Attribution Estimation" (§3.2) contribution is essentially the rollout structure, not a new loss function.** The paper is transparent that the adopted "soft" variant uses the standard GRPO objective (line 142: "While we retain the original GRPO loss formulation…"), and Figure 5 shows it outperforms the "hard" variant. The novelty lies in how the rollout structure creates shared prefixes, not in the advantage estimation or loss function itself. This should be acknowledged more directly rather than presented as two co-equal contributions.

3. **Key hyperparameters unspecified in the main text.** The entropy-based branching mechanism depends on α (base probability), β (stability coefficient), τ (threshold), Z (number of branches from each fork), global rollout size M, initial global trajectories N, and the look-ahead token count k. None of these values are reported in the main paper, making the method difficult to reproduce or implement without consulting the appendix. (The appendix is stripped by the parser, but these values should appear in the main text.)

4. **Deep search training data not identified.** The paper states "1k samples from an open-source web search dataset" (Section 5.1) without naming the dataset. Given that the deep search results (GAIA, HLE, WebWalkerQA) are among the paper's strongest evidence, not identifying the training data makes the results difficult to contextualize and reproduce.

5. **Computational complexity claim is unclear.** The paper states ARPO "reduces the computational complexity of each rollout from the trajectory-level RL's O(n²) to between O(n log n) and O(n²)" (Section 3.1). Since branching generates *more* total tokens than standard trajectory-level sampling, the basis for a complexity *reduction* is not self-evident. The footnote about "neglecting the minor overhead from token-level entropy calculations" does not resolve this.

6. **Entropy normalization description is confusing.** The paper describes normalization as "summing all the values of ΔH and dividing by the vocab size V" (line 106). ΔH is a vector of per-token entropy differences (size k); the description conflates vector and scalar operations. A clearer mathematical specification would benefit reproducibility.

### Trivial
- Evaluation uses temperature 0.6 and top-p 0.95 (Section 4), which is higher than the typical 0.0 used for deterministic evaluation. A brief justification would strengthen the methodology section.

## Nice-to-Haves
- An ablation comparing entropy-based branching vs. branching at random tool-call steps vs. branching at every tool-call step, to isolate whether the entropy *trigger* specifically is valuable or if any step-level branching helps.
- Reporting GPU-hours or wall-clock training time to contextualize the efficiency gain beyond tool-call counts.
- Discussion of LLM-as-Judge bias when using Qwen2.5-72B-instruct as the evaluator for models fine-tuned from Qwen checkpoints.
- Analysis of inference-time tool-use efficiency for ARPO-trained models.

## Removed Points
- **"Advantage estimation is vacuous"** — removed because the paper is transparent about using GRPO's loss for the soft variant (line 142). The contribution is the analysis of how GRPO's importance-sampling ratio handles shared prefixes in the branching context, which is a non-trivial application insight even if the loss formula itself is unchanged.
- **"pioneeringly quantify" overstatement** — this is a phrasing issue, not a technical weakness. The paper provides novel measurements of post-tool-call entropy that go beyond existing single-turn entropy analyses.
- **Missing appendix content / related works concerns** — removed per hard rules.
- **Generic reproducibility concerns about undisclosed hyperparameters beyond the main text** — weakened to minor since the appendix (stripped by parser) likely contains details; the main text should still list key values.
- **"Could be measuring proxy uncertainty" speculation about entropy measurement** — removed because the paper's entropy definition is standard (Equation 1, per-token entropy over vocabulary), and the claim is specifically about tool-use behavior patterns.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add step-level/segment-level baselines** (Guo et al., 2025; Li et al., 2025g; Zheng et al., 2025a) to the experimental comparison. Without this, the central claim about step-level exploration being superior to trajectory-level cannot be properly evaluated.
2. **Report results from 3+ random seeds with standard deviations** for all main results (Tables 1 and 2). The small margins on Qwen2.5-7B require this to establish reliability.
3. **Remove or honestly reframe the GPG Theorem** as a standard background result rather than a contribution.
4. **Disclose hyperparameter values** (α, β, τ, Z, M, N, k) in the main text and name the deep search training dataset.
5. **Add an ablation** comparing entropy-based branching vs. random branching vs. branching at every tool-call step to isolate the value of the entropy signal.

## Score and Decision

**My final score: 5.0**
**My final decision: Reject**

**Calibration summary:**
- Round 1 bracket: 4.5–6.0. ARPO is clearly stronger than EAST (4.75, Reject — 2-arm bandit only), DfPO (5.25, Reject — technical derivation issues). Comparable to Agent Q (5.60, Reject — strong results but missing ablations/presentation issues) and R-MCTS (5.75, Accept — thorough ablations but missing baselines). Below MA-RLHF (6.20, Accept — clean execution).
- Round 2 narrowing: 5.0 is the correct position. ARPO has more comprehensive evaluation than R-MCTS (13 benchmarks vs 1) but inherits the missing-baselines issue while adding a lack-of-variance problem that R-MCTS did not have. The paper is borderline but the evidential gaps (particularly the missing step-level baselines) are too significant for acceptance in the current form.
- The paper's core idea (entropy-guided adaptive branching) is sound and the results are promising, but the evidential shortcomings prevent confident acceptance. With added baselines and variance reporting, this could reach 6.0+ territory.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>