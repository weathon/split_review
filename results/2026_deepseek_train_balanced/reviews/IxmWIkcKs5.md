Here is my consolidated final review.

---

## Summary

This paper proposes Light-DDG, a lightweight ΔΔG (binding free energy change) predictor that combines knowledge distillation from heavier predictors with supervised pre-training on a large-scale augmented mutation dataset (SKEMPI-Aug, 670k samples). The authors then wrap Light-DDG into Uni-Anti, a framework for antibody optimization guided by iterative Shapley-value-based mutation explanations and efficient search. Experiments show that Light-DDG achieves a 89.7× inference speedup over the state-of-the-art Prompt-DDG while simultaneously improving per-structure Pearson correlation by 15.45% on the SKEMPI v2.0 benchmark.

## Strengths

1. **Simultaneous large speedup and accuracy improvement**: Light-DDG achieves a measured 89.7× inference acceleration over Prompt-DDG *while* improving per-structure Pearson by 15.45% and Spearman by 17.55% (Table 2, Fig. 1). This simultaneous advance on both efficiency and effectiveness is the paper's strongest empirical result.

2. **Student outperforms its teacher across diverse architectures**: Fig. 5(a) shows that the distilled Light-DDG student outperforms multiple different teachers (Prompt-DDG, RDE-Network, ProMIM, DiffAffinity) regardless of which predictor is used as teacher. This holds even when neither teacher nor student is pre-trained on SKEMPI-Aug, demonstrating that distillation itself provides a consistent boost beyond any single architecture.

3. **K-fold cross-augmentation strategy prevents label leakage**: Section 4.1 and Fig. 2 describe a protocol where SKEMPI v2.0 is split into K folds and a fresh teacher is trained on K−1 folds to annotate the held-out fold. This explicitly prevents the teacher from annotating data it was trained on — a known failure mode in self-training/distillation pipelines that prior work does not address.

4. **Comprehensive ablation isolates component contributions**: Table 4 separately ablates knowledge distillation and data augmentation, showing each alone improves over Prompt-DDG and their combination yields further gains. The ablation of input contexts (sequence-only vs. wild-type structure vs. predicted mutant structure) demonstrates that structural information is necessary for best performance but predicted mutant structures add little beyond what the teacher already captures implicitly.

5. **Directed mutation search demonstrably outperforms random search under the same oracle**: Table 6 shows that guided mutation (via the Mutation Explainer) achieves substantially lower predicted ΔΔG than random mutation, especially on larger search spaces (3× improvement on 26-site joint optimization). The pattern that random mutation degrades with more sites while directed mutation improves provides evidence that the Shapley-based guidance captures meaningful signal in the predictor's landscape.

6. **Large-scale augmented dataset released**: SKEMPI-Aug (670k mutation samples with ΔΔG labels) addresses the scarcity of annotated mutation data and is itself a contribution for follow-up work.

## Weaknesses

### Fatal

None.

### Major

1. **Antibody optimization evaluation lacks independent validation**: The optimization results in Table 6 are evaluated *by the same Light-DDG predictor* that guides the search. While comparisons to random mutation under the same oracle are internally valid (both search strategies are measured on the same landscape), the headline claim that Uni-Anti "optimizes" antibodies in a biologically meaningful sense is unsupported without external validation. The comparison to generative baselines (RefineGNN, MEAN, DiffAb, dyMEAN) is also asymmetric: Uni-Anti's search directly minimizes Light-DDG's score, while the generative models were not trained or tuned for this objective. The paper acknowledges this limitation (Section 6: "wet experimental assays... will be left for future work"), but the gap remains substantial for a paper that prominently frames antibody optimization as a central contribution. At minimum, evaluation by an independently trained predictor or a biophysics-based method (e.g., FoldX, Rosetta ddG) is needed.

2. **Pre-training data asymmetry not fully contextualized**: Light-DDG benefits from supervised pre-training on 670k Prompt-DDG-annotated mutations, while baselines (RDE, ProMIM, DiffAffinity, Prompt-DDG) use unsupervised pre-training on 143k unlabeled structures. The headline "15.45% improvement over Prompt-DDG" partly reflects training on Prompt-DDG's own outputs with 4.7× more data. The ablation (Table 4, Fig. 5(b)) partially addresses this by showing w/o KD and w/o Aug variants, but the main comparison table (Table 2) presents all methods without discussing this asymmetry or including a baseline that matches the pre-training regime.

### Minor

1. **No variance or statistical significance reported**: All tables report only mean values from 3-fold cross-validation without standard deviations, confidence intervals, or significance tests. On a dataset of 348 complexes split into only 3 folds, variance across folds could be substantial. This is needed to assess whether the claimed improvements are robust.

2. **No parameter count or FLOPs comparison**: The paper repeatedly calls Light-DDG "lightweight" and reports 89.7× speedup, but never states the model's parameter count or FLOPs, nor compares these to baselines. The speedup measurement hardware and protocol are also not described, limiting reproducibility of the efficiency claim.

3. **Mutation Explainer lacks validation against simpler alternatives**: The iterative Shapley value estimation (Section 4.3) is presented without comparison to simpler baselines (e.g., single-mutation ΔΔG ranking, random sampling with the same budget, or exact Shapley values on a tractable subset). The explainer identifies five known valid mutations (Fig. 6), which is a positive signal, but precision/recall against alternative explainability methods is not quantified.

### Trivial

- The "unsupervised" framing is somewhat imprecise: Light-DDG itself is trained via supervised pre-training on 670k labeled examples. The paper clarifies (abstract, line 10) that "unsupervised" refers to not requiring *additional* functional annotations beyond ΔΔG, which is reasonable but could confuse readers expecting the standard meaning.
- The mutation evolutionary tree (Fig. 6d) is presented but not analyzed in any depth; its added insight beyond the Shapley values is unclear.

## Nice-to-Haves

- Add a "vanilla Transformer" baseline trained only on SKEMPI v2.0 (no augmentation, no distillation) to establish the absolute floor for the ablation.
- Validate the Mutation Explainer against: (a) single-mutation ΔΔG ranking, (b) random sampling with the same budget, (c) exact Shapley values on a small tractable subset.
- Provide hardware details and measurement protocol for the speedup claim.
- Report per-fold results or standard deviations for all main tables.

## Removed Points

These points were raised in the input reviews but are excluded or downgraded from the main weaknesses for the following reasons:

- **Data leakage in cross-augmentation (Critic: "student sees structures during pre-training that appear in the evaluation fold")**: This is standard practice in protein ML — pre-training on structures that appear in downstream tasks is common and does not constitute label leakage. The paper's K-fold cross-augmentation specifically prevents label leakage from the teacher, which is the relevant form of leakage. Removed as not a genuine weakness.
- **Missing "w/o KD + w/o Aug" row in ablation**: The existing ablation already shows each component's individual contribution. The missing row is a minor gap that would strengthen the analysis but does not undermine the conclusions. Demoted to Nice-to-Have.
- **"Unsupervised" framing as misleading**: The paper explicitly qualifies what "unsupervised" means ("doesn't require any additional functional annotations and deep generative models"). This is a defensible usage. Demoted to Trivial.
- **Section 1 claim about IPA-style backbone "burdening inference" lacking evidence**: This is a qualitative statement common in related-work summaries. The speedup numbers in the paper itself provide the actual evidence. Removed as too minor.
- **Table 5 comparison being "different from optimization framing"**: Table 5 is explicitly about *screening*, which is a distinct but related task. The paper separates screening (Table 5) from optimization (Table 6). Not a weakness.

## Novel Insights

The reviews surface a genuine tension: the paper's strongest and most well-validated contribution (Light-DDG as an efficient, accurate ΔΔG predictor) is evaluated on ground-truth experimental data from SKEMPI v2.0, while its most eye-catching framing (a unified unsupervised antibody optimizer) relies on circular evaluation using the same predictor. The core ΔΔG prediction work is solid and independently valuable; the optimization would benefit from being presented as an *application* or *case study* of the predictor rather than a co-equal contribution. The K-fold cross-augmentation strategy for preventing teacher label leakage is a well-designed methodological contribution that the reviews did not challenge.

## Suggestions

1. Evaluate the optimized antibodies using an independent predictor or biophysics-based method (FoldX, Rosetta ddG) to break the circularity in the optimization evaluation.
2. Report standard deviations or per-fold results for all main tables (Tables 2, 3, 4, 5, 6).
3. State the model parameter count, FLOPs, and hardware/measurement setup for the speedup claim.
4. Add simpler baselines for the Mutation Explainer (single-mutation ΔΔG ranking, random sampling) to validate its advantage.
5. Add a "w/o KD + w/o Aug" row to the ablation to establish the floor.
6. Reframe the antibody optimization results as a case study/application of Light-DDG rather than a co-equal contribution, or provide external validation.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>