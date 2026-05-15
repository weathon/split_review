I've verified all claims against the paper. Here is the consolidated final review.

---

## Summary

This paper tackles two problems in long-text-to-image generation: (1) CLIP's token limit prevents it from encoding long text inputs, and (2) preference-based fine-tuning for T2I alignment suffers from overfitting to text-irrelevant factors (e.g., aesthetics). The authors propose segment-level encoding to extend CLIP to long texts, and a preference decomposition method that separates the text-relevant and text-irrelevant components of CLIP-based preference scores, with a gradient reweighting strategy to suppress overfitting. After ~20 hours of fine-tuning SD v1.5, the resulting model (longSD) shows improved long-text alignment.

## Strengths

- **Preference decomposition into text-relevant and text-irrelevant components is a clean analytical contribution.** The paper identifies that CLIP-based preference scores contain a common direction **V** (text-irrelevant, capturing aesthetics and visual quality) and an orthogonal text-relevant part. This is clearly motivated, grounded in the cone effect (Gao et al., 2019; Liang et al., 2022, cited at line 136), and empirically supported by retrieval results in Table 1, where using only the text-relevant component **C_P^⊥** improves retrieval accuracy across all preference models tested.

- **Gradient reweighting strategy provides a principled solution to a known overfitting problem.** The authors connect the text-irrelevant component **V** to the overfitting patterns observed in reward fine-tuning (Figure 6), and propose a simple reweighting factor ω that suppresses **V**'s gradient contribution. Figure 5 shows that ω=0.3 yields stable FID while improving both Denscore and Denscore-O, whereas other values trigger overfitting. This is a natural, well-motivated fix for a practical problem.

- **Segment-level encoding and loss enable CLIP-based preference models to handle long texts.** The segment-level training loss (Equation 5) allows weakly supervised training without per-segment annotations. Table 1 shows that only the segment-level trained Denscore benefits from averaged segment embeddings (vs. single-pass), while other models are confused by the extra information. This is a practical contribution that extends the utility of CLIP-based reward models.

- **Multiple evaluation angles mitigate concerns about reward hacking.** The paper uses FID, Denscore, Denscore-O, and VQAscore on a 5k held-out set, plus GPT-4o evaluation on 1k images (Figure 7) as an independent judge. The GPT-4o results are consistent with the automated metrics, providing some confidence that improvements are not merely overfitting to the reward model.

- **Orthogonal to existing frameworks (P2I).** Table 3 shows that applying the method on top of P2I yields consistent improvements, demonstrating that the fine-tuning strategy is complementary to architectural improvements.

## Weaknesses

### Fatal
None.

### Major

- **Cross-model comparison against foundation models is weakened by evaluation set distribution.** The 5k evaluation set is a held-out subset drawn from the same data sources (SAM, COCO2017, LLaVA subset, JourneyDB) used to train longSD (line 181). PixArt-α and Kandinsky v2.2 were not trained on this distribution. FID is distribution-dependent, so the comparison in Table 2 (where longSD "outperforms stronger foundation models") is not a clean measure of generalization. This does **not** invalidate the paper — the GPT-4o evaluation (Figure 7) serves as an external, independent judge and supports the same conclusion — but the headline claim would be substantially stronger if backed by results on a widely-used held-out benchmark (e.g., MS-COCO 30K, PartiPrompts) where no model has a distributional advantage. The paper mentions DPG-Bench but does not present results in the main text.

### Minor

- **Denscore training confounds methodological improvements with data changes.** Denscore is trained on Pickscore's original data *plus* additional LLaVA-Next captions, using a new segment-level loss (line 181). Any improvement over Pickscore could partially come from the larger/different training data rather than the proposed loss or encoding. A controlled ablation (e.g., training a baseline with the same augmented data but the original Pickscore loss) would be needed to isolate the effect of the segment-level loss. The retrieval gains in Table 1 are also modest (60.1%→62.1%) and reported without confidence intervals or significance tests.

- **The segment-level encoding for the diffusion model encoder is not used in the final best system.** Section 5.3 (Figure 4) shows that CLIP+T5 significantly outperforms CLIP-cat (the segment-level encoding approach), and the paper adopts CLIP+T5 for the final model. The contribution remains valid for the preference model (Denscore), but the framing in Section 3.1 as a general solution for diffusion model text encoding is somewhat overclaimed given the final architecture choice.

- **Gradient reweighting ablation is limited to a single encoding setup.** The ω ablation (Figure 5) and overfitting analysis (Figure 6) use CLIP-cat encoding with LCM-LoRA and DRTune for speed (line 208). The paper acknowledges that "the optimal value of ω can vary depending on the model and training strategy used" (line 213), but does not validate whether ω=0.3 transfers to the full CLIP+T5 model used in the final results. A demonstration of the reweighting's effect with the actual final configuration would strengthen the causal claim.

### Trivial

- None.

## Nice-to-Haves

- A controlled ablation that trains Denscore with the original Pickscore loss on the *same augmented data* to isolate the benefit of the segment-level loss.
- Reporting results on a standard held-out benchmark (e.g., MS-COCO 30K, PartiPrompts, or DPG-Bench) for the cross-model comparison.
- Validating the ω=0.3 reweighting factor on the final CLIP+T5 encoding configuration rather than only on CLIP-cat.

## Removed Points

The following points from the reviews were removed with justification:

- **"The paper does not cite these references for the cone effect"** (Harsh Critic, Section-by-Section notes on Section 4). REMOVED — factually wrong. The paper explicitly cites Gao et al., 2019 and Liang et al., 2022 at line 136: "The presence of V is referred to as the cone effect (Gao et al., 2019; Liang et al., 2022)."

- **"Segment-level encoding... is a straw contribution"** (Harsh Critic, Critical Issue 2). REMOVED as stated — the encoding is used for the preference model (Denscore) and the paper's contribution claim is about encoding models generally, not exclusively about the diffusion model encoder. The criticism is partially addressed below as a minor weakness (the framing is slightly overclaimed), but the "straw contribution" framing is too strong.

- **"DPG-Bench results are promised but never shown"** (Harsh Critic, Section 5). REMOVED — the parser strips appendix/supplementary material; these results likely exist in the original submission's appendix.

- **"The abstract claims... but does not specify the evaluation protocol"** (Harsh Critic, Abstract & Introduction). REMOVED — abstracts are summaries and are not required to specify evaluation protocol.

- Various generic or unsupported "strengths" from the Strength Finder (e.g., "this paper addressed an important problem") that lack specific content. These add no information beyond what is already stated.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add held-out benchmark results for cross-model comparison.** Evaluate longSD, PixArt-α, and Kandinsky v2.2 on a standard benchmark like MS-COCO 30K or PartiPrompts, where no model has a distributional advantage. This would directly address the main evaluation concern and substantially strengthen the headline claim.

2. **Add a controlled ablation for Denscore.** Train a version of Denscore using the original Pickscore loss on the same augmented training data (Pickscore data + LLaVA-Next captions). This would isolate whether the segment-level loss provides benefit beyond just having more training data.

3. **Report confidence intervals or significance tests** for the retrieval accuracy results (Table 1) and key comparison metrics to quantify the reliability of the reported improvements.

4. **Demonstrate gradient reweighting on the final CLIP+T5 configuration.** Validate that ω=0.3 (or a recalibrated value) provides the same overfitting mitigation when applied to the full system, not just the CLIP-cat+LCM-LoRA proxy used in the ablation.

## Score and Decision

**Overall assessment:** The paper makes genuine contributions — the preference decomposition is analytically clean, the gradient reweighting is well-motivated and empirically supported, and the segment-level encoding extends the practical utility of CLIP-based preference models. However, the evaluation of the headline cross-model comparison (longSD vs. PixArt-α/Kandinsky) is weakened by the evaluation set's distributional overlap with longSD's training data. This does not invalidate the paper (the GPT-4o evaluation and P2I comparisons provide independent support), but it prevents the claim from being fully established. The paper would be strong with revision addressing this concern.

**Originality:** Good. The preference decomposition and reweighting are novel directions.  
**Importance of question:** High — long-text alignment is a recognized challenge.  
**Claims well-supported:** Partially — core technical claims (decomposition, reweighting) are well-supported; the cross-model superiority claim is weakened.  
**Soundness of experiments:** Moderate — sound internal ablations but the external comparison needs strengthening.  
**Clarity of writing:** Clear; well-structured.  
**Value to community:** Moderate — the decomposition insight and reweighting strategy are likely to be adopted by practitioners.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>