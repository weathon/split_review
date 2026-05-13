# Report Cards: Qualitative Evaluation of Language Models Using Natural Language Summaries

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
The rapid development and dynamic nature of large language models (LLMs) make it difficult for conventional quantitative benchmarks to accurately assess their capabilities. 
We propose \cards, which are human-interpretable, natural language summaries of model behavior for specific skills or topics.
We develop a framework to evaluate \cards based on three criteria: specificity (ability to distinguish between models), faithfulness (accurate representation of model capabilities), and interpretability (clarity and relevance to humans). We also propose an iterative algorithm for generating \cards without human supervision and explore its efficacy by ablating various design choices. Through experimentation with popular LLMs, we demonstrate that \cards provide insights beyond traditional benchmarks and can help address the need for a more interpretable and holistic evaluation of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework for qualitative evaluation, based on specificity, faithfulness, and interoperability. To do so, the paper proposes a PRESS algorithm to generate natural language descriptions for LLMs in an iterative way. The experiments cover multiple LLMs, and the corresponding analyses read well.

**update after rebuttal**: I am not fully convinced by the authors' response, in particular the human evaluation part. If the authors suggest that they need more time to collect data for reliable evaluation, I suggest they fully prepare it and submit the paper to other suitable conferences.

### Strengths
This paper is generally well-written and is very interesting.

### Weaknesses
1. There are other works focusing on qualitative evaluation, such as [1], which formulate the problem in a very similar way, i.e., generating human languages to describe the limitation of LLMs.
2. There are some unavoidable and major limitations, although the authors have discussed them in the limitation section. For example, the selection of tasks is limited, and seems that the framework cannot be easily extended to generation tasks.
3. The human evaluation to me is not that reliable. There are 18 annotators but with only 230 instances. I am concerned that there can be a bid variance between different annotators. Also, I did not find the human annotation agreement. Could please the authors remind me if I am wrong?

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes Report Cards, human-interpretable natural language summaries, based on three criteria: specificity, faithfulness, and interpretability. They also propose PRESS an iterative algorithm for generating report cards. They show through experimentation with popular LLMs that report cards provide insights beyond traditional benchmarks.

PRESS (Progressive Refinement for Effective Skill Summarization) is an iterative algorithm for generating Report Cards without human supervision. PRESS works by iteratively generating and refining summaries of model behavior, focusing on specific aspects in each iteration and synthesizing them into a comprehensive overview.

The authors conducted experiments across multiple datasets, including MMLU (Massive Multitask Language Understanding), the Anthropic Advanced AI Risk dataset, and a Chinese grammar dataset. They tested various models, from OSS models like Llama-3.1-8B-Instruct and Mistral-7 B to closed models like GPT-4 and Claude 3.5 Sonnet.

### Strengths
1) There is a need for more than model cards in the LLM information space, while model cards report model parameters, and other minute details like data, training steps (including post training), and evaluations on various benchmarks, they do not provide holistic insights into model capabilities and nor are these insights granular in nature. Evaluations on benchmarks are ultimately unidimensional and limited to the number, and do not provide specific insights into what the model is good or bad at.

2) It also perhaps addresses a real need in LLM development and deployment, where model providers or users are interested in models that are better at specific tasks (or sub tasks) vs overly general models.

### Weaknesses
1) The PRESS algorithm ultimately depends on a judge model (in this case, Claude) to provide the final report card; usage of Claude or any model at that scale would add some costs to the generation of the report card vs. model cards that do not rely on LLM judgement. 

2) The reliance on LLM as a judge model perhaps also showcases a shortcoming, would a model be good at verifying or recognizing a model better than it or rely on its own (perhaps wrong) judgement. This is particularly concerning when the judge model might have inherent biases or limitations in its understanding, potentially leading to inaccurate or skewed report cards. The lack of a clear mechanism to validate the judge model's assessment raises questions about the reliability of the generated summaries.

3) It is not wholly clear if the report card works for advanced topics, MMLU while it covers a variety of topics, is not a benchmark covering all the depth and breadth of any one subject. The current evaluation lacks a rigorous assessment of the method's performance on highly specialized or complex domains, which limits the generalizability of the findings. The absence of experiments on datasets that require deep domain expertise raises concerns about the applicability of report cards in real-world scenarios where models are often deployed for specific, advanced tasks.

### Questions
1)) Assuming a specific case, a question that cannot be reliably solved by the judge model as well, but a fine-tuning of the base model does solve it, can a judge model reliably generate a summary for the same? Is the method generally constrained by the capability of the larger, better model? Is there any recourse for this?
2)  Is the readability of the report card considered at the macro level? What is done to balance specificity vs general comments? Figure 10 is a very good example of capturing nuances. Still, if this is done regularly at a global level across questions and subjects, this would quickly add to the length of the report card, and thus, the readability of the report card would be affected, right?

Could you showcase a full report card for any model of your choice? While the methodology to create it makes sense, it is not quite the same as looking at the final product.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper suggests a qualitative way to summarize an LLM's performance on a benchmark using "Report Cards". E.g., for Llama-70B-Instruct on MMLU High School Physics, the report card describes strength/weaknesses across ~10 dynamic facets, like "* Newton's Laws Mastery: The student demonstrates a solid understanding of Newton's laws, ...  However, it shows a misunderstanding of Newton's third law ...".

They generate report cards for 9 models across 10 tasks, evaluating their quality through some proxy metrics: 1) Contrastive accuracy: How well can a "guesser LLM" look at two models' reponses to a quiz (k questions in a task) along with a report card for each model, and guess which responses are from which model. 2) Card Elo: A "judge LLM" compares to report cards to decide which is the "best" model, to derive a "Card Elo" rating. How well does that agree with some "ground truth" Elo rating of the models? 3) Human scoring of report cards clarity, relevance, informativeness.

They use an "evaluator LLM" to generate the report cards, trying two main approaches (one-pass prompting and iterative PRESS method). The results on the proxy metrics indicate that the iterative method works better, and also is better than some other baseline approaches for each metric.

### Strengths
The paper's focus on getting more insights into LLM performance, beyond just accuracy numbers, is an important topic. The presentation is reasonably clear, with good descriptions of the approach.

### Weaknesses
The utility of these report cards is very unclear, the few concrete examples given in the paper give little confidence that any actionable insights can be derived.

The report cards are trying to identify useful subtopics for a task, and describe a model's performance on such sub topic. A much more concrete way of doing that would be to generate some hypotheses (like the example in Figure 10 that Llama-3-8B-Instruct "struggles with combinatorial concepts".) based on seeing a subset of the dataset. Then associate that with a score on that subtopic (model scores 45% on questions with "combinatorial concepts" vs 65% overall). Then further test that hypothesis on a held out set of questions to see if the drop in performance hold up. This seems like a minimal expectation for this kind of work.

The proxy metric of "Contrastive accuracy" seems like it would have many confounders, and a strong dependency on the size of the quizzes (which sounds like it's 120 questions, it's a bit unclear). Some attempts are done to "de-stylizing" the model outputs, which deals with the confounder of CoT style, that's a good idea. But as a measure of report card utility, it seems quite farfetched.

The Card Elo metric is extracting a measure of overall performance from the report card itself (according to a judge LLM), computing correlation with Elo based on actual task performance. They get reasonable R^2 scores of around 0.8, beating out R^2 from a generic ChatBot Arena Elo. It's far from perfect in ranking the models though, so not a substitute for the raw score.

This section has a quote "Importantly, k-shot completion Elo, using the same number of comparisons as Card Elo, obtains a significantly worse faithfulness score than Card Elo." which is a bit unclear in what is meant. It looks like "k" in this context is 2 or 4 (according to section 3.2, this is a different "k" from the 120 apparently used for quiz sizes?). So unclear what "same number of comparisons" means here, maybe the number of model matchups which seems a bit irrelevant (there's only a fixed number of models to possibly match up here).

Finally, the human evaluation (and associated LLM-simulating-human evaluation) of the report cards could be the most insightful. But the most interesting "informativeness" score (which averages a high 4.5 out of 5 from the humans) is based on a generic question: "How informative is the excerpt about the model's capabilities with respect to the question and the model answer?" with choices like

4. Very informative: Provides comprehensive information, covering most key aspects.
5. Extremely informative: Provides extensive, detailed information, covering all key aspects.

which tells us very little about how effective this report card is to actually understand something useful about the models' performance. 

Admittedly this is a hard task to evaluate, but the current effort leaves me with no confidence that these report cards are actually useful for anything. 

Also missing is any analysis across the models' report cards to hypothesize actionable differences, both for improving the models, or at least to estimate performance on new subsets.

### Questions
NA

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Report Cards, a technique to evaluate LLMs using natural language instructions, and provide interpretable and holistic results.
The authors present the algorithm for progressively generating report cards, PRESS - it features accumulating / summarizing LLM judgement results of models' predictions for text-based tasks. They as well present 3 ways to evaluate Report Cards themselves: the Contrastive Accuracy (given 2 model predictions and 2 report cards, a judge is asked to match a report card to the prediction), Card Elo (given 2 predictions and 2 cards, determine a winner), and human scoring.

They evaluate Report cards on 3 datasets (MMLU, Adv. AI Risk and CN Grammar) using a range of small to large backbone models.
In the contrastive learning judgement, they compare Report Cards with 2 baselines: Constant (judging based on accuracy on ground truth labels) and few-shot (instead of report cards, the contrastive judge is given k predictions the training set)
Card Elo is evaluated via R2 score against Ground Truth Elo (for which either gold labels or another LLM judge are used). Finally, in human scoring, the cards were assessed on a 5-point Likert scale along Relevance, Informativeness and Clarity dimensions.

Evaluations show that Report cards achieve competitive results using the proposed Contrastive Evaluation technique, although with an unexpectedly high result of the few-shot baseline; Card Elo achieves superior R2 scores against competing Elo methods and baselines; Report Cards also attain consistently high scores in human evaluation.

### Strengths
* a new method for evaluation of models on text generation tasks is proposed
* it provides high human interpretability and achieves high accuracy together with 2 evaluation methods, Contrastive Evaluation and Card Elo

### Weaknesses
 * few-shot baseline for Contrastive evaluation is confusing - it's unclear to me how informative is matching a model's prediction on testset to k sampled predictions on the trainset
* de-stylization issue suggests that few-shot baseline captures not very useful information and should ideally be re-thought
* Ground truth Elo for R2 faithfulness evaluation uses yet another judge - so it should probably be renamed into Oracle Elo

### Questions
N/A

### Soundness
2

### Presentation
4

### Contribution
2
