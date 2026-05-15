Now I have all the information I need. Let me write the consolidated review.

## Summary

The paper introduces PA-RL (Parameterization-Agnostic RL), a method that decouples policy improvement from policy parameterization by first optimizing actions in action space (via Q-based re-ranking and gradient ascent) and then distilling them into the policy via supervised learning. This enables offline RL and online fine-tuning of multiple policy classes—Gaussian, diffusion, and autoregressive transformer policies—within a single algorithmic framework. The paper demonstrates strong empirical results on simulated benchmarks (D4RL, CALVIN) and real-robot fine-tuning of diffusion policies.

## Strengths

- **Core idea is clean and principled.** Decoupling policy improvement from policy parameterization by optimizing actions first and then using supervised learning for distillation directly addresses a real problem: existing RL algorithms co-developed for Gaussian policies (e.g., SAC's reparameterization gradient) can be unstable or intractable for diffusion or autoregressive transformer policies. The decomposition is conceptually simple and well-motivated.

- **Demonstrates effectiveness across multiple policy classes in simulation.** The results on antmaze, FrankaKitchen, and CALVIN cover diffusion policies, autoregressive categorical transformers, and Gaussian policies, all within the same approach (Tables 1–2, Figure 2). The 224% improvement over tanh-Gaussian with autoregressive transformer policies (Table 2) and the 69% improvement on CALVIN (Table 1) are notable.

- **Real-robot fine-tuning of diffusion policies is a strong practical contribution.** Improving pre-trained diffusion policies by 20–35% within 1–2 hours on two real WidowX manipulation tasks (Table 3), with only 20 initial demonstrations, is practically meaningful and addresses a genuine bottleneck in robot learning.

- **Ablation study provides actionable guidance.** Table 4 systematically shows when global optimization is critical (diverse data like antmaze) and when local optimization additionally helps (narrower data like CALVIN), giving practical deployment recommendations.

## Weaknesses

### Fatal

- **OpenVLA claim is entirely unsubstantiated in the paper body.** The abstract (line 4) and introduction (line 15) claim that PA-RL "is the first RL method to improve 7 billion parameter OpenVLA by 75% within 40 minutes of real-world interaction." This is presented as a headline result that would be the strongest demonstration of PA-RL's generality. However, the paper contains **zero experimental evidence** for this claim: no table, figure, setup description, or even a passing mention of OpenVLA appears anywhere in the experimental sections (Section 5.2). The real-robot experiments describe only diffusion policy fine-tuning on a WidowX arm. Readers cannot verify, understand, or interpret this result. A paper cannot claim a specific quantitative result without presenting the corresponding experimental evidence. This is a serious reporting failure that undermines trust.

### Major

- **No statistical variance or number of seeds reported.** Table 1 and other quantitative results report only point estimates. For an RL paper claiming state-of-the-art performance across benchmarks, standard errors (or at minimum the number of random seeds) are essential. Without them, the reader cannot assess whether PA-RL's claimed 13% aggregate improvement over the next best method is statistically meaningful or within run-to-run noise. This is particularly important given that the paper itself notes that DQL and IDQL are known to be unstable.

### Minor

- **Theoretical comparison (Equation 4.6) is weak and does not establish a meaningful advantage over AWR.** The inequality states that applying local gradient ascent yields larger Q-values than not doing so—a near-tautological claim under the Taylor expansion assumption. Moreover, the claimed comparison to AWR is misleading: the RHS represents a maximum over sampled actions (PA-RL's global optimization), not a dataset action as in actual AWR. The equation compares PA-RL with both components to PA-RL without local optimization, not to AWR. This theoretical section does not substantively justify PA-RL's advantage over prior supervised RL methods, though the empirical results do.

- **Cal-QL backup modification is not isolated from the actor modification.** PA-RL changes both (a) the actor update (replacing policy gradient with supervised learning on optimized actions) and (b) the TD-backup samples (using optimized actions instead of policy samples, since Cal-QL's critic loss requires on-policy action samples). The paper never ablates whether using optimized actions in the backup alone (without changing the actor loss) would produce gains. The IQL variant (which does not use policy samples in the backup) provides partial evidence but does not fully address this confound for the Cal-QL results.

- **Distillation choice is underspecified.** The paper describes two options for distilling optimized actions into the policy (single best action vs. softmax-weighted combination over top-m actions, Equation 4.3) but does not state which is used in the experiments or ablate between them.

- **Hyperparameter sensitivity is not analyzed.** The action optimization introduces four interacting hyperparameters (k, m, T, α). No analysis of sensitivity to these choices is provided, which would aid reproducibility.

- **Figure 2 uses different X-axis scaling for DPPO.** The paper discloses this ("for kitchen each unit is 500 episodes, for antmaze each unit is 100 episodes, for calvin each unit is 10 episodes"), but plotting methods with different axis scales on the same figure makes visual comparison difficult and potentially misleading. A cleaner presentation would use separate plots or consistent scaling.

### Trivial

- None beyond what is covered above.

## Nice-to-Haves

- Add variance/confidence intervals across multiple seeds for all quantitative results.
- Ablate the Cal-QL backup modification separately from the actor modification.
- Provide sensitivity analysis for action optimization hyperparameters (k, m, T, α).
- Clarify which distillation strategy (single-best vs. softmax-weighted) is used.

## Removed Points

These points were raised by reviewers but are removed following the guidelines:

1. *Missing CRR/AWAC citations* — Removed per "DO NOT mention missing related works" rule (cannot externally verify).
2. *Claim that IDQL/DQL are actor-critic, contradicting paper's "first" claim* — Removed as it misreads the paper's claim about "a single approach" working across multiple classes (IDQL uses re-ranking only, DQL uses reparameterized gradients specific to diffusion; neither provides a universal approach).
3. *Overclaiming universality (NLL-only limitation)* — Removed; the paper explicitly scopes itself: "as long as the policy updates use a supervised learning loss."
4. *20 demonstrations being "very small"* — Removed; this is actually a strength of the method (effective fine-tuning from limited data).
5. *"Figures 12-13 missing from submission"* — Removed; appendix content is stripped by the PDF parser.
6. *Instrumentation biases in reward function not discussed* — Removed; scope creep beyond the paper's contribution.

## Novel Insights

The reviews surface two insights not fully developed in the paper itself. First, the confound between the actor modification and the backup modification in the Cal-QL variant is genuinely important—understanding whether the gains come from better policy samples for the Bellman update, from the supervised actor loss, or from their combination would sharpen the community's understanding of why PA-RL works. Second, the paper's ablation showing that global optimization matters more on diverse data while local optimization helps on narrow data (Table 4) suggests an interesting hypothesis: the two mechanisms serve fundamentally different roles (exploration across modes vs. refinement within a mode), which could inform future method design. Beyond these, the paper's own contributions (decoupling improvement from parameterization, demonstrating cross-class applicability) are the main insights.

## Suggestions

1. **Either substantiate or remove the OpenVLA claim.** If the experiment exists, include the full setup, results table, and experimental details in the main paper. If it does not, remove the claim from the abstract and introduction entirely. This is non-negotiable for a credible submission.

2. **Add statistical rigor.** Re-run experiments over at least 5 seeds and report mean ± standard deviation for all tables. Without this, the claimed SOTA results cannot be evaluated.

3. **Ablate the Cal-QL backup modification.** Run PA-RL with standard Cal-QL actor (reparameterized gradient) but with optimized actions in the TD-backup, and vice-versa, to isolate where improvements come from.

4. **Clarify experimental choices.** Specify which distillation strategy (single-best vs. softmax-weighted) is used, and report the hyperparameter values (k, m, T, α) used in all experiments.

5. **Improve Figure 2 presentation.** Either plot DPPO on a separate panel with its own axis or use consistent episode scaling with a clear annotation explaining DPPO's total environment steps.

## Score and Decision

The paper presents a genuinely useful core idea and provides solid empirical evidence for its effectiveness with diffusion and autoregressive policies in simulation and on real robots. However, the submission contains a fatal reporting flaw: the abstract and introduction make a specific, headline quantitative claim about OpenVLA (75% improvement in 40 minutes) that is entirely unsubstantiated anywhere in the paper body. This is not a minor omission—it is a claim that would significantly raise the paper's impact, yet readers cannot verify or interpret it. Combined with the lack of statistical rigor (no variance or seed counts) and unablated methodological confounds, the paper in its current form does not meet the standard for acceptance. A substantially revised version that addresses these issues could be a strong contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>