Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces VideoUntier, a text-video retrieval framework that uses a Part-of-Speech-based Token Generator (PTG) to extract object (noun-derived) and event (verb-derived) tokens from query text, then employs a Language-guided Progressive Vision Merging (LPVM) module to extract corresponding multi-grained video features. The model computes similarity at global, object, and event levels with a top-\(K\) matching mechanism and uses coarse filtering for efficiency. Experiments on MSRVTT, DiDeMo, and MSVD show consistent improvements over strong baselines like ProST and HBI, along with domain generalization gains.

## Strengths

- **Consistent state-of-the-art retrieval accuracy across multiple benchmarks**: VideoUntier achieves the best reported R@1 on MSRVTT-9k (49.4%, vs. 48.2% for ProST), DiDeMo (37.8%), and MSVD (53.8%) in text-to-video retrieval, outperforming recent fine-grained methods. These gains are supported by comparisons across Tables 1, 3, and 5.

- **Demonstrated domain generalization improvement**: When pretrained on MSRVTT and tested without fine-tuning on DiDeMo and MSVD, VideoUntier surpasses prior domain-generalization work DVD by 2.6% and 2.2% R@1 respectively (Table 6), providing concrete evidence that the text-guided object features produce more transferable representations.

- **Computational efficiency via coarse filtering**: The coarse-filtering strategy (selecting top-\(H\) hard samples for fine-grained comparison) reduces inference time to 20.1s on MSRVTT-9k while delivering 49.4% R@1, compared to 25.2s for ProST at 48.2% R@1 (Table 1). Table 8 validates this trade-off: using all samples increases time 11.3× with only 0.2% R@1 gain.

- **Ablative validation of multi-grained components**: Table 7 shows that adding object-level similarity to global similarity improves R@1 by 2.9%, and incorporating all three granularities yields a 4.2% total gain over global-only alignment, confirming each level contributes meaningfully.

## Weaknesses

### Fatal
None.

### Major

**1. The paper overclaims that event features are extracted under direct language guidance from text event tokens.**  
The paper repeatedly states (Abstract, Sec. 1, Sec. 3.1) that "object and event tokens from the text query guide the extraction" of both object and event video features. However, in the actual implementation (Sec. 3.4), the object merger genuinely uses text object tokens \(\{t^o\}\) as queries in cross-attention, but the "Temporal Feature Interaction" that produces event features \(\{v^e\}\) is simply a Transformer Encoder applied to the already-extracted object features with positional embeddings: \(\{v^e\} = \operatorname{Transformer-Enc}(\{v^o + p\})\). The text event tokens \(\{t^e\}\) are **not used as queries or guidance during event feature extraction** — they only appear in the event alignment loss (Eq. 13). This means the video event features are temporally aggregated object features, not directly conditioned on the query's event cues. The paper's central narrative — that text guides extraction of both objects and events — is only half-accurate. While the SOTA results are not invalidated by this issue, the framing misrepresents what the method actually does and would require either a corrected narrative that honestly characterizes the event features or a redesign of the event extraction to genuinely incorporate text guidance.

**2. The PTG module's design choices are heuristic and insufficiently validated.**  
The method indexes word positions by PoS tags (nouns → objects, verbs → events) and pads with other parts of speech when counts fall below fixed hyperparameters \(N_{noun}, N_{verb}\). Several concerns go unaddressed: (a) Nouns may not correspond to visual objects (e.g., "situation," "idea") and verbs may not correspond to visual events (e.g., "seem," "exist"), yet no analysis of tagging accuracy or token-to-concept mapping errors is provided. (b) CLIP's tokenizer can split a word tagged as a single noun into multiple subword tokens (e.g., "bookshelf" → "book" + "##shelf"), creating a potential misalignment between the word-level PoS index and the subword-level CLIP features — this is not discussed. (c) The effect of padding with non-noun/non-verb words is not ablated; the paper only states the priority order without showing how much padding occurs in practice or how it affects downstream performance. Since the entire extraction pipeline depends on these initial tokens, the lack of robustness analysis is a structural gap.

### Minor

**1. No statistical significance or variance estimates for main results.**  
Performance gains over strong baselines (ProST, HBI) are often 1–2% R@1. Without standard deviations or significance tests across multiple runs, it is unclear whether these differences are reliable rather than noise. This is particularly relevant given the modest margin of improvement on some benchmarks.

**2. Key hyperparameter values are not disclosed.**  
The paper defines symbols \(N_{noun}\), \(N_{verb}\), \(H\), \(K\), \(N_f\) (frames per video), and batch size \(B\), but does not state their actual numerical values in the text. While some may appear in the (unreadable) table images, the values should be explicitly reported for reproducibility and sensitivity analysis.

**3. The term "disentanglement" is used loosely.**  
The paper uses "disentangle" in the title and throughout the text to describe separating features into global/object/event levels, but there is no explicit disentanglement loss or constraint ensuring these representations are actually independent or complementary. The term carries a more specific meaning in representation learning (e.g., factorizing latent factors) that does not apply here. A less loaded term like "decomposition" or "separation" would be more accurate.

**4. Domain generalization results could be stronger with more comparisons.**  
Table 6 only compares against CLIP4Clip (reproduced) and DVD. Several other methods have domain generalization capabilities or evaluations that are not discussed, making it difficult to assess how significant the 2–3% improvement is relative to the broader field.

**5. Visualization analysis is purely qualitative.**  
Figure 3 shows attention maps with anecdotal claims (e.g., "the feature based on 'bus' accurately focuses on the bus area"), but there is no quantitative measure (e.g., IoU with ground-truth regions, or a user study) to substantiate that the extracted object features indeed localize correct regions.

### Trivial
None.

## Nice-to-Haves

- **Ablation: remove the object-merger's text guidance** — replacing object tokens with random or pooled text tokens as cross-attention queries would isolate the benefit of using specific noun-derived tokens, strengthening the causal claim.
- **Sweep over \(H\)** — Table 8 shows only two extremes (all vs. \(H\)=40); a sweep over intermediate values would demonstrate robustness of the efficiency-accuracy trade-off.
- **Redesign the event extraction to symmetrically use text event tokens as queries** (analogous to the object merger), which would make the pipeline fully support the "language-guided" claim, or alternatively, correct the narrative to honestly describe the current design.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The paper's novelty claim is overstated given precedents (JPoSE, cross-modal attention)"* — Removed because the paper does cite JPoSE in Related Work, and the specific combination (PTG + LPVM + multi-grained top-\(K\) alignment) is distinct. The novelty concern is better subsumed by Major Weakness #1 (narrative mismatch), which captures the real overclaiming issue more precisely.
- *"Coarse-filtering is a well-known heuristic (hard-negative mining)"* — Removed because the paper presents this as an efficiency technique, not a core novelty claim, and the empirical validation (Table 8) is sufficient.
- *"Missing comparison with methods that have domain generalization claims"* — Partially removed because asking for exhaustive comparisons across all domain generalization methods would expand scope beyond what is reasonable; kept in attenuated form as Minor #4.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the narrative for event feature extraction** — either (a) redesign the Temporal Feature Interaction to incorporate text event tokens \(\{t^e\}\) as queries (making the pipeline genuinely symmetrical), or (b) honestly describe the current design as temporal aggregation of text-guided object features and tone down claims about "language-guided event extraction."

2. **Add robustness analysis for the PTG module** — report PoS tagging accuracy on the datasets, analyze how often padding is triggered, study how subword token splits interact with word-level indexing, and ablate \(N_{noun}, N_{verb}\) to show sensitivity.

3. **Disclose all key hyperparameter values** (\(N_{noun}, N_{verb}, H, K, N_f, B\)) explicitly in the main text or a reproducibility table, and report results with variance estimates (multiple seeds or bootstrapped confidence intervals).

4. **Replace "disentanglement" with more precise terminology** (e.g., "decomposition" or "separation") to avoid misleading readers about the nature of the feature separation.

## Score and Decision

The paper makes a genuine empirical contribution: it proposes a text-guided object feature extraction pipeline for video retrieval that achieves SOTA results across three benchmarks with improved efficiency and domain generalization. The core strength — the language-guided object merger using noun tokens as cross-attention queries — is sound, well-validated, and produces consistent gains. The multi-grained similarity and top-\(K\) matching are sensible design elements supported by ablation.

The most significant issue is the mismatch between the claimed "language-guided event feature extraction" and the actual implementation (event features are temporal aggregates of object features, not directly guided by event tokens). This is a narrative problem rather than a methodological failure — the results are not invalidated — but it must be corrected before the paper accurately represents its own contribution. The PTG module's heuristic nature and lack of robustness analysis is a secondary concern that can be addressed with additional experiments or discussion.

Overall, the paper has real contributions and solid empirical support. The weaknesses are addressable and do not undermine the core findings.

**Score**: 7.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>