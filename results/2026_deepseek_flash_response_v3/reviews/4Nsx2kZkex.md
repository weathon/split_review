## Summary

This paper proposes DV-RL, a framework that replaces discrete formal verification oracles (SMT solvers) with differentiable surrogate functions integrated into the RL policy gradient loop for code synthesis. The approach uses bilevel optimization: an inner loop trains a surrogate to approximate the discrete verifier, while an outer loop optimizes the policy using the surrogate-augmented reward. Experiments on 100 programming tasks (algorithmic, system programming, DSL) report 95.8% verification success rate (VSR), 74.6% functional correctness (FC), and 85ms per verification check.

---

## Strengths

1. **Novel formulation of differentiable verification surrogates for RL-based code synthesis.** The core idea — replacing discrete SMT verification calls with learned differentiable approximations trained via bilevel optimization (Eq. 8–9) — is genuinely novel and addresses a real limitation of prior work that treats verification as a post-hoc filter or black-box reward. This is a meaningful departure from existing paradigms.

2. **Well-structured ablation study.** Table 2 systematically ablates four components: bilevel optimization (+6.6% VSR), hierarchical verification (+12.4%), gradient injection (+17.2%), and hard-constraint calibration (+4.3%). Each component's individual contribution is clearly quantified, providing good evidence that the design choices are not arbitrary.

3. **Practical efficiency gains at inference.** The 85ms per verification check (Table 1) versus 420ms for post-hoc SMT and 380ms for constrained RL demonstrates a genuine practical advantage of the learned surrogate once trained.

4. **Hard-constraint injection mechanism (Eq. 13).** The periodic mixing of exact verification results with the learned surrogate ($\tilde{V}_{\text{final}} = (1-\gamma)\tilde{V} + \gamma V$) is a well-motivated design that addresses surrogate drift — a known failure mode for learned approximations of formal systems.

---

## Weaknesses

### Fatal
None.

### Major

1. **Numerical claims in the text are inconsistent with Table 1.** The paper states "DV-RL improves verification success by 26.5% over pure RL and 6.1% over constrained RL" (line 274). However, from Table 1: Pure RL VSR = 38.2%, DV-RL = 95.8% (absolute difference 57.6 pp, relative ~151%); Constrained RL VSR = 75.3%, DV-RL = 95.8% (difference 20.5 pp, relative ~27%). Neither "26.5%" nor "6.1%" matches any plausible computation from the reported values. This undermines confidence in the paper's quantitative claims and suggests either the text or the table contains errors that must be resolved.

2. **Gradient flow through discrete program generation is not explained, leaving the method underspecified.** Equation 7 (line 128) writes: $\nabla_\theta J(\theta) = \mathbb{E}_{P \sim \pi_\theta} [\nabla_\theta \log \pi_\theta(P) \cdot R(P)] + \lambda \nabla_\theta \tilde{V}(P, \phi)$. The first term is standard REINFORCE. The second term, $\lambda \nabla_\theta \tilde{V}(P, \phi)$, treats the differentiable surrogate as directly differentiable with respect to policy parameters $\theta$. However, $\tilde{V}$ takes program $P$ as input, and $P$ is generated through discrete token sampling from $\pi_\theta$. The paper provides no mechanism for how $\nabla_\theta \tilde{V}(P, \phi)$ is computed — whether through Gumbel-Softmax, straight-through estimators, REINFORCE-style score functions, or some other method. This is not a minor implementation detail; it is central to whether the claimed gradient-based safety refinement is feasible. Without this, the method as described cannot be reproduced or evaluated.

### Minor

3. **Figure 2 is presented in a misleading manner.** The stacked area chart (and accompanying table) shows "Total" proportions reaching 191% (94% memory safety + 97% termination guarantees). These two safety properties are not mutually exclusive — a snippet can satisfy both — so summing their percentages can exceed 100% because overlapping snippets are double-counted. However, the y-axis is labeled "Proportion of Generated Code Snippets (%)" and the stacked area chart format visually implies parts of a whole. This presentation is substantially misleading. A grouped bar chart or separate line plots would be appropriate. The data itself is not impossible, but its communication is poor.

4. **Selective comparison with Syntax-Guided synthesis.** Syntax-Guided achieves 97.5% VSR — higher than DV-RL's 95.8% — yet the paper's "Key observations" (lines 274-276) highlight improvements only over Pure RL and Constrained RL. The paper acknowledges Syntax-Guided only in the context of FC ("+11.4% higher FC than syntax-guided approaches"), omitting that this baseline outperforms the proposed method on the primary metric. The trade-off (higher FC, slightly lower VSR) should be honestly discussed.

5. **Partial program verification is assumed without justification.** Equation 10 uses $\tilde{V}(P_{\leq t}, \phi)$ to compute verification scores on *partial programs* (incomplete ASTs) during token-level generation. The paper does not explain how the differentiable surrogate evaluates safety properties on incomplete code. For properties like memory safety and termination, which are defined over complete executions, evaluating them on partial programs is a known hard problem. This design choice needs explicit justification and methodological support.

6. **Training cost of the surrogate is not accounted for.** The 5× verification efficiency improvement (85ms vs 420ms, Table 1) compares the learned surrogate's inference time to SMT solver time. However, training the surrogate (Eq. 8) requires running the exact SMT verifier on generated programs to produce ground-truth labels $V(P, \phi)$. The total system cost — number of SMT calls during training, total wall-clock time to convergence — is never reported. The efficiency comparison conflates inference efficiency with total system efficiency.

### Trivial

7. The contributions paragraph (line 19) contains a garbled sentence: "handling right-of-way and correctness while generality and specificity, using bilevel programming." This should be revised for clarity.

---

## Nice-to-Haves

- Adding variance/confidence intervals to the reported results would strengthen the experimental analysis.
- An analysis of what the surrogate actually learns (e.g., correlation between surrogate scores and ground-truth verification on held-out programs) would help verify that gradients are semantically meaningful.
- A discussion of how safety properties are formalized for each benchmark task would improve reproducibility.

---

## Removed Points

These points were considered but removed after verification against the paper:

- **"Figure 2 data is fabricated/numerically impossible"** — Removed. The data shows two overlapping properties whose percentages are summed (not the union). While the stacked chart format is misleading, the data itself is not impossible. Demoted to Minor (#3 above).
- **"KL divergence with degenerate V distributions causes infinite loss"** — Removed. This is a minor technical detail easily handled with standard epsilon-clipping; it does not constitute a structural flaw.
- **"Bilevel optimization still requires SMT, undermining the core motivation"** — Removed as stated. The surrogate is trained using exact verification (standard for student-teacher setups), and inference is SMT-free. The training cost concern is folded into Minor #6.
- **"Missing related works"** — Removed per instructions (cannot independently verify existence of cited works).
- **"LLM polishing / writing quality concerns"** — Removed (parser artifacts and style issues per instructions).
- **"No specification of SMT solver details or property formalization"** — Removed; implementation details at this level are not a requirement for a conference submission.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Reconcile the numerical claims** in lines 274-276 with the values in Table 1. Clarify whether the percentages refer to absolute percentage points, relative improvement, or some other measure.
2. **Explain how $\nabla_\theta \tilde{V}(P, \phi)$ is computed** given discrete program generation. Specify the gradient estimation technique (Gumbel-Softmax, straight-through, REINFORCE, etc.) and, ideally, provide a diagnostic experiment showing that safety gradients correlate with meaningful program edits.
3. **Replace Figure 2** with a non-stacked visualization (grouped bars or separate line plots) and clarify in the caption that the two safety properties are not mutually exclusive.
4. **Acknowledge the Syntax-Guided comparison honestly** — discuss the VSR vs. FC trade-off explicitly.
5. **Explain how the surrogate evaluates partial programs** in Eq. 10, or clarify the scope of the claim.
6. **Report total training cost** including the number of SMT solver calls and wall-clock time to convergence.

---

## Score and Decision

### Calibration

**Round 1 — Bracketing (5 bands across the score range):**

| Band | Sample Path | Avg Score | Comparison |
|------|------------|-----------|------------|
| Strong Reject (<2.5) | `/home/.../dsALpkd1OU.md` | 1.67 | Much weaker — paper has no coherent contribution |
| Weak (2.5–4.5) | `/home/.../N18Z2MkMEa.md` | 3.00 | Similar profile (interesting idea, flawed execution) |
| Weak (2.5–4.5) | `/home/.../8oNzf7u5lT.md` | 3.67 | Comparable — interesting idea with implementation concerns |
| Weak (2.5–4.5) | `/home/.../GFaplOjE7E.md` | 4.25 | Better execution but less novel |
| Middle (4.5–6.1) | `/home/.../vLqkCvjHRD.md` | 4.75 | Better experiments, cleaner presentation |
| Middle (4.5–6.1) | `/home/.../vf8iou7FNF.md` | 5.75 | Significantly stronger — thorough eval across domains |
| Strong (>7.5) | `/home/.../OI3RoHoWAN.md` | 8.00 | Far stronger — top-tier execution |

**Round 1 bracket: 2.5–5.0**

**Round 2 — Narrowing (3 queries inside the bracket):**

| Sample Path | Avg Score | Comparison |
|------------|-----------|------------|
| `/home/.../N18Z2MkMEa.md` (FALCON) | 3.00 | Similar issues: interesting framing, execution problems |
| `/home/.../zPPy79qKWe.md` (RLEF) | 4.50 | Better execution but less novelty; our paper is weaker |
| `/home/.../vLqkCvjHRD.md` (Coarse-Tuning) | 4.75 | Cleaner methodology and results |
| `/home/.../KTL534o7Ot.md` (ProgSyn) | 5.33 | Solid execution, less novelty |
| `/home/.../GRlKzhHl9Z.md` (Bayesian Surrogate) | 5.33 | Stronger empirical validation |

Our paper has a more novel core idea than any of these anchors, but the execution is substantially weaker. The numerical inconsistency, underspecified gradient mechanism, and misleading figure are verifiable problems that the anchors at 4+ do not share. The closest comparable papers are Pylic (3.67) and FALCON (3.00), which similarly have interesting ideas undermined by execution issues.

**Final score: 3.5** — a reject-level paper with a genuinely interesting core idea that requires major revision (correcting numerical errors, explaining the gradient mechanism, fixing Figure 2, honestly reporting comparisons and training costs) before it could be considered for publication.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>