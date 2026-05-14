## Summary

This paper introduces *PPI candidate ranking* — a task that prioritizes unconfirmed protein–protein interactions for experimental validation by leveraging a target protein's known interaction partners. The authors propose a two-stage framework: (1) interpretability-guided retrieval that extracts activated residue regions from D‑SCRIPT/Topsy‑Turvy contact maps of known partners and uses region‑restricted cosine similarity to rank novel candidates, and (2) a multi‑source re‑ranking module incorporating interaction scores, structural plausibility (pDockQ), functional enrichment, and LLM‑based semantic similarity. Evaluation uses a prospective STRING v11→v12 design, demonstrating large improvements over raw interaction-probability baselines.

## Strengths

- **Novel and practically motivated problem formulation.** The paper carves out PPI candidate ranking as a distinct task — prioritizing interactions for experimental validation — which directly addresses a real bottleneck in interactome mapping. This is well-scoped and clearly motivated (Sections 1, 4).

- **Well-designed prospective evaluation.** Using consecutive STRING releases (v11→v12) as a testbed is a sound design that moves beyond static retrospective evaluation. The consistent gains across Recall@k, MAP, nDCG, MRR in Table 1 provide credible evidence that the framework reshapes rankings in practically meaningful ways.

- **Substantial improvement over interaction-probability baselines.** Table 1 shows the method lifts D‑SCRIPT Recall@10 from ~1.2% to 26.4% and Topsy‑Turvy Recall@10 from ~0.12% to 11.1%. MRR increases 4–6×. These are large, practically meaningful gains.

- **Informative multi‑source re‑ranking analysis.** Table 2 shows that semantic signals (PubMedBERT, functional enrichment) can sharpen already-retrieved top‑10 lists, with PubMedBERT improving or maintaining rank for 75.5% of rediscovered interactions. This provides actionable guidance on which complementary signals add value.

## Weaknesses

### Fatal

None.

### Major

- **Missing ablation on the region‑selection mechanism.** The paper compares the proposed method (contact‑map‑guided region selection from known partners) against baselines that rank solely by predicted interaction probability without using known‑partner information. The observed gains could arise from simply using *any* embedding similarity to known partners, not specifically from the contact‑map‑guided region selection. No ablation is provided using whole‑embedding cosine similarity to known partners (without region restriction) or random‑region selection. Without these comparisons, the claimed advantage of the active‑region extraction — a central methodological novelty — remains unsubstantiated. This weakens confidence in the specific mechanism the paper markets.

- **Re‑ranking evaluation lacks absolute retrieval metrics.** The re‑ranking analysis (Section 5.3, Table 2) reports only pairwise rank‑shift fractions ("maintained or improved") among the top‑10 candidates per query. This metric does not measure whether true partners are actually recovered at higher positions after re‑ranking. It is possible that all methods shuffle a pool of already‑correct candidates, producing high "maintain‑or‑improve" fractions without genuine gains in discovery. Standard retrieval metrics (Recall@k, MAP@k) after re‑ranking would clarify whether any of the additional signals genuinely improve candidate prioritization.

### Minor

- **Overstated "two orders of magnitude" claim.** The abstract and conclusions state improvements of "up to two orders of magnitude." The largest improvement in Table 1 is ~95× for Topsy‑Turvy Recall@10 (0.00117→0.1106), which is borderline. Most other improvements are in the 5–25× range (e.g., D‑SCRIPT Recall@10: 21×, MRR: 6.6×). The phrase overstates the typical case and should be softened to better reflect the data.

- **Active‑region extraction procedure is under‑specified.** Section 4.1 states that "maximal contiguous segments of highly activated residues" are identified, but does not define a concrete threshold for "activated." The activation score is defined as max contact probability (continuous [0,1]), but the criterion separating "activated" from "not activated" residues — needed to determine segment boundaries — is not stated. This ambiguity affects reproducibility.

- **PiNUI results are relegated to the appendix.** Appendix A.3 shows the method on PiNUI achieves far lower absolute performance than on STRING (Recall@500 of 0.133 vs. 0.814), though the *relative* improvement over D‑SCRIPT's baseline is still large (Rediscovery Ratio 0.008→0.385). This limitation is not discussed in the main text or conclusions, which present the method as broadly effective. Moving this discussion (or at least a summary) to the main paper would give a more balanced picture of generalizability.

### Trivial

- The phrase "two orders of magnitude" in the abstract and conclusions should be replaced with numerically precise language (e.g., "5–20× improvement across most metrics").

## Nice-to-Haves

- **Validate active regions against known biological interfaces.** Overlap with PDB binding interfaces or independent interface predictors would strengthen the "interpretability‑guided" label and provide biological grounding for the region‑selection mechanism.

- **Evaluate re‑ranking with standard retrieval metrics** (Recall@k, MAP@k, MRR on the re‑ranked lists) so the actual improvement in true‑partner recovery can be measured.

- **Include a whole‑embedding cosine similarity baseline** (using the full embedding of each known partner without region restriction) and a random‑segment baseline to isolate the contribution of the contact‑map‑guided region selection.

- **Extend evaluation beyond STRING.** Broader testing on datasets like IntAct or HPRD would strengthen generalizability claims beyond STRING‑derived interaction data.

## Removed Points

*These points were raised by reviewers but are flagged as unreliable — treat with caution.*

- **"Unfair baseline" framing (from Harsh Critic, Point 1).** The critic argued baselines are unfair because they don't use known-partner information. However, the baselines represent the natural deployment mode of those models (pairwise probability scoring). The paper's contribution is precisely *showing that using known partners improves over probability-only ranking*. The missing ablation (whole-embedding vs. region‑guided) is a separate, valid concern already captured under Major Weaknesses. The "unfair baseline" framing is removed as it mischaracterizes a reasonable comparison.

- **"xCAPT5 comparison is not parallel" (from Harsh Critic).** xCAPT5 outputs interaction probability scores from sequence embeddings; using it as a probability baseline is entirely parallel to D‑SCRIPT and Topsy‑Turvy. Removed.

- **"Cross‑encoder learns annotation co‑occurrence rather than genuine generalization" (from Harsh Critic).** This is speculation. The cross‑encoder is trained on STRING v11 annotations and evaluated on novel v12 interactions — a strict temporal split. Removed as an unsupported claim.

- **"Garbled pDockQ equation" (parser issue).** The equation formatting artifacts are parser‑side, not author errors. Removed per instructions.

- **"STRING v12 may not represent high‑confidence physical interactions" (from Harsh Critic).** The paper explicitly filters for binding interactions with experimental support > 0 (Section 5.1), discarding indirect associations (co‑expression, homology, text mining). Removed as factually incorrect.

- **Strength Finder: "Methodological clarity and reproducibility" as an unqualified strength.** The active‑region extraction threshold is under‑specified (see Minor Weaknesses). This strength is downgraded to neutral.

- **Strength Finder: "Additional validation on PiNUI" presented as purely positive.** The PiNUI results show substantial relative improvement but weak absolute performance. The strength is retained but contextualized.

## Novel Insights

None beyond the paper's own contributions. The paper makes a clear methodological contribution in proposing PPI candidate ranking as a task and showing that known‑partner‑guided retrieval can substantially improve ranking quality. The re‑ranking analysis provides practical evidence that semantic signals (PubMedBERT, functional enrichment) are the most cost‑effective complement to embedding‑based retrieval — a finding that could guide future work in this space.

## Suggestions

- Add a whole‑embedding cosine similarity baseline and a random‑region ablation to Table 1. This is the single most important experiment to strengthen the paper.
- Report Recall@k and MAP@k on the re‑ranked top‑10 lists for each signal in Table 2 so readers can judge whether re‑ranking improves absolute recovery.
- Define the threshold or procedure for "maximal contiguous segments of highly activated residues" explicitly (e.g., residues with activation score above the mean plus one standard deviation, or above the 75th percentile).
- Soften "two orders of magnitude" to a precise and supportable figure (e.g., "5–20×"). If retaining "up to two orders," clearly specify which metric and model pair achieves this.
- Move a summary of the PiNUI results and their implications into the main text (Section 5 or 6) for a balanced discussion of generalizability.

## Score and Decision

### Anchor comparison

- **Dp1RM3gPg8 (RaftPPI, avg 5.00, Accept Poster):** PPI retrieval with strong efficiency contribution; comparable in domain, slightly stronger in technical novelty and ablation rigor. Our paper has a better problem framing.
- **kXpXKe3KnA (HIPPO, avg 3.50, Reject):** PPI prediction framework with presentation issues and limited novelty. Our paper is clearly stronger in both presentation and contribution clarity.
- **NskQgtSdll (PepBenchmark, avg 6.00, Accept Poster):** Comprehensive benchmark paper; different category, stronger in dataset scope but our paper is more methodological.
- **S3kSOFhs5m (QCAI, avg 5.50, Accept Poster):** Interpretability method for protein binding; similar domain, slightly stronger in evaluation rigor.
- **2wshkCgNYk (avg 3.00, Reject):** Interpretability/performance trade-off on protein classification. Our paper is clearly stronger.
- **zWwU6tyDGt (avg 2.50, Reject):** Evolution-aware PU learning. Our paper is clearly stronger.

This paper makes a genuine contribution with a novel problem formulation and promising results, but the missing ablation on the core region‑selection mechanism and the re‑ranking evaluation's limited metrics weaken confidence in specific claims. It is somewhat weaker than RaftPPI (5.00) in evaluation rigor but stronger than HIPPO (3.50) in contribution clarity. Score: **5.0**.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>