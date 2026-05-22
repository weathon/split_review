Now I have enough information to write the final review. Let me synthesize everything.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me compile the final review:

**Summary:** The paper introduces PPI candidate ranking as a novel task and proposes a two-stage pipeline: (1) interpretability-guided retrieval that uses predicted contact maps of known interaction partners to identify active residues and compute cosine similarity for ranking novel candidates, and (2) re-ranking using multiple biological signals (interaction scores, structural plausibility from SpeedPPI, functional annotations, LLM embeddings). Evaluated prospectively using STRING v11→v12 (279,568 novel interactions), the method shows large improvements over raw PPI prediction probabilities from D-SCRIPT, Topsy-Turvy, and xCAPT5.

**Strengths:**
1. Well-posed problem formulation and prospective evaluation design. The paper formalizes PPI candidate ranking, a practically important task for guiding experimental validation, and evaluates it prospectively using interactions that appeared only in STRING v12 after training on v11. This is stronger than the standard single-release retrospective benchmark.
2. Large and consistent improvements in early-ranking metrics. Table 1 shows Recall@10 rising from 1.24% to 26.41% and MRR from 0.034 to 0.169 for D-SCRIPT (roughly 4-25×), with gains replicated on Topsy-Turvy. The absolute hit rates (13% of top-10 candidates are true novel partners) are practically meaningful.
3. Comprehensive re-ranking analysis. Table 2 systematically compares 10 different re-ranking signals (IS, pDockQ, TF-IDF, three overlap measures, three LLM encoders), finding that PubMedBERT offers the most consistent refinement (75.5% maintain-or-improve rate) while lightweight heuristics like KeyTerm overlap (69.3%) are surprisingly competitive. This is a useful empirical resource.
4. Generalizability across backbone architectures. The interpretability-guided retrieval improves over both D-SCRIPT and Topsy-Turvy raw scores, showing the framework is not tied to a specific model.

**Weaknesses:**

### Major
1. **Missing ablation: the contribution of active-residue selection is not isolated from the use of known partners.** The proposed method (Equations 3-4) combines two operations: (a) using known partners KP(p) as anchors for retrieval, and (b) restricting similarity computation to the predicted contact-map-active region. The baselines in Table 1 (raw D-SCRIPT/Topsy-Turvy/xCAPT5 probabilities) do not use known partners at all. Thus the reported gains could partly or largely come from simply using known partners as anchors, not from the interpretability-guided segment selection specifically. A control experiment—ranking candidates by full-embedding cosine similarity to known partners (i.e., Equation 4 without focusing on I_k)—is needed to attribute the improvement. Without it, the paper's central claim that contact-map guidance drives performance is not fully supported by evidence.

### Minor
2. **"Two orders of magnitude" is an overstatement.** The abstract and conclusion claim improvements "by two orders of magnitude" and "up to two orders of magnitude." The largest gain in Table 1 is Recall@5 for D-SCRIPT (~25×), and most other gains are 4-10×. No metric reaches 100×. This should be corrected (e.g., "up to 25× improvement" or "substantial improvements").

3. **Re-ranking analysis limited to top-10 candidates.** The re-ranking evaluation (Table 2) only examines rank shifts within the subset of candidates already in the top-10 from retrieval. This reveals relative signal quality but does not measure impact on overall retrieval metrics (Recall, MRR on the full candidate set). The paper acknowledges the computational constraint, but the claim that re-ranking "enhances ranking quality" is only demonstrated on this truncated set.

4. **Active-residue selection heuristic not validated against known interfaces or simpler alternatives.** The method selects the contiguous region with highest average contact probability from predicted contact maps. The paper does not validate whether these regions correspond to actual binding interfaces (e.g., from PDB structures), nor does it compare against a random-segment baseline or a fixed-length N-terminal segment. While the overall pipeline works, this leaves the "interpretability guidance" claim somewhat unsubstantiated.

### Trivial
5. **Table 2 caption is incomplete.** The caption mentions both "†" and "‡" but only explains the † statistic; "‡ is reported" is a dangling fragment. The table is also missing diagonal entries and the asymmetry direction is not explained in-text.
6. **Ambiguous threshold for "highly activated" residues.** Section 4.1 says "identify all maximal contiguous segments of highly activated residues" but never defines a threshold. Later it states the segment with "highest average activation score" is selected, suggesting no threshold is used—making "highly activated" misleading. This should be clarified.
7. **No analysis stratified by number of known partners.** Given the method's dependence on KP(p), results stratified by KP(p) size (e.g., few vs. many known partners) would reveal practical applicability boundaries.

### Nice-to-Haves
- Add a baseline using full-embedding cosine similarity to known partners (as mentioned in weakness #1)
- Validate active-residue segments against known binding interfaces or random-segment baselines
- Report re-ranking impact on global retrieval metrics (even if limited to top-100)
- Break down computational cost per target/candidate

### Removed Points
- "Baselines are unfair" (Harsh Critic #1): The paper compares its pipeline against existing PPI methods—this is standard practice, not unfair. The missing ablation (above) is the real issue, not the baseline choice itself.
- "Re-ranking does not demonstrate overall ranking improvement" (rephrased as Minor weakness #3 — the analysis is limited but still informative within top-10)
- "The paper cites unreleased models/datasets": Not applicable; all cited resources are published.
- "Method fails for proteins with few known partners": The paper acknowledges this as a limitation honestly; not a weakness.
- "Selection of D-SCRIPT as backbone for re-ranking not justified": The paper provides justification (D-SCRIPT better for early ranking).
- Generic or superficial strengths from Strength Finder removed.

### Novel Insights
None beyond the paper's own contributions.

### Suggestions
1. Add the ablation experiment: rank candidates by max full-embedding cosine similarity to known partners (remove active-residue selection) and compare to the proposed method. This directly tests whether contact-map guidance adds value beyond using known partners.
2. Correct the "two orders of magnitude" claim to reflect actual observed gains.
3. Validate the active-residue selection heuristic against a random-segment baseline or known PDB interfaces.
4. Clarify the "highly activated" threshold in Section 4.1 and complete the Table 2 caption.

### Score and Decision
Score: 6.0, Decision: Accept

Round-1 bracket: I searched for PPI/candidate-ranking papers and found:
- Weak anchors (<3.5): avg scores 3.0-3.4 (44IKUSdbUD, S2WHlhvFGg, etc.) — papers with serious flaws
- Middle anchors (3.5-7.5): avg scores 4.6-6.0 (MAPE-PPI 5.67, LLaPA 6.0, PPIformer 5.8, PEEP 5.6, etc.)
- Strong anchors (>7.5): avg scores 8.0 (GeSubNet, FlexDock, etc.)

Round-2 narrowing (4.5-6.5): The paper is stronger than PEEP (5.60, Reject — lower novelty, small dataset) and jsQPjIaNNh (5.25, Reject — function prediction, not PPI ranking). It is comparable to MAPE-PPI (5.67, Accept) and LLaPA (6.0, Reject for fatal data leakage issues this paper doesn't share). The paper's prospective evaluation design and clear problem formulation place it above 5.5, but the missing ablation for the core mechanism caps it below 7.

Final calibration anchors consulted:
- itGkF993gz (MAPE-PPI, 5.67, Accept): Similar quality — clear methodology, solid experiments. Current paper has stronger evaluation design but missing an ablation MAPE-PPI doesn't need.
- eh1fL0zw8o (LLaPA, 6.0, Reject): Rejected for data leakage and unclear LLM benefit. Current paper avoids these flaws.
- 760br3YEtY (PEEP, 5.60, Reject): Lower novelty than current paper.
- xcMmebCT7s (PPIformer, 5.80, Accept): Comparable — dataset contribution + model.

The paper's key gap (missing ablation for the central mechanism) is real but fixable, and its strengths (prospective evaluation, well-posed problem, comprehensive re-ranking analysis) are substantial. Score: 6.0.

---

## Summary

This paper introduces PPI candidate ranking as a novel task and proposes a two-stage pipeline that first uses interpretability-guided retrieval (from predicted contact maps of known partners) to rank candidates, then refines the ranking using multiple biological signals. Evaluated prospectively on STRING v11→v12 (279,568 novel interactions), the method achieves large early-ranking improvements over raw PPI prediction probabilities from D-SCRIPT, Topsy-Turvy, and xCAPT5.

## Strengths

1. **Well-posed problem and prospective evaluation design.** The paper formalizes the practically important task of PPI candidate ranking for experimental guidance and evaluates it prospectively using interactions that only appeared in STRING v12 after training on v11. This is a stronger evaluation than the standard single-release retrospective benchmark used in prior PPI work.

2. **Large and consistent improvements in early-ranking metrics.** Table 1 shows Recall@10 rising from 1.24% to 26.41% and MRR from 0.034 to 0.169 for D-SCRIPT (roughly 4-25× improvement). Gains replicate on Topsy-Turvy. The absolute hit rates (~13% of top-10 candidates are true novel partners) are practically meaningful for screening.

3. **Comprehensive re-ranking analysis across 10 evidence sources.** Table 2 systematically compares interaction scores, pDockQ, TF-IDF, three token-overlap measures, and three LLM encoders. PubMedBERT provides the most consistent refinement (75.5% maintain-or-improve rate) while lightweight heuristics (KeyTerm overlap at 69.3%) are surprisingly competitive. This is a useful empirical resource.

4. **Generalizability across backbone architectures.** The retrieval framework improves over both D-SCRIPT and Topsy-Turvy raw scores, showing it is not tied to a specific model.

## Weaknesses

### Major

1. **Missing ablation: active-residue selection is not isolated from simply using known partners.** The proposed method (Eqs. 3-4) combines (a) using known partners KP(p) as anchors and (b) restricting similarity to contact-map-active regions. The baselines in Table 1 (raw D-SCRIPT/Topsy-Turvy/xCAPT5 probabilities) do not use known partners at all. The reported gains could partly arise from operation (a) alone, not from the contact-map-guided selection. A control—ranking candidates by full-embedding cosine similarity to known partners (Eq. 4 without the I_k focus)—is needed. Without it, the paper's central claim that interpretability guidance drives performance is not fully isolated.

### Minor

2. **"Two orders of magnitude" is an overstatement.** The abstract and conclusion claim improvements "by two orders of magnitude." The largest gain in Table 1 is Recall@5 for D-SCRIPT (~25×), and most gains are 4-10×. No metric approaches 100×. This should be corrected.

3. **Re-ranking analysis is limited to top-10 candidates.** Table 2 only examines rank shifts within the top-10 retrieved set. It does not evaluate impact on global retrieval metrics (Recall@k, MRR) on the full candidate list. While the computational constraint is acknowledged, the claim that re-ranking "enhances ranking quality" is only demonstrated on this truncated set.

4. **Active-residue selection heuristic is not validated against known interfaces or simpler alternatives.** The method picks the contiguous region with highest average contact probability. The paper provides no evidence that these correspond to actual binding interfaces (e.g., from PDB) and does not compare against a random-segment or fixed-length baseline. The "interpretability guidance" claim would be strengthened by such validation.

### Trivial

5. Table 2 caption mentions both "†" and "‡" but only explains the † statistic; "‡ is reported" is an incomplete fragment. The table is also missing diagonal entries and the asymmetry direction is not explained.
6. Section 4.1 says "identify all maximal contiguous segments of highly activated residues" but never defines a threshold for "highly activated." Later text clarifies no threshold is used (the segment with highest average is selected), making "highly activated" potentially misleading.
7. No results stratified by number of known partners per target, which would illuminate practical applicability for underexplored proteins.

## Nice-to-Haves

- Add the full-embedding baseline (weakness #1) to directly test whether contact-map guidance adds value.
- Validate active-residue segments against known PDB interfaces or random-segment baselines.
- Report re-ranking impact on global retrieval metrics (even for top-100).
- Break down computational cost per target and per candidate.

## Removed Points

The following points from the inputs were removed for the reasons stated:
- **Harsh Critic #1 ("unfair baseline comparison"):** The paper compares its pipeline against existing PPI prediction methods, which is standard practice. The real issue (moved to Major weakness #1) is the missing ablation for the active-residue selection, not the baseline choice itself.
- **"Method fails for proteins with few known partners":** The paper acknowledges this honestly as a limitation. Not a weakness.
- **"Selection of D-SCRIPT not motivated":** The paper justifies this choice (D-SCRIPT better for early ranking than Topsy-Turvy).
- **Generic strengths from Strength Finder** (e.g., "domain-informed extraction is a design novelty"): These are restatements of the method, not evidence-backed strengths.
- **Formatting/style nitpicks,** parser artifacts, and speculative claims about missing appendix content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add the critical ablation: rank candidates by max full-embedding cosine similarity to known partners (removing the I_k selection) and compare to the proposed method. This cleanly tests whether contact-map guidance adds value beyond using known partners.
2. Correct the "two orders of magnitude" claim to reflect actual gains (~25× max).
3. Validate active-residue selection against a random-segment baseline or known PDB interfaces.
4. Clarify the "highly activated" threshold description and complete the Table 2 caption.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>