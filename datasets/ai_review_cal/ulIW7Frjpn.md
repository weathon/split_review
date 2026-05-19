- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6
Now I have all the evidence I need. Let me construct the final review.

---

## Summary

This paper proposes using a frozen LLM (LLaMA3-8B) as a plug-in entropy model for transform coding. It introduces a latent-codes arrangement module that maps quantized codes from diverse codecs (JPEG, VQGAN, SpeechTokenizer) into LLM-compatible token sequences, then fine-tunes only the input/output layers (<2% of parameters). Experiments report BD-rate improvements of 54.07% over JPEG, 17.61% over VQGAN, and 34.61% over SpeechTokenizer, suggesting LLMs can serve as effective entropy models across codecs and modalities.

## Strengths

- **Consistent compression gains across three structurally different codecs**: The method works with classic DCT+scalar quantization (JPEG), neural VQ (VQGAN), and neural RVQ (SpeechTokenizer). Reporting BD-rate improvements (17.61% for VQGAN, 34.61% for SpeechTokenizer) across all three demonstrates generality beyond a single codec design.

- **Extremely parameter-efficient adaptation**: Table 3 shows that even for the largest vocabulary size tested (16,384), only 1.52% of LLaMA3-8B's parameters are updated. For smaller vocabularies (256 for JPEG), the fraction is well under 1%. This makes the approach practical for deployment on top of large backbones.

- **Empirically grounded LLM selection**: The paper benchmarks several recent LLMs on enwik9 text compression (Table 1) and selects LLaMA3-8B based on measured compression ratio and context length, rather than appealing to popularity or model size alone.

- **Systematic analysis of design trade-offs**: Section 5.3 examines chunk size effects (Figure 7), raster vs. zigzag flatten order (Table 5), and inference time per code (Figure 8, Table 4). This provides actionable engineering guidance beyond the headline numbers.

## Weaknesses

### Fatal
None.

### Major

- **JPEG latent-code truncation introduces unaccounted distortion, invalidating the headline BD-rate claim**: The paper states (lines 111–112) that for JPEG, "we empirically set the offset to 127 and the maximum value to 255, with all exceeding values truncated to 255." Quantized DCT coefficients in standard JPEG can exceed this range (the JPEG standard allocates up to 12 bits per coefficient). Truncation changes the latent codes themselves — the LLM-enhanced decoder receives different quantized values than the original JPEG decoder for the same quality factor. This introduces additional distortion beyond JPEG's own quantization step and means the comparison is no longer rate-distortion fair: the anchor JPEG and the LLM-enhanced JPEG are operating on different underlying data at the same nominal bitrate. The 54.07% BD-rate improvement cannot be trusted unless the paper either (a) extends the vocabulary to cover the full observed range, or (b) provides empirical evidence that truncation affects negligibly few coefficients (<0.1%) and measures the induced distortion. This is a structural flaw in the paper's most dramatic result — the VQGAN and SpeechTokenizer experiments are not affected by this issue because their codebooks define a closed set of values.

- **No comparison to a simple learned entropy model**: The paper compares LLM-enhanced codecs only against the original codecs' default entropy coders (JPEG's Huffman, VQGAN's basic entropy model, SpeechTokenizer's default). This conflates two effects: (1) the benefit of any adaptive/causal entropy model vs. a static one, and (2) the specific benefit of using a large LLM. Without a baseline that replaces the LLM with a small learned predictor (e.g., a lightweight transformer or PixelCNN-like model) using the same arithmetic coding, the paper cannot attribute the 17–35% gains to the LLM's scale rather than simply replacing a weak entropy model with any better one.

### Minor

- **Numerical inconsistency in the SpeechTokenizer BD-rate**: The abstract (line 4), the contribution list (line 25), and the experimental section (line 147) report 34.61% BD-rate improvement for SpeechTokenizer, but the conclusion (line 196) reports 36.61%. This discrepancy (2 percentage points) suggests a data error or revision artifact that must be resolved.

- **Separate LLMs per RVQ layer without cost analysis**: For SpeechTokenizer's 8-layer RVQ, the paper trains separate LLMs for each layer (line 123). This multiplies the memory and fine-tuning cost by 8×, yet the paper does not discuss whether a single conditional model (e.g., conditioning on layer index) would suffice or why separate models are necessary. The computational overhead of this design choice is not reported.

- **Fine-tuning percentage inconsistency**: The abstract and Section 5.3 state "<2% of parameters are fine-tuned," while Section 4.1 (line 105) says "less than 1%." Both can be true depending on vocabulary size (JPEG's 256 → <1%; VQGAN's 16,384 → <2%), but the text should be precise to avoid confusion.

### Trivial
- None.

## Nice-to-Haves
- Full rate-distortion tables (bpp and PSNR/VISQOL at each operating point) alongside the BD-rate numbers would aid independent verification (Figures 5–6 are visually hard to read numerically).
- An ablation comparing arithmetic coding with a small learned context model vs. the LLM would cleanly isolate the source of improvement.
- For JPEG, adopting a larger vocabulary (e.g., 512 or 1024) would avoid the truncation issue entirely with minimal overhead in fine-tuned parameters (<1% even for vocab 1024).

## Removed Points

- *Criticism that the paper overstates novelty by not discussing PixelCNN-like autoregressive models.* **Removed**: The paper claims "first work to introduce an *LLM-based* entropy model for transform coding," which is distinct from general autoregressive models. The claim is specific and reasonable.
- *Criticism that BD-rate is not reported in sufficient detail (requires full bit-per-pixel tables).* **Removed**: BD-rate computed from RD curves (Figures 5–6) is standard practice in the compression literature. The visual curves are sufficient for peer review.
- *Criticism about chunk size choices being ad hoc.* **Removed**: The paper provides a thorough chunk-size analysis in Figure 7 and explains the rationale behind the choices.
- *Criticism about the 4.62% CR being "extreme" and demanding an ablation to show it's not from using arithmetic coding.* **Removed**: The paper already analyzes compression ratio as a function of chunk size (Figure 7). That JPEG DCT coefficients are sparse is well known, and the paper does not claim the improvement is solely from the LLM prior.
- *Criticism about overfitting from 5 epochs on 13,830 images.* **Removed**: Speculative; the paper uses weight decay and evaluates on held-out datasets (Kodak, CLIC), which is standard.
- *Criticism about memory footprint not being discussed.* **Removed**: The paper discusses inference time (Table 4, Figure 8), which is the more directly relevant practical concern. Memory footprint is a standard cost of using an 8B-parameter model.
- *Criticism about not discussing the overhead of transform/inverse transform.* **Removed**: The anchor codec's transform cost is the same in both conditions; the incremental cost is the entropy coding step, which is what Table 4 reports.
- *All formatting, typo, and grammar nitpicks.* **Removed per instructions** (parser artifacts, not author errors).

## Novel Insights

The reviews surface one genuinely novel observation beyond what the paper itself articulates: the truncation issue in the JPEG experiment reveals a tension between LLM vocabulary constraints and unbounded latent code ranges — a challenge that is absent for VQ-based codecs (VQGAN, SpeechTokenizer) with closed codebooks but fundamental for scalar-quantization-based codecs. This structural difference means the method is not equally plug-and-play across codec families; DCT-based codecs with unbounded coefficient ranges require either sufficiently large vocabularies or evidence that truncation is negligible. This is an important design constraint that future work in this direction should address explicitly.

## Suggestions

1. **Fix the JPEG truncation**: Extend the vocabulary to cover the full range of observed quantized DCT coefficients (or at least demonstrate empirically that the induced distortion is negligible and does not affect the BD-rate calculation). Without this, the JPEG experiment cannot be published as a fair comparison.

2. **Resolve the SpeechTokenizer BD-rate inconsistency**: Correct the numerical discrepancy (34.61% vs. 36.61%) between the abstract/conclusion and ensure all reported numbers are consistent.

3. **Add a small learned entropy model baseline**: Compare against VQGAN/SpeechTokenizer with a lightweight transformer or LSTM-based entropy model using the same arithmetic coding to disentangle the benefit of "any learned predictor" from "an LLM-scale predictor."

4. **Clarify RVQ layer handling**: Discuss why separate LLMs are used per SpeechTokenizer layer and report the total parameter/computation cost of this design. Consider whether a single conditional model would suffice.
