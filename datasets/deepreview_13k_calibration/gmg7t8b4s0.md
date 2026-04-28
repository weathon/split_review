# Can LLMs Keep a Secret? Testing  Privacy  Implications of Language Models  via Contextual Integrity Theory

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 3, 8, 6

## Abstract
Existing efforts on quantifying privacy implications for large language models (LLMs) solely focus on measuring leakage of training data.
In this work, we shed light on the often-overlooked interactive settings where an LLM receives information from multiple sources at inference time and generates an output to be shared with other entities, creating the potential of exposing sensitive input data in inappropriate contexts.
In these scenarios, humans naturally uphold privacy by choosing whether or not to disclose information depending on the context.
We ask the question ``\textit{Can LLMs demonstrate an equivalent discernment and reasoning capability when considering privacy in context?}''
We propose \benchmark, a benchmark grounded in the theory of contextual integrity and designed to identify critical weaknesses in the privacy reasoning capabilities of instruction-tuned LLMs. 
\benchmark consists of four tiers, gradually increasing in complexity, with the final tier evaluating contextual privacy reasoning and theory of mind capabilities.
Our experiments show that even commercial models such as GPT-4 and ChatGPT reveal private information in contexts that humans would not, 39\% and 57\% of the time, respectively, highlighting the urgent need for a new direction of privacy-preserving approaches as we demonstrate a larger underlying problem stemmed in the models' lack of reasoning capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an official benchmark to evaluate the privacy reasoning capabilities of LLMs. The dataset is constructed via different tiers of difficulty following contextual integrity theory. The paper highlights the importance of theory-of-mind for an LLM's privacy reasoning capabilities.

### Strengths
- strong foundation of approach in contextual theory
- thorough experiments
- clear presentation
- human preference collection

### Weaknesses
 - no discussion of limitations of study (i.e. small samples sizes), and how the performance metrics might be misleading

### Questions
1. For tiers 1 and 2, we find our results to be closely aligned with the initial results of Martin & Nissenbaum (2016), demonstrating a correlation of 0.85, overall --> correlation between what?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces CONFAIDE, a benchmark based on contextual integrity theory that aims to pinpoint fundamental gaps in the privacy analysis abilities of LLMs fine-tuned through instructions. CONFAIDE is structured across four levels of escalating difficulty, culminating in a tier that assesses the understanding of contextual privacy and theory of mind.

### Strengths
Pros:
1. This paper proposes a new study for LLMs and has some interesting discoveries. Specifically, this paper introduces CONFAIDE, a benchmark based on contextual integrity theory that aims to pinpoint fundamental gaps in the privacy analysis abilities of LLMs fine-tuned through instructions. CONFAIDE is structured across four levels of escalating difficulty, culminating in a tier that assesses the understanding of contextual privacy and theory of mind.
2. Extensive experiments are conducted to support the discoveries.

### Weaknesses
Cons:
1. The “Contextual Integrity” concept cannot be explained by the given example: "For example, if your healthcare provider shares your medical history, which contains sensitive health details, with an insurance company for marketing purposes, it would be a violation of contextual integrity. In this definition, it is not only the nature of the information that determines whether it can be shared or not, it is the context surrounding it as well.” "medical history” itself is private information in nature regardless of the people to share. It is unclear that “it is not only the nature of the information that determines whether it can be shared or not”. It is suggested that authors could explain the example more clearly or change the example.
2. Some references are missing. For example, The reference for "theory-of-mind (i.e., tracking mental states of others)”.
3. The experiment design is questionable. The authors find that “GPT-4 and ChatGPT reveal secrets 22% and 93% of the time in Tier 3, and flow information to inappropriate actors 39% and 57% of the time in Tier 4, even though they are directly instructed to preserve privacy.”
    1. a) First, how to ensure that LLMs really understand the concept of “privacy”? Does LLMs understand the concept of “privacy” in the same way of humans? Does “privacy” indicate “cannot be shared” for LLMs in nature?
    2. b) Second, do the LLMs really understand the experiment setting? How to ensure LLMs really understand the experiment setting? How to ensure that the LLMs’ responses are meaningful? Although this paper has some brief discussion: “(3) Understanding private information sharing: We evaluate the model whether it understands the concept of shared private information. Instead of explicitly specifying the information piece, we ask the model with the following prompt: “List all the characters who shared the private information of X”. Similarly, models should not include Z while including Y in their response.”  It is still not very clear. More detailed explanations are desired.
4. It is not well explained what causes the bad performance of LLMs. Does it mean that LLMs do not have theory-of-mind? Or LLMs potentially just do not understand the setting well?
5. The significance of this study is not very clear. It is not convinced that "contextual privacy” is a very important problem for LLMs because this paper does not show convincing real-world examples to illustrate the importance of LLMs' "contextual privacy” property. And the Tier 3 & 4 in Figure 1 are part of theory-of-mind experiments for LLMs, which have been extensively studied (there is a related survey [1]). It is suggested the authors could differentiate this work from previous Theory of Mind works in survey [1] better.
6. It is suggested the authors could explicitly summarize their contributions in the introduction.

### Questions
See weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper develops a benchmark to evaluate the ability of LLMs to maintain privacy of prompt information in different contexts. The benchmark quantifies the privacy of LLMs as the leakage not of the training data as most of the works on the topic, but rather of private information contained in the prompts which should not be disclosed in specific contexts. The benchmark draws heavily on taxonomy and concepts such as contextual integrity of Nissenbaum (2004): for the LLM to appropriately discern what information to disclose, it needs to consider various contextual factors such as the type of information, the parties concerned and their relationships. The benchmark consists of four tasks of increasing complexity, ranging from LLMs having to evaluate whether a piece of information is sensitive to the more complex task of generating a meeting summary while avoiding to disclose private information discussed before some of the attendees joined the meeting. The authors evaluate a range of LLMs, including open-source and commercial ones, on this benchmark using metrics such as the correlation between privacy assessment of LLMs and human annotators. Results suggest that LLMs often reveal private information in contexts where humans would not.

### Strengths
- 1) The contribution is significant and original. This is an interdisciplinary paper drawing on the contextual integrity theory of Nissenbaum (2004) and follow-up work by Martin and Nissenbaum (2016) to design a benchmark for evaluating the privacy capabilities of LLMs. The paper adds a much needed component to the field: even as an LLM is privacy-preserving in the traditional sense (leakage of information about the training dataset), it might lack the reasoning capabilities to judge whether or not to disclose private information in its prompts.
- 2) Practically useful contribution: the benchmark can be used by LLM developers to assess the extent to which their model preserves privacy of prompt information.
- 3) Extensive empirical evaluation: several LLMs are evaluated against the benchmark.

### Weaknesses
 - 1) Some of the metric definitions seem to be lacking in the main paper, making results hard to interpret, e.g., the sensitivity score in Table 2, the metric of Fig. 2 isn’t named, Table 4 includes five undefined metrics. This is all the more important for figures such as Fig. 2 which are very complex and seem to be lacking a clear trend. 
- 2) No error rate is given for results derived from automated parsing of LLM responses. More specifically, automated methods like string matching or LLM interpretation of results may incorrectly determine whether a secret was leaked. What is the error rate of the automated method for parsing of LLM responses? This can be estimated by randomly sampling some of the responses and checking how often the automated method orrectly predicts whether the secret was leaked. This should give some notion of confidence in the results.

### Questions
- 1) Since part of the benchmark is generated by LLMs (e.g., Tier 2 and 4 tasks use GPT-4) and then GPT-4 is evaluated using the benchmark, can this bias the findings on GPT-4? E.g., is it possible for GPT-4 to be more “familiar” with the wording produced by itself and somehow be at an advantage compared to the other models? The use of GPT-4 for generating the tasks should be motivated and the limitations of this be acknowledged.
- 2) The limitations stemming from using human annotators of Mechanical Turk for deciding what is private and what isn’t aren't acknowledged. Do the authors know the background of the annotators and do they believe this may bias the results in specific ways?

Minor (suggestions for improvement):
- 3) Please include statistics of the benchmark such as how many examples are generated for each task, how many of them are human-generated vs LLM-generated.
- 4) To facilitate the interpretation of results, I suggest to include more context about LLMs being evaluated. Some statements are made such as “models that have undergone heavy RLHF training and instruction tuning (e.g. GPT-4 and ChatGPT)” and “Overall, we find the leakage is alarmingly high for the open source models, and even for ChatGPT” without it being clear which LLMs are commercial, open-source, and trained using RLHF.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper first introduces the concept of contextual privacy into LLM study. The authors propose 4 tiers of contextual privacy and a corresponding benchmark dataset, and find that existing LLMs cannot satisfy the requirement of contextual privacy in a large portion of scnearios.

### Strengths
1. The paper first introduces the concept of contextual privacy into LLM study
2. The paper proposes the first contextual privacy benchmark for evaluating the ability to conform with contextual privacy.

### Weaknesses
The concept of contextual privacy, as the name indicates, heavily depends on the context. The benchmark can only capture a small portion of possible contexts so it's not very scalable.

### Questions
Is there a way to construct scalable benchmark?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
