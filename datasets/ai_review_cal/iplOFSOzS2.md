- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

The paper proposes **Attentional Vision Calibration (AVC)**, a training-free decoding method that reduces object hallucinations in Large Vision Language Models (LVLMs). The core idea is to identify "blind tokens" — image tokens that receive disproportionately high attention but carry little discriminative information — and apply contrastive decoding between the original visual input and a version that isolates only the blind tokens. The method operates in three steps: layer selection based on image-attention proportion, blind token identification via a statistical threshold (μ+λσ), and contrastive logit adjustment. Evaluated on POPE, MME, and AMBER benchmarks with LLaVA-1.5 and InstructBLIP, AVC consistently outperforms VCD and M3ID baselines.

## Strengths

- **Training-free method with consistent empirical gains across multiple benchmarks.** On POPE (Table 1), AVC achieves the highest Accuracy and F1 across COCO, A-OKVQA, and GQA datasets under Random, Popular, and Adversarial setups for both InstructBLIP and LLaVA-1.5, outperforming both VCD and M3ID. On AMBER (Table 4), AVC achieves the highest overall AMBER score with improvements in both generative (CHAIR↓) and discriminative (F1↑) tasks.

- **Model-agnostic layer selection that adapts to architectural differences.** The paper documents (Fig. 9) that InstructBLIP concentrates image attention in later layers while LLaVA-1.5 concentrates it in earlier layers. The top-P layer selection method (Eq. 3) automatically adapts to this difference without architecture-specific tuning, which is validated by the method working well on both models.

- **Ablation of the masking scheme confirms the design choice is reasonable.** Table 5 compares zero-out, ones-out, noise, and mask alternatives for constructing the biased visual input, showing the chosen zero-out scheme is on average the most effective. This provides evidence that the contrastive construction (V* isolating blind tokens) is a well-motivated implementation choice.

## Weaknesses

### Fatal
None.

### Major

1. **Core empirical motivation is demonstrated only anecdotally.** The paper's central claim — that zeroing out high-attention tokens barely changes logits while zeroing out low-attention tokens drastically changes them — is supported by a single example (Figures 1 and 2). This is the foundational observation that motivates the entire method. Without aggregate statistics across many images (e.g., distribution of logit changes when zeroing top-k vs. bottom-k tokens over the full POPE dataset), it is unclear whether this is a general phenomenon or an artifact of one cherry-picked case.

2. **Key hyperparameters (λ, γ, α) are not ablated.** The method has three important hyperparameters: λ (threshold for blind token identification), γ (cumulative attention proportion for layer selection), and α (contrastive strength). The paper fixes these at λ=1, γ=0.5, α=3 (InstructBLIP) / α=2.5 (LLaVA-1.5) and provides no analysis of how performance varies with these choices. It is also unclear whether layer selection (γ) is actually beneficial — what happens if all layers are used? Since the paper notes different α values for different models, this suggests sensitivity that should be documented.

### Minor

1. **Baseline comparison is limited to only contrastive-decoding methods.** The paper restricts comparison to VCD and M3ID (both contrastive decoding), but cites other training-free output-level methods such as OPERA (Huang et al., 2023) in the related work. While the paper scopes itself to contrastive decoding, the claim of "consistently outperform[ing] existing decoding techniques" is broader than the evidence supports. Including at least one additional training-free baseline would strengthen the claim.

2. **Potential hyperparameter asymmetry in baseline comparisons.** AVC uses manually tuned α values (3 for InstructBLIP, 2.5 for LLaVA-1.5). For VCD and M3ID, the paper notes they were "reimplemented within our evaluation framework" but does not report whether their hyperparameters were tuned per model or if default settings from the original papers were used. If baseline hyperparameters were not also tuned per model, the comparison may partly reflect hyperparameter selection rather than method quality.

3. **Base model decoding configuration is unspecified.** The paper compares "Base" (standard decoding) but does not specify whether this uses greedy decoding, sampling with temperature, or other settings. Since contrastive decoding methods (including this one) can improve results simply by sharpening the output distribution, the specific benefit of the blind-token mechanism over generic contrastive effects is unclear. An ablation using contrastive decoding with a *random* subset of tokens (rather than blind tokens) would isolate the effect of the proposed identification mechanism.

4. **Performance trade-offs on the MME Count task are noted but not explained.** The paper reports that VCD achieves the highest Count scores on MME while AVC is lower, and notes "both models see a decline in performance for the Count category with Ours." This trade-off is acknowledged but not analyzed — does the attention calibration mechanism harm counting ability specifically? Understanding this would clarify the method's limitations.

### Trivial
None.

## Nice-to-Haves
- Aggregate statistics (across the full dataset) for the core motivating observation (high-attention tokens being non-informative).
- Ablation studies for λ (e.g., 0.5, 1.0, 1.5, 2.0), γ (e.g., 0.3, 0.5, 0.7), and α (e.g., 1, 2, 3, 4) on at least one benchmark.
- A comparison against using contrastive decoding with a random set of tokens rather than blind tokens, to verify that blind-token *selection* (not just contrastive decoding generically) drives the improvement.
- A dedicated limitations paragraph discussing when the method works best and when it may degrade performance (e.g., counting tasks).

## Removed Points

- **Criticism about the one-word constraint in discriminative tasks (from Harsh Critic).** Removed because Appendix discussion of this effect is stripped by the parser; the paper states it exists in the supplementary (line 192), and parser-stripped content should not be held against the paper.
- **Strength about "Empirically grounded token identification via attention statistics" (from Strength Finder).** Demoted because the supporting evidence is limited to a single example, which conflicts with the verified weakness that the core motivation is only anecdotally demonstrated.
- **Criticism about missing code release.** Removed per instructions — this is a reproducibility nitpick about artifacts impractical for a submission.
- **Request for analysis of attention redistribution (entropy of attention weights before/after Ours).** Moved from weakness to nice-to-have; it is not required to validate the core contribution.

## Novel Insights

The reviews do not surface any insight beyond what the paper itself provides. The harsh critic's observation that the method's performance on the MME Count task degrades relative to VCD is a useful specific diagnostic that the authors should address, but it is consistent with the paper's own reporting.

## Suggestions

1. Provide aggregate quantitative support for the core motivation: compute the average KL divergence or logit-change when zeroing out the top-k attention tokens vs. bottom-k tokens across the entire POPE or AMBER dataset. This would ground the blind token concept in solid evidence.
2. Add ablation experiments for λ, γ, and α on a single benchmark to demonstrate robustness or document appropriate ranges.
3. Add a "contrastive decoding with random tokens" baseline to verify that blind token *identification* is driving the gains, not just the contrastive mechanism generically.
4. Either add one more training-free baseline (e.g., OPERA) or explicitly scope the paper's claims to contrastive-decoding methods and adjust the "outperform existing decoding techniques" language accordingly.
