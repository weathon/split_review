I have thoroughly cross-checked all reviewer claims against the paper. Let me now produce the consolidated review.

## Summary

This paper proposes EDT, a backdoor attack method for large pre-trained vision models that is both training-free and data-free. The key idea is to inject a lightweight codebook between the encoder and downstream layers: when a trigger patch is detected at a specified location, the entire image embedding is replaced with a target image embedding, causing the model to output the attacker's desired label/caption. The codebook can also be populated with OOD→in-distribution mappings to improve domain adaptation performance as a cover for the attack. Experiments on ViT, CLIP, BLIP, and Stable Diffusion across classification, captioning, and generation tasks demonstrate the method's broad applicability.

## Strengths

- **Genuinely training-free and data-free operation.** EDT requires no access to the original training data and no parameter updates (gradient-based training). The codebook is constructed by a single forward pass through the encoder (Section 3.2). This is the paper's primary technical contribution and is convincingly demonstrated — Table 4 (tab:time) shows 0.00 hours of training time, a stark contrast to all baselines.

- **Broad applicability across architectures and tasks.** EDT is applied to ViT, CLIP-ViT32, CLIP-ResNet50 (image classification), Stable Diffusion (image generation), and BLIP (image captioning). This breadth supports the claim that the method generalizes across both vision-only and vision-language models without task-specific adaptation.

- **Clean accuracy preservation.** With the grey trigger, EDT achieves 0% ΔCA across all tested models and datasets (CIFAR-10, GTSRB, ImageNet) in Table 1. This is a non-trivial property — the codebook only fires when the trigger is detected, leaving clean inputs unaffected, and the analysis of why white triggers cause collisions (clean images naturally containing white squares, Section 4.1) is reasonable.

- **Clear formulation of a relevant threat model.** Sections 2.2–2.3 explicitly define three required properties (stealthy & model-agnostic, data-free, training-free) plus a bonus multi-trigger property, and situate the attack in a realistic weak-adversary scenario (public model download, no training data access, no fine-tuning budget). This framing usefully distinguishes the setting from traditional training-phase backdoor attacks.

## Weaknesses

### Fatal
None.

### Major

- **The claim "outperforms state-of-the-art" (Contribution 4) is misleading given the asymmetrical baseline comparison.** EDT is compared against BadNets, Fine-tune, Reprogram, and TrojanNet — all of which require access to the training data and substantial computation. These baselines operate under a fundamentally different (and more constrained-for-the-attacker) threat model. No training-free or data-free backdoor baselines are evaluated. The paper also does not report results for most baselines on CLIP models (Table 1, "—" entries), meaning for CLIP there is effectively no comparison at all. While EDT's advantages under its own threat model are real, claiming it "outperforms" methods that cannot even be applied under the same constraints is an overclaim. The absolute merits of EDT (training-free, data-free, works across models) are the real contribution, not superiority over mismatched baselines.

- **The domain adaptation / OOD improvement claim is insufficiently supported.** The method for OOD codebook entries (Section 3.2, line 134) is described only briefly: OOD images are encoded, stored as keys, and mapped to in-distribution value embeddings with "location set as the whole image." Important details are absent: how many few-shot OOD images are used, how they are selected, how many codebook entries are added, what similarity threshold ε is used for matching, and how well this generalizes to unseen OOD inputs. The evaluation (Table 2) tests only ImageNet-Sketch on two models. No other OOD datasets (e.g., ImageNet-R, ImageNet-A, stylized ImageNet) are tested. The striking 20% gain on ViT could reflect overfitting to a small set of sketches. Without understanding the trade-off between OOD coverage and codebook size, and without testing held-out OOD generalization, this claim remains anecdotal rather than established.

- **The defense evaluation lacks quantitative rigor.** Figure 5 shows overlapping STRIP entropy and Scale-UP SPC distributions, but no quantitative metrics are reported — no AUC, no true positive rate at a fixed false positive rate, no optimal detection threshold analysis. The paper concludes these defenses "cannot distinguish" backdoor samples (line 375), but the distributions show visible separation in their modes, and without measuring separability, this conclusion is unsubstantiated. Additionally, only one dataset (likely CIFAR-10 based on the threat model context) is shown, leaving generalizability across trigger patterns and datasets untested.

### Minor

- **100% ASR is a guaranteed property of the embedding-replacement mechanism, not a learned empirical result.** Because the codebook explicitly replaces the entire image embedding with the target embedding whenever the trigger patch is detected (lines 146–153), ASR is structurally guaranteed (assuming the similarity check works correctly for the same encoder/trigger combination). The paper repeatedly presents 100% ASR as an empirical achievement (Table 1, Table 5, Contribution 4), which overstates the significance of this metric. The real empirical question is about clean accuracy preservation, detectability, and generalizability — not whether the embedding replacement works.

- **The similarity threshold ε is never specified or ablated.** The matching function (line 144) uses a threshold ε, but its value is never given in the paper. The implementation details (line 218) specify cosine similarity as the measurement but omit ε. It is unclear whether ε is tuned, set to a conservative value like 0.99, or derived in some other way. Since a poorly chosen ε could cause false positives (clean images misclassified as triggered) or false negatives (triggered images not recognized), this is a design parameter that should be reported and ablated.

- **The CIDEr score of 10.00 for AAₚ (Table 3 in the paper, "tab:caption") is anomalously high and unexplained.** Standard CIDEr on COCO typically ranges around 0.8–1.2. A score of 10.00 (exactly 10) for the poisoned-caption similarity is suspicious and could indicate a different normalization or a reporting issue. This is especially concerning because the AAₚ metric measures similarity between the model's output on poisoned inputs and the target caption — since both are the same fixed string "a cat laying on a couch," a perfect score is expected by construction, mirroring the 100% ASR issue for classification.

- **Training time of 0.00 hours (Table 4) omits codebook construction cost.** While no gradient-based training is required, the codebook construction involves encoding trigger patterns and target/OOD images through the encoder, which takes non-zero time. Reporting this as 0.00 hours is misleading; the paper should report wall-clock time including codebook construction and integration.

### Trivial
- The matching process equation (line 150) uses `f_θ(x_ij) = k` but the earlier mechanism (line 144) uses cosine similarity with a threshold. These are inconsistent formulations — exact equality vs. similarity thresholding.

## Nice-to-Haves

- A simple training-free baseline for comparison — e.g., directly patching the classifier weights to output the target class when the trigger is present — would contextualize EDT's value beyond the guaranteed 100% ASR.
- Ablation of ε values and their effect on false positive/negative rates would strengthen the method specification.
- Additional OOD datasets and an analysis of how many few-shot OOD examples are needed would substantially improve the domain adaptation claim.
- White-box detection: a discussion of whether a defender who inspects the model weights can trivially extract the codebook and identify the attack.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **The critic's claim that "the paper conflates model editing with backdoor injection, and the distinction is not acknowledged."** The paper explicitly states it is "driven by the similar objective in model editing" and "draw inspiration from model editing techniques" (Abstract, lines 22, 104). The distinction is acknowledged — the paper frames EDT as inspired by, not identical to, model editing. This criticism misunderstands the paper's framing.
- **The critic's claim that domain adaptation evaluation "could be overfitting to a handful of sketches."** While the evaluation is indeed underspecified (a valid concern kept above), the critic presents this as a definitive failure rather than a concern about missing details. The paper does report real accuracy improvements; the issue is insufficient rigor, not evidence of overfitting.
- **The critic's request for "no attack" baselines for CLIP.** The paper already includes the clean pre-trained model's accuracy as an implicit baseline (CA_before in Table 2 for domain adaptation, and the CA values for EDT can be mentally compared to what one would expect from a clean model). This is a minor omission that doesn't affect the main conclusions.
- **The strength from Strength Finder about "robustness against two runtime defenses"** is moved here because the defense evaluation is insufficiently rigorous (no quantitative metrics), and per the rule "when a strength and weakness disagree, the weakness wins." The distributions shown do suggest partial evasion, but the evidence is too weak to list as a supported strength.

## Novel Insights

The most interesting observation spanning the reviews is that EDT exposes a fundamental ambiguity in how we define backdoor attacks in the era of large pre-trained models. Traditional backdoor attacks are defined by the *process* (data poisoning + training), which ensures the backdoor is latent and learned. EDT achieves the same input-output mapping through a hard-coded lookup, raising the question of whether the attack community needs new definitions of "backdoor" for models that are distributed as black boxes or APIs. The tension between EDT's guaranteed ASR and the paper treating it as an empirical result reflects this deeper ambiguity — the method is simultaneously too effective (100% ASR by fiat) and potentially too detectable (the codebook is an explicit structure a defender can inspect). This suggests that the paper's real contribution is not the 100% ASR but rather the demonstration that training-free/data-free backdoor injection is possible *at all*, which has implications for model distribution platforms like HuggingFace.

## Suggestions

1. **Reframe the paper's claims.** Drop "outperforms state-of-the-art" and instead focus the narrative on proposing EDT's threat model as a *new* setting where no prior methods exist. Position the 100% ASR as a correctness property of the mechanism rather than an empirical victory. The value proposition is: "this is the first training-free, data-free backdoor attack applicable across diverse architectures and tasks."

2. **Add details for ε.** Report the threshold value used in experiments and include an ablation study showing how different ε values affect false positive rate (clean images accidentally matched) and false negative rate (triggered images not matched).

3. **Strengthen the domain adaptation evaluation.** Test on additional OOD datasets (ImageNet-R, ImageNet-A, stylized ImageNet), report the number of few-shot OOD examples used, and show the trade-off between codebook size and OOD accuracy improvement. Include a held-out evaluation to demonstrate generalization beyond the few-shot examples.

4. **Add quantitative defense metrics.** Report AUC, TPR@1%FPR, or similar standard detection metrics for STRIP and Scale-UP across multiple datasets and trigger patterns.

5. **Acknowledge the CIDEr anomaly.** Explain why the CIDEr score is 10.00, or if it is an error/implementation difference, clarify the metric computation.

## Score and Decision

- **Originality:** 6/10 — The codebook-based, training-free backdoor injection is novel, but the core mechanism (embedding replacement on trigger detection) is conceptually simple.
- **Importance of research question:** 7/10 — The threat model (weak adversaries attacking customized pre-trained models) is timely and relevant.
- **Claims supported:** 4/10 — The core claims (training-free, data-free, works across models) are supported. However, key claims about "outperforming SOTA," domain adaptation, and defense evasion are not adequately supported.
- **Soundness of experiments:** 4/10 — Missing baselines for the same threat model, underspecified OOD evaluation, and non-quantitative defense evaluation significantly weaken experimental rigor.
- **Clarity of writing:** 6/10 — The threat model and codebook mechanism are clearly explained, but key details (ε value, OOD key count, CIDEr normalization) are missing.
- **Value to community:** 5/10 — The proof of concept is useful, but the paper needs substantial revision to provide a reliable evaluation that the community can build on.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>