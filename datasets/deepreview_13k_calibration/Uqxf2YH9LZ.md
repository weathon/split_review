# BDetCLIP: Multimodal Prompting Contrastive Test-Time Backdoor Detection

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Multimodal contrastive learning methods (e.g., CLIP) have shown impressive zero-shot classification performance due to their strong ability to joint representation learning for visual and textual modalities. However, recent research revealed that multimodal contrastive learning on \emph{poisoned} pre-training data with a small proportion of maliciously backdoored data can induce backdoored CLIP that could be attacked by inserted triggers in downstream tasks with a high success rate. To defend against backdoor attacks on CLIP, existing defense methods focus on either the pre-training stage or the fine-tuning stage, which would unfortunately cause high computational costs due to numerous parameter updates and are not applicable in the black-box setting. In this paper, we provide the first attempt at a computationally efficient backdoor detection method to defend against backdoored CLIP in the \emph{inference} stage. We empirically find that the visual representations of backdoored images are \emph{insensitive} to both \emph{benign} and \emph{malignant} changes in class description texts. Motivated by this observation, we propose BDetCLIP, a novel test-time backdoor detection method based on contrastive prompting. Specifically, we first prompt the language model (e.g., GPT-4) to produce class-related description texts (benign) and class-perturbed random texts (malignant) by specially designed instructions. Then, the distribution difference in cosine similarity between images and the two types of class description texts can be used as the criterion to detect backdoor samples. Extensive experiments validate that our proposed BDetCLIP is superior to state-of-the-art backdoor detection methods, in terms of both effectiveness and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed BDetCLIP to defend against backdoor attacks on CLIP. Different from cuttent methods, this is the first attempt at a computationally efficient backdoor detection method in the inference stage. The experiments show that BDetCLIP performs well in terms of both effectiveness and efficiency.

### Strengths
-	This paper proposed a inference-stage method, which does not access to the pre-traing or finetuning, and also the training data.
-	The method is well-motivated, i.e., the visual representations of backdoored images are insensitive to both benign and malignant changes in class description texts. 
-	Overall, the ablation studies are well-organized, illustrating the effectiveness of the proposed method.

### Weaknesses
 - This paper only focused on the classification task, assuming that there a closed category space. However, VLMs are good at open-set classification tasks.
- The authors introduce a method that helps to choose the threshold $\epsilon$ in Appendix B. However, the selection method requires a small set of clean validation data. It would be better to include the sensitivity analysis of the threshold $\epsilon$ to show the robustness of $\epsilon$.
- The investigation of adaptive attack is missing. Since the proposed defense is based on the property of backdoor samples, it is necessary to go deep into adaptive attacks.

### Questions
Please see the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents BDetCLIP, a novel method for detecting backdoored samples in multimodal contrastive learning models during the inference time. The proposed method is computationally efficient and effective.

### Strengths
1. The paper considers a novel scenario that detects backdoors in inference time for MCL. The proposed method is efficient and effective.
2. The authors conduct extensive experiments on multiple datasets and diverse attack types. The results demonstrate that BDetCLIP outperforms existing detection methods (e.g., STRIP, SCALE-UP, TeCo) in both effectiveness and efficiency.

### Weaknesses
1. **Clarity of Methodology**

(1) **Motivation Lacks Depth**
The authors base their proposed approach on a single observation: “the distribution difference of backdoored images between the benign and malignant changes of class prompts is smaller than that of clean images.” In my view, this constitutes an insufficient contribution. The paper does not explain the underlying mechanism of this phenomenon, making it hard to validate whether this observation holds across different attack scenarios. Specifically, the paper lacks a discussion on why backdoor triggers, which are designed to be effective across different prompts, would exhibit this behavior. The authors need to provide a more detailed explanation of the interaction between backdoor triggers and the contrastive learning framework to justify their core assumption.

(2) Furthermore, the authors have not provided theoretical validation regarding the hyperparameter m and its relationship with $\epsilon$; instead, they rely solely on empirical evidence to suggest that their method outperforms existing unimodal detection approaches. This lack of theoretical grounding renders the method less solid. The paper should include an analysis of how the number of benign prompts, $m$, affects the sensitivity of the detection method and how this relates to the chosen threshold $\epsilon$. Without this, it is unclear how to choose these parameters for optimal performance in different scenarios.

(3) Additionally, the authors have not assessed the detection capabilities of their proposed method against adaptive attacks. Consequently, the reliability of the proposed approach against different types of backdoor attacks comes into question. It is crucial to evaluate the method against attacks that are specifically designed to evade detection, such as those that use dynamic triggers or adversarial perturbations. The absence of such experiments leaves a gap in understanding the robustness of the proposed method.

2. **Insufficiency of Experiments**

(1) Although the authors claim to be the first to propose a detection method for CLIP during the inference phase and assert that the costs of fine-tuning defense methods are higher than those for inference-stage detection, this does not justify the absence of comparisons with existing defense methods. Both defense and detection share the common goal of preventing backdoor attacks. If defenses are indeed more effective than detection methods, then it is unlikely that practical applications would forgo defenses due to cost concerns. The authors argue that the metrics for the two approaches differ; however, I believe they could establish a specific threshold to convert detection results into Attack Success Rate (ASR) for a more direct comparison with existing defense methods. Without this, the authors cannot substantiate the superiority of their proposed method. The paper needs to demonstrate how the detection method's performance translates into a reduction in the attack success rate, which is a more practical metric for evaluating the effectiveness of a defense.

(2) The authors predominantly use AUROC to evaluate the effectiveness of their method, which is insufficient for assessing the impact on model performance. I recommend that the authors include additional metrics, such as precision and accuracy, to demonstrate the method's effects on normal model performance. The paper needs to show how the detection method affects the overall model accuracy and precision, especially when a threshold is applied to filter out potentially backdoored samples. The trade-off between detection performance and model utility should be clearly presented.

(3) Moreover, I believe the use of BadNet and Blended in the main experiments is inadequate. Given that the focus of this research is on multimodal contrastive learning, both BadNet and Blended are unimodal methods. The authors should compare their method against more recent multimodal contrastive learning attack methods to showcase its advantages. While the authors do compare against BadCLIP in Table 6, the low AUROC raises the question of whether the proposed method is less effective for detecting multimodal backdoor attacks. The paper should include experiments with more sophisticated multimodal backdoor attacks that are specifically designed to target CLIP models. This would provide a more comprehensive evaluation of the method's capabilities.

(4) Dependency on Large Language Models: The reliance on models like GPT-4 for generating prompts could introduce significant computational costs. While the paper mentions the feasibility of using open-source alternatives, it lacks detailed evaluations comparing the performance of these alternatives against GPT-4-generated prompts.

### Questions
Please see the Weaknesses for the identified issues.

### Soundness
2

### Presentation
2

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
This paper introduces a new method for detecting backdoors in CLIP models at test time. The main idea is to use how backdoored samples remain insensitive to changes in text descriptions. The method generates two types of prompts with LLMs and measures the difference in cosine similarities between images and these prompts to detect backdoors. It's efficient because it doesn't require parameter updates.

### Strengths
- The paper highlights a key gap in current backdoor defenses for multimodal models:  
  - While previous methods focus on training or fine-tuning, which require high computational costs, test-time detection hasn't been explored yet. This leads to a new research direction that's both interesting and practical.

- The contrastive prompting mechanism is effective because:
  - It uses the multimodal features of CLIP, addressing a limitation of previous unimodal detection methods that ignore the text modality.
  - The use of benign and malicious prompts provides a natural way to measure semantic sensitivity without modifying the model.

### Weaknesses
 - The method relies on the assumption that backdoor samples are insensitive to changes in text descriptions while clean samples are sensitive. However:
  - Limited Analysis of Multi-target Attacks: The analysis only covers single-target backdoor attacks. If backdoor triggers cause different outputs based on context (e.g., indoor vs outdoor scenes), the assumption of semantic insensitivity may not hold, exposing a gap between simplified models and real-world cases. Furthermore, the method's effectiveness against multi-target attacks, where multiple classes are targeted by the same trigger, is not explored. This is a critical omission as real-world backdoors are likely to be more complex than single-target scenarios, and the method's ability to generalize to such cases is unclear.
  - Simplified Trigger Representation: Current assumption: $x^*=(1-M) \odot x+M \odot \Delta$, where $\Delta$ is a simple pixel-pattern trigger. Modern backdoor attacks may use semantic-level triggers that naturally align with textual descriptions, yet the paper does not analyze how this alignment impacts the distribution difference  $\Omega(x)$. This is a significant limitation because semantic triggers could potentially circumvent the proposed detection mechanism by exhibiting sensitivity to text changes, thus invalidating the core assumption of the method. The paper needs to address how the method would perform against triggers that are not simple pixel patterns but rather semantically meaningful perturbations.

- Prompt Quality Variation: There is no mechanism to ensure prompt quality is consistent across different categories or evaluations, and no metrics to assess prompt quality. The effect of prompt variation on detection reliability is also not examined. The method's reliance on LLM-generated prompts introduces a potential source of variability and bias. The lack of a systematic approach to evaluate and control prompt quality could lead to inconsistent detection performance across different categories and experimental runs. The paper should include a more robust analysis of how prompt variations affect the reliability of the detection mechanism.
- Gaps in Theory: There’s no clear definition of what makes a “good” prompt, nor an analysis linking prompt properties to detection performance. The absence of a theoretical framework to guide prompt selection and to explain the relationship between prompt characteristics and detection performance is a significant gap. Without a theoretical understanding, it is difficult to optimize the method or to predict its behavior under different conditions. The paper should provide a more rigorous analysis of the prompt properties that contribute to effective backdoor detection.

### Questions
- Considering the complexity of semantic-level backdoor attacks:
  - Have you considered scenarios with semantically meaningful triggers?
  - How would your method handle triggers that respond naturally to changes in prompt semantics?

- How do you ensure prompt quality consistency across different categories, runs, and LLM implementations?

- Have you considered a framework for assessing prompt quality, looking at:
  - Coverage of category-specific features,
  - Distinctiveness from other categories,
  - Stability across different prompts?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents BDetCLIP, a novel test-time backdoor detection method for multimodal contrastive learning models like CLIP. The approach leverages contrastive prompting to differentiate between clean and backdoored images by analyzing the distribution differences in cosine similarity with benign and malignant class description texts. Extensive experiments demonstrate the method's superior effectiveness and efficiency compared to state-of-the-art detection methods.

### Strengths
The authors claim that this is the first work on backdoor detection during the inference phase.
The paper introduces a novel approach by using contrastive prompting, which is innovative and leverages the strengths of large language models.
This work offers a computationally efficient solution for real-world applications, surpassing previous methods by large margins.

### Weaknesses
The experiments focus on specific attack types and large multimodal models. Including a broader range of attacks and models could enhance the robustness of the evaluation.
Some technical aspects, such as the choice of thresholds and specific parameter settings for both CLIP and attack methods, could be explained in greater detail. 
While the method is computationally efficient, its applicability in highly dynamic environments or with evolving backdoor techniques might require further exploration. Discussing potential challenges and solutions for such scenarios could improve the work's practical relevance.

The method looks overly reliant on large language models like GPT-4 to generate class-specific prompts. Is the key to the apparent effectiveness of the method in how well a prompt is designed?

Are the clean samples used for detection the same as those used for threshold selection? Additionally, was the complete validation set used when selecting the threshold?

Attack concerns: (a) Why use BadNet-LC and Blended-LC instead of the original version LC? (b) The number of selected backdoor classes (3, 1, 1, respectively) is not sufficient compared to the total number of classes in the dataset. (c) The range of attack methods requires further inclusion, e.g., IAD and WaNet. (d) More detailed attack settings should be provided.

Experimental results concerns: (a) In table 1, why is the performance of TeCo on Blended and Blended-LC higher in certain cases? (b) For BadCLIP attack, the performance order of the three comparative detection methods seems to be completely opposite to the previous results. (c) Why did the AUROC increase after incorporating CleanCLIP? The model after defense should be more similar to a clean model, thereby reducing the backdoor effect. (d) In table 9, the AUROC of Blended-LC decreases when using contrastive prompts.

### Questions
The method looks overly reliant on large language models like GPT-4 to generate class-specific prompts. Is the key to the apparent effectiveness of the method in how well a prompt is designed?

Are the clean samples used for detection the same as those used for threshold selection? Additionally, was the complete validation set used when selecting the threshold?

Attack concerns: (a) Why use BadNet-LC and Blended-LC instead of the original version LC? (b) The number of selected backdoor classes (3, 1, 1, respectively) is not sufficient compared to the total number of classes in the dataset. (c) The range of attack methods requires further inclusion, e.g., IAD and WaNet. (d) More detailed attack settings should be provided.

Experimental results concerns: (a) In table 1, why is the performance of TeCo on Blended and Blended-LC higher in certain cases? (b) For BadCLIP attack, the performance order of the three comparative detection methods seems to be completely opposite to the previous results. (c) Why did the AUROC increase after incorporating CleanCLIP? The model after defense should be more similar to a clean model, thereby reducing the backdoor effect. (d) In table 9, the AUROC of Blended-LC decreases when using contrastive prompts.

### Soundness
2

### Presentation
3

### Contribution
2
