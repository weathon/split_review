Now let me do calibration searches.Round-1 bracket: The most topically similar anchor is "Is Your Video Language Model a Reliable Judge?" (6.50, Accept). Rejected anchors at ~3-4.5. Initial bracket: **(4.5, 7.0)**.## Summary
VideoJudge proposes a generator–evaluator bootstrapping pipeline that synthesizes pointwise (1–5) and pairwise training data for MLLM judges of video understanding outputs, without human labels. The authors release 3B/7B trained judges plus a rubric-generating variant, construct two pointwise and two pairwise meta-evaluation benchmarks using the same pipeline, and report that the fine-tuned smaller judges match or surpass much larger zero-shot MLLMs (Qwen2.5-VL-32B/72B) across several settings. The paper also analyzes calibration, frame budgets, temperature robustness, and rubric quality.

## Strengths
- **Concrete artifact release**: Trained pointwise/pairwise judges (3B/7B), a rubric-generating variant (VideoJudgeR-3B), a bootstrapped corpus of 103,825 examples from 25K seeds, and four meta-eval benchmarks — a tangible community contribution rather than a method-only paper.
- **Data-quality validation includes human study with high agreement**: §5.2 reports Cohen's κ = 89.5 with >92% correctness on the hardest 2-vs-3 boundary cases, providing direct human evidence (not just BLEU/BERTScore) that the pairwise supervision is meaningful where the labels are most ambiguous.
- **Robustness analyses are genuinely informative**: The temperature ablation (Figure 4) shows VideoJudge holding Spearman ~0.66–0.73 while base Qwen2.5-VL-3B degrades from 0.56 to 0.42; the `maxframes` analysis (training ~240, evaluation ~120) gives concrete operational guidance.
- **Honest error analysis**: §6.2 surfaces a substantial overestimation bias (14.8% ≥2-point overestimates vs 1.5% underestimates; only 36.9% of rating-3 scored correctly), and §7 acknowledges the partial closed-loop nature of the bootstrapped benchmarks — these admissions are unusual and useful.
- **Rubric-generation contribution has independent human evidence**: Figure 3 reports 53.4% unanimous human-preferred wins over GPT-4o-mini and 63.9% over Qwen2.5-VL-72B for rubrics produced by VideoJudgeR-3B, with three annotators per pair.

## Weaknesses

### Fatal
None. The closed-loop concern is real but the paper acknowledges it (§7) and the trained artifacts still provide value on the genuinely independent benchmarks.

### Major
- **Headline "matches/surpasses 10× larger models" is partially driven by in-distribution benchmarks.** Four of the seven meta-evaluation datasets (VideoJudgeLLaVA-MetaEval, VideoJudgeVCG-MetaEval, VideoJudge-Pairwise, VideoJudge-Pairwise-H) are built by the same bootstrapping pipeline (§4.2: "generating additional responses via our bootstrapping pipeline with threshold 0") that produced training labels, and the acceptance criterion |r − r̂| ≤ α (Eq. 3) guarantees label alignment with the evaluator by construction. On the three independent benchmarks the story is more measured: on VATEX, VideoJudge-7B's RMSE (1.46) is worse than Qwen2.5-VL-72B's (1.40); on LongVideoBench, VideoJudge-7B PSUP (0.66) trails Qwen2.5-VL-32B (0.73) and 72B (0.71); on VideoAutoArena, VideoJudge-7B (85.49/87.45) loses to Qwen2.5-VL-72B (89.80/89.80). The §7 admission is too narrow given that abstract, intro, and §6 all repeat the dominance claim — the framing should be reconciled with what the independent benchmarks actually show.
- **Pairwise w/ FB vs w/o FB pattern contradicts the methodological pitch.** In Table 3, "w/o FB" frequently beats "w/ FB" — Qwen2.5-VL-32B on VAA (80.78 → 90.59), VideoJudge-3B on VJ (94.00 → 95.80), VideoJudge-7B on VJ (95.60 → 98.60), VideoJudge-7B on VAA (85.49 → 87.45). The paper's central claim is that generator–evaluator feedback is the key mechanism; if feedback hurts on multiple pairwise settings the paper needs to define what "feedback" means at inference on a pairwise benchmark (the term is never explicitly disambiguated in §6.2) and explain the pattern. As written, the table works against the thesis without acknowledgement.
- **Rubric ablation in Table 2 is missing the matched baseline.** §6.1 trains VideoJudgeR-3B on 10% of data with rubric supervision and compares it to *zero-shot* 3B/7B/32B/72B baselines. The natural attribution baseline — a non-rubric VideoJudge-3B trained on the same 10% slice — is absent, so the reported gain (MAE 0.59 vs 1.15) cannot be cleanly attributed to rubric generation rather than to fine-tuning on the slice. Since rubric generation is one of the paper's headline contributions, this is the most important missing ablation.
- **The §6.2 calibration findings are in tension with the calibration framing elsewhere.** The error analysis reports that 81.3% of rating-4 responses are scored 5 and 46.6% of rating-3 are inflated to 5 — the model effectively collapses the upper half of the scale, which is precisely the rating band where practical model-comparison decisions live. The paper still frames VideoJudge as superior on ECE in Table 1 (e.g., ECE 0.63/0.64 on VATEX). Both can be technically true (low aggregate ECE alongside collapse near the top of the scale) but the headline claim of "stronger calibration" deserves to be qualified in light of the band-specific failure.

### Minor
- **§5.1 BLEU/BERTScore monotonicity validates the wrong thing.** Figure 2 shows BLEU drops from 11.0 (5-4) to 3.0 (5-1) and BERTScore from 91.1 to 86.9. The paper concludes this validates "the controlled response generation process." This only confirms that the generator obeyed its own conditioning to produce more lexically dissimilar responses for lower targets — it is largely tautological for assessing whether the rating ladder reflects *quality* in any externally meaningful sense. The §5.2 human study tests this, but only at the 2-vs-3 boundary, so the full-scale quality calibration is not directly validated.
- **"MLLM > LLM judge, CoT doesn't help, so video inputs are crucial" overgeneralizes.** §6.1 notes the unimodal Qwen3 baselines consume MLLM-generated descriptions; the experiments therefore show *current video-to-text descriptions are lossy*, not that "providing video inputs is crucial" as a general claim. The abstract's wording goes further than the experiments support.
- **LongVideoBench adaptation as a proxy for open-ended judgment is unusual.** §4.2 adapts a multiple-choice benchmark by rating correct vs. distractor options and reporting PSUP/Δ(C-D). The abstract advertises evaluation of *open-ended* video understanding; whether scoring distractors is a faithful proxy for that ability is not argued.
- **VideoJudge-Pairwise-H accuracy is reported on the agreement-filtered subset.** §4.2 keeps only pairs where both annotators agree (≥200 from 250 sampled). This is fine for ground-truth purity but inflates measured accuracy versus reporting on the full 250 with disagreement handling — the filtered subset is, by construction, the easier half.

### Trivial
- The "first bootstrapped framework for training scalable MLLM-based evaluators across diverse video understanding tasks" claim in §1 is a precisely scoped first-of-kind statement; given prior MLLM-judge work (Prometheus-Vision, LLaVA-Critic, etc., cited in §2), a softer phrasing would be more defensible without weakening the contribution.

## Nice-to-Haves
- An **evaluator-swap experiment** — re-run the bootstrap pipeline with a different evaluator (e.g., GPT-4o) and retrain VideoJudge — would directly break the closed loop and would be the single most informative additional experiment.
- Surface the **generator/evaluator identity** and the **α threshold** in the main text rather than only the appendix, since both directly govern how to read the headline numbers.
- A version of Table 1 split by **in-distribution vs. independent benchmarks** would let readers see the difference at a glance without recomputing.
- A **hard-negatives variant** addressing the 4→5 / 3→5 collapse identified in §6.2 would close the most actionable gap the paper itself surfaces.

## Removed Points
These points are flagged to be removed, treat them with caution.

- *"Generator/evaluator identities are deferred to the appendix and this is fatal."* — The paper does specify the bootstrap process and references §A.2 for the description generator; the parser strips the appendix, so the apparent omission is not verifiable from the submission as written. Demoted into the nice-to-have above.
- *"VideoJudgeR-3B's 92.7% LLM-as-judge win rate over GPT-4o-mini is undermined because GPT-4o-mini is the judge."* — The paper does present this alongside human evaluation (Figure 3) with three annotators, so the LLM-judge dependency is not the only evidence. The human-evaluation portion stands on its own.
- *"BLEU/BERTScore on benchmarks the paper trained on are unfair to baselines."* — The asymmetry the harsh critic flagged is between in-distribution and independent benchmarks (already kept), not a strawman about lexical metrics for baselines.
- Strength: *"Small models match or surpass much larger models in pointwise evaluation (VideoJudge-3B Spearman 0.82)"* — This conflicts with the verified Major weakness that the dominance holds primarily on in-distribution benchmarks; moved here per the strength-vs-weakness conflict rule.
- Strength: *"Pairwise performance exceeds larger baselines (98.6 on VJ)"* — VJ is one of the bootstrapped (in-distribution) pairwise benchmarks; on the independent VideoAutoArena, VideoJudge-7B loses to Qwen2.5-VL-72B, so this strength is not robust as stated.

## Novel Insights
None beyond the paper's own contributions. The combination of generator-conditioned rating ladder + evaluator filtering + iterative refinement is a sensible composition of known ideas (controlled response generation, self-consistency, self-refinement), and the rubric-generation extension is a useful but incremental step. The paper's own §6.2 finding — that the trained judge collapses ratings 3 and 4 into 5 — is a genuinely useful empirical observation for the community building on this line of work.

## Suggestions
- Run the evaluator-swap experiment (different evaluator family) and report independent-benchmark performance under the swap; this directly addresses the closed-loop concern.
- Add a no-rubric, same-10%-data VideoJudge-3B baseline to Table 2 to cleanly attribute rubric gains.
- Define "w/ FB" / "w/o FB" precisely for pairwise inference in §6.2, and explain the cases where w/o FB wins.
- Restate the headline as "competitive with 10× larger zero-shot judges on independent benchmarks; superior on bootstrapped in-distribution benchmarks" rather than blanket dominance.
- Report VideoJudge-Pairwise-H accuracy on the full sample (250) with disagreement cases marked, in addition to the filtered subset.
- Either fold the 4→5/3→5 collapse into the headline framing or fix it with a hard-negative augmentation pass.

## Evaluation on Standard Axes
- **Originality**: Moderate. The bootstrapping pipeline is a sensible composition of self-refinement and rejection-sampling-with-an-evaluator ideas, transferred to video judges. The rubric-generation variant is a useful add-on.
- **Importance of research question**: High — scalable supervision for video judges addresses a real bottleneck.
- **Support for claims**: Mixed. The dominance claim is well-supported on bootstrapped benchmarks and partially supported on independent ones; the pairwise feedback claim is contradicted by parts of Table 3; the calibration claim is in tension with §6.2.
- **Soundness of experiments**: Adequate coverage, but the closed-loop construction and the missing rubric ablation reduce the inferential power of the central comparisons.
- **Clarity of writing**: Generally clear; the methodology, training setup, and benchmark construction are easy to follow. Definitions of "feedback" at inference and the in-distribution status of the bootstrapped benchmarks should be made more prominent.
- **Value to research community**: Real — trained checkpoints, bootstrapped corpus, and meta-eval benchmarks are useful artifacts even if some headline numbers should be reframed.

## Calibration

Anchors retrieved:
- `YGWxpOI6Y0.md` — VideoGPT+ — avg 3.40 — Round 1 — less relevant (not a judge paper); weaker than this paper.
- `ujNe7sybJu.md` — Video Summarization — avg 2.50 — Round 1 — much weaker, unrelated.
- `cagNCwQEEN.md` — Hybrid State Space MLLM — avg 3.40 — Round 1 — unrelated.
- `HfJxXbXlYJ.md` — LLM2CLIP — avg 3.00 — Round 1 — unrelated.
- `uHgVrGF2Wn.md` — LVBench — avg 4.50 — Round 1, read in full — benchmark-only paper, narrower in scope; this paper is broader (method + artifacts + benchmarks).
- `m8yby1JfbU.md` — Is Your Video Language Model a Reliable Judge? — avg 6.50 (Accept) — Round 1, read in full — the closest topical match; that paper is largely an analysis of collective-judge approaches without releasing trained judges; this paper releases trained models and a pipeline but suffers from the closed-loop concern.
- `VaUy5GZO3f.md` — Q-Bench-Video — avg 4.80 — Round 1 — narrower scope (quality only).
- `ZJo6Radbqq.md` — VideoNIAH — avg 5.75 (Accept) — Rounds 1+2, read in full — synthetic benchmark for video MLLMs; similar artifact-style contribution; closer in shape to this paper.
- `HnhNRrLPwm.md` — MMIE — avg 8.00 — Round 1 — much broader, more polished benchmark.
- `z8sxoCYgmd.md` — LOKI — avg 8.00 — Round 1 — more comprehensive synthetic-detection benchmark.
- `9Cu8MRmhq2.md` — Multi-granularity Correspondence — avg 8.00 — Round 1 — unrelated.
- `GGlpykXDCa.md` — MMQA — avg 8.00 — Round 1 — unrelated.
- `U1o9KaRgYQ.md` — Data-Juicer Sandbox — avg 5.75 — Round 2 — multimodal data-model co-development; broader scope.
- `ToWKyjwDqO.md` — Direct Judgement Preference Optimization — avg 5.00 (Reject) — Round 2, read in full — text-only judge with three sources of preference data; the rejected reviewers cited weak organization and unclear data-curation novelty. This paper is similar in spirit but more scoped to video with concrete artifacts; closed-loop concerns are this paper's analog of DJPO's data-curation novelty concern.
- `gtkFw6sZGS.md` — Generative Judge for Evaluating Alignment — avg 5.33 (Accept) — Round 2 — text-only generative judge; the scope/contribution is comparable.
- `8m7p4k6Zeb.md` — Synthetic Needle Finetuning — avg 6.00 — Round 2 — narrower contribution, well-supported.
- `hUD9ugK2OH.md` — Synthetic Context Extension — avg 5.75 (Reject) — Round 2 — analysis paper.
- `NO6Tv6QcDs.md` — Limits to scalable evaluation — avg 6.50 (Accept) — Round 2 — theoretical study, more pointed contribution.
- `xpw7V0P136.md` — Teaching LMs to hallucinate less — avg 6.00 — Round 2.
- `le4IoZZHy1.md` — CG-Bench — avg 6.20 (Accept) — Round 2 — benchmark with strong scoping.
- `fCi4o83Mfs.md` — Temporal reasoning MFMs — avg 6.75 (Accept) — Round 2.

Round-1 bracket: (4.5, 7.0), since the paper is clearly stronger than the rejected 3–4 anchors but the closed-loop and ablation concerns put it below the 7+ anchors.

Round-2 narrowing: Among the closest matches, this paper sits between DJPO (5.00 reject, similar artifact contribution but cleaner experimental story) and "Generative Judge" (5.33 accept). VideoNIAH (5.75 accept) has a similar artifact profile but a cleaner methodological story than VideoJudge. "Is Your Video Language Model a Reliable Judge?" (6.50) is more focused/cleaner; this paper has more artifacts but a meaningfully shakier inferential story for its headline claim. Net assessment: this paper is comparable to DJPO/Generative-Judge in score, slightly below VideoNIAH because of the closed-loop framing, well below the 6.5+ tier because the dominance claim does not survive scrutiny on the independent benchmarks and the pairwise feedback table contains a pattern the paper does not address.

Final placement: **5.0** — between the rejected DJPO (5.0) and the accepted Generative-Judge (5.33), reflecting that the artifact contribution is genuine but the central empirical claim is overstated relative to the independent-benchmark evidence and the rubric/feedback claims are not cleanly attributable.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>