Here is the consolidated review:

---

## Summary

LegoMT2 proposes a training framework for massive multilingual NMT that combines (1) data grouping by language-centric size, (2) a multi-way detachable encoder-decoder architecture (one local module per group + one shared global module), and (3) asynchronous federated learning with PUSH/MERGE/PULL operations. The paper claims a 16.2× training speedup over distributed training for a same-size NLLB model and reports a 2.2 spBLEU gain over a fine-tuned NLLB-200-1.3B baseline on Flores-101, supporting 435 languages and 22k directions.

## Strengths

- **Clear translation quality improvement on Flores-101**: LegoMT2 outperforms Single-FT (NLLB-200-1.3B fine-tuned on the same data) by 2.2 spBLEU on many-to-one and 2.5 spBLEU on one-to-many translation (Table 1). This is a credible, fairly-controlled comparison that demonstrates the benefit of the multi-way architecture for reducing parameter interference.

- **Unprecedented language coverage**: The system supports 435 languages and 22,613 translation directions, exceeding all existing open-source MNMT systems. Even with the limited evaluation (86 languages via Flores-101, plus back-translation samples), this coverage is a genuine scaling achievement.

- **Inference-efficient architecture**: Training uses 10.4B parameters (9 encoder-decoders + shared embeddings), but inference uses only the 1.6B global encoder-decoder. This separation of training and inference capacity is practical and well-motivated.

- **Evidence that asynchronous updates do not degrade quality**: The analysis (Figure 2) shows that using delayed global parameters from other clients does not harm inference performance, providing empirical justification for the non-blocking design.

- **Principled language grouping validated experimentally**: The paper compares data-size-balanced grouping against similarity-based (KMeans) and random clustering (Table 5), showing that balanced grouping yields better performance — a useful empirical finding.

## Weaknesses

### Fatal
None.

### Major

- **The 16.2× speedup claim is completely unsubstantiated.** The paper states this number in the abstract, introduction, and conclusion as a central contribution, yet the experimental section (§4) contains *no wall-clock training times, no GPU-hour counts, no throughput measurements, no convergence-speed comparison (e.g., steps to target BLEU), and no comparison to any distributed training baseline*. Table 1 and the entire §4 focus exclusively on translation quality. §5 discusses asynchronous training qualitatively (delayed parameters, save/load intervals) but never quantifies the claimed speedup. A claim this prominent — "16.2× faster than the distributed training method for the same-size NLLB" — must be backed by concrete, reproducible efficiency measurements. Its absence means the paper's primary claimed advantage is unverifiable. This is the single largest flaw in the paper.

- **Missing ablations that isolate the contribution of each component.** The paper combines three design elements: language grouping, the multi-way architecture, and the asynchronous federated learning algorithm. Yet there are no experiments that:
  - Train the multi-way model with *synchronous* aggregation (to measure the effect of asynchrony),
  - Apply the same asynchronous FL to a *standard single model* (to measure the effect of the multi-way architecture),
  - Train the multi-way model *without the global module* (to measure the value of global sharing).
  
  The ablations that do exist (grouping strategies, save/load intervals, Dec-Flow) are useful but do not isolate these fundamental design decisions. Consequently, it is impossible to attribute the 2.2 BLEU gain to any specific component of the proposed framework.

### Minor

- **The 435-language quality evaluation is weak.** Only 86 languages are covered by Flores-101 (the standard benchmark). For the remaining ~350 languages, the paper relies on a back-translation metric (Back-spBLEU) but shows results for only a few exemplary language pairs (Table 2) — no aggregate statistics over language groups, no systematic coverage analysis. The claim of supporting 435 languages at useful quality is not rigorously validated.

- **The Back-spBLEU metric description is confusing and non-standard.** The paper states "Lower S-T and higher S−S_b are better" (Table 2 caption). In standard evaluation, S-T (src→trg) BLEU should be *high* for good translations. The paper's justification — "to avoid counting direct copies" — makes sense as an intuition (a model that copies source to target would have artificially high S-T), but the framing is incoherent and needs a clearer explanation with quantitative evidence that the model is not simply copying.

- **No experiment disentangling pre-training from the proposed framework.** Both global and local parameters are initialized from NLLB-200-1.3B. Without an ablation using random initialization (or comparing to a standard Transformer of similar size trained from scratch on the same data), it is unclear how much of the 2.2 BLEU gain comes from the proposed framework versus the quality of the pre-trained initialization.

- **The α and β interval specification is inconsistent.** In §4.1, α and β are given as "6 and 12" without units. In §5, they are specified as "10min and 20min" / "20min and 40min" — different values with explicit units. This makes it impossible to determine the actual configuration used for the main results.

### Trivial

- The language grouping example in §3.2 contains overlapping data instances across clients (e.g., Fr→Nl appears in both D_S1 and D_S3). While the paper correctly states that *language sets* are disjoint (S_i ∩ S_j = ∅), the relationship between language sets and data instances is not clearly explained, which could confuse readers.

## Nice-to-Haves

- Compare training throughput or wall-clock time against a standard distributed training baseline (e.g., fairseq's built-in data-parallel training) on the same 64 A100 GPUs to ground the 16.2× claim.
- Report aggregate Back-spBLEU statistics (mean, variance) over all 8 language groups or a random sample of language directions.
- Discuss how vocabulary expansion (256K→490K via per-language BPE merging) affects coverage and how overlapping token embeddings are transferred.
- Include convergence curves (BLEU vs. training steps or time) to demonstrate training efficiency.
- A comparison to a standard Transformer of similar inference size (1.6B) trained from scratch on the same data would further isolate the benefit of NLLB initialization.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength: "16.2× training speedup"** — Removed because it conflicts with the verified weakness that this claim is completely unsubstantiated in the paper. A strength and verified weakness disagree; the weakness wins.
- **Criticism about human evaluation results not being presented** — Removed because the human evaluation description cuts off mid-sentence (line 173), strongly suggesting the actual results table was in the appendix, which the parser strips. Following the missing-appendix rule, this is not a valid criticism of the submission.
- **Criticism about "missing related works" (Megatron-LM, DeepSpeed)** — Removed per the rule that missing-related-work criticisms should not be included without external confirmation.
- **Criticism about NLLB baselines not being fine-tuned** — Partially removed/downgraded. The paper explicitly designates Single-FT (fine-tuned NLLB-200-1.3B) as the fair baseline, so the critic's claim that "the only fair baseline is Single-FT" actually confirms the paper's own approach. The NLLB-200-54.5B comparison is shown as reference but not used as the primary baseline.
- **Criticism about Table 5 / Table 4 being missing** — Removed as a parser artifact (the tables are images that could not be rendered in the plain-text extraction).
- **Strength about "large efficiency gains" / 16.2× from Strength Finder** — Already addressed above; removed due to conflict with verified weakness.

## Novel Insights

The most interesting observation from the reviews is the disconnect between the paper's two central claims. The translation quality improvement (2.2 spBLEU) is well-supported and represents a genuine contribution: it shows that a multi-way architecture + federated learning can outperform standard fine-tuning of the same base model. The efficiency claim (16.2×), however, is presented as a headline result without any supporting measurements, which is unusual and suggests either that the efficiency analysis was deferred to an appendix (which cannot be assumed to exist) or that the number was computed under assumptions that are not disclosed. Beyond this, the reviews do not surface a novel insight that goes beyond the paper's own contributions.

## Suggestions

1. **Provide direct efficiency measurements.** Report wall-clock training time, GPU-hours, and/or throughput (sentences/second) for LegoMT2 versus Single-FT and versus a distributed data-parallel baseline trained on the same compute budget. State the exact resource configuration and how the 16.2× number was derived. Without this, the core claim of the paper is unsupported.

2. **Add ablations isolating the three components.** The most informative experiments would be: (a) multi-way model + synchronous aggregation, (b) single model + the same asynchronous FL procedure, (c) multi-way model without the global module. This would directly attribute the 2.2 BLEU gain and would also provide indirect evidence about whether the speedup is plausible.

3. **Clarify the back-translation evaluation.** Either adopt a standard round-trip metric with a clear explanation, or replace the "lower S-T is better" framing with a more conventional comparison (e.g., reporting both S-T and S-S_b with the explanation that comparable S-T scores rule out copying). Report aggregate Back-spBLEU across all language groups.

4. **Fix the α/β inconsistency** and specify units throughout.

## Score and Decision

This paper tackles an important problem and demonstrates a real improvement in translation quality (2.2 spBLEU) at unprecedented language coverage (435 languages). The multi-way architecture + asynchronous FL combination is a sensible approach worth investigating. However, the paper suffers from a critical evidentiary gap: its headline contribution — a 16.2× training speedup — is stated as fact in the abstract, introduction, and conclusion but is completely unsubstantiated in the experimental section. Missing ablations further prevent attribution of the quality gains to specific design decisions. These are structural issues that cannot be resolved in a short rebuttal.

The paper has real contributions (the quality improvement and coverage are credible), but in its current form, the unsubstantiated central claim and missing ablations make it unsuitable for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>