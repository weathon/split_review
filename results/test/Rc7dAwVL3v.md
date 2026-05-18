Now I have all the information needed. Let me compile the final review.

## Summary

This paper presents NaturalSpeech 2, a large-scale text-to-speech system that combines continuous latent vectors (from the sum of residual vector-quantizer embeddings) with a latent diffusion model. The key design choices are: (1) continuous vectors instead of discrete tokens to avoid the reconstruction-quality vs. sequence-length dilemma, (2) a non-autoregressive diffusion model to avoid error propagation, and (3) a speech prompting mechanism for zero-shot in-context learning. Trained on 44K hours of speech and 30 hours of singing data (400M parameters, 5K speakers), the system achieves strong zero-shot synthesis results on LibriSpeech and VCTK, including a CMOS of +0.04 vs. ground truth on LibriSpeech, SMOS of 3.28 (vs. YourTTS 2.03), and a WER of 2.26% (vs. YourTTS 7.10%). It also demonstrates zero-shot singing synthesis using only a speech prompt.

## Strengths

- **Novel combination of continuous latent vectors and latent diffusion resolves the discrete-token dilemma.** The paper identifies a fundamental tension in prior large-scale TTS systems (Table 2): discrete tokens from RVQ force a trade-off between reconstruction quality and sequence length. NaturalSpeech 2's approach of summing RVQ embeddings into continuous vectors preserves detail without lengthening the sequence, and the non-autoregressive diffusion model avoids error propagation. The ablation study (Table VIII) confirms that key components (diffusion prompt, query attention, CE loss) each contribute meaningfully to prosody similarity.

- **Strong zero-shot speaker similarity and naturalness outperforming strong baselines.** On LibriSpeech, NaturalSpeech 2 achieves SMOS of 3.28 (vs. YourTTS 2.03, ground truth 3.33) and CMOS of +0.04 vs. ground truth (Table 3). Compared to VALL-E, it improves SMOS by 0.30 and CMOS by 0.31 (Table 7). WER on LibriSpeech is 2.26%, substantially better than YourTTS at 7.10% and close to ground truth at 1.94%.

- **Speech-prompting mechanism with query-based attention is shown to be critical for zero-shot capability.** The ablation study confirms that removing the diffusion-model prompt causes non-convergence ("-"), and removing the query attention (directly attending to prompt hidden) degrades prosody similarity metrics (pitch mean diff rises from 10.11 to 10.78).

- **Zero-shot singing synthesis with only a speech prompt is a genuinely novel capability.** The system can generate a singing voice from a speech prompt without any singing reference, going beyond prior work that requires a singing prompt. Audio samples are provided via a demo page.

## Weaknesses

### Major

- **VALL-E is claimed to have robustness issues but is not included in the robustness comparison.** The robustness test (Table VI) compares NaturalSpeech 2 against Tacotron (2017) and Transformer TTS (2019) as the AR baselines, both achieving 24-34% error rates. The paper states in text that "VALL-E will have a high error rate on these hard sentences" but provides no data — VALL-E does not appear in the table. To support the claim that diffusion models are inherently more robust than modern AR models, VALL-E (the paper's primary competitor) must be evaluated on the same 50 hard sentences. Without this, the table primarily confirms that decade-old AR models are less robust than modern NAR models — a well-known result.

- **Singing synthesis and extensions (voice conversion, speech enhancement) lack any quantitative evaluation.** Section 5.6 presents zero-shot singing as a novel contribution — "interestingly…with only a speech prompt, which unlocks the truly zero-shot singing synthesis" — yet provides no objective or subjective metrics (no prosody similarity, speaker similarity, naturalness, or even a simple ABX preference test). Similarly, Sections 5.7 (voice conversion and speech enhancement) include no quantitative results whatsoever. These tasks inflate the paper's scope without supporting evidence. At minimum, the singing results need evaluation, or the claims should be explicitly marked as preliminary demonstrations.

### Minor

- **CMOS and SMOS results lack confidence intervals or significance tests.** The paper reports CMOS of +0.04 (LibriSpeech) and −0.30 (VCTK) vs. ground truth, with only 20 utterances and 12 listeners. The headline claim "comparable to the ground-truth recording in LibriSpeech" rests on a +0.04 difference that is almost certainly not statistically significant at this sample size. SMOS similarly lacks uncertainty quantification. This is critical because the paper uses "comparable to ground truth" as a headline result.

- **The WER comparison against ground truth on VCTK is methodologically problematic.** NaturalSpeech 2 achieves 6.99% WER on VCTK vs. ground truth at 9.49%. The authors attribute the high ground-truth WER to "noisy environment and the lack of ASR model fine-tuning." However, if the ASR model is poorly adapted to VCTK's acoustic conditions, the model's output — which may be cleaner or match the ASR's training distribution better — could artifactually achieve a lower WER without being more intelligible. The "surpasses ground truth" claim in Section 5.3 is unwarranted without controlling for this mismatch (e.g., matched-noise comparison or a VCTK-fine-tuned ASR). The authors acknowledge the caveat but still make the claim.

- **The ablation "cannot converge" without the diffusion prompt raises unanswered design questions.** The paper marks "w/o diff prompt" as non-convergent ("-") but does not explain why the diffusion model fails without the prompt. This suggests the conditioning in the diffusion model may rely on the prompt to determine the overall acoustic space, potentially meaning the zero-shot capability is less about "in-context learning" and more about providing an acoustic anchor that compensates for the conditioning pipeline being insufficiently informative on its own. Some discussion of this design dependency would strengthen the paper.

- **The benefit of continuous vectors over discrete tokens is not isolated from the benefit of diffusion over autoregressive models.** The paper's comparison of NaturalSpeech 2 (continuous + diffusion) to VALL-E (discrete + AR) confounds two variables. An ablation holding the generative model fixed (diffusion) and varying only the representation (continuous vs. discrete) would more directly support the claim that continuous vectors are the key advantage. As it stands, improvements could be attributed to the diffusion model's non-autoregressive nature rather than the continuous representation.

### Trivial

None.

## Nice-to-Haves

- The CE loss ablation (w/o CE loss) shows moderate degradation, but the paper does not discuss why this discrete-token regularization is needed despite the narrative of avoiding discrete representations. A brief explanation would be helpful.
- An experiment with a smaller training set (e.g., 1K hours) could help disentangle benefits due to scale vs. architectural choices.
- A matched-condition comparison for the VCTK WER (e.g., adding VCTK-like noise to ground truth before ASR evaluation) would resolve the concern cleanly.

## Removed Points

- **Typo critique ("Non-Autoregressvie"):** Removed per formatting/style rule — these are parser-level presentation artifacts, not substantive issues.
- **"Continuous vs. discrete not isolated" kept but downgraded** from the reviewer's framing as a critical oversight to Minor, because the paper's contribution is the whole system design, not isolating a single variable. The existing VALL-E comparison is valid as a system-level comparison.
- **"Source-Aware Diffusion Process may produce unstable results"** from the Harsh Critic's "Other Observations": removed as speculative — the paper briefly acknowledges this, and the reviewer provides no evidence of instability.
- **"The ablation diffusion prompt non-convergence"** concern about the prompt being "functionally necessary" kept but reclassified from implied fatal flaw to Minor, since the paper clearly presents this result and the implication supports the importance of the design rather than invalidating it.

## Novel Insights

The Harsh Critic makes an interesting observation about the "w/o diff prompt" ablation: that the model's inability to converge without it suggests the prompt is doing more than improving prosody similarity — it may be providing essential conditioning information that the phoneme encoder and duration/pitch predictor pipeline alone cannot supply. This points to a potential coupling between the prompting mechanism and the basic conditioning architecture that would be worth probing in future work, particularly to understand whether the zero-shot ability relies on the prompt as a crutch for insufficiently informative text-side conditioning. The Strength Finder correctly notes that the paper's strongest evidence is the CMOS on LibriSpeech (+0.04 vs. ground truth) combined with the SMOS advantage over baselines — this is genuinely impressive for a zero-shot TTS system.

## Suggestions

1. **Include VALL-E in the robustness test (50 hard sentences).** This is essential to support the claim that diffusion models are more robust than modern AR models. Without it, the robustness comparison is against decade-old systems.
2. **Add confidence intervals or Bayesian credible intervals for all subjective evaluations (CMOS, SMOS).** Without these, the reader cannot distinguish a genuine match from an underpowered test on the headline "comparable to ground truth" claim.
3. **Provide at least a basic quantitative evaluation for singing synthesis** — a speaker similarity ABX test or pitch accuracy metric would significantly strengthen the novelty claim. For VC and speech enhancement, even simple objective metrics (e.g., WER, speaker similarity) would help.
4. **Address the VCTK WER mismatch** by either running a matched-condition evaluation or explicitly reframing the claim from "surpasses ground truth" to "achieves lower WER under the current ASR, likely due to acoustic condition mismatch."
5. **Add a discussion of why the model cannot converge without the diffusion prompt.** If the prompt is functionally necessary for basic generation, the zero-shot claim should be qualified accordingly.

## Score and Decision

**MY FINAL SCORE:** <score>7.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>