Now I have a thorough understanding of the paper and all the review inputs. Let me synthesize the final review.

---

## Summary

This paper proposes the first sentence-level multilingual visual speech recognition (VSR) system using a single model. The key ideas are: (1) discretizing visual speech features into "visual speech units" (tokens) via a novel multilingual AV-HuBERT (mAV-HuBERT) trained on 5,512 hours of audio-visual data across 9 languages; (2) pre-training an encoder-decoder on these discrete units with a curriculum that transitions from audio-visual to purely visual inputs via progressive masking; and (3) finetuning on continuous features. The approach reduces input data size to 0.016% of raw video and achieves competitive results across 5 languages with a single model, outperforming prior monolingual models on 3 of 5 languages.

## Strengths

- **First sentence-level multilingual VSR with a single model (genuine novelty).** The paper demonstrates that one model can handle 5 languages (En, Es, It, Fr, Pt). Table 7 shows it outperforms the best prior language-specific models on 3 languages (Es: 38.9% vs 40.6% WER; It: 40.9% vs 46.7%; Fr: 42.3% vs 44.8%) and achieves second-best on the remaining 2, all with a single architecture. This is a clear step forward for a field that has been almost entirely monolingual.

- **mAV-HuBERT multilingual pre-training is validated and effective.** Table 2 shows that training the self-supervised model on multilingual data (9 languages, 5,512 hours) yields >10% absolute WER improvement on non-English languages compared to English-only AV-HuBERT, while maintaining competitive English performance. This directly supports the claim that multilingual visual speech pre-training captures cross-lingual viseme information.

- **Curriculum learning with progressive audio masking is essential to the method.** The ablation in Table 5 shows removing curriculum (−Curriculum) degrades performance dramatically (e.g., En WER rises from 31.7% to 39.2%, Es from 38.9% to 48.1%), even underperforming the no-pretraining baseline. This convincingly demonstrates that the audio-to-visual transition is critical for learning from discrete visual units.

- **Visual speech units demonstrably compress data while retaining linguistic content.** The paper quantifies the compression (61,952 bits/frame → 10-bit token, 0.016% of original size) and validates through speaker verification (EER increases from 2.38% on raw audio to 32.74% on visual units in Table 4) and viseme analysis (Figure 2) that discretization suppresses non-linguistic information while preserving phonemic/visemic content.

- **Practical resourcefulness in overcoming data scarcity.** The paper leverages automatic text labels (Ma et al., 2023; Yeo et al., 2023c) to construct 4,545 hours of multilingual video-text data without manual annotation, and uses a shared SentencePiece vocabulary across all 5 languages.

## Weaknesses

### Major

- **The efficiency claims in the abstract and introduction are misleading.** The abstract states "boost the training more than 10 times faster than the standard VSR training" and the introduction repeats this. However, Section 4.3.2 reveals this compares *pre-training only* (6.6 hours for 11 epochs) against standard full training (52.5 hours for 8 epochs). The finetuning stage, which is required to reach usable performance and re-attaches the mAV-HuBERT visual front-end, takes 34.9 hours for 5 epochs. The total pipeline is 6.6 + 34.9 = **41.5 hours** vs 52.5 hours — a **1.26× speedup**, not ~10×. The contributions list (item 4) correctly says "pre-training time," but the abstract and intro use unqualified "training," which readers will naturally interpret as the overall pipeline benefit. The paper should present total end-to-end training time transparently and clearly separate the legitimate pre-training-only speedup from the overall wall-clock advantage.

### Minor

- **The framing of "comparable performances" on English and Portuguese is somewhat optimistic.** Table 7 shows the proposed model's English WER is 24.4% vs the prior best (Ma et al., 2023) at 20.5% — a 3.9% absolute gap. Portuguese is 12.8% vs 11.6%. The paper attributes these to the "curse of multilinguality" but does not investigate whether the gap on high-resource languages is inherent or addressable (e.g., via language-specific embeddings, oversampling, or different tokenization). The claim "new state-of-the-art multilingual VSR performances" is accurate for multilingual VSR (where there is no prior work), but the comparison to monolingual models would benefit from a more explicit discussion of the trade-off between coverage/convenience and per-language accuracy.

- **The curriculum learning schedule is a free parameter with no sensitivity analysis.** The masking ratio is linearly increased from 0 to 100 between 10% and 70% of training (a single configuration). The ablation shows the curriculum is important, but there is no investigation of alternative schedules (faster/slower transition, different starting ratios). Given that curriculum learning is listed among the contributions, showing robustness to the schedule or at least stating the design rationale would strengthen the paper.

- **No explicit confirmation that mTEDx test splits match those of prior work.** The paper states it follows Ma et al. (2022a); Kim et al. (2023c); Yeo et al. (2023c) for mTEDx evaluation, but does not explicitly confirm the test sets are identical. Since the comparisons in Table 7 depend on this, a brief verification statement is needed.

- **The speaker recognition analysis lacks details on the evaluation setup.** The paper does not report how many speakers from VoxCeleb2 were used, whether the training/evaluation sets were balanced, or the speaker count. While the EER trend is clear and the conclusion (units suppress speaker info) is well-supported, these details would improve reproducibility.

### Trivial

- **The paper could explicitly state why 4 of the 9 mAV-HuBERT languages (De, Ru, Ar, El) were not used for VSR training** — this is inferable (no text annotations available), but stating it directly would remove ambiguity.
- **Automatic label quality** from Ma et al. (2023) and Yeo et al. (2023c) could be briefly mentioned (e.g., estimated WER of the labels), though the cited papers cover this.

## Nice-to-Haves

- A Pareto-style or average-WER comparison across all 5 languages in Table 7 would make the multilingual vs. monolingual trade-off more interpretable.
- Testing 1–2 alternative curriculum schedules (e.g., faster transition, slower transition) to show robustness.
- A simple analysis of whether English representations degrade during multilingual training (e.g., language-wise loss trajectories) would add depth to the "curse of multilinguality" discussion.

## Removed Points

- **"First work" claim is unsupported** — Removed. The related work section (Section 2) surveys the field and the claim is qualified with "to the best of our knowledge." This is adequately contextualized for a conference paper.
- **AV-HuBERT vs mAV-HuBERT comparison confounded by data scale** — Removed. This is the intended experimental design: the experiment tests whether multilingual pre-training data helps, and the same architecture is used for both. The comparison is valid for the claim being made.
- **Criticism that the paper should cover additional tasks/languages beyond its stated scope** — Removed. The paper targets 5 languages for VSR with text annotations available. Demanding more languages or tasks is scope creep.
- **Formatting/style nitpicks** — Removed per hard rules (parser artifacts).
- **Reproducibility nitpicks about undisclosed hyperparameters** — Removed. The paper provides architecture details, training configurations, learning rate schedule, and states supplementary materials exist for further details.

## Novel Insights

The key tension revealed by cross-examining the reviews is that this paper's technical contribution is genuinely novel and well-engineered (first multilingual VSR model, clever use of discretization + curriculum learning, thorough ablations), but its presentation of results — particularly the efficiency claims — undercuts its credibility unnecessarily. The 1.26× total pipeline speedup is still positive and the pre-training-only speedup (~8–12×) is real and useful, but the abstract's unqualified "10× faster" claim creates an expectation the paper cannot deliver. Similarly, the "comparable" framing for English glosses over a 3.9% WER gap that merits more discussion. The paper would be stronger if it owned these trade-offs directly rather than hedging around them — the community will value the contribution more if it is presented honestly.

## Suggestions

1. **Fix the efficiency framing.** In the abstract and introduction, either qualify the speedup claim as "pre-training" (matching the contributions list) or give the total pipeline numbers. Section 4.3.2 already presents both numbers — the abstract just needs to align with them.
2. **Add a sentence explicitly confirming mTEDx test split identity** with prior work.
3. **Briefly note the curriculum schedule design rationale** (or acknowledge it as an empirical choice) and consider showing 1–2 alternative schedules in the supplement.
4. **Reframe the multilingual vs. monolingual comparison more neutrally.** The paper already does this partially ("curse of multilinguality"), but an explicit statement like "the single model trades ~4% WER on English and ~1.2% on Portuguese for coverage across all 5 languages" would be more transparent than "comparable performances."
5. **Include speaker count and balance information** for the speaker recognition analysis.

## Score and Decision

**Originality:** High — first sentence-level multilingual VSR with a single model; visual speech units are a novel application of discretization to VSR.

**Importance of research question:** High — multilingual capability is essential for VSR to be practically useful.

**Claims well supported:** Mostly yes, except the overclaimed efficiency in the abstract.

**Soundness of experiments:** Good — thorough ablations (Table 5), comparisons against both multilingual baseline (Table 6) and monolingual SOTA (Table 7), and analyses (Tables 2, 4). Missing sensitivity analysis on curriculum schedule and explicit test split verification.

**Clarity of writing:** Generally clear, though the efficiency framing is misleading in the abstract/intro.

**Value to the community:** High — the method, trained models, and code (promised for release) will be useful resources.

The paper has a genuinely novel contribution with solid experiments. The main weakness is presentation — the efficiency overclaim in the abstract is real but fixable, and no core claim is invalidated. The work does not have fatal flaws, and the method is sound. I recommend acceptance after a minor revision that corrects the efficiency framing in the abstract/intro and addresses the minor verification points.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>