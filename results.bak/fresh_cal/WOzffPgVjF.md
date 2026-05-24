Now I have thoroughly read the paper and verified the reviewer's claims. Let me synthesize the final review.

---

## Summary

This paper proposes TA-STVG, a Transformer for spatio-temporal video grounding that replaces standard zero-initialized object queries with queries generated from target-specific cues in the video-text pair. Two cascaded modules — Text-guided Temporal Sampling (TTS) for selecting target-relevant frames and Attribute-aware Spatial Activation (ASA) for extracting fine-grained appearance/motion attributes — produce queries that carry discriminative target information into the decoder. Experiments on HCSTVG-v1/v2 and VidSTG achieve state-of-the-art results, and the modules generalize to other architectures (TubeDETR, STCAT).

## Strengths

- **Oracle experiment provides direct causal evidence for the central motivation (Figure 2).** The paper demonstrates that replacing zero-initialized queries with groundtruth-generated queries yields +18.0% m_IoU and +13.5% m_vIoU absolute gains on HCSTVG-v1. This is not a correlation argument — it isolates query initialization as the bottleneck, which directly justifies the paper's direction.

- **State-of-the-art results across three benchmarks with consistent gains (Tables 1–3).** TA-STVG outperforms prior methods on all metrics on HCSTVG-v1 (e.g., +1.6% vIoU@0.3 over CGSTVG), all four metrics on HCSTVG-v2, and all eight metrics on VidSTG for both declarative and interrogative sentences. The improvements are not cherry-picked.

- **Thorough ablation isolates each component's contribution (Tables 4–9).** The paper independently ablates TTS and ASA (Table 4: +2.3%/+1.5%/+3.1% for TTS alone/ASA alone/both), the appearance/motion branches in TTS (Table 5), the attributes in ASA (Table 6), the activation strategy (Table 7), and the hyperparameters δ and θ (Tables 8, 9). This granularity lets the reader see exactly what drives improvements.

- **Generality validation on other architectures (Table 10).** Plugging TTS and ASA into TubeDETR yields +2.3%/+1.9% m_tIoU/m_vIoU and into STCAT yields +1.7%/+1.8% gains. This shows the modules are not tied to one architecture and that target-aware query generation is a broadly beneficial strategy.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Attribute label generation is described only at a high level in the main paper.** The paper states that "explicit weak attribute labels" are generated from the textual expression (line 178–179) and gives examples of attribute types (color, shape, action, line 176), but the extraction mechanism (e.g., predefined vocabulary, parser-based extraction, or LLM prompting) is deferred entirely to the supplementary material. Since the ASA module's effectiveness depends on these labels, a brief sketch in the main paper — even one sentence describing the extraction approach — would let readers assess the method without consulting supplementary material.

- **The comparison in Table 7 (ASA vs. instance-level activation) uses different supervision signals**, which makes it not a pure ablation of activation strategy. ASA uses weak attribute labels (from text), while the instance-level baseline uses dense binary masks from groundtruth boxes. Notably, the baseline receives *stronger* supervision (accurate, per-frame box masks) yet performs worse, which actually strengthens the paper's claim that attribute-specific activation is beneficial. However, a cleaner comparison with matched supervision (e.g., both using attribute labels, or both using box masks) would eliminate the confound. This does not invalidate the result but limits precision of the ablation.

- **Gains over prior SOTA on some metrics are modest** (e.g., +0.1% m_vIoU on HCSTVG-v1 over CGSTVG). The paper describes these as "significantly outperforming" — which is defensible given the saturated nature of these benchmarks and the much larger gains (+2–5%) over the fair baseline (same architecture with zero queries). Still, the language slightly overstates the SOTA margins.

- **Variance across runs is not reported.** The modest SOTA margins would benefit from confidence intervals to assess stability. This is common practice in the field, so it is not a methodological gap, but it would strengthen the empirical case.

### Trivial
None.

## Nice-to-Haves

- Compare the TTS hard-threshold sampling (θ=0.7) against soft weighting or top-k sampling as an additional ablation.
- Add a brief description of the subject extraction method in the main paper rather than deferring entirely to supplementary.
- Include a Limitations section discussing when the method might struggle (e.g., ambiguous textual descriptions, occluded targets, failure cases of TTS/ASA).

## Removed Points

These points were considered and removed with justification:

1. **"ASA comparison conflates supervision signals" framed as weakening the paper's claim.** The reviewer argued the comparison in Table 7 is unfair because instance-level activation uses dense box masks while ASA uses weak attribute labels. However, the direction of the potential bias favors the baseline (stronger supervision), not ASA. The fact that ASA outperforms instance-level activation *despite* weaker supervision makes the result *more* convincing, not less. The criticism was kept in a weakened form above as a precision concern, but the claim that it "weakens the specific claim" is not supported.

2. **"TTS hard threshold could discard marginally relevant frames; no comparison against soft weighting."** This is a reasonable suggestion for an additional ablation but not a weakness of the current method. The paper provides ablations for the threshold θ (Table 9) showing the optimal value, which is sufficient. Moved to Nice-to-Haves.

3. **Formatting, style, and grammar nitpicks** (parser artifacts, not author issues). Removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Provide a one-paragraph description of how attribute labels are extracted from text in the main paper (e.g., "we use a dependency parser to extract the target noun phrase and map adjectives/verbs to a predefined attribute vocabulary of 15 appearance and 10 motion classes"). This addresses the most significant clarity gap.
- Add confidence intervals or standard deviations for the main results to contextualize the modest SOTA margins.
- For the Table 7 comparison, optionally run an additional ablation where the instance-level baseline is also trained with the same weak attribute labels (keeping supervision identical) to further strengthen the claim.

## Score and Decision

The paper makes a clear, well-executed contribution to STVG. The oracle experiment convincingly motivates the approach, the method is clean and modular, the ablations are thorough, and the generality experiments demonstrate broad applicability. The weaknesses are minor and do not threaten the core claims.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>