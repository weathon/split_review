Now I have enough context for calibration. Let me synthesize the final review.

**Calibration Analysis:**

**Round 1 (Bracketing):**
- Weak anchors (scores 1.67–3.40): AudioMorphix (3.4), Spatial Speaker ID (2.75), HarmonyLM (1.67), SaMoye (3.0) — all much weaker papers with fundamental methodological gaps, unclear contributions, or poor evaluations.
- Middle anchors (scores 4.0–5.25): AVS segmentation papers, soundscape stylization papers — these have moderate contributions but concerns about novelty, baseline fairness, or narrow scope.
- Strong anchors (scores 7.6–8.0): Multi-modal reliability bias (8.0), CyberHost (7.6), Loopy (8.0), MMIE (8.0) — top-tier oral/poster papers with broader impact and more polished presentation.

**Initial bracket: 4.5–7.0** — OmniSep is clearly stronger than the weak-anchor papers and the weaker end of the middle band.

**Round 2 (Narrowing within bracket):**
- AVS segmentation papers (5.0, 5.25): These had concerns about being pipelines of existing methods, unfair comparisons, and limited novelty. OmniSep has stronger contributions: Query-Mixup is a clean training strategy, negative query is well-evaluated, and Query-Aug is clearly defined. The evaluation is thorough against proper baselines.
- OmniBind (6.25): A representation learning paper accepted as poster. Mixed reviews (6,8,6,5). OmniSep is comparable in quality but narrower in scope. OmniSep's experiments are more complete against direct baselines.
- Soundscape stylization (avg ~4.0): Much weaker — concerns about baselines and novelty. OmniSep is clearly stronger.

**Final calibration:** OmniSep sits between the 5.0–5.25 anchor papers and the 6.25 anchor paper. It has clearer contributions than the AVS segmentation papers and better-aligned experiments than the soundscape stylization paper, but narrower scope than OmniBind. Score: **6.0**.

---

## Summary

OmniSep introduces a unified sound separation framework that can handle queries from text, image, audio, and composed multi-modal inputs. The core technical contributions are: (1) Query-Mixup — a training strategy that blends query features from different modalities with random weights to enable joint training, (2) a negative query mechanism to suppress unwanted sounds at inference time, and (3) Query-Aug — a retrieval-augmented approach that maps unrestricted natural language descriptions to the nearest in-domain class label. Experiments on MUSIC, VGG SOUND-CLEAN+, and MUSIC-CLEAN+ show state-of-the-art SDR across text-, image-, and audio-queried sound separation tasks.

## Strengths

1. **First unified omni-modal query framework for sound separation.** The paper is the first to handle text, image, audio, and composed queries in a single model. The Query-Mixup strategy (Eq. 1) is a clean and effective solution to the training objective misalignment problem identified in prior work (CLIPSEP). This is evidenced by Table 2 where joint training with Query-Mixup (row #5, AVG SDR 6.70) outperforms joint training without it (row #4, AVG SDR 6.45) while matching the text-only model's TQSS performance (6.70).

2. **Consistent state-of-the-art results across all query types and datasets.** Table 1 shows OmniSep outperforms prior specialized methods on every task–dataset combination. For example, on VGG SOUND-CLEAN+ the Mean SDR gains are: TQSS 6.70 vs. CLIPSEP-Text 5.49 (+1.21), IQSS 6.69 vs. CLIPSEP 5.46 (+1.23), AQSS 7.12 vs. AQSS (Lee et al.) 5.34 (+1.78). These are substantial margins over strong query-based baselines.

3. **Negative query provides robust and well-characterized improvements.** Figure 2 systematically evaluates the negative query mechanism across two datasets and three query types. The proposed proportional weighting (Eq. 4) consistently outperforms naive subtraction, and the method shows remarkable robustness to the choice of α (SDR range ≤ 0.45 across α values). Table 1 quantifies gains of +0.10 to +1.60 SDR from adding negative queries.

4. **Query-Aug enables handling of unrestricted text descriptions.** Table 3 shows that Query-Aug improves OmniSep's Mean SDR from 4.95 to 6.32 with out-of-domain text descriptions, substantially outperforming CLIPSEP-Text (3.53). The method is clearly described (Eq. 5) and the evaluation uses GPT-rewritten descriptions to create a realistic test of linguistic variation.

5. **Well-designed ablation study.** Table 2 systematically disentangles the contributions of multi-modal training data (text → image → audio) and the Query-Mixup strategy, providing clear evidence for each design choice.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Negative query evaluation uses idealized access to interference labels.** The paper evaluates negative queries using datasets where the identities of all sources in the mixture are known, so the negative query Q_N corresponds to the ground-truth interference label. The paper does not discuss how the negative query would be obtained when the user does not know the exact identity of the unwanted sound, nor does it evaluate a more realistic scenario (e.g., using a classifier estimate or user-provided description). This does not invalidate the method — the scenario where the user knows what to remove is itself useful — but the current framing implies a broader applicability than is demonstrated.

2. **"Open-vocabulary" claim is narrower than standard usage.** Query-Aug (Eq. 5) retrieves the nearest in-domain class label from the training label set and uses that as the query. This handles *phrasing variation* (e.g., "a child singing" → "child_singing") but does **not** enable separation of sounds from categories never seen during training. The paper's use of "open-vocabulary" is defensible — any text input is accepted — but readers familiar with the zero-shot sense of the term will find the scope narrower than implied. The paper could clarify this distinction.

3. **Query-Mixup's improvement over joint training without MixUP is modest.** From Table 2, the addition of Query-Mixup (row #5 vs. row #4) improves AVG SDR by 0.25 (6.45→6.70). While the main value of Query-Mixup is enabling unified training, the paper's framing ("enables OmniSep to optimize multiple modalities concurrently") could benefit from acknowledging that the per-modality gains are incremental and the key contribution is practical unification rather than dramatic improvement.

4. **Non-queried baselines are competitive on some metrics.** On MUSIC, TDANet (non-queried) achieves 10.31 SDR while OmniSep (text) achieves 10.65 — a 0.34 dB gap. While query-based methods offer the fundamental advantage of source-selection flexibility that non-queried methods lack by design, the paper does not discuss this comparison in the main text. A brief contextualization would help.

5. **The demo URL is inconsistent** — the abstract cites `omnisep.github.io` while the conclusion cites `omnisept.github.io` (line 246). This appears to be a typo that should be corrected.

### Trivial
- Table 1: Some baselines are listed with "—" for certain dataset columns (e.g., LabelSep, i-Query on MUSIC-CLEAN+). A brief note explaining why these are absent would improve clarity.

## Nice-to-Haves
- An analysis of when negative query *hurts* performance (e.g., when the interference is semantically similar to the target) would strengthen the characterization of the method's limitations.
- The paper reports only SDR; including SI-SDR would align with recent sound separation conventions.
- A discussion of how α would be selected in practice without a validation set would be helpful for practitioners.

## Removed Points

- **"Table 2 AVG SDR omits AQSS"** — The table header states: "AVG SDR represents the average SDR across different sound separation models queried with text and image." This is explicitly explained. **Removed: paper already addresses this.**
- **"Qualitative results are placeholder images"** — The images are missing due to parser stripping, not paper error. **Removed: parser artifact.**
- **"Code and model are not available"** — The paper states "The code and models will be released" which is standard. **Removed: reproducibility nitpick.**
- **"No SI-SNR or SISDR reported"** — SDR is the standard metric for these benchmarks. **Removed: demands non-standard practice.**
- **"Missing related works about multi-modal methods"** — The paper cites relevant prior work across all three query types and explicitly discusses multi-modal representation learning (Section 2.3). **Removed: per rule against adding missing references.**
- **Strength: "Query-Aug enables open-vocabulary sound separation"** — Kept but noted in weaknesses as narrower than implied. The strength is real (handles unrestricted text), but the weakness about scope is also real.
- **Strength about "important problem" / generic praise** — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on well-understood issues (claim calibration, evaluation scope) without surfacing an unexpected perspective.

## Suggestions

1. Add a paragraph or experiment discussing how the negative query is obtained in practice — e.g., evaluate using a classifier prediction or user-provided description instead of the ground-truth label, or at minimum acknowledge this as a current limitation.
2. Replace or qualify "open-vocabulary" with more precise terminology (e.g., "phrasing-robust" or "unrestricted-text") and clarify that Query-Aug maps out-of-domain descriptions to the nearest seen class rather than enabling zero-shot separation of novel categories.
3. Add a brief discussion comparing OmniSep's query-based setup to non-queried methods, noting that query-based methods enable per-source selection while non-queried methods separate all sources without user control.
4. Fix the demo URL inconsistency (line 16 vs. line 246).

## Score and Decision

**Calibration anchors consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| a8dQutiF9E (AudioMorphix) | 3.40 | 1 | Much weaker: training-free editing with limited evaluation |
| W4yLHZGqdp (Spatial Speaker ID) | 2.75 | 1 | Much weaker: short-utterance speaker ID, limited scope |
| mp8ZgMZ1RG (HarmonyLM) | 1.67 | 1 | Much weaker: broken writing, unclear contributions |
| kbSU5bwoRv (SaMoye) | 3.00 | 1 | Much weaker: SVC with feature disentanglement concerns |
| nuWVS4SBUu (AVS segmentation) | 5.00 | 1,2 | Weaker: novelty concerns, pipeline-of-existing-methods criticism |
| 8VnS320esG (AVS segmentation) | 5.25 | 1,2 | Weaker: similar pipeline concerns, missing comparisons |
| 1HgJZl3HgT (Soundscape stylization) | 4.00 | 2 | Clearly weaker: baseline fairness issues, limited novelty |
| PdDm14eXO4 (AVSET-10M dataset) | 4.75 | 2 | Weaker: dataset paper, narrower contribution |
| WqL4wOU3tw (Sounding video generation) | 4.75 | 2 | Weaker: simple baseline approach |
| l2izo0z7gu (OmniBind) | 6.25 | 2 | Slightly stronger: broader scope, accepted poster, but comparable rigor |
| M8J0b9gNfG (Multilingual VSR) | 6.20 | 2 | Comparable: good experiments but scope differences |
| 3UaOlzDEt2 (CREMA) | 6.80 | 2 | Stronger: accepted poster, broader multimodal reasoning |
| TeVAZXr3yv (MMAU) | 7.50 | 2 | Stronger: accepted spotlight, benchmark contribution |
| TPZRq4FALB (Test-time adaptation) | 8.00 | 1 | Stronger: accepted poster, polished presentation |
| vaEPihQsAA (CyberHost) | 7.60 | 1 | Stronger: oral presentation, broader impact |
| weM4YBicIP (Loopy) | 8.00 | 1 | Stronger: oral, polished audio-driven avatar work |

**Round 1 bracket:** 4.5–7.0  
**Round 2 narrowing:** Compared to the 5.0–5.25 anchors, OmniSep has stronger and clearer contributions. Compared to the 6.2–6.8 anchors, OmniSep is slightly narrower in scope but comparably rigorous. The final score of **6.0** places it above the withdrawn/weak papers and in the range of a solid accept-tier paper for a venue like ICASSP, Interspeech, or a mid-tier CV/ML conference.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>