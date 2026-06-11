Now I have a clear picture from all anchors. Let me finalize.

**Round 2 Anchor Comparisons:**

| Anchor | Score | How ARPO compares |
|---|---|---|
| EAST (YCu7H0kFS3) | 4.75 | ARPO is substantially stronger — broader evaluation, more practical method |
| ReSpect (BSBZCa6N3E) | 5.00 | ARPO stronger — broader eval, better empirical grounding |
| StepTool (PNHjoWcQje) | 5.50 | ARPO slightly stronger — more novel mechanism, broader benchmarks, better motivation |
| R-MCTS (GBIUbwW9D8) | 5.75 | Comparable — ARPO has broader eval but weaker mechanistic validation of its core mechanism |
| LAM Simulator (Dpqw0namg3) | 6.00 | Comparable — both have overclaiming issues, ARPO has broader evaluation |
| REFUEL (cVyELMpMRS) | 6.50 | ARPO is weaker — less theoretical depth, missing key ablation, overclaimed contributions |

**Final Score: 5.5**. ARPO has a genuinely novel and well-motivated core idea (entropy-based adaptive branching), broad empirical evaluation (13 benchmarks, 4 model families), and consistent performance gains. But the paper is weakened by overclaimed contributions (advantage attribution is standard GRPO behavior, GPG theorem is a notational reframing), a missing critical ablation (random branching), and modest gains that don't fully validate whether entropy specifically drives the improvement.

---

## Summary

ARPO proposes an RL algorithm for training multi-turn LLM-based tool-use agents. The core idea is to branch rollouts at tool-call steps where token entropy is high, rather than sampling only complete trajectories. The method is motivated by a pilot experiment showing that LLMs exhibit elevated token entropy after receiving tool-call feedback. ARPO is evaluated across 13 benchmarks spanning math, knowledge reasoning, and deep search, showing consistent but modest improvements over trajectory-level RL baselines (GRPO, DAPO, REINFORCE++) while using fewer tool calls during training.

## Strengths

- **Empirically-grounded motivation (Section 2):** The pilot experiment measuring token entropy after tool calls across search engine and Python interpreter settings provides a clear, data-driven motivation. The three observations — entropy spikes post tool call, tool-call entropy exceeds early-reasoning entropy, and search feedback produces more uncertainty than Python feedback — are well-visualized in Figures 2 and 4. This is a genuine empirical insight that drives the algorithm design.

- **Consistent empirical gains across diverse benchmarks (Tables 1, 2):** ARPO outperforms GRPO, DAPO, and REINFORCE++ across all 10 math and knowledge-intensive reasoning benchmarks on both Llama3.1-8B and Qwen2.5-7B, with average gains of ~4% and ~2% respectively. Table 2 extends this to deep search tasks, where ARPO on Qwen3-14B achieves 43.7% on GAIA vs. GRPO's 36.9% and 36.0% on WebWalkerQA vs. 30.0%. The evaluation spans three task families and four model backbones, providing evidence for generality.

- **Tool-call efficiency (Figure 7a):** ARPO achieves higher accuracy while using substantially fewer tool calls during training compared to GRPO on Qwen2.5-7B — a practically meaningful result for reducing the cost of agentic RL training.

- **Pass@K scaling analysis (Figure 6):** ARPO's gains compound with increased sampling budget — Qwen3-14B with ARPO reaches 61.2% Pass@5 on GAIA — demonstrating that learned behaviors are robust to increased inference-time compute.

## Weaknesses

### Fatal

None.

### Major

- **Advantage Attribution Estimation is not a substantive contribution.** The "soft" variant (which ARPO adopts as default) amounts to observing that GRPO's importance sampling ratio is naturally identical for tokens on shared trajectory prefixes (Eq. 4, line 136) — this is standard GRPO behavior when applied to branched rollouts, not a novel estimation technique. The "hard" variant, which *would* constitute a novel contribution, performs dramatically worse (Figure 5) and contains a technical issue (see below). The paper's actual contribution lies in the entropy-based branching mechanism (Section 3.1), yet "Advantage Attribution Estimation" is presented as a separate named contribution in the abstract, introduction, and contributions list.

- **Missing random-branching baseline.** The central claim is that *entropy-based* branching improves exploration. However, there is no comparison against a control that branches randomly at tool-call steps with the same branching budget. Without this ablation, we cannot determine whether entropy specifically drives the observed gains, or whether *any* form of intermediate branching at tool-call steps — regardless of the signal used to select branching points — would produce similar improvements. This leaves the paper's core mechanism unvalidated.

- **The GPG Theorem (Section 3.3) does not provide a novel theoretical contribution.** Equation 6 expresses the policy gradient in terms of macro-actions (token segments) rather than individual tokens. This is a straightforward consequence of the linearity of the gradient operator applied to the standard Policy Gradient Theorem — grouping token-level actions into segments and summing their gradients is a notational reframing, not a theoretical advance. The theorem provides no guarantees about ARPO's convergence, sample complexity, or why entropy-based branching should help. Presenting this as a standalone contribution (line 48-49) overstates the paper's theoretical depth.

### Minor

- **"Half the tool-call budget" claim is narrowly substantiated.** This headline claim appears in the abstract, introduction, contributions list, and conclusion, but is supported only by a single training curve on one model (Qwen2.5-7B, Figure 7a). Tool-call counts are not reported for the full benchmark results in Tables 1 or 2. The claim should either be qualified as observed in a specific setting or substantiated more broadly.

- **Hard advantage estimation is technically ill-posed in the RLVR setting.** The hard advantage formula (line 122) uses a per-token reward `r_t`, but the paper's reward design (Eq. 5) defines only a trajectory-level reward `R`. The origin of `r_t` is unexplained. While the paper ultimately adopts the soft variant, presenting the hard formulation as a genuine alternative without resolving this inconsistency is problematic.

- **Implementation details under-specified in the main text.** The branching mechanism depends on at least five hyperparameters (α, β, τ, Z, and the global/partial budget split M-N), none of whose values are reported in the main paper. The paper also does not specify how `Branch(Z)` generates branched paths (different random seeds? different temperatures?), and the "Normalize" operation in ΔH_t (line 96) is ambiguously described. While details may be in the appendix, the core mechanism should be reproducible from the main text.

### Trivial

- Table 2 presents zero-shot large models (GPT-4o, DeepSeek-R1-671B) in the same table hierarchy as RL-trained methods, differentiated only by gray text. A clearer visual separation would improve readability.

## Nice-to-Haves

- A sensitivity analysis for the DBSCAN clustering (Figure 7b): the difference between 54 and 48 clusters is reported without any measure of variance across multiple runs or parameter settings, making the claimed improvement in "structured" diversity unconvincing.
- Tool-call budget measurements across all experimental settings, not just Figure 7a.
- Ablation on the effect of the multi-tool collaboration bonus `r_M` in the reward design (Eq. 5).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **HC: Comparison against GPT-4o/DeepSeek-R1 is misleading.** The paper clearly presents zero-shot large models in gray as reference in Table 2, and the text explicitly distinguishes them from RL-trained methods. The fair comparison (ARPO vs. GRPO) is clearly reported. This is a presentation preference, not a substantive concern.

- **HC: "Pioneeringly quantify" is strong language.** This is a stylistic judgment about word choice, not a substantive weakness in the method or results.

- **SF: GPG Theorem as a strength.** Removed — as discussed under Major weaknesses, the theorem is a notational reframing rather than a substantive theoretical contribution.

- **SF: "Rigorous ablation of advantage estimation design."** Removed — the hard vs. soft comparison is a straightforward ablation on one design choice; the paper lacks ablations on the core entropy-based mechanism.

- **SF: "Sample efficiency in deep search."** Removed as a separate strength — this is a restatement of the main results in Table 2.

- **SF: "Mechanistic evidence via rollout diversity analysis."** Removed — the 54 vs. 48 cluster difference with no error bars or sensitivity analysis is insufficient to claim strong mechanistic evidence.

## Novel Insights

None beyond the paper's own contributions. The pilot entropy observation — that token entropy spikes after tool-call feedback — is genuinely interesting and reasonably well-documented, though the paper cites prior entropy-based RL studies that have investigated related phenomena.

## Suggestions

- Add a random-branching baseline (branch at tool-call steps but ignore entropy, same branching budget). This is the single most important experiment to validate the core claim that entropy specifically drives improvement.
- Either ground the GPG Theorem in a non-trivial result (e.g., convergence rate, sample complexity bounds) or present it as a clarifying formalization rather than a standalone theoretical contribution.
- Qualify the "half the tool-call budget" claim with the specific setting where it was observed, or extend the measurement to all experimental configurations.
- Clarify the hard advantage formulation — if `r_t` cannot be defined in the RLVR setting, acknowledge this rather than presenting it as a genuine alternative.
- Report all branching hyperparameters (α, β, τ, Z, M, N, k) and their values in the main text for reproducibility.

## Score and Decision

### Anchor Summary (all rounds)

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| zEhTnQZB3D (LLIT) | 2.33 | R1 | Not similar; strong reject template |
| hCfhfwSfCg (LanGoal) | 2.00 | R1 | Different domain; strong reject template |
| 6e3hoDZKuO (Zero-Shot Goal Dialogue) | 3.50 | R1 | ARPO much stronger — broader eval, better method |
| E2CR6hmV1I (CollabUIAgents) | 3.00 | R1 | ARPO stronger |
| F0q880yOgY (Language Agents vs RL) | 4.40 | R1 | ARPO stronger, more practical |
| YCu7H0kFS3 (EAST) | 4.75 | R2 | ARPO substantially stronger — broader evaluation |
| DWLlTNhig1 (JOSH) | 4.75 | R2 | ARPO comparable or stronger |
| BSBZCa6N3E (ReSpect) | 5.00 | R1 | ARPO stronger — broader eval, better empirical grounding |
| PNHjoWcQje (StepTool) | 5.50 | R2 | Most similar paper; ARPO slightly stronger — more novel mechanism, broader benchmarks |
| GBIUbwW9D8 (R-MCTS) | 5.75 | R2 | Comparable; ARPO broader eval, R-MCTS better mechanistic validation. R-MCTS accepted. |
| Dpqw0namg3 (LAM Simulator) | 6.00 | R1 | Comparable; ARPO broader eval, both have overclaiming issues |
| l1pNNQSzZv (Rational Agent) | 6.25 | R2 | ARPO weaker — less novelty |
| cVyELMpMRS (REFUEL) | 6.50 | R1 | ARPO weaker — less theoretical depth, missing key ablation |

**Round 1 bracket:** 5.0–6.5. **Round 2 narrowing:** The most comparable anchors are StepTool (5.50, reject) and R-MCTS (5.75, accept). ARPO is slightly stronger than StepTool (more novel mechanism, broader evaluation, better motivation) and comparable to R-MCTS (ARPO has broader evaluation but weaker validation of its core mechanism). ARPO is clearly weaker than REFUEL (6.50). The paper lands at 5.5 — a borderline paper with a genuinely novel core idea and broad empirical evidence, but undermined by overclaimed contributions and a missing critical ablation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>