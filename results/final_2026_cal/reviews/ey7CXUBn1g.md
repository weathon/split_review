Now I have sufficient calibration data to produce the final review. Let me synthesize everything.

## Summary

The paper proposes AdaSVD, an SVD-based LLM compression method with two components: **adaComp** (alternating update of U and V^T using Moore-Penrose pseudoinverses to compensate for truncation error) and **adaCR** (adaptive layer-specific compression ratios based on cosine similarity between layer inputs and outputs). The method is evaluated on LLaMA2-7B, OPT-6.7B, Mistral-7B, and Vicuna-7B across perplexity and zero-shot reasoning benchmarks, consistently outperforming SVD-LLM.

## Strengths

1. **AdaComp provides a technically sound approach to post-truncation compensation.** The alternating update of U and V^T via Moore-Penrose pseudoinverse (Eqs. 8–13) is a principled way to minimize the reconstruction error $\|\mathcal{U}_k^\sigma \mathcal{V}_k^\sigma \mathcal{X} - \mathcal{W}\mathcal{X}\|_F^2$, and Figure 3(a) empirically shows it yields stable MSE reduction (smooth curve) compared to the naive update. The stack-of-batch strategy (Eqs. 14–15) is a practical solution to fitting more calibration data under GPU memory limits, with Figure 3(b) demonstrating improved MSE stability.

2. **AdaCR offers a simple and effective adaptive compression ratio scheme.** Figure 4 convincingly shows that layer importance varies substantially across models (the first layer always being most important), and Table 3b demonstrates that adaptive ratios improve over uniform ratios at every tested compression ratio (e.g., WikiText-2 PPL drops from 27.33 to 25.58 at 50% target ratio). The ablation is clean and well-controlled.

3. **Thorough experimental evaluation across model families and metrics.** The paper evaluates on 4 LLM families (LLaMA2, OPT, Mistral, Vicuna) plus VLMs (LLaVA), across 3 language modeling datasets and 5 reasoning benchmarks, at compression ratios 40–80%. Table 1 shows consistent improvements over SVD-LLM at all settings. Table 4 further demonstrates orthogonality with GPTQ quantization — a practically relevant property.

4. **Comprehensive ablation study.** Table 3 systematically ablates the effect of adaComp (3a), adaCR (3b), iteration count (3c), and minimum retention ratio (3d), providing clear evidence about which component contributes how much.

## Weaknesses

### Major

1. **Figure 1 caption is inconsistent with Table 1 data, creating a misleading visual summary.** The Figure 1 caption states the y-axis is "Perplexity in log10 Scale (Y-axis, ranging from 10^0 to 10^2)" and claims to compare vanilla SVD alongside other methods. However, Table 1 reports vanilla SVD perlexity at 40% = 39,661 (log10 ≈ 4.6), which is far above the stated axis maximum of 10² = 100. Vanilla SVD cannot be plotted on this axis range. Either the figure does not actually show vanilla SVD (making the caption misleading), or the axis range is misstated, or the figure data is inconsistent with Table 1. While the tabular results are clear and the core contribution rests on the tables, this figure caption misleads readers about what is being displayed and raises unnecessary questions about data integrity. The authors must clarify what is actually plotted and correct the caption to accurately describe the figure content.

2. **Gains over SVD-LLM at practical compression ratios are modest.** At 40% compression (the most practically relevant setting), AdaSVD achieves WikiText-2 PPL 14.76 vs. SVD-LLM's 16.11 — an ~8% relative improvement. At 50%, the improvement is ~6% (25.58 vs. 27.19). Accuracy gains on reasoning benchmarks are similarly modest (e.g., average accuracy 42.63% vs. 40.69% at 40%). While consistent, these improvements are incremental, and the paper would benefit from discussing whether the additional complexity of alternating updates is justified by the magnitude of gains at moderate compression ratios.

3. **Theoretical justification for cosine-similarity-based importance is weak.** The paper states (Eq. 17) that layer importance = similarity(input, output) = cosine similarity(X, Y). High cosine similarity between input and output can equally indicate that a layer does minimal transformation (identity-like behavior, thus less important) or that it performs a critical transformation that preserves direction. The paper does not justify why this specific measure captures "importance" for compression purposes — i.e., why retaining more parameters in high-cosine-similarity layers preserves model quality. Figure 4's empirical result that the first layer has consistently high similarity is plausible (embedding layers differ from the rest), but the paper does not validate that the metric assigns appropriate importance across all layers (e.g., by comparing against an oracle or gradient-based importance measure).

### Minor

1. **FWSVD and ASVD baselines essentially collapse** at the tested compression ratios (perplexities in the thousands), making them uninformative comparisons. The paper acknowledges this ("FWSVD and ASVD fail on these LLMs with compression ratios under 60%"), and the primary comparison is with SVD-LLM, so this is not a fatal flaw. However, the space devoted to these baselines could be reduced.

2. **Limited to 7B-scale models.** The largest model compressed is 7B parameters. While this is consistent with related work (SVD-LLM, ASVD all test at similar scales), the paper's claim of generalizability would be stronger with at least one result on a 13B or 30B model, especially since the method involves per-layer SVD which may face practical challenges at larger scales.

### Trivial

- None that are not parser artifacts.

## Nice-to-Haves

- A comparison of the proposed importance metric (cosine similarity) against an alternative importance measure (e.g., gradient-based, or reconstruction-error-based) would strengthen the motivation for adaCR.
- Reporting the wall-clock time cost of the alternating update procedure vs. SVD-LLM's single-pass update would help practitioners assess the trade-off.
- Discussion of whether 1 iteration of adaComp is sufficient at low compression ratios (Table 3c shows it is), and what drives the overfitting at higher iteration counts.

## Removed Points

- **Harsh critic's "data fabrication / fatal inconsistency" characterization of Figure 1.** Removed because: the parser-generated "table" of ~1.1–1.2 values between the image tag and the caption is a PDF extraction artifact from OCR'ing the embedded JPG — it is not paper-authored data and cannot be used as evidence. However, the underlying concern about the figure caption being inconsistent with Table 1 is retained as a Major weakness (see above), as it is verifiable from the caption text and Table 1 data alone.

- **Harsh critic's claim that FWSVD/ASVD are "straw men."** Removed. The paper explicitly acknowledges they fail at these ratios (Sec. 4.2: "FWSVD and ASVD fail on these LLMs with compression ratios under 60%") and the primary comparison is with SVD-LLM. Including them is standard practice for completeness.

- **Strength Finder's strength about Figure 3(a) showing smooth MSE decrease.** Retained but moved to Strengths section, as it is well-supported by the paper.

- **Strength Finder's strength about stack-of-batch strategy (SoBC).** Retained as a supporting point in Strengths section, as Figure 3(b) provides clear evidence.

## Novel Insights

None beyond the paper's own contributions. The paper is a clean engineering contribution: applying an alternating Moore-Penrose update to SVD-truncated matrices and using input-output cosine similarity for adaptive compression ratios. Both ideas are well-executed but follow straightforwardly from the problem formulation.

## Suggestions

1. **Fix Figure 1.** Either (a) show vanilla SVD by extending the y-axis to accommodate it (though this would compress the relevant methods), or (b) restrict the figure to methods that fit in the 10^0–10^2 range and explicitly note in the caption that vanilla SVD/FWSVD/ASVD are off the chart (or are omitted). Then verify that all plotted values match Table 1 exactly.

2. **Validate the cosine-similarity importance metric** against an alternative (e.g., using held-out calibration data to measure per-layer reconstruction error sensitivity, or comparing against a gradient-based importance measure on a small subset).

3. **Add a complexity/runtime comparison** with SVD-LLM, especially the cost of the alternating update iterations (which can be run for multiple rounds) versus SVD-LLM's single sequential pass.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched for SVD-based LLM compression papers across three bands.

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| ERC-SVD (WL4qCY0nBk) | 2.50 | R1 | Significantly weaker; arbitrary design choices, limited novelty |
| AA-SVD (fIpDd5UlFP) | 2.50 | R1 | Weaker; less thorough evaluation |
| LayerDecompose (0IWZjbMmry) | 3.00 | R1 | Different approach (weight sharing vs SVD) |
| Adaptive Nonlin. Comp. (p66qXIp5jv) | 4.00 | R1 | Accepted poster, different technique |
| Distribution-Aware Whitening (89Cafo48YM) | 4.50 | R1 | Comparable breadth but split reviews (2,8,6,2) |
| DF-SVD (TuzsCiHocG) | 5.00 | R1 | Similar topic, rejected; stronger theory but comparable evaluation |
| SAES-SVD (KMAYsQO8pU) | 5.00 | R1 | Accepted poster; stronger theory, narrower model coverage |
| Repr. Drift Comp. (9I1G8PjEnA) | 5.00 | R1 | Similar quality, rejected |

**Initial bracket: 4.0 – 6.0**

**Round 2 (Narrowing):** Searched within the bracket to refine.

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| SAES-SVD (KMAYsQO8pU) | 5.00 | R2 | Accepted poster; stronger theoretical analysis but AdaSVD has broader model coverage |
| DF-SVD (TuzsCiHocG) | 5.00 | R2 | Rejected; comparable quality, both incremental over SVD-LLM |
| Distribution-Aware Whitening (89Cafo48YM) | 4.50 | R2 | Rejected; mixed reviews |
| Repr. Drift Comp. (9I1G8PjEnA) | 5.00 | R2 | Rejected; comparable approach |

AdaSVD is comparable to DF-SVD and SAES-SVD (both anchored at 5.00). It has broader model coverage than SAES-SVD and more thorough ablations than DF-SVD, but its theoretical depth is shallower than SAES-SVD and its key figure is misleading. The Figure 1 issue (a real presentation flaw, though not data fabrication) differentiates it negatively from SAES-SVD which was accepted. Setting the score at 5.0 positions it comparably to these anchors.

**Final score: 5.0. Decision: Reject.** The paper has a useful technical contribution and solid experiments, but the Figure 1 inconsistency undermines presentation integrity, and the improvements over SVD-LLM are modest at practical compression ratios. With corrections, it could be reconsidered.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>