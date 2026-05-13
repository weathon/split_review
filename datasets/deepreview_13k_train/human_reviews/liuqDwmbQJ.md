# ViLMA: A Zero-Shot Benchmark for Linguistic and Temporal Grounding in Video-Language Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
With the ever-increasing popularity of pretrained Video-Language Models (\VideoLMs), there is a pressing need to develop robust evaluation methodologies that delve deeper into their visio-linguistic capabilities. To address this challenge, we present \dataset{}\footnote{Project page: \url{https://cyberiada.io/ViLMA}} (\datasetfull{}), a task-agnostic benchmark that places the assessment of fine-grained capabilities of these models on a firm footing. Task-based evaluations, while valuable, fail to capture the complexities and specific temporal aspects of moving images that \VideoLMs need to process. Through carefully curated counterfactuals, \dataset{} offers a controlled evaluation suite that sheds light on the true potential of these models, as well as their performance gaps compared to human-level understanding. \dataset{} also includes proficiency tests, which assess basic capabilities deemed 
essential to solving the main counterfactual tests.
We show that current \VideoLMs' grounding abilities are no better than those of vision-language models which use static images. This is especially striking once the
performance on proficiency tests is factored in. Our benchmark serves as a catalyst for future research on
\VideoLMs, helping to highlight areas that still need to be explored.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new suite of benchmarks for video-language models (VidLMs), which requires the VidLMs to distinguish between factual and counterfactual descriptions of the videos. The benchmarks are further divided into a number of tests, including Action Counting, Situation Awareness, Change of State, Rare Actions, and Spatial Relations. Each test has an easy version (proficiency test) and a hard version (main test). 

The paper further evaluates a large number of VidLMs, together with LMs and ILMs. Interestingly, even the blind LMs can achieve significantly higher-than-random accuracy on the Situational Awareness and Spatial Relations tests, which suggests strong linguistic prior. However, the VidLMs often perform worse than the blind LMs on the two tests. Further, the image-only ILMs often outperform the VidLMs.

### Strengths
Evaluations of large VidLMs pose significant challenges. As the paper noted, even if the models achieve good accuracy on the main test, it does not mean it can achieve high scores on the supposedly easier proficiency test. Hence, many test results create misleadingly high performance numbers that lead to the illusion of human-like performance, and contribute to concerns of existential risks. 

This paper presents a solid step in rigorously evaluating VidLMs. The datasets are carefully designed and curated. The AMT protocols seem well thought over. The Action Counting test seems especially challenging.

### Weaknesses
The Situational Awareness tests and Spatial Relations tests seem to suffer from strong linguistic priors (despite mediocre VidLM performance). The Rare Actions tests are surprisingly easy, with VindLU achieving 88% for the difficult P+T condition. 

The analysis is relatively cursory (even though it's called "in-depth results" in the appendices). The number of parameters and amount of training data of the VidLMs should be reported along with the results. Preferably the authors can say a few words about the model architectures. I understand the reader can track these down from the original papers, but doing so would require significant effort given the number of baselines. Having these meta-data would help the reader understand if the model strengths are derived from the model size, the training data, or the architecture design.

### Questions
Nil

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of evaluating the temporal understanding ability of Video Language Models (VidLMs). It proposes a benchmark called VILMA by constructing “foil” video captions from existing datasets. Specifically, the foil captions are created by replacing certain phrases in the original captions and then the VidLMs are asked to distinguish between the original and foil captions. The foil captions can be divided into five categories, covering a wide range of temporal understanding abilities. This paper also introduces the **proficiency tests**, which assess the primary abilities required to effectively understand the temporal dynamics (**main tests**). The proficiency tests are designed to examine whether the performance in main tests is robust.

Based on VILMA, a number of VidLMs, image-language models (ILMs) and text-only models are tested. The results show that: (1) existing VidLMs exhibit very poor temporal understanding ability, which is not better than ILMs (even not better than random baseline in particular categories). (2) The performance of VidLMs and ILMs declines significantly when considering the proficiency test, which suggests that they may predict correct answers by chance or by exploiting some spurious features.

### Strengths
* The proposed benchmark is novel and valuable, which can provide a more comprehensive evaluation of temporal understanding ability than existing benchmarks.
* The evaluation results reveal the poor temporal understanding ability of existing VidLMs struggle, which can guide the development of more advanced VidLMs.
* The paper provides comprehensive details of the proposed benchmark, including the construction process, data distribution and examples.

### Weaknesses
 * The difference between VILMA and existing foiling benchmarks is not adequately described. The reviewer would like to know more details about why VILMA is more comprehensive. Specifically, it's unclear what specific limitations of benchmarks like Contrast Sets and Test of Time are addressed by VILMA. For example, does VILMA include more complex temporal relationships or a wider range of linguistic variations in the foil captions? A more detailed comparison of the types of temporal reasoning required by each benchmark would be beneficial.
* The gap between P+T suggests that there exists inherent dataset bias in VILMA, which can be exploited to achieve good performance. This phenomenon seems contradictory to the claim on page 24 that “the biases are not significantly present”. It is important to understand what specific biases are present in the dataset that allow models to perform well on T but not on P+T. For instance, are there lexical or syntactic patterns in the foil captions that make them easily distinguishable from the original captions, even without temporal understanding? This needs further investigation.
* The evaluation could be more comprehensive by including recent Video Large Language Models (Video LLMs), e.g., VideoChat [1], Otter [2], Video-LLaMA [3]. The current evaluation focuses on older models, and it is important to see how state-of-the-art Video LLMs perform on this benchmark. The absence of these models limits the impact of the study, as it does not reflect the current capabilities of the field.

### Questions
Please refer to the **Weaknesses**

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a zero-shot evaluation benchmark designed to require a strong temporal understanding of video-language models. The proposed benchmark is task-agonistic. They evaluate multiple video-language models and image-language models on the proposed benchmark. They find that video-language models do not have a significant advantage over image-language models, and the input understanding of the model is not robust.

### Strengths
1. The proposed benchmark is novel and fills a gap in video language model evaluation that tests the zero-shot temporal understanding and reasoning capabilities.
2. The required capabilities in the proposed benchmark are well-classified.

### Weaknesses
1. There are some of the most recent VidLMs with good performances missing in the evaluation. E.g. InternVideo [1], mPLUG2 [2], Uniformer v2 [3], etc. The necessity of the proposed dataset needs more evaluation to validate.



### Questions
1. When testing image-language models, which frame from the video is input to the model?
2. Next-QA [1] also requires the model to perform temporal understanding and reasoning. It seems the main difference between the proposed dataset and Next-QA is the format. Can the author explain the core challenges posed by the proposed dataset?

[1] NExT-QA: Next Phase of Question-Answering to Explaining Temporal Actions

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a zero-shot benchmark for linguistic and temporal grounding in video-language models. The evaluation focuses on five aspects: action counting; the recognition of specific actions or action participants; the recognition of action or event subphases; the recognition of rare actions; and distinguishing spatial relations. Experiments show that there is no essential difference between video-language models and image-language models in terms of temporal reasoning abilities.

### Strengths
1. The motivation of this paper is very important, that is, to establish a fair and reasonable benchmark for linguistic and temporal grounding in video-language models.
2. The experiments in this paper reveal that there is no essential difference between video-language models and image-language models in terms of temporal reasoning abilities. It provides the direction for the future development of the video-language models.
3. The paper is well written and easy to follow.

### Weaknesses
1. The form of the benchmark is still relatively simple, just let models choose the correct answer from two candidate sentences. However, simple two-choice questions are not enough to fully measure the ability of the model. The limited scope of the two-choice format restricts the evaluation to a coarse level, failing to capture the nuances of temporal understanding. For instance, models might succeed by exploiting superficial cues rather than demonstrating genuine comprehension of temporal dynamics.

2. In my opinion, the temporal understanding ability should include having the model locate where an event starts and ends in a video based on the description. More complex temporal understanding requires the model to analyze the events that occur in the video, and infer the actions that may occur in subsequent videos. Therefore, in my opinion, the proposed benchmark does not fully measure the temporal understanding ability of video-language models. The benchmark does not assess the model's ability to perform fine-grained temporal localization or predict future states based on observed events. This limits its applicability to real-world scenarios where such capabilities are crucial.

3. With the success of large language models, the latest video-language models, e.g., BLIP2 can output text with variable length and free content. The community may be more concerned about how to properly evaluate these open outputs. The proposed benchmark does not address the evaluation of generative models, which are becoming increasingly prevalent. The focus on a closed-set evaluation limits the benchmark's relevance to the current landscape of video-language models.

### Questions
Do you consider doing more analysis on the video itself, such as exploring the sensitivity of the model's temporal understanding ability to the length of the video? What happens to the model if you insert noise frames into the video?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
