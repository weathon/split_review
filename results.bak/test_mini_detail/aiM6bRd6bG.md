Now I have a good picture of the calibration landscape. Let me finalize my analysis.

**Round 1 bracket**: Based on the calibration search, the paper sits between the weak anchors (2-3.4) and the strong anchors (8), with the most comparable papers in the 4.0-6.5 range. Initial bracket: [4.5, 6.0].

**Round 2 narrowing**: The relevant anchors in the 4-6 range are:
- NovoBench-100K (4.6) - dataset paper with significant evaluation concerns
- PPB Affinity (4.6) - missing baselines, unclear methodology
- ProtAC (5.2) - reasonable methodology but missing baselines
- LLaPA (4.75) - data leakage concerns, methodology clarity issues
- ProteinBench (6.5) - strong benchmark paper

My paper is clearly stronger than the 4.6 anchors (which had more fundamental issues) but weaker than ProteinBench (6.5). It's comparable to ProtAC (5.2) but with clearer contributions and more addressable weaknesses.

Final score: **5.0**

Now let me write the consolidated review.

The paper defines a novel task (PPI candidate ranking) and proposes a two-stage approach using interpretability-guided retrieval and multi-source re-ranking. The prospective evaluation on STRING v11→v12 is a genuine strength. However, two major evidential gaps — the missing ablation of the active-region selection and the absence of end-to-end evaluation of the re-ranking pipeline — mean the core claims are not fully supported. The overclaiming of "two orders of magnitude" improvement also needs correction.

Let me write the full review now.## Summary

This paper introduces the problem of *PPI candidate ranking* — given a target protein and its known partners, ranking novel candidates by likelihood of interaction. The authors propose a two-stage framework: (1) interpretability-guided retrieval that uses predicted contact maps to focus cosine-similarity computations on active residue regions of known partners, and (2) re-ranking with multiple biological signals (interaction scores, structural plausibility, semantic/text features). The framework is evaluated prospectively using STRING v11 (known) → v12 (novel) as a temporal testbed, benchmarking against raw interaction probabilities from D-SCRIPT, Topsy-Turvy, and xCAPT5. Results show substantial improvements over these baselines.

## Strengths

1. **Prospective evaluation on successive STRING releases.** The paper validates PPI candidate ranking using STRING v11 (known) → v12 (novel) as a temporal testbed, directly assessing whether models can anticipate interactions confirmed only in later releases. This avoids the common pitfall of static benchmarks within a single release. (Section 5.1, Abstract)

2. **Novel task formulation.** The paper clearly defines the PPI candidate ranking problem — prioritizing novel candidates for experimental validation given known partners — which is practically motivated by the high cost of experimental screening. The formalization in Equations (1)–(5) is clean and sensible. (Section 4)

3. **Large-scale ground-truth construction.** The paper filters STRING v12 to obtain 279,568 new high-confidence physical interactions, enabling a realistic and challenging test set for ranking. (Section 5.1)

4. **Systematic multi-source re-ranking analysis.** The pairwise rank-shift matrix (Table 2) provides a thorough, apples-to-apples comparison of four complementary signal families (interaction score, structural plausibility, TF-IDF/Jaccard features, and three biomedical LLMs), showing that a fine-tuned PubMedBERT cross-encoder improves or maintains 75.5% of rediscoveries. (Section 4.2, Table 2)

## Weaknesses

### Fatal
None.

### Major

1. **The interpretability-guided retrieval component is not properly ablated.** The paper's central methodological claim is that using *active residue regions* (identified from predicted contact maps) yields better rankings than using model outputs directly. However, Table 1 compares the proposed approach only against ranking by raw interaction probabilities from the same models. The natural control — ranking by **full-embedding cosine similarity** (without active-region selection) — is missing. Without this, the large improvements (e.g., Recall@10 from 1.2% to 26.4%) cannot be attributed to the interpretability-guided focus; they could arise simply from switching from scalar scores to embedding-based similarity and aggregating across known partners. The "active region" mechanism could be non-central to the improvement. A single additional row in Table 1 for "full embedding cosine similarity" (without contact-map filtering) would resolve this.

2. **The re-ranking pipeline is evaluated only through pairwise rank-shifts, not through end-to-end retrieval performance.** The re-ranking module is presented as a key part of the framework (Section 4.2), yet Table 1 reports only the initial interpretability-guided stage. The evaluation of re-ranking (Table 2) consists of pairwise comparisons — fractions of interactions that improve/maintain rank when switching from one signal to another — but it does **not** show the final ranking quality *after* re-ranking. We are left unable to answer whether the full pipeline (retrieval + re-ranking) outperforms the retrieval stage alone. Without a comparison of overall metrics (Recall, MRR, Success@k) before and after re-ranking, the utility of the re-ranking step is unquantified. Moreover, the re-ranking is applied only to the top-10 candidates; the effect on the full ranking at multiple cutoffs is not shown.

3. **Re-ranking signals are not combined into a single pipeline.** The paper states "a new ranking is obtained for each new signal used" (Section 4.2), and Table 2 evaluates each signal independently. The paper does not specify which signal the pipeline ultimately uses, or whether they are ensembled. If the contribution is to analyze complementarity, that is fine, but the title and framing ("Domain Knowledge-Guided Pipeline") suggest a single coherent pipeline, yet the actual design is a comparative analysis of independent signals.

### Minor

4. **Overclaiming of improvement magnitude.** The abstract and conclusion state that the approach "improves ranking metrics by two orders of magnitude" or "up to two orders of magnitude." The actual improvements in Table 1 are roughly 5× for MRR (0.034 → 0.169) and 25× for Recall@5 (0.007 → 0.183). While large, these are not "two orders of magnitude" (100×). This should be corrected to an accurate characterization of the gains.

5. **Underspecified threshold for active region identification.** Section 4.1 states: "We then scan the resulting activation profile along the sequence of $p_k$ and identify all maximal contiguous segments of highly activated residues." The paper never states what threshold defines "highly activated." Since the activation score is defined as the maximum contact probability over residues of $p$, it is unclear whether a hard cutoff is used or whether "high" is relative. This affects reproducibility. Additionally, selecting the single segment with highest average activation implicitly assumes each known partner contributes a single continuous binding interface — this may not hold for multi-domain interactions or flexible interfaces.

6. **"Prediction Coverage" metric formatting.** In Table 1, Prediction Coverage appears as a single column alongside k-varying metrics. The metric definition says "Total number of true novel partners that are successfully retrieved across all proteins," which is a single number, not per-k. The table formatting is ambiguous and should be clarified.

### Trivial
None.

## Nice-to-Haves

- **Stratified analysis by number of known partners.** The paper acknowledges the limitation for proteins with few known partners (Section 6), but quantifying performance for proteins with ≤3 known partners would strengthen practical guidance.
- **Network-based baselines.** Adding a simple baseline (e.g., ranking by STRING confidence scores or known interactor counts) would help calibrate task difficulty. This is not a core flaw — the paper already compares against three learned models.

## Removed Points
- *Criticism about "‡ is reported" being incomplete in Table 2*: This is a parser artifact; the original submission has a complete description.
- *Criticism about verifying v12 interactions were absent from v11*: The paper's preprocessing (filtering to experimental support > 0) is clearly described. The critic's concern about low-confidence evidence is speculative and not grounded in a specific error in the paper.
- *Criticism about missing computational cost quantification*: The paper references Figures 2 and 3 for runtime comparison; these are in the appendix which was stripped by the parser.
- *Strength about "honest discussion of limitations"*: While the paper does discuss limitations, this is a generic attribute expected of any paper and does not constitute a distinguishing strength.
- *Strength about "large-scale ground-truth construction"*: Retained as a supporting strength (not a core strength), since it supports the evaluation but is not a methodological contribution.
- *Various formatting/style nitpicks*: These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same set of issues: the harsh critic correctly identifies the missing ablation and incomplete pipeline evaluation as the central weaknesses, while the strength finder correctly identifies the prospective evaluation and the multi-source re-ranking analysis as the main strengths. The key insight from synthesizing both is that the paper's claims are directionally correct but the evidence is incomplete — the improvements are real and large relative to raw probabilities, but the specific contribution of the active-region mechanism and the additive value of the re-ranking stage are not properly isolated.

## Suggestions

1. **Add the missing ablation.** Add a row to Table 1 that ranks candidates by cosine similarity between **full embeddings** of target and candidate (without contact-map filtering). If the active-region approach outperforms full-embedding similarity, the interpretability guidance is justified. If not, the contribution is still interesting (embedding-based retrieval beats raw scores) but tells a different story.

2. **Evaluate the full pipeline end-to-end.** After re-ranking using the best signal (e.g., PubMedBERT), report the same metrics as Table 1 (Recall, MRR, Success@k) on the full ranking. Show the change in metrics before and after re-ranking across multiple cutoffs.

3. **Correct the "two orders of magnitude" claim** to an accurate characterization of the gains (e.g., "up to 25× improvement in early recall, and 5× improvement in MRR").

4. **Specify the threshold** for "highly activated" residues in Section 4.1, and discuss the assumption of single contiguous binding interfaces.

## Score and Decision

**Calibration details:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| NovoBench-100K (ZkpDdCQUC4) | 4.6 | 1,2 | Dataset paper with significant evaluation concerns. Our paper has stronger methodological novelty and a cleaner evaluation design, but both share the issue of incomplete evidence for core claims. Our paper is stronger. |
| PPB Affinity (xNDydjYBmC) | 4.6 | 1,2 | Missing baselines entirely, unclear methodology, duplicate figures. Our paper is clearly stronger — it has a clear methodology, compares against baselines, and has a well-designed prospective evaluation. |
| ProtAC (R7l5kMJTut) | 5.2 | 2 | Protein data cleaning with missing baselines. Our paper has a clearer novel contribution (task definition) and more specific, addressable weaknesses. Comparable quality. |
| LLaPA (AK9uRqzLjt) | 4.75 | 2 | Data leakage concerns, unclear methodology. Our paper is more rigorous methodologically. |
| ProteinBench (BksqWM8737) | 6.5 | 1 | Comprehensive benchmark with strong evaluation. Our paper has more methodological novelty but significantly weaker evaluation (missing ablation, incomplete pipeline evaluation). Clearly weaker. |

**Round 1 bracket**: [4.5, 6.0]  
**Round 2 narrowing**: The paper is stronger than the 4.6 anchors (which had more fundamental issues like missing baselines entirely or unclear methodology) but weaker than ProteinBench (6.5) due to the two major evidential gaps. It is comparable to ProtAC (5.2) — both have clear contributions but incomplete evaluation.

**Final score**: 5.0

This paper defines a genuinely novel task and uses a clever prospective evaluation setup. The improvements over raw model probabilities are large and real. However, two major evidential gaps — the missing ablation of the active-region selection and the absence of end-to-end evaluation of the re-ranking pipeline — mean the core claims about the specific contribution of the interpretability-guided mechanism and the pipeline's additive value are not fully supported. The ideas are promising enough to warrant resubmission after the missing analyses are completed.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>