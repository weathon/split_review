# MathEval: A Comprehensive Benchmark for Evaluating Large Language Models on Mathematical Reasoning Capabilities

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 6, 6, 3, 3

## Abstract
Mathematical reasoning is a fundamental aspect of intelligence, encompassing a spectrum from basic arithmetic to intricate problem-solving. Recent investigations into the mathematical abilities of large language models (LLMs) have yielded inconsistent and incomplete assessments. In response, we introduce MathEval, a comprehensive benchmark designed to methodically evaluate the mathematical problem-solving proficiency of LLMs across varied contexts, adaptation strategies, and evaluation metrics. MathEval amalgamates 19 datasets, spanning an array of mathematical domains, languages, problem types, and difficulty levels, from elementary to advanced. This diverse collection facilitates a thorough appraisal of LLM performance and is stratified by language (English and Chinese), problem category (arithmetic, competitive mathematics, and higher mathematics), and difficulty. To overcome the challenges of standardizing responses across diverse models and prompts, we've developed an automated LLM-driven pipeline for answer extraction and comparison, ensuring consistent evaluation criteria. To broaden the utility of MathEval beyond the scope of GPT-4, we have harnessed the extensive results from GPT-4 to train a deepseek-7B-based answer comparison model, enabling precise answer validation for those without access to GPT-4. This model will also be made publicly available. MathEval not only assesses mathematical proficiency but also introduces a method to identify potential data contamination within pre-training datasets. This is done by hypothesizing that enhancements in one mathematical dataset should be mirrored by advancements in correlated datasets, thus signaling potential contamination—like the inadvertent inclusion of test data in the pre-training phase. To mitigate this and truly gauge progress, MathEval incorporates an annually refreshed set of problems from the latest Chinese National College Entrance Examination (Gaokao 2023), thereby benchmarking genuine advancements in mathematical problem solving skills. MathEval strives to refine the assessment of Large Language Models' (LLMs) capabilities in mathematics.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
MathEval is an extensive benchmark that includes various math scenarios, different types of prompts, and LLM-based evaluation. This solves the problem of incomprehensiveness, inadequate adaption, and inconsistency. MathEval incorporate 22 datasets in English and Chinese. MathEval also has dynamically updated content to prevent data contamination. In addition, it uses a robust evaluation framework, leveraging GPT-4 for automated comparison. It also uses its findings to fine-tune a DeepSeek-7B-based model and validates evaluation accuracy through human annotation. It also evaluates 52 models across three categories and proviees a comparative analysis.

### Strengths
Overall, much of what I mentioned in the summary is a strength of the paper, but here are some more specific strengths I have noticed:
- I very much appreciate how clear the introduction is. The the distinction between the three primary issues in evaluation the mathematical reasoning capabilities of LLMs is precise and clean.
- The experiments are very thorough, evaluation 52 models across 22 datasets.
- I appreciated the use the human annotation process to demonstrate precision.
- The two-stage evaluation approach combining GPT-4 and regex methods is great.
- I think the flexible prompt adaptation strategies for different model types is very useful for future research.
- Overall, this paper systematically addresses the challenge of mathematical answer comparison.

### Weaknesses
Here is a list of areas for improvement:
- I find it a bit difficult to read Figure 2 due to the acronyms. You could use icons for each category (e.g. flag icons for languages, school building icons for grade levels, etc.) or use a combination of icons and abbreviated text.
- Although Figure 3 is very informative, I find it a bit difficult to read the light green text on the gray background. I recommend updating the color scheme to dark text on light background or increasing the font size of the text within the boxes. You might also want to use a colorblind-friendly palette to ensure accessibility.
- For Figure 4, am I correct in saying that part c uses the results from parts a and b? If so, I recommend including arrows from parts and b to part c. This would help understand the flow of the components and the overall framework.
- Although it is great that MathEval has math problems from multiple levels of education, I am curious about why you don’t have more college level mathematics, at least at the undergraduate level. Ideally, this includes both academic math, such as real analysis, and competition math, such as the Putnam competition. I think this would provide more insights into how different models fare on different difficulty levels. Can you explain your rationale for focusing on K-12 levels and discuss the potential benefits and challenges of incorporating higher-level mathematics in future iterations of MathEval?
- I like how you mention details on what datasets are included in MathEval in the appendix. However, I think it would be beneficial to include a more detailed summary in the main paper. Otherwise, the reader may be left wondering what kind of data is in MathEval and how difficult it really is. I suggest including a brief summary table or paragraph in the main text that outlines key characteristics of the datasets (e.g. number of problems, difficulty levels, main mathematical concepts covered).
- You mention that you use calculation scheduling. However, I recommend including in the Appendix more details of the algorithm used and why it was chosen.
- I recommend including more middle school datasets (only Arith3K exists in MathEval at this point) for balance.
- Can you add some implementation details of the evaluation pipeline? This would aid reproducibility.
- I think training details for the DeepSeek-7B comparison model could be more detailed.
- Can you add more details on how the dataset is automatically updated?
- Can you include more details on how you generated the parts of MathEval that are labeled with “(ours)” in Table 2?

### Questions
- Would you have significantly different results if you used Claude rather than GPT-4 for the LLM-based evaluation? What are the limitations of using GPT-4 as an evaluator?
- Why did you choose Chinese as the second language to consider? Why not consider other languages? What unique advantage, if any, does analyzing Chinese language performance over other languages bring?
- What are the failure modes are error patterns that consistently appear because of dataset construction? - - What are some limitations?
- Why do chat models consistently outperform base models in these tasks?
- What types of mathematical reasoning are not currently captured by the benchmark?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
MathEval represents a comprehensive benchmark designed to rigorously evaluate the mathematical problem-solving skills of large language models (LLMs).The benchmark is stratified by language, problem category, and difficulty, ensuring a comprehensive evaluation.To standardize responses and ensure consistent evaluation criteria, an automated LLM-driven pipeline for answer extraction and comparison has been developed.MathEval provides an extensive benchmark that includes a diverse array of mathematical problems across different types and difficulty levels. MathEval have developed a standardized method for comparing answers that effectively addresses the complexities associated with outputs from mathematical word problems (MWPs).MathEval implements a strategy of using a dynamically updated dataset.

### Strengths
This proposed framework is really useful and provides a more general evaluation standard for the evaluation of mathematical reasoning ability of subsequent large language models.And the problems it can solve are also diversified.

### Weaknesses
1. For a more mathematical process, it seems that a better evaluation standard cannot be given; 
2. For the multi-step mathematical reasoning process, it seems impossible to evaluate whether this process is moving towards the expected solution process.
3. The classification of mathematical reasoning evaluated in the experiment is still a little rough.

### Questions
1. Can this framework evaluate the reasoning process? Because sometimes the results are the same, the complexity of the reasoning process is also a point that needs to be considered in the reasoning evaluation of large language models.

### Soundness
2

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
5

### Summary
The authors present a benchmark that aims to address three dimensions of current math benchmarks: comprehensiveness, adaptation, and consistency. MathEval is a benchmark specifically designed to evaluate the mathematical reasoning abilities of LLMs across problem types, languages, and difficulty levels, encompassing primary through high school math problems in English and Chinese. The benchmark includes 22 datasets and integrates a dynamic update feature, adding new problems annually to reduce test data contamination. MathEval uses a tailored prompting approach to adapt to the unique characteristics of different models and problem types, ensuring fairer and more accurate comparisons. To maintain consistency and overcome the limitations of traditional rule-based evaluation methods, the benchmark uses GPT-4 for answer extraction and comparison, with a publicly available deepseek-7B model as an accessible alternative.

### Strengths
* The authors create a comprehensive benchmark that includes 22 math reasoning benchmarks, some of which they create. The benchmark is annotated with the following dimensions: language of the problem, educational level (primary to high school), and problem type (arithmetic vs. word problem).
* Because different models and different datasets require unique prompting techniques, the paper also includes adaptable prompt templates which make it easier to evaluate a model under zero/few shot conditions depending on what is more suited for the model.
* The paper also presents an open model that can be used to compare mathematical answers for researchers who might not have access to GPT-4 to use for grading.

### Weaknesses
 * Some previous work (https://arxiv.org/pdf/2407.00900) has been done around using open source LLMs as part of the grading framework, although fine tuning a specific model for the answer comparison task is still a notable contribution.
* While the paper presents a significant effort in benchmarking (and the tools presented to the broader research community via this paper will be useful to researchers), the discussion from the numerical results support a lot of things that are already well known (the supremacy of closed-source over open-source models, the performance of math domain models generally being better, few-shot prompting generally resulting in better performance when compared to zero-shot, etc.)


### Questions
* To minimize compute costs, wouldn’t it make more sense to first try regex-based answer extraction on an answer, and in the case that the regex-extracted answer is incorrect (which could be caused by either a genuinely incorrect answer, or a mis-extracted answer), run GPT-4/the custom model on the answer? Because in Figure 14, we see that precision for answer verification with regex-only is high enough that GPT-4 doesn’t need to be run on every single model output, and rather only on ones that are originally marked as incorrect.
* In lines 415-418, the authors note that the dataset-level higher setting consistency outperforms using either few- or zero-shot prompting. However, isn’t dataset-level higher defined as the higher accuracy between few- and zero-shot accuracy at the dataset level? So wouldn’t this behavior be expected by definition? Sorry if I am misunderstanding the definition.
* Just a quick note about the conclusion section (line 464): the paragraph mentions 2 datasets when MathEval actually includes 22.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces MathEval, a unified evaluation suite for mathematical reasoning of LLMs. It puts together 22 datasets, and provides a unified method to extract and score answers given model responses. The base answer extraction method in MathEval uses GPT-4, but the authors provide a fine-tuned DeepSeek-Math 7B model just for the task of answer extraction. Authors provide experiments on 52 closed and open models, with Claude 3.5 Sonnet performing best overall in both English and Chinese.

### Strengths
* The paper is easy to read
* The unified dataset is likely to be useful for the community. Answer extraction is indeed a pain for math evaluations, and it's useful to have a standardized method / model for this. I believe people would use this.

### Weaknesses
 * While I do think the effort behind MathEval is useful, I'm not sure if it provides sufficient insight or novelty for an ICLR research paper. I did not gain any insights from the paper, and by construction it is composed of existing evaluations of reasoning capabilities.
* It's unclear to me how much overlap there is in the datasets in terms of distribution of problems. Besides the multilinguality, I'm not sure the datasets are measuring fundamentally different things.
*


### Questions
* Have the authors looked at correlations between performance on all the 22 datasets?
** If this correlation is high (which I'd suppose it is), what is the gain in using so many datasets, since their performance can be predicted from one another?
** If this correlation is low between some pairs, what orthogonal abilities might they be measuring?
* What insights did the authors derive from running all the evaluations that would not be obvious from just a small subset of them (e.g. one from each category in Fig 2)?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a more comprehensive benchamrk for LLMs in the domain of maths, elaborates on how elicitations mechanisms (prompt engineering, chain of thought, et.c) should be applied to different families and then introduces automatic evaluation of the results via GPT-4 and a finetuned model. The experimental results are consistent with previous evidence. Nothing especially relevant is found from the experiments.

### Strengths
- Comprehensiveness, at least in languages and types of problems.
- Releasing a low-cost finetuned model (DeepSeek-7B) that can be used for automated evaluation can be very useful.
- Number of models and configurations being evaluated.

### Weaknesses
 - The contribution is limited to the aggregation of benchmarks (some of them recently introduced with less contamination, but not evaluated separately) and automated grading.

- It's not clear whether the collection includes very difficult problems and may saturate soon. Current best results are around 70%, but not sure if there are some datasets or subdatasets where errors are quite high still. Aggregate results do not give a lot of insight.

- The prompt adaptation for models and datasets is not fully motivated. Is it the goal to evaluate each model and dataset in the condition that gets the best results? Is that fair and meaningful about an ecologically-valid use of these models in scenarios where maths knowledge is necessary? It's different to evaluate a specific LLMs for a competition and another is when these models are used in educational or engineering settings, to put two examples. In the end, why prompt adaptation instead of an off-the-shelf use? Language models should work in natural conditions, or all with similar china-of-thought prompts. In any case, how do we know that we use the optimal generic prompt for each LLMs?

Evaluation using LLMs is quite usual today. Section 2.3 tries to present this as new (but it's not even if multiple-choice problems are still very common), but there's significant work in this area:  https://arxiv.org/abs/2403.02839, https://arxiv.org/pdf/2406.18403, https://arxiv.org/abs/2408.02666 or https://eugeneyan.com/writing/llm-evaluators/.
Section 2.3 raises the qustion about how the evaluation from GPT-4 is validated. It seems this section is going to cover this, a comparison with a sample of answers evaluated by human experts? And it refers to appendix G.1 shows Table 7, but what's 0.6264 for instance? Inter-rater agreement? The caption says "overall average score". Are we choosing human annotations as ground truth? If this is agreement this is very low. What's the sample annotated by humans? The read may get confused because it seems this section is going to clarify what the quality of evaluation is by using GPT4. Then, this is expanded in section 3.2, and Figure 5 more specifically. But since the sample size is not mentioned, there's no sample and humans evaluate all the instances? What's the number of instances being labelled by each of the annotators? Using Kappa and having 0.8871 is good to use the human average (or mode?) as golden standard. Why for the 22 datasets or only 19? Why only 19? If this is done for 22, why figure 5 only with 19? Why not a sample of the 22? But then, in Figure 5, what does it mean to calculate an "absolute difference"? Are the answer other than correct and incorrect to calculate a "difference"? Why not Kappa as you did before? I cannot really determine whether the automated evaluations are good or bad as I cannot interpret the disagreement. And this is one of the key contributions of the paper.

Figure 3 and the related text is confusing. It's not clear whether all the things in blue and green are alwasy used, but not the one in black: "[COT prompt]". Is this optional? When is it introduced?

Is the configuration of prompts per model and dataset different? What if we need to explore a new model? Should we try to find the best prompts for each and every dataset in MATHBENCH?

The details about "Calculation Scheduling" and parallel processing are not part of the benchmarks, and definitely not part of the "prompts section". This is just experimental details or it could go to the appendix.

The evaluation results are based on an arithmetic mean of all datasets. This is a common practice but requires a justification, as the different datasets are incommensurate in difficulty. Why are easy datasets weighting the same as hard datasets? Do we have models failing at easy items but succeeding at difficult ones? Averages are not the best way of comparing systems. It is telling that the paper also reflects the results for GSM8K and MATH, and they see only minor discrepancies, so what's the point then about this comprehensive dataset if the same results could have been obtained with only GSM8K and MATH?

With this aggregate results, many of the observations in Fig. 6 are confirmatory, such as the best LLMs for maths (as we knew for some other dataset collections) are the best for this benchmark, and also the effect of finetuning, but specifically parameters (perhaps FLOPS would have been a better metric).

The separation between Math word problems and arithmetic in Fig. 6 (bottom) is more insightful, but the arithmetic variability is not explained (this is partly explained by "arithmetic plugins", but isolated benchmarks with basic operations using large numbers could have been conducted to know what models are using them or not).

The main contribution is an aggregation of datasets and some experimental results from them. The unification of prompting is questionable, especially in the way new models can be evaluated with this benchmark in an easy way, without the need for prompt adaptation.

Minor issues:
- Sometimes the authors use triple quotes, i.e., '''xxx''', which is non-standard.
- Conclusions, line 1: "In this papar"

### Questions
- Is prompting specialised for each pair of model and dataset?
- Is CoT used for some models but not others?
- How many instances did humans evaluate? 
- Why 19 out of 22 for the comparison humans - automated scoring?
- What's the distribution of difficulty of the datasets and the evolution across that difficulty?
- Is there any unexpected finding in the experimental results?

### Soundness
3

### Presentation
2

### Contribution
2
