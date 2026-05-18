I've now thoroughly read and verified the paper against the reviewer claims. Here is my consolidated review.

---

## Summary

This paper proposes MFC (Multi-Scale Frequency Domain Causal), a plug-and-play MIL framework for WSI classification that combines (1) a Causal Memory Intervention Module (CMIM) replacing costly clustering with trainable memory for front-door deconfounding, (2) a Multiscale Spatial Representation Module (MSRM) for multi-resolution tissue features, and (3) a Frequency-domain Structural Representation Module (FSRM) applying the Hilbert transform to capture phase-based information. Experiments on Camelyon16 and TCGA-NSCLC show consistent gains in accuracy, F1, and specificity across five MIL baselines.

## Strengths

1. **Plug-and-play compatibility yields consistent improvements across multiple MIL baselines.** The MFC framework is applied to ABMIL, DSMIL, TransMIL, CLAM-SB, CLAM-MB, and DTFD-MIL. Table 1 shows every baseline improves on accuracy, F1, and specificity (e.g., DSMIL accuracy rises from 89.53% to 94.80% on Camelyon16). This demonstrates practical value as a generally applicable module.

2. **Thorough ablation and hyperparameter analysis substantiate each module's contribution.** Tables 3 and 4, and Figure 3 systematically isolate CMIM, MSRM, and FSRM effects and study memory size \(k\) and joint dimension \(D_j\). CMIM alone improves specificity by ~10% over the TransMIL baseline (Table 3); performance peaks at moderate \(k\) values (16 for high-res, 32 for low-res), providing practical design guidance.

3. **Honest discussion of metric trade-offs strengthens empirical credibility.** The paper explicitly acknowledges that AUC gains are sometimes modest or negative (e.g., CLAM methods on Camelyon16) and explains that MFC shifts the decision boundary to favor specificity over recall (Section 4.4, Section 4.5.1). This nuanced treatment of trade-offs is rare and valuable.

4. **Clear causal motivation grounded in Structural Causal Models.** The paper uses an SCM diagram (Figure 1b–d) and Equations 3–5 to trace \(P(Y|do(X))\) through the mediator \(M\), providing a principled justification for the front-door intervention framing.

## Weaknesses

### Fatal
None.

### Major

1. **The CMIM memory-based intervention is mathematically underspecified, preventing reproducibility.**  
   Section 3.1 introduces the front-door intervention (Eq. 4–5) and then states that a trainable memory module with \(k\) slots is combined with "attention-weighted inputs" and "Normalized Weighted Geometric Mean (NWGM)" to estimate the equation. However, the paper never defines: how the attention weights over memory slots are computed, how \(P(M=m\mid X=x)\), \(P(X=\hat{x})\), or \(P(Y\mid X=\hat{x},M=m)\) are derived from the memory, how the NWGM approximation is applied in this context, or how the memory parameters are updated during training (lines 87–88 contain the entire description). Since CMIM is the paper's central methodological contribution (replacing clustering with a memory module for front-door intervention), the absence of these equations means the core technique cannot be reproduced, evaluated, or compared against prior work. This is the most serious issue in the paper.

2. **The application of the Hilbert transform to feature vectors is technically unjustified and underspecified.**  
   Section 3.3 defines FSRM as applying the Hilbert transform operator \(H\) to a 512-dimensional feature vector \(\mathbf{W}_1\mathbf{x}+\mathbf{b}_1\) (line 140). The Hilbert transform is a well-defined operation on continuous-time signals or discrete-time *sequences* where adjacent samples have a meaningful ordering (time, space). A neural network feature vector has no such ordering—its dimensions correspond to learned features, not indices along a meaningful axis. The paper provides no explanation of how the transform is discretely implemented (e.g., via FFT or convolution), along which axis it is applied, or why this operation yields meaningful structural information for pathology features. Without this justification, the entire FSRM contribution rests on technically shaky ground.

3. **The causal deconfounding claims are not evaluated in any controlled setting.**  
   The paper's central narrative is that MFC "eliminates spurious correlations" and "mitigates data bias" through causal intervention. Yet no experiment directly tests this: no synthetic datasets with known confounders, no counterfactual analysis, no evaluation under introduced biases (color shift, staining artifacts), and no comparison of decision patterns before/after intervention. The performance gains on real datasets could plausibly arise from the multiscale features, the frequency-domain representations, or better optimization—not necessarily from successful causal deconfounding. The AUC degradation on several baselines even raises the possibility that the method improves threshold-based metrics at the expense of ranking, which is not obviously a causal effect. A paper making causal claims needs causal validation.

### Minor

1. **No computational cost analysis despite efficiency claims.** The paper argues that CMIM avoids "time-consuming feature clustering" (lines 16, 40, 87) and "enhances computational efficiency," but never reports training times, memory usage, or runtime comparisons against CaMIL or IBMIL. This is a significant omission for a paper claiming efficiency as a selling point.

2. **The Hilbert-versus-alternatives comparison is presented only in text, not in a clear table.** Section 4.5.3 discusses numerical results comparing Hilbert (AUC 97.68%) against FFT (91.66%), DCT, and DWT, but these numbers appear in prose rather than a dedicated table with standard deviations. A proper table would make the comparison far more transparent and reproducible.

3. **The claim that FSRM "reduces interference from staining techniques and color contrast" is never tested.** The paper asserts this in the introduction (line 18) and conclusion (line 242) but includes no stain variation experiments, no cross-dataset generalization evaluation under domain shift, and no ablation with stain augmentation. This claim should either be supported or removed.

4. **IBMIL comparison is limited to one dataset and one baseline.** Table 2 compares against IBMIL only on Camelyon16 with DSMIL. Testing on TCGA-NSCLC and with another baseline (e.g., ABMIL or TransMIL) would substantially strengthen the comparison.

5. **The integration of the three modules into a coherent pipeline is not clearly specified.** The method section presents MSRM, FSRM, and CMIM separately; it is left to the reader to infer the data flow (e.g., which features feed into which module, how \(X_{hl}\) and \(X_{ll}\) relate to the mediator \(M\), whether FSRM applies to one or both scales, how the outputs combine before or during the intervention). A pipeline diagram or algorithm pseudocode would resolve this.

6. **Memory slot sensitivity analysis is only for one model-dataset pair.** Figure 3 varies \(k\) only for TransMIL on Camelyon16. Whether the optimal \(k\) values generalize to other architectures or the TCGA-NSCLC dataset is unknown.

### Trivial
None.

## Nice-to-Haves

- A synthetic confounder experiment (e.g., introducing a color bias into the Camelyon16 training set and measuring whether MFC is more robust than baselines) would directly validate the causal claims.
- Including a controlled analysis distinguishing threshold shift from genuine deconfounding (e.g., examining full ROC curves, computing partial AUC at high specificity, or evaluating calibration) would clarify the specificity/recall trade-off.
- Reporting training time comparisons against CaMIL and IBMIL would substantiate the efficiency motivation.
- A dedicated table comparing Hilbert, FFT, DCT, and DWT with standard deviations would improve transparency.

## Removed Points

The following points from the harsh critic were removed or downgraded based on verification against the paper:

- **"AUC degradation suggests non-causal improvements"** — kept as Major #3 (causal evaluation missing) but removed the stronger accusation that AUC degradation *proves* non-causal improvement, as the paper openly discusses this trade-off and the improvement on other metrics is consistent.
- **"CMIM increasing specificity while decreasing recall could be a threshold shift"** — moved to Nice-to-Haves since the paper already discusses this trade-off honestly; a more rigorous analysis would be a reasonable extension rather than a flaw.
- **"Figure 2 content not parseable"** — this is a parser artifact, not an author error. The information is conveyed in the text.
- **"The paper should also cover more domains/tasks"** — scope creep; the paper covers two major WSI benchmarks with five baselines, which is appropriate for its scope.

## Novel Insights

Beyond the paper's own contributions, a genuinely novel observation that emerges from the reviews is that the specificity-vs-recall pattern produced by CMIM (specificity approaching ~100%, recall dropping) is precisely the pattern one would expect from a decision boundary that becomes more conservative on negative examples. This raises an important question that the paper does not resolve: is this shift a sign of genuine deconfounding (i.e., the model learns to avoid false positive confounders) or a threshold artifact unrelated to causality? Resolving this would require either (a) a controlled confounder experiment showing that the model is robust to specific spurious correlations that fool baselines, or (b) evidence that the same decision boundary shift does *not* occur when the model is trained on data without the suspected confounder. The paper's current empirical setup cannot distinguish these explanations, and the field would benefit from a clearer disentanglement.

## Suggestions

1. **Provide the full mathematical specification of CMIM.** Include explicit equations for: computing attention weights over memory slots (e.g., \(\alpha_i = \text{softmax}(q^T m_i)\)), deriving \(P(M=m|X=x)\) and \(P(X=\hat{x})\) from memory activations, the NWGM approximation in this context, and the memory update rule during training.
2. **Justify or redesign the Hilbert transform application.** Specify the discrete implementation (FFT-based or convolution-based), the axis along which it is applied, and why the operation is meaningful on neural feature vectors. If no principled justification exists, consider replacing the Hilbert transform with a better-motivated frequency-domain operation (e.g., learned filter banks).
3. **Add a controlled causal evaluation.** Design a synthetic confounder experiment (e.g., color bias injected into Camelyon16 training data) and show that MFC is more robust than baselines, or use counterfactual explanation techniques to verify that decisions rely on diagnostically meaningful features after intervention.
4. **Report training time/memory comparisons** against CaMIL and IBMIL to substantiate the efficiency claim.
5. **Provide a pipeline diagram or algorithm pseudocode** showing the exact data flow: which features enter MSRM, how the outputs \(X_{hl}\) and \(X_{ll}\) are processed by FSRM, how these connect to the CMIM mediator, and the order of operations.

## Score and Decision

The paper tackles an important problem and shows promising empirical results across multiple baselines. The ablation studies are thorough and the honest discussion of metric trade-offs is commendable. However, the paper suffers from three significant weaknesses that undermine its core contributions: (1) the central CMIM method is mathematically underspecified and cannot be reproduced, (2) the Hilbert transform application to feature vectors is technically unjustified and lacks implementation details, and (3) the causal deconfounding claims are not validated by any controlled experiment. These gaps are too substantial to be addressed in a short rebuttal. I encourage the authors to address them in a major revision.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>