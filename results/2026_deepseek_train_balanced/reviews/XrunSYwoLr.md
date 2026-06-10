## Summary

This paper proposes Spatio-Temporal Approximation (STA), a pipeline for converting pretrained ANN Transformers (specifically CLIP ViT-B/32) into purely event-driven SNNs. It introduces Universal Group Operators (UGOs) that approximate nonlinear operations (GELU, sqrt, exp) by training small ReLU networks on synthetic data and then converting them to spiking neurons, and a Temporal-Corrective Self-Attention Layer (TCSA) that uses an estimation-correction mechanism to handle non-causal variable-variable multiplications in self-attention. The paper provides theoretical error bounds for both components and demonstrates zero-shot and fine-tuned classification on several benchmarks.

## Strengths

1. **First conversion pipeline for pretrained Transformers to purely event-driven SNNs.** Prior ANN-to-SNN conversion was limited to CNNs, and existing spiking Transformers required training from scratch. Converting a pretrained ViT-B/32 from CLIP without task-specific training is a genuine first. The TCSA mechanism for handling non-causal self-attention multiplications (Section 5.2) addresses a real problem that prior conversion work could not, because it focused on CNNs where this issue does not arise.

2. **TCSA estimation-correction mechanism with formal guarantees.** The temporal approximation for non-causal multiplications is the most technically novel component. Theorem 2 establishes unbiased estimation at every time step (\(\mathbb{E}[\Psi(t)] = AB\)), and Theorem 3 provides a quadratic convergence rate of the estimation error (\(\mathbb{D}\{\Psi(t)\} \propto (1/t - 1/T)^2\)). The mechanism ensures that all computations reduce to Boolean ANDs and weighted additions, preserving the event-driven nature.

3. **Decomposed theoretical error bound for spatial approximation.** Theorem 1 provides a three-term error decomposition (empirical gap, parameterization gap, quantization gap) with known scaling behavior — e.g., the parameterization gap scales as \(\mathcal{O}(\mathcal{L}_f |y|_{\max} / N^2)\) and the quantization gap as \(\|w_1|x|_{\max}+b_1\|_\infty \cdot \|w_2\|_1 / T\). The authors derive concrete implementation guidelines (layer-specific regularization, principled hyperparameter search balancing the three competing dependencies on \(N\)) from this analysis, going beyond the heuristic threshold-balancing typical of prior conversion work.

## Weaknesses

### Fatal
None.

### Major

1. **Original ANN ViT baseline accuracy is never reported.** The paper repeatedly claims "much lower accuracy drop after conversion" (line 265) and "small accuracy gap to ANN ViT" (line 274), but nowhere in the text are the original CLIP ViT-B/32 accuracy numbers given for any benchmark. The tables (embedded as images) may contain these numbers, but the text provides no reference to specific ANN ViT accuracies. Without this baseline, the conversion loss cannot be assessed — the reader cannot determine whether the converted SNN retains 95% or 70% of the original model's performance. This is the single most important experiment for evaluating a conversion method.

2. **No comparison against existing spiking Transformer methods.** The paper cites Spikingformer (Zhou et al., 2022) and the fully event-driven Transformer (Zhou et al., 2023) in Section 2.2 as alternatives that "differ from ANN Transformers structurally and require training from scratch." These are directly comparable approaches for obtaining a Transformer-based SNN. Without any experimental comparison against them (even on a single benchmark like CIFAR-100), the paper's positioning relative to existing work is unsubstantiated. If these methods significantly outperform the converted model, the contribution is different from what is claimed; if STA is competitive, that would strengthen the paper.

3. **Ablation studies are described only qualitatively, with no numerical results reported.** The ablation discussion (Section 6.3, lines 279–284) states that "UGO nearly eliminates the three Gaps" and "significantly improving performance over the naive method," but no accuracy numbers, error values, or other quantitative metrics are provided in the text. The ablation figure (Fig. 6) is an embedded image whose numerical content cannot be verified from the text. For a paper whose contributions include theoretical error bounds and guidelines for hyperparameter selection, the complete absence of quantitative ablation results is a significant gap.

### Minor

1. **"Training-free" framing is imprecise.** The title and contributions call this a "training-free pipeline," but Section 4.1 (lines 117–119) explicitly trains small ANNs (UGOs) on synthetic data. The paper is transparent about this, and the distinction from task-specific training is meaningful. However, in the ANN-to-SNN conversion literature cited by the paper itself (Diehl et al., 2015; Rueckauer et al., 2017; line 36), "training-free" means no gradient-based optimization of any kind. The UGOs require training; calling the pipeline "task-training-free" or "without task-specific training" would be more accurate and would avoid inviting the very criticism the harsh reviewer leveled.

2. **Standard classification comparison confounds fine-tuning status.** Section 6.3 (line 274) compares fine-tuned STA ViT against "pretrained ResNet-50 baselines from CLIP." If the ResNet baselines are not fine-tuned on the same benchmarks while the proposed method is, the comparison systematically favors the proposed method. The paper does not clarify whether baselines receive the same fine-tuning protocol, making it impossible to attribute the reported gains to the conversion method rather than the fine-tuning.

3. **No ImageNet-1K evaluation.** The paper evaluates on CIFAR-10/100, CIFAR-10.1/10.2, and ImageNet-200. ImageNet-1K is the standard benchmark for vision models. Its absence limits the generalizability claims, particularly given the use of a CLIP-pretrained model that was designed for large-scale tasks.

### Trivial
- In Eq. 1, $T$ is used for both the number of layers and the number of time steps, which is potentially confusing.

## Nice-to-Haves
- Reporting UGO approximation error on held-out synthetic data (MSE between UGO and true function) would directly validate the spatial approximation quality and connect the theoretical bound to practice.
- Analyzing how TCSA affects downstream attention patterns compared to the original ANN's softmax would strengthen the temporal claims.
- A more detailed decomposition of how Softmax (exponentiation + normalization) is implemented via UGOs + multiplications would aid reproducibility.

## Removed Points
These points were considered but removed from the main weaknesses with justification:

1. **"No readable quantitative results"** — The tables (Table 1, Table 2) are present in the original PDF as embedded images. The parser cannot extract text from images, making this a parsing artifact rather than a paper defect. The criticism about missing ANN ViT baseline (retained as Major #1 above) is distinct and valid.

2. **"Unfair zero-shot comparison (ViT vs ResNet)"** — This comparison demonstrates the value proposition of converting Transformers (which prior methods could not do). The paper is not claiming superior conversion quality over other ViT conversion methods (there are none); it is showing that converting Transformers yields better results than converting CNNs, justifying the need for the method. This is a reasonable framing for a first-of-its-kind result.

3. **"UGO is a straightforward application of known techniques, not novel"** — This is a subjective value judgment that understates the contribution. Applying universal approximation + ANN-to-SNN conversion to the specific operations in Transformers, combined with the novel three-term error decomposition (Theorem 1) and derived regularization, constitutes non-trivial work. The theoretical analysis goes beyond what prior "threshold balancing" approaches provided.

4. **"Theoretical analysis rests on strong, unvalidated assumptions"** — The paper explicitly states the independence assumption for Theorem 3 (line 228: "for clarity, we assume all elements are independent"). This is a standard simplifying assumption in theoretical analyses and is not presented as an empirical claim. The paper does not assert that Theorem 3's quantitative expression holds exactly in practice; it provides insight into the mechanism's convergence behavior.

5. **"Softmax implementation not described"** — Section 4.2 describes the decomposition approach for high-dimensional operations like LayerNorm and Softmax via integration of basic spiking operations (weighted addition, UGO, multiplication). The description is at the level of a methodology outline, and greater specificity would be helpful (noted in Nice-to-Haves), but it is not absent.

6. **"Energy analysis ignores system-level costs"** — The energy estimation follows standard methodology from Rathi & Roy (2020) that is widely used in the SNN literature. Isolating operation-level energy comparisons is the norm in this field, not a flaw.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Report the original ANN ViT-B/32 accuracy on every benchmark** alongside the converted SNN results, so conversion loss is transparent to the reader. This is the single most important missing piece.
2. **Include at least one comparison against a directly-trained spiking Transformer** (e.g., Spikingformer on CIFAR-100) to contextualize the quality of the converted model relative to the alternative paradigm.
3. **Add quantitative ablation tables** showing accuracy with/without UGO, with/without TCSA, and across varying N and T values. Report the numerical values in the text or in a machine-readable table.
4. **Rephrase "training-free" to "task-training-free" or "without task-specific training"** in the title and framing to accurately reflect the method's relationship to training.
5. **Clarify the fine-tuning protocol for all baselines** in the standard classification experiments to ensure the comparison is fair.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>