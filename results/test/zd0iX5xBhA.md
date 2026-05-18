Now I have all the information I need to produce the consolidated review. Let me synthesize everything carefully.

---

## Summary

This paper introduces System 1.x, a hybrid planning framework that interleaves fast System-1 (direct plan generation without search) and slow System-2 (explicit search over actions) reasoning within a single LLM. A learned controller decomposes problems into sub-goals and routes easy ones to System-1 and hard ones to System-2, guided by a user-specified hybridization factor x that controls the accuracy-cost trade-off. Experiments on Maze Navigation and Blocksworld show that System 1.x outperforms pure System-1, pure System-2, and a symbolic A* planner at matched exploration budgets, while offering both train-time and test-time controllability.

## Strengths

- **Consistent superiority over both System‑1 and System‑2 across budgets**: At the default budget of 13.6 states on Maze Navigation, System 1.x achieves 70.4% accuracy versus 48.7% for System‑1 and 37.2% for System‑2 — absolute gains of 21% and 33% respectively (Figure 2a, Section 4.1). This directly validates the core claim that hybrid planning with intelligent resource allocation outperforms either extreme at matched compute.

- **Controllability via the hybridization factor**: Training with different values of x (e.g., x=0.5 for System‑1.5 vs. x=0.75 for System‑1.75) yields models with systematically different accuracy‑efficiency trade-offs: System‑1.75 achieves 75.7% accuracy at 16.6 states compared to System‑1.5's 70.4% at 13.6 states (Figure 5, Section 4.3). This is a novel train‑time control mechanism absent from prior search‑trained planners (Searchformer, Stream‑of‑Search), which are purely System‑2 models without a built‑in knob for hybridization.

- **Generalizability across search algorithms**: System 1.x outperforms the corresponding System‑2 when trained on BFS, DFS, and A* traces (Figure 6, Section 4.3). For example, System‑1.x (BFS) beats System‑2 (BFS) by up to 39% at 17.4 states, demonstrating robustness to the choice of search algorithm.

- **Neuro‑symbolic variant matches or outperforms symbolic A***: Replacing the neural System‑2 with a symbolic A* solver, neuro‑symbolic System 1.x surpasses standalone A* by 39% at 11.6 states (70.5% vs. 31.0%) and matches A* at full budget (99.2%) (Figure 4, Section 4.2), demonstrating flexibility that pure neural or pure symbolic planners do not offer.

- **Sub‑goal decomposition is empirically critical**: The full System 1.x consistently beats the variant without sub‑goal decomposition (e.g., by 20% at 13.6 states in Maze, Figure 2a). In OOD Blocksworld, the variant without decomposition drops to near 0% while System 1.x with sub‑goals reaches 25% at 30 states (Figure 2b).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by its experiments and none of the identified issues invalidate them.

### Minor

- **Reliance on handcrafted hardness functions limits the generality claim.** The controller training data generation (Algorithm 1) depends on domain-specific hardness functions (obstacle count for Maze, block-position distance for Blocksworld). The paper asserts these "can be constructed for most planning domains where heuristic searches like A* are frequently applied" (Section 3), but this is an assumption rather than a demonstrated property. The paper does not compare against a controller trained without handcrafted hardness functions — e.g., using the model's own prediction uncertainty or a learned regressor — which would be a natural ablation to assess whether the method can transcend domain-specific engineering. The paper works well on the two tested domains, so this is not fatal, but it tempers the claimed generality.

- **Blocksworld OOD results show modest absolute performance for all methods.** At 30 states, System 1.x achieves 25% vs. System‑2's 13%, but at maximum budget both converge to ~28-30%. While the relative improvement is directionally positive, the best method still fails roughly 70-75% of the time on OOD instances (plan lengths 7-10). The paper presents this as "outperforms at all budgets except the highest, where comparable," which is accurate, but the practical significance of these relative gains is modest when absolute performance is so low. The System‑2 baseline is also naively truncated at test time rather than trained to be budget-aware, which may overstate System 1.x's relative advantage in this setting (though the paper acknowledges truncation is ad-hoc).

- **No confidence intervals or variance estimates for key results.** Blocksworld OOD evaluation uses only 200 test samples, and Figures throughout the paper lack error bars or confidence bands. Given the low accuracy numbers and modest test size, this makes it difficult to assess the statistical reliability of the reported advantages, especially for the OOD setting where the gap between methods is narrow at some budget levels.

- **The three-way (or two-way) decomposition is a rigid design choice without ablation.** Algorithm 1 always produces exactly one contiguous System‑2 segment of fixed proportional length x×n between two System‑1 segments. This assumes that hardness is concentrated in a single contiguous block. The paper acknowledges in limitations that "long plans might require more windows," but provides no experimental justification for why three sub-goals (or the contiguous-block assumption) is appropriate. An ablation varying the number of sub-goals or allowing non-contiguous decomposition would strengthen the paper.

### Trivial

- No analysis of training cost (e.g., computational overhead of training three LoRA adapters vs. a single System‑2). Including this would help practitioners assess the practical trade-offs.

## Nice-to-Haves

- Validate the hardness function by showing it correlates with actual model accuracy on sub-goals.
- Analyze cases where the controller's System‑1/System‑2 assignment is "wrong" and quantify the performance cost of such errors.
- Investigate whether a budget-aware System‑2 (trained with variable search budgets) would narrow the gap with System 1.x.
- For practitioners: discuss the mapping between x and token/state budgets more concretely.

## Removed Points

These points were flagged by the reviewers but are removed or downgraded per the review guidelines:

1. **"Missing appendix content about hardness function comparison."** — Removed per rule (parser strips appendix; the comparison exists in the original submission).

2. **"The paper claims to be a fully neural planner but requires search traces from symbolic solvers for training."** — Not a valid weakness: the paper is transparent about this (Section 2, lines 100-101), and this is the same setup as Searchformer and Stream‑of‑Search. The "fully neural" claim refers to inference-time self-containedness.

3. **"The mapping between x and compute is indirect; picking x from a state budget is post-hoc fitting."** — The paper primarily demonstrates controllability by training with different x values and showing systematic trade-offs. The suggestion about inverting the mapping (Section 5) is a discussion point, not a claimed contribution. The test-time bias control is presented as the more practical knob.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge with the paper's own framing and do not surface a fundamentally different perspective on the work.

## Suggestions

1. **Add a learned hardness baseline.** Even a simple learned regressor trained on validation data to predict sub-goal difficulty (or using the LLM's own confidence/uncertainty) would substantially strengthen the generality claim by showing the method does not fundamentally require handcrafted heuristics.

2. **Report confidence intervals for OOD Blocksworld results.** With only 200 test samples and low accuracy numbers, bootstrapped confidence intervals (or standard errors across multiple LoRA training seeds) would significantly improve the reliability assessment of the claimed improvements.

3. **Ablate the decomposition structure.** Vary the number of sub-goals (2, 4, or variable) or allow non-contiguous System‑2 segments to justify the design choice or, if performance is insensitive, strengthen the generality claim.

4. **Qualify the OOD narrative.** The paper should more prominently acknowledge that all methods perform poorly on OOD Blocksworld (~70-75% failure rate) and that System 1.x's advantage is primarily at low budgets, not in absolute success rate.

## Score and Decision

**Score:** 7.0 — A solid paper with a well-motivated idea, clean experiments on two domains, and clear empirical support for its core claims. The weaknesses are real but non-fatal and addressable through revision. The paper makes a meaningful contribution to LLM-based planning by introducing controllability and hybrid resource allocation.

**Decision:** Accept

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>