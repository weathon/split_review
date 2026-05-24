Now I have sufficient calibration data. Let me compile the final review.

## Summary of Calibration

**Round 1 (Bracketing):**
- Low band (<3.5): Papers at avg 3.0 — clearly flawed/rejected
- Middle band (3.5–7.5): MAPE-PPI (5.67, accept), DeepSSInter (5.00, reject), LLaPA (6.00, reject)
- High band (>7.5): Papers at 8.0 — strong accepts

**Round 2 (Narrowing 4.5–7.5):**
- Illuminating Protein Function (5.25, reject) — missing baselines, incomplete descriptions
- MAPE-PPI (5.67, accept) — solid methodology but mixed reviews
- RankNovo (5.50, reject) — similar retrieval+reranking structure
- EBMDock (5.75, accept) — clear docking contribution
- PEEP (5.60, reject) — metric learning for enzymes

**Initial bracket:** 4.5–6.5

**Narrowing:** The paper under review has clearer novelty than the 5.25 anchor (new task formulation) and comparable evaluation rigor to MAPE-PPI (5.67). It is most similar in structure to RankNovo (5.50, rejected) but with a stronger evaluation framework. The weaknesses (missing ablation, overclaimed numbers) are real but addressable. Placing it at 5.5 reflects a solid paper whose core claims are partially undersupported but whose contributions (task formulation, prospective evaluation, multi-signal analysis) are genuine.

Now writing the consolidated review:

## Summary
This paper introduces the task of PPI candidate ranking — given a target protein and its known partners, rank novel candidates most likely to interact — and proposes a two-stage framework. Stage 1 uses interpretability-guided retrieval: predicted contact maps from D-SCRIPT/Topsy-Turvy identify "active regions" in known partners' embeddings, then cosine similarity between those active regions and candidates produces an initial ranking. Stage 2 re-ranks top candidates using diverse signals (interaction scores, structural plausibility via SpeedPPI/pDockQ, semantic overlaps from GO/domains/pathways, and LLM-based semantic similarity). Evaluation uses a prospective STRING v11→v12 setup, showing substantial improvements over direct prediction probabilities.

## Strengths

**1. Novel task formulation with practical relevance.** The paper explicitly frames PPI candidate ranking as distinct from standard PPI classification, directly targeting the experimental validation bottleneck. This framing is well-motivated and fills a gap in how computational PPI methods are typically evaluated.

**2. Prospective evaluation on STRING v11→v12 is a strong methodological contribution.** Rather than static retrospective benchmarks, models are built on v11 data and tested on interactions newly added in v12. This setup directly measures whether methods can anticipate future experimental discoveries, which is more realistic and practically meaningful than within-release evaluation. The careful preprocessing (CD-HIT clustering at 40% identity, length filtering, negative sampling at 10:1 ratio) adds to the rigor.

**3. Interpretability-guided retrieval produces large ranking improvements.** Table 1 shows that the method lifts D-SCRIPT Recall@10 from 1.2% to 26.4% and MRR from 0.034 to 0.169. While the missing ablation (see Weaknesses) prevents attributing this entirely to the contact-map masking, the overall pipeline clearly outperforms direct prediction probabilities across all metrics and cutoffs.

**4. Systematic multi-signal re-ranking analysis.** The pairwise rank-shift analysis (Table 2) across 10 evidence sources (IS, pDockQ, TF-IDF, token/location/key-term overlap, BioBERT, BioMedRoBERTa, PubMedBERT) provides a useful map of signal complementarity. Findings such as PubMedBERT improving 75.5% of cosine-based rankings, and lightweight heuristics like KeyTerm overlap achieving 69.3%, offer practical guidance for practitioners.

**5. Strong attention to data leakage prevention.** The cross-encoder training uses GroupKFold at the protein level, ensuring no protein appears in both training and validation sets, and all evaluation is on the disjoint STRING v12 set. This careful design strengthens confidence in the results.

## Weaknesses

### Fatal
None.

### Major

**1. The benefit of interpretability-guided *active-region selection* over simply using known partners is not isolated.**  
The method is compared only against direct prediction probabilities from D-SCRIPT, Topsy-Turvy, and xCAPT5 — baselines that do *not* use known interaction partners at all. The large improvements could therefore be driven entirely by access to known partners rather than by the contact-map masking. The paper never tests a simpler "full-embedding" baseline that also uses known partners — e.g., ranking candidates by max cosine similarity to the complete (unmasked) embedding of any known partner. Without this ablation, the claimed benefit of the interpretability-guided residue selection is unsupported. If a full-embedding k-NN baseline performs similarly, the core methodological novelty of the Stage 1 retrieval collapses. This does not invalidate the overall pipeline (using known partners is itself a useful design), but it undermines the specific selling point of "interpretability-guided" retrieval. *(Relevant to: Table 1, Section 4.1)*

### Minor

**2. The "two orders of magnitude" claim is overstated.**  
Table 1's largest improvement factor is roughly 26× (D-SCRIPT Recall@5: 0.0071 → 0.1832), approximately 1.4 orders of magnitude. The claim appears twice: "improve ranking metrics by two orders of magnitude" (Introduction) and "up to two orders of magnitude" (Conclusions). Neither is supported by the data. This should be corrected. *(Relevant to: Introduction, Conclusions)*

**3. Re-ranking signals are evaluated independently; no combined ranking is demonstrated.**  
The paper's language ("integrating complementary sources of evidence," "re-ranking strategy") suggests signals are combined. Yet Table 2 evaluates each signal in isolation via pairwise rank shifts. No ensemble, learned aggregation, or combined ranking is presented or evaluated for end-to-end metrics (nDCG@k, Success@k). The practical impact of re-ranking — how many more true partners reach the top of a *final combined* list — remains unclear. The individual analyses are still useful, but the framing should be adjusted or a combined ranking should be demonstrated. *(Relevant to: Abstract, Section 4.2, Table 2)*

**4. Inconsistency in the definition of the interaction score.**  
Section 3 describes the IS as the output of a logistic activation that compresses convolutional features. Equation (6), however, defines it as the maximum of contact-map entries \( C(p,p_c)_{ij} \). These are different quantities unless the model architecture is misrepresented. The paper states "This probability, sharpened through a logistic activation, is reported as the IS," which partially bridges the gap, but the equation and surrounding text should be clarified to avoid confusion. *(Relevant to: Section 3, Section 4.2, Equation 6)*

**5. Missing implementation details affecting reproducibility.**  
(a) The source layer and dimensionality of embeddings \( z_p \) are not specified (before or after the D-SCRIPT/Topsy-Turvy projection module?). (b) The construction of the key-term set \( K(p) \) is under-specified: which word lists are used, and what corpus is used for TF-IDF? These are needed for reproducibility. *(Relevant to: Section 4.1, Section 4.2)*

**6. No variance or significance estimates.**  
Metrics in Table 1 are reported as point estimates without confidence intervals, standard deviations, or significance tests. Given that candidate sets and true-partner distributions vary widely across proteins, some measure of variability would help judge reliability. *(Relevant to: Table 1)*

**7. Tone overstates practical readiness.**  
Even with the best method, Success@10 is ~13% (D-SCRIPT backbone), meaning ~87% of target proteins have no novel partner in the top-10. This is not a flaw in the paper — the problem is inherently difficult — but the abstract and conclusions should temper phrases like "step change" and "accelerating discovery" to reflect the considerable room for improvement, which the limitations section already partially acknowledges. *(Relevant to: Abstract, Conclusions)*

### Trivial

- Equation numbering and reference style: Eq. (6) uses \( \hat{p} \) for the interaction score, but Section 3 also uses \( \hat{p} \) for the logistic output — clarifying the relationship would resolve the inconsistency noted above.
- Table 1 has a typo (0.00117 should likely be 0.0117 for Topsy-Turvy Recall@10).

## Nice-to-Haves

- **Full-embedding known-partner baseline** (as described in Major weakness 1) would strengthen the core claim.
- **A combined re-ranking demonstration** (even simple score averaging) would validate the "integration" framing.
- **Breakdown by known-partner count** would assess how the method degrades when a target has only 1–2 known partners.
- **Hard negative mining** for the PubMedBERT cross-encoder (rather than random negative sampling) might improve discriminative power.

## Removed Points

These points were flagged for removal from the inputs; I list them here for transparency:

- *"The 'two orders of magnitude' claim is unsupported by the data"* — **Kept as Minor** (Weakness 2). It is a factual overstatement, but not fatal. The paper's conclusions do not collapse without it.
- *"The re-ranking analysis does not actually integrate multiple sources of evidence"* — **Kept as Minor** (Weakness 3). The paper evaluates signals independently, which is useful but overclaimed as "integration."
- *"Section 4.1 – Embeddings: It is not specified which layer's output is used"* — **Kept as Minor** (Weakness 5a). A genuine reproducibility gap.
- *"Section 4.2 – Semantic scores: construction is under-specified"* — **Kept as Minor** (Weakness 5b). Needs clarification for reproducibility.
- *"Table 1 – No variance or significance"* — **Kept as Minor** (Weakness 6). Standard expectation for such comparisons.
- *"Table 2 – Interpretation of rank-shift fractions"* — **Absorbed into Weakness 3.** The practical significance point is already covered.
- *"Success@10 is low"* — **Kept as Minor** (Weakness 7). Tone should be tempered.
- *"Impact of the number of known partners"* — **Moved to Nice-to-Haves.** Useful analysis but not required.
- *"Negative example generation: hard negatives vs. random"* — **Moved to Nice-to-Haves.** A reasonable suggestion but not a flaw.
- *"Computational cost not contextualized"* — **Removed.** The paper mentions runtime in Figures 2/3 and the text notes "hundreds of hours." Further breakdown would be nice but is not a weakness.
- *"Potential major error in chemistry facts"* — **Removed.** This was from a different paper's review (LLaPA), not relevant here.
- *"Unfair comparison"* — **Removed.** The comparison is to prediction probabilities; this is appropriate for showing the value of using known partners. The critic's demand for a known-partner baseline is valid (kept as Major weakness 1), but the comparison itself is not unfair.
- *"Missing related works"* — **Removed per instructions.**
- *Strengths Finder generic strengths* (e.g., "the paper addresses an important problem") — **Removed.** Generic/superficial strengths that lack specific evidence.
- *"The paper is well-written" —* **Removed.** Generic. The concrete strengths (task formulation, prospective evaluation, re-ranking analysis) are kept.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge with the paper's own framing, though the Harsh Critic usefully identifies a missing decomposition (known-partner access vs. contact-map masking) that the paper does not currently address. The Strength Finder's emphasis on the prospective STRING evaluation as the paper's strongest methodological contribution is well-placed and may be under-emphasized in the paper relative to the interpretability narrative.

## Suggestions

1. **Add a full-embedding known-partner baseline.** For each target protein, rank candidates by max cosine similarity to the complete (unmasked) embedding of any known partner. If the contact-map masked version outperforms this, the interpretability contribution is validated. If not, the contribution shifts to the overall framework design rather than the masking.

2. **Correct the "two orders of magnitude" claim** and instead report precise improvement factors (e.g., "Recall@5 improves by ~26×, MRR by ~5×").

3. **Demonstrate at least one combined re-ranking** — e.g., average normalized scores from cosine + PubMedBERT + IS — and report end-to-end metrics. Alternatively, reframe the re-ranking section more modestly as an analysis of signal complementarity rather than "integration."

4. **Clarify the interaction score definition** by either fixing Equation (6) to match the Section 3 description or explaining the relationship between the contact-map max and the logistic output.

5. **Specify the embedding source and dimensionality** used for \( z_p \). Provide details on the TF-IDF corpus and key-term construction for reproducibility.

## Score and Decision

**Calibration summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| 44IKUSdbUD (diversified sampling) | 3.00 | R1 | Much weaker — unclear methodology, poor evaluation |
| S2WHlhvFGg (DTI prediction) | 3.00 | R1 | Much weaker — overclaimed, poor evaluation |
| itGkF993gz (MAPE-PPI) | 5.67 | R1/R2 | Comparable — similar evaluation thoroughness, similar issues |
| wCwz1F8qY8 (DeepSSInter) | 5.00 | R1 | Slightly weaker — incremental over prior work |
| eh1fL0zw8o (LLaPA) | 6.00 | R1/R2 | Comparable but more ambitious scope |
| jsQPjIaNNh (ProtIR) | 5.25 | R2 | Weaker — missing baselines, incomplete descriptions |
| 87B3zDRMjv (RankNovo) | 5.50 | R2 | Comparable — similar retrieve+rerank structure |
| qg2boc2AwU (EBMDock) | 5.75 | R2 | Slightly stronger — cleaner method contribution |
| 760br3YEtY (PEEP) | 5.60 | R2 | Comparable — similar evaluation gaps |

**Round 1 bracket:** 4.5–6.5.  
**Round 2 narrowing:** The paper is weaker than EBMDock (5.75) on methodological isolation but stronger than ProtIR (5.25) on evaluation rigor. It is most comparable to MAPE-PPI (5.67, accepted) and RankNovo (5.50, rejected) — both have genuine contributions undermined by insufficiently supported core claims. The PPI candidate ranking paper's prospective evaluation is a clear strength, but the missing known-partner ablation and overclaimed "integration" are significant enough gaps to position it slightly below MAPE-PPI.  
**Final score:** 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>