- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

This paper proposes SeMDiff, a diffusion-based framework for image-to-long text generation that uses a semantic concept predictor (SCP) to extract salient concepts from visual representations, a semantic conditional memory (SCM) to enhance those concepts with stored image-text correlation information, and a diffusion decoder that iteratively generates text conditioned on both visual features and enhanced semantic concepts. The paper introduces COCO-LT, a new dataset of 54,785 image–long text pairs built by prompting ChatGPT to fuse five COCO captions into a paragraph. Experiments on four datasets (MIMIC-CXR, CC-SBU, Localized Narratives, COCO-LT) report improvements over several baselines and claim to outperform large vision-language models.

---

## Strengths

- **New dataset (COCO-LT) for I2LTG.** The paper introduces a dedicated benchmark with 54,785 image–long text pairs (Table 1), filling a gap in resources for evaluating long-text generation in image captioning. This is a concrete and reusable contribution.
- **Clean ablation study showing component contributions.** Table 2 compares four variants (Diff, Diff+SCP, Diff+SCM, Diff+SCP+SCM) across all four datasets. The full model consistently achieves the best scores on BLEU, METEOR, and ROUGE-L, with statistical significance markings. This directly validates the paper's central architectural claim that both SCP and SCM contribute to better generation.
- **Comprehensive hyperparameter analysis.** Figure 2 systematically studies the effect of semantic matrix size (N_s), memory size (N_m), and number of queried memory vectors (κ) on BLEU-4. The analysis reveals clear patterns (e.g., performance convergence at memory size 2048, overfitting with too many concepts), providing practical guidance for applying the model.
- **Qualitative evidence of reduced word repetition.** Figure 3 shows the iterative generation process of the full model vs. the baseline, illustrating that the semantic guidance reduces repetitive words and produces more semantically aligned outputs — directly addressing a known weakness of non-autoregressive text generation.

---

## Weaknesses

### Fatal
None.

### Major
- **LLM comparison protocol is unspecified.** The paper's strongest claim — that SeMDiff outperforms BLIP-2 (8.3B), MiniGPT-4 (7.7B), LLaVA (13B), XRAYGPT, and Med-PaLM on all four datasets (Table 3, Table 4, line 198) — is presented without stating how these models were evaluated. Were they fine-tuned on each dataset? Used zero-shot? Provided with task-specific prompts? Given that several of these datasets (e.g., CC-SBU, COCO-LT) are not standard evaluation benchmarks for these LLMs, the reader cannot assess whether the reported superiority reflects method strength or an asymmetry in evaluation conditions. This is not a minor transparency issue: the paper's narrative heavily emphasizes this result ("appropriate semantic guidance is more efficient than using a massive amount of parameters in LLMs," line 198-199). Without clarifying the evaluation protocol, this central comparative claim is unverifiable from the paper as submitted.

### Minor
- **"Long text" framing is not experimentally validated.** The paper motivates the need for *long* text generation throughout (title, abstract, introduction), but no experiment isolates text length as a variable. The method is evaluated on datasets with average lengths of 40.9–105.7 words, yet there is no comparison showing that performance scales with length, that the method specifically helps on longer outputs, or that the semantic guidance matters more when texts are longer. The results remain valid, but the framing as an "image-to-long text" solution specifically is undersupported.
- **SCM gains are marginal on several metrics.** In Table 2, the difference between Diff+SCP and the full model (Diff+SCP+SCM) is very small on some metrics (e.g., the reviewer reports BLEU-1 of 0.397 vs. 0.398 and ROUGE-L of 0.335 vs. 0.338 on MIMIC-CXR). The paper claims the full model "achieves the best result" (line 193) but does not discuss where the memory module provides meaningful gains vs. where it plateaus. A targeted analysis (e.g., does SCM help most when concepts are noisy, or does it reduce repetition rates?) would strengthen the contribution.
- **Hyperparameter analysis (Figure 2) lacks error bars or repeated trials.** The curves show BLEU-4 scores for a single metric across hyperparameter settings, but without error bars or multiple runs it is unclear whether the observed trends (especially the sharp drops at certain values) are stable or artifacts of a single trial.

### Trivial
- **Case study (Figure 3) shows only one example.** While informative, a single illustration is not evidence of systematic improvement. Including 2–3 examples or a small human evaluation would be more convincing.

---

## Nice-to-Haves

- **Human evaluation of generated texts.** For long-text generation, automated metrics like BLEU and ROUGE are known to correlate weakly with human judgment on coherence and completeness. Even a small-scale human rating (e.g., on fluency, completeness, and coherence for 50–100 samples) would significantly strengthen the evidence.
- **Analysis of SCP prediction accuracy.** Since SCP is a core component, reporting concept prediction accuracy (e.g., precision/recall of predicted concepts against gold concepts) would help disentangle whether generation failures stem from concept prediction errors or from the diffusion decoder.
- **Length-stratified analysis.** Binning test samples by output length and showing that the margin over baselines grows with length would directly validate the "long text" framing.
- **Repetition rate quantification.** The case study qualitatively shows reduced repetition; reporting repetition rates across the test set would provide quantitative evidence for this claimed benefit.

---

## Removed Points

*These points were flagged for removal; treat them with caution:*

- **"Non-MIMIC baseline setups are unclear (MIR, SATIC, SCD-NET)."** — The paper cites "existing state-of-the-art solutions" with footnote references (⁸, line 198) which are stripped by the parser. These footnotes likely specify how published results were obtained. The concern is speculative given the stripped content.
- **"ResNet-101 backbone is outdated."** — ResNet-101 is a standard backbone choice. The contribution is about the semantic guidance framework, not the backbone. This is a style opinion, not a substantive weakness.
- **"Mean pooling in SCP discards per-concept information."** — The critic acknowledges this is "a valid choice." It is a design decision, not a flaw.
- **"Concept extraction pipeline inconsistency across datasets."** — The paper transparently describes the per-dataset annotation process (MTI for MIMIC-CXR, POS filtering for others). This is appropriate adaptation to different data modalities, not a weakness.
- **"No code release mentioned."** — Per the review guidelines, code release is not a standard requirement for evaluating the paper's technical contribution.
- **"No human evaluation."** — Moved to Nice-to-Haves above. Many papers in this area do not include human evaluation, and its absence is not a flaw.
- **"N_c (number of predicted concepts) not specified."** — This detail may be in the stripped footnotes or in-line description that was lost in extraction. Not verifiable from the available text.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine concern about the LLM comparison's verifiability but do not reveal novel connections or alternative interpretations that the authors missed.

---

## Suggestions

1. **Clarify the LLM evaluation protocol.** In the main text, explicitly state whether each LLM was fine-tuned, used zero-shot, or provided with task-specific prompts. If results are taken from published papers, cite them directly and state this clearly. If the LLMs were used zero-shot, reframe the claim as "outperforms zero-shot LLMs" and discuss the tuning advantage transparently.
2. **Add a length-stratified experiment.** Bin test samples by output length (e.g., short/medium/long) and show that the margin over baselines grows with length, or at minimum show that the model performs well across lengths.
3. **Discuss SCM's contribution more honestly.** Acknowledge where the gains are marginal in Table 2 and provide additional analysis (e.g., repetition rate, concept accuracy) to clarify where SCM helps most.
4. **Add error bars or repeated trials to Figure 2.** Given the sensitivity of some curves (sharp drops at certain K values), indicate whether these patterns are stable across runs.
5. **Report the total parameter count of SeMDiff** to contextualize the comparison against much larger LLMs.

---
