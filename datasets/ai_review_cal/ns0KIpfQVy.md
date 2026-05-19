- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 8, 3, 5
Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary

This paper introduces MBD (Multimodal Banking Dataset), a large-scale public dataset of ~1M labeled corporate clients with three event-sequence modalities (bank transactions, geo-position events, and technical-support dialogue embeddings) plus monthly product purchase labels. The paper provides benchmarks for two tasks: next-month purchase prediction (campaigning) and cross-modal client matching. The dataset fills a genuine gap — no existing public dataset offers multimodal event sequences at this scale — and the experiments show that relative model rankings are preserved under anonymization, supporting MBD's utility as a research proxy for proprietary banking data.

## Strengths

- **Largest-scale open-source multimodal event-sequence dataset.** MBD substantially exceeds prior financial datasets like DataFusion2022 (17K clients, single modality) with ~1M labeled clients, 950M transactions, 1B geo events, and 5M dialogue embeddings. This is documented in Sections 1–2 with exact counts, and the comparison to existing datasets in Section 5 (Related Work) is accurate.

- **Demonstrated preservation of model ranking after anonymization.** The central validation claim — that relative method rankings are identical between the public anonymized MBD and the original private data — is supported by Tables 1 and 2. For example, TabGPT on Trx achieves 0.802 (MBD) vs. 0.796 (private); Supervised on Trx+Dialog+Geo achieves 0.824 (MBD) vs. 0.821 (private); and the ordering across all method-modality combinations is stable. This is the strongest evidence that MBD can serve as a faithful research proxy.

- **Multi-task benchmark with realistic challenges.** The two tasks (campaigning and matching) reflect real business problems, and the data exhibits practical difficulties the paper acknowledges: missing modalities for many clients (Section 2), high class imbalance (81% clients with zero purchases, Section 2), and the need to handle asynchronous temporal events across modalities (Section 3).

- **Public release with fixed train/test splits and folds.** The dataset is on HuggingFace with explicit out-of-fold splits (Section 3.2.1), enabling direct comparability for future work.

## Weaknesses

### Fatal

None. The paper's core contribution — releasing the dataset — is not undermined by any single error.

### Major

- **The matching benchmark table contradicts its description, and claims about dialogue performance are unsupported.** Section 3.2.2 states that Table 3 "includes both transactions and dialogues" (line 315) and the caption reads "Transactions and Dialogues," but the table rows only show Trx2Geo and Geo2Trx. No dialogue-involving pairs (Trx↔Dialog, Geo↔Dialog, or any combination) appear. The text then asserts that "dialogue data consistently exhibits weaker matching performance compared to other modalities" (line 317) — a claim made without any data visible anywhere in the paper. This is not a missing detail; it is an empirical claim presented without evidence. The matching benchmark is one of the paper's two stand-alone tasks, so this gap must be corrected: either supply the missing results or revise the text to reflect what was actually evaluated.

### Minor

- **The claim of multimodal "superiority" is broader than the evidence supports.** The abstract states the results "demonstrate the superiority of our multi-modal baselines over single-modal techniques." The data in Table 2 tells a more nuanced story: adding Geo to Trx sometimes yields no gain or a slight drop (TabGPT: 0.802→0.800; TabBERT: 0.762→0.764; Supervised: 0.819→0.819). Adding Dialog helps consistently but by small margins (1–2%). The strongest formulation is that adding dialogue embeddings yields small but consistent improvements, while geo provides mixed results depending on the encoder. The current framing oversells the finding and should be tightened.

- **Inconsistent client count.** The abstract and introduction say "more than 1.5M" and "approximately 1.5 million" clients, while Section 2 reports 2,186,230 selected clients (of which 1M have purchase labels), and the conclusion says "1M bank clients." It is unclear whether the released dataset contains all 2.18M clients (with 1M labeled), or 1.5M, or some other number. This should be clarified, as dataset size is a headline claim.

- **Blending fusion method mentioned but results not shown.** Section 3.1 describes blending (weighted sum of scores) as a fusion technique alongside late fusion, but Table 2 is explicitly labeled "late fusion setting" and no blending results are reported in the main paper. The authors should either include blending results or remove the mention from the methods section.

- **Dialogue baselines are weak.** The dialogue modality uses only mean pooling and last-embedding aggregation (Section 3.1). These are appropriate as simple baselines, but the paper does not provide a stronger sanity check (e.g., a small GRU or attention-based aggregator on the dialogue embedding sequence). The Supervised dialogue model achieves an anomalously low 0.540 AUC — below mean pooling's 0.595 — which the paper does not discuss. This gap weakens the dialogue-focused claims.

- **Three geohash precisions not clearly scoped.** The paper states that geo coordinates are encoded at precisions 4, 5, and 6 (Section 2) but does not specify how these are used — as separate features, concatenated, or selected. This is a small clarity issue that should be addressed.

### Trivial

- Table 2 uses multiple row colors (purple, gray, blue, red) without a legend. This makes the table harder to parse than necessary.

## Nice-to-Haves

- Provide a summary statistics table (sequence length quantiles, missing-modality rates per client, number of clients per modality) in the main text rather than deferring entirely to figures.
- Add a simple Spearman rank correlation between MBD and private dataset results, with a confidence interval, to quantitatively support the qualitative claim about ranking preservation.
- Include a brief pseudocode snippet or loading guide for the HuggingFace dataset to lower the entry barrier for new users.
- Report paired statistical tests (e.g., Wilcoxon) across folds to clarify which multimodal gains are reliable.

## Removed Points

These points were raised in the reviews but are excluded from the main weakness list for the following reasons:

- **Anonymization noise parameters not disclosed (Harsh Critic):** The paper explicitly states (lines 84–86) that "the specific parameters of the noise are not disclosed to prevent potential attacks on the dataset." This is an intentional security measure, not an oversight. Removed.
- **Commented-out text in LaTeX source (Harsh Critic):** These are source-code artifacts that do not appear in the compiled PDF. Removed as a formatting nitpick.
- **Truncated HuggingFace link in abstract (Harsh Critic):** This is a line-break artifact from the PDF text extraction process, not an error in the actual submission. Removed.
- **Color coding unexplained in tables (Harsh Critic):** This is a minor presentation issue that does not affect the substance. Moved to Trivial.
- **Generic strengths from Strength Finder:** Strengths that were generic ("addressed an important problem," "valuable resource for the community") without specific grounding in the paper's content were removed. Only concrete, evidence-backed strengths are retained.

## Novel Insights

The harsh critic and strength finder together surface a useful observation that is not explicitly discussed in the paper: the matching task results (Recall@1 of 0.004–0.006 for Trx↔Geo) are near floor-level, suggesting that cross-modal matching from raw behavioral sequences is an extremely difficult unsolved problem even at industrial data scale. This fact — more than the campaigning results — may be what makes MBD a uniquely challenging benchmark for the multimodal sequence learning community. The paper presents the matching results but does not highlight how remarkably hard this task is relative to typical multimodal alignment benchmarks (e.g., CLIP-style image-text retrieval).

## Suggestions

- **Fix the matching table immediately.** This is the most critical issue. Either populate Table 3 with results for all modality pairs you evaluated (including dialogue-involving pairs), or, if only Trx↔Geo was evaluated, correct the text and caption to say so and remove the unsubstantiated claims about dialogue modality performance.
- **Revise the abstract and conclusion** to state the multimodal finding precisely: "Adding dialogue embeddings yields small but consistent improvements (1–2% ROC AUC), while geo provides mixed results depending on the encoder." Avoid blanket "superiority" language.
- **Resolve the client-count inconsistency.** State exactly how many clients are in the released dataset, how many have labels, and how the 1.5M figure arises (e.g., "1.5M clients with at least one modality present, of which 1M have purchase labels").
- **Either show blending results or remove the mention** from the methods section to avoid raising expectations the paper does not meet.
