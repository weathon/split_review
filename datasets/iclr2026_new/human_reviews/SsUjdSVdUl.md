## Human Reviewer 1

### Summary
The paper proposes Critique-RL, a two-stage reinforcement learning (RL) framework for training critiquing language models. The critic  models that assess the correctness of an actor’s response and provide natural language feedback to guide refinement. The core motivation is to avoid reliance on stronger supervisors for critique annotation, which is costly and hard to scale. The key insight is that optimizing solely via indirect rewards, whether the actor’s refined output is correct, leads to poor discriminability, the critic’s ability to accurately judge whether an initial response is correct. To address this, Critique-RL introduces a two-stage training process. Experiments on mathematical reasoning benchmarksshow consistent improvements over baselines.

### Strengths
1. The problem setup, motivation, and methodology are clearly articulated with intuitive figures (e.g., Figure 2, 3) and precise definitions of evaluation metrics
2. Scalable oversight remains a critical bottleneck in LLM alignment and self-improvement. By explicitly disentangling and jointly optimizing two key critique capabilities, the work offers a practical and empirically validated pathway toward more reliable critique models.
3. The identification of problem due to conflicting objectives under indirect rewards is compelling.

### Weaknesses
1. The paper claims to avoid “stronger supervisors” for critique data, yet relies heavily on ground-truth answers (i.e., golden labels) to construct both direct (Stage I) and indirect (Stage II) reward signals. These labels are typically human-annotated or derived from curated datasets (e.g., MATH, GSM8K). Thus, the method still depends on human-provided supervision, albeit not in the form of natural language critiques. This undermines the central motivation that existing approaches “rely on stronger supervisors for annotating critique data”—since here, human-labeled answers serve as an equally strong (if not stronger) form of supervision.
2. Lack of analysis of some highly related works in this paper [1], which also proposes to use the refinment as the additional feedback.

> [1] Training Language Models to Critique With Multi-agent Feedback

### Questions
No question

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

---

## Human Reviewer 2

### Summary
The paper addresses the challenge of insufficient scalable supervision for LLMs in complex reasoning tasks. It proposes Critique-RL, a two-stage reinforcement learning framework without strong supervision. In the first stage, the critique model’s discriminative ability is optimized using direct rule-based rewards. In the second stage, the framework integrates indirect rewards from agent-corrected response accuracy with regularization to enhance the usefulness of feedback while preserving discriminative capacity. Critique-RL achieves  performance improvements over baselines on several mathematical reasoning and question-answering tasks.

### Strengths
- The proposed two-stage RL method is effective to provide constructive critique feedback for better refinement and precise filter for effective time-time scaling.
- The experiments contain several benchmarks across different tasks.
- This paper is well-written and easy to follow.

### Weaknesses
My main concern lies in the experimental design, as I am not fully convinced that the current experiments sufficiently demonstrate the proposed method’s advantage on complex reasoning tasks.

- Since the authors explicitly state in the Abstract and Introduction that their method targets complex reasoning tasks, more challenging benchmarks such as AIME and GPQA should have been included in the evaluation.

- Although the main text reports significant improvements on Qwen-3B and Qwen-7B, the appendix reveals that the performance gains on stronger models, such as DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-72B-Instruct, are quite limited. These results should be reported and discussed in the main paper.

- The proposed method requires access to ground-truth answers to compute rewards. Under this setting, it remains unclear what advantages it offers over directly training the model’s reasoning ability using RLVR methods (e.g., GRPO, DAPO). Additional experiments are needed to clarify this distinction.

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper proposes Critique-RL, a two-stage reinforcement learning (RL) approach to train critiquing language models without requiring stronger supervision. The authors first show that baseline RL methods, which use only indirect rewards from an actor's refinement, fail. This is because they improve the critic's helpfulness (constructive feedback) but not its discriminability (judging correctness), leading to poor performance. Critique-RL solves this by:
- Stage I: Explicitly optimizing discriminability using direct, rule-based reward signals.
- Stage II: Optimizing helpfulness using indirect rewards (actor refinement) while using regularization to maintain the discriminability from Stage I.

This two-stage strategy delivers performance improvements on both in-domain and out-of-domain tasks, e.g., +9.02% in-domain and +5.70% OOD for Qwen2.5-7B.

### Strengths
- The paper's core originality is its clear diagnosis of a key failure mode in training critics: baseline RL methods create a conflict between "discriminability" (judging correctness) and "helpfulness" (providing feedback), optimizing the latter at the expense of the former.
- The paper's quality is high, with a rigorous methodology. The training dynamics in Figure 3 clearly show the baseline's failure , while decisive ablation studies in Table 3 prove that both stages of Critique-RL and its specific regularization are essential for success.
- The work significantly contributes to scalable oversight by providing an effective method to train critics without stronger supervisors. Its value is shown through broad applicability, including "weak-to-strong" generalization (a 7B critic improving a 72B actor) and effectiveness on OOD and open-ended tasks .

### Weaknesses
- The paper's primary motivation is to train critics "without stronger supervision"1. However, the entire method, especially the critical Stage I, is heavily reliant on an "oracle reward function" $r_{oracle}(x,y)$ to compute the direct discrimination reward $r_{dis}$. For the main experiments on math tasks, this oracle is a rule-based verifier that knows the correct answer. This oracle is a form of strong, external supervision.
- The framework's success, particularly in Stage II, hinges on a critical assumption: the fixed actor model $\pi_{\theta}$ is already a good "refiner". The authors state the actor is pre-trained to be "capable of... faithfully refining them according to critiques". This assumes away a large part of the problem. The helpfulness reward $r_{refine}$ is a convolved signal of both the critique's quality and the actor's ability to understand it. If the actor is a poor refiner, $r_{refine}$ becomes a noisy or meaningless signal, and Stage II would fail to optimize for helpfulness.
- The paper correctly highlights its inference-time compute-efficiency benefits (e.g., in Figure 1 and Figure 6). However, it completely omits the training-time cost of this complex, two-stage RL pipeline. Stage II, for example, requires at least three model forward passes per training sample (one for the critic $c=\pi_{\phi}(x,y)$, one for the actor's refinement $y^{\prime}=\pi_{\theta}(x,y,c)$, and one for the oracle/RM $r_{refine}=r_{oracle}(x,y^{\prime})$). This is significantly more expensive than the SFT or baseline RL methods it's compared against.
- The paper's core insight is that final-outcome rewards are insufficient, and a more direct signal is needed. The proposed solution, $r_{dis}$, is a direct reward for judging the outcome of the original response. This overlooks a more direct comparison to Process-based Reward Models (PRMs), which provide supervision at each step of the reasoning. The qualitative examples (Figs. 8, 9) show the critic is evaluating step-by-step, but it is only trained on the final answer's correctness.

### Questions
The paper is motivated as an approach for training critique models "without stronger supervision". However, the method's crucial first stage relies entirely on a direct reward $r_{dis}$ from an "oracle reward function" $r_{oracle}(x,y)$. This oracle, which knows the ground-truth correctness, seems to be a form of strong supervision.

Could you please clarify this apparent contradiction?

1. How do you formally define the "stronger supervision" (which you avoid) versus the "oracle verifier" (which you use)?
2. The paper's contribution seems to be a novel way to distill the knowledge of a "weak" binary oracle (answer-checker) into a "strong" generative critic (feedback-generator). Would you agree with this framing?
3. How does this framework scale to complex domains (e.g., creative writing, complex coding) where no such simple oracle or high-quality reward model exists?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes an online RL approach called Critique-RL for developing critiquing language models without stronger supervision. This approach contains a two-player paradigm, where the actor generates a response, the critic provides feedback, and the actor refines the response accordingly. The authors devise a two-stage optimization strategy, where stage I reinforces the discriminability of the critic with direct rule-based reward signals and stage II introduces indirect rewards based on actor refinement to improve the critic’s helpfulness. Experimental results show the effectiveness of Critique-RL.

### Strengths
1. The proposed two-stage RL method is sound and well-motivated, which deals with the core problem of critique generation.
2. Extensive experiments show the effectiveness of the proposed method.
3. This paper is overall well-written and easy to follow.

### Weaknesses
1. The design of indirect rewards based on actor refinement is similar to [1], which is not discussed in the current paper. The authors should further clarify the difference between this work and [1] to highlight their novelty.

2. The quality of generated critiques should be individually measured via automatic metrics or human evaluation.


[1] Training Language Model to Critique for Better Refinement. ACL 2025 Findings.

### Questions
I have included my questions in the weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4