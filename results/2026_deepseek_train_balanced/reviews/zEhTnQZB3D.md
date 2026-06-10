Now let me produce the final consolidated review.

## Summary

This paper proposes LLIT (Learning with Language Inference and Tips), a continual reinforcement learning method that uses a frozen LLM to generate natural-language task descriptions ("content" and "tips") from observation/action space descriptions. These language outputs are used to (1) train an auxiliary transformer-based reward model that bridges language guidance to the observation space, and (2) populate a modulation pool (prompt pool) with learned keys and modulation vectors that enable selective parameter sharing across tasks via a Decision Transformer backbone. An inverse-selection-count routing mechanism discourages unrelated tasks from sharing the same key. Experiments on Continual World (CW10, CW20) show LLIT outperforming a range of continual RL baselines as well as multi-task learning (MTL/MTL+PopArt) on both average performance and generalization metrics.

## Strengths

- **Strong empirical results on Continual World benchmarks, including outperforming multi-task learning baselines.** Table 1 reports that LLIT outperforms all regularization-based, structure-based, rehearsal-based methods, and crucially also the multi-task learning baselines (MTL, MTL+PopArt) on CW20. Since multi-task learning is often considered a soft upper bound for continual learning, this provides meaningful evidence that the method delivers on its core claim of a favorable plasticity-stability trade-off.

- **Systematic ablation isolating the contribution of each component.** Table 2 tests four variants ("D frozen," "α frozen," "both frozen," "lazily update D") against the full method. The "both frozen" variant shows noticeable degradation, and "D frozen" degrades on both metrics. This provides granular evidence that both the learnable dictionary (keys) and the prompt optimization contribute to the reported results.

- **Inverse-selection-count routing in the modulation pool (Eq. 5, lines 98–102).** The paper introduces an $n(k)^{-1}$ term in the key-retrieval cosine-similarity computation that penalizes queries from different tasks attending to the same key. This goes beyond standard L2P and provides a concrete mechanism for reducing harmful cross-task interference while still enabling related tasks to share modulation vectors.

## Weaknesses

### Fatal

None.

### Major

- **Results on mixed task sequences are claimed but never shown.** Section 4.1 (line 120) describes constructing "mixed control task sequences" from Classical Control, Mujoco Control, and Continual World environments. Section 5.1 (line 160) states the evaluation is "on mixed task sequence and CW benchmarks." However, Table 1 only reports results on Continual World (CW10, CW20). No results for the mixed sequences or the individual Classical Control / Mujoco Control environments are presented anywhere in the paper. This is a significant gap between what is claimed and what is evidenced.

- **The training of the auxiliary reward model is critically underspecified.** This model is the central bridge between language guidance and policy optimization (Section 3.2), yet its training procedure is never described. The paper states that "the concatenated embedding will be the input to train a transformer model" (line 75) and gives an equation $R_a = f_{ARM}([e_{tip}; e_o])$ (line 78), but never specifies: (a) what loss function or training signal is used, (b) what data it is trained on and how that data is stored/collected, or (c) how the model produces a scalar reward from the concatenated embeddings. This makes it impossible to understand or reproduce a core component of the method.

- **The LLM, similarity model, and tokenizer are never identified.** The paper refers to "a frozen and pre-trained LLM" (line 20), "a frozen similarity model" (line 73), and "a pre-trained tokenizer" (line 75) without naming any of them. The prompt templates (Eq. 2, lines 61–67) are said to be "carefully designed" but are not shown. For a method whose core novelty depends on LLM-generated language guidance, the omission of these specifications is a significant reproducibility concern. Coupled with the underspecified reward model training, the contribution cannot be assessed independently.

### Minor

- **Terminological confusion between the method section and the ablation study.** The ablation (line 168) refers to "dictionary D" and "prompt optimization α" which are never introduced in the method section (Section 3). Section 3.3 describes a "modulation pool" with keys $K_{pool}$ and modulation vectors, but the relationship between "dictionary D" and the modulation pool is left entirely implicit. The ablation also claims "prompt optimization proposed in Sec. 3.3," but Section 3.3 does not describe any optimization of prompts — it describes key-query matching with cosine similarity. This makes the ablation difficult to interpret.

- **Overclaim on "adaptation to unseen tasks."** The abstract (line 5) and conclusion (line 177) claim the method achieves "adaptation to unseen tasks," but this is not directly evaluated. The "Generalization" metric (line 148) measures the average number of steps needed to reach a success threshold on *each task as it is learned* — this measures learning speed, not zero-shot transfer to held-out task sequences or genuinely unseen tasks. No experiment evaluates performance on tasks not encountered during training.

- **Inconsistency regarding experience replay.** The paper claims LLIT operates "without any experience replay" (line 177) and "without the replay buffer" (line 20). However, the auxiliary reward model must be trained on interaction trajectories (Section 3.2). The paper never explains how these trajectories are obtained, stored, or used for training without violating the "no replay" claim.

- **CoTASP mentioned but not introduced.** Line 166 references CoTASP as a method LLIT outperforms, yet CoTASP is not listed among the baselines (Section 4.2) and no citation is provided. The reader cannot determine what CoTASP is or how the comparison was conducted.

- **Unsubstantiated claim about sparse coding.** Line 41 (related work) states "By contrast, LLIT generates masks by highly efficient sparse coding (solving a relatively small lasso problem)," but the method section contains no sparse coding or lasso optimization. The sparsity parameter $\lambda$ is mentioned only in the experiments (line 170) with no description of how it mechanically induces sparsity in the network.

### Trivial

None.

## Nice-to-Haves

- Ablation removing the LLM entirely (e.g., using random or hand-designed tips instead of LLM-generated ones) would directly establish whether the LLM is necessary for the reported results — this is the most important missing control experiment for the paper's core claim.
- Analysis of the claimed interpretability (abstract, line line 5 in PDF): the paper claims an "interpretable policy" but provides no analysis of what the learned policies represent or how language guidance translates to behavior.
- A limitations section acknowledging the reliance on human-provided observation/action dimension descriptions and the computational cost of LLM inference would improve the paper.

## Removed Points

The following points raised by the reviewers were removed for the stated reasons:

- **Criticism about the paper being irreproducible because the LLM/similarity model/tokenizer are not named, framed as a "fatal" flaw.** While this omission is significant (and retained as a Major weakness above), calling it fatal overstates the case. The modular architecture could be instantiated with various LLMs; the core contribution (reward model + modulation pool) does not collapse if the LLM name were provided. Demoted to Major.
- **Criticism about missing hyperparameters and training details.** These could reside in the appendix (stripped by the parser). Per the rules, criticisms about missing appendix content are removed. The more severe issue is that the *training procedure* for the auxiliary reward model is underspecified even in the main text — this is retained in Major.
- **Criticism about missing LLM-based RL baselines (Eureka, Text2Reward, etc.).** These address reward design for single-task RL, not continual RL. Criticizing their absence is scope creep; the paper's stated scope is continual RL.
- **Formatting/style nitpicks** (grammar, dangling references like "Fig.??", "outperforms overall performance most baselines") — per instructions, these are removed as parser artifacts.
- **Generic area-of-concern sweeps** (e.g., "could the metric be measuring a proxy?" without a specific anchor in the paper) — removed.
- **Several strengths from the Strength Finder** that were generic or superficial (e.g., "the paper addresses an important problem," "the problem is well-motivated") — removed. The retained strengths are concrete, specific, and verified against the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews surface well-known tensions (reproducibility vs. novelty, claim scope vs. experimental scope) but do not introduce observations that meaningfully extend the paper's own analysis.

## Suggestions

1. **Show the mixed task sequence results** or remove the claim. This is the single most impactful fix — the paper explicitly states it evaluates on mixed sequences but provides no data.
2. **Specify every component fully:** name the LLM, similarity model, and tokenizer; show the prompt templates in full. State the loss function and training procedure for the auxiliary reward model.
3. **Resolve the terminological inconsistency** between the method section (modulation pool, keys $K_{pool}$, modulation vectors) and the ablation (dictionary D, prompt optimization α). Make the mapping explicit.
4. **Add an ablation without the LLM** (e.g., random tips or hand-crafted tips) to directly establish the value of LLM-generated language guidance.
5. **Temper the "unseen tasks" language** or add a held-out task evaluation to support it.
6. **Clarify the replay buffer question:** does the auxiliary reward model training require storing trajectories or not? If it does, revise the "without any experience replay" claim.

## Score and Decision

The paper presents a plausible architecture and strong results on Continual World, with a useful ablation study and a novel inverse-selection-count routing mechanism. However, the experimental evidence is significantly narrower than claimed: the mixed task sequence results are promised but never shown, and the generalization/adaptation claims overreach. The method description has critical gaps — the auxiliary reward model's training procedure is unspecified, and the LLM, similarity model, and tokenizer are not identified — that prevent independent assessment. The terminological confusion between the method section and ablation further undermines clarity. For a top conference, these issues are too substantial for acceptance in the current form.

**Score:** 4.0 / 10  
**Decision:** Reject

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>