## Summary

This paper proposes Q-flow, a neural ODE model that learns a continuous invertible transport map between two arbitrary distributions $P$ and $Q$ from finite samples. The flow network is trained to minimize the Benamou-Brenier dynamic OT cost, with the terminal condition enforced via a classifier-estimated KL divergence. After training, the learned OT trajectory is leveraged for telescopic density ratio estimation via a separate continuous-time ratio net. The method is evaluated on high-dimensional OT benchmarks, density ratio estimation (including mutual information estimation and energy-based modeling), and image-to-image translation.

## Strengths

- **End-to-end learning of dynamic OT without pre-computed couplings.** Unlike prior neural OT methods (OTCFM, rectified flow) that require pre-computed mini-batch OT solutions or iterative coupling rectification, Q-flow directly minimizes the Benamou-Brenier transport cost from finite samples by parameterizing the flow as a neural ODE and using a classifier to estimate the terminal KL divergence. This is a clean and principled formulation.

- **Strong and consistent empirical results across multiple tasks.** Q-flow achieves the best or tied-best L2-UVP and cosine similarity on Gaussian mixture OT benchmarks across dimensions 32–256 (Table 1), outperforms NOT, OTCFM, W2, and MM methods on CelebA64 image OT (Table 2), and achieves lower FID than NOT, CycleGAN, and DiscoGAN on handbag→shoes and CelebA male→female translation (Table 3). The improvements are consistent across nearly all settings.

- **Demonstrated benefit of OT trajectory for density ratio estimation.** The ratio net trained on the Q-flow trajectory achieves substantially lower MAE on 2D GMM DRE (2.38 vs. 3.22 for DRE-inf and 3.05 for TRE) and near-perfect mutual information estimation on high-dimensional Gaussians where baselines degrade significantly as dimension increases (Figure 4).

- **Continuous and invertible transport.** The neural ODE formulation provides a continuous-time interpolation between $P$ and $Q$ that is invertible, which enables both forward and reverse DRE and provides interpretable trajectories for image translation.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Alternating optimization lacks convergence and stability analysis.** The training procedure (Algorithm 1) alternates between updating the flow network and retraining the classifiers $c_1, \tilde{c}_0$, which the paper notes is "crucial" (line 305). However, no analysis of convergence, sensitivity to the number of inner-loop epochs ($E_{\rm in}$), or monitoring of classifier accuracy/gradient norms is provided. While the paper's empirical results demonstrate that the procedure works in practice, the lack of any diagnostic or ablation on the alternating dynamics is a gap in methodological validation.

2. **No error bars or confidence intervals reported.** All main results (Tables 1–3) are reported as point estimates without standard deviations or confidence intervals. Many improvements over baselines are modest (e.g., L2-UVP 3.27 vs. 3.74 for OTCFM at d=32; BPD 1.05 vs. 1.09 for RQ-NSF). Without statistical significance measures, it is difficult to assess whether the improvements are reliable or within the noise of the evaluation.

3. **OT baselines cited from prior work, not re-run.** The paper explicitly notes that the last three rows of Tables 1 and 2 (MMv1, MMv2, W2; MM, MM:R, W2) are from \citep{korotin2021do}. The paper does not state whether OTCFM and NOT results were re-run or cited. Without re-running baselines under controlled conditions (same architectures, training budgets, data splits), strict comparisons are inexact.

4. **No ablation isolating the benefit of OT optimality for DRE.** The DRE experiments show that the Q-flow trajectory improves over linear-interpolant baselines (TRE, DRE-inf). However, it is unclear whether this improvement is due to the OT optimality of the trajectory or simply because the Q-flow trajectory is a well-regularized non-linear flow. An ablation comparing DRE on the initial (pre-refinement) flow vs. the refined (OT) flow would directly isolate the contribution of OT optimality.

5. **Computational cost comparison lacks detail.** The paper states that Q-flow took ~8 hours to converge on MNIST EBM vs. ~33 hours for DRE-inf (on one A100 GPU). No details about model sizes (parameter counts), batch sizes, ODE solver tolerances, or number of function evaluations are provided, making it difficult to assess the fairness or generalizability of this comparison.

6. **No explicit discussion of limitations or failure modes.** The Discussion section mentions theoretical open questions and computational scaling, but does not discuss practical failure modes (e.g., when $P$ and $Q$ are far apart and the classifier becomes inaccurate, or when data has complex high-dimensional structure). Including limitations would improve the paper's completeness.

### Trivial

- The reference to Table \ref{inv_err} (inversion errors) at line 297 is not present in the main text; this table likely belongs in an appendix that was not extracted.

## Nice-to-Haves

- An ablation showing the transport cost (W2 regularization term) decreasing during training from the initial flow to the refined flow would provide direct evidence that the refinement procedure succeeds.
- Testing DRE on a higher-resolution dataset (e.g., CIFAR-10) would strengthen the claim of high-dimensional applicability.
- More detailed analysis of the 8h vs. 33h computational comparison, including parameter counts and solver settings.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Central claim—that the trained flow approximates dynamic OT—is not directly verified."** — *Removed as factually incorrect.* The paper validates this claim on standardized OT benchmarks (Tables 1, 2) using L2-UVP and cosine similarity metrics, which directly measure how well the learned transport map matches ground-truth optimal maps. The transport cost is also explicitly minimized as part of the training objective (Equation 6). The paper does provide direct verification of its central claim.
  
- **"The paper does not discuss stochastic interpolants (Albergo et al., 2023) or flow matching (Lipman et al., 2023) in sufficient depth."** — *Removed as inaccurate.* The paper cites both Albergo et al. (2023) (line 83) and Lipman et al. (2023) (line 84) and explicitly distinguishes its approach (optimizing the interpolant) from these prior works (which use pre-specified interpolants). The initialization schemes are presented as modular starting points, not as part of the claimed novelty.
  
- **"The initialization schemes weaken the claimed novelty."** — *Removed as misunderstanding.* The paper frames initialization as a warm-start (Section 3.3) and explicitly states that the novelty lies in the end-to-end refinement that minimizes the OT cost, not in the initialization itself.
  
- **"Inversion errors cannot be assessed (inv_err table not present)."** — *Removed per rule: the parser strips appendix/supplementary sections; the table exists in the original submission.*

- **Criticisms about missing/stale classifier samples and the need to retrain classifiers** — *The paper already acknowledges and addresses this empirically, stating that diligent classifier updates are "crucial" (lines 304–306). The reviewer's concern is a question of rigor rather than an unaddressed flaw.*

- **"The method should test irrotationality of the velocity field."** — *Removed as scope creep. Verifying Benamou-Brenier necessary conditions at this level of detail is not standard practice for empirical OT papers and would be a separate contribution.*

- **Several section-by-section nitpicks (e.g., "only one configuration shown for 2D GMM" — factually there are multiple qualitative panels plus quantitative MAE; "improvements are small for MNIST EBM" — the improvements are small but consistent across all three settings; "only two image translation tasks" — two tasks is standard for this type of paper).** — *Removed as nitpicky or lacking substantive impact on the core claims.*

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add standard deviations or confidence intervals (across multiple runs with different random seeds) for all main quantitative results, especially when improvements over baselines are modest.
2. Include an ablation that compares DRE performance using the initial (pre-refinement) flow trajectory vs. the final (refined OT) flow trajectory to isolate the benefit of OT optimality.
3. Provide detail on the 8h vs. 33h computational comparison (model sizes, ODE solver tolerances, batch sizes) to make the speed-up claim actionable.
4. Add a brief discussion of practical limitations and failure modes — for example, cases where $P$ and $Q$ are far apart and classifier-based density ratio estimation may become unreliable.

## Score and Decision

**Overall assessment:** The paper makes a clear contribution by formulating an end-to-end method for learning dynamic OT between arbitrary distributions and demonstrating its usefulness across multiple downstream tasks. The empirical validation is extensive, covering OT benchmarks, DRE, and image translation. The weaknesses are real but minor — they concern missing ablations, statistical rigor, and presentation gaps rather than fundamental flaws. The core claims are well-supported.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>