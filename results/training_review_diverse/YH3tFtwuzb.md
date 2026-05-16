Here is my final consolidated review.

---

## Summary

This paper proposes DP-BiTFiT, a differentially private fine-tuning method that trains only the bias terms of pre-trained models. The core insight is that bias gradients have a special computational structure (they do not require input activations for their computation), which eliminates the need for per-sample weight gradient storage and forward-activation caching that burden other DP fine-tuning methods. The paper provides a complexity analysis demonstrating that DP-BiTFiT's DP overhead is independent of the feature dimension \(T\), and validates this empirically across NLP and vision tasks, showing competitive accuracy with 2–30× speedup and 2–8× memory reduction relative to DP full fine-tuning.

## Strengths

- **Parameter efficiency across diverse architectures (Table 1):** DP-BiTFiT trains only ~0.1% of total parameters for models ranging from VGG16 (0.009%) to ViT-large (0.090%) and GPT2-large (0.066%), a fraction 10–1000× smaller than competing DP PEFT methods (e.g., LoRA at 0.94% for RoBERTa-base).

- **Computational overhead independent of feature dimension \(T\) (Table 2, Figure 3):** The complexity analysis shows DP-BiTFiT's additional DP overhead is only \(+3Bp\) (time) and \(+Bp\) (space), with no dependence on \(T\), whereas all weight-based DP methods have overhead linear or quadratic in \(T\). This is validated empirically in Figure 3, where DP-BiTFiT's memory and time remain nearly constant as sequence length grows, while other methods increase sharply.

- **Competitive accuracy under DP, matching or exceeding SOTA (Tables 3–6):** On RoBERTa-large (Table 3), DP-BiTFiT matches or exceeds DP full fine-tuning on multiple GLUE tasks (SST2: 94.5% vs. 93.8%). On GPT2-large (Table 4), it achieves BLEU 65.21 vs. 64.64 for DP full at \(\epsilon=8\). On CIFAR10 with ViT-large (Table 5), it reaches 99.0% at \(\epsilon=2\). The gap between DP-BiTFiT and DP full fine-tuning consistently shrinks as model size increases (Remark 4.1).

- **Memory/speed advantages enabling previously infeasible tasks (Figures 3, 4):** DP-BiTFiT supports a 70× larger batch size and 3× higher throughput on ResNet152 with 512×512 images compared to DP full fine-tuning, and 3× less memory on RoBERTa-large/MNLI.

- **First rigorous complexity analysis for DP PEFT:** Table 2 provides a per-layer time/space complexity breakdown for DP full, LoRA, Adapter, and BiTFiT, filling a gap in prior DP and non-DP PEFT literature and formally deriving the 1.5× speedup over non-private full fine-tuning and 2× over DP full fine-tuning.

- **Model-agnostic design:** DP-BiTFiT applies to transformers (BERT, RoBERTa, GPT2, ViT) and CNNs (VGG, ResNet) without adding new modules or modifying architecture. For bias-free architectures, DP-BiTFiT-Add extends the method with minimal overhead.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported, and no weakness undermines its central contribution.

### Minor

- **The vision experiments train the classification head alongside biases, but the impact on the "activation-free" efficiency claims is not fully analyzed.** The paper acknowledges (line 395) that for CIFAR/CelebA, the randomly initialized classification head is trained alongside biases (adding ~100k parameters for ViT-large). However, the paper does not specify whether the head is trained with DP-SGD requiring activation storage (undoing the activation-free benefit for that single layer). While the efficiency impact is likely negligible given the head is one layer out of hundreds, the lack of explicit analysis leaves a gap in the empirical support for the claimed memory/time savings on vision tasks. The authors should clarify the head's training protocol and quantify its contribution.

- **No error bars or variance estimates are reported for accuracy results.** Across all tables, accuracy differences of 0.1–0.8% (e.g., CIFAR10 ViT-large at \(\epsilon=2\): 99.0% vs. 98.9%) are presented without standard deviations or confidence intervals. Given that hyperparameter tuning may not have been identical across methods, these small gaps could be within noise. Reporting at least one repeat or confidence interval would strengthen the "on par with SOTA" claim.

- **The "2∼30× faster and 2∼8× less memory" range in the abstract is sweeping and underspecified.** These numbers are substantiated in the experiments (Figures 3, 4), but presenting such a wide range without anchoring conditions in the abstract reduces precision. A qualified statement (e.g., "depending on model size, sequence length, and batch size") would be more informative.

- **The DP-BiTFiT-Add extension (Section 3.4) is underdeveloped.** This extension is important for architectures without biases (e.g., LLAMA, CNN+BN), but it is only briefly evaluated on ResNet18/CelebA with a small +0.4% accuracy gain. There is no analysis of how added biases interact with pre-trained representations, nor experiments on larger bias-free architectures.

- **Hyperparameter sensitivity is not reported.** The paper notes that the optimal learning rate for BiTFiT is larger than for full fine-tuning, but does not report the search range or sensitivity curves. Given that DP fine-tuning is often sensitive to learning rates, this omission makes it harder to assess the robustness of the results.

- **The "baseline comparison is somewhat dated" concern is partially valid but not severe.** The primary DP PEFT baselines (LoRA, Adapter, Compacter) are taken from Yu et al. (2021). While the paper also includes more recent DP full fine-tuning baselines (De et al. 2022, Bu et al. 2022), a brief discussion of whether newer DP-PEFT methods could close the efficiency gap would strengthen the positioning. This does not threaten the paper's contributions, as the core efficiency advantage is architecture-level, not method-level.

### Trivial

- Table 2's structure could be clarified: the "forward & output grad" column is shared across all methods, but the table's layout makes it easy to miss that the bias column only shows *additional* overhead. Adding a footnote or clarifying the column header would help.

## Nice-to-Haves

- An ablation that trains only biases but *still stores input activations* (as DP-full does) would isolate whether the memory saving comes from not storing activations versus having fewer trainable parameters, directly supporting the paper's claimed mechanism.
- A diagnostic of which bias groups contribute most to accuracy (e.g., training only certain layers' biases) would deepen understanding.
- An experiment with very long sequences (e.g., document-level NLP with \(T\approx 20{,}000\)) or very high-resolution images (e.g., 1024×1024) would dramatically demonstrate the regime where \(T\)-independence of DP overhead becomes decisive.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Table 2 does not account for output gradient storage"* — **Removed (factually wrong).** The "forward & output grad" column explicitly includes the output gradient in its space complexity `pd + BT(p+d)` (where `BTp` is the output gradient). The paper also states that output gradients are tracked "in a just-in-time fashion" (line 117), confirming per-layer computation. The bias column only shows *additional* overhead on top of this shared baseline. The "activation-free" claim refers to input activations \(a_l\), not output gradients, which the paper distinguishes clearly (line 138).

- *"Codebase claim not verifiable"* — **Removed per hard rules.** The appendix was stripped by the parser; concerns about missing appendix content are parser artifacts, not author omissions. Citing a codebase is standard practice.

- *"The paper should compare to more methods / missing related works"* — **Removed per hard rules.** The paper's chosen baselines (Yu et al. 2021, De et al. 2022, Bu et al. 2022) are the standard and most relevant comparisons for DP fine-tuning. Demanding additional comparisons without specifying which methods is scope creep.

- *"The engineering contribution is overstated because it's just one line of code"* — **Removed.** The paper correctly notes that the engineering simplicity is enabled by the theoretical analysis establishing that *only* BiTFiT can be activation-free. The contribution is the analysis + demonstration, not the code change itself. The paper's own phrasing appropriately frames this as an engineering effort, not the primary contribution.

- *"The 'activation-free' label is an overstatement because output gradients are still needed"* — **Removed (misreading of the paper).** The paper clearly defines "activation-free" as not storing input activations \(a_l\) (Section 2, line 138: "the computation of bias gradient does not need \(a_l\)"). Output gradients \(\partial\mathcal{L}/\partial s_l\) are a separate quantity and are accounted for in the shared column of Table 2.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting observation: the paper's complexity framework is general enough to analyze *any* DP fine-tuning method's overhead, and the key insight is that the bias gradient's structure (summation over the feature dimension, removing dependence on \(T\) for per-example gradient norms) is *unique* among parameter-efficient methods. No other PEFT method (LoRA, Adapter, Compacter, prefix tuning) shares this property because they all involve weight-like tensor contractions. This suggests that the efficiency gains of DP-BiTFiT are not just incremental but structural — they stem from a fundamental property of the computation graph that cannot be replicated by simply parameter-count reduction. The reviews also highlight that the paper's main experimental gap is not in its core claims but in the precision of its reporting (variance, head-training protocol), which is addressable.

## Suggestions

1. **Clarify the vision head training protocol.** Specify whether the classification head is trained with DP-SGD requiring activation storage or whether a linear probe (frozen backbone) approach is used. If the head uses activation storage, add a sentence quantifying its marginal impact on total memory/time.

2. **Add variance estimates for key accuracy results.** Report at least one repeat (mean ± std) for the main tables, especially for comparisons where differences are < 1%.

3. **Tighten the abstract's efficiency numbers** by adding qualifiers or focusing on the most representative savings (e.g., "2× faster and 2× less memory on typical tasks, up to 30× faster on high-resolution images").

4. **Expand the DP-BiTFiT-Add evaluation** with at least one additional architecture (e.g., a bias-free transformer) and report whether the added biases converge to non-trivial values.

5. **Add an explicit note in Table 2** that the "forward & output grad" column is a shared baseline, and that the method-specific columns represent additional overhead, to prevent misreading.

## Score and Decision

This paper makes a solid contribution. The core insight (bias gradients' unique structure eliminates input activation storage and \(T\)-dependent DP overhead) is sound and well-motivated. The complexity analysis is novel and fills a gap in the DP PEFT literature. The experimental validation covers diverse architectures and tasks, and the accuracy results are competitive with or exceed SOTA. The weaknesses are limited to reporting precision (no error bars, underspecified head protocol, wide abstract range) rather than fundamental flaws. All identified issues are addressable.

Originality: Good — first to study DP-BiTFiT specifically and provide rigorous complexity analysis.
Importance: Good — addresses a practical need for efficient DP fine-tuning of large models.
Claims support: Adequate — core claims are supported; some reporting gaps weaken precision.
Soundness: Good — methodology is sound; no fatal flaws identified.
Clarity: Adequate — generally clear; Table 2 could be better labeled; abstract could be more precise.
Value: Good — the complexity analysis and empirical demonstrations will be useful to practitioners.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>