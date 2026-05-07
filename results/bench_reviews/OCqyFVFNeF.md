Now I have a good understanding of both the paper and the calibration anchors. Let me verify a few key claims from the harsh critic against the actual paper content before writing the final review.

Key claims from the harsh critic I need to verify:

1. **Circular evaluation**: The claim is that the method optimizes for support overlap (Eq 6/7) and then evaluates on support overlap (Fig 3). Let me verify this is accurate.

2. **Non-identifiability of AND/OR decomposition**: The claim is that the decomposition v_and = 0.5v + γ and v_or = 0.5v - γ introduces free parameters that are optimized to create shared supports rather than discovered.

3. **Fidelity**: The claim that the paper doesn't show reconstruction fidelity using only the extracted salient/shared primitives.

Let me re-read the relevant sections.

From what I've read:

1. **Circular evaluation**: The paper defines transferability as support overlap (Definition 1), then optimizes Eq 6/7 to maximize shared supports, and measures success by support overlap in Fig 3. This IS circular — the method is explicitly designed to increase the metric it's evaluated on. However, the paper does show results beyond just overlap (sparsity curves, low-order interaction analysis, visualizations). The circularity is real but partial — the generalization metric (s_and, s_or) is indeed the quantity being optimized.

2. **Non-identifiability**: The paper acknowledges this in Sec 3.2 with "Challenge 1" about ambiguous decomposition. The paper's response is to use sparsity + generalization as regularization to select a decomposition. The harsh critic's point that this doesn't establish the selected decomposition is "intrinsic" is valid — the paper assumes "sufficiently trained DNNs tend to have similar decompositions" (line ~185), which is what it's trying to prove.

3. **Fidelity**: The paper shows universal matching error in Fig 4 (mentioned in text around line 191), but this uses ALL interactions, not just the sparse/shared ones. The claim that only 0.1%-2.0% of interactions are salient (Fig 2 caption) doesn't come with reconstruction fidelity at that sparsity level.

Let me also check: does the paper actually evaluate fidelity with only the shared primitives?

Looking at the experimental section more carefully — Fig 2 shows sparsity curves, Fig 3 shows generalization power (overlap), Fig 5 shows order-wise shared interaction ratios, and Fig 6 shows visualizations. There is no reconstruction fidelity experiment using only shared primitives at matched sparsity.

Now let me calibrate:
- 3pWSL8My6B (avg 7.0, Accept): This is the prior work by the same group on proving sparse interactions emerge. Scored highly for theoretical contributions.
- ih3BJmIZbC (avg 6.80, Accept): RSVC comparing DNNs via shared visual concepts. Stronger evaluation, including regression-based similarity metrics and identification of unique concepts.
- FnIRtzK5wX (avg 4.25, Reject): QiGan/Go paper, same research group. Weaker experimental support.
- bXeSwrVgjN (avg 6.0, Reject): TRACE framework — circular evaluation concern but with important theoretical insight.
- rGP2jbWt0l (avg 5.25, Accept): MDA — optimizing the metric you evaluate on. Similar circularity concern.

The paper under review has:
- A clear and important problem identification (AND/OR decomposition ambiguity)
- A reasonable optimization formulation (Eq 6-7)
- Valid theory on noise sensitivity (variance scales as 2^|T|σ²)
- But the main experimental claim has a circularity issue
- Missing fidelity evaluation for the extracted primitives
- No held-out model evaluation

The circularity concern is serious but somewhat mitigated by the fact that: (1) the method extracts specific interactions, not just overlaps — the qualitative visualizations show semantically plausible shared interactions; (2) the low-order interaction finding is consistent with known theory about Shapley/Harsanyi stability; (3) the prior work on sparse interactions (cited as 3pWSL8My6B with score 7.0) provides theoretical foundation.

However, the core claim — "extracted interactions can better reflect common knowledge shared by different DNNs" — is evaluated primarily through the metric it optimizes (support overlap), which is circular. And the sharing assumption γ_T = γ̄_T + γ̂_T essentially builds in what it seeks to prove.

Given the anchors:
- Similar topic papers with solid contributions: 6.5-7.5
- Papers with similar circular evaluation issues: 3.0-6.0 (bXeSwrVgjN got 6.0 but was rejected; rGP2jbWt0l got 5.25 but accepted)
- Directly related paper by same group (3pWSL8My6B): 7.0, but that has stronger theoretical proofs

This paper makes a meaningful contribution in identifying the AND/OR decomposition identifiability problem and proposing a multi-model extraction objective. But the experimental validation has a fundamental circularity issue, and the claims about "faithful" and "common knowledge" go beyond what the evidence supports. The paper would be significantly strengthened by held-out model evaluation and fidelity-reconstruction experiments.

I'd place this paper around 4.5 — it identifies a real problem and proposes a reasonable first approach, but the evaluation is too circular and the claims are too strong relative to what's demonstrated.</think>Now I have read the full paper and calibration anchors. Let me synthesize the final review.

## Summary

This paper addresses the identifiability problem in AND-OR interaction-based explanations of DNNs: different decompositions of a network's output into AND and OR components can yield different primitive interaction sets. The authors propose a joint optimization across multiple DNNs trained for the same task (Eq. 6–7) that uses a rowmax-based sparsity objective to encourage shared interaction supports, parameterized as γ_T^(i) = γ̄_T + γ̂_T^(i). Experiments across three task domains (sentiment classification, dialogue, MNIST) show that the extracted interactions achieve higher support overlap (s_and, s_or) across models than traditional sparsity-only extraction, and that low-order interactions are more reliably shared.

## Strengths

- **Identifies a real and underappreciated problem**: The paper correctly identifies that AND/OR interaction decompositions are non-unique (Challenge 1, Sec. 3.2) and demonstrates it empirically (only ~21% overlap between two runs of the same extraction method on the same model). This is an important weakness of existing interaction-based explanation methods that many papers gloss over.

- **Noise sensitivity analysis is informative**: The derivation that interaction variance scales as 2^|T|σ² under Gaussian noise (Sec. 3.3) provides a principled explanation for why high-order interactions are less stable and less likely to be shared. This is consistent with known properties of Harsanyi/Shapley decompositions and adds useful theoretical insight.

- **Rowmax objective is a concrete and well-motivated design**: Eq. 6 ensures that if any single model has a strong interaction for subset T_k, the same interaction can be extracted from other models without penalty. The redundancy term (Eq. 7, α‖I‖₁) addresses a identified shortcut solution. This is a reasonable engineering contribution.

- **Broad experimental coverage**: Testing across NLP (BERT variants on SST-2, LLaMA/OPT on SQuAD) and vision (ResNet-20/VGG-16 on MNIST) provides evidence that the approach is not limited to a single domain.

## Weaknesses

### Fatal
None.

### Major

- **Circular evaluation of the main claim**: The paper defines transferability/generalization as support overlap (Definition 1: the ratio of shared to total interaction supports), optimizes Eq. 6–7 to maximize exactly this overlap, and then evaluates success by reporting s_and and s_or in Fig. 3. This is the same quantity the method is designed to increase. There is no held-out model, no independent semantic or behavioral criterion, and no fidelity experiment to validate that the shared interactions faithfully reflect genuine common knowledge rather than being optimization artifacts. As the paper itself acknowledges (line ~184), the rowmax function ensures "much higher penalties to non-generalizable interactions than generalizable interactions" — precisely the metric being reported. This circularity undermines the headline claim that "extracted interactions can better reflect common knowledge shared by different DNNs."

- **No demonstration that shared primitives faithfully approximate DNN behavior**: The paper frames its goal as summarizing DNN knowledge "without losing much information" (abstract), but the experiments only show sparsity curves (Fig. 2) and support-overlap metrics (Fig. 3). The universal matching theorem (Theorem 3) uses all interactions, not the sparse shared set. Without reporting reconstruction fidelity (e.g., approximating v(x_T) for masked samples) using only the top-k shared interactions at matched sparsity levels, it remains unclear whether the extracted primitives retain explanatory power or merely produce overlapping but potentially shallow supports.

### Minor

- **The sharing assumption presupposes what the method aims to discover**: The parameterization γ_T^(i) = γ̄_T + γ̂_T^(i) with bounded |γ̂_T^(i)| assumes that well-trained DNNs "tend to have similar decompositions" (line ~185). This is a reasonable heuristic, but then the resulting shared supports cannot serve as strong evidence that DNNs genuinely encode similar AND/OR decompositions — it may partly reflect the inductive bias of the constraint.

- **Task 2 target output may differ between models**: In Task 2 (LLaMA/OPT on SQuAD), each model's top predicted word y^max may differ, meaning the interactions being compared explain different scalar outputs. This makes support overlap harder to interpret as "shared knowledge" (acknowledged implicitly but not addressed).

- **Support overlap ignores sign/magnitude agreement**: Definition 1 counts two models as sharing an interaction if the same subset T appears in both salient sets, regardless of whether I^(1)(T) and I^(2)(T) have the same sign, comparable magnitude, or similar behavioral effects. Two models could share a support with opposite effects and still count as "generalizable."

- **Only two models per task**: Since the method jointly optimizes over the models being evaluated, two-model overlap provides limited evidence. Held-out model evaluation would significantly strengthen the claims.

## Trivial
None.

## Nice-to-Haves

- Evaluate on held-out models not used during joint extraction to test out-of-sample transfer.
- Report reconstruction fidelity using only extracted shared primitives at matched sparsity, compared against baselines.
- Scatter plots of I^(1)(S) vs I^(2)(S) for shared supports to assess sign/magnitude agreement.
- Ablation of the optimization components (rowmax, α‖I‖₁, shared γ̄_T, learned ε) to understand their individual contributions.

## Removed Points

- **Harsh critic claims about "shared decomposition biasing extracted supports toward agreement"**: While true that the sharing constraint creates an inductive bias, this is explicitly acknowledged in the paper and is the design intent. This is not a hidden flaw but a deliberate tradeoff. The real issue is circular evaluation, not the constraint itself. → Kept in weakened form under Minor.

- **Harsh critic demands synthetic/ground-truth experiments**: While this would strengthen the paper, it is beyond the scope of what is standard in this research area, where DNN explanation methods are typically evaluated on real models. → Moved to Nice-to-Haves.

- **Harsh critic claims about 2^|T| variance scaling being problematic**: The paper explicitly addresses this with the learned error term ε_T, and demonstrating higher-order instability is a contribution, not a weakness. → Removed.

- **Harsh critic claims about masking/baseline dependence**: This is inherited from the Harsanyi/interaction framework and is not a novel weakness of this paper. All interaction methods face this. → Removed.

- **Strength finder claims about "broad experimental evaluation across diverse tasks and architectures" as a core strength**: This is generic; ResNet-20/VGG-16 on MNIST with manually selected patches and LLaMA/OPT with potentially different target words are limited. → Removed as generic.

- **Strength finder claims the paper has "clear empirical demonstration that existing methods suffer from poor generalization"**: The 21% overlap between two initializations is shown, but it motivates the need rather than constitutes a major empirical contribution. → Kept in weakened form under Strengths (identifying the problem).

## Novel Insights

The most genuinely novel insight emerging from the reviews is the tension between the paper's important theoretical observation (AND/OR interaction decompositions are non-identifiable) and its proposed solution, which resolves this ambiguity by an optimization preference rather than a principled identification criterion. The paper identifies the right disease but prescribes a treatment whose efficacy is measured by a metric that the treatment itself optimizes. The noise variance result (2^|T|σ²) is a clean theoretical contribution that stands independently of the evaluation circularity concern.

## Suggestions

- Run the joint extraction on N-1 models and evaluate support overlap on the held-out Nth model to break the circularity. Even with only 2 models per task, one could use cross-validation or use models from different training runs.
- Report reconstruction error curves (approximation of v(x_T)) vs. number of primitives used, comparing shared primitives vs. traditional primitives at the same sparsity level.

## Score and Decision

Calibration anchors:
- 3pWSL8My6B (avg 7.0, Accept): Same research group's prior work on sparse interaction emergence proofs — stronger theoretical foundation, scored higher.
- ih3BJmIZbC (avg 6.80, Accept): RSVC for comparing DNNs via shared visual concepts — similar motivation but with stronger and more diverse evaluation.
- FnIRtzK5wX (avg 4.25, Reject): QiGan/Go paper — related interaction disentanglement but with weaker validation.
- bXeSwrVgjN (avg 6.0, Reject): TRACE framework — also has circular evaluation concerns about optimizing the metric being reported.
- rGP2jbWt0l (avg 5.25, Accept): MDA — directly optimizes attribution metrics it evaluates on; similar circularity concern but accepted because the theoretical contribution stood independently.

The paper under review has a real and important observation (AND/OR decomposition ambiguity) and a reasonable first-pass solution, but the experimental validation of its primary claim is circular, and no fidelity evidence is provided for the shared primitives. This is a meaningful contribution that falls short of convincing validation — similar to papers in the 4–5 range. The theoretical contributions (noise variance, decomposition ambiguity identification) are real but not as deep as the prior work (3pWSL8My6B, avg 7.0) that this paper builds upon.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>