## Summary
DTERM proposes a framework for dynamically weighting multiple reward components (compilation success, test case passing, code similarity, style adherence, computational efficiency) in RL for code generation tasks. A transformer-based task embedding is fed into a "hypernetwork" that generates task-conditioned scalar weights, augmented by FiLM modulation and cross-attention over learned reward prototypes for zero-shot generalization. The framework is evaluated on CodeXGLUE, APPS, DeepFix, and HumanEval benchmarks.

---

## Strengths

- **Modular reward decomposition with learned weighting:** Equations 5–6 implement a trainable softmax over task-conditioned linear projections of sub-reward weights. The ablation (Table 2) shows a 4.6 Pass@1 drop when this mechanism is removed (22.7 → 18.1), concretely demonstrating that dynamic weight generation contributes to performance.
- **FiLM-based task-conditioned reward specialization:** Equation 7 applies FiLM modulation per sub-reward network, and Table 2 shows removing it reduces performance by 1.9 Pass@1 points (22.7 → 20.8), confirming it is an independently useful component.
- **Compiler-aware reward integration:** Equation 11 encodes compiler error counts as an exponentially decaying reward signal. Table 2 confirms it contributes: removing compiler feedback reduces Pass@1 by 1.6 points.
- **Broad multi-benchmark evaluation:** Table 1 shows consistent improvements over three static baselines (Uniform, Expert-Tuned, GradNorm) on five task types, which supports the paper's claim of general applicability over narrow task-specific tuning.

---

## Weaknesses

### Fatal

- **Conclusion contains text from a completely different paper.** Section 6 opens with: *"The Dual Selfular-Acting Machine (DSAM.Mouth Rachel) A new method for analyzing the dual selfular acting machine (DSAM), a generative text model architecture akin to one employed by ChatGPT."* This is not about DTERM at all; it appears to be text from another submission pasted in by mistake. The actual DTERM conclusion is one sentence. Section 7 then discloses: *"We use LLM polish writing based on our original paper"* — further corroborated by artifacts throughout: *"Bat var 'Learning from choice of model (RLHF)"* (Section 4.6), *"The Word xog **e** is a resulting embedding"* (Section 3.4), and two explicit placeholder citations written as *"(?)"* in Sections 2.3 and 2.5. This is a serious integrity issue independent of technical merit: the manuscript was not checked before submission, and key bibliographic content is absent or corrupted.

- **The core technical claim ("hypernetwork") does not match the implemented mechanism.** Section 3.3 correctly defines hypernetworks per Ha et al. (2016): a network that *generates the parameters of another network*. Equation 5, however, is a softmax over learned linear projections of the task embedding: `α_i = exp(w_i^T e_t + b_i) / Σ_j exp(...)`. This generates *scalar weights over reward components*, not network parameters for a main network. Sections 3.3, 4.1, and the abstract are all built on the hypernetwork framing, so the causal story — that "the hypernetwork learns to interpolate between weighting schemes" — rests on a mislabeled mechanism. Equation 9 adds prototype cross-attention (more substantive), but this still does not constitute a hypernetwork in the Ha et al. sense. Mislabeling the core mechanism is not a presentation error; it affects the paper's novelty claims.

### Major

- **Figure 2's zero-shot generalization evidence is unverifiable.** The ten "unseen tasks" in Figure 2 are never identified — they are labeled only "Task 1" through "Task 10" with no description of what they are. The y-axis metric "normalized reward values" is undefined: it is not stated whether values are normalized per-task, per-method, or against a common floor/ceiling. Since DTERM's five sub-reward components measure quantities with different scales and semantics, aggregation into a single number without explanation renders the figure uninterpretable. This matters because the generalization result is the *only* direct evidence for Contribution 3 (zero-shot adaptation), and it is entirely opaque.

- **Figure 3 reward compositions contradict the paper's central thesis of task-aware specialization.** For "problems" (competitive programming, where functional correctness is paramount), the learned weight for *test case passing rate* is 0.08 — the lowest of all components, below compilation success (0.10), code similarity (0.25), and style adherence (0.22). For "repair" tasks (where fixing compilation errors is the primary objective), *computational efficiency* receives the largest weight (0.28) while compilation success receives only 0.22 and test case passing rate 0.10. These weights are nearly uniform across tasks and do not reflect task-relevant priorities. The paper describes Figure 3 as demonstrating "the hypernetwork's dynamic adjustment capability," but the data shows no such meaningful specialization.

- **Critical ablation inconsistency in Table 2.** "w/o Hypernetwork" scores 18.1 Pass@1, while "w/o Task Embedding" scores 19.3. Since the hypernetwork's primary function is to *consume the task embedding* to generate context-aware weights, removing the entire hypernetwork (which includes the task embedding pipeline) should not outperform merely removing the task embedding. This inconsistency is unexplained and casts doubt on whether the ablation conditions are properly controlled.

- **Meta-training setup is entirely absent.** Section 4.3 states that prototype vectors are "learned during meta-training on many different types of tasks," but neither the meta-training corpus nor the split from test benchmarks is ever specified. Without this, it is impossible to assess whether the generalization gains in Figure 2 are genuine or artifacts of overlap between meta-training and evaluation tasks.

### Minor

- **BLEU-4 is used as the sole metric for code translation and summarization.** BLEU is a surface-level n-gram metric and is known to correlate poorly with functional correctness for code. The paper uses execution-based metrics (Pass@1, Fix Rate, Exact Match) for other tasks but reverts to BLEU for translation (where functional correctness is also evaluable via execution). This weakens the evaluation for those two tasks.

- **No variance reported despite using 3 seeds.** Section 5.1 states "each experiment runs on... 3 random seeds," but Table 1 and Table 2 report only point estimates. Given that improvements such as +12.7 BLEU on translation may or may not be statistically significant, reporting standard deviations from the three seeds is expected.

- **The policy model's identity is not specified.** Section 5.1 states that "CodeBERT embeddings are used" and "we train using PPO," but does not specify what the policy model is — whether it is CodeBERT, a generative LLM, or another architecture. This omission makes the experimental setup underspecified.

- **Baseline selection does not include execution-based RL methods.** For a 2026 submission comparing reward modeling for code generation, the absence of any execution-based RL baselines (e.g., CodeRL, which the paper itself cites) means the gains in Table 1 are measured only against static reward weighting strategies, not against the broader field.

### Trivial

*(None beyond formatting artifacts already addressed under Fatal.)*

---

## Nice-to-Haves

- If Figure 3 is to serve as the paper's core interpretability result, it should compare learned weights against expert-defined "oracle" weights (e.g., for HumanEval, test pass rate should dominate; for DeepFix, compilation success should dominate) and discuss cases where the learned weights agree or disagree with expert intuition. This would either validate the method or generate an interesting finding that challenges the intuition.
- Fully describing the 10 unseen tasks in Figure 2 and defining the normalization scheme would turn an opaque figure into genuinely meaningful evidence.
- Replacing or supplementing BLEU on code translation with execution-based metrics (e.g., CodeBLEU or functional test pass rates) would strengthen the evaluation of that benchmark.

---

## Removed Points

*These points are flagged for removal — treat them with caution.*

- **"Reward Machine" title is misleading (Harsh Critic, Section 3.5):** The paper itself explicitly states *"While our approach differs in implementation, we take the insight from modular reward decomposition"* (Section 3.5). This is a clear authorial acknowledgment. The use of the term as a loose analogy is not ideal, but the paper does not claim otherwise. REMOVED as a strawman.

- **Missing comparison with CodeRL baselines as unfair (Harsh Critic, Section 5.1 framing):** The paper compares reward weighting strategies on equal footing (Uniform, Expert-Tuned, GradNorm all use the same sub-reward components). CodeRL is a policy-level method using a different setup, and including it would not isolate the reward weighting contribution. WEAKENED from fatal to a nice-to-have observation.

- **Strength Finder — "Task-adaptive reward composition visualization" (Figure 3 as a strength):** Directly contradicted by the verified weakness: the weights in Figure 3 do not show meaningful task specialization. REMOVED as a strength.

- **Strength Finder — "Zero-shot adaptation via cross-task prototypes" as a clean strength:** Figure 2 does show DTERM outperforms baselines, but since the tasks are unlabeled and the metric is undefined, this cannot be verified as a clean strength. DOWNGRADED — the approach is potentially interesting, but the evidence is not credible as written.

- **Harsh Critic's request for confidence intervals as a standard practice concern:** Single-run or low-replicate reporting is common in code generation benchmarks. However, since the authors explicitly ran 3 seeds and chose not to report variance, this is kept as a Minor rather than removed.

---

## Novel Insights

None beyond the paper's own contributions. The idea of conditioning reward weights on task embeddings is conceptually reasonable, and the prototype-based cross-attention for zero-shot generalization (Section 4.3) is the most technically substantive component. However, the core mechanism is mislabeled, the evidence for the main claims is either unverifiable or counter-productive, and the manuscript integrity issues mean no novel insight can be reliably attributed to this submission.

---

## Suggestions

1. **Fix the conclusion immediately.** Remove the DSAM text and write a proper DTERM conclusion. Remove all LLM artifacts and placeholder citations "(?)".
2. **Rename the mechanism accurately.** Equation 5 is a task-conditioned softmax attention over reward weights, not a hypernetwork. Either implement a true hypernetwork (where network parameters, not just scalar weights, are generated) or relabel the contribution accurately.
3. **Describe the 10 unseen tasks in Figure 2.** Define what "normalized reward value" means operationally.
4. **Explain the ablation inconsistency** in Table 2 between "w/o Hypernetwork" and "w/o Task Embedding."
5. **Specify the meta-training corpus** and confirm no overlap with evaluation benchmarks.
6. **Report standard deviations** from the 3 seeds in Tables 1 and 2.
7. **Confront Figure 3 directly.** If the learned weights are approximately uniform, explain why that is — either it is a finding that undermines the specialization claim, or there is a reason uniform-ish weights still outperform fixed baselines that should be articulated.

---

## Score and Decision

**Originality:** The idea of task-conditioned reward weighting is reasonable and modestly novel, but the "hypernetwork" framing is technically inaccurate. Rating: 2/5
**Importance of research question:** Dynamic reward modeling for code generation is a valid and practically relevant problem. Rating: 3/5
**Claims well-supported:** The ablation gives modest support for individual components, but the central generalization claim (Figure 2) is unverifiable, and Figure 3 actively contradicts the specialization claim. Rating: 1/5
**Soundness of experiments:** The ablation has an internal inconsistency, the base model is unspecified, meta-training is undescribed, and variance is not reported. Rating: 1/5
**Clarity of writing:** The manuscript contains text from a different paper in the conclusion, LLM artifacts, and missing citations. The writing quality is not acceptable for publication. Rating: 1/5
**Value to the research community:** The idea has potential value if properly executed, but this submission does not deliver it in a verifiable or trustworthy form. Rating: 1/5

The paper's FUNDAMENTAL ISSUES — a conclusion copied from another paper, a mischaracterized core mechanism, unverifiable generalization evidence, and an internally inconsistent ablation — are all directly verifiable from the paper as written. These collectively render the submission not scientifically valid in its current form.

MY FINAL SCORE: <score>1.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>2</originality>
<importance>3</importance>
<claims_supported>1</claims_supported>
<soundness>1</soundness>
<clarity>1</clarity>
<community_value>1</community_value>
</subscores>