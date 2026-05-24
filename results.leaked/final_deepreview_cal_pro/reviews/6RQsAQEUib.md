Now I have a clear calibration picture. Let me write the final review.

**Bracket from Round 1:** This paper sits above F0GNv13ojF (5.17, rejected; novelty concerns on RL reward design) but below mMPMHWOdOy (8.00, accepted; WizardMath with stronger results and more comprehensive experiments). Range: ~5.5–7.0.

**Narrowing from Round 2:** The closest anchor is IcVNBR7qZi (6.25, accepted) — identifies vanishing gradients in RL finetuning, proposes SFT warmup, has theoretical analysis but simpler solution. GHPO is roughly comparable: more novel adaptive mechanism, broader empirical evaluation, but less theoretical grounding and some presentation issues. GHPO is stronger than DzKdjWe59v (5.75, rejected; Hint Marginalization with marginal gains) and weaker than 3ogIALgghF (7.00, accepted; Auto-CEI with better ablations and novelty).

**Final score: 6.0** — a solid contribution with real empirical gains, but the core algorithm description needs clarification and missing ablations weaken confidence in the claimed mechanisms.

---

## Summary

This paper proposes Guided Hybrid Policy Optimization (GHPO), a method that augments GRPO-based RL training for LLM reasoning by dynamically detecting "difficult" problems (those where all G sampled responses from the current policy are incorrect) and providing partial ground-truth solution traces as prompt augmentation. The goal is to mitigate reward sparsity caused by capacity-difficulty mismatch, converting unsolvable problems into learnable ones without discarding training data. Experiments on mathematics benchmarks with Qwen2.5 models show consistent improvements over GRPO and a curriculum-learning baseline.

## Strengths

- **Clear problem framing and well-motivated approach.** The paper identifies a real bottleneck in GRPO-style RLVR: when none of the G sampled responses for a query are correct, all advantages become zero and no learning signal is produced. The idea of using available ground-truth traces to convert these dead queries into useful training signals is intuitive and well-justified (Section 2.3, Section 3.1).

- **Consistent empirical improvements across diverse benchmarks and model families.** GHPO improves average accuracy over GRPO on both the Math3to5 dataset (Table 1: 39.8% → 44.2%) and the more challenging NuminaMath-S dataset (Table 2: 40.9% → 44.2%), with gains observed across all six evaluated benchmarks. The method also improves the stronger Qwen2.5-Math-7B base model (47.3% → 50.8%), demonstrating generalization across model families.

- **Training dynamics analysis provides meaningful insight.** Figure 4 shows that GHPO maintains lower, more stable gradient norms than GRPO while achieving higher accuracy rewards and generating longer reasoning traces. Figure 3 confirms that ~60% of mini-batch problems persistently require guidance throughout training, validating the premise that reward sparsity is a pervasive issue.

- **Simple difficulty detection with no auxiliary models.** The difficulty detector uses only the group-level reward sparsity already computed during GRPO rollouts (Section 3.3, Equation 2), avoiding the cost of external LLM-based filters used in prior work.

## Weaknesses

### Major

- **The core algorithm is imprecisely specified regarding re-sampling, creating ambiguity about its theoretical soundness.** Equation 1 draws responses from π_{θ,old}(·|q) — the old policy conditioned on the *original* query q. But for "difficult" queries, the probability ratio in Equation 2 uses q* = q + ω·h_{f,q} (the augmented query) in both numerator and denominator. Since the responses were not actually sampled from π_{θ,old}(·|q*), the denominator does not represent the distribution under which the tokens were generated. This means the ratio is not a proper importance weight, and it is unclear whether the gradient estimates correspond to a well-defined optimization objective. The text (Section 3.2) and Figure 2 do not clarify whether responses are re-sampled after prompt refinement. While the method may work in practice (the gradient still pushes up log-probability of favorable tokens under q*), the paper should explicitly address this discrepancy and justify why the approach remains valid despite the mismatch.

### Minor

- **No ablation of individual GHPO components.** The method combines difficulty detection, multi-stage hint ratio scheduling (ω), and a cold-start strategy. No experiment isolates their individual contributions. The comparison to GRPO-CL-H(0.5) (Table 2) partially tests fixed vs. adaptive hints, but it bundles curriculum learning with the fixed hint, so the effect of adaptivity alone is not cleanly measured. An ablation table would substantially strengthen the claim that each component matters.

- **Sample efficiency claims are stated but not directly measured.** The paper repeatedly frames reward sparsity as a sample efficiency problem (Sections 2.3, 3.1), yet the evaluation reports only final accuracy and training dynamics vs. global steps — not accuracy vs. number of samples seen or wall-clock time. Standard sample-efficiency curves are absent.

- **No variance estimates across training runs.** All results in Tables 1–2 are point estimates. Given the well-known instability of GRPO-style training (which the paper itself discusses), reporting results from multiple random seeds — or at minimum acknowledging this limitation — would strengthen confidence in the reported gains.

- **Assumption 1's framing as "OOD generalization" is stronger than what the experiments test.** The assumption posits that using ground-truth traces on failing in-domain problems improves out-of-distribution generalization. The experiments evaluate on held-out math benchmarks which, while not in the training set, are drawn from similar distributions (same domain, similar format). The connection between the formal assumption and the actual evaluation is loose, and the assumption serves more as verbal motivation than a testable claim.

### Trivial

- The abstract's "approximately 5%" average gain rounds up the actual improvements: 4.4 percentage points absolute in Table 1 and 3.3 in Table 2. These are in the right ballpark but the 5% figure is generous.

## Nice-to-Haves

- A comparison to a simpler baseline that uses the same privileged information (ground-truth traces) in a non-adaptive way — e.g., SFT on all traces followed by GRPO, or always augmenting the bottom K% of problems with a fixed hint ratio — would more directly isolate the value of adaptive difficulty detection.
- Reporting computational overhead of the hint mechanism (e.g., token overhead from augmented prompts, any additional forward passes) would help practitioners assess the cost-benefit tradeoff.
- The multi-stage guidance strategy (Appendix B.3) is central to the method but not summarized in the main text; a brief description of how ω changes over training stages would improve readability.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The core algorithm is underspecified; its soundness is therefore unverifiable" at the Fatal level.** The harsh critic framed this as fatal. I have downgraded it to Major because: (a) the gradient ∇_θ log π_θ(o|q*) still provides a meaningful learning signal even if the importance weight is technically mis-specified, (b) the empirical results demonstrate the method works, and (c) this is a clarity issue that can be resolved with revision, not a proof that the approach is fundamentally broken.

- **"Missing simple baselines that also exploit the ground-truth traces."** The paper does include GRPO-CL-H(0.5) as a fixed-hint baseline; additional baselines would be nice but their absence is not a fatal or major flaw. Moved to Nice-to-Haves.

- **"The diagram in Figure 2 does not loop back to the policy model for re-sampling."** This is subsumed under the Major weakness about algorithmic specification above — the figure alone is not the issue; the issue is whether the text and equations describe re-sampling or not.

- **"Missing related works like LUFFY comparison."** The harsh critic noted LUFFY is mentioned but not compared. I cannot verify whether LUFFY is a fair comparison point, and the paper does cite it. Removed.

- **Various formatting/style nitpicks** (typos, grammar, presentation details) — removed per instructions.

- **"The paper would benefit from situating itself relative to other works that combine demonstrations or SFT with RL."** This is vague and speculative — removed.

## Novel Insights

The paper's observation that ~60% of problems persistently require guidance throughout training (Figure 3) provides concrete evidence that reward sparsity is not merely an initial training problem but a sustained challenge in GRPO-based RLVR, even as the policy improves. The gradient norm comparison (Figure 4) offers practical evidence that prompt-level guidance yields smoother optimization trajectories, which could inform future work on stabilizing RL for LLMs.

## Suggestions

- Clarify in Section 3.2 whether responses are re-sampled after prompt refinement. If they are not, explicitly state this and justify why the probability ratio computed under q* is a valid training objective despite the distribution mismatch. If they are, describe the re-sampling step and quantify its computational cost.
- Add a minimal ablation table isolating difficulty detection, multi-stage ω scheduling, and cold-start. Even a 2×2 ablation (e.g., with/without adaptive detection × with/without multi-stage ω) on one dataset would substantially strengthen the paper.
- Replace or qualify the "sample efficiency" language with evidence (sample-efficiency curves) or reframe those claims around training stability and final accuracy, which are better supported.

### Score and Decision

**Anchor comparison summary:**
| Anchor | Avg Score | Round | Comparison to GHPO |
|--------|-----------|-------|---------------------|
| F0GNv13ojF (RL reward design) | 5.17 | R1 | GHPO stronger: more novel method, more consistent gains |
| DzKdjWe59v (Hint Marginalization) | 5.75 | R2 | GHPO clearly stronger: larger gains, more principled |
| IcVNBR7qZi (Vanishing Gradients) | 6.25 | R2 | Comparable: similar problem-solution structure; GHPO more empirical breadth but less theory |
| 3ogIALgghF (Auto-CEI) | 7.00 | R2 | GHPO somewhat weaker: fewer ablations, less novelty in framing |
| mMPMHWOdOy (WizardMath) | 8.00 | R1 | GHPO clearly weaker: smaller gains, narrower scope |

**Round 1 bracket:** 5.5–7.0. **Round 2 narrowed:** GHPO is closest to IcVNBR7qZi (6.25) in contribution quality but with somewhat weaker presentation rigor (no ablations, algorithmic imprecision) → final score 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>