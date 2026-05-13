## Summary
The paper introduces Aria-MIDI, a piano MIDI dataset of ~1.19M files (~100K hours; 800K after compositional deduplication) built via a three-stage pipeline: (1) Llama-3.1-guided crawling of YouTube via the related-videos API, (2) a distilled CNN solo-piano audio classifier trained on pseudo-labels generated from the MVSep source-separation model, and (3) transcription with the Aria-AMT model. The paper's methodological contribution is the pseudo-label-via-source-separation distillation, which yields a classifier that filters non-piano content roughly 8× more aggressively than an ablation while retaining most high-quality piano material.

## Strengths
- **Pseudo-labeling via source separation is a genuinely useful idea**: distilling MVSep (estimated 5,000 A100h on the corpus) into a CNN classifier (20 A100h) preserves piano/non-piano discrimination — 98.83% non-piano removal vs. 91.10% for the AudioSet-negatives ablation (Table 4), and 100% non-piano per-file rejection at T≥0.7 while retaining 95.28% of pristine piano (Table 5).
- **Two-stage filter is well motivated and quantified**: the paper explicitly shows LM-only scoring is insufficient (Table 3 F1 ≈82% at threshold 4) and demonstrates that an additional audio stage is needed (Section 3, Table 5).
- **Scale is real and the largest of its kind**: ~100K hours of piano MIDI, ~order of magnitude beyond Lakh in hours and ~two orders beyond GiantMIDI (Table 1).
- **Per-file classifier scores and metadata are released alongside MIDI**, enabling downstream researchers to pick threshold-based subsets (Table 5 trade-off curve).
- **Methodology is evaluated against human-labeled ground truth** at every pipeline stage (250 crawl items, 250 audio segments, 200 metadata items), with ablations and external baselines (MVSep direct).

## Weaknesses

### Fatal
None.

### Major
- **No direct transcription-quality audit on Aria-MIDI itself.** Section 1 names "Transcription Quality" as the first persistent AMT-dataset challenge, and Contribution 3 claims the dataset is "one of the cleanest to date." Section 3 evaluates the upstream classifier/segmenter, but note-level transcription accuracy on the actual crawled (out-of-distribution-from-MAESTRO) corpus is inherited from Aria-AMT and deferred to Appendix A.3. Without a held-out audio→MIDI evaluation on a representative slice of the actual crawl, the "cleanest" claim is supported only by audio-side filtering, not by MIDI output quality — which is the dataset's actual artifact.
- **No downstream-utility experiment.** The paper repeatedly frames Aria-MIDI in the lineage of ImageNet/C4 but offers no evidence that training a symbolic-music model on Aria-MIDI improves over Lakh/GiantMIDI on any downstream task (generation perplexity, MIR probe, retrieval). For a dataset paper this is a real gap — scale and cleanliness should translate into measurable model improvements.

### Minor
- **"8-fold improvement" framing is established against the authors' own ablation, not actual prior classifiers.** Section 3 / Table 4 explicitly says the ablation is meant "to mimic classifiers used for segmentation in other work," but it reuses the authors' architecture, pipeline, and data and merely drops pseudo-labels. The 8× number rigorously measures the value of pseudo-labels in their own setup; framing it as "improvement … when compared to previous work" (Contribution 2) overstates what was measured.
- **Cross-dataset comparison (Figure 2) uses the proposed classifier as the filter for what to inspect.** Files in GiantMIDI/ATEPP/PiJAMA are flagged as suspect when their score falls below 0.7 — the same classifier that was trained partly on GiantMIDI audio with MVSep pseudo-labels. This biases which subset gets human-categorized; the directional conclusion (GiantMIDI has many non-piano files) may be correct, but the procedure does not cleanly establish it independent of the authors' tooling.
- **Compositional deduplication is limited by metadata sparsity.** Opus and piece-number tags are present on only 32% and 22% of files respectively (Table 6). The 1.19M→800K dedup therefore operates on a small fraction of cleanly-tagged works, and the footnote that "moonlight" appears 6,819 times suggests substantial residual compositional duplication outside the classical tail. The dedup is reasonable best-effort but should be acknowledged as such — and a MIDI-content-based duplicate estimate would bound what remains.
- **Evaluation set is thin and no inter-annotator agreement reported.** All three core evaluations rest on 200–250 manually labeled examples from two annotators. For a dataset paper of this scale, even one IAA number on the audio-segmentation set would be appropriate.
- **Hyperparameter selection on the same set used for reporting.** The pseudo-label thresholds (per-source $dB_{\min}$, $l_{\min}$), and the inference knobs $d=3, \lambda=0.5, T=0.7$, are tuned on the same 250-recording set whose results are reported in Tables 4–5. The risk of overfitting the evaluation is real and a clean dev/test split is not described.
- **Cost/accuracy trade-off for 70B vs. 405B is asserted, not computed.** Table 3 shows 405B@T≥4 attains the best F1 (86.84) over 70B's 81.93; the paper picks 70B on cost grounds but does not quantify the actual cost difference or the marginal number of videos that would change classification.

### Trivial
- The 50 seed videos and YouTube's recommendation-driven snowballing are inherently non-reproducible; a brief discussion of how others should extend/replicate would help.
- No licensing/ethics statement covering YouTube-sourced piano performances or transcribed MIDI derived from copyrighted recordings. A takedown protocol is standard for releases of this provenance.

## Nice-to-Haves
- A score-vs-quality calibration curve (continuous, not just discrete thresholds in Table 5) so users can pick informed cutoffs.
- A hand-audit of pseudo-label noise on a few hundred labels, since pseudo-labels are the foundation of the classifier.
- A MIDI-space (fingerprint/n-gram) nearest-neighbor pass to estimate residual compositional duplicates after the metadata-based dedup.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Harsh critic's reproducibility framing around YouTube non-determinism**: this is structural to crawl-based datasets and not a flaw of this paper specifically; kept only as a trivial note.
- **Strength Finder's "metadata extraction accuracy" as a core strength**: kept implicitly via Table 6 but de-emphasized — accuracy figures are conditional on presence, which is low for opus/piece-number; presenting it as an unqualified strength is misleading.
- **OCR-rendered nonsense in Figure 4 ("Crown", "Bee", month names)**: parser artifact, not a paper flaw — removed per hard rule on formatting/garbled-text.
- **Strength Finder's generic "comprehensive methodological evaluation"**: retained in a narrower form (human-labeled ground truth at every stage); generic framing dropped.

## Novel Insights
None beyond the paper's own contributions. The distillation-of-source-separation-into-a-classifier idea is the main novel observation; the merged review largely converges on its value plus the gap between upstream classifier quality and downstream MIDI quality.

## Suggestions
- Add a small-scale transcription audit (50–100 clips spanning the score range, manual reference or Disklavier overlap) reporting onset / onset+offset / velocity F1 on Aria-MIDI itself.
- Run a matched-compute downstream training comparison (Aria-MIDI vs. GiantMIDI vs. Lakh) on at least one symbolic-music task and report perplexity plus one MIR probe.
- Reapply (or approximate) the actual GiantMIDI/PiJAMA classifiers on the same 250-segment evaluation set to substantiate the "8×" framing against prior work.
- Add IAA on the human-labeled segmentation set; describe train/dev/test separation for hyperparameter tuning.
- Add an ethics/licensing/takedown statement.
- A MIDI-fingerprint duplicate estimate to bound residual compositional duplication after metadata dedup.

## Evaluation Axes
- **Originality**: Moderate-to-high. The source-separation-as-pseudo-label distillation is a clean, novel pipeline trick.
- **Importance**: High. Symbolic music modeling is genuinely bottlenecked by data; an order-of-magnitude jump is impactful.
- **Claims supported**: Mostly — but "cleanest to date" and "8-fold improvement vs. previous work" both have softer empirical backing than the wording suggests.
- **Soundness**: Solid pipeline analysis with human labels and ablations; weakest on hyperparameter discipline and the absence of an end-to-end MIDI quality audit.
- **Clarity**: Clear, well-structured.
- **Value to community**: High — large clean MIDI corpus + open classifier + metadata.

## Calibration

Anchors retrieved:
- **High band**:
  - `dRXxFEY8ZE` (BirdSet, 7.5): large curated audio corpus with strong benchmarking infrastructure — Aria-MIDI is comparable in scale/curation rigor but lacks the benchmarking layer.
  - `TeVAZXr3yv` (MMAU, 7.5): carefully curated audio benchmark with human annotations across speech/sound/music — more eval-heavy than Aria-MIDI.
  - `qPx3i9sMxv` (BEWO-1M, 7.5): simulation+GPT-assisted spatial-audio dataset — similar pipeline-construction story.
  - `G5DziesYxL` (Data Provenance, 6.5): audit paper, only loosely topical.
- **Medium band**:
  - `PY7KSh29Z8` (SONICS, 5.0 Accept): synthetic music detection dataset — closest borderline-accept anchor.
  - `FDhAngvHuf` (5.5 Reject): web-filter bias study, methodology-heavy.
  - `RvfPnOkPV4` (4.75 Accept): web-data analysis platform.
  - `rMR2P8e0Zx` (SongComposer, 4.6 Reject): symbolic music dataset rejected for weaker construction.
  - `Tgsc0KEkN6` (ViML, 4.5 Reject): large multimodal dataset that didn't make it.
- **Low band**:
  - `HUjFpOgVCK` (ACAV-1M, 4.0): rejected for undisclosed sources, licensing ambiguity, weak filtering eval — Aria-MIDI is notably stronger here (sources fully disclosed, classifier evaluated against humans, ablations present), though it shares ACAV-1M's licensing-statement omission.
  - `burz7mU0YD` (OpenMU, 3.5): rejected for low novelty.
  - `FOcleL0ltt` (UniComposer, 3.0): rejected for unclear contribution.

Aria-MIDI sits clearly above the low band (ACAV-1M-style problems are largely absent — sources and pipeline are well documented), and above borderline medium anchors like SongComposer/ViML in pipeline rigor and human-labeled validation. It does not quite reach BirdSet/MMAU because it lacks a benchmarking/downstream-utility layer and defers the MIDI-side quality measurement to a cited paper. That places it in the upper-medium range — comparable to a strong-borderline accept like SONICS, leaning higher because of the scale and the genuinely novel pseudo-labeling trick.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>