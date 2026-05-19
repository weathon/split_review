Now I have a thorough understanding of the paper and the reviews. Let me write the consolidated review.

---

## Summary

This paper proposes PA-RL, a method that decouples policy improvement from policy parameter update in actor-critic RL. Instead of propagating gradients through the policy's parameters (which is unstable for diffusion policies and intractable for autoregressive categorical policies), PA-RL first optimizes action samples via global re-ranking by Q-values and local gradient ascent on actions, then trains the policy to imitate these optimized actions via a standard supervised (NLL) loss. The method is instantiated on top of Cal-QL and IQL and evaluated on simulated benchmarks (D4RL AntMaze, FrankaKitchen, CALVIN), real-robot fine-tuning of diffusion policies, and simulated autoregressive transformer policies.

## Strengths

- **Strong and consistent empirical results across multiple domains (Table 1)**: PA-RL+Cal-QL outperforms the next best method by 13% in aggregate across AntMaze, FrankaKitchen, and CALVIN, with a 69% improvement on the challenging multimodal CALVIN task. The learning curves (Figure 2) show PA-RL consistently dominating prior methods (IDQL, DQL, DPPO, standard Cal-QL) throughout fine-tuning, demonstrating that the method effectively leverages expressive policy classes.

- **Real-world robot fine-tuning of diffusion policies (Table 3)**: PA-RL achieves 20–35% improvement in success rate on two WidowX manipulation tasks within 1–2 hours (30–70 episodes) of autonomous interaction. The filtered BC baseline shows no improvement, confirming RL is adding value. Figure 3 shows clear behavioral evolution from failure to success.

- **Works across multiple policy classes**: The paper demonstrates PA-RL with diffusion policies (simulation + real), autoregressive categorical transformer policies (simulation), and Gaussian policies (as the Cal-QL baseline), all using the same algorithmic framework. This directly supports the "parameterization-agnostic" claim.

- **Informative ablation study (Table 4)**: The ablation cleanly separates the roles of global optimization (critical on diverse data like antmaze-large-diverse) and local optimization (important on narrower data like CALVIN play data), providing actionable deployment guidance.

- **Clean conceptual contribution**: The core insight — replace the policy gradient with a supervised NLL loss on critic-optimized actions — is simple, intuitive, and clearly explained. The paper correctly identifies why prior approaches (AWR, MPO, filtered BC) differ and why PA-RL can make more aggressive updates.

## Weaknesses

### Fatal
None.

### Major

- **Unsupported headline claim about OpenVLA**: The abstract states that PA-RL "successfully fine-tune[s] diffusion policies and OpenVLA, a 7B parameter generalist robot policy, on real robots," and the introduction claims "PA-RL is the first RL method to improve 7 billion parameter OpenVLA by 75% within 40 minutes of real-world interaction." However, the entire experimental section (Section 5.2) only discusses fine-tuning diffusion policies on a WidowX robot — there is no mention of OpenVLA results, no table, no figure, no experimental setup in the visible main paper. This is not a minor omission: it is the most prominent claim in the paper (abstract + introduction) and it is entirely unsupported in the experimental body. If the results exist in the (parser-stripped) appendix, the main paper should at minimum reference them in the experimental section. As presented, the abstract and introduction are misleading about what the paper demonstrates.

- **Critic backup using optimized actions in Cal-QL is unaddressed**: For Cal-QL, PA-RL replaces the standard policy-sampled actions in the Bellman backup with actions from the optimized distribution $\pi_{\phi}^{\text{Opt}}$ (Section 4.3). This changes the Bellman target: $\mathcal{B}^{\pi}\bar{Q}(s,a) = r(s,a) + \gamma\mathbb{E}_{a' \sim \pi_{\phi}^{\text{Opt}}(\cdot|s')}[\bar{Q}(s',a')]$, which does not correspond to the Q-function of the policy being trained nor of any fixed policy. The paper acknowledges this modification but provides no theoretical or empirical justification that this scheme produces a consistent value function. The IQL variant avoids this concern (IQL never samples the policy for TD targets), and it is telling that the IQL results (Table 2) show only marginal improvement over IDQL. The paper should either justify why this modified backup is valid (e.g., showing it approximates a policy iteration step) or ablate against using the actual policy for the Bellman backup.

- **No variance reporting for any quantitative result**: Tables 1, 2, 3, and 4 report raw scores (returns, success rates) without standard deviations, confidence intervals, or even mention of the number of seeds. Given the known instability of diffusion policy fine-tuning (acknowledged for DQL and DPPO in the paper), the reader cannot assess whether the claimed improvements (13% aggregate, 69% on CALVIN, 224% for transformers) are statistically significant or reflect a single run. This is the paper's primary quantitative evidence, and the lack of any uncertainty measure is a serious omission.

### Minor

- **DPPO comparison requires clarification**: The paper notes DPPO is "substantially more data inefficient" and uses different x-axis units in Figure 2, but Table 1 reports numbers for all methods "after 1k episodes of fine-tuning." It is unclear whether DPPO's reported numbers in Table 1 are after 1k episodes or a different budget. Since DPPO is a key baseline, this should be clarified.

- **Equation 4.6 (AWR comparison) is heuristic**: The paper acknowledges that obtaining the LHS requires Taylor expansion assuming small step size $\alpha$, and that the Q-function may be inaccurate OOD. This is fine as intuition but should be more clearly labeled as heuristic rather than a formal guarantee.

- **Real-robot results lack confidence intervals**: The paper reports improvement ranges (20–35%) and mentions 30–70 episodes of interaction, but does not provide per-trial outcomes or confidence intervals. Given the small sample count, success rates could be noisy.

### Trivial

- The transformer architecture used for autoregressive categorical policies is described only as "discretizes each dimension of the action space independently into a set of 128 bins" with no details on architecture size, number of layers, or training cost.

## Nice-to-Haves

- **Gaussian policy trained with PA-RL**: The paper's central "agnosticism" claim would be strengthened by showing that PA-RL trained on a standard Gaussian/MLP policy performs no worse than SAC's reparameterization gradient on standard benchmarks. This would directly demonstrate that PA-RL is not just "works for diffusion" but genuinely agnostic.

- **Quantify the computational cost**: The paper mentions sampling multiple actions per state as a limitation but does not quantify wall-clock time or number of forward passes. For a 7B parameter model like OpenVLA, understanding this cost is important.

## Removed Points

These points were flagged in the reviews but are removed with justification:

- **"Missing hyperparameters in main text"**: The paper states implementation details are in the appendix, which the parser strips. Per instructions, criticisms about missing appendix content are removed.
- **"Missing theoretical proof for critic consistency"**: The paper is primarily an empirical contribution. Requesting full theoretical proofs for an empirical systems paper goes beyond community standard. The critic backup concern is retained as a Major weakness, but the call for formal proof is downgraded.
- **"OpenVLA results may not exist"**: Removed per instruction that cited references are assumed to exist. The weakness retained is about the **absence of support in the visible main body**, not about the existence of the results.
- **"Missing related works"**: Removed per instruction not to mention missing related works without external verification.
- **Strength about OpenVLA being first RL fine-tuning of 7B model**: Removed because it conflicts with the verified weakness that this claim is unsupported in the experimental section.

## Novel Insights

None beyond the paper's own contributions. The reviews largely recapitulate the paper's claims and concerns without offering a genuinely new synthesis or insight that the paper itself does not provide.

## Suggestions

1. **Either include the OpenVLA experiment in the main paper or remove the claim from the abstract and introduction.** This is the most important action. If the results are in the appendix, add a clear reference (e.g., "See Appendix X") in Section 5.2 and ideally a summary table or learning curve in the main paper.

2. **Add variance estimates to all quantitative results.** Report means and standard deviations over at least 3–5 seeds for Tables 1, 2, and 4. For the real-robot results (Table 3), report per-trial outcomes or bootstrap confidence intervals.

3. **Address the Cal-QL critic backup concern.** Either (a) provide a justification showing the modified Bellman backup is valid (e.g., it corresponds to a form of policy iteration), or (b) include an ablation comparing to a version that uses the actual policy (trained on optimized actions) for the Bellman backup.

4. **Clarify the DPPO comparison** — specify the fine-tuning budget used for DPPO in Table 1.

## Score and Decision

The paper addresses an important problem (RL algorithms tied to specific policy parameterizations) with a clean, intuitive method. The core experiments on diffusion policies and autoregressive transformers are strong and represent a genuine advance. However, the paper currently makes an unsupported headline claim about OpenVLA in its abstract and introduction with zero supporting evidence in the experimental body, lacks basic statistical reporting, and uses a questionable critic backup without justification. These are not fatal to the paper's core contribution but require substantive revision. Given the strength of the core method and results on diffusion + transformer policies, I lean toward acceptance with major revisions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>