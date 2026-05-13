# Fool Your Large (Vision and) Language Models with Embarrassingly Simple Permutations

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Large language and vision-language models are rapidly being deployed in practice thanks to their impressive capabilities in instruction following, in-context learning, and so on. This raises an urgent need to carefully analyse their robustness so that stakeholders can understand if and when such models are trustworthy enough to be relied upon in any given application. 
In this paper, we highlight a specific vulnerability in popular models, namely permutation sensitivity in multiple-choice question answering (MCQA). 
Specifically, we show empirically that popular models are vulnerable to adversarial permutation in answer sets for multiple-choice prompting, which is surprising as models should ideally be as invariant to prompt permutation as humans are.  
These vulnerabilities persist across various model sizes, and exist in very recent language and vision-language models. %

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper reveals an interesting phenomenon of existing LLM and VLLMs: they are vulnerable to adversarial permutation in answer sets for multiple-choice prompting, which is surprising as models should ideally be as invariant to prompt permutation as humans are.

### Strengths
1. This paper reveals an interesting phenomenon:  they are vulnerable to adversarial permutation in answer sets for multiple-choice prompting, which they should not be ideally.

2. Experiments are conducted across different multiple LLM / VLLMs, demonstraing the universality of the phenomenon.

### Weaknesses
While the finding is interesting, I wonder if authors could provide any intuitive explanations on the observation? Position bias (Zheng et al., 2023a) may not be able to fully explain this phenomenon, but it can be potentially one of the reasons why they are vulnerable to the adversarial permutation in answer sets from my understanding. I am willing to see more analysis on the potential causes of this observation. Can the explanations on similar problems in other tasks besides MCQA apply to this case？Authors may put more efforts on it.

### Questions
Please refer to Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper examines permutation sensitivity in MCQA for generative language models and vision-language models. They show that a wide range of models display severe permutation sensitivity in a variety of MCQA benchmarks, and show that existing mitigation strategies do not solve permutation sensitivity.

### Strengths
A large number of language models and vision language models are used in the experiments. The datasets chosen are diverse and there are enough datasets to draw strong conclusions. 

There is concurrent work in the area (pointed out by the authors themselves), but the broadness of the experimental evaluation is original. While limited in scope to MCQA, it is significant, as it may point to underlying problems in LLM reasoning that cannot be easily fixed.

### Weaknesses
I think it's overclaiming to call this an "adversarial" attack. Permuting the choices is done as a matter of course in evaluation (see Section 4.1 in [1]). 

Additionally, I think important context is missing. We know parameters like the temperature and the sampling strategy have a significant effect on output. But I don't see these numbers reported. Do the numbers change if we reduce / increase the temperature?

There's no discussion on prompting. Does providing in-context examples effect permutation sensitivity? In-context examples for MCQA should always be available. They also provide a convenient way to alter the posterior distribution (for example, you could set the answer to always be the last answer in the in-context examples; would the positional bias then change?)

Also, no information is reported on the model perplexity / confidence during permutation. It may be possible that certain permutations have much lower perplexity / higher confidence, and hence the model's answer on those is more trustworthy. So in practice, we might evaluate the model on all the permutations, then select the model's most confident answer. Of course, if we can do this, it is better to avoid MCQA entirely and have the model assess the answers one-by-one.

### Questions
Please see the weaknesses section. I am willing to raise my rating if the weaknesses are addressed.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper aims at the vulnerabilities of large language and vision-language models, specifically concerning permutations in multiple-choice question answering (MCQA). The authors conduct experiments that reveal performance degradation when models are exposed to permutation-based attacks, even though these models have shown capabilities in various tasks. The findings underscore the need for a deeper analysis of robustness before deploying such models in real-world applications.

### Strengths
The paper addresses the robustness of widely used models, a pertinent topic given the real-world deployment of these models.

### Weaknesses
1. The methodology's depth and novelty are not entirely clear. More analysis could be provided on how natural variations in the way are ordered may impact models.

2. While the paper focuses on permutation-based vulnerabilities, it might benefit from a broader discussion on other potential vulnerabilities or comparisons to other attack methods.

3. The experiments provided are on a specific dataset. It would be beneficial to see how the models fare on diverse datasets to ensure the findings, which are not specific to one dataset's characteristics.

### Questions
See the above weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores and experiments with the permutation attack on current large vision-language models for multiple-choice question answering (MCQA). The authors show that these models are susceptible to adversarial permutations in the answer sets for multiple-choice prompts. This is concerning because the models should be invariant to the permutations.

### Strengths
- Well written
- Interesting and important area of work that many are overlooking 
- An important area to look at specially for industry wide adaptation of large vision-language models. 
- Experiments are easy to understand

### Weaknesses
1. I don't see any related work section. That would have made the work more sound
2. The comparison tables on LLMs seems to be inconsistent. For example Table 3 has GPT-3.5 turbo but Table 5, 6 (that are also comparison on LLM) do not have GPT-3.5 turbo
3. On the experimentation section, it would be good if the authors described some more details. For example - did they used model APIs or model weight's for testing? This would give us an idea on the consistency of experiments

### Questions
1. In Table 3 for GPT3.5 turbo, how did the authors do the testing? Is it using OpenAI API?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
