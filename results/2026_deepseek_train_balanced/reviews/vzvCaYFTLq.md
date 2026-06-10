## Summary

Sapling proposes compressing LLMs for domain-specific deployment by iteratively dropping decoder layers during fine-tuning. The method uses a calibration-scanning importance score (and optionally an activation-norm tiebreaker) to decide which layer to drop after each epoch, combined with a sparse update scheme that only trains layers likely to be retained. Evaluated on LLaMA-7B across medical, legal, and financial QA tasks, Sapling shows that substantial depth reduction (40–50% of original parameters) is possible while retaining ≥90% of fine-tuned accuracy, with measured wall-clock speedups on a V100 GPU.

## Strengths

1. **Measured wall-clock inference speedup from depth reduction without specialized kernels.** Table 1 demonstrates that Sapling achieves real inference speedup (overhead ratio 0.37 at 40% size) on a V100 GPU, whereas LLM.int8() (2.17×) and GPTQ (1.83×) are *slower* than the FP16 baseline on the same hardware due to missing efficient kernels. This is a genuine practical differentiator: depth reduction gives a "guaranteed" speedup on any hardware without requiring kernel support, unlike precision reduction.

2. **Sparse update scheme is validated as a genuine improvement.** Table 3 shows that updating all layers (r=1) consistently produces worse compression results than sparse update at r=1/4 across all target-selection methods. The best variant (calibration scan + activation-norm tiebreaker, r=1/4) reaches ~50% model size while maintaining ≥90% of full fine-tuning accuracy. This ablation directly supports the methodological design choice and is non-obvious.

3. **Empirical evidence for layer-wise specialization across domains.** Figure 3 shows that different tasks (SciQ, MedMCQA, LexGLUE, FinanceQA) produce measurably different layer-dropping patterns, and more MLP layers are dropped than attention layers across all tasks. Table 4 further shows that domain-specialized models perform worse on out-of-domain tasks. While these observations are not as strong as claimed (see Weaknesses), they provide reasonable evidence that the model's layers are not equally important across domains.

4. **Flexible Pareto frontier of operating points.** Figure 2 shows that Sapling offers a continuous spectrum of size/accuracy trade-offs (one per dropped layer), whereas quantization provides only discrete bit-precision levels. This is a practical advantage for fitting models to heterogeneous hardware constraints.

## Weaknesses

### Fatal
None.

### Major

1. **Section 3.1 ("Preliminaries and Layer-Wise Specialization") is empty.** The paper's roadmap (line 55) promises that this section presents "our hypothesis and empirical evidence concerning the existence of layer-wise specialization." Instead, the section (lines 59–62) contains only two sentences — one stating the obvious (decoder blocks have MHA and MLP layers) and one fragment that ends mid-sentence with "Based on observations and findings." No hypothesis is stated, no preliminary evidence is presented, and the empirical results that should anchor this section (Figure 1a, layer-dropping curves) appear in the introduction rather than here. This is a structural gap in the paper's logical flow, as the claimed empirical foundation for the method is missing from the Methods section where it is promised.

2. **Missing critical baseline: comparison against a smaller pre-trained model.** Sapling compresses LLaMA-7B by reducing depth. The most natural baseline is a smaller pre-trained model (e.g., LLaMA-3B, TinyLLaMA, or a 3B-class model) fine-tuned on the same domain data. If a 3B model fine-tuned on the same data matches or exceeds the performance of Sapling-compressed LLaMA-7B at comparable inference cost, the core value proposition is substantially weakened. This baseline is entirely absent, making it impossible to assess whether the method provides advantages beyond what is achievable with a smaller model from the same family.

3. **The "knowledge localization" claim is overclaimed relative to the evidence.** Contribution 1 states the paper "observe[s] and empirically verif[ies] the layer-wise knowledge localization phenomenon." The supporting evidence (Table 4, Figure 3) is insufficient for this strong claim:
   - **Table 4** shows cross-domain performance degradation, but the specialized models have different numbers of remaining parameters (e.g., SciQ model at 40% vs. MedMCQA model at 50%). Without controlling for total parameter count, the degradation could simply reflect smaller models being less capable, not that specific dropped layers encoded domain-specific knowledge.
   - **Figure 3** shows different tasks produce different dropping patterns, but this is also consistent with different tasks simply benefiting from different amounts of retained capacity.
   
   The paper never directly tests whether the *identity* of the dropped layers (vs. the *number*) determines which out-of-domain tasks are most affected. The weaker claim — that layers are not equally important across tasks — is supported; the stronger "knowledge localization" framing is not uniquely justified by the data.

### Minor

1. **Activation-norm importance metric rests on questionable theoretical grounds.** The paper claims (line 98) that "activation tensors with higher entry-wise matrix norm generally have higher ranks" and uses Frobenius norm as a proxy for rank to identify layers to drop. This is not a general mathematical truth — a rank-1 matrix with a large singular value can have a very high Frobenius norm, while a full-rank matrix with small entries can have a low Frobenius norm. The metric therefore does not reliably distinguish "high-rank representations with sparse domain-specific knowledge" from layers that simply have large activations. **However**, this metric is only used as a tiebreaker in the "both" method, and the primary calibration-scanning method is unaffected. The impact is limited, but the theoretical justification as written is unsound and should be corrected or removed.

2. **No statistical variance or confidence intervals reported for any result.** All accuracy numbers are reported as point estimates with no indication of stability across calibration splits, random seeds, or multiple runs. Given that calibration-set sampling introduces stochasticity into layer-selection decisions, it is impossible to assess whether observed differences between methods (e.g., between calibration-scanning alone vs. the combined method in Table 3) are meaningful. This is standard practice for large LLM experiments but remains a limitation.

3. **Train-test mismatch for FinanceQA evaluation.** The model is fine-tuned on FinanceQA (described as combining FiQA, Stanford-Alpaca, and ChatGPT QA dialogues) but evaluated on the "economics" subset of MMLU. The paper does not discuss whether MMLU economics questions overlap with the training data or what the relationship is between the training mixture and this evaluation set. This makes the reported accuracy numbers difficult to interpret.

4. **Time complexity claim (line 77) oversimplifies the cost.** The paper states that fine-tuning complexity increases from O(1) to O(N) where N is the number of layers dropped. In practice, each drop requires scanning *all remaining layers* on the calibration set, leading to O(L·N) total forward passes (L = initial layer count), which in the worst case approaches O(L²). While the practical cost is small given LLaMA-7B's 32 layers, the complexity statement as written is misleading and should be corrected.

5. **δ parameter in Equation 3 is introduced but not ablated or discussed.** The calibration-scanning score (Equation 3) includes a tunable parameter δ, described as "a small positive number." Its chosen value, sensitivity, and effect on rankings are never discussed. If δ is not meaningfully used, it should be removed; if it is, its impact should be analyzed.

6. **"Proposition 1" (line 75) is mislabeled.** The statement is a design heuristic (drop layers one at a time to enable gradual adaptation) rather than a proposition in the formal sense — it is not stated with formal rigor, not proven, and not used for deductive reasoning. This is a presentational issue.

### Trivial
- Section 3.1 heading promises content that is not delivered (this overlaps with Major weakness 1 above).
- The paper uses "Forbenius" (line 100, 101) instead of "Frobenius."

## Nice-to-Haves
- Compare Sapling against quantization methods *with their intended efficient kernels* on hardware that supports them (e.g., AWQ with INT4 kernel on an A100). This would make the comparison more complete, though the paper's current framing (consumer hardware without kernel support) is a valid and transparent use case.
- Add a controlled experiment for Table 4 where cross-domain degradation is compared between models with the *same* number of remaining parameters but different dropped-layer identities, to more directly test the knowledge localization claim.
- Report variance or confidence intervals for the main results to improve reproducibility assessment.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's claim that the quantization comparison is "staged to make Sapling look maximally favorable."** The paper explicitly acknowledges the kernel dependency in both the abstract and introduction (lines 12–13, 27). The comparison is performed under the paper's stated conditions (consumer-level hardware where efficient kernels are unavailable), and the transparency about this context means the framing is not deceptive. The missing smaller-model baseline (retained in Major weakness 2) is a separate, valid concern.
- **Harsh critic's claim that Section 3.3's activation-norm argument is "faulty theoretical premise" at the "Structural" level.** The criticism of the Frobenius norm / rank relationship is factually correct, but since the metric is only a tiebreaker and the calibration-scanning method carries the main weight, this does not rise to a structural/fatal issue. Demoted to Minor weakness 1 above.
- **Harsh critic's claim that the paper "runs without their optimized kernels" constitutes a fatal flaw in the evaluation.** The paper is transparent about this limitation and explicitly frames its contribution around hardware-independent speedup. The comparison is appropriate for the claimed use case, though adding the kernel-enabled comparison would strengthen it (Nice-to-Have above).
- **Strength Finder's claim that different layer-dropping patterns "provide concrete empirical evidence for the 'layer-wise knowledge localization' claim."** This overstates what the data show. Table 4 does not control for model size, and the patterns in Figure 3 are consistent with simpler explanations. Kept as Strength 3 but downgraded from "core strength" framing to "supporting evidence" — the weakness (Major 3) notes the overclaim.

## Novel Insights

Beyond the paper's own contributions, the reviewers did not surface a genuinely novel insight. The observation that the Frobenius norm does not reliably indicate rank (used to weaken the activation-norm justification) is a standard mathematical fact, not a new finding about Sapling specifically. The missing comparison against smaller pre-trained models is an evaluation gap that the authors should address, not an insight.

## Suggestions

1. **Add the missing smaller-model baseline** (e.g., LLaMA-3B, TinyLLaMA, or OpenLLaMA-3B fine-tuned on the same domain data). This is the single most important missing piece. If Sapling's compressed 7B model outperforms a comparably-sized 3B model, the paper's value proposition is much stronger.
2. **Either fill Section 3.1 with the promised empirical evidence or restructure the paper** so that the experimental results in the introduction (Figure 1a) are properly contextualized and the "layer-wise specialization" hypothesis is stated and tested within the Methods section.
3. **Replace the activation-norm tiebreaker with a simpler alternative** (e.g., gradient-based importance, random tiebreaking) or provide a sound theoretical basis. The current justification is mathematically questionable and adds little value given that calibration scanning is the primary method.
4. **Tone down the "knowledge localization" claims** to match what the data actually support: that layers contribute unequally across tasks, and that dropping task-specific layers during fine-tuning can produce effective compressed models.
5. **Disclose the chosen δ value** in Equation 3 and evaluate its sensitivity, or remove it if it has no meaningful effect.
6. **Report results with variance across at least 2–3 runs** or explain why single-run reporting is sufficient for the claims made.

## Score and Decision

The core idea — successive layer dropping during fine-tuning with a sparse update scheme — is sensible and has practical merit. The paper shows real wall-clock speedups on hardware where quantization methods struggle, and the sparse update ablation is cleanly validated. However, the paper as presented has significant issues: the Methods section has a structural gap where promised foundational evidence is missing (Section 3.1 is effectively empty), the evaluation lacks a critical baseline (smaller pre-trained models), and the "knowledge localization" framing overclaims what the data show. For a top-tier venue, these gaps are too substantial to ignore.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>