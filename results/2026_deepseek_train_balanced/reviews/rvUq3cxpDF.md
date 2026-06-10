## Summary

LFO introduces an unsupervised method for recovering latent action representations from purely observational video data. The key idea is to jointly train an inverse dynamics model (IDM) and a forward dynamics model (FDM) with a vector-quantized information bottleneck, forcing the IDM to encode only transition-specific information needed for future-state prediction. The resulting latent-action policies can be fine-tuned online or decoded offline with minimal labeled data to recover expert-level performance. Experiments across all 16 games of the Procgen benchmark show that the learned latent spaces align with true action structure and enable substantially faster online RL than PPO from scratch.

## Strengths

- **Compelling qualitative evidence of action-structure recovery**: UMAP projections across all 16 Procgen games (Figure 5) show that LFO's unsupervised latent actions form clusters that cleanly align with ground-truth discrete actions, despite zero action labels during training. This directly and strongly supports the paper's central claim that comprehensive action information can be recovered from pure video.

- **VQ bottleneck is principled and empirically validated**: The "RL, no-SL, no-VQ" ablation (Figure 1) degrades performance relative to the full method, confirming that vector quantization is causally important. The paper provides a clear theoretical justification: VQ forces the IDM to reuse a limited set of discrete codes across the state space, promoting state-invariant latent actions that are easier to decode (lines 92–93).

- **Online fine-tuning demonstrates practical utility**: The latent policy fine-tuned for 4M online frames recovers expert performance and exceeds it in 9/16 games, while PPO from scratch reaches only 44% of expert performance over the same budget (Figure 1). This head start is substantial under the paper's stated setting (abundant video, limited interaction budget).

- **Clean, well-motivated method**: The predictive-consistency objective between IDM and FDM, with VQ as the information bottleneck, is clearly described (Section 4) and architecturally simple relative to the difficulty of the problem. The paper explicitly identifies and addresses ILPO's known mode collapse failure mode through specific design choices (IDM rather than policy, continuous latents rather than discrete).

## Weaknesses

### Fatal

None.

### Major

- **Insufficient evaluation of the closest baseline (ILPO)**: ILPO is the most directly related prior work, yet it receives only one sentence of experimental results (line 138: "immediately collapses in several Procgen tasks... when it does not collapse, online decoding did not perform better than PPO from scratch"). No per-environment results, no evidence of hyperparameter tuning for ILPO, and no quantitative comparison of the learned latent spaces are provided. The paper's architectural critique of ILPO (lines 44–45) is detailed and plausible, but the experimental dismissal is too cursory to convincingly establish LFO's superiority over its closest competitor.

- **Missing baselines that also leverage the 8M unlabeled frames**: The headline comparison (LFO with 8M pretraining + 4M online vs. PPO from scratch at 4M) conflates the benefit of LFO's specific representation learning approach with the sheer availability of 8M expert frames. The paper does not compare against simpler alternatives that also exploit the same unlabeled data, such as: (a) behavioral cloning on the 8M frames with true action labels (oracle upper bound), or (b) a VPT-style semi-supervised approach (train an IDM on ~200 labeled transitions, pseudo-label the remaining 8M, then BC). Without these, it is unclear whether LFO's specific latent-action pretraining provides a meaningful advantage over straightforward alternatives that also use the unlabeled data. This weakens the claim that the downstream results reflect the quality of the learned latent representation.

- **Offline decoding data-efficiency claim is uncontextualized**: The statement that "~200 labeled transitions exceed the performance of 4M steps of regular RL via PPO" (line 149) compares a decoder trained on 200 labels *on top of a full latent policy trained on 8M frames* against PPO from scratch. The more informative quantity would be how many labeled transitions LFO needs compared to alternatives that also use the 8M frames (e.g., BC on 200 labeled transitions, or VPT-style with 200 labeled + pseudo-labels). The absolute number "200" is impressive in isolation but its significance cannot be assessed without this context.

### Minor

- **No per-environment tabular results**: The paper relies entirely on figures (Figure 1, Figure 3) with no numerical table of mean returns and standard deviations per environment. Given that Procgen has 16 diverse games with known performance distributions, a table is important for reproducibility and cross-paper comparison. The aggregated plots hide potentially informative variation across environments.

- **The gap between the motivating scenario and the evaluation is large and unaddressed**: The paper motivates LFO for pretraining on "vast amounts of videos readily available on the web" (line 6) but evaluates on a homogeneous dataset of 8M frames from a single expert PPO policy on a single benchmark. Real web video has suboptimal/mixed-quality demonstrations, stochastic dynamics, camera motion, scene cuts, and task-irrelevant visual variation. The limitations section (lines 163–165) acknowledges stochasticity and delayed effects but does not test robustness to any of these factors. The paper is honest about being a "first step," but the framing exaggerates the demonstrated scope.

- **Key hyperparameters are not ablated**: The VQ codebook size, latent dimensionality, and dataset size (8M frames) are not ablated or even fully specified. The choice of k=1 context frames is described but not justified or varied. These are important for understanding the method's behavior and limitations.

- **The FDM (8M-parameter U-Net) is much more expressive than the IDM (IMPALA CNN)**: The paper does not discuss the risk that the FDM could "cheat" by predicting o_{t+1} from o_t alone using its powerful backbone, reducing the pressure on the latent bottleneck. The empirical results suggest this does not prevent the method from working, but the architectural asymmetry and its implications are not analyzed.

### Trivial

- No compute or runtime reporting, which would help assess practical feasibility.

## Nice-to-Haves

- An analysis of whether the behavior-cloning loss on latent actions predicts downstream fine-tuning performance would strengthen the validity chain.
- Ablating the context length \(k\) and exploring different VQ codebook sizes would improve understanding of the method's sensitivity.
- Testing robustness to at least one dimension of real-video messiness (e.g., mixed-quality trajectories, randomized backgrounds) would strengthen the claim of applicability to web video.

## Removed Points

- *"No citation evidence for ILPO mode collapse"* (Harsh Critic): Removed per the hard rule that citing a reference establishes its existence. The paper cites `ilpo_followup` and also reports its own experimental observation of collapse (line 138).
- *Criticism that the "first method" claim is overstated*: Removed. The paper explicitly distinguishes LFO from ILPO on architectural grounds (IDM vs. policy, continuous vs. discrete latents) and provides evidence. The claim is strong but supportable given the differences.
- *Reproducibility nitpicks about undisclosed hyperparameters and implementation details*: Removed per hard rule — these are trivial details impractical to include in a submission.
- *Strength Finder's generic strengths*: Removed claims that were generic, sycophantic, or not specifically grounded in paper evidence (e.g., "this paper addresses an important problem").
- *Criticism that the paper "should not be accepted because the experimental design does not rule out the alternative explanation that the benefit comes from having 8M frames of expert data"*: Weakened from fatal to major. The missing baselines are a significant gap but the paper's core contribution (action-structure recovery) is independently supported by the UMAP visualizations and is not invalidated by the comparison design.

## Novel Insights

Beyond the paper's own contributions, the cross-review reveals a striking asymmetry: the paper provides genuinely strong qualitative evidence for its core claim (action-structure recovery via VQ-bottlenecked predictive consistency) but comparatively weak quantitative evidence for the downstream benefits of this representation. The UMAP plots convincingly show that the latent space mirrors true actions — this is the paper's novel and well-supported finding. However, the downstream RL experiments, as designed, cannot rule out that simpler methods leveraging the same 8M unlabeled frames would achieve similar or better performance. This tension between the clean qualitative result and the under-powered quantitative evaluation is the central issue that future work should address.

## Suggestions

1. **Add a table** of per-environment mean returns and standard deviations for LFO, both ablations, PPO at multiple budgets, and at least one baseline that also uses the 8M unlabeled frames.
2. **Evaluate ILPO systematically** with per-environment results and proper hyperparameter tuning, or calibrate the novelty claim to not depend on outperforming it.
3. **Add at least one baseline that uses the same 8M frames** — either BC-oracle (to quantify the upper bound) or VPT-style with ~200 labeled transitions (to isolate LFO's unsupervised advantage). This would directly address the central interpretive ambiguity.
4. **Ablate the VQ codebook size and dataset size** to show sensitivity and help readers understand practical scaling.
5. **Calibrate the web-scale framing** to match the experimental scope, or add a simple robustness test (e.g., suboptimal demonstrations) to bridge the gap.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>