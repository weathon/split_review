- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary
This paper proposes a compression method for Transformers that merges multiple feed-forward (FF) sublayers into a single tied parameter set via permutation-based neuron alignment and weight averaging. The method is tested on GPT-2 (language modeling), ViT (image classification), and an OPUS-MT translation model. At 1/3 of FF sublayers removed (~21% total parameter reduction for ViT), the compressed models retain near-original performance after recovery fine-tuning, and the method consistently matches or outperforms a structured layer-dropping baseline.

## Strengths
- **Consistent performance retention across diverse modalities and architectures**: At 1/3 FF sublayers removed, the method achieves only a 1% accuracy drop on ViT, 1 PPL increase on GPT-2, and 2 BLEU drop on translation (Figure 2). The experiments span decoder-only, encoder, and encoder-decoder Transformers, supporting generalizability.
- **Favorable comparison against structured layer-pruning baseline**: When both methods receive identical recovery fine-tuning, merging matches or outperforms layer-dropping at comparable parameter reductions across all three tasks (Figure 3). This is a properly controlled comparison.
- **Novel insight into FF sublayer redundancy via CKA**: The paper shows clear regions of high CKA similarity between FF sublayer activations within the same model, despite being separated by attention layers and residual connections (Figure 5). This provides an explanation for why merging works and goes beyond prior work on full-layer similarity.
- **Orthogonality to quantization**: Combining merging with LLM.int8() quantization further reduces model storage while retaining high performance (Table 4), demonstrating compatibility with standard compression techniques.
- **Robustness to design choices**: After fine-tuning, different anchor positions and different random consecutive layer windows all yield similar final performance (Tables 2, 3), indicating the method is not brittle to implementation choices.

## Weaknesses

### Fatal
None. The paper's core contribution — a merging-based compression method for Transformer FF sublayers — is sound and the method is clearly described. The main evidential concern (below) is significant but does not invalidate the paper.

### Major
1. **Missing fine-tuned baseline for ViT and machine translation tasks**. The paper states in Section 4.1: "Because we have access to the training data for the machine translation and ViT models, we do not provide a fine-tuned baseline for those as the data we use already appears in their original training data." This means the compressed ViT/MT models receive additional recovery fine-tuning (50k–100k steps) on data the original model was already trained on, while the reported baseline is the original model *without* this extra training. Pre-fine-tuning performance (Figure 4) shows large drops (e.g., ViT accuracy from ~85% to ~70% at 1/3 FF removed), and the recovery fine-tuning closes most of this gap. Without a control where the original, uncompressed model is fine-tuned for the same number of steps on the same data, the observed recovery cannot be cleanly attributed to the merging step versus simply additional training. Layer-dropping baselines are properly controlled (both methods get identical fine-tuning), and the GPT-2 experiments also control for this, but the headline claims about ViT and MT performance retention rest on an asymmetric comparison. **Impact**: This weakens the evidence for the paper's central claim that merging FF sublayers is itself an effective compression technique, rather than the effect being primarily driven by additional fine-tuning.

2. **The layer-dropping baseline removes full layers (attention + FF) rather than only FF sublayers**. The comparison in Figure 3 drops entire Transformer layers to match parameter reduction ratios. This confounds the comparison: the baseline loses both attention and FF parameters while the merging method only compresses FF parameters. A more direct baseline would remove only the FF sublayers (keeping attention) and apply the same recovery fine-tuning. The current comparison, while still informative, makes it harder to isolate whether the advantage of merging comes from preserving attention or from the merging procedure itself. **Impact**: Reduces the precision of the claimed advantage over pruning.

### Minor
1. **No measurement of actual inference speed or memory footprint**. The paper claims memory savings from weight tying but reports only parameter counts and theoretical parameter reduction. Actual disk size, GPU memory usage, or inference latency measurements would ground the practical claims.
2. **The CKA analysis is not directly linked to the merge selection procedure**. The paper shows high CKA similarity between certain FF sublayers (Figure 5) but does not verify whether the sliding-window selection (which picks merge candidates via validation performance, not similarity) actually selects windows falling within high-CKA regions. The connection between the similarity analysis and the method's effectiveness remains circumstantial.
3. **The robustness result (Tables 2, 3) may actually undercut the method's specificity**. After fine-tuning, different random merge windows achieve similar performance to the selected window. While the paper correctly frames this as robustness, it also suggests that recovery fine-tuning dominates the outcome and that the merge selection is less important than claimed. Including pre-fine-tuning performance for the random selections would clarify whether the selection provides a meaningful initialization advantage.

### Trivial
- The abstract states "removing over 21% of total parameters from a Vision Transformer, while maintaining 99% of its original performance." This is technically accurate but potentially misleading given that the 99% figure reflects post-fine-tuning performance versus a pre-fine-tuning baseline.

## Nice-to-Haves
- **Add a fine-tuned baseline for ViT and MT**: Fine-tune the original uncompressed model for the same number of steps (same batch size, learning rate schedule, data) as the recovery fine-tuning. This is the single most important control to strengthen the paper's claims.
- **Ablate the averaging step**: Compare the full merging procedure (permutation + averaging) to simply copying the anchor sublayer's weights into all k positions (without averaging) and then fine-tuning. This would isolate whether averaging provides additional benefit beyond tying.
- **Report pre-fine-tuning performance in the main results figure (Figure 2)** alongside the post-fine-tuning numbers so readers can visually assess how much recovery comes from fine-tuning.
- **Compare against a baseline that removes only FF sublayers** (keeping attention) to make the layer-dropping comparison more direct.

## Removed Points
These points are flagged to be removed; treat them with caution.
- Critic's characterization of the missing baseline as "fatal" and "undermining the paper's central claim" is removed because (a) the layer-dropping comparison IS properly controlled and shows merging's advantage, (b) the GPT-2 experiments have a proper fine-tuned baseline, and (c) pre-fine-tuning performance is reported in Figure 4, providing partial transparency. The issue is Major, not Fatal.
- Critic's claim that "the method's contribution is not clearly isolated from the fine-tuning component" is merged into the Major weakness above; it is not a separate issue.
- Critic's point about "no comparison to quantization-only baselines" is removed — the paper's claim about quantization is orthogonality, not superiority, and adding yet another baseline is scope creep.
- Critic's suggestion about non-adjacent merges is removed; the paper explicitly acknowledges this as a scope limitation and marks it as future work.
- Strength Finder's strengths are all concrete and specific; none needed removal.

## Novel Insights
The most interesting observation from the reviews is that the paper's robustness results (random layer selections all converge to similar performance after fine-tuning) create an inherent tension with the claim that the selection procedure is important. This tension is not resolved in the current draft: the pre-fine-tuning performance varies substantially across windows (Figure 4), yet post-fine-tuning the differences vanish (Table 2). This pattern, if explored further, could either reveal that fine-tuning dominates to the point that selection is nearly irrelevant (which would weaken the method's novelty) or that the selection provides a better initialization that fine-tuning exploits more efficiently (which would strengthen it). The paper does not currently address this distinction.

## Suggestions
1. **Run the missing control experiment**: Fine-tune the original uncompressed ViT and OPUS-MT models on the same data for the same number of steps as the compressed models receive, and compare. Report whether merging provides a benefit over equivalently trained baselines.
2. **Add pre-fine-tuning data points to Figure 2** so readers can assess compression-only performance without the confounding effect of additional training.
3. **Report actual memory/latency measurements** (e.g., GPU memory usage, inference time) rather than just parameter counts, since the paper's practical claims hinge on memory savings.
4. **Include an ablation** where FF sublayers are simply removed (not merged) and the model is fine-tuned, to directly test whether the merging step provides benefit over plain removal at the same parameter budget.
5. **Clarify in the abstract and conclusion** that the reported performance after compression is after recovery fine-tuning, and make the asymmetric baseline treatment for ViT/MT vs. GPT-2 explicit early in the paper.
