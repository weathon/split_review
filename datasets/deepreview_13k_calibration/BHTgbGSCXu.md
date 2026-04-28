# Securing Multimodal Large Language Models: Defending Against Jailbreak Attacks with Adversarial Tuning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
While multimodal large language models (MLLMs) have achieved remarkable success in recent advancements, their susceptibility to jailbreak attacks has come to light. In such attacks, adversaries exploit carefully crafted prompts to coerce models into generating harmful or undesirable content. Existing defense mechanisms often rely on external inference steps or safety alignment training, both of which are less effective and impractical when facing sophisticated adversarial perturbations in white-box scenarios. To address these challenges and bolster MLLM robustness, we introduce SafeMLLM, a novel adversarial tuning framework. SafeMLLM operates in two stages during each training iteration: (1) generating adversarial perturbations through a newly proposed contrastive embedding attack (CoE-Attack), which optimizes token embeddings under a contrastive objective, and (2) updating model parameters to neutralize the perturbation effects while preserving model utility on benign inputs. We evaluate SafeMLLM across six MLLMs and six jailbreak methods spanning multiple modalities. Experimental results show that SafeMLLM effectively defends against diverse attacks, maintaining robust performance without compromising normal interactions with users.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel defense framework, SAFEMLLM, that employs the CoE-Attack strategy to craft adversarial embeddings and iteratively refines model parameters, ensuring resilience against attacks while preserving benign input performance. Comprehensive experiments across six multimodal language models and six jailbreak attack techniques validate SAFEMLLM's effectiveness, especially in challenging white-box scenarios.

### Strengths
1. This paper proposes a novel adversarial training framework, SAFEMLLM, and demonstrates its effectiveness across diverse MLLMs and jailbreak methods in white-box scenarios, showcasing robust defense without sacrificing user interaction
2. This paper excels in its writing style, which is fluid, clear, and easy to read.
3. This paper stands out with thorough experimental comparisons across three jailbreak attack scenarios: image-based, text-based, and image-text jailbreak attacks.

### Weaknesses
1. The Introduction could be strengthened by more clearly emphasizing the article's unique contribution, originality, and effectiveness. Currently, these elements are not sufficiently highlighted, which might undermine the article's impact.
2. The proposed framework has limitations as it only considers image and text data, excluding audio, video, and other multimedia types. This narrow focus restricts the framework's applicability to real-world scenarios where diverse multimodal inputs are common. The lack of consideration for temporal data, such as video, is a significant gap, as many jailbreak attacks could exploit vulnerabilities in the temporal processing of multimodal models.
3. Authors fail to provide experimental results demonstrating that their framework can reduce overall computing resources. The paper claims that optimizing adversarial perturbations on both image and text inputs simultaneously is computationally intensive, but this claim lacks empirical support. Without concrete evidence, it is difficult to assess the practical efficiency of the proposed method compared to alternative approaches.

### Questions
1. In Section 4, four datasets were chosen for robustness evaluation. Please explain why the paper selected there four datasets? Please provide criteria and rationale for their authority and suitability. For the LLaVA-Instruct-80K dataset, specifically, why was it chosen to assess the utility of the fine-tuned models? A brief summary of each dataset's relevance in the main text would also enhance readability.
2. The introduction part presents previous work, such as VLGuard, which is effective against black-box attacks but fails to defend against white-box attacks. Please provide further explanations on why this occurs. Specifically, how does an attacker's possession of parameters and gradient information enable them to launch more effective attacks in white-box scenarios, and what are the key points of defense in such cases.
3. Figure 2 presents an overview of the proposed SAFEMLLM framework, with a focus on the first phase, CoE-Attack. In this phase, the paper emphasizes the optimization of two noise metrics: noisy image and noisy text. Are these the only types of noise considered in the SAFEMLLM, or does the framework have the potential to incorporate other modalities such as video and audio? If not, it it better to discuss the limitations of the current approach in terms of its applicability to a broader range of multimodal data?
4. Why are there many missing values for the VLGurad metric in the performance indicators listed in Table 1?

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
This paper presents a novel adversarial training method called SAFEMLLM, aimed at strengthening VLM models against jailbreak attacks. Specifically, SAFEMLLM consists of two phases: (1) introducing adversarial embedding tokens, where adversarial tokens are initialized in the token embedding layer and optimized to produce adversarial responses; (2) using the adversarial noise from Phase 1 and additional defense data to fine-tune the model for robustness. The authors validate the effectiveness of the proposed defense method across six mainstream VLM model architectures.

### Strengths
- This work addresses the security defense of multimodal VLMs, which is crucial for enhancing the secure deployment of VLMs.
- Comprehensive experiments conducted on multiple model architectures and datasets demonstrate the effectiveness of the proposed method.

### Weaknesses
 - The definitions of formulas are unclear. For example, what do $P_h$ and $P_t$ represent in lines 240-244? Why initialize two tokens instead of one?

- Why does the CoE-attack optimize at the embedding token level? Why not at the representation level?


- How does $\text{equ.2}$ guarantee output quality while ensuring the model’s replies are relevant to the query?

- There is formula redundancy. Both equ.3 and equ.4} describe the same optimization objective, yet the authors define it twice as $loss_{adv}$ in equ.3 and as $loss_{def}$ in equ.4. This complexity should be reduced; maintaining clear formula definitions is essential to avoid redundancy.

- The results in Table 3 are unclear. The authors state that results were tested on ImgJP (image) and AdvBench (text) datasets, yet the table does not present the experimental results for these two modalities separately. Additionally, what is the distinction between $J_{target}/J_{contra}$ and $L_{target}/J_{contra}$? The authors should avoid using multiple ambiguous definitions, as this complicates understanding the experimental results.


- What are the specific settings for model output quality in Figure 3? The authors tested only 100 samples, which may not effectively reflect changes in model output capabilities. It is recommended that the authors test on 500 benign samples to assess the effects accurately.

- How can the model avoid generating garbled outputs? In lines 511-513, the authors indicate that using $L_{contra}$ and $J_{contra}$ to fine-tune the model may lead to meaningless garbled outputs (e.g., repeating "safe"). I request the authors to further explain the reasons for this phenomenon and how to prevent garbled outputs during optimization. This is crucial for assessing the effectiveness of the optimization steps in their method. Additionally, could the authors provide examples of model outputs in both successful and failed optimization scenarios?

Overall, I acknowledge the proposed adversarial training method for enhancing the robustness of VLMs against jailbreak attacks. However, there are still issues regarding unclear loss definitions and ambiguous optimization details in the methods section. On the other hand, in the experimental section, the authors need to further elucidate the roles of the different loss components. Moreover, an explanation and experimental results on how to prevent the model from generating meaningless outputs (such as repetitive and low-quality responses) during adversarial training are also required. If the authors can address the aforementioned concerns, I would like to increase my score.

### Questions
see weakness.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose the first adversarial training algorithm for VLMs. They introduce a new loss function based on contrastive learning for attack optimization and model training and demonstrate the effectiveness of the new components in an ablation study. Compared to prev. work in the LLM setting, they show that their algorithm provides higher robustness.

### Strengths
* Multimodal adversarial training is an underexplored research area and this paper provides numerous insights on some of the design choices that need to be considered in this context. 
* Robustness is evaluated from multiple perspectives, which makes it easier to assess differences between multi-modal and LLM only robustification approaches. 
* State-of-the-art attack methods are used for evaluation
* Exhaustive hyperparameter ablations are conducted for the presented method.

### Weaknesses
 * Doesnt the argument in line 90 only apply to the method proposed by Mazeika et al.? I think the framing could be improved. 
* The two-step algorithm is just standard adversarial training with nontypical loss functions. I think it would be easier to understand if the authors framed their contribution accordingly. Initially, I thought that this 2 stage algorithm would be something different. 
* Include the dataset that was used for the experiment in Figure 3
* “We attribute this to the fact that in all MLLMs, the image is always placed before the text as input” This information would be helpful when you describe the method. To give a better intuition about P_0^h

### Questions
* Do I understand it correctly, that no images are used during attack optimization? If yes, did you ablate if encoding a given image and starting the attack from this initialization is helpful? 
* What are the hyperparameters of the competitor approaches? Are there any ablations regarding the “best” or reasonably “best” possible achievable robustness with the different methods. Hard to compare methods directly to each other otherwise
* Could the authors clarify how they measured over-refusal after safety training in their framework?

In summary I believe this to be an interesting contribution to the ICLR and robustness community and would be willing to increase my score if all my concerns and questions are addressed.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces SAFEMLLM, a novel adversarial tuning framework to defend multimodal large language models (MLLMs) against jailbreak attacks. The framework operates in two stages: 1) generating adversarial perturbations using a contrastive embedding attack (CoE-Attack), and 2) updating model parameters to neutralize perturbation effects while preserving model utility. The authors evaluate SAFEMLLM across six MLLMs and six jailbreak methods spanning multiple modalities, demonstrating its effectiveness in defending against diverse attacks without compromising normal interactions.

### Strengths
- Comprehensive experiments are conducted across multiple models and jailbreak attack methods, demonstrating the effectiveness of this framework.
- The idea is easy to understand and the paper is easy to follow.

### Weaknesses
 - This paper lacks novelty. Though it's the first paper to perform adversarial tuning on MLLMs, the attack method is only conducted on the embedding layer and there is no specific modification to the components directly related to VLLM such as the image encoder. Previous work[1, 2 ] on LLMs has already demonstrated the effectiveness of adversarial training in the latent space. Meanwhile, previous work also propose to first perform attacks on multiple layers of LLM (including the embedding layer) and then fine-tune the model against such attacks. Since this method only performs attacks on the embedding layer, it's not clear why previous work cannot be directly applied to this task.
-  More recent attack methods could be added, such as GPTFuzzer [3] and PAIR [4].

### Questions
- How is this method different from other latent adversarial training methods [1] [2] ?
- Could this training approach be adapted to improve model safety against other types of attacks?



[1] Sheshadri, Abhay, et al. "Targeted latent adversarial training improves robustness to persistent harmful behaviors in llms." arXiv preprint arXiv:2407.15549 (2024).

[2] Casper, Stephen, et al. "Defending Against Unforeseen Failure Modes with Latent Adversarial Training." arXiv preprint arXiv:2403.05030 (2024).

### Soundness
3

### Presentation
2

### Contribution
1
