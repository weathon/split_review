- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3
Now I have all the evidence I need. Let me compile the final review.

## Summary

NMCLK proposes a noisy multi-view contrastive learning framework for knowledge-aware top-K recommendation, generating three graph views (collaborative via LightGCN with noise, semantic via a KNN item-item graph, structural via attention-based KG aggregation) and applying multi-level cross-view contrastive learning plus alignment/uniformity constraints.

## Strengths

- **Three complementary graph views with multi-level contrastive learning**: The paper explicitly designs collaborative (user-item graph, LightGCN-based), semantic (KNN item-item graph), and structural (full user-item-entity graph, attention-based) views and applies both local-level (collaborative vs. semantic) and global-level (combined vs. structural) contrastive learning (Sections 4.1.1–4.2.2). This goes beyond single-view KG-aware methods like KGAT or KGCN. Table 2 shows NMCLK improves over KGAT on ML-100K and KGCN on ML-1M.

- **Incorporation of feature alignment and field uniformity constraints**: The framework adapts alignment/uniformity objectives from representation learning theory (Wang et al., 2022) to the recommendation setting, pulling same-field item features together and pushing different-field features apart (Section 4.3, Eqs. 11–12). This is a principled addition to contrastive learning that is concretely instantiated in the multi-task loss (Eq. 15).

## Weaknesses

### Fatal
None.

### Major

- **Outdated baselines and unsubstantiated SOTA claim**: The latest baseline included is KGIN (2021). The paper claims "state-of-the-art performance" but does not compare against any method from 2022–2026, despite citing SimGCL (a 2022 contrastive recommendation method) in the method section itself (line 110). The stated improvements over KGAT and KGCN are legitimate, but they do not establish the claimed superiority over contemporary contrastive or KG-aware recommenders. The SOTA claim is unsubstantiated by the evaluation presented.

- **Complete absence of ablation studies**: The model contains multiple interacting components — three views, noise injection, local and global contrastive losses, feature alignment loss, field uniformity loss, and five loss coefficients. The paper performs zero ablation analysis to isolate the contribution of any single component. It is impossible to determine whether gains come from the multi-view design, the noise, the alignment/uniformity constraints, or simply careful tuning. For example, one cannot tell whether the "noise addition module" (in the title and abstract) adds any value over the same framework without noise.

- **Noise injection mechanism is critically underspecified**: The noise injection — central to the model's identity ("Noisy" in the name) — is described in only two sentences (lines 91 and 110): "we adopt a matrix-wise perturbation technique" that "introduces varied uniform noises to distinct parameter matrices, contingent on the standard deviations of the parameters," and "we also perform a similar addition of noise to the generated user and item embeddings." No equation specifies the noise distribution, its scale/range, whether it is applied per-step or once, or any hyperparameter governing its magnitude. This prevents reproducibility and meaningful assessment of the claimed robustness benefits.

- **No statistical significance or variance reporting**: All results in Table 2 are single-point estimates without standard deviations, confidence intervals, or significance tests. Given the test set (20% of ~100K interactions), differences between methods could be within noise. This weakens the reliability of every comparative claim.

- **No hyperparameter sensitivity analysis**: Five loss coefficients (α=0.2, β=0.1, λ=0.01, γ=0.5, δ=0.05) are fixed at single values with no sensitivity study (Section 4.5). For a framework with many tunable terms, the absence of any analysis showing that results are robust to these choices is a significant gap.

### Minor

- **Evaluation limited to two small, same-domain datasets**: Both ML-100K and ML-1M are from the movie domain. The abstract mentions "extensive experiments on CTR task-based datasets" but these are deferred to supplementary material not presented in the main paper, weakening the claim of generalization.

- **"Model-agnostic" claim undemonstrated**: The contribution bullet states NMCLK is "model-agnostic" (line 48), but no experiment replaces the collaborative or structural backbone with a different KG-aware model to verify this property.

- **Conclusion mentions "textual and visual aspects" not discussed elsewhere**: Line 323 states the framework "merges item representations from multiple views, including textual and visual aspects," but neither textual nor visual modalities appear in the method or experiments. This appears to be a carryover from another draft.

- **View naming is inconsistent between abstract and method**: The abstract uses "global-level structural view," "item-item semantic view," and "local view," while Section 4 uses "collaborative view," "semantic view," and "structural view." The mapping is inferable but never explicitly stated, making the paper harder to follow.

### Trivial
None that survive filtering.

## Nice-to-Have
- A sensitivity curve over noise magnitude would greatly strengthen the claimed noise contribution.
- Including SimGCL, NCL, or other recent contrastive KG recommenders as baselines would substantiate the SOTA claim.
- Replacing the collaborative/structural backbone with a different model (e.g., KGCN) would substantiate the "model-agnostic" claim.
- Reporting standard deviations over multiple runs is standard practice.

## Removed Points
- **Claim about redundant contribution bullets**: The harsh critic asserted the third contribution bullet repeats the second bullet. The paper's three bullets are distinct (framework introduction, three learning signals, experimental validation) — this criticism was factually wrong.
- **Equations poorly formatted / missing brackets**: These are parser artifacts from PDF extraction, not author errors.
- **"[32]" in braces in Semantic View Encoder**: Acknowledged as likely a formatting artifact by the critic. Not an author error.
- **Missing related works**: SimGCL is cited in the method section. The paper's related work is limited compared to recent literature, but this is subsumed under the outdated-baselines weakness in evaluation, not a standalone criticism.
- **License/dataset version not stated**: Trivial standard-practice nitpick not substantive enough for this review.
- **Training efficiency / convergence analysis requested**: A nice-to-have, not a weakness of the presented work.

## Novel Insights

None beyond the paper's own contributions. Both reviews accurately characterize the paper's central tension: it assembles several established techniques (LightGCN, GAT-style KG aggregation, SimGCL-style noise, alignment/uniformity) into a multi-view contrastive framework, but the evaluation is too incomplete (outdated baselines, no ablations, underspecified noise mechanism) to establish whether the assembly yields a genuine advance or simply reflects engineering effort.

## Suggestions
1. Add at least 2–3 recent (2022+) contrastive or KG-aware recommenders (e.g., SimGCL, NCL, KGRec) as baselines. Without this, the SOTA claim is indefensible.
2. Perform component-wise ablation: remove each view, remove noise, remove each loss term. Report the results in a table.
3. Specify the noise injection with an equation: distribution family (e.g., Uniform(-ε, ε)), scale ε, and whether it is applied per training step.
4. Report mean and standard deviation over at least 3 random seeds.
5. Conduct sensitivity analysis on at least α (local vs. global contrastive ratio) and the noise magnitude.
6. Clarify the view naming and mapping from abstract to method (Table or explicit sentence).
