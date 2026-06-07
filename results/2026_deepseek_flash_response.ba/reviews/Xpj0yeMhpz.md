Now let me output the final consolidated review.

## Summary

This paper introduces a taxonomy of label-domain mismatch scenarios in class-wise machine unlearning (target mismatch, model mismatch, data mismatch) that go beyond the conventional "all matched" setting where the class label and target concept coincide. The authors propose TARF (TARget-aware Forgetting), a framework combining annealed gradient ascent on forgetting data with target-aware gradient descent on identified hard-to-affect retaining data. Experiments on CIFAR-10/100, ImageNet-1k, stable diffusion, and TOFU/LLaMA show TARF achieving lower Gap scores than baselines across all settings.

## Strengths

1. **Novel formal taxonomy of mismatch scenarios.** The paper systematically defines three new unlearning settings via relations among $\mathcal{L}_D$, $\mathcal{L}_M$, and $\mathcal{L}_T$ (Section 3.1), where prior class-wise unlearning work assumed $\mathcal{L}_D = \mathcal{L}_T = \mathcal{L}_M$. This is a meaningful conceptual contribution that expands the space of problems being studied.

2. **Strong empirical results across all four settings on CIFAR-10/100 (Table 3).** TARF achieves the lowest overall Gap in every task, often by large margins — e.g., CIFAR-100 target mismatch: TARF Gap=0.21 vs best baseline GA at 8.86. The improvements are consistent and substantial across tasks.

3. **Large-scale verification on ImageNet-1k (Table 4).** TARF obtains the lowest Gap across all settings on 1000-class high-resolution data, demonstrating that gains are not limited to small benchmarks.

4. **Cross-domain validation.** Applications on stable diffusion concept removal and TOFU/LLaMA personal-information unlearning show the framework transfers beyond image classification.

5. **Well-structured three-phase framework (identification → separation → approximation).** The phases map naturally to the challenges identified and the framework unifies all four settings within a single objective (Eq. 3).

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation-retrained-reference mismatch with framing.** The Retrained reference for all tasks is trained on $\mathcal{D}_r = \mathcal{D} \setminus \mathcal{D}_f$ (line 61). In target/data mismatch, $\mathcal{D}_f \subset \mathcal{D}_t$, meaning the false retaining data $\mathcal{D}_{fr} = \mathcal{D}_t \setminus \mathcal{D}_f$ remains in the Retrained model's training set. The Retrained model has *not* forgotten the full target concept — it has only forgotten $\mathcal{D}_f$. Yet the paper's framing consistently says "forget the target concept 'people'" (Figure 1). The Gap metric measures approximation to a model that forgot only $\mathcal{D}_f$, not $\mathcal{D}_t$. There is no direct metric on $\mathcal{D}_{fr}$ accuracy in target/data mismatch (Table 2 provides UA-F/UA-R for model mismatch only). The paper needs either (a) explicit metrics on $\mathcal{D}_{fr}$ to verify that TARF's Phase I identification leads to actual forgetting of the broader concept, or (b) clearer reframing that the contribution is about handling mismatch scenarios rather than forgetting beyond $\mathcal{D}_f$.

This is major because it creates a gap between the motivating narrative (forgetting the broader concept) and what the evaluation actually measures. It is not fatal because: (i) the paper's formal objective (Eq. 1) is explicitly to approximate retraining on $\mathcal{D} \setminus \mathcal{D}_f$, (ii) Phase I of TARF specifically addresses $\mathcal{D}_{fr}$ identification with supporting evidence in Figure 5(a), and (iii) the core contribution — handling settings where $\mathcal{D}_f \neq \mathcal{D}_t$, which prior work did not address — is still supported by the existing evaluation.

### Minor

2. **Theorem 3.2 is conceptually useful but not design-driving.** The bound shows that the loss gap during gradient ascent on two subsets is proportional to their representation distance. This formalizes known intuition but is not used to derive specific design choices (form of $k(t)$, $\tau$, or $\beta$), and the bound is too loose to be predictive. The "representation gravity" concept is a descriptive label rather than a framework that generates testable predictions. The paper's claim of "theoretical analysis" (line 100) slightly overstates the depth.

3. **Hyperparameter sensitivity with limited guidance.** Key parameters ($k$, $t_0$, $t_1$, $\beta$) affect performance, and the ablation on $k$ (Figure 7, left) shows sensitivity. While the paper provides some guidance (e.g., $\beta$ estimation via accuracy-drop ranking, Appendix E), the practical recipe for setting these in a new domain is underspecified.

4. **TOFU table (Table 5) has confusing presentation.** The table structure is garbled with repeated headers, and TARF(GA) and TARF(NPO) show identical values in multiple blocks. If these identities hold in the original submission, they require explanation; if they are parser artifacts, the table should be restructured for clarity.

### Trivial
None.

## Nice-to-Haves
- An ablation where TARF's Phase I is bypassed and ground-truth $\mathcal{D}_t$ is given, to quantify the contribution of target identification.
- Reporting std values in the main table rather than only in the appendix.
- Discussion of how the number of classes in $\mathcal{D}_{un}$ belonging to the target concept is determined in practice (currently assumed known for evaluation construction).

## Removed Points
Points flagged for removal; treat with caution:
- "Prior work claim is overstated" — the paper specifically discusses class-wise unlearning, where the claim holds. Too nitpicky.
- "Assumption about known number of target classes weakens applicability" — this is an evaluation construction assumption, not a method requirement. TARF's Phase I identifies $\mathcal{D}_{fr}$ automatically.
- "MIA=100.00 is suspicious" — consistent with UA=0.00; not anomalous.
- "Statistical significance not in main table" — std values in appendix is standard practice.
- "Only 6 methods on ImageNet" — SAUfn is missing but the set is otherwise comparable to Table 3.
- "No guidance on setting hyperparameters" — paper does discuss $\beta$ estimation (line 152) and provides ablation guidance in Appendix E.
- Most formatting/typo complaints — parser artifacts.

## Novel Insights
None beyond the paper's own contributions. The reviews reinforce the paper's stated findings without adding new interpretive angles.

## Suggestions
1. Add explicit metrics on $\mathcal{D}_{fr}$ (accuracy or loss on false retaining data) for target/data mismatch settings to directly measure forgetting of the full target concept and align the evaluation with the framing.
2. Either redefine the Retrained reference as $\mathcal{D} \setminus \mathcal{D}_t$ for target-mismatch settings, or explicitly clarify in the introduction that the goal is approximating $\mathcal{D} \setminus \mathcal{D}_f$ while using $\mathcal{D}_{fr}$ identification as an auxiliary mechanism.
3. Provide a concrete procedure for setting $k$, $t_0$, $t_1$ in new domains (e.g., a validation metric or heuristic rule).
4. Clean up Table 5 to avoid ambiguity — ensure the table structure is self-contained and that identical values across method variants are either explained or corrected.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>