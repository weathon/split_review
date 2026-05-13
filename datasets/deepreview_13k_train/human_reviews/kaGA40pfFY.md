# Rationality of Thought Improves Reasoning in Large Language Models

- Decision: Reject
- Scores: 6, 8, 6, 6

## Abstract
While the capabilities of large language models (LLMs) have been progressively advanced, their competence in addressing intricate reasoning tasks remains inadequate, primarily due to their insufficient cognitive capabilities. To explore the cognitive proficiency of models like GPT-4, we turn to methodologies from cognitive psychology: cognitive abilities reflect rational thinking skills, and cognitive bias tasks are often used to assess rational thinking levels. In this paper, we develop a cognitive bias dataset to measure the rational thinking and cognitive levels of LLMs. Our observations indicate that GPT-4, akin to humans, exhibits limitations in its rational thinking ability. We propose a new method, “Rationality of Thought” (RoT), to prompt LLMs into a rational thinking process during task execution. This method significantly improves the accuracy of GPT-4 on the cognitive bias task by 18.7\%. Cognitive capacity is also essential for tackling complex issues, therefore, we implement RoT across various reasoning tasks. Using only a zero-shot setting, RoT outperforms inference enhancement techniques such as CoT using few-shot, such as GSM8K (+0.4), AQUA-RAT (+4.8), ARC-c (+0.7) in multiple arithmetic and common sense reasoning tasks. Our empirical evaluation shows that RoT helps LLMs elevate their cognitive capabilities through rational thinking, thereby becoming more adept at navigating complex reasoning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a new prompt for LLM called "Rationality of Thought" especially designed to extract more rational answers from input queries. The prompt is evaluated on a proposed cognitive bias dataset as well as a number of reasoning datasets and is shown to outperform both direct prompting as well as the existing "chain-of-thought" prompting.

### Strengths
The paper is easy to read and the overall presentation is clear.

The contribution of this work -- the RoT prompt, seems novel and works especially well for super large model like GPT-4.

### Weaknesses
I think the only missing element is an ablation study. Given the rather wordy prompt, one wonders which part of it contributes the most to improving answer quality.

Although it is in the appendix, I am not sure what role Table 4 plays in this work. Where is this algorithm used?

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes Rationality of Thought, a prompting technique for reducing cognitive biases in LLMs. Based on a diverse collection of psychology papers, the authors compose a dataset of 464 questions reflecting 29 cognitive bias types. The RoT prompt improves performance of GPT-3.4 and -4 on this set of questions, and transfers effectively to other LLM benchmarks.

### Strengths
- The approach is well grounded in studies of human psychology. 
- The authors expend significant effort on summarizing the cognitive bias types in prior psychology work.
- The constructed dataset is valuable for assessing the cognitive biases of general-purpose AI agents.
- The RoT prompt is simple and effective. It improves the performance of LLMs significantly, outperforming chain-of-thought.

### Weaknesses
 - The data collection process is insufficiently detailed. See questions. 
- The prompt search process is not transparent. See questions
- Missing ablation studies. 
- The authors do not discuss the limitations of this approach (e.g., time/#tokens, generalizability).
- The dataset's limited scope, with only 464 questions across 29 bias types, raises concerns about its comprehensiveness and potential for overfitting. The lack of detail regarding the selection criteria for these questions makes it difficult to assess the dataset's representativeness of the broader landscape of cognitive biases.
- The prompt engineering process lacks transparency, specifically regarding the rationale behind the chosen steps and the iterative process used to arrive at the final prompt. Without a clear description of the search space and the evaluation metrics used during prompt optimization, it is difficult to assess the robustness of the resulting prompt.
- The absence of ablation studies makes it difficult to ascertain the contribution of each step in the RoT prompt. It is unclear whether all steps are necessary or if some steps are more critical than others. This lack of analysis limits the understanding of the method's inner workings and potential for further improvement.
- The authors do not discuss the computational cost of the RoT prompting technique, particularly concerning inference time and token usage. This is important for practical applications, especially when comparing it with simpler methods like direct prompting or chain-of-thought. Furthermore, the generalizability of the RoT prompt to other types of tasks and models is not discussed, which is a crucial consideration for its broader applicability.

### Questions
- Does the dataset have a train and a test set? If yes, are the results in figure 2 on the train or test set? If no, did you search for a prompt to overfit GPT-4 on the dataset?
- The questions are collected from "multiple authoritative psychological works"? Are they the same as those from which you compose the list 93 common cognitive biases? If not, you must cite them explicitly. 
- What are the limitations of the dataset? Is it also biased in some way (e.g., representing only Western culture, focusing on a majority group)?
- How did you come up with the prompt? Are these steps of solving a problem proposed prior psychology work?
- For a fair comparison, can you also provide the results of CoT zeroshot in table 3? It is possible to put the average cost of each prompting technique as a column?
- Can you conduct an ablation study to demonstrate the importance of each step in RoT? 
- Step 3 of the prompt encourages "probability calculations, Bayesian methods, and other data analysis techniques". It is a very specific request. Do you have evidence that the models actually follow this instruction? How do they behave when the solution of a problem does not require one of those techniques? 
- Do you use the same prompt for each evaluation domain? Are there any customizations?
- Do you specify all the RoT steps all at once or input one step, wait for GPT to respond and then input the next step?
- It would be more interesting to try this method on tasks on which the Direct-zeroshot performance is low (e.g., code generation?). Except GSM8K, performance of GPT-4 on other tasks is already strong.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a prompt engineering technique, called RoT (Rationality of Thought), whose goal is to align with the underlying logic of human cognition. The paper claims that RoT can assist large language models (LLMs) to reduce cognitive biases. Compared with Chain-of-Thought and other reasoning-enhancement techniques, RoT does not need additional manual annotations. RoT integrates various methods to improve reasoning of LLMs (e.g. thought chains, self-reflection, and expert knowledge) into a unified theoretical framework rooted in cognitive psychology. As part of the study, the paper has created a cognitive bias dataset.

### Strengths
1. The paper proposes a new prompt engineering technique, RoT designed to avoid cognitive bias. RoT include steps: identification, decomposition, reflection, calculation, and evaluation, among other markers of rational thought. 

2. When applied RoT to GPT-3.5-turbo and GPT-4 on the cognitive bias test set, accuracy improvements are 1.5% and 18.7%, respectively. 

3. The paper collects a cognitive bias test dataset including 29 such biases.

### Weaknesses
1. There does not seem to be convincing evidence that Rational of Thought method can improve arithmetic reasoning and common sense reasoning tasks. Specifically improvements on GSM8K (Cobbe et al., 2021), SVAMP (Patel et al., 2021),AQUA-RAT (Ling et al., 2017) , and ARC (Clark et al., 2018) over CoT are +0.4, -0.6, +4.8, -0.3, +0.7. Other than AQUA-RAT, the performance degradations and improvements are all very small. However, the paper does not dive deep into AQUA-RAT performance improvement.

As shown in the paper "Large Language Models Cannot Self-Correct Reasoning Yet", it is not clear RoT can improve reasoning when compared with CoT.

2. Despite connecting RoT to human cognition, there is little insight on why RoT can improve cognitive biases.

### Questions
Now there are a large number of prompt engineering techniques that decompose problems into sub-problems. The paper should comment and hopefully compare to some of the most notable ones, such as Least to most prompting, tree of thoughts, etc.

Besides the GPT family models, the authors are encouraged to study Anthropic Claude and open source models such as LLaMA2. This would be very important to see whether the techniques can also apply to other LLMs.

The evaluation seems to focus on multiple choices. LLMs are known to have position bias. Does the result change if you change the ordering of the answer choices?

== post rebuttal == 

The authors have made a good effort addressing my comments. The paper has improved quite a bit. However, there are still some remaining concerns. 

1. RoT zeroshot does not perform better than CoT zeroshot on GSM8K. Are there any insights? 
2. The improvement over CoT for GPT4 is 3% absolute. It is still relatively small.
3. Given the negative results on LLaMA, it is important to consider Claude.

As a result, my rating is borderline, between marginally accept and marginally reject. However, I have marked my score to marginally accept since there is rating in between.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose Rationality of Thought as a new method to prompt LLMs into a rational thinking process. In addition, they propose a new benchmark inspired by problems that have been used to study cognitive biases in humans. Their methods improve the accuracy of LLMs on their new benchmark and on existing reasoning benchmarks (but to a lesser degree).

### Strengths
The proposed method is interesting, clean, and well-motivated.

The paper is well-written and easy to follow.

The authors propose a new and interesting benchmark.

The obtained results are promising.

### Weaknesses
The authors write that each type of bias has 16 questions in their data set. Were all of these problems taken from prior literature or does this also include novel problems created by the authors? My main concern about the current state of the paper is regarding this issue. Many of the original cognitive bias problems (e.g., the Linda problem) are presumably heavily featured in the training data. To ensure that we are probing the reasoning capabilities of LLMs, it would be important to include novel (i.e., rephrased) versions of the original problems. While the current set does not include any such problems, I am unlikely to increase my score further. Maybe this is already done but the information is just not provided. In this case, the authors should describe how the rephrasing was done.

Important references to prior work are missing. For example, Binz & Schulz (2023) already studied some of the biases included in the present benchmark. In addition, the present paper takes quite a one-sided view in claiming that LLMs are becoming increasingly similar to human reasoning. There are many examples where this is not the case, see for instance Ullman (2023) or Mitchell & Krakauer (2023).

Binz, M., & Schulz, E. (2023). Using cognitive psychology to understand GPT-3. Proceedings of the National Academy of Sciences, 120(6), e2218523120.

Ullman, T. (2023). Large language models fail on trivial alterations to theory-of-mind tasks. arXiv preprint arXiv:2302.08399.

Mitchell, M., & Krakauer, D. C. (2023). The debate over understanding in AI’s large language models. Proceedings of the National Academy of Sciences, 120(13), e2215907120.

The visual presentation could be improved in places. In particular, while Figure 1 gives a good intuitive understanding of the approach, the reader has to go to the SI to see the exact RoT prompt. This is unfortunate as this is the heart of the paper. Furthermore, Table 1 does not add any value in my opinion. A good solution would be to therefore replace Table 1 with Table 5 from the SI or similar.

Minor:

Formatting is a bit weird in places, especially spaces are often used wrongly/inconsistently.

Equation on page 3:
* is not numbered.
* p_rot does not appear.
* \in \mathcal{D} should be in the subscript (also for the equations later in the paper).
* the equation implies that there is some optimization happening but that is not the case to my understanding (maybe I am missing something here).

Figure 3: legend and text are way too small to be readable. To allow for larger font sizes, subplots a and c could be removed given that they display redundant information with b and d.

The conclusion is not a conclusion as it is followed by a related work section.

Page 9: the authors say “Research by Alaina ...” but then cite another author (maybe first and surnames are exchanged here).

### Questions
The authors use zero-shot CoT for the experiments in section 3 and few-shot CoT for the experiments in section 4. Why was this choice made? It would have been easy to also use zero-shot CoT for the experiments in section 4 (especially if the claim is that RoT is nice because it does not require example solutions). Related to that, the fact that zero-shot CoT actually decreases performance on the cognitive bias dataset is surprising. Any idea why this is the case?

Given that the improvements were not so great in GPT3.5, would you say that RoT prompting is an emergent ability?

Finally, I was wondering whether all the steps in RoT prompting are needed or whether some of them could be removed without a loss of performance. I am not asking the authors to run additional ablations but I think this is still interesting to think about.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
