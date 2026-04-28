# Can LLM-Generated Misinformation Be Detected?

- Decision: Accept
- Avg Score: 4.75
- Scores: 3, 3, 8, 5

## Abstract
The advent of Large Language Models (LLMs) has made a transformative impact. However, the potential that LLMs such as ChatGPT can be exploited to generate misinformation has posed a serious concern to online safety and public trust. A fundamental research question is: \textit{will LLM-generated misinformation cause more harm than human-written misinformation?} We propose to tackle this question from the perspective of \textit{\textbf{detection difficulty}}. We first build a taxonomy of LLM-generated misinformation. Then we categorize and validate the potential real-world methods for generating misinformation with LLMs. Then, through extensive empirical investigation, we discover that LLM-generated misinformation \textit{\textbf{can be harder}} to detect for \textit{humans} and \textit{detectors} compared to human-written misinformation with the same semantics, which suggests it can have more deceptive styles and potentially cause more harm. We also discuss the implications of our discovery on combating misinformation in the age of LLMs and the countermeasures.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper primarily discusses the ways in which LLMs can generate or can be leveraged to generate misinformation. It discusses its implications via various means of generation (established through an LLM generated misinformation taxonomy) and how easy/difficult it is detect this misinformation when compared to human-written misinformation.

The paper notes that LLM generated misinformation is harder to detect and can potentially cause more harm, through human evaluations and LLM based detection experiments.

### Strengths
The paper does a good job at describing the problem statement and their contributions. It's a good survey on the related techniques within this space.
- The misinformation taxonomy and the generation strategies of hallucination, Arbitrary Misinformation and Controllable Misinformation generation are interesting to note
- Utilizing CoT and non CoT prompting to study LLM based misinformation detection is interesting

Overall the paper is a comprehensive study on LLM generated misinformation and related techniques.

### Weaknesses
The paper lacks a review or comparison with pre-LLM era misinformation or fake news detection strategies. There are techniques within fact-finding and source-attribution space which can be leveraged to detect misinformation and those haven't been discussed.

The paper often uses Appendix sections to support the claims made which makes it less readable and less self-contained.

The paper establishes what 'detectors' are, rather late.

Overall the paper is a comprehensive study on LLM generated misinformation and related techniques, but found it to be lacking in making a significant/original innovation.

Minor:
spelling mistake in word 'Appendx' in section 4

### Questions
"against HC method" in section 3, page 4, is it supposed to be HG?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Summary: Large Language Models (LLMs) have become increasingly powerful and are capable of generating human-like text. This capability has raised concerns that LLMs could be used to generate misinformation. The authors investigate the difficulty of detecting LLM-generated misinformation compared with human-written misinformation. The authors find that LLM-generated misinformation can be harder to detect for both humans and detectors.

### Strengths
The paper is a well-written and informative contribution to the field of misinformation research. It provides important insights into the potential for LLMs to be used to generate deceptive and harmful misinformation.
- It is one of the first papers to systematically investigate the detectability of LLM-generated misinformation.
- It creates a taxonomy and identifies three different types of LLM-generated misinformation: Hallucinated News Generation, Totally Arbitrary Generation, and Partially Arbitrary Generation.
- It evaluates the detectability of different types of LLM-generated misinformation by humans.

### Weaknesses
Cencern1: The study is relatively small number of evaluators and only evaluates a limited number of LLM-generated news items. This means that the findings of the study may not be generalizable to all LLM-generated news items.

Concern 2: The study does not evaluate the effectiveness of different detection methods for LLM-generated misinformation. This means that it is not clear how well existing detection methods would perform at detecting the LLM-generated news items used in the study.

### Questions
Cencern1: The study is relatively small and only evaluates a limited number of LLM-generated news items. This means that the findings of the study may not be generalizable to all LLM-generated news items.

Concern 2: The study does not evaluate the effectiveness of different detection methods for LLM-generated misinformation. This means that it is not clear how well existing detection methods would perform at detecting the LLM-generated news items used in the study.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies a problem with high significance and urgency: detection of LLM-generated misinformation. More specifically, the development of advanced LLM make it easy for misinformation creators to efficiently generate misinformation. A critical question is: is the LLM-generated misinformation detectable? To understand this question better, the authors built up a LLM-generated misinformation dataset and then compare its detection difficulty with human-written misinformation for both human verifiers and machine learning models. Extensive experiments suggested that compared to human-written misinformation, LLM-generated misinformation is more deceptive and potentially more harmful.

### Strengths
1. Significance of the research question: AI-generated misinformation is a very critical problem for the development of LLM. The development of RLHF-based LLM can make the misinformation creators easily generate misinformation without any preliminary knowledge about deep learning. We urgently needed exploration on the topic. 

2. Contribution to the community: This paper discuss the problem in a great details and can provide us with good resources (dataset and prompts) to study this problem.

3. Experiment details are discussed in details.

### Weaknesses
1. The dataset seems to be not very large. I understand that for evaluating human detection difficulty, we can not use too large dataset. But the authors can enlarge the dataset for evaluation of machine learning model.

2. For detector difficulty, the authors only discussed the zero-shot detection of generative LLMs. The results on other kinds of models (i.e. in-context-learning boosted LLMs, soft-prompt based LLMs, and encoder-based Large models like BERT and its variants) are not discussed.

3. Dataset is not opensourced. Actually, the data can be opensourced anonymously on GitHub.

### Questions
1. Will the datset be opensourced once the paper is accepted?

2. Is it possible to generate more data for detection evaluation?

3. Will few-shot learning improve the performance of the detection?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates the possibility of the generation of misinformation from LLMs, whether human evaluators can identify LLM-generated misinformation, and assesses the performance of automated detectors in identifying human vs. LLM-generated misinformation. Among other things, the paper finds that LLM-generated misinformation is harder to detect for humans compared to human-written misinformation and that LLM-generated misinformation is harder to detect for automated methods.

### Strengths
I would like to thank and applaud the authors for working on this very important and timely problem; this research has the potential to have a big impact on the research community and help mitigate emerging problems like the spread of misinformation online. I liked that the paper creates a taxonomy of LLM-generated misinformation and then goes further and investigates the generation of LLM misinformation across types, sources, and domains. Also, an important strength of the paper is that the paper’s evaluation considers many state-of-the-art LLMs used for in-context learning purposes to solve the problem of misinformation detection.

### Weaknesses
While I believe that this study is an important research effort, I have some concerns with the way that the paper conducts the experiments and the interpretation of the results. Below, I provide more details on my main concerns with the paper.

First, the paper’s evaluation is done on a very small scale, particularly 100 pieces of news, and leveraging only 10 human evaluators to assess the performance of humans and compare it with various LLM-based automated detectors. Due to this, I am wondering how robust and generalizable the presented results are. At the same time, the paper does not discuss whether the presented results and differences between human-written and LLM-generated misinformation are statistically significant. That is, the paper simply presents the results and differences without providing any additional context of how statistically significant the results. I suggest to the authors to consider expanding their evaluation and discussing the statistical significance of these results.

Second, the paper lacks important details on how the ten human evaluators are selected. Do these evaluators have previous experience with annotating piece of information as misinformation or not? Do you take any steps to ensure that the annotations are of high quality and that the annotators did not use LLM to solve the task? For instance, the paper by Veselovsky et al. [1] demonstrated that crowd workers are using LLMs to solve tasks, so I am wondering if the paper took any steps to ensure that the human evaluators solved the task on their own. I think this is a crucial part of the paper as many results rely on the quality of these annotations and more details can shed light into these concerns. Finally, it is unclear to me why the paper studies the performance of the human evaluations on a per evaluator basis rather than taking the majority agreement of the evaluators per piece of information and then reporting the results on aggregate. Also, I suggest to the authors to include the inter-annotator agreement of the evaluators so that we can assess how difficult was the presented task for them. 

Finally, from the paper, it’s unclear how the attack rates in Section 3 are calculated. Are these based on manual evaluations from the authors? I suggest to the authors to provide more details on how the annotated the generated pieces of information, how many people annotated each piece, etc.

### Questions
1. How are the 10 human evaluators selected, and did you take any steps to ensure that their annotations are of high quality? Also, did you take any steps to assess if the annotators used LLMs to solve the task (see paper by Veselovsky et al., 2023)
2. Are the presented results and differences between human and LLM-misinformation statistically significant?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
