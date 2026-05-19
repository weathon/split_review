Now I have all the information I need. Let me compose the consolidated review.

## Summary

This paper proposes SIRLC (Self-Improvement by Reinforcement Learning Contemplation), an unsupervised method that uses an LLM's own self-evaluation as a reward signal for PPO-based fine-tuning. The LLM acts as both student (generating answers to unlabeled questions) and teacher (evaluating its own outputs via correctness/quality prompting), and is updated via RL to maximize self-evaluation scores. Experiments on BigBench reasoning tasks, IWSLT 2017 translation, and CNN/Daily Mail summarization show improvements over unsupervised baselines.

## Strengths

1. **Empirical demonstration that evaluation is easier than generation** — Section 4.1 (Fig. 1) systematically shows across FLAN-T5 model sizes (80M–780M) that self-evaluation accuracy exceeds text generation accuracy on CommonGen, with a 15% gap for smaller models. This evidence directly supports the paper's central premise and motivates the approach.

2. **SIRLC outperforms unsupervised baselines (SC and LMSI) on reasoning** — Table 3 shows SIRLC achieves higher accuracy than Self-Consistency and LMSI on 9 of 12 BigBench tasks. Since SC and LMSI both use Chain-of-Thought prompting (making them fair comparisons), this provides genuine evidence that RL with self-evaluation rewards improves reasoning beyond existing unsupervised methods.

3. **Consistent improvement across model scales** — Figure 5 (fig:bbh_different_model) shows SIRLC improves FLAN-T5-Small (80M), Base (250M), and Large (780M) on three BigBench tasks, with larger relative gains for the smallest model. This demonstrates the method is not limited to a specific model size.

4. **Applicability to both reasoning and text generation** — The method is evaluated on multiple task families (multi-step reasoning, machine translation, summarization), showing improvements on IWSLT 2017 (BERTScore 0.818→0.86) and CNN/Daily Mail (BERTScore 0.886→0.899) in addition to reasoning benchmarks.

## Weaknesses

### Major

- **DG baseline comparison is confounded by prompting strategy** — The paper reports a headline "5.6% higher average accuracy than DG" on BigBench tasks. However, SIRLC explicitly uses Chain-of-Thought prompts for reasoning problems (Section 5, "For reasoning problems, we use the Chain-of-Thought (CoT) prompt"), while DG is described only as "directly generating the answer using the deterministic output of the LLM" with no mention of CoT. If DG does not use CoT while SIRLC does, the observed improvement could partly or entirely reflect the prompting strategy rather than the RL training. The comparison against SC and LMSI (both CoT-based) is fairer and still favorable to SIRLC, but the headline claim against DG is uninterpretable without clarification. The authors should specify whether DG also uses CoT or remove the comparison as a primary result.

### Minor

- **Missing PPO hyperparameters** — The implementation details (Section 6.1) report 6,000 gradient steps, batch size 12, and FLAN-T5-Large, but omit standard PPO hyperparameters: learning rate and schedule, clipping parameter ε, KL divergence coefficient, entropy regularization coefficient, discount factor γ, and reward normalization details. These are essential for reproducibility and for meaningful comparison with future work.

- **Translation/summarization results reported only via BERTScore** — Figure 4 (fig:training_on_trans_sum) reports only BERTScore for the main translation and summarization results, despite the paper's own correlation analysis (Table 1) using BLEU and ROUGE alongside BERTScore. Reporting all three metrics consistently would provide a more complete picture and rule out the possibility that BERTScore gains reflect quirks of a single evaluation model.

- **No error bars in the main results table** — Table 3 reports results "averaged over three random trials" (Section 6.1) but does not include standard deviations or significance tests. Training curves in Figure 4 show shaded std. dev. for only 3 of 12 tasks. Without variance estimates, it is impossible to assess whether small improvements (e.g., +0.2% on "Reasoning about Colored Objects") are meaningful.

- **Correlation between self-evaluation and standard metrics is weak** — Table 1 reports correlation coefficients of only 0.16–0.29 between self-evaluation and BLEU/ROUGE/BERTScore. While positive, these are weak correlations. The paper frames this as evidence that self-evaluation is "a reliable way to measure the quality of the generated text" — this overstates what the data supports. The authors should acknowledge the weakness of this signal and discuss its implications.

- **Novelty claim is overstated** — The paper states it is "the first study that formally verifies the self-evaluation capability of LLMs" (Section 1). The related work section itself discusses prior self-evaluation approaches (self-verification, re-prompting, self-consistency, generate-&-rank) that implicitly or explicitly rely on LLM self-evaluation. The claim of being "first" should be scoped more carefully or removed.

- **Generalization results are modest** — Table 4 shows an average improvement of 0.8% across 5 unseen tasks, with declines on 2 of 5 tasks (Sports Understanding: −0.4%, Tracking Shuffled Objects (5): −0.1%). The paper's claim that the method "generalizes well to new and unseen datasets" overstates what a 0.8% average gain with multiple declines supports.

### Trivial

None.

## Nice-to-Haves

- Provide the exact text of CEP and QEP prompts (the paper gives the template but exact wording matters for reproducibility).
- Validate self-evaluation accuracy on reasoning tasks directly — e.g., compare the frozen evaluator's judgments against ground-truth labels on a held-out set — rather than relying only on correlation with metrics on summarization/translation.
- Report training time and GPU hours for practical reference.

## Removed Points

- **"LMSI baseline numbers seem unusually low"** — The reviewer speculates about implementation fidelity (e.g., "LMSI should typically outperform DG, not underperform it by 20%"). This is speculation that cannot be verified from the paper as written; the reported numbers are what they are.
- **"RLFT is an upper bound, not a competitor; framing is misleading"** — The paper's framing ("catches up with the performance of RLFT") is factually accurate and acknowledges that RLFT uses oracle rewards. No misrepresentation.
- **"SE accuracy is affected by quality of generated text"** — The paper already acknowledges this limitation in the text ("it is essential to note that the evaluation accuracy is affected by the quality of the generated text").
- **"Missing related work" about specific papers** — Per policy, I do not flag missing citations.
- **Formatting/style nitpicks and section-by-section opinion notes** — Removed as noise or not substantive.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's actual content and do not surface a hidden strength or fatal flaw that the authors themselves miss. The DG prompting confound is the most substantial issue raised and is clearly a question the authors should have anticipated and addressed.

## Suggestions

1. Clarify whether DG uses CoT prompting or not. If it does not, either (a) re-run DG with CoT, or (b) remove DG from the headline comparisons and pivot to SC/LMSI as the primary baselines, or (c) explicitly report both (DG w/ CoT and w/o CoT) and discuss the difference.
2. Include standard deviations or confidence intervals for all entries in Table 3.
3. Report BLEU and ROUGE alongside BERTScore for the translation and summarization main results, or explain why they are omitted.
4. Disclose all PPO hyperparameters (learning rate, clip range, KL coefficient, entropy coefficient, discount factor, reward normalization).
5. Tone down the "first study" claim and the characterization of the correlation results (0.16–0.29 is weak, not strong validation).
6. Acknowledge more directly the modest generalization results rather than claiming the model "generalizes well."

## Score and Decision

**Originality**: The idea of using self-evaluation as a reward for RL-based LLM fine-tuning is reasonably novel, though it builds on a recognizably active line of work.  
**Importance of research question**: Reducing dependence on labeled data is a high-value goal. The question is important.  
**Claims supported**: Partially. The core claim (SIRLC improves over unsupervised baselines) is supported against SC and LMSI, but the headline DG comparison is confounded, and several claims outrun the evidence.  
**Soundness of experiments**: Adequate breadth (3 task families, model size variation, generalization tests) but weakened by missing hyperparameters, incomplete metrics, and absent error bars.  
**Clarity of writing**: Generally clear. The method and motivation are well explained.  
**Value to community**: Moderate. If the evaluation issues are resolved, the method is simple and the premise (evaluation is easier than generation) is broadly useful.

The paper has a clean conceptual premise and shows genuine improvements over CoT-using baselines (SC, LMSI). However, the confounded DG comparison undercuts the headline result, and multiple evaluation gaps (missing hyperparameters, incomplete metrics, no variance estimates) weaken the experimental contribution. These issues are fixable but non-trivial.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>