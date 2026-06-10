## Summary

This paper proposes CM², an audio-visual speech enhancement (AVSE) framework that introduces two types of contextual information—semantic context (from pre-trained AV-HuBERT features via SeCM) and signal context (via bidirectional Mamba sequence modeling in SiCM)—and fuses them across both time and frequency domains (CCFM). The method is evaluated on the LRS3+DNS4 dataset and reports large improvements over prior methods, particularly at very low SNR (-15 dB).

## Strengths

- **Validated dual-context modeling with component-level ablation**: The SeCM and SiCM modules are individually ablated (Tables 2, 4), confirming that both semantic context from AV-HuBERT features and signal context from bidirectional Mamba contribute to performance. The layer-wise analysis of AV-HuBERT encoder features (Table 3) provides nuanced and useful empirical guidance about which layers provide the most benefit, honestly noting exceptions (e.g., layer 12 outperforming layer 24 on SDR at some SNR levels).

- **Concrete architectural specifications**: The CCFM with its Channel Swapping Block (CSBlock), TF-Upsampler, and separate time/frequency-domain fusion blocks is clearly described (Section 3.4, Equations 132–134). The use of Bidirectional Mamba for sequence modeling in the AVSE context is a reasonable and well-motivated architectural choice.

- **Strong absolute performance at very low SNR**: At −15 dB SNR, the method achieves substantial raw improvements (63.6% SDR, 58.1% PESQ, 20.3% STOI relative gains over prior methods), suggesting the approach makes meaningful progress on the hardest conditions that motivate the work.

## Weaknesses

### Fatal
None.

### Major

- **Claimed contribution about frequency-domain visual fusion is not experimentally validated**: The paper states as its second contribution that it has "experimentally validated the critical role of visual information along the audio frequency domain" (line 54). Yet none of the ablation experiments (Tables 2–4) isolate the frequency-domain fusion block. There is no comparison against a variant that performs only time-domain fusion (removing the frequency-domain fusion block in CCFM), no ablation that varies whether frequency-domain fusion is present, and no direct measurement of whether visual features contribute specifically to frequency-domain modeling. A claim this prominent must be backed by targeted evidence, not assumed from overall system performance. Without such an ablation, this contribution is asserted, not validated.

- **Evaluation presented on only one of four claimed datasets**: The abstract claims "Comprehensive evaluations across various datasets" (line 16) and contribution 3 states "Comprehensive evaluations on four composite datasets" (line 55). However, the paper explicitly states: "Due to space constraints, we only present the experimental results on the widely-used LRS3+DNS4 dataset here" (line 216). Even granting that other results may reside in an appendix, the main paper presents evidence from a single dataset. The four dataset pairs (LRS3+DNS4, GRID+CHiME3, TCD-TIMIT+NTCD-TIMIT, MEAD+DEMAND) include diverse conditions (constrained vocabulary, emotional speech, different noise types). The claim of "comprehensive" evaluation across broad conditions cannot be assessed from one dataset alone.

- **Unclear fairness of baseline comparisons given anomalously large improvements**: The paper reports relative improvements of 63.6% in SDR and 58.1% in PESQ at −15 dB SNR, and states that the −15 dB results "even surpass those achieved by the DualAVSE method at 0 dB" (line 232). Such enormous gains demand a credible explanation of the comparison setup. The training SNR range is −15 to 0 dB (line 220). The paper does not state whether prior methods were retrained on this same SNR range or whether published numbers from different training setups are being used. If baselines were trained on different, less challenging SNR ranges, comparing at −15 dB would be fundamentally asymmetric. No variance, confidence intervals, or standard deviations are reported for any result, making it impossible to assess statistical significance.

### Minor

- **Phonemic restoration framing is metaphorical, not operational**: The paper is motivated throughout by phonemic restoration, describing how "the auditory system's ability to perceptually reconstruct interrupted speech using visual cues and semantic context" (line 7) inspired the approach. However, the actual architecture implements no mechanism that specifically models or simulates phonemic restoration. The "semantic context" is obtained from standard AV-HuBERT speech recognition features, and the "signal context" from generic bidirectional Mamba sequence modeling. Neither component is designed to operationalize the cognitive phenomenon. The paper could be described as "AVSE with cross-modal fusion using AV-HuBERT features and Mamba-based sequence modeling" without reference to phonemic restoration. The framing inflates the paper's conceptual novelty without doing substantive work.

- **The claim that most AVSE methods overlook frequency-domain correlations is imprecise**: The paper states that "most existing AVSE methods focus solely on the fusion in the temporal domain and overlook the potential correlations between the frequency dimensions of the visual and audio modalities" (line 67). Several prior AVSE methods operate in the time-frequency domain and perform spectrogram-level fusion (e.g., mask prediction), which inherently involves frequency dimensions. The paper would benefit from a more precise characterization of what distinguishes its frequency-domain fusion from prior spectrogram-level approaches.

- **No variance or uncertainty quantification**: No standard deviations, confidence intervals, or statistical significance tests are reported for any metric. Given that SDR, PESQ, and STOI vary across noise realizations and random seeds, this weakens the evidence base.

- **PESQ-predicting discriminator is under-discussed**: The discriminator is designed to estimate the non-differentiable PESQ metric and use it as a training objective (Section 3). The paper does not analyze how well the discriminator approximates PESQ or whether this setup risks the generator overfitting to the discriminator's PESQ estimate rather than to actual speech quality.

### Trivial
None.

## Nice-to-Haves

- Add an ablation comparing the full CCFM (time + frequency fusion) against a variant with time-domain-only fusion to directly validate the frequency-domain claim.
- Show results on at least one additional dataset pair (e.g., GRID+CHiME3 or MEAD+DEMAND) in the main paper to support the claim of comprehensive evaluation.
- Clarify whether baseline methods were retrained on the same SNR range (−15 to 0 dB) or whether published numbers from different setups are being used.
- Add a limitations paragraph discussing conditions where performance may degrade (e.g., occluded visual stream, unseen speaker categories).

## Removed Points

These points were flagged by reviewers but removed per the filtering guidelines:
- *Notation corruption at line 78 ($X^{\prime}\in\mathbb{R}^{3\times T_{x}}^{\star}Y_{x}$) and dimension formatting ($B\dot{\times}C_{e}\times T_{e}$)* — These are parser-induced formatting artifacts, not author errors.
- *"Baseline method names not enumerated in text"* — This is a minor presentation issue; the names are in the table.
- *"Missing related works"* — Per instructions, I cannot validate this assertion.
- *Generic strength finder claims* (e.g., "the paper addresses an important problem") — These are superficial and lack specific evidence.

## Novel Insights

The reviews collectively surface an interesting tension: the paper's strongest evidence (component-level ablations for SeCM and SiCM) validates the less architecturally distinctive claims (use of speech recognition features and sequence modeling), while its most distinctive claims (frequency-domain visual fusion role, comprehensive multi-dataset evaluation) are the least supported. This creates a mismatch between what the paper *does* well and what it *claims* as novel—a pattern that careful reading of the ablation design reveals but individual component analyses might miss.

## Suggestions

1. Add a targeted ablation: compare full CM² against a variant where the CCFM performs only time-domain fusion. Report the difference in SDR/PESQ/STOI to directly validate contribution 2.
2. Move results from at least one additional dataset (e.g., GRID+CHiME3) into the main paper to support the "comprehensive evaluation" claim.
3. State explicitly whether each baseline was retrained on the same SNR range (−15 to 0 dB) and report variance across runs or noise samples.
4. Tone down the phonemic restoration framing if no direct mechanism connects the architecture to the cognitive phenomenon.
5. Add a brief analysis of the PESQ-predicting discriminator's accuracy and potential failure modes.

## Score and Decision

The paper proposes a well-engineered AVSE system with reasonable components and some informative ablations. However, it suffers from a significant gap between its claims and its evidence: (a) the most distinctive claimed contribution (frequency-domain visual fusion) is never directly tested, (b) the "comprehensive" evaluation is presented on only one of four datasets, and (c) the extraordinarily large improvements lack clarity on whether baseline comparisons are fair. These are structural evidential problems, not methodological fatal flaws. The core method has merit, but the paper in its current form substantially oversells its contributions. Major revision is required before the paper's conclusions can be accepted at face value.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>