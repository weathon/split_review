Now I have all the information I need from the paper. Let me produce the consolidated review.

## Summary

The paper presents Scaff-PD, a novel algorithm for distributionally robust federated learning that combines accelerated primal-dual (APD) optimization with SCAFFOLD-style bias-corrected local steps. The algorithm solves a general min-max DRO formulation (Eq. 1) that unifies several existing fair FL objectives (AFL, q-FFL, CVaR). Theoretically, the paper proves an accelerated O(1/T²) rate in the strongly-convex-concave setting and linear convergence in the strongly-convex-strongly-concave setting—the first such rates for federated DRO. Experiments on CIFAR-100 and TinyImageNet show improvements in worst-20% accuracy compared to baselines.

## Strengths

- **First federated DRO algorithm with accelerated and linear convergence guarantees**: The paper proves that Scaff-PD achieves O(1/R²) convergence in the strongly-convex-concave setting (Theorem 1) and linear convergence exp(−O(R)) in the strongly-convex-strongly-concave setting (Theorem 2). Prior federated DRO methods such as DRFA (Deng et al., 2020) achieved only O(1/R) and AFL/q-FFL had no accelerated guarantees. This is a genuine theoretical advance.

- **Clean unifying min-max formulation (Eq. 1)**: The objective F(x, λ) = Σᵢ λᵢ fᵢ(x) − ψ(λ) recovers AFL, q-FFL, α-CVaR, and Nash bargaining solutions through different choices of Λ and ψ (Section 3). This provides a single algorithmic framework for a broad class of fair/robust FL problems.

- **Novel algorithmic integration of APD + SCAFFOLD bias correction**: The combination is technically well-motivated. Performing accelerated primal-dual updates on the server while using control variates to correct client drift in local primal updates is a clean design. The choice to do local steps only on the primal variable (not the dual) is properly justified: clients lack the global information needed to update λ locally (Section 4).

- **Empirical fairness improvements under high heterogeneity**: On CIFAR-100 with α=0.01, Scaff-PD achieves 29.30% worst-20% accuracy, outperforming the next best method DRFA (26.77%) by 2.53 pp while also achieving the best average accuracy (49.03%). The pattern holds across multiple datasets and heterogeneity levels.

## Weaknesses

### Fatal
None.

### Major

- **Experimental evaluation lacks statistical rigor**: Table 1 presents single-point accuracy numbers with no error bars, confidence intervals, or any indication of variance across runs. Given the small number of clients (20), random Dirichlet partitioning with additional 30% subsampling, and stochastic training, results could vary substantially across different random seeds. The paper does not state how many seeds were used (searching for "seed," "trial," "run," "repetition" in the paper finds no such details). For CIFAR-100 α=0.05, the average accuracy advantage over AFL is only 42.06 vs 44.73 (AFL is higher), and on TinyImageNet α=0.01, AFL achieves 45.32% average vs Scaff-PD's 41.26%. Without multiple trials, it is impossible to tell which differences are significant. The synthetic experiments also lack error bars despite the scatter-plot-style curves.

- **Deep learning claim is not validated**: The paper introduces a "two-stage Train-Convexify-Train" method for deep learning (Section 1) but the experiments use a pre-trained ResNet-18 as a fixed feature extractor, training only a linear classifier on frozen features—a convex problem. The "convexifying" step after federated pre-training is never actually carried out or evaluated. The theory only covers strongly convex objectives, so the claimed applicability to deep (non-convex) networks remains aspirational. This gap between the claimed scope and the experiments is significant.

- **No hyperparameter tuning details for baselines in real-world experiments**: The paper states that parameters for the synthetic experiment were selected via grid search (Section 6.1) but provides no description of how baselines (FedAvg, SCAFFOLD, q-FFL, AFL, DRFA) were tuned in the real-world experiments (Section 6.2). In tables where Scaff-PD outperforms baselines, it is unclear whether this reflects algorithmic superiority or simply suboptimal baseline configurations.

### Minor

- **The convergence analysis does not explicitly show how the number of local steps J affects the rate**: The theorems (Theorem 1, Theorem 2) and conditions (Condition 1, Condition 2) are expressed purely in terms of communication rounds R and the algorithmic parameters {τᵣ, σᵣ, γᵣ, θᵣ}. The local step parameters J and η_ℓ appear only in Algorithm 2 (Local-update) but not in the convergence bounds. This does not invalidate the results—the bias correction is designed precisely so that the per-round convergence is independent of J (matching centralized rates)—but the paper would be stronger if it explicitly characterized how J and η_ℓ should be set and how they affect the constants or noise accumulation. The reviewer's claim that this is "fatal" or implies "J=1" is incorrect (the SCAFFOLD-style analysis matches rates in communication rounds regardless of J by construction), but the omission is still worth addressing for completeness.

- **Per-round communication cost is not discussed**: Scaff-PD requires each client to send (1) a scalar loss Lᵢʳ, (2) a gradient cᵢʳ = gᵢ(xʳ), and (3) a local update Δuᵢʳ per round—amounting to 2 vectors + 1 scalar per client. Standard FedAvg sends 1 vector. SCAFFOLD sends roughly 1–2 vectors depending on the variant. The paper claims "communication efficiency" throughout but never quantifies the per-round overhead or compares total communication cost (rounds × per-round cost) against baselines. This is a practical consideration the paper should address, though the overhead relative to SCAFFOLD is modest (1 extra scalar per client per round).

- **Synthetic experiment compares only against DRFA**: The synthetic convergence plot (Figure 1) includes only Scaff-PD and DRFA. While DRFA is the most relevant federated DRO baseline with guarantees, including FL algorithms like SCAFFOLD or AFL on the synthetic task would provide a more complete picture of convergence behavior.

- **Missing ablation on the effect of J**: The paper uses J=100 local steps for all experiments but never varies J to show its effect on convergence speed or communication efficiency. This is the most direct way to support the communication-efficiency claim.

### Trivial
None beyond the formatting artifacts that are parser issues.

## Nice-to-Haves
- A box plot or violin plot of per-client test accuracy would visually demonstrate tail improvements over baselines.
- Convergence curves (accuracy vs. rounds) for the main real-world experiments, analogous to Figure 2 but including all baselines.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"cᵢʳ is a full gradient, not stochastic"**: The paper explicitly defines gᵢ as the stochastic gradient (Eq. on line 85: "we let g_i(u_{i,j-1}) denote the stochastic gradient of f_i at iterate u_{i,j-1}"). Therefore cᵢʳ = gᵢ(xʳ) is a stochastic gradient, not a full batch gradient. The critic's concern about contradicting the stochastic setting is based on a misreading.

- **"Communication is doubled" (vs FedAvg/SCAFFOLD)**: Compared to SCAFFOLD (which also sends model update + control variate information), the per-client overhead of Scaff-PD is just 1 additional scalar (the loss Lᵢʳ). The critic's claim of "doubling" is only true versus FedAvg, but comparing a DRO method against the simplest non-DRO baseline on communication cost is misleading.

- **"DRFA is a slow baseline"**: DRFA is the standard prior federated DRO algorithm with convergence guarantees. Comparing against it on synthetic data is appropriate and does not constitute a weakness.

- **"SCAFFOLD is not a DRO method so comparing against it in Figure 2 is odd"**: Figure 2 studies the effect of ρ in Scaff-PD; SCAFFOLD is shown as a reference point for what average-objective optimization achieves. This is a reasonable visualization choice.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the cross-review is the tension between the paper's ambitious framing ("communication efficient for deep learning") and the actual evaluation (convex objectives, no J-ablation, single-run results). The theoretical contribution—matching centralized accelerated primal-dual rates for DRO—is solid and genuinely advances the state of the art. But the empirical validation is notably thin for a paper making practical efficiency claims. The reviewers converge on the view that the algorithmic idea is strong but the experiments need a major upgrade (multiple seeds, J-ablation, communication cost analysis, end-to-end deep learning) to match the scope of the claims.

## Suggestions

1. **Add multiple trials with error bars to all real-world experiments** (at least 5 random seeds). Report mean ± std for both average and worst-20% accuracy. This is the single most impactful improvement.

2. **Ablate the number of local steps J**: Show convergence (in both rounds and wall-clock time) for J ∈ {1, 5, 20, 100} to directly support the communication-efficiency claim.

3. **Quantify total communication cost**: Provide a comparison of total bytes communicated (rounds × per-round cost) between Scaff-PD and baselines, explicitly noting the extra scalar and vector per round.

4. **Provide hyperparameter tuning details** for all baselines in real-world experiments, or adopt a standardized tuning protocol (e.g., grid search over learning rates, local steps for each method).

5. **Either remove or explicitly qualify the deep learning claim**: The current experiments validate Scaff-PD on convex problems (linear classifier on frozen features). If the "Train-Convexify-Train" approach cannot be evaluated end-to-end, the paper should clearly state that deep learning is future work.

6. **Characterize the dependence on J in the theory**: Even a discussion of how J and η_ℓ affect the constants in the convergence bounds would significantly strengthen the theoretical narrative.

## Score and Decision

**Originality**: High. The APD + SCAFFOLD combination for DRO is novel, and achieving accelerated/linear rates for federated DRO is a clear advance over prior O(1/R) rates.  
**Importance of research question**: High. Fair and robust federated learning is an important problem with practical relevance.  
**Claims well supported**: Partially. The theoretical claims are supported, but the empirical evidence is weakened by single-run results and missing ablations.  
**Soundness of experiments**: Below average for a top conference. The lack of error bars and hyperparameter tuning transparency significantly weakens the empirical findings.  
**Clarity of writing**: Adequate. The paper is generally well-structured, though the notation is dense and some algorithmic steps could be explained more intuitively.  
**Value to the research community**: Moderate. The theoretical framework and algorithm are useful, but the experiments need strengthening before the paper can serve as a reliable empirical reference.

The paper has genuine theoretical contributions (accelerated/linear convergence for federated DRO, clean unifying formulation) and a novel algorithmic design. However, the experimental evaluation has notable gaps—most critically, the absence of multiple trials and error bars, missing ablations on the number of local steps, and no communication cost analysis—that prevent the empirical claims from being fully trusted. The paper would benefit significantly from a revision addressing these issues.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>