Now I have all the evidence needed to produce the final consolidated review.

## Summary

Vevo presents a self-supervised framework for controllable zero-shot voice imitation that disentangles timbre, style, and linguistic content by applying VQ-VAE tokenizers at different vocabulary sizes (K=32 for content, K=4096 for content-style) on HuBERT features. These tokens drive a two-stage pipeline: an autoregressive transformer for content-to-content-style modeling (style-controllable), and a flow-matching transformer for acoustic generation (timbre-controllable). The framework is evaluated across timbre imitation, style imitation (accent/emotion conversion), voice conversion, and TTS tasks.

## Strengths

- **Novel and validated disentanglement via VQ codebook-size bottleneck**: The paper demonstrates that varying the VQ-VAE vocabulary size on HuBERT features progressively filters timbre first, then style. Table 2 provides clear quantitative evidence (e.g., at K=4096, speaker similarity to source drops to 0.236 vs. 0.737 for continuous features while F0 correlation stays high at 0.797; at K=32, FPC falls to 0.706). This is a clean, fully self-supervised approach.

- **Strong and properly-controlled results on timbre imitation and voice conversion (Table 3)**: Vevo-Timbre and Vevo-Voice are evaluated against four SOTA baselines on a fixed 700-sample set from LibriSpeech, CommonVoice, ACCENT, and EMOTION. Vevo-Timbre achieves the best S-SIM (0.494), SS-MOS (4.02), and FPC (0.763) among all methods. This evaluation is well-controlled and supports the framework's effectiveness.

- **Competitive TTS performance despite training data limitations (Table 5)**: Vevo-TTS is compared against Voicebox (same 60K-hour audiobook data), VALL-E, VoiceCraft, CosyVoice, and MaskGCT. Against Voicebox (identical training data), Vevo-TTS excels across all style-related metrics (A-SIM 0.541 vs. 0.543, ES-MOS 4.03 vs. 3.94). Despite training only on audiobook data, it matches models trained on larger in-the-wild data on emotion similarity.

- **Thorough ablation and analysis**: Section 4.1 systematically investigates the effect of vocabulary size, compares K-means vs. VQ-VAE, and selects K values empirically with reasoned tradeoffs. Table 6 further validates the duration reduction strategy and two inference modes, strengthening technical soundness.

- **Scalable, annotation-free training**: The entire pipeline is trained via self-supervised objectives (next-token prediction and conditional flow matching) on 60K hours of audiobook data without style labels or parallel corpora, supporting the claim of reduced annotation dependence.

## Weaknesses

### Fatal
None.

### Major

- **Style imitation evaluation (Table 4) uses uncontrolled, non-overlapping demo website samples, undermining the core claim of matching/surpassing existing methods in accent and emotion conversion.** The paper explicitly states that "Evaluation samples for each group are sourced from the baseline's demo website" (Table 4 caption). This means: (a) test sets are tiny and curated by each baseline team to showcase their best outputs; (b) test sets are non-overlapping across methods (different speakers, utterances, recording conditions); (c) the comparison is not controlled. The paper's abstract and contributions prominently emphasize that Vevo "matches or surpasses existing methods in accent and emotion conversion tasks," but this claim rests on an evaluation protocol that does not meet standard experimental practice. The other tasks (timbre imitation, voice conversion, TTS) are properly evaluated and remain convincing, but the most distinctive claim about zero-shot style imitation is unsubstantiated. Without a controlled evaluation — either on a common benchmark (e.g., accented/emotional subsets of VCTK, ESD, or the Expresso data already used for other experiments) with all methods re-evaluated, or at least on a fixed independently-collected test set — this central contribution cannot be verified.

### Minor

- **No statistical significance or variance reported.** None of the tables report confidence intervals, standard deviations, or significance tests. Given the moderate sample sizes (e.g., 700 for Table 3, smaller for Table 4), some observed differences could be within noise. This is standard practice for large-scale speech generation papers, but its absence is worth noting.

- **No discussion of limitations or failure cases.** The paper does not address scenarios where the method might struggle (e.g., very short style references, heavy background noise, non-speech content in reference, the higher WER observed in autoregressive stages). While common in conference papers, this omission prevents a balanced understanding of the approach's boundaries.

- **F0 correlation (FPC) as the sole prosody/style metric in the disentanglement analysis (Table 2).** While FPC is a standard and meaningful proxy, the "progressive disentanglement" claim would be strengthened by additional metrics capturing rhythm, energy, or broader prosodic patterns. The paper's downstream results partially address this, but the core validation in Section 4.1 relies heavily on this single style-related metric.

### Trivial
None.

## Nice-to-Haves

- **Controlled style imitation evaluation on a standard benchmark** (e.g., evaluating all methods on the same accented/emotional test set) would resolve the main weakness. This is a must-fix rather than a nice-to-have, but since it would require a substantial additional experiment, it is noted here as the single highest-priority revision.

- **TTS results on LibriSpeech test-clean or CommonVoice** to complement the ACCENT/EMOTION-focused evaluation in Table 5 and enable comparison with the broader TTS literature. The paper already evaluates on these datasets for timbre/voice conversion, so extending to TTS would be natural.

- **A direct validation of the content-style token's style-preservation** (e.g., training a linear classifier on the tokens to measure accent/emotion classification accuracy) would strengthen the disentanglement claim independently from the downstream tasks.

## Removed Points

- **"Evaluation of zero-shot style imitation is fundamentally flawed, invalidating the boldest claims"** — This is kept as the Major weakness above. However, the characterization that it "invalidates the paper's central thesis" is overstated. The paper has multiple contributions (disentanglement methodology, unified framework, TTS/VC results) that are independently valid. The style imitation claim is one important contribution, not the sole thesis.

- **"The progressive disentanglement claim is supported only by indirect and insufficient evidence"** — Partially removed. Point (b) about circular reasoning is incorrect: the downstream experiments in Tables 3 and 5 directly validate that the tokens preserve usable style information, and Table 2 independently measures FPC. Point (c) about missing comparison to adversarial/MMI techniques is scope creep — the paper compares against K-means and ASR features, which are the most directly relevant baselines.

- **"Strength: Outperforms existing methods in zero-shot style imitation"** — Removed because it conflicts with the verified weakness about Table 4's uncontrolled evaluation. The evidence for this claim is not reliable.

- **"Zero-shot TTS evaluation on standard benchmarks (LibriSpeech test-clean)"** — Demoted to Nice-to-Have. The paper already evaluates on LS/CV for other tasks. Focusing TTS evaluation on ACCENT/EMOTION is a reasonable scope decision for a style-focused paper.

- **"Missing comparison to other disentanglement techniques (adversarial, mutual information minimization)"** — Removed as scope creep. The paper compares against K-means and ASR features, which are the most relevant baselines for VQ-based disentanglement.

- **"The paper uses an information bottleneck approach that is not new"** — The harsh critic acknowledges this is "a novel combination." The reviewer does not present this as a weakness. Not included.

## Novel Insights

The most insightful observation from the reviews is that the paper's strongest and most distinctive claim (zero-shot style imitation matching/surpassing existing methods) rests on an evaluation protocol that would be considered weak even in a workshop paper: comparing against baselines using each baseline's own cherry-picked demo samples. This is not a subtle methodological nitpick — it is a basic failure of controlled experimentation that means the reader simply cannot trust the reported superiority in accent and emotion conversion. Meanwhile, the other evaluations (Tables 3 and 5) are properly controlled and show genuine promise for the disentangled token approach, particularly in timbre imitation and TTS. The disconnect between the rigor of the controlled experiments and the lack of rigor in the style imitation experiment is striking and suggests the authors should either (a) conduct a proper controlled evaluation or (b) recalibrate their claims to match what the evidence actually supports.

## Suggestions

1. **Replace the style imitation evaluation (Table 4) with a controlled experiment.** Use a standard benchmark dataset (e.g., the accented/emotional subsets of VCTK, ESD, or Expresso itself — which you already use in other experiments). Evaluate Vevo-Style and all baselines on exactly the same test utterances. If baselines' code/models are unavailable, at minimum include a strong disclaimer and present the current results as illustrative rather than comparative.

2. **Report confidence intervals or standard deviations** for all metric tables, especially given the moderate sample sizes.

3. **Add a limitations section** discussing known failure cases (short references, noise, the WER degradation in autoregressive stages, etc.).

4. **Consider adding TTS results on LibriSpeech test-clean** to enable direct comparison with the broader TTS literature (VALL-E, VoiceCraft, etc.).

## Score and Decision

The paper presents a well-motivated, technically sound approach to disentangled speech representation learning and a versatile framework for multiple voice imitation tasks. The controlled experiments on timbre imitation, voice conversion, and TTS (Tables 3 and 5) provide reasonable evidence for those contributions. **However, the paper's most distinctive advertised contribution — matching or surpassing existing methods in zero-shot accent and emotion conversion — is evaluated using a fundamentally flawed protocol (demo website samples), rendering that central claim unsubstantiated.** Since the abstract, introduction, and conclusion all prominently feature this as a key result, the paper cannot be accepted in its current form. With a proper controlled evaluation, the paper would be a strong contribution.

**Score: 5.0** — Marginally below the acceptance threshold. The paper has real strengths but the main novel claim is not properly supported.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>