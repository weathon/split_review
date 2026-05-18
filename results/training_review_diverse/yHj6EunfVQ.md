Here is the consolidated final review:

---

## Summary

This paper proposes CoSPaL, a weakly-supervised spatio-temporal video grounding (WSTVG) method that adapts the open-vocabulary detector G-DINO to video by adding three components: (1) Tubelet Phrase Grounding (TPG) for spatio-temporal alignment via contrastive learning, (2) Contextual Referral Grounding (CRG) which uses GPT-3.5 to decompose queries into referral-specific sub-queries, and (3) Self-Paced Scene Understanding (SPS) for curriculum training that progressively increases scene complexity. CoSPaL achieves state-of-the-art weakly-supervised results, outperforming prior methods by 7.9% m_vIoU on HCSTVG-v1 and 3.9% on VidSTG, while using 1–3% of the GPU memory of fully-supervised approaches.

## Strengths

1. **Substantial and consistent performance gains**: CoSPaL outperforms the previous SOTA (WINNER) by large margins (7.9% m_vIoU on HCSTVG-v1, 3.9% on VidSTG declarative), with even larger relative improvements at stricter IoU thresholds (2× at vIoU@0.3, 3× at vIoU@0.5). These gains are verified across three benchmarks (Tables 2, 3).

2. **Clean ablation demonstrating individual contributions**: Table 5 provides a clear decomposition: TPG alone outperforms the W-GDINO baseline by +10% m_vIoU; adding CRG yields an additional +1%; adding SPS on top of TPG+CRG adds +1.1% m_vIoU and +3.4% m_tIoU. Each component is shown to be independently beneficial and complementary.

3. **Dramatic computational efficiency**: The paper explicitly reports single-GPU training, a frozen G-DINO backbone, and total memory usage of only 1–3% compared to fully-supervised methods (which require 8–32 GPUs). This is a practical strength for a weakly-supervised method aimed at reducing annotation costs without shifting the burden to compute.

4. **Controlled backbone comparison**: Table 6 compares CoSPaL against WINNER using the same Faster R-CNN backbone, isolating the methodological contribution from the benefit of a stronger foundation model detector. CoSPaL outperforms WINNER even with this weaker backbone, confirming that the gains are not merely driven by G-DINO.

5. **Well-motivated SPS curriculum**: The three-stage difficulty schedule (4, 7, then all tubelets) is simple but effective, with the ablation showing increasing gains at stricter metrics (e.g., +2.8% at vIoU@0.5), indicating that coarse-to-fine training genuinely improves precise localization.

## Weaknesses

### Fatal
None.

### Major

1. **CRG module lacks transparency on GPT-3.5 usage**: The paper states only that "We use GPT-3.5 to extract quantifier and phrases from original caption for CRG" (Section 4). While the supplementary (stripped by the parser) likely contains examples and additional details, the main paper does not specify: (a) whether this decomposition is performed offline as preprocessing or at inference time, (b) the exact prompt used, (c) the accuracy/reliability of the decomposition, or (d) how decomposition errors affect downstream performance. If GPT-3.5 is used only for offline preprocessing (which seems likely given it is listed alongside frame sampling and tracking choices), the authors should state this explicitly and commit to releasing the processed queries. If used at inference, dependence on a third-party API with version instability is a genuine concern. Given that CRG contributes ~1% improvement over TPG alone, this does not invalidate the core contribution, but it is the most significant gap in reproducibility.

### Minor

1. **No analysis of failure modes or limitations**: The paper does not discuss when or why CoSPaL fails — e.g., scenes with extreme occlusion, abstract/rare action descriptions, videos with very large numbers of tubelets, or cases where the SPS curriculum does not help. Understanding boundary conditions is essential for evaluating a weakly-supervised method's robustness.

2. **Single controlled comparison row in Table 6**: While Table 6 does provide a controlled comparison (CoSPaL with Faster R-CNN vs. WINNER), it only reports one metric configuration. Expanding this to the full set of metrics (m_vIoU, vIoU@0.3, vIoU@0.5, m_tIoU) would strengthen the claim that the proposed modules — not just the backbone — drive the improvement.

3. **No variance/seed reporting**: Results are reported as single numbers without standard deviations across random seeds. Given that some gains are modest (e.g., CRG contributes ~1%), confidence intervals would help assess reliability.

### Trivial
None beyond what can be attributed to PDF extraction artifacts.

## Nice-to-Haves
- An ablation replacing GPT-3.5-based CRG with a simple rule-based extraction (e.g., first noun phrase or POS-based heuristics) to quantify the value of LLM-based decomposition and determine whether the API dependency is necessary.
- Qualitative examples of CRG's query decompositions (these may already be in the supplementary material).

## Removed Points

- **Criticism about "unfair comparison" and numbers being inconsistent**: The critic initially expressed confusion about W-GDINO vs. WINNER numbers but then resolved it, acknowledging the results are consistent. Removed as the reviewer self-resolved.
- **"Temporal grounding module is not new / reconstruction is standard"**: The paper explicitly acknowledges building on prior reconstruction-based temporal grounding (Lin et al. 2020; Zheng et al. 2022a/b). The contribution is in the overall system integration and the novel combination with spatial contrastive learning and CRG — not in claiming novelty of the temporal module itself. Removed because it evaluates against the wrong expectation (a method paper can use standard components in a new combination).
- **"SPS is a simple curriculum / not compared to alternative measures"**: The paper provides a clear ablation showing SPS works. Simplicity is a virtue, and demanding comparisons to object density or motion complexity as alternative difficulty measures constitutes scope creep. Removed.
- **"Missing related works (e.g., Wan et al. 2023, CVPR 2024, ECCV 2024)"**: Per guidelines, missing related works should not be raised as a weakness since the reviewer cannot verify their existence/relevance without external sources.
- **"Sloppy notation"**: Attributed to PDF extraction artifacts, not author errors.
- **Demand to run WINNER with G-DINO backbone**: The paper already provides the symmetric controlled comparison (CoSPaL with the same backbone as WINNER). Asking for the reverse is not necessary to establish the contribution.

## Novel Insights

The harsh critic's observation that the core module CRG is a "black box" whose contribution is modest (~1% over TPG) is actually revealing: it suggests that the paper's main contribution may be the TPG+SPS pipeline rather than CRG. The strength finder's identification of the computational efficiency story (1–3% of fully-supervised GPU cost) as a key practical strength is well-taken — but notably, neither reviewer examined whether the frozen G-DINO approach might impose an upper bound on performance compared to fine-tuning the backbone, which would be a natural question for future work.

## Suggestions

1. **In the rebuttal/camera-ready, explicitly state whether CRG's GPT-3.5 decomposition is offline preprocessing or at inference, and commit to releasing the processed queries if preprocessing.** Provide the prompt template and a table of example decompositions with correctness analysis.
2. **Add a limitations section** that characterizes when CoSPaL underperforms (e.g., dense scenes, rare actions, long videos) and the failure patterns observed in qualitative analysis.
3. **Report results with standard deviations** across at least 3 random seeds, particularly for the metrics where margins are small.
4. **Expand Table 6** to report the full metric set (m_vIoU, vIoU@0.3/0.5, m_tIoU) for the controlled backbone comparison.

## Score and Decision

The paper makes a solid contribution to WSTVG: it demonstrates that a foundation model can be effectively adapted with well-designed, ablated components to achieve SOTA results while being dramatically more efficient than fully-supervised methods. The main weakness — insufficient transparency about CRG's GPT-3.5 usage — is addressable in a rebuttal. The core experimental evidence (TPG + SPS gains, controlled backbone comparison) is not undermined by this issue.

**Originality**: The integration of a modern open-vocabulary detector (G-DINO) with TPG and the SPS curriculum is novel in the WSTVG setting, though individual components draw from prior work.
**Quality**: Experiments are thorough with clear ablations and efficiency analysis; the CRG reproducibility gap is the main quality concern.
**Clarity**: Method description is mostly clear despite PDF artifacts; the CRG process is the least well-specified part.
**Significance**: SOTA results on standard benchmarks + dramatic efficiency gains make this practically relevant; the approach is likely extensible to other video grounding tasks.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>