- Decision: Accept
- Scores: 5, 6, 6, 8, 8

## Merged Review

### Summary
The paper proposes FRLoRA (Federated Residual Low-Rank Adaptation) to improve fine-tuning of LLMs in federated learning under data heterogeneity. It addresses intrinsic constrained parameter space and extrinsic client drift by performing global updates in a higher-rank parameter space via accumulating residual low-rank matrix products, and reinitializing local low-rank matrices each round using principal singular values and vectors of pre-trained weights. Extensive experiments on nine NLU and NLG benchmarks show performance gains over various FL baselines.

### Strengths
- The idea of enlarging the parameter space for LoRA in FL is promising (Reviewers 2, 5).
- FRLoRA effectively addresses non-IID challenges by addressing both client drift and constrained parameter space through aggregated ΔW updates via SVD (Reviewers 2, 4, 5).
- Reinitializing local low-rank matrices each round alleviates client drift, enhancing convergence and performance (Reviewer 2).
- Theoretical justification via rank analysis of the parameter space is provided (Reviewer 4).
- Extensive experiments on nine benchmarks (NLU and NLG) validate consistent improvements over existing FL methods, including FedAvg+LoRA, FedYogi, FedAdam, FedProx, and FFA-LoRA (Reviewers 1, 2, 3, 4, 5).
- The paper is clearly presented and related works are thoroughly summarized (Reviewers 1, 5).
- The method incorporates a unique adaptation of LoRA with residual low-rank updates and reinitialization in the principal singular space (Reviewer 3).

### Weaknesses
- **Practical value and communication cost**: One reviewer finds the paper lacks a compelling real-world application scenario and that FRLoRA introduces significant communication overhead, limiting practicality for LoRA customers. [Reviewer 1, score 5]
- **Discrepancy in averaging**: The updates derived from averaging uploaded matrices A and B at the server differ from the averaged updates across clients; this discrepancy is likely to amplify under data heterogeneity. [Reviewer 2]
- **Rank increase not guaranteed**: The claim that residual updates expand parameter space is not fully supported: Eq. (14) only gives an upper bound on the rank, not a guarantee of increased rank. The paper does not clearly specify whether model rank strictly improves after each residual update. Additionally, standard LoRA in FL can also be formulated as Eq. (13), so the real difference between FRLoRA and the standard method (beyond initialization) is unclear. [Reviewers 2, 5]
- **Computational overhead of SVD**: Reinitializing local low-rank matrices via SVD introduces significant computational overhead for large-scale models. The paper lacks an in-depth analysis of time and memory requirements or potential optimizations. [Reviewers 3, 4] Reviewer 3 also asks about SVD stability and alternative initialization strategies; reviewer 4 calls for a computational complexity comparison against other methods. [Reviewers 3, 4]
- **Insufficient evidence on problem formulation**: The characterization of client drift via Figure 1 (c-d) is not convincing. The norm and standard deviation of ΔW could be affected by learning rate or other factors. A more rigorous analysis should focus on a single round, observe cosine similarity distributions, analyze other FL methods, and control for confounding factors (e.g., learning rates, batch sizes). [Reviewer 4]
- **Limited non-IID testing scenarios**: Experiments use a mild Dirichlet (0.5) non-IID setting with only five clients for binary classification; NLG tests are performed on IID data. Broader and more extreme non-IID experiments (e.g., varying the Dirichlet parameter, few overlapping classes) are needed to demonstrate robustness. [Reviewer 4] Reviewer 4 also asks about NLG with severe heterogeneity. [Reviewer 4]
- **Limited comparison to existing LoRA-based FL methods**: Baselines FedYogi, FedAdam, FedProx do not integrate LoRA, making comparisons less relevant. Only FFA-LoRA is directly comparable. The paper should compare with FlexLoRA (arxiv:2402.11505, Feb 2024), which also uses per-round SVD, and discuss Chain of LoRA (arxiv:2401.04151, Jan 2024) which uses a residual structure. [Reviewer 4]
- **Not consistently outperforming baselines in all subcases**: In Tables 3 and 4, FRLoRA does not dominate across all evaluations, indicating it may not consistently outperform baselines in every setting. [Reviewer 3]
- **Impact of SVD initialization on generalization and convergence**: Initializing local low-rank matrices from top singular values while keeping the residual as the global model may reduce generalization capacity or convergence speed, since the global model should retain more generalized information from the pre-trained model. The motivation for this parameter decoupling lacks detailed discussion (e.g., via landscape visualization). Why not use the full pre-trained model as global initialization? [Reviewer 5]
- **Catastrophic forgetting risk**: Direct updates to W₀ in a low-rank context may risk catastrophic forgetting; can SVD initialization mitigate this? Additional ablation studies on learning rates are suggested. [Reviewer 4]
- **Does FRLoRA fully address the intrinsic challenge?**: While the global parameter space is expanded, local optimization constraints remain unchanged; the paper does not address whether this fully mitigates intrinsic issues at the local level. [Reviewer 4]
- **Missing ablation on rank r**: The paper does not systematically study how rank r impacts FedAvg+LoRA performance, and whether increasing r alone can achieve comparable results to FRLoRA, along with communication cost trade-offs. [Reviewer 4]
- **Lack of SVD stability analysis**: The paper briefly mentions SVD stability but does not explore potential impacts or alternative initialization methods for cases where SVD may cause convergence issues. [Reviewer 3]