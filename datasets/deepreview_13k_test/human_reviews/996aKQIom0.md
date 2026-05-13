# PingPong: A Benchmark for Role-Playing Language Models with User Emulation and Multi-Model Evaluation

- Decision: Reject
- Scores: 3, 5, 3, 3, 3, 6

## Abstract
We introduce a novel benchmark for evaluating the role-playing capabilities of language models. Our approach leverages language models themselves to emulate users in dynamic, multi-turn conversations and to assess the resulting dialogues. The framework consists of three main components: a player model assuming a specific character role, an interrogator model simulating user behavior, and a judge model evaluating conversation quality. We conducted experiments comparing automated evaluations with human annotations to validate our approach, demonstrating strong correlations across multiple criteria. This work provides a foundation for a robust and dynamic evaluation of model capabilities in interactive scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces PingPong a benchmark that aims to simulate and assess multi-turn interactions using three components Player, Interrogator, and Judge models. The authors have focused on role-playing models for entertainment purposes. They do this in two versions: In the first version the judge and the interrogator are played by a single model while in the second version these roles are separated in two different models. The player is provided a character card defining its role while the interrogator has the details of the scenario. The judge is supposed to score each turn based on 3 criteria: entertainment, character consistency and language fluency.

### Strengths
The authors have focused on role-playing models tailored for entertainment, which is an underrepresented area in benchmarks and that too in multi-turn settings.

### Weaknesses
I have many concerns with this paper. A Judge which is itself an LLM with inherent biases is assessing a highly subjective quality like “Entertainment”. Measuring entertainment is not straightforward and can have varying stylistic and cultural traits. Evaluating that without a human reference data compounds this issue and thus the reliability of the judge can’t be established. Similar concerns with character consistency.

In role-playing, each turn can be dependent on prior turns, which can’t be fully captured by scoring turns in isolation. While scoring each turn provides a granular view of performance, it may miss the overarching coherence of the character and storyline across multiple turns. The evaluation also overlooks user-centric metrics like engagement, user satisfaction, ability to sustain engagement over extended interactions which are important for role-playing. The paper’s current scoring approach does not seem to assess these aspects. Also these criteria can vary in priority and a weighted scheme would make more sense where entertainment is weighted higher than other criteria, from a role-playing perspective, users might value character consistency over fluency, or vice versa.

Although authors have mentioned these in limitations but I would highlight that with only 64 conversations per model, the benchmark’s robustness is very limited, While the authors report a positive correlation with human annotations, they used only a single human annotator, which is a significant limitation. Having a single annotator introduces subjective biases to a subjective dimension like entertainment.

### Questions
My suggestions would be to experiment with weighting or adjusting criteria based on specific user feedback, perhaps allowing users to prioritize different aspects like consistency or entertainment. Also, Increasing the diversity of human annotations should help validate the scores against a more reliable ground truth of human judgment.

### Soundness
2

### Presentation
2

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
This work presents a novel benchmark for assessing language models' role-playing abilities in dynamic, multi-turn dialogues. The evaluation framework includes three components: a player model embodying a specific character, an interrogator model simulating user interactions, and a judge model assessing dialogue quality. Experiments showed strong correlations between automated and human evaluations, supporting the framework's reliability. This benchmark lays the groundwork for robust and adaptive evaluations of model performance in interactive contexts.

### Strengths
This work introduces the concept of an "Interrogator," which serves as a user simulator. Unlike traditional static evaluation, dynamic evaluation—incorporating both the user simulator and AI character—offers a more realistic assessment. This approach holds significant value.

### Weaknesses
While this work has a strong starting point, it lacks rigorous experimental validation in several areas. For example:

1. The authors have not adequately addressed the consistency between “Interrogators” and real-world human users. In practical scenarios, users typically employ informal language with various omissions and slang. Additionally, their motivations for engaging with a character are often unpredictable. Thus, a deeper examination of the alignment between “Interrogators” and human users would significantly enhance the quality of this work.

2. Point-wise evaluations by Large Language Models often diverge from human annotators’ assessments, especially in subjective tasks. Furthermore, the generated scores tend to be biased towards specific values, resulting in a leaderboard that lacks differentiation.

### Questions
Typos in Table 1  and Table 2: Enteraining -> Entertaining

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work examines the role-playing capabilities of language models with a benchmark that uses LMs to emulate specified characters and users in multi-turn conversations and also judge these conversations. The authors validate this framework by comparing the automated evaluations with human annotations and showing strong correlations across various criteria. The authors show that ensembling model judgements lead to better correlation with human judgement on the criteria of fluency, character consistency, and entertainment.

### Strengths
- This work addresses issues with prior work that examines role-playing capabilities with either single-turn interactions or using static datasets that may have issues with data contamination.

### Weaknesses
- There are no comparisons to other evaluation benchmarks other than creative writing, which is an odd choice given the mention of other role-playing benchmarks with single-turn evaluations, and therefore the value added by this benchmark is not substantiated by previous work on role-playing evaluation and results. In addition, results are descriptive, rather than analytical. It is unclear whether any of the results from this benchmark is interesting or surprising. 
- There is no explanation on what makes this dataset dynamic while previous efforts are considered static. 
- While correlation using a multi-model setup shows higher correlation with human annotations, the human annotations were done by a single person and the margin with a single-model setup is not big enough to motivate the use of multiple models given that it would incur higher costs. 
- The paper is written poorly. Please refer to details in the Questions section.

### Questions
- lines 30-32: what are these other applications?
- lines 33-34: why do you believe so? What are the alternatives that were studied before?
- lines 35-36: provide citations for these popular benchmarks. It shouldn't be as thorough as the related work section, but each claim should be backed by a citation or by empirical results from the current paper.
- Introduction: 'novelty' is repeatedly mentioned, but it is unclear what the novelty is. How is your LLM-as-a-judge different from prior work?
- line 46: what is meant by dynamic? What is meant by data contamination in this context? Give a brief summary in what your methodology is for generating dynamic questions as opposed to static ones.
- End of introduction: give a brief summary of what the novel and interesting findings are that were enabled by this proposed benchmark
- Related work: it has too many subsections, which makes this section  feel disconnected. If role-playing is the most important aspect of this work, I'd suggest starting with them and how the other aspects (static vs dynamic, multi-turn, data contamination, multi-model judges) are related to a more realistic evaluation of role-playing capabilities.
- What is meant by asymmetrical in line 136? Do you mean that the player only gets the character description while the interrogator only gets the situation information? Are there any concerns about the base persona of the interrogator being a confounding factor for the player's ability to role-play?
- What's the meaning of "separated soles" in line 166?
- What were the limitations of the combined approach in line 168? I see that this is explained later. I would suggest rewording this sentence so that the key issues of the combined approach is introduced first or mentioned even in section 3.3 as to motivate section 3.4.
- How important is it to introduce version 1 (section 3.3)? This feels less important and thus can be deferred to the appendix.
- line 192: what are the 16 language models?
- line 194: using a single annotator is not sufficient for measuring reliable correlation with a language model's scores because it's not representative of human judgement.
- What's the human performance on this role-playing task?
- Apart from the quantitative results of the leaderboard, what are the interesting findings that are revealed through this benchmark that was not known before? Are they different from the results on static, single-turn benchmarks?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a "benchmark" for role playing dialog. It involves 3 LLM's playing different roles
1. a user/interogator LLM which talks to 
2. a system LLM playing a character role, and
3. a Judge LLM which looks at the resulting conversation between 1 and 2, and grades how well 2 has played the assigned character role

The paper uses state-of-the art LLMs for these, releases some code. The contribution is minor however for reasons given below.

### Strengths
The contributed code may provide a framework for some members of the community to experiment with. However there are no scientific questions posed in this paper, it's a limited engineering style contribution with observations -- such as separating of judge and user LLM, which was well motivated and made sense -- on how to construct such a simulation environment.

### Weaknesses
There is very limited novelty in this submission. This is a basic simulation system these days, and multiple other papers have performed similar setups with LLM's playing conversation roles. Even if application to a role playing character is new, it's a minor increment.  

Aside from that, there are a very small number of conversations generated here (60), and of greater concern they are evaluated only by 1 human grader, who has apparently limited English abilities (mentioned in results section) which limits them from noticing any nuances in the dialog.

### Questions
NA

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a multi-turn, dynamic and multimodel benchmark for assessing the role-playing abilities of language models. Their framework depends on three components: player, interrogator and judge. The authors compare the automatic vs human scores for Russian and English. Additionally, they compare their results with a Creative Writing benchmark.

### Strengths
* The community has put much effort into similar goals: automatic evaluation and setting benchmarks.
* This benchmark can be the seed for further investigation of role-playing capabilities.
* The benchmark is automatic and could be easily reproduced.

### Weaknesses
* There was only one annotator. 
* The relationship between the annotator and the authors was not disclosed.
* The instructions given to the annotator were not disclosed. 
* The elements of the evaluation (e.g., annotation aspects and their Likert scale) were not discussed. 
* Comparison between v1 and v2 is not thorough since only one model was used on v2. 
* The motivation for comparing with creative writing is not clear.

### Questions
* Can you describe the role of the human annotator? Which profile did he have (author, student, extern), and which instructions was he/she given? How much was he/she paid? How long did it take to annotate? 
* What was the motivation for using the creative writing benchmark?
* Why are the scores too close to each other? Can this be improved so the differences among LLMs can be better quantified?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a benchmark to evaluate language models' role-playing abilities in dynamic, multi-turn conversations. It features a unique three-part framework: a player (the language model in a character role), an interrogator (emulating user interactions), and a judge (assessing dialogue quality). A multi-model evaluation strategy uses various language models as judges to reduce bias, aligning well with human evaluations.

### Strengths
By using dynamic, multi-turn interactions that mimic the unpredictable flow of real conversations, the benchmark does a great job of capturing authentic role-playing scenarios.

The benchmark supports both English and Russian for now, but its flexible setup suggests it could easily expand to other languages. This forward-thinking design could make it a valuable tool for building models that are more culturally and linguistically inclusive.

A standout feature of this benchmark is its use of language models not only as players but also as simulated users and judges. This design boosts scalability and provides a consistent, less biased way to evaluate huge datasets, making it possible to explore different role-playing interactions without needing a lot of human input every time.

### Weaknesses
Given that budget limitations kept the sample size small, it would be helpful if the paper discussed how scaling up the tests might affect costs and computational resources. This would be useful for readers who are looking to use or expand on this benchmark.

The paper does touch on ethics broadly, but a more in-depth look at the ethical issues specific to role-playing language models would be valuable—especially when it comes to handling sensitive or potentially harmful content. Examining how well the models respect ethical boundaries, respond to user distress, or navigate social nuances could add key safety considerations to the benchmark.

### Questions
The paper shows how the benchmark works in both English and Russian, but how feasible would it be to extend it to other languages and cultural contexts? Have the authors considered specific challenges in keeping results consistent across models with different linguistic backgrounds?

The paper focuses on metrics like fluency, character consistency, and entertainment value, but would the authors consider adding other metrics to measure contextual understanding? For instance, it could be useful to evaluate how well a model keeps up with a storyline or handles unexpected, non-linear questions.

### Soundness
3

### Presentation
3

### Contribution
3
