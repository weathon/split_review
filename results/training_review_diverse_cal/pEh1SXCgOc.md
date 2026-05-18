Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes DCoND, a divide-and-conquer framework for decoding attempted speech from neural activity. The key idea is to model phoneme distributions by marginalizing over diphone (two-phoneme) probabilities, motivated by neuroscientific evidence that neural representations of phonemes are context-dependent. Combined with an LLM-based ensembling step that feeds both phoneme and transcription candidates to GPT-3.5 (via ICL or fine-tuning), the method achieves 5.77% WER on the Brain-to-Text 2024 benchmark — a substantial improvement over the previous SOTA of 8.93% (LISA). The paper includes controlled ablations isolating the contribution of diphone marginalization, the loss weighting, and each LLM component.

## Strengths

1. **Neuroscientifically motivated and empirically validated approach.** The paper grounds its method in coarticulation evidence (Bouchard et al., Mugler et al.) and supports it with t-SNE visualizations (Fig. 4A) showing neural activity clusters by preceding phoneme context. This provides a clear motivation for why diphones (context-dependent units) should improve over monophone decoding.

2. **Clear empirical isolation of the diphone marginalization contribution.** DCoND-L achieves PER 15.34% vs. 16.62% from monophone-based NPTL (Table 1) using the same backbone RNN and language models. The α-ablation (Table 3) shows α=0.6 (combined loss) outperforms α=1.0 (pure monophone, matching NPTL's 16.62% PER). This directly supports the claim that the divide-and-conquer strategy, not architectural differences, drives improvement.

3. **Large and well-ablated WER improvement from the LLM pipeline.** DCoND-LIFT achieves 5.77% WER vs. 8.93% from LISA (Table 1). The step-wise ablation in Figure 5 transparently decomposes contributions: 5-gram → +OPT rescoring → +ICL GPT-3.5 (at 5/15/25 exemplars) → +fine-tuned GPT-3.5 w/ and w/o phoneme inputs. The DCoND-LIFT w/o P (no phoneme inputs) vs. DCoND-LIFT (with phoneme inputs) comparison directly validates the claim that including phoneme sequences in the LLM ensemble helps.

4. **Systematic exploration of alternative context representations.** The paper tests triphone with K=50/100/200 and a pronunciation-similarity grouping baseline (Table on alternative subclasses). DCoND-L (diphone) achieves the best WER (8.06%) while all triphone variants yield higher WERs (9.67–13.98%), validating diphones as the "sweet spot" between context richness and class manageability.

5. **Practical ICL alternative.** DCoND-LI achieves 7.29% WER with 25 in-context examples, offering a resource-efficient alternative to fine-tuning that may be valuable in deployment scenarios where API fine-tuning is infeasible.

## Weaknesses

### Major
None. The core claims are supported by controlled experiments, and no structural flaw invalidates the results.

### Minor

1. **Missing α=0.0 (pure diphone loss) ablation in the combined loss study.** The α sweep (Table 3) ranges from 0.2 to 1.0 but omits α=0.0. Since the paper claims the combined loss is optimal, the condition with zero monophone loss weight is the most direct test of whether the diphone objective alone suffices. The α=0.2 condition (PER 15.64, WER 8.47) already performs worse than α=0.6, suggesting some monophone loss helps, but without α=0.0 we cannot assess the full range. The authors should clarify whether α=0.0 was tested and, if so, report it.

2. **Rationale for the combined loss and α schedule is underspecified.** The paper states that α "is designed to be small at the beginning and gradually increase over the course of training" but does not explain *why* this schedule is chosen or what each loss term contributes. Since the monophone probabilities are a deterministic marginalization of the diphone outputs, the two CTC losses (diphone targets vs. monophone targets) provide different alignment supervision — this dynamic is not discussed. A brief principled explanation would strengthen the methodological contribution.

3. **LLM fine-tuning details not reported, limiting reproducibility.** The most performant variant (DCoND-LIFT, 5.77% WER) relies on fine-tuning GPT-3.5, but the paper does not report fine-tuning hyperparameters (learning rate, number of steps/epochs, prompt template format, number of training examples used, API version). For a contribution explicitly naming the LLM strategies, these details are necessary for reproducibility. The ICL variant's exemplar count analysis (Figure 5) is also limited to three data points (5, 15, 25), so we cannot assess whether performance saturates at 25 or could improve further.

4. **No limitations or generalizability discussion.** The paper lacks a limitations section. The Brain-to-Text 2024 benchmark is a single-subject dataset (Section 4.1: "a human subject with ALS"). This is standard and appropriate for clinical BCI research, but readers outside the field should be explicitly informed that results are demonstrated on one individual and may not generalize to other subjects with different electrode placements or disease progression. The absence of error bars or confidence intervals also makes it difficult to assess trial-level variability, though this is common practice for this benchmark.

5. **Triphone grouping ablation is underspecified.** Table 4 includes a "Grouping" condition that performs significantly worse (PER 28.55, WER 13.98), but the paper does not describe how phonemes were grouped by "pronunciation similarity" — e.g., whether this was based on articulatory features, IPA tables, or an automated clustering. Without this information, the result is difficult to interpret or reproduce.

6. **Architecture-independence claim is not empirically tested.** The paper states that the divide-and-conquer strategy is "adaptable to various decoder architectures" and could be interchanged "without the need for adaptations," but all experiments use only a GRU decoder. While the paper notes that GRU was found optimal for this benchmark, the architecture-independence claim would be stronger with at least one alternative architecture tested.

### Trivial

- The t-SNE visualizations (Fig. 4C, 4D) are presented qualitatively. A quantitative cluster metric (e.g., Silhouette score, within-cluster variance) would strengthen the visual argument that diphone latent space is more condensed and separable than monophone latent space.
- The P-WER metric is reported only for NPTL and DCoND-L but not for LLM-refined variants. A brief note explaining why would be helpful.

## Nice-to-Haves

- A brief analysis of how ICL performance varies with more than 25 exemplars (potentially using a model with a longer context window) would strengthen the ICL story.
- An explicit statement about how the 10 transcription candidates are selected from the N-best list of the 5-gram + OPT rescoring step would improve clarity.
- Reporting model size and inference latency would help practitioners assess the practical trade-offs of the full pipeline.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism questioning single-subject generalizability as a fatal flaw.** The reviewer framed this as a severe limitation undermining SOTA claims. However, the Brain-to-Text 2024 benchmark is inherently a single-subject benchmark, and all prior work (NPTL, LISA) is evaluated on the same subject. This is standard practice in clinical BCI research where collecting multi-subject neural data is extremely difficult. The paper's SOTA claims are correctly scoped to this benchmark. The *absence* of a limitations section is kept as a minor weakness (see above), but the evaluation being single-subject is not itself a flaw.

- **Criticism that the architecture-independence claim is fundamentally unsubstantiated.** The paper explicitly acknowledges GRU was identified as optimal for this benchmark and notes "as further datasets become available the neural decoder is interchangeable." The claim is appropriately hedged. I retain a weakened version as a minor weakness (the claim could be more strongly tested) rather than a major issue.

- **Criticism that no statistical significance is reported.** Lack of confidence intervals is common practice for large-scale benchmark evaluations in this domain where single-run evaluation is the norm. Retained as a trivial point.

- **Strength Finder's generic strength framing** ("this paper addressed an important problem") — dropped as too generic.

## Novel Insights

The most interesting finding that goes beyond the paper's own claims is the asymmetry between PER and WER improvements across context representations. Triphone achieves PER comparable to diphone (15.02% at K=100 vs. 15.34%) but substantially worse WER (9.67% vs. 8.06%). The paper attributes this to distribution mismatch with the downstream 5-gram model, but this raises a broader question for the field: improvements in phoneme-level decoding may not linearly translate to word-level accuracy because the language model was trained on monophone distributions. This suggests that the *interface* between the neural decoder and the language model — not just each component in isolation — is a critical design dimension that the divide-and-conquer framework partially addresses by keeping the output space as monophones.

## Suggestions

1. Report the α=0.0 (pure diphone loss) condition in the ablation to complete the sweep and strengthen the combined loss story.
2. Add a limitations section explicitly discussing single-subject evaluation, the absence of cross-validation, and the dependency on GPT-3.5 API.
3. Provide LLM fine-tuning hyperparameters (learning rate, number of steps, prompt template, training set size) in the main text or supplement.
4. Describe the triphone "grouping" method and/or add a brief explanation of the grouping criteria.
5. Add confidence intervals or error bars to the main results if trial-level variance estimates are available.

## Score and Decision

The paper presents a well-motivated, clearly ablated contribution that achieves substantial improvements on a challenging benchmark. The core weaknesses (missing ablation condition, underspecified LLM details, no limitations discussion) are addressable in a minor revision and do not threaten the validity of the main results. The work should be accepted.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>