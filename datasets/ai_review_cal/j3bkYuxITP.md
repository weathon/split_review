- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper identifies a limitation of the Multiple Gradient Descent Algorithm (MGDA): it can converge to suboptimal Pareto stationary points when objectives are individually but not jointly strictly convex. The paper proposes RP-MGDA, which partitions variables based on objective-dependency structure and applies MGDA separately per partition. The motivating examples and two synthetic experiments show that RP-MGDA avoids suboptimal stationary points that vanilla MGDA gets stuck on.

## Strengths

- **Identifies a genuine, well-documented failure mode of MGDA with quantitative evidence.** Section 3.2 gives a clean bi-objective example (Equation 8) showing that individually strictly convex objectives are insufficient for Pareto optimality under MGDA because joint strict convexity can fail. Section 5.1 confirms this empirically: on a 3-variable chain problem, MGDA converges to suboptimal stationary solutions for **72.66%** of 512 random initializations (Figure 4), while RP-MGDA consistently reaches the true Pareto front.

- **Demonstrates that standard fixes (regularization) do not resolve the issue.** The regularization experiment (Figure 5) systematically tests adding strong-convexity-inducing regularization. Large regularization pushes solutions farther from the Pareto front; small regularization recovers the suboptimal stationary set. This evidence supports the paper's argument that the limitation is structural and requires accounting for variable dependencies, not just stronger convexity.

- **Sound core conceptual idea.** The basic insight — that when objectives have structured variable dependencies, applying MGDA holistically ignores that structure and can yield suboptimal stationary points — is correct and relevant. The paper correctly identifies a tradeoff: naive full partitioning can also fail (Section 4.1 gives a concrete example where coordinate-wise MGDA yields zero descent), motivating a principled middle ground.

## Weaknesses

### Major

- **Experimental evidence is far too thin to support the paper's broad claims.** The paper claims RP-MGDA "outperforms MGDA in many cases" and motivates the work with multi-task learning, federated learning, and reinforcement learning. Yet experiments are limited to **two tiny synthetic problems**: a 3-variable chain (Section 5.1) and a 5-variable random dependency matrix (Section 5.2). Both are quadratic (with one non-smooth variant). No real-world tasks from any of the motivated domains are included. Only vanilla MGDA is used as a baseline; no comparison to other multi-objective methods (e.g., PCGrad, CAGrad, or even weighted-sum approaches). This level of evidence is insufficient to establish the method's practical value or its claimed superiority "in many cases."

- **No ablation study to isolate the contribution of the "refined" partitioning rules.** The paper does not test whether any reasonable partitioning (e.g., random grouping, greedy partitioning, or even full independent optimization) would achieve similar or better results on the same problems. Without such an ablation, it is unclear whether the specific three rules matter, or whether the benefit comes simply from separating variables that have disjoint objective dependencies — which would be obvious from the problem structure in both examples. The chain example's correct partition (θ₁ alone, θ₂ with both, θ₃ alone) is essentially given by inspection.

### Minor

- **The claim about extending RP-MGDA to other methods (PCGrad, CAGrad) is stated but never explored.** The abstract and conclusion assert that "the concept of refined variable partitioning in RP-MGDA is not limited solely to MGDA and holds promise for enhancing other multi-objective gradient methods." The paper provides no argument, sketch, or experiment to support this, and the relationship between the stationary-point issue addressed here and the gradient-conflict issues addressed by PCGrad/CAGrad is not discussed.

- **The motivating example (Section 3.2) involves completely separable variables** (f₁ depends only on w₁, f₂ only on w₂), where any sensible partition would work. The paper does not discuss the more challenging middle ground: problems with partial overlap where the correct partition is non-obvious. The 5×5 random matrix example partially addresses this but is still a tiny synthetic instance.

### Trivial

- None.

## Nice-to-Haves

- **Discussion of how to obtain the dependency matrix M in practice.** In most ML settings (deep networks, multi-task architectures), the dependency structure is complex and not known a priori. The paper assumes M is given but does not address how to construct it.

- **Computational cost analysis.** RP-MGDA runs multiple independent MGDA subproblems per iteration. The paper should compare the per-iteration cost and convergence rate to vanilla MGDA.

- **Scalability discussion.** The experiments max out at 5 variables. The paper would benefit from at least discussing whether the approach scales to problems with thousands of variables (e.g., neural network parameters) and whether the dependency graph structure can be exploited efficiently.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The partitioning procedure is not specified (structural flaw)."** The paper states "three rules" (line 182–183) and a heading for subsection 4.2.1 "REFINED PARTITIONING PROCEDURE" (line 195) exists, but the content between line 195 and the next section heading (line 199) is missing from the extracted text — this is a PDF-extraction artifact, not an author omission. Fragments of Rules (II) and (III) are reconstructible from Section 5.2, and Rule (I) ("Dense block") is referenced in Figure 2. The full specification was likely present in the original submission.

- **"Theoretical guarantees claimed but unsubstantiated in the main text."** The paper states "we give theoretic analysis" (line 31) and "we demonstrated theoretically that RP-MGDA is at least as good as MGDA" (line 255), but no theorem or proof appears in the extracted text. The theoretical analysis may have been in the missing subsection 4.2.1 or in the appendix (which is referenced but stripped by the parser). Given that the parser systematically strips appendices and the content of Section 4.2.1 is missing, this cannot be verified as a genuine omission.

- **"Missing comparison to PCGrad/CAGrad/GradNorm as baselines."** These methods address a different limitation of MGDA (stochastic gradient conflict in deep multi-task learning) rather than the deterministic stationary-point suboptimality issue that RP-MGDA targets. A comparison would be informative but is not required to evaluate the paper's core claim.

- **Strength: "Empirical validation across different dependency structures."** While technically true (chain structure and random matrix), the validation is on only two tiny synthetic problems. This is more accurately characterized as a limitation than a strength given the paper's broad claims.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder converge on the same core assessment: the paper identifies a real MGDA limitation and proposes a sensible conceptual fix, but the execution is too preliminary (thin experiments, no ablation, no real-world validation) to support the claimed scope.

## Suggestions

1. **Expand experiments significantly.** At a minimum: (a) test on problems with more variables (10–100), (b) include at least one realistic problem from the motivated domains (e.g., a small multi-task learning problem with known or learnable task-variable dependencies), (c) add baselines beyond vanilla MGDA (e.g., weighted-sum optimization, PCGrad, or a simple "partition everything" baseline), and (d) run an ablation comparing the refined partition to random/simple partitions of the same granularity.

2. **Add an ablation study** that compares refined partitioning to: (i) no partitioning (vanilla MGDA), (ii) full per-variable partitioning (coordinate-wise MGDA), and (iii) a random grouping with the same number of partitions. This would isolate whether the specific rules matter or whether any reasonable grouping suffices.

3. **Provide guidance on constructing the dependency matrix** for practical problems, or at minimum discuss the assumptions under which such a matrix can be obtained.

4. **Either substantiate or remove the claims about extending to other methods** (PCGrad, CAGrad). A brief argument about how the partitioning idea would transfer would suffice.
