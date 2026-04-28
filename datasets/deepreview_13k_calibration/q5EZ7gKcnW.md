# Iterative Label Refinement Matters More than Preference Optimization under Weak Supervision

- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 5, 8, 8

## Abstract
Language model (LM) post-training relies on two stages of human supervision: task demonstrations for supervised finetuning (SFT), followed by preference comparisons for reinforcement learning from human feedback (RLHF). As LMs become more capable, the tasks they are given become harder to supervise. Will post-training remain effective under unreliable supervision? To test this, we simulate unreliable demonstrations and comparison feedback using small LMs and time-constrained humans. We find that in the presence of unreliable supervision, SFT still retains some effectiveness, but DPO (a common RLHF algorithm) fails to improve the model beyond SFT. To address this, we propose *iterative label refinement* (ILR) as an alternative to RLHF. ILR improves the SFT data by using comparison feedback to decide whether human demonstrations should be replaced by model-generated alternatives, then retrains the model via SFT on the updated data. SFT+ILR outperforms SFT+DPO on several tasks with unreliable supervision (math, coding, and safe instruction-following). Our findings suggest that as LMs are used for complex tasks where human supervision is unreliable, RLHF may no longer be the best use of human comparison feedback; instead, it is better to direct feedback towards improving the training *data* rather than continually training the *model*.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors examine how to improve model performance when SFT and preference data is unreliable (contains some proportion of mistakes). They find that doing SFT training still results in improvements with unreliable data, but DPO does not improve. They propose a new method, iterative label refinement, which involves iteratively training models on data subsets, and then using the models to relabel the SFT data (with an unreliable supervisor deciding if the new label should be accepted), and retraining. The proposed method outperforms DPO when applied to SFT models both in an artificial setup (using small models to train larger ones) and a time-constrained human-labeller setup.

### Strengths
- I think the experimental setup is good, looking at a variety of models and tasks, and the human labeling experiment is also interesting.
- The analysis of why DPO does not perform well with unreliable data is interesting, and provides reasonable evidence that DPO can fit too hard to the unreliable preferences.
- The performance of the proposed method seems robust, with it being tested both in multiple settings and with (time-constrained) human annotators. The performance gains seem robust across the tasks and models tested.

### Weaknesses
 - Missing Baseline: it would be good to compare against just doing SFT on the chosen sample or unreliable DPO pairs (my understanding is that this is not the same as training only on the model’s proposals because there is an additional trained classifier that may pick the right answer, albeit unreliably).
- I wonder if the comparison between DPO and SFT/ILR methods are entirely fair since the DPO method doesn’t use the original ground truth answer, just two model generations. Could the DPO results perform better if the original ground truth label was also provided as an option when picking chosen and rejected pairs (as it is for the ILR approach)? Would it be possible to run the same ILR algorithm outlined in section 5.1, but rather than replace labels, just use the accepted/rejected proposals to construct chosen/rejected pairs instead?
- Figure 6b is quite hard to parse, as the label box overlaps with a large chunk of the figure, and the differences between round 1 and 2 are somewhat small.
- Did the authors try longer DPO training with a high beta? They clearly show that using a larger beta with unreliable feedback can improve a bit, I wonder if training for longer with higher beta results in further improvements with DPO or if it then starts to over-optimize as well (potentially a different way that the issues with DPO could be alleviated).

### Questions
1. I was a bit unclear on how the unreliable DPO dataset is constructed: so, you generate responses from a model checkpoint, and train a classifier to pick the original ground truth label instead of the model response, and then use this classifier to pick between two samples from the same model checkpoint? Or is the classifier the same across rounds?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes iterative label refinement (ILR) as an alternative to reinforcement learning from human feedback (RLHF) for language model post-training under unreliable supervision. The authors argue that in settings where human supervision is unreliable, methods such as direct preference optimization (DPO) become less effective. Instead, ILR iteratively refines the supervised fine-tuning (SFT) dataset by replacing unreliable human demonstrations with better model-generated responses, thus improving the model’s training data. Experiments show that ILR outperforms DPO in tasks such as math, coding, and safe instruction-following, especially when human supervision is noisy or unreliable.

### Strengths
1. **Motivation.** Safe post-training of language models with noisy fine-tuning data is a highly practical problem with a lot of relevant research done to address the issue.

2. **Experiments and analyses.** The paper conducts a range of experiments, simulating unreliable supervision using small LMs and time-constrained human evaluators to evaluate ILR under multiple settings.

3. **Performance.** ILR demonstrates improvements over DPO under the unreliable supervision settings considered in the work.

### Weaknesses
1. **Limited evaluation of alternatives.** Several approaches exist for handling noisy feedback data, including conservative DPO [1], which combines regular DPO with label smoothing, IPO [2], MMPO [3], and filtering noisy labels, among others. However, empirical evaluations of some of these methods in the unreliable supervision setting considered are missing. Specifically, the paper lacks a comparison to methods that explicitly address noisy labels in preference learning, such as those that incorporate uncertainty or confidence measures in the preference modeling process. A more thorough evaluation should include a wider range of baselines that are designed to be robust to noisy supervision, and not just those that are designed for random noise.

2. **Unreliable supervision not well-defined.** The concept of unreliability is not quantitatively well-defined. For example, it is unclear whether a small LM trained as a classification model actually provides unreliable comparison feedback, and if so, to what extent the labels are considered inaccurate. Relatedly, it is unclear how unreliable the “time-constrained” human supervision really is. The paper should provide a more rigorous definition of unreliability, perhaps by quantifying the error rate or the level of disagreement between the unreliable labels and a ground truth or gold standard. Without a clear definition, it is difficult to assess the generalizability of the results.

3. **Questionable assumptions.** For the ILR framework to be effective, it seems that the SFT model needs to generate responses that are often better than those in the SFT dataset, and the annotator must be able to identify these better responses. While the latter assumption is discussed in the paper, the former depends on the SFT model being sufficiently capable and not overfitted to the SFT data, so that it can generate responses than the SFT data at least some of the time. This depends on factors such as the size of the SFT dataset, the proportion of unreliable data, and the size of the SFT model, raising questions about how generally applicable ILR is. The paper should provide more analysis on how the performance of ILR varies with these factors, and under which conditions the assumption of the SFT model generating better responses holds.

### Questions
1. How does ILR compare to having annotators review each sample in the SFT data to remove low-quality ones? This approach seems less expensive, as it avoids generating new responses with the SFT model and lets the annotators avoid pairwise comparisons.

2. How frequently are the model-generated responses considered better than the SFT data depending on the size of the model?

3. Typos: “Ground Truth” in Figure 5.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a novel approach, Iterative Label Refinement (ILR), aimed at improving language model (LM) post-training when demonstration and human supervision is unreliable. The authors identify that RLHF (specifically DPO) struggles under unreliable feedback due to overoptimization, and they propose ILR as an alternative that improves the supervised fine-tuning (SFT) dataset itself. The approach replaces low-quality human demonstrations with (small) model-generated alternatives based on comparison feedback, which is then used to retrain the model. The paper provides evidence that ILR outperforms DPO in various tasks, including math, coding and safe instruction-following, under both LM-simulated and human supervision settings.

Comments:
- Scalability and Computational Cost: The paper could include a more detailed discussion on the computational trade-offs involved in using ILR versus DPO. Given that ILR requires multiple rounds of refinement, it would be useful to know how this affects training time and computational resources.
- Clarification on Theoretical Boundaries: Theoretical analysis could be expanded to explore the long-term behavior of ILR. For example, will the refinement process converge effectively without introducing new errors or biases into the dataset over time?
- Additional Visualizations: It would be helpful to see additional visualizations that show the progression of ILR versus DPO over multiple training rounds, especially in terms of how the refined dataset improves in quality and how the model’s performance evolves.
- Task Extension: Future work could explore extending ILR to more diverse task types, including more subjective ones or tasks where human demonstrations are more error-prone (e.g., complex visual tasks or tasks requiring nuanced judgment).

### Strengths
- Novelty and Significance: ILR introduces a fresh approach to addressing the key challenge of unreliable human supervision in language model post-training. This is quite crucial as RLHF is becoming increasingly important for scaling LMs in practical applications.
- Comprehensive Evaluation: The experiments cover different tasks including math, coding, safe instruction-following and use both LM and real human feedback, ensuring the findings are well-supported. The robustness of ILR under different conditions and tasks is thoroughly tested and clearly explained.
- Clear Motivation: The paper presents a strong investigation and reasoning for why RLHF, especially DPO, struggles under weak supervision. The overoptimization problem is well-identified and investigated, which motivates the need for a method like ILR, which focuses on refining the training data rather than the model directly.
- Effective Use of Feedback: The authors highlight the importance of directing comparison feedback towards improving the dataset, not just the model. This is a significant insight and could influence future work in RLHF, encouraging researchers to rethink more about how to utilize human feedback in post-training.

### Weaknesses
 - Potential ensembling effect that may explain performance gain: 5.1 describes training one model on each half of the SFT data, then using these models to cross-label during ILR. There does not seem to be an ablation either. I think a fair comparison would be against a two-model ensemble, as opposed to a single model baseline. 
- Limited Comparison with other RLHF Methods: While the paper focuses on comparing ILR to DPO, it does not address how ILR might perform compared to other RLHF algorithms, like PPO. Including more comparisons could make the paper’s conclusions more robust and introduce a broader impact. Specifically, it is unclear if the overoptimization issues observed with DPO are unique to that algorithm or if they extend to other preference optimization methods. A more thorough investigation of this aspect would be beneficial.
- Computational Cost and Scalability: The ILR approach, which requires iterative refinement and cross-evaluation of datasets, which means  both SFT model and DPO needs to be retrained for every iteration. This might introduce higher computational complexity compared to DPO or traditional RLHF methods. The paper could benefit from a more detailed discussion of the trade-offs between performance improvement and computational cost. The current discussion lacks a quantitative analysis of the computational overhead of ILR compared to DPO, which is crucial for assessing its practical applicability.
- Task Diversity: While the paper tests ILR on math, coding, and safe instruction-following, it would be beneficial to see it applied to a broader range of tasks, particularly more complex or open-ended ones where human feedback is highly subjective or unreliable (e.g., creative writing or subjective question-answering or toxicity). The current evaluation tasks may not fully capture the challenges of applying ILR to more nuanced and subjective domains.
- Theoretical Depth: The theoretical tracking of ILR is solid, but the paper could elaborate more on the theoretical limits of ILR. In particular, the long-term stability of ILR, and whether it risks introducing new forms of bias through the iterative refinement process, could be explored. The paper lacks a formal analysis of the convergence properties of the iterative refinement process, which is essential for understanding its robustness and reliability.

### Questions
- How does ILR compare to other RLHF methods like PPO? Would similar overoptimization issues arise in other preference optimization methods, or are they more resistant to unreliable supervision?
- Could ILR be extended or adapted to address tasks that involve more subjective or open-ended feedback, such as creative writing or opinion-based tasks?
- Does ILR introduce any risks of bias through its iterative process, particularly as models continue to generate and refine their own data? How would you address or mitigate such risks?

### Soundness
2

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
2

### Summary
The paper shows that DPO is ineffective in the presence of unreliable feedback. The paper introduces a new method that replaces data samples in the SFT demonstrations dataset with synthetic demonstrations if the reward model prefers the synthetic demonstration. This process is iterated.

### Strengths
- Demonstrating the failure of DPO via overoptimization in the presence of unreliable feedback is important, given the prevalence of unreliable feedback.
- The introduced method is simple and performs clearly better.
- Validation on human setting increases confidence that the results on synthetic setting are reasonable

### Weaknesses
 - Doesn't compare against PPO

 - Is it specifically necessary to do 1:1 replacement of training data points with new synthetic ones? Does it make sense to decouple the number of data points removed due to low quality, and the number of new synthetic data points accepted? How much of the effectiveness is due to the filtering vs the addition of synthetic data points?

### Questions
- Is it specifically necessary to do 1:1 replacement of training data points with new synthetic ones? Does it make sense to decouple the number of data points removed due to low quality, and the number of new synthetic data points accepted? How much of the effectiveness is due to the filtering vs the addition of synthetic data points?

### Soundness
3

### Presentation
3

### Contribution
3
