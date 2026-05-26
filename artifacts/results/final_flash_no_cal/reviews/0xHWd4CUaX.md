## Summary

This paper presents a reinforcement learning framework for automated code refactoring that combines contrastively pre-trained code graph embeddings with a composite reward function. The method pre-trains a graph encoder via a contrastive objective on synthetically augmented code graphs, then uses the frozen embeddings within an RL policy trained with PPO, incorporating embedding dynamics and semantic preservation checks into the reward. Experiments on three refactoring datasets (Refactory, CodeRef, BigCloneBench) show the method outperforming several baselines (PMD, Checkstyle, Code2Seq, Graph2Edit, RLRefactor, GraphRL, NeuroRefactor) across five metrics, and ablation studies confirm the contribution of each component.

## Strengths

1. **The contrastive pre-training component is shown to be empirically valuable.** Table 2's ablation demonstrates that removing contrastive pre-training drops Syntactic Improvement (SI) from 83.7% to 76.2% (-7.5%) and Maintainability Gain (MG) from 27.9% to 22.4%, establishing that the learned representations contribute meaningfully beyond random initialization or end-to-end RL training.

2. **The framework achieves the highest reported numbers across all five metrics in Table 1**, including SI (83.7% vs. next-best 79.4%), SP (93.8% vs. 90.5%), MG (27.9% vs. 24.6%), and GS (72.4% vs. 67.2%), with the lowest edit distance (0.36). The margin on the generalization score (GS) is particularly notable.

3. **The embedding-guided exploration strategy (Eq. 6) is a principled and well-motivated component.** The ablation (Table 2) confirms its value: replacing it with random exploration drops SI from 83.7% to 74.8% and MG from 27.9% to 21.8%. Figure 2 provides supporting evidence with a positive correlation (Pearson's r=0.72) between embedding dynamics (Δh) and actual syntactic improvement.

4. **Systematic ablation study.** Table 2 tests four ablated variants (w/o contrastive pre-training, w/o embedding rewards, w/o semantic tests, random exploration), each degrading performance in interpretable ways. The qualitative case studies (Section 5.5) add practical credibility beyond aggregate metrics.

## Weaknesses

### Major

1. **No variance or statistical significance reported for any result.** Tables 1–3 and the ablation study report single values with no standard deviations, confidence intervals, or significance tests. Given that RL training is inherently high-variance, the reported margins (e.g., SI 83.7% vs. 79.4% for NeuroRefactor; GS 72.4% vs. 67.2%) could plausibly fall within noise. The paper does not state how many independent runs were performed. This is the most consequential weakness because it undermines confidence in all the empirical comparisons.

2. **The action space is not concretely defined in the main text.** The MDP tuple in Section 3.1 mentions "A denotes the action space (possible refactorings)," but no concrete set of refactoring operations is ever enumerated. Without knowing whether actions are low-level AST edits, high-level patterns (Extract Method, Rename Variable, etc.), or something else, the MDP is underspecified and the method is not reproducible from the main exposition. While this detail may reside in the (stripped) appendix, the core definition belongs in the method section.

3. **The differential-testing component (Section 4.5) lacks any computational cost analysis.** The paper describes generating test cases via symbolic execution at each RL step to compute the semantic preservation penalty δ_t. No wall-clock time, number of test cases generated per method, coverage statistics, or any runtime measurements are reported. Running symbolic execution on arbitrary code within an RL loop of 1M episodes over 12,500+ instances raises serious feasibility concerns that are not addressed. Without evidence that this component was actually executed as described, the reward signal used during training is unverified.

4. **The cross-language evaluation (Table 3) is too narrow to support the claimed generalization strength.** It compares only against one rule-based tool per language (PyLint for Python, Cppcheck for C++) with no learning-based baselines. Since the main claim is that contrastive pre-training enables cross-language transfer, the comparison should include at least one learning-based method (e.g., Code2Seq, Graph2Edit, or a zero-shot transformer) that could also be language-agnostic.

### Minor

5. **The claim of reduced need for expert demonstrations is not directly tested.** The paper states the approach "reduces the necessity of expert demonstration based learning" and contrasts with GraphRL which uses expert demonstrations, but no experiment isolates this factor (e.g., comparing against GraphRL with demonstrations removed, or controlling for demonstration budget). The claim is plausible but unsubstantiated.

6. **The contrastive pre-training's use of subtree masking as a "syntax-preserving" positive pair may create a tension with downstream use of embeddings.** Subtree masking removes AST subtrees, which changes program semantics, yet the InfoNCE loss pushes embeddings of the original and masked programs closer together. This could train the encoder to become partially invariant to semantic differences. Later, the RL reward uses embedding dynamics (Δh) as a signal for meaningful improvement, and the exploration strategy uses the embedding space to guide search. If the encoder has been taught to compress semantically different programs into similar representations, these downstream uses become less reliable. The paper does not analyze or address this tension.

7. **Hyperparameter sensitivity not explored.** The reward function (Eq. 5) has manually specified weights (w_q = [0.4, 0.3, 0.3], α = 0.2, β = 1.0, γ = 0.5). No sensitivity analysis is provided, so it is unclear how robust the results are to these choices. The temperature τ in the contrastive loss and the PPO hyperparameters similarly lack analysis.

8. **Figure 1 only shows learning curves for two methods (Ours and GraphRL) from a single run.** It is unclear whether the other RL baselines (RLRefactor, NeuroRefactor) are omitted, and a single trajectory cannot establish convergence properties. Additionally, the caption says "RL baselines" but only one baseline appears.

### Trivial

9. **Table 1's caption says "higher is better" but Edit Distance (ED) is lower-is-better** (they report 0.36, the lowest). The data is correctly presented but the caption is inconsistent.

10. **Several sentences in the abstract and introduction are grammatically garbled** (e.g., "something that necessarily requires the existing RL approaches to accomplish and that most often do last year"). These appear to be PDF extraction artifacts rather than author errors, but they hamper readability.

## Nice-to-Haves

- A comparison against GraphRL without expert demonstrations would directly test the claim about reduced supervision.
- An analysis of whether subtree masking in contrastive pre-training desensitizes the encoder to semantic changes would strengthen the methodological justification. If the concern is real, using only semantics-preserving augmentations (variable renaming, statement reordering) for positive pairs would be more defensible.
- Runtime/cost breakdown of the differential-testing component vs. the RL training loop would clarify feasibility.
- Reporting results over multiple random seeds (at least 5) with error bars would address the most significant evidential gap.

## Removed Points

*These points were flagged by reviewers but are removed for the reasons stated; they should be treated with caution.*

- **The claim that symbolic execution is "almost certainly impractical"** — this is speculative. The paper calls the checker "lightweight" and provides no runtime data either way; the criticism about lacking evidence is kept (Major weakness #3), but the assertion of impracticality is removed.
- **Criticism about garbled text in the abstract** — this is a PDF extraction artifact, not an author error, per the hard rules.
- **Criticism that the appendix may not contain missing details** — the appendix was stripped by the parser and cannot be verified; the criticism about action space missing from the main text is kept (Major weakness #2).
- **Missing related works** (e.g., CodeBERT, PLBART for code-diff) — the instructions prohibit mentioning missing related works since external confirmation is unavailable.
- **Nitpick about Figure 1 caption saying "RL baselines" but only showing one** — the figure shows "Proposed Method" and "GraphRL," so two methods are shown; the critic misread this.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that substantially reframes or extends what the paper itself provides.

## Suggestions

1. **Report all metrics with standard deviations over at least 5 independent runs.** This single change would substantially raise confidence in the results.
2. **Concretely define the action space** in the main text (or clearly reference the appendix where it is defined).
3. **Provide a computational cost analysis** of the differential-testing component, including wall-clock time, number of test cases generated, and any approximations used.
4. **Add at least one learning-based baseline to the cross-language evaluation** (Table 3) to support the generalization claim.
5. **Include an experiment that controls for expert demonstration data** (e.g., train GraphRL without demonstrations, or match the demonstration budget) to directly test the claim of reduced supervision.
6. **Analyze whether subtree masking in contrastive pre-training induces undesired invariance** to semantic changes, and consider restricting positive pairs to truly semantics-preserving transformations.

## Score and Decision

The paper proposes a novel and interesting combination of contrastive pre-training with RL for code refactoring, and the empirical results (in terms of raw numbers) are promising. However, the evaluation is marred by a critical lack of statistical rigor — no variance, no multiple runs, no significance tests — which makes it impossible to assess whether the claimed improvements are reliable or within noise. Additional concerns (underspecified action space, unverified feasibility of the differential-testing component, narrow cross-language baselines) further weaken the contribution's credibility in its current form. The ideas are worth pursuing, but the evidence as presented does not meet the standard for acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>