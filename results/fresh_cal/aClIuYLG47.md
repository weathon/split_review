Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes VideoUntier, a text-video retrieval method that uses Part-of-Speech tagging to extract noun (object) and verb (event) tokens from text queries, then uses those tokens as queries in cross-attention over video frames to extract object-level and event-level visual features. Multi-grained (global, object, event) similarity scores are combined for retrieval, with a coarse-to-fine matching strategy for efficiency. Experiments on MSRVTT, DiDeMo, and MSVD show modest but consistent improvements over recent baselines like ProST, HBI, and UCOFIA, alongside a notable inference speedup.

## Strengths

1. **Novel pipeline for text-guided video feature extraction.** The paper introduces a specific combination of PoS-based token extraction (PTG) with language-guided cross-attention over video frames (LPVM) to produce explicit object and event visual tokens. Using text tokens as queries to drive attention over visual patches — then temporally aggregating object features into event features — is a coherent design that differs from prior fine-grained matching methods that primarily align pre-extracted patch tokens without text-guided extraction.

2. **Consistent empirical improvements across multiple benchmarks.** On MSRVTT-9k (Table 1), VideoUntier achieves 49.4% text-to-video R@1, outperforming ProST (48.2%), HBI (48.6%), and TS2-Net (47.0%). On DiDeMo (Table 3, text-to-video), it reaches 48.6% R@1 vs. ProST's 46.0% and UCOFIA's 47.6%. On MSVD (Table 5) it achieves 57.8% R@1 vs. ProST's 56.0%. These gains hold for video-to-text and with a stronger ViT-B/16 backbone (+2.1% over ProST on MSRVTT-9k). While the margins are modest, the pattern is consistent across all three datasets.

3. **Meaningful computational efficiency via coarse-to-fine matching.** The coarse filtering strategy (selecting H hard samples using global similarity before applying fine-grained alignment) provides a large practical speedup. Table 8 shows that with H=30, inference takes 20.07s on a single RTX 3090 vs. 227.01s for full fine-grained matching, with only a 0.2% R@1 drop (49.4% vs. 49.6%). This is arguably the paper's most impactful result and is properly ablated.

## Weaknesses

### Fatal
None.

### Major
None. The paper's methodology is sound and the core results are positive.

### Minor

1. **The central novelty claim is overstated.** The paper repeatedly claims (lines 23, 229) to be "an original effort in learning object and event features from videos with guidance from text queries in TVR." However, several prior works already perform fine-grained or token-level cross-modal interaction (e.g., HBI with cross-modal token interactions, ProST with token-level fine-grained alignment, TS2-Net with temporal matching). The specific use of PoS tagging to isolate noun/verb tokens is a practical engineering choice, not a fundamentally new paradigm. The paper would benefit from more precise positioning of its contribution — the specific pipeline design and efficiency advantage — rather than claiming novelty in the high-level direction.

2. **The ablation in Table 7 does not fully isolate the core claimed benefit.** The paper argues that language-guided disentanglement helps, but Table 7 shows the effect of adding object (S^o) and event (S^e) similarity terms to the loss. The +2.9% (adding S^o) and +4.2% (adding S^o+S^e) improvements could partly come from the additional supervised similarity terms rather than from the PoS-based language guidance in feature extraction. The paper does include one partial control: using only global features at inference, the method still outperforms CLIP4Clip by +0.7%, suggesting the training procedure improves representations. However, a direct control — using the same multi-grained similarity losses but without PoS-guided extraction (e.g., randomly initialized or learned tokens instead of PoS-based ones) — would more convincingly isolate the value of language guidance. This is the paper's single most consequential missing experiment.

3. **No statistical significance or variance reporting.** No error bars, confidence intervals, or multi-run averages are reported for any retrieval metric. Given that the improvements over strong baselines are modest (e.g., +1.2% vs. ProST on MSRVTT-9k, +0.6% vs. HBI on DiDeMo, +0.8% vs. HBI on MSRVTT-9k), it is unclear whether these are stable improvements or noise from a single run. Reporting mean and std over 3 seeds is standard practice and should be added.

4. **Key hyperparameter values and selection process are not reported.** The values of N_noun (number of noun tokens) and N_verb (number of verb tokens) are defined as architectural constants (line 93) but their specific values and how they were chosen (e.g., validation set search) are not stated. Similarly, the default H (number of hard samples) and K (top-K neighbors) used in main experiments are only clear from the ablation table, and the paper does not state which values were used for the main results in Tables 1–5. This affects reproducibility.

5. **It is unclear whether coarse filtering is used during training or only at inference.** The coarse filtering strategy (selecting H hard samples) is described in Section 3.5 in the context of efficiency during retrieval. The training objective (Eq. 13–15) computes similarity over all B×B pairs in a batch. The paper does not explicitly state whether the coarse filter is applied during training. If it is only an inference-time technique, there is a train-test mismatch in how similarity is computed. This should be clarified.

6. **The domain generalization experiment is insufficiently detailed.** The paper reports outperforming "recent works specializing in domain generalization (Jin et al., 2023b) by 2.6% and 2.2%" (line 197). However, only one domain generalization baseline (Jin et al., 2023b) and CLIP4Clip are compared. No description is given of the Jin et al. approach, its training data, or its intended setup — the reader cannot assess whether the comparison is appropriate. A comparison with standard TVR methods (e.g., ProST, HBI) under the same cross-domain setup would further strengthen the claim of improved feature robustness.

### Trivial

1. **The term "disentanglement" is somewhat loosely used.** The method separates video features into object, event, and global components guided by text queries, but does not separate independent factors of variation (e.g., content vs. style) as "disentanglement" traditionally implies. Terms like "query-guided feature decomposition" or "text-conditioned feature selection" would be more precise.

2. **Qualitative examples (Figure 3) are cherry-picked.** While this is standard practice, the claim that object/event tokens "accurately focus on relevant regions" would be strengthened by quantitative evaluation (e.g., attention alignment with ground-truth object annotations when available).

## Nice-to-Haves

- An ablation comparing the full method against one that uses the same multi-grained losses but with random/learned tokens (no PoS-based guidance) would directly test whether the language guidance itself drives improvement.
- Reporting performance on the MSRVTT-1k-A split (a standard test subset) would facilitate more direct comparison with works that only report on that split.
- The efficiency result (Table 8) is arguably the paper's strongest finding and could be emphasized more in the abstract and conclusion.

## Removed Points

These points from the reviewers were checked against the paper and removed:

- **Related work missing discussion of text-guided methods:** The related work section (line 30–32) ends mid-sentence and appears truncated by the parser (images/footnotes stripped). The original submission likely contains a fuller treatment. Removed per the rule that parser artifacts should not be treated as author omissions.

- **Event token length not explained:** The paper explicitly states at lines 126–127 that "the sequence length of the event features here is equal to the length of visual object features, not corresponding to the length of text event features." The reviewer missed this explanation. Removed.

- **Missing ablation of using only object-level or event-level features:** Table 7 already provides this comparison (global only, global+object, global+object+event). Removed.

- **Inference time comparison unclear:** The paper states (line 183) "The inference time is measured on a single NVIDIA RTX 3090 GPU." This provides the hardware context. Removed.

- **Criticism that baselines are "unnamed":** The paper explicitly names CLIP4Clip and Jin et al. (2023b) in Table 6 and the text. The cited reference exists. Removed per hard rules.

- **Appendix missing:** Removed per hard rule about parser-stripped content.

- **Tables presented as images:** This is a parser artifact. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviewers raised valid questions about experimental rigor and framing but did not uncover fundamentally new insights about the approach.

## Suggestions

1. Add a control ablation: train with the same multi-grained similarity losses but with learned/random tokens instead of PoS-based ones to isolate the effect of language guidance.
2. Report mean and std over 3 random seeds for all main results.
3. Tone down the "original effort" claim and position the paper's contribution more precisely as a specific, efficient pipeline design.
4. Clarify whether coarse filtering is used during training or only at inference.
5. Report the values of N_noun, N_verb, and default H/K in a table or in the method section.
6. Expand the domain generalization comparison to include standard TVR methods under the same cross-domain setup.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>