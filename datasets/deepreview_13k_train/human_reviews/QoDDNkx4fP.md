# ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference-Time

- Decision: Accept
- Scores: 8, 5, 5, 6

## Abstract
Vision Language Models (VLMs) have become essential backbones for multimodal intelligence, yet significant safety challenges limit their real-world application. While textual inputs are often effectively safeguarded, adversarial visual inputs can easily bypass VLM defense mechanisms. Existing defense methods are either resource-intensive, requiring substantial data and compute, or fail to simultaneously ensure safety and usefulness in responses. To address these limitations, we propose a novel two-phase inference-time alignment framework, \textbf{E}valuating \textbf{T}hen \textbf{A}ligning (ETA): \romannumeral1) Evaluating input visual contents and output responses to establish a robust safety awareness in multimodal settings, and \romannumeral2) Aligning unsafe behaviors at both shallow and deep levels by conditioning the VLMs' generative distribution with an interference prefix and performing sentence-level best-of-$N$ to search the most harmless and helpful generation paths. Extensive experiments show that ETA outperforms baseline methods in terms of harmlessness, helpfulness, and efficiency, reducing the unsafe rate by 87.5\% in cross-modality attacks and achieving 96.6\% win-ties in GPT-4 helpfulness evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces ETA, a two-phase framework for enhancing Vision Language Model (VLM) safety at inference time. The proposed method assesses visual and textual safety using CLIP scores for images and a reward model for text. It also applies a "safety prefix" (shallow alignment) and best-of-N search (deep alignment) to ensure responses are harmless and relevant. The ETA significantly reduced unsafe responses through comprehensive experiments.

### Strengths
1. The idea of the method is intuitive and easy to follow.
2. The method is plug-and-play, could be deployed to many VLM systems.
3. Comprehensive experiments on some VLMs with good performance.

### Weaknesses
 1. The method itself, is more like a combinaiton of pre-processing and post-processing techniques. The contribution of this method maybe limited.
2. As a plug-and-play method, I expect to see it to be applied to more recent VLMs, such as LLaVA-Next, LLaMA3.2.
3. Also I would expect to see the model performance drop on more recent and widely-used benchmarks like MMMU
4. Some highly-relevant references about VLM/LLM safety are missing [1][2]

### Questions
Is there any compromised approach to also employ similar strategy to API-based VLM/LLMs like GPT-4(V)?

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
The paper explores solutions for enhancing the safety of Vision Language Models (VLMs). The authors introduce a strategy called Evaluating Then Aligning (ETA) to address this issue at inference time. 

ETA first detects unsafe visual inputs using CLIP similarity to an unsafety-specific prompt (pre-generation score) and an LLM-based reward model to assess initial output safety (post-generation score). If both scores indicate that the input is unsafe (pre-generation score is above the threshold, post-generation score is below the threshold), ETA appends a predefined prefix (e.g., "As an AI assistant,") to the prompt, guiding the VLM to generate a safer response by maximizing the weighted sum of two factors: the similarity between the current output sentence and the visual input, and the post-generation score of the previously generated sentence.

The authors conduct experiments across various LLMs and datasets to demonstrate the effectiveness of the proposed strategy.

### Strengths
1.	This paper introduces a straightforward, training-free strategy to address safety issues in VLMs.
2.	Experiments conducted across multiple models and datasets demonstrate the strategy's effectiveness and generalizability.
3.	The paper is well-structured, providing a clear narrative that effectively outlines both the problem and solution.

### Weaknesses
1.	The setting of the helpfulness experiment (Table 2) is not well rigorous. 
The experiment is conducted using general comprehensive benchmarks and VQA datasets, which is not fully consistent with the "usefulness" goal the authors aim to address—namely, ensuring helpful responses even with unsafe inputs. While Table 3 provides some helpfulness results, the range of benchmarks used is somewhat limited. Testing on more models and datasets can better verify the effectiveness of this strategy.
2.	The analysis of the ablation study results is inadequate:
When the Utility Guide component is removed from the strategy, the unsafe rate actually decreases, yet this result is not fully analyzed. Does this suggest that the Utility Guide might be unnecessary? A deeper exploration is needed to clarify its role and significance.
3.	The proof of the Motivation in the MULTIMODAL EVALUATION (i.e. Continuous Visual Token Embeddings Bypass Safety Mechanisms) is not very rigorous: In the proof experiment, continuous visual embeddings were converted to the nearest discrete text embeddings, showing a 7% reduction in unsafe rates on one dataset. Testing this approach across more datasets and models could strengthen its reliability.
4.	The effectiveness of the strategy is not well proven. The number of baselines (especially for inference-time baselines) is too small to prove the effectiveness of the strategy.

### Questions
Please address the concerns in the Weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposed a new safeguard mechanism for the Vision Language Model (VLM) during inference phase. This simple and straightforward approach largely reduces the unsafe responses while ensuring the helpfulness corresponding to the given input instruction.

### Strengths
- The proposed safeguard mechanism induces helpfulness, which better promotes usefulness of VLMs in a safe manner, rather than simply refusing the given user instruction.
- The paper is well written to easily understand
- The defense performance is well-improved compared to the baseline defense methods.

### Weaknesses
 - Novelty: although the simplicity of the proposed methods, the novelty seems significantly limited, as the proposed methods are based on the simple application of existing models such as CLIP and Reward Models.
- Clarification of the motivation: While the authors posed the major cause of the VLMs being jailbroken is the continuous nature of the visual embeddings, I think it is due to the visual embeddings not being safety-aligned with RLHF. Also, I'm not sure if the proposed methods correspondingly resolve the motivation behind the visual embedding's continuous nature.
- Potential side-effects of the proposed method:
   1) Pre-generation Evaluator: although the image contains the harmful image, the textual instruction might be normal and benign (e.g., a criminal scene image + "How to prevent such crimes?"). According to the proposed method, it may judge these benign inputs as unsafe, which possibly leaves as a side-effect.
    2) Sentence-level Deep Alignment: since the proposed deep alignment selects the optimal sentence under the consideration of the safeness of the given sentence and its correlation with the input image in a greedy manner, the resultant sequence of sentences might not be ensured to be logically connected. This potential side-effect might rather hinder the reliability of the VLMs.

### Questions
- Performance comparison with the safety-aware visual RLHF (if any) would be appreciated to see if the proposed method would rather be the optimal way of safeguard VLMs.

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
5

### Summary
The paper proposes a two-phase approach called "Evaluating Then Aligning" (ETA), aiming at improving the safety and utility of Vision Language Models (VLMs) during inference. It begins by assessing the safety of both visual and textual inputs and outputs using multimodal evaluation. If unsafe behavior is detected, ETA applies a bi-level alignment strategy to ensure responses are safe and useful.  Overall, ETA offers a plug-and-play solution that requires no additional training, making it a practical approach for real-world applications of VLMs.

Key Contributions:

(1) The framework uses visual content analysis and a reward model to evaluate the safety of inputs and outputs, creating a more robust safety awareness across both modalities.

(2) The method features shallow alignment using an interference prefix to activate safety mechanisms, followed by deep alignment with sentence-level best-of-N searching to ensure helpfulness without compromising safety.

(3) Extensive experiments demonstrate that ETA significantly reduces unsafe responses across various VLMs and benchmarks, outperforming existing inference-based methods. It maintains the general capabilities of the models while enhancing safety and efficiency.

### Strengths
Originality: 

The paper introduces a novel framework, ETA (Evaluating Then Aligning), which addresses a critical gap in the safety of Vision Language Models (VLMs) by focusing on inference-time alignment. Unlike existing approaches that primarily rely on extensive fine-tuning or are limited to specific types of inputs, ETA offers a fresh perspective by combining multimodal evaluation and bi-level alignment without requiring additional training. This plug-and-play nature makes it a highly original contribution, providing a more flexible and scalable solution for enhancing VLM safety.

Quality: 

The technical quality of the paper is robust, with a well-structured methodology that is clearly articulated and backed by extensive experimental validation. The authors systematically evaluate ETA across multiple dimensions, including safety, helpfulness, and efficiency. The experiments are comprehensive, covering various adversarial benchmarks and showing consistent improvements over baseline methods.

Clarity: 

The paper is clearly written. The framework’s methodology is detailed and easy to follow, aided by diagrams that illustrate key concepts, such as the two-phase evaluation and alignment process. Additionally, the use of concise and relevant examples helps in understanding how ETA addresses existing limitations.

Significance: 

The significance of this work is substantial, as it addresses one of the key challenges in deploying VLMs in real-world applications—ensuring safety without compromising utility. By introducing a method that does not require fine-tuning, ETA can be easily integrated into existing systems, making it practical for widespread use. The ability to improve safety while maintaining model efficiency and general capabilities could encourage broader adoption of VLMs.

### Weaknesses
1. Limitations in Pre-Generation Evaluation Using CLIP

A notable weakness of the paper lies in the reliance on CLIP for pre-generation safety evaluation, specifically through the use of predefined prompts (e.g., checking for "physically harmful" content). While CLIP is a powerful model for general vision-language tasks, its training data may not always align well with the specific categories being evaluated, such as physical harm. This could lead to situations where CLIP fails to accurately assess certain types of harmful content because it was not explicitly trained on safety-critical datasets. To improve this, the authors could consider using adaptive prompts that are tailored to different scenarios, enabling more precise evaluations. By refining prompts based on the context of the input (e.g., using distinct prompts for detecting physical hazards, offensive imagery, or illegal content), the system could achieve more accurate safety checks across a wider range of situations.

2. Potential Instability in Post-Generation Evaluation Using Reward Models (RMs)

The use of reward models (RMs) for post-generation evaluation could introduce instability, as the ability of RMs to accurately judge safety and utility might vary depending on the context. The RM employed may not be inherently designed to handle safety-specific assessments, which raises concerns about the consistency and reliability of its evaluations. Furthermore, this approach can lack interpretability, as it does not always provide clear reasons for why a response was considered safe or unsafe. To address this, it would be beneficial to either fine-tune the RM specifically for safety-related tasks or incorporate explainability mechanisms that can offer insights into how safety decisions are being made, thus building more trust in the evaluation process. For instance, the model could be designed to generate detailed explanations for its safety assessments, which could then be evaluated themselves to ensure they align with safety standards.

### Questions
(1) How can the interpretability of the post-generation evaluation process be improved?

The reliance on RMs can sometimes lead to a lack of clear explanations for why a response is deemed safe or unsafe. Have you considered methods to enhance interpretability, such as generating explanations alongside safety scores, or using models that can provide reasoning for their evaluations?

(2) Did you observe any scenarios where the ETA framework failed or produced unexpected results?

Understanding the limitations of ETA would be useful for assessing its real-world applicability. Are there specific types of inputs or adversarial attacks where ETA was less effective? For example, were there instances where CLIP misinterpreted visual content, leading to unsafe outputs, or where the RM failed to accurately judge the safety of a response? Additionally, if such limitations were observed, what improvements or adjustments could be considered to address these cases effectively?

### Soundness
3

### Presentation
4

### Contribution
3
