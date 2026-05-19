- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5
Now I have all the evidence I need. Let me write the final consolidated review.

## Summary

This paper makes two contributions: (1) **V2M**, a large-scale video-to-music dataset with 360K video-music pairs (~18,000 hours) spanning diverse genres, constructed via a multi-step cleaning pipeline with coarse filtering, music detection, source separation, and audio-visual alignment ranking; and (2) **VidMuse**, a video-to-music generation framework featuring a Long-Short-Term Visual Module (LSTV-Module) that fuses segment-level and video-level visual cues via cross-attention, feeding into an autoregressive music token decoder. Experiments on the V2M benchmark show VidMuse outperforming several baselines across objective metrics (FAD, FD, KL, Density, Coverage, ImageBind Score) and a user study.

---

## Strengths

- **Large-scale, rigorously curated dataset.** V2M contains 360K video-music pairs (~18,000 hours), substantially larger than prior datasets (HIMV-200K, dance-only datasets, MIDI-only datasets). The multi-step pipeline (coarse filtering, fine-grained filtering via music detection and static-image detection, music source separation, audio-visual alignment ranking) is clearly described and well-motivated (Section 3, Fig. 1). Genre diversity analysis and dataset comparisons (Fig. 2a/b) support the claim of being the largest and most diverse dataset for this task.

- **LSTV-Module with demonstrated advantages over unimodal variants.** The ablation study (Section 5.5) explicitly compares VidMuse (full LSTV) against VidMuse-STM (short-term only) and VidMuse-LTM (long-term only), reporting that the full model outperforms both across all metrics. This directly validates the core architectural claim that jointly modeling local and global visual cues yields better audio-visual alignment and diversity.

- **Comprehensive evaluation with convergent evidence.** The paper uses five objective metrics (FAD, FD, KL, Density, Coverage, ImageBind Score) on a held-out benchmark, plus an A/B user study with 40 participants and 600 comparisons across four criteria (audio quality, alignment, musicality, overall). The objective results and human judgments consistently favor VidMuse over all non-ground-truth baselines, providing convergent evidence from complementary evaluation paradigms.

- **Clean, end-to-end design without intermediate representations.** VidMuse directly predicts music tokens from video features via an autoregressive decoder, bypassing symbolic MIDI or text intermediaries. The ablation and main results supporting higher Density and Coverage suggest that this design choice contributes to more diverse and less repetitive music compared to MIDI-based or text-bridge methods.

---

## Weaknesses

### Fatal
None.

### Major

- **MIDI-to-audio conversion for baselines is undocumented.** The main results (Table 1) compare VidMuse against Video2Music and CMT, both of which output symbolic MIDI. Metrics such as FAD, FD, KL, Density, and Coverage are computed on generated *audio*, yet the paper never describes how MIDI outputs were converted to audio waveforms for metric computation. Different MIDI rendering pipelines (e.g., FluidSynth with different soundfonts, neural synthesis, or silence for silent frames) can dramatically affect audio quality metrics. Without this detail, the objective gap between VidMuse and the MIDI-based baselines cannot be properly assessed. The user study partially mitigates this (listeners heard direct audio), but the objective metrics are presented as primary evidence and should be independently interpretable.

- **No confidence intervals or statistical significance for any objective metric.** FAD, a primary metric, is known to require hundreds to thousands of samples for stable estimates, yet the V2M benchmark contains only 300 samples (9 hours). The paper reports point estimates only, with no confidence intervals, standard deviations, bootstrapped estimates, or significance tests. Given the modest benchmark size, the marginal gaps in metrics such as KL and Density may not be reliable. While the user study provides supporting evidence, the objective evaluation as presented is incomplete without uncertainty quantification.

### Minor

- **Ambiguity about whether self-attention parameters are shared between STM and LTM.** The paper states that "self-attention mechanism" is used in both long-term and short-term modeling (lines 165), but does not clarify whether these are separate parameter sets or a shared layer. This affects both reproducibility and understanding of the model's capacity. The figure (Fig. 3, LST-module) likely makes this clear but the text should state it explicitly.

- **M²UGen's input modality in the comparison not clarified.** M²UGen is a multimodal system that processes video, audio, and text. For the video-to-music task, it is important to know whether M²UGen was given the video *with or without* its original audio track as input, since providing the original audio would give it an unfair advantage. This should be stated in the experimental setup.

- **User study protocol is somewhat ambiguous.** The paper states "600 video-music pairs" are sampled from a 300-pair benchmark (line 229). It later clarifies that each method pair was compared 60 times (yielding 600 total comparisons across C(5,2)=10 method pairs). However, the phrase "video-music pairs" conflates unique videos with comparison instances. A clearer description of how the 300 benchmark samples were used across the 600 comparisons would aid reproducibility.

- **No discussion of selection bias in the finetuning data selection.** The Audio-Visual Alignment Ranking step uses ImageBind scores to select the top-ranked videos for the finetuning set (V2M-20K). This could bias the finetuning set toward videos where the pre-existing soundtrack already aligns well with visuals, potentially inflating downstream alignment metrics. While this is a reasonable design choice (better-aligned training data improves learned alignment), it should be acknowledged as a potential limitation.

- **No discussion of data copyright, licensing, or ethical considerations.** The dataset is scraped from YouTube with automated queries. For a large-scale dataset contribution, the paper should at minimum mention the licensing status of the collected data and any steps taken to respect content ownership. The limitations section focuses only on technical model-level limitations (codec quality, compute cost) and omits dataset-level considerations.

- **No stated plans for code or dataset release.** The paper does not mention whether the V2M dataset or VidMuse code will be released, which limits the community impact—especially for a paper whose primary contributions include a large dataset.

### Trivial
None.

---

## Nice-to-Haves

- A companion website with audio examples would substantially strengthen the qualitative analysis, since music quality cannot be conveyed in a static paper.
- Reporting confidence intervals (e.g., via bootstrapping over the 300 benchmark samples) would address the main methodological concern cleanly.
- Clarifying whether the 300-sample benchmark is sufficient for stable FAD estimates (e.g., by citing established FAD evaluation guidelines or providing a bootstrap analysis) would preempt concerns about reliability.
- A brief discussion of geographical/genre biases in the YouTube-sourced data would strengthen the dataset contribution.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing ablation table numbers" (Harsh Critic, Point 3).** The ablation tables are included via `\input{}` directives that the text parser could not resolve. These tables exist in the original submission. The criticism stems from a parser artifact, not an author omission.

- **"VM-NET inclusion in generative evaluation is questionable" (Harsh Critic, Section-by-Section).** Per the hard rules: if an asymmetry in comparison favors the *baseline* (not the author's method), the criticism should be removed. VM-NET retrieves existing music from a database, which is an easier task than generating from scratch (the retrieved music is real, not synthesized), so the asymmetry favors the baseline. The paper acknowledges the distinction, and including a strong retrieval baseline as a reference point is standard practice.

- **"ImageBind score limitations for music" raised as a weakness.** The paper already explicitly acknowledges this limitation (line 215: "We acknowledge that ImageBind has limitations as it is not specifically trained on music data, but it currently seems to be a possible option for evaluating the semantic alignment"). The paper addresses this concern, albeit imperfectly.

- **Minor formatting/style nitpicks, grammar issues, or abstract-to-introduction repetition.** These are parser-level artifacts, not author errors.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's strengths (dataset scale and curation rigor, clean LSTV architecture, comprehensive evaluation) and identify the same core methodological gap (undocumented MIDI-to-audio conversion, missing confidence intervals). No unexpected patterns or contradictions emerge from the reviews that would suggest an alternate interpretation of the paper.

---

## Suggestions

1. **Describe the MIDI-to-audio conversion pipeline** used for Video2Music and CMT. Specify the synthesizer, soundfont, sample rate, and any post-processing. If no conversion was needed (e.g., the original implementations already output audio), state that explicitly with a reference.

2. **Report confidence intervals** (e.g., bootstrapped 95% CIs) for all objective metrics, or provide a justification (with citations) for why point estimates are sufficient for the 300-sample benchmark.

3. **Clarify the self-attention parameter sharing** between STM and LTM (shared vs. separate weights) in the method description.

4. **State whether M²UGen received video with or without original audio** during evaluation.

5. **Clarify the user study protocol:** how exactly were 600 comparison instances derived from 300 benchmark samples? Clarify the wording to distinguish unique videos from comparison trials.

6. **Add a brief discussion** of data licensing, copyright status of YouTube-sourced content, and release plans for code/dataset.

7. **Acknowledge the ImageBind-based selection bias** for the finetuning set in the limitations section.

---
