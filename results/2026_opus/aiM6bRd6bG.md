I've read the paper. Now let me do calibration search to anchor the score.Now I have enough to score. Let me write the final review.

## Summary

The paper introduces the "PPI candidate ranking" task — given a target protein with known partners, rank novel candidates by interaction likelihood — and proposes a two-stage pipeline: (i) interpretability-guided retrieval that scores candidates by max cosine similarity to "active" residue regions of known partners (extracted from D-SCRIPT/Topsy-Turvy contact maps), followed by (ii) a re-ranking step combining D-SCRIPT IS, pDockQ from SpeedPPI, TF-IDF/Jaccard text features, and biomedical LLM scorers. Evaluation uses STRING v11 → v12 prospective rediscovery on a CD-HIT filtered human subset.

## Strengths

- **Prospective benchmark design.** The v11→v12 transition (Section 5.1) tests a genuinely forward-looking question — can a model anticipate interactions confirmed only in a later release — rather than retrospective classification. The resulting test set of 279,568 new positives is substantial.
- **Real and concrete early-rank improvements.** Table 1 shows D-SCRIPT Recall@10 rising from 0.0124 to 0.2641 and MRR from 0.0340 to 0.1685, with similar gains for Topsy-Turvy (Recall@10 0.00117→0.1106; MRR 0.0256→0.0925). Even after discounting the comparison-fairness caveat below, these are nontrivial reshapings of the early rank list.
- **Problem formulation is a real contribution.** Section 4 formally defines candidate ranking as ranking candidates in P\KP(p) by predicted likelihood given KP(p) — distinct from binary pair classification and well-matched to the wet-lab triage motivation.

## Weaknesses

### Fatal
None. The methodological concerns below are real and substantial but do not invalidate the existence of the reported improvements; they bear on the interpretation of those improvements.

### Major

- **The headline comparison conflates "use known partners" with "use active regions" (Section 5.3 / Table 1).** The proposed method scores p_c by cosine similarity to anchors in KP(p) (Eqs. 3–5), while D-SCRIPT, Topsy-Turvy, and xCAPT5 baselines just score the pair (p, p_c) with no KP(p) conditioning. The missing baseline is the trivial ablation — max cosine similarity to *full* known-partner embeddings (no contact-map filtering), with the same KP(p) anchor set. Without it, the reader cannot tell whether the gains come from "using known partners as anchors" (interolog/paralog-style transfer in embedding space) or from "the contact-map-derived active region" (the actual claim of interpretability-guided retrieval). Because the contribution is framed as the latter, this gap directly bears on whether the experiments support what the paper says they do.

- **"Two orders of magnitude" is not what Table 1 shows.** D-SCRIPT MRR moves 0.034→0.169 (~5×), Topsy-Turvy MRR 0.026→0.093 (~3.6×). The largest ratios (e.g., Recall@5 0.0071→0.1832, ~26×) are still <1.5 orders of magnitude. The abstract, §5.3, and §6 all use the "two orders of magnitude" framing; the underlying improvements are real, but the headline claim is inflated and should be revised.

- **Re-ranking is evaluated with a metric that cannot quantify what it should (Table 2 / §5.2).** Table 2 reports pairwise "maintain-or-improve" fractions on the 2,280 candidate pairs surviving top-10 retrieval. This does not tell the reader (a) how much absolute Recall@k/MRR/Avg. Rank changes after re-ranking, (b) the magnitude of position shifts among rediscoveries, or (c) anything about partners outside top-10 — which, given Recall@10 ≈ 0.26 for D-SCRIPT, is at minimum 74% of true v12 partners. The mechanical ceiling of re-ranking is not acknowledged, and the "best re-ranker" claim rests on a pairwise diagnostic rather than an absolute metric. Absolute post-re-ranking metrics on the full pipeline are needed to support the conclusion that re-ranking adds value.

- **Re-rankers are not on the same footing (§4.2 end; §5.3).** PubMedBERT is fine-tuned as a cross-encoder on STRING v11 positives/negatives (with a GroupKFold split), while BioBERT, BioMedRoBERTa, and Sentence-BioBERT are used zero-shot via cosine similarity over text profiles. PubMedBERT then "wins" Table 2 at 75.5% maintain-or-improve. The paper's own caveat — "it is uncertain if their gains reflect…latent knowledge of interactions from the training data" — applies most sharply to the very re-ranker held up as the winner. A zero-shot PubMedBERT control, or a fine-tuned-with-same-protocol set of all four, would be needed for the comparison to be clean.

### Minor

- **The asymmetry in Eq. 3 is unmotivated (§4.1).** The known partner gets the active-region restriction (I_k), but the candidate p_c is scanned exhaustively across all windows of length |I_k|. Why not also restrict p_c by its own contact-map activation against p? The current asymmetry is not justified, and an ablation on multi-segment aggregation (vs. picking only the single highest-average contiguous segment) would directly test the design choice.

- **Discovery vs. homology question is unaddressed (§6 limitations).** CD-HIT clusters at 40% identity, which removes close redundancy but leaves paralogs above 40% identity in the candidate set. Because the method ranks by similarity to known-partner active regions, a stratification of v12 rediscoveries by sequence/structural similarity to the closest v11 partner of the same target would directly indicate how much of the gain is interolog/homology retrieval vs. genuinely novel binding. The paper acknowledges the modeling assumption ("novel interactions follow mechanisms similar to known ones") but does not quantify the homology component, leaving open whether this is "prospective discovery" or "modernized interolog transfer."

- **Candidate-set size and per-protein ranking universe are ambiguous (§5.1).** Negative sampling at 10:1 is mentioned for training but the ranking universe is unclear; with Avg. Rank values of 240–900 and Recall@500 ≈ 0.5–0.8, the universe is clearly larger than 500, but the explicit per-protein candidate-set size should be stated so Avg. Rank is interpretable.

- **pDockQ underperformance attributed to seed sensitivity but not quantified (§5.3).** The paper attributes pDockQ's weak re-ranking to AlphaFold2's seed sensitivity but does not measure variance across seeds. A small multi-seed analysis would either support or refute this explanation.

### Trivial

- None substantive — formatting/parser artifacts are excluded by policy.

## Nice-to-Haves

- Replace Table 2's pairwise diagnostic with absolute post-re-ranking Recall@k/MRR/Avg. Rank, and report the fraction of true partners promoted into top-5 from positions 6–10 (the quantity that actually matters for wet-lab triage).
- Add the "full known-partner cosine, no active region" baseline; this single experiment is what gates the interpretability-guided claim.
- Stratify rediscoveries by sequence similarity to the nearest v11 partner to disentangle homology transfer from novel-mechanism retrieval.
- Either add a zero-shot PubMedBERT control or fine-tune all biomedical encoders symmetrically.

## Removed Points

These points are flagged to be removed; treat them with caution.

- Strength: "interpretability-guided retrieval dramatically improves early ranking" framed as 4–5× MRR and >20× Recall@10 improvement — the magnitude is real but the harsh critic correctly notes the comparison is between a KP(p)-conditioned method and KP(p)-unaware baselines, so the strength is overstated relative to the comparison's informativeness; kept above only as a more measured statement.
- Strength: "Multi-source re-ranking measured via systematic rank-shift analysis" as written by the strength finder — moved to a weakness because the metric, on inspection, cannot quantify absolute re-ranking value (Major weakness above).
- Harsh critic's note about Bepler & Berger embedding dimension d=6165 being "unusual / likely OCR" — the paper's value is what it is, this is a formatting/parser concern and the critic himself flagged it as not a paper flaw.
- Harsh critic's complaint about §5.3 discussion of Jaccard/TF-IDF being a different feature view than embedding cosine — this is largely a reframing of Major weakness 1 (missing apples-to-apples baseline). Merged.
- Harsh critic's "limitation understates deeper concern about more-of-the-same bias" — partly redundant with the homology stratification point already retained in Minor.

## Novel Insights

None beyond the paper's own contributions. The "use active residue regions of known partners as anchors" is an intuitive inductive bias and the v11→v12 prospective framing is the most genuinely fresh idea here. The reviewers' critiques converge on a single structural point — that the experiments do not isolate which of two plausible mechanisms (KP-conditioning vs. active-region selection) is doing the work.

## Suggestions

1. Add a "full known-partner cosine similarity" baseline using the same KP(p) anchor set. This is the single most important experiment.
2. Replace Table 2 with absolute post-re-ranking metrics on the retrieval-then-rerank pipeline. Keep the pairwise table as a supplementary diagnostic.
3. Stratify v12 rediscoveries by sequence/structural similarity to the closest v11 partner; report MRR/Recall@k within each similarity stratum.
4. Rephrase "two orders of magnitude" wherever it appears to match the actual ratios (roughly 4–25× depending on the metric).
5. Either fine-tune all biomedical encoders on STRING v11 with the same protocol or report a zero-shot PubMedBERT control in Table 2.
6. State explicitly the per-protein candidate universe size and report multi-seed variance for the pDockQ branch.

## Calibration Summary

**Round 1 anchors retrieved:**
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/S2WHlhvFGg.md (avg 3.00, R1 low) — DTI domain adaptation; weaker theory paper, less topically aligned.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/An87ZnPbkT.md (avg 3.00, R1 low) — docking algorithm selection; weak, unrelated.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/44IKUSdbUD.md (avg 3.00, R1 low) — gene-gene interaction sampling, not very similar.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/jqx5XI4Yr3.md (avg 3.40, R1 low) — ProteinAdapter, incremental adapter paper.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/QfyZ28FpVY.md (avg 4.00, R1 mid) — DEL-Ranking, ranking-based denoising; analogous ranking flavor.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/eh1fL0zw8o.md (avg 6.00, R1 mid, **read in full**) — LLaPA for PPI; richer multimodal architecture, mixed reviews, still rejected. Stronger contribution than this paper.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/wCwz1F8qY8.md (avg 5.00, R1 mid, **read in full**) — DeepSSInter, PPI contacts; incremental with comparison concerns. Comparable issue profile to this paper.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/xcMmebCT7s.md (avg 5.80, R1 mid) — PPIformer for designing PPIs; a larger, more cohesive contribution than this one.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/gHLWTzKiZV.md (avg 8.00, R1 high) — Flow matching for docking; methodologically much stronger.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/ja4rpheN2n.md (avg 8.00, R1 high) — GeSubNet; stronger framework.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/kJFIH23hXb.md (avg 8.00, R1 high) — FoldFlow; much stronger.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/zMPHKOmQNb.md (avg 8.00, R1 high) — Discrete Walk-Jump Sampling; much stronger.

**Round 1 bracket:** between 3.5 and 5.5 — this paper is clearly not in the strong (≥7.5) band; it's stronger than the weakest 3.0–3.4 anchors because the task formulation is genuinely novel and the gains are real, but it has substantive comparison-fairness problems that put it below the strongest anchors.

**Round 2 anchors retrieved:**
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/jsQPjIaNNh.md (avg 5.25, R2, **read in full**) — Inter-protein similarity for function prediction; comparison fairness issues, retriever-vs-predictor framing. Closest topical match. This paper's missing-baseline issue is comparable in spirit but somewhat more central to the headline claim.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/GDDqq0w6rs.md (avg 4.75, R2) — Gene-property benchmark; mixed.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/ZkpDdCQUC4.md (avg 4.60, R2) — NovoBench-100K; protein ranking benchmark, comparable execution quality.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/gB2ZeqDpl6.md (avg 4.00, R2) — DTI benchmark; weaker.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/C81bqFCmMf.md (avg 5.75, R2) — Multi-omics benchmark.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/opv67PpqLS.md (avg 5.67, R2) — DNALongBench.

**Narrowing logic:** This paper sits closer to jsQPjIaNNh (5.25) and ZkpDdCQUC4 (4.60) — papers that introduce a useful retrieval/ranking framing but have substantive comparison-fairness or experimental-design gaps. The "two orders of magnitude" overclaim plus the missing full-embedding baseline plus the weak re-ranking metric collectively pull it below jsQPjIaNNh's 5.25. It is stronger than gB2ZeqDpl6 (4.00) because the task formulation and empirical lift are more substantive.

Final placement: **4.0**. Stronger than pure 3.0–3.4 anchors (real numerical lift, real task novelty) but below 5.0–5.25 anchors (the central comparison does not isolate the claimed contribution, and one headline framing is inflated).

## Scoring axes

- **Originality:** Medium. The task framing (prospective candidate ranking with KP(p) anchors) is fresh; the underlying machinery (cosine similarity over selected residue regions) is straightforward.
- **Importance:** Yes — wet-lab triage from computational rankings is a real problem.
- **Claims supported:** Partially. The "interpretability-guided" claim is undermined by the missing same-anchor full-embedding baseline. The "two orders of magnitude" framing is overstated. Re-ranking value is asserted via a metric that cannot quantify it.
- **Soundness of experiments:** Medium-low. Setup is reasonable but the comparison is structurally apples-to-oranges; the strongest re-ranker is on different footing from its peers.
- **Clarity:** Reasonable; equations and pipeline are followable.
- **Value to community:** A useful task definition and a real (if narrower than claimed) empirical result; with the missing baselines and absolute re-ranking metrics added, this becomes a solid contribution.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>