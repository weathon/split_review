Now I have all the information needed to write the final consolidated review. Let me synthesize everything.

---

## Summary

LARP proposes a novel video tokenizer that replaces patchwise tokenization with learned holistic queries (decoupling tokens from local patches) and co-trains a lightweight AR transformer as a generative prior during tokenizer training. The AR prior is discarded at inference. The method achieves state-of-the-art FVD of 57 on UCF-101 class-conditional generation and strong results on K600 frame prediction.

## Strengths

- **Co-trained AR prior demonstrably closes the reconstruction–generation gap.** The ablation (Table 4) is the paper's strongest piece of evidence: removing the AR prior model degrades gFVD from 107 to 190 on UCF-101 (a 78% relative increase), while rFVD actually *improves* (31→23). This directly supports the central claim that the prior shapes the latent space for AR generation rather than merely improving reconstruction. This finding is genuinely novel for video tokenization.

- **State-of-the-art generation results with meaningful comparisons.** LARP achieves 57 gFVD on UCF-101, surpassing all published methods including MAGVIT-v2-MLM (58). On K600 frame prediction, LARP-L-Long (632M generator) achieves 5.1 gFVD, outperforming OmniTokenizer (32.9), MAGVIT-MLM (9.9), and closely trailing MAGVIT-v2-MLM (4.3). Within the AR model family, LARP's advantage is dramatic — e.g., LARP-L (343M) at 107 gFVD vs MAGVIT-v2-AR (840M) at 109 gFVD.

- **Novel holistic tokenization decouples tokens from patch locality.** The query-based design (Section 3.2) demonstrably supports flexible token counts (1024 down to 256) with graceful generation degradation — gFVD increases only 1.46× when tokens are halved twice, compared to rFVD's 1.9× increase. This property is not exhibited by patchwise tokenizers and is validated by the ablation where even "No AR prior model" still uses the holistic design.

- **Careful architectural design for the prior model is well-motivated.** The continuous input (de-quantized latents via linear projection rather than token indices) and cosine-similarity-based output prediction are explicitly motivated by the need for gradient flow and codebook-awareness during joint training. The scheduled sampling component is shown to matter (142 vs 190 gFVD without it).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the evidence.

### Minor

- **Overclaimed language about "determining an optimal order."** The abstract (line 10), introduction (line 48), and conclusion (line 379) state that the AR prior "defines a sequential order," "automatically determines an order," and "defines an optimal token order." However, the query embeddings $\mathbf{Q}_L$ have a fixed index order (positions 1 through *n* by construction, Section 3.2, lines 146–153), and the AR prior is trained to predict tokens in this fixed order. There is no mechanism that optimizes or searches over token permutations. What actually happens is that the encoder learns to produce representations that are *predictable in this fixed order* — a valuable property, but meaningfully different from "determining an optimal order." This language should be corrected to match the actual mechanism: the fixed query order is given, and the AR prior aligns representations to it. The paper's argument that this "eliminates the need to manually define a flattening order" is valid (since the fixed query order replaces the flattening problem), but framing this as the prior *determining* the order is misleading.

- **Continuous AR prior formulation is not isolated in the ablation.** The paper claims the *continuous* formulation (input from de-quantized latents, output as embedding predictions) is a key design choice that enables gradient flow and handles the evolving codebook (Section 3.3). However, no ablation compares this to a standard discrete AR prior (operating on token indices with straight-through gradient estimation, similar to what the paper uses for SVQ itself). Without this ablation, it is unclear whether the benefit comes from having *any* sequential regularizer or specifically from the continuous design. Given that the continuous formulation is a core claimed contribution (it's in the title: "Learned Autoregressive Generative Prior"), this gap weakens the mechanistic understanding of what drives the improvement.

- **No discussion of limitations.** The paper concludes without acknowledging any limitations. Notable limitations include: training is conducted only on 16-frame 128×128 clips (scaling to longer/higher-res videos is not demonstrated), the AR prior roughly doubles training computation (two forward passes + scheduled sampling per iteration), and the query-based transformer encoder processes $n+m$ tokens where $m$ scales with resolution (potentially quadratic cost at larger resolutions). A brief limitations paragraph would improve scientific positioning.

- **SOTA comparison has an unacknowledged model size caveat.** The best reported result (57 gFVD on UCF-101) uses a 632M generator, while the closest competitor (MAGVIT-v2-MLM, 58 gFVD) uses a 307M generator. The paper does note that LARP-L with a 343M generator achieves 107 gFVD (already superior to all AR baselines), but the text's framing of the SOTA claim could more explicitly acknowledge this size difference.

### Trivial

- **Figure 1's two-round forward pass is underspecified in the text.** The description (Section 3.3, line 208) says "we randomly mix the predicted output sequence with the original input sequence at the token level" but does not specify the mixing mechanism (per-position independent? what probability schedule beyond a linear warm-up to 0.5?). While the implementation details (line 245) provide the schedule parameters, the method section itself is vague. Pseudocode or a step-by-step algorithm would help.

- **The notation for $f_T, f_H, f_W$ is reused** for both the patchification downsampling factors (Section 3.2, line 139) and the latent downsampling factors (Section 3.1, line 117) with the same values in practice, which could cause confusion on first reading.

## Nice-to-Haves

- **Controlled comparison of holistic vs. patchwise tokenization** with matched architecture, token count, and training data would strengthen the claim that the query-based design specifically contributes to the results. Currently the holistic design's contribution is conflated with the AR prior's.

- **Analysis of learned query embeddings** (e.g., attention maps between queries and patches, or clustering of query representations over video content) would provide direct evidence for the "more semantic and global" claim about the holistic latent space.

- **Token-level predictability analysis:** computing the NLL of the downstream AR generator on tokens from LARP with vs. without the prior would directly show whether the prior-aligned latent space is easier for AR models to predict.

- **Training time and resource reporting** would aid reproducibility and adoption.

## Removed Points

- **"Reproducibility concern about cited models/tools not being released"**: The reviewer mentioned no such issue. Not applicable.
- **"Missing related works"**: The reviewer did not raise this. Not applicable.
- **"Typos/formatting nitpicks"**: The reviewer's note about "hilighting" (line 309) is a parser artifact and not included.
- **Criticism that "the holistic tokenization versus patchwise tokenization is not evaluated as a controlled comparison"** framed as a fatal flaw: The paper is a systems paper proposing a complete method (holistic tokenization + AR prior). The holistic design is an enabler for the AR prior (which requires a sequence of tokens without patch-locality constraints). A controlled comparison would strengthen the paper but its absence does not invalidate the contributions. The paper's main experiments and ablation already demonstrate the combined system works. Downgraded from the reviewer's framing to Nice-to-Haves.
- **"Computation and training cost — not reported"** framed as a weakness: Worth noting but standard for this class of paper. Moved to Nice-to-Haves as a suggestion for better reproducibility.

## Novel Insights

Beyond the paper's own contributions, the most striking finding from the review is that the ablation reveals a clean *inverse correlation* between reconstruction quality and generation quality: removing the AR prior improves rFVD (31→23) while catastrophically degrading gFVD (107→190). This is a strong and rare empirical demonstration that optimizing for reconstruction fidelity is not only insufficient for generation but actively counterproductive in the video tokenization setting. The scheduled sampling ablation (142→190 without it) further shows that the prior's training stability mechanism is nearly as important as the prior itself. This suggests that future video tokenizer work should prioritize the training objective and latent space structure over raw reconstruction metrics.

## Suggestions

1. **Correct the "order" language.** Replace phrasing like "automatically determines an order" and "optimal token order" with precise descriptions: the fixed query index order defines the sequence, and the AR prior optimizes representations to be predictable in that order. This is still a valuable contribution (it solves the flattening problem by sidestepping it with an aligned latent space) and avoids misleading readers.

2. **Add an ablation comparing the continuous AR prior to a discrete AR prior** (token indices as input with straight-through gradient estimation, standard cross-entropy loss). This is the single most important missing experiment to validate the claimed design choices.

3. **Add a limitations paragraph.** Explicitly discuss at least: the 16-frame 128×128 training resolution, the training compute overhead from the AR prior's two-forward-pass design, and potential scalability concerns with larger token counts or resolutions.

4. **Acknowledge the generator size difference** when comparing to MAGVIT-v2-MLM (307M vs 632M) in the SOTA claim, while noting that LARP's smaller generator (343M at 102 gFVD) still outperforms all AR baselines.

5. **Clarify the scheduled mixing mechanism** in Section 3.3 with either pseudocode or a precise description of how predicted tokens are mixed with ground-truth tokens per position.

## Score and Decision

**Score: 7.0** — A technically solid paper with a clear, well-ablated core contribution (the AR prior meaningfully improves video generation from discrete tokenizers). The weaknesses are presentation-level overclaims and one missing ablation that would strengthen mechanistic understanding but do not undermine the empirical results. The paper makes a genuine contribution to video generation.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>