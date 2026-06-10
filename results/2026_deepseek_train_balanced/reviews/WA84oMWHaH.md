## Summary

The paper proposes SPP (Solution Path Pruning), a pruning method for pretrained transformers that uses differential inclusion dynamics to generate masks at multiple sparsity levels from a single search stage. The method introduces a pairwise-shared mask design for transformer attention and MLP modules, and provides a convergence guarantee under the Kurdyka-Łojasiewicz framework. Experiments on DeiT, Swin, CLIP, and LLMs demonstrate that SPP can produce multiple sparse models from one search run with competitive accuracy.

## Strengths

1. **Single-search-stage multi-sparsity production**: The paper demonstrates that SPP produces multiple sparse models at different compression ratios from a single search run. In the CLIP experiment (line 223), a 6-epoch search stage yields 5 sparse architectures with different sparsity levels, each requiring only 5 fine-tuning epochs. This concretely shows the claimed efficiency advantage over methods that restart pruning per target ratio.

2. **Pairwise-shared mask design**: The paper introduces a structured pruning decomposition that divides MHSA into query-key pairs (shared mask M_QK) and value-output pairs (shared mask M_V), and applies a similar scheme to MLP layers (Section 3.1, Equations 4-6). This enables the (Q,K) pair and V to have different pruned dimensions, providing more flexibility than uniform-head pruning while maintaining dimensional consistency.

3. **Global convergence guarantee**: Theorem 1 provides a convergence proof showing the iterative sequence converges to a critical point of the masked loss from arbitrary initialization under the KL framework (lines 192-198). The step-size condition is explicitly stated. This is a stronger theoretical foundation than many pruning methods that lack convergence guarantees.

4. **Demonstrated extension to LLMs**: The method is extended to Llama2-7B and OPT-6.7b at 50% sparsity (Table 5), showing accuracy comparable to specialized methods RIA and Wanda across multiple datasets. This indicates broader applicability beyond vision transformers.

## Weaknesses

### Major

1. **Underspecified optimization problem and update dynamics**: The "Sparse optimization of masks" subsection (line 92) is a single sentence with no equations. The full optimization objective — how the ℓ₁ penalty is incorporated, what loss function is minimized with respect to the mask variable M, and the specific dynamics coupling M and Γ — is never explicitly stated. Section 4 gives the linearized Bregman iteration template (Eq. 10) and defines Ψ(P), but the reader must infer the exact objective and update rules from the convergence analysis rather than from a clear method description. This makes it difficult to assess what distinguishes SPP from prior LBI-based pruning (Fu et al., 2020) and hampers reproducibility.

2. **Internally inconsistent description of the solution path direction**: Line 16 states "the sparsity of the projected target model incrementally increases" while line 56 states the dynamics generates "a regularization solution path from sparse to dense." These describe opposite directions (increasing sparsity vs. going from sparse to dense). Since the paper's mechanism for obtaining multiple sparsity levels relies on early stopping along this path, the confusion over whether the path starts sparse and becomes denser (unmasking more weights) or starts dense and becomes sparser (masking more weights) undermines the reader's ability to understand the core algorithm. The paper also does not clearly state the initial state of M and Γ or how the pretrained dense weights interact with the mask trajectory.

### Minor

3. **The convergence guarantee does not address the multi-sparsity claim**: Theorem 1 proves convergence to a critical point of the masked loss, but says nothing about whether intermediate masks along the trajectory correspond to useful subnetworks or whether the solution path property (ordering features by importance) holds for the non-convex transformer loss. The paper's central claim — that one can obtain a family of viable sparse models at different sparsity levels from one run — depends on empirical validation and properties inherited from LBI theory for convex problems, not on the theorem presented. The paper would benefit from explicitly acknowledging this gap.

4. **LLM experiments do not validate the multi-sparsity advantage**: The LLM extension (Table 5) evaluates at only a single sparsity level (50%). This does not demonstrate the paper's headline advantage of obtaining multiple sparsity levels from one run. Any standard pruning method operating at a single target ratio would suffice for this comparison. The paper positions this as showing "potential," but it does not support the thesis.

5. **Ablation does not isolate contributing factors**: The ablation against DessiLBI (Section 5.2, line 231) shows SPP outperforms DessiLBI under identical fine-tuning, but the ablation does not isolate which component drives the improvement — the pairwise mask design, the pretrained initialization, or the specific optimization formulation. Without such isolation, the comparison is informative but incomplete.

6. **Claim of asymmetric dimensionality is overstated**: The paper claims the method "enables an asymmetric dimensionality between the query, key, and value matrices after pruning" (line 39). However, Q and K share the same mask M_QK (Eq. 4), so they remain symmetric in dimension. The asymmetry exists between the (Q,K) pair and V — a more modest flexibility gain than the blanket statement suggests.

### Trivial

7. **The paper lacks a limitations section** that would contextualize the theoretical and practical scope of the method.

## Nice-to-Haves

- **Quantify the computational savings**: The paper repeatedly claims SPP reduces cost by avoiding restarts. A direct comparison (wall-clock time or FLOPs for SPP in one run vs. running a standard method at 3-5 sparsity targets) would strengthen this claim.
- **Validate intermediate checkpoints as useful subnetworks**: Show that checkpoints at different sparsity levels from the *same* run, after fine-tuning, perform comparably to models pruned independently at each level.
- **Explicitly state the initial conditions**: Clarify the initial values of M and Γ and how they relate to the pretrained weights.
- **Clarify the distinction from prior LBI work**: Provide a clearer delineation of what algorithmic changes SPP introduces versus Fu et al. (2020)'s application to CNNs trained from scratch.

## Removed Points

These points were considered and removed per the filtering rules:
- "The core method is not specified (STRUCTURAL) / structural failure" — overstatement; the Bregman iteration framework IS provided (Eq. 10), but the method is underspecified. Downgraded from claimed "structural failure" to Major weakness #1.
- "Missing hyperparameters and reproducibility details" — these may be in the appendix (stripped by parser). Removed per hard rule.
- "Constants Lip, C, ν, κ not defined in terms of model architecture" — standard practice in convergence analysis to use abstract constants. Removed.
- Critic's complaint about missing baselines for the core claim (DessiLBI on multi-sparsity) — partially addressed by existing ablation. Merged into Minor weakness #3 and #5.
- Various formatting/style nitpicks — removed per hard rules.

## Novel Insights

Beyond the paper's own contributions, the review process highlights a recurring tension in pruning research: convergence guarantees (like Theorem 1) address optimization trajectory properties, not subnetwork quality, yet papers often present them as evidence for the latter. The gap between "the iterates converge" and "the intermediate iterates are good pruned models" is a methodological distinction that remains underexplored in the pruning literature. Additionally, the pairwise mask design raises an interesting architectural question — whether the optimal allocation of sparsity across Q, K, V, and output projections differs enough to justify the added complexity of per-pair masks, or whether simpler uniform-head pruning captures most of the benefit.

## Suggestions

1. Restructure Section 3 to explicitly state the full optimization objective (e.g., min_{M,Γ} L(W⊙M) + λ‖Γ‖₁ with the differential inclusion dynamics) and provide closed-form update equations for M and Γ.
2. Resolve the path-direction inconsistency: clearly state whether the mask starts sparse (mostly zeros) and becomes dense (adding features) or vice versa, and explain precisely how early stopping along this path yields models at different sparsity levels.
3. Report LLM results at multiple sparsity levels (e.g., 30%, 50%, 70%) to validate the multi-sparsity claim.
4. Add an ablation that isolates the pairwise mask design from the optimization framework.
5. Include a direct wall-clock comparison showing the computational savings of a single SPP run vs. independent runs of a baseline method at multiple sparsity targets.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>