Here is my consolidated final review:

---

## Summary

This paper addresses the disparate impact of pruning—where sparse models exhibit unequal accuracy drops across sub-groups—by formulating a constrained optimization problem (CEAG) that directly bounds per-group excess accuracy gaps (EAGs) between dense and sparse models. The authors propose an algorithm using proxy constraints (negative loss gaps as surrogates for the non-differentiable accuracy gaps) and replay buffers to stabilize stochastic constraint estimates. Experiments on FairFace, UTKFace, and CIFAR-100 show that CEAG reliably satisfies disparity constraints on the training set across architectures and sparsity levels, and the paper honestly documents that all surveyed mitigation methods (including CEAG) fail to generalize to test data.

## Strengths

- **Direct, interpretable constraints on accuracy gaps.** The formulation (Equation 2) bounds per-group EAGs between dense and sparse models with a tolerance parameter ε, providing clear semantics: a feasible model guarantees that no group's accuracy degrades more than ε beyond the average degradation. This is a cleaner, more directly interpretable target than loss-based surrogates (Section 3.3).

- **Novel algorithm for constrained optimization with stochastic, non-differentiable constraints.** The paper contributes a practical method combining proxy constraints (Cotter et al., 2019) with replay buffers to handle the non-differentiability and high variance of accuracy-gap estimates from mini-batches. The alternating GDA scheme (Algorithm 1) requires only one forward/backward pass per iteration, matching the cost of ERM—a non-trivial engineering contribution.

- **Replay buffers improve training dynamics.** The introduction of replay buffers demonstrably reduces variance in constraint estimates, improving disparity metrics for both CEAG and the equalized-loss baseline (EL). The CIFAR-100 experiment (Section 5.3) shows that replay buffers improve max ψ_g on both train and test sets, confirming this is a broadly useful technique.

- **Honest documentation of the generalization barrier.** The paper is the first to systematically document that all current mitigation approaches (CEAG included) fail to guarantee low disparity on unseen data (line 56, Section 6, Ethics Statement). This is a genuine empirical finding that clarifies the current frontier for the field.

- **Empirical consistency across tasks and sparsity levels.** CEAG consistently achieves the lowest training-set max ψ_g and Ψ_pairwise across FairFace (99% sparsity), UTKFace (85–95%), and CIFAR-100 (92.5%), with lower variance across seeds than baselines.

## Weaknesses

### Fatal

None.

### Major

- **The paper's framing overstates what has been demonstrated, creating a tension with its own central finding.** The paper repeatedly claims CEAG can "reliably mitigate the disparate impact of pruning" (introduction bullet list, line 28 caption, line 337, conclusion line 396) without consistently qualifying that this holds *on the training set*. Yet the paper's most striking empirical result is that *all methods, including CEAG, fail to mitigate on unseen data* (line 56). A method whose constraints are violated on test data at comparable levels to baselines is not yet a practical mitigation tool. The paper acknowledges this gap honestly in multiple places, but the framing foregrounds the method as a solution. The actual contribution is a clean formulation + algorithm for constrained optimization on the training distribution, plus the documentation that this does not transfer. These are valuable, but the paper would be stronger if this were the headline, with CEAG presented as a tool for *studying* the gap rather than as a deployed solution. The gulf between "reliably mitigates" (unqualified) and "fails on unseen data" is too wide.

- **The generalization gap is documented but not analyzed.** The paper identifies an important finding that no method generalizes, but does not investigate *why*. Is it because training-set constraints force the model to memorize group-specific patterns? Does the surrogate (negative loss gap) misalign with the true constraint on test data? Does the replay buffer variance reduction bias estimates toward old measurements that don't reflect distribution shift? Without even a preliminary analysis (e.g., tracking per-group accuracy on a validation split and early-stopping on test disparity), the paper stops at documenting the problem rather than advancing understanding of it. This limits the paper's impact from a "finding that shapes future work" to an "observation that needs follow-up."

### Minor

- **The one-sided constraint (only bounding positive ψ_g) is handled too briefly in the main text.** The paper imposes only upper bounds on ψ_g (Equation 5), while the disparity metric used (Ψ_pairwise = max ψ_g − min ψ_g) depends on both tails. A group that improves far more than average (negative ψ_g) can inflate Ψ_pairwise even if all positive ψ_g are ≤ ε. The paper acknowledges this (Section 3.2) and cites the appendix for justification, but the main-text explanation ("challenging due to the small feasible region relative to estimation noise") is asserted without evidence. An analysis of whether min ψ_g is typically large in practice (e.g., a correlation plot of min vs. max ψ_g during CEAG training) would substantially increase confidence that the practical impact is small.

- **The surrogate–true constraint alignment is not analyzed.** The primal objective uses ∇ψ̃_g (negative loss gaps) while the dual update uses the true ψ_g (accuracy gaps). The paper asserts this is "a reasonable choice because drops in accuracy correspond to increases in loss" (line 208), but the correspondence is neither linear nor monotonic in general: a small loss increase can correspond to a large accuracy drop near a decision boundary, and vice versa. No empirical correlation analysis between ψ̃_g and ψ_g during training is provided. If the surrogate gradient points in a direction that does not reduce (or even increases) the true accuracy gap, the primal and dual signals could conflict. A simple figure tracking both quantities over training would address this.

- **Scalability claim of "hundreds of sub-groups" is supported by only one experiment with 100 groups (CIFAR-100) and a moderate-sized model (CIFAR-ResNet-56).** The UTKFace intersectional experiment has ~10 groups. While the computational overhead argument (Section 4.3) is plausible, it is not backed by wall-clock or memory measurements. The claim should be tempered or better evidenced.

- **The specific ε values used in experiments are not stated in the main text.** The paper describes ε conceptually and uses "feasible" to indicate max ψ_g ≤ ε, but the actual ε values per experiment are not reported in the running text (they may appear in the table files, which are included via \input commands). Adding them to the main text would aid reproducibility.

- **Computational overhead is claimed but not measured.** Section 4.3 argues the overhead is negligible, but no wall-clock time per epoch or total training time is reported for any task.

### Trivial

- "Hundreds" (abstract, line 4, line 54) is an overstatement for 100 groups. The number of groups in the scalability experiment is exactly 100, which is closer to "one hundred" than "hundreds."
- The asymmetry of the normative choice (treating over-improvement as equally problematic as degradation via Ψ_pairwise, without constraining negative ψ_g) is not discussed in the ethics statement.

## Nice-to-Haves

- The paper could compare against EL without replay buffers on all tasks (currently only done on CIFAR-100), to strengthen the claim that replay buffers are a broadly useful contribution.
- An ablation study on the replay buffer size k (bias–variance trade-off) would strengthen the engineering contribution.
- Reporting the dense model's per-group accuracy would help readers assess whether the dense model itself introduces bias that propagates through the EAG definition.

## Removed Points

The following points were raised by reviewers but are removed or downgraded based on verification against the paper:

- *"The equalized loss baseline (EL) is re‑implemented and enhanced with replay buffers, but the original paper's version is not run on the same tasks."* — The paper explicitly states this is a "re-implementation... enhanced with replay buffers" (line 302) and compares against EL without buffers on CIFAR-100 (line 358). The comparison is transparent. Removed because the paper acknowledges this design choice.
- *Criticisms based on missing appendix content* — Removed per instructions: the parser strips appendices, which exist in the original submission.
- *Formatting nitpicks and hypothetical missing references* — Removed per instructions.
- *"The paper criticizes loss-based methods as surrogate/indirect, but the accuracy-gap definition also makes a specific normative choice."* — This is a valid observation but not a weakness; the paper's ethics section (line 406–422) covers limitations. Including normative implications of the one-sided constraint would be nice, but its absence is not a flaw in the technical contribution.

## Novel Insights

The most striking finding to emerge from the review process is that the paper's empirical honesty about the generalization gap (all methods fail on test data) is simultaneously its strongest and weakest point: it is a genuine contribution to document this barrier, but the paper does not leverage this finding to advance understanding of *why* the gap occurs. The reviews converge on the same structural observation: the paper sits at the boundary between "here is a new method that works on the training distribution" and "here is a surprising failure mode affecting all methods in this area." Pushing further into the latter direction—characterizing the causes of the gap—would transform the paper from a solid-but-limited engineering contribution into a genuinely insightful piece of research.

## Suggestions

1. **Reframe the central narrative.** Make the generalization gap a primary contribution rather than an afterthought. Present CEAG as a tool for *studying* why training-set disparity guarantees do not transfer, and add even a preliminary analysis (e.g., does the gap correlate with per-group sample size? Does early-stopping on test disparity help? Does the surrogate misalign on test data?).
2. **Add a correlation analysis** between ψ̃_g (loss-based surrogate) and ψ_g (accuracy gap) over training for at least one task (e.g., CIFAR-100 or FairFace). A scatter plot showing alignment (or misalignment) would substantially strengthen confidence in the optimization.
3. **Report ε values per experiment in the main text** and add a brief analysis of whether min ψ_g ever becomes large enough to inflate Ψ_pairwise despite bounded max ψ_g.
4. **Include wall-clock training time** for at least one task to substantiate the "negligible overhead" claim.
5. **Tone down unqualified claims** of "reliably mitigates disparate impact" and consistently specify "on the training set" where appropriate, to avoid the tension with the generalization finding.

## Score and Decision

The paper has genuine methodological contributions: a clean, interpretable formulation for the accuracy-based disparate impact of pruning, a practical algorithm with proxy constraints and replay buffers, and the honest documentation that all current methods fail on test data. These are real contributions that advance the field's understanding.

However, the framing systematically overstates what the evidence supports. The paper presents CEAG as a mitigation method, but the evidence only shows it works reliably on the training set. The generalization gap is documented but not analyzed—stopping at observation rather than advancing understanding. The optimization has plausible gaps (one-sided constraints, surrogate alignment) that are not empirically evaluated. These issues do not invalidate the methodological contributions, but they prevent the paper from delivering on the promise of its headline claims.

The core ideas are worth pursuing, and with a major revision that reframes the contribution and adds even preliminary analysis of the generalization gap, the paper could become a strong candidate. In its current form, the distance between what is claimed and what is demonstrated is too large.

**Score and Decision**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>