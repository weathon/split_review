Now I have all the information needed to write the final consolidated review. Let me compose it.

---

## Summary

This paper proposes a post-training compression method for Transformers that merges multiple adjacent feed-forward (FF) sublayers into one by permuting their neurons for alignment (solving a linear assignment problem), then averaging the aligned parameters, and finally tying the merged weights. The method is evaluated on GPT-2 (language modeling), ViT (image classification), and OPUS-MT (machine translation), achieving near-original performance while removing 1/3 of FF sublayers (10–21% total parameter reduction). The paper also presents a CKA similarity analysis showing regions of high similarity between FF sublayer activations, which may help explain their mergeability.

## Strengths

1. **Novel idea evaluated across diverse architectures and modalities.** The method applies permutation-based alignment (from the model-merging literature) to merge sublayers within a single model rather than across separate models. Results span a decoder-only LM (GPT-2), an encoder-only vision model (ViT), and an encoder-decoder translation model (OPUS-MT) — demonstrating generalizability that few compression papers attempt.

2. **Consistent performance retention at 1/3 FF sublayer removal.** At this compression level, the method retains near-original performance across all three tasks (1% accuracy drop for ViT, 1 PPL increase for GPT-2, 2 BLEU drop for translation), and maintains competitive results even at 1/2 FF sublayer removal. These results are validated by Figure 2, which also shows that permutation alignment consistently outperforms vanilla (un-aligned) averaging, especially at higher compression ratios.

3. **Robustness to hyperparameter choices.** Tables 2 and 3 show that post-fine-tuning performance is stable regardless of which consecutive group of sublayers is merged or which sublayer serves as the permutation anchor. This is practically important — it means users don't need to carefully tune these parameters.

4. **Orthogonality to quantization.** Table 4 demonstrates that merging is complementary to LLM.int8() quantization, enabling combined compression ratios of ~25% in storage without significant additional performance degradation (e.g., ViT: 77.4% → 77.1%).

5. **CKA similarity analysis provides a post-hoc explanation.** Figure 5 reveals clear block-diagonal regions of high CKA similarity between FF sublayer activations across all three models — a novel empirical observation that supports the method's plausibility and may be independently useful for future compression work.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claim — that merging aligned FF sublayers is an effective post-training compression technique — is supported by the experimental evidence. The issues below are substantive but do not invalidate the central contribution.

### Minor

1. **The contribution of merging is not cleanly separated from the cost of recovery fine-tuning.** The paper reports only final post-fine-tuning performance in the main results (Figure 2). While Figure 4 does show pre-tuning performance across different windows, there is no reporting of (a) how many fine-tuning steps were actually needed to reach the reported performance vs. the maximum budget (100k for GPT-2/MT, 50k for ViT), or (b) a learning curve showing accuracy/perplexity vs. fine-tuning steps. The abstract's claim of "a small amount of recovery fine-tuning" is unquantified. For context: 50k steps with batch size 128 on ImageNet-1k is ~5 epochs — non-trivial, even if less than full pre-training. The paper should report the actual steps needed to reach acceptable performance so readers can assess whether the fine-tuning cost is indeed "small" relative to alternatives.

2. **The layer-dropping baseline (Figure 3) is structurally favorable to merging.** Dropping entire layers removes both attention and FF parameters, while merging compresses only FF sublayers while preserving all attention capacity. At the same parameter budget, merging therefore retains more architectural capacity, making the comparison unsurprising in favor of merging. The paper's claim that merging is "a competitive alternative to strong pruning-based methods" would be better supported by a baseline that compresses only FF sublayers — e.g., removing entire FF sublayers (replacing with identity) or pruning FF neurons at comparable ratios. The "vanilla" merge baseline is an ablation (no alignment), not a literature baseline. As it stands, the comparison validates that FF-merging is better than layer-dropping at the same parameter budget, but overstates the case against pruning more broadly.

3. **The CKA similarity analysis is not directly linked to mergeability.** The paper presents high CKA similarity between FF sublayers (Figure 5) and speculates this explains their mergeability, but never tests the correlation. A direct test — e.g., whether sublayer pairs with higher CKA similarity yield better pre-fine-tuning performance when merged — would substantiate the claim. Without it, the CKA analysis and the merging method remain two separate observations rather than a unified story.

4. **The paper claims attention sublayers do not show the same similarity patterns (abstract, contributions), but never shows the comparison.** No CKA plots for attention sublayers are presented, and no quantitative comparison is reported. This claim is therefore unsupported in the paper.

5. **Only adjacent sublayers are considered for merging, with no justification beyond simplicity.** The paper acknowledges this as future work, but it limits the method — non-adjacent merging could potentially yield better compression. Similarly, the sliding-window selection procedure is not guided by the CKA similarity signal, missing an opportunity to connect the two analyses.

6. **Computational cost of the alignment and selection steps is not reported.** The paper states the cost is low (a single forward pass for features), but providing approximate wall-clock time or number of forward passes for the per-candidate LAP solves would help readers assess practical deployability. Given the method involves evaluating ~N-k candidates, the cost scale is relevant even if small.

### Trivial

- The CKA/quantization combination experiments (Table 4) show merging+quantization vs. the uncompressed model, but not against quantization alone. The additive benefit of merging beyond quantization is therefore not isolable.
- The choice of collecting features before the φ activation (pre-activation) is sensible, but a brief justification would strengthen Section 3.3.

## Nice-to-Haves

- A learning curve (perplexity/accuracy vs. fine-tuning steps) for the final selected model, to quantify the "small amount of recovery" claim.
- A baseline that compresses only FF sublayers (e.g., removing entire FF sublayers or pruning FF neurons) for a cleaner comparison in Figure 3.
- A quantitative comparison between merging pairs with high vs. low CKA similarity to directly test the redundancy → mergeability hypothesis.
- CKA similarity plots for attention sublayers to substantiate the claim that they do not exhibit the same patterns.

## Removed Points

The following criticisms from the Harsh Critic review were removed after verification against the paper:

1. **"Output biases are not permuted before averaging" (Issue 1).** This criticism is factually wrong. The permutation matrix P acts on the FF hidden dimension (d_ff), while b^{out} operates in the output space (d_model). The paper's equation is correct: b^{out} does not need to be permuted because it is not in the space affected by the permutation. Averaging the output biases directly is the correct operation. The reviewer appears to have confused the output space with the hidden space.

## Novel Insights

The most interesting observation that emerges from combining the paper's results with the reviews is the tension between the CKA similarity analysis and the merging method itself. The CKA analysis (Figure 5) shows block-diagonal regions of high similarity, suggesting adjacent sublayers are particularly redundant. Yet the paper uses brute-force sliding-window search to select which group to merge, rather than exploiting the similarity signal to guide selection. A unified approach — where CKA similarity directly informs which sublayers to merge, potentially including non-adjacent ones — could both strengthen the method and validate the explanatory hypothesis. The paper's current separation between analysis and method leaves an intriguing gap that a follow-up could fill.

## Suggestions

1. Report the actual number of fine-tuning steps required to reach acceptable performance (not just the maximum budget) and provide a learning curve. This is the single most impactful improvement for the paper.
2. Add a baseline that compresses only FF sublayers — e.g., replacing whole FF sublayers with the identity function — to make the comparison with pruning more apples-to-apples.
3. Test whether CKA similarity between sublayer pairs predicts merge quality (pre-fine-tuning performance of the merged model).
4. Include CKA plots for attention sublayers to substantiate the claim that the high-similarity pattern is unique to FF sublayers.

## Score and Decision

The paper presents a novel compression method with solid experimental breadth across three diverse architectures and tasks. The core claim is supported by evidence: merging aligned FF sublayers with recovery fine-tuning achieves near-original performance while reducing parameter count. The method is simple, the permutation alignment step is justified, and the ablation (vanilla vs. permuted merging) cleanly demonstrates the value of alignment. The CKA analysis is an interesting post-hoc observation, though it could be better integrated.

The main weaknesses are: (1) insufficient separation of merging's effect from the cost of fine-tuning, (2) a baseline comparison that structurally favors the method, and (3) unsubstantiated claims about attention sublayers. None of these are fatal — they weaken but do not invalidate the contribution. The issues are addressable with additional experiments and clarifications.

I recommend acceptance with the expectation that the authors address the fine-tuning quantification, add appropriate baselines, and substantiate the attention comparison in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>