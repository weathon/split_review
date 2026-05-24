Now I have a thorough understanding of the paper and the calibration anchors. Let me compile my final review.

---

## Summary
AtlasKV proposes a parametric method for augmenting LLMs with knowledge graphs by converting KG triples into query-key-value representations (KG2KV) and using hierarchical key-value pruning (HiKVP) to achieve sub-linear memory scaling at inference. The system can load 1B KG triples under 20GB VRAM and achieves dramatically better out-of-distribution knowledge grounding accuracy than the KBLaM baseline, with only 3K training steps.

## Strengths
- **Sub-linear memory scaling to billion-scale KGs is convincingly demonstrated**: Figure 4 shows AtlasKV's VRAM usage stays near 20GB from 10^4 to 10^9 triples, while KBLaM exceeds 40GB at 10^5. This is a clear, well-measured result that directly validates the HiKVP contribution.

- **KG2KV yields dramatically better OOD generalization than prior synthetic methods**: Table 3 shows AtlasKV achieving 90–100% Top-1 accuracy on three held-out datasets where KBLaM (using synthetic training data) often scores 0–50%. The diversity advantage in Table 1 (7.864% unique enquiry attributes vs. 0.003% for synthetic) and lower token cost (165.7 vs. 349.9) provide a crisp explanation for why KG2KV succeeds.

- **HiKVP introduces only a modest accuracy drop while enabling huge memory savings**: Table 3 directly compares AtlasKV (128-64-16) against AtlasKV w/o HiKVP — e.g., on ATLAS-CC-QKV with 10^2 triples, ACC@1 is 89.1% with HiKVP vs. 96.4% without. The drop is real but the pruned version still crushes KBLaM.

- **Training efficiency is substantially better than KBLaM**: AtlasKV trained for only 3K steps consistently outperforms KBLaM trained for 20K steps across all dataset-size combinations in Table 3, demonstrating that KG2KV data enables more sample-efficient learning.

- **Ablation study on entity types is well-executed and informative**: Table 4 cleanly shows that removing event entities causes a meaningful drop (e.g., ATLAS-Pes2o-QKV 10^3 triples: ACC@1 100% → 90%) and using only event entities collapses performance (9.1% at 10^4 triples), validating the design to include both named and event entities.

## Weaknesses

### Major
- **Knowledge grounding accuracy is only evaluated on KGs up to 10^3 triples, but the paper claims billion-scale capability**: Figure 4 proves that memory scales to 1B triples, and Table 3 proves that retrieval accuracy is strong at small scale. However, the paper presents no evidence that HiKVP's hierarchical pruning preserves retrieval accuracy when the KG grows from thousands to millions or billions of triples — where noise from weakly relevant keys could overwhelm the 16 selected leaf keys, or relevant knowledge could be pruned away. The method architecturally *should* scale (the same number of leaf keys are selected regardless of KG size), but the empirical validation stops three orders of magnitude short of the claimed scale. This does not invalidate the contribution — the memory results are real and the small-scale accuracy is strong — but it weakens the "billion-scale knowledge grounding" headline.

### Minor
- **End-to-end generation quality (GPTScore) is reported only for the unpruned variant, not the full AtlasKV system**: Figure 5 shows GPT-4o scores for "AtlasKV w/o HiKVP" against KBLaM and ICL. Table 3 does report attention accuracy for the pruned AtlasKV, which is a reasonable retrieval proxy, but the paper would be stronger if it also showed that HiKVP-pruned generation quality remains high.

- **Comparison against RAG baselines is limited to ICL and complexity analysis**: The paper's ICL baseline places the entire KG in the prompt — this is not how practical KG-RAG systems work (they typically retrieve a small set of relevant triples via dense retrieval). Table 2 provides a reasonable analytical complexity comparison, and the paper's primary comparison target is KBLaM (the same parametric paradigm), but a head-to-head against a realistic KG-RAG pipeline on QA accuracy would strengthen the practical case. The paper's contribution does not depend on this comparison, so it is minor.

### Trivial
- The paper directs readers to Appendix A.2 for the rationale behind choosing the 15th attention layer for evaluation; this is a minor presentation issue since the appendix exists in the original submission.

## Nice-to-Haves
- Scaling the knowledge grounding evaluation to larger KGs (e.g., 10^5 or 10^6 triples) would close the gap between the memory-scaling proof and the accuracy claims.
- Reporting GPTScore for AtlasKV *with* HiKVP would connect the attention-accuracy proxy to end-to-end answer quality.
- Discussing the computational cost of building the hierarchical clustering (UMAP + GMM) for billion-scale KGs would strengthen the feasibility narrative.
- Testing on a larger backbone LLM would bolster the generality claim.
- A realistic KG-RAG baseline (dense retrieval of top-k triples + LLM generation) would contextualize AtlasKV's advantages.

## Removed Points
*These points are flagged to be removed, treat them with caution.*

- **"The reliance on an LLM for rewriting adds an external dependency; the cost and potential noise are acknowledged but not deeply analysed"**: The paper explicitly notes this in the main text and refers to Appendix B.2 for analysis. The appendix exists in the original submission; the parser simply stripped it. Not a valid weakness.
- **"The construction of the hierarchical clustering for 1B triples (UMAP+GMM) is not discussed"**: The paper states it is done offline; discussing computational cost is already noted as a Nice-to-Have, not a weakness.
- **"The choice of the 15th layer is not explained in the main text"**: The appendix explains this. Since the appendix exists, this is at most Trivial (already noted).
- **"Testing on a larger backbone would bolster the generality claim"**: Already noted as Nice-to-Have.
- **"The paper does not discuss the effect of the sentence encoder choice beyond all-MiniLM-L6-v2"**: The paper mentions in Section 5.2 that "We also report the results with a larger model as the sentence encoder in Appendix B.1." The appendix exists. Not a valid weakness.

## Novel Insights
The paper's key insight — that KG triples naturally decompose into query-key-value structures mirroring transformer attention — is genuinely novel and well-motivated. The observation that this decomposition, when combined with relation rewriting, yields an order-of-magnitude more diverse training data than schema-based synthesis (7.864% vs. 0.003% unique enquiry attributes) is a crisp, measurable finding that explains the generalization gains. This provides a principled reason to prefer KG-derived training data over synthetic data for parametric knowledge augmentation, which is a non-obvious result.

## Suggestions
- Add even one experiment at 10^4 or 10^5 triples with HiKVP to show the accuracy trend does not collapse as KG size grows. This would substantially strengthen the paper.
- Report GPTScore for AtlasKV with HiKVP alongside the attention accuracy in Table 3, connecting retrieval quality to generation quality.

## Score and Decision

**Round 1 bracket**: Based on comparing against KBLaM (5.80), SubgraphRAG (6.00), and strong accept papers (7.50–8.00), this paper plausibly sits in the **6.0–7.5** range.

**Round 2 narrowing**: AtlasKV is clearly stronger than KBLaM (5.80) — it addresses KBLaM's training data diversity problem with KG2KV and its linear scaling limitation with HiKVP, and demonstrates dramatically better results. It is somewhat comparable to the parametric knowledge transfer paper (mIEHIcHGOo, 6.67) in contribution level, with more substantial empirical results but less complete evaluation coverage. It falls short of the Query Localization paper (tfyHbvFZ0K, 7.50), which has more thorough experiments and analysis.

**Anchor summary**:
| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| KBLaM (aLsMzkTej9) | 5.80 | R1, R2 | AtlasKV directly improves on this baseline; clearly stronger |
| In-context or In-parameter (sl4hOq9wm9) | 5.50 | R1, R2 | Different problem; AtlasKV more substantial |
| SubgraphRAG (JvkuZZ04O7) | 6.00 | R1 | Different approach; AtlasKV more innovative |
| Self-Updatable LLMs (aCPFCDL9QY) | 5.75 | R2 | AtlasKV has stronger results |
| Parametric Knowledge Transfer (mIEHIcHGOo) | 6.67 | R2 | Comparable contribution; AtlasKV slightly stronger results |
| Query Localization (tfyHbvFZ0K) | 7.50 | R2 | More thorough than AtlasKV; AtlasKV is weaker |
| Synthetic Continued Pretraining (07yvxWDSla) | 8.00 | R1 | Clearly stronger than AtlasKV |

The paper introduces genuine innovations (KG2KV, HiKVP), demonstrates compelling memory scaling, and dramatically outperforms its most direct baseline (KBLaM). The main limitations are evaluation gaps: knowledge grounding is only shown up to 10^3 triples while claiming billion-scale capability, and end-to-end generation quality is missing for the pruned system. These are substantive but not fatal — the architecture and small-scale results provide reasonable evidence that the method works. The paper sits above KBLaM (5.80) but below the more thoroughly evaluated strong-accept papers.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>