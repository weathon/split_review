# You Only Look at Screens: Multimodal Chain-of-Action Agents

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Autonomous graphical user interface (GUI) agents aim to facilitate task automation by interacting with the user interface without manual intervention. Recent studies have investigated eliciting the capabilities of large language models (LLMs) for effective engagement in diverse environments. To align with the input-output requirement of LLMs, most existing approaches are developed under a sandbox setting where they rely on external tools and application-specific APIs to parse the environment into textual elements and interpret the predicted actions. Consequently, those approaches often grapple with inference inefficiency and error propagation risks. To mitigate the challenges, we introduce Auto-GUI, a multimodal solution that directly interacts with the interface, bypassing the need for environment parsing or reliance on application-dependent APIs. Moreover, we propose a chain-of-action technique---leveraging a series of intermediate previous action histories and future action plans---to help the agent decide what action to execute. We evaluate our approach on a new device-control benchmark AITW with 30$K$ unique instructions, spanning multi-step tasks such as application operation, web searching, and web shopping. Experimental results show that Auto-GUI achieves state-of-the-art performance with an action type prediction accuracy of 90\% and an overall action success rate of 74\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a multimodal work for Auto-UI, it proposes to leverage the chain-of-action (including previous history actions and future actions) for model prediction. Their model builds on the top of Llama 2 with an image encoder (for screen image). Empirical experiments on the AITW dataset shows very promising results.

### Strengths
1. This work proposes a chain of action operation, leveraging the action history and future actions for current action prediction.
2. Based on Llama 2, it incorporates a pretrained image encoder into the pretrained LLM for action decision, and shows promising results on AITW dataset.

### Weaknesses
1. A potential weakness is where is the gain from? It looks PaLM and ChatGPT are pretty low on this dataset, while they only take text input, and BC models and Auto-UI models take image screen as input, and get very high results, it is unclear where is the gain from? image encoder? or a chain of action input?

### Questions
I try to understand the setting of the experiments, and why the strong PaLM and ChatGPT baselines are so low. Based on the main Table 2, it looks the most gain is from the image encoder, right? Since PaLM-CoT and ChatGPT-CoT only take text input, and their performance is pretty low, and also similarly for Llama 2. Is this right? Probably needs a baseline/ablation to see the performance of model without image encoder.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an autonomous UI agent called Auto-UI that can interact in a multimodal UI environment without environment parsing or application-dependent API access. Specifically, it proposes a chain-of-action technique to help the agent make decisions.

### Strengths
1. It is novel that the paper pays attention to the limitations in the real-world applications of autonomous agents and seeks to provide an agent that does not need extra intermediate environment parsing or interval application-dependent APIs.

2. The paper proposes a chain-of-action technique which helps the agent to decide step-by-step.

### Weaknesses
1. The Figure 1 in this paper is somewhat not clear enough, making it difficult to understand the two paradigms in (a) and (b).

2. The author does not provide a specific explanation of the Sandbox Paradigm and the First Principles Thinking Paradigm, which is confused. 

3. We find some grammar mistakes in the paper, for example, on page 2, paragraph 2, line 5, do you want to express inefficiency instead of efficiency?

4. The authors don't explain exactly what touch_point, lift_point, etc. mean in the first place, causing some confusion.

5. The authors do not provide a specific example between Auto UI and other baselines in Section 5, which is not clear to understand the effectiveness of the provided Auto UI.

### Questions
In Section 4.3, why do you use 14% instead of other number to evaluate the correction of a click action, could you provide some references?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a “chain-of-action” approach to tackle the autonomous web-searching agent problem. Specifically, they propose a multimodal framework that firstly encodes both the language goals and the web-interaction histories, as well as the screen images, into a combined representation, where a decoder will generate a look-ahead future action plan and a formatted immediate next action to perform.
The authors conducted experiments on the AITW dataset where an AI agent is tasked to interact with a Web UI following certain goals, where they demonstrate the effectiveness of the proposed models against three major baselines.

### Strengths
- The proposed framework is claimed to be much lighter weight than methods that try to take the whole web information into textualized format for agents to comprehend.
- The formatted action is sound and should be generalizable to other web-search domains.
- The paper is pretty easy to follow, with illustrations onto the points.
- The generalization ablation studies are helpful to gauge the capacity of the proposed framework.

### Weaknesses
- The paper does not describe much about the actual training details, in that sense, to me, the proposed method is still a kind of BC, where the target decoding is optimized towards mimicking the golden action sequences. (Unless some RL or other mechanism is used here, which is not described.) In my opinion, the novelties here mainly lie in the multimodal representations (both modality taken into account) and the format of the action performed.
- I’m a bit skeptical about the ICL baseline, first of all more details (e.g., how actions are represented, how OCRed results are used) of that baseline need to be described, at least in the appendix. Secondly, it also needs to be evaluated at the action plan level, my guess is that this method should be quite accurate on those but might fail more on the lower-level executions. Thirdly, it is indeed unfair simply because the model is not taking the images into account, which could be the key towards the success of the proposed method in this work. So, at least a multimodal version of it needs to be taken into consideration, or, a better spatial representation of the html syntax is required. (HTML can be many times too coarse to represent a spatial layout.)
- Similar to above, the third baseline, fine-tuning LLMs, need to have a version with multimodal inputs.
- An error analysis is required both on the quantitative and qualitative sides, what are the major errors that these models exhibit?

### Questions
- I’m a bit surprised that the language decoder is able to predict tokens as precisely as four decimal places, or is the actual precision here not important? I.e., could you not simply split image screens into patches and just use their centers as the coordinate representations? (And the more patches you grid the screen, the more precise it would be.)
- What are the main types of errors observed by the proposed framework? And, does the framework provide good insights on how to assign these errors to specific modules? I.e., where should the improvements be?

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes Auto-UI, a multimodal solution that directly interacts with the interface, which eliminates the need for environment parsing or reliance on application-specific APIs. The authors introduce a chain-of-action technique that incorporates previous action histories and future action plans to guide the agent's decision-making process. The approach is evaluated using a device-control benchmark called AITW, which consists of 30,000 unique instructions covering tasks like application operation, web searching, and web shopping. Experimental results demonstrate that Auto-UI achieves state-of-the-art performance, with high accuracy in predicting action types (90%) and an overall success rate of 74%. The authors have made the code available for review.

### Strengths
1. The proposed Auto-UI approach demonstrates a level of originality in addressing the challenges of autonomous user interface agents. By directly interacting with the interface instead of relying on environment parsing or application-specific APIs, it offers a novel solution that bypasses common inefficiencies and risks associated with existing approaches. The introduction of the chain-of-action technique also adds a unique element to the decision-making process of the agent.
2. The approach is evaluated through experiments with the AITW benchmark. The inclusion of 30,000 unique instructions covering various multi-step tasks provides a comprehensive assessment of the Auto-UI system. Achieving a state-of-the-art performance demonstrates the effectiveness and reliability of the proposed solution.
3. Overall, the paper is clear and easy to follow. The text provides a clear description of the challenges faced by existing approaches, introduces the Auto-UI solution, and explains the chain-of-action technique. The inclusion of experimental results contribute to a clear understanding of the proposed methodology and its performance.
4. By addressing the challenges of inference inefficiency and error propagation, Auto-UI offers a more efficient and reliable approach to task automation. The multimodal solution and the elimination of environment parsing and reliance on application-specific APIs provide a significant advancement in the development of autonomous UI agents. Furthermore, the state-of-the-art performance achieved on the AITW benchmark showcases the practical applicability and potential impact of the proposed approach.

### Weaknesses
1. While the authors highlight the chain-of-action technique as a contribution, it appears to primarily concatenate the output actions, which can be confusing. It would be helpful to provide a more detailed explanation or clarification of how the chain-of-action technique enhances the decision-making process and contributes to the overall effectiveness of the Auto-UI approach.

2. The experiment section lacks an explanation for the rationale behind selecting specific baselines. It would be valuable to include a justification for choosing the particular baselines used in the evaluation. Additionally, providing information on the performance of a GPT4 model, if available, would offer a useful benchmark to compare the performance of the proposed Auto-UI approach.

### Questions
GPT4 is reported to possess significantly improved agent capabilities compared to existing LLMs. However, it is important to note that the specific performance metrics and details of GPT4 have not been provided in the given context. Therefore, the performance of GPT4 remains unclear and unavailable for direct comparison in this discussion. What is the performance of GPT4?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
