Now I have sufficient information. Let me produce the final consolidated review.

## Summary

The paper introduces VLOOD, a backdoor attack method for Vision-Language Models (VLMs) that operates under the realistic constraint that the attacker lacks access to the original training data and must instead rely on Out-Of-Distribution (OOD) public data (e.g., 3000 image-text pairs). The method comprises three technical components — Clean Knowledge Preservation (CKP, a KL-divergence distillation from the benign model), Conceptual Consistency Preservation (CCP, an L1-distance constraint on token embeddings for poisoned samples), and dynamically adjusted weights to balance clean/poisoned training — designed to simultaneously achieve high attack success rates while preserving the semantic quality of generated text. Experiments span three VLM architectures (BLIP-2, MiniGPT-4, InstructBLIP) on image captioning (Flickr8k, Flickr30k, COCO) and VQA (OK-VQA, VQAv2), with results showing VLOOD maintains clean-input utility (ASR ≈ 0 on clean inputs) and high poisoned-input ASR (≥ 0.997) while preserving conceptual consistency far better than six baselines.

## Strengths

1. **Novel and practical problem formulation.** The paper is the first to systematically address backdooring VLMs under the realistic assumption that the attacker has no access to the original training data and must operate with OOD public data (Sec. 3.1). Prior VLM backdoor attacks (Shadowcast, AnyDoor, VL-Trojan, etc.) all assume access to original training data, as the paper explicitly delineates in Sec. 2 (Related Work). This gap is well-motivated and timely.

2. **Comprehensive evaluation covering multiple architectures, tasks, and datasets.** VLOOD is tested on BLIP-2, MiniGPT-4, and InstructBLIP; on image captioning (Flickr8k, Flickr30k, COCO) and VQA (OK-VQA, VQAv2); and against six baselines (BadNet, Blended, Poisoning, BadEncoder, Shadowcast, AnyDoor). Results are reported with multiple metrics (B@4, METEOR, ROUGE-L, CIDEr, ASR, VQA score). This breadth convincingly demonstrates cross-architecture generalization.

3. **Individual component ablation (Table 1) justifies the three-component design.** The paper shows that using only the default LM loss ("Default") yields high clean-input ASR (0.627); adding CKP alone washes out the backdoor entirely (ASR 0.000 on both CI and PI); adding CCP alone causes false triggers on clean inputs (ASR 0.852); and dynamic weights alone fails on clean inputs (ASR 0.000 CI but 0.999 PI). Only the full VLOOD combination achieves ASR 0.000 on CI and 0.999 on PI with strong conceptual consistency — directly supporting the claim that all three components are necessary.

4. **Robustness to data size, trigger size, and existing defenses.** Ablations (Table 5) show stable performance across 1000–5000 training samples and trigger sizes 10–30px. The defense evaluation (Table 4) shows both Spectral Signatures and Beatrix fail to meaningfully detect VLOOD's poisoned samples, which the paper correctly attributes to the mismatch between classification-oriented defenses and generative image-to-text tasks.

## Weaknesses

### Fatal
None.

### Major

1. **The dynamically adjusted weight λ is critically underspecified.** The update rule λ = λ + (Impact_clean − Impact_poisoned) is given (Eq. 6), and the overall loss uses λ as a mixing weight (Eq. 7), but the paper never states: (a) the initial value of λ, (b) whether λ is bounded or clamped to [0,1] (which the mixing equation (1−λ) and λ implicitly requires), or (c) how the "impacts" — which are sums of per-token cross-entropy scores across a batch — are normalized to prevent λ from exploding or oscillating. Since Impact_clean and Impact_poisoned are sums over different token sequences, their scale depends on vocabulary size, batch size, sequence length, and the training epoch, making the raw update magnitude arbitrary. Without these details, this central balancing mechanism cannot be reproduced, and its claimed convergence is unverifiable.

2. **The OOD training data source is not stated in the main text.** The paper says "To achieve OOD training, we train the backdoored model on one dataset and evaluate it on another. Details can be found in Appx." (Sec. 4.1). The main text never identifies which specific dataset is used as the OOD training source for each evaluation target (e.g., for the Flickr8k column in Table 2, is the model trained on COCO data? On web-scraped data? On a random subset of some other corpus?). The reader cannot interpret the experimental results without knowing what "OOD" means concretely. While the appendix likely contains this information, the main text should state it explicitly, as this is the paper's central experimental variable.

### Minor

3. **The baseline comparison conflates VLOOD's advantage with the benefit of auxiliary losses.** VLOOD's CKP and CCP losses provide additional supervision signals (preserving clean output distributions, constraining poisoned-token embeddings) that none of the six baselines employ. An attacker using BadNet or AnyDoor could conceivably add CKP and/or CCP. However, the paper partially addresses this through the ablation in Table 1, which shows that the "Default" approach (standard LM loss, which is the core of most baselines) fails when given CKP alone (ASR collapses to 0) or CCP alone (high false-positive ASR). Only VLOOD's full combination succeeds. While a direct test of, e.g., BadNet+CKP+CCP would further strengthen attribution, the existing ablation provides reasonable evidence that the benefit arises from the combination, not simply from adding losses. This concern is substantive but not fatal.

4. **Several baselines exhibit catastrophic utility degradation, making the comparison less informative.** BadEncoder achieves B@4=0.0 and CIDEr=0.0 on both clean and poisoned inputs across all datasets (Table 2); Shadowcast and Blended drop to CIDEr≈6.9 on poisoned inputs. These baselines are essentially non-functional under OOD conditions, so outperforming them on conceptual consistency is a low bar. The paper's central claim — that VLOOD "enhances conceptual consistency preservation over baselines" — is supported, but the contrast with collapsed baselines is not surprising. A more informative comparison would report baseline performance under in-distribution training to quantify the gap that OOD conditions create.

5. **The defense evaluation is thin.** Only two defense methods (Spectral Signatures and Beatrix) are tested, and both are acknowledged to be designed for classification tasks rather than image-to-text generation. The paper correctly notes that VLM-specific defenses do not yet exist, but the evaluation would be strengthened by also testing against more general data-poisoning detection methods (e.g., activation clustering, STRIP adapted to generative outputs) or by implementing a simple baseline defense adapted from the classification domain.

6. **The CKP-induced "backdoor washing" (ASR=0.000) is an interesting phenomenon left unexplained.** When CKP is added to the default LM loss, the model not only preserves clean behavior but *completely* eliminates the backdoor (Table 1, Default+CKP row: ASR 0.000 on poisoned inputs). The paper notes this is "overly strong" and motivates CCP, but provides no analysis of why CKP completely suppresses the backdoor — e.g., whether this arises from gradient conflict, representational collapse, or the distillation loss dominating the LM loss. Understanding this mechanism would strengthen the paper's scientific contribution.

### Trivial
None.

## Nice-to-Haves

- Including baselines under *in-distribution* training conditions would quantify the penalty that OOD mismatch imposes, providing a stronger reference for VLOOD's improvement.
- A brief analysis of λ's trajectory over training (e.g., a plot of λ values across epochs) and its sensitivity to initialization would resolve the underspecification concern.
- Reporting the specific OOD dataset source in the main text (not just in the appendix) would make the paper self-contained.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"ChatGPT evaluation results are not shown in the main text"** — The paper explicitly states "Please refer to Appx. for the detailed prompt and results." This content exists in the appendix of the original submission but was stripped by the PDF parser. The criticism reflects a parser artifact, not an author omission.

2. **"The paper claims 'We are the first to explore backdooring VLMs … using OOD data' without clearly distinguishing from related work"** — The paper explicitly distinguishes itself in Sec. 2 (Related Work): "Other methods… assume that attackers have access to the original training data, which is often unrealistic. Our study addresses this gap." The delineation is clear and the claim is substantiated.

3. **"Defense discussion transitions to a general statement about the lack of existing defenses, which does not strengthen the paper"** — The paper provides a substantive discussion of why the tested defenses fail (no fixed target class in generation tasks, representations in text space vs. image space). This is a valid and informative analysis, not a generic hand-wavy statement.

4. **"The paper does not include any ablated version of a baseline with CKP or CCP"** — This is factually incorrect. Table 1 (tab:default_and_mine) provides exactly this: "Default + CKP," "Default + CCP," "Default + Dynamic" are the baselines augmented with VLOOD's individual components. The "Default" method uses the same LM loss that forms the backbone of most baseline attacks.

5. **"Testing Spectral Signatures and Beatrix is a strawman"** — The paper explicitly acknowledges these defenses are designed for classification and are the closest available methods. The paper is transparent about the absence of VLM-specific defenses. Evaluating against available methods is standard practice, not a strawman.

6. **Various formatting/style nitpicks and parser artifacts** — Removed per instructions.

## Novel Insights

The reviews surface one genuine insight beyond the paper's own contributions: the "backdoor washing" phenomenon where CKP alone drives ASR to exactly 0.000 on poisoned inputs (Table 1) is a striking empirical result that the paper notes but does not explain. This might indicate a fundamental tension between knowledge-distillation-based preservation and backdoor retention — possibly because the distillation loss enforces distributional alignment across *all* inputs (including poisoned ones but through the lens of the clean teacher), which conflicts with the model learning a distinct trigger-dependent output distribution. Understanding this mechanism could inform both attack and defense design for generative models.

## Suggestions

1. **In the main text, explicitly state which dataset is used as the OOD training source for each evaluation target** (e.g., "For the Flickr8k evaluation, we train on COCO images; for the OK-VQA evaluation, we train on VQAv2 images"). This is the single most important clarification needed.
2. **Specify the initial value of λ, add clamping to [0, 1], and describe how the cross-entropy impacts are normalized** (e.g., by sequence length or softmax temperature) to make the dynamic weighting mechanism reproducible and well-defined.
3. **Add a brief analysis of why CKP alone eliminates the backdoor entirely** — even a paragraph offering a hypothesis (gradient conflict, distillation dominance) would significantly strengthen the paper.
4. **Report baseline performance under in-distribution training** as a separate column/table to isolate the effect of OOD mismatch from the attack's inherent capability.

## Score and Decision

Based on the paper's novelty (first OOD backdoor for VLMs, practical problem formulation), the soundness of its three-component approach (supported by ablation showing each component's necessity), the breadth of evaluation (3 architectures, 2 tasks, 5 datasets, 6 baselines), and the significance of the security issue it reveals, I assess the paper as a solid contribution. The major weaknesses — underspecification of the dynamic λ mechanism and the absent OOD data source disclosure in the main text — are addressable in revision and do not invalidate the core claims. The paper has real contributions and the evaluation, while imperfect, supports its main findings.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>