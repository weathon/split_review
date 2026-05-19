- Decision: Reject
- Avg Score: 6.67
- Scores: 6, 6, 8
Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper proposes SAIL (Structured-Initialization Learning), a method that accelerates neural network training by: (1) transforming parameters from pre-trained models (via width/depth linear mappings) to match a target architecture, (2) computing optimal weighted combination coefficients (proximal parameter) based on total variation distances between training datasets, and (3) using this combined parameter vector as initialization for training a new model. Theoretical results include convergence bounds (under linear model assumptions) and closed-form optimal weights. Experiments on small GPT-2 (21M parameters) and ResNet variants across NLP and vision tasks show that SAIL-initialized models converge faster and reach lower loss than random initialization.

## Strengths

1. **Closed-form optimal merging weights (Theorem 3, Eqs. 7–8)**: The paper derives explicit formulas for the optimal combination coefficients \(\gamma_i^*\) in terms of total variation distances between datasets, for both the n=2 and n>2 cases. This provides a principled, theoretically-grounded approach to weighting pre-trained models rather than relying on heuristics. The empirical validation in Section 4.4 (theoretical \(\gamma^* = -0.1244\) via MMD vs. empirical optimum in Figure 2b, with step resolution 0.1) provides supporting evidence.

2. **Cross-architectural parameter transformation (Section 4.1, Eqs. 5–6)**: Unlike prior model reuse methods such as Net2Net which require identical or expandable architectures, SAIL provides explicit linear mappings for both width (Eq. 5, using \(C_{\text{in}}, C_{\text{out}}\) matrices) and depth (Eq. 6, using \(D_{\text{depth}}\) matrix), enabling transfer from pre-trained models with arbitrary layer dimensions and numbers to a different target architecture. The mathematical formulation is clean and extends the scope of model merging.

3. **Evaluation spans NLP and vision, supervised and self-supervised**: Experiments cover GPT-2 for language modeling (Section 4.4) and multiple ResNet variants (ResNet-18, ResNet-34, modified versions) on CIFAR-10/100 and Tiny ImageNet under both supervised (SupCE) and self-supervised (BYOL) paradigms (Section 4.5), demonstrating modality-agnostic applicability beyond a single domain.

4. **Systematic analysis of data overlap effects (Figure 2c)**: The paper studies how overlap between pre-training datasets (\(D_1, D_2\)) and the target dataset (\(D_t\)) affects the optimal merging ratio, revealing symmetry properties at high overlap and asymmetry at low overlap. This provides useful practical insight for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **Parameter transformation method is critically underspecified (Section 4.1)**: Equations (5) and (6) define the form of the width and depth transformations using matrices \(C_{\text{in}}, C_{\text{out}}, D_{\text{depth}}\), but the paper gives **no concrete algorithm** to construct these matrices. It states only: *"This mapping can be learned or defined using schemes such as random projection or interpolation, followed by normalization"* (line 160–161). This is a placeholder, not a method specification. The paper does not disclose how the transformations were actually implemented in the experiments — the method is irreproducible as written. For a paper whose core contribution is the parameter transformation + integration pipeline, this is a significant gap.

2. **Evaluation does not match the claimed use case**: The abstract and introduction frame SAIL as a method for *"leveraging knowledge from (publicly available) pre-trained models"* (line 8) such as GPT-3, PaLM, etc. However, every experiment trains models from scratch on artificially partitioned subsets of the same dataset (OpenWebText split by mean token value, CIFAR-10 partitioned by feature similarity). The cross-dataset experiment (OpenWebText → WikiText-103) still uses models trained on OpenWebText partitions. The vision experiments explicitly state *"we pre-train ResNet models using both supervised and self-supervised learning paradigms"* — again from scratch. The **claimed scenario** (grabbing existing checkpoints from diverse sources with different architectures, training data, and objectives) is never tested. This disconnect between motivation and evaluation undermines the paper's claims about practical applicability.

3. **Theoretical guarantees (Theorem 1) do not apply to the experimental setting**: Section 3.2 explicitly states: *"We concentrate on linear models, assuming that all pre-trained models share an identical architecture"* (line 129). Yet the experiments use deep nonlinear networks (GPT-2 with self-attention, ResNets with convolutions and batch normalization). The paper provides **no bridging argument** connecting the linear theory to the nonlinear experiments — no discussion of neural tangent kernels, PAC-Bayes, or any other framework. No empirical validation of the theoretical bounds is provided. The theory is effectively ornamental to the claimed contributions.

4. **Insufficient empirical evaluation**:
   - **Limited training**: The NLP experiments use only 50–200 training steps (Section 4.4) on a 21M-parameter GPT-2. This is far too few steps to demonstrate meaningful "accelerated training" for language models.
   - **No error bars or statistical significance**: All results (Figures 2a–d, Figures 3a–c) are presented as single runs without confidence intervals, standard deviations, or any measure of variability, making the results uninterpretable.
   - **Missing critical baselines**: The paper compares only against random initialization and undefined *"baseline transformation methods"* (line 263). There is no comparison to: training from scratch on the combined dataset \((D_1 \cup D_2 \cup D_t)\), standard transfer learning (fine-tuning a single pre-trained model), Model Soup (Wortsman et al., 2022), or any existing model merging method cited in the related work. 
   - **No compute measurements**: Despite emphasizing computational efficiency as a primary motivation, the paper reports no wall-clock time, FLOPs, energy consumption, or training duration. Figure 3 shows accuracy curves with no axis labels for training steps/epochs.
   - **"Baseline transformation methods" never defined**: The paper repeatedly claims SAIL outperforms *"baseline transformation methods"* but never specifies what these are.

### Minor

5. **TV→MMD substitution made without justification (Section 4.4)**: Theorem 3 is derived in terms of total variation (TV) distance between distributions, but the experiments compute \(\gamma^*\) using Maximum Mean Discrepancy (MMD): *"we compute the theoretical optimal \(\gamma^*\) using the Maximum Mean Discrepancy (MMD) distances between datasets"* (line 233). The paper provides **no theoretical justification** for this substitution or discussion of when MMD is a valid proxy for TV distance. The MMD kernel choice and estimation details are also absent.

6. **Handling of non-weight parameters not addressed (Section 4.1)**: The transformation section discusses weight matrices but does not clarify how biases, batch normalization running statistics, layer norm parameters, positional embeddings, or layer-specific structures (e.g., Q/K/V matrices in attention) are handled. This level of detail is essential for reproducibility.

7. **No analysis of failure cases**: All experiments show SAIL outperforming the baseline. There is no discussion of conditions under which parameter averaging might degrade performance (e.g., models trained on very different tasks, large architecture gaps, or conflicting learned representations). This makes the claims feel one-sided.

### Trivial
None.

## Nice-to-Haves

- Reporting wall-clock time to reach a given performance level would substantially strengthen the efficiency claims.
- Comparing against training on the full combined dataset \((D_1 \cup D_2 \cup D_t)\) would provide a natural upper bound and strengthen the paper's argument for why SAIL is beneficial over simply pooling data.
- The paper could benefit from a clear statement of how the transformation matrices (\(C_{\text{in}}, C_{\text{out}}, D_{\text{depth}}\)) were instantiated in the experiments (e.g., exact interpolation scheme used).
- A brief discussion of how the linear-model theory might relate to the nonlinear experimental setting (e.g., via the NTK regime or as a boundary-case intuition) would bridge the current gap.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

1. **Criticism that Theorem 3 requires prohibitively expensive TV distance computation**: The TV distances are between datasets (distributions), between dataset pairs — this is \(O(n^2)\) in the number of datasets. For the n=2 case used in experiments, this is trivial. For large n, the matrix inversion is \(O(n^3)\) which is still manageable. This criticism overstates the computational burden.

2. **Criticism that "the t-SNE visualization shows three clusters" (implying the partitioning is artificial)**: The paper acknowledges the partitioning is synthetic (it was created for controlled evaluation). The t-SNE visualization is provided to confirm that the partitioning did create distinct distributions as intended. This is standard experimental practice, not a flaw.

3. **Criticism about missing code**: The abstract states code will be made publicly available, which is standard for a submission. The primary issue is that the method specification (not code availability) makes the paper irreproducible.

4. **Criticism that Theorem 3 requires the true target distribution \(D^*\) which is unknown**: This is understood — the paper substitutes empirical datasets for distributions, which is the standard practice in statistical learning theory when applying such results. The substitution of MMD for TV is a separate concern (see Weakness #5).

5. **Strength about "systematic analysis of data overlap effects" being a core strength**: This is retained as a supporting strength (Strength #4) but is not among the core theoretical contributions.

## Novel Insights

The most interesting finding from the reviews is the tension between the paper's clean theoretical formulation (especially the closed-form optimal weights in Theorem 3, validated empirically via MMD substitution) and the substantial gap between that theory and the actual experimental setup. This gap — linear theory applied to nonlinear networks, TV-distance formulas computed via MMD, claimed public-model reuse tested only on self-trained models — is the paper's central weakness but also a potential path forward. The theoretical core (optimal weighted combination of transformed pre-trained parameters) is a genuinely novel idea that could be made rigorous with appropriate bridging arguments (e.g., NTK-based justification for the linear approximation, PAC-Bayes bounds for transfer). What is missing is not the idea itself but rather the verification chain connecting the mathematical claims to the experimental evidence.

## Suggestions

1. **Specify the transformation concretely**: Provide an exact algorithm for constructing \(C_{\text{in}}, C_{\text{out}}, D_{\text{depth}}\) (e.g., the interpolation scheme or projection used in the experiments). Without this, the method cannot be reproduced or built upon.
2. **Add critical baselines**: Compare against training on the combined data \((D_1 \cup D_2 \cup D_t)\), against standard transfer learning from one pre-trained model, and against Model Soup / Task Arithmetic.
3. **Report error bars and compute time**: Run experiments with multiple seeds and report standard deviations. Report wall-clock training time or steps-to-target-loss.
4. **Bridge theory and experiments**: Either extend the theory (e.g., using NTK to justify linear approximation in the lazy training regime) or explicitly reposition the linear theory as intuition-building while adding empirical validation of the bounds on the actual nonlinear models.
5. **Test the claimed scenario**: Even at small scale, demonstrate SAIL using actual publicly available checkpoints (e.g., HuggingFace GPT-2 variants trained on different data) rather than self-trained models on artificial partitions.
6. **Scale up**: Demonstrate the method on larger models (e.g., GPT-2 Medium/Large) with more training steps to make the "accelerated training" claim credible.
