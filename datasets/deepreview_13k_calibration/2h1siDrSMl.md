# RoRA-VLM: Robust Retrieval-Augmented Vision Language Models

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Though vision-language models (VLMs) have demonstrated impressive capabilities as general-purpose visual assistants, they still exhibit inferior performance on knowledge-intensive tasks such as information-seeking visual question answering, primarily due to the challenge of accurately encoding all the associations between visual objects and scenes to their corresponding entities and background knowledge.  
While retrieval augmentation methods offer an efficient way to integrate external knowledge, extending them to vision-language domain presents unique challenges in (1) precisely retrieving relevant information from external sources due to the inherent discrepancy within the multimodal queries, and (2) being resilient to the irrelevant, extraneous and noisy information contained in the retrieved multimodal knowledge snippets. 
In this work, we introduce \arch{}, a novel and robust retrieval augmentation framework specifically tailored for VLMs, 
with two key innovations:  
(1) a 2-stage retrieval process with \Retrieval{} to
synergistically combine the visual and textual information in the query and retrieve the most relevant multimodal knowledge snippets;
and (2) a robust retrieval augmentation method that strengthens the resilience of VLMs against irrelevant information in the retrieved multimodal knowledge by injecting adversarial noises into the retrieval-augmented training process, and filters out extraneous visual information, such as unrelated entities presented in images, via a query-oriented visual token refinement strategy.
We conduct extensive experiments to validate the effectiveness and robustness of our proposed methods on three widely adopted benchmark datasets: OVEN, InfoSeek and Enc-VQA. Our results demonstrate that with a minimal amount of training instance, \arch{} enables the LLaVA-v1.5 model to achieve significant performance improvement and constantly outperform state-of-the-art retrieval-augmented VLMs on all benchmarks while also exhibiting a novel zero-shot domain transfer capability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces RORA-VLM, a retrieval-augmented framework designed to enhance Vision-Language Models (VLMs) by addressing two main challenges: managing multimodal query discrepancies and filtering out irrelevant, noisy retrievals. RORA-VLM employs a two-stage retrieval process: 1) Image-Anchored Entity Retrieval: This stage retrieves visually similar images based on the query image, anchoring the retrieval with associated entity information 2) Query-Expanded Text Retrieval: Using entity names from the first stage, the method expands the query to retrieve additional textual knowledge from sources like Google Search.

### Strengths
- The paper is well written and easy to follow
- The authors clearly state the motivation for the proposed method and its necessity.
- RORA-VLM introduces a unique two-stage retrieval approach, effectively bridging the gap between visual and textual information for more accurate knowledge retrieval.
- The paper tackles the common issue of irrelevant or noisy data in retrieval-based methods by implementing noise resilience strategy
- The paper address a clearly practical application that might be useful for the community and the industry.

### Weaknesses
Method:

- Section 3.2: The authors describe in details two stages. For my understanding, stage-1 is just formulation of the K-NN of the query image in the WIT images (within CLIP latent space). This is a well-known concept, especially in this line of work. I think this is well-detailed stage but it should be on the appendix, while the main paper should contain a brief description of the stage.
- Line 270: “Similarly, the image I is encoded into a sequence of visual embeddings…” - this is not clear. CLIP encodes an image/text intro a shared embeddings space of dimension d. How do you encode the image patches (n) to the same dimension? Do you feed-forward each patch, separately, to the CLIP model? Do you use the N internal CLIP features for each patch? If so, are you sure that their dimension is d, before the last projection layer? Do you project them with the last visual projection layer as the pooled [CLS] token projected? Please elaborate more on this procedure.

Section 5 currently combines results, ablation study, and discussion, which affects the clarity and flow of these findings. Separating these into distinct sections—such as “Results,” “Ablation Study,” and “Discussion”—would make it easier for readers to follow each component and understand the contributions more clearly. Additionally, crucial details and experiments appear to be missing, and some existing experiments do not convincingly support the claims made. Below are specific areas where the section could be strengthened:

Evaluation:

- Main results: Lines 307-316 (Baselines): The authors list a several MLLM backbones for the QA task which is great. However,  baselines to compare to should be other RAG methods. If I understand correctly, only RORA-VLM and Wiki-LLaVA* are using Retrieval Augmentations. If so, how is it comparable to other baselines that uses zero-shot?
- Building on previous point, I am not fully understand the entire training setup: the only model that was tuned (lines 317-345) was RORA-VLM? If so, again, how is it comparable to other baselines? Please clarify these points.

There are not enough details about the evaluation protocols and datasets in the paper, and some comparisons are missing. For example, what was the training set of each baseline in Table 1? Did the authors fine-tuned each baseline on the same dataset? which one of them use the proposed RAG method? what about other RAG methods and baselines?

Ablation Study:

- Lines 365-367 states “we use the widely adopted average pooling (kernel size of 2, stride of 2) to obtain the same number of visual tokens as our refinement approach” What does “widely adopted average pooling” mean on N CLIP vectors? How does it relate to a kernel size of size 2 and stride 2? Did you manipulated the input image/kernel of CLIP to get the same amount of CLIP vectors? The authors should elaborate on the experiment that was done here, it is unclear.
- Lines 405-419:  I am not convinced why this experiment proves that the model ignore “noise” in the retrieval samples. I would be more convinced with an following experiments, for example: providing the model 1 relevant sample with 2 other randomly-sampled ones, will not change the model’s answer, regardless which 2 noise samples were chosen, or by just proving the 1 relevant sample with no other samples. 
- Lines 420-430 describe Figure 4 that supposed to show how the model ignore “noise” samples. However, it seems like the model pays attention to specific words the correlate with the question (e.g., row 1,  “how wide…” attend “height” and “width”). These examples does not show any rubsness to “noise” retrieval as intended.

### Questions
- In line 257 - do you mean top-2 (instead of top-(k-1))?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a multimodal version RAG targeting multimodal large language models, such as LLaVA-1.5 for information-seeking VQA. To solve two challenges, the authors propose a 2-stage retrieval process with image-anchored textual query expansion and noise-resilient retrieval augmented generation. Experimental results highlight its effectiveness on OVEN and InfoSeek benchmarks.

### Strengths
1. The motivation for this work is clearly presented and easy to follow.
2. Experiment results demonstrate its effectiveness.

### Weaknesses
1. In the Introduction section, providing a figure showing the process of the 2-stage retrieval method would be easier to understand.
2. Related work discussion and method novelty. How to incorporate multi-modal knowledge into models is not a new problem[1][2]. Some related work is proposed in other multi-modal tasks, such as knowledge-based VQA. Besides, adversarial training is also adopted in existing vision and language training, such as [3]. The authors are encouraged to discuss the existing work and compare the related ones with the proposed method.
3. The correspondence between the ablation model variants in Table 2 and the proposed module is somewhat unclear. What about the ablation of the two-stage retrieval ?
4. Figure 2 lacks some of the details of the methodology. The authors are encouraged to refine it.

### Questions
Please refer to the above section.

### Soundness
3

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
The paper introduces RORA-VLM, a framework aimed at improving Vision-Language Models (VLMs) on knowledge-intensive tasks. The method addresses two challenges: (1) effectively retrieving relevant multimodal information given the inherent discrepancy between vision and language modalities, and (2) managing the noisy and extraneous information in retrieved knowledge. The paper’s contributions include a two-stage retrieval process with image-anchored textual-query expansion and a robust retrieval augmentation method that employs adversarial noise and visual token refinement. Extensive experiments demonstrate that RORA-VLM outperforms current models on benchmarks such as OVEN, InfoSeek, and Enc-VQA.

### Strengths
1. **Novelty**: The authors address two core challenges in multimodal retrieval-augmented generation (RAG): the retrieval inaccuracies caused by modality discrepancies and the noise often present in retrieved content. To tackle these issues, they propose an innovative solution using a two-stage retrieval process that mitigates modality inconsistency, allowing the system to capture multimodal background information more comprehensively. Combined with an anti-noise strategy, this approach effectively suppresses irrelevant information while enhancing retrieval accuracy and overall performance in multimodal tasks.

2. **Significance**: RORA-VLM offers a valuable method for improving VLMs, especially in knowledge-intensive domains, where retrieval-augmented tasks are often challenged by noise. This framework effectively addresses this key issue, making it particularly suitable for such applications.

3. **Clarity of Presentation**: The paper is well-structured with a clear research motivation, providing thorough explanations of the methodology and experimental results. This clarity aids readers in understanding both the approach and its effectiveness.

### Weaknesses
1. **Inconsistency in Method and Motivation**: The two-stage retrieval in the paper looks like an image entity-driven retrieval approach, would modal differences be better handled with image+query composite retrieval; Additionally, the motivations behind the designs of Query-oriented Visual Token Refinement and Adversarial Noise Injection for Robust Augmentation seem to conflict. The former introduces noise for adversarial learning, while the latter focuses on denoising. It might align better with the concept of adversarial learning if the former were applied solely during the inference phase and the latter exclusively during training. Specifically, the visual token refinement process, which aims to remove query-irrelevant visual elements, appears counterintuitive when used in conjunction with adversarial noise injection during training, as it might interfere with the adversarial learning process by removing the very noise the model is supposed to learn to handle. A more principled approach might involve using visual token refinement only during inference to clean up inputs, while relying on adversarial noise injection during training to enhance robustness.
2. **Fairness of Experimental Comparisons**: In the main experiments presented in Table 1, the authors' method has undergone pre-training and fine-tuning on knowledge-intensive datasets, whereas many baseline models may not have been trained on such datasets. This raises questions about the fairness of the experimental comparisons. It is crucial to ensure that all models are evaluated under comparable conditions to draw meaningful conclusions about the effectiveness of the proposed approach. The lack of clarity on the training regimes of the baseline models makes it difficult to ascertain whether the reported performance gains are solely attributable to the proposed method or are also influenced by the differences in training data and procedures.
3. **Lack of Ablation Studies**: The paper lacks ablation studies on key parameters such as k, l, and m. Including these analyses would provide valuable insights into the impact of these parameters on the model's performance. Specifically, the absence of a detailed analysis of how the number of retrieved knowledge snippets (m), the number of top-k images retrieved in the first stage (k), and the number of visual tokens used in refinement (l) affect the overall performance makes it difficult to understand the sensitivity of the model to these hyperparameters. Such studies are essential for a comprehensive understanding of the model's behavior and for optimizing its performance in practical applications.

### Questions
1. **Differences in Approach and Motivation**: The two-stage retrieval approach proposed in the paper seems to be driven by image entities. Does a retrieval approach that combines images and queries better address pattern differences? Furthermore, how do the authors reconcile the conflicting motivations behind query-oriented visual token refinement (introducing noise for adversarial learning) and adversarial noise injection (focusing on denoising)? Would it be more consistent with adversarial learning principles if the former were used only during inference and the latter only during training?
2. **Fairness of experimental comparisons**: In Table 1, do the authors plan to conduct more experiments to ensure that all models are evaluated on a level playing field?
3. **Lack of ablation studies**: Can the authors provide insights on the impact of these parameters (k,l,m) on model performance?

### Soundness
3

### Presentation
3

### Contribution
3
