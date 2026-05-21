---
job_id: b65028ed-a1fd-4871-98fd-2cece16dd2da
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: aiM6bRd6bG.pdf
paper: PPI Candidate Ranking: Large-Scale Evaluation of a Domain Knowledge-Guided Pipeline
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as an ML-for-biology submission centered on representation learning, interpretability of learned representations, ranking, and large-scale empirical evaluation for PPI prediction.

## Minimum Quality
Pass ✅. The paper includes the expected scientific components, namely abstract, introduction, related work, methodological sections, experiments/results, and conclusion, and it presents a non-trivial empirical study. While I have important concerns about methodological specification and evaluation, these are review-time issues rather than desk-reject-level defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided manuscript text or figures.

# Expected Review Outcome:
## Summary
This paper introduces the task of PPI candidate ranking, where, given a target protein and its known partners, the goal is to prioritize new candidate interactors for experimental validation. The proposed pipeline first retrieves candidates by comparing candidate embeddings to activated embedding regions of known interactors, derived from D-SCRIPT or Topsy-Turvy contact maps, and then optionally re-ranks top candidates using additional signals such as interaction scores, SpeedPPI/pDockQ, semantic overlap features, and biomedical language models. Evaluation is performed prospectively using interactions present in STRING v12 but absent from v11.

## Strengths
The problem formulation is well motivated. Reframing PPI prediction as candidate ranking for downstream wet-lab prioritization is practically meaningful, especially in a domain where validation is costly and throughput is limited. That framing is one of the paper’s clearest contributions.

The retrieval idea is intuitive and reasonably original in how it repurposes internal model structure. Instead of using only a scalar interaction score, the method exploits contact-map-derived active regions and compares local embedding segments across proteins. This is a sensible attempt to turn an interpretable architectural component into a retrieval signal rather than merely an explanation artifact.

**Figure 1** is helpful and does real work for the paper. It makes the pipeline understandable by showing the flow from known partners, to contact maps, to active residues, to cosine similarities, and then to max aggregation across anchors. Given that the method is otherwise under-specified in parts of Section 4.1, this figure materially improves comprehension of the proposed ranking mechanism.

The paper also deserves credit for using a prospective evaluation protocol based on successive STRING releases rather than a purely static split. That is closer to the discovery scenario the authors care about than standard retrospective pair classification.

There are some promising empirical signals. In **Table 1**, the proposed retrieval strategy appears to move true novel partners substantially upward in the ranked lists compared with direct prediction probabilities from the underlying models. The gains at early cutoffs are particularly notable for the D-SCRIPT-based variant, which is exactly where a candidate prioritization method should matter most.

The authors also attempt to look beyond pure accuracy. The runtime analyses in **Figure 2** and **Figure 3** are useful because they expose the computational trade-offs between retrieval and re-ranking, and they make clear that some refinement strategies, especially structure-based ones, may be hard to justify operationally at scale.

## Weaknesses
1. **Core methodological details in Section 4.1 are underspecified, and this matters because the retrieval signal depends entirely on those details.**  
   The definition of the active region \(I_k\) is not operationally clear enough to reproduce or evaluate. On **Page 5**, the text says the method identifies “maximal contiguous segments of highly activated residues” and then selects the segment with highest average activation score, but it never defines what “highly activated” means. Is there a threshold on the residue activation profile, a percentile, a connected-component rule after binarization, or something else? Without this, the retrieval procedure is not fully specified. This is not a cosmetic omission, because changing the thresholding rule could radically alter the region length \(|I_k|\), which then changes the matching objective in **Equation (3)** and therefore the ranking itself.

2. **There are mathematical and notational issues around Equations (3)-(6), including at least one apparent inconsistency with the underlying model description.**  
   In **Equation (3)** on **Page 5**, the sliding-window index is written as
   \[
   \max_{i=0}^{i<n_c-|I_k|} \cdots
   \]
   which is an odd upper-bound notation and appears to exclude the final valid window. If the candidate subsequence is \(z_c[i:i+|I_k|]\), the usual bound would be \(i=0,\ldots,n_c-|I_k|\), assuming inclusive start and exclusive end indexing. This needs correction.  
   More importantly, **Equation (6)** on **Page 6** defines the D-SCRIPT interaction score as
   \[
   \hat p=\max_{i\le n,j\le m} C(p,p_c)_{ij},
   \]
   but this contradicts the paper’s own background in **Section 3**, where D-SCRIPT is described as applying convolutional and pooling operations on the contact map and then a logistic activation to produce a scalar interaction probability. The interaction score is therefore not simply the maximum contact probability in the map, at least not according to the model description given in the paper. Since IS is one of the main re-ranking signals, this inconsistency is important and should be fixed or justified carefully.

3. **The evaluation protocol is motivated, but the evidence is weaker than the paper’s claims because the baseline set is narrow and some key comparisons are missing.**  
   For retrieval, **Table 1** compares against direct prediction probabilities from D-SCRIPT, Topsy-Turvy, and xCAPT5, but this is still a limited baseline set for a paper claiming a general candidate-ranking advance. There is no simple nearest-neighbor or homology-style retrieval baseline, no baseline using the full embedding without active-region selection, and no ablation showing whether the gain comes from active-region localization versus merely using known-partner embedding similarity. That last ablation is especially important because the paper’s central claim is specifically about interpretability-guided local matching. Without it, it remains unclear whether the contact-map-derived region extraction is necessary.

4. **The main results table is difficult to interpret and contains suspicious regularities that should be explained.**  
   **Table 1** has several presentation and interpretability issues. The model grouping is unclear, many cells for Prediction Coverage, MRR, and Average Rank are left blank, and some rows appear malformed, for example the entries around “200” and “500” for one model block. More substantively, in many rows MAP@k is numerically identical to Recall@k, sometimes to four decimal places. That is unusual unless the evaluation setup has a very particular label structure, such as essentially one relevant item per query, which is not what the task definition suggests because \(NP(p)\) can contain multiple new partners. If there is a task-specific reason why MAP collapses to Recall here, the authors need to explain it explicitly. Otherwise this raises concerns either about metric computation or table reporting.  
   The text on **Page 9** also discusses MRR improvements, but MRR is not actually reported in a usable way in **Table 1**, which makes that claim hard to verify.

5. **The re-ranking evaluation in Section 5.3 is not strong enough to support the broad conclusions drawn about complementary evidence sources.**  
   The analysis in **Table 2** reports only the fraction of v12 interactions whose rank was maintained or improved when moving from one method to another. This is a fairly weak statistic. It does not tell the reader the magnitude of the rank improvement, whether the improvement occurs near the top of the list where it matters most, or whether overall retrieval metrics after re-ranking actually improve. A method could improve many examples by one position and still be practically useless. Conversely, it could worsen many examples slightly while dramatically improving a smaller set into the top 10. Those scenarios are indistinguishable in the current table.  
   Relatedly, the paper proposes a two-stage pipeline, but it never reports the final end-to-end ranking quality after re-ranking using the same metrics as **Table 1**. That is a major gap. The paper therefore demonstrates that some signals often reshuffle ranks, but not convincingly that the full pipeline yields the best candidate prioritization in terms that matter operationally.

6. **The paper’s main assumption, that novel interactors resemble previously known ones for the same protein, is plausible but insufficiently stress-tested.**  
   The authors acknowledge in the conclusion that the method depends on proteins having known partners, but the empirical section does not analyze performance as a function of \(|KP(p)|\), target-protein degree, or novelty regime. This matters because the method could perform well mainly on proteins with many known interactions and fail in the sparse regimes where discovery would arguably be most valuable. A stratified analysis by number of known partners would materially strengthen the paper.

7. **Some of the strongest claims are overstated relative to the evidence provided.**  
   On **Page 2** and again in the conclusion, the paper suggests improvements “by two orders of magnitude” and a “step change” in prioritization. Those are punchy statements, but the evidence is less clean than that wording suggests. The retrieval gains in **Table 1** are certainly encouraging, yet the baseline choice is narrow, the metric table is partially malformed, and the end-to-end re-ranking outcome is not shown in the same standard ranking metrics. In a paper like this, where the entire value proposition is ranking quality, the claims should be stated more conservatively unless the evaluation is airtight.

8. **The runtime analysis is useful but only partially fair and only partially actionable.**  
   **Figure 2** shows retrieval runtime for the prediction-probability baseline versus the proposed approach, and **Figure 3** shows total re-ranking time for 2,280 pairs. However, the paper notes in the appendix that some preprocessing costs are excluded for the semantic methods. That choice is understandable for isolating algorithmic cost, but it also means the comparison is not a full pipeline cost comparison. In particular, if annotation retrieval or curation is non-trivial, the practical attractiveness of those methods could be overstated. Since the paper frames this as a realistic candidate-screening pipeline, the omission matters.

9. **Positioning relative to related work is somewhat narrow for a paper making general claims about candidate ranking from modern PPI representations.**  
   The related work focuses heavily on D-SCRIPT, Topsy-Turvy, xCAPT5, structure-based pipelines, and text models, which are relevant. Still, the experimental positioning would be stronger with at least some discussion of more recent PPI predictors based on protein language models or graph/hybrid architectures, especially because the paper’s retrieval logic is potentially applicable beyond the two backbones emphasized here. As written, the paper reads a bit too tied to a specific family of backbones, which weakens the “general framework” claim.

## Questions
1. Please define exactly how the active region \(I_k\) is extracted from the residue activation profile. What is the thresholding rule for “highly activated residues,” how are contiguous segments determined, and how are ties handled? A precise algorithm or pseudocode would substantially increase my confidence.

2. Please clarify **Equation (6)**. Is the D-SCRIPT interaction score really implemented as \(\max_{ij} C_{ij}\), or is the actual D-SCRIPT scalar output used? If the latter, Equation (6) is incorrect and should be fixed.

3. Can you provide an ablation that compares:  
   (a) direct model probability,  
   (b) full-protein embedding similarity without active-region selection,  
   (c) your active-region similarity retrieval?  
   This would isolate whether the gain truly comes from interpretability-guided localization rather than from using known-partner similarity more generally.

4. Can you report final post-re-ranking metrics, for example Recall@k, nDCG@k, MAP@k, MRR, on the end-to-end pipeline, rather than only pairwise maintain-or-improve percentages in **Table 2**? This is probably the single most important missing experiment for evaluating the proposed two-stage system.

5. Please explain why MAP@k equals Recall@k in so many rows of **Table 1**, and why some entries in the table are blank or appear misaligned. If there is a task-specific reason, spell it out.

6. How does performance vary with the number of known partners \(|KP(p)|\)? A degree-stratified analysis would be very informative, because the method’s utility likely depends heavily on this quantity.

7. For the cross-encoder re-ranker, could you clarify whether tuning, threshold choices, and model selection were performed strictly without touching any v12-based evaluation signal? The paper gives a reassuring high-level description, but a more explicit training/validation/test protocol would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond the standard caveat that biological interaction prediction can affect downstream biomedical decision-making. The paper itself is a computational ranking study and does not raise a clear ethics-review trigger based on the information provided.

## Soundness Rating
2: fair. The paper is built around a sensible idea and reports promising empirical results, but key parts of the method are under-specified, one equation appears inconsistent with the underlying model, and the evaluation does not fully support the strongest end-to-end claims.

## Presentation Rating
3: good. The paper is generally readable, motivated, and well structured, and **Figure 1** is helpful. However, several sections contain awkward or repetitive wording, and the presentation of **Table 1** in particular is not publication-ready.

## Contribution Rating
2: fair. The task framing is useful and the interpretability-guided retrieval idea is interesting, but the empirical validation and methodological specification are not yet strong enough for me to view this as a clear ICLR-level contribution in its current form.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper tackles an important practical problem and has a promising core idea, but the current manuscript leaves too many methodological details unspecified and does not yet provide sufficiently clean, end-to-end evidence for the proposed two-stage ranking pipeline.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main equations, figures, and tables carefully, though some implementation details are missing from the paper and limit absolute certainty.