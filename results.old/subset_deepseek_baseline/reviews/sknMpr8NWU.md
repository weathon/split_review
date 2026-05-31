## Summary

The paper proposes Multi-Agent Evolve (MAE), a framework that instantiates three roles—Proposer, Solver, and Judge—from a single LLM and trains them jointly via task-relative REINFORCE++. The system forms a closed propose–solve–judge loop with domain-agnostic self-rewarding signals (quality, difficulty, format rewards) and quality filtering, aiming to improve LLM reasoning across math, coding, science, and general knowledge without external verifiers or human-annotated ground truth. Experiments on Qwen2.5-3B-Instruct show average gains of 4–5% over the base model and competitive or better results compared to the AZR self-play baseline and supervised fine-tuning.

## Strengths

- **General-domain self-improvement without verifiable rewards.** The framework’s use of an LLM-based Judge to provide reward signals for both question generation and answering removes the need for environment-specific verifiers (e.g., Python interpreters), extending self-play RL to tasks where ground-truth rewards are unavailable.
- **Comprehensive experimental evaluation.** The paper tests on 22 benchmarks spanning in-distribution and held-out sets, covering math, coding, reasoning, and general knowledge. The results show consistent improvements over the base model and competitive performance against AZR and SFT, with ablations that isolate the contribution of each role and of quality filtering / format rewards.
- **Training dynamics analysis.** The authors monitor dataset growth, difficulty scores, and overall accuracy over 250 steps, demonstrating that the model learns to produce increasingly challenging but solvable questions and that performance improves accordingly. This provides supporting evidence for the “desirable difficulty” effect.
- **Ablation study confirms design choices.** Disabling training of any one role or removing quality filtering leads to measurable drops in performance, validating that each component plays a role in the co-evolution process.

## Weaknesses

### Fatal
None

### Major

- **Unspecified LLM judge for evaluation.** The paper states that most benchmarks (except coding) are evaluated by “a strong LLM as the judge”, but never identifies which model is used. This is a critical reproducibility issue: the evaluation pipeline is not transparent, and the judge’s accuracy or potential biases (e.g., favoring certain answer styles, making mistakes on hard questions) are not validated. Without knowing the evaluator or its reliability, the reported scores must be interpreted with caution.
- **Only one backbone model tested.** All experiments use Qwen2.5-3B-Instruct. While the paper promises future scaling, claims about **scalability and generality** of the framework would be much stronger with at least one additional model size (e.g., 7B or 8B). The results on a single small model are insufficient to demonstrate that the method generalizes beyond the specific setting tested.
- **Marginal improvement over the AZR baseline.** In the “zero” setting (no real-world data), MAE (zero) achieves an overall average of 58.51 vs. AZR’s 57.72—a gain of only 0.79 points. On many individual benchmarks, AZR outperforms MAE (zero). The paper claims that MAE “surpasses previous methods”, but the improvement is small and inconsistent, weakening the significance of the contribution relative to the state of the art.

### Minor

- **Ablation sensitivity is modest.** Removing any single role (Solver, Proposer, or Judge training) drops overall average by only 2–3% (from 59.87 to 57.24–57.90). While the direction is consistent, the magnitude is small, which raises the question of whether the roles are as essential as claimed or whether the main benefit comes from the overall RL training loop.
- **Incremental novelty.** The combination of LLM-as-judge, multi-agent interaction, and self-play RL has been explored in prior works (Self-Rewarding LM, SPIRAL, Self-RedTeam, R-Zero). The specific triad of Proposer–Solver–Judge with synchronized updates is new, but the individual components are well-established, limiting the conceptual novelty.
- **Dependence on seed data.** Even the “no reference” setting initializes the valid question pool with 967 questions from real datasets (without ground truth). The “zero” setting uses 16 self-generated questions, which is minimal but still a non-zero seed. The claim of “no human annotation” is largely true, but the framework still requires a small set of domain-covering initial questions to bootstrap.

### Trivial

- Figure 2’s caption is a near-duplicate of the same text in the main body; this does not affect content quality.

## Nice-to-Haves

- Specify the LLM judge used for evaluation (e.g., GPT-4, Qwen2.5-72B) and include a validation experiment showing high agreement with human judgments on a sample of test instances.
- Run the same experiments on a larger backbone (e.g., Qwen2.5-7B-Instruct or Llama-3.1-8B) to demonstrate that the approach scales.
- Provide qualitative examples of generated questions and Judge evaluations to illustrate how self-rewarding signals drive improvement.
- Compare with additional self-play baselines that also target general domains (e.g., SPIRAL if applicable, or a variant of Self-Rewarding with RL).

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

- Clearly state the LLM judge used for evaluation in both the main text and the experiment section, and describe the evaluation prompt or rubric. Consider validating judge accuracy against human labels for a subset of 100–200 samples.
- Add experiments on at least one larger model (7B or larger) to support claims of scalability and general applicability.
- Provide a more detailed comparison with AZR: analyze on which benchmark categories MAE excels and where it falls short, and discuss whether the differences are statistically significant.
- In the ablation section, report the variance across multiple runs (seeds) to assess whether the 2–3% drops are significant.

## Score and Decision

**Score:** 6  
**Decision:** Accept