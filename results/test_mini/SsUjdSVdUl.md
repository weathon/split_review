Here is the final consolidated review.

---

## Summary

This paper proposes Critique-RL, a two-stage reinforcement learning approach for training critiquing language models (critics) that can both accurately judge response correctness (discriminability) and provide helpful feedback for refinement, without relying on a stronger supervisor or oracle verifier at test time. The key insight is that naive RL using only indirect reward signals (based on actor refinement correctness) improves helpfulness but fails to optimize discriminability, leading to overly conservative or aggressive critics. Stage I optimizes discriminability via a direct rule-based reward, and Stage II optimizes helpfulness via refinement rewards while regularizing toward the Stage I model to maintain discriminability. Experiments on Qwen2.5-3B and 7B across MATH, GSM8K, AQuA, and two OOD tasks show consistent gains over SFT, STaR, Retroformer, and CTRL baselines.

## Strengths

- **Well-diagnosed problem with compelling training dynamics analysis**: Section 4.1 (Figure 3) empirically demonstrates that RL with indirect rewards r_refine, r_correction, and r_Δ collapses discriminability — critics become either overly conservative or aggressive. This diagnosis directly motivates the two-stage design and is a useful finding for the community. The visualization of how discriminability degrades separately for correct and incorrect responses is particularly informative.

- **Substantial and consistent gains across tasks and model sizes**: Critique-RL outperforms all baselines on MATH, GSM8K, and AQuA for both 3B and 7B models, often by wide margins (e.g., +9.02% Acc on MATH for 7B over CTRL, +5.31–13.76 Acc@Dis over CTRL on GSM8K). The gains are systematic across every setting, not cherry-picked.

- **Generalization to out-of-domain tasks**: The method maintains improvements on SVAMP and TheoremQA (e.g., 89.7% Acc on SVAMP for 7B vs. CTRL's 85.1%), demonstrating that the trained critic transfers beyond its training distribution without loss of effectiveness.

- **Ablations validate component necessity**: Removing Stage I or Stage II individually degrades both accuracy and discriminability (Table 3). The discrimination regularization in Stage II (r_dis + KL to Stage I) is shown to be critical — removing it causes a sharp drop in Acc@Dis from 82.8 to 77.7 on MATH. This supports the claim that both stages and the regularization are essential.

## Weaknesses

### Major

- **No variance or statistical reliability reported for any main result**: All results in Tables 1 and 4 are single-point accuracy numbers with no standard deviations, confidence intervals, or replication across random seeds. RL training, especially with relatively small models (3B, 7B) and RLOO, is known to be noisy. Without any measure of variance, the reader cannot assess whether the reported improvements (e.g., 2–5 percentage points over CTRL) are statistically significant or within the noise range of the training process. This is the most significant evidential gap in the paper and undermines confidence in the experimental contribution. Every main experiment should be run with at least 3 seeds with mean and std reported.

### Minor

- **Missing one-stage joint optimization baseline**: The paper's central claim is that a two-stage approach is necessary — that jointly optimizing r_dis + r_refine from scratch (without a dedicated discrimination-first stage) would fail. However, the ablation in Table 3 only tests removing Stage I entirely (falling back to baseline RL) or removing Stage II (only discriminability). It never tests a single-stage RL that jointly optimizes r_dis + r_refine with KL to SFT from the start. Such a comparison would directly validate whether the two-stage design is strictly necessary or whether a well-tuned joint objective suffices. The training dynamics (Figure 3) partially address this (showing that baseline RL fails to optimize discriminability), but a direct ablation would be stronger.

- **Stage II ablation is coarse**: The "Stage II w/o discrimination" condition removes both r_dis and the KL(Stage-I || Stage-II) regularization simultaneously. This does not isolate which mechanism — the discriminability reward signal or the KL anchor to Stage I — is more responsible for maintaining discriminability. A finer ablation (removing only r_dis, or only KL) would be more informative.

- **Inference compute efficiency comparison is underspecified**: The paper claims that K× critique-refinement sampling is more efficient than 3K× parallel sampling. The figure caption mentions "@2k and @3k" indicating the comparison controls for total samples, which partially addresses this concern. However, it is not entirely clear whether "3K× parallel sampling responses" refers to 3K independent reasoning samples (no critique), or K samples each with a different type of processing. The visualization itself is hard to parse: the data appears to be read from a chart, and the legend descriptions are ambiguous. The claim is important for the practical value of the method but rests on a figure that would benefit from clearer presentation (e.g., accuracy vs. total tokens or FLOPs, not just number of samples).

- **Preliminary analysis limited to one setting**: The motivating findings (Figure 3, Section 4.1) are demonstrated only on GSM8K with Qwen2.5-3B. While the main results confirm the method works for 7B and other tasks, the dynamics analysis itself is not replicated for larger models or other datasets.

### Trivial

- The paper mentions "without stronger labeling" in the abstract, but the method still requires rule-based answer verifiers (ground-truth answers) for training rewards. This is a reasonable setup for math tasks and is acknowledged in the paper, but the framing slightly over-promises generality.

## Nice-to-Haves

- Evaluate on open-ended domains (e.g., summarization, as referenced in Appendix G) using learned reward models instead of rule-based verifiers — this would validate the method's scalability beyond answer-verifiable tasks.
- Report the actor's baseline "obedience" or improvement rate when given oracle critiques, to separately assess whether the critic's feedback or the actor's refinement ability is the limiting factor.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about "duplicate legend in Figure 1"**: The extracted text shows "w/o Critique-RL (3B)" listed twice in the table. This is a PDF parsing artifact (the original PDF likely has distinct entries like "w/o Critique-RL" and "w/o Critique-RL (3B)" with different curve styles). Not a paper flaw.

- **Criticism about missing appendix content / unverifiable claims**: The parser strips appendix sections from all submissions. The references to Appendix C, E, F, G, J are present in the original paper and are standard practice. Not a valid weakness.

- **Criticism about "oracle verifier assumption conflicting with 'no stronger labeling' claim"**: The paper is explicit ("without stronger labeling" refers to not needing a stronger HUMAN/LLM supervisor) and acknowledges the use of rule-based verifiers for math tasks — a standard and well-understood convention in the reasoning literature.

- **Criticism about baselines using different RL algorithms (PPO/GRPO vs. RLOO)**: The baselines Retroformer and CTRL use their originally proposed RL algorithms. This is standard practice for reproducing prior work. Critique-RL uses RLOO because it does not require a value model. The comparison may not isolate the effect of the two-stage design from the RL algorithm choice, but this is a minor concern that does not undermine the main claim.

## Novel Insights

Beyond the paper's own contributions, one novel observation emerges from the reviews: the paper's diagnostic finding — that RL optimization of indirect refinement rewards systematically degrades discriminability — is a genuinely useful characterization of an optimization pathology. Prior work (Retroformer, CTRL) treated the critic as a black box optimized purely by outcome; this paper opens that black box and shows that discriminability and helpfulness can compete under naive RL, and that explicitly decoupling them is beneficial. However, the same pathology diagnosis also raises a question the paper does not fully answer: can a simpler joint reward (r_dis + r_refine) with careful weighting achieve similar results without two-stage training? Missing this ablation is the single largest empirical gap.

## Suggestions

1. **Run all main experiments (Tables 1, 4) with at least 3 random seeds and report mean ± std.** This is the most impactful improvement the authors can make. If the results are as robust as they appear across settings, the variance is likely small, and this would substantially strengthen the paper.
2. **Add a one-stage joint optimization baseline**: train from the SFT checkpoint with objective r_refine + β₁·r_dis and KL to SFT (no dedicated Stage I). This directly tests whether the two-stage design is strictly necessary.
3. **Fine-grain the Stage II ablation**: separately test (a) removing only r_dis while keeping KL(Stage-I), and (b) removing only KL(Stage-I) while keeping r_dis.
4. **Present the inference compute scaling analysis more clearly**: plot accuracy vs. total generation tokens (or FLOPs) rather than number of samples, and include explicit error bars or multiple runs.

## Score and Decision

### Calibration Anchors

- **Critique-Coder** (`/home/wg25r/review_agent/human_reviews_2026/tsuxIeLUsz.md`, avg 5.50, Accept): Similar topic (RL for critique), but our paper has a deeper methodological contribution (training dynamics diagnosis + two-stage design vs. simple data mixing). Our paper has weaker evidential reporting (no variance). Roughly comparable quality.
- **RefCritic** (`/home/wg25r/review_agent/human_reviews_2026/qgMvotqkXd.md`, avg 4.00, Reject): Very similar topic, rejected mainly for novelty overlap with prior work. Our paper has stronger originality and cleaner motivation. Our paper is clearly stronger.
- **DeepCritic** (`/home/wg25r/review_agent/human_reviews_2026/wyCnT4BUsT.md`, avg 4.67, Reject): Two-stage framework for critics with strong data curation. Our paper has a cleaner RL methodology but weaker experiments. Comparable overall.
- **CORE** (`/home/wg25r/review_agent/human_reviews_2026/pRSRiXdpkm.md`, avg 5.00, Accept): Math reasoning + RL with concept supervision. Accepted despite one weak review. Our paper has comparable rigor and clearer abalations. Slightly worse on evidential completeness (no variance).
- **RL's Razor** (`/home/wg25r/review_agent/human_reviews_2026/7HNRYT4V44.md`, avg 6.00, Accept): Strong theoretical contribution with clean experiments. Our paper is substantially weaker on both theory and experimental rigor.
- **Critique to Verify** (`/home/wg25r/review_agent/human_reviews_2026/he7BMZwm8t.md`, avg 3.00, Withdrawn): Similar topic but notably weaker execution and analysis. Our paper is substantially stronger.
- **In-Context RL** (`/home/wg25r/review_agent/human_reviews_2026/keCXNHOe4W.md`, avg 4.67, Accept): Novel prompting framework for in-context RL. Our paper has stronger empirical evidence but weaker novelty. Comparable quality.

Relative to these anchors, the paper is clearly above the Reject-tier papers (RefCritic at 4.00, DeepCritic at 4.67) due to better motivation and cleaner methodology, but below the strongest Accept papers (RL's Razor at 6.00) due to the missing variance reporting and incomplete ablation. It sits in the borderline Accept range alongside Critique-Coder (5.50) and CORE (5.00), with the missing variance preventing a higher score.

**Score**: 5.0  
**Decision**: Accept

The paper makes a genuine contribution — the diagnosis of discriminability collapse under naive RL is a valuable finding, the two-stage design is well-motivated and empirically effective, and the results are consistent across tasks and model sizes. The main weakness (no variance reporting) is significant but addressable, and the consistency of the improvements across many settings mitigates concerns about noise. I recommend acceptance with the expectation that the authors add variance reporting and the one-stage ablation before the final version.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>