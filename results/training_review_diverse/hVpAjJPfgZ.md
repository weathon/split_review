Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper addresses the Lookback Window Limitation (LWL) in long-term time series forecasting by proposing two model-agnostic modules: Information Bottleneck Filter (IBF) to reduce information redundancy, and Hybrid-Transformer-Mamba (HTM) to address Transformer's difficulty with long sequences. Combined with PatchTST, the resulting PIH model extends the lookback window to L=1024—longer than typical prior work—and achieves state-of-the-art results across seven datasets.

## Strengths

- **Novel dual-principled approach to overcoming LWL.** The paper identifies two distinct causes of LWL (information redundancy and architectural limitations) and proposes separate modules targeting each. IBF applies a variational information bottleneck with noise injection to filter redundant subsequences (Section 3.2), while HTM partitions long sequences so Mamba handles global dependencies and Transformer handles short-range patterns (Section 3.3). This combined information-theoretic + architectural approach is new relative to heuristic patching or sparse-attention methods.

- **Demonstrates effective scaling to L=1024 with consistent monotonic improvement where existing methods degrade.** Figure 3(a) shows that as the lookback window increases from 96 to 1024, PatchTST's performance improves up to 512 then declines at 1024, while PIH's MSE decreases monotonically across all window sizes. This is the paper's strongest evidence—it directly validates the central thesis that longer windows can be beneficial when LWL is properly addressed.

- **Model-agnostic modules improve multiple Transformer architectures.** IBF and HTM are integrated into Transformer, Informer, and Autoformer, with clear performance lifts shown in Figures 4 and 5. For instance, on ETTm1, Electricity, and Traffic (T=720), the original models' effective window limitations are 48, 48, and 120 respectively; after integration these increase to 192, 96, and 228 with better absolute MSE. This demonstrates generality beyond the authors' own PIH model.

- **Computational efficiency gains.** HTM reduces runtime and memory by 2–3× compared to PatchTST (Figure 3b), supported by the complexity analysis (overall O(L/P) + O((L/PK)²)). IBF adds negligible overhead since it consists of a simple MLP. This makes the approach practical for very long windows.

## Weaknesses

### Fatal
None.

### Major

- **Undefined variables A and B in the IBF loss derivation.** In Equation 9 (Section 3.2), the variational upper bound for the compression term is given as:
  \[
  -I(\mathbf{z}^{\text{noise}},\mathbf{z}) \leq \mathbb{E}_{\mathbf{z}}\left(-\frac{1}{2}\log A + \frac{1}{2N}A + \frac{1}{2N}B^{2}\right)
  \]
  The symbols \(A\) and \(B\) are introduced without any definition or derivation. Since this bound is central to training the IBF module, the omission makes it impossible for readers to verify or reproduce a core component of the method. The surrounding text notes that "we can derive its variational upper bound" but provides no sketch of how this follows from the mutual information term, the noise distribution \(\mathbf{z}^{\text{noise}} = \lambda\mathbf{z} + (1-\lambda)\epsilon\), or the Gaussian prior on \(\epsilon\). This is a structural presentation gap: a reader cannot determine whether \(A\) and \(B\) denote quantities like \( (\mathbf{z}^{\text{noise}} - \mu)^\top\Sigma^{-1}(\mathbf{z}^{\text{noise}} - \mu) \) or some other variance-related terms without either guessing or consulting external references.

- **Integration of HTM and IBF into non-Mamba models is unspecified, undermining the claim of model-agnosticity.** Section 4.2 reports that HTM and IBF are integrated into Transformer, Informer, and Autoformer, leading to improved performance (Figures 4, 5). However, the paper never explains *how* this integration is done. The IBF module is described as operating on the output of Mamba layers (Section 3.2: "we apply IBF after Mamba layers"), and HTM partitions sequences so Mamba processes the long sequence while Transformer handles short subsequences. For models that have no Mamba component (vanilla Transformer, Informer, Autoformer), it is unclear which parts are replaced, added, or modified—whether Mamba is introduced as an additional encoder, whether existing attention layers are replaced, or how the HTM partitioning works without a Mamba module. Without this information, the claimed generality of the modules cannot be evaluated, and the experiments in Section 4.2 are not reproducible.

### Minor

- **Hyperparameter choices for \(\beta\), \(\tau\), and \(K\) are not discussed, and no sensitivity analysis is provided.** The IBF loss uses a Lagrangian multiplier \(\beta\) (Equation 10), the Gumbel sigmoid uses a temperature \(\tau\), and HTM requires choosing the number of blocks \(K\) (Section 3.3). None of these values are reported, nor is there any ablation showing how they affect performance. This limits reproducibility and makes it difficult to assess the robustness of the method.

- **No statistical significance measures.** Results are reported as point estimates (MSE/MAE) without standard deviations, confidence intervals, or significance tests. Given modest differences between PIH and strong baselines like PatchTST (e.g., average MSE 0.264 vs. 0.284) and the limited number of datasets (7), it is unclear whether improvements are stable across runs. While single-run evaluation is common in this field, reporting variance would substantially strengthen the evidence.

- **Missing values in Table 1 are not discussed.** The table has missing entries (e.g., Informer runs out of memory for some horizons), and the paper does not state how these are handled when computing column-wise averages in the final row. This is a minor but easily fixable oversight.

### Trivial

- The choice between interval split and block split (Section 4.3) is acknowledged as dataset-dependent but not analyzed for correlation with dataset periodicity or other properties—this is already noted as future work by the authors, so it carries no weight in evaluation.

## Nice-to-Haves

- Figure 3(a) would be more informative if it also included a Mamba-only baseline (e.g., S-Mamba or a Mamba+patch variant) on the same window sweep, to better isolate the contributions of each architectural choice.
- The interpretability analysis (Figure 3c) is a single example. A quantitative evaluation—such as comparing the subset selected by IBF to a random subset in terms of forecasting error, or measuring compression rate vs. accuracy—would strengthen this claim.
- Reporting each baseline's performance at L=1024 alongside its optimal-window performance in an appendix would provide additional clarity, though the paper's current design (baselines at their best windows vs. PIH at L=1024) is already a fair and arguably stringent comparison.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Asymmetric baseline comparison (Critical Issue 3 from Harsh Critic).** The critic claims the comparison is unfair because baselines were evaluated at their optimal windows while PIH is only shown at L=1024. However, the asymmetry favors the *baselines* (they receive an advantage from window selection), and the paper provides same-window controls in Figure 3(a) for PatchTST and sets DLinear/NLinear at L=1024. The rule states that weaknesses about unfair comparison should be removed when the asymmetry favors the baseline. This criticism is not valid against the paper's actual experimental design.

- **"The paper does not mention any failure cases or datasets where longer windows hurt."** Factually incorrect—the paper's Conclusion (Section 5) explicitly states: "we found that longer lookback windows are not always beneficial for all datasets. Therefore, identifying which types of data are suitable for very long windows is another important area for future research." The paper acknowledges this limitation directly.

- **Criticism about the derivation of Eq. 9 being "not even sketched."** This overlaps entirely with the A/B definition issue (kept as Major above) and adds no new content. Redundant points are consolidated.

## Novel Insights

The harsh reviewer's observation that the paper's central evidence (Figure 3a) would benefit from additional baselines is a useful suggestion but not a novel insight about the paper itself. The strength finder's observation that the paper demonstrates *monotonic* improvement to L=1024 where PatchTST degrades after 512 is the strongest empirical insight—it shows the LWL is not a fundamental bound but a solvable engineering problem. The broader implication—that information-theoretic filtering and hybrid architectures can unlock longer windows—is the paper's own contribution, not an external insight.

## Suggestions

1. **Define A and B explicitly** in Equation 9 and provide a brief derivation (2–3 lines) showing how the variational upper bound on \(I(\mathbf{z}^{\text{noise}},\mathbf{z})\) leads to the given expression. This should reference the noise distribution \(\epsilon \sim \mathcal{N}(\mu_\mathbf{z}, \sigma_\mathbf{z}^2)\) and the Gamma/Poisson identity if that is the intended derivation.

2. **Specify the integration procedure** for non-Mamba models. Provide a clear recipe: for vanilla Transformer, does HTM introduce Mamba as a parallel encoder? How is IBF placed when there is no Mamba-produced encoding? A figure or pseudocode in the appendix would suffice.

3. **Report hyperparameters** \(\beta\), \(\tau\), and \(K\) used in the experiments, and ideally include a sensitivity analysis showing how performance varies with these choices (at least for one dataset).

4. **Add multiple-run statistics** (mean and std over at least 3 seeds) to the main results, especially for the closest comparisons between PIH and PatchTST.

## Score and Decision

The paper addresses a well-motivated problem, proposes a novel dual-module approach, and provides compelling empirical evidence that scaling to L=1024 with monotonic improvement is achievable. The core empirical contribution is real. However, two structural presentation gaps—undefined symbols (A, B) in the IBF loss derivation and unspecified integration details for non-Mamba models—prevent verification and reproduction of key components. These are fixable in revision but are significant enough to preclude acceptance in the current form. The minor issues (missing hyperparameters, no statistical measures) further weaken the presentation.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>