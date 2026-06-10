## Summary

This paper presents **Optima**, an iterative training framework for LLM-based multi-agent systems (MAS) that jointly optimizes task effectiveness and communication efficiency. It employs a generate-rank-select-train paradigm with a three-term reward function balancing task performance, token efficiency, and language naturalness, instantiated via iSFT, iDPO, and a hybrid approach (iSFT-DPO). An MCTS-inspired procedure generates preference pairs for DPO. Evaluated on 8 benchmarks across information-asymmetric QA and debate settings with Llama 3 8B, Optima achieves up to a 2.8× F1 improvement with 90% fewer tokens on 2WikiMultiHopQA relative to the untrained Multi-Agent Debate baseline.

## Strengths

- **Substantial and well-documented efficiency-performance gains on information-exchange tasks.** On 2WikiMultiHopQA, iSFT-DPO improves F1 by 38.3% (2.8×) while using only 10% of the tokens required by MAD (line 191). This is a concrete, task-level measurement that directly supports the paper's central claim of simultaneously optimizing both objectives.

- **Ablation study causally validates each reward component.** Removing the token penalty causes verbosity; removing the LM loss causes overly concise, hallucination-prone outputs (lines 236–238). This provides empirical evidence that all three reward terms (task performance, token efficiency, readability) serve distinct and necessary roles.

- **Broad evaluation across diverse settings.** The paper tests on 8 datasets spanning two fundamentally different MAS paradigms (information-asymmetric QA and debate), with consistent evaluation using task-appropriate metrics (F1, accuracy, symbolic equivalence). Transfer learning experiments further probe generalization across related domains (HotpotQA→TriviaQA/2WMHQA, MATH→GSM8k).

- **Qualitative communication evolution traced across iterations.** Figure 4 shows the concrete progression from verbose, unfocused exchanges at the base model to concise, task-oriented communication at later iterations, aligning with the quantitative patterns.

## Weaknesses

### Major

1. **Missing trained baseline — central comparison conflates training benefit with framework benefit.** The paper's headline results (e.g., the 2.8×/10% claim) compare Optima-trained models against **untrained** inference-only baselines (MAD, AutoForm on vanilla Llama 3 8B). Any task-specific fine-tuning is expected to outperform an off-the-shelf base model on in-distribution tasks. Without a trained single-agent SFT baseline — i.e., fine-tune Llama 3 8B on the same task data and then use it as the backbone for MAD/AutoForm — it is impossible to attribute Optima's gains to the *multi-agent training framework* rather than to training *per se*. This is the most significant weakness in the paper's evaluation design.

2. **Reward function is specified at a level that prevents reproduction.** Equation 1 defines $R(\tau) = R_\text{task}(\tau) - \lambda_\text{token} R_\text{token}(\tau) + \lambda_\text{loss} / R_\text{loss}(\tau)$, but none of $R_\text{task}$, $R_\text{token}$, or $R_\text{loss}$ are defined as concrete functions. $R_\text{task}$ is described as "ensuring the model improves on the intended task" — is this binary correctness, F1 score directly, or something else? $R_\text{token}$ presumably measures token count, but normalized how (per-turn, per-trajectory, z-scored)? $R_\text{loss}$ is described as "probable under the base model," and the reciprocal form $1/R_\text{loss}$ is unusual and numerically sensitive if a loss is used. The hyperparameters $\lambda_\text{token}$ and $\lambda_\text{loss}$ are never given numerical values. The reward function is the engine that drives data selection for all three training instantiations; without these details the framework is not reproducible.

### Minor

3. **On 2 of 8 benchmarks, the method does not improve task performance.** On MATH and GSM8k, Optima variants show "comparable or slightly lower performance than SC" (line 191) — only token efficiency improves. The paper acknowledges this but attributes it to task difficulty and training set size ("small size of their training set" — MATH has ~7,500 problems, which is not obviously small). This is presented as a secondary observation rather than a meaningful boundary condition on the claimed "simultaneous optimization" of both objectives. The paper would benefit from a concrete failure analysis (e.g., does the token penalty suppress necessary reasoning steps?) rather than speculation.

4. **The "MCTS-inspired" component is overstated.** The procedure described (lines 135–139) selects 10 high-reward nodes, samples one via softmax, expands 3 trajectories from that node, and backpropagates average rewards — repeated 8 times for 24 trajectories. There is no UCB-based selection, no explicit exploration-exploitation trade-off, and no principled tree policy. This is a shallow best-first search with limited rollouts, not MCTS in any meaningful sense. The paper's framing ("integrate Monte Carlo Tree Search-inspired techniques") invites comparison with full MCTS implementations that the method does not deliver.

5. **Key procedural hyperparameters unreported.** $\theta_\text{init}$, $\theta_\text{sft}$, $\theta_\text{dpo-filter}$, $\theta_\text{dpo-diff}$, the sample size $N$, the maximum iterations $T$, and the format prompt pool size $K$ are all defined but never given numerical values. This compounds the reproducibility gap left by the unspecified reward function.

6. **Format specification prompts are not described.** The initialization step uses a pool $\mathcal{P} = \{p_1, ..., p_K\}$ of format prompts (line 81), but the paper never states what these prompts look like, how many are used, or how they are constructed. This is a non-trivial component of the method.

### Trivial

- Section 4 (Analysis, lines 256–259) appears to be an empty section header in the extracted text — possibly a parser artifact from an \input{} command, but if genuinely empty it is an odd omission.

## Nice-to-Haves

- Reporting variance or confidence intervals across multiple seeds would help assess the reliability of the reported gains, though single-run LLM benchmark evaluation is the current norm.
- Reporting the total training compute cost (GPU-hours) would contextualize the inference efficiency claims, especially since training involves iterative data generation from the current model — which is itself expensive.
- Exploring whether training separate models per agent (rather than sharing parameters as done here) improves the diversity of multi-agent interaction.

## Removed Points

These points were flagged by reviewers but removed or downgraded after verification:

- **"No statistical significance or variance reported"** → Demoted to nice-to-have. Single-run evaluation on established LLM benchmarks is standard practice at top venues; requiring it here would be a double standard.
- **"Single-model limitation fundamentally limits MAS diversity"** → Removed. The paper explicitly acknowledges this and frames it as future work (line 184). This is a scope note, not a flaw.
- **"The MCTS component is oversold"** → Kept at Minor (see Weakness 4), but the critic's framing of a "fatal" overselling is too strong. The paper says "MCTS-inspired" and "MCTS-like," which are qualifiers — the issue is that what is described barely resembles MCTS.
- **"Criticism about debate task results undermining core claim"** → Demoted from "undermining" to Minor (see Weakness 3). The paper already acknowledges these results; the issue is framing, not validity.
- **"Missing related works"** → Removed per instruction (cannot verify from external sources).
- **"The Analysis section is empty — significant gap"** → Moved to Trivial because it may be a parser stripping artifact from an \input{} command.
- **"Formatting/style nitpicks and typos"** → Removed per instruction (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The two synthetic reviews largely converged on the same issues (missing trained baseline, underspecified reward function) without adding genuinely unexpected analytical angles. The key structural tension — that the paper's strongest evidence comes from IE tasks where the baselines are weakest — is correctly identified but not surprising given the paper's framing.

## Suggestions

1. **Add a trained baseline.** Fine-tune Llama 3 8B on each task's training data with standard SFT, then use that model as the backbone for MAD and AutoForm. This directly isolates the benefit of the multi-agent training framework from the benefit of any task-specific fine-tuning. Without this, the headline claims lack proper attribution.

2. **Fully specify the reward function.** Provide concrete definitions (equations) for $R_\text{task}$, $R_\text{token}$, and $R_\text{loss}$. Report the numerical values of $\lambda_\text{token}$, $\lambda_\text{loss}$, and all $\theta$ thresholds. If $R_\text{loss}$ is a negative log-likelihood, justify the reciprocal form or consider alternatives (e.g., adding the loss directly with a negative coefficient).

3. **Reframe the MCTS component honestly.** Describe the tree-search procedure as "a best-first search with limited rollouts for generating preference pairs" and drop the MCTS label, which carries precise technical expectations that the method does not meet.

4. **Provide a failure analysis for MATH/GSM8k.** Instead of speculating about training set size, analyze concrete examples where Optima degrades performance. Does the token penalty suppress necessary reasoning? Do agents converge on wrong answers too early? This would be more informative than the current conjecture and would strengthen the paper's scientific contribution.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>