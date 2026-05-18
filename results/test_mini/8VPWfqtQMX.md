Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes In-Context Risk Minimization (ICRM), a framework that reformulates domain generalization as next-token prediction. The key idea is to treat unlabeled test examples from the same environment as context that a transformer can attend to, enabling it to "zoom-in" on the test environment's risk minimizer. The authors provide theoretical results (zoom-out, zoom-in under iid and OOD settings), a toy example showing how extended feature spaces reveal invariances, and experiments across four benchmarks (FEMNIST, Rotated MNIST, WILDS Camelyon17, Tiny ImageNet-C) demonstrating consistent improvements over ERM, ARM, and TENT.

## Strengths

1. **Novel and well-motivated conceptual framework**: The paper draws a compelling parallel between "environment" in domain generalization and "context" in next-token prediction. This reframing—that context is environment—is genuinely insightful and opens a new direction for DG research that bridges two previously separate literatures.

2. **Consistent empirical improvement across all benchmarks (Table 1)**: ICRM outperforms ERM, ARM, and TENT on all four datasets on both average and worst-case accuracy. The gains are substantial: e.g., +7.9% average over ERM on FEMNIST (with 25 context samples), +6.3% on Tiny ImageNet-C, and dramatic improvements on Camelyon17 (92.0% vs. 68.6% even at 0 context). This consistency across diverse benchmarks provides genuine evidence that the approach works.

3. **Architecture ablation isolates the role of context (Table 3)**: The paper includes ERM$^{+}$ (same transformer as ICRM, no context) and ARM$^{+}$ (transformer + context averaging). Crucially, ERM$^{+}$ *underperforms* ERM on most datasets (e.g., 50.1% vs. 68.6% on Camelyon17), and ARM$^{+}$ underperforms ARM on Camelyon17 and Tiny ImageNet-C. This shows that the transformer architecture alone does not drive the gains—the in-context mechanism is essential.

4. **Mixed-context ablation (ICRM-Mix, Table 2)**: When context is constructed from i.i.d. samples across all environments rather than from a single environment, performance degrades on FEMNIST and Rotated MNIST. This demonstrates that same-environment context is valuable, supporting the framing of "context as environment."

5. **New perspective on invariance**: The toy example (Section 5) and discussion of extending rather than removing features to reveal invariance is a thoughtful conceptual contribution that contrasts productively with the dominant invariance-removal paradigm.

## Weaknesses

### Major

- **The theoretical results rely on strong assumptions that limit their force**: Theorem 1 (Full iid zoom-in) assumes the existence of an amortization function $b$ that converges almost surely to the environment-specific parameter $\theta_X^E$. This essentially assumes the core learning problem is solved. Theorem 3 (Full ood zoom-in) is an existence statement ("there exists an ICL algorithm that produces Bayes optimal predictions") without constructive guarantees. The Zoom-out proposition (no context → ERM) is unsurprising. While these results are not meaningless—they provide formal consistency guarantees—they fall short of explaining when or why ICRM works in practice. The gap between the theory's assumptions and the practical implementation is not bridged.

- **The 0-context performance gap is not adequately disentangled**: On Camelyon17, ICRM achieves 92.0% at 0 context vs. ERM's 68.6%—a 23.4% gap before any test-time context is used. The paper attributes this to the training regimen producing better representations, but this raises a fundamental question: is the primary benefit of ICRM due to in-context adaptation at test time, or due to better representation learning during training from the sequential training procedure? The ERM$^{+}$ ablation (transformer, no context, trained on single examples) does not control for the sequential training structure. A baseline trained on sequences but predicting all labels independently (without autoregressive conditioning) would isolate the contribution of the training data structure from the adaptation mechanism. Without this, the paper's framing privileges one explanation (in-context zooming-in) over an equally plausible one (the sequential training procedure produces better features).

### Minor

- **The main comparison table (Table 1) does not include architecture-controlled baselines**: The main table shows ICRM (backbone + GPT-2 transformer) vs. ERM/ARM (backbone only), which are not architecture-controlled. While the ablation (Table 3) provides this control in a separate table, including ERM$^{+}$ and ARM$^{+}$ in the main comparison would make the architecture-controlled story more transparent and avoid the appearance of an unfair comparison.

- **The "worst-case = same as average" note for Camelyon17 is unexplained**: The footnote that worst-case accuracy is the same as average accuracy for Camelyon17 is suspicious and needs justification. If there is only one test environment, this should be stated explicitly. If there are multiple environments with identical accuracy, this is unusual and warrants discussion.

- **Framing overstates the OOD generality**: The abstract/introduction motivate the problem using self-driving cars failing in "completely new environments" that differ in kind. However, the experiments test held-out versions of the same type of shift seen during training (held-out rotations, held-out writers, held-out hospitals). Theorem 3 assumes test environments fall in Voronoi cells of training environments—an interpolation setting. The paper would benefit from acknowledging this framing gap more explicitly and clarifying that the contribution is about test-time adaptation to seen types of shift rather than extrapolation to qualitatively different environments.

- **Attention visualizations are qualitative and anecdotal**: Figure 2 shows attention patterns for a few selected query images. While visually interesting, there is no quantitative evaluation (e.g., do attention patterns correlate with prediction accuracy? how often does the model attend to the "right" examples?). The claim about "semantic understanding of similarity" is not supported by quantitative evidence.

### Trivial

- The Camelyon17 results show ICRM decreasing slightly from 0 context (92.0) to 25+ context (90.7-90.8). This is a small effect but the paper does not comment on why adding context might slightly hurt performance on this dataset.

## Nice-to-Haves

- A baseline trained on sequences (same-environment batches) without the autoregressive task (e.g., predicting all labels independently from the pooled set representation) would help disentangle representation learning from in-context adaptation.
- A test-time-only adaptation baseline using the same backbone (e.g., TENT applied to the ICRM backbone without the context mechanism) would further isolate the adaptation benefit.
- Per-domain breakdown for Camelyon17 and Tiny ImageNet-C to validate the worst-case metric and provide more granular insight.
- Quantitative analysis of how context length affects performance over a finer grid (0 to 25) and whether saturation occurs.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Unfair baseline comparison undermines central empirical claim"**: The harsh critic claimed the architecture mismatch makes the comparison invalid. However, the ablation (Table 3) shows that ERM$^{+}$ (transformer without context) underperforms ERM, meaning the transformer architecture alone hurts—the gains come from context. This criticism is invalid as stated; the architecture-controlled ablation supports rather than undermines the paper's claim. The critic's logic that the comparison is "fatally compromised" is not supported by the evidence in the paper itself.

- **"Theoretical results are tautological"**: The harsh critic claimed the theorems assume the core problem is solved. While the assumptions are indeed strong, the results are consistency guarantees (if amortization works, then zoom-in occurs)—a standard form of theoretical result in ML. Calling them "tautological" is an overstatement; they provide formal grounding for the framework's intuition.

- **"Missing related works"**: Per instructions, I cannot verify or raise criticisms about missing related works.

- **"Section 5 toy example connection is tenuous"**: The paper explicitly states it provides the extended features "instead of requiring the algorithm to learn such representation from general-form sequential context" — it is a pedagogical example to illustrate a conceptual point, not an empirical demonstration.

- **Various formatting/style nitpicks**: Removed per hard rules.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation that the paper itself does not fully develop: the 0-context performance gap (ICRM > ERM by 23.4% on Camelyon17 before any context is used) suggests that training on sequential same-environment batches induces better representations even for the first test example. This "pre-adaptation" benefit is distinct from the in-context adaptation benefit and raises the interesting possibility that the sequential training procedure itself—independent of the autoregressive prediction format—could be a generally useful DG training technique. The paper attributes this to "a better featurizer" but does not probe the mechanism. A follow-up exploring whether sequential-environment training (without any autoregressive conditioning at test time) already beats ERM would sharpen our understanding of what ICRM actually contributes.

## Suggestions

1. Include ERM$^{+}$ and ARM$^{+}$ in the main results table (or at minimum, reference them prominently) so readers can immediately see the architecture-controlled comparison.
2. Add a baseline that trains on same-environment sequences but predicts all labels simultaneously (non-autoregressively) to isolate the effect of the sequential training procedure from the in-context adaptation mechanism.
3. Clarify the Camelyon17 worst-case metric—explain why it equals the average and whether there is one or multiple test environments.
4. Temper the framing to more accurately describe the setting as test-time adaptation to held-out environments of the same type, rather than extrapolation to qualitatively different environments.
5. Add quantitative evaluation of attention patterns (e.g., correlation between attention weights and label similarity, or classification accuracy conditioned on whether the model attends to the "right" examples).

## Score and Decision

### Calibration Anchors

All anchors retrieved by the single calibration_search call:

- **yOhNLIqTEF.md** (avg 6.67, Accept): Systematic ICL generalization study with well-designed experiments. Compared to this paper: weaker empirical DG results but stronger experimental design rigor. This paper is slightly below this anchor.

- **aKJr5NnN8U.md** (avg 6.50, Accept): ICL vs. IWL theory with experiments. Compared to this paper: stronger theoretical rigor but narrower scope (synthetic tasks only). Comparable overall.

- **wCOJpXm0Me.md** (avg 6.25, Accept): DG pre-training analysis. Compared to this paper: more focused on understanding than proposing new methods. This paper has stronger methodological novelty.

- **2PKLRmU7ne.md** (avg 5.60, Reject): ICL and Occam's razor theory. Compared to this paper: weaker experiments, interesting but loose theory. This paper has stronger empirical validation.

- **tG5mpAM7ZK.md** (avg 5.33, Reject): Domain extension via vision-language models. Compared to this paper: less direct contribution to DG methodology.

- **2XwBIcywWM.md** (avg 5.00, Reject): Test-time DG via variational neighbor labels. Similar setting (test-time adaptation). This paper's results are more comprehensive.

- **KstDMYkfj4.md** (avg 3.80, Reject): DG limitations study. This paper demonstrates positive results where that paper argues they are impossible.

- **b5MCteb3w7.md** (avg 4.75, Reject): In-context RL. Lower quality than this paper.

- **OLi39lZS9Y.md** (avg 3.50, Reject): In-context learning for sequential decision-making. Weaker results.

- **ZbOSRZ0JXH.md** (avg 3.00, Reject): Data-free DG via LLMs. Much weaker empirical rigor and missing baselines. This paper is clearly stronger.

- **PxL35zAxvT.md** (avg 4.67, Reject): TTA with auxiliary tasks. Comparable relevance but weaker scope.

- **gK1rl98VRp.md** (avg 6.00, Accept): Auto-regressive next-token prediction theory for ICL. Stronger theory but purely synthetic.

- **vSh5ePa0ph.md** (avg 6.75, Accept): ICL task complexity for linear regression. Strong theory in restricted setting.

- **pw2ssoOTpo.md** (avg 6.50, Accept): DG testbed. Different contribution type (benchmark).

- **ENVwvyiJXY.md** (avg 4.00, Reject): Dataset distillation for DG. Weaker empirical results.

- **d2TOOGbrtP.md** (avg 5.00, Reject): Bayesian DG. Comparable quality but less novel methodology.

- **jeNWwtIX71.md** (avg 5.00, Reject): Information-theoretic DG. Comparable quality.

- **4kJfWZChJI.md** (avg 5.00, Reject): Domain-specific experts ensemble. Related but different approach.

### Assessment

The paper presents a genuinely novel conceptual synthesis connecting DG and ICL, with solid empirical results across four benchmarks and useful ablations. Its main weaknesses are: (1) the theory relies on strong assumptions that do not explain the empirical success, (2) the 0-context performance gap suggests a significant representation-learning benefit that is not fully disentangled from the claimed adaptation benefit, and (3) the framing modestly overstates the OOD generality. These are real but not fatal. The paper makes a contribution that advances the DG conversation in a new direction.

Based on comparison with calibration anchors—sitting above papers scoring 3-5 but below the high-6 papers with stronger theoretical or experimental rigor—this paper merits a score of 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>