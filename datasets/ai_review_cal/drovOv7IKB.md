- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3, 5
Now I have enough information to verify the claims. Let me write the consolidated review.

## Summary

The paper proposes FreCoformer, a Transformer model that operates in the frequency domain by patching DFT outputs into contiguous frequency bands and applying channel-wise attention to model cross-channel correlations per frequency band. A "divide-and-conquer" framework combines FreCoformer with a simple time-domain linear module (T-Net), and a lightweight Nyström variant is introduced. Experiments on eight multivariate forecasting benchmarks are reported.

## Strengths

1. **Frequency patching with channel-wise attention is a well-motivated design.** The method patches the full frequency spectrum into contiguous bands and applies independent channel-wise attention within each band. Figure 3(b) shows that this produces a more balanced energy distribution across the frequency spectrum compared to the input, evidencing that the mechanism extracts features beyond the dominant low frequencies — directly addressing the paper's stated motivation of capturing short-term (mid-to-high frequency) variations.

2. **The combined frequency/time framework shows genuine complementarity on data with different frequency characteristics.** Table 4 (Left) demonstrates that on ETTh1 (rich in high-frequency information) FreCoformer alone outperforms T-Net alone, while on Weather (low-frequency dominant) the reverse holds. The full framework outperforms both individual modules on each dataset. This provides concrete evidence that the two modules are complementary and that the combined model adapts to the dominant frequency characteristics of different datasets.

3. **Nyström variant offers practical efficiency gains.** Figure 4 and Table 5 show that the Nyström-FreCoformer reduces GPU memory substantially (e.g., on Weather from ~1.08 GB to ~0.56 GB) with negligible accuracy loss, and in some cases slightly improves accuracy. This is a practically useful contribution for scaling to high-channel datasets.

4. **Frequency patching with adjustable patch size tied to real-world phenomena.** Section 3.1 notes that the patch dimension P can be set based on domain knowledge (e.g., hourly sampling rates, alpha waveforms at 8–12 Hz), providing a practical mechanism grounded in known physical/physiological frequency ranges.

## Weaknesses

### Fatal
None.

### Major

1. **The L=512 comparison is unsubstantiated and the aggregated "63/64" claim is misleading.** The paper states that baselines were run at L=336 ("for fair comparisons") and that "we further explored the impact of an extended look-back window by evaluating with L=512" — but there is no mention of re-running any baseline at L=512. The natural reading is that FreCoformer at L=512 is compared against baselines at their default L (mostly 336 or 96). The 41 top-1 / 21 top-2 claims for L=512 depend on this comparison, and the aggregated "63 out of 64 top-1 considering both look-back window settings" collapses a fair setting (L=336) with a potentially unfair one (L=512). This is a significant experimental reporting flaw. The L=336 results (27 top-1, 34 top-2 out of 64) are fairly obtained; the paper should either run baselines at L=512 or restrict claims to the setting where all methods are compared on equal footing.

### Minor

1. **No standard deviations or statistical significance reported.** The strong top-1/ top-2 claims are presented without any indication of variance across runs. Given that many baselines are close in performance, it is impossible to assess whether the reported differences are stable or within noise. Time series forecasting papers in this subfield increasingly report variance across seeds; this would strengthen the paper.

2. **"Automatically identify relevant frequency components" claim is imprecise.** The method does not select or gate individual frequencies — it patches all frequency bands contiguously (with patch size P as a hyperparameter) and applies attention. The "automatic identification" occurs via attention weight learning, not through frequency selection. The framing could mislead readers into expecting a learned frequency masking mechanism. The paper's actual mechanism is still valid and interesting; the wording should be aligned with what the method does.

3. **DFT usage lacks clarification about Hermitian symmetry.** For real-valued input signals, the DFT produces a conjugate-symmetric spectrum (positive and redundant negative frequencies). The paper does not specify whether both halves are kept or only the positive frequencies (F = L/2+1). This affects the effective patch counts and the complexity analysis. Adding one sentence would resolve this.

4. **Nyström complexity analysis oversimplifies.** The paper states complexity reduces from O(L/P·C²) to O(L/P·C), but the Nyström approximation involves m landmark points; the actual complexity is O(L/P·(m·C + m²)). While m is typically a small constant in practice, omitting it from the stated complexity gives an incomplete picture.

5. **"Divide-and-conquer" is better described as an ensemble or multi-view model.** The two modules are trained jointly and their outputs summed. This is a multi-view ensemble (frequency-domain + time-domain), not a recursive decomposition. The name is not incorrect in spirit, but more precise framing (e.g., "complementary view ensemble") would better reflect the design.

6. **Ablation study would benefit from a stronger baseline.** The module ablation (Table 4, Left) only tests the two full modules in isolation and combined. Replacing FreCoformer with a simple linear model (or removing the frequency path entirely) would more directly establish the value added by the frequency-domain design, beyond showing that combining two things is better than either alone.

### Trivial

- The type of "patch-wise normalization" (line 68) is not specified (LayerNorm? BatchNorm?). "PreNorm" is mentioned, suggesting standard LayerNorm, but this should be stated explicitly for reproducibility.
- The paper would benefit from clarifying why treating channels as the token dimension (sequence length = C) is appropriate for this task, as this is an unconventional use of Transformer attention that is central to the method.

## Nice-to-Haves

- Provide standard deviations over multiple runs (at least 3 seeds) for main results.
- If possible, add a comparison with iTransformer, which similarly uses channel-wise attention (though in the time domain) and is a closely related contemporaneous work.
- Analyze which frequency ranges each module (FreCoformer vs. T-Net) focuses on by reconstructing their individual forecasts in the frequency domain, to better support the "divide-and-conquer" framing.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Missing contemporary baselines (iTransformer, TiDE):** The hard rule states "DO NOT mention missing related works, as you do not have external sources to confirm their existence and could be making things up." This criticism is removed per that rule.

- **TimesNet evaluation protocol asymmetry:** The paper gives TimesNet the better of L=96 and L=336, while the proposed method uses fixed L=336. The hard rule states to remove criticisms about unfair comparison if the asymmetry favors the baseline. This asymmetry benefits TimesNet, not the proposed method, so it is removed.

- **Table 3 rendered as image:** This is a PDF parsing artifact; the original submission has the table in readable form. Removed per formatting artifact rule.

- **Frequency selection is not learned (strong version):** The harsh critic asserted frequency selection is purely a hyperparameter and not learned. This overstates the case — the attention mechanism does learn to weight frequency bands differently. This is moved here as the criticism was partially strawman.

- **Strong claim about Nyström not enhancing high-channel datasets:** The harsh critic claimed the evidence in Table 5 is not convincing for Traffic (862 channels). The table is image-only and the exact numbers cannot be verified from the text version, so this speculative criticism is removed.

- **"Non-CW" ablation critique:** The harsh critic argued that replacing attention with a linear projection "cannot capture non-linear interactions that attention can" — this is circular reasoning, as the point of the ablation is precisely to test whether the non-linearity matters. Removed as strawman.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear structural issue (unfair L=512 comparison) but do not reveal any deeper insight about the method or problem beyond what the paper already presents.

## Suggestions

1. **Fix the L=512 comparison decisively.** Either (a) re-run all baselines at L=512 and report the fair comparison, or (b) restrict the paper's claims to L=336 where all methods are on equal footing, and remove or clearly caveat the aggregated "63/64" claim.
2. Clarify the DFT handling of Hermitian symmetry (positive frequencies only, or full spectrum).
3. Add standard deviations for main results over multiple random seeds.
4. Tone down the "automatically identify frequency components" language to match what the mechanism actually does (attention-weighted correlation learning per frequency band).
5. Include the landmark count m in the complexity statement for the Nyström variant.
