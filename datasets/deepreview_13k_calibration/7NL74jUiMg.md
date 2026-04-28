# Alchemy: Amplifying Theorem-Proving Capability Through Symbolic Mutation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Formal proofs are challenging to write even for experienced experts. 
Recent progress in Neural Theorem Proving (NTP) shows promise in expediting this process.
However, the formal corpora available on the Internet are limited compared to the general text, posing a significant data scarcity challenge for NTP.   
To address this issue, this work proposes \textit{Alchemy}, a general framework for data synthesis that constructs formal theorems through symbolic mutation. 
Specifically, for each candidate theorem in Mathlib, we identify all invocable theorems that can be used to rewrite or apply to it. 
Subsequently, we mutate the candidate theorem by replacing the corresponding term in the statement with its equivalent form or antecedent. 
As a result, our method increases the number of theorems in Mathlib by an order of magnitude, from 110k to 6M. 
Furthermore, we perform continual pretraining and supervised finetuning on this augmented corpus for large language models.
Experimental results demonstrate the effectiveness of our approach, achieving a 5\% absolute performance improvement on \textit{Leandojo} benchmark.
Additionally, our synthetic data achieve a 2.5\% absolute performance gain on the out-of-distribution miniF2F benchmark.
To provide further insights, we conduct a comprehensive analysis of synthetic data composition and the training paradigm, offering valuable guidance for developing a strong theorem prover.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a symbolic method called Alchemy to augment formal theorem proving data. Specifically, it mutates "the candidate theorem by replacing the corresponding term in the statement with its equivalent form or antecedent", which increases the number of theorem in mathlib4 from 110k to 6M. After continual pre-training and supervised fine-tuning with the generated data, it improves downstream performances (pass rate) on standard theorem proving benchmarks such as mathlib-test and miniF2F from 2.5% to 5%.

### Strengths
Some originality: This is a good and new attempt for augmenting a human-written library (although similar ideas have been applied for "pure symbolic and from scratch" methods for generating theorems such as INT, HTPS-Equations and AlphaGeometry)
Good quality: the paper is well written and all settings are of high relevance
Good clarity: the paper is presented in a clear manner. The experimental setting and results are presented in a standard way and easy to follow
Fair significance: The improvement on pass rate on mathlib-test and miniF2F is consistent, with almost all differences being positive compared with the baseline.

### Weaknesses
1. Poor improvement: although the improvement on pass rate is consistent, it's very limited: ranging from 0.62% to 4.7% on mathlib and only 2.47% on miniF2F (34.01% to 36.48%). This is pretty marginal in terms of improvement. The absolute gains are small, and the relative improvement is not compelling enough to justify the complexity of the approach. The fact that the method only achieves such small gains despite generating a large number of new theorems (6M) suggests that the generated theorems are not of high quality or are not diverse enough to significantly improve the performance of the downstream theorem prover.
2. Narrow application possibility: the approach highly replies on a library of existing equivalence (or implying) theorems and their usage in proofs of other theorems. This limits its applicability to domains where such libraries are readily available. The method is not a general solution for theorem proving but rather a technique that is tightly coupled to the availability of a rich set of existing theorems and their proofs. It is not clear how this method could be applied to other domains where such a library is not available or is not as well-developed.

### Questions
How do you explain a Conversion Ratio of only 37% while the idea seems to work with a theoretical guarantee (i.e. 100%)?
Do you think a framework like Alchemy is the correct way to significantly improve NTP to face challenging problems such as IMO problems?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper concerns data augmentation for neural theorem proving. The authors propose a method for augmenting theorem statements and the set of (state, tactic) examples given a collection of Lean statements and proofs. Their method augments theorem statements by (1) rewriting expressions in hypotheses or the statement's goal using a rewrite tactic with a suitable premise, (2) replacing a hypothesis with a different set obtained with an apply tactic with a suitable premise. It augments proofs by undoing the rewrite and/or apply and introducing a have statement, which sometimes introduces new (state, tactic) examples.

The authors apply their augmentations to Mathlib, and finetune models with (1) continued pretraining on mathlib plus the augmented statements and proofs, followed by (2) finetuning on (state, tactic) examples from Mathlib plus those from their augmentations. 

The models that have undergone continued pretraining and (state, tactic) finetuning outperform the same models when they have only undergone (state, tactic) finetuning on Mathlib alone. For example, there is a 2.69% improvement on the random LeanDojo test split, and a 4.22% improvement on the novel_premises split with DeepSeek Coder.

### Strengths
Originality
- The idea of synthesizing new theorem statements through rewrites and applies is new (as far as I'm aware). 

Quality
- Aside from the concerns discussed below, the experiments were carried out well for several variants while adhering to standard benchmarks and search algorithm protocols.
- Implementing modifications to data extraction in Lean is likely nontrivial.

Clarity
- The data synthesis methodology was explained clearly.

Significance
- Lack of data is widely regarded as a core issue in neural theorem proving. Augmenting data using symbolic techniques is a potential approach to alleviating this issue, and the authors demonstrate a first step in this direction.
- The general direction of augmenting data using symbolic techniques is interesting and under-explored.

### Weaknesses
As mentioned in the strengths above, the general direction of augmenting data using symbolic techniques is interesting and under-explored. I have two primary concerns: (1) the experimental evaluation of the proposed techniques; (2) the data augmentation techniques explored in the current paper. 

### Experimental evaluation
1. **Baselines**: the baseline method is a LM finetuned on (state, tactic) pairs from Mathlib. However, the proposed method does (i) continued pretraining and (ii) (state, tactic) finetuning. As a result it is difficult to interpret the main results, since there are two finetuning methodologies used. How does the baseline method perform after continued pretraining on Mathlib (without augmentation), followed by (state, tactic) finetuning on Mathlib (without augmentation)?

2. **Possible train-test overlap**: The LeanDojo benchmark consists of theorems from Mathlib. Therefore, there is potential train-test overlap in at least two places. 
    - (i) First, the continued pretraining dataset, if it includes theorems from the LeanDojo test set (or premises used in the novel_premises split). How was train-test overlap prevented for continued pretraining? I wasn't able to find details on exactly what was done for continued pretraining, so it would be great to clarify this.
    - (ii) Second, the rewrites and applies may use premises that are "novel" in the novel_premises split. How do you ensure that these are not used in the data augmentation process?

As a result of (i) and (ii), it is difficult to interpret the improvement on the novel premises split. Namely, (i) and (ii) may have exposed the model to the premises required in this split, which would negate the purpose of the split. Moreover, (i) may lead to improvements on the random split as well.

3. **Finetuning hyperparameters**. This is perhaps less important than (1) and (2), but the augmented dataset leads to more gradient updates compared to finetuning on the non-augmented dataset, since finetuning is performed for a fixed number of epochs. Do the results change if the baseline is finetuned for the same number of steps as the model finetuned on the augmented dataset?

### Data augmentation techniques
1. The computational cost is very high; it takes 14 days for the rw operation on 512 CPU nodes. To make the authors' method more practical, it would have been nice to see some innovation that makes the extraction faster (either at the algorithmic level or the implementation level).

2. Currently the methods only modify the statement goal using 1 step of rewriting. The overall scientific contribution could be made stronger with more exploration of techniques (e.g., at least > 1 step of rewriting). Could you clarify why only the 1-step rewriting and apply were explored? I realize that it is hard to say how many techniques are needed (and it's always nicer to have more), so this is less of a concern for me than the experimental evaluation of the two techniques described above.

3. From what I understand, proofs are only modified by introducing a have statement that reverses the 1-step augmentation, and then the proof is the same as the original. Again it would be nice to see additional innovation in this direction.

4. It was unclear why each technique helped on unseen_premises split; could you give an intuition or an analysis of why it might help?

### Questions
Please see the questions above discussed in the Weaknesses. In particular, if the authors can provide a strong response to the questions regarding the experimental setup I would be willing to raise my score.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Alchemy, a framework to generate synthetic theorem data by applying symbolic mutations to existing theorems within Lean’s Mathlib. By mutating known theorems through symbolic operations, Alchemy expands the theorem corpus by an order of magnitude (from 110k to over 6M theorems). The authors evaluate Alchemy’s effectiveness on theorem-proving tasks, reporting a 5% improvement on the Leandojo benchmark and a 2.5% gain on the out-of-distribution miniF2F benchmark (to 36.48% test accuracy).

### Strengths
1. The approach is technically robust, with well-documented use of symbolic mutations (specifically rw and apply tactics) to ensure the correctness of new theorems by construction. The improvements seen on Leandojo and miniF2F benchmarks support the framework’s validity.
2. Alchemy significantly increases the number of available theorems in Mathlib, scaling up to 6 million theorems through systematic symbolic mutations. This large corpus helps address the issue of limited formal proof data for theorem-proving models. By providing a synthetic theorem corpus directly in the symbolic space, Alchemy addresses a key limitation in neural theorem proving, especially in formal languages like Lean where data is scarce and difficult to formalize manually.
3. The limitations of the approach, such as data diversity and computational cost, are clearly addressed.

### Weaknesses
1. Marginal Gains in Benchmark Performance: Despite generating millions of new theorems, the gains in miniF2F accuracy are limited to 2.5%, notably lower than the >60% accuracy achieved by SOTA models such as DeepSeekProver and InternLM Prover. This modest improvement raises questions regarding the utility and quality of the synthetic theorems for real-world theorem-proving tasks. The lack of substantial improvement suggests that the generated theorems, while syntactically correct, may not significantly enhance the model's ability to generalize to more complex, out-of-distribution problems. The mutations might be creating theorems that are too similar to the originals or that do not introduce sufficient novel mathematical concepts.
2. Computational Cost: The process of generating and verifying theorems is highly resource-intensive. The implementation reports substantial computational overhead, with 14 days on 4,096 CPU cores for rw mutations and 7 days on 2,048 cores for apply mutations, potentially limiting the accessibility and scalability of Alchemy in practice. This high computational cost makes it difficult for researchers with limited resources to reproduce or extend the work, and it also raises concerns about the practical applicability of the method for large-scale theorem proving.
3. Lack of Quality Metrics for Synthetic Theorems: Although Alchemy generates a large corpus, there is limited analysis of the quality or mathematical significance of the produced theorems. Without metrics or evaluation methods beyond correctness by construction, it is challenging to assess whether the synthetic theorems provide meaningful, diverse training examples. The absence of such metrics makes it difficult to determine if the generated theorems are truly useful for improving theorem-proving capabilities, or if they are merely redundant variations of existing theorems. It is unclear if the generated theorems are increasing the breadth of the model's understanding or just reinforcing existing knowledge.
4. Limited Innovation Beyond Mutation: The paper relies heavily on mutating existing theorems via basic rw and apply tactics, which may restrict the variety of new insights or concepts that the synthetic data introduces. Advanced tactics (e.g., simp, linarith) and some premise selection approaches are critical in solving more challenging problems, especially in competition-level mathematics. Without these, the generated dataset might lack the depth needed to fully improve theorem-proving performance on complex out-of-distribution tasks.

### Questions
1. Given the modest improvement in miniF2F accuracy, are there metrics or quality checks available to assess the mathematical value or diversity of the generated theorems beyond correctness?
2. Which specific theorems in miniF2F were newly proved by the models fine-tuned with Alchemy data? This would provide insights into the areas where synthetic training data are particularly beneficial.
3. Given the computational demands, are there potential optimizations in the synthesis process to reduce the time and resources required for theorem mutation?	
4. How do you avoid the data contamination problem in the evaluation/generation phase?

[1] Xin, Huajian, et al. "DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search." arXiv preprint arXiv:2408.08152 (2024). 
[2] Ying, Huaiyuan, et al. "Lean Workbook: A large-scale Lean problem set formalized from natural language math problems." arXiv preprint arXiv:2406.03847 (2024).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a new method to synthesize theorem training data for improving LLM's ability in theorem-proving. Given an existing theorem, the proposed method finds theorems that can imply its assumptions and assertions. Then, it replaces the corresponding assumptions/assertions and invokes these theorems to obtain the expanded new theorem. Experiments show the proposed method can generate 5M data and improve 7b models by a 2-4% pass rate.

### Strengths
- The paper is well-written and easy to understand. It has a clear motivation and proposes a novel method to generate a lot of new theorem data.

- The experimental results validate the effectiveness of the generated data. It can improve current LLMs by >4% pass rate on the novel_premises split.

### Weaknesses
The method seems unable to generate diverse theorem data. It mainly expands existing theorem by combining other theorems. The diversity problem may result in a lower improvement on the harder benchmark miniF2F. I guess the generated theorem can be very different from the original theorem if it has a deep variant proof tree. Authors may show the depth statistics of the generated theorem or other statistics to verify the diversity of the generated theorem.

Why many generated theorems not pass the Lean prover? Since the generation process is based on symbolic replacement, I suppose most of the theorem should pass the prover.

### Questions
Why many generated theorems not pass the Lean prover? Since the generation process is based on symbolic replacement, I suppose most of the theorem should pass the prover.

### Soundness
3

### Presentation
3

### Contribution
3
