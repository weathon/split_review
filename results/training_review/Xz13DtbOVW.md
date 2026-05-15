Now I have a complete picture. Let me compose the final consolidated review.

## Summary

This paper tackles the disparate impact of model pruning — the phenomenon where sparse models disproportionately harm accuracy on certain sub-groups. The authors formulate a constrained optimization problem (CEAG) that directly bounds per-group excess accuracy gaps (EAGs) between the dense and sparse models, providing interpretable semantics (e.g., ε = 1% means no group degrades more than 1% beyond the average). They propose an algorithm using proxy constraints (for non-differentiable accuracy-based constraints) and replay buffers (for variance reduction in stochastic constraint estimation), and evaluate on FairFace, UTKFace, and CIFAR-100 across multiple architectures and sparsity levels.

## Strengths

- **Interpretable, directly-targeted formulation**: The EAG-based constraints directly control what matters for pruning-induced disparity — the group-level accuracy change relative to the global change — rather than relying on loss-based surrogates. The tolerance ε has a clear practical meaning. This is a genuine conceptual improvement over prior work (e.g., Tran et al. 2022) that used loss equalization agnostic to the dense model's per-group performance. Evidence: Section 3.1-3.2, lines 106-178.

- **Practical algorithm with minimal overhead**: The Alt-GDA algorithm with proxy constraints requires only one forward and one backward pass per iteration, matching the cost of ERM. The replay buffer mechanism for variance reduction is simple and demonstrably effective. Evidence: Section 4.3, lines 278-284; Table 3 (CIFAR-100) shows replay buffers cut CEAG's train max_ψ_g from 1.56% to 0.91%.

- **Transparent documentation of generalization limitations**: Unlike many papers that bury negative results, this paper explicitly states upfront (line 56-59) that all methods including CEAG fail to mitigate disparities on unseen data, and reiterates this in the Discussion, Conclusion, and Ethics Statement. This openness is valuable for the community.

- **Consistent training-set feasibility**: CEAG is the only method that reliably satisfies the disparity constraints on the training set across all tasks and sparsity levels, while maintaining comparable aggregate accuracy to naive fine-tuning. On FairFace (99% sparsity), CEAG achieves train max_ψ_g = 0.71% (within ε = 1%) versus 7.52% for NFT and 5.47% for EL.

## Weaknesses

### Fatal

None.

### Major

- **The core claim outruns the evidence on test data**: The abstract states the technique "directly addresses the disparate impact of pruning" and the introduction claims to "reliably mitigate the disparate impact of pruning across multiple architectures, datasets, and sparsity levels" — without the qualifier "on the training set." Since the paper itself documents that all methods (including CEAG) fail to mitigate on unseen data, and that on CIFAR-100 ELGRB actually achieves better test disparity than CEAG (line 363), the framing is over-optimistic. The paper honestly documents the limitation everywhere else, but the abstract and bullet points in the introduction do not carry the caveat, creating a mismatch between the headline claims and the actual findings. This is a presentation issue that inflates the perceived contribution.

- **CEAG does not consistently achieve best *test* disparity across all tasks**: On CIFAR-100, ELGRB achieves the smallest max_ψ_g on the test set (line 363), while CEAG only wins on the training set. On FairFace and UTKFace, CEAG does achieve the best test max_ψ_g. This mixed result weakens the claim of "reliability" in deployment settings — the method works best on training data, but on test data its advantage over ELGRB is task-dependent.

### Minor

- **Proxy constraint surrogate is unvalidated**: The paper replaces the non-differentiable accuracy-gap constraints with surrogates based on negative loss gaps (Section 4.1, lines 206-208). This is a reasonable choice (drops in accuracy correspond to increases in loss), but the paper provides no empirical correlation analysis between the true accuracy-gap constraints and the loss-gap surrogates, nor an ablation comparing this surrogate to alternatives. Given that the primal gradients depend on this surrogate, a reader cannot assess whether gradient signal quality is adequate. The authors should at minimum include a small-scale experiment showing that the surrogate tracks the true constraint direction.

- **No ablation on replay buffer size k**: The paper acknowledges that "the choice of buffer size k introduces a trade-off between reducing the variance of the constraints, and biasing estimates towards old measurements" (line 268), but provides no sensitivity analysis. The main results use a single value of k. Understanding how sensitive CEAG is to this hyperparameter, especially for rare groups with few samples, would substantially strengthen the paper.

- **FairGRAPE comparison is not directly controlled**: The paper quotes FairGRAPE numbers from the original paper (with the caveat that they did not re-run it), but FairGRAPE uses a fundamentally different pruning procedure (importance-based pruning) rather than the GMP + fine-tuning protocol used by all baselines in this paper. A direct comparison under a unified protocol would be needed to make a clean empirical claim. This does not invalidate the paper's main results (which compare against NFT, NFTES, and ELGRB under the same protocol), but the inclusion of FairGRAPE in Table 1 is potentially misleading without a controlled comparison.

- **CIFAR-100 test results temper the "reliability" claim**: The paper honestly reports that CEAG "obtains the best disparity on the train set" while ELGRB achieves the best test disparity (line 363). However, the paper's emphasis on "reliably mitigating" could give readers the impression that CEAG uniformly dominates, which is not the case on this task.

### Trivial

- Line 374 contains a typo: "unsucessful" should be "unsuccessful."

## Nice-to-Haves

- A correlation scatter-plot (accuracy gap vs. loss gap per group per epoch) to validate the proxy constraint assumption empirically.
- An ablation on buffer size k to understand sensitivity, especially for groups with few samples.
- A per-group breakdown of train vs. test accuracy gaps (Δ_g for dense, sparse-NFT, and CEAG) to help diagnose why the generalization gap exists — is it uniform across groups or concentrated in certain groups?
- Reporting feasibility rates across seeds (e.g., "CEAG satisfied all constraints in 5/5 seeds") rather than just mean ± std.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic's point 1 labeled as "Fatal — structural generalization failure"**: The paper openly acknowledges this limitation (lines 56-59, 376, 388-390, 399, 419-420) and does not claim the method solves deployment generalization. The critic overstates this as invalidating the core contribution, but the paper's formulation-level contribution (direct EAG constraints) and algorithm remain valid. The abstract's omission of the qualifier is a genuine but minor presentation issue, not a fatal flaw. Moved from Fatal → a Major weakness re: framing.

- **Criticism that "only bounding positive EAGs cannot guarantee low overall disparity" (Section 3.2)**: The paper explicitly discusses this trade-off (lines 144-148) and refers to the appendix for justification. The critic's claim that this is "not empirically or theoretically justified" ignores the paper's acknowledgment of the limitation. The paper's formulation is a design choice with honest documentation of its scope.

- **Criticism that the paper doesn't analyze why other methods fail on FairFace training feasibility**: The paper does discuss this throughout Section 5 — other methods don't directly constrain accuracy gaps, so it's natural they fail to meet the EAG constraints. This is implicit in the problem setup.

- **Strength Finder's generic strengths about "addressing an important problem"**: Removed as too generic. The remaining strengths are concrete and evidence-backed.

## Novel Insights

The most striking finding from this review process is the tension between the paper's transparent reporting of its generalization failure and the critic's claim that this failure invalidates the contribution. The paper is actually quite unusual in its honesty: it clearly states in the introduction, discussion, conclusion, and ethics statement that all mitigation methods fail on unseen data. Rather than hiding this, the paper frames it as an open problem and documents it systematically. The real weakness is not the generalization gap itself (which is an honest finding) but the mismatch between the abstract's unqualified language and the caveats everywhere else in the paper. Another insight is that CEAG's advantage over ELGRB diminishes on test data — on CIFAR-100, ELGRB actually wins — suggesting that the direct accuracy-gap constraint may be inducing some overfitting to the training set's group structure that the indirect loss-based approach of ELGRB avoids.

## Suggestions

1. **Revise the abstract and introduction bullet points** to include the qualifier "on the training set" when claiming the method "reliably mitigates the disparate impact of pruning." This would align the headline claims with the paper's own honest documentation.

2. **Add a small-scale correlation study** between accuracy gaps and loss-gap surrogates (e.g., on one task for one seed) to empirically validate the proxy constraint choice. This would take minimal space (a single figure) and significantly strengthen the methodological contribution.

3. **Include a buffer-size ablation** (e.g., k ∈ {100, 500, 1000, full dataset}) on at least one dataset to characterize the variance-bias trade-off the paper acknowledges.

4. **Either remove the FairGRAPE comparison** from the main table or add a clear note explaining that the protocols are fundamentally different (importance-based pruning vs. GMP + fine-tuning) and the numbers are quoted from separate papers for reference only.

5. **Add per-group train/test accuracy gap plots** for at least one representative run to help the community understand where the generalization gap originates.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>