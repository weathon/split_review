- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 6, 5, 5
Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper proposes RagVL, a three-stage pipeline for multimodal RAG: (1) CLIP-based image retrieval, (2) instruction-tuned MLLM as a reranker with adaptive thresholding to filter top-*N* candidates, and (3) noise-injected training (NIT) — at both the data level (hard negative sampling) and token level (logit contrasting with distorted images) — to make the generator robust to noisy correspondences. Experiments on WebQA and MultimodalQA show that the reranker substantially improves retrieval quality (e.g., LLaVA-v1.5-13B R@2 on WebQA from 45.35 to 79.74) and that the full pipeline with NIT achieves strong generation performance approaching oracle-level accuracy.

## Strengths

1. **MLLM reranker dramatically improves retrieval quality.** Table 1 (tab:main_retrieval_results) shows that caption-aware instruction tuning boosts recall across five different MLLMs by large margins — e.g., InternVL2-2B R@1 on MultimodalQA goes from 66.52 to 98.26, and R@2 on WebQA from 42.79 to 81.91. The benefit is consistent regardless of which initial retriever is used (CLIP, Vis-BGE, or InternVL).

2. **Adaptive thresholding further refines retrieval precision.** Table (tab:internvl_retrieval_results) reports that with the adaptive threshold on WebQA, precision rises from 59.26 (reranker alone) to 88.34, while maintaining a strong F1 of 77.03. This validates the filtering mechanism that complements the reranker.

3. **Noise-injected training improves generation robustness.** Table (tab:internvl_rag_results) shows NIT lifts InternVL2-1B overall accuracy from 43.79 to 61.72 and InternVL2-2B from 44.67 to 62.23. The attention heatmaps in Figure 4 provide qualitative evidence that the NIT-trained model produces more focused attention on relevant image regions.

4. **Ablation studies isolate each component's contribution.** Table (tab:intern_ablation) shows that removing the reranker, noise-injected data (ND), or noise-injected logit contrasting (NLC) each hurts overall accuracy on WebQA (from 64.25 down to 61.70, 63.39, and 63.52 respectively), with the largest drop when both ND and NLC are removed (62.42). This cleanly validates the design.

5. **Cross-dataset and low-resource generalization are demonstrated.** Figure 2(a) shows a reranker trained on WebQA transfers competitively to MultimodalQA, and Figure 2(b) shows that with only 2.5% of WebQA training data the reranker still outperforms the strong InternVL-G retriever on R@2.

## Weaknesses

### Fatal
None.

### Major

1. **The "RagVL w/o NIT" baseline in the generation table is not comparable to the ablation's "w/o ND & NLC" condition — but the paper does not clarify this.**  
   The critic noticed that Table (tab:internvl_rag_results) reports "RagVL w/o NIT" for InternVL2-2B as 46.60 (with natural threshold) while the ablation (tab:intern_ablation) reports "w/o ND & NLC" as 62.42 — a 16-point gap. **This is not actually an inconsistency**: "RagVL w/o NIT" in Table 2 uses the *base MLLM* as a zero-shot generator (scores close to the CLIP-retrieval baseline of 44.39), whereas the ablation conditions all involve *fine-tuning* the generator on the dataset (the "w/o ND & NLC" model is fine-tuned with noise components removed, giving 62.42). The 16-point gap is thus the benefit of dataset-specific fine-tuning of the generator, not a contradiction.  

   **However**, the paper never explicitly states that "RagVL w/o NIT" means zero-shot evaluation of the base MLLM generator. The figure caption in the qualitative analysis (Figure 4) mentions "the model fine-tuned w/o NIT," further muddying the terminology. This conflates "without noise injection" and "without any fine-tuning" into the same label across different contexts. The result is that a reader cannot tell, from the tables alone, how much of the reported gain comes from noise injection vs. from simple supervised fine-tuning on the dataset. The ablation clarifies that NIT itself contributes ~2 points (64.25 vs. 62.42), but the paper does not acknowledge that the headline "NIT gain" of ~18 points in Table 2 actually conflates fine-tuning + NIT together. **The paper needs to either (a) report a "fine-tuned w/o NIT" baseline in the main generation table so that the reader can cleanly decompose the gains, or (b) explicitly state that "RagVL w/o NIT" uses the base model zero-shot.**

2. **No direct comparison to existing multimodal RAG methods (MuRAG, SKURG).**  
   The paper claims to "advance multimodal RAG" but only compares against CLIP-based retrieval, InternVL-retrieval, and non-retrieval MLLMs. MuRAG and SKURG are mentioned in related work but do not appear in any experiment. The paper argues that none of these works address MNC specifically, but since the contribution is a *multimodal RAG system*, the absence of direct head-to-head comparison with the two best-known prior multimodal RAG systems makes it impossible to assess whether RagVL is competitive as a RAG system beyond its specific methodological components. This is a significant omission that weakens the "advancing" claim.

### Minor

3. **Generator training details for the "w/o NIT" condition are underspecified.**  
   The paper describes NIT training in detail but never specifies what training (if any) the "RagVL w/o NIT" generator receives. The scores suggest it is used zero-shot, but the paper should state this explicitly. Similarly, it is unclear whether the ablation models (including "w/o ND & NLC") are all trained with the same hyperparameters, number of epochs, and optimizer as the full NIT model.

4. **Adaptive threshold selection uses the same validation set as evaluation.**  
   The paper states that the adaptive threshold is determined "on the validation set" by finding the intersection point of correct/incorrect recall curves, and results are reported on the validation set (line 123: "Since the test set labels… are not publicly available, we report the results on the validation set"). This introduces optimism in the adaptive threshold results. However, the natural threshold (η=0.5) results do not suffer from this issue and still show consistent improvements, which partially mitigates the concern.

5. **No error bars or significance tests.**  
   Key comparisons (e.g., ablation differences of 1–2 points) could fall within noise. Single-run evaluation without standard deviations is standard in this field but limits the reader's ability to assess confidence, especially for small-margin improvements.

6. **Missing details: K (initial retrieval count) and N (reranked count) are not reported.**  
   The paper discusses top-*K* retrieval and top-*N* reranking but never states the specific values used. These are needed for reproducibility.

### Trivial

- None distinct from the above.

## Nice-to-Haves
- A "fine-tuned w/o NIT" row in the main generation table (Table tab:internvl_rag_results) would cleanly separate the effect of fine-tuning from the effect of noise injection.
- The connection to VCD (Leng et al., 2024) is cited but could be discussed more explicitly: the main novelty relative to VCD is applying the logit-contrasting idea during *training* rather than inference and combining it with data-level noise injection.

## Removed Points

- **"Table 2 and Table 3 directly contradict each other" (Harsh Critic Point 1, as stated):** This claim is factually incorrect. The conditions are different — the "RagVL w/o NIT" entry in Table 2 uses the base MLLM zero-shot (not fine-tuned on the dataset), while the ablation's "w/o ND & NLC" entry fine-tunes the generator on the dataset. The paper should be clearer about this, but there is no contradiction. MOVED TO Major Weakness #1 (reframed as a clarity/terminology issue).

- **"The paper overclaims the reranker's role" (Harsh Critic Point 2):** The critic argues that the reranker contributes only +2.2 points on generation accuracy. However, the reranker's primary evidence is in *retrieval quality* (Table 1), where it shows massive improvements. The title "MLLM Is a Strong Reranker" is well-supported by the retrieval results. The paper frames both reranking and NIT as joint contributions, which is appropriate. REMOVED — not a valid weakness; the critic misidentified the reranker's role as being primarily about generation accuracy.

- **"Threshold tuning introduces information leakage that invalidates reported test metrics" (Harsh Critic Point 4, as stated):** The critic asserts this "invalidates the reported test metrics," which is too strong. The adaptive threshold is set by a simple intersection heuristic (not by optimizing the evaluation metric), and the natural threshold results (which are not data-dependent) show similar trends. The concern is valid but minor, not invalidating. MOVED to Minor Weakness #4.

- **"No error bars" as a fatal flaw:** Moved to Minor Weakness #5 — standard in this field but worth noting.

- **Strength Finder strengths about "the problem is important" or generic framing:** All kept strengths are concrete and evidenced. No generic strengths were present.

## Novel Insights
None beyond the paper's own contributions. The reviews largely align on the paper's merits (strong retrieval reranking, well-validated components) and one key clarity issue (the conflated "w/o NIT" baseline across tables). The most interesting observation is that the paper would benefit from separating "zero-shot" from "fine-tuned without NIT" in its main results table, which would cleanly decompose the fine-tuning benefit from the noise-injection benefit.

## Suggestions

1. **Add an explicit "fine-tuned w/o NIT" row to the main generation results table** (tab:internvl_rag_results), or clearly label the existing "RagVL w/o NIT" rows as "RagVL (zero-shot generator)." This resolves the ambiguity that drives the critic's main complaint and lets readers decompose the gains into fine-tuning vs. noise injection.

2. **Compare against at least one prior multimodal RAG method** (MuRAG or SKURG) on the same WebQA/MultimodalQA splits, or provide a principled justification for why such a comparison is infeasible and temper the "advancing" language accordingly.

3. **State the specific *K* and *N* values** used for retrieval and reranking in the experimental setup section.

4. **Use a separate development split for adaptive threshold selection** (if the validation set supports it), or at minimum acknowledge the potential optimism and note that the natural threshold results corroborate the findings.

---
