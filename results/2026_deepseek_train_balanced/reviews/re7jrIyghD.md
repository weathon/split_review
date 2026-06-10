## Summary

The paper proposes CHIRon, a decoder-only (GPT-style) transformer foundation model for structured sequential medical data (diagnosis codes, procedure codes, medications, lab results, demographics, place of service). Key contributions include: (1) architectural additions for healthcare-specific context (visit embeddings, place-of-service embeddings, age embeddings), (2) three methods for tokenizing continuous lab results, (3) multi-task pre-training with extra prediction heads for place-of-service and age-at-encounter, and (4) a visit-based causal masking scheme. The model is pre-trained on 44M patients and evaluated on five disease classification tasks and a conditional code-continuation task. Classification results indicate CHIRon outperforms Med-BERT, RETAIN, TransformEHR, and GBT on 4/5 tasks.

## Strengths

- **Decoder-only generative FM achieves competitive or superior classification performance against discriminative FMs.** Section 4.1 (Figure 2) shows CHIRon achieves the highest AUROC and AP in 4 of 5 disease classification tasks (CKD, CKD-P, COPD, diabetes) by a statistically significant margin over Med-BERT (BERT-based), TransformEHR (encoder-decoder), RETAIN (RNN-based), and matches GBT on dementia. This is a noteworthy result: a generative architecture does not sacrifice — and can improve — discriminative performance on structured medical sequences.

- **Systematic evaluation of three distinct methods for embedding continuous lab values.** Section 3.1.2 describes three tokenization methods (per-decile bin, embedding scaling with continuous values, shared decile embeddings) with detailed preprocessing (decile computation, exponential tail fitting, outlier removal). Section 4.2 (Figure 3) quantitatively compares them across all five disease outcomes, showing the decile-embedding method significantly outperforms alternatives in 4/5 conditions. This is a methodological contribution beyond what prior FMs (Med-BERT, BEHRT, TransformEHR) provide.

- **Multi-task pre-training (CHIRon+) demonstrably improves generation quality.** Section 4.4 (Figure 5) shows that adding prediction heads for place-of-service and age-at-encounter improves BERTScore and ROUGE-1 across all truncation lengths compared to base CHIRon. This provides empirical evidence that auxiliary clinical prediction tasks benefit generative fidelity for structured medical sequences.

- **Scale of pre-training data.** The model is pre-trained on 44 million patients (Section 3, line 34), which the paper notes is the largest patient dataset used to train a foundation model for structured sequential medical data. For context, Med-BERT was trained on ~28M patients.

- **Novel place-of-service embedding adds clinically meaningful context.** The paper introduces place-of-service embeddings (7 categories: outpatient, inpatient, emergency, custodial, independent lab, home, unknown) and motivates them with a concrete clinical example (Section 3, line 39). This embedding is used in both pre-training and generation, enabling CHIRon+ to generate contextually appropriate service locations alongside medical codes.

## Weaknesses

### Fatal
None.

### Major

- **Generative evaluation lacks any baseline and tests the wrong task.** Section 4.4 evaluates generation by truncating the last T codes from patient records, generating T codes, and comparing to ground truth via ROUGE-1 and BERTScore. The *only* comparison is CHIRon vs. CHIRon+ — an internal ablation. There is no comparison against any other model (not CLMBR, not a simpler n-gram baseline, not a GRU-based model, not even a frequency-based predictor). Without a reference point, the absolute metric values are uninterpretable — the reader cannot tell whether a ROUGE-1 of ~0.3 or a BERTScore of ~0.85 reflects "realistic" generation or poor performance. Furthermore, the truncation task measures conditional *continuation* (next-code prediction given a prefix), not synthetic data generation. The paper motivates generation for "privacy-preserving data sharing" and "synthetic visit sequences" (abstract, line 4), yet evaluates neither distributional fidelity (are generated full trajectories plausible?), downstream utility (do models trained on synthetic data perform comparably?), nor privacy (membership inference, memorization). The stated motivation and the evaluation are misaligned.

- **No numerical results are reported in tables; all key metrics are presented in figure images only.** The classification results (Figure 2), lab embedding comparisons (Figure 3), masking ablations (Figure 4), and generation metrics (Figure 5) are all presented as figure images. The text describes qualitative trends ("statistically significant margin") but does not report exact AUROC/AP/ROUGE/BERTScore values, confidence interval widths, or effect sizes. Given the dataset contains 44M patients, even trivially small differences will reach statistical significance. The reader cannot assess whether improvements are practically meaningful (e.g., a 0.001 vs. 0.05 AUROC gain). For a top venue, numerical results in tables with confidence intervals are expected.

### Minor

- **CLMBR, the most closely related generative foundation model for EHR data, is omitted from all experiments.** The paper acknowledges CLMBR in Section 2 (line 25) as an "auto-regressive Transformer-based foundation model for EHR data" and describes the data regime difference (regularly-sampled daily inpatient data vs. irregularly-sampled longitudinal data). While this difference is real and justifies careful framing, the paper's headline claims about being a "generative FM" for structured medical data would be substantially strengthened by including CLMBR (or a reasonable adaptation) as a baseline for both classification and generation. Without it, the reader cannot assess whether CHIRon advances the state of the art over the only other generative model in the same paradigm.

- **Visit-based causal masking is presented as a contribution but empirically deteriorates performance, with no analysis of why.** Section 4.3 reports that visit-based masking "deteriorated the performance of the fine-tuned models on all of the conditions." The paper offers no investigation into why this happens (e.g., do within-visit code dependencies carry crucial short-term information? does it interact with sequence length?). A negative result can be informative, but requires analysis to be useful to future researchers.

- **The discussion section is one-sided and does not address any limitations.** Section 5 discusses CHIRon's foundation model status and justifies the use of private data, but does not mention the missing generative baselines, the failure of visit-based masking, the scope limitations of the generation evaluation, or any failure cases. Including a limitations paragraph would improve scientific rigor.

- **The weighting scheme for multi-task pre-training is underspecified.** Section 3.2 (line 62) states: "We used fixed weighting based on initial loss value to balance these losses during pretraining." The paper does not specify what the weights were, how they were determined, or how sensitive the results are to this choice.

### Trivial

- ROUGE and BERTScore are NLP text summarization metrics; their validity for evaluating structured medical code sequences (taxonomic proximity, clinical plausibility) is asserted (Section 4.4, line 119) but not independently justified or validated. This is worth noting for the authors to address in revision.

## Nice-to-Haves

- A privacy evaluation (membership inference, nearest-neighbor memorization) would directly support the paper's stated motivation of "privacy-preserving data sharing."
- A human/clinical evaluation of generated sequences (even small-scale clinician plausibility review) would strengthen the generative claims substantially.
- Reporting computational cost (training time, inference speed) relative to baselines would support practical deployment claims.

## Removed Points

*These points were flagged during review synthesis as noise or misreadings. Treat with caution.*

- The claim that CLMBR omission is "structural" and "invalidates the paper's comparative claims" (downgraded from fatal to minor): The paper provides a reasonable justification for the difference in data regime and its comparative claims are specifically against Med-BERT, TransformEHR, RETAIN, and GBT — not CLMBR. CLMBR's absence is a gap but not a claim-invalidating flaw.
- The assertion that GBT being a non-FM baseline undermines the paper: GBT is a standard non-neural baseline; the paper's main comparison is against other FMs. Not a weakness.
- The suggestion that the paper "lacks a Conclusions section": Section 5 (Discussion) serves this role; this is a stylistic preference.
- Criticisms about missing appendix content, missing proofs, or unreleased models: Out of scope or based on parser-stripped content.
- Generic formatting/style nitpicks and reproducibility complaints about missing trivial implementation details.
- The strength finder's generic statements about the "importance of the problem" (removed as superficial).

## Novel Insights

The most interesting tension across the reviews is the asymmetry between the strength of the classification evidence and the weakness of the generative evidence. The paper's central claim is that a decoder-only architecture can serve *both* discriminative and generative purposes for medical sequences, but the evidence for the generative half is substantially weaker — lacking any external baseline and measuring conditional continuation rather than synthetic data quality. This raises an underexplored question for the community: should generatively-pretrained medical sequence models be accepted primarily on the basis of their discriminative performance, with generation as a secondary benefit, or do generative claims require a higher standard of evidence (distributional fidelity, privacy, clinical realism)? The paper implicitly adopts the former view, but the evaluation does not fully test the latter.

## Suggestions

1. **Add at least one non-trivial generation baseline** — a frequency-based next-code predictor, a GRU/LSTM trained on the same data, or a simpler Markov model — to calibrate the ROUGE and BERTScore values. Without this, the generative results are uninterpretable.
2. **Report all key metrics in tables** with exact numerical values and confidence intervals. Figures are complementary, not substitutes.
3. **Reframe the generative claims** to match what is actually evaluated (conditional next-code continuation quality), or add experiments on full-trajectory generation, distributional fidelity, or downstream utility on synthetic data.
4. **Include CLMBR as a baseline** for classification if the data regime can be reasonably adapted, or explicitly scope the claims to clarify why the comparison is infeasible.
5. **Add a limitations paragraph** acknowledging the scope of the generative evaluation, the missing baselines, and the visit-based masking failure analysis gap.
6. **Provide analysis of why visit-based causal masking fails** (e.g., ablation by code type, sequence length, visit structure) so the negative result becomes informative.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>