Now I have all the information I need. Let me construct the final review.

---

## Summary

This paper makes three contributions toward generalizable ML for protein–protein interaction (PPI) design: (1) PPIRef, the largest non-redundant dataset of 3D PPI structures (322K raw, 46K unique), built using (2) iDist, a scalable structural deduplication algorithm achieving 480× speedup over iAlign with 99%/97% precision/recall; and (3) PPIformer, an SE(3)-equivariant transformer pre-trained on PPIRef via masked modeling and fine-tuned for ΔΔG prediction via a thermodynamically motivated log-odds ratio. The model is evaluated on non-leaking splits of SKEMPI v2.0 (5 held-out PPIs) and two case studies (SARS-CoV-2 antibody optimization and staphylokinase engineering), outperforming ML baselines on most metrics.

## Strengths

- **PPIRef dataset and iDist algorithm are substantial community resources.** PPIRef (322K raw structures, 46K unique interfaces) is an order of magnitude larger than DIPS (40K, 9K unique) and MaSIF-search (6K, 5K unique). iDist achieves 480× speedup over iAlign with 99% precision and 97% recall for near-duplicate detection (Section 3.1), enabling deduplication at a scale not previously feasible. These contributions are well-engineered and independently useful regardless of the downstream model's performance.

- **Rigorous identification and quantification of data leakage in prior PPI benchmarks.** Using iDist, the paper shows that 53–88% of test examples in standard DIPS data splits have near-duplicates in the training data (Section 3.2, Figure 2). This analysis directly motivates the non-leaking evaluation splits used in the paper and is a valuable methodological contribution to the field.

- **Principled adaptation of pre-training for ΔΔG prediction.** The log-odds ratio formulation (Eq. 4–5) maps the masked modeling objective to binding energy estimation in a way that mirrors the thermodynamic definition ΔΔG = RT(log K_wt – log K_mut). This physics-motivated loss is conceptually cleaner than prior approaches that either ignore the antisymmetry or require two forward passes (Section 4.4).

- **Competitive results on non-leaking SKEMPI evaluation.** On 5 held-out PPIs with controlled data leakage, PPIformer achieves Spearman 0.44 (±0.03), outperforming all ML baselines on 6 of 7 metrics. The 183% relative improvement over RDE-Network (Spearman 0.24) is notable given that the non-leaking splits likely depress all ML scores relative to prior reported numbers.

## Weaknesses

### Fatal
None. The paper's contributions (dataset, algorithm, model architecture, fine-tuning strategy) are real, and the core claim of improved generalization over ML baselines is supported by the data, albeit with limitations.

### Major

1. **Missing ablations prevent attribution of performance to the claimed innovations.** The paper does not compare PPIformer fine-tuned after pre-training on PPIRef against (a) the same architecture trained from scratch (random initialization) on SKEMPI, (b) fine-tuning with a standard regression head on the [MASK] embeddings instead of the log-odds formulation, or (c) pre-training on DIPS/DIPS-Plus instead of PPIRef. Without these controls, it is impossible to determine whether the observed performance stems from the pre-training, the thermodynamic loss, the larger dataset, or merely the architecture itself. This is the most critical gap: the three main contributions (PPIRef, pre-training, thermodynamic fine-tuning) are asserted as enablers but empirically untested in isolation.

2. **The main evaluation rests on only 5 held-out PPIs with limited statistical characterization.** The central benchmark (Table labeled fig:skempi_test) reports metrics averaged across 5 test complexes, with no per-PPI breakdown. Baseline methods are shown without error bars or confidence intervals. With only five test cases, the observed improvements could be driven by a single favorable complex, and readers cannot assess variability across different PPI families, interface sizes, or mutation types. The paper mentions a "non-leaking cross-validation split" for training but does not report CV-based test performance on the full SKEMPI dataset.

3. **PPIRef/iDist contributions are not causally linked to the generalization claim.** The paper presents PPIRef as a critical enabler of performance, yet runs no experiment showing that pre-training on PPIRef (vs. DIPS or DIPS-Plus) improves downstream ΔΔG prediction. Similarly, the iDist deduplication is used to build PPIRef, but the model is not evaluated on a version of PPIRef that retains near-duplicates to isolate the effect of redundancy removal. The dataset and algorithm are valuable in their own right, but their connection to the generalization claim is asserted rather than demonstrated.

### Minor

1. **Mixed case-study results complicate the generalization narrative.** On the SARS-CoV-2 antibody task, PPIformer detects 2 of 5 favorable mutations in the top 10% (vs. 3 for RDE-Network). The P@1=100% reflects a single correct top-1 hit and overstates practical superiority — the other methods have more high-quality hits in the top 10%. While PPIformer achieves the best mean rank (11.60%) and min-max rank, the results are not unambiguously superior. The paper's own text acknowledges this tension (line 221) but the overall narrative leans harder on the positive interpretation.

2. **The thermodynamic motivation for the log-odds ratio is plausible but not rigorously justified.** The connection between masked-modeling log probabilities and binding free energies (Eq. 2 → Eq. 4 → Eq. 5) is stated as reasoning ("we reason that during pre-training PPIformer learns the correlates of ΔG values") rather than derived from first principles. This does not invalidate the approach — many effective methods in this space are heuristic — but the paper presents it as a physics-informed contribution without testing whether the pre-trained model alone (zero-shot, without fine-tuning) correlates with ΔΔG, which would be a natural validation.

3. **No per-PPI breakdown is reported for the main SKEMPI evaluation.** The reader cannot assess whether PPIformer's average performance is consistent across all 5 test complexes or dominated by easy cases. Given that different PPI families have very different interface geometries and mutation tolerance, this is a meaningful omission.

### Trivial
None.

## Nice-to-Haves

- **Zero-shot evaluation of the log-odds ΔΔG estimate.** Before fine-tuning, the pre-trained model's log-odds ratio could be compared against SKEMPI labels. If the thermodynamic motivation holds, some correlation should be observable without any supervised training. This would significantly strengthen the claim that pre-training captures ΔG correlates.
- **Cross-validation on the full SKEMPI dataset** using the non-leaking split strategy (e.g., 5-fold) would provide more robust estimates and allow per-PPI analysis.
- **A control experiment pre-training on PPIRef vs. DIPS** with identical architecture and fine-tuning protocol would directly validate the dataset contribution.

## Removed Points

These points are flagged to be removed, treat them with caution:

- Critic's claim that "the force-field baseline flex ddG outperforms all ML methods, directly contradicting the narrative that ML generalizes better" — **Removed (strawman):** The paper explicitly acknowledges that flex ddG outperforms ML methods (line 190) and frames "enhanced generalization" as a comparison against *other ML methods*, not force fields. The paper does not claim to beat force fields.
- Critic's claim that the paper "tries to spin" COVID results as superior — **Removed (factually wrong):** The paper's own text (line 221) says "PPIformer is superior in prioritizing favorable mutations among random ones but does not prioritize 5 annotated mutants as high as the DDGPred and RDE-Network models." This is balanced, not a spin.
- Critic's claim that the iDist deduplication analysis of DIPS splits is a "reprint" of the authors' earlier work — **Removed (unverifiable):** The paper cites Bushuiev et al. 2024. Without access to that work, I cannot verify whether this is a reprint or new analysis.
- Critic's claim that "'opens up the possibility of training large-scale foundation models for PPIs' is a generic claim" — **Removed (nitpick):** This is a standard forward-looking conclusion statement, not a technical weakness.
- Critic's claim about "no comparison to alternative self-supervised tasks (denoising, contrastive learning)" during pre-training — **Removed (scope creep):** The paper's contribution is masked modeling with thermodynamic fine-tuning. Demanding a survey of all possible self-supervised tasks is outside the stated scope.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves did not make. The key tension — that the method's components (dataset, algorithm, loss) are individually interesting but not causally validated — is a standard evaluation critique rather than a novel synthesis.

## Suggestions

1. **Add ablation experiments** (pre-training vs. no pre-training, PPIRef vs. DIPS pre-training, log-odds vs. MLP regression head). These three experiments would directly validate or refute the claimed contributions.
2. **Report per-PPI breakdown** for the 5 held-out test complexes in the main SKEMPI evaluation, along with confidence intervals for baselines (e.g., bootstrapping or multiple seeds).
3. **Test the zero-shot log-odds correlation** against SKEMPI labels to validate the thermodynamic motivation.
4. **Tone down the generalization claim** in the title and abstract to match the empirical scope (5 PPIs, mixed case studies), or expand the evaluation to justify the claim.

## Score and Decision

The paper delivers a valuable new dataset (PPIRef) and an efficient deduplication tool (iDist) that are independently useful. The PPIformer architecture and thermodynamic fine-tuning are sensibly designed. However, the core performance claim — that these innovations yield "enhanced generalization" — is not adequately supported: key ablations are absent, the main evaluation is limited to 5 test complexes, and the connection between the dataset/algorithm contributions and the downstream results is asserted rather than demonstrated. The paper would require substantially stronger evaluation (at minimum ablations and expanded test coverage) to make the case credible for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>