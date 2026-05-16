Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes MA-RLHF, a framework that integrates macro actions (sequences of tokens treated as single decision units) into the RLHF pipeline for aligning LLMs. By operating at a coarser temporal granularity under a semi-Markov decision process formulation, MA-RLHF reduces the temporal distance between actions and reward signals, addressing the credit assignment problem in token-level RLHF. The method is evaluated across summarization (TL;DR), dialogue (HH-RLHF), and question answering (WebGPT) using Gemma models from 2B to 7B parameters, achieving consistent improvements in RM scores (up to +68%), GPT-4/human win rates, and convergence speed (1.7–2× faster).

## Strengths

- **Novel application of macro actions (options) to RLHF for LLMs.** The paper formalizes macro actions within an SMDP framework (§3.2) and applies hierarchical RL concepts to the LLM alignment problem. This is a principled approach grounded in established RL theory (Sutton 1999, Precup 1997) that prior RLHF work has not exploited. The idea is clearly motivated by the credit assignment problem, which is a genuine bottleneck in token-level RLHF.

- **Large and consistent empirical improvements across multiple tasks and model sizes.** On TL;DR summarization, MA-PPO improves test RM scores by +68% (2B) and +30% (7B) over vanilla PPO (Table 2). On HH-RLHF dialogue the improvement is +18% for both model sizes, and on WebGPT QA it reaches +8% (7B). GPT-4 win rates against vanilla PPO reach 86% (TL;DR 7B) and 78% (TL;DR 2B) (Figure 3). These gains are substantial and span multiple open-ended generation tasks, with human evaluation corroborating the trend (e.g., 74% and 69% win rates on TL;DR).

- **Faster convergence without additional computational overhead.** MA-PPO achieves parity with vanilla PPO 1.7× to 2× earlier in training: e.g., the Gemma-2B model requires ~1.7k MA-PPO updates to match the test RM score that vanilla PPO reaches after 3.7k updates (Figure 2). The paper explicitly states that this does not increase computational complexity during training or inference, which is a practical advantage.

- **Connection to prior methods as extreme cases of macro-action length.** Section 3.2.3 notes that when macro action length = 1, MA-RLHF reduces to standard token-level RLHF, and when length → ∞, it converges to RLOO/REINFORCE. This provides a unified perspective that clarifies how MA-RLHF interpolates between dense and sparse reward settings.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Primary quantitative evaluation relies on the same reward model used for training.** The RM scores in Table 2 (the main quantitative results) are computed using the same RM that provided the training signal. While the paper supplements these with GPT-4 and human pairwise evaluations, those are conducted on only 50 instances per setting. The GPT-4–human agreement is moderate (58–64%, averaging 62%), and the RM–human agreement (74–76%) is decent but not conclusive. The small sample size (50) means the win-rate point estimates (e.g., 78–86%) carry substantial uncertainty (roughly ±14 percentage points at 95% confidence for a 78% win rate). The paper should report confidence intervals or error bars on all win-rate figures and ideally increase the human evaluation sample size or acknowledge the limitation more explicitly.

- **The value of n for the fixed n-gram termination condition is not stated.** Section 3.3.1 says fixed n-gram performs best and is used as the default, but the specific value of n is never provided in the visible main text. This is a concrete reproducibility gap for a core design choice. (This detail may appear in the analysis/appendix sections that were stripped by the parser; if so, it should be stated in the main paper.)

### Trivial

- The paper refers to "Marco-Action RLHF" in the section header (line 86) instead of "Macro-Action RLHF" — a minor typo.

## Nice-to-Haves

- A sweep over n-gram lengths (n = 1, 2, 3, 5, 10, etc.) showing how performance varies would provide the cleanest evidence for the credit-assignment story. The paper mentions that such analysis is deferred to §sec:ma_analysis, which was stripped; if it appears there, including a summary in the main text would strengthen the paper.

- An analysis of how macro actions affect advantage estimates (e.g., variance or temporal delay) would deepen the mechanistic understanding beyond reporting final scores.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Unreported hyperparameters and potential baseline under-tuning"** — Removed per the rule about missing appendix content and nitpicks about reproducibility. The parser strips appendix sections; hyperparameter details standardly appear there. The paper references \Cref{datasets} and includes \input{section/analysis}, indicating the original submission contained these details.

- **"Lack of transparent comparison among macro-action strategies"** — Removed per the rule about missing appendix content. The paper explicitly states "We provide further analysis on the impact of |ω_τ| in \S\ref{sec:ma_analysis}" and includes \input{section/analysis}, which was stripped by the parser.

- **"Code generation results absent from main text"** — Removed per the rule about missing appendix content. The paper mentions code generation in §4.1 and the abstract; results were likely in the stripped analysis section.

- **"Missing related works"** — Per instructions, I do not mention missing related works without external confirmation.

## Novel Insights

The most notable insight across the reviews is that the macro-action formulation in MA-RLHF provides a principled bridge between token-level PPO and sequence-level methods like RLOO/REINFORCE — this unifying perspective (Section 3.2.3) is itself a conceptual contribution that goes beyond the empirical results. The reviews did not surface any novel insight that the paper's own contributions do not already capture.

## Suggestions

1. Include confidence intervals or error bars on the win-rate bar charts (Figure 3) and explicitly discuss the uncertainty introduced by the 50-instance sample.
2. State the specific n-gram length used as the default in the main experimental section (§4.1), not just in the appendix.
3. Add a brief summary of the ablation over termination conditions and n-gram lengths to the main paper, even if the full analysis remains in the appendix.
4. Clarify in the main text that the RM scores serve as a training-progress metric while the primary evidence for downstream quality comes from GPT-4 and human evaluations.

## Score and Decision

The paper introduces a well-motivated, principled method that is clearly explained and backed by consistent empirical gains across tasks and model sizes. The weaknesses are primarily around the thoroughness of statistical reporting (lack of confidence intervals on small-sample evaluations, reliance on the training RM for the main quantitative metric) and minor missing details (n-gram length). None of these undermine the core claim that macro actions improve RLHF — they are addressable in a camera-ready revision. The methodological contribution is novel in the RLHF context, the experiments are broad, and the results are compelling.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>