- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 8, 3, 6
Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary

VRG-SLT is a sign language translation framework that combines a hierarchical VQ-VAE (sign-tokenizer) to discretize sign motions, a fine-tuned FLAN-T5 (SignLLM) with a merged text-sign vocabulary for sequence-to-text generation, and retrieval-augmented generation (RAG) as a post-hoc refinement step. The system is evaluated on How2Sign (ASL→English) and PHOENIX-2014T (DGS→German), reporting competitive BLEU and ROUGE scores.

## Strengths

- **Hierarchical VQ-VAE architecture is ablated and shows clear gains.** Table 2b compares hierarchical VQ-VAE against standard VQ-VAE and VQ-VAE-2, with BLEU-1 improving from 34.08 → 35.11 → 35.61. This directly validates the multi-level design for sign encoding.

- **State-of-the-art results on two distinct sign languages.** Table 1 shows VRG-SLT surpassing prior methods on both How2Sign (ASL) and PHOENIX-2014T (DGS), demonstrating cross-linguistic generalizability. The gains on PHOENIX-2014T (BLEU-4 +1.70, ROUGE +1.81 over the prior best) are concrete and non-trivial.

- **Systematic ablations of design choices.** The paper studies model size (FLAN-T5-base vs. larger variants), tokenizer hierarchy (standard VQ-VAE, VQ-VAE-2, hierarchical), and codebook capacity (256, 512, 1024). These provide reproducible evidence that each component choice contributes to the final performance.

## Weaknesses

### Fatal

None.

### Major

1. **RAG is claimed as a core contribution but never ablated.**  
   Contribution (3) explicitly states: "RAG strategy is integrated into VRG-SLT, enabling the retrieval and combination of relevant knowledge for more accurate and content-rich output." The abstract claims RAG "further improves the accuracy of the generated text." Yet the paper provides **no experiment comparing VRG-SLT with and without RAG**. Section 4.2 mentions "RAG strategies" as a focus of ablation analysis, but no RAG ablation results are presented or discussed — only model size, tokenizer architecture, and codebook size are ablated. Without this comparison, it is impossible to determine whether RAG helps, hurts, or is neutral, and the claimed contribution of RAG remains unsubstantiated. This is not a minor omission: it means one of the three signature contributions has zero direct evidence.

2. **Comparison fairness is compromised by RAG's external knowledge.**  
   The RAG module draws on the SQuAD database and ECMWF weather data (Section 3.4) — external knowledge sources that none of the baselines in Table 1 had access to. The paper does not acknowledge this asymmetry or discuss its potential effect on the reported scores. If higher BLEU/ROUGE scores partly reflect this external factual knowledge (e.g., weather terminology for PHOENIX-2014T) rather than superior sign-language modeling, the SOTA comparison is unfair. A direct comparison of VRG-SLT *without* RAG against the same baselines is needed to isolate the sign-language modeling contribution.

### Minor

3. **Inconsistency between the hierarchical VQ-VAE's loss function and its claimed architecture.**  
   The paper describes (lines 41–42) that both upper-body codes $e_u$ and hand codes $e_h$ are fed into the decoder for reconstruction. However, Eq. 2 defines the reconstruction loss as $\|m - \mathcal{D}(e_h)\|_2$ — only $e_h$ appears in the reconstruction term. Line 43 further states "the sign decoder $\mathcal{D}$ projects $e_h^{1:L}$ back to raw motion space," again only mentioning $e_h$. The role of $e_u$ in reconstruction is unclear from the main text. The hierarchical mechanism as presented is either incompletely specified or the loss function is incorrect. (The supplementary material may clarify this, but the main text should be self-consistent on this point.)

4. **Claimed confidence intervals not reported.**  
   Section 4.1 states "The results are calculated with a 95% confidence interval from 10 repeated runs," but Table 1 presents only point estimates with no error bars, standard deviations, or confidence intervals. Without variance information, the statistical significance of the reported gains (e.g., BLEU-4 +1.70 on PHOENIX-2014T) cannot be assessed.

5. **RAG module is underspecified.**  
   The retrieval pipeline lacks key details: BERT is used for "querying and retrieving" but no specific variant (e.g., Sentence-BERT) or retrieval method is named; the refinement model is described only as "an open-source large model" without identification; the document indexing method is unspecified; and using SQuAD (a reading comprehension QA dataset) as a general knowledge base for sign language translation is not justified. These gaps hinder reproducibility.

### Trivial

- None.

## Nice-to-Haves

- Clarify whether RAG is applied only at inference or if the model is trained end-to-end with retrieval (Section 3.4 describes it as separate "tuning," but the terminology "RAG" typically implies a trained retrieval-generation pipeline).
- Explain how the two encoders ($\mathcal{E}_u$ and $\mathcal{E}_h$) operate on the same input $m^{1:M}$ yet capture different granularities of motion.
- Justify the choice of SQuAD and ECMWF as knowledge bases for general sign language translation.

## Removed Points

These points were raised by reviewers but are excluded from the main weaknesses for the following reasons:

- **"BLEU-1 vs. BLEU-4 inconsistency on How2Sign"** — The critic claimed that BLEU-1 of ~35 implies BLEU-4 should be higher than the ~4 reported. This misunderstands the BERTScore/BLEU metrics: BLEU-1 (unigram precision) and BLEU-4 (4-gram precision with brevity penalty) naturally differ by an order of magnitude on challenging translation tasks. For How2Sign, BLEU-4 values in the low single digits and BLEU-1 in the 30s are consistent with prior literature. **Removed: factually incorrect.**

- **General underspecification nitpicks** (e.g., "what 'upper body' and 'hands' mean in terms of input keypoint sets") — These are reasonable questions but the paper states keypoints are the input representation, and the architecture follows established practices from VQ-VAE-2 and text-to-motion works (Zhang et al., 2023b; Jiang et al., 2023) cited in the paper. The level of detail is standard for a conference paper with supplementary material. **Removed: within-norm scope for a 9-page paper with supplement.**

- **Strength about RAG reducing hallucination** — The Strength Finder claimed RAG reduces hallucination as a strength, but this conflicts with the verified weakness that RAG is never ablated. Without experimental evidence, this claimed strength is unsupported. **Removed: conflicts with verified weakness.**

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs did not surface any perspective that meaningfully recontextualizes or extends the paper's findings beyond what the authors already state.

## Suggestions

1. **Add a RAG ablation.** This is the single highest-priority addition. Compare VRG-SLT with and without RAG on both datasets, and report the delta. If RAG provides minimal gains, the paper's core contribution is the VQ-VAE + SignLLM pipeline, and the RAG claim should be revised accordingly. If RAG provides substantial gains, the comparison against baselines must note this asymmetry.

2. **Clarify the VQ-VAE decoder input.** State explicitly whether $\mathcal{D}$ receives $e_h$ alone, $e_u$ alone, both, or a fusion; correct Eq. 2 or the text so they are consistent.

3. **Report confidence intervals or error bars** in Table 1, or remove the claim about 10 repeated runs.

4. **Disclose the RAG implementation details** — identify the retrieval model, the refinement model, and the indexing method — to support reproducibility.
