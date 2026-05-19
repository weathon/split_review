- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 8, 6
Now I have thoroughly reviewed the paper and all review claims. Let me compose the final consolidated review.

## Summary

This paper addresses the disparate impact of model pruning by proposing a constrained optimization formulation (CEAG) that directly bounds per-group excess accuracy gaps between a dense model and its pruned version. The constraints are interpretable (a tolerance ε directly translates to allowable accuracy degradation), and the optimization is made tractable through proxy constraints (using negative loss gaps as differentiable surrogates) and replay buffers for variance reduction. Experiments on FairFace, UTKFace, and CIFAR-100 (with up to 100 groups) show that CEAG reliably satisfies constraints on the training set across architectures and sparsity levels, while the paper honestly documents that all methods—including CEAG—fail to generalize disparity mitigation to unseen data.

## Strengths

- **Direct, interpretable constraints on accuracy gaps (not loss surrogates).** The CEAG formulation (§3.2, Eq. 5) bounds per-group excess accuracy gaps ψ_g = Δ_g − Δ, giving practitioners an interpretable success criterion: ε = 1% means the worst-affected group's accuracy degradation is at most 1% above the global average. This is a concrete advantage over the equalized-loss approach (Tran et al., 2022), which controls loss—a surrogate that does not directly correspond to the accuracy-based notion of disparate impact.

- **Scalable to hundreds of groups with negligible computational overhead.** Section 5.3 demonstrates feasibility with 100 constraints on CIFAR-100, and §4.3 shows each iteration costs one forward and one backward pass—matching standard ERM fine-tuning. This addresses a key limitation of prior work (e.g., FairGRAPE) whose per-weight-per-group importance scores become prohibitively expensive for large numbers of groups.

- **Replay buffers improve training dynamics.** Section 4.2 introduces replay buffers for variance-reduced constraint estimation, and Table 3 provides empirical evidence that both CEAG and the equalized-loss baseline perform strictly better with replay buffers than without (e.g., on CIFAR-100, CEAG with buffers achieves train max ψ ≤ ε, while CEAG without buffers has a gap ≈ 1 dt).

- **Consistently achieves feasible solutions on the training set across diverse settings.** Tables 1–3 and Figure 2 show CEAG attains max_g ψ_g ≤ ε on training data for three datasets (FairFace, UTKFace, CIFAR-100), two architectures (ResNet-34, MobileNet-V2), and sparsity levels 85–99%, while naive fine-tuning and equalized-loss often violate the constraint.

- **First documentation of the generalization challenge for pruning-disparity methods.** The paper transparently states (lines 56–59, 376, 388–390) that all methods fail to mitigate disparity on unseen data. This honest finding is a novel empirical contribution that sets a clear direction for future work.

## Weaknesses

### Fatal
None.

### Major

- **The method only reliably controls disparity on the training set; all methods (including CEAG) fail to generalize to unseen data.** This is the most significant limitation. As shown in every table, disparity metrics max ψ and Ψ_PairW on the test set are substantially larger than on the training set, and constraints satisfied during training are routinely violated at test time. The paper is transparent about this (lines 56–59, 376, 388–390, 418–420), but the abstract and introduction frame the contribution as "directly address[ing] the disparate impact of pruning" without qualifying that this holds primarily for the training distribution. For any deployable system, the gap between train and test behavior is large and uncontrolled. The paper's contribution is real but bounded: CEAG is a better *training-time* approach to an unsolved problem, and its practical significance depends on future progress on generalization.

### Minor

- **FairGRAPE comparison is not fully apples-to-apples.** CEAG uses GMP pruning; FairGRAPE uses its own saliency-based pruning. The comparison (Table 1) therefore conflates the pruning strategy with the mitigation technique. FairGRAPE results are also quoted from the original paper at 3 seeds, versus 5 seeds for CEAG. This does not undermine the paper's core claims (the main comparison is with NFT and EL), but the FairGRAPE row should be interpreted with this caveat rather than as a direct mitigation-method comparison.

- **Surrogate choice is not empirically validated.** The paper replaces non-differentiable ψ_g with a loss-based surrogate ψ̃_g (Eq. 4, line 206). While this is a reasonable choice (accuracy drops correspond to loss increases), there is no analysis of how well the surrogate tracks the true constraint over training, no convergence guarantees for the proxy-Lagrangian with this specific substitution, and no ablation comparing alternative surrogates. The dual update does use the true ψ_g (mitigating concern somewhat), but an empirical correlation plot would increase confidence.

- **No ablation for buffer size k.** The paper acknowledges (line 268) that buffer size introduces a trade-off between variance reduction and staleness, but provides no sensitivity analysis or recommended range. This is a critical hyperparameter for practitioners.

- **EL without replay buffers not shown on FairFace/UTKFace.** The isolated benefit of replay buffers is only demonstrated for CIFAR-100 (Table 3). On the face datasets, only EL_GRB is reported, so the effect of replay buffers themselves cannot be separated from the effect of the equalized-loss formulation for those settings.

### Trivial

- **The abstract could more precisely scope claims.** The abstract states the method "scales reliably" and "directly addresses the disparate impact of pruning" without noting the train/test discrepancy that is revealed in the body. Adding a brief qualifier (e.g., "on the training set") would avoid misleading readers who skim the abstract.

## Nice-to-Haves

- A systematic diagnostic of the generalization gap (e.g., per-group train vs. test accuracy correlation, analysis of distribution shift in group proportions) would strengthen the paper's own narrative and provide concrete guidance for future work.
- A sensitivity analysis for ε (tolerance) showing how max ψ and accuracy trade off as ε varies would help practitioners calibrate the method.
- A correlation analysis between ψ̃_g (surrogate) and ψ_g (true constraint) over the course of training.
- An ablation study or recommendation for buffer size k.

## Removed Points

- **Criticism about the "Failure modes" paragraph lacking quantification:** Removed because the tables *do* quantify test-set disparity for all methods. The critic's claim that the paragraph does not quantify the failure is inaccurate (see Tables 1–3 which report both train and test metrics).
- **Criticism that claims are overstated because the method fails on unseen data, treated as a "fatal" flaw:** Demoted to Major. The paper is transparent about the generalization challenge and does not claim to have solved it. The contribution is clearly scoped as a training-time mitigation method and the first documentation of the generalization challenge. The critic's framing as a fatal flaw ignores the paper's own extensive qualification of this limitation.
- **Strengths that were too generic removed:** None from the Strength Finder were generic; all were concrete and evidence-backed.

## Novel Insights

The most notable insight emerging from the cross-review is that the paper's transparency about the generalization gap is simultaneously its greatest weakness and an important contribution. The harsh critic correctly identifies that the method's practical value is limited without a generalization bridge, but this criticism lands on a limitation the paper already flags prominently. What makes the paper interesting is precisely this tension: it demonstrates that straightforward constrained optimization *can* control pruning disparity on training data at scale, but also provides clean empirical evidence that this control systematically collapses at test time across every method tested. This "negative result" framing—showing that the problem is harder than prior work assumed—is arguably as valuable as the positive algorithmic contribution.

## Suggestions

1. **Add a brief qualification to the abstract** clarifying that disparity mitigation is demonstrated on training data, with generalization flagged as an open challenge. This would better align the abstract with the paper's own honest discussion.
2. **Include a surrogate correlation plot** (ψ̃_g vs. ψ_g over training for 1–2 representative groups) in the main paper or appendix. This would address a natural concern about the optimization's validity.
3. **Add buffer-size sensitivity** as a small ablation study, even if only for one setting.
4. **Show EL without replay buffers** on FairFace or UTKFace in the main paper (or move the CIFAR-100 buffer comparison to a more prominent position).
