- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 8, 6, 6, 6
I have now thoroughly read the paper and verified each reviewer claim against the text. Let me produce the final consolidated review.

---

## Summary

This paper proposes CDAM (Class Distribution-induced Attention Map), a training-free method that refines the last attention layer of CLIP for open-vocabulary semantic segmentation. The core insight is that patch-wise class distributions are more reliable indicators of object membership than argmax class predictions — an observation quantitatively demonstrated in Section 3.2.1. CDAM constructs attention weights from Jensen-Shannon divergence between patch class distributions, integrates them with multi-scale aggregation and augmented text prompts, and uses an entropy-based background thresholding heuristic. Experiments across seven benchmarks show consistent and substantial gains over existing training-free methods (e.g., +15.4 mIoU on VOC21 for MaskCLIP).

## Strengths

1. **Novel and well-evidenced empirical observation.** Section 3.2.1 quantitatively demonstrates that CLIP-based baselines achieve only ~67–71% patch-level prediction accuracy on VOC21 but ~79% accuracy in identifying same-class patches via distribution similarity. This concrete discovery directly motivates CDAM and is a genuine departure from prior work that treats argmax predictions as the primary signal.

2. **Consistent and substantial gains across multiple baselines.** Tables 1–2 show CDAM improves every compatible training-free method (MaskCLIP, SCLIP, ClearCLIP, GEM) on all benchmarks. The ablation study (Table 3) cleanly decomposes each component's contribution, with all components showing positive impact across four baselines.

3. **Training-free with minimal computational overhead.** Section 4.3 reports at most 34 ms added inference time per image and ~200× speedup over CaR on COCO-Obj, making the method practical for real-time settings.

4. **Empirical justification of key design choices.** The paper compares JS divergence against KL divergence and Wasserstein distance (Table 8) and selects JS based on average performance across baselines — providing evidence for a non-obvious design decision.

## Weaknesses

### Fatal

None.

### Major

1. **Integration of CDAM into the last attention layer is underspecified (Section 3.2.4).** The paper states: "we incorporate this localized attention map, $\mathbf{Attn}_{\mathrm{MS}}$, into the last attention layer of CLIP to compute the final similarity map S. We reuse the latent features from the $L-1$ th attention layer of CLIP, $\mathbf{x}^{(L-1)}$, as value features." This leaves several critical questions unanswered:

   - Does $\mathbf{Attn}_{\mathrm{MS}}$ *replace* the original self-attention weights $\mathrm{Softmax}(QK^T/\sqrt{D})$, or is it fused with them (e.g., added or averaged)?
   - Are "value features" the raw $\mathbf{x}^{(L-1)}$ or the projected version $\mathbf{x}^{(L-1)}\mathbf{W}_v$?
   - Are the residual connection and MLP in the last transformer block preserved?
   - When integrating with methods like MaskCLIP (which replaces attention with the identity matrix) or SCLIP (which uses query-query attention), what exactly does CDAM override or complement? The paper claims CDAM can be "seamlessly integrated" but does not specify how it interacts with these modifications.

   This underspecification prevents faithful reproduction and weakens the paper's credibility as a complete method description. A precise algorithmic specification (pseudocode or explicit equations) is needed.

### Minor

2. **Entropy-based background thresholding is a heuristic with limited justification (Section 3.3).** The formula $\mathrm{Thr}_{\mathrm{ent-bg}} = \alpha \, \mathrm{Thr}_{\mathrm{default}} / \mathrm{H}(\mathbf{S})_{\mathrm{center}}$ is introduced without explanation of why dividing by the center entropy is the correct functional form. The text states that foreground patches have low entropy and background patches have high entropy, but the relationship between this observation and the specific formula is not derived or referenced. The hyperparameter $\alpha=2.5$ is fixed across all datasets with no sensitivity analysis shown. While the empirical results validate the heuristic's effectiveness, the paper would benefit from either a principled derivation or a sensitivity study demonstrating robustness to $\alpha$.

3. **Ablation on augmented text prompts is incomplete.** The ATP uses 80 attribute/super-category prompts drawn from PACO, COCO-Stuff, and MSCOCO. The paper does not ablate the contribution of ATP alone (without CDAM attention refinement) or compare against a control condition using random unrelated prompts of the same count. This would strengthen the claim that ATP specifically enriches class distributions rather than simply adding more text entries.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis for $\alpha$ in the entropy thresholding (e.g., a plot of mIoU vs. $\alpha$ on VOC21 and COCO-Obj).
- An ablation comparing ATP with a set of 80 random/irrelevant class names to verify that the benefit is not simply from increasing the number of text prompts.

## Removed Points

1. **"ATP dataset bias on COCO-Obj"** (from Harsh Critic, Critical Issue #3). *Reason for removal:* The ATP consists of generic attributes (colors like "yellow," materials like "fabric," super-categories like "animal," "indoor") — these are universal descriptors that apply to any image dataset. The criticism that these constitute "indirect supervision" specific to COCO-Obj is unsupported; the super-categories from MSCOCO are high-level groupings (e.g., "food," "furniture") that provide no class-specific leakage. Furthermore, ATP is used only to construct the attention map, not for final classification. This is a strawman weakness.

2. **"Missing related works"** and **"typos/formatting/parser artifacts"** criticisms. *Reason for removal:* Per the hard rules, missing related work citations cannot be verified without external sources, and formatting artifacts are parser issues, not author errors.

3. **Generic area-of-concern sweep statements** from the Harsh Critic (e.g., "the paper evaluates the threshold only on limited empirical evidence," "the integration step is the main flaw" stated without the specific anchor questions). *Reason for removal:* These are either captured more concretely in the retained weaknesses above or lack a specific anchor in the paper text. Only the concretely grounded concerns are retained.

## Novel Insights

The Harsh Critic's most valuable observation is the precise specification gap in Section 3.2.4 — the fact that the paper never clarifies whether CDAM replaces, adds to, or modulates the original attention weights, and never specifies how the value projection and residual connections are handled. This is a genuinely structural issue that the authors can fix but that materially affects the paper's completeness. Separately, the observation that the entropy thresholding formula inverts an expected relationship (higher entropy → lower threshold, making foreground classification *easier* when the model is *more* uncertain) is an insightful catch that the paper does not address, though a plausible defense exists (when all confidence scores are lower, a proportionally lower threshold compensates).

None beyond the paper's own contributions.

## Suggestions

1. **Provide a precise algorithmic specification of the integration.** Add pseudocode or explicit equations showing the forward pass of the last attention layer when CDAM is applied. Specify: (a) whether $\mathbf{Attn}_{\mathrm{MS}}$ replaces or augments $\mathrm{Softmax}(QK^T/\sqrt{D})$, (b) the exact computation of value features (with or without $\mathbf{W}_v$), (c) whether the residual connection and MLP are preserved, and (d) how the final similarity map $\mathbf{S}$ is computed from the attention layer's output.

2. **Add a sensitivity analysis for $\alpha$** in the entropy-based background thresholding (mIoU vs. $\alpha$ on at least one dataset) to demonstrate that the fixed choice of 2.5 is not brittle.

3. **Ablate ATP more thoroughly:** show performance (i) without ATP entirely, (ii) with ATP but excluding CDAM attention refinement, and (iii) with a control set of 80 random class names replacing the attribute prompts.
