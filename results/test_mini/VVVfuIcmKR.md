Now I have all the information I need. Let me compose the consolidated review.

## Summary

This paper identifies and systematically investigates a genuine issue with contrastively trained VLMs (like CLIP): the inter-modal contrastive loss that aligns image-text pairs leaves intra-modal similarities (image-image, text-text) uncalibrated, causing "intra-modal misalignment." The authors propose converting intra-modal tasks (e.g., image retrieval) into inter-modal ones by applying optimization-based modality inversion (OTI for images, OVI for text) at the single-feature level. Across 15+ datasets and 5 model variants (CLIP, OpenCLIP, SigLIP), they show that inter-modal comparisons (OTI-image) consistently outperform intra-modal baselines (image-image). Converging evidence from zero-shot classification (where inversion hurts), SLIP (where intra-modal losses narrow the gap), and modality-gap manipulation experiments further supports the causal story tying the modality gap to the observed misalignment.

## Strengths

1. **Well-framed problem with a clear root cause.** The paper provides a rigorous formal argument (Sec. 4) that CLIP's contrastive loss explicitly ignores intra-modal relationships, creating uncalibrated similarities. The toy experiment in Sec. 2 nicely illustrates the issue in concrete terms (81.4% mAP even after perfect inter-modal filtering).

2. **Consistent, broad empirical support.** Table 1 reports improvements on every combination of 15 datasets × 5 models — the consistency (not just the magnitude) is strong evidence that the phenomenon is systematic, not dataset- or architecture-specific. The pattern holds for text retrieval (Table 2 left) as well.

3. **Critical control experiment (zero-shot classification).** Table 2 (right) shows that applying OTI to an inherently inter-modal task (image→text classification) *hurts* performance dramatically (e.g., 56.0→17.9 on CIFAR100). This is the paper's strongest piece of evidence that the benefit comes from crossing modalities, not from inversion artifacts — the same inverted features help on intra-modal retrieval but hurt on inter-modal classification.

4. **Converging causal evidence from SLIP and modality-gap manipulation.** Table 3 shows that SLIP (which adds intra-modal losses) substantially reduces the OTI advantage, and Table 4 shows that closing the modality gap via high-temperature fine-tuning eliminates it entirely. These experiments tie the narrative together convincingly.

5. **Introduction of OVI for text→image inversion.** While OTI is adapted from prior work, OVI is new and extends the analysis to the text modality, showing the phenomenon is symmetric.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Improvement magnitudes are modest.** Many gains in Table 1 are 0.2–2.0 mAP. While the consistency across 75 (15×5) settings is impressive, the practical significance is limited, especially given the computational cost (150 optimization steps per query for OTI, 1000 for OVI). The paper honestly acknowledges cost as a limitation, but the modest gains and the computational overhead together constrain the approach's practical utility.

2. **No variance or significance reporting.** The paper reports single-run results without standard deviations or significance tests. Given the small improvements, one cannot rule out that some individual results could be within noise range — though the cross-dataset consistency mitigates this concern somewhat.

3. **The zero-shot classification degradation hints at information loss.** The dramatic drop in zero-shot classification (56→18 on CIFAR100) suggests OTI is lossy — it trades away semantic information. The paper frames this as supporting evidence, which it is, but the magnitude of the loss is worth deeper discussion. If OTI loses enough information to drop classification by ~38 points, why should readers be confident the retrieval gains come from better alignment rather than from some other artifact of the degraded representations? The paper's causal experiments (SLIP, modality gap) help here, but a direct analysis of what information is lost would strengthen the story.

### Trivial
None.

## Nice-to-Haves

- **OTI–OTI intra-modal baseline:** An experiment comparing OTI-inverted queries to OTI-inverted gallery features (both in text space) could further isolate whether the benefit is purely from crossing modalities. If OTI–OTI ≈ image–image, the inter-modality story is strengthened. If OTI–OTI > image–image, the inversion process itself contributes. The paper's zero-shot experiment partially addresses this concern, but a direct OTI–OTI comparison would be cleaner.
- **Image-text-image chaining baseline:** Comparing to a simple baseline that retrieves text nearest to the query image, then retrieves images nearest to that text, would test whether the benefit of OTI comes from optimizing individual query features versus simply exploiting the modality crossing more cheaply.
- **Qualitative examples of where OTI helps/fails:** A few case studies showing retrievals where OTI succeeds and the intra-modal baseline fails (and vice versa) would help build intuition for when this approach matters most.

## Removed Points

- **"Missing OTI-OTI control invalidates the core claim"** — The harsh critic presents this as a critical weakness, but the paper already addresses the same underlying concern via the zero-shot classification experiment (Table 2 right): the *same* OTI features help when the resulting comparison is inter-modal (OTI-image) and hurt when it is intra-modal (OTI-text). This directly shows the benefit is modality-dependent, not inversion-dependent. The OTI–OTI experiment would be a useful addition but is not required to support the core claim, and calling the evidence "insufficient" overstates the gap.
- **"The asymmetry between retrieval gains and classification losses suggests OTI is lossy and retrieval gains come from a different mechanism"** — The paper explicitly uses this asymmetry as supporting evidence for its claim (Sec. 6.3: "This experiment demonstrates that modality inversion does not inherently improve performance... Performance improvement is observed only when an intra-modal task is converted into an inter-modal one"). Framing this as an unaddressed weakness misreads the paper.
- **Claim that 81.4% mAP on Dogs vs Cats shows the problem "is not catastrophic"** — The paper never claims the problem is catastrophic; it quantifies it (28.5% of relevant images ranked below irrelevant ones) and uses it to motivate the investigation. The critic's characterization is a strawman.
- **Demand for ablation on regularization loss in OTI** — The paper explicitly justifies omitting the regularization loss to avoid external data influence (Sec. 5.1, "we aim to avoid influencing the inversion process with external data"). The cosine loss and Fig. 3c provide evidence the features stay on the text manifold. This is adequately addressed.
- **"No discussion of the possible lossiness of inversion in the Limitations section"** — The paper mentions computational cost as the primary limitation but also could have discussed lossiness. However, this is a minor omission, and the zero-shot experiment already surfaces the trade-off.

## Novel Insights

None beyond the paper's own contributions. The reviews largely concur with the paper's framing and contribution claims.

## Suggestions

1. Add variance estimates (or at minimum note single-run vs. multi-run status) to allow readers to assess the reliability of small improvements.
2. Consider adding the OTI–OTI control experiment and/or an image-text-image chaining baseline to further isolate the mechanism.
3. Include a brief analysis (or at least discussion) of what information OTI loses — a simple correlation study between OTI features and image features vs. class prototypes could help explain the classification degradation.
4. Add a few qualitative retrieval examples showing cases where OTI markedly improves or degrades results.

## Score and Decision

**Calibration anchors (all from the human-reviewed corpus):**

| Anchor | Avg Score | Comparison to this paper |
|--------|-----------|------------------------|
| `Dyo2tS5A8b` (What do we learn from inverting CLIP models?) | 4.25 | Much weaker — mostly qualitative, limited scope. This paper has far more rigorous and extensive experiments. |
| `wE8wJXgI9T` (It's Not a Modality Gap) | 4.75 | Similar topic area but less convincing empirical case. This paper is stronger. |
| `b2UlHeyyC0` (Retrieval-Enhanced Contrastive Vision-Text Models) | 5.67 | Proposes a method with larger practical gains. This paper has a stronger scientific analysis and broader evaluation. |
| `aPTGvFqile` (Mitigate the Gap) | 6.29 | Comparable empirical rigor but proposes a new training method. This paper is more of an analysis contribution. |
| `S5yOuNfSA0` (Understanding Transferable Representation Learning in CLIP) | 6.50 | Theoretical analysis of CLIP. Similar quality tier — both make solid contributions with thorough evaluation. |
| `uAFHCZRmXk` (Two Effects, One Trigger) | 8.00 | Deeper theoretical analysis with more novel insights. This paper is less theoretically ambitious. |

This paper makes a clear, well-supported scientific point about intra-modal misalignment in CLIP, backed by extensive experiments across 15+ datasets and 5 models with converging evidence from multiple controlled studies. The improvements are consistent but modest, and the practical applicability is limited by computational cost. The contributions are solid but not transformative. Positioning against the anchors, this paper sits comfortably above the 4–5 range papers and around the level of well-executed empirical analyses like aPTGvFqile (6.29) and S5yOuNfSA0 (6.50), though below the top tier of deep analytical work like uAFHCZRmXk (8.00).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>