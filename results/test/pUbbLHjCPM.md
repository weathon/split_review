Now I have a thorough understanding of the paper. Let me compile the final review.

## Summary

The paper proposes Progressive Thought Refinement (PTR), a framework to train LLMs to iteratively refine their own outputs without task-specific fine-tuning or external feedback. PTR has two stages: (1) constructing a dataset using a weak-strong model collaborative selection strategy (weak model generates initial thoughts, strong model produces refined answers, with consistency filtering), and (2) weighted thought-mask fine-tuning that teaches the model to improve upon previous thoughts by masking the thought tokens and optimizing a multi-term loss. Experiments across ten diverse tasks show average improvement from 49.6% to 53.5%, with the method outperforming Prompt, IFT, and RL baselines.

## Strengths

- **Demonstrated generalization across ten diverse tasks without task-specific fine-tuning**: The paper shows PTR raises average performance from 49.6% (base) to 53.5%, with gains spanning knowledge reasoning (MMLU +7%), code (HumanEval), math (GSM8K, MATH), comprehension (DROP), summarization (XSum), and complex reasoning (ARC, GPQA). This directly supports the central claim of activating general progressive refinement ability.

- **Novel weak-strong model collaborative selection strategy for annotation-free dataset construction**: The approach of using a weaker model to generate initial thought sequences (which may be incorrect) and a stronger model to produce refined answers via ICL, followed by consistency filtering, eliminates the need for ground-truth labels — a key limitation in prior refinement work. This is a genuine methodological contribution.

- **Weighted thought-mask fine-tuning that targets the improvement process**: The thought-mask mechanism that computes loss only on the refined final answer, combined with the multi-term loss encouraging logical consistency and increasing confidence, differs meaningfully from standard IFT. The comparison showing IFT on the same data fails to activate iterative refinement (Table 1) provides evidence that the design is nontrivial.

- **Robustness across different prompts and LLMs**: Table 3 shows PTR yields consistent iterative improvements under three different prompt templates, and both Qwen2-7B and Llama3-8B exhibit similar upward trends, demonstrating the benefit is not tied to a specific instruction or model architecture.

## Weaknesses

### Fatal
None.

### Major

- **Loss function is critically underspecified (Equation 1).** Three terms appear in the loss but key components are not defined: (a) $\mathcal{F}_{\text{cons}}(y_t, y_{t-1})$ — called "logical consistency" — is given no mathematical or operational definition; it could be KL divergence, cosine similarity on hidden states, a reward signal, or something else. (b) The $\beta_t$ coefficients for the confidence term have no specified schedule. (c) The $\lambda_1, \lambda_2, \lambda_3$ weights are said to be "dynamically adjusted according to the model's needs, with their sum constrained to 1" but no mechanism, schedule, or update rule is given. Since the loss function is the paper's central technical contribution, this level of vagueness makes the method unreproducible and prevents proper evaluation of the core claim.

- **Weak and strong models used in dataset construction are not named.** The paper describes three selection criteria (Model Parameter Strength, Model Version, Domain-Specific Fine-Tuning) but never states which concrete models served as $\theta_w$ and $\theta_s$ for any experiment. Were Qwen2-7B and Llama3-8B (the target models) also the weak model? Was the strong model GPT-4, Qwen2-72B, or something else? This is essential for interpreting the results: if the strong model is significantly more capable, the method may be distilling that model's refinement behavior rather than "activating intrinsic ability" as claimed, and the IFT comparison does not fully rule this out since IFT is a different objective (supervised on answers only).

- **Inference procedure for iterative refinement is not described.** The paper reports performance over multiple "iterations" (up to 10 in Figure 4) but never specifies the inference protocol. Is the model called multiple times with the refinement instruction ("Please continue thinking and refine your answer") as a prompt appended to its previous output? Is the previous iteration's output fed as a "thought" in the same format as during training? Without a precise description, the iteration-based results are not reproducible, and it is unclear whether the model is being used as the authors intend.

### Minor

- **RL baseline (DPO) preference construction is underspecified.** The paper states it uses the PRD dataset to "construct preference data, and prefer model to produce stronger answers through DPO," but never specifies how preferences are determined — by model confidence, answer length, automatic evaluation, or something else. This makes the RL baseline comparison difficult to interpret.

- **No analysis of data leakage between training set and evaluation benchmarks.** The training data is cleaned from WizardLM (~50k→40k pairs). The paper states "we exclude domain-specific testing queries during training" but provides no overlap analysis. Since WizardLM is a general instruction dataset that likely contains questions similar to MMLU, GSM8K, HumanEval, etc., and the evaluation benchmarks are popular, the possibility of data leakage exists and is not addressed. This would be a standard addition to strengthen confidence in the generalization claim.

- **"Emergence" terminology is overstated.** The paper describes the gradual improvement of performance during training as "emergence" or "emergent behavior" (e.g., "emergence of inference capabilities," "clear emergent behavior"). This is simply a learning curve with task-specific timing differences; calling it "emergence" adds no analytical value and could mislead readers into inferring phase-transition-like phenomena that are not demonstrated.

- **ICL and consistency filtering details are missing.** The paper mentions using in-context learning and consistency filtering during dataset construction but does not specify what ICL examples are used, how they are selected, or how "consistency" is measured and what threshold is applied for filtering.

### Trivial

- The term "PRD" appears in the RL baseline description (line 235) while the dataset is called "PTR" elsewhere; this inconsistency should be resolved.

## Nice-to-Haves

- An ablation study isolating the contributions of the three loss terms (removing $\lambda_2$ and/or $\lambda_3$ individually) would clarify whether the thought-mask mechanism alone drives improvements or whether the extra terms are necessary.
- An ablation where the weak and strong models are the same model (or the gap is narrowed) would help test whether the benefit comes from the training objective itself or from the strong model's knowledge.
- Human evaluation or qualitative analysis for open-ended tasks like XSum would strengthen the claim that the model produces more "thoughtful" outputs beyond accuracy.

## Removed Points

These points were raised by the initial reviewers but are removed or downgraded per the review guidelines:

- **"No comparison to Self-Refine with fine-tuning"**: Self-Refine (Madaan et al., 2023) is a prompting-only method, not a fine-tuning approach. The paper does cite it in related work. Asking for experimental comparison to a prompting method when the paper focuses on fine-tuning is a mismatch of expectations. The paper's baselines (Prompt, IFT, RL) are reasonable for its class. _(Removed — evaluates paper against wrong class of method)_

- **"The weak-strong selection criteria could lead to weak model outperforming strong model on some domains"**: While technically possible, the paper's goal of ensuring $\theta_s \gg \theta_w$ is stated as a design principle, and the three selection strategies (parameter strength, version, domain fine-tuning) provide reasonable heuristics. This is a theoretical edge case that does not undermine the experimental results. _(Downgraded — hypothetical concern not shown to affect actual results)_

- **"Performance improvement report should specify which iteration's results"**: The paper reports the average across tasks and the improvement from 49.6% to 53.5%. While it would be cleaner to specify, the improvement is clear from context. _(Removed — parser artifact ambiguity; the main result is interpretable)_

## Novel Insights

The most interesting observation across the reviews is the tension between the paper's claimed mechanism ("activating intrinsic refinement ability") and an alternative explanation ("distilling the strong model's refinement process"). The IFT comparison partially addresses this, but the real test — which the paper does not run — would be to narrow or close the weak-strong capability gap and see whether the training signal still produces iterative improvement. If the benefit disappears when the weak and strong models are the same, that would suggest the method is fundamentally about distilling refinement behavior from a stronger model; if it persists, the "activation of intrinsic ability" claim would be more strongly supported. This distinction is important for future work in this direction.

## Suggestions

1. **Define $\mathcal{F}_{\text{cons}}$ explicitly** — even a simple cosine similarity or KL divergence with a reference would suffice.
2. **State the schedule for $\beta_t$ and the adjustment rule for $\lambda_{1,2,3}$** — these could be simple (e.g., fixed constants, linear decay) but must be specified for reproducibility.
3. **Name the specific weak and strong models** used for each experiment (e.g., "Qwen2-1.5B as weak, Qwen2-72B as strong").
4. **Describe the inference protocol precisely**: provide the exact prompt template used at each iteration, how the previous output is fed back, and how the process is terminated.
5. **Add a data overlap analysis** between the WizardLM-derived training set and the ten evaluation benchmarks, or at minimum discuss the likelihood of leakage and its potential effect on results.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>