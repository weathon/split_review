---
job_id: 2b76afd6-da26-4df3-a593-22fb160d6733
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: yBFXOZPESZ.pdf
paper: Ano : Faster Is Better in Noisy Landscapes
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies stochastic optimization for deep learning, includes theory for non-convex optimization, and evaluates on vision, language, and reinforcement learning.

## Minimum Quality
Pass ✅. The paper contains the expected core components, namely Abstract, Introduction, Related Work, Algorithm/Method, Analysis, Experiments, Ablations, Limitations, and Conclusion, and it presents nontrivial empirical and theoretical content. That said, there are several technical inconsistencies and experimental-design concerns that significantly weaken the submission, but they do not rise to the level of an obvious desk rejection from the manuscript alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any visible hidden prompts, reviewer-targeted instructions, or suspicious manipulative text in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes **Ano**, an adaptive optimizer that decouples update direction and magnitude: the update direction comes from the sign of momentum, while the step magnitude uses the instantaneous gradient magnitude normalized by a second-moment estimator. The paper also introduces **Anolog**, a variant with a time-varying momentum schedule, provides a non-convex convergence analysis in the spirit of recent sign-based optimizer analyses, and evaluates the methods on CIFAR-100, GLUE, MuJoCo SAC, and Atari PPO, with the main claimed benefits appearing in noisy and non-stationary reinforcement learning settings.

## Strengths
- The paper studies a relevant problem. Robust optimization under high stochasticity and non-stationarity is important, especially in RL, where many optimizer papers look good on supervised benchmarks but do not hold up in harder regimes.

- The core design idea is simple and easy to state: use momentum only for direction, and use the current gradient magnitude for scaling. This is a clean conceptual contrast to Adam-like methods and is easy to implement.

- The empirical coverage is reasonably broad for a main-paper submission. The paper includes supervised learning, language fine-tuning, synthetic/noise analysis, SAC on MuJoCo, PPO on Atari, and ablations. Even though I have concerns about some details, the scope is better than many optimizer papers that only show one regime.

- The RL results are the strongest part of the paper. In **Table 4** on MuJoCo, Ano has the best mean rank and the best normalized average in both the default and “best version” summaries. In **Table 5** on Atari, Ano again has the strongest normalized average and mean rank among the listed methods. If the evaluation protocol is fully clean, this is a meaningful positive signal that the optimizer may indeed help in noisy regimes.

- The figures help convey the intended story. **Figure 2** is particularly useful because it shows learning curves rather than just endpoints, and the authors’ claim that Ano often reaches Adam’s final performance with fewer steps is at least visually plausible on several environments. **Figure 4** similarly suggests that the benefits are not isolated to one RL algorithm. I appreciate that the paper does not rely only on terminal-score tables.

- The ablation table is useful. **Table 6** tries to isolate the roles of the second-moment rule, sign-based direction, gradient magnitude, and the scheduled \(\beta_{1,k}\). This is the right kind of decomposition for a paper whose main contribution is a particular combination of components.

- The paper includes an explicit limitations section, and the limitations are not entirely cosmetic. The authors do acknowledge that their second-moment tweak seems more beneficial in RL than in stationary supervised settings, and they admit that Ano can become unstable due to larger steps.

## Weaknesses
1. **The algorithm is underspecified and internally inconsistent across the main paper, pseudocode, and theory. This is the most immediate technical issue.**  
   In **Algorithm 1 on Page 2**, line 6 defines a bias-corrected variance \(\tilde v_k = v_k / (1-\beta_2^k)\), but line 7 updates parameters using \(\sqrt{v_k}+\epsilon\), not \(\sqrt{\tilde v_k}+\epsilon\). On **Page 3**, the prose writes the Ano update with \(\sqrt{\bar v_k}+\epsilon\), which suggests the corrected quantity should be used. Then in **Algorithm 2** in the appendix, the update is written as \(\sqrt{v_k+\epsilon}\), which is again different from both \(\sqrt{v_k}+\epsilon\) and \(\sqrt{\hat v_k}+\epsilon\). These are not cosmetic discrepancies. Early-iteration behavior of adaptive optimizers is quite sensitive to whether variance correction is applied before or after the square root, and whether it is applied at all. As written, the reader cannot tell what exact optimizer produced the empirical results.

2. **The theory does not actually analyze the practical algorithm presented in the main paper, so the central convergence claim is overstated.**  
   The paper states on **Page 1** and **Page 4** that it provides a convergence guarantee for Ano. However, the proof in **Appendix D** analyzes a different update:
   \[
   x_{k+1,i}=x_{k,i}-\frac{\eta_k}{\sqrt{v_{k-1,i}}+\varepsilon}|g_{k,i}|\operatorname{sign}(m_{k,i}),
   \]
   see **Equation (2)** on **Page 17**, which uses the **delayed** second moment \(v_{k-1}\), not the same-step \(v_k\) used in Algorithm 1. The proof also assumes a **time-varying** \(\beta_{1,k}=1-1/\sqrt{k+1}\) and \(\eta_k=\eta/(k+2)^{3/4}\), which is much closer to the Anolog-style analysis than to practical Ano with fixed \(\beta_1=0.92\) from **Page 3**. This mismatch matters because the paper repeatedly frames the theorem as supporting Ano itself. At best, the theory supports a stylized variant motivated by Ano, not the main practical optimizer evaluated in Section 6.

3. **Several mathematical statements in the proof chain are fragile, inconsistent, or simply not written carefully enough for the level of claim being made.**  
   A few concrete examples:
   - In **Lemma 2** on **Page 18**, the statement
     \[
     \mathbb{P}(\operatorname{sign}(m_{k,i})\neq\operatorname{sign}(\nabla_i f(x_k))\leq \frac{C_m^2}{|\nabla_i f(x_k)|^2\sqrt{k+1}}
     \]
     is malformed, missing a closing parenthesis, and more importantly divides by \(|\nabla_i f(x_k)|^2\). This quantity is undefined when \(\nabla_i f(x_k)=0\), exactly where sign disagreement is not even the right notion. The proof later explicitly says “if \(\nabla_i f(x_k)\neq 0\)”, but the lemma statement itself does not handle the zero-gradient case.
   - In **Theorem 1** on **Pages 23-24**, the denominator constant changes in an unexplained way from \(\tilde G+\varepsilon\) in earlier statements, to \(\sqrt{2}G+\varepsilon\), and then to \(C_{LHS}=\eta/(G+\epsilon)\). These are not the same constants, and no derivation is provided for these substitutions.
   - The proof relies on a “local assumption” with \(g_{k,i}\le \tilde G\) in **Lemma 1** on **Page 17**, while the main assumptions only bound \(|\nabla_i f(x_k)|\le G\) and the variance of \(g_k\). A bounded stochastic gradient itself is stronger than bounded mean plus bounded variance, and the paper says this local assumption “plays no role in the convergence results”, but it is subsequently used in **Lemma 3** to bound the denominator via **Lemma 1**. That is not a minor bookkeeping issue, it is structurally part of the lower bound on \(A_k\).
   - There are repeated notation slips, for example using \(\mathbb E_{k,i}\) once where \(\mathbb E_{k-1}\) is intended, and switching between \(C_A\), \(C_B\), \(C_\Delta\), \(C_m\), and \(C_v\) with uneven definitions. The proof is not at the level where I would feel comfortable saying the technical story is airtight.

4. **The experimental selection protocol is problematic and potentially optimistic in a way that directly affects the headline results.**  
   On **Page 6**, for RL the paper states that “each baseline reports the better of its default or tuned configuration.” This is already an unusually favorable model-selection rule on final benchmark tasks. More concerning, **Appendix C on Page 15** says “we then selected the configuration achieving the highest validation accuracy per seed.” Per-seed hyperparameter selection is not a standard fair protocol, because it lets each random seed pick its own best hyperparameters. For RL, there is also no clearly defined validation split in the usual supervised sense, so the exact model-selection signal becomes very important. Since optimizer comparisons can swing substantially under different tuning rules, this issue is not peripheral. It weakens the credibility of the numerical margins in **Tables 4 and 5**.

5. **The empirical positioning against the most relevant baselines is weaker than it should be, especially given the paper’s own framing.**  
   The paper argues that Ano combines sign-based robustness with adaptive scaling, yet the main supervised and RL benchmark tables omit some especially relevant comparators. In particular:
   - **Yogi** is central to the paper’s second-moment story on **Page 3**, but Yogi is absent from the main benchmark tables. Since the variance update is one of the two core contributions, this omission matters.
   - **Signum** is discussed in Related Work and appears in the ablation **Table 6**, but not in the main benchmark tables. If the paper’s message is that decoupled sign-direction methods are particularly robust in noisy settings, I would expect a direct main-table comparison to Signum or a similarly close sign-based baseline.
   - The comparison to **Grams** is also not developed deeply enough. Grams is arguably the most conceptually adjacent method mentioned in **Section 2**, since both methods decouple direction and magnitude but swap which source provides which signal. This should have been the centerpiece comparator, not just another row in the tables.

6. **The noise-robustness evidence is too narrow relative to how central “noisy landscapes” is to the paper’s title and pitch.**  
   The dedicated robustness analysis in **Section 5.2** is a single CIFAR-10 CNN experiment with additive Gaussian perturbation injected into gradients, summarized in **Table 1**. That is useful, but it is thin relative to the paper’s main motivation. It does not test heavy-tailed noise, label noise, non-stationary supervised targets, batch-size-induced noise changes, or optimizer sensitivity under changing signal-to-noise ratio over training. The paper then draws broad claims about non-stationarity and high-variance robustness. Those claims are mainly supported by RL experiments, not by a systematic robustness analysis. I would have liked a much stronger bridge between the mechanism and the claimed failure mode.

7. **Some tables and figures raise interpretation issues, and a few presentation errors are serious enough to blur the scientific message.**  
   - **Table 3** on **Page 6** contains two rows labeled “Adam” in both the Default and Tuned blocks. One of them is presumably Adan, but as written the table is incorrect. This is not a typo in a caption, it affects the identity of a baseline in a central results table.
   - **Table 4** on **Page 7** contains “Leon” where clearly “Lion” is intended. Again, not fatal alone, but it contributes to a pattern of carelessness.
   - In **Table 2** on **Page 5**, Ano achieves dramatically lower training loss than Adam and Adan under default settings, yet only a modest accuracy gain. That gap suggests either calibration/generalization differences or a learning-rate/regularization tradeoff that is not discussed. The text instead uses this mostly to claim stable supervised behavior. I do not think the table supports that interpretation cleanly.
   - **Figure 1** shows only Adam, Adan, and Ano, whereas **Table 2** includes Lion, Grams, and Anolog as well. Since the figure is used to support the claim that Ano reduces loss “faster and more stably than Adam”, it is fine for that narrow point, but it does not help compare Ano against the full optimizer set actually studied.
   - **Figure 2** appears to visualize only four MuJoCo environments even though **Table 4** reports five, and the panel arrangement is awkward enough that it is hard to match plot to environment. Since the main argument is partly about faster convergence in RL, clarity of this figure matters.

8. **The empirical gains on supervised learning are modest, and in some cases the paper’s own evidence cuts against the broader optimizer story.**  
   On CIFAR-100 in **Table 2**, Ano is slightly ahead under default settings but not under tuned settings, where it is roughly tied with Adam and below its own default result. On GLUE in **Table 3**, the average gain over baselines is small, and the strongest improvements are on a few small tasks with high variance, especially RTE. That is not necessarily bad, but it means the optimizer’s impact seems quite regime-specific. The paper is honest about this in places, yet some of the broader framing still reads as if the method is broadly competitive, whereas the data suggest a more narrow contribution concentrated in RL-like noise.

9. **The stability claim is not fully supported, because several reported confidence intervals remain wide and occasionally overlap heavily with baselines.**  
   The paper frequently uses “more stable” language, for example in **Figure 1** and throughout the RL discussion. But in **Table 4**, Ano’s confidence intervals are quite wide on several tasks, especially HalfCheetah, Ant, Humanoid, and Hopper. In **Table 5**, the intervals on some Atari tasks are also broad. This does not negate the mean improvements, but it does complicate the narrative that the method is inherently more stable rather than simply more aggressive and sometimes better.

10. **The presentation quality is below the standard expected for a mature optimizer paper, especially given the amount of theory included.**  
    Beyond isolated typos, there are recurring issues with notation consistency, line-by-line algorithm formatting, capitalization, missing definitions, and table labeling. The paper is understandable overall, but it often feels one revision away from being precise enough rather than already there. For a submission making both algorithmic and theoretical claims, this matters more than usual.

## Questions
1. **What is the exact update rule used in the experiments?**  
   Please state unambiguously whether the denominator uses \(v_k\), \(\hat v_k\), or \(v_{k-1}\), and whether the implementation is
   \[
   \frac{|g_k|}{\sqrt{v_k}+\epsilon},\quad \frac{|g_k|}{\sqrt{\hat v_k}+\epsilon},\quad \text{or} \quad \frac{|g_k|}{\sqrt{v_k+\epsilon}}.
   \]
   Right now Algorithm 1, the text on Page 3, Algorithm 2, and Appendix D do not agree. A concise clarification here would substantially increase my confidence.

2. **Can the authors clarify precisely what the theorem applies to, and tone down the main-text claim if necessary?**  
   If the convergence guarantee is for a delayed-variance, scheduled-\(\beta_{1,k}\), decaying-step-size variant rather than practical Ano, please say that explicitly. If you believe the theorem still supports the implemented Ano, explain why the mismatch is inessential.

3. **Please clarify the hyperparameter-selection protocol in a benchmark-clean way.**  
   What exactly does “highest validation accuracy per seed” mean on each domain, especially RL? Was model selection done using a held-out validation environment metric, an internal proxy task, or final benchmark returns? Also, if the final tables report the better of “default” and “tuned,” was that choice made using the same test metric later reported? This point could materially change my assessment.

4. **Why is Yogi absent from the main comparison tables, despite being central to the second-moment design?**  
   Since the variance update is one of the two advertised contributions, a direct comparison to Yogi in at least RL and noise-robustness experiments seems important.

5. **Can the authors explain the anomalous behavior of Grams in Table 1 more rigorously?**  
   The current explanation on **Page 5** is speculative. Since Grams is one of the closest conceptual baselines, a more systematic diagnosis, perhaps with step-size/variance traces, would strengthen the paper considerably.

6. **Please fix the likely table labeling errors, especially in Table 3.**  
   If the duplicate “Adam” row is actually Adan, that should be corrected. Seemingly small presentation errors become high-friction when the contribution is mostly empirical.

7. **Could the authors provide stronger evidence for the “faster is better” claim beyond endpoint tables?**  
   For example, in the style of **Figure 2**, reporting area-under-learning-curve, time-to-threshold, or sample-efficiency metrics would better support the title claim than final IQM alone.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard compute usage and benchmarking. I did not identify a paper-specific ethics issue that requires escalation.

## Soundness Rating
2: fair. The paper has a plausible core idea and a nontrivial empirical study, but the mismatch between the analyzed and implemented algorithms, proof inconsistencies, and the unclear tuning/selection protocol prevent me from rating the technical support higher.

## Presentation Rating
2: fair. The paper is readable at a high level, but there are too many inconsistencies across equations, pseudocode, theory, and tables, and some central result tables contain labeling errors.

## Contribution Rating
2: fair. The optimizer idea is interesting and the RL results are potentially useful, but the contribution feels narrower and less well-supported than the paper claims, especially given the limited robustness analysis and the incomplete comparison to the most relevant baselines.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a reasonable optimizer idea and promising RL evidence, but at present there are too many technical and experimental ambiguities for me to support acceptance. With a cleaner algorithm specification, a theory claim that matches the actual method, and a less optimistic, more transparent evaluation protocol, this could become a much stronger submission.

## Reviewer Confidence
4: confident. I am familiar with optimization and deep learning evaluation practice, and I checked the main algorithmic and mathematical claims carefully, though I did not independently verify every appendix derivation line-by-line.