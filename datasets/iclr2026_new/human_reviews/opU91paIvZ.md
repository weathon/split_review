## Human Reviewer 1

### Summary
This paper addresses chain-of-thought (CoT) monitorability by focusing on faithfulness (whether reasoning reflects the true factors) and conciseness (brevity for monitoring). The authors claim standard reinforcement learning fails due to sparse rewards. They propose a prior-guided framework where a 7B auxiliary model transforms CoT traces from a 1.5B base model into monitorable versions, which are filtered and used for supervised fine-tuning. Experiments on MMLU-Pro, GSM8K, and MATH500 show approximately 10% faithfulness improvement and up to 60% length reduction while maintaining roughly 96% of base accuracy.

### Strengths
- Important problem for AI safety: Given the acceleration in AI capabilities, the field needs monitoring capabilities.
- Clear mathematical formulation: Constrained optimization framework (Eq. 1) provides principled setup.
- Proof-of-concept validation: Figure 3 demonstrates monitorable traces preserve task performance.

### Weaknesses
- Unsupported "RL fails" claim: No algorithm details, or hyperparameter specification provided. The contradiction with successful GRPO/PPO applications in practice makes me doubt the credibility of the results (DeepSeek-R1, o1).
- Faithfulness-conciseness tradeoff ignored: These objectives directly conflict but are treated independently with no joint optimization or Pareto analysis.
- Circular teacher dependency: Requires 7B model to fix 1.5B model. If prior generates faithful reasoning, why not use it directly?
- Uninspiring empirical results: 25% faithfulness means 75% unfaithfulness remains.
- Flawed evaluation: Hint injection is artificial proxy for real unfaithfulness.
- Missing critical baselines: No properly-tuned GRPO/PPO, or even strong prompting baselines.

### Questions
- What specific RL algorithm and hyperparameters did you use? Why only 500 steps? Properly-tuned GRPO works quite well with length penalty. 
- How do you handle the faithfulness-conciseness tradeoff when optimizing jointly?
- Can you provide human evaluation for faithfulness claims?

### Soundness
1

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes a framework for improving the monitorability of chain-of-thought (CoT) reasoning in large language models.
The authors define two key criteria—faithfulness (alignment between reasoning and actual model decision process) and conciseness (brevity of explanations)—and introduce a prior-guided distillation method.
In this approach, a stronger teacher model (e.g., Qwen2.5-Instruct) rewrites verbose CoT traces produced by a smaller base model into shorter, more faithful forms. The refined data are then used for supervised fine-tuning of the base model.
Experiments on GSM8K, MATH500, and MMLU-Pro show that the distilled model generates shorter reasoning traces while maintaining comparable answer accuracy, suggesting improved monitorability.

### Strengths
1. Clear problem motivation (improving interpretability and faithfulness of CoT).

2. Well-written and reproducible experiments.

3. Results show meaningful improvement in conciseness and surface-level faithfulness without major accuracy loss.

4. Framing the goal of “monitorable reasoning” provides a useful vocabulary for reasoning safety discussions.

### Weaknesses
1. The method is essentially a simplification distillation—a teacher rewrites long CoTs and the student learns to mimic them.
This process is widely adopted and not novel as a training paradigm.

2. Simplifying CoTs may harm reasoning fidelity in complex multi-step problems; longer chains often encode necessary intermediate logic.
The paper does not test this on genuinely complex reasoning tasks (e.g., proofs, multi-hop logical reasoning, or coding).

3. The “faithfulness” metric relies on external LLM judgments and does not truly measure causal reasoning alignment.

### Questions
1. How does the proposed distillation perform on genuinely long or compositional reasoning tasks, where simplification may remove necessary steps?

2. Does the method generalize without a stronger teacher model for rewriting?

3. How is this approach different in substance from previous CoT distillation or self-distillation works (e.g., Self-Review)?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper introduced a framework for improving the monitorability of CoT reasoning. They identify the current CoT traces are often unfaithful or verbose, and it is hard to control. To address this, this paper propose to use CoT monitorability as a  constraint during optimization. A key contribution is they introduced a prior-guided data generation method: using a prior model to transform unfaithful or lengthy reasoning traces into high-quality and monitorable ones. Experimental results on MMLU-Pro, GSM8K, and MATH500 show the proposed approach improves faithfulness by ~10-22% and reduces the length by ~60%.

### Strengths
1. This paper works on a pretty valuable and interesting direction: monitorability in reasoning models. It is important because we need a faithful reasoning model which outputs trustworthy CoT. The area is underexplored in previous literature. 
2. The proposed prior-guided data generation method is new and effective, which is a good synergy to RL training recipe.
3. The empirical results are quite strong. It improves the faithfulness by 10% and reduces the length by 60%, although the performance drops a bit (4%).

### Weaknesses
1. The proposed prior-guided distillation method heavily relies on an external prior model (e.g., Qwen-7B Instruct) to generate “monitorable” reasoning traces. This suggests that the observed improvement may stem from the prior model’s inductive bias, rather than the generalizability of the proposed framework itself.
2. The faithfulness evaluation depends on judgments made by the llm-as-a-judge approach, lacking objective annotation or inter-rater reliability verification.
3. The authors define monitorability as consisting of faithfulness and conciseness, but do not provide a unified quantitative formulation for this concept.
4. At line 171, the authors used 950 as a threshold to judge the conciseness. I wonder why 950? 
5. The experimental design could be improved by introducing more datasets. Testing on MATH500/GSK8K and MMLUPro is not sufficient. Existing models are powerful on more complex tasks like AIME, LiveCodeBench. It is better to test the method on more complex tasks.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3
