## Summary

This paper identifies a genuine limitation of the Multiple Gradient Descent Algorithm (MGDA): when objectives have structured variable dependencies that prevent joint strict convexity, MGDA can converge to Pareto stationary points that are not Pareto optimal. The paper proposes RP-MGDA, which partitions variables according to a dependency-based procedure before applying MGDA updates per partition. The core idea—that variable dependency structure matters for MGDA, and that careful partitioning can improve solution quality—is clearly motivated and illustrated with clean toy examples.

---

## Strengths

- **Concrete identification of MGDA's precise failure mode (§3.2).** The paper provides a minimal 2-variable bi-objective example where both objectives are individually strictly convex but MGDA converges to dominated solutions. This cleanly isolates the mechanism: because neither objective is strictly convex in *all* variables jointly, the Lemma 1 guarantee does not apply. The example is reproducible and pedagogically effective.

- **Quantitative evidence that the failure is systematic, not rare (§5.1).** On a 3-variable chain-structured quadratic problem, 372 out of 512 uniformly random initializations (72.66%) lead MGDA to inferior Pareto stationary solutions. This establishes the problem as pervasive rather than an edge case.

- **Empirical demonstration that conventional regularization does not fix the problem (§5.1).** The paper varies regularization strength and shows that it either recovers the same poor stationary set (small regularization) or moves solutions further from the Pareto front (large regularization). This supports the claim that the root cause is the variable dependency structure itself.

- **Clear counterexample motivating why naive full partitioning fails (§4.1).** A concrete 2D bi-objective example with gradients ∇f₁=(1,3) and ∇f₂=(-3,-1) shows that coordinate-wise MGDA stops immediately while full MGDA finds a valid descent direction. This justifies why the proposed partitioning must be *refined* rather than exhaustive.

---

## Weaknesses

### Fatal

**1. The core partitioning procedure — the paper's central contribution — is not specified.**

Section 4.2 states that the refined partitioning "consists of three rules." However, Section 4.2.1 ("Refined Partitioning Procedure") is empty — no text follows the subsection header before Section 5 begins. The three rules are never formally described:

- **Rule I** is never mentioned by name or described anywhere in the text. The figure caption refers to a "Dense block" rule but provides no definition.
- **Rule II** (the "Loop" rule) is partially inferable from a brief application in §5.2 ("a loop with different colors of length 3 exists") but the general condition — what constitutes a loop, what "different colors" means precisely, and when merging is triggered — is never formally stated.
- **Rule III** is described only as "the remaining variables are partitioned and optimized separately" (again from §5.2).

The algorithm sketch (lines 187–191) calls `REFINED_PARTITION(M)` without defining this function. A reader cannot implement RP-MGDA from the paper as written. For a methods paper whose entire contribution is a new algorithmic procedure, this is a fatal structural deficiency. The method cannot be evaluated, reproduced, or compared.

### Major

**2. Experiments are limited to tiny synthetic quadratic problems (2–5 variables), far below the ML applications used to motivate the work.**

The introduction and background frame the contribution as relevant to multi-task learning, federated learning, reinforcement learning, and fair ML. The paper references "a personalized federated learning setting" as a key motivating scenario. Yet every experiment in the main text is on hand-crafted 2- to 5-variable quadratic problems with no evaluation on any actual ML task. This creates a near-total gap between the claimed scope and what is demonstrated. Even a small-scale experiment on a standard multi-task learning benchmark would substantially increase credibility.

**3. The chain example (§5.1) does not state what partitioning RP-MGDA actually uses.**

The 3-variable chain problem (f₁=θ₁²+θ₂², f₂=(θ₂−1)²+(θ₃−1)²) is the paper's main quantitative experiment (512 initializations, regularization ablation). Yet the paper never explains which variables are grouped and which are separated under the proposed partitioning rules. Without this information, the reader cannot determine whether the reported advantage follows from the rules or from an ad-hoc choice, and the experiment is not reproducible.

### Minor

**4. Theoretical claims about RP-MGDA are stated only informally in the main text.**

The introduction claims the paper "give[s] theoretic analysis of the algorithm, and demonstrate[s] its superiority over MGDA." The conclusion states "We demonstrated theoretically that RP-MGDA is at least as good as MGDA." However, the main text contains no formal statement (theorem, proposition, or even a precise definition of what "at least as good" means — dominated limit points? convergence rate? something else?). If the formal claims and proofs are in the appendix (stripped by the parser), the main text should at minimum contain the theorem statements.

**5. The regularization experiment (§5.1) is observational, not analytical.** The paper reports that larger regularization worsens solutions and smaller regularization recovers MGDA's poor stationary set, but offers no explanation of *why* this happens. A deeper analysis would strengthen the structural claim.

### Trivial

None.

---

## Nice-to-Haves

- A sensitivity analysis of how the partitioning rules respond to misspecification or noise in the dependency matrix M.
- A discussion of computational cost: running MGDA per group may require multiple min-norm oracle solves per iteration, depending on the number of groups.
- A comparison with other multi-objective gradient methods (PCGrad, CAGrad) mentioned in the abstract — though this is outside the paper's stated scope of improving vanilla MGDA, such comparisons would help calibrate the practical significance of the improvement.

---

## Removed Points

These points were raised by the reviewers but are removed or demoted per the filtering rules. Treat with caution.

- **Theoretical analysis "absent" from the paper**: The paper references §A.2 for theoretical analysis; the appendix was stripped by the parser. The criticism is demoted to a minor point about main-text structure rather than a claim of absence. *(Hard rule: missing appendix content)*
- **Federated learning example referenced but not in main text**: This content was in the appendix, which was stripped. Removed. *(Hard rule: missing appendix content)*
- **No comparison to PCGrad/CAGrad**: The paper's scope is improving vanilla MGDA; comparing to other methods is a nice-to-have, not a required baseline. Moved to Nice-to-Haves.
- **The 2-variable motivating example is trivially solvable**: The paper explicitly acknowledges this ("partitioning the variables and then separately optimizing them is a simple but effective approach"), using the example only as motivation for why a more systematic approach is needed for complex dependencies. The point does not weaken the paper.
- **Computational cost / sensitivity analysis / larger datasets**: These are speculative demands for content not standard for a theoretical-methods paper at this stage. Moved to Nice-to-Haves.
- **Formatting, style, and parser-artifact nitpicks**: Parser issues, not author errors. Removed.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Specify the partitioning rules completely.** Write out Rules I, II, and III in formal terms (with definitions, conditions, and pseudocode). Until this is done, the paper has no method to review.
2. **State the theoretical claim formally.** Provide at least one theorem or proposition in the main text (e.g., "Under [conditions], the Pareto front found by RP-MGDA dominates the Pareto front found by MGDA"), even if the proof is deferred.
3. **Run one experiment on a real ML problem.** Even a small-scale multi-task learning or fair ML benchmark would bridge the gap between the claimed scope and the demonstrated scope.
4. **State the partitioning explicitly for every experiment.** For each problem, show which variables are grouped, which are separated, and which rule justifies each decision.

---

## Score and Decision

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>