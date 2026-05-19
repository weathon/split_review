- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6
Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me compose the final review.

## Summary

This paper introduces 260 legal text classification tasks derived from the U.S. Supreme Court Database and Court of Appeals Database — nearly all new to the ML community — and conducts a comprehensive empirical study comparing zero-shot prompting (GPT-4, Llama 3, Mistral, etc.) against fine-tuned models. The central finding is that a single fine-tuned Llama 3 8B model ("Lawma 8B") outperforms zero-shot GPT-4 by 17.3 percentage points on average, and that strong performance can be achieved with as few as 250 labeled examples. The paper additionally studies scaling behavior, sample efficiency, multi-task vs. single-task specialization, cross-database generalization, and intercoder agreement contextualization.

## Strengths

- **Fine-tuned open-source model dramatically outperforms GPT-4 zero-shot.** Lawma 8B achieves 82.4% accuracy (Supreme Court) and 79.9% (Appeals Court) compared to GPT-4's 59.78% and 63.42%, respectively (Table 1, Figure 2). Lawma 8B outperforms GPT-4 on ~95% of all 260 tasks (Figure 1). This directly challenges the common assumption that prompting commercial models is the best available approach for legal classification.

- **Sample efficiency is demonstrated convincingly.** Fine-tuning Llama 3 8B on just 250 examples matches or beats GPT-4 zero-shot on 8 out of 10 highlighted tasks, and 50 examples suffice for 6 of 10 tasks (Figure 6). This is practically important because labeling a few hundred documents is typically financially feasible for legal scholars.

- **Single multi-task model matches specialized per-task models.** A single Lawma 8B model fine-tuned on all 260 tasks simultaneously performs within small single-digit accuracy of separately specialized models (Figure 8). This obviates the need to train and maintain 260 separate models.

- **Fine-tuning generalizes to unseen databases.** Training only on Court of Appeals tasks improves accuracy on Supreme Court tasks by 18.8 percentage points over the base model (Figure 9), demonstrating cross-task transfer beyond the training distribution.

- **Systematic intercoder agreement analysis provides meaningful context.** Table 3 shows Lawma 8B's adjusted accuracy is within single-digit points of human agreement on several tasks (e.g., GENISS: 93.2% vs. 97.6%), and matches the agreement rate on COMMENT (100% vs. 100%). This contextualizes model performance against a natural upper bound.

- **Scaling analysis reveals diminishing returns.** Mean task accuracy on Appeals Court tasks improves only 8.5 points when scaling from Pythia 1B to Llama 3 70B (a 3000× increase in pretraining compute), suggesting future gains will likely come from data quality/diversity rather than model scale alone (Figure 5).

- **Few-shot prompting does not improve GPT-4.** Three-shot evaluation with the 32K-token version yields 58.38% accuracy, lower than zero-shot 62.89% (Table 1). This rebuts the assumption that adding examples helps commercial models on these legal tasks.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The headline accuracy numbers are reported on an artificially balanced (subsampled) test distribution without upfront clarification.** The paper subsamples the majority class in each task so that no class has more examples than all others combined (line 97), and this subsampling is applied to the test set as well. The absolute numbers (82.4%, 79.9%) reflect this modified distribution rather than the natural class distribution a practitioner would encounter. While all comparisons (Lawma vs. GPT-4, etc.) are evaluated on the same distribution — so the relative improvements are valid — the paper should more transparently flag this when presenting headline numbers and also note it as a limitation (the current Limitations subsection does not mention subsampling). The paper already has the machinery to report natural-distribution accuracy (it does so for 9 tasks in Table 3), so extending this to all tasks would resolve the concern.

- **No fine-tuning comparison with another modern instruction-tuned open-source model.** The paper's main experiment fine-tunes only Llama 3 (8B and 70B). The scaling analysis does include fine-tuned Pythia models and Llama 2 7B, showing that better base models yield better fine-tuned performance. However, a direct comparison with a fine-tuned Mistral 7B (or similar) would more clearly demonstrate that the benefit of fine-tuning — the paper's central thesis — generalizes beyond the Llama 3 family. Without this, the claim that "fine-tuned open-source models" are the solution is somewhat tied to the specific model chosen.

- **Computational cost of fine-tuning is not reported.** The paper describes the fine-tuning as "lightweight" but does not report GPU hours, hardware specifications, or monetary cost. This information is directly relevant to practitioners evaluating whether the approach is practical for their setting, especially legal scholars without access to large compute budgets.

### Trivial

- The paper does not report the number of unique case opinions (as opposed to task examples), which would help the reader understand data leakage and overlap across tasks.
- A per-task accuracy table for all 260 tasks would be valuable (the paper references a task list section likely in the appendix, but only 10 tasks are analyzed in detail in the main text).

## Nice-to-Haves

- Report natural-distribution accuracy for all tasks alongside the balanced accuracy (the machinery already exists, as demonstrated by the adjusted accuracy computation in Table 3).
- Provide a brief qualitative analysis of tasks where model accuracy is far below intercoder agreement, checking whether the majority opinion text contains sufficient information to determine the label. This would address potential construct validity concerns.
- Analyze which specific Supreme Court tasks benefit most from cross-database training on Court of Appeals data.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Construct validity concern** (Harsh Critic Critical Issue 3): The reviewer questions whether all labels are inferable from majority opinions alone, speculating about specific variables. This is speculative — no evidence from the paper supports the claim that any task is impossible from the given input. The paper already provides intercoder agreement analysis (Table 3) that contextualizes performance against human disagreement rates. **Reason for removal:** Speculative, no concrete evidence in the paper.

- **Epoch asymmetry between Lawma 8B and 70B**: The reviewer questions the comparison because 8B was trained for 3 epochs and 70B for 1 epoch. The paper explicitly addresses this (line 210): "We find that by training the 8B model on more epochs than the 70B model, it attains a similar loss as the 70B model. Further training either model results in overfitting." **Reason for removal:** Already addressed by the paper.

- **Few-shot prompting criticism used as a strength**: The Strength Finder's point #2 about few-shot not helping GPT-4 is valid but the Harsh Critic also raises this as a finding. No conflict; both are accurate.

- **Generic "the problem is important" strength from Strength Finder**: Not present — all strengths listed by the Strength Finder are concrete and evidence-backed. All are retained.

## Novel Insights

The most interesting cross-perspective insight is that what the Harsh Critic treats as a "critical issue" (subsampled test distribution) is actually a standard methodological choice for imbalanced classification benchmarks, and the paper is transparent about it. The reviewer's demand for natural-distribution accuracy is reasonable but its framing as an "evidential issue" overstates the problem because every comparative finding in the paper — the 17.3-point gap, the 95% task-level superiority — is measured on the identical distribution and thus unaffected. The real issue is purely about the absolute-interpretability of headline numbers for practitioners. Conversely, the Harsh Critic's criticism about missing a fine-tuned Mistral comparison is genuinely insightful because the paper's practical recommendation ("researchers are better off using a fine-tuned open-source model") implicitly generalizes beyond Llama 3, and the scaling analysis, while helpful, doesn't fully substitute for a direct head-to-head fine-tuning comparison of two similarly-sized modern models.

## Suggestions

1. Add a row or column reporting accuracy on the original (unsubsampled) distribution for all 260 tasks, alongside the balanced-test-set accuracy. The adjustment method used for the 9-intercoder tasks already demonstrates this is feasible.
2. Fine-tune at least one additional instruction-tuned model (e.g., Mistral 7B Instruct) on the same tasks and report results vs. Lawma 8B. This would directly test whether the benefit of fine-tuning generalizes beyond Llama 3.
3. Report GPU hours and approximate cost for the main fine-tuning experiments, to help practitioners assess feasibility.
4. Add the subsampling of the test set as an explicit caveat in the Limitations subsection.
5. Include a brief table or figure showing per-task accuracy for all 260 tasks (even in the appendix) to increase the benchmark's utility.
