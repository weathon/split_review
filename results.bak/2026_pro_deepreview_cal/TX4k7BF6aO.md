Now I have a complete calibration picture. Here is my final consolidated review.

---

## Summary

This paper proposes Agentic Reinforced Policy Optimization (ARPO), an RL algorithm for training LLM-based agents in multi-turn tool-use settings. The key insight is that LLMs exhibit high token entropy immediately after receiving tool-call feedback. ARPO exploits this by adaptively branching rollout sampling at high-entropy tool-call steps, combined with an advantage attribution scheme that handles shared vs. branched trajectory segments. The method is evaluated across 13 benchmarks spanning mathematical reasoning, knowledge-intensive QA, and deep search, using multiple model backbones (Llama, Qwen) and RL baselines (GRPO, DAPO, REINFORCE++).

## Strengths

- **Well-motivated by concrete empirical observations**: The pilot entropy study (Section 2, Figure 2) quantifies token-level entropy after tool calls and clearly demonstrates sharp uncertainty increases — particularly for search feedback. This provides a principled, evidence-based motivation for the adaptive rollout mechanism rather than a post-hoc justification.

- **Consistent and substantial performance gains across diverse benchmarks**: On 10 math and knowledge-intensive reasoning tasks (Table 1), ARPO outperforms GRPO, DAPO, and REINFORCE++ for both Llama and Qwen backbones, yielding an average accuracy improvement of approximately 4 percentage points (e.g., 55.3% vs. 51.1% for Llama3.1-8B). Gains generalize across model families and task types.

- **Compelling deep-search results with strong sample efficiency**: With only 1k RL training samples, ARPO-trained Qwen3-14B reaches 43.7% on GAIA and 36.0% on WebWalkerQA (Table 2), substantially exceeding much larger models including DeepSeek-R1-671B and GPT-4o. The Pass@K scaling analysis (Figure 6) corroborates that the gains are not brittle.

- **Practical efficiency benefits**: The training-time analysis (Figure 7a) shows ARPO consumes roughly half the tool calls of GRPO while achieving higher accuracy, directly validating the claimed efficiency advantage of selective entropy-guided branching.

- **Sound theoretical grounding**: The Generalized Policy Gradient theorem (Section 3.3) provides a formal justification for treating partial rollout segments as macro-actions. The hard vs. soft advantage comparison (Figure 5) empirically justifies the chosen soft estimation.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The GPG theorem is framed as more novel than it is**: Section 3.3 presents the Generalized Policy Gradient theorem as a novel theoretical foundation, but the result — that policy gradients apply to macro-actions in a semi-MDP — is a standard consequence of the policy gradient theorem. The paper would be stronger if it acknowledged this as an application of known results rather than a new theorem. The theorem does not specifically justify *entropy-based* branching, only that segment-level optimization is valid.

- **The "fair setting" for Table 1 is under-specified**: The paper states "In a fair setting, ARPO consistently outperforms..." without detailing how rollout counts, tool-call budgets, or total compute were equalized across methods. GRPO with the same total trajectory count M as ARPO's M (global + partial) would be a natural baseline, but whether Table 1 reflects this is unclear. The efficiency analysis in Figure 7a is a separate demonstration and does not clarify Table 1's setup.

- **Deep-search training data source is vague**: The paper states ARPO is trained with "1k samples from an open-source web search dataset" without naming the dataset or discussing its relationship to test sets. While the 1k sample size makes systematic contamination unlikely, transparency about the training source would strengthen the results' interpretability.

### Trivial

- The rollout diversity analysis (Figure 7b: 54 vs. 48 clusters) lacks any significance testing or repeated measurement, making the claimed "more distinct and clearer cluster centers" difficult to assess — the difference could be due to random variation.

- The complexity claim in Section 3.1 (reducing from O(n²) to between O(n log n) and O(n²)) is stated without derivation, and the footnote disclaiming "negligible overhead from token-level entropy calculations" is insufficient to evaluate the claim.

## Nice-to-Haves

- A controlled ablation comparing entropy-based branching against random branching at tool-call steps (with the same partial-sampling budget) would directly isolate whether the entropy signal specifically matters, or whether any form of step-level exploration yields the observed gains. The paper references ablation studies in Appendix A.2, which may contain this analysis.

- Specifying the exact training data source used for the 1k-sample deep-search RL experiments and briefly justifying the choice of Qwen2.5-72B-instruct as LLM judge (e.g., agreement with human evaluation or exact-match on available subsets) would improve transparency.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Missing ablation of entropy-based branching criterion** (from Harsh Critic, Critical Issue 1): The paper explicitly references "More ablation and scaling analyses can be found in the Appendix A.2." Per review guidelines, the appendix is stripped during parsing and exists in the original submission; I cannot penalize the paper for missing appendix content. The ablation may exist there.

- **Undisclosed hyperparameters** (from Harsh Critic, Section-by-Section Notes): The harsh critic notes that α, β, τ, k, N, Z are not specified. Per review guidelines, undisclosed hyperparameters are considered "trivial implementation details" and fall under the reproducibility nitpick removal rule. Implementation details are provided in Appendix E (referenced in the paper).

- **Missing proofs in appendix** (from Harsh Critic): The theoretical relationship between hard and soft advantage estimation (referenced as Appendix F.2) and the GPG theorem proof (Appendix F.3) are noted as missing. Per guidelines, stripped appendices exist in the original submission.

- **"The observed entropy spikes could simply reflect the model's surprise at seeing external content"** (from Harsh Critic): This is speculative and unfalsifiable from the evidence presented. The paper already addresses this through the pilot experiment which shows systematic entropy patterns across tool types and reasoning stages. The entropy signal is used as a practical branching heuristic, not claimed as a deep cognitive insight.

- **"The deep-search evaluation uses LLM-as-judge... the reliability should be briefly justified"** (from Harsh Critic): LLM-as-judge with Qwen2.5-72B-instruct is a widely adopted evaluation protocol in the LLM agent literature and is standard practice for benchmarks like GAIA and HLE where exact-match scoring is infeasible. This is a scope/norm issue.

- **"Consistent and substantial performance gains"** (from Strength Finder): This strength is real and verified — kept in the main review.

- **"Theoretical grounding through the Generalized Policy Gradient Theorem"** (from Strength Finder): Partially kept but qualified; the theorem is standard but its application to ARPO's segmentation is valid. Downgraded from a core strength to a supporting one.

## Novel Insights

The paper's most striking empirical finding — that token entropy reliably spikes in the first 10–50 tokens after tool-call feedback, with search feedback producing substantially more uncertainty than deterministic code execution — is both novel and actionable. It transforms entropy from a passive diagnostic into an active exploration signal. This observation bridges the gap between token-level uncertainty studies in single-turn reasoning and the design of multi-turn agent training algorithms in a way that prior work has not done. The finding that this entropy-guided exploration yields both better performance *and* substantially fewer tool calls is a genuinely surprising and valuable result.

## Suggestions

- If the Appendix A.2 ablation studies include an entropy-vs-random-branching comparison, consider moving it to the main paper, as it directly addresses the most natural question about whether the entropy signal specifically drives the gains.

- Provide a concrete definition of the "fair setting" used in Table 1, e.g., "All methods use M total rollouts per question; ARPO allocates N to global sampling and M−N to partial sampling, while GRPO/DAPO/REINFORCE++ use all M as full trajectories."

- Report the exact open-source dataset used for the 1k-sample deep-search RL training, or at minimum describe its provenance and relationship to the test benchmarks.

## Score and Decision

**Calibration anchors used:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| CollabUIAgents | E2CR6hmV1I | 3.00 | R1 (weak) | ARPO far stronger — broader eval, clearer novelty |
| JOSH | DWLlTNhig1 | 4.75 | R1/R2 (mid) | ARPO stronger — 13 benchmarks vs. 1, better novelty |
| StepTool | PNHjoWcQje | 5.50 | R2 (narrow) | ARPO clearly stronger — more novel, broader eval, larger gains |
| R-MCTS | GBIUbwW9D8 | 5.75 | R1/R2 (mid) | ARPO comparable/slightly better — broader eval, better theoretical grounding |
| LLM Priors RL | e2NRNQ0sZe | 6.25 | R2 (narrow) | ARPO slightly stronger — broader eval, more practical impact |
| WebRL | oVKEAFjEqv | 6.67 | R2 (narrow) | ARPO comparable — broader eval but WebRL has more thorough internal ablations |
| MaestroMotif | or8mMhmyRV | 7.75 | R1 (strong) | ARPO clearly below — less comprehensive ablations |

**Bracket**: Round 1 placed ARPO between 5.5–7.0. Round 2 narrowed it to 6.0–6.5, sitting between the LLM Priors RL paper (6.25) and WebRL (6.67). ARPO has broader evaluation than both but less thorough internal component ablations than WebRL. The paper's core claims are well-supported, the method is genuinely novel and well-motivated, and the remaining weaknesses are all minor and addressable.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>