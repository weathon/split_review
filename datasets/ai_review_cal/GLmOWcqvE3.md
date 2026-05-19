- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces BOIL (Blackbox Oracle Information Learning), a method for learning transition probabilities over a directed graph for multi-agent coverage tasks. The core idea is to decompose edge probabilities into node stationary distributions × transition probabilities, then use gradient-free optimization with PageRank to minimize an entropy-like loss derived from visibility bounds. The paper also briefly sketches extensions to patrolling and reachability.

---

## Strengths

- **Handles non-reversible agent movements explicitly.** The paper formulates coverage over a directed graph $\mathcal{G}_d$ using global balance (Equation 2) rather than detailed balance, permitting one-way passages, elevation-constrained movement, and trapdoor scenarios that reversible-assuming methods (e.g., Rahili et al. 2017) cannot model. This is a genuine technical contribution. (Section 4.1, lines 94–96; Section 2, line 25.)

- **Loss function is independent of agent count.** Theorem 1 provides upper and lower bounds relating the visibility integral to $A(w) = \sum P((u,v))V_s((u,v))(w)$, and the resulting loss $\mathcal{L} = -\sum A(w)\log A(w)$ does not depend on $n$. This yields a scalable objective for multi-agent settings. (Lines 110–116; the statement "the proof also covers why the loss is independent of the agent count" at line 116.)

- **Empirical verification that the optimized distribution is internally consistent.** Figure 3 shows that the Optimal agent (which directly samples from the BOIL-derived transition distribution) converges to zero total variation distance from the target distribution, confirming that PageRank-based optimization successfully produces a consistent stationary distribution. (Lines 275–277.)

- **Computationally efficient optimization.** Algorithm 1 uses gradient-free optimization with PageRank as a subroutine, running on 19 CPU cores with no GPU. This is practical for medium-scale environments. (Line 214.)

---

## Weaknesses

### Fatal

None.

### Major

1. **The "blackbox oracle" framing is misleading and disconnected from the actual method.** The abstract and introduction repeatedly frame BOIL as extracting information from an oracle whose behavior "adapts to environmental changes" (lines 14–18). The $h^i_{(u,v)}(t)$ functions are said to be "generated from an oracle that provides paths for the agents" (line 104). Yet Algorithm 1 takes only the graph $\mathcal{G}_d$ and the loss $\mathcal{L}$ as input — it contains no oracle query, no oracle call, and no mechanism for interacting with any external information source. The "information" being extracted is simply the optimized transition probabilities $P(u \to v)$, computed entirely from the environment structure and visibility function. The authors acknowledge this gap at line 150 ("The oracle is supposed to give continuous paths but we solved for only the softer probabilistic constraint") without resolving it. This mismatch between the central framing and the actual method undermines the paper's claimed contribution. The method is a PageRank-based transition optimizer for coverage — a potentially interesting idea — but it is not a method for "extracting information from a blackbox oracle," and the paper would be improved by removing that framing.

2. **The loss function derivation is not properly justified.** The paper states that coverage can be defined as "maximizing the common information Liu et al. (2010)" (line 110) and that Theorem 1 allows reducing the problem to minimizing $\mathcal{L} = \sum_w -A(w)\log A(w)$. However:
   - "Common information" is never defined or explained. The citation to Liu et al. (2010) is not contextualized.
   - Theorem 1 provides inequalities bounding $\int Y_t(w)dt$ in terms of $nT\sum P V_s$ and $T\sum P V_s$, but the paper does not show how these bounds translate into the entropy-like loss $-\sum A\log A$. The loss appears to be the negative entropy of the $A(w)$ vector, which pushes $A(w)$ toward uniformity — but the connection from Theorem 1 to this specific loss is asserted, not derived.
   - The paper says "The proof also covers why the loss is independent of the agent count" (line 116) but does not provide the proof.
   
   This gap weakens the theoretical foundation: the reader cannot evaluate whether $\mathcal{L}$ is the correct objective for uniform coverage under the given formulation.

3. **The experimental evaluation is insufficient to support the paper's claims.** The abstract claims BOIL "surpasses heuristic approaches in complex environments," but the evidence does not support this:
   - **Only one environment** (a $36\times36$ grid) is tested. No ablation on environment size, graph connectivity, number of agents, or visibility function parameters is performed.
   - **No comparison to any state-of-the-art coverage method.** The paper itself admits "To our knowledge, no baseline provides a fair comparison for evaluation" (lines 216–217), but this means the central claim of "surpassing heuristic approaches" is untested against any standard baseline from the cited literature (e.g., Stern et al. 2006, Rahili et al. 2017, Mathew & Mezic 2011).
   - **The most favorable results come from an unrealistic agent.** The "Optimal Agent" and "OptRandom Agent" both teleport across the graph, violating the movement continuity constraints the method is designed to respect (lines 225, 249). The "Sample Agent" and "Comm Sample Agent," which do respect continuity, fail to converge to the BOIL distribution within $10^5$ steps (Figure 3: "it plateaus for the Sample and Comm Sample agents, though it continues to decrease slowly").
   - **Results are from 10 runs only** with no statistical significance testing reported.
   - **Figure 2 interpretation is confusing:** a "prominent peak" in the Optimal agent's visibility count distribution is presented as desirable (line 270–274), but for a uniform coverage task, a flatter distribution across nodes would be expected. The paper does not clarify why peaking at certain nodes represents "effective utilization."

### Minor

4. **Algorithm 1 omits several details needed for reproducibility.** The PageRank subroutine's damping factor is not specified. The gradient-free optimization's step size $\mu$ and number of steps $N$ are listed as inputs but the values actually used in experiments are not reported. The non-reversible MH sampling mentioned in Section 5.1 (line 236) is referenced but not described in sufficient detail to replicate. These details are not fatal — the algorithm structure is clear — but they hinder verification.

5. **Extension claims (patrolling, reachability) are stated without any empirical support.** Section 6.1 replaces the loss function over $V$ with one over $V_p \subseteq V$ for patrolling, and swaps visibility for a reachability function for reachability (lines 293–301). No experiments, analysis, or even illustrative examples are given. These are suggestions for future work, not contributions, but the abstract and conclusion present the applicability to "coverage, patrolling, and stochastic reachability" as part of the paper's contribution (lines 4, 305).

6. **Theorems 3 and 4 (fine-grained estimation) are proposed but never empirically validated.** The path-augmentation (Theorem 3) and temporal partition (Theorem 4) methods are presented as central to "fine-grained control over trade-offs" (Section 4.3), but no experiment tests whether they improve coverage quality or provide meaningful spatial/temporal resolution. They remain purely theoretical.

### Trivial

None.

---

## Nice-to-Haves

- **Remove the oracle framing entirely** and describe the method as learning transition probabilities for coverage under flow constraints. This would align the presentation with the actual algorithm and remove the central disconnect.
- **Provide a proper derivation of the loss function** showing how the bounds in Theorem 1 lead to the entropy objective $\mathcal{L}$, or replace it with a more directly justified objective.
- **Add at least one additional benchmark environment** and compare against a standard coverage method (e.g., ergodic control, genetic algorithm, or a properly cited baseline).
- **Report the hyperparameter values** ($\mu$, $N$, PageRank damping factor) used in the experiments.
- **Report the convergence behavior of the BOIL optimization itself** (loss over optimization steps) to verify that Algorithm 1 converges.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No code, no hyperparameters" details about trivial implementation specifics** — Algorithm 1's structure is described; full hyperparameter values are a reasonable ask but the critic's framing as a fatal omission is excessive. Moved to Minor (#4 above).
- **"Notation is unnecessarily complex"** (Section 4.1) — subjective presentation preference, not a weakness of the method.
- **"Figures appear grayscale"** — parser/formatting artifact, not an author error.
- **"No analysis of how the loss function relates to the probability that all nodes are covered"** — beyond the standard scope for a conference paper; the entropy framing is a common proxy for uniformity.
- **"The paper cannot be accepted in its current form" and "The problems are not fixable"** — these are the critic's overall opinion, not a specific weakness. The assessment below supersedes them.
- **"Missing related works"** — cannot verify without external sources.
- **Strength: "Fine-grained control over trade-offs"** — Theorems 3 and 4 are never empirically validated, making this strength speculative rather than evidence-based.
- **Strength: "Scalable loss function"** — kept as a strength because it is concretely shown (loss does not depend on $n$).

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the oracle framing mismatch and the insufficient evaluation, but neither reviewer identifies a novel perspective on the underlying coverage problem that the paper itself does not contain.

---

## Suggestions

1. **Redescribe the method without the oracle framing.** State the contribution as learning transition probabilities over a directed graph for coverage via PageRank-based optimization. This is honest and removes the paper's most misleading aspect.
2. **Derive the loss function rigorously** or replace it with a more clearly motivated objective (e.g., direct minimization of the total variation distance to uniform coverage).
3. **Expand the evaluation** to at least two environments, include a genuine coverage baseline from the literature (even if it must be adapted to non-reversible settings), and report convergence of the BOIL optimization itself.
4. **Focus on the Sample Agent** — analyze why it converges slowly and characterize the gap between the optimized distribution and achievable agent trajectories. This is the paper's most practically relevant finding.

---
