# Curse of Instructions: Large Language Models Cannot Follow Multiple Instructions at Once

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
Large language models (LLMs) have demonstrated impressive performance across various natural language processing (NLP) tasks owing to the strong capability of following instructions. To further accelerate the integration of LLMs into our society, it is essential to have LLMs follow many instructions as accurately as humans do. This study reveals that LLMs unexpectedly struggle to follow all instructions simultaneously as the number of instructions increases.  First, to validate our claim, we introduce ManyIFEval, a large-scale benchmark dataset comprising task prompts with up to ten objectively verifiable instructions. Second, we conduct experiments based on ManyIFEval with GPT-4o, Claude-3.5, Gemini-1.5, Gemma2, and Llama3.1, demonstrating that as the instruction count rises, the models' ability to follow individual instruction deteriorates gradually but constantly. As a result, the models' ability to follow all the instructions significantly drops: the success rate of all the instructions is precisely explained by the success rate of individual instructions to the power of total number of instructions. We refer to it as the ``curse of instructions''. Third, to remove the curse without retraining models, we propose an inference-time strategy that enhances performance through iterative self-refinement. We demonstrate that instruction-level chain-of-thought reasoning significantly improves their capability to detect and correct instruction-following errors. Notably, our method has improved the success rate of following ten instructions by GPT-4o from 15% to 31% and Claude 3.5 Sonnet from 44% to 58%. We also show that precision is more important than recall in feedback: just telling LLMs that they are not following all the instructions also improves self-refinement success. Our findings highlight a fundamental limitation of instruction-following ability and suggest a future direction for building trustworthy LLMs that can coexist with human society.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed ManyIFEval, a large-scale benchmark dataset comprising task prompts with up to ten objectively verifiable instructions to test LLMs' ability of following multiple instructions. The authors conducted comprehensive analysis on ManyIFEVAL with different models including GPT-4o, Claude-3.5, Gemini-1.5, etc. The results suggested that models struggle to follow multiple instructions at once when scaling the number of instructions. The author also proposed a method to mitigate the performance degradation by iterative self-refinement through self-feedback loops in combination with chain-of-thought reasoning for each instruction.

### Strengths
- This paper is technically sound and the topic (LLMs' capability to follow multiple instructions at the same time) studied in the paper is valuable.
- The experiments are well designed and contains comprehensive analysis.

### Weaknesses
 - The major concern I have regarding this paper is that the lack of excitement compared to the literature. First, as pointed out by the authors, the benchmark is an extension of IFEval (for both prompt construction and evaluation framework). The main ingradient added in this paper is to extend the number of instructions and balance the number of instructions per sample. Both are too trivial to establish a new benchmark in my opinion. Second, one of the major conclusions in the paper that "as instruction count rises, the models’ ability to follow individual instruction deteriorates gradually but constantly" is not new and it's already discussed in the ComplexBench. Third, the mitigation method (self-refinement) is also a widely adapted method to improve LLMs performance across different tasks. I am not sure if there are new insights community can gain from the mitigation on this specific benchmark. 
- Section 4.3 and Figure 4 are quite confusing to me. To me, isn't that quite intuitive that if instruction-level accuracy is $p$, it means for each instruction, the probability of correct instruction following is $p$ on average. Then, for $n$ instructions, prompt-level accuracy is $p^n$, which is equation (3). Why do we need a simulation in Figure 4? Also, why is this a secret rule?

### Questions
- In Table 1, why "Model & Program" is marked as "X"? Does it suggest model-based eval is bad?
- In line 419, the repetition is set to 5. I am wondering have you tried different number of $T$ to see the trend of performance?
- In Table 2, do you have the performance numbers on instruction-level? I think put that number would also help better understand the results.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper extends the IfEval dataset by combining instructions to demonstrate how LLMs fail to follow compound instructions. The task prompts used are free-form generation but the authors incrementally add instructions (upto 10) from one of 6 categories (keyword inclusion, length constraint, Case requirements, Punctuation, Start/End, Formatting - eg use of bullets).  Zero-shot evaluations on GPT4o, Gemini 1.5 Pro and Claude Sonnet 3.5 demonstrate that the performance deteriorates as the number of instructions increase. The paper also suggests inference time improvements -- specifically, providing feedback and CoT based refinement for each instruction that fails. Experiments have also been included where the feedback is returned by the oracle verifier. Interestingly, simply giving feedback that all instructions were a failure (regardless of whether that was true) results in a significant improvement of performance.

### Strengths
- Simple extension to IFEval
- Interesting observation of Instruction-following feedback (as referenced in summary)
- Programmatic evaluation

### Weaknesses
 - This work inherits the weaknesses of IFEval -- for instance, task level performance is never assessed
- refinement w/ feedback+each+cot appears to be a very expensive solution (no discussion in paper)
- Evaluation only on three (closed) models

### Questions
No questions

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work studies the problem of following multiple instructions at once. To create a dataset for this study, this work extracts prompts and instructions from IFEval and produces a new dataset called ManyIFEval where each prompt has 10 instructions. The main empirical finding of this paper is that when there are n instructions, the prompt-level accuracy is equal to the instruction-level accuracy to the power of n. This work also proposes a feedback+refine-based method to improve multi-instruction following.

### Strengths
1. Analyzing the model's behavior on following multiple instructions at once is a simple yet insightful angle. 
2. The feedback+refine framework provides nice improvement on multi-instruction following.

### Weaknesses
1. My biggest concern of this paper is that the discovered rule seems to be a direct consequence of the instruction-level errors being randomly distributed across different examples. This seems to be an artifact of the way how the dataset is designed. I would imagine the finding to be different if the dataset containing examples with different level of difficulties. For instance, if the dataset contained prompts where some instructions are consistently easy and others consistently hard, the observed relationship between prompt-level and instruction-level accuracy might not hold. The current dataset construction doesn't seem to account for this potential confounding factor, making the generalizability of the core finding questionable.
2. The size of the dataset (100) is relatively small. In practice, this may lead to unstable evaluation metrics.
3. Besides the concern in weakness 1, there are a number of additional important  questions left unanswered for this study. Specifically,
    1. When there are n instructions, does the instruction following performance of the 1st instruction differs from the instruction following performance of the last (nth) instruction?
    2. How does the performance of the methods proposed in Sec. 5 change w.r.t the number of total instructions?
    3. Can we discover any pattern on how Inst-level Accuracy (n) changes w.r.t n? Finding such patterns allow us to extrapolate performance prediction from smaller n to larger n.
4. No details of the Zero-shot-CoT are mentioned in the paper.
5. This is a minor point, but the definition of "Precision" and "Recall" in Table 2 is a bit counter-intuitive.

### Questions
1. LINE 249 only mentions a training set and a test set. In that case, does all model development in Sec. 5 done on the test set? Will that have a risk of overfitting?
2. There are several typos in this paper:
    * ManyIFE**VAL** at LINE 099 and 102.
	* **O**ur at LINE 154
	* I'm not sure what "refinement w/o zero-shot" means in LINE 458.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper first introduces ManyIFEval, which is a dataset comprising task prompts with up to ten objectively verifiable instructions. Through this benchmark, the paper shows that current LLMs fails to comply to multiple instructions at once. To mitigate this problem, the paper apply a inference-time self-refinement strategy which boosts the performance.

### Strengths
- The paper is clearly written and straightforward.
- The reviewer agrees with the problem formulation; we need a LLM that can solve multiple instructions efficiently.

### Weaknesses
 - In related works (Figure 2), the authors claim that the contribution of ManyIFEval lies on complexity. However, the complexity does not significantly differ from ComplexBench.
- The size of the benchmark is too small and limited. It is specified that there are 110 for training, 100 for testing, and 6 for few-shot prompting which is a small number of prompts for evaluation. Also, the paper evaluates on only 15 instructions which is very narrow and distinct from real use cases mentioned in Figure 1 (legal and medical). 
- There are no further analysis depending on the model size or the  pretraining data scale for the result of Figure 1. 
- In Section 4.3, the authors claim that the finding of the paper is a 'rule': however, the paper only investigates 5 LLMs with a limited evaluation dataset. The paper should provide correlation or similar quantitative measure to claim that the finding is a 'rule'.
- It is expected that the performance reduces as the number of instructions increases; humans would also struggle to generate a response correctly when provided with multiple instructions.
- The proposed approach in Section 5 shows comparable performance with a heuristic baseline 'refinement w/ all false'. This weakens the effectiveness of the proposed approach; even though the baseline is much simpler with similar inference costs, it performs similarly.
- Performance of another heuristic baseline is missing: conditioning on task prompt $P$, single instruction $I_{i}$, and previous output $O_{i-1}$ (repeating this for the number of instructions). (1st inference: $P$, $I_0$ -> $O_0$, 2nd inference $P$, $I_1$,  $O_0$,-> $O_1$,... )

### Questions
- For the current setup, the task prompt is fixed and there are multiple instructions for each instance. Would a similar finding be observed when there are multiple task prompts and corresponding instruction for each instance (ex) Task 1, Instruction 1, Task 2, Instruction 2, .., )
- Would few-shot ICL mitigate the curse of instructions?

### Soundness
2

### Presentation
3

### Contribution
2
