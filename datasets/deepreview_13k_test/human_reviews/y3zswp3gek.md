# HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models

- Decision: Accept
- Scores: 6, 6, 10, 6

## Abstract
\looseness=-1 
Safety guard models that detect malicious queries aimed at large language models (LLMs) are essential for ensuring the secure and responsible deployment of LLMs in real-world applications.
However, deploying existing safety guard models with billions of parameters alongside LLMs on mobile devices is impractical due to substantial memory requirements and latency.
To reduce this cost, we distill a large teacher safety guard model into a smaller one using a labeled dataset of instruction-response pairs with binary harmfulness labels. Due to the limited diversity of harmful instructions in  the existing labeled dataset, naively distilled models tend to underperform compared to larger models. To bridge the gap between small and large models, we propose \textbf{HarmAug}, a simple yet effective data augmentation method that involves jailbreaking an LLM and prompting it to generate harmful instructions. Given a prompt such as, ``Make a single harmful instruction prompt that would elicit offensive content", we add an affirmative prefix (\eg, ``I have an idea for a prompt:") to the LLM's response. This encourages the LLM to continue generating the rest of the response, leading to sampling harmful instructions. Another LLM generates a response to the harmful instruction, and the teacher model labels the instruction-response pair. We empirically show that our HarmAug outperforms other relevant baselines. Moreover, a 435-million-parameter safety guard model trained with HarmAug achieves an F1 score comparable to larger models  with over 7 billion parameters, and even outperforms them in AUPRC, while operating at less than 25\% of their computational cost. Our \href{https://anonymous.4open.science/r/HarmAug/}{code}, \href{https://huggingface.co/AnonHB/HarmAug_Guard_Model_deberta_v3_large_finetuned}{safety guard model}, and  \href{https://huggingface.co/datasets/AnonHB/HarmAug_generated_dataset}{synthetic dataset} are publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Safety guard models (SGMs) are often deployed along with a target large language model in order to detect malicious and unsafe queries. They are also used for red teaming LLMs to detect vulnerabilities to attacks such as jailbreaks.

The paper proposes to address the challenges associated with large SGMs such as high compute and memory requirement, latency, and operational costs (which are impractical e.g. on mobile devices). It proposes to perform knowledge distillation of a large SGM into a smaller one (sub-billion parameters) using a labeled dataset of instruction-response pairs with harmfulness labels. 

To address the limited diversity of harmful instructions in the labeled dataset, the paper proposes HarmAug, a simple but effective data augmentation method that generates synthetic harmful instructions using a second LLM by jailbreaking it (to bypass its refusal). Specifically, HarmAug designs a special jailbreak prompt that asks the LLM to generate a harmful instruction by including an affirmative prefix at the end of the prompt `“I have an idea for a prompt”`. This encourages the LLM to continue generating a harmful instruction instead of refusing. 

By generating diverse harmful instructions in this way, the method augments the training set of knowledge distillation and creates a student SGM that generalizes better than existing augmentation methods. The experimental results show that knowledge distillation with HarmAug can train much smaller student SGM models that have comparable (and sometimes better) detection metrics to the large teacher SGM. The smaller SGMs have the benefit of much lower computation, memory, latency, and operational costs. They also enable faster/cheaper red teaming and more efficient adaptation to evolving threats.

### Strengths
1. The paper is well written and the method and results are presented clearly.

1. Tackles an important problem since the detection of malicious queries and jailbreaks is important for the safe deployment of LLMs. Moreover, making the safety guard models smaller (sub-billion parameters) allows for their efficient deployment in low-resource environments (reduced latency, memory, and cost), and allows for faster red teaming, as well as adaptation to new attacks.
  
1. The experiments are comprehensive. In addition to the detection performance of safety guard models on multiple benchmarks, it covers the benefits to red teaming due to reduced computational cost and runtime, and efficient fine-tuning of the safety guard model against new/evolving jailbreak attacks. Then it presents a number of ablation experiments to justify different design choices. Finally, the paper is careful to report average metrics with error bars. 

1. The authors release their code, models, and synthetic datasets allowing reproducibility and further research.

### Weaknesses
1. The proposed data augmentation method relies on jailbreaking an LLM in order to generate a diverse set of malicious instructions. This is based on a simple idea of using a jailbreak prompt asking an LLM to generate a harmful instruction, but with an affirmative prefix “I have an idea for a prompt.” at the end which encourages the LLM to continue with the generation, thus bypassing its safety alignment driven refusal. 
While this special jailbreak prompt is shown to be effective against a variety of safety-aligned LLMs, it is possible for future iterations of these LLMs to circumvent this jailbreak through careful alignment via RLHF or a similar method. I wonder if this decreases the long-term value of the proposed augmentation method for generating diverse harmful instructions? 

2. Related to the previous question, I wonder if one can use an LLM that has *not* been safety aligned (via SFT and RLHF) for the generation of harmful instructions? That way, one does not need to use a special jailbreak based on the affirmative prefix to bypass the LLMs guardrails. Is there any practical reason not to do this?

3. The paper performs ablation experiments on the size of the student model and the choice of student model backbone (Section 4.4). While this is informative, I wonder if there is some bias introduced in the main results by reporting with the best student model backbone and size (DeBERTa-v3-large with 435M parameters)? In a practical deployment, we may have to make these choices without access to such results. Hence, the performance of the student safety guard model may not be as optimistic.

### Questions
1. Referring to lines 221 - 223, could you explain how the second LLM is finetuned using few-shot adversarial examples in order to generate harmful responses. This is not clear. Also, there are not many details available on the `boyiwei/pure_bad_100-7b-full` LLM. 

1. Lines 265 - 267: is the knowledge-distillation based training sensitive to this configuration of optimization hyper-parameters? 

1. Is knowledge distillation used for the baselines EDA and GFN?

1. In Eqn (5), it should be $y^{(j)} \sim p_{target}(y | x^{(i)})$.

1. In Eqn (4), it is not so clear what the trajectory balancing objective is? Is it to be minimized?

1. The prompt format in page 4 specifies that the instruction should be a single sentence. However, there are examples in Table 11 in Appendix D that have multiple sentence instructions. Any idea why this happens with the LLM generation?

1. Referring to the qualitative results in section 4.1, are you embedding only the instruction or the combination of instruction + response for the clustering?

1. Referring to the experimental setup paragraph on line 408: how big is the CipherChat dataset used for fine-tuning? Are the metrics reported in Figure 5 on a test split of CipherChat?

### Soundness
4

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
3

### Summary
This paper introduces *HarmAug*, a data augmentation technique designed to improve the performance of small safety guard models through knowledge distillation from larger models. The authors aim to address the challenge of deploying large safety guard models (with billions of parameters) on resource-constrained devices like mobile phones. To achieve this, they propose generating synthetic harmful instructions by "jailbreaking" a safety-aligned LLM. This is done by adding an affirmative prefix (e.g., "I have an idea for a prompt:") to the prompts, encouraging the LLM to produce harmful instructions it would normally refuse to generate due to its safety constraints. These synthetic instructions, along with their corresponding responses labeled by the large teacher model, are used to augment the training data for a smaller student model. The authors claim that this method enhances the diversity of harmful instructions, allowing the smaller model to perform comparably to larger models while significantly reducing computational costs.

### Strengths
1. The paper tackles an important and practical problem—how to deploy effective safety guard models on devices with limited computational resources. It is a good motivation and this is increasingly relevant as AI applications become more prevalent on mobile platforms.
2. The authors present experimental results showing that a 435-million-parameter model trained with HarmAug achieves performance comparable to larger models (over 7 billion parameters) on several benchmark datasets.
3. The paper is well-written and organized. The methodology is explained in detail, making it easy to follow. Figures and tables are effectively used to illustrate key points and results.

### Weaknesses
1. **Dataset Quality and Inclusion of NULL Responses**: Upon inspecting the provided dataset (https://huggingface.co/datasets/AnonHB/HarmAug_generated_dataset), I noticed that a significant number of responses are NULL (empty). While it's acceptable for some responses to be NULL—representing appropriate refusals or lack of response—the dataset contains a large proportion of such responses without explicit justification in the paper. Moreover, some NULL responses receive high harm scores, while others receive low scores. Since the harm score is based on both the prompt and the response, it's possible for a harmful prompt with a NULL response to still receive a high harm score. However, the paper does not explicitly explain this aspect, leaving the rationale unclear.
2. **Potential Impact on Model Training**: The inclusion of numerous NULL responses with varying harm scores could affect the learning process of the student model. Without a clear explanation, it's difficult to assess whether these data points contribute positively or negatively to the model's ability to detect harmful content.
3. **Limited Methodological Novelty**: While the practical application is important, the methodological contribution is relatively incremental. The use of LLMs for data augmentation is a common practice, and adding an affirmative prefix is a modest modification. The paper does not introduce significant new insights beyond this.

### Questions
1. Prevalence of NULL Responses in the Dataset:
- Your synthetic dataset contains a significant number of responses that are NULL. Could you explain why there are so many NULL responses? Is this an intentional aspect of your data generation process, or does it indicate an issue with the response generation step?

2. Impact on Model Performance: 
- Have you analyzed how the inclusion of NULL responses with varying harm scores affects the student model's performance? Does it improve the model's ability to detect harmful content, or could it introduce confusion during training?

3. Impact on Diverse Harmful Instructions:
- While you provide evidence of increased diversity in the training data, have you evaluated the model's ability to generalize to completely new types of harmful content not represented in your synthetic dataset? How does the model perform on real-world examples or emerging threats?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper focuses on distilling the safeguarding ability of LLMs into a smaller one, particularly through the data augmentation perspective.

### Strengths
1. Overall, this is a well-written paper. The motivation and setting are clearly stated.
1. The problem of distilling large safeguard models into small ones is novel and has good applications.
1. The proposed HarmAug method of using ICL examples is simple and easy to understand.
1. The experiment is very comprehensive.
1. Code and other resources are provided.

### Weaknesses
1. While not explicitly instructed in the Call for papers, the Reproducibility statement and Ethics statement should be in \section*{} format (following previous years).
1. The overall prompt design shares similar notions with 2 existing works, which may should be cited in Section 3.2: 
    - using prefixes to bypass the safety guardrails of the LLMs is similar to Prefix Injection [1]
    - using ICL examples to bypass the safety guardrails of the LLMs is similar to in-context attack [2]
1. Are there other applications of HarmAug beyond model distillation? This point was not well-discussed in the paper.

[1] Jailbroken: How Does LLM Safety Training Fail? https://arxiv.org/pdf/2307.02483

[2] Jailbreak and Guard Aligned Language Models with Only Few In-Context Demonstrations https://arxiv.org/pdf/2310.06387

### Questions
See weaknesses

### Soundness
4

### Presentation
4

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
This paper introduces HarmAug, a method for creating efficient safety guard models for LLMs. They propose to distill large safety models into smaller ones where the output is binary label indicating whether the input is safe or not. To overcome the limited diversity of harmful instructions in existing datasets, they introduce HarmAug, a data augmentation method that involves:
   a. Prompting an LLM to generate harmful instructions
   b. Using an affirmative prefix to encourage the LLM to complete the harmful instruction
   c. Generating responses to these instructions using another LLM
   d. Labeling the instruction-response pairs using the teacher model

Based on this they are able to outperform much large LLMs (7B compare to ~500Mb), showing the importance of synthetic data generation and knowledge distillation to create small robust safety guardrail classifiers.

### Strengths
Originality:
1. The main novelty is HarmAug, the data augmentation method for generating harmful instructions to train safety guard models.
2. They also propose an effective "prefix attack" to bypass safety guardrails of language models when generating harmful content for training data.
3. Results show the feasibility of distilling large safety guard models into much smaller, more efficient models without significant performance loss.

Quality:
1. The results section is mostlycomprehensive in the experiments across multiple benchmark datasets.
2. Provides detailed ablation studies to analyze the impact of different components and design choices.
3. Compares the proposed method against several relevant baselines and existing safety guard models.
4. Evaluates both performance (F1 score, AUPRC) and efficiency metrics (FLOPs, latency, memory usage).

Clarity:
1. Clearly explains the motivation, methodology, and experimental setup.
2. Uses effective visualizations to illustrate key results and comparisons.
3. Provides a detailed breakdown of the proposed method, making it easier for others to reproduce or build upon.

Significance:
1. Addresses an important practical challenge in deploying safety guard models on resource-constrained devices.
2. Demonstrates that smaller models can achieve comparable or better performance than much larger models for this task.
3. Shows potential for improving the efficiency of red-teaming and fine-tuning processes for language model safety.
4. Provides open-source code, models, and datasets to facilitate further research in this area.

### Weaknesses
* Limited Analysis of Jailbreaking Technique: While the prefix attack is effective, the paper doesn't provide an in-depth analysis of why this particular method works or explore alternative jailbreaking techniques. 
* Generally, if the novelty lies in HarmAug in diversifying generated data it would be nice to see comparison to other instructions and their failure modes w.r.t to HarmAug. 
* Table 4 could also include other prefixes as baselines to further motivate that particular string of texts effectiveness. 
* the utility of these models on mobile devices is mentioned a few times but never experimented with on-device. Arguably outside of the paper but would definitely be a stronger set of results to have.

### Questions
* For the baseline LLMs (LlamaGuards and Aegis adapter-finetuned LlamaGuard) did you use their default safety policy or did you replace it with the test set specific information ? Because a lot of these datasets (e.g in Table 1) already have categories of safety, toxicity or content moderation that can replace the "Should not" and "Can" behaviors of LlamaGuard and I'd imagine this would make the baselines perform better compared to their default template. 

* Why not consider 3rd party APIs ? It would be interesting to see other providers such as Azure Content Safety, OpenAI Moderation, gpt 3.5-turbo/mini/4/ or 4o for example. I understand some of these require payment but worth considering if feasible.

* What's the tradeoff in terms of performance (e.g F1) when guardrailing prompts compared to llm responses with HarmAug ?

### Soundness
4

### Presentation
4

### Contribution
3
