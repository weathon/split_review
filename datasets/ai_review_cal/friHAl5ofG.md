- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8
Now I have a comprehensive understanding. Let me produce the final consolidated review.

## Summary

This paper proposes Generative Value Learning (GVL), which uses a frozen vision-language model to predict temporal task progress from video by auto-regressively generating completion percentages over **shuffled** frames. The core insight is that frame shuffling breaks the temporal bias that causes VLMs to produce uninformatively monotonic values when given chronological video, forcing the model to attend to actual semantic content. The method is evaluated at substantial scale (51 datasets, 300+ tasks across OXE and a new 250-task bimanual ALOHA dataset), and demonstrated on downstream applications including dataset quality filtering, success detection, and advantage-weighted regression for policy learning — all without any model fine-tuning.

## Strengths

1. **Frame shuffling elicits meaningful value predictions by breaking temporal bias.** This is the paper's central contribution and is convincingly demonstrated. Section 3 (Input observation shuffling) motivates why chronological prompting yields degenerate monotonic values, and the ablation in Section 4.4 shows quantitatively that removing shuffling collapses predictions to linear ascending patterns regardless of trajectory quality, while the full GVL method produces diverse and discriminative values.

2. **Zero-shot value prediction generalizes to over 300 real-world tasks across 51 datasets and 20 embodiments.** Section 4.1 evaluates on 50 OXE datasets (1000 trajectories) plus a newly collected 250-task bimanual ALOHA dataset. GVL's VOC scores skew heavily positive on OXE and outperform LIV (prior state-of-the-art) — significantly on language goals and marginally on image goals. The scale of zero-shot real-world evaluation exceeds prior work in value learning.

3. **Cross-embodiment in-context learning from human videos improves robot value prediction.** Section 4.2 (Figure 6) demonstrates that one human demonstration as an in-context example raises GVL's VOC on ALOHA tasks substantially above zero-shot. This is genuinely novel: prior in-context learning for robotics required robot-specific fine-tuning; GVL uses a frozen VLM and benefits from heterogeneous embodiments including humans.

4. **Careful ablations validate each design choice.** The single-frame VQA ablation (VOC -0.08 vs GVL's 0.74 on RT-1) convincingly shows that autoregressive batch prediction is essential. The no-shuffling ablation shows degenerate monotonic behavior. These are the right ablations and they cleanly support the method's design.

5. **VOC serves as a useful proxy for dataset quality and success detection.** Section 4.3 shows interpretable VOC rankings across OXE subsets (RT-1: 0.74, RoboNet: -0.85) that align with human intuition and prior work on dataset mixing. Success detection using a VOC threshold achieves 0.75 accuracy vs. 0.62 for SuccessVQA, with substantially higher precision.

## Weaknesses

### Major

- **AWR results on real-world tasks are too thin to support strong claims about offline RL.** The paper reports 10 trials per task on 7 real-world tasks (Table 4). Only 4 of 7 tasks show improvement over the DP baseline (with one tie), and 2 tasks show clear degradation. The reported fractions 6.5/10, 4.67/10, and 1.5/10 are inconsistent with binary outcomes from "10 trials per task" — they appear to be averaged over checkpoints, but this is not clearly stated for the AWR experiments. The paper claims "a clear correlation between improvement over DP and the VOC score," but with only 7 data points, 2 of which show the opposite trend, this is suggestive at best. The core contribution of GVL (zero-shot value prediction) does not depend on these results, but the strength of the "offline RL" claim should be calibrated to match the thinness of the evidence.

- **The VOC metric, while useful, conflates value quality with dataset quality in a way that is not fully disentangled.** The paper acknowledges in the Limitations section that VOC is "most suitable for a-periodic tasks," but the core evaluation treats high VOC on expert trajectories as the primary signal of good value prediction. A model that outputs somewhat sensible values could score well largely because the expert trajectories have clean temporal structure. The failure trajectories and low-quality datasets do provide a counterpoint, and the no-shuffling ablation helps, but the interpretation of absolute VOC scores across diverse datasets with different quality levels remains ambiguous. The paper would benefit from a more precise decomposition of what VOC captures vs. what is being measured about the value function itself.

- **Results are reported without confidence intervals or uncertainty quantification.** The OXE evaluation (1000 trajectories across 50 datasets) is reported as aggregate histograms without per-dataset breakdowns, variances, or significance tests against LIV. The few-shot scaling curve (Figure 3 right) shows means without error bars. Given the heterogeneity of the datasets, some quantification of uncertainty is expected.

### Minor

- **The AWR experiments use a proprietary VLM (Gemini-1.5-Pro) without the prompt format being included.** While the method is described at a conceptual level, the exact prompt used for value prediction is not provided in the paper. For a method that proposes a prompting strategy as its core technical contribution, this omission impedes independent reproduction. The paper states the exact prompt would be in the appendix (which the PDF parser strips), but this should be present in the main paper or supplementary.

- **No systematic characterization of failure modes.** The paper identifies tasks where GVL underperforms (open-drawer, remove-gears from top-down view) but does not analyze across the 300+ tasks what visual or task properties correlate with low VOC. Are failures concentrated in certain camera angles? Task horizons? Visual similarity between frames? A deeper analysis would strengthen the paper's contribution as a diagnostic tool.

- **Cost and latency are not discussed.** Using a large proprietary VLM (Gemini-1.5-Pro) for per-frame value prediction has practical implications (API cost, latency, throughput) that are never mentioned. For a method proposed as a practical tool for dataset filtering and policy learning, this is a notable omission.

### Trivial

- The reported "300 tasks" aggregates 50 OXE datasets (each containing many tasks) with 250 bimanual ALOHA tasks. While factually correct, these are qualitatively different task collections, and the paper would benefit from being more precise about the composition.

## Nice-to-Haves

- A controlled simulation experiment comparing GVL-weighted AWR against an oracle using ground-truth timestep-based values would establish an upper bound and clarify how much information GVL's values actually capture for policy learning.
- Reporting per-task VOC distributions (rather than aggregate histograms) for the OXE dataset would help practitioners understand when GVL can be trusted and where its failure modes cluster.

## Removed Points

These points were flagged for removal with justifications:

1. **"Zero-shot claim is less interesting because VLM pre-training includes robot data"** — REMOVED. The paper claims "without any robot or task specific training," which is accurate: no fine-tuning on target tasks. The standard usage of "zero-shot" in the VLM literature does not require the VLM to have never seen any related data during pre-training. This criticism would apply to essentially all zero-shot VLM methods.

2. **"VOC metric directly rewards LIV's training objective"** — REMOVED (weakened version kept above). This claim is inaccurate: LIV was trained with a contrastive embedding objective on human videos to align embedding distances with temporal distances. VOC measures rank correlation between predicted values and chronological order on shuffled frames — these are different objectives. The fact that GVL still outperforms LIV (especially on language goals where LIV is near-random) makes the comparison meaningful.

3. **"The no-shuffling ablation is qualitative rather than quantitative"** — REMOVED. The paper provides histograms comparing the full method vs. no-shuffling (Figure 5), which clearly shows qualitative collapse to monotonic predictions. Moreover, quantitative VOC scores are reported elsewhere for comparisons. This criticism overlooks the visual evidence presented.

4. **"The '300 tasks' claim papers over qualitative differences"** — DEMOTED to Trivial (kept in modified form above). The number is factually correct and the paper separately discusses the OXE and ALOHA evaluations. This is a minor presentation precision issue.

5. **Strengths removed from Strength Finder:** Generic strengths such as "this paper addressed an important problem" are removed as they lack specific content. Only concrete, evidence-grounded strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations largely surface standard evaluation rigor concerns (confidence intervals, sample sizes, failure analysis) that are common in large-scale empirical papers, rather than novel perspectives on the methodology or its implications.

## Suggestions

1. Disclose the exact prompt format used for GVL value prediction (or confirm it will be in the supplementary materials).
2. Add per-dataset VOC breakdowns with variances for the OXE evaluation, so readers can assess where the method works best and worst.
3. Clarify the AWR evaluation protocol (are the reported numbers averaged over checkpoints or trials?), and temper the claim about "clear correlation between improvement and VOC" given only 7 data points.
4. Add a discussion of practical compute cost and latency, given the use of a proprietary VLM.
5. Provide a brief analysis of failure modes across the 300+ tasks: what visual or task properties correlate with low VOC?
