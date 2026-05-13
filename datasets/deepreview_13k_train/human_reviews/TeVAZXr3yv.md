# MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
The ability to comprehend audio—which includes speech, non-speech sounds, and music—is crucial for AI agents to interact effectively with the world. We present MMAU, a novel benchmark designed to evaluate multimodal audio understanding models on tasks requiring expert-level knowledge and complex reasoning. MMAU comprises 10k carefully curated audio clips paired with human-annotated natural language questions and answers spanning speech, environmental sounds, and music. It includes information extraction\footnote{We define an \textit{\textbf{information extraction}} question as one that requires a deep understanding of audio, detailed content analysis, and the application of external world knowledge when necessary.} and reasoning~\footnote{We define a \textit{\textbf{reasoning}} question as one that requires intentional, complex thinking beyond basic content understanding, analysis, and knowledge application, simulating expert-level cognitive processes.} questions, requiring models to demonstrate 27 distinct skills across unique and challenging tasks. Unlike existing benchmarks, MMAU emphasizes advanced perception and reasoning with domain-specific knowledge, challenging models to tackle tasks akin to those faced by experts. We assess 18 open-source and proprietary (Large) Audio-Language Models, demonstrating the significant challenges posed by MMAU. Notably, even the most advanced Gemini Pro~\textsubscript{\tiny{v1.5}} achieves only 52.97\% accuracy, and the state-of-the-art open-source Qwen2-Audio achieves only 52.50\%, highlighting considerable room for improvement. We believe MMAU will drive the audio and multimodal research community to develop more advanced audio understanding models capable of solving complex audio tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces MMAU, a new benchmark designed for audio large language models, akin to the role of MMLU and MMMU for text and vision. The authors hired "domain experts" to curate a challenging set of 10,000 annotated audio-based question-response pairs spanning speech, music, and environmental sounds. The author further benchmarked 18 open-source and proprietary large audio-language models, and shows a few interesting observation and insights.

### Strengths
1. The topic of this paper is very important — currently, most audio LLMs are benchmarked using different evals, and researchers must test other models for comparison, which is tedious and impractical for many. A unified benchmark is common in text and vision, such as MMLU, MMMU, and DocVQA, and has already demonstrated its effectiveness as a good measure of models. We need one for audio. 

2. The authors also benchmarked 18 LLMs, which is a non-trivial task as some open-source repositories are not easy to use. With this benchmark, we gain insights into performance comparisons among them, making this paper also serve as a very valuable review paper. The result numbers contain a lot of information.

3. The paper includes some good discussions.

4. Overall, the writing is clear, with detailed information provided in the appendix.

### Weaknesses
1. I would like to see more discussion for an ICLR submission. Although the authors did significant work, I encourage them to add more insights to the results, such as exploring why one model performs better than another in specific benchmarks.
- e.g., is the difference of a specific test more likely from the training data (e.g., Google's model trained on more data than those from academia), or from the architecture/training (e.g., early fusion, late fusion, discrete token vs continuous embedding vs text input). And what's the potential way to improve. 

2. Evaluations are crucial but must be carefully designed. I did not notice a few-shot setting mentioned in the paper (unless I overlooked it), yet few-shot evaluation is quite common in LLM benchmarking (i.e., Q1->A1; Q2->A2; Q3-?).
- If running few shot on all models / tests is hard, I suggest to run it for some representative models and report the gap between zero-shot and few-shot, this is particular important for model not post-trained on things like multi-choice questions (select one from ABCD). 

3. I understand this might be due to the timing of when the authors prepared the paper or potential rate limitations, so this is not a major flaw. However, given that OpenAI now offers real-time API and voice mode API, it would be a valuable addition to include these capabilities.
- And I understand it might be quite expensive to run the full test, if that is the case, maybe you can run on a set of hard tests and compare with Google's model. But I feel a full run would greatly increase the value of the paper - it tells the reader which is the best audio model.

### Questions
Section 5.2

I am wondering about the breakdown (e.g., categories) for this experiment. Do you provide the ground truth text of the speech to the model? It seems a bit strange to me that, for sound classification and speech recognition, the model could do anything meaningful with Gaussian noise.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work introduces MMAU, an audio understanding benchmark designed to evaluate the advanced auditory perceptual and reasoning capabilities of LALMs. MMAU features 10,000 human-annotated audio-question-response pairs, encompassing 27 distinct skills across unique tasks. Most existing LALMs are tested on MMAU in the paper, highlighting the challenges in auditory understanding faced by current models.

### Strengths
- In this paper, a large-scale audio understanding benchamrk "MMAU" is built to evaluate LALMs. Different from previous benchmarks, MMAU not only pays more attention to deeper and more difficult auditory reasoning tasks, but also covers a wide range of sound signals as well.
- I believe MMAU is a reliable benchmark, as it is carefully designed during the build process with human review at each step.
- Most exsiting LALMs are evaluated on MMAU in this paper. Besides, the authors have analysed the weaknesses of existing LALMs in detail, providing directions for further studies.

### Weaknesses
 - It seems that MMAU primarily focuses on short audio (around 10 seconds) and lacks evaluations involving perception and reasoning for long audio. Since long audio includes more contextual information, the model's ability to understand long audio might offer a broader indication of its overall performance.
- MMAU is still predominantly multiple choice, but existing LALMs may not be good at multiple choice. Perhaps open-ended questions could be used as prompts instead when testing.

### Questions
- What tasks is the synthesised data primarily aimed at? How is the data synthesised?
- How is the difficulty ("easy", "medium", "hard") of a question determined? Since for some skills, existing models consistently perform badly regardless of the difficult levels of the questions, does this mean that the difficulty should be classified by the skill type, rather than the question?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents MMAU, a new benchmark to evaluate large audio-language models (LALMs) on complex multimodal audio understanding tasks. It includes 10,000 human-annotated audio-question-response pairs covering speech, sound, and music. The goal is to benchmark knowledge extraction and advanced reasoning across 27 distinct skills. The authors evaluate 18 open-source and proprietary models, revealing a significant gap between current LALMs and human capabilities. The benchmark's difficulty and breadth emphasize the limitations of current audio-language models, encouraging future research.

### Strengths
- MMAU significantly improves upon existing benchmarks by covering 27 distinct skills across three domains (speech, sound, and music). The low accuracy scores of state-of-the-art models highlight the benchmark's difficulty and push for more advanced models to handle complex tasks.
- It is the first benchmark for reasoning and expert-level knowledge extraction in literature, setting it apart from previous benchmarks focused on foundational audio processing tasks. This aligns with the growing demand for AI systems capable of human-like reasoning.
- The paper includes a detailed analysis of error types (perceptual, reasoning, etc.) across different ALMs and domains, offering valuable insights into current model limitations and how to improve them.
- The paper is well-written and easy to follow

### Weaknesses
 - MMAU focuses solely on multiple-choice tasks, which could skew results towards models trained for MCQ-type question-answering and possibly even contrastive models. It would be beneficial to include an open-ended subset, even a small one, to contrast performance with the close-ended tasks.
- The current version treats skills needed for information extraction and reasoning as separate, potentially oversimplifying the evaluation of tasks requiring a combination of skills.
- [Minor] The contrastive models are tested on the MMAU dataset, but the results are added only in the appendix and Table 4. It would be better to add the Table 4 rows to the main Table 3 and include one main insight from the contrastive model results in the main paper.
- [Overall] The paper is well-executed, delivers on its promises, and devoid of any major weaknesses

### Questions
- The authors mention using robust regular expressions and response-processing workflows to extract key information, matching it to the provided options via string matching. Evaluating ALMs that produce open-ended responses is challenging as they often don't adhere to multiple-choice options or instructions, making regex unsuitable. Have the authors considered using an LLM to evaluate outputs for this task? More details on the regex method, including human annotation verification for a subset of randomly sampled data, would be helpful.
- In Appendix E, the authors list dataset sources used. Among these, AudioSet and AudioSet-strong are commonly used to train ALMs. This overlap between training and test audio data could skew results and conclusions. Have the authors conducted experiments to ensure this isn't the case or used a separate test set to avoid this issue? Clarification would be appreciated.
- Additional information on the synthetic data generation and its domain would be helpful, I could not find this in the paper

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
The paper introduces a new benchmark for evaluating multimodal audio-language models across speech, sound, and music domains, with tasks requiring both information extraction and complex reasoning. The benchmark comprises 10,000 audio clips paired with annotated questions and answers, challenging models to demonstrate proficiency in 27 distinct skills. The authors provide a comprehensive analysis of 18 models, revealing current limitations in multimodal understanding, with the best-performing model achieving only 53% accuracy, highlighting significant room for improvement in this area.

### Strengths
1. MMAU is novel in its scope and comprehensiveness, covering a wide range of tasks that target specific skills in multimodal audio understanding and reasoning, addressing a critical gap in existing benchmarks.
2. The authors enlisted real-world human experts, conducted thorough evaluations, and used GPT-4 to enrich the dataset with additional options. Detailed prompt information is also provided in the appendix.

### Weaknesses
1. While the authors claim that tasks may require multiple skills, a review of Appendix H reveals that most tasks can be completed using a single skill. This claim lacks precision and is not sufficiently supported in the paper.
2. The data is sourced from 13 datasets, but the paper does not provide enough explanation regarding the selection of the 10,000 data points from these large datasets. In Section 3.2, the authors mention that experts were involved in classifying abilities and question-answer pairs, but there is no clear description of the selection process. How was the initial screening conducted, and how were quality and diversity ensured? Even Appendix E provides only a brief overview of the datasets, raising concerns about data quality.
3. Although expert annotation is mentioned, there are no specific details on how bias was controlled during the annotation process. The accuracy and consistency of benchmark data are central to evaluation reliability, but Appendix C.2 lacks elaboration on how expert annotations were quality-checked and bias-mitigated.
4. In the experimental section, while bias in model selection was avoided, the response quality of most models (e.g., SALAMONN and Qwen2-Audio) was significantly influenced by the prompts. These models were primarily trained in a QA format, and there is a noticeable difference between their open-ended responses and multiple-choice selections. This raises concerns about whether the evaluation method accurately reflects the models' limitations, and further discussion on this issue is necessary.
5. The evaluation in the experimental section relies on multiple-choice questions and uses string matching to determine correct answers. This method seems overly simplistic. Given the openness of LLM responses, a more sophisticated approach should be used to evaluate whether a model's output is sufficiently similar to the correct answer. The authors should provide more details about the evaluation methodology to ensure results are reliably reproducible.

### Questions
1. The paper mentions the distinction between reasoning and extraction tasks. However, some tasks appear to require a combination of both skills inherently. What is the rationale behind maintaining this distinction?
2. In Appendix L, the prompt requires the model to generate a correct option. What is the purpose of this approach, and how does it impact the evaluation?

### Soundness
3

### Presentation
3

### Contribution
2
