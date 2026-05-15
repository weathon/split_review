Now I have thoroughly verified all claims against the paper. Let me produce the consolidated review.

## Summary

This paper introduces DISTA, a test-time adaptation method that augments the standard entropy-minimization objective with a knowledge-distillation auxiliary task performed on unlabeled source-domain data. The authors propose a "lookahead" metric to evaluate whether an auxiliary task actually accelerates adaptation, and show that both a simple entropy auxiliary and their distillation auxiliary yield positive lookahead. DISTA is evaluated on ImageNet-C and ImageNet-3DCC under episodic, continual, and federated protocols, demonstrating consistent gains over prior state-of-the-art methods.

## Strengths

- **Novel lookahead analysis framework for evaluating auxiliary tasks in TTA**: The paper introduces a principled quantitative metric (Equations 3, 5) to measure whether an auxiliary objective actually accelerates adaptation on corrupted data, rather than relying on ad-hoc proposals. This is a methodological contribution that future work can build on regardless of the specific auxiliary task chosen.

- **Consistent and substantial improvements across multiple benchmarks and protocols**: DISTA outperforms prior state-of-the-art EATA by 1.5% on episodic evaluation (Table 1), 6% on continual evaluation (Table 3), and 6% in federated evaluation (Table 5) on ImageNet-C, with similar or larger margins on ImageNet-3DCC (Tables 2, 4). These gains hold across all 15 corruptions individually, not just on averages.

- **Robustness across architectures, batch sizes, and computational budgets**: DISTA improves over baselines on ResNet-18, ResNet-50, ResNet-50-GN, and ViT (Figure 2c), and at batch size 8 it surpasses EATA by over 15% (Figure 2b). Figure 2a further shows that even with 50% reduced auxiliary frequency, DISTA retains 1.4% gain over EATA, demonstrating practical flexibility.

- **Pioneering federated TTA evaluation**: The paper introduces a realistic category-wise federated setup where clients observe different domain shifts (e.g., all weather corruptions), and shows that federated averaging helps even across different shifts — and that DISTA amplifies this benefit. This opens a new and underexplored evaluation direction for the community.

- **Orthogonal benefit demonstrated**: Table 6 shows that the auxiliary task concept (even the simple entropy version) improves both Tent and SHOT, confirming the approach is broadly applicable and not tied to the distillation objective specifically.

## Weaknesses

### Fatal
None.

### Major

- **The claim that distillation is "better and more powerful" than the simple entropy auxiliary is not directly supported by the evidence provided**. The paper presents Figure 1a (lookahead for entropy auxiliary) and Figure 1b (lookahead for DISTA's distillation auxiliary) but never overlays them or quantitatively compares their magnitudes on the same scale. The lookahead metric is defined identically for both (Equation 3), so direct comparison is possible and should be shown. Without this, the superiority claim relies on the downstream Tables 1–5, which compare DISTA against EATA — but EATA uses source data for a regularizer, not for an entropy auxiliary. The paper never directly compares DISTA vs. a *controlled baseline that also gets the same auxiliary gradient steps on source data but using entropy instead of distillation* (e.g., "EATA + source entropy" or "DISTA-variant with entropy auxiliary"). Table 6 partially addresses this by showing Aux-Tent improves Tent, but it does not pit Aux-Tent against DISTA in the same table. The reader cannot tell whether the gains come from the *distillation* task or simply from having *any* auxiliary gradient on source data.

- **Missing comparison against prior methods that also leverage source data (DDA, Kang et al.)**. These are cited in Related Work (Section 3) as methods that use source data during adaptation, yet they appear in none of the experimental tables. Since the paper's contribution is specifically about leveraging source data, these are the most relevant baselines. Their absence weakens the claimed state-of-the-art in the "source-aided TTA" setting.

### Minor

- **The lookahead analysis (Figures 1a, 1b) is only shown for 3 out of 15 corruptions (Gaussian Noise, Motion Blur, Snow)**. The paper claims "positive lookahead over all observed batches" for DISTA but does not show whether variance exists across other corruptions. Expanding this would strengthen the analysis.

- **Data selection functions λ_t and λ_s are borrowed from EATA without ablation**. The paper does not test whether the distillation auxiliary works without these selection mechanisms, or with simpler alternatives. This makes it unclear how much of the gain comes from the distillation objective vs. the filtering scheme.

- **Federated evaluation (Section 4.3) aggregates clients with different corruption categories (e.g., all weather corruptions) but does not explain why this helps**. The paper notes the result is "despite the fact that in each communication round, models adapting to different domain shifts are being aggregated" but provides no analysis or hypothesis. The finding is interesting but under-explored. Additionally, there is no baseline where each client stores and uses source data locally (which would be the direct extension of DISTA to this setting without communication).

### Trivial
None.

## Nice-to-Haves

- Wall-clock timing or FLOPs comparison alongside the 2× computational overhead discussion would help practitioners assess the practical trade-off.
- Per-corruption breakdown of the federated results (Table 5) across all 15 corruptions rather than only the 4 category aggregates would reveal whether the benefit is uniform.
- A discussion of why the auxiliary task also improves performance on clean data would enrich the analysis.

## Removed Points

- **"Unfair baseline comparison — baselines do not have access to source data"**: This claim is factually incorrect. EATA (Niu et al., 2022) explicitly leverages 𝒟_s for its anti-forgetting regularizer, as stated in the paper (line 48). EATA is the primary baseline throughout the paper. The comparison between DISTA and EATA is a comparison between *two methods that both use source data*, just in different ways. The critic's broader point about unequal *amount* of source data usage is addressed by moving it to the "Major" weakness about missing controlled comparison between distillation and entropy auxiliary on source data — but the absolute claim that baselines lack source data access is removed as factually wrong.

- **"Framing is misleading — bandwidth limitation is circumvented by using data not on the stream"**: The paper clearly states in both the abstract and introduction that it "leverage[s] unlabeled data from the training distribution" (line 14). The framing is transparent; this is a matter of interpretation, not a flaw.

- **"Only one dataset (ImageNet-C) for main evaluations"**: The paper also uses ImageNet-3DCC (Tables 2, 4), which is a second large-scale benchmark. Two benchmarks is standard for the TTA literature.

- **"Figure 2a x-axis not precisely defined"**: The paper states (line 193) that the x-axis represents the "additional computational requirement" corresponding to "frequency of updates on x_s" and "batch size of x_s." While more precise labeling would be nice, this criticism is a presentation nitpick that does not affect the validity of the results.

- **Strength Finder's generic strengths about "important problem" and "interesting question"**: These are removed as generic. All remaining strengths in the main review are specific and evidence-backed.

## Novel Insights

The most interesting finding that emerges from the reviews is the tension between the paper's two related but distinct contributions. The lookahead analysis demonstrates that *any* auxiliary task on source data (even simple entropy) accelerates adaptation — yet the paper's main claim is that *distillation specifically* is superior. The reviews collectively identify that the paper never fully decouples these two claims experimentally. This suggests a deeper empirical question worthy of follow-up: is the benefit of the distillation auxiliary primarily a regularization effect (keeping the model close to the pretrained initialization) or an acceleration effect (providing more informative gradients than entropy)? The continual evaluation results (Tables 3, 4) hint at the former (DISTA is far better at retaining source performance), but the paper does not disentangle this from the latter.

## Suggestions

1. **Add a direct head-to-head comparison** in the main episodic table between DISTA and a controlled baseline that uses the *same* auxiliary gradient on source data but with the entropy objective (e.g., "EATA + source entropy" or "Aux-EATA"). This would isolate whether distillation specifically adds value beyond simply having more gradient steps on source data.

2. **Overlay the lookahead curves** from Figures 1a and 1b on the same axes, or report the quantitative lookahead values for both methods, to directly support the claim that distillation is "better and more powerful" than the entropy auxiliary.

3. **Include DDA and Kang et al. as baselines** in at least the episodic evaluation (Table 1), since these are the most closely related methods that also leverage source data during adaptation.

4. **Ablate the data selection schemes** (λ_t, λ_s) for the distillation auxiliary to clarify whether the gains come from the objective or the filtering.

5. **Report per-corruption results** for the federated evaluation to show whether the improvement is uniform or driven by specific shift types.

## Score and Decision

The paper presents a clean idea (auxiliary tasks on source data for TTA), a useful analysis tool (lookahead), and strong empirical results across multiple protocols and architectures. The main weakness is that the paper does not fully isolate whether the gains come from the distillation objective specifically or from the auxiliary gradient on source data generally — the comparison against the entropy auxiliary is missing from the main results, and the lookahead analysis does not quantitatively compare the two. This does not invalidate the contributions but limits the precision of the claims. The federated evaluation is a genuine novel contribution. The paper is solid and makes a clear contribution to the field.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>