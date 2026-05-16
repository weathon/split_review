Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

This paper proposes a two-stage Variational Information Bottleneck (VIB) framework for disentangling neural speech model representations into textual and acoustic components. Stage 1 compresses representations to retain only transcription-relevant information; Stage 2, conditioned on the frozen Stage 1 latents, captures complementary acoustic features for a target task (emotion recognition or speaker identification). The authors validate disentanglement via probing experiments showing near-random cross-modal performance, analyze layerwise contributions revealing how fine-tuning shifts acoustic-to-textual encoding, and present a preliminary feature attribution method. The framework is principled, the corroborating evidence is strong where it counts, and the central claim is believable.

## Strengths

- **Principled two-stage VIB disentanglement framework.** The information-theoretic design is clean: Stage 1 uses CTC + information loss to isolate textual content; Stage 2 conditions on frozen textual latents with a second information bottleneck to capture complementary acoustic features. The ablation without information loss (footnote in Section 2.2) confirms the information loss term is essential — without it, disentanglement fails. This is a genuine methodological contribution over prior work relying on autoencoders or adversarial training (Section 2.2–2.3).

- **Strong probing-based validation of disentanglement.** Figure 2 (Section 5) shows a clear pairwise failure pattern: textual latents achieve random-level performance on acoustic features (pitch, intensity, gender, speaker ID) while matching or exceeding hidden-state performance on transcription; acoustic latents perform at random on transcription while substantially outperforming baselines on acoustic features. This is direct, quantitative evidence supporting the core claim.

- **Novel layerwise analysis revealing fine-tuning dynamics.** By applying disentangled representations per layer (Section 6, Figure 4), the paper shows that fine-tuned Wav2Vec2 loses acoustic information in its final layers in favor of textual encoding, whereas HuBERT retains stronger acoustic contributions in middle layers. This finding — obtainable only through the proposed disentanglement — is a genuine empirical insight about how fine-tuning reshapes neural speech model representations.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Missing ablation: performance of the acoustic latent alone on target tasks.** Table 1 and the main results only report the combined performance (Z_textual + Z_acoustic concatenated). Showing Z_acoustic alone on emotion recognition and speaker identification would directly confirm that the acoustic latent carries non-redundant, task-relevant information beyond what the textual latent already provides. The probing in Figure 2 already shows Z_acoustic captures acoustic features (pitch, intensity, etc.), which is evidence of disentanglement, but the utility of Z_acoustic *for the target task* remains inferred rather than measured. This is a completeness gap, not a fatal one — the core claim about disentanglement is separately validated.

- **No quantitative comparison with prior disentanglement methods.** The related work cites AutoVC, SpeechSplit, NANSY, Prosody2Vec, and others, but the paper provides no empirical comparison against any of them on the same tasks or metrics (e.g., DCI, MIG, or task accuracy). While the VIB-based approach is methodologically distinct (post-hoc on frozen representations), a comparison would substantially strengthen the contribution. The absence does not invalidate the results, but it limits the paper's ability to demonstrate relative advantage.

- **HuBERT-FT Large WER gap under-discussed.** In Table 1, probing on HuBERT-FT Large gives WER=6.9 while VIB gives WER=25.6 — a large gap. The paper (line 164) states "VIB demonstrates a similar or sometimes even lower word error rate (WER) compared to probing classifiers," which is misleading for this case. The paper should explicitly discuss why compression hurts fine-tuned HuBERT so much more than other models and whether this affects the trustworthiness of textual latents from such models.

- **No error bars on layerwise probing results (Section 6, Figure 4).** While Table 1 reports averages over 3 seeds, the layerwise probing plots (left and middle panels of Figure 4, plus the right panel showing textual vs. acoustic contributions) do not report variance. Given that per-layer data is more limited, confidence intervals would help assess whether the observed trends are stable.

### Trivial

- **Bottleneck dimension analysis not shown.** The paper mentions experimenting with d={16,32,64,128,256} (line 107) but only reports d=128. Showing how disentanglement quality scales with dimension would strengthen characterization of the method.

- **Claim about "independent of the target task" is overstated.** Line 32 says textual latents "can be easily applied to new downstream tasks." In practice, only the same stage 1 encoder is demonstrated. This is a minor overclaim easily corrected.

- **Probing resolution for acoustic features is coarse.** The discretization into 4 quartiles (Section 5) gives a 25% random baseline; probing scores around 40–60% are above chance but well below ceiling. The paper could note this limitation.

## Nice-to-Haves

- A stage 2 ablation without the information loss (mirroring the stage 1 ablation already in a footnote) would strengthen the claim that the conditional VIB setup is necessary for acoustic disentanglement.
- Using a completely held-out transcription dataset (e.g., LibriSpeech test-clean) for probing textual latents, rather than a held-out split of Common Voice which partially overlaps with the stage 1 training domain.
- Reporting the effect of bottleneck dimension on both task performance and probing-based disentanglement metrics.

## Removed Points

- **Criticism about Feature Attribution lacking rigor (Critical Issue 3):** The paper explicitly states (Section 7) "While a comprehensive evaluation of disentangled attribution is beyond the scope of this work, we do conduct a preliminary investigation." The critic's concerns about no statistical tests, no baseline comparisons, and no validation are accurate *if* the section claimed to be a rigorous evaluation — but the paper openly frames it as preliminary/exploratory. This is a limitation the authors already acknowledge. Downgraded from a weakness to a context note: the attribution section is clearly preliminary and should be read as such.

- **Criticism that "probing results for acoustic features using 4 buckets is coarse":** This is a reasonable methodological note but not a weakness — 4-way classification with a 25% random baseline is standard practice, and the probing results still convincingly show above-chance performance for acoustic latents and random-level for textual latents. The coarseness affects both equally.

- **Criticism about Common Voice overlap inflating textual latent probing quality:** The paper uses a held-out test split of Common Voice, and the probing results for transcription are not the paper's main claim (disentanglement is). The textual latents' strong transcription performance is a sanity check, not the central result. Even if inflated, the cross-modal random performance (textual→acoustic, acoustic→text) is unaffected.

## Novel Insights

The reviews collectively highlight an important nuance that goes beyond what the paper explicitly discusses: the VIB framework does not just *separate* features — it also *reveals the information-processing strategy of the underlying speech model*. The layerwise analysis showing that fine-tuned models shift acoustic→textual encoding in later layers is only interpretable as a finding *because* the disentanglement framework exists. This suggests that the paper's method may be as valuable as an *analysis tool* for understanding pretrained speech representations as it is as a disentanglement method per se. The reviews also surface the tension that the strongest evidence (probing-based pairwise failure) and the weakest section (attribution) are evaluating different claims — the paper is strongest as a disentanglement method paper, weakest as an attribution method paper, and the attribution section should be de-emphasized.

## Suggestions

1. **Add the Z_acoustic alone experiment.** Train a classifier on acoustic latents (without textual latents) for emotion recognition and speaker identification and report the accuracy. This directly confirms the acoustic latents carry task-relevant non-textual signal and only takes one additional row in Table 1.
2. **Add a brief discussion of the HuBERT-FT Large WER gap** (25.6 vs. 6.9) explaining why compression is more detrimental for fine-tuned models and whether this affects any downstream conclusions.
3. **Add error bars (e.g., over 3 seeds) to the layerwise probing plots** to establish stability of the observed trends.
4. **Either add a quantitative comparison with one prior method on a shared task** (even a single row in a table), or add a clear statement explaining why such comparison is not feasible (different setups, different assumptions) so readers are not left wondering.
5. **Clarify that the feature attribution results are exploratory** by adding a limitations paragraph in Section 7 that acknowledges the absence of statistical testing, the lack of validated attribution metrics, and the preliminary nature of the comparison with Integrated Gradients.

## Score and Decision

The paper makes a sound, well-motivated contribution. The core claims — that VIB can disentangle textual and acoustic features, validated by cross-modal probing — are well supported. The identified weaknesses (missing Z_acoustic-alone ablation, no comparison with prior methods, under-discussed WER gap, missing error bars) are real but addressable and do not threaten the central findings. The paper should be accepted after minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>