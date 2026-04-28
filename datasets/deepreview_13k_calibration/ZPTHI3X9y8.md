# From Pixels to Tokens: Revisiting Object Hallucinations in Large Vision-Language Models

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 8, 5

## Abstract
Hallucinations in large vision-language models (LVLMs) are a significant challenge, \ie, generating objects that are not presented in the visual input, which impairs their reliability. Recent studies often attribute hallucinations to a lack of understanding of visual input, yet ignore a more fundamental issue: the model's inability to effectively extract or decouple visual features. In this paper, we revisit the hallucinations in LVLMs from an architectural perspective, investigating whether the primary cause lies in the visual encoder (feature extraction) or the modal alignment module (feature decoupling). Motivated by our findings on the preliminary investigation, we propose a novel tuning strategy, PATCH, to mitigate hallucinations in LVLMs. This plug-and-play method can be integrated into various LVLMs, utilizing adaptive virtual tokens to extract object features from bounding boxes, thereby addressing hallucinations caused by insufficient decoupling of visual features. PATCH achieves state-of-the-art performance on multiple multi-modal hallucination datasets. We hope this approach provides researchers with deeper insights into the underlying causes of hallucinations in LVLMs, fostering further advancements and innovation in this field.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses hallucinations in Large Vision-Language Models (LVLMs), proposing that they stem more from ineffective feature decoupling than a lack of visual input understanding. The authors introduce PATCH, a tuning method that employs adaptive virtual tokens to improve feature extraction from bounding boxes, effectively reducing hallucinations. PATCH claims that it achieves state-of-the-art results across multi-modal hallucination datasets, offering new insights into the architectural causes of hallucinations in LVLMs.

### Strengths
1. **Parameter Efficiency**: PATCH is designed to be parameter-efficient, reducing the need for extensive model adjustments while achieving high performance.
2. **Performance on Hallucination Datasets**: The proposed PATCH method achieves state-of-the-art results across multiple multi-modal hallucination datasets, demonstrating its effectiveness and robustness.
3. **Clarity and Simplicity**: The methodology is straightforward, and the paper is well-structured, making it easy to understand and follow.

### Weaknesses
1. **Lack of Novelty in Methodology**: The approach relies partially on using a pretrained object detection model for feature recognition and fine-tuning the vision-language model (VLM), which is a common strategy in previous works such as GLaMM, LISA, and Groundhog. This makes the method less innovative in this aspect. The paper does not sufficiently articulate how its approach to feature extraction and fine-tuning differs fundamentally from these existing methods, particularly in the context of mitigating hallucinations. A more detailed explanation of the specific architectural differences and training procedures that set PATCH apart is needed.

2. **Insufficient Ablation Study on Virtual Tokens**: The paper introduces virtual tokens as part of the PATCH tuning strategy but lacks comprehensive ablation studies to validate their effectiveness, limiting insight into how much these tokens specifically contribute to mitigating hallucinations. The paper should include a more granular analysis of the impact of varying the number of virtual tokens, their initialization, and their interaction with other components of the model. Without these details, it is difficult to assess the true contribution of the virtual tokens.

3. **Limited Plug-and-Play Functionality**: Although advertised as plug-and-play, the method requires fine-tuning for each personalized model, which contradicts its plug-and-play claim and may increase implementation complexity. The need for fine-tuning significantly reduces the practical appeal of the method, as it necessitates additional computational resources and time for each new application. A true plug-and-play method should ideally be usable without any further model training.

4. **Lack of Baseline Comparisons**: The study does not adequately compare its approach against similar methods. Baseline plug-and-play strategies, such as visual prompt-based methods (e.g., Set-of-Mark and so on), as well as fine-tuning methods like GLaMM, Lisa, and Groundhog, are absent, making it difficult to assess the actual improvements PATCH offers. The absence of these comparisons makes it challenging to determine whether the performance gains are due to the specific design of PATCH or simply due to the fine-tuning process itself.

### Questions
1. **Novelty**:  How does PATCH specifically improve over zero-shot visual prompts methods like Set-of-Mark and  fine-tuning methods like GLaMM, Lisa, and Groundhog?

2. **Virtual Tokens**: Is there an ablation study showing the effectiveness of virtual tokens?

3. **Plug-and-Play Claim**: Since fine-tuning is needed, how is PATCH truly plug-and-play?

4. **Baseline Comparisons**: Would including comparisons with similar methods, like visual prompts mehtods and other fine-tuning models, provide further context for PATCH’s effectiveness?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a parameter-efficient tuning technique that introduces detection for hallucination mitigation in multimodal large language models. The method utilizes adaptive virtual tokens to extract object features from bounding boxes, thereby addressing hallucinations caused by insufficient decoupling of visual features.

### Strengths
Computational Efficiency: The proposed PATCH strategy achieves parameter-efficient tuning by freezing LVLM parameters and optimizing a small number of virtual tokens, making it lightweight and practical for deployment scenarios.

### Weaknesses
1.  Lack of Clarity in Preliminary Experiments: Section 2 is confusing, particularly regarding Table 1. Definitions of “correct detection” and “wrong detection,” along with their calculation methods, are not adequately explained.
2.  Insufficient Support in Analysis: The performance gap between detection and inference is not convincingly attributed to the struggles of the visual projection module. The reasoning lacks robust experimental evidence.
3.  Contradiction in Motivation: While the motivation suggests that incorporating detection information may introduce redundancy, the method still relies on detection information plus soft visual tokens, creating a contradiction.
4.  Limited Novelty: The method primarily involves parameter-efficient tuning (soft prompt tuning), which does not introduce significant novelty beyond existing tuning techniques.
5.  Unfair Experimental Setup: The use of a portion of the test data for training gives an in-domain testing advantage, compromising the fairness of comparisons with baselines.
6.  Incomplete Baseline Comparisons: Not all baselines are consistently compared across different LVLMs, particularly in the main results table, diminishing the thoroughness of the evaluation.
7.  Omission of Experimental Details: Important experimental details, such as decoding strategies, are missing, limiting the reproducibility of the experiments.
8.  Absence of Ablation Studies: An ablation study isolating the added visual tokens is needed to properly assess their contribution to the model's performance. (e.g., tuning only the projector on the same data)
9.  Overclaimed Results: Some claims, such as those in lines 316–317 about enhanced semantic alignment via visual tokens, are overstated without sufficient empirical support.
10. Incomplete Related Work: The related works section neglects recent advances in LVLMs, such as Qwen2VL and LLaVA-OneVision, as well as relevant hallucination mitigation methods like GAVIE, limiting the contextual relevance of the paper.

### Questions
Please refer to the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper investigates the root causes of hallucinations in LVMs, identifying the main issue as the insufficient separation of textual and visual features during multi-modal integration. To address this, the authors introduce a tuning-based method, designed to help LVMs leverage object detection to reduce hallucinations. The effectiveness of this method is demonstrated through validation on two multi-modal hallucination evaluation datasets across three different LVMs.

### Strengths
1. The paper is very clear and easy to follow.

2. The experiments support the main claims in the text, and the presented approach is simple and useful.

3. Most of the design choices are ablated to verify their effectiveness.

### Weaknesses
1. The paper claims that the reason for hallucinations is the feature decoupling. Nevertheless, many of the hallucinations in Table 1 are also not detected by the detection model (308 vs. 191). This suggests that the encoder is an additional significant source of hallucinations. I would like to see the same table, after the replacement of $prompt_1$ with $prompt_2$.

2. The paper claims that the additional computational cost of training the extra tokens is negligible. Nevertheless, the paper omits the fact that the model relies on an additional object detector that should also be trained. It is not clear to me if the additional computational cost and model parameters that were spent on the object detector, can be spent instead on a larger encoder/adapter/llm, and result in a much cleaner solution for hallucination reduction. 

3. Overall, the paper presents a simple soft-prompting approach for targeting hallucination reduction. Are the detections necessary, or can they be achieved solely from additional soft-prompting with more learned tokens?

### Questions
1. For $prompt_2$ and along the rest of the paper, the additional information that is extracted from the object detector and given to the language model includes not only the existence of objects but also their location (x1,x2,y1,y2). Although according to Table 4, it is necessary, it is not clear why (the VQA is about object existence and not localization). Do you have any intuition for this property? Can you compare the accuracy of the bboxes to their hallucination removal rate?  

2. Is the VLM even needed, given the soft prompt and the detection results? What is the baseline of soft-prompting a text-only LLM on the object detection results, without the use of images?

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
4

### Summary
This paper revisits the reason for LVLM object hallucination by conducting a preliminary study and finding that visual feature decoupling instead of extraction is the main reason. Based on a potential solution, the authors propose PATCH, a novel plug-and-play prompt-tuning-based LVLM hallucination mitigation method. Experiments on the POPE and PhD datasets verify the effectiveness of the proposed method.

### Strengths
- Starting from a preliminary study and then introducing the proposed method, the writing is good.
- The proposed method is plug-and-play without requiring a large amount of computing.
- The authors demonstrate the effectiveness of the proposed methods on three baseline models.

### Weaknesses
 - About the Cascade Mask-RCNN head:
  - Do you use a separate Cascade Mask R-CNN detector or just the detector head which is then connected with the vision encoder of the LVLM?
  - If the former, you cannot get the conclusion in Sec. 2 since the capabilities of the detector and the vision encoder of LVLM might differ from each other.
  - If the latter, how do you do that? Is the detection head exactly pre-trained with the same vision encoder of the LVLM, or do you need further training?

- About PATCH:
  - On the one hand, detection information might be redundant.
    - In lines 226-227, the authors suggest that,
      > In scenarios where no extra detection information is required, the LVLM can revert to processing the input using its standard capabilities without PATCH involvement.
    - I wonder how to do that, since the detection module of PATCH is query-irrelevant, suggesting that the detector will detect all objects in the image regardless of the question. This raises concerns about the practical applicability of PATCH, as it seems to require manual selection of when to use it, limiting its zero-shot capabilities.
  - On the other hand, detection information is limited by the granularity of the detector.

    - PATCH aims at directly providing the object information detected by the detector to LLMs, which, however, cannot provide information that cannot be detected by detectors. For example, attributes (colors and shapes) cannot be detected, which are more common phenomenon of LVLM hallucinations nowadays. Furthermore, the reliance on a pre-trained detector limits the method's ability to recognize objects beyond its training classes.
    - Moreover, objects beyond the recognizable classes of the detector are also not recognizable.
  - Therefore, beyond experiment numbers, an analysis of why PATCH eases LVLM hallucination is also feasible. For example, will PATCH help if the queried object is *without* or *beyond* the class set of the pre-trained detector?

- About experiments:
  - Baselines: HA-DPO and HACL are both methods requiring training. Do you train them with the same training set with PATCH? The lack of a consistent training regime across baselines makes it difficult to assess the true effectiveness of the proposed method.
  - We care about hallucination, but we do not want to hurt the utility of LVLMs. Therefore, besides experiments on hallucination benchmarks like POPE and PhD, results on utility benchmarks (e.g., MME, MMBench, and SEED) are also important to demonstrate that hallucination mitigation is not at the cost of utility. The current evaluation lacks a comprehensive assessment of the method's impact on general LVLM capabilities, focusing solely on hallucination-specific datasets.

### Questions
- About title: 
  - The overall idea of this paper is to help LVLMs better utilize the object recognition information extracted by the vision encoder. 
  - So what does the "From Pixels to Tokens" suggest in the title?
- About the potential solution:
  - How do you get the object-related information, by using the ground truths or prediction results of Cascade Mask R-CNN?
  - How do you deal with objects which are not existing in the image?

### Soundness
2

### Presentation
3

### Contribution
2
