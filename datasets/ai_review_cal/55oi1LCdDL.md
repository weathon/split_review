- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5, 5
Now I have a thorough understanding of both the paper and the reviews. Let me synthesize the final consolidated review.

---

## Summary

This paper proposes Duct (DUal ConsolidaTion) for domain-incremental learning (DIL) with pre-trained models. It identifies two sources of forgetting in DIL — feature drift and classifier mismatch — and consolidates each separately. Representation consolidation merges fine-tuned backbones (weighted by task similarity) into a unified embedding space; classifier consolidation retrains the new domain's classifier on the unified embedding then uses optimal transport, driven by class-center costs in the pre-trained space, to estimate old classifier weights. Experiments on Office-Home, DomainNet, CORe50, and CDDB show consistent gains over prior DIL methods including prompt-based and exemplar-based approaches.

## Strengths

1. **Well-motivated dual-consolidation framework validated by ablation (Table 2).** The paper explicitly breaks forgetting into feature-level and classifier-level causes and designs separate mechanisms for each. The ablation on CDDB is clean and convincing: representation merging alone (Var 1) jumps from 63.40% to 74.17%, adding task-similarity weighting (Var 2) reaches 76.82%, adding new-classifier retraining (Var 3) reaches 80.31%, and the full method with old-classifier transport reaches 82.35%. Each component contributes, which directly supports the core claim.

2. **Consistent and large-margin gains across four datasets and two backbones (Table 1, Figure 2).** Duct outperforms both exemplar-based methods (Replay, iCaRL, MEMO) and prompt-based methods (L2P, DualPrompt, CODA-Prompt, S-iPrompt) on Office-Home, DomainNet, CORe50, and CDDB with both ViT-B/16 IN1K and IN21K. For example on DomainNet with IN1K, Duct achieves 67.16% average accuracy vs. 64.78% for the best exemplar-based method (Replay) and 59.85% for the best prompt-based method (CODA-Prompt). Gains are stable across multiple task orders.

3. **Forgetting measure confirms stability (Figure 3b).** On CDDB across five task orders, Duct achieves the lowest forgetting measure (0.12) among all methods including prompt-based and exemplar-based ones, directly supporting the claim that dual consolidation resists catastrophic forgetting.

4. **Hyperparameter robustness analysis (Figure 3c).** A systematic 5×5 sweep over α_ϕ and α_W on Office-Home shows broad stability, with best performance near 0.5. This demonstrates the method is not brittle w.r.t. its merging hyperparameters.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Ambiguity in the cost matrix for classifier transport (Section 4.2, Eq. 13 / lines 205–210).** The optimal transport cost is defined as Q_{i,j} = ‖c⁰_i − c⁰_j‖², where c⁰_i are class centers extracted using the pre-trained backbone φ₀. The paper states "classes i and j are from different domains," but it only explicitly describes extracting class centers from the current domain's data (lines 205–206). Since Q has dimensions |Y| × |Y_o| and |Y_o| grows with the number of domains, it is unclear whether previous-domain class centers are retained or the same current-domain centers are reused for all columns. This is a clarity gap, not a flaw: storing previous-domain centers (|Y| d-dim vectors per domain) is trivial memory and does not violate the exemplar-free constraint. The authors should explicitly specify how centers for old-domain classes are obtained. The core contribution of the OT-based transport is still valid and well-supported by the ablation.

2. **Missing discussion of computational cost.** Duct fine-tunes the full ViT backbone for each new domain (15 epochs), whereas prompt-based competitors (L2P, DualPrompt, CODA-Prompt) freeze the backbone and train only a small prompt pool. Training time, FLOPs, and parameter counts are not reported. While the empirical comparison is valid (the "Finetune" baseline shows that straightforward fine-tuning fails, and Duct's gains arise from consolidation), readers cannot assess the compute/performance trade-off. A brief discussion of overhead relative to lighter alternatives would improve the paper.

3. **Fixed 15 training epochs across all datasets.** The paper uses 15 epochs for all four datasets without discussing whether this was tuned or if results are sensitive to epoch count. A note on early stopping or convergence behavior would improve reproducibility.

### Trivial

- The paper could clarify in Algorithm 1 that class centers from previous domains are saved along with the consolidated backbone, making the cost matrix construction fully explicit.

## Nice-to-Haves

- Report wall-clock training time or approximate FLOPs per domain to contextualize the comparison with prompt-based methods.
- Add a brief discussion of conditions under which task-vector merging might cause negative transfer (e.g., if task vectors are not linearly mode-connected), to preempt a natural concern.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"Computational cost makes comparison misleading" (as a Major issue):** The paper includes a "Finetune" baseline that also fine-tunes the backbone, showing that fine-tuning alone catastrophically forgets. The comparison is therefore informative, not misleading. The cost discussion is missing but the comparison itself is fair. Demoted to Minor.
- **"Critical issue" label for the cost matrix ambiguity:** The critic called this "critical" and "structural," but the cost matrix is well-defined under the natural reading (class centers capture semantic class-level similarities via φ₀; the "different domains" tag refers to which classifier sets the classes belong to, not to needing old-domain data). The issue is a clarity gap, not a methodological gap. Demoted to Minor.
- **"No pseudocode for cost matrix construction":** Algorithm 1 already lists the steps; the cost matrix is computed implicitly in steps 2 (extract centers), 6 (solve OT), and 7 (consolidate classifiers). The description is sufficient.
- **"Potential negative transfer through merging":** The robustness analysis (Figure 3c) already addresses this implicitly by showing stable performance across a wide range of α values. This is a nice-to-have discussion point, not a weakness.
- **Strength Finder's generic strengths**: Claims like "this paper addressed an important problem" are generic and removed. Only concrete, evidence-grounded strengths are retained.
- **Strength Finder's claim about t-SNE visualization**: Retained as a supporting strength, but noted as qualitative.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's strengths (clean ablation, strong results) and the main unresolved point (cost matrix clarity) is a presentation issue the authors can address.

## Suggestions

1. Add 2–3 sentences in Section 4.2 explicitly stating how old-domain class centers are obtained (whether stored from prior stages or computed from the current domain's data), including the negligible memory footprint.
2. Include a brief paragraph or supplementary table comparing training/inference cost (parameters, training time) with prompt-based methods.
3. Add a note on whether the 15-epoch training budget was tuned per dataset or fixed across all experiments.
