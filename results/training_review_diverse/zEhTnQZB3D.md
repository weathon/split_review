Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me write the consolidated review.

## Summary

This paper proposes LLIT (Learning with Language Inference and Tips), a framework for continual reinforcement learning that combines LLM-generated task descriptions and tips with an auxiliary reward model and a modulation prompt pool. The LLM generates task content and tips from descriptions of the observation/action spaces; these are used to train an auxiliary reward model that provides semantic reward signals, while task content embeddings are organized in a pool that retrieves modulation vectors for the Decision Transformer. Experiments on Continual World benchmarks (CW10, CW20) show strong empirical performance — highest average performance (0.94 on CW20), lowest forgetting (−0.02), and best generalization — against ten baselines including regularization-based, structure-based, and rehearsal-based methods.

## Strengths

- **Strong and consistent empirical outperformance**: On CW10 and CW20 sequences, LLIT achieves the highest average performance across all compared methods (0.90/0.94 vs. next-best ~0.86/0.89), the lowest forgetting, and the best generalization metric. The gains over strong baselines like ClonEx-SAC and HAT are substantial and consistent across multiple random seeds. The improvement holds on both standard CW sequences and mixed-domain task sequences.

- **Novel conceptual integration of language into continual RL**: Using a frozen LLM to generate task content and tips from observation/action space descriptions (Section 3.1), then grounding these in a learnable auxiliary reward model (Section 3.2), is a genuinely novel idea in the continual RL setting. The paper positions this against prior structure-based, rehearsal-based, and regularization-based methods that do not leverage semantic language signals.

- **Ablation confirms the necessity of learnable components in the modulation pool**: The ablation study (Table 2) shows that freezing the dictionary ("D frozen") or freezing both dictionary and prompt optimization ("both frozen") degrades performance significantly (from 0.94 to as low as 0.82), confirming that the learnability of the modulation pool components is essential to the reported gains.

- **Memory efficiency without replay**: The modulation pool avoids storing past experiences, directly reducing memory and computation compared to rehearsal-based methods like CLEAR. The strong results on long sequences (CW20) demonstrate effective forgetting control without a replay buffer.

## Weaknesses

### Major

1. **The auxiliary reward model training is critically underspecified.** The paper states that an auxiliary reward model "is trained" (Section 3.2) and "pre-trained" (abstract) as a transformer that takes concatenated embeddings of parsed tips and observations, outputting an auxiliary reward R_a. However, the paper never specifies: (a) the loss function used to train this reward model, (b) what data it is trained on (online rollouts? offline trajectories? synthetic data from the LLM?), (c) whether it is trained jointly with the policy or separately and at what stage, (d) how the auxiliary reward is combined with the environment reward in the Decision Transformer framework, and (e) how the reward model is validated to have "converged" before the policy training proceeds. The "frozen similarity model" that parses tips (Section 3.2) is also never identified — is it a sentence encoder, an LLM, a simple string matcher? Because the reward model is a core claimed contribution (the mechanism by which language influences the policy), these omissions prevent evaluation of the method's soundness and reproducibility from the paper alone. (Code is provided, which mitigates this somewhat, but the paper should be self-contained.)

2. **The claim of "adaptation to unseen tasks" overreaches the experimental evidence.** The abstract, introduction, and conclusion repeatedly claim that LLIT achieves "generalization to unseen tasks" and "adaptation to unseen tasks." However, the experiments (Section 5.1) evaluate only on standard Continual World sequences (CW10, CW20) where the agent sees and learns every task sequentially. There is no evaluation where tasks are held out during training and tested zero-shot afterward. The "Generalization" metric (Section 4.3) measures the average number of steps to reach a success threshold when first encountering each task in the sequence — this measures *learning speed* on the current task, not transfer to held-out tasks. The paper would need at minimum a held-out task experiment (e.g., training on 16 tasks, testing zero-shot on 4 unseen ones) to support the "unseen tasks" claim. This is an overclaim that inflates what the experiments demonstrate.

3. **Weak coupling between the language component and the modulation pool; the language reward model is never ablated.** The paper's narrative claims the modulation pool "captures the semantic correlations among tasks" and that this arises from language instructions. However, the modulation pool queries are *state-derived* (mean-pooled state token embeddings from the DT), not language embeddings. The task content embedding e_tn feeds into the prompt pool's key-value structure, but the retrieval mechanism (Equation 5) uses the *state-based* query q_t against pool keys — it is unclear how language semantics actually influence which modulation vectors are selected. Meanwhile, the auxiliary reward model (the sole language-grounded component) operates entirely separately from the modulation pool. Crucially, the ablation study (Table 2) tests variants of the modulation pool (dictionary frozen, prompt frozen) but *never ablates the auxiliary reward model* — there is no variant that replaces the LLM-generated tips with random text, empty strings, or removes the reward model entirely. Without this ablation, the contribution of the language component is never isolated, and the paper cannot rule out that the performance gains come entirely from the modulation pool architecture rather than from the language grounding.

### Minor

1. **Undefined notation in the ablation study.** The ablation (Section 5.1) uses terms "D frozen" and "α frozen" that are never introduced in the method section. "D" is never defined — it appears to refer to the pool keys (K_pool in Section 3.3) but this is never stated. "α" does not appear anywhere in the method section (Sections 3.1–3.3), making it impossible for the reader to know what "α frozen" actually means or what "prompt optimization" refers to.

2. **No analysis isolating the LLM's role.** The paper does not evaluate whether the specific LLM output matters. An ablation replacing the LLM-generated tips with random strings, empty strings, or hand-crafted rules would isolate whether the LLM's semantic content drives performance or whether the architecture alone (modulation pool + any auxiliary signal) suffices. Without this, the claim that "language inference" is the source of improvement is undersupported.

3. **Tension between "task-agnostic" claim and LLM usage.** The paper claims a "task-agnostic setting" (Sections 1, 3) but the method invokes the LLM at the start of each task to generate content and tips, which requires knowing when a task boundary occurs. The paper acknowledges that task boundaries are hard to obtain in task-agnostic settings (Section 3.1) but does not explain how LLIT detects task boundaries or why the method is task-agnostic rather than task-labeled (the modulation pool retrieves by state similarity, which offers some task-agnostic capability, but the LLM inference step still needs a trigger).

### Trivial

None significant beyond parser artifacts.

## Nice-to-Haves

- Visualizations showing the similarity between task queries and pool keys (e.g., t-SNE of query vectors colored by task), which would directly support the claim that the pool captures task correlations.
- An explicit held-out task experiment withholding ~4 of 20 CW tasks during training and measuring zero-shot or few-shot adaptation.
- Analysis of using different LLMs (or no LLM) to understand sensitivity to the language model choice.
- Discussion of how the auxiliary reward and environment reward are weighted/combined during Decision Transformer training.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Fig.??" reference and table-as-image citations**: These are parser artifacts from PDF extraction; the original submission has proper references. Removed per instructions.
- **Missing related works on language-conditioned RL (SayCan, ELLM, CLIPort) and L2P**: L2P is explicitly cited in Section 3.3 ("Similar to L2P"). The rule prohibits flagging missing citations since external verification is not possible. Removed.
- **"The method is not described with sufficient precision to be understood or reproduced" (as a global dismissal)**: This criticism is folded into the specific, verified gaps above (reward model training, similarity model identity, undefined notation). The dismissive framing is replaced by precise, verifiable omissions.
- **Complaints about tables not showing raw numeric values in nearby paragraphs**: Parser artifact — the table image references cannot display in extracted text. Removed.
- **"The penalty n(k)^{-1} is not motivated"**: The motivation is clear from context (discouraging repeated selection of the same key). Removed.

## Novel Insights

The reviews surface a real tension in the paper that goes beyond its own analysis: the architecture has two independently-motivated components (language-grounded reward model and modulation pool), but the paper never demonstrates that the language signal is causally responsible for the performance gains. The modulation pool alone (modelling after L2P/(IA)³) with state-based queries could plausibly account for the results, and the language reward model might be a secondary contributor or even a distractor. The paper needs an experiment that cleanly disentangles these two sources to validate its core narrative that language *semantics* — not just the modulation pool architecture — drives the improvement. This is a testable hypothesis that the current experiments do not address.

## Suggestions

1. **Specify the reward model training completely**: state the loss function (is it regression toward some target? contrastive? classification?), the data source and collection procedure, the training stage (pre-training before policy learning vs. joint training), and how R_a is combined with the environment reward in the Decision Transformer.
2. **Identify the frozen similarity model** used for tip parsing.
3. **Define "D" and "α" in the method section** and explain what "prompt optimization" entails in Section 3.3.
4. **Run an ablation removing or replacing the language component**: replace LLM tips with random strings, or remove the auxiliary reward model entirely, to isolate the contribution of language.
5. **Either add a held-out task experiment or temper the claims**: if the paper cannot run a zero-shot evaluation, replace "adaptation to unseen tasks" with language about "faster adaptation to sequentially presented tasks."
6. **Explain the task-agnostic claim more carefully**: clarify whether task boundaries are assumed known or detected automatically.

## Score and Decision

**Originality**: 6/10 — combining LLM language with prompt pool for CRL is a novel integration, though individual components (auxiliary reward models, L2P-style prompting) exist separately.  
**Importance of research question**: 7/10 — continual RL with language guidance is timely and well-motivated.  
**Whether claims are well supported**: 4/10 — the central "unseen tasks" claim is not tested; the language contribution is not isolated.  
**Soundness of experiments**: 5/10 — standard benchmarks and baselines, but the method description gap and missing ablation of the language component weaken the experimental narrative.  
**Clarity of writing**: 4/10 — key method details missing, notation undefined in ablation.  
**Value to the research community**: 5/10 — interesting high-level idea that could inspire follow-up work, but the current exposition is too incomplete to build on reliably.

The paper presents an interesting and timely idea with strong preliminary empirical results, but three substantial issues prevent acceptance: (1) a core component (the auxiliary reward model) is critically underspecified, (2) the central claim about "unseen tasks" overreaches what is tested, and (3) the language component's contribution is never isolated by ablation. These require major revisions that go beyond what a rebuttal can address.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>