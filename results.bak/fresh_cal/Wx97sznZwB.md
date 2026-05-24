Now I have all the information I need. Let me synthesize the consolidated review.

## Summary

This paper proposes COPL (CLIP-guided Open-vocabulary Policy Learning), a method for training RL agents in Minecraft to follow language instructions involving unseen objects. The key idea is to use a modified MineCLIP to produce 2D confidence maps locating the target object from the instruction, then use these maps as both the policy input (replacing text embeddings) and as a dense intrinsic reward (the "focal reward"). Experiments in Minecraft's MineDojo benchmark show that COPL's focal reward significantly outperforms the standard MineCLIP reward in single-task learning, and that training with confidence maps as input enables zero-shot transfer to tasks with novel objects.

## Strengths

1. **Focal reward clearly outperforms MineCLIP reward in single-task settings.** Figure 5 shows across four hunting tasks (cow, sheep, pig, chicken) that the focal reward reaches 60–80% success while MineCLIP reward and ND_CLIP reward both stay below 20%. This is a clean, well-controlled result supported by multiple seeds.

2. **Ablation studies isolate contributions of denoising and the Gaussian kernel.** Figures 6(a)–(d) systematically compare raw vs. denoised focal rewards and with/without the Gaussian kernel in a two-target setting, showing that both design choices are meaningfully justified by the experimental evidence.

3. **Controlled multi-task comparison varying only the target representation.** On hunt-domain training tasks (Figure 7a), COPL (confidence map input), EmbCLIP (text embedding input), and One-Hot are trained with the same focal reward, differing only in target representation. COPL's large margin isolates the advantage of the spatial confidence map over text embeddings.

4. **Evaluation on two distinct task domains (hunt and harvest) with different behavioral patterns.** The paper shows COPL generalizes to novel objects in both domains, and in the harvest domain outperforms EmbCLIP on novel tasks despite similar training performance, demonstrating robustness across skill types.

5. **Precision metric complements success rate to confirm discrimination.** Figures 7(c) and 8(d) report precision (correct kills/harvests on the specified target), showing that the agent genuinely identifies the specified target rather than acting indiscriminately.

## Weaknesses

### Fatal

None.

### Major

1. **Missing EmbCLIP baseline in the hunt-domain open-vocabulary test.** The paper's central claim is that confidence maps as policy input enable better open-vocabulary generalization than text embeddings. The authors correctly compare COPL vs. EmbCLIP on *training* tasks (Figure 7a), but for the *open-vocabulary* generalization test in the hunt domain—arguably the strongest test case—Figures 7(b) and 7(c) only compare COPL against Cai et al. and STEVE-1 (both imitation learning methods with different training paradigms). EmbCLIP is entirely absent from these plots. The harvest-domain open-vocabulary tests (Figures 8c,d) *do* include EmbCLIP, and COPL outperforms it there. But the hunt domain is where the largest performance gap on training tasks was observed, and the authors themselves characterize the harvest tasks as "easier" where "the impact of the target representation's complexity diminishes." This means the best available evidence for the confidence map's benefit in the hardest cases comes from the easier domain only. Without the EmbCLIP comparison in the hunt-domain open-vocabulary evaluation, the reader cannot fully attribute the generalization to the *representation choice* rather than to other factors. This is the most significant gap in the paper's empirical support for its central thesis.

### Minor

1. **Segmentation quality of the modified MineCLIP is not quantitatively evaluated.** The paper presents qualitative examples (Figure 3) but reports no metric (e.g., patch-level detection rate, pixel-level IoU where ground truth is available) for how often the confidence map correctly localizes the target. Since both the focal reward and the policy input depend on this pipeline, a failure mode exists: if segmentation quality degrades for novel objects, the open-vocabulary claim could be weakened without indicating whether the limitation is in the policy or the VLM.

2. **Analysis of why MineCLIP reward fails relies on a single qualitative trajectory.** Figure 4 shows one episode of "milk a cow" to illustrate that the MineCLIP reward is uncorrelated with distance. While the claim is supported by prior work (Cai et al., 2023), and the single-task experimental results (Figure 5) provide strong *outcome* evidence, the causal story would be strengthened by quantitative analysis (e.g., correlation coefficient between reward and distance over many episodes).

3. **Target extraction via ChatGPT is acknowledged but not evaluated.** The paper notes that ChatGPT extracts the target noun from instructions (Section 3.3), but no analysis of extraction reliability is provided. Errors at this step would cascade into both segmentation and reward computation.

4. **Focal reward ablation tests only one scenario.** The Gaussian kernel ablation (Figures 6c,d) is tested with two targets in the scene. A broader test across tasks or target configurations would strengthen the generalization of the ablation claim.

5. **No failure analysis for the zero-confidence-map case.** The paper does not discuss what happens when the target is not in view and the confidence map is all or mostly zeros. Does the agent wander randomly? Is this a known failure mode?

### Trivial

None.

## Nice-to-Haves

- Quantitative analysis of the focal reward's distance correlation (e.g., reward vs. distance over many trajectories) to substantiate the causal story.
- Sensitivity analysis for hyperparameters: focal reward Gaussian kernel width (σ), threshold (τ = 0.2), and reward weight (λ = 5).
- Quantitative segmentation metrics (e.g., patch-level detection rate) on the objects used in experiments, to distinguish policy failures from VLM failures.

## Removed Points

The following points from the inputs were evaluated and either found factually incorrect or filtered per the rules:

- **Strength Finder point 1** (claiming EmbCLIP is shown in Figures 7b–c with near-zero success): **Incorrect.** EmbCLIP does not appear in Figures 7b–c. The harvest-domain open-vocabulary tests (Figures 8c–d) do include EmbCLIP, and COPL outperforms it there. This strength is removed because it misattributes the evidence.
- **Harsh critic point 3** ("open-vocabulary claim conflates VLM's zero-shot ability with the policy's generalization"): **Removed.** The paper is reasonably clear that the open-vocabulary capability is *inherited* from MineCLIP's segmentation and that the contribution is about *using* VLM outputs in RL. The abstract and Section 3.3 both explain this mechanism explicitly ("We leverage the capability of CLIP to segment the target object…"). This is not a conflation; it is a correct description of a pipelined approach.
- **Harsh critic mention of "missing related works"** : **Removed per rule.** I cannot confirm the existence of missing references without external sources.
- **Criticisms about typos, formatting, missing appendix content, or reproducibility nitpicks**: **Removed per rules** as these reflect parser errors or standard practices.

## Novel Insights

None beyond the paper's own contributions. The reviews predominantly surface an evidential gap (missing baseline) rather than uncovering a deeper conceptual insight about the method or problem.

## Suggestions

The most impactful improvement would be adding EmbCLIP results to the hunt-domain open-vocabulary evaluation (Figures 7b–c). This single addition would either confirm the central claim (if COPL significantly outperforms EmbCLIP on novel hunt objects, as it does in the harvest domain) or reveal task-dependent benefits, which would also be valuable. Additionally, adding quantitative segmentation quality metrics and a brief failure analysis for out-of-view targets would preempt common reviewer concerns and strengthen the reproducibility of the work.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>