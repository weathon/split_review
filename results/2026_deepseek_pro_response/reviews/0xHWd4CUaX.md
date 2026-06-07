Now I have a clear calibration picture. Let me synthesize the final review.

**Round 1 bracket**: 3.5 – 5.5 (above COSTAR at 3.00, below ContraDiff at 5.67)

**Round 2 narrowing**: Read anchors at 3.50 (Generalist k-Server), 4.80 (Structured Predictive Representations), 5.00 (Defects4C). The paper under review has more structural validity issues than the 4.80 paper (unspecified action space, miscited baselines vs. limited evaluation scope) but more experimental breadth and a more original idea than the 3.50 paper.

Final score: **4.0**. The structural issues with reproducibility and baseline validity are significant enough to warrant rejection, but the ablation analysis and idea are not worthless.

---

## Summary
This paper proposes a framework combining contrastive pre-training of code graph embeddings with PPO-based reinforcement learning for automated code refactoring. The core idea is to replace handcrafted reward features with a composite reward that includes learned embedding dynamics alongside traditional code quality metrics and a semantic preservation signal, using a graph attention policy operating over the joint representation space.

## Strengths
- **Ablation supports the value of contrastive pre-training**: Table 2 shows that removing contrastive pre-training drops Syntactic Improvement from 83.7% to 76.2% (−7.5 pp), the single largest degradation among ablations. This directly supports the paper's central claim that learned representations matter.
- **Embedding dynamics correlate with refactoring quality**: Figure 2 reports Pearson's r = 0.72 between embedding-space movement (Δh) and Syntactic Improvement (SI), providing non-trivial evidence that the latent space captures meaningful refactoring signals beyond what random embeddings would produce.
- **Embedding-guided exploration shows concrete gains**: Replacing the Mahalanobis-based exploration with random exploration drops SI from 83.7% to 74.8% and MG from 27.9% to 21.8% (Table 2), demonstrating the exploration strategy contributes independently.
- **Reward component dynamics are interpretable**: Figure 3 shows a meaningful progression where traditional metrics dominate early stages (≈80% of reward) while embedding dynamics grow to ≈70% by stage 100, validating the design intuition that learned representations become more valuable for fine-grained optimization after coarse issues are resolved.

## Weaknesses

### Fatal
None.

### Major
- **The action space is never specified**: Section 3.1 states only that "A denotes the action space (possible refactorings)." The paper never enumerates what refactoring actions are available, how they are parameterized, how the policy selects among them, or how many discrete actions exist. Section 4.4 describes graph-level attention weights over node features but never connects this to action selection. Without a specified action space, the method is not reproducible and it is unclear whether the system performs genuine refactoring or merely produces transformations that score well on the reward.

- **Several baselines are miscited or inappropriate for refactoring**: (a) GraphRL is cited as "GNN policy with expert demonstrations" (line 203) but the reference (Darvari et al., 2024, lines 347–349) is "Graph reinforcement learning for combinatorial optimization: A survey and unifying perspective" — a survey paper, not a refactoring method. Using a survey as a baseline with quantitative results in Table 1 and Figure 1 is indefensible. (b) Code2Seq (Alon et al., 2018) is a code summarization model that generates natural language descriptions, not refactored code. (c) Graph2Edit (Cai et al., 2023) is described in its own reference as "Generating vulnerable code via learning-based program transformations" — a vulnerability generation paper, not a refactoring tool. No explanation of how any of these were adapted for refactoring is provided. These issues directly undermine the credibility of the comparative evaluation.

- **The contrastive augmentations are unsubstantiated as semantics-preserving**: Section 4.1 claims that subtree masking ("Randomly removing AST subtrees while maintaining program validity"), edge rewiring ("Modifying non-critical control flow edges without altering semantics"), and identifier shuffling are syntax-preserving transformations for generating positive pairs. Removing AST subtrees or rewiring control flow edges can change program behavior. The paper provides no mechanism, criterion, or empirical validation (e.g., running test suites on augmented code) that these operations actually preserve semantics. Since contrastive pre-training is foundational to the approach, this gap undermines the central premise of learning "refactoring-aware" representations.

- **Evaluation metrics substantially overlap with the reward function, threatening comparison fairness**: The SI metric measures reduction in PMD/Checkstyle violations (Section 5.1), while the reward function's "traditional metrics" component explicitly includes style violations (Section 4.2). The SP metric measures test case pass rate, while the reward uses differential test verification (δ_t). The proposed method is rewarded during training for the same quantities it is later evaluated on, while the baselines — particularly the non-RL ones — were not trained against equivalent signals. This alignment inflates the apparent performance advantage.

### Minor
- **δ_t notation is inconsistent between sections**: Section 4.2 defines δ_t as a binary indicator I[test(G_t) = test(G_{t-1})], while Section 4.5 defines it as a continuous Hamming-distance-based score. The conceptual intent is consistent (4.5 provides the actual implementation), but the conflicting definitions and notation reuse create confusion.
- **No variance, standard deviation, or confidence intervals reported**: Tables 1–3 and Figure 1 report only point estimates. Performance differences between methods are sometimes as small as ~4 percentage points (e.g., Ours 83.7% vs. NeuroRefactor 79.4% SI), where variance across runs or data splits could account for the gap. Figure 1 also shows both methods converging to approximately the same asymptotic reward (~0.85), which is inconsistent with the claim of superior final performance.
- **Cross-language transfer drops are understated**: Table 3 shows SI dropping from 83.7% (Java) to 68.7% (Python) and 63.5% (C++) — substantial degradation. The paper describes this as "reasonable performance" without discussing the magnitude of the drop.
- **Background section describes GCN but method uses GAT**: Section 3.3 presents the GCN message-passing formulation (Eq. 3), but the actual method uses graph attention networks (Section 4.4, Implementation Details). The background is not well-aligned with the method.

### Trivial
- Two citations from Section 2.3 (Prasad & Srivenkatesh, 2025; Ye et al., 2025) do not appear in the reference list.

## Nice-to-Haves
- Comparison against LLM-based refactoring tools would strengthen the evaluation given the 2026 date.
- An analysis of what the contrastive embeddings actually capture (e.g., nearest-neighbor retrieval, probing classifiers) would strengthen the representational claims beyond the correlation in Figure 2.
- The paper freezes the encoder during RL training (Section 4.6) but never justifies why fine-tuning is not used, especially given the potential distribution shift between pre-training data (CodeSearchNet) and refactoring data.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "most often do last year" and other garbled text** — REMOVED per formatting/typo rule. These are parser/language-polishing artifacts, not substantive issues.
- **Harsh Critic: Related work citations from atypical venues (researchgate.net, academia.edu)** — REMOVED per the rule that all cited works are treated as real. The Marvellous et al. and Polu references do appear in the reference list.
- **Harsh Critic: "Three claimed contributions are not individually novel"** — REMOVED as overly subjective framing criticism. The paper does combine components in a specific way and evaluates the combination. The method's novelty is better assessed through the specific weaknesses above.
- **Strength Finder: "Broad evaluation across five complementary metrics"** — REMOVED as generic. Having multiple metrics is standard practice, not a distinctive strength.
- **Harsh Critic: Missing LLM-based refactoring baselines as a structural omission** — DEMOTED to Nice-to-Have. This is a scope expansion request, not a flaw in what the paper actually does.
- **Harsh Critic: The Section 4.3 exploration uses pre-training covariance that may differ from RL state distribution** — REMOVED. This is speculative; the ablation in Table 2 empirically shows the exploration strategy helps, which answers the concern.
- **Harsh Critic: Section-by-section presentation complaints (abstract incoherence, generic discussion)** — REMOVED per formatting/presentation rules. These are presentation quality issues, not technical flaws.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- **Specify the action space concretely**: Enumerate the available refactoring operations, their parameterization, and how the policy selects among them. Without this, the method description is incomplete and the system is not reproducible.
- **Replace or properly adapt the miscited baselines**: GraphRL (Darvari et al., 2024) is a survey and cannot serve as a baseline. Either substitute actual refactoring systems or clearly document how existing models were adapted for refactoring.
- **Validate contrastive augmentations**: Run test suites on original vs. augmented code to verify semantics are preserved, or acknowledge the approximation and discuss implications for the learned representations.
- **Disentangle evaluation from the reward function**: Measure SI and SP using held-out signals (e.g., different linting tools, human judgments) not used in the reward computation, to ensure a fair comparison with baselines.
- **Report variance across multiple runs** for all results in Tables 1–3.

---

## Anchor Comparison

| Anchor | Path | Score | Round | Comparison |
|---|---|---|---|---|
| COSTAR (safe RL + contrastive) | hZztyfmr8n | 3.00 | R1 | Paper under review has broader experiments and more concrete ablation results; clearly stronger |
| FALCON (LLM + RL for code) | N18Z2MkMEa | 3.00 | R1 | Similar quality tier; paper under review has more structural issues but also more original idea |
| Generalist k-Server (RL+GNN) | gCSEQIgbWH | 3.50 | R2 | Paper under review has more original idea and broader experiments but more severe validity issues (miscited baselines, unspecified action space) |
| Structured Predictive Reps (GNN+RL) | sEv6vHIUnu | 4.80 | R2 | Anchor has a complete, reproducible method with valid comparisons but limited evaluation scope; paper under review has more structural validity gaps |
| Defects4C (program repair benchmark) | gXK3Y6WNVv | 5.00 | R2 | Anchor is a solid dataset contribution with limited novelty; paper under review is weaker due to structural validity issues |
| ContraDiff (contrastive+RL) | XMOaOigOQo | 5.67 | R1 | Anchor has theoretical justification issues but comprehensive experiments and clear method; paper under review is clearly weaker |
| CoRNStack (code retrieval) | iyJOUELYir | 6.25 | R1 | Strong, complete contribution; paper under review is substantially weaker |

**Final bracket**: 3.5 – 5.0 → narrowed to **4.0**. The paper has a reasonable idea and some supporting evidence, but the structural issues — unspecified action space, miscited baselines, unvalidated core augmentations, and evaluation/reward circularity — prevent the experimental results from credibly supporting the claims. These issues are more fundamental than the scope/overclaiming problems that characterize the 4.80 anchor but the paper has more substance than the 3.50 anchor.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>