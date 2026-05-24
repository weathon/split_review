Now I have thorough calibration. Let me write the consolidated review.

## Summary

This paper introduces the problem of PPI candidate ranking — given a protein and its known interactors, rank novel candidate proteins by likelihood of interaction — and proposes a two-stage framework. The first stage uses interpretability-guided retrieval: from D-SCRIPT/Topsy-Turvy predicted contact maps, the method identifies the "active" residue region of each known partner, then ranks candidates by cosine similarity between that region and sliding windows over candidate embeddings. The second stage re-ranks the top-10 candidates using 10 different signals (interaction scores, pDockQ, functional/ semantic similarity, and three biomedical LLMs). The framework is evaluated prospectively on STRING v11→v12 (279,568 novel interactions), and the paper reports substantial improvements over raw prediction probabilities from the same underlying models.

## Strengths

1. **Prospective evaluation paradigm using successive STRING releases.** Instead of a static benchmark, the paper tests whether models anticipate interactions experimentally confirmed only in a later database version (v11→v12). This forward-looking design (Section 5.1) directly addresses whether computational predictions have practical value for guiding wet-lab experiments, and the scale (279,568 new positives) makes this one of the more rigorous prospective PPI evaluations available.

2. **Interpretability-guided retrieval from active embedding regions is a well-motivated idea.** Rather than naively using the full embedding or raw prediction scores, the method extracts residues highlighted by predicted contact maps and computes similarity only on those regions (Section 4.1, Eq. 3, Figure 1). The results in Table 1 show that this approach dramatically improves early ranks — e.g., Recall@10 rises from 0.0124 (D-SCRIPT raw score) to 0.2641, MRR from 0.0340 to 0.1685. The idea of using model internals as a structural lens for ranking is creative and extends prior case-specific work (Borghini et al., 2024) to systematized interactome-scale retrieval.

3. **Comprehensive multi-source re-ranking with pairwise rank-shift analysis.** The re-ranking module (Section 4.2) integrates ten different signals: interaction scores, structural plausibility (pDockQ), five functional/semantic similarities, and three LLM embeddings. Table 2 quantifies how each signal changes the ranking of true novel partners relative to every other signal. This systematic cross-comparison goes beyond prior work and produces useful findings (e.g., PubMedBERT improves/maintains 75.5% of rediscoveries; pDockQ is poorly suited for direct ordering at just 47.2%). The cross-encoder fine-tuning is carefully designed with GroupKFold protein-level splitting to prevent leakage (Section 4.2).

4. **Large-scale evaluation with practically interpretable hit rates.** The best configuration achieves Success@5 of 7.78% (D-SCRIPT backbone) and Recall@5 of 18.32%, meaning roughly one in five of the top five candidates is a true novel partner. The paper reports metrics at multiple cutoffs (k=5 to 500), providing a concrete sense of what experimentalists can expect.

5. **Careful experimental design preventing data leakage.** The cross-encoder (PubMedBERT) is trained exclusively on STRING v11 with protein-level GroupKFold, and evaluation is on entirely disjoint v12 interactions. This temporal separation adds rigor that many PPI evaluations lack.

## Weaknesses

### Major

1. **Missing ablation: known-partner baseline without active-region selection.** The paper's core comparison pits the proposed method (which uses known partners + active-region selection) against raw prediction probabilities from D-SCRIPT/Topsy-Turvy/xCAPT5 (no knowledge of known partners). This leaves a critical attribution gap: the large improvements in Table 1 could come from (a) simply conditioning on known partners (e.g., ranking candidates by cosine similarity to any known partner's full embedding) or (b) the active-region selection mechanism specifically. Without a baseline that uses known partners with full embeddings (e.g., averaging known-partner embeddings and ranking by cosine similarity to that average, or taking max similarity to any known partner's full embedding), we cannot tell which component drives the improvement. The paper claims "two orders of magnitude" improvement, but this overstates what is demonstrated because a simpler known-partner baseline could plausibly produce similar gains. This is the single most important experiment the paper is missing.

2. **Re-ranking evaluation shows rank-shift fractions but not actual retrieval improvement.** Table 2 reports pairwise rank-shift fractions (e.g., PubMedBERT improves or maintains 75.5% of rediscoveries vs. cosine). However, we are never shown whether re-ranking actually improves standard retrieval metrics — recall@k, precision@k, MRR, or success@k — relative to the initial cosine ranking. A re-ranker could hypothetically maintain or improve most pairwise positions while still degrading overall ranking quality (e.g., by pushing a few true positives down by many slots). Without evaluating the actual ranking after re-ranking, the claim that re-ranking "refines prioritization" is only partially supported. Adding metrics like Recall@1, Recall@3, and MRR after re-ranking would directly address this.

### Minor

3. **The "two orders of magnitude" framing overstates the measured improvement.** Checking Table 1, the best improvements are roughly 20× (Recall@10: 0.0124→0.2641 for D-SCRIPT), not 100×. While the improvement is substantial, "two orders of magnitude" is imprecise and should be tempered, especially given the missing baseline issue above.

4. **STRING v12 circularity for structure-based confound.** The paper notes that STRING v12 includes structure-based predictions (Szklarczyk et al., 2023) that may share methodology with the pDockQ re-ranking signal. The paper acknowledges this briefly. This concern is partially mitigated because (a) the main retrieval result (Table 1) does not use pDockQ, (b) pDockQ is the *worst* re-ranking signal (47.2% improvement), and (c) the paper discusses it. However, it remains a confound worth explicitly bounding — e.g., estimating the fraction of v12 interactions from structure-based sources and showing the main results hold on a filtered subset.

5. **No variance or significance reported in Table 1.** All metrics are reported as point estimates without standard deviations or confidence intervals across proteins. With thousands of proteins per split, some measures of variability would help assess reliability.

6. **Unclear applicability scope.** The method requires at least one known partner for each target protein. The paper does not report what fraction of the human proteome this covers in STRING v11, which would help readers gauge practical applicability.

### Trivial

7. Minor: The parsing artifact in the abstract ("~~D~~SCRIPT D-SCRIPT") and the repeated/restructured sentence in Section 4.1's first paragraph should be cleaned up in revision.

## Nice-to-Haves

- Adding a known-partner baseline using full embeddings (no active-region selection) would directly isolate the contribution of the interpretability-guided component and is the most impactful addition the authors could make.
- Reporting recall/MRR/precision@k after re-ranking (not just rank-shift fractions) would complete the re-ranking evaluation.
- Reporting the fraction of proteins with at least one known partner in STRING v11 would clarify the method's coverage.

## Removed Points

- *"Active-region selection threshold is underspecified"* — Removed per hard rule: the paper explicitly states "Details of experimental setup and parameter choices are reported in Appendix A.1," which was stripped by the parser. The threshold specification likely appears in the appendix.
- *"High dimensionality of flattened embeddings (Eq. 3) not discussed"* — Removed: cosine similarity on high-dimensional vectors from sliding windows is standard practice; the paper normalizes via cosine similarity which already accounts for scale issues.
- *"Cross-encoder vs. unsupervised comparison asymmetry"* — Removed per hard rule: this is a known-partner baseline issue already captured in Weakness #1. The asymmetry is noted in the paper's discussion of methods.
- *"Pure formatting/style nitpicks"* — Removed per hard rule.
- *"Computational cost not mentioned"* — The paper references Figures 2 and 3 which present runtime information (not visible due to parser). Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a well-identified methodological gap (the missing known-partner ablation) that the authors should address, but do not contribute new scientific insights beyond what the paper already proposes.

## Suggestions

1. **Add a known-partner baseline without active-region selection.** The simplest version: rank candidates by max cosine similarity between the target protein's *full embedding* and each candidate's full embedding (or between each known partner's full embedding and each candidate). If this baseline performs comparably to the active-region method, the contribution of the active-region component is minimal; if not, the active-region selection is validated.

2. **For the re-ranking evaluation, additionally report recall@1, recall@3, and MRR** for the re-ranked top-10 lists vs. the cosine-only top-10 baseline. These metrics give a cleaner picture of whether re-ranking actually improves retrieval.

3. **Temper the "two orders of magnitude" claim** to something like "substantial improvements (up to ~20× on early-recall metrics)" or specify which metrics achieve this magnitude.

4. **Add standard deviations or confidence intervals** to Table 1 metrics, or at minimum note whether trends are consistent across proteins.

5. **Report the coverage fraction** of proteins with KP(p) ≠ ∅ in STRING v11 so readers know the method's scope.

6. **Discuss the potential STRING v12 structure-prediction confound more quantitatively.** If possible, filter out v12 interactions originating from structure-based predictions and show the main results hold.

## Score and Decision

### Calibration Summary

**Round 1 (bracketing, all queries on PPI/ranking topics):**
- Weak band (avg < 3.5): 44IKUSdbUD (3.00), nWO75tVjfp (3.00), n9CqhWGK4o (2.50), S2WHlhvFGg (3.00) — all clearly weaker, typically incremental or flawed methods.
- Middle band (3.5–7.5): eh1fL0zw8o / LLaPA (6.00), itGkF993gz / MAPE-PPI (5.67), jsQPjIaNNh / ProtIR (5.25), wCwz1F8qY8 / DeepSSInter (5.00) — most topically relevant and closest in quality.
- Strong band (avg > 7.5): ja4rpheN2n (8.00), KbetDM33YG (8.00), zMPHKOmQNb (8.00), gHLWTzKiZV (8.00) — clearly stronger papers with more mature architectures and comprehensive experimental validation.

**Round 1 bracket: 5.0–6.0**

**Round 2 (narrowing within bracket):** Anchors in (4.5, 6.5) and (5.0, 7.0) confirmed the bracket: LLaPA (6.00, Reject), MAPE-PPI (5.67, Accept), ProtIR (5.25, Reject), DeepSSInter (5.00, Reject), SMP (5.50, Reject), MARS (5.50, Reject).

**Comparative judgment:** This paper is stronger than DeepSSInter (5.00, Reject) and ProtIR (5.25, Reject) because its evaluation framework (prospective STRING v11→v12, temporal separation, no leakage) is more rigorous. It is comparable to MAPE-PPI (5.67, Accept) and LLaPA (6.00, Reject) in ambition and quality but has a clearer methodological gap (the missing ablation) than MAPE-PPI. The strongest papers in the corpus (8.00) are clearly at a higher level of maturity.

**Final score: 5.5.** The paper has genuine contributions (problem formulation, prospective evaluation design, interpretability-guided retrieval idea) and is well-written. However, the missing ablation (known-partner baseline without active-region selection) prevents the central claim about the active-region component from being fully supported, and the re-ranking evaluation is incomplete. These are addressable weaknesses, but the paper as submitted does not fully validate its strongest claims. With the missing ablation addressed and the re-ranking evaluation completed, the paper could warrant acceptance.

**Decision: Reject** — the paper requires major revisions (specifically, the missing ablation and complete re-ranking evaluation) before its contributions are convincingly demonstrated. The core ideas are solid, and I would support acceptance after these issues are resolved.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>