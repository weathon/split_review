Now I have a thorough understanding of the paper and can verify each claim against the source text. Let me produce the final review.

---

## Summary

This paper introduces a method to prune redundant communication edges in LLM-based multi-agent systems. The key idea is to model the system as a spatial-temporal graph, learn continuous mask weights for each edge via policy-gradient optimization with low-rank regularization, then perform one-shot magnitude pruning to obtain a sparse communication topology. Experiments across six benchmarks show that the method reduces token consumption by 28–73% while maintaining or slightly improving task performance, and provides modest robustness gains against two types of agent-level attacks.

## Strengths

- **First formal framing of communication redundancy in LLM-MA systems.** The paper identifies that a significant fraction of inter-agent message passing is non-essential, and supports this claim with a preliminary experiment (randomly pruning 10–30% of edges actually improves MMLU accuracy by up to 2.83%). This motivates the problem effectively.

- **Substantial and well-documented cost reductions.** The method consistently reduces token consumption (e.g., 39.4% prompt tokens on GSM8K+GPTSwarm, 64.0% on HumanEval+AutoGen) with dollar savings of up to $177.58 (Table 3). These savings are achieved while maintaining or improving performance, which is the paper's central practical claim.

- **Seamless integration into existing frameworks.** The plug-and-play design is validated by combining the method with AutoGen and GPTSwarm across multiple datasets, showing the approach is not tied to a specific system.

- **Demonstrated robustness improvements.** Under two types of adversarial attacks (agent prompt attack and agent replacement attack), applying the method boosts accuracy by 3.5–10.8 percentage points over the unmodified baselines (Figure 3), indicating the pruning mechanism can filter malicious messages.

## Weaknesses

### Fatal
None.

### Major

- **The policy gradient formulation (Eq. 7–8) has an unclear probabilistic grounding.** The definition of \(p_\mathbf{S}\) in Eq. 8 as the product of continuous, unnormalized mask values \(\mathbf{S}^\mathcal{S}[i,j]\) multiplied across edges does not constitute a valid probability distribution over the discrete space of subgraphs. A proper REINFORCE estimator requires \(\nabla \log p\) for a distribution \(p\) that sums to 1 over the sample space. As written, it is unclear how this quantity normalizes. Additionally, the formulation omits the \((1-\mathbf{S})\) terms that would be needed for a standard independent-Bernoulli product distribution over edge inclusion/exclusion. The DAGSampling procedure (deferred to the appendix) may address this, but the main paper does not resolve whether the gradient estimates have a sound probabilistic foundation or are a heuristic weighted-score update. This is a methodological concern that requires clarification.

- **No variance or uncertainty reported for main results.** Table 1 reports single accuracy numbers for each method with no confidence intervals, standard deviations, or number of runs. Given the stochasticity of LLM generation (temperature=1) and the policy-gradient sampling procedure, it is impossible to assess whether the observed improvements (e.g., \ourmethod-C 84.72 vs GPTSwarm 83.98 on MMLU, or \ourmethod-R 90.30 vs Reflexion 91.40 on HumanEval) are statistically significant or within the noise range.

### Minor

- **The low-rank regularization operates on very small graphs (3–5 agents).** The adjacency matrices \(\mathbf{S}^\mathcal{S}, \mathbf{S}^\mathcal{T}\) are at most \(5\times5\). While not "vacuous" (the reviewer's term is overstated — even a 5×5 matrix can meaningfully reduce from rank 3 to rank 2), the practical effect of nuclear norm minimization in this regime is limited, and the paper's citation of results from large-network robustness literature does not automatically transfer. The robustness improvements in Section 4.3 may stem more from the general pruning mechanism than from low-rank regularization specifically; without ablation at larger scales, this component's contribution is unclear.

- **The abstract's cost claim ($5.6 vs $43.7) is not directly traceable to a single table.** The numbers appear to be derived from a combination of token counts and pricing, but no table in the main paper explicitly states "$5.6" and "$43.7" side by side with a clear breakdown of which methods and tasks these correspond to. The reader must cross-reference multiple figures and tables to reconstruct this comparison.

- **The definition of communication redundancy (Definition 1) is a basic formal statement of the problem** rather than a substantive discovery. It asserts that a subgraph with \(\phi(\mathcal{G}^\text{sub}) \ge \phi(\mathcal{G})\) exists — an empirical claim supported by the preliminary experiment. This is a reasonable framing, not a flaw, but the paper overclaims it as a "system discovery" when the actual contribution is the pruning method, not the definition.

### Trivial

- In Table 1, the Avg. column for the Chain row shows 92.92, but the correct average of the six constituent accuracy values (82.35, 85.57, 94.38, 83.41, 70.94, 80.88) is 82.92. This appears to be a genuine data error in the original LaTeX.

## Nice-to-Haves

- An analysis of why pruning removes malicious messages. Currently the robustness experiments demonstrate the effect but do not explain the mechanism (e.g., do pruned edges correspond to the compromised agent's outgoing connections?).
- A direct comparison of total cost (training + inference) versus vanilla inference, not just the post-pruning savings, since the \(K'\) training rounds with \(M\) samples per step incur nontrivial overhead.
- Experiments with larger agent counts (e.g., 10–20 agents) to test scalability and give the low-rank regularization more room to operate.

## Removed Points

These points from the reviewers were evaluated against the paper text and removed with justification:

- **"Low-rank regularization is vacuous for small agent graphs" (Harsh Critic, Critical Issue 2)** — Partially removed/weakened. The claim that the term is "vacuous" and "has no effect in the tested setting" is an overstatement. A 5×5 matrix can still be regularized toward lower rank (e.g., rank 3→2). However, the strength of the effect is limited at this scale, so this concern is moved to Minor weaknesses with appropriate framing.

- **"Definition of Communication Redundancy is trivial / a tautology" (Harsh Critic, Critical Issue 3)** — Removed. The definition asserts the *existence* of a better subgraph, which is an empirical claim (not a tautology), verified by the preliminary experiment. A formal definition of the problem is standard and appropriate; it is not meant to solve the problem.

- **"Table 2 discrepancy — AutoGen 90.06 vs Complete Graph 86.49"** — Removed. These are different methods (AutoGen vs Complete Graph topology); there is no discrepancy.

- **"Robustness attack implementation deferred to appendix"** — Removed per hard rules. The appendix existed in the original submission; the parser stripped it.

- **"Missing cost analysis equation"** — Removed per hard rules. The blank equation (line 183) is a parser artifact.

- **"Multi-Query Training relegated to appendix"** — Removed. The main paper (Section 3.4) describes the idea in one paragraph and appropriately defers details to the appendix, which is standard practice.

- **Various generic/presentation nitpicks** — Removed per hard rules (formatting, typos, missing appendix details).

## Novel Insights

None beyond the paper's own contributions. The reviews raise standard experimental-concern points (the need for variance estimates, the small-scale regime, the probabilistic grounding of the optimization) but do not introduce fundamentally new perspectives on the work.

## Suggestions

1. **Clarify the policy gradient formulation.** Either provide a proper normalized distribution over subgraphs (e.g., independent Bernoulli with sigmoid-constrained parameters) or explicitly state the approximation being made and its validity. This is the most important issue to address.

2. **Report variance.** Run the main experiments (Table 1) multiple times with different seeds and report mean ± std, or at minimum provide bootstrap confidence intervals for the key accuracy comparisons.

3. **Directly trace the $5.6 vs $43.7 claim.** Add a short table or footnote that explicitly shows which methods, token counts, and pricing yield these specific dollar figures.

4. **Add a larger-scale experiment** with at least 10 agents on one benchmark to demonstrate that the method and the low-rank regularization are effective beyond the 3–5 agent regime.

5. **Explain the robustness mechanism** with a concrete example or analysis showing that pruned edges preferentially correspond to compromised agents' outgoing messages.

## Score and Decision

The paper addresses a timely and practical problem (token cost in LLM-MA systems) and provides compelling empirical evidence of cost savings with maintained performance. The overall method is well-motivated and the experiments are reasonably extensive. However, the policy gradient formulation has an unresolved technical issue — the definition of \(p_\mathbf{S}\) in Eq. 8 as a product of unnormalized continuous mask values does not obviously constitute a valid probability distribution over subgraphs, which is needed for the REINFORCE estimator to be theoretically sound. Combined with the lack of any variance reporting — which is essential given the stochastic nature of both LLM outputs and the sampling procedure — the paper's empirical claims are presented without the statistical rigor needed to fully support them. These issues are addressable in revision but substantively weaken the current version.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>