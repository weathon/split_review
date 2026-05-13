# How to Build a Pre-trained Multimodal model for Simultaneously Chatting and Decision-making?

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
Existing large pre-trained models typically map text input to text output in an end-to-end manner, such as ChatGPT, or map a segment of text input to a hierarchy of action decisions, such as OpenVLA. However, humans can simultaneously generate text and actions when receiving specific input signals. For example, a driver can make precise driving decisions while conversing with a friend in the passenger seat. Motivated by this observation, we consider the following question in this work: is it possible to construct a pre-trained model that can provide both language interaction and precise decision-making capabilities in dynamic open scenarios. We provide a definitive answer to this question by developing a new model architecture termed Visual Language Action model for Chatting and Decision Making (VLA4CD), and further demonstrating its performance in challenging autonomous driving tasks. We build VLA4CD on the basis of transformer-based LLM architecture. Specifically, we leverage LoRA to fine-tune a pre-trained LLM with data of multiple modalities covering language, visual, and action. Unlike the existing LoRA operations used for LLM fine-tuning, we have designed new computational modules and training cost functions for VLA4CD. These designs enable VLA4CD to provide continuous-valued action decisions while outputting text responses. In contrast, existing LLMs can only output text responses, and current VLA models can only output action decisions. Moreover, these VLA models handle action data by discretizing and then tokenizing the discretized actions, a method unsuitable for complex decision-making tasks involving high-dimensional continuous-valued action vectors, such as autonomous driving. The extensive experimental results on the closed-loop autonomous driving platform CARLA validate that: (1) the model construction method we proposed is effective; (2) compared to the state-of-the-art VLA model, VLA4CD can provide more accurate real-time decision-making while retaining the text interaction capability inherent to LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The current manuscript proposes to build a large language model (LLM) capable of understanding multiple modalities like text, vision, and actions; and producing them as outputs. In particular, it develops a Visual Language Action model for Chatting and Decision Making (VLA4CD) that produces continuous actions without losing its ability to chat with a user simultaneously. Notably, the action space is not discretized and kept continuous, unlike prior works in this area. The paper also demonstrates experiments on CARLA dataset to claim that this approach is effective and can provide real-time decision making compared to prior art, while retaining its text interaction capability.

### Strengths
(S1) In general, the intended direction of this work, i.e., a model that can take actions while retaining the ability to generate textual responses to a user is useful. Please see weaknesses for further discussion.

(S2) The technical details as presented in the paper are easy to understand and follow.

### Weaknesses
 (W1) The current manuscript suffers from a clear lack of motivation for why we need a model that can produce both actions and also “chat” (L21, for instance) with a user. There are two main problems here:
* Throughout, the ability of “chatting with people” (L88) has not been characterized well. It is not open-ended dialog on any topic but rather an explanation of what actions to take or why it has taken a certain action in a given situation. This is misleading as currently phrased.
* Much of the motivation is around “a human driver can operate while chatting with a friend”, which does not apply to why we need a unified model. For instance, why not have an actuation model and an open-ended dialog model in the autonomous vehicle to achieve the above desired motivation? This indicates the lack of a clear motivation from an application standpoint.


(W2) Even if one were to scope the “chatting with users” ability down to producing explanations as responses to a fixed set of templated questions (see A.10), the manuscript does not follow through via corresponding experiments. Both actions and text-generation capability has been evaluated independently, once again begging the question as to why such a unified system is useful. There are no experiments to verify the following:
* The model actually actuates based on the textual outputs? I.e., if the model responds with “I will take the right lane in 20 mins”, does it actually do that?
* Are these textual explanations correct/sound given the state of the environment?
* What is the correlation of the GPT-4o score evaluation with human evaluation?


(W3) There are some concerns around the experimental validation of the proposed methodology:
* The reported experiments on town03 and town04 from the CARLA environment do not seem to match with any of the existing benchmarks with prior works (C, D).
* To further exacerbate this issue, none of the baseline results are from literature and have been reported based on reproductions in this work.
* Missing baselines, see [A] for more information.
This raises serious questions about the efficacy and usefulness of the proposed methods from an empirical standpoint. Why were existing, standardized benchmarks not used for model comparisons? Request the authors to address these concerns without which the benefits of this approach will remain unclear.

### Questions
(Q1) L154: Do you also include model textual response \hat{w}_i, i = {1,..,H} in w_i?

(Q2) Eq 1: \hat{w} is overloaded as both the model textual response and the embeddings of text inputs

(Q3) Eq 1: Each of w_i might have a different number of tokens (different from n). Do you pad them to n or is the index (n_i) dropped for brevity? That is: (w_i^1, w_i^2….w_i^{n_i}) instead of just (w_i^1, w_i^2….w_i^{n})

(Q4) L222-L225: The observed phenomenon is not clear here. Referring to the appendix also doesn’t add more details, apart from the empirical observation. Can the authors describe this with an example? 

(Q5) VLA4CD (no-language): What is the architecture, inputs for this model? Ideally, the human question in the input and the {s_t^{l+1}, .., s_t^{l+n}} must be removed while training.

(Q6) L413: How did you balance the two losses for DriverGPT4? Did you have a hyperparameter search for the loss weights similar to your approach?

(Q7) L477: The reasoning here is heavily dependent on the discretization strategy used for each environment. How were the actions discretized for this environment? Was there a hyperparameter search performed to get the best strategy?

(Q8) L140-142: How is this problem avoided in the current setup? It’s not clear in the text here.
* Action space dimension is small, i.e., 2 (acceleration and steering) How does this scale with more variables?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
- The authors propose VLA4CD, a model for self-driving that is capable of generating both language and action tokens. 
- VLA4CD is trained using three different types of loss functions: language generation, action generation, and image reconstruction. 
- The trained model demonstrates superior performance in both decision-making and question answering compared to models such as DriverGPT4 and OpenVLA in the gym-carla environment.

### Strengths
The main contribution of this work is that the authors add a language generation capability to VLA in self-driving scenarios.
- The paper is well-structured, making it easy to read and understand the authors' approach.
- The finding that separating language and action prediction loss can improve decision-making is a significant contribution that provides valuable insights into how VLAs can be effectively trained. It is encouraging to see that this is empirically demonstrated to be useful in self-driving scenarios. However, it is concerning that introducing some language noise into the training dataset can have a considerable impact on decision-making processes. Since real-world datasets will inevitably contain substantial noise, developing methods to ensure robustness against such noise is essential for the model's practical application.

### Weaknesses
 - I don't quite understand why VLAs need to chat based on the author's motivation. Chatting is an inherently multi-turn conversation with a specific topic, but example of such capability of the model is completely lacking. I wonder what the authors' definition of chatting is. The model doesn't actually "chat" but simply outputs action description. It is far from the example in the introduction where authors want to build a model that can talk with a friend while driving.
- Text generation has already been explored with DriveGPT4. In this paper, text generation is not used for any novel applications other than simply translating action tokens into language. I fail to understand why does the author claim text+action generation is something novel since there's already a model that does it.
- Adding chat capabilities could potentially make the model less robust when exposed to noise in language interactions. Since the model learns to associate language with specific action tokens, any slight disruption to that association (e.g., due to noise) could significantly impair its action prediction performance. If the model can engage in unrestricted conversation, it is likely to encounter more noise, which could seriously affect its decision-making abilities, which is the most important goal of VLAs. It might be more effective for VLAs to focus solely on action prediction and incorporate chat functionality with separate models. With the current motivation, it seems there is no strong rationale or necessity to integrate chat capabilities into VLAs.
- Following the point above, I feel like the paper could be better framed on how to manage loss when training VLAs, which is a much interesting topic.

Typo: Figure 1 interatcion

### Questions
- How does the model compare to DriveGPT4 and why does DriveGPT4 do so bad? DriveGPT4 is doing exactly same thing as this model aims to do (text generation + action generation).
- Why are there no use case of the model actually chatting? How do the authors define chatting? The example of the introduction mentions the authors are inspired by human driver talking to a friend while driving, but the model doesn't actually engage in free form chat that goes beyond a single step.
- How does author plan to make the model robust to noise when exposed to unrestricted chat?
- Why should we add language generation capability to VLAs? The motivation for that seems non-existent in this paper and there's no novel use case of the generated language.
- Why do the authors think using separate loss for language and action generation (unlike DriveGPT4) improves the decision making performance?
- Why do the authors only focus on the self-driving task?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper opposed to simulating MLLMs as human in a real-world situation that require both chatting and decision making. For example, human drive can drive safely while having conversations with passengers. This is an important application problem in autonomous driving system.

### Strengths
1. The problem that developing a chatting and simultanenous decision making, itself is underexplored and important.
2. The proposed model gives both reasonable question answering output and reasonable action output.

### Weaknesses
1. I don't buy the idea that by simply concatenating the question answer data and action prediction data together and supervised finetune the LLaVA-like MLLM can solve the proposed problem. As described in the abstract, driving and chatting simultaneously, however the proposed LLM-based model is autoregressive decoding. From the architecture overview, we can see this proposed model can only provide a prediction after a very long answer output. No inference speedup or simultaneous decoding technology is being used or proposed to achieve this.
2. The only contribution to me seems combining action prediction and question answer data, which is very trivial. No siginificant improvement is achieved compared with specialist model in each single task. And the approach to combine these two tasks chatting and decision making tasks are not actually achieving prediction both but sequentially.
3. The paper neeeds to be revised in the writing. Such as notions in Figure 1 is totally missing. Training and architecture details are missing in Experiments section, etc.

### Questions
1. What is the average number of images per training and inference case?

### Soundness
1

### Presentation
2

### Contribution
2
