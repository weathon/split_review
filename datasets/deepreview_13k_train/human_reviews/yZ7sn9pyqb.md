# Generative Monoculture in Large Language Models

- Decision: Accept
- Scores: 5, 6, 8, 6, 5

## Abstract
We introduce {\em generative monoculture}, a behavior observed in large language models (LLMs) characterized by a significant narrowing of model output diversity relative to available training data for a given task: for example, generating only positive book reviews for books with a mixed reception. While in some cases, generative monoculture enhances performance (e.g., LLMs more often produce efficient code), the dangers are exacerbated in others (e.g., LLMs refuse to share diverse opinions). As LLMs are increasingly used in high-impact settings such as education and web search, careful maintenance of LLM output diversity is essential to ensure a variety of facts and perspectives are preserved over time. We experimentally demonstrate the prevalence of generative monoculture through analysis of book review and code generation tasks, and find that simple countermeasures such as altering sampling or prompting strategies are insufficient to mitigate the behavior. Moreover, our results suggest that the root causes of generative monoculture are likely embedded within the LLM's alignment processes, suggesting a need for developing fine-tuning paradigms that preserve or promote diversity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the critical issue of "generative monoculture" in large language models (LLMs), where output diversity narrows compared to training data. This is particularly concerning as LLMs are increasingly used in diverse applications like product reviews, sentiment analysis, and scholarly summarization. The study focuses on book reviews and code solutions to demonstrate this phenomenon and tests various mitigation strategies, such as temperature adjustment and prompt engineering, though with limited success.

### Strengths
This paper highlights a critical issue in LLMs around narrowing of output diversity compared to the training data. The paper addresses an important problem esp when LLMs are being increasingly applied in diverse fields such as automated product reviews, sentiment analysis, scholarly paper summarization etc. The paper demonstrates the prevalence of narrowing of output diversity, which they refer to as 'generative monoculture'. They consider book reviews and code solutions as two primary use cases to study the narrowing phenomenon. 
The paper tests various methods to mitigate 'monoculture', including temperature adjustment and prompting strategies. 

The paper provides a well-structured methodology for measuring generative monoculture, including diverse metrics like entropy, mean pairwise similarity and other such metrics. 

The paper discusses the impact of narrowing of output diversity on the societal and code security aspects. These discussions strengthens the paper.

### Weaknesses
While the paper tests various methods to mitigate 'monoculture', including temperature adjustment and prompting strategies, the attempted countermeasures showed limited efficacy in mitigating narrowing of output diversity. This warrants more experimentation and ideation. I would also think use cases/tasks other than book reviews and code generation should be investigated to test the generalizability of the method. Dialogue / chat bot as an application may be an important area to test these methods on. The inability to redefine the alignment process limits the degrees of freedom with which one could operate. I would have liked to see a bit broader scope that covers alignments and comparing the dispersions to alignment data rather than the training data of CPT. 

Rich getting richer / Echo Chamber / Feedback loops are commonly studied phenomenon in recommender system literature. Methods like Bandits and Exploration/Exploitation are commonly used to mitigate the homogeneity of recommended items over time. Authors have an opportunity to connect to this rich work and draw inspiration from this field.

### Questions
I would like authors to comment on feedback loop effects. How do they anticipate monoculture evolving as LLMs are increasingly used to generate their own training data in feedback loops ? Do they think this will further exacerbate the monoculture effect. What strategies and/or guardrails do the authors suggest to mitigate this very long term "model collapse" situation ?

Authors could also further comment on composition of training data. Would increased diversity play a role in mitigating feedback loops and how can LLM training incorporate such diversity. 

Lastly, what role model size plays ? Have authors ablated along model size/complexity dimension ?

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
5

### Summary
The main idea of this paper can be summarized in the following toy example: if 90% of humans say that chocolate is tasty, should language models *always* describe chocolate as tasty, or should they aim to somehow reflect the diversity in human opinions, and occasional refer to chocolate as bad-tasting?

The authors apply this thought experiment to two domains---book reviews and code implementation---and analyze the various ways in which language models enforce a monoculture by failing to model the diversity present in actual human-written content. Adding more entropy into the decoding pipeline helps a bit, but does not meaningfully bring diversity to human levels.

The authors include an interesting discussion of the scenarios in which diversity is desirable--for example, generated book reviews ought to reflect the range of opinions real reader mights have on said books---and the scenarious where diversity might be less important---for example, it is more important for generated code to be correct than to be diverse.

### Strengths
The main idea of this paper is very interesting, and I am glad the authors have done this exploration. The authors have done a good job of discussing nuances around the merits of diversity, and I appreciate their selection of two complementary domains where the value of having diversity is quite different.

### Weaknesses
## Primary weakness - incomplete description of methodology
Unfortunately, it is not possible to assess this paper as it was submitted because crucial information required to understand and reproduce the methodology is purported to be in the appendix, but no appendix was included in the submission. Since the paper is incomplete, there is no choice but to give a score of 1 (strong reject). Despite this, I have tried to leave some constructive feedback below for the authors.

## LLMs for attribute extraction
Line 163 states that "care must be taken to use LLMs for attribute extraction, as they are known to be biased towards their own responses." It seems like this care was taken for the sentiment classifier (the paper notes the classifier's accuracy on SST-2 and it's widespread usage). However, the same care does not seem to have been taken for the "efficiency" attribute, which uses gpt-3.5 to assess runtime efficiency of generated code. It is unclear why a reader should trust that gpt-3.5 is efficient and unbiased at this task. The authors should provide a more rigorous justification for using gpt-3.5 for this task, perhaps by comparing its assessments with actual runtime measurements on a subset of the generated code.

## Takeaway #2
Line 393 states that humans "largely prefer text with positive sentiment." Is this actually true? In a 5 minute literature review, I found several papers such as the two listed below which suggest a much more complex story. Needless to say, statements such as this one should not be made without citation.

Sangwon Park, Juan L. Nicolau. Asymmetric effects of online consumer reviews, ISSN 0160-7383, (https://www.sciencedirect.com/science/article/pii/S0160738314001273).

Lotte M. Willemsen, Peter C. Neijens, Fred Bronner, Jan A. de Ridder. “Highly Recommended!” The Content Characteristics and Perceived Usefulness of Online Consumer Reviews, (https://academic.oup.com/jcmc/article/17/1/19/4067647).

## Takeaway #3
Takeaway #3 claims RLHF hurts diversity more than any of the other factors did. This claim would be much stronger if it had been backed by experiments with more than just one pair of models. I would like to see additional experiments with other model pairs (for example instruction-tuned and RLHF'ed OLMO). Otherwise, a caveat should be added to this claim about the limitation of the result.

## Nitpicks

Here are a few nitpicks (which wouldn't much affect my overall assessment).
1. I am not a fan of the phrase "human-generated." It is extremely atypical to talk about a human generating a book review or generating some code (unless the speaker wants to imply the human is using genAI tools); rather, in common parlance, humans **write** book reviews and **write** code. I suggest replacing instances of "human-generated" with "human-written."
2. I think the paper would be more engaging to read if the description of the attributes of interest was moved before the section on metric calculation (Section 3.3). Section 3.3 felt out of place to read when I didn't yet know what exactly the attributes were for each domain. 
3. Figure 4 has too much information in it, which impeded communication. It would be more effective to break this into multiple figures each with their own caption. In particular, the (a), (b) and (c) in the middle bar graph are especially confusing since (a), (b) and (c) are also used to refer to subfigures. Can you instead put shorthands for the actual names of the models? Also, for the topic model I am confused why the word 'novels' occurs in two groups. 
4. For Figure 5, an easier-to-understand x-axis label for the top-right plot would be "Self-similarity" rather than "Similarity."
5. One additional paper citation for the first paragraph of your Related Work section ("Forcing Diffuse Distributions out of Language Models" https://arxiv.org/abs/2404.10859).
6. Many of the references are formatted incorrectly with missing capitalization in the paper titles.

### Questions
1. What was `{person}` replaced with in the prompt?
2. I do not understand the method used to generate correct solutions for the coding task. Specifically, I did not understand this sentence (line 309): We instantiated this by generating k samples (100 for GPT-4 and 200 for Claude-3), and verifying that at least 20 of them were correct." What did you do if it wasn't the case that 20 were correct? Does your sampling method here ensure then that "correctness" will never fall below 20%?

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper defines and documents the problem of “generative monoculture” in LLMs – that is, the situation in which LLMs produce outputs that are significantly less diverse that what was present in their input training data. The authors focus on diversity over task-specific and intuitive metrics – specifically, the sentiment of book reviews or the algorithms employed in generated code. This is in contrast to measuring over some more systematic but arguably less informative metric such as lexical distributions. The authors find that, across models, the problem of generative monoculture is present and argue that it seems to get worse for models which are “aligned” to human preferences via RLHF.

I really like this paper. It's a nice, intuitive idea that deserves to be highlighted. I think the study was executed well for the most part but would have preferred to see some human evaluations, rather than solely automatic ones. But I think despite this, it warrants publication in the current form.

### Strengths
The paper formalizes the idea of “monoculture”. This idea isn’t wildly novel–it’s intuitive and consistent with other similar ideas such as mode collapse–but to my knowledge there isn’t a clean documentation of it and thus the paper has value in being an official cite for this phenomenon

The authors focus on measuring monoculture using task-specific notions of salient attributes (e.g., sentiment in book reviews, algorithms in code) which differs meaningfully from measures that use e.g., vocabulary of generations. I think this distinction is meaningful as it's a better measure of the type of distribution shift that will matter in practice if GenAI is widely deployed.

### Weaknesses
My primary concern is that the evaluation focuses entirely on automatic metrics. Granted, there are many metrics that the authors use, and they are somewhat diverse. Still, many of the metrics rely on using LLMs themselves (mostly GPT 3.5) to evaluate LLM output. There is something circular (though hard to articulate) about doing this especially given the premise of the paper itself. That is: if we assume LLMs are not good at generating diverse outputs, might we also worry that they aren’t good at recognizing such diversity? Or, said differently, why are we confident that the collapse is due to actual differences in what the LLMs produce, and not differences in what the LLM evaluator can detect?

To address this, I think the paper should include some evaluations which are determined entirely by human judgments. I.e., ask humans to rate the sentiment rather than asking LLMs to do so, ask humans to evaluate the big-O complexity rather than having GPT do it, etc. I would be dramatically more convinced if the conclusions held up under human eval, rather than just automatic eval. But, admittedly, I do expect the result to hold even if all evaluations were switch to human eval.

### Questions
None beyond what was raised in weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the concept of “generative monoculture”, which refers to the phenomena that an LLM's output distribution is less diverse than the original input (data) distribution.
Generative monoculture is investigated on two tasks: generating book reviews, and generating coding solutions, across multiple LLMs.
The monoculture is measured with a number of metrics (depending on the task): distribution of the mean, entropy and standard deviation, and mean pairwise similarity.
The authors find that monoculture exists across the LLMs that are investigated. The authors propose several mitigations, such as changing the sampling parameters, or diversifying the prompts, but this has little impact.

### Strengths
* **Interesting quantification of generic monoculture:** As the authors also mention in their related work section, the idea that current alignment practices hurt diversity is not necessarily new. However, this work presents a new way of measuring this, which gives additional insights in the output of (aligned) LLMs.
* **Considerations (pros and cons) of approach are clearly presented, and largely make sense:** The authors clearly mention their considerations for adopting their chosen methodology, in a space where they sometimes had to make some shortcuts or assumptions. For example regarding their data selection and their used metrics.
* **Authors present negative results, that are insightful:** The presented mitigation strategies do not really help, but this is an insightful finding for the community.

### Weaknesses
 * **Investigated datasets are not very large.** This holds especially for the code solutions, where the data is limited to a subset of 100 easy solutions. Although this gives a first impression, I wonder how results hold over larger data samples, and especially when harder problems are included as well. The limited dataset size makes it difficult to generalize the findings to more complex scenarios. For example, the observed monoculture might be more or less pronounced with a larger and more diverse set of coding problems, potentially including those that require more intricate algorithms or data structures. The restriction to 'easy' problems also raises concerns about the practical relevance of the findings, as real-world coding tasks often involve a wide range of difficulties.
* **Coding solutions are checked by GPT-3.5.** The authors give some details in the appendix of the autojudge, but it is not entirely clear to me how quality is ensured. After all, GPT-3.5 needs to check the results of a stronger model (GPT-4) and, as the authors also mention elsewhere in the paper, LLMs tend to be biased towards their own responses. The reliance on GPT-3.5 for evaluating the correctness and other attributes of code generated by more powerful models like GPT-4 and Claude-3 introduces a potential bias. The evaluation might be skewed towards solutions that GPT-3.5 is more likely to understand or favor, rather than reflecting the true quality of the generated code. This is especially concerning given the known limitations of LLMs in accurately assessing code correctness and efficiency, and the potential for the evaluation model to be influenced by its own training data and biases.

### Questions
* Can the authors explain what they mean on line 309: “We instantiated this by generating k samples [...], and verifying that at least 20 of them were correct.” Does this mean 20 samples were checked, and 80 were not? 
* Can the authors provide a reference that shows that humans prefer positive reviews, to support take-away 2?

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
The paper investigates generative monoculture in LLMs, defined as the reduction in diversity from training data to the model’s outputs. It examines this phenomenon in two tasks: sentiment of book reviews and code generation. The paper found consistent monoculture in all experiments.

### Strengths
Generative monoculture is a subtle phenomenon that may not be immediately noticeable to users but can have a lasting impact on society, making it an important area of study. The paper is well-written and clearly presented.

### Weaknesses
W1: One major risk in this study is that measuring generative monoculture with “a source dataset that is likely to have been used in training the LLM we wish to investigate” (line 128) could introduce substantial inaccuracies. This approach risks significant biases, undermining the validity of the measurements. I will elaborate below and hope the authors could discuss these risks and present evidence to support validity of their approach.

W1-1: First, the selected source data may not actually be part of the LLM’s training data. The authors do not provide any evidence that the selected GoodReads dataset is actually included in the training data of the LLMs under investigation. This lack of evidence is a major concern, as it undermines the entire premise of the study. Without knowing if the source data is part of the training set, the measured distributions may not reflect the true training distribution at all.

W1-2: Even if the selected source dataset is indeed in the training data, it may not represent the full range of relevant training data. For instance, other sources or non-English reviews of the same books could dominate the distribution from training data, meaning that the measured distribution may not reflect the true distribution of the training data at all. This concern is especially relevant since the study uses relatively small datasets (742 books with 10 reviews per book for book reviews and 100 coding questions with 20 correct solutions each for code).

W1-3: Additionally, the filtering of the source dataset introduces biases. The authors mention in Appendix B2 that book reviews are filtered to be between 300-700 words. Filtering by length could affect the sentiment distribution, potentially skewing the results. The authors should investigate whether this filtering introduces a bias in the sentiment distribution.

W2: Could the authors clarify why they filter out low-quality (generated) book reviews by examining perplexity? While low-quality reviews may seem less helpful to users, excluding them might introduce bias in the sentiment distribution of LLM-generated book reviews. I recommend testing whether this filtering step influences the measured sentiment distribution, although it might be preferable to retain these low-quality reviews to avoid introducing additional bias.

W3: To strengthen the study’s validity, I suggest measuring generative monoculture in a more controlled environment, where the training data is known and the training distribution can be accurately measured. Without certainty that the source dataset is part of the training data, all findings are at risk of being unreliable. The authors should consider using a model where the training data is fully known, such as the OLMo model, to provide a more reliable measurement of generative monoculture.

W4: In Line 317, the efficiency of LLM generated code is measured by ``prompt GPT-3.5 to infer the big O time and space complexity’’. Please establish the reliability of this LLM evaluation. The authors should provide evidence that the LLM is accurately evaluating the time and space complexity of the generated code.

W5: In line 328, Code Summary (categorical) is measured by “prompt GPT-3.5 to assign tags to a code segment by providing it a set of tags to choose from”. Please establish the reliability of this LLM evaluation. The authors should validate the accuracy of the LLM's tag assignments.

W6: In Figure 4 (d), decay T p = 1.0 seems to have higher entropy, therefore more diverse, than source distribution. Could the authors discuss this, as it disagrees with the statement in line 379 “there exists significant narrowing from the source to generation distribution in all attributes considered for both scenarios”? This discrepancy needs to be addressed to ensure the consistency of the paper's claims.

### Questions
Q1: Could the authors explain how the plagiarism score is computed in Figure 5 (b)? It seems is not mentioned in paper.

### Soundness
2

### Presentation
4

### Contribution
2
