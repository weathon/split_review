Here is the final consolidated review.

---

## Summary

This paper makes two contributions: (1) **CompA**, two expert-annotated benchmarks (CompA-order with 400 instances and CompA-attribute with 200 instances) that evaluate compositional reasoning in audio-language models (ALMs), and (2) **CompA-CLAP**, a fine-tuning method that combines composition-aware hard negatives with a modular contrastive learning objective to improve compositional reasoning. The paper demonstrates that current ALMs perform near chance on these benchmarks and that CompA-CLAP significantly improves over baselines on CompA-order while largely retaining standard retrieval/classification performance.

## Strengths

- **First systematic study of compositional reasoning in ALMs, backed by expert-annotated benchmarks.** No prior work in the audio space has targeted compositional reasoning. The paper shows concretely that existing ALMs perform near random on these benchmarks (e.g., CLAP-LAION achieves a group score of only 5.50% on CompA-order vs. 16.67% random baseline). The benchmarks fill a genuine gap and are carefully constructed — more than 90% of CompA audios are real-world samples from AudioSet Strong (CompA-order) or synthetically generated with expert validation (CompA-attribute), and human baselines (80–91%) show the tasks are feasible.

- **CompA-CLAP achieves large and convincing improvements on CompA-order while retaining standard-task performance.** On CompA-order, CompA-CLAP obtains a group score of 33.85% compared to 4.70% for CLAP and 5.50% for CLAP-LAION — a >28% absolute gain. At the same time, on text-to-audio retrieval (AudioCaps R@1) CompA-CLAP scores 36.1 vs CLAP (ours) 35.9, and on zero-shot ESC-50 it drops only from 90.2% to 89.1%. This directly supports the claim that compositional understanding can be improved without sacrificing general capabilities.

- **Ablation study confirms both training stages contribute.** The ablation rows in Table "Performance comparison on CompA-order and CompA-attribute" show that removing either the hard-negative stage or the modular contrastive stage causes substantial degradation (e.g., CompA-order group score drops from 33.85 to ~20-21), isolating the gains to the proposed components.

- **Novel training techniques to address data scarcity.** The paper proposes two methods not previously used in audio: (a) LLM-generated composition-aware hard negatives constrained to plausible real-world scenarios, and (b) modular contrastive learning that creates synthetic compositional audios from single-event clips without requiring existing compositional pairs. The modular approach is shown to scale (≈251k training audios from ≈500k snippets).

- **Transparent reporting of limitations.** The paper honestly acknowledges that CompA-CLAP performs worse than random on CompA-attribute audio and group scores ("leaves plenty of room for improvement") and discusses common failure cases (acoustically similar events, unseen prepositions). This candor strengthens the paper's credibility.

## Weaknesses

### Fatal
None.

### Major

- **No explicit decontamination between training and test data from AudioSet Strong.** The CompA-order benchmark (test) is sourced from AudioSet Strong, and both the AudioSet-CompA training dataset (~110k pairs) and the modular template dataset (≈500k snippets → ≈251k training audios) are also sourced from AudioSet Strong. The paper states no decontamination procedure — no assertion that training clips and test clips were drawn from non-overlapping AudioSet Strong sessions, IDs, or temporal regions. Given that AudioSet Strong is a finite collection, overlap is a genuine risk. If the same audio stretch appears in both training and evaluation, the CompA-order results could be inflated by familiar acoustic content rather than compositional understanding. **Why this matters:** this concern affects the central quantitative evidence for the method's effectiveness on the order benchmark. The authors must clarify how overlap was prevented, or the results carry an unresolved confound.

- **Evaluation metric for three-pair instances in CompA-order is undefined.** The paper states that 100 of the 400 CompA-order instances have three audio-caption pairs (C₂, A₂ for simultaneous events), but Equations (1)–(3) define the text, audio, and group scores only for two pairs (C₀,A₀,C₁,A₁). No formula or explanation is given for extending these metrics to three pairs. Were these instances evaluated pairwise among all three possible pairings, as a 3-way accuracy, or discarded? This must be specified, since one quarter of the order test set lacks a documented evaluation procedure.

### Minor

- **CompA-CLAP performs near or below random on audio and group scores for CompA-attribute.** On CompA-attribute, the audio score is 22.52 (random: 25.0) and the group score is 15.13 (random: 16.67). While the paper honestly acknowledges this, the claim that CompA-CLAP demonstrates "superior compositional reasoning capabilities" and improves "by 10%-28%" is heavily driven by the order benchmark. On attribute binding specifically, the improvement over the strongest baseline (CLAP-ours) is small (audio: 22.52 vs 20.50; group: 15.13 vs 14.75), and the model has not learned a usable representation for this task. The framing should more clearly separate the strong results on order from the weak results on attribute binding.

- **Asymmetric inclusion of hard negatives in the contrastive loss (both stages).** In Equations (4)–(5) and (6)–(7), hard-negative captions appear only in the audio-to-text loss's denominator (ℓⁱᵃ²ᵗ), not in the text-to-audio loss's denominator (ℓⁱᵗ²ᵃ). This is a structural consequence of the hard negatives being text-only (they have no audio embeddings), so they cannot be added to the t2a denominator. However, the paper does not discuss this asymmetry or its effect, and it may partly explain why audio scores are systematically lower than text scores across all models (CompA-order: text 40.70 vs audio 35.60). The authors should at minimum note this limitation and discuss its implications.

- **Multiple-granularity positives may dilute the compositional signal in modular contrastive learning.** The modular stage averages all positives (including simpler captions like "dog barking") equally with the exact compositional caption in the numerator of Equations (6)–(7). The model can satisfy the objective via similarity with simpler captions that do not require understanding composition. The paper does not analyze whether this dilutes learning; a weighting scheme or treating simpler variants as lower-weight positives could be explored.

- **Training details for the hard-negative stage are sparse.** The paper states that "only the last few layers are fine-tuned" (line 182) but does not specify which layers, the learning rate, batch size, number of steps, or early stopping criteria. Given that the method operates in a low-resource regime (~100k pairs), these details matter for reproducibility.

### Trivial
- None that are not already encapsulated above.

## Nice-to-Haves
- **Ablation of modular dataset scaling** — an experiment showing how performance varies with modular training set size (e.g., 50k vs 100k vs 250k) would strengthen the scalability claim.
- **Disentangling data vs. objective effects** — an ablation that controls for data by using the same AudioSet-CompA data with the modular contrastive objective (or vice versa) would help attribute gains to the algorithmic choices rather than data composition.
- **A quantitative analysis of the modular template dataset** — statistics on how many unique events, how often each combination appears, and examples of LLM-generated scenes would improve reproducibility.

## Removed Points
- *Criticism that the shuffling experiment uses only one benchmark (unclear which).* The paper explicitly states it runs on both Clotho and AudioCaps (Section 2.1, line 73: "the most commonly used audio-retrieval benchmarks, Clotho and AudioCaps"). This is factually inaccurate and is removed.
- *Framing the below-random CompA-attribute results as a fatal flaw that "undermines the central claim."* The paper candidly acknowledges this limitation (line 279: "all models, including CompA-CLAP, perform worse than our random baseline on CompA-attribute, which leaves plenty of room for improvement") and the central claim — improvement over baselines — is still supported by the data. The criticism overstates the impact. Retained as a Minor weakness about framing above.
- *The asymmetric loss criticism framed as a fundamental error.* The asymmetry is a structural necessity (text-only hard negatives have no audio embeddings to put in the t2a denominator), not an oversight. The underlying observation that it may affect audio scores is valid and retained as Minor.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a genuine but addressable data-contamination concern and a technically interesting asymmetry in the loss formulation that could inform future work on contrastive learning with modality-specific hard negatives.

## Suggestions
1. **Address the decontamination concern explicitly.** Provide a clear statement in the final version that no AudioSet Strong recordings used in training (either in AudioSet-CompA or the modular synthesis pool) appear in the CompA-order test set, and describe the procedure that guarantees separation. If overlap cannot be ruled out, re-report results on a verified disjoint split.
2. **Define the three-pair evaluation metric.** Specify how text, audio, and group scores are computed for the 100 three-pair instances in CompA-order (e.g., evaluated via pairwise comparisons among all three pairs with appropriate aggregation).
3. **Discuss the loss asymmetry and its implications.** Acknowledge that hard negatives are text-only and therefore only influence the a2t direction, and discuss whether this could explain the consistent gap between text and audio scores.
4. **Tone down the framing around CompA-attribute in the abstract/intro** to match the empirical findings — the method is effective on order reasoning but not yet on attribute binding.
5. **Provide the missing training hyperparameters** for the hard-negative fine-tuning stage in the supplement.

## Score and Decision

The benchmark contribution is solid, well-motivated, and fills a genuine gap. The method shows convincingly strong results on order reasoning (CompA-order) with clean ablations, while being transparent about its struggles with attribute binding. The two major concerns — lack of documented test-train decontamination and undefined three-pair metrics — are addressable in revision but need to be resolved before the results can be fully trusted. Given the inherent value of the benchmarks and the soundness of the experimental design modulo these clarifications, the paper merits acceptance contingent on addressing the major weaknesses.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>