Now I have all the information I need. Let me carefully compose the final consolidated review.

---

## Summary

This paper presents OmniSep, a unified sound separation framework that handles queries from multiple modalities (text, image, audio, and composed combinations) in a single model. The key technical contributions are: (1) **Query-Mixup**, a training strategy that blends query features from different modalities to enable joint optimization without modality-specific performance trade-offs; (2) **Negative Query**, a proportional-weighting mechanism to suppress interference by incorporating undesired sound information; and (3) **Query-Aug**, a retrieval-augmented inference method that maps unrestricted natural language descriptions to in-domain class labels for open-vocabulary separation. Experiments on MUSIC, VGGSOUND-CLEAN+, and MUSIC-CLEAN+ show that OmniSep achieves state-of-the-art SDR across text-, image-, and audio-queried sound separation tasks.

## Strengths

- **Query-Mixup enables a single model to handle multiple query modalities without sacrificing per-modality performance.** Table 2 (ID #5 vs. #4) shows that adding Query-Mixup raises average SDR from 6.45 to 6.70, and the text-SDR of the mixed model (6.70) matches the text-only model (ID #1, 6.70), demonstrating that the mixing strategy avoids the performance trade-off typical of alternating modality training.

- **The proportional-weighting negative query (Eq. 4) consistently improves separation and is robust to the choice of weight α**, unlike naive subtraction. Figure 2 (denoted as Figure 3 in the paper's main text) shows that across all three tasks and two datasets, the proposed method (solid line) outperforms naive subtraction (dashed line), with SDR varying by less than 0.45 over a wide α range, while naive subtraction can drop by >3 dB.

- **Query-Aug enables open-vocabulary sound separation that matches or exceeds in-domain class-label performance.** Table 3 reports that OmniSep+Query-Aug achieves a Mean SDR of 6.32 on unrestricted natural language descriptions, which is higher than CLIPSEP-Text's 5.49 on predefined class labels (ID #6) and close to OmniSep's own 6.70 on predefined labels (ID #7).

- **Comprehensive state-of-the-art results across three separate tasks and three datasets.** In Table 1, OmniSep (without negative query) outperforms every prior method in 11 of 12 reported Mean SDR cells, with gains of 0.43–4.36 dB over the previous best (e.g., on MUSIC AQSS: 10.26 vs. 6.43). This validates that the unified framework does not degrade single-modal performance.

- **Ablation study (Table 2) rigorously isolates the effect of multi-modal joint training and Query-Mixup.** The stepwise addition of image data (ID #3), audio data (ID #4), and Query-Mixup (ID #5) shows monotonic improvement in average SDR (5.12 → 6.03 → 6.42 → 6.70), providing clear evidence that each component contributes positively.

## Weaknesses

### Fatal

None. The paper's core contributions (Query-Mixup, negative query, Query-Aug) are all validated through within-framework ablations, and the weaknesses below are addressable without invalidating the central claims.

### Major

- **The negative query evaluation uses perfect knowledge of the interference, limiting evidence for realistic deployment.** The paper states that the negative query "aligns semantically with the interference audio" (Figure 1 caption), and all +NQ experiments use the ground-truth interfering source's query as the negative query (Section 3.2 makes clear that Q_N is extracted from the interference "employing the same method as for other modal queries"). While the proportional-weighting formulation and its robustness to α are convincingly demonstrated, the paper never evaluates how performance degrades when the negative query is imperfect (e.g., a related but wrong label, or a vague description). The Limitations section also does not discuss this operational assumption. A user in practice may not know the exact interfering source. **Why it matters**: Without analysis of imperfect negative queries, the claimed "flexibility" benefit is only validated under ideal conditions, leaving an open question about real-world utility.

- **The SOTA comparison (Table 1) conflates the benefit of the proposed method with the choice of a stronger pre-trained encoder (ImageBind).** OmniSep uses the frozen ImageBind encoder, while nearly all baselines (CLIPSEP, CLIPSEP-Text, AudioSEP) use weaker or different encoders (CLIP, CLAP). The ablation in Table 2 isolates Query-Mixup's contribution as +0.25 dB (within the OmniSep/ImageBind framework), but the SOTA gaps over baselines are often 1–4 dB. The paper does not run a controlled experiment where, e.g., ImageBind is replaced with CLIP/CLAP in the OmniSep pipeline. **Why it matters**: Without such a control, it is impossible to attribute the large SOTA gains to Query-Mixup rather than to the superior representations of ImageBind. The core methodological novelty (Query-Mixup) is reasonably well-validated via the within-framework ablation, but the paper's framing of "state-of-the-art" as evidence for the method's strength is overstated without an encoder-controlled comparison.

### Minor

- **The paper does not explicitly state how the negative query is obtained in the experimental setup.** Section 4.1 describes query extraction for the target source but omits the negative query's selection procedure. While Figure 1's caption and Section 3.2 make the answer clear (it is the interference source's query), the omission in the experimental section is a clarity issue that should be fixed for reproducibility.

- **Some SDR comparisons have overlapping standard deviations (e.g., OmniSep vs. AudioSEP on MUSIC TQSS: 10.65±1.07 vs. 9.82±0.89).** The paper does not report confidence intervals or statistical significance tests. While not uncommon in this field, this weakens the strength of individual SOTA claims.

- **The Limitations section (§8) focuses narrowly on dataset scope and does not discuss the negative query's operational assumption or the encoder confound.** These are the most significant limitations and should be acknowledged.

### Trivial

- None.

## Nice-to-Haves

- An experiment replacing ImageBind with CLIP/CLAP encoders in OmniSep's pipeline (or replacing baselines' encoders with ImageBind) would cleanly isolate whether Query-Mixup's training strategy, rather than encoder quality, is responsible for the large SOTA margins.
- An evaluation of negative query performance with imperfect/mismatched queries (e.g., a similar but wrong class label, or a vague description). This would substantially strengthen the claims about practical flexibility.
- The AQSS comparison relies on a single 2019 baseline (Lee et al.). Adding more recent audio-query baselines would strengthen this task's evaluation.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Query-Aug is not novel (retrieval-augmented inference is common)"** — This criticism frames a practical engineering solution as insufficiently novel. The paper does not claim fundamental novelty for retrieval augmentation; it presents Query-Aug as a specific instantiation to solve the open-vocabulary problem. Calling it "not novel" is a subjective judgment of the contribution's significance, not a concrete weakness. The ablation shows it works (Table 3, #10→#11: +1.37 dB SDR).

2. **"The negative query evaluation is fundamentally flawed / cheating"** — The harsh critic suggests the setup might be "cheating by looking at the test-time label." However, the paper clearly describes that the negative query is extracted from the interfering source (Figure 1 caption, Section 3.2). This is a controlled experimental validation of the mathematical formulation, not a deception. The paper's framing could be clearer about the operational scenario, but the evaluation is not flawed — it is limited in scope (only perfect negative queries tested). The criticism is demoted from "fatal flaw" to a Major weakness above.

3. **"Missing related works"** — As per instructions, this criticism is removed because the reviewer cannot independently verify which related works are missing.

4. **Criticisms about missing appendix content** — The parser strips appendix sections. The paper's original submission includes them.

5. **"Outdated AQSS baseline"** — Moved to Nice-to-Haves; the paper does compare against available baselines and follows CLIPSEP's evaluation protocol.

## Novel Insights

None beyond the paper's own contributions. The reviews largely surface expected limitations of a first unified sound separation system (encoder confound, perfect negative query assumption) rather than novel perspectives that the paper itself does not discuss.

## Suggestions

1. **Add an encoder-controlled ablation**: Replace ImageBind with CLIP/CLAP in OmniSep's pipeline (or the reverse in a baseline) and compare performance. This would cleanly separate the benefit of Query-Mixup from the benefit of a stronger encoder, and either way, it would strengthen the paper.
2. **Evaluate negative query under imperfect conditions**: Test scenarios where the negative query is a semantically similar but incorrect label (e.g., positive="child singing", negative="baby crying" instead of "dog barking"). Report how performance degrades and discuss practical usage guidelines.
3. **Explicitly state the negative query selection procedure** in Section 4.1 to remove ambiguity.
4. **Acknowledge the two major limitations (negative query assumption, encoder confound)** in the Limitations section.
5. **Report confidence intervals or bootstrap significance tests** for the main comparisons to strengthen the statistical claims.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>