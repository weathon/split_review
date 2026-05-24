## Summary

This paper introduces PPI Candidate Ranking — a task where, given a target protein and its known interaction partners, the goal is to rank novel candidate proteins by likelihood of interaction. The authors propose a two-stage framework: (1) interpretability-guided retrieval that uses D-SCRIPT/Topsy-Turvy contact maps to identify active residue regions in known interactors and ranks candidates by cosine similarity over those activated embeddings; (2) a re-ranking module that refines the top-10 candidates using additional signals (interaction scores, structural plausibility via SpeedPPI, and semantic/LM-based features). Evaluation is performed prospectively using STRING v11→v12, where v11 provides known interactions and v12's newly added interactions serve as ground truth. The interpretability-guided step shows substantial gains over raw interaction probability baselines (e.g., D-SCRIPT Recall@10 improves from 1.2% to 26.4%).

## Strengths

- **Novel, prospectively evaluated task definition**: The paper defines PPI candidate ranking as a distinct problem and constructs a rigorous prospective evaluation using two successive STRING releases (v11→v12). This directly addresses the lack of prospective validation in prior PPI prediction work and provides a realistic testbed for prioritizing experimental screening (Section 1, Section 4, Section 5.1).

- **Leakage-free experimental design**: The dataset construction applies CD-HIT clustering at 40% identity, uses only v11 interactions for training/anchors, and reserves v12 interactions as truly novel positives. Cross-encoder fine-tuning uses GroupKFold by protein identity (Section 5.1, Section 4.2), ensuring no protein-level contamination. This is careful and well-executed.

- **Substantial ranking improvements demonstrated**: Table 1 shows the interpretability-guided method reshapes rankings dramatically — D-SCRIPT Recall@10 rises from 0.0124 to 0.2641, MRR from 0.0340 to 0.1685. The rich metric suite (Recall, Precision, MAP, nDCG, Success, MRR, Average Rank at cutoffs k∈{5,10,50,100,200,500}) provides a detailed picture of ranking quality.

- **Multi-signal re-ranking analysis**: Table 2 systematically evaluates multiple complementary evidence sources (interaction scores, structural plausibility, TF-IDF, token/location/key-term overlap, BioBERT, BioMedRoBERTa, PubMedBERT) via pairwise rank-shift comparisons. PubMedBERT achieves 75.5% maintain-or-improve rate over the cosine baseline, and lightweight semantic heuristics show surprisingly robust gains (~70%).

## Weaknesses

### Fatal
None.

### Major

- **Missing whole-protein embedding cosine similarity baseline (isolates the core mechanism)**. The paper's central claim is that contact-map-guided activation selection is the key to improved ranking. But the comparison in Table 1 is only against raw interaction probabilities from D-SCRIPT, Topsy-Turvy, and xCAPT5. There is no baseline that ranks candidates by cosine similarity of *whole-protein embeddings* without contact-map selection. This means the observed gains conflate two changes: (a) switching from supervised interaction scores to embedding cosine similarity, and (b) the contact-map-guided selection of active residue regions. Without the whole-protein embedding cosine similarity control, a reader cannot determine whether the interpretability mechanism adds any value over a simpler embedding-similarity baseline. This is a structural gap in the experimental design that directly affects the paper's main contribution claim.

- **Re-ranking evaluation does not demonstrate retrieval improvement**. The re-ranking experiments (Table 2, Section 5.2–5.3) are restricted to the top-10 candidates from the initial ranking, and the only reported metric is the fraction of interactions whose rank is maintained or improved when switching between re-rankers. No absolute retrieval metrics (Recall@k, MRR, nDCG, Precision@k) are reported after re-ranking. It is therefore impossible to assess whether re-ranking actually improves overall retrieval quality — it could merely be rearranging the top-10 without pushing more true positives into higher positions. The paper frames re-ranking as a core part of the framework (Section 4.2, abstract: "integrating complementary sources of evidence"), yet never demonstrates it adds practical value beyond the initial interpretability-guided step.

### Minor

- **"Two orders of magnitude" is an overstatement**. The paper claims improvements "by two orders of magnitude" (Section 1, line 29) and "by up to two orders of magnitude" (Section 6, line 526). The best improvement in Table 1 is approximately 26× (Recall@5 for D-SCRIPT: 0.0071→0.1832), which is roughly 1.4 orders of magnitude; most metrics show 5–25× gains. Two orders of magnitude (100×) is not achieved by any reported metric.

- **"Integration" language in the abstract is not supported by experiments**. The abstract states the framework "refines prioritization by integrating complementary sources of evidence," but the re-ranking experiments evaluate each signal in isolation (Table 2). No combined multi-signal re-ranker is presented or evaluated. The language should be softened or a joint strategy demonstrated.

- **No empirical breakdown by number of known interactors**. Section 6 acknowledges the method relies on having known partners and may fail for proteins with few interactors, but no analysis partitions performance by the number of known partners. Such a breakdown would substantiate the limitation discussion and help practitioners understand applicability.

### Trivial

- The description of negative example generation at a 10:1 ratio in Section 5.1 is a training-protocol artifact that creates mild confusion about how the retrieval candidate set is constructed, though the core setup ($P \setminus KP(p)$) is clear.

## Nice-to-Haves

- A contact-map quality sanity check (e.g., randomizing contact maps and measuring ranking degradation) would build confidence in the interpretability mechanism.
- Exploring whether xCAPT5 embeddings could be used analogously (instead of only its interaction scores) would make the comparison more informative.
- Runtime figures mentioned in the text would help assess practical feasibility for screening pipelines.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "The paper overstates integration — there is no combined multi-signal re-ranker."** Partially retained as a Minor weakness (the abstract language is overstated), but downgraded from the critic's framing as a structural failure. The pairwise analysis in Table 2 does provide useful complementarity information even without a joint model.

- **Harsh Critic: "The abstract's statement about improvement over SOTA models is misleading — it's over raw scores, not the models themselves."** Removed. The paper is clear in the results section about what is being compared. The abstract phrasing is slightly imprecise but not misleading to a reader who reaches Table 1.

- **Harsh Critic: "The definition of active residue intervals is given without discussion of alternatives."** Removed. The choice is clearly described and reasonable; demanding an exhaustive discussion of alternatives is scope creep for a paper introducing a new task and framework.

- **Harsh Critic: "The xCAPT5 baseline is only tested with raw prediction scores."** Moved to Nice-to-Haves. Exploring xCAPT5 embeddings is a reasonable extension but not a weakness — the paper's method is built on D-SCRIPT/Topsy-Turvy's interpretable contact-map structure, which xCAPT5 does not provide.

- **Strength Finder: "Two-order magnitude gains."** Weakened — the gains are substantial but not two orders of magnitude. Retained as a strength with corrected framing.

- **Strength Finder: "Multi-signal re-ranking improves prioritization."** Weakened — the re-ranking analysis is informative but incomplete without absolute retrieval metrics.

## Novel Insights

The paper's strongest contribution is the framing of PPI prediction as a *ranking* problem with prospective evaluation, rather than a static classification benchmark. The use of successive STRING database versions to create a realistic time-split evaluation — where v11 provides known interactions and v12 provides genuinely novel positives — is a methodological insight that could benefit the broader PPI prediction community beyond this specific method. Additionally, the finding that lightweight semantic features (TF-IDF, token/location/key-term overlap) achieve ~70% maintain-or-improve rates in re-ranking (Table 2) is a practically useful observation: it suggests that even coarse functional annotation signals can meaningfully sharpen retrieval lists without requiring expensive structural modeling or large language models.

## Suggestions

- Add the whole-protein embedding cosine similarity baseline to Table 1. This is the single most important addition — it would directly test whether the contact-map-guided activation selection is responsible for the observed gains, and would allow the paper to properly claim credit for its core mechanism.

- Complete the re-ranking evaluation by reporting absolute retrieval metrics (Recall@k, MRR, nDCG) on the re-ranked lists, and demonstrate that re-ranking pushes more true partners into the very top positions relative to the initial cosine ranking. If re-ranking does not improve these metrics, the paper should honestly report that and adjust its claims accordingly.

- Soften the "two orders of magnitude" claim to reflect the actual ~5–25× improvements observed, or point to the specific metric(s) where a 100× gain is achieved if one exists.

---

**Originality:** The task formulation and prospective evaluation paradigm are genuinely novel for PPI prediction. The interpretability-guided retrieval approach adapts prior work (Borghini et al., 2024) from a single case study to a systematic, large-scale framework.

**Importance:** The problem — prioritizing experimental validation of predicted interactions — is practically significant given the cost and throughput constraints of wet-lab PPI assays. A method that reliably surfaces true novel interactions in the top ranks has clear utility.

**Claims supported:** The claim of improved ranking over raw interaction scores is well-supported by Table 1. The claim that the interpretability mechanism (contact-map selection) drives this improvement is not adequately isolated. The claim that re-ranking adds value is not demonstrated with appropriate metrics.

**Soundness:** The prospective evaluation design is sound and well-controlled for leakage. The missing baseline and incomplete re-ranking metrics are the main threats to soundness.

**Clarity:** The paper is generally well-written. The problem setup (Section 4) is clearly defined with formal notation. The re-ranking section (4.2) clearly describes each signal. Some overstatements in the abstract/conclusion slightly undermine precision.

**Value to community:** The STRING v11→v12 prospective benchmark and the PPI candidate ranking task formulation are valuable contributions that could spur follow-up work, even if the proposed method's specific mechanisms need further validation.

## Score and Decision

**Calibration anchor comparison (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `1S8ndwxMts` — Protein generative model metrics | 3.00 | R1 (weak) | Paper under review is substantially stronger — it has a concrete task, clear evaluation, and demonstrated improvements |
| `jsQPjIaNNh` — ProtIR protein function prediction | 5.25 | R1/R2 (mid) | Paper under review is stronger — cleaner experimental design, clearer task framing, better-controlled prospective evaluation |
| `itGkF993gz` — MAPE-PPI microenvironment-aware PPI | 5.67 | R2 (narrow) | Paper under review is somewhat stronger — more novel task framing, cleaner evaluation, though both have baseline gaps |
| `eh1fL0zw8o` — LLaPA multimodal PPI | 6.00 | R1/R2 (mid) | Comparable quality — LLaPA has more architectural novelty; current paper has cleaner evaluation and prospective design |
| `RyWypcIMiE` — Drug design evaluation reframing | 6.50 | R2 (narrow) | Paper under review is slightly weaker — both reframe evaluation paradigms; drug design paper has more fully developed framework |
| `ja4rpheN2n` — GeSubNet disease subtype networks | 8.00 | R1 (strong) | Paper under review is clearly weaker — GeSubNet has stronger novelty, richer experiments, and biological validation |

**Round 1 bracket:** 5.25–8.00 → narrowed to plausible range 5.5–7.0.  
**Round 2 narrowing:** Anchors at 5.25–6.50 confirm the paper sits in the 5.67–6.50 range. The paper is comparable to LLaPA (6.00, Reject) and somewhat below the drug design reframing paper (6.50, Accept). The two major weaknesses — missing baseline that directly affects the core claim, and incomplete re-ranking evaluation — pull it toward the lower end of this range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>