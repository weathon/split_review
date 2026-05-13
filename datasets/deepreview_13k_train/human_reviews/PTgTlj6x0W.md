# TREANT: Red-teaming Text-to-Image Models with Tree-based Semantic Transformations

- Decision: Reject
- Scores: 8, 6, 5, 6

## Abstract
The increasing prevalence of text-to-image (T2I) models makes their safety a critical concern. Adversarial testing techniques have been developed to probe whether such models can be prompted to produce Not-Safe-For-Work (NSFW) content. Despite these efforts, current solutions face several challenges, such as low success rates, inefficiency, and lack of semantic understanding. To address these issues, we introduce TREANT, a novel automated red-teaming framework for adversarial testing of T2I models. The core of our framework is the tree-based semantic transformation. We employ semantic decomposition and sensitive element drowning strategies in conjunction with Large Language Models (LLMs) to systematically refine adversarial prompts for effective testing. Our comprehensive evaluation confirms the efficacy of TREANT, which not only exceeds the performance of state-of-the-art approaches but also achieves an overall success rate of 88.5% on leading T2I models, including DALL·E 3 and Stable Diffusion.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed red-teaming framework for adversarial testing of T2I models to detect their ability to generate NSFW content. Specially, the proposed TREANT utilizes  tree-based semantic transformations to systematically refine adversarial prompts for effective testing.

### Strengths
1. The proposed method is able to adjust and refine prompts using semantic decomposition and sensitive element drowning enhances its practical utility and effectiveness.
2. The experimental results demonstrate the efficacy of TREANT through comprehensive evaluations, achieving an overall success rate of 88.5% on leading T2I models like DALL-E 3 and Stable Diffusion.

### Weaknesses
1. Missing related work white-box adversarial prompt attack baselines such UnlearnDiffAtk [1], which is even able to enforce unlearned T2I model to generate images containing harmful contents.

2. To demonstrate scalability, it is better to add time efficiency as one main evaluation metric.

### Questions
Check weakness section

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
I think this paper is targeting at an important problem and the method seems to be very effective. More specifically, this paper presents TREANT, a tool for testing text-to-image (T2I) models to see if they can produce inappropriate content. TREANT works by changing sensitive words in prompts to less sensitive ones and adding harmless details to help avoid safety checks. This approach has a high success rate of 88.5% in getting T2I models to generate unwanted images, performing better than other methods. The tool aims to improve how we evaluate the safety of these models.

### Strengths
The TREANT framework has several strengths that make it effective for testing text-to-image (T2I) models. It achieves a high success rate of 88.5% in generating unwanted content, demonstrating its reliability. 

TREANT operates automatically, allowing for quick and easy testing without manual effort. It uses smart techniques to bypass safety checks on both text and images while maintaining the original meaning of prompts. The organized tree structure helps manage prompts efficiently, reducing wasted queries. 

Additionally, it has been thoroughly tested across various scenarios, proving its robustness, and the authors provide open access to their code and data for others to use.

### Weaknesses
1. It would be great if the authors could include more qualitative results in their paper because it would really help us understand how well TREANT performs. The success rate of 88.5% sounds impressive, but sharing some specific examples of the images generated would give us a clearer idea of what’s going on. It would be useful to see the types of content TREANT produces and how it handles different situations. I get that safety concerns might limit what they can show, but if they can share more examples, it would definitely make the paper more engaging and helpful for readers. E.g. in figure 7 it would be better if more examples can be shown for a more convincing conclusion,

2. And more analysis together with the qualitative results could be more helpful.

3. Besides, while TREANT is trying to improve scalability, it would be really helpful to talk more about how well it can work with different models and handle prompts that are more complex than the ones they tested.

### Questions
See the weakness for the questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces TREANT, a novel automated red-teaming framework designed to enhance adversarial testing of T2I models. It utilizes tree-based semantic transformations, semantic decomposition, and sensitive element drowning strategies, leveraging LLLMs to refine adversarial prompts. TREANT demonstrates superior performance in generating NSFW content on DALL·E 3 and Stable Diffusion.

### Strengths
1. Red-teaming T2I models is an important topic to investigate. It is also a practical issue.
2. Overall, this paper is easy to follow and well-organized.
3. The proposed method is easy to implement and can perform black-box red-teaming, which should be efficient.

### Weaknesses
For method:

1. The proposed method lies in the category of prompt engineering, unaware of the T2I model and without any black-box optimization strategy. I fail to see clear novelty compared to token replacement and insertion. Especially, in some cases, this method performs worse than BAE or even SneakyPrompt.
2. It would be better if the authors provided any form of guarantee or evidence showing the proposed algorithm can cover more possible prompts toward NSFW semantics.
3. It is misleading that the proposed method is designed to bypass image safety filters. However, GPT-4o is used to check whether NSFW content is generated, which means GPT-4o can serve as a good image safety filter to drop all the malicious prompts generated by TREANT.

For evaluation and comparison:

4. The paper fails to include important baselines, such as MMA-Diffusion: MultiModal Attack on Diffusion Models. Yang et al. CVPR 2024.
5. Only unprotected models are considered, the authors are encouraged to investigate the effectiveness of models such as Safe Latent Diffusion: Mitigating Inappropriate Degeneration in Diffusion Models. Schramowski et al. CVPR 2023.
6. Please try to include DiT-based models like PixArt-α: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis. Chen et al. ICLR 2024.
7. Please consider more image safety filters for evaluation, and also check the attack transferability.

### Questions
1. For red-teaming, a white-box attack should also be acceptable. Is there any special case for the need for black-box attacks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces an automated black-box red-teaming framework designed for adversarial testing of T2I models. The proposed method leverages a tree-based semantic transformation approach to recursively refine prompts, aiming to bypass both text and image safety filters. Two key red-teaming strategies semantic decomposition (probe text safety filter) and sensitive element drowning (probe image safety filter) are applied to transform sensitive prompts into adversarial ones.

### Strengths
- The paper provides a clear and understandable explanation of how T2I model safety mechanisms work, especially focusing on DALL·E 3, which is widely regarded as difficult to jailbreak.
- The high success rate in jailbreaking DALL·E 3 is impressive, showcasing the method's robustness and effectiveness.
- The introduction of the Prompt Parse Tree (PPT) and the recursive editing process to construct adversarial prompts is a novel and interesting approach.
- The method may prove to be query-efficient, which could be beneficial for practical applications.

### Weaknesses
 - The method of semantic decomposition could benefit from further clarification (e.g., in line 253 you say you query the T2I model, but in your algorithm you query LLM, so which do you query). It would be helpful to provide more details on how this process works, specifically how the LLM is prompted to perform the decomposition and what constraints are placed on the output structure. For example, what specific instructions are given to the LLM to ensure a consistent and useful decomposition of the prompt, and how is the depth of the tree controlled?
- The construction of the Prompt Parse Tree (PPT) is interesting, but it’s not fully clear why it’s beneficial for the method. Could strategies like semantic decomposition and sensitive drowning be performed without the need for PPT? Explaining why PPT is essential would strengthen the argument. For instance, could a simpler flat representation of the prompt, with identified sensitive elements, be sufficient for the proposed transformations? What specific advantages does the hierarchical structure of the PPT offer over such a flat representation in terms of efficiency or effectiveness?
- The comparison baselines in the experiment section could be expanded. Testing against more robust safety mechanisms, such as those in Stable Diffusion variants like ESD [R1], SLD [R2], and others, would provide a more convincing case for the method’s effectiveness. It would be beneficial to see how the method performs against defenses that specifically target adversarial attacks, rather than just relying on general safety filters.
- The method seems to be tailored specifically to DALL·E 3, which raises questions about its generalizability to other T2I models. More evaluation on different models could be valuable. Specifically, it would be useful to understand how the performance varies across models with different architectures and training datasets, and whether the method’s effectiveness is tied to specific characteristics of DALL·E 3's safety mechanisms.

### Questions
- Clarification on what you mean by "misleading the safety filter" as opposed to "bypassing" it? A clear distinction would be helpful, since you state that your method generated adversarial prompts that actually bypass the safety filters of T2I models.
- How do you convert the PPT back into a prompt (your final adversarial prompt) after decomposition? Is this done manually or through an automated process, such as querying a LLM?
- Provide further clarification on how the method determines whether the adversarial prompt is blocked by the text filter or the image filter, as different red-teaming strategies are triggered in your method.
- Your method seems to rely heavily on querying a LLM for constructing the PPT, performing semantic decomposition, and implementing sensitive drowning. More details on how you ensure the LLM accurately understands the task, particularly in terms of constructing the PPT correctly?
- Since models like SD1.4, SD2.1, and SDXL have weaker safety mechanisms compared to DALL·E 3, it would be helpful to provide more explanation on why the results for these models are not better than the baselines. The mention of these T2I models potentially not understanding the structural information of the language need more elaboration. Is your generated adversarial prompts somewhat different from your baselines?
- In Table 1, the success rate of TREANT-SED appears quite low. It might be useful to discuss this in more detail, particularly since TREANT-SED employs prompt dilution (adding non-sensitive information into the prompt), which has been shown to be effective in many prior studies.

### Soundness
3

### Presentation
3

### Contribution
2
