# Human Simulacra: Benchmarking the Personification of Large Language Models

- Decision: Accept
- Scores: 8, 3, 6, 5, 6

## Abstract
Large language models (LLMs) are recognized as systems that closely mimic aspects of human intelligence. This capability has attracted attention from the social science community, who see the potential in leveraging LLMs to replace human participants in experiments, thereby reducing research costs and complexity. In this paper, we introduce a framework for large language models personification, including a strategy for constructing virtual characters' life stories from the ground up, a Multi-Agent Cognitive Mechanism capable of simulating human cognitive processes, and a psychology-guided evaluation method to assess 
human simulations from both self and observational perspectives. Experimental results demonstrate that our constructed simulacra can produce personified responses that align with their target characters. 
Our work is a %pioneering
preliminary 
exploration which offers great potential in practical applications. All the code and datasets will be released, with the hope of inspiring further investigations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper introduces a benchmark to assess the potential of LLMs in simulating human behaviours and personality traits for psychological and sociological applications. This work includes the creation of the "Human Simulacra" dataset, which features detailed virtual characters with diverse life stories constructed with human feedback to enhance realism and ethical accuracy. The authors present a Multi-Agent Cognitive Mechanism (MACM), which simulates human memory and cognitive functions, allowing virtual characters to process emotions and memories for more realistic responses. Evaluation is conducted through a psychology-guided framework that includes self-reports for self-awareness and observer-based assessments where human judges evaluate character responses in various scenarios. Experiments comparing MACM to other simulation methods show that MACM enables LLMs to better replicate human-like behaviour, although limitations remain, particularly in capturing the nuanced adaptability of real human responses to social pressures. This benchmark aims to foster future research on using LLMs as proxies for human participants in psychological experiments while acknowledging ethical implications and the need for authentic simulations.

### Strengths
Originality: This paper brings together ideas from psychology, cognitive science, and artificial intelligence to create a unique benchmark for evaluating how well language models (LLMs) can act like humans. Unlike previous studies that mainly focus on simple character traits or responses, this paper takes a deeper approach using Jungian psychology to model personalities with eight different dimensions. This gives a fresh perspective on capturing complex human traits. Additionally, the Multi-Agent Cognitive Mechanism (MACM) is a new tool that helps the models better remember, process emotions, and respond in context, making their behavior more human-like.

Quality: The paper is thorough and well-executed. The Human Simulacra dataset is carefully built, with multiple rounds of expert review to ensure quality, accuracy, and ethical considerations. Each character's story is carefully crafted and reviewed to provide a deep foundation for testing the LLMs’ performance in simulating humans. The MACM’s design, which coordinates memory, emotion, and logical processing, is a clear improvement over simpler models that rely on only one type of agent or basic retrieval methods.

Clarity: The paper is well-organized and clearly explains its methods and objectives. From the motivation to simulate human personalities, through the dataset creation, model mechanism, and evaluation framework, each part is easy to follow. 

Significance: This paper makes an important contribution to AI and psychology, especially by opening up possibilities for LLMs to replace humans in some psychological studies. By creating a foundation for simulating complex human traits, this benchmark could allow LLMs to ethically stand in for human participants in specific research settings.

### Weaknesses
No outstanding weaknesses.

### Questions
No questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper aims to test llms to generally model human personalities and behavior. To do this, they first build a bank of personas based on Jung’s personality theory, they build a biography of the character with the help of a language model. To probe the behavior of the simulated human characters, the authors use two types of evaluations: Self report, asking questions about the characters themselves, and observer reports with human judges. For observer reports, the authors use 55 scenarios from a situational judgement test for testing personality traits. The paper also proposes a new cognitive architecture to simulate humans Multi-Agent Cognitive Mechanism (MACM). To test the capacity of models in simulating psychology experiments, the authors try a social conformity experiment (the bandwagon effect). The authors show that the MACM aligns with human data better than a baseline (simulated characters from character ai).

### Strengths
- The paper is well motivated and tries to address a relevant problem.
- The authors test a wide variety of LLMs.
- The authors release the dataset and the recreation results are very comprehensive.
- The set of experiments in the paper is quite extensive.

### Weaknesses
 **Clarity**

- The abstract is vague and does not provide any specifics. I urge the authors to provide more information of their empirical experiments and results.
- In paragraph 2 of the introduction, could you please provide examples of “complex characteristics of human behavior” that we’d want to simulate?
- The introduction could be made more clear. Jung’s theories seem to be central to the framework, but haven’t been explained clearly.
- The methods section lacks clarity. The authors refer to the figure, but don’t explain it, making it difficult to understand. How exactly is generation broken down? What are sub tasks? What is the reason for picking these sub tasks, are there any alternatives?
- While generating the dataset, how is human feedback collected? Do the authors provide feedback themselves? What is the measure of quality? How does it improve with the iterations?
- “To ensure the validity of responses, we create a comfortable chatting environment for each simulacrum and act as their best friend, encouraging them to respond honestly to the questions.” What are the authors trying to say here?
- Cloze is not defined in the main text. I urge the authors do define what the cloze methodology is in the main text.
- How are the models from character ai exactly used?
- Do the llms see the stimuli in the conformity experiment? If they do not, it is strange to use the conformity experiment. This wasn’t clear in the main text.

**Validity**

- The authors choose Jung’s theories for personality over MBTI citing that MBTI has no scientific validity, but Jung’s theory also has very little to no empirical /scientific backing! Just writing “on the recommendation of psychologists” is not scientific evidence.
- The actual evaluations of the personas are limited. The introduction is motivated by trying to study complex human behaviors, but  Only a very small number of scenarios from a Mussel et al. (2016) are used.
- No ablations are conducted with the MACM, only baselines like RAG have been compared. Moreover the gains over a simple RAG based method seem limited. Similarly, the character ai baseline for simulating the conformity experiments seems inadequately justified. I would like the authors to explain why this a good baseline? RAG is not compared with the MACM baseline for the conformity experiments.


### Questions
Please see weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This study introduces a new benchmark to assess the ability of large language models to mimic human personalities in psychological experiments. The researchers created a dataset of virtual characters with detailed life stories, a cognitive mechanism that simulates human thought processes, and a framework for evaluating large language models based on psychological principles. After testing large language models, the results showed that while top models can accurately simulate self-reported personality traits, they struggle with observer-reported traits. Additionally, a replication of a classic psychology experiment found that large language models can exhibit human-like behavior, but in a more rigid and less nuanced way, highlighting both the potential and limitations of using large language models in psychological research.

### Strengths
- Comprehensive review on psychology theory
- Clear descriptions of experiment setups
- Test a variety of agent architecture 
- Experiments in Section 5.2 compares human behaviors with LLM-driven simulation results. 
- The tasks in evaluation are hard and meaningful

### Weaknesses
 - The paper doesn't present very straightforwardly and clearly what exactly the benchmark is measuring. A diagram of what's considered good and what's considered bad eval result would be helpful.
- Evaluation dataset depends a lot on human expert. Ablation on human expert is not done.
- The constructions of evaluation/frameworks in this paper are very psychology-theory driven. I have two concerns: 1. there are many theories to choose one, why one over another? Are all components derived from theories necessary? Or are we missing some important aspects. 2. It's probably more preferable to motivate with real-world applications of persona-driven simulations and design evaluations based on components that are useful and necessary in these applications.
- There might be variations of difficulty in different kinds of personas for models to follow (e.g. real world vs fictional world). The paper doesn't consider those.

### Questions
- Section 3.1 describes the following attribute set for virtual characters: {name,
age, gender, date of birth, occupation, personality traits, hobbies, family background, educational
background, short-term goals, and long-term goals}. What's the motivation for this set? Is this set exhaustive and all necessary?
- Same question for Figure 5: What are the alternative architectures/mechanism and what's unique about this formulation of cognitive mechanism?
- What are the possible applications of persona-based simulation in real life, and how are personas that are used in benchmark related to those possible applications?

### Soundness
2

### Presentation
2

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
- The paper introduces a personification benchmark involving high-quality data supervised by psychology experts.  
- It incorporates rigorous evaluation methods based on psychological theories and comprehensive benchmark tests. 
- Fourteen widely-used large language models (LLMs) are tested across four simulation methods in extensive experiments.

### Strengths
- This paper proposes a high-quality simulated human profile dataset, developed with real human input, alongside a more advanced evaluation benchmark to assess the ability of large language models (LLMs) to emulate specific individuals. 
- A novel multi-agent-based cognitive memory mechanism is implemented to enhance the alignment of personality traits in LLMs. It is proved useful with psychological experiments.
- Extensive experiments were conducted to evaluate existing LLMs and validate the effectiveness of the proposed MACM method.

### Weaknesses
 - The data collection process is somewhat tiresome,  and requires a lot of human efforts, to avoid the ethical problems of using real personality. Besides, the proposed benchmark framework also requires human effort.

- The paper emphasizes using Jung's personality theory and its advantages over MBTI, resulting in 640 personality descriptions, but at the end, only 11 characters are introduced, so it seems there is no need to use such a lot of personalities. Jung's theory also gives scores for each dimension, the scale of these scores also affects personality analysis. It seems 10 descriptions for each ranking are not enough. The paper seems to overclaim their use of Jung's Theory.

- When the author trying to compare a genuine character with a simulated profile. The hallucination part is not understandable. Simulated profiles could also lead to hallucination if using LLMs, the simulated ones are even harder to detect.  Considering the labor of building a profile, why not use characters from storybooks that also avoid ethical problems?

### Questions
- The description score of MACM seems lower than RAG in Table 3, could you help explain why?

- The multi-agent cognitive method is interesting, but it poses a high requirement on LLMs' capability.  Could you give more deeper analysis of this information processing structure?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a benchmark for evaluating the LLM’s capabilities of human simulation. It contains the life stories of 11 virtual characters and request the LLM to simulate one of them. The LLM’s simulation capability is assessed based on its self-reports and observer reports, both in the form of question-answering.

Compared with previous research on role-playing LLMs, the authors emphasize the novelty of this work in the following aspects: 
- **Personality modeling**: they model personality from eight dimensions inspired by Jung’s psychology theory, instead of using MBTI; 
- Virtual characters: they construct a **virtual character** dataset (containing 11 characters) for evaluating the LLMs capabilities of simulating these characters, instead of using genuine characters;
-  they evaluate human simulation capabilities by integrating both **self reports** and **observer reports**. 

In addition to this benchmark, they also propose an LLM-based system for more advanced human simulation, named MACM, which encompasses various modules mimicking human cognitive processes.

### Strengths
- Given the popularity of role-playing applications for LLMs, assessing their performance in human simulations is a critical research direction.
- The proposed benchmark for assessing the role-playing capabilities of large language models (LLMs) is constructed more rigorously than current benchmarks (to the best of my knowledge). It is based on more robust psychological theories and involves greater human effort to ensure high-quality data.
- The paper conducts extensive benchmarking studies on a broad set of models.
- Clear and detailed tables and figures that enhance the presentation.

### Weaknesses
 - The introduction claims that this paper is exploring “*How far are LLMs from replacing human subjects in psychological and sociological experiments?*”. However, I have reservations about how effectively the proposed benchmark addresses this research topic. The benchmark utilizes self-report evaluations, which resemble question-answering or reading comprehension tests based on character profiles (see appendix D.1, e.g., “When is your birthday?”). The addition of observer reports is interesting and novel, but it remains unclear if the hypothetical scenarios used for observer reports are sufficient and appropriate for evaluating the LLM’s potential in replacing human subjects in psychological and sociological experiments. The scenarios, while drawing inspiration from situational judgment tests, may not fully capture the nuances of real-world social interactions and psychological responses. The reliance on pre-defined scenarios limits the evaluation to a constrained set of situations, potentially missing the complexities of human behavior in dynamic and unpredictable contexts. More data samples and a detailed rationale for the design of these scenarios should be provided to support this evaluation. As for the experiments on bandwagon effect, it is simply a single case of psychological and sociological experiments, which can hardly support the research topic. 
- More qualitative analysis about the model failures would enhance the evaluation by providing deeper insights. A deeper analysis of failure modes, such as inconsistencies in character behavior or deviations from the intended personality traits, would be beneficial. This could involve examining specific instances where the LLM's responses deviate significantly from the expected behavior of the simulated character, and categorizing these failures to identify underlying patterns or limitations. I also suggest highlighting the main takeaways at the end of the experiments. 
- The title, “personification of LLMs”, is a little misleading and over claimed, as “personification” entails many more aspects that are not well explored in this paper.

### Questions
- Can you provide more data samples used for observer reports and how you design  these hypothetical  scenarios?
- The process of how you conducted the experiments in Section 5.2 is not clearly illustrated. Can you provided more details on how you conduct this set of experiments?
- Could the terms "psychology support" and "human feedback" in Table 1 be defined more clearly? They are difficult to understand when viewed in isolation in Table 1 and Section 2. Additionally, the phrase "full life story" also seems to be an overstatement (especially in terms of the word "full").

### Soundness
3

### Presentation
3

### Contribution
2
