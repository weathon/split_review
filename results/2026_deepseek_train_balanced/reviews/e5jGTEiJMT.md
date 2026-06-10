Now I will write the complete final review.

## Summary
The paper proposes **Policy Decorator**, a framework that learns a small residual policy via online RL (SAC) to refine a frozen, offline-trained imitation learning policy. The key technical contribution is **controlled exploration** — bounding the residual action with a parameter α and progressively introducing it via a schedule parameter H — which prevents the random exploration of vanilla residual RL from destroying performance in sparse-reward, precision-sensitive tasks. The method is evaluated on 8 robotics tasks (ManiSkill + Adroit) with two structurally different base policies (Behavior Transformer and Diffusion Policy), achieving near-perfect success rates while (qualitatively) preserving smooth motion.

---

## Strengths

1. **Controlled exploration convincingly addresses a real failure mode of residual RL.** The paper identifies that vanilla residual RL without constraints fails on precision tasks (ablated in Fig. 9), and demonstrates that both bounded residual actions and the progressive exploration schedule are individually and jointly necessary. The ablation is clean and directly supports the core claim.

2. **Genuinely model-agnostic improvement across divergent architectures.** Policy Decorator improves both Behavior Transformer (non-differentiable k-means clustering) and Diffusion Policy (denoising diffusion + receding horizon control) — two structurally different IL models — as a black-box wrapper. This is a non-trivial achievement that fine-tuning-based methods cannot replicate (DIPO fails entirely; Cal-QL and RLPD fail on all ManiSkill tasks).

3. **Broad and rigorous evaluation setup.** The experimental design spans 8 tasks (stationary manipulation, mobile manipulation, dual-arm coordination, dexterous manipulation, articulated objects, high-precision tasks), diverse demonstration sources (teleoperation, TAMP, RL, MPC), and both low-dimensional state and high-dimensional visual observations. This directly supports the paper's claim of versatility.

4. **Informative ablation and hyperparameter analysis.** The ablation (Fig. 9) isolates each component's contribution, and the hyperparameter analysis for α (Fig. 10) shows robustness across a wide range (e.g., 0.1–0.5 for PushChair), providing practical tuning guidance.

---

## Weaknesses

### Fatal
None.

### Major

1. **No statistical reporting across random seeds.** The paper reports all results — success rates and learning curves — without any indication of variance (no standard deviations, no error bars, no mention of the number of seeds). In deep RL, results are known to be highly variable across seeds, and a single run could be lucky or unlucky. Without this information, the reader cannot assess the reliability of the headline quantitative claims. The near-perfect success rates reported would need to be sustained across multiple seeds to be convincing. *This is the single most impactful weakness because it undermines the evidential backbone of the paper.*

2. **No working fine-tuning baseline established for Diffusion Policy.** The paper claims Policy Decorator outperforms fine-tuning for Diffusion Policy, but the only fine-tuning baseline used (DIPO) "failed to obtain any success signals across all tasks." DPPO — a contemporaneous diffusion-policy RL method — was tested only in preliminary experiments and explicitly described as not fully adapted. This means the paper has **no established, working fine-tuning comparison for Diffusion Policy**. The non-fine-tuning baselines (JSRL, Residual RL, FISH) do serve as comparisons, but the specific claim about outperforming *fine-tuning* for DP is unsupported by a viable competitor. The paper should either develop a working fine-tuning baseline or clearly scope this claim.

### Minor

1. **No quantitative evidence for the smooth-motion advantage.** Section 5.5 claims the refined policy "exhibits significantly smoother behavior" than pure RL policies and preserves the smooth motions of imitation learning. The evidence is limited to qualitative descriptions and links to videos. No quantitative metric (jerk, acceleration variance, action smoothness, frequency-domain analysis) is provided. Since the paper presents motion smoothness as a key advantage over alternatives (including JSRL), quantified backing would substantially strengthen this claim.

2. **Visual observation experiments lack baseline comparisons.** Figure 8 shows learning curves for Policy Decorator on 2 visual-observation tasks, but without any baseline comparisons. The text says "results validated that Policy Decorator also performs well," but without baselines, this constitutes a demonstration rather than a comparison. This limits the strength of the claim that the method works under visual observations.

3. **DPPO comparison presented as preliminary evidence but used in a definitive claim.** The paper states "Results indicate that our method significantly outperforms DPPO" based on preliminary experiments where DPPO "was released around three weeks before the ICLR deadline" and the authors "had insufficient time to fully adapt it." Including this comparison alongside a candor disclaimer is reasonable, but the definitive phrasing ("significantly outperforms") overstates what a preliminary, incompletely-adapted experiment can support. Either report the comparison properly with full adaptation, or drop the definitive language.

### Trivial
None.

---

## Nice-to-Haves

- **Wall-clock time and computational cost comparison.** The paper motivates the approach by arguing that fine-tuning large models is "prohibitively costly," but provides no runtime or parameter-count comparison between Policy Decorator and fine-tuning baselines. A comparison table (policy parameters, training time, environment steps) would substantiate this claim.
- **Failure case analysis.** The paper achieves near-perfect success rates on most tasks. Analyzing the remaining failure cases would deepen the contribution and provide insight into the method's limitations.
- **Total environment interaction budget.** Not explicitly stated in the main text, which would help assess sample efficiency.

---

## Removed Points

The following points from the inputs were identified as invalid, misinformed, or redundant and are removed from the main review:

- **JSRL criticism ("not actually improving the base policy").** The harsh critic argues this is a "strange criticism." However, the paper's claim is that JSRL does not *preserve the base policy's properties* (smoothness), not that JSRL cannot improve task performance. Text (Sec. 5.3): "JSRL does not actually 'improve' the base policy but instead learns an entirely new policy. This means that even if it achieves a high success rate, it does not preserve the desired properties of the original base policy, such as smooth and natural motion." The critic misreads the paper; this is a strawman. **Removed.**
- **"The claim about raising the critical research question is overstated."** Generic criticism about a contribution framing statement, not a substantive weakness about the method or evidence. **Removed.**
- **"Treatment of residual learning in Related Work is thin."** Generic related-work scope complaint without a concrete omission. **Removed.**
- **"Implementation details missing from the main text."** The paper explicitly refers to the appendix for several implementation details (architecture sizes, etc.). The parser strips appendices from all papers. Per instructions, "REMOVE weaknesses about missing appendix." **Removed.**
- **Strength Finder's smooth-motion strength.** The Strength Finder lists "preserves smooth motion" as a core strength, but the evidence for this claim is only qualitative (videos), which conflicts with the verified weakness (no quantitative metric). Per instructions: "Drop strengths that conflict with a verified weakness — when a strength and weakness disagree, the weakness wins." **Removed from strengths.**
- **"The evaluation lacks rigor" / "baselines may not be fair" (general framings).** The harsh critic's initial framing sentences without concrete anchors. The specific, verifiable substrengths/weaknesses are retained; the sweeping generalizations are removed.

---

## Novel Insights

None beyond the paper's own contributions. The key insight — that compounding errors in IL policies can be corrected by small, bounded residual adjustments with controlled exploration — is well-articulated by the paper itself.

---

## Suggestions

1. **Add multi-seed results with variance.** Run all main experiments with at least 5 random seeds and report mean ± std in bar plots and shaded regions in learning curves. This single change would transform the paper's evidential quality.
2. **Establish a working fine-tuning baseline for Diffusion Policy.** Either (a) properly adapt DPPO to the paper's tasks, or (b) develop a simplified fine-tuning approach for DP and compare against it, or (c) clearly scope the claim to "outperforms non-fine-tuning baselines" for the DP setting.
3. **Add a quantitative smoothness metric** (e.g., mean absolute jerk, action variance, or frequency-domain smoothness) to substantiate the smooth-motion advantage.
4. **Include baseline comparisons for visual observation experiments.**
5. **Either fully report the DPPO comparison or remove the definitive "significantly outperforms" language.**

---

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>