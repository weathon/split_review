## Summary

3DMolFormer proposes a unified dual-channel transformer framework that handles both protein-ligand docking and pocket-aware 3D drug design within a single architecture. It represents 3D complexes as parallel sequences of discrete tokens (atoms/SMILES) and continuous 3D coordinates, processed by a GPT-2-style model augmented with a numerical prediction head. The model is pre-trained on a large mixed dataset (228M samples), then fine-tuned via supervised learning for docking and reinforcement learning for drug design — with the docking-fine-tuned weights reused for coordinate generation during drug design to exploit the duality between the two tasks.

## Strengths

- **First unified framework that concretely exploits the docking–drug-design duality**: 3DMolFormer is the first approach to handle both tasks within a single architecture and explicitly leverages their duality: the docking-fine-tuned weights are frozen and reused for coordinate generation during RL-based drug design (Section 3.4.2, lines 137–138). This is a principled mechanism absent in prior work, and the paper demonstrates how the predictive task (docking) directly feeds into the generative task (drug design).

- **Parallel sequence format that preserves coordinate continuity**: By separating discrete tokens from continuous floating-point values, the design avoids the coordinate discretization that prior transformer-based 3D methods (XYZ-transformer, BindGPT, Token-Mol) impose (Section 2, lines 40–41). The dual-channel architecture (Section 3.2) processes both modalities simultaneously, directly addressing a known challenge in 3D molecular modeling.

- **No initial ligand conformation required for docking**: Unlike all baseline docking methods, 3DMolFormer does not require an initialized 3D ligand conformation as input (line 176). This is a practical advantage that simplifies the docking pipeline and suggests the model acquired conformation prediction through pre-training.

- **Pre-training shown to be critical via controlled ablation**: The w/o PT ablation in Table 1 demonstrates substantially degraded docking performance without pre-training, confirming that the "pre-training + fine-tuning" strategy is essential — not decorative.

- **Fast inference suitable for virtual screening**: 3DMolFormer predicts a binding pose in 0.8 seconds on a single A100 GPU (line 178), orders of magnitude faster than search-based methods, making it practical for large-scale virtual screening applications.

## Weaknesses

### Fatal
None.

### Major

1. **Drug design comparison is asymmetric: per-pocket RL optimization vs. one-shot generation**. The RL fine-tuning runs 500 optimization steps per pocket with a batch size of 128 (line 212), generating and evaluating ~64,000 molecules per pocket during optimization. The baselines (AR, liGAN, GraphBP, Pocket2Mol, TargetDiff, DecompDiff) are one-shot generative models that produce molecules in a single forward pass — they were not designed to perform per-pocket optimization at inference time. The paper presents this as a direct comparison of method quality ("outperforms" all baselines across all metrics, line 218), but the results conflate the power of per-pocket multi-objective optimization with the quality of the dual-channel representation. A fairer evaluation would compare against other per-pocket optimization methods (e.g., RL-based SMILES generators, genetic algorithms like AutoGrow) under a matched optimization budget to isolate whether the architecture and docking-weight initialization provide a genuine advantage.

2. **No statistical uncertainty reported anywhere**. Table 1 (docking) and Table 2 (drug design) report only point estimates — no standard deviations, confidence intervals, or measures of variance. Given the modest test set sizes (285 complexes for docking, 100 pockets for drug design), the stochastic nature of generation and RL fine-tuning, and the close margins on some metrics (e.g., Smina leads on RMSD < 1.0 Å), the absence of uncertainty quantification makes it impossible to determine whether reported improvements are reliable or within noise. This is an evidential weakness: the conclusions may be correct, but the evidence does not support them at the stated confidence level.

3. **Reward function uses the same scoring function (Quick Vina 2) as a key evaluation metric**. The composite reward function (Eq. 3–5) includes a Vina Dock component computed by Quick Vina 2 (line 193, line 207). One of the four main evaluation metrics (Vina Dock, Table 2) is also computed by Quick Vina 2 (line 188). This creates a circularity where the method is explicitly optimized to maximize scores from a particular scoring function and then evaluated on that same scoring function — a well-known pitfall that can produce molecules exploiting weaknesses in the proxy rather than genuinely possessing high binding affinity. The QED and SA metrics are independent and mitigate this somewhat, but the headline Vina Dock and Success Rate metrics are directly affected.

### Minor

1. **SE(3)-equivariance claim is asserted without evidence**. Section 5 (lines 229–230) states that "it appears that through the normalization of 3D coordinates and random rotations during data augmentation, 3DMolFormer has acquired the SE(3)-equivariance." No empirical evidence is provided — no rotation tests at inference time, no equivariance error analysis, no comparison to an equivariant baseline. However, this claim is hedged ("it appears") and is not central to the paper's contributions or results; it is discussed speculatively in the conclusion.

2. **Data replication ratios in pre-training are unexplained and not ablated**. Section 4 (line 149) replicates protein pockets 5× and pocket-ligand complexes 20× to reach 228M training samples. These specific ratios are not justified, and no ablation study explores their impact on downstream docking or drug design performance. The 20× amplification of complex data substantially changes the effective training distribution relative to natural frequencies.

3. **No validation monitoring for docking fine-tuning**. The model is fine-tuned for 2000 epochs on ~18K training samples (line 172). Despite data augmentation (SMILES randomization + random rotation), no validation set performance or training curves are reported to demonstrate that overfitting is controlled during this extended training.

### Trivial
None.

## Nice-to-Haves
- Report standard deviations or confidence intervals for all main results (Tables 1 and 2).
- Compare against per-pocket optimization methods (e.g., AutoGrow, RL-based SMILES generators) under a matched optimization budget to isolate the contribution of the dual-channel architecture.
- Validate generated molecules with an independent docking scoring function (not Quick Vina 2) to address reward-hacking concerns.
- Provide empirical equivariance tests (rotate inputs and check prediction consistency), or remove the unsupported claim from Section 5.
- Ablate the data replication ratios (5×, 20×) to justify these choices.
- Report per-pocket result distributions (median, quartiles) for drug design across the 100 pockets.
- Discuss alternative token-value fusion strategies (addition vs. multiplication) for the dual-channel input stage.

## Removed Points
These points were flagged for removal; treat them with caution.
- "Numerical values in the table are embedded in an image and cannot be verified from the text": This is a PDF extraction artifact, not a paper flaw. Removed.
- "The token-embedding multiplication creates unstable dynamics near zero coordinates": Speculative — the model demonstrably works. Moved to nice-to-have.
- Various formatting/style nitpicks, typo/grammar concerns, missing appendix/proof concerns: These are parser artifacts or rule-excluded categories. Removed.
- Generic or unanchored criticisms ("evaluation lacks rigor" without specific anchor, "evidence is weak for the claims" without concrete citation): Removed per filtering discipline.
- Strength finder's generic strengths ("addressed an important problem," "targeted an interesting question"): Generic/insufficiently specific. Removed.

## Novel Insights
None beyond the paper's own contributions. The reviews surface evaluation-design issues (comparison asymmetry between RL-optimized and one-shot generation, reward–metric overlap) that are recognized concerns in the generative drug design literature but are not novel methodological insights.

## Suggestions
1. **Fix the drug design comparison**: Add baselines that also perform per-pocket optimization (RL-based SMILES optimization with the same reward, or a genetic algorithm like AutoGrow) under a matched budget of scoring function evaluations. This would isolate whether the dual-channel architecture and docking-weight transfer provide a genuine advantage over simpler optimization-based approaches.
2. **Report variance**: Add standard deviations or confidence intervals to Tables 1 and 2. For drug design, per-pocket quartiles would be more informative than a single mean.
3. **Validate with an independent scoring function**: Use a different docking program to evaluate generated molecules, addressing the reward-hacking concern.
4. **Empirical equivariance test**: Remove or substantiate the SE(3)-equivariance claim in Section 5.
5. **Ablate the data replication ratios**: Vary the 5×/20× ratios and report impact on performance to justify the choices.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>