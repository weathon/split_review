Now I have all the information I need to write the review. Let me synthesize everything.

**Round 1 bracket:** I initially bracketed between 3.5 and 7.5.

**Round 2 anchoring:** After detailed comparison with ADOPT (5.25, Reject — similar optimizer proposal with theory+experiments but marginal gains, criticized for theoretical vacuity), SoftSignSGD (6.2, Reject — sign-based optimizer with solid experiments but theoretical concerns), "Do Stochastic, Feel Noiseless" (6.0, Accept Poster — clean theory, limited experiments), and "Flatter, Faster" (5.0, Reject — theory with limited experiments), I place the Ano paper at approximately **4.5**.

The key differentiating factor is the algorithmic inconsistency (|g_k| vs g_k) which is a structural flaw not present in any of the comparison anchors. This is more severe than the weaknesses in ADOPT or SoftSignSGD. The RL results are solid but not overwhelmingly strong (overlapping CIs), and the CV/NLP results are explicitly positioned as "diagnostic checks" with modest margins. The theory is disconnected from practice (analyzed schedule ≠ used schedule).

Let me write the review now.

---

Wait, I need to think more carefully. One thing the harsh critic says is that the SignumGrad variant (which seems to use |g_k|·sign(m_k) — the described form) performs catastrophically poorly (53.93% on CIFAR-100 vs 69.74% for Ano). This confirms the actual implemented algorithm (g_k·sign(m_k)) is what works, not the described one.

But is it truly the case that |g_k|·sign(m_k) is what SignumGrad implements? Let me re-read the ablation table.

The SignumGrad row (Table 6) has checkmarks in:
Looking at the raw text: "SignumGrad | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\beta_1$"

The columns are: Second Mom. Rule, Grad. Norm., Mom. Norm., Mom. Dir., Decoup. WD, β_{1,k}

So SignumGrad has checkmarks in columns 2, 3, 4, 5, and 6... but column 2 is "Second Mom. Rule" and the first column is the optimizer name, which doesn't have a checkmark. Let me look at this more carefully.

Actually, looking at the table structure:
Row header: "Optimizer | Second Mom. Rule | Grad. Norm. | Mom. Norm. | Mom. Dir. | Decoup. WD | β_{1,k} | Score DRL | Acc. (%) CIFAR-100 | Acc. (%) MRPC | Acc. (%) SST-2"

For SignumGrad: "SignumGrad | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\beta_1$"

So there are 5 checkmarks. But the columns after Optimizer are: Second Mom. Rule, Grad. Norm., Mom. Norm., Mom. Dir., Decoup. WD, β_{1,k}

So 5 checkmarks could correspond to columns 2-6 (all components except the optimizer name), or it could be something else.

Hmm, the table is hard to parse from the raw text. Let me look at what the paper's text says about SignumGrad:

"Performance drops when either gradient normalization (SignumGrad) or gradient magnitude (YogiSignum) is removed"

So SignumGrad uses "gradient normalization" (Grad. Norm.) — this seems to mean it uses |g_k| instead of g_k. Let me check what the paper says about normalization.

Actually, looking more carefully at the paper description (Section 3, line 69): "replaces the momentum magnitude with the instantaneous gradient norm |g_k|" 

And then the text equation shows |g_k|·sign(m_k), while the algorithm shows g_k·sign(m_k).

The text says about SignumGrad (line 374): "Performance drops when either gradient normalization (SignumGrad)..."

So "gradient normalization" probably means using |g_k| (normalizing the gradient by dividing by its absolute value/magnitude). And SignumGrad uses Grad. Norm. (|g_k|) and Mom. Dir. (sign(m_k)) — exactly the described but not implemented form. And it performs terribly.

This is strong evidence that the description |g_k|·sign(m_k) is not what makes Ano work, but rather the actual g_k·sign(m_k) is crucial.

OK, I'm now confident that this inconsistency is real and meaningful. Let me write the review.

I'll score the paper as 4.5. The algorithm itself (g_k·sign(m_k)) is a reasonable variant worth studying, but the paper's narrative is fundamentally inconsistent, and this flaw is severe enough to recommend rejection in its current form.Now I have all the information needed to write my comprehensive review.

## Summary

This paper introduces Ano, an optimizer that decouples update direction from magnitude by combining momentum sign (for direction) with gradient-based scaling (for magnitude), targeting noisy and non-stationary optimization landscapes like reinforcement learning. It also proposes Anolog, a variant with a logarithmic β₁ schedule to reduce hyperparameter sensitivity. The paper provides convergence theory (O(K^{-1/4})), an ablation study, and experiments across CV, NLP, and RL.

## Strengths

1. **RL evaluation across two paradigms (SAC/PPO) with best practices.** Tables 4 and 5 show Ano achieving the best mean rank (1.4/1.6 for SAC, 2.2/1.8 for PPO) across 5 MuJoCo and 5 Atari environments with 10 seeds, IQM, and 95% CIs. This is a thorough evaluation that follows community best practices (Agarwal et al., 2021) and is the paper's strongest evidence that the design benefits noisy, non-stationary optimization.

2. **Ablation study isolating individual components (Table 6).** The ablation compares 11 variants, showing that the full Ano configuration achieves the best DRL score (10520), substantially outperforming variants that omit gradient-based scaling (Signum, 9393) or use Adam-style second moments (AdamGrad, 9855). This provides empirical justification for the specific design choices.

3. **Hyperparameter robustness visualization (Figure 3).** Ano maintains high reward across a wider range of learning rates and β values than Adam on the HalfCheetah proxy task, supporting the claim that performance improvements are not solely due to favorable hyperparameter choices.

4. **Competitive on low-noise supervised benchmarks.** Ano matches or slightly exceeds Adam and Adan on CIFAR-100 (70.31% vs 69.57% and 69.87%) and achieves the highest average GLUE score (82.92 default), showing the optimizer does not degrade in stable settings outside its intended niche.

## Weaknesses

### Major

1. **Algorithmic inconsistency between the described design principle and the implemented update.** The text in Section 3 (lines 69–77) states that Ano replaces the momentum magnitude with |g_k| and presents the equation: `x_{k+1} = x_k - η_k/(√v_k+ε)·|g_k|·sign(m_k)`. However, Algorithm 1 (lines 59, 63) implements: `x_{k+1} = x_k - η_k/(√v_k+ε)·g_k·sign(m_k)`. These are not equivalent: when sign(g_k) ≠ sign(m_k), |g_k|·sign(m_k) points in direction sign(m_k) while g_k·sign(m_k) points in the opposite direction (i.e., the gradient's direction). The ablation data confirm this matters: the "SignumGrad" variant — which appears to use |g_k|·sign(m_k) (the described form) — achieves only 53.93% on CIFAR-100 vs 69.74% for Ano. The paper's central narrative (clean decoupling of direction=sign(m_k) and magnitude=|g_k|) does not match what the algorithm actually does. This is not a minor presentation issue; it undermines the motivation, the claimed design principle, and the theoretical analysis, which was written for the |g_k|·sign(m_k) form.

2. **Theory-practice gap.** The convergence proof (Section 5.1) assumes a square-root β₁ schedule (β_{1,k}=1−1/√k) and η_k=η/k^{3/4}, but the practical algorithm uses constant β₁=0.92. The Anolog variant uses yet another (logarithmic) schedule. The ablation shows the square-root schedule performs catastrophically (DRL score −221.45), yet this is the schedule the theory assumes. The paper does not explain why the theoretical guarantees should apply to the constant-β₁ version used in experiments, nor how the sign-mismatch lemma interacts with the g_k·sign(m_k) update (vs the |g_k|·sign(m_k) form described in the proof sketch).

3. **RL improvements are often within overlapping confidence intervals.** In Table 4 (SAC), several per-environment comparisons show substantial overlap: HalfCheetah (Ano 10864±1052 vs Adam 10549±722), Humanoid (Ano 5255±816 vs Adam 5357±212), Hopper (Ano 3535±781 vs Adam 3165±600). The mean rank advantage (1.4 vs 3.4) is meaningful but aggregated across only 5 environments. The "+10% normalized average" claim depends on the specific pool of baselines used for normalization. For Atari (Table 5), Ano's CI on BattleZone tuned is ±1870 vs Adam's ±1299, making the point estimate advantage uncertain. While the consistent ranking advantage is noteworthy, the per-environment gains are modest.

### Minor

1. **Table 3 (GLUE) has two rows labeled "Adam" in both Default and Tuned sections** (lines 192–193, 199–200). The second row in each section likely corresponds to "Adan" based on other tables, but this is not stated. This typographical error undermines trust in table accuracy.

2. **The Yogi+β₂-decay variance update is under-explained.** The paper says it "introduces an additional decay factor to control its memory" (Section 3) but never explicitly compares with Yogi's original update or clarifies what the β₂ multiplier does differently. The ablation (AnoWoTweak using vanilla Yogi performs worse) shows it matters, but the mechanism is not discussed.

3. **Theoretical analysis does not establish which algorithm it covers.** The proof sketch references a sign-mismatch lemma and uses sign(m_k) with some scaling, but it is ambiguous whether the proof applies to |g_k|·sign(m_k) or g_k·sign(m_k). Since the ablation data suggests these have very different empirical behavior, this ambiguity is consequential.

4. **Reproducibility statement says "it isn't included in the source code for double-blind review"** (Section 10) about the pip package, which reads as contradictory since the source code is in an anonymous repository. This is likely a phrasing issue.

### Trivial

- None beyond what has been described above.

## Nice-to-Haves

- Clarify whether the SignumGrad row in Table 6 implements |g_k|·sign(m_k) (the described but unused form) and explicitly state why it performs poorly. This would strengthen the paper's narrative.
- Include formal significance testing (e.g., paired bootstrap) across environments, given the CI overlap.
- Add a version of Anolog that uses the theoretically analyzed square-root schedule as a baseline, with explanation for why it diverges in practice.

## Removed Points

- **Criticism that RL gains are "modest" generically** — the mean rank advantage is meaningful and the paper reports proper RL evaluation methodology (IQM, CIs, 10 seeds). However, the CI overlap concern is kept as Major weakness 3 (reworded).
- **Concern about "normalized average" compressing differences** — this is a standard metric in RL benchmarking (Agarwal et al., 2021). The paper also reports raw scores with CIs. Kept the CI overlap concern but removed this framing.
- **Criticism of 100k-step proxy for hyperparameter tuning** — acknowledged as a pragmatic compromise by the authors; this is standard practice in RL.
- **Missing related works** — cannot verify without external knowledge.
- **Formatting/style nitpicks** — parser artifacts.
- **"Second Adam row" being a naming confusion** — kept as Minor weakness 1 since it's verifiably present in the paper.
- **Criticism about missing appendix content** — parser strips these sections.
- **Strength Finder's generic strengths** about "addressing an important problem" etc. — removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation that the paper itself does not identify.

## Suggestions

1. **Resolve the |g_k| vs g_k inconsistency.** Either (a) acknowledge that the actual update is g_k·sign(m_k) and rewrite the motivation, theoretical analysis, and explanatory text to match this form, explaining why g_k·sign(m_k) is preferable to |g_k|·sign(m_k); or (b) change the algorithm to actually implement |g_k|·sign(m_k) and re-run the experiments (though the ablation suggests this will not work). Option (a) is more practical.

2. **Align the theoretical analysis with the implemented algorithm.** If the proof assumes |g_k|·sign(m_k), it needs to be re-derived for g_k·sign(m_k) (or the algorithm changed). If the proof already applies to g_k·sign(m_k), state this explicitly and explain why the constant-β₁ version used in practice inherits the guarantees.

3. **Correct the two "Adam" rows in Table 3** to distinguish between Adam and Adan (or whatever the second row represents).

4. **Clarify the Yogi+β₂-decay update** by explicitly comparing with Yogi's original formulation and explaining the effect of the β₂ multiplier.

5. **Consider reframing the contribution around the actual algorithm** (g_k·sign(m_k) with second-moment scaling) as a sign-informed adaptive method, rather than claiming a clean decoupling that does not exist. This would make the paper internally coherent.

## Score and Decision

**Round 1 bracket:** [3.5, 7.5] based on first calibration pass.

**Round 2 anchoring:**

| Anchor Paper | Avg Score | Decision | Round | Comparison |
|---|---|---|---|---|
| Do Stochastic, Feel Noiseless | 6.0 | Accept (Poster) | 1 | Clean theory, clean description, limited experiments. Stronger narrative coherence than Ano but narrower empirical scope. |
| Flatter, Faster | 5.0 | Reject | 1 | Theory-focused with limited experiments. No algorithmic inconsistency issue. Comparable overall quality. |
| Exact risk curves of signSGD | 5.0 | Reject | 1 | Theoretical analysis only. No algorithm proposed. Different scope but similar score tier. |
| ADOPT | 5.25 | Reject | 2 | Clean algorithm description but marginal empirical gains and criticized theory. More coherent narrative than Ano but similar limitations. |
| SoftSignSGD (S3) | 6.2 | Reject | 2 | Sign-based optimizer with strong experiments and cleaner narrative. Higher quality due to consistent description and broader evaluation (LLM). |
| On Convergence of Adam (non-uniform smoothness) | 4.25 | Reject | 2 | Theory paper with significant reviewer disagreement. Shows the typical score for papers with substantive reviewer concerns. |
| Improving Resistance to Noisy Labels | 5.2 | Reject | 2 | Method + experiments paper. Similar scope (noise robustness) but cleaner execution. |

**Narrowing:** The Ano paper is clearly weaker than SoftSignSGD (6.2) and "Do Stochastic, Feel Noiseless" (6.0), which have consistent narratives and lack structural flaws. It is comparable to or slightly weaker than ADOPT (5.25), which was Rejected. The algorithmic inconsistency is a more severe flaw than ADOPT's issues (marginal gains, vacuous theory bounds). Compared to "On the Convergence of Adam" (4.25), Ano has stronger experiments but a more fundamental clarity problem. The final score of **4.5** reflects a paper with interesting empirical findings (particularly in RL) that is undermined by a verifiable inconsistency between its central narrative and actual implementation — a flaw that requires substantial rewriting before the paper can be fairly evaluated.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>