Here is the final consolidated review.

---

## Summary

The paper proposes CFOHLR, a meta-RL framework for zero-shot task-level adaptation. It introduces two innovations: (1) a coarse-to-fine policy refinement where language-guided expert selection (coarse) is combined with a hypernetwork-generated task-aware policy (fine), and (2) a holistic-local contrastive representation that structures task representations at both the category level and the instance level. Experiments on Meta-World ML-10 and ML-45 report ~42–45% improvement over prior methods.

## Strengths

- **Well-motivated hierarchical design that mirrors the structure of task-level adaptation.** The paper correctly identifies that task-level adaptation has two natural levels (across categories and within categories) and designs both the policy and representation components to reflect this hierarchy. This is a principled architectural choice that directly connects the problem diagnosis to the method design.

- **t-SNE visualization provides direct empirical evidence of the intended representation structure.** Figure 3b shows clear separation of test task categories in the learned representation space. Each task category forms a distinct cluster, validating that the contrastive losses produce the claimed inter-category distinctiveness and intra-category structure.

- **Ablation study confirms both components contribute.** Removing either the coarse-to-fine policy (CFO) or the holistic-local contrastive representation (HLR) degrades performance, and their combination yields the best results. This provides causal evidence for the two claimed innovations.

- **Computationally efficient language processing via a fixed pre-trained DistilBERT encoder** avoids the heavy data requirements of training a transformer from scratch (as in Million), a practical design choice for the online meta-RL setting.

## Weaknesses

### Major

1. **Coarse-to-fine policy combination mechanism is not specified.** This is the paper's central architectural claim, but the text never explains how the coarse policy (weighted sum of expert modules) and the fine policy (hypernetwork-generated task-aware policy) are actually combined. The paper says "the output from the coarse policy is then fed into a refinement stage" and "refine this policy using the task-aware control policy" (Section 3.2), but the exact mechanism is absent. Is the final action an additive combination? Does the hypernetwork modify the coarse policy network's weights? Does the fine policy reweight the experts? The hypernetwork takes the task representation $z_t$ as input, not the coarse policy output (line 97), so the interaction path is unclear. A reader cannot implement or evaluate the core contribution based on the description as written.

2. **Training of the skill-specific expert modules is not described.** The paper introduces $k$ "skill-specific expert modules" ($\pi_{\text{expert}}^j$) that are central to the coarse policy (Eq. 3), but never specifies: (a) how they are trained (pre-trained on specific task subsets? jointly trained end-to-end?); (b) what $k$ is; (c) what skills correspond to which modules; or (d) whether the experts specialize through any auxiliary loss or emerge from random initialization. These are not minor details — the expert modules constitute half of the coarse-to-fine contribution.

3. **Key hyperparameters and architectural details are missing.** The composite loss weights $\lambda_{\text{HCR}}$ and $\lambda_{\text{LCR}}$ are named but never given values. The number of expert modules $k$ is never specified. The architectures of the hypernetwork $\mathcal{H}$, the expert policy modules, the optimizer, learning rate, and batch size are all absent. Critically, Meta-World does not natively include language descriptions — how language instructions were obtained for the 50 task types is not explained. These omissions collectively prevent reproducibility.

### Minor

4. **The large reported improvements (42.3%, 45.4%) are ambiguous.** The paper does not clarify whether these are relative or absolute percentage improvements. A 42.3% relative improvement (e.g., 40% → 56.9%) and a 42.3 percentage-point absolute improvement (e.g., 40% → 82.3%) would make very different claims, and both would be unusually large for this benchmark. This should be disambiguated.

5. **The ablation study does not isolate the individual contributions of the holistic vs. local contrastive losses.** The HLR variant ablates both contrastive losses together (Table 2), so it is unclear whether the holistic category-level contrast, the local instance-level contrast, or both are responsible for the gains. Since instance-level contrastive learning in meta-RL is already established (FOCAL, Moss), a finer-grained ablation is needed to justify the novelty of the holistic component specifically.

6. **Evaluation is limited to a single benchmark (Meta-World).** While Meta-World is standard for task-level adaptation, testing on at least one additional environment (e.g., Procgen or a custom hierarchical task suite) would substantially strengthen the claim of generalizability.

### Trivial

7. Notation typo: "$N_{\text{cucgory}}$" in Eq. 6 should be "$N_{\text{category}}$."

8. Minor inconsistency: the expert weights $\alpha_j$ are described as "derived from the attention mechanism" (line 84), but the preceding equation (line 78–79) shows they are computed by a fully connected layer with softmax — a linear projection, not an attention mechanism.

## Nice-to-Haves
- Analyze whether the expert modules develop meaningful specialization (e.g., visualize activation patterns across language instructions).
- Report whether the ablation differences are statistically significant across the 5 random seeds.
- Supplement the t-SNE visualization with a quantitative metric (e.g., inter/intra-category distance ratio).

## Removed Points
These points were raised by reviewers but are either parser artifacts, misreadings, or not verifiable from the paper:

- *"Tables are rasterized images and inaccessible"* — This is a PDF-to-text parsing artifact. The original submission has proper tables.
- *"Holistic contrastive loss is undefined for the evaluation protocol since test categories are unseen"* — The holistic loss is a training-time objective applied to training categories (which have parametric variants). At test time the representation space is fixed and transferred. The paper provides t-SNE evidence and an ablation showing HLR contributes. The concern is reasonable as a call for finer-grained analysis (captured in Minor point 5) but not as a structural flaw.
- *"The critique of SDVT is asserted rather than demonstrated"* — This concerns how the paper positions itself against related work, not a weakness of the proposed method.
- *"The claim that Million demands large training data is stated without evidence"* — This is a characterization of a baseline, not a core flaw.
- *Generic area-of-concern sweeps* (whether confounders are controlled, whether the metric measures a proxy) — Lacked specific anchors in the paper.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Specify the coarse-to-fine combination mechanism precisely** — provide an equation for how $\pi_{\text{coarse}}$ and $\pi_{\mathcal{H}(z_t)}$ produce the final action distribution. A computational graph diagram would help.
2. **Describe how the skill-specific expert modules are trained and what $k$ is.**
3. **Disambiguate whether the 42.3%/45.4% improvements are relative or absolute.**
4. **Add a finer-grained ablation separating the holistic and local contrastive losses.**
5. **Report all key hyperparameters** ($\lambda_{\text{HCR}}$, $\lambda_{\text{LCR}}$, learning rate, architecture details) and explain how language descriptions were obtained for Meta-World tasks.

## Score and Decision

This paper addresses an important problem and has a sensible high-level design. However, it suffers from a significant specification gap: the core coarse-to-fine combination mechanism — the paper's primary claimed contribution — is not concretely described. Combined with the missing training details for the expert modules and absent hyperparameters, the method is not reproducible from the current submission. While the high-level ideas are interesting, the paper does not meet the standard of completeness required for a top-tier venue.

**MY FINAL SCORE:** <score>4.5</score>
**MY FINAL DECISION:** <decision>Reject</decision>