Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated review.

## Summary

This paper proposes a two-stage Variational Information Bottleneck (VIB) framework for disentangling textual and acoustic features from neural speech representations (Wav2Vec2, HuBERT). In Stage 1, speech frame representations are compressed via VIB to decode transcriptions (textual latent). In Stage 2, a second VIB encoder is trained on the same speech representations, conditioned on the frozen textual latents, to decode a downstream task (emotion recognition or speaker ID), producing acoustic latents. The paper evaluates disentanglement via probing, provides a layerwise analysis of contributions, and introduces a preliminary attribution method based on attention weights. The probing results (Figure 3) show near-perfect separation: textual latents predict transcriptions well but perform at chance on acoustic features, and vice versa for acoustic latents.

## Strengths

1. **Strong probing evidence for disentanglement.** The sanity-check probing (Figure 3) is the paper's strongest piece of evidence. Across multiple Large model variants (HuBERT, Wav2Vec2, pre-trained and fine-tuned), textual latents achieve near-random performance on all acoustic features (pitch, intensity, gender, speaker ID) while remaining competitive on transcription, and acoustic latents show the complementary pattern. This goes beyond qualitative demonstration to quantitative validation of the core claim.

2. **Competitive task performance after aggressive compression.** Table 1 shows that VIB-compressed representations (d=128) match or exceed probing classifiers on emotion recognition and speaker identification across most model variants. For example, HuBERT-Large emotion accuracy improves from 57.3% (probing) to 66.1% (VIB). This demonstrates that the information bottleneck does not sacrifice task-relevant information during compression — a non-trivial result.

3. **t-SNE visualization provides intuitive confirmation.** Figure 4 shows that textual latents cluster perfectly by transcription label while acoustic latents cluster by emotion label, with no cross-clustering. This model-free visualization corroborates the probing results from a different angle.

4. **Layerwise analysis yields interpretable insights.** Figure 5 reveals that fine-tuned Wav2Vec2 loses acoustic information for emotion recognition in later layers while gaining textual contribution — a finding consistent with ASR fine-tuning effects that would be difficult to obtain without a disentanglement framework. This demonstrates the framework's utility as an analysis tool beyond the core disentanglement claim.

5. **Broad evaluation across model families and scales.** The paper tests two model families (Wav2Vec2, HuBERT) at both Base and Large scales, including pre-trained and fine-tuned variants (six model configurations total). This breadth strengthens the generalizability of the findings.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative comparison to existing disentanglement methods.** The paper's evaluation (§5) consists entirely of self-consistency checks (probing) against original hidden states. While these checks demonstrate that the method *can* separate textual and acoustic factors, they do not establish whether the framework offers advantages over existing approaches surveyed in the related work (§8) — adversarial decorrelation (Wang et al. 2021), AutoVC/SpeechSplit, NANSY, Prosody2Vec, or even a simpler β-VAE baseline. For a method paper proposing a new framework, the absence of any baseline comparison is a significant gap. Even a single comparison — e.g., an adversarially trained encoder to prevent a discriminator from recovering transcriptions — would help situate the contribution.

2. **Attribution analysis mentions Integrated Gradients comparison without presenting results.** §7 (Section 6 in the paper) states that Integrated Gradients was used to compute frame-level attribution and the scores were normalized for comparison with the attention-based scores, but no IG results are shown in Figure 6 or anywhere else. The reader cannot evaluate whether the proposed disentangled attention offers advantages over existing gradient-based methods. Combined with the observation that textual attention scores also correlate with acoustic features (attributed to polar words being spoken with emphasis), this undermines the claim of cleanly separated attribution. The section is explicitly labeled as preliminary, but mentioning a comparison without presenting it is an unfulfilled claim.

3. **No sensitivity analysis for the β coefficient.** The paper uses a linear schedule from 0.1 to 1 (line 110) but provides no ablation or sensitivity analysis for different β values, schedules, or constant values. Since the information loss term (controlled by β) is central to the method — the footnote confirms training without it fails to disentangle — the lack of any analysis showing how performance and disentanglement vary with β is a meaningful omission. Similarly, the paper experiments with bottleneck dimensions d ∈ {16, 32, 64, 128, 256} (line 107) but only reports d=128 results throughout, leaving the trade-off between compression and performance unexplored.

### Minor

1. **Sanity probing only shown for Large models.** Figure 3 reports probing results only for Large model variants, yet Table 1 includes results for Base models on downstream tasks. Since the method's effectiveness could scale with model capacity, showing that disentanglement holds for Base models would strengthen the claims. The probing setup (acoustic features on Common Voice) is model-agnostic and could be run on Base models without additional data.

2. **Critical ablation (training without information loss) relegated to a footnote.** The paper's own most informative control experiment — training the encoders without the KL information loss term — is described only in a footnote (line 86). The footnote states that this variant "failed to disentangle... as intended (shown in Section 5)," but no quantitative ablation results are visible in the evaluation section. Given that this control directly supports the central claim that the information bottleneck is essential, it deserves a dedicated figure or table in the main body rather than a single off-hand remark.

3. **Layerwise analysis uses separately trained VIB models per layer.** Rather than using the weighted-average framework (which could be adapted to yield per-layer contributions via attribution of the learned weights), the paper trains the entire two-stage pipeline independently for each layer (line 225). This is computationally expensive and raises the question of whether hyperparameters (β schedule, learning rate, bottleneck dimension) were independently optimized per layer or reused uniformly, making it unclear whether observed patterns reflect genuine layer differences or artifacts of suboptimal training for some layers.

### Trivial
None.

## Nice-to-Haves

- **In-domain stage 1 training for IEMOCAP.** Stage 1 is trained on LibriSpeech/Common Voice but applied to IEMOCAP in stage 2. An experiment where stage 1 is also trained on a small amount of IEMOCAP data (for which transcripts exist) would test whether in-domain textual latents improve downstream emotion recognition.
- **Qualitative attribution examples.** Showing individual test examples with attention weights overlaid on audio frames, transcriptions, and acoustic contours — where acoustic peaks and sentiment-laden words do not co-occur — would be more convincing than the aggregate dot-product plot in Figure 6.
- **Report probing results for Base models** in the same format as Figure 3, or state clearly if they were not computed for a specific reason.

## Removed Points

- The harsh critic's point that the layerwise analysis is "extremely computationally expensive" and potentially "biased against layers that require different β values" — this is a valid concern but overstated. Per-layer VIB training is a standard (if costly) approach and the paper's main findings use the weighted-average framework. Downgraded to **Minor**.
- The harsh critic's suggestion that "the paper should present direct comparisons between acoustic attention, textual attention, and Integrated Gradients on specific test examples" — this is a nice-to-have rather than a core weakness, since the paper explicitly frames the attribution analysis as preliminary. Moved to Nice-to-Haves.
- The harsh critic's claim that "the method's effectiveness may scale with model capacity" for Base model probing — this is speculative; the real issue is that the data simply isn't shown, not that it would necessarily differ.
- Strength Finder's claim that "ablation confirms necessity of information loss" — this partially conflicts with the verified weakness that the ablation is only in a footnote without visible quantitative results. The strength is retained but the weakness is that it's not properly presented.

## Novel Insights

The reviews surface a tension in the paper: the probing evidence for disentanglement is genuinely strong and the t-SNE visualization is compelling, but these are *necessary* conditions for a new disentanglement method, not *sufficient* ones to establish that the method improves upon the state of the art. The paper's main weakness is not that its core claim is false — the probing results convincingly show the method disentangles textual and acoustic features — but that the paper stops at self-consistency without situating its contribution against any alternative. This is a case where the reviewer critiques are better classified as "unrealized potential" rather than "fatal flaws," but the evaluation gap is real and significant for a venue that evaluates papers competitively.

## Suggestions

1. Add at least one baseline comparison — the simplest being an adversarial disentanglement approach where a single VIB encoder is trained for the target task while a discriminator is adversarially prevented from recovering transcriptions. This directly tests whether the two-stage conditioning offers advantages over an adversarial objective.
2. Present the Integrated Gradients comparison that is already mentioned in §7, or remove the mention if the comparison was not systematically conducted.
3. Include a brief sensitivity analysis for β (e.g., 3-5 values or schedules) and show probing results for at least 2-3 bottleneck dimensions to substantiate the claim that d=128 is a reasonable choice.
4. Either show Base model probing results or add a clear statement that they were omitted for space/scope reasons.
5. Move the ablation study (training without information loss) from the footnote to the main text with a dedicated figure or table.

## Score and Decision

The paper proposes a well-motivated framework and provides convincing in-house evidence that it achieves disentanglement. However, the absence of any comparison to existing methods, the unfulfilled claim about Integrated Gradients in the attribution analysis, and the lack of sensitivity analyses for the core hyperparameters (β and bottleneck dimension) leave the contribution insufficiently contextualized. The paper would benefit substantially from revisions to address these gaps.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>