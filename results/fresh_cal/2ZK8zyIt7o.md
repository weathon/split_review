Now I have all the information needed to write the consolidated review.

## Summary

This paper tackles the problem of long-text alignment in text-to-image diffusion models. It proposes two main contributions: (1) a **segment-level encoding** method that divides long text into segments, encodes each separately, and merges the results, enabling CLIP-based models to handle inputs beyond their native 77-token limit; and (2) a **preference decomposition** approach that orthogonally decomposes CLIP-based preference model scores into text-relevant (T2I alignment) and text-irrelevant (aesthetics, etc.) components, with a gradient reweighting strategy (parameter ω) that downweights the text-irrelevant component during reward fine-tuning to mitigate overfitting. After ~20 hours of fine-tuning SD v1.5 with these techniques, the resulting model (longSD) is reported to outperform larger foundation models (PixArt-α, Kandinsky v2.2) in long-text alignment.

## Strengths

1. **Segment-level encoding is well-motivated and empirically validated.** The method overcomes CLIP's token limit while preserving its image-text alignment advantage. Figure 4 shows that CLIP-cat (the segment-level encoding) achieves comparable FID and Denscore to T5-mlp on long-text inputs, demonstrating that CLIP can be adapted without switching to LLM encoders. The ablation on special token handling (<sot>, <eot>, <pad*>) is a careful design decision.

2. **Preference decomposition into text-relevant and text-irrelevant components is supported by multiple lines of evidence.** Figure 2(b) shows that the common direction **V** has strong positive projection (η > 0.4 for CLIP, > 0.6 for Pickscore/Denscore) across all tested models. Figure 2(c) shows that C_X·C_P^⊥ (text-relevant) distinguishes matched from unmatched pairs, while C_X·η**V** (text-irrelevant) does not. Table 1 further shows that using C_P^⊥ consistently improves retrieval accuracy across all preference models.

3. **Gradient reweighting demonstrably mitigates overfitting.** Figure 5 provides clear evidence: with ω=0.3, FID remains stable across training steps while both Denscore and Denscore-O improve; with ω=1.0 or ω=0.0, FID degrades significantly (overfitting). Figure 6 shows visual improvements from reweighting across four different reward signals (CLIP, HPSv2, Pickscore, Denscore), demonstrating generality.

4. **The method is orthogonal to existing alignment approaches.** Table 3 shows that applying the proposed fine-tuning on top of the P2I diffusion framework yields consistent improvements across FID, Denscore, and GPT-4o win rate, confirming the method can be combined with other strategies without conflict.

5. **Multiple independent evaluation signals are provided.** While Denscore is the primary reward and one evaluation metric, the paper also evaluates with FID (distribution distance, independent of the preference model), VQAscore (an external metric from Lin et al., 2024), GPT-4o as an independent judge (Figure 7), and DPG-Bench (an external benchmark). The GPT-4o results are reported as consistent with the Denscore-based findings.

## Weaknesses

### Fatal

None. The paper's core claims are supported by evidence; no flaw is severe enough to invalidate the entire contribution.

### Major

1. **Circular dependency between the reward signal and the primary evaluation metric (Denscore).** The fine-tuning reward is derived from Denscore, and the main comparison in Table 2 uses Denscore as one of the headline metrics. While this is partially mitigated by other evaluation signals (FID, VQAscore, GPT-4o, DPG-Bench), the paper's central claim — that longSD outperforms PixArt-α and Kandinsky v2.2 — relies most directly on the Denscore column of Table 2. The GPT-4o evaluation (Figure 7) provides some independent corroboration but covers only 1k images and is presented as a bar chart without raw numbers, confidence intervals, or pairwise agreement statistics. This does not fully eliminate the concern that the model is optimized specifically for the Denscore reward.

2. **The preference decomposition mechanism lacks direct causal validation.** The paper asserts that **V** (the average of all text embeddings) captures "text-irrelevant" preferences and that overfitting during fine-tuning is caused by **V** dominating the gradient. While the indirect evidence is suggestive (retrieval improves with C_P^⊥, Figure 2(c) shows C_X·η**V** doesn't distinguish matched/unmatched pairs, Figure 3 provides anecdotal visual examples), the paper does not:
   - Directly measure whether **V** activation correlates with human-judged aesthetics but not semantic correctness (e.g., on a dataset with explicit annotations).
   - Provide gradient norm analysis showing that the **V** component of the gradient is indeed larger in magnitude than the C_P^⊥ component during optimization, and that ω=0.3 balances them.
   - Ablate specific dimensions of **V** to verify it encodes text-irrelevant features.

   The core claim that overfitting is *caused* by **V** dominating the gradient is asserted from the structure of the gradient equation (Section 4.2) rather than demonstrated empirically.

### Minor

1. **No confidence intervals or variance reported for main results.** Tables 2 and 3 present FID, Denscore, and GPT-4o win rates without standard deviations, confidence intervals, or statistical significance tests. Given that the evaluation set is 5k images (with rank-based metrics like R@1 particularly sensitive to small changes), the stability of the reported improvements is unclear.

2. **Denscore training details are underspecified.** The paper states "same settings as Pickscore" with "LLaVA-Next captions" and a "segment-level loss function," but does not specify the exact data mixture used for training the preference model — e.g., how many preference pairs were used, how the LLaVA-Next captions were integrated, or the proportion of segment-level vs. original training data. This limits reproducibility.

3. **Primary evaluation is on a held-out subset of the training data distribution.** The 5k-image evaluation set is reserved from the same dataset used for training (same sources: SAM, COCO, LLaVA subset, JourneyDB). While DPG-Bench and GPT-4o offer some external validation, the main numerical results (Table 2) are on the in-distribution set. Performance on truly out-of-distribution long prompts with different styles or composition is not systematically measured.

### Trivial

None that warrant separate listing.

## Nice-to-Haves

- **Isolate the effect of segment-level encoding from SFT.** The paper could compare segment-level encoding + SFT against standard truncated CLIP + SFT on the same data to quantify the marginal benefit of the encoding itself, separate from the benefit of adding large-scale long-caption SFT data.
- **Quantify the special token handling improvement.** The paper mentions that direct concatenation (without special token handling) yields poor images (Figure 10 in the appendix) but does not provide quantitative FID/Denscore comparison of the two approaches.
- **Provide ablation of ω sensitivity.** The paper notes ω=0.3 works well but also that "the optimal value of ω can vary depending on the model and training strategy used." A sensitivity analysis (e.g., ω ∈ {0.1, 0.2, 0.3, 0.5, 0.7}) would be useful.

## Removed Points

These points from the reviews are removed because they do not hold up against the paper as written:

- **"Comparison to foundation models is unfair"** — The paper compares a fine-tuned SD-1.5 against off-the-shelf foundation models. The claim is that their *training method* enables a smaller model to outperform larger ones, which is a legitimate experimental design. PixArt-α uses T5 (handles long text) and Kandinsky uses both CLIP and T5, so the prompt-truncation concern does not apply to those baselines. The demand that baselines receive equivalent fine-tuning is scope creep — the paper does not claim architectural superiority; it claims "significant potential beyond altering the model structure."
- **"LCM-LoRA introduces additional approximation"** — The paper explicitly states LCM-LoRA is used *only* for acceleration in ablation studies (Section 5.4), not for the final model. This is a reasonable methodological choice for efficient ablation.
- **"Risk of reward hacking is under-discussed"** — The paper explicitly acknowledges this concern and uses GPT-4o evaluation specifically to "mitigat[e] the risk of overfitting to Denscore." The concern is partially addressed.
- **Reproducibility nitpicks about hyperparameters** — The paper provides learning rate, batch size, warmup steps, LoRA rank, training steps, and GPU configuration. These are standard and sufficient for the field.
- **Formatting, missing appendix, and style nitpicks** — Parser-stripped content and formatting artifacts are not author errors.

## Novel Insights

The harsh critic correctly identifies a genuine tension at the heart of the paper: the method uses a preference model (Denscore) as both the training signal and one of the main evaluation metrics. This is a real concern, but the paper's design partially mitigates it with independent evaluations (FID, VQAscore, GPT-4o, DPG-Bench). What is more interesting is that the GPT-4o results are reported as consistent with the Denscore results — if this holds, it suggests the Denscore-based evaluation is not merely capturing reward overfitting. The deeper insight, however, is that the decomposition claim (separating text-relevant from text-irrelevant preferences) is structurally plausible but would benefit enormously from direct causal validation — e.g., showing that perturbing **V** changes image aesthetics while preserving semantic content, or showing that the gradient norm of the **V** component is measurably larger than the C_P^⊥ component during optimization. Without such evidence, the causal story (overfitting *because* **V** dominates the gradient) remains an elegant but unverified hypothesis.

## Suggestions

1. **Report all main results with confidence intervals or standard deviations** (bootstrap or multiple seeds). This is especially important for rank-based retrieval metrics where small fluctuations can change rankings.
2. **Provide gradient norm analysis** showing the magnitude of the **V** vs. C_P^⊥ components during RFT, to directly validate the claim that **V** dominates the gradient and that ω=0.3 rebalances them.
3. **Add a controlled experiment** comparing segment-level encoding + SFT vs. truncated CLIP + SFT on the same 2M dataset to isolate the encoding's contribution.
4. **Release the trained Denscore model** and specify its training data mixture precisely to support reproducibility and independent evaluation.
5. **Expand the GPT-4o evaluation** with more detailed reporting: exact sample sizes per model pair, breakdowns by prompt length, and agreement statistics (e.g., Cohen's κ).

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>