Now let me finalize the review.

**Round 1 bracket:** Based on comparisons with WtHKqtHVXo (4.00 — weaker, fewer tasks, oversold claims), qGL6fE1lqd (4.40 — similar issues with unvalidated core claims), and iTsHStJKcm (5.25 — better validated, real robot experiments), CoRAL sits in the **4.0–5.5** range. Applying the instruction to lower brackets below 5 by 1-2 points: narrowed to **3.5–5.0**.

**Round 2 narrowing:** Comparing CoRAL against the round-2 anchors: u6imHU4Ebu (5.75 — LLaRP, much stronger evaluation with 150K training tasks, cleaner validation) sits clearly above CoRAL. Aqfwhna1D7 (5.20 — CrayonRobo, also better validated) is above CoRAL. qGL6fE1lqd (4.40 — LLMPhy, similar mix of interesting ideas + unvalidated claims) is the closest comparator below. WtHKqtHVXo (4.00) is clearly below.

CoRAL has more architectural substance and task diversity than qGL6fE1lqd but shares the fundamental problem of unvalidated core claims, plus has a factual inconsistency (Figure 4 vs. text) that qGL6fE1lqd doesn't have. I place CoRAL at **4.5**, slightly above LLMPhy due to richer architecture and broader evaluation, but held well below the 5.0+ range by the combination of the numerical inconsistency and unsubstantiated core novelty.

---

## Summary
CoRAL proposes a modular framework that separates vision-based perception (FoundationPose for pose tracking, GPT-4o as VLM for estimating physical parameters) from LLM-based reasoning (GPT-4o generating MPPI cost functions and contact strategies), connected through a reactive MPPI controller with nested feedback loops and a memory unit. Evaluated on six simulated contact-rich manipulation tasks, the system is compared against OpenVLA-OFT, π₀.₅, human-designed cost baselines, and several ablations. The core idea — having an LLM formulate the mathematical structure of an optimal control cost function — is genuinely novel, but the paper does not adequately substantiate its central claims.

## Strengths
- **LLM as cost-function designer — a genuine conceptual advance.** Rather than using LLMs merely as perceptual guides (as in IMPACT/VLMPC), CoRAL has the LLM formulate the structure and weights of the MPPI cost function (Sec. 3.2, lines 85–98). This is a clear conceptual step beyond prior work and is well-positioned against the literature (lines 43–44).
- **Contact-strategy ablation yields compelling quantitative evidence.** Removing the LLM's initial contact strategy C₀ on T6 ("Flip with Wall") and forcing uninformed random sampling makes the guided approach 83.9% faster (32 vs. 199 steps) and cuts end-effector travel by 63.9% (1.33 m vs. 3.69 m; Sec. 4.1.4, lines 216–218). This is a clean, well-measured result.
- **Unified VLM ablation starkly validates role separation.** Collapsing perception and planning into a single multimodal prompt yields 0/10 on four of six tasks (T1, T3, T5, T6; Table 1), demonstrating that explicit VLM/LLM role separation is essential — though the ablation does confound prompt structure with role separation.
- **Memory unit produces consistent cross-task improvements.** Comparing CoRAL with vs. without memory (Table 1) shows gains across five of six tasks: T1 (2/10→4/10), T3 (9/10→10/10), T5 (7/10→9/10), T6 (5/10→7/10), with speed improvements.
- **w/o Refinement ablation demonstrates outer loop's functional importance.** Removing the online adaptation loop causes dramatic drops: T1 from 4/10 to 0/10, T3 from 10/10 to 3/10, and T5 from 9/10 to 4/10 (Table 1).

## Weaknesses

### Fatal
None.

### Major
- **Factual inconsistency between text and Figure 4 undermines the parameter adaptation evidence.** The text (line 220) states the initial mass was deliberately set to 2.0 kg with ground truth 0.1 kg, but Figure 4's caption and axis labeling show initial mass at 1.00 kg corrected to ~0.85 kg. These are entirely different numerical regimes, making the key robustness result incoherent. Furthermore, friction convergence is claimed in the text but not visualized. This is not a minor typo — it directly affects the credibility of a central result.
- **VLM physical parameter estimation is entirely unvalidated.** The system asks GPT-4o to estimate mass and friction from RGB-D images — a remarkable claim. The paper provides zero measurement of estimation error against ground truth, no ablation substituting ground-truth parameters to measure the VLM's contribution, and no comparison against naive defaults (e.g., mass=1kg, friction=0.5). The online adaptation loop may correct VLM errors, but this raises the question of what value the VLM adds beyond reasonable default values.
- **LLM-generated cost functions — the paper's core technical novelty — are never shown concretely.** Equation 2 is explicitly labeled "only an illustrative example" (line 91). The paper provides zero examples of actual GPT-4o-generated cost functions for any of the six tasks. The reader cannot assess whether the LLM produces sensible costs, what terms it introduces, or how it determines weights. The central contribution is asserted but not demonstrated in the main text.
- **$x_{des}$ is undefined in Equation 7, making the reactive control augmentation non-reproducible.** The feedback term $K_f \cdot (x_{des} - x_{measured})$ (line 128) relies on a desired state $x_{des}$ that is never defined anywhere. Where it comes from and how it relates to the MPPI plan is unclear, preventing implementation from the paper alone.

### Minor
- **Underpowered trial counts.** 10 trials per task with binary success/failure provides limited statistical power. The difference between CoRAL with memory (4/10) and without (2/10) on T1 is 2 trials and could be consistent with noise. No confidence intervals or statistical tests are reported.
- **Completion time is conditioned on success.** Methods with different success rates are not comparable on time-to-completion, yet Table 1 reports completion times only for successful trials without acknowledging this confound.
- **VLA comparison demonstrates OOD generalization, not architectural superiority.** OpenVLA-OFT and π₀.₅ were evaluated using LIBERO checkpoints on the authors' custom contact-rich tasks. The paper acknowledges this (line 193) but claims of "significantly outperforms" (lines 193–194) oversell what this comparison demonstrates.
- **"Unified VLM" ablation confounds several variables.** It uses a single prompt instead of structured multi-step prompting, may have different effective context budgets, and produces less structured outputs. The result is informative but doesn't cleanly isolate role separation as the causal factor.
- **Both VLM and LLM are GPT-4o, making the "separation" prompt-level only** (confirmed at line 153). The framing in Sections 3.1–3.2 could be read as implying distinct models; this should be stated more prominently.
- **Memory retrieval mechanism is underspecified.** Line 75 states "the LLM embeds the current task into a latent semantic space" but it is unclear whether this uses an embedding endpoint, a separate model, or is done via prompting; similarity thresholds are not specified.

### Trivial
None beyond the above.

## Nice-to-Haves
- Report computational cost (GPT-4o API latency) for the inner/outer loops, as this affects real-time feasibility.
- Replace the random-sampling baseline in the contact strategy ablation with a heuristic baseline (e.g., sample near the object's closest face) for a more informative comparison.
- Run 20–30 trials with confidence intervals for stronger quantitative claims, especially given small deltas between conditions.

## Removed Points
*These points were flagged for removal — treat them with caution if referencing.*

- **HC: VLA baselines fundamentally invalidate headline comparison (claimed as Fatal).** REMOVED as fatal — the paper openly acknowledges the VLAs were fine-tuned on LIBERO (line 193), and the comparison does test zero-shot generalization, which is a valid evaluation paradigm. Kept as Minor since the paper could more carefully frame what this comparison demonstrates.
- **HC: Should compare against ForceVLA, RDP, FACTR.** REMOVED — these are hardware-centric approaches requiring specialized force/tactile sensors, which is a different paradigm the paper explicitly distinguishes (lines 45–46).
- **HC: w/o Pose Tracking ablation is a straw man.** REMOVED as a standalone criticism — conflating "obvious" with "uninformative." The ablation demonstrates a specific claim (VLM cannot substitute for a pose estimator) which is useful.
- **HC: Expert FSM underperformance shows CoRAL is weak.** REMOVED as an independent weakness — the paper honestly acknowledges CoRAL remains below the FSM upper bound (lines 195–197). This is transparency, not a flaw.
- **SF: "Comprehensive evaluation design with meaningful baselines."** REMOVED — too generic and conflicts with valid concerns about trial counts and VLA baseline framing.
- **SF: "w/o Pose Tracking ablation provides conclusive evidence."** Merged into strengths but noting the finding is expected rather than surprising.
- **Missing appendix / Appendix ?? references.** REMOVED per instructions — parser strips appendices; these exist in the original submission and should not be flagged.
- **HC: "the paper does not substantiate its central claims… in its current form, the paper does not make a convincing case"** — this is a summary judgment, not a specific weakness rooted in evidence. Removed as a distinct weakness; the substance is captured in the Major weaknesses above.
- **HC: "The LLM cost-function generation is treated as a black box"** — merged into the Major weakness about LLM outputs never being shown.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- **Highest priority:** Resolve the Figure 4 / line 220 numerical inconsistency. If the text is correct (2.0→0.1 kg), update the figure; if the figure is correct (1.0→0.85 kg), update the text. Either way, show both mass and friction convergence.
- **Define $x_{des}$** explicitly in Section 3.3 and explain how it relates to the MPPI plan.
- **Add a simple validation experiment:** compare CoRAL using VLM-estimated physical parameters against CoRAL using ground-truth parameters and against CoRAL using naive constants (mass=1kg, friction=0.5) to quantify the VLM's added value.
- **Show the LLM's actual outputs** — include a table mapping each task to the LLM's generated cost terms, weights, and contact regions, with a brief qualitative assessment of whether each is physically sensible.
- **Temper claims about the VLA comparison** — explicitly state it demonstrates zero-shot generalization rather than architectural superiority per se.

## Score and Decision

**Anchor comparison:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| N581Nje6fH | 1.50 | R1 | Much weaker — no empirical contribution |
| koza5fePTs | 2.00 | R1 | Different domain (LLM planning benchmark) |
| hCfhfwSfCg | 2.00 | R1 | Weaker — limited evaluation |
| zEhTnQZB3D | 2.33 | R1 | Weaker — limited evidence |
| 70kYH6InYU | 3.50 | R1/R2 | Weaker — less comprehensive, lower novelty |
| WtHKqtHVXo | 4.00 | R1/R2 | CoRAL is stronger — more tasks, richer architecture, better ablations |
| qGL6fE1lqd | 4.40 | R1/R2 | CoRAL has richer architecture and broader evaluation but shares issues with unvalidated core claims; CoRAL's factual inconsistency is an additional concern |
| iTsHStJKcm | 5.25 | R1/R2 | Above CoRAL — better validated claims, real robot experiments |
| Aqfwhna1D7 | 5.20 | R2 | Above CoRAL — better validated |
| u6imHU4Ebu | 5.75 | R2 | Clearly above — much stronger evaluation at scale |
| MWHIIWrWWu | 6.25 | R1 | Above — different domain, stronger |
| lFYj0oibGR | 6.50 | R1 | Clearly above — SOTA benchmark results |
| OI3RoHoWAN | 8.00 | R1 | Far above — exceptional paper |
| 7BLXhmWvwF | 8.00 | R1 | Far above — exceptional paper |

**Round 1 bracket:** 4.0–5.5, adjusted to 3.5–5.0 per the lower-range adjustment rule.
**Round 2 narrowing:** CoRAL sits between qGL6fE1lqd (4.40) and iTsHStJKcm (5.25), closer to the lower anchor. The combination of the Figure 4 inconsistency, unvalidated VLM parameter estimation, unshown LLM cost functions, and the undefined $x_{des}$ places it below the 5.0 threshold. The architecture is novel and the ablation design is thoughtful, but the core claims are insufficiently substantiated.

**Final score: 4.5**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>