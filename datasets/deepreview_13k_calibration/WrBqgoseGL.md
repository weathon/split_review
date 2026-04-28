# Putnam-AXIOM: A Functional & Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs

- Decision: Reject
- Avg Score: 5.80
- Scores: 5, 5, 6, 8, 5

## Abstract
As large language models (LLMs) continue to advance, many existing benchmarks designed to evaluate their reasoning capabilities are becoming saturated. Therefore, we present the Putnam-AXIOM Original benchmark consisting of 236 mathematical problems from the William Lowell Putnam Mathematical Competition, along with detailed step-by-step solutions. To preserve the Putnam-AXIOM benchmark's validity and mitigate potential data contamination, we created the Putnam-AXIOM Variation benchmark with functional variations of 52 problems. By programmatically altering problem elements like variables and constants, we can generate unlimited novel, equally challenging problems not found online. We see that almost all models have significantly lower accuracy in the variations than the original problems. Our results reveal that OpenAI's o1-preview, the best performing model, achieves merely 41.95\% accuracy on the Putnam-AXIOM Original but experiences around a 30\% reduction in accuracy on the variations' dataset when compared to corresponding original problems. Moreover, we explore metrics beyond boxed accuracy to assess models on complex tasks like natural language theorem proving, crucial for evaluating reasoning capabilities  in depth, opening the possibility for open-ended evaluation of reasoning strings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Putnam-AXIOM, a benchmark of 236 problems from the William Lowell Putnam
Mathematical Competition, for evaluating reasoning capabilities of Large Language Models (LLMs).
It allows for automated evaluations with an equivalence function for potential different mathematical
presentations of the same final answer, that must be provided inside of "\boxed{}".
The paper shows state-of-the-art LLMs perform poorly in Putnam-AXIOM. The authors addressed the
potential data contamination issue with Putnam-AXIOM Variations, by altering the variable names,
constant values, or the phrasing of the question, on selected 52 problems of the original Putnam-AXIOM
and showed the performance of LLMs on this dataset is even worse.

### Strengths
The benchmark addresses the limitations of LLMs reasoning, such as not being able to solve really unseen
problems which indicates that they are probably memorizing solutions patterns from training data, instead
of true understanding and reasoning. This is showed in the paper, by the low performance on this novel
benchmark (Original) and by the even worse performance when altering variables, constants and question
phrasing while maintaining the same logical reasoning required to solve the question (Variations). The
paper shows it is an useful benchmark to evaluate LLMs reasoning capabilities since current benchmarks
are already saturated. It also addresses the data contamination issue with the Putnam-AXIOM Variations.

### Weaknesses
ROSCOE metrics are not applied to the evaluation in Putnam-AXIOM and the boxed answer requirement
discards intermediate steps to be used in the performance metric, so it doesn’t address the known LLM’s
logical mistakes and leaps in the reasoning process, even when getting the right answer, despite being a
problem identified by the authors in the beginning of the paper.
The proposed TFA proxy metric is not evaluated on proprietary models so the state-of-the-art models are
left out of the most comprehensive evaluation.

The 52 variations can give rise to an unlimited set of problems but they were created manually, and their
logic can eventually be data contaminated as well which is not addressed. Also it is a too small dataset.

### Questions
Is there a way of automating the creation of new Putnam-AXIOM variations in order to avoid Logic data
contamination? Do you agree Logic data contamination can happen, if not, why not?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Putnam-AXIOM - a new dataset to evaluate LLMs’ mathematical reasoning abilities. The dataset is difficult for state-of-the-art models, where we see the highest accuracy being only around 42%. The paper further aims to address the data contamination problem by introducing functional variations which alters variables, constants, and phrasing of the problems. The dataset allows automatic evaluation of final solution. 

The paper also introduces simple evaluation metrics such as teacher-forced accuracy (TFA), which evaluates intermediate steps by comparing to ground truth step by step solution. They observe TFA has better correlation to the final solution correctness than existing metrics like ROSCOE and BPC, despite TFA’s dependency on the ground truth and expectancy to under represent model abilities.

### Strengths
* The paper addresses the issue that existing reasoning benchmarks are getting outpaced by the LLMs. The proposed dataset is difficult for state-of-the-art LLMs such as GPT-o1
* The paper addresses the issue of data contamination by following methods to generate new data unseen during LLM training introduced by Srivastava et al. (2024). Specifically, the variables, constants, and phrasing of some eligible problems are altered. The proposed dataset variation sees LLM performances drop significantly.
* The paper introduces an evaluation metric that achieves higher correlation to the box accuracy when tested on easier arithmetic reasoning dataset.

### Weaknesses
Weaknesses:
* According to the paper, the proposed evaluation metrics cannot be used to evaluate proprietary models, which makes up a large portion of the state-of-the-art models.
* The LLMs evaluated are relatively small outside of the few state-of-the-art models: other than Claude-3.5 Sonnet, GPT-4, GPT-4o, GPT-o1, only 7B/8B models are evaluated in table 1. How does larger models like llama-70b perform?
* The dataset is relatively small, and is not easily extendable since a lot of manual work is required for new problems, including editing the problem to perform modified boxing (sec 3.1) and the need to manually identify problems suitable for functional variation (section 3.2), as well as writing the generation code for each problem (ex. https://anonymous.4open.science/r/putnam-axiom-B57C/src/variations/putnam2023.py).

Other comments:
* Figure 3 and 11 needs to be better presented, the labels are hard to read.

### Questions
1. I am confused why the paper did not present TFA scores for SOTA models in table 1. The paper justifies this by stating that “we can’t evaluate TFA on proprietary models as we require the log probabilities of the input tokens.” However, the TFA score introduced in section 3.4 seem to only require the ground truth data and the predicted tokens.

2. How is correlation calculated for evaluating the TFA metric?

3. What LLM model is used to produce table 2 to evaluate the metric? Does TFA out perform other metrics using different sized models? 

4. The paper claims that the generated variations of the dataset has the same level of difficulty as the original. However, won’t perturbing the constants can sometimes make a problem more difficult? Would it still be a fair comparison if each LLM is evaluated on different variations?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Benchmarks are crucial for machine learning research. Existing benchmarks have become increasinglily struggle to sufficiently asses the reasoning capabilities of modern large language models. This is in part due to the impressive advancements that we have seen in the recent past, but also due to the problem of data leakage. Since modern models are trained on huge text corpora that are often scraped from the internet, it is increasingly hard to hold out challenging problems for assessment.

The submission introduces the Putnam-AXION benchmark dataset, which consists of 236 challenging mathematical problems from the  William Lowell Putnam Mathematical Competition. All questions are modified so that there is a unique numerical answer (concrete number or formula) and the prompt instructs the model to provide the final answer in \boxed{} brackets, which simplifies evaluation (boxed-accuracy). Besides providing a new collection of challenging mathematical problems, the authors also identify a set of 52 question that can be altered in a systematic way as to lead to new problems with different solutions. The changes included rephrasing, renaming of variables and changing the value of constants. These functional variants are of particularly useful to asses how much of the performance on the original questions is due to memorization. The authors test a multitude f different model, both open source and commercially available ones, and experience a significant drop in performance when comparing the original Putnam-AXIOM questions with their functional variants. Almost all models show a statistically significant decrease in accuracy and the best performing model (o1-preview) shows a drop of 30%. 

Additionally, the authors evaluate metrics which are capable of assessing the quality of an LLM's answer in more complex scenarios. Since Putnam-AXIOM is still quite challenging for most models, the evaluation was conducted on the simpler MATH dataset. Metrics:
- Teacher forcing: Condition model on ground truth rather than on its own output. Variants: Accuracy, cross entropy, perplexity, bits per character
- ROSCOE: Metrics defined by the ROCOE suit.

The evaluation uses that boxed-accuracy is available for the benchmark. The authors compute the correlation of each metric to the boxed accuracy in oder to evaluate their quality. It turns out that teacher forced accuracy had the highest correlation with the boxed-accuracy.

It should be mentioned that similar approaches to generate variants of benchmarks have already been explored with similar results, which is also clear stated by the authors. Although I think that the dataset will be a useful addition to the existing portfolio, especially because the problems are really challenging, I feel that it is not quite closing a unique gap. The evaluation of reasoning metrics is a useful addition. However, it is not quite clear to which extend additional rationales given in the ground truth were tested in these experiments. The authors should be a bit more precise at this point. Overall, I can give a weak recommendation for acceptance.

### Strengths
- New and challenging mathematical problems.
- 52 questions with functional variants.
- Evaluation of many open source and commercial LLMs.
- Evaluation of proxy metrics.

### Weaknesses
 - Variants creation is very simple.

### Questions
- How is testing for equivalent answers combined with the teacher forced metrics?
- Can you describe the setup for the evaluation of the proxy metrics? Was teacher forcing conducted on the boxed answer or on the entire rationale?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new benchmark to evaluate the reasoning capabilities of languages models. The benchmark is generated by taking original Putnam problems from the Putnam Mathematical Competition and adapting them such that they are well-suited for automated verification of proposed solutions to the problem. Furthermore, the problems are parametrized meaning that new problems can be generated continuously generated. These two features set the proposed benchmark apart from existing reasoning benchmarks for LLMs.

### Strengths
The paper tackles an important problem of creating a benchmark for which solutions can be verified in an automated fashion (avoiding expensive human labor) and for which the train set contamination set can be addressed. That is, new problems can be generated ad infinitum simply by changing the parametrization of the problem.

Under the premise that LLMs can never see all possible problems this benchmarks poses an interesting challenge to the reasoning capabilities of LLMs. As such it has the potential to play an important role in the further development of new language models architectures.

### Weaknesses
1) The paper is a little bit short on how new problems are generated.

### Questions
- How important are the two functional changes that can be made to the problems. That is, variable change and constant change. Intuitively one would say constant change. Have you investigated this?

- When would you consider the benchmark to be solved?
- How do you generate/sample new problems? And how to you make sure that you sample problems uniformly form the problem space. It might be that all the problems you sample fall into the same region and that the LLM could pick up on the statistics of this once we have train data contamination. This ties into the question on when you would consider the benchmark solved. As it might be possible that a different sampling strategy might again lead to degrading performance.

- Is it correct to say that is an LLM can reason it will be able to solve to benchmark but the inverse is not true. I.e. if it solves the benchmark it might not perform reasoning.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Authors propose a new benchmark namely Putnam-AXIOM  with 236 problems taken from the famous William Lowell Putnam Mathematical Competition and they also include 52 additional problems with variations. They perform experimentation and explore new metrics and evaluate the performance of SOTA LLMs on their benchmark

### Strengths
1) The proposed benchmark consists of problems from an age old well known competition known for its hardness so these problems can be potentially useful to the community

2) Authors have carefully chosen the problems and have made changes so that LLMs could be evaluated for the problems.

3) Authors have explored various metrics and have done sufficient number of experiments to show that even the largest of LLMs perform rather poorly on their benchmark

4) Authors have included another 52 problems with variations and have shown that performance of LLMs drops siginificantly with even slightest of variations

### Weaknesses
1) Given benchmark is too small, I fully acknowledge the hardness of the problems from Putnam mathematical competition but a dataset of just 236 problems is too small . For instance JEEBench [1] which has problems of same difficulty as the problems present in the proposed dataset has around 515 problems. So I think that there should be atleast 500 problems for the dataset to be more comprehensive or authors can define broad problem categories and can include sufficient number of problems in each category such that the total number of problems in the dataset is more than 500. 

2) Given that the dataset is the primary contribution of the paper, authors should include a discussion about the dataset construction. process, i.e, how the problems were selected, % of problems selected for each category. For example 
a) there are 11 distinct domains that have been defined in the paper, how many problems are present in each of these domains?
b) How were the problems selected for each domain. Was there any criteria that was followed for selecting problems
c) Authors can define relatively define easy, medium and hard categories and further classify the problems based on this

3) Authors could have experimented with other prompting methods apart from few shot prompting such as Progressive Hint Prompting [2], as for each problem the LLM interacts utilises the previously generated answer as a hint which allows the LLM to potentially correct its mistake. Experimenting with such methods would provide crucial insights if the LLMs could correct its mistakes.

### Questions
1) Can you describe potential limitations and future scope for your work 

2) Is the evaluation process automated or does it require a human with considerable amount of mathematical rigour and expertise to sit down and check the responses of LLMs to see if the answers?

### Soundness
3

### Presentation
3

### Contribution
2
