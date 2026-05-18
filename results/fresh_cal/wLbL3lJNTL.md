Now I have a clear picture. Let me produce the final consolidated review.

## Summary

This paper proposes learning joint representations from multiple sensor modalities (images and proprioception) for reinforcement learning using Recurrent State Space Models (RSSMs). The key idea is to assign reconstruction-based losses to clean low-dimensional sensors (proprioception) and contrastive losses to high-dimensional noisy sensors (images), rather than the common practice of learning image representations in isolation and concatenating them with proprioception. The method is evaluated across two RL paradigms (model-free and model-based), two visual modalities (color and depth), four task suites (including new challenging benchmarks), and a large set of baselines. The evidence consistently shows that joint representations significantly outperform concatenation-based approaches and enable solving tasks where image-only methods fail entirely.

## Strengths

1. **Per-sensor loss selection is well-motivated and validated.** The paper proposes using reconstruction for clean low-dimensional proprioception and contrastive losses for noisy high-dimensional images. This is directly supported by ablation results: Joint(CV+R) and Joint(CPC+R) consistently outperform purely contrastive Joint(CV+CV)/Joint(CPC+CPC) and purely reconstruction-based Joint(R+R) across all task suites (Figures 2–5).

2. **Joint representations systematically outperform concatenation.** Across all four task suites, joint approaches (Joint(CV+R), Joint(CPC+R)) consistently and significantly outperform the corresponding concatenation baselines (Concat(R), Concat(CV), Concat(CPC)). This is the paper's core claim and it is thoroughly supported, with especially large gaps on Occlusions (Fig. 3) and Locomotion (Fig. 4).

3. **Solves tasks that are intractable for all image-only SOTA methods.** On the Occlusion suite (Fig. 3), every image-only baseline — DreamerPro, DBC, TIA, DenoisedMDP, DrQ-v2 — achieves near-zero performance, while Joint(CPC+R) achieves substantial and reliable performance. This qualitative finding is robust and demonstrates that combining modalities with appropriate losses unlocks capabilities no single-modality approach can achieve.

4. **Broad and rigorous evaluation.** The paper evaluates across model-free (SAC) and model-based (Dreamer) RL, both color and depth images, 7 DMC tasks × 3 visual conditions, a new 6-task Locomotion suite, and a realistic mobile manipulation task. Statistical reporting follows best practices (IQM + 95% stratified bootstrap CIs).

5. **Introduces useful new benchmarks.** The Occlusion and Locomotion suites fill genuine gaps in the existing evaluation landscape for representation learning in RL.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Baseline comparison transparency is under-documented.** The paper claims to "outperform several SOTA baselines" (Dreamer-v3, DreamerPro, DBC, TIA, DenoisedMDP, DrQ-v2) but does not explicitly state whether these baselines were re-run under identical conditions or whether numbers were taken from original papers. This matters most for fine-grained comparisons on standard images. However, this does **not** threaten the paper's core claims for two reasons: (a) the most striking results (Occlusions, Fig. 3) show image-only SOTA methods at near-zero performance — a gap far too large to be explained by tuning differences; (b) the paper honestly acknowledges that its Img-Only(R) "cannot quite match the performance of Dreamer-v3 and DreamerPro on Standard Images" (line 139), showing measured claims. Clarifying the source of each baseline number would eliminate this concern.

2. **Model-based evaluation omitted on the most realistic task.** The paper's finding that joint representations "almost close the gap between model-free and model-based for contrastive image losses" (line 127) is one of its most interesting insights, but this claim is not tested on OpenCabinetDrawer (the hardest, most realistic task) because the paper only reports model-free results there. The paper acknowledges and explains this ("we still find that model-free methods perform better for contrastive representations and thus only consider those for the Locomotion suite and OpenCabinetDrawer," line 127), but the omission leaves the generalizability claim about model-based RL weaker than it could be. Adding this experiment or explicitly narrowing the scope of the claim would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- **Ablate the reward prediction loss for model-free agents.** The paper includes an auxiliary reward prediction loss even for model-free agents (following Srivastava et al., 2021). An ablation removing it would clarify whether the improvement comes from the joint representation itself or from this auxiliary loss, which model-free baselines like DrQ-v2 do not use.
- **Quantitative analysis of learned latent spaces.** The qualitative saliency maps (Fig. 6) are informative but could be complemented with metrics such as linear probing accuracy for task-relevant factors or mutual information between latent dimensions and ground-truth state variables.
- **Computational cost comparison.** A brief note on training time or parameter counts between joint and concatenation approaches would help practitioners assess the trade-off.

## Removed Points

*These points were removed per the filtering rules; treat with caution if encountered elsewhere.*

- **Hyperparameter not disclosed** (Harsh Critic's "Missing Parts"): The paper references code availability and a supplement (line 104, 157). Hyperparameters (batch size, learning rate, KL weighting, etc.) are standard appendix content that the parser strips. Removed per hard rules about missing appendix content.
- **OpenCabinetDrawer task details missing**: Likely in the stripped appendix. Same rationale as above.
- **Dreamer-v3 vs. Img-Only(R) confusion** (Harsh Critic's Critical Issue 1 framing): The critic suggests the paper's Img-Only(R) is claimed to be Dreamer-v3 and raises concerns. In fact, the paper lists Dreamer-v3 as a *separate* baseline (line 108) and honestly states Img-Only(R) "corresponds largely to Dreamer-v1" (line 110). This criticism misreads the paper and is removed.
- **Generic "evaluation lacks rigor" style criticisms**: The critic's overall framing of the baseline issue as an "evidential issue" is too strong given the core claims are unaffected and the qualitative gaps are large; this has been demoted to a Minor point.

## Novel Insights

The harsh critic's observation that the joint representation nearly closes the model-free vs. model-based performance gap for contrastive agents (Fig. 2, 3) surfaces an important subtlety that the paper itself does not fully emphasize: the benefit of joint representations is not uniform — it is largest precisely where the individual modalities are weakest individually. Contrastive image-only representations struggle with dynamics learning for model-based RL (a known issue), but adding reconstruction-based proprioception into the joint latent space provides a strong dynamics signal that almost eliminates this gap. This suggests the value of multi-sensor representations may be synergistic rather than merely additive: each sensor's loss function compensates for specific failure modes of the others.

## Suggestions

1. In a final version, add a short paragraph or table clarifying the source of each baseline result (re-implemented in the same codebase vs. taken from original papers) and, for re-implemented baselines, how hyperparameter tuning was handled.
2. Consider adding the model-based results on OpenCabinetDrawer, even if only as an appendix figure, to fully support the claim about joint representations improving contrastive model-based RL.
3. Add a brief ablation on the reward prediction loss for model-free agents to clarify whether the improvement is from the joint representation or the auxiliary loss.

## Score and Decision

**Originality**: The per-sensor loss assignment (reconstruction for clean low-D, contrastive for noisy high-D sensors) within RSSM-based joint representations is a novel and well-motivated combination that prior work has not systematically explored.

**Importance of research question**: Multi-sensor RL is practically important (most real robots have both cameras and proprioception), and the paper addresses a genuine gap: the common practice of concatenating independently learned representations is shown to be suboptimal.

**Claims well supported**: The core claims (joint > concatenation, combined losses > pure contrastive or pure reconstruction) are supported by consistent results across diverse settings. The minor transparency issue about baseline sourcing does not undermine these core claims.

**Soundness of experiments**: Rigorous methodology (IQM + bootstrap CIs, multiple seeds, multiple task suites, multiple RL paradigms). Some nice-to-have ablations are missing but not essential.

**Clarity**: Well-written and clearly structured.

**Value to community**: The method is actionable for practitioners, the benchmarks fill a gap, and the findings about joint representations for contrastive model-based RL are informative.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>