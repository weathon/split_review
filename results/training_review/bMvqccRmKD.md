Now I have all the evidence I need. Let me synthesize the final consolidated review.

## Summary

This paper introduces CSR (Causality-guided Self-adaptive Representations), a framework for RL generalization that handles both distribution shifts and state/action space expansions in a unified manner. CSR augments Dreamer-style world models with binary causal masks \(D\) that encode structural relationships among latent variables, plus a task-specific change factor \(\boldsymbol{\theta}_i\) to capture distribution shifts. A three-step strategy (detection, expansion, pruning) enables the agent to autonomously determine whether a new task involves only distribution changes or requires adding new causal variables, then adapts the policy with minimal retraining. Experiments on CartPole, CoinRun, and Atari games show strong generalization.

## Strengths

- **Addresses a genuine gap in RL generalization**: The paper explicitly tackles two types of environmental change — distribution shifts and space expansions — while most prior work (e.g., AdaRL, Dreamer) assumes fixed state/action spaces. This is a practical and underexplored problem setting.

- **Proposes a principled causal framework with structural masks**: The use of binary masks \(D\) to encode causal relationships among latent variables (Eq. 2) and the domain-specific factor \(\boldsymbol{\theta}_i\) provides an interpretable way to identify which variables matter for each task. The pruning mechanism (Sec. 3.3) that removes irrelevant variables based on these masks is a clean operationalization of causal minimality.

- **Empirically strong results on the reported settings**: On CartPole (Table 1), CSR achieves perfect scores (500) on all four tasks while all baselines fail on space expansion tasks. On the 5 Atari games reported (Table 2), CSR achieves the highest mean scores (e.g., 1586.9 on Alien vs. 1147.5 for AdaRL). The ablation studies (Fig. 2c-d) confirm that both the causal structure and the self-adaptive expansion strategy contribute to performance.

- **Ablation studies validate design choices**: Figure 2c shows that removing the structural matrices \(D\) significantly degrades performance, and Figure 2d confirms that the Self-Adaptive expansion strategy outperforms Random and Deterministic alternatives.

## Weaknesses

### Fatal
None.

### Major

- **Inadequate baselines for the space expansion scenario**: The paper's core claim is handling state/action space expansions, yet it compares only against methods that assume fixed state/action spaces (Dreamer, DQN, SPR, AdaRL). Showing that CSR outperforms these on space expansion tasks is nearly a foregone conclusion. The related work section (line 299) cites lifelong learning/dynamic architecture methods (DEN, PackNet, APD, CPG, Learn-to-Grow) that are explicitly designed for expanding architectures, but none are included as baselines. Without these comparisons, the claim of "state-of-the-art" performance under space expansions is not adequately supported.

- **Atari evaluation is limited to 5 of 26 games without justification**: The Atari 100K benchmark contains 26 games. The paper selects 5 (Alien, Bank Heist, Crazy Climber, Gopher, Pong) and calls them "representative" but provides no rationale for this selection or any aggregate metric (e.g., human-normalized mean/median across all 26). Given the small subset, there is a risk of selection bias. Large standard deviations (e.g., Crazy Climber: 88306.5 ± 18029.6) are reported without statistical significance tests, making it hard to assess whether CSR's improvements over AdaRL/Dreamer are robust.

### Minor

- **The detection threshold \(\tau^\star\) is a heuristic with limited justification**: The criterion for distinguishing distribution shifts from space expansions is a threshold set to the source task's final prediction loss (line 182). There is no formal analysis of why this value is a meaningful separator, no robustness/sensitivity experiments with alternative thresholds, and no discussion of failure cases (e.g., large distribution shifts that inflate loss, small space expansions that barely increase it). While the three-step pipeline has some built-in redundancy (Step 2 can catch cases misclassified by Step 1), the detection mechanism remains the least rigorous component of an otherwise coherent framework. The paper would benefit from a sensitivity analysis or a more principled statistical test.

- **Theoretical results are not connected to the experimental methodology**: The identifiability theorems (Theorems 1-3, Corollary 1) rely on assumptions that are not verified in the tested environments — e.g., Theorem 2 assumes linear transition dynamics and full-rank matrices, while the actual world model uses neural networks. The paper does not demonstrate that the learned representations satisfy the identifiability conditions or that the theoretical guarantees translate into practical benefits. The theory section currently reads as conceptually grounding but not integrated with the empirical claims.

- **CoinRun results lack numerical summary**: Only learning curves are shown (Fig. 2b) without reporting final scores, standard deviations, or statistical comparisons, making it difficult to quantitatively assess the improvement over baselines.

### Trivial

- The paper does not explain how the binary masks \(D\) are optimized (e.g., whether they use continuous relaxations, straight-through estimators, or another mechanism for discrete optimization). The \(\mathcal{J}_{\text{reg}}\) sparsity penalty is described but the optimization of discrete entries is glossed over.

- The simulated experiment (Fig. 2a) lacks details on the synthetic data generation process, making those results unverifiable.

- The table caption (Table 1) defines the XSolidBrush symbol as indicating a method "fails to adapt under limited training steps due to non-convergence or suboptimal performance" — this conflates two distinct failure modes and would benefit from clearer separation.

## Nice-to-Haves

- Reporting full Atari 100K results (all 26 games) with human-normalized scores and confidence intervals would substantially strengthen the empirical claims.
- A sensitivity analysis of the detection threshold \(\tau^\star\) (e.g., multiples of the source loss, or using held-out validation) would help assess the robustness of the detection mechanism.
- Providing visualizations of the learned causal graphs (masks \(D\)) before and after adaptation would improve interpretability.
- Reporting the number of parameters updated per task and total environment steps for adaptation beyond CartPole would better quantify the "low-cost" claim.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"CartPole results have internal inconsistencies (Dreamer 397.6 on Task 2 but marked as fails)"** — REMOVED. This is a misunderstanding. The score (397.6) and the Minimum Adaptation Steps metric measure different quantities. Dreamer achieves suboptimal performance within the step budget, which is precisely what the table caption defines as a "fail" ("fails to adapt under limited training steps due to non-convergence or suboptimal performance"). There is no inconsistency.

2. **"The expansion strategy used in the main experiments is ambiguous; the paper never states which strategy"** — REMOVED as stated. The paper explicitly says: "The results demonstrate that seeking for the optimal structure significantly improves expansion performance, leading us to apply the Self-Adaptive approach" (line 291). However, it is a minor presentation issue that this statement appears only in the ablation section rather than in the individual experiment descriptions. The criticism as originally phrased is factually incorrect.

3. **"Dreamer marked as fails on Task 2 is puzzling since it clearly fine-tunes"** — REMOVED. Fine-tuning partially (397.6 vs. 500 max) while being inefficient in adaptation steps is not a contradiction; the two metrics are complementary.

4. **"The self-adaptive search is 'highly time-consuming' — it is plausible a cheaper strategy was used"** — REMOVED. This is speculation without evidence and contradicts the paper's explicit statement about using Self-Adaptive.

5. **"No detail is given on how d' is decided for the self-adaptive approach"** — PARTIALLY REMOVED. The paper does describe the approach: "we transform expansion into a decision-making process by considering the number of causal variables added to the graph as actions. Inspired by Xu et al. (2018), we define the state variable to reflect the current causal graph and derive the reward based on changes in predictive accuracy" (lines 189-190). More detail would be welcome but the approach is described.

## Novel Insights

The critical tension revealed by cross-referencing the reviews is that the paper's central claimed contribution — automatic detection of *what type* of change occurred — rests on the weakest component (a heuristic prediction-error threshold). The rest of the framework (causal representations, structural masks, self-adaptive expansion search, pruning) is coherent and well-supported by ablations. This suggests the paper's real strength may be its causal representation and expansion pipeline rather than the binary detection step, and reframing the contribution around "structured adaptation to new variables with fallback mechanisms" rather than "precise detection of change type" would better align the claims with the evidence.

## Suggestions

1. Add comparisons with lifelong learning / dynamic architecture methods (DEN, PackNet, progressive networks) on the space expansion tasks (CartPole Tasks 3-4, CoinRun hard levels). This is the most impactful improvement for supporting the core claim.

2. Either (a) report full Atari 100K results (all 26 games) with human-normalized scores, or (b) provide a principled justification for the 5-game subset (e.g., they cover the range of mode/difficulty combinations).

3. Perform a robustness analysis of the detection threshold \(\tau^\star\) — show how performance changes when \(\tau^\star\) is varied (e.g., 0.5×, 1×, 2× the source loss).

4. Clarify how the binary masks \(D\) are optimized (relaxation method, thresholding schedule, etc.) to improve reproducibility.

5. Report numerical results with confidence intervals for CoinRun and simulated experiments to match the reporting standard used for CartPole and Atari.

## Score and Decision

The paper tackles an important and timely problem with a novel causal framework. The experimental results on the reported settings are strong. However, the evaluation has significant gaps: missing baselines for the space expansion claim (which is the paper's headline contribution) and limited Atari coverage without justification. The detection mechanism also merits stronger validation. These issues are addressable but weigh against acceptance in current form.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>