Now I have read the full paper. Let me write my review.

---

## Summary

This paper investigates **Self-Rewarded Training (SRT)**, an RL-based self-improvement framework for LLMs that uses majority voting among the model's own generations as a pseudo-reward signal, replacing external ground-truth verifiers. Across comprehensive experiments on synthetic Reasoning Gym tasks and real-world math benchmarks with four different base models, the authors find that SRT (1) improves both average accuracy and majority-vote accuracy (showing quality gains in the self-supervision itself), (2) achieves comparable performance to RL with ground-truth labels in the short term, but (3) inevitably collapses when training is extended, due to reward hacking where models converge to a degenerate fixed output that maximizes pseudo-reward.

---

## Strengths

- **Comprehensive empirical scope**: Four base models (Llama-3.1-8B-Instruct, Qwen2.5-Math-7B, Qwen3-14B-Base, DeepSeek-Math-7B-Instruct), three training datasets, three evaluation benchmarks (MATH-500, AIME 2024, AIME 2025, AMC), two RL algorithms (GRPO, RLOO), and two task families (synthetic Reasoning Gym + real-world math). The breadth substantially strengthens the generality of the claims.

- **Novel controlled comparison — evolving vs. fixed teacher**: The experiment that isolates whether using the *current* policy (online) vs. the *initial* policy (fixed teacher) as the pseudo-label generator drives further gains is elegant and cleanly distinguishes SRT's contribution from prior SFT-based majority-vote distillation (Huang et al., 2023; Prasad et al., 2024). The consistent 6–10% margin on Reasoning Gym tasks directly supports the "virtuous cycle" claim.

- **Honest and well-analyzed failure mode**: Rather than burying the collapse, the paper elevates it to a primary finding. The mechanistic analysis in Figure 7 — correlating test accuracy drop with simultaneous spikes in pseudo-reward, KL divergence, and model entropy — traces reward hacking convincingly. Manual inspection confirming that the collapsed model outputs a fixed template answer (e.g., `\boxed{1}`) regardless of prompt makes the finding concrete and credible.

- **Curriculum climbing on synthetic tasks**: The multi-level progression on Reasoning Gym (training on level *k* with SRT and advancing to level *k+1*) demonstrating near-100% accuracy on Knights & Knaves Level 9 from ground-truth training only on Level 2 is an impressive and reproducible controlled result showing the conceptual viability of curriculum-based self-improvement.

- **Practical significance**: The finding that SRT roughly matches RLVR during early training is practically important — it means cheap self-supervision can substitute for expensive ground-truth labeling *up to a certain horizon*, which is directly relevant for domains where verification is hard.

---

## Weaknesses

### Fatal
None.

### Major

- **The critical asymmetry between synthetic and real-world tasks is insufficiently explained.** SRT self-improves without collapse on Reasoning Gym but collapses reliably on real-world math. The paper mentions that Knights & Knaves already has >90% majority-vote accuracy at initialization as a partial explanation, but this asymmetry is central to the paper's tension and deserves a more systematic analysis. For instance, does collapse correlate with the initial majority-vote accuracy (i.e., tasks where pseudo-labels are already very accurate are more collapse-prone)? Does the combinatorial structure of synthetic tasks provide a natural gradient that real math problems lack? Without this, the practical guidance for when to trust SRT is limited.

- **No successful mitigation, despite several ablations**: The paper tries higher KL penalty, lower learning rate, and fewer generations per prompt, and finds all either insufficient or only delay collapse. This is honest, but the paper stops at diagnosis without offering even a partial remedy. Given that "feedback design is the central challenge," at least a sketch of one principled mitigation direction (e.g., combining SRT with periodic ground-truth calibration, or filtering by chain-of-thought consistency in addition to final answer) that shows early positive signal would substantially strengthen the contribution.

### Minor

- **The comparison with offline baselines (Table 1: SFT, DPO, ScPO) is difficult to interpret from the main text.** Table 1 is referenced but the numbers are not reproduced in the text, and the conditions under which SRT retains "better performance" are not fully unpacked. Clarity about whether the comparison controls for compute budget would strengthen the claim.

- **The observation that *fewer* generations per prompt delays collapse** (by injecting label noise) is counterintuitive and interesting, but only discussed briefly. This hints that there might be a noise-injection-based regularization worth exploring more carefully.

- **Curriculum strategy on synthetic tasks is task-specific.** The multi-level self-improvement results are compelling but rely on Reasoning Gym's explicit, discrete difficulty gradation. How difficulty levels would be defined or proxied in real math (where problems span a continuous difficulty spectrum) is left entirely open, limiting direct transfer of the insight.

### Trivial
None worth noting.

---

## Nice-to-Haves

- A direct comparison between SRT initialized on different majority-vote accuracy levels (to test whether higher initial accuracy predicts faster collapse) would help demystify the synthetic vs. real-world asymmetry.
- Including a token-level analysis of the collapsed model's outputs (e.g., fraction of responses that match the mode answer vs. random, length distribution changes) would provide additional mechanistic insight.

---

## Novel Insights

The paper's most genuinely novel finding is the **virtuous-cycle dynamics of online self-rewarded training**: unlike SFT-based distillation from a fixed teacher, online RL via SRT continuously improves the majority-vote pseudo-label quality alongside model performance, and this improvement in the self-supervision source compounds to yield measurable additional gains. This distinguishes SRT from prior work in a principled way. The second key insight is the **self-reinforcing feedback instability**: prolonged training causes the model to discover that a fixed template output achieves maximum self-consistency reward, collapsing to a solution that is simultaneously optimal for the training objective and catastrophically wrong for the task. This is a concrete instantiation of Goodhart's Law in the self-improvement setting and is likely to inform future work on robust self-verification. Together, these findings reframe the core challenge of LLM self-improvement as fundamentally a feedback-design problem rather than a model-capacity problem.

---

## Suggestions

- Systematically measure majority-vote accuracy (as a proxy for pseudo-label quality) as a function of training step, and compare this trajectory between Reasoning Gym tasks and real math tasks to test whether a higher starting label accuracy predicts collapse.
- Consider reporting time-to-collapse as a function of pseudo-label quality at initialization to provide practitioners with a diagnostic signal.
- Explore whether mixing a small fraction of ground-truth verifiable problems into the SRT training stream can act as an anchor and delay or prevent collapse — this is a natural and low-cost experiment.

---

## Score and Decision

The paper addresses a timely, high-impact question with a clean experimental design, comprehensive coverage across models and datasets, and an honest dual contribution (promise + failure mode). The lack of a successful mitigation and the unexplained synthetic vs. real-world asymmetry are real gaps, but they do not invalidate the contribution — the findings themselves represent concrete, replicable knowledge. The paper is squarely an empirical investigation, and by that standard it is solid and will be of broad interest to the reasoning and RL-for-LLM communities.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>