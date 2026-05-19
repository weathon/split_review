- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5
Now I have all the information I need. Let me synthesize the final review.

## Summary
This paper proposes Dynamical Skill Refinement (DSR), an on-policy skill-based RL method that unifies the optimization objectives of the high-level policy and skills. The paper provides theoretical analysis showing monotonic improvement in the temporally abstract MDP (TA-MDP) and establishing that optimizing in the TA-MDP is equivalent to optimizing a lower bound of performance in the original MDP. It identifies "skill space collapse" as a novel phenomenon where direct skill refinement degrades all skills due to shared parameters, and proposes an RND-based dynamic weighting mechanism to prevent this. Experiments on four robotic manipulation tasks compare DSR against SPiRL, Skill-Critic, ReSkill, PPO, and PPO+BC.

---

## Strengths

1. **Theoretical guarantee of monotonic improvement in TA-MDP (Theorem 1).** The paper proves that the proposed unified update formulae yield a non-decreasing state value function in the TA-MDP, a formal guarantee that prior on-policy skill-refinement methods like ReSkill lack due to their inconsistent optimization objectives across the two levels.

2. **Novel theoretical connection between TA-MDP and original MDP (Theorem 3).** The paper establishes that with \(\tilde{\gamma} = \gamma^H\), optimizing the hierarchical policy in the TA-MDP is equivalent to optimizing a lower bound of its performance in the original MDP for sparse-reward tasks. This grounds skill-based RL as a proxy for flat RL, moving beyond prior work that treats them as parallel paradigms.

3. **Identification and mitigation of skill space collapse.** Section 5.2 identifies the novel phenomenon that directly refining skills embedded in a shared parametric low-level policy causes stochastic degradation of all skills. The proposed DSR mechanism (residual policy + RND-based dynamic weighting) is a practical solution, and Figure 7 empirically validates that it prevents collapse on PyramidStack where direct refinement fails entirely.

4. **Empirical validation against ReSkill — the most relevant baseline.** DSR outperforms ReSkill on 3 of 4 tasks (TableCleanup, PyramidStack, ComplexHook) with lower variance, and is competitive on the 4th (SlipperyPush). This comparison is fair and directly supports the paper's core algorithmic claims.

5. **Ablation confirming the necessity of both refinement and the DSR mechanism.** Figure 7 distinguishes three conditions: NoRefinement (limited asymptotic performance), DirectRefinement (fails on PyramidStack due to skill space collapse), and DSR (succeeds). This cleanly isolates the value of the proposed mechanism. Figure 8 further confirms that refined skills improve optimality under the same high-level policy.

---

## Weaknesses

### Fatal
None.

### Major

1. **Unfair comparison against Skill-Critic undermines "temporal abstraction shift" argument.** The paper removes Skill-Critic's SPiRL-based warm-up phase (lines 202-204), which the authors themselves acknowledge "Skill-Critic depends on" (line 16-17). The resulting performance collapse is then attributed to ignoring temporal abstraction shift. This conflates two issues: removing a method's critical initialization component versus the method's inherent properties. The argument that "the temporal abstraction shift can not be ignored" (line 204) is not fairly supported by this comparison. The authors should either compare against Skill-Critic as originally proposed (with warm-up) or explicitly justify why the ablated variant is the relevant comparison for their specific claim. This does not invalidate the paper's core contributions (which stand on the ReSkill comparison and theoretical analysis) but does weaken a secondary supporting argument and the broad "SOTA" framing.

### Minor

1. **The RND-based weighting mechanism is heuristic with limited analysis.** The mapping from RND prediction error to action-increment weight is described only in vague terms ("We can map the prediction error... to the weight of action increment," line 180), with no explicit functional form provided. The paper provides no analysis of why this specific design avoids collapse, how hyperparameters \(c\) and \(k\) relate to the interference dynamics, or whether RND error is a reliable proxy for "sufficiently refined." The PyramidStack ablation (Figure 7) provides empirical support, but this is a single task; the mechanism's behavior on tasks where RND predictor convergence is different (e.g., high-dimensional skill spaces) is unexplored.

2. **The lower-bound framing (Theorem 3) is technically correct but warrants clearer qualification.** The paper states that "refining skills under this objective is equivalent to optimizing the lower bound of \(V(s)\)" (line 149). While this statement is mathematically correct, a reader could infer that an increase in \(V^h\) guarantees an increase in the original MDP performance \(V\). It does not: because the TA-MDP dynamics \(p_{\pi^l, H}\) change as \(\pi^l\) is updated, \(V\) and its lower bound are measured under different MDP dynamics at each iteration. The paper would benefit from explicitly discussing this gap and the conditions under which the bound meaningfully tracks actual task performance.

3. **Limited diagnosis of skill space collapse.** The paper motivates skill space collapse with a helpful conceptual illustration (Figure 4) but provides no quantitative analysis — e.g., tracking cosine similarity of skill embeddings, change in VAE reconstruction error on fixed test segments, or correlation between RND error and interference magnitude — to confirm the hypothesized mechanism. Figure 7 shows DSR prevents performance collapse, but the internal dynamics of collapse remain inferred rather than directly measured.

4. **Hyperparameter sensitivity analysis is limited.** Figure 9 tests only one task (TableCleanup) with narrow ranges (\(k\) varied from -400 to -200, \(c\) from 0.2 to 0.6). Demonstrating insensitivity on a single task with modest ranges does not constitute strong evidence of robustness, especially for a method whose core mechanism depends on two hand-scripted parameters and an RND training budget.

### Trivial
None.

---

## Nice-to-Haves

- Include a comparison of computational cost / wall-clock time across methods.
- Benchmark against Skill-Critic with its warm-up (as originally published) to provide a complete picture.
- Report statistical significance measures (e.g., confidence intervals or p-values) beyond means over 4 seeds.
- Provide the explicit functional form of the RND-error-to-weight mapping to aid reproducibility.

---

## Removed Points

These points were flagged by reviewers but are removed per the filtering guidelines:

1. **"Proofs are relegated to an appendix we do not have"** — Removed. The parser strips appendix sections from all papers; proofs exist in the original submission.
2. **"Code is not mentioned"** — Removed per hard rule against reproducibility nitpicks about code release.
3. **"Missing comparison with flat RL methods using action repeat"** — Removed as scope creep; the paper already compares with PPO and PPO+BC, and its scope is skill-based RL.
4. **"The relationship between TA-MDP and original MDP via discount-factor adjustment is standard in the options literature"** — Removed. The specific lower-bound framing and its use to justify skill refinement as a proxy for flat RL optimization is not a standard result; the paper's contribution here is in the framing and application, not the discount-factor identity itself.
5. **"Missing related works"** — Removed per instruction: DO NOT mention missing related works without external sources.
6. **"Typographical and formatting issues"** — Removed as parser artifacts.
7. **"The paper claims state-of-the-art results but does not report statistical significance tests"** — Removed. The paper reports means over 4 seeds with learning curves, which is standard practice in this subfield; significance testing is not a requirement.

---

## Novel Insights

Beyond the paper's own contributions, a novel observation emerges from synthesizing the reviews: the paper's theoretical framing exposes a subtle gap in how the field evaluates skill-refinement methods. Prior work (ReSkill, Skill-Critic) either separates the high-level and low-level objectives or uses off-policy updates without addressing non-stationarity. The paper's Theorem 3 makes explicit that skill-based RL with refinement is fundamentally a lower-bound optimization problem — a framing that simultaneously justifies the approach and surfaces the limitation that the lower bound is with respect to a changing MDP. This reframing could serve as a template for analyzing other hierarchical methods that jointly optimize across temporal abstraction levels.

---

## Suggestions

1. **Address the Skill-Critic comparison directly.** Either include Skill-Critic with its warm-up stage (as originally published) as an additional baseline, or explicitly argue why the ablated variant is the appropriate comparison for isolating the temporal abstraction shift effect. Clarify that the paper's core claims do not depend on this comparison (they are supported by the ReSkill comparison and ablations).
2. **Provide the explicit functional mapping** from RND prediction error to the action-increment weight, not just a verbal description.
3. **Add quantitative analysis of skill space collapse**, e.g., tracking the entropy or variance of skill-conditional action distributions over training, or measuring reconstruction error changes on held-out demonstration segments, to substantiate the claimed mechanism.
4. **Broaden the hyperparameter sensitivity study** to at least one additional task and wider parameter ranges.
5. **Discuss the theoretical limitation** that the lower bound guarantee (Theorem 3) is per-iteration and cumulative improvement in \(V\) depends on the bound not loosening as the policy changes, so that readers have a clear understanding of what is and is not guaranteed.

---
