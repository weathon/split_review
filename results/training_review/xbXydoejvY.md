Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes Channel-Wise Parameter Sharing (CWPS), a method for knowledge transfer that operates at the granularity of individual channels (neurons) rather than layers or individual weights. The key idea is to assign each channel of a new task's model to the most similar channel from previously trained models via a fast nearest-neighbor search (CPMS), then use a learned channel mask to decide which channels to reuse vs. retrain. The method is evaluated on the ImageNet-to-Sketch (MDL) and DomainNet (MTL) benchmarks, and the paper claims state-of-the-art precision-to-parameter ratio among parameter-efficient methods.

---

## Strengths

1. **Novel channel-level sharing granularity fills a genuine gap.** The paper identifies that existing methods share at the layer level (too coarse) or the individual weight level (too fine, breaking neuron atomicity), and proposes sharing at the channel/neuron level as a natural middle ground. Figure 1 clearly illustrates this conceptual distinction, and the design is formalized via a channel mask in Eqs. (6–8). This intermediate granularity is a reasonable and well-motivated contribution.

2. **CPMS is a computationally lightweight search strategy.** The composite parent model searching method (Section 3.2.2, Eqs. 3–5) reduces the search space to a per-channel nearest-neighbor assignment using simple similarity metrics (L2/cosine). This avoids costly learned searches or heuristic enumeration while still enabling fine-grained selection, which directly addresses the granularity-vs-search-space dilemma stated in the introduction.

3. **Strong results on the primary MDL benchmark.** On the ImageNet-to-Sketch benchmark with ResNet-50 (Table 1), among parameter-efficient methods (those using ≤1× backbone parameters), CWPS achieves the highest reported mean Top-1 accuracy (89.0% with 0.7× parameters). The text confirms that only methods using ≥1× parameters (full fine-tuning, Spot-tune) beat CWPS on accuracy, which is expected given they use a full backbone copy per task. This supports the core claim of a superior precision-to-parameter ratio among efficient methods.

4. **Interpretable task relation visualization.** Figure 4 (right) quantifies shared neurons between task pairs, producing intuitively sensible patterns (e.g., Sketch–Flowers stronger than Cars–Flowers, all tasks most related to ImageNet). This is a useful diagnostic that emerges naturally from the method.

---

## Weaknesses

### Fatal
None.

### Major

1. **The key hyperparameter λ is never defined.** The entire ablation study (Table 3, Figure 5) centers on varying λ from 1 to 0 and analyzing its effect on the accuracy-parameter trade-off, but λ is never introduced or defined anywhere in the paper — not in Section 3 (Methodology), not in the loss function, not in the mask optimization procedure. There is no loss/objective function formalized at all. The reader cannot tell whether λ is a mask sparsity regularizer, a weight on a regularization term, a threshold for binarization, or something else. This renders the central ablation study uninterpretable and the method non-reproducible. **This is the most impactful weakness and must be addressed for the paper to be considered publishable.**

2. **Critical training and implementation details are missing, harming reproducibility.** 
   - The "soft mask training stage" and "hard mask training stage" are mentioned (Section 3.2.3) but never described: how is the mask initialized, optimized (gradient-based or binary), or transitioned from soft to hard? 
   - No hyperparameters are reported: total training epochs, learning rate, batch size, optimizer, or weight decay. The search phase is said to use "one-quarter of the total training epochs" (line 108) but the total is never stated for any dataset. 
   - The similarity function D is said to use "L2 distance and cosine similarity in practice" (line 121) but it is never specified which was used in the reported experiments or how they were combined. 
   - These gaps prevent independent verification and replication.

3. **The "plug-and-play" claim is overstated.** The method requires (a) a pre-trained parent model, (b) a search phase computing channel-wise similarity against all previously trained models, and (c) a mask vector per layer per task that adds parameters during training. The search cost scales linearly with the number of tasks and channels, and the method has no clear application when no prior model exists (e.g., training all tasks from scratch). Calling this "plug-and-play" overstates its generality.

### Minor

4. **Limited baseline comparisons on DomainNet multi-task benchmark.** On DomainNet (Table 2, bottom), the only quantitative comparison is against AdaShare. While the paper's main focus is MDL (where the baseline set is adequate), the claim of state-of-the-art in multi-task learning would be strengthened by comparisons against Cross-stitch Networks, NDDR-CNN, MTAN, or other standard MTL methods.

5. **Statistical uncertainty is not reported.** All results are presented as single point estimates without standard deviations or confidence intervals. While single-run evaluations are common practice in this benchmark setting, the absence of any variance information makes it impossible to assess whether the reported improvements over baselines are significant.

6. **Inference speed claim is unverified.** The paper asserts (Section 3.2.3) that "CWPS would not reduce the inference speed compared to fine-tuning" based on the reasoning that masks can be folded into weights. The reasoning is sound in principle, but no wall-clock time, throughput, or FLOPs comparison is provided. This central practical claim needs empirical support.

7. **The iterative joint learning selection criterion is underspecified.** Algorithm 1 (parser-stripped) is referenced but the text states only that "we replace the weights from the worst model in W_trained" (line 167) without operationalizing how "worst" is determined (lowest validation accuracy? a combined metric?).

### Trivial

8. **The similarity metric ambiguity** (L2 vs. cosine — line 121) is a small presentational issue but should be resolved with a clear specification.

---

## Nice-to-Haves

- Reporting results with multiple random seeds (3 runs) with mean and std would significantly strengthen the evaluation.
- A wall-clock time comparison (e.g., inference throughput in images/sec for CWPS vs. fine-tuning) would substantiate the practical efficiency claim.
- Extending the DomainNet comparison to include more standard MTL baselines would broaden the paper's impact.
- An analysis of how robust the CPMS search is to the quality of the reference child model (trained for only one-quarter of epochs) would be valuable.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Missing comparison against weight-level methods like Piggyback"* — The paper includes PackNet (from the same Mallya et al., 2018 paper) in Table 1 as a weight-level baseline, and cites the weight-level family. The omission of Piggyback by name is not a significant gap.
- *"Missing appendix/Algorithm 1"* — The parser strips these; they exist in the original submission.
- *"No comparison against MoE-based or prompt-based methods on benchmarks"* — Section 5 provides qualitative discussion of these families and explicitly scopes the paper's quantitative scope to parameter-efficient sharing, not all possible MTL approaches. Criticizing this absence is scope creep.
- *"PackNet comparison is insufficient"* — PackNet is a weight-level method and is included in Table 1. The comparison set is adequate for the MDL setting.
- *"The search cost is not analyzed"* — The paper states the search is "a trivial cost" (line 108) and uses only one-quarter of training epochs. The criticism demands a formal complexity analysis that is not standard for this type of work.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Define λ explicitly** in the methodology section: state what it controls (e.g., whether it is a coefficient in a loss function like `L = L_task + λ * ||mask||_1`, a sparsity threshold, or something else), how it interacts with the mask, and why values 0–1 are the meaningful range.
2. **Provide a complete training specification** for all benchmarks: number of epochs (and the total from which "one-quarter" is derived), learning rate schedule, optimizer, batch size, and data augmentation details beyond random horizontal flip.
3. **Describe the mask training pipeline** (soft-to-hard transition): initialization scheme, whether the mask is trained with straight-through estimators, Gumbel-softmax, or another technique, and how the hard mask is derived.
4. **Clarify which similarity metric** (L2, cosine, or a combination) was used for each reported experiment and justify the choice.
5. **Add wall-clock inference speed measurements** to support the "no speed degradation" claim, or at minimum a FLOPs comparison between the folded-weight version and standard fine-tuning.

---

## Score and Decision

The paper proposes a genuinely interesting intermediate granularity for parameter sharing and demonstrates competitive results on a standard MDL benchmark. However, the omission of λ from the methodological description is a serious flaw — it makes the ablation study (Table 3, Figure 5) uninterpretable and undermines the paper's completeness. When combined with the missing training details that impede reproducibility and the overstated "plug-and-play" claim, the paper cannot be accepted in its present form. The core ideas have merit and the issues are fixable, but a major revision with full specification of λ, the training pipeline, and missing hyperparameters is needed before the paper can be fairly evaluated.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>