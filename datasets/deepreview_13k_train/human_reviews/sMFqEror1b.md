# MMToM-QA: Multimodal Theory of Mind Question Answering

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Theory of Mind (ToM), the ability to understand people’s mental states, is an essential
ingredient for developing machines with human-level social intelligence. Recent
machine learning models, particularly large language models, seem to show some
aspects of ToM understanding. However, existing ToM benchmarks use unimodal
datasets – either video or text. Human ToM, on the other hand, is more than video or
text understanding. People can flexibly reason about another person’s mind based
on conceptual representations (e.g., goals, beliefs, plans) extracted from any available data. To address this, we introduce a multimodal Theory of Mind question answering (MMToM-QA) benchmark. MMToM-QA comprehensively evaluates machine ToM both on
multimodal data and on different kinds of unimodal data about a person’s activity
in a household environment. To engineer multimodal ToM capacity, we propose
a novel method, BIP-ALM (Bayesian Inverse Planning Accelerated by Language
Models). BIP-ALM extracts unified representations from multimodal data and
utilizes language models for scalable Bayesian inverse planning. We conducted
a systematic comparison of human performance, BIP-ALM, and state-of-the-art
models, including GPT-4. The experiments demonstrate that large language models
and large multimodal models still lack robust ToM capacity. BIP-ALM, on the
other hand, shows promising results, by leveraging the power of both model-based
mental inference and language models.\footnote{Code and data are available at the project website: \url{https://chuanyangjin.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This benchmark evaluates ToM on multimodal data and various unimodal data, addressing the limitations of existing unimodal ToM benchmarks. The proposed method, BIP-ALM (Bayesian Inverse Planning Accelerated by Language Models), successfully integrates unified representations from multimodal data with scalable Bayesian inverse planning using language models. Comparative experiments reveal that while large language and multimodal models lack robust ToM capacity, BIP-ALM exhibits promising results by combining model-based mental inference and language models.

### Strengths
1. The motivation is clear and the problem tackled is indeed interesting and important.
2. The dataset contribution is helpful for the community.
3. The paper is overall well presented.

### Weaknesses
1. Currently, this benchmark still significantly lacks of comprehensive baseline comparisons and in-depth analysis to really show the audience **why** the identified problem is so important and challenging.

a. More baselines like few-shot GPT4/3.5, evaluating LLM/Multimodal LLM with chain-of-thought types of reasoning process, open-sourced models with different sizes should be further studied to provide a better understanding of the performance of existing methods on this task.

b. Error analysis of existing models like GPT-4 or VideoLLAMA should be provided since it is important for the audience to understand how the proposed method solves the flaws in existing methods exactly. With the recent release of GPT4V, it will be great if some insights could be drawn from this case study as well.

c. Currently the evaluation setting among different models is also not very clear. For example, models like VideoLLAMA actually takes video frames as input but other LLM models seem to only take parsed information. It is important to clearly annotate the exact format of each modality for all the model variants to make it clear to understand the possible difference from the input side.

2. Currently, some limitation/ design choice is not well justified.

a. Why is the proposed method not applied to VideoLLaMA and Instruct BLip?

b. Is the synthetic video data really capturing important goal and belief in real world? What is the domain gap? There should be at least case studies on some real procedural videos, investigating the possible domain shift to validate the usage of synthetic video and revealing the possible limitation of this benchmark more explicitly.

### Questions
Please check weakness for details.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a benchmark and a model for evaluating theory of mind in machine learning models. The benchmark consists of synthetic videos, explanations, questions, and answers. The associated proposed model leverages GPT-4 for translating natural language text into symbolic representations as well as a visual perception model to extract visual information into symbolic representations. Several baselines are evaluated on the proposed benchmark on three modalities: multimodal, text-only, and video-only.

### Strengths
The paper includes a multimodal QA dataset with synthetic videos that can be potentially useful for future research and includes a human baseline.

### Weaknesses
1. The paper should do a better job of justifying the proposed task itself. The paper argues that Theory of Mind is important for developing machines with human-level social intelligence. However, it is unclear why having machines with “human-level social intelligence” is necessary. First, can “social intelligence” be measured or evaluated? It is still unclear how to define intelligence alone and how to measure it within the machine-learning context. Second, what types of applications will benefit from this skill?

2. Without a clear goal and definition, it is hard to validate whether the proposed benchmark aligns with the task described in the introduction of the paper. Can we draw conclusions from the results in the proposed benchmark about a model’s social intelligence? It is hard to say in the current setting.

3. The text is unclear about using synthetic videos in the test set. As it is written in Section 3.1, it looks like the 134 test videos are real image videos, whereas the 1000 training videos are synthetically generated. However, in Section 3.3, it looks like the test videos are also synthetic. If test videos are not synthetic, how are they obtained?

### Questions
- What are the statistics of the benchmark per question type?
- Please include an overall column in Table 1 or the actual numbers in Figure 4.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a multimodal dataset called MMToM-QA for evaluating machines' understanding of a person's activities in a household environment. Based on the dataset, the authors propose a BIP-ALM method to encode information from multimodal inputs and utilize language models (LMs) for inference. They find that LMs and multimodal models are still lacking the knowledge to solve MMToM-QA, but BIP-ALM shows a promising direction.

### Strengths
The paper is easy to follow and every details are clearly described.

### Weaknesses
MMToM-QA is flawed. VQA has been studied for years and the issues in crowdsourcing and annotations are clearly mentioned in many piror works. However, the paper lacks quantitative studies regarding these issues. For example, whether the questions designed can be attacked by counting the repeating semantic meaningful words, whether the text question already implied the answers. From Table 1, the high performance in text-only models may mean these flaws in dataset design.

The conclusion that "large language models and large multimodal models still lack robust ToM capacity" is not convincing, as the paper only tests BIP-ALM on the proposed MMToM-QA dataset. There are many other datasets that evaluate models' understanding of people's activities, such as VQA [1] and VCR [2]. The paper should compare BIP-ALM to the state-of-the-art methods on these benchmarks and also cite these benchmarks in related works.

Comparison to baselines is unfair. The paper tested BIP-ALM tuned on the dataset, yet use zero-shot approach to test the baselines such as GPT, LLaMA, InstructBLIP etc. So the pretraining of these baselines may fail to generalize to a totally different MMToM-QA data. The authors need to finetune these LLMs or prompt these models to provide a more fair comparison.

### Questions
Please read the weaknesses I listed.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of the theory of mind (ToM) by taking advantage of multi-modal information and the Bayesian inverse planning method. A new dataset is constructed with a focus on the scenarios where agents perform a sequence of household activities. The proposed method designs a collection of prompts and leverages a large language model for converting the multi-modal information (visual scene graph and textual description) into representations suitable for probabilistic inference. Experimental results demonstrate the effectiveness of the method in multiple settings.

### Strengths
+ It is an interesting question whether or not large language models are able to infer the internal state of the other agents. The paper presents a new multi-modal dataset, which can facilitate future research along the direction. 

+ The proposed probabilistic model could potentially enable the understanding of how models aggregate information to address the problem of ToM, e.g., the relationships between observations and the dynamic of belief.

+ The paper proposes a principled approach for integrating multi-modal information into an unified representation, which shows promise in inferring the belief and goal.

### Weaknesses
 - Despite leveraging a probabilistic planning method and showing considerable improvement, the paper pays little attention to investigating the model’s underlying mechanism. It would be more interesting to understand how the observed information influences the inference of belief, and which strategies are used by the models for tackling the challenges. Specifically, the paper lacks a detailed analysis of how the model's belief states evolve over time given different types of observations (e.g., visual, textual, and their combinations). It would be beneficial to see a breakdown of which specific aspects of the visual scene graph and textual descriptions contribute most to accurate belief inference, and how the model handles conflicting or ambiguous information from these modalities.

- The authors highlight that the proposed method solves the problem in a zero-shot manner, however, the appendix mentions that it is fine-tuned with ground truth annotations, please explain. In addition, I feel like a considerable portion of important details are compressed into the appendix, which makes the main paper difficult to understand. The discrepancy between the zero-shot claim and the fine-tuning details needs clarification. Furthermore, the paper should include more crucial details in the main body, such as the exact prompt templates used, the architecture of the large language model, and the specific training procedure, instead of relegating them to the appendix.

- Constructing visual scene graphs is a challenging task, especially in naturalistic data of broader domains. How would the accuracy of predicted scene graphs affect the performance of the proposed method? With the increasing complexity of the visual scenes (e.g., from synthetic household environments to naturalistic scenarios in the wild), what are the potential ways of generalizing the method? Additionally, it seems that the paper does not mention which models are used for visual perception. The paper should discuss the limitations of the current scene graph generation method, and how errors in scene graph construction might propagate through the model. The paper also needs to address the scalability of the approach to more complex and realistic visual environments, including a discussion of the computational cost associated with processing more complex scenes.

- Related to the aforementioned comment, the textual parsing and information fusion rely heavily on pretrained large language models (e.g., GPT-4) and a collection of carefully-tuned prompts (for household scenarios), it is relatively unclear whether or not such a paradigm is able to accommodate the diversity of more complicated environments. The paper should include an analysis of the sensitivity of the method to variations in the prompt design and the potential for prompt engineering to introduce bias. It is also unclear how well the current approach would generalize to scenarios that are not well-represented in the training data of the large language model, or to environments that require more complex reasoning beyond simple household activities.

- It appears that there is a significant variance in the performance of different types of problems, any idea why (e.g., GPT-4 fails drastically in setting 2.3)? The paper should include a more detailed error analysis to understand the failure modes of the model. It would be beneficial to categorize the types of errors made by the model and provide a qualitative analysis of why the model fails in certain scenarios. For example, does the model struggle with long-range dependencies in the action sequences, or does it have difficulty with specific types of belief updates?

### Questions
(1) How would the proposed method benefit understanding behind the model’s inference of ToM?

(2) What are the challenges and potential solutions for generalizing the method toward broader domains?

(3) Is there any typical failure modes of the method, and why?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
