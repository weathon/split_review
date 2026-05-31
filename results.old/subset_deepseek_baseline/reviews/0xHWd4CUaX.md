## Summary
The paper proposes a reinforcement learning (RL) framework for automated code refactoring that uses contrastive pre-trained code graph embeddings. A syntax-guided contrastive encoder learns structural invariant representations of code graphs via self-supervision, which are then combined with traditional code quality metrics into a composite reward function. The policy is a graph attention network operating on the joint representation space. Experiments on three refactoring datasets claim improvements over several baselines across multiple metrics.

## Strengths
- **Novel combination of ideas**: Integrating contrastive pre-training of code graph embeddings with an RL refactoring agent is a reasonable and underexplored direction. The use of syntax-preserving augmentations for contrastive learning is well-motivated.
- **Composite reward design**: The reward function fuses learned embeddings with traditional metrics and a semantic preservation term, attempting to balance syntactic improvement and behavior preservation.
- **Graph attention policy**: Using a GAT to directly operate on the joint representation space is natural for code structure and enables context-dependent action selection.

## Weaknesses
### Fatal
None.

### Major
1. **Insufficient experimental rigor**:
   - The paper reports point estimates for all metrics without standard deviations or confidence intervals, making it impossible to assess statistical significance.
   - Baseline implementations are not described (e.g., whether official code was used, hyperparameter tuning). The RL baselines (RLRefactor, GraphRL, NeuroRefactor) are from arXiv/preprint sources and may not be established benchmarks.
   - The evaluation datasets (Refactory, CodeRef, BigCloneBench) are partially misaligned: BigCloneBench is a clone detection benchmark, not a refactoring dataset, raising questions about how it was used for "cross-project evaluation."
   - The metric "Syntactic Improvement (SI)" is defined as percentage reduction in code smells, but the method for measuring code smell violations is not specified, and the reported numbers (83.7%) seem implausibly high for realistic refactoring tasks.

2. **Missing ablation of key components**:
   - The exploration strategy (Mahalanobis distance to prototype states) is described in Section 4.3 but is not ablated. The ablation study only removes "contrastive pre-training," "embedding rewards," "semantic tests," and replaces with "random exploration," which does not isolate the effect of the proposed guided exploration.
   - The value of the embedding dynamics term in the reward is partially tested (w/o embedding rewards) but its interaction with the exploration strategy is not studied.

3. **Unconvincing generalization claims**:
   - The cross-language generalization experiment (Table 3) shows a model trained on Java (CodeSearchNet) evaluated on Python and C++ without fine-tuning. The reported SI (68.7% for Python) is surprisingly high given the domain shift, but no analysis is provided to confirm that the model is actually performing meaningful refactoring rather than trivial transformations. The baselines (PyLint, Cppcheck) are static analyzers, not RL-based methods, so the comparison is not apples-to-apples.

### Minor
- The related work section includes several references with 2025 dates (e.g., Marvellous et al., 2025; Kupari et al., 2025) that appear to be preprints or non-peer-reviewed sources. While not a fatal flaw, this reduces the credibility of the literature positioning.
- The qualitative analysis (Section 5.5) gives vague examples without concrete evidence that these patterns were discovered by the proposed model rather than being cherry-picked.
- Figure 3 and its associated table show a clear shift in reward components, but the underlying mechanism (how the embedding dynamics become more important) is not explained or validated.

### Trivial
- The paper includes a section "The Use of LLM" (Section 8) which is unconventional. The writing appears polished but occasionally contains unclear phrasing (likely parser artifacts in the abstract).

## Nice-to-Haves
- Provide open-source code and trained models to enable reproducibility.
- Include error bars and statistical tests for all experiments.
- Add an ablation study of the exploration strategy (comparing Mahalanobis-guided vs. uniform random exploration).
- Evaluate on more widely used refactoring datasets (e.g., from refactoringguru or fine-grained commit histories) to strengthen external validity.

## Novel Insights
The observation that contrastive pre-training on code graphs can produce embedddings that correlate with refactoring quality (Pearson’s r=0.72 in Figure 2) is interesting, but the analysis is shallow. The paper does not investigate what aspects of the embedding space drive this correlation or whether it generalizes across different codebases.

## Suggestions
1. Add standard deviations and perform statistical significance tests (e.g., paired bootstrap) for all metrics in Table 1.
2. Provide clear details on baseline implementation: were official repositories used? How were hyperparameters tuned?
3. Ablate the exploration strategy and show its contribution relative to uniform exploration with the same reward function.
4. For cross-language evaluation, include a comparison with a supervised approach fine-tuned on the target language or a stronger RL baseline to demonstrate generalization convincingly.
5. Release the code and a sample pretrained encoder to facilitate reproducibility.

## Score and Decision
**Score**: 3  
**Decision**: Reject

MY FINAL SCORE: 3  
MY FINAL DECISION: Reject