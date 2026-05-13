# Tracking the Copyright of Large Vision-Language Models through Parameter Learning Adversarial Attacks

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Large vision-language models (LVLMs) have demonstrated remarkable image understanding and dialogue capabilities, allowing them to handle a variety of visual question answering tasks. However, their widespread availability raises concerns about unauthorized usage and copyright infringement, where users or individuals can develop their own LVLMs by fine-tuning published models. In this paper, we propose a novel method called Parameter Learning Attack (PLA) for tracking the copyright of LVLMs without modifying the original model. Specifically, we construct adversarial images through targeted attacks against the original model, enabling it to generate specific outputs. To ensure these attacks remain effective on potential fine-tuned models to trigger copyright tracking, we allow the original model to learn the trigger images by updating parameters in the opposite direction during the adversarial attack process. Notably, the proposed method can be applied after the release of the original model, thus not affecting the model’s performance and behavior. To simulate real-world applications, we fine-tune the original model using various strategies across diverse datasets, creating a range of models for copyright verification. Extensive experiments demonstrate that our method can more effectively identify the original copyright of fine-tuned models compared to baseline methods. Therefore, this work provides a powerful tool for tracking copyrights and detecting unlicensed usage of LVLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper tackles the problem of unauthorized usage and copyright infringement of LVLMs due to unlicensed fine-tuning of publicly available models. It proposes a method called Parameter Learning Attack (PLA) to address this issue by enabling copyright tracking without modifying the original model. PLA employs an adversarial attack to generate trigger images that produce distinct outputs for copyright verification. To enhance robustness, it involves adjustment of model parameters, ensuring the trigger images remain effective even on fine-tuned versions. This approach is non-intrusive, as it can be applied post-release without impacting the model’s performance. Experiments simulating real-world fine-tuning scenarios, show that PLA outperforms baseline methods in accurately identifying original ownership. It offers a solution for detecting unauthorized LVLM usage.

### Strengths
The proposed approach PLA offers several valuable strengths:
- is a non-intrusive way of copyright tracking
- generates robust trigger images that are resistant to model finetuning
- outperforms traditional methods by reliably identifying copyright ownership

The paper is well-written, presenting concepts clearly and systematically.

### Weaknesses
 - PLA’s core innovation involves updating parameters in reverse to increase trigger robustness; however, the paper lacks an in-depth explanation of why this specific approach effectively simulates fine-tuning. The mechanism by which reversing the gradient during adversarial training leads to robustness against fine-tuning is not clearly articulated. It's unclear how this process mimics the actual parameter changes that occur during fine-tuning, and what specific properties of the model are being exploited by this reverse update.
- The experiments focus solely on fine-tuning for VQA tasks, which limits the assessment of PLA’s robustness across broader vision-language tasks. Testing on additional tasks, such as image captioning, visual grounding, or multi-modal classification, would provide a more comprehensive evaluation of PLA's effectiveness in diverse VL applications. The current experiments do not sufficiently demonstrate the generalizability of the proposed method to different types of vision-language tasks, which is crucial for its practical applicability.
- Scalability and Computational Efficiency: Reverse parameter updates during adversarial training may be computationally intensive, raising questions about PLA’s scalability for large models. The paper does not provide a detailed analysis of the computational cost associated with reverse parameter updates, particularly in terms of time and memory requirements. Adding discussion or experiments on PLA’s computational demands, along with potential optimizations, would improve its applicability for real-world use. It is unclear how the computational cost scales with model size and the number of trigger images.
- Limited novelty:  While the paper proposes PLA for copyright tracking, the use of adversarial triggers to mark models has similarities to prior watermarking and adversarial attack research. The paper does not clearly differentiate the proposed method from existing techniques in terms of both the methodology and the specific application to copyright tracking in LVLMs. The novelty of the approach needs to be more clearly established by highlighting the unique aspects of PLA compared to prior work.

### Questions
- Is the statement that "changing the weights in the attention layers has a greater impact on trigger images than altering the weights in the MLP layers" based on empirical observation? Could you provide further reasoning or experimental data to support this claim?
- Have you considered potential vulnerabilities where attackers might detect or circumvent PLA’s adversarial triggers? If so, what measures could be implemented to defend against such countermeasures?
- How does PLA’s approach of reverse parameter updates specifically differentiate itself from existing model watermarking and adversarial trigger methods?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method for tracking the copyright of LVLMs, i.e. detecting whether an LVLM is finetuned from another one. They use adversarial attacks to create trigger images that, when paired with specific questions, elicit predetermined responses from models derived from the original model. The trigger is created in an adversarial training fashion, where the model is fine tuned to resist the attack while the attack is created again on the robustified model. The authors evaluate their method on LLaVA-1.5 across various fine-tuning scenarios and datasets, demonstrating improved detection rates compared to baseline methods.

### Strengths
Problem significance. This paper addresses an important and timely issue in AI model protection.

Writing is generally clear and easy to read.

### Weaknesses
Methodological limitations.
1. The authors do not provide detailed description on which part of the LVLM is being fine tuned. It seems that they only consider language model fine-tuning and ignore vision encoder and adapter fine-tuning, which does not cover the full picture of fine-tuning. The authors should provide analyses on how finetuning different parts of the LVLM influences the detection rate. Specifically, the impact of fine-tuning the vision encoder, the projection layer, and the language model independently and in combination should be explored. Furthermore, the authors should clarify whether they are using LoRA or full fine-tuning for each component, as this can significantly affect the model's behavior and the effectiveness of the proposed method.
2. In line 353, why do you need to enhance the concealment of trigger images? For copyright detection purposes, there is no inherent need for imperceptibility. Arbitrary patterns or even pure noise can work as triggers, since the goal is detection accuracy, not visual stealth. And the perturbation budget of ε=16/255 seems arbitrary, and the author should provide varying levels of perturbation budgets and reveal the trend of detection rate as the budget increases. It is also unclear how the perturbation is applied (e.g., L-inf norm, L2 norm), and whether the perturbation is constrained to a specific range of pixel values.

Insufficient experiments and analyses.
1. This paper does not provide analysis on how to determine the number of steps for adversarial attacks. The authors should provide the detection rate vs the number of attack steps. The authors should also analyze the convergence behavior of the adversarial training process, and how the number of steps affects the quality of the generated triggers. It is crucial to understand if more attack steps always lead to better triggers or if there is a point of diminishing returns.
2. There is no proper treatment of false positives and false negatives. And it is missing ROC curves and threshold analysis. Not clear how this method works in practice. The authors should provide a detailed analysis of the trade-off between true positive rate and false positive rate. The absence of ROC curves and threshold analysis makes it difficult to evaluate the practical utility of the proposed method. The authors should also analyze the impact of different thresholds on the detection performance.
3. Why would model creators prefer post-release triggers than finger-prints implemented during training? This paper shows in table 1 that the proposed method is more effective than training time triggers. It should elaborate more on this aspect by showing more comparisons. The authors should provide a more detailed comparison of the advantages and disadvantages of post-release triggers versus training-time fingerprints, considering factors such as implementation complexity, robustness to various attacks, and impact on model performance.

### Questions
1. Can you show more details of how IF (Xu et al., 2024) is implemented in this paper? Why is IF less effective than the proposed method that does not embed trigger information into the model during training?

1. How does the method handle model ensemble or knowledge distillation?

1. Is this approach still effective when the model stealer finetunes the model using adaptive methods to evade detection?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on identifying whether a model has been fine-tuned based on a publicly released pre-trained visual-language model.
It proposes the use of adversarial data, generated through targeted attacks on the original pre-trained model, to detect outputs from downstream models, thereby assessing potential copyright issues.
To enhance generalization, the paper introduces a Parameter Learning Attack (PLA), which incorporates an adversarial training process to simulate parameter changes in downstream tasks.
Experiments on six downstream VQA datasets show that adversarial data generated by PLA can effectively track the copyright of pre-trained VLMs, achieving satisfactory accuracy.

### Strengths
1. The issue addressed in this paper—copyright tracking for open-source VLMs—is highly significant. The approach of constructing adversarial examples to detect outputs from downstream models provides an insightful solution for identifying unlicensed usage of pre-trained VLMs.
2. The paper is well-structured and easy to follow.

### Weaknesses
1. Although the paper presents a novel scenario, the techniques employed to address the problem are not particularly innovative. The core issue can be understood as constructing adversarial examples with cross-model transferability based on a given pre-trained model through targeted adversarial attacks. This is a widely studied topic in the field of adversarial attacks. While the application of targeted attacks for copyright tracking is indeed creative, the paper overlooks many comparative methods, such as [1]-[5]. I believe that most adversarial attacks focusing on cross-model transferability could be tailored for the task presented in this paper.

2. The paper should evaluate the performance of PLA under varying degrees of model parameter changes. The experiments conducted are limited to relatively simple VQA datasets, where the parameter changes are minimal. If fine-tuning occurs on more complex datasets (such as ScienceQA), the extent of parameter changes may be more substantial. How would PLA perform under such conditions?

### Questions
See in Weaknesses.

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
3

### Summary
The paper propose a method PLA to track copyrights and detect unlicensed usage of LVLMs. The method is to design rare question-answer pairs, and optimize corresponding adversarial images. These adv image-text pairs are used as triggers to detect if the model are copyright infringing. To increase generalization, the paper adds gradient-based updates to model parameters when optimizing adv images.

### Strengths
1) The topic is both significant and practical.

2) The writing is clear and easy to follow.

3) The method is novel and the experiments show a clear increase compared to previous ones.

### Weaknesses
Please refer to the questions.

minor: line 94: traqcking

### Questions
1) The experimental results include finetuning on Llava1.5, ST-VQA, etc. Have the authors tried some other advanced models such as miniGPT4, QWEN2-VL (2b or 7b version), and InternVL (2b version )? What are the results?

2) The paper finetunes the model on certain datasets using both full finetuning and lora. Can the authors provide the performances on relevant benchmarks of the VLMs before and after fine-tuning? This is to check if the fine-tuning is conducted correctly.

3) can the authors also provide the TMR for related and unrelated models? For example, if the image-text pairs are designed for llava1.5, what's the TMR for llava1.6 and for miniGPT4?

I'm willing to raise the score once the questions are addressed.

### Soundness
3

### Presentation
3

### Contribution
3
