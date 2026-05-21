---
job_id: efed9a05-3c11-460e-a509-82ad79d91c02
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: YETCQLcKtn.pdf
paper: PolicyFlow: Policy Optimization with Continuous Normalizing Flow in Reinforcement Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies reinforcement learning, generative policies, and optimization for expressive policy classes in robotics/control settings.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, presents a concrete method, and includes quantitative and qualitative experiments; while I have substantial concerns about theory, exposition, and evaluation, these are review-level weaknesses rather than desk-reject issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes PolicyFlow, an on-policy reinforcement learning method that combines PPO-style optimization with continuous normalizing flow policies. The core idea is to avoid full likelihood evaluation along the CNF trajectory by approximating the importance ratio using velocity-field differences along an interpolation path, and to add a Brownian-inspired regularizer intended to encourage entropy growth and reduce mode collapse. The method is evaluated on MultiGoal, MuJoCo Playground, and IsaacLab benchmarks against PPO and selected generative-policy baselines including FPO and DPPO.

## Strengths
The paper tackles a relevant problem. Extending PPO-style policy optimization to more expressive policy classes is important, especially for multimodal action distributions where Gaussian policies are a poor fit. Framing CNF policies in an on-policy RL setting, while trying to avoid full pathwise likelihood computation, is a worthwhile direction.

The method has a reasonably clear high-level structure. Equation (4) defines the conditional flow, Equations (12)-(13) give the practical training objective, and Algorithm 1 makes the proposed training loop fairly concrete. Even though I have concerns about some details, the overall recipe is understandable.

The empirical section contains both qualitative and quantitative evidence across multiple environments. In particular, **Figure 2** is useful because it directly visualizes the claimed advantage of expressive multimodal policies: PPO, DPPO, and FPO show much weaker goal coverage, whereas PolicyFlow with the Brownian regularizer reaches a visibly more balanced spread over the six targets. This figure is one of the paper’s strongest pieces of evidence that the proposed regularizer is doing something nontrivial in a deliberately multimodal setting.

The paper also includes ablations rather than just headline benchmark numbers. **Figure 4(a)** is helpful because it tests the paper’s own central claim that the clipping range \(\epsilon\) trades off approximation quality and learning progress. **Figure 4(b-c)** further show that initialization and time-sampling choices do matter, and the authors do not hide these implementation sensitivities.

There are some encouraging benchmark results. **Table 1** shows that PolicyFlow is at least competitive with PPO on several IsaacLab tasks, with statistically significant gains on Navigation and G1, even if the margins are modest elsewhere. **Table 2** is also useful: it addresses the practical concern that CNF-based policies may be too expensive, and the reported runtime overhead appears moderate rather than prohibitive.

## Weaknesses
1. **The central importance-ratio approximation is only weakly justified, and the math in the main paper overstates what is actually established.**  
   The key methodological step is the replacement of the terminal displacement \(\delta_{\varphi_1}(\mathbf z; \mathbf s)\) by velocity variation evaluated along the interpolation path in **Equation (10)**, followed by the approximation of the PPO ratio in **Equation (13)**. The main text then states in **Equation (11)** that the approximation error is \(\mathcal O(\epsilon)\), with the explanation that PPO clipping naturally enforces a small-update regime. There are several problems here. First, the approximation in Eq. (10) uses an expectation of Gaussian density ratios over \(t\), whereas Appendix A eventually derives a first-order statement for the **log** likelihood under additional assumptions. Those are not the same object. The appendix even says “we thus correct the conclusion from the main text” in **Appendix A.2**, which is a red flag because it means the main-paper statement is not cleanly aligned with the actual derivation. Second, the argument depends on assumptions such as \(\|\delta_{v_t}\|\le \epsilon\) and a Lipschitz constant \(L_\delta = \mathcal O(\epsilon)\), stated on **Page 15**, which are precisely the nontrivial quantities one would need to justify from the optimization dynamics. In other words, the theory is largely conditional on the approximation already being benign. This matters because the entire algorithm lives or dies on whether the approximate ratio behaves enough like the PPO ratio to support stable policy improvement. Right now the paper gives a heuristic, not a convincing guarantee.

2. **There are mathematical and notation inconsistencies around the PPO objective and state distribution, which make it harder to trust the derivation.**  
   In **Equation (2)** on Page 3, the outer expectation is written as \(\mathbb E_{p_\pi(\mathbf s)}\mathbb E_{\hat\pi(\mathbf a|\mathbf s)}[\cdots]\), but the text immediately below refers to \(p_{\hat \pi}(\mathbf s)\) as the policy’s state distribution. This is inconsistent with standard PPO notation, where one optimizes using states sampled from the old/reference policy, not the new policy. A similar mismatch appears in **Equation (3)** and then in **Equation (7)**, where the paper “rewrites” the proxy objective but changes the state distribution notation again. This is not a cosmetic issue. The exact sampling distribution matters in policy gradient surrogates, especially when the claimed monotonic-improvement intuition is invoked. If the derivation is meant to be under data from \(\hat \pi\), the equations should consistently say so; if not, the algorithmic estimator in Algorithm 1 does not match the stated objective.

3. **The Brownian regularizer is interesting, but its connection to actual entropy regularization is much looser than the prose suggests.**  
   Section 4.1 starts from the heat equation and continuity equation, then motivates choosing \(v_t(\mathbf x) = -\nabla_{\mathbf x}\log p_t(\mathbf x)\). But the actual regularizer in **Equations (15)-(16)** does not regularize the policy entropy, nor does it derive from an explicit lower bound on entropy growth. The paper itself concedes this in the remark on **Page 7**: “The Brownian regularizer should not be regarded as a theoretically exact derivation.” That honesty is appreciated, but it also undercuts the stronger language used earlier, where the method is described as an entropy regularizer “inspired by Brownian motion” that promotes monotonic entropy growth. At present, this is closer to a heuristic velocity-field penalty than to a principled entropy objective. The distinction matters scientifically, because readers may otherwise infer stronger guarantees about exploration and diversity than the paper actually provides.

4. **The empirical comparisons are incomplete in places where they matter most.**  
   The paper claims broad competitiveness against PPO, FPO, and DPPO, but the evidence is uneven. On IsaacLab, the paper compares only against PPO and explicitly omits FPO/DPPO due to engineering difficulty, see **Section 5.2** and the remark below **Table 2**. I understand the engineering burden, but from an evaluation standpoint this weakens the paper’s positioning because the main novelty is precisely in the context of expressive generative policies. If the strongest competing methods are absent on the most realistic robotics benchmark, the reader cannot tell whether PolicyFlow’s gains come from the CNF parameterization, the regularizer, or simply from being compared to a Gaussian baseline.

5. **Some of the claimed benchmark conclusions are stronger than what the presented numbers support.**  
   The text around **Table 1** says PolicyFlow “consistently matches or surpasses PPO across all tasks.” That is too generous. In the table, PolicyFlow is numerically lower on Open-Drawer, Quadcopter, H1, and Go2. The \(p\)-values indicate statistically significant wins on Navigation and G1, but also a statistically significant loss on H1. This is not a disaster, but the paper should describe the results more carefully. Likewise, the MuJoCo Playground discussion on **Page 8** says PolicyFlow achieves performance comparable to or exceeding FPO in most environments and outperforms DPPO. Yet **Figure 3** is only a set of learning curves without a summarized terminal-performance table or statistical comparison, which makes that claim difficult to verify rigorously. A results table corresponding to Figure 3 would materially strengthen the paper.

6. **Fairness of experimental budgets is not fully convincing, especially on MultiGoal.**  
   The MultiGoal setup in the appendix shows substantially different training configurations across methods. For example, **Table 8** gives FPO 4096 parallel environments, 32 minibatches, 16 epochs, and \(1.2\times 10^8\) total environment steps, while **Table 7** gives PolicyFlow 1024 environments and 5 epochs. These are not obviously matched compute or sample budgets. If Figure 2 is intended as a comparative statement about optimization quality rather than “best effort under separate tuning,” this mismatch should be controlled more carefully. The same concern applies to DPPO/FPO tuning more broadly: the paper says it follows configurations from the FPO paper, but that does not automatically imply fairness in a new environment or under different implementation details.

7. **The strongest qualitative figure is persuasive, but it also exposes how narrow the evidence for multimodality really is.**  
   **Figure 1** and **Figure 2** together are visually compelling. Figure 1 shows exploration heatmaps in PointMaze, and Figure 2 shows MultiGoal rollouts with markedly better mode coverage under the Brownian regularizer. However, these figures mainly establish that the regularizer helps on specially structured multimodal navigation problems. They do not show that multimodal action distributions are actually important in the higher-dimensional locomotion/manipulation tasks where most of the benchmark weight lies. If the paper’s central thesis is that CNF expressivity materially improves RL, I would have liked at least one additional diagnostic on the larger benchmarks, for example action-distribution visualizations, diversity metrics, or policy entropy proxies, rather than just reward curves.

8. **Equation-level implementation details that affect reproducibility are underspecified in the main paper.**  
   In **Equation (13)** and Algorithm 1, the approximate ratio \(\rho\) is used inside a clipped PPO objective. But several practical details are unclear from the main text: whether \(\sigma^2\) is state-independent or state-dependent, how it is parameterized and constrained positive during optimization, whether the same sampled \(t_k\) is reused across epochs, and whether the expectation in **Eq. (10)** is estimated with one sample or multiple samples per transition. Algorithm 1 suggests one sample, but the theoretical notation uses \(\mathbb E_{p(t)}\). These details affect both variance and approximation quality. For a method whose claimed advantage is computational efficiency without loss of stability, such omissions matter.

9. **The exposition is rough in several places, including typos and citation issues, and this is not just cosmetic.**  
   Examples include “PolicyFlow demonstrates is widely favored” in the abstract, “velocity filed variations” below **Equation (13)**, “we purpose a practical entropy regularizer” above **Equation (15)**, and several inconsistent symbols such as \(w_h\) vs. \(w_b\) in **Tables 10** and **15**. The references section also appears noisy, with several author names and dates mangled. Individually these are minor, but in aggregate they make an already delicate method harder to parse and reduce confidence that all mathematical statements were checked carefully.

## Questions
1. The main technical concern is the approximation underlying **Equations (10), (11), and (13)**. Can the authors clarify, in the rebuttal, the exact object for which they claim a first-order bound: the ratio itself, the log-ratio, or the induced policy-gradient estimator? A clean statement that aligns the main text with Appendix A would increase my confidence.

2. Can the authors provide empirical evidence that the approximate ratio \(\rho\) tracks the exact conditional ratio \(\pi(\mathbf a|\mathbf z,\mathbf s)/\hat\pi(\mathbf a|\mathbf z,\mathbf s)\) on small tasks where exact ODE-based evaluation is feasible? Even a calibration plot or correlation statistic on MultiGoal would be very informative.

3. For the Brownian regularizer, can the authors better justify why minimizing \(\|\eta_t(\mathbf x_t;\mathbf s,\theta)\|_2^2\) in **Equation (15)** should be interpreted as promoting entropy growth, rather than simply acting as a smoothness or anti-collapse prior on the velocity field? A more careful conceptual explanation, possibly separating “entropy-inspired” from “entropy-regularizing,” would help.

4. Regarding **Table 1**, can the authors temper or refine the claim that PolicyFlow “consistently matches or surpasses PPO across all tasks,” especially given the significant degradation on H1? If there are per-task qualitative or stability patterns that explain these mixed outcomes, that would be useful to include.

5. For **Figure 3**, can the authors provide a corresponding summary table with terminal rewards and uncertainty across MuJoCo Playground tasks? The current figure suggests competitive performance, but a quantitative table is needed to support claims like “exceeding FPO in most environments.”

6. Can the authors clarify fairness of budgets for MultiGoal and other benchmarks? In particular, are DPPO, FPO, PPO, and PolicyFlow matched in environment steps, wall-clock time, or parameter updates? If not, I would like to understand the comparison protocol more precisely.

7. Since IsaacLab is the most practically interesting benchmark suite here, it would help if the authors could discuss whether comparisons to FPO/DPPO are feasible in a limited subset, even if a full integration is not. A partial comparison would significantly strengthen the paper’s empirical positioning.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics concerns that require separate review are evident from the paper. The work studies standard RL algorithms in simulated environments and does not present human-subject data, private data, or obvious misuse-sensitive artifacts beyond the usual dual-use considerations for robotics/control.

## Soundness Rating
2: fair. The method is plausible and partially supported empirically, but the core approximation is only heuristically justified, the math in the main text is not fully aligned with the appendix, and the experimental support does not fully validate the strongest claims.

## Presentation Rating
2: fair. The high-level idea is understandable, and the figures help, but there are several notation inconsistencies, equation-level ambiguities, and writing issues that materially affect clarity.

## Contribution Rating
2: fair. The paper addresses an important problem and contains an interesting approximation strategy plus a useful regularization idea, but the current theoretical and empirical support is not yet strong enough for me to view it as a clearly solid contribution for ICLR.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see real promise here, especially the multimodal-policy motivation and the qualitative results in **Figures 1-2**. However, the core ratio approximation is not yet pinned down rigorously enough, the Brownian regularizer is more heuristic than the presentation initially suggests, and the experimental story is missing some key comparisons and quantitative summaries. With a tighter derivation, cleaner exposition, and stronger validation of the approximation itself, this could move up meaningfully.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I checked the main derivations and experiments carefully, and the remaining uncertainty is mostly about whether some omitted implementation details or additional evidence could alleviate the concerns above.