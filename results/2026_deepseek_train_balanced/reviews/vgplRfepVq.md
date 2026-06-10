## Summary

This paper proposes Gradient Inversion Transcript (GIT), a generative approach for reconstructing training data from leaked gradients in distributed/federated learning. The key innovation is constructing the threat model's architecture adaptively by translating the leaked model's backpropagation equations into a neural network structure (via derived formulas involving pseudoinverses), rather than using a fixed architecture (MLP/UNet) as prior generative methods do. Two variants are introduced: FineGIT (parametrizing the weight matrices based on the derived formulas) and CoarseGIT (using MLPs to approximate each reconstruction step). Experiments on CIFAR-10 with LeNet and ResNet architectures show GIT outperforming both DLG (gradient matching) and fixed-MLP generative baselines across most batch sizes and settings.

## Strengths

- **Adaptive architecture design grounded in the leaked model's structure**: Unlike prior generative approaches that use a fixed MLP or UNet regardless of the model under attack, GIT constructs its threat model by translating the leaked model's backpropagation into a neural network (Sections 3–4, Equations 4 and 6, Figure 1). This structural correspondence is the paper's core contribution, and the empirical results in Table 3 confirm that GIT consistently outperforms the fixed-MLP baseline, validating the advantage of an adaptive architecture.

- **Superior reconstruction over gradient matching for batch sizes > 1**: GIT maintains competitive reconstruction quality as batch size increases, while DLG's performance degrades significantly (Table 3). The paper honestly reports the one exception (LeNet, batch size 1, where DLG nearly perfectly recovers the input), which is expected given DLG's access to per-instance online optimization. For the practically more challenging multi-instance setting, GIT's offline generative approach proves advantageous.

- **Robustness to noisy gradients**: Section 5.2 shows that GIT maintains MSE ~0.01 even when Gaussian noise with std 0.1 is added to gradients, while DLG's reconstruction fails entirely at noise std 0.01. This is a practical advantage since gradient perturbation is a standard defense against leakage.

- **No label information or model parameter access required**: The paper's threat model (Section 1) explicitly forgoes assumptions common in gradient matching work — no knowledge of labels, no access to the backpropagation process, and no global model parameters — making the setting more realistic for distributed learning scenarios.

- **Theoretical extension to skip connections**: Section 3.3 derives Equation (6) extending the reconstruction framework to ResNet-style architectures with shortcut connections, going beyond simple feedforward networks.

## Weaknesses

### Major

- **Overstated "theoretically grounded" claim with mathematically unsubstantiated derivation**: The paper's central distinguishing claim is that GIT is "theoretically grounded" (Abstract, Contributions). However, the derivation from Equation (2) to Equations (3)-(4) relies on pseudoinverse manipulations of tensor operations (⊗, ⊙) whose algebraic properties are never established. The definition of a tensor pseudoinverse as "the Moore-Penrose inverse of each of its subspace via the first dimension" (line 62) is non-standard, and the paper does not verify the conditions under which the inversion formula holds (e.g., full rank conditions needed for (AB)⁺ = B⁺A⁺). The method's empirical success does not depend on exact inversion — FineGIT treats weight matrices as learnable parameters, and CoarseGIT replaces pseudoinverses with MLPs — so the approach is better described as "theory-inspired architectural design" rather than "theoretically grounded reconstruction." This overclaim is significant because the paper frames theoretical grounding as what distinguishes GIT from prior "empirical" work.

- **Overfitting acknowledged but unresolved, limiting practical utility**: The paper states (line 137) that training MSE "can drop below 0.005 while the test loss demonstrated in Table 3 is significantly larger" and attributes this to "insufficient training data and lack of regularization schemes," deferring the problem to future work. While the method does generalize to test data (it outperforms baselines on the test set), the large train-test gap means the generative model partially memorizes input-gradient pairs rather than learning a truly general inversion function. This is not a fatal flaw (the critic's claim that the method "does not generalize" is contradicted by the paper's own test-set results), but it is a significant limitation for a method whose practical value depends on reconstructing unseen gradients — and the paper's deferral to future work leaves it unaddressed.

### Minor

- **Only two baselines compared, excluding cited generative methods**: The paper compares against DLG and a fixed-MLP generative model (Wu et al., 2023). However, it cites Pan et al. (2020) and Huang et al. (2021) as generative methods in the related work but does not include them as baselines. The justification that "both achieve competitive performance in their respective category" (line 130) does not explain why these other generative methods are absent. Including at least one additional generative baseline would strengthen the evaluation.

- **Evaluation on a single dataset (CIFAR-10)**: All quantitative experiments use CIFAR-10. No results on CIFAR-100, Tiny ImageNet, or higher-resolution images are presented. The brief mention of higher-resolution results (line 145) does not provide actual data. This limits support for the paper's claim of being a "generic" framework applicable to diverse settings.

- **Only MSE is reported as a quantitative metric**: For image reconstruction quality, MSE alone is a weak indicator. SSIM, LPIPS, or classification accuracy on reconstructed images would provide a more informative assessment of reconstruction fidelity. The paper mentions PSNR in Table 2's caption but does not report actual PSNR values in the main results.

- **Unclear which variant (FineGIT vs. CoarseGIT) is used in main experiments**: The paper introduces FineGIT (follows the derived formulas with trainable {W_i}) and CoarseGIT (MLPs replacing each step) in Section 4, noting that FineGIT is more principled but numerically unstable while CoarseGIT is more flexible. However, the main experiments (Section 5) refer only to "GIT" without specifying which variant is deployed. The Section 5.5 experiment on FineGIT (Figure 3) uses a tiny "leaked model with two convolutional layers," which is not representative of the main evaluation. This ambiguity hinders reproducibility and interpretation of results.

- **Inconsistent default training data size**: The paper states "one-tenth of the training data, which consists of 5,000 samples" (line 128) as the default, but Table 2's caption says "We use 10000 samples to train generative models." Section 5.3 experiments with 1,000, 5,000, and 10,000 samples, but the inconsistency in the stated default is confusing.

- **No error bars or variance estimates**: None of the reported results include variance or confidence intervals, making it difficult to assess the statistical reliability of the reported improvements.

### Trivial

- The tables in the extracted text are embedded as raster images, making it difficult to read exact numerical values in this format.

## Nice-to-Haves

- Ablation study comparing FineGIT vs. CoarseGIT on the main benchmarks would clarify which variant drives the reported performance and under what conditions each is preferable.
- Additional metrics (SSIM, LPIPS) would strengthen the evaluation of reconstruction quality.
- Experiments on an additional dataset (e.g., CIFAR-100 or Tiny ImageNet) would support the claim of generality.

## Removed Points

**These points are flagged to be removed; treat them with caution.**

- *"Tables are unreadable images — central quantitative evidence unverifiable"*: This is a PDF extraction artifact; the original submission's tables are proper text tables. Removed as a formatting artifact per the filtering rules.

- *"The method does not generalize to unseen gradients / only retrieves training samples"*: This claim (made by the harsh critic) contradicts the paper's own test-set results showing GIT outperforms baselines. The paper acknowledges overfitting but does demonstrate generalization. Removed as factually incorrect.

- *"Missing gradient matching baselines (Geiping et al., 2020; Yin et al., 2021; Chen & Vikalo, 2024)"*: These methods operate under different threat model assumptions (label access, model query ability). DLG is a representative gradient matching baseline. Removed as scope creep.

- *"No code/model release mentioned"*: Code release statements are typically in a separate section that may have been stripped during parsing. Removed per rules about stripped sections.

- *"Training hyperparameters not disclosed"*: Removed as a reproducibility nitpick per filtering rules.

- *"Reproducibility concerns about model availability"*: Removed per hard rules — all cited models are assumed to exist.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension that the reviews themselves do not resolve: the paper's claimed "theoretical grounding" is technically overstated, yet the core idea (using the leaked model's backpropagation structure to design an adaptive generative threat model) is genuinely novel and empirically validated. This is a paper where the contribution is stronger than the justification given for it, and the reviews correctly identify the gap between the claimed rigor and the actual derivation, but do not produce an independent insight beyond this observation.

## Suggestions

- **Temper the theoretical claims**: Reframe the derivation as an architectural template inspired by backpropagation rather than as a rigorous mathematical inversion. Drop or qualify the "theoretically grounded" language. The empirical results are strong enough to stand on their own.
- **Address overfitting explicitly**: Since the paper identifies overfitting as a known limitation, the experiments should include at least one attempt to mitigate it (e.g., data augmentation, regularization, or a simple early stopping analysis) rather than deferring entirely to future work.
- **Specify which variant is used where**: Clearly state whether FineGIT, CoarseGIT, or a combination is used in each experiment, and include a comparative analysis between the two variants on a representative setting.
- **Add at least one more baseline**: Include Pan et al. (2020) or another generative method cited in the paper.
- **Report additional metrics**: SSIM or reconstruction-based classification accuracy alongside MSE.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>