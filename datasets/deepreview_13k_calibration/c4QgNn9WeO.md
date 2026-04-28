# LMEye: An Interactive Perception Network for Large Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 3, 5, 8

## Abstract
Training a Multimodal Large Language Model (MLLM) from scratch, like GPT-4, is resource-intensive. Regarding Large Language Models (LLMs) as the core processor for multimodal information, our paper introduces LMEye, a human-like eye with a play-and-plug interactive perception network, designed to enable dynamic interaction between LLMs and external vision information. Previous methods incorporate visual information into LLMs with a simple visual mapping network or Q-former from BLIP-2. Such networks project the image feature once yet do not consider the interaction between the image and the human input query. Hence, the obtained visual information without being connected to human intention may be inadequate for LLMs to generate intention-following responses, which we refer to as static visual information. LMEye addresses this issue by allowing the LLM to request the desired visual information aligned with various human instructions, which we term as the dynamic visual information interaction. Specifically, LMEye consists of a simple visual mapping network to provide the basic perception of an image for LLMs. It also contains additional modules responsible for acquiring requests from LLMs, performing request-based visual information interaction, and transmitting the resulting interacted visual information to LLMs, respectively. In this way, LLMs act to understand the human query, deliver the corresponding request to the request-based visual information interaction module, and generate the response based on the interleaved multimodal information. We evaluate LMEye through extensive experiments on some multimodal benchmarks, demonstrating that it significantly improves the zero-shot performance on various multimodal tasks compared to previous methods, with less parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces LLMEye, a trainable module designed to enable dynamic interaction between LLMs and external vision information. LLMEye employs a two-stage approach for enhanced interaction. The first stage involves feature alignment training, which utilizes a Q-former from BLIP2 and linear projection layers to map image features into text space, capturing static visual information. In the second stage, LLMEye introduces a linear layer and a multi-layer transformer block to facilitate request-based visual information interaction. The paper also presents an evaluation of LLMEye on various multimodal benchmarks, including MME, SEED-Bench, and VQA tasks, alongside a custom evaluation set focusing on VQA tasks with long answers and detailed descriptions.

### Strengths
- The paper presents a variety of evaluation benchmarks and shows the potential of LLMEye
- Extending the capabilities of Multimodal-Models by training lightweight modules is an interesting direction also proposed by previous work (e.g MiniGPT4)

### Weaknesses
 - Figure 1 could be improved a lot. First, I will suggest including and specifying each component of LMEye. Adding this will help the reader to connect the notation mentioned in Section 3.1 and the flow of the figure
- Ablations.
	- It would be beneficial to understand the contribution of the RVII module if authors include ablations with and without that module in MME and SEED-Bench benchmarks.
	- I also suggest specifying the Vision Model and Language Model with their corresponding parameters to have a better and fairer comparison while reading Tables 1 and 2.
	- Add ablations without RVII module in LLMEye (BLIP2) in Tables 3 & 4
	- Why not include the Qwen-VL model? I believe it was already published at the moment of the paper submission.
- Minor:
	- > ... which shows supervisor performances on various multimodal scenarios. (Page 2)

		Should it be "superior"?

### Questions
Please see above weaknesses

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the language-vision tasks by proposing a dynamic attetion-based model that uses human questions/instructions as input to dynamically query visual features for better visual information summarization. The authors claim the method is better than Blip model due to interactive attention and show promising results.

### Strengths
+ The overall motivation of the paper is sound. The authors add dynamic attention to better summarize the information on the visual feature map.
+ The presentation is mostly clear. 
+ The experimental results support the claims.

### Weaknesses
Overall, the paper lacks significant enough contribution to vision and language community:
- The so called "interactive perception model" is actually a standard and common technique used everywhere. Early since attention was proposed, the visual information is dynamically summarized (attended). Some old works on VQA, such as NMN, have extensively used instruction-based condition to process visual information.
- The network/module themselves are also pretty common, and do not convey any significant "direction-shifting" messages.

The paper's writing also needs some improvements. For example, section 3.1 gives way too many engineering details (which should've been put into supplementary) and lacks top-down summarization for easier read.

### Questions
See above.

### Soundness
2 fair

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
This paper proposes a multimodal LLM, LMEye. Different from preivous works using a simple mapping network to coneect vision and LLM, the visual information to LLM of LMEye is language-query conditioned. It first utilizes a LLM to extract the information of both vision and language, followed by a Request-based Visual InformationInteraction module to fuse vision and language signal. Finally the fused information and human queries are fed into another LLM to complete the instruction. The proposed method is evaluated on comprehensive multimodal benchmark like MMBench and SEED-Bench, traditional tasks like VQAv2 and a self-collected QA dataset, where LMEye achieves promising results.

### Strengths
- The motivation and implementation are clear and straightforward. The visual information should interact with language queries in multimodal LLMs. Current MLLMs does not point out this issue but I think it is important for deeper understanding of the visual signal.
- The evaluation on multiple tasks are promising. I believe LMEye can serve as a strong baseline for future works.
- A new VQA dataset with long answer. Traditional VQA datasets are not suitable for current MLLMs since their answers are usually one word or phase, while MLLMs are tend to generate long and detailed answers. So this dataset will motivate the research community to pay more attention to improve MLLM's problem solving capability rather than fitting to traditional VQA benchmarks.

### Weaknesses
 - As the core contribution of the paper, the authors did not carefully explore the contribution of RVII module. For example, the impact of  RVII module under the same data and training process.
- In my view, I think there is no essential difference between RVII and LoRA. LoRA is too insert some parameters inside the LLM , while RVII is more like an Adapter module outside LLM. The authors claim that visual feature from RVII is dynamic and conditioned on human queries. Since the decoding process of LLM are autogressive, a token to be decoded is also conditioned on privous visual tokens and human queries. The LoRA layer will take as input both visual tokens and human queries.

### Questions
- What are the training parameters in the instruction tuning phase?
- Since the visual information needs to be fed into LLM twice, will the model run slower?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Recognizing the challenges of training Multimodal Large Language Models (MLLM) from scratch, the authors propose LMEye, an interactive perception network that acts as a "human-like eye" for LLMs. In contrast to previous methods, LMEye facilitates a dynamic interaction between the LLM and external visual information, akin to Visual LLM Agent . This is accomplished by enabling the LLM to specify the kind of visual information it needs based on the human instructions it receives. The LMEye system is composed of a basic visual mapping network for initial image perception and novel RVII modules that can receive visual information requests from the LLM, process these requests, and subsequently relay the interacted visual information back to the LLM. This method ensures that the LLM not only receives visual data but can actively seek out specific visual information in alignment with human instructions. Experimental evaluations on various multimodal benchmarks reveal that LMEye notably enhances zero-shot performance on diverse multimodal tasks (MM-Bench and SEED-Bench), suppressing prior methods, and doing so with fewer parameters (LMEye-4B vs. MLLMs >7B).

### Strengths
1. Overall Novelty and Contributions: 
The LMEye approach stands out as a monumental stride in the integration of visual perception with LLMs. The unique design of Request-based Visual Information Request (RVII), allowing LLMs to 'request' specific visual information, is both intuitive and groundbreaking, which reflects a deep understanding of how multimodal processing might emulate human brain-like cognition. The motivation is clear and interesting, and the experiments are solid for supporting their ideas. The impressive results on two comprehensive multimodal benchmarks validate the effectiveness of LMEye (less parameters, better results). The section of Discussion and Future Work present the current development of Multimodal Large Language Models and give useful advice for constructing a multimodal language model, such as selecting language models and how to design interaction between human instructions and visual information. This paper might become a foundational reference for future studies about LLMs as the core processor of Multimodal Agent. 

2. Presentation:
The overall description of the paper is clear and the motivation of incorporating human-like eyes for LLMs is novel, different from construction of current multi-modal large model. The extensive experiments including two widely-used benchmarks, other downstream datasets, and self-constructed benchmarks, fully verified the author's motivation and proposed approach. The experimental analysis are solid.

3. Method: 
a. LMEye introduces dynamic visual information interaction between LLMs and objective Visual Information. By recognizing and addressing the gap between static and dynamic visual information processing, LMEye offers a more holistic approach to multimodal understanding. It allows LLMs to actively request and incorporate relevant visual content based on specific human instructions, ensuring a more tailored and context-aware response. By preserving the inherent structure of LLMs, LMEye ensures that their original performance on NLP tasks is not compromised, thereby maintaining the robust generalization abilities of LLMs.
b. A novel Request-based Visual Information Interaction module (RVII) is introduced. This module enables the LLM to understand the basic visual information and human queries, send a request for additional specific visual information, and then construct a response based on the integrated understanding of the image, text instruction, and the interacted visual information. As we know, when humans complete tasks according to instructions, they usually interact with the external environment multiple times. 
c. The whole training process is parameter-efficient and RVII module could be injected into various LLMs, e.g., Llama, Bloom, BLIP-2, and FlanT5-xl. The scalability of the proposed method, LMEye: interactive perception network, is easy and stable.

4. Experiments:
a. Superior Performance with Fewer Parameters: The results from the experiments are commendable. LMEye demonstrates superior performance in multimodal understanding and reasoning when tested on two comprehensive evaluation benchmarks: MMBench and SEED-Bench. What's striking is its ability to outperform other MLLMs while using substantially fewer parameters (4.4B for LMEye vs. >7B for others). This suggests that LMEye isn't an incremental improvement but offers a significant leap in the direction of efficient and effective multimodal modeling.
b. Consistent Improvements in Ablation Studies: Ablation studies further solidify the effectiveness of LMEye. There is a significant improvement in zero-shot multimodal performances across different scales and types of LLMs. The exact gains mentioned, such as a 5.0% improvement on OK-VQA for LMEye (BLIP-2) in comparison to BLIP-2 alone, and a remarkable 20% gain on VQA with long answer for LMEye (LLaMA-7b) against LLaVA (Vicuna-7b), speak volumes about the robustness of the method. This consistency in improvement across different benchmarks and tasks emphasizes the versatility and generalizability of LMEye.
c. The authors present intriguing cases that highlight several noteworthy aspects of their proposed method. These include multi-round interactions between Large Language Models (LLMs) and visual information, showcasing the model's ability to handle multilingual data, as well as its capability for artwork analysis. These examples provide valuable insights into the versatility and potential applications of the proposed approach.
d. The comprehensive Section: Discussion and Future Work in the paper serves as a valuable synthesis of the key steps involved in constructing large multimodal models. It substantiates the claims made by the authors with corresponding experimental evidence.

### Weaknesses
 1. The experimental part should offer a concise description of the structure of LMEye (BLIP-2). Specifically, details regarding the integration of the visual encoder, the Q-former, and the T5-Encoder within the LMEye (BLIP-2) architecture should be clarified. It's unclear how the image representations are translated into the language space and how the probe vector '<img-q>' is utilized to prompt visual information acquisition. A more detailed explanation of the RVII mechanism's role in gathering and enriching visual information is needed to fully understand the model's architecture and information flow.

2. The caption and top line of tables 1 and 2 should be spaced wider. This minor formatting issue detracts slightly from the readability of the results.

3. In the section discussing multimodal instruction-following part, it would be beneficial to provide a more comprehensive description of data, such as a figure. Specifically, elucidating the various categories of images within the dataset would offer readers a clearer understanding of its composition and scope. The current description lacks detail on the specific types of images used (e.g., natural images, artwork, specific object categories) and the distribution of these categories within the dataset. This information is critical for assessing the generalizability of the model.

4. Whether the inference process will consume some time for different types of models, a brief inference efficiency description is given for the design of the LMEye variant for the encoder-decoder and the decoder-only models. The paper should include a discussion of the computational cost and inference time associated with the LMEye variants, particularly when comparing the encoder-decoder and decoder-only models. This is important for practical applications and for understanding the trade-offs between model performance and computational resources.

### Questions
1. See 3 and 4 in Weakness.
2. Would this approach expand to video understanding and provide more detailed description of video and action inference? 
3. To alleviate the Hallucination problem shown in Appendix, could we introduce visual information request during text generation, like ReAct?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
