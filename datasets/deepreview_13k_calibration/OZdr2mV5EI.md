# Instruction Contrastive Tuning for Zero-shot Composed Image Retrieval

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 3, 5

## Abstract
Composed Image Retrieval (CIR) requires retrieving a target image based on a composed query consisting of an image and accompanying text that modifies or instructs changes to the visual reference. This task is particularly challenging as it demands the model effectively follow modification instructions for accurate retrieval. Additionally, data acquisition difficulties hinder training models for specific tasks. To address these challenges, recent approaches explore Zero-Shot CIR (ZS-CIR), mainly leveraging CLIP-based models with tailored projections to compose images and textual modifications. However, these base models are not trained on instruction-aware data, limiting their ability to effectively combine visual and textual cues. In this paper, we propose a novel embedding method utilizing an instruction-tuned Multimodal Large Language Model (MLLM) to generate unified embeddings that seamlessly integrate images and modification instructions. Instruction-tuned MLLMs inherently align vision and text while exhibiting strong instruction-following capabilities, though they are primarily used in text generation. We introduce a two-stage training strategy to efficiently transform the MLLM’s text generation capabilities into embedding extraction, and further refining its ability to follow modification instructions in CIR. Our model demonstrates significant advancements in ZS-CIR, outperforming state-of-the-art baselines across four public datasets: FashionIQ, CIRR, GeneCIS, and CIRCO. Our model highlights the potential of instruction-tuned MLLMs in capturing nuanced instruction comprehension and advancing CIR systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a two-stage training method that instruction-tunes MLLMs for zero-shot CIR tasks. In the first stage, the authors train the MLLMs to encode images and text into a joint embedding space. In the second stage, the model is trained to generalize to different instructions, enabling better zero-shot CIR performance. Experiments demonstrate results across various benchmarks, along with  ablation studies on different modules of the model.

### Strengths
- The model leverages LLMs to generate modified text and target captions, presenting a novel and efficient strategy that avoids additional annotation costs.

-  This method achieves significant improvements across various benchmarks. Comprehensive ablation studies illustrate the contribution of each module of the model.

### Weaknesses
 - My concern is about the efficiency of using MLLMs for zero-shot CIR tasks. Traditional zero-shot CIR methods are typically very efficient, for example Pic2word, SEARLE, LinCIR, Context-I2W. Could the authors provide a comparison of inference times, like average inference time per image when testing on the same device?

- The authors did not specify inference details. Could the authors provide a detailed description of the inference process after training.

### Questions
Please refer to the weakness above. I will carefully review the rebuttal and consider the opinions of the other reviewers to adjust my rating.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on Zero-Shot Composed Image Retrieval (ZS-CIR). To effectively combine visual and textual cues, the authors propose an embedding method utilizing an instruction-tuned Multimodal Large Language Model (MLLM) to generate unified embeddings that integrate images and modification instructions. They introduce a two-stage training strategy to efficiently transform the MLLM’s text generation capabilities into embedding extraction, and further refining its ability to follow modification instructions in CIR. Experiments on four datasets shows the effectiveness of the proposed method, compared to the selected baselines.

### Strengths
1. The authors propose a new method based on MLLM.
2. The fine-tuning procedure of the proposed method is rational.
3. The writing is easy to follow.

### Weaknesses
1. Data leakage: the data in the first training stage of the proposed method utilize the data source of the adopted CIR datasets, such as MSCOCO. In zero-shot settings, no data (no matter training data or test data) in the target dataset can be utilized in model construction or optimization. Section 3.2 has not addressed this problem.
2. Important baselines are missing: As the authors utilize GPT-4o to combine the image and the modification text into a combined text, an important baseline is directly utilizing the combined text to retrieve the composed image using image-text retrieval methods, such as CLIP. This is because this baseline is a simple and direct method, which is very easy to implement in applications.
3. The proposed model is much larger (in terms of memory) and slower (in terms of speed) than the baseline models in the inference. The efficiency is concerned.

### Questions
Please respond to Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a two-stage training strategy for instruction-tuning a Multimodal Large Language Model (MLLM) for Zero-Shot Composed Image Retrieval (ZS-CIR). Training by this strategy, this paper proposed InstructCIR, an embedding method leveraging an instruction-tuned MLLM to generate composed embedding for composed image retrieval. InstructCIR demonstrates outperforming state-of-the-art baselines across four public datasets.

### Strengths
1.	Instruction-tuning an MLLM for CIR is interesting. 
2.	The various ablation studies show the effectiveness of InstructCIR.
3.    The proposed method demonstrates outperforming state-of-the-art baselines across four public datasets.

### Weaknesses
1. The setting of this paper is inconsistent with standard ZS-CIR tasks [1,2,3,4,5,6,7], which aim to leverage the frozen CLIP model with alignment knowledge to achieve zero-shot compose image retrieval. However, this method of pretraining the entire MLLM diverges from the established settings of published ZS-CIR models, which may not be a "Zero-Shot" setting in the ZS-CIR task. Therefore, it is unfair to compare. It seems more aligned with what "the Semi-Supervision CIR" [8] aims to address. This inconsistent setting may cause potential data leakage in the instruction tuning process, which is a fitting bias of the CIR data, leading to potential data leakage. Moreover, this method required training of the entire MLLM, introducing significant training parameter size, computational resources cost, and time increase, which is unfair compared to existing ZS-CIR methods.

2. The novelty is confused. The primary motivation :``these base models are not trained on instruction-aware data, limiting their ability to effectively combine visual and textual cues.’’ is unreasonable to me. The authors should carefully explain the relation between “instruction-aware data” and “ZS-CIR task”; for example, why does ZS-CIR require instruction-aware data? The claim that existing models lack instruction-following capabilities is not well-supported, as many ZS-CIR methods already demonstrate effective combination of visual and textual cues using frozen CLIP embeddings and alignment techniques. The authors need to clarify why these existing methods are insufficient and how instruction-aware data specifically addresses their limitations.

3. The technology contribution is limited. The two-stage training method is really similar to LLaVA [9], which only add a special token [EOS] as the global feature for retrieval. The instruction data generation process, which leverages GPT-4o, is not analyzed. The qualitative results may show that GPT-4o could achieve the goal of this method, which aims to generate the modified caption. Therefore, I would like to question the necessity of this method. The use of a special token for global feature extraction is a common practice, and the authors need to demonstrate a more significant technical difference from LLaVA. The lack of analysis on the GPT-4o data generation process raises concerns about the method's dependence on this specific LLM and the potential for bias or limitations in the generated data.

4. The inference stage for retrieval is NOT included in this paper, and the code are not given. This paper only shows the two-stage training process. However, the retrieval process, which is one of the most important stages, may be overlooked. The retrieval seems to leverage the MLLM encoder for all candidate images first and then uses the compose embedding as a query for retrieval. In this way, the computational resources cost and time required by this method are challenging for CIR, which is used in online e-commerce and recommendation systems. This raises me concerns about the practical significance of this method. The absence of details regarding the inference process makes it difficult to assess the real-world applicability of the proposed method. The computational cost of encoding all candidate images using an MLLM could be prohibitive for large-scale retrieval tasks.

5. The comparison of the main results might not be complete. For example, the SoTA of the CIRCO dataset is CIReVL(ViT-G-14) [6], and CIRR is LinCIR (ViT-G-14) [1], which this paper does not compare. This method includes a significant increment of modal size and pre-trained knowledge, which needs to be compared with ZS-CIR methods with larger CLIP backbones. The lack of comparison with state-of-the-art methods using larger backbones makes it difficult to assess the true performance of the proposed method. The authors should include comparisons with models that utilize similar or larger backbones to provide a more comprehensive evaluation.

6. Need more ablation studies. For example, what is the influence of other MLLM? What is the influence of GPT-4 or GPT-4-mini in data generation process?

### Questions
1.	Why ZS-CIR requires instruction-aware data?
2.	Why just leverage GPT-4o to achieve your goal? 
3.	What is necessary for this method? 
4.	How did you conduct your retrieval process?
5.	What do training parameter sizes compare to the existing ZS-CIR (e.g., Pic2Word)?
6.	What is the influence of different MLLMs? 
7.	What is the influence of GPT-4 or GPT-4-mini in the data generation process?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the challenges of Composed Image Retrieval (CIR), where the goal is to retrieve a target image based on a reference image and a textual modification. The approach involves a two-stage training strategy includes Embedding Alignment: The MLLM is trained on image-caption pairs to transform its text generation capabilities into effective embedding extraction; and the Instruction-Aware Tuning: Using a triplet dataset derived from image-caption data, the model is fine-tuned to generate embeddings that align with the combined image and modification text. This method allows InstructCIR to excel in Zero-Shot CIR (ZS-CIR), showing significant improvements over state-of-the-art methods on benchmarks like FashionIQ, CIRR, CIRCO, and GeneCIS. The paper demonstrates the potential of MLLMs in CIR tasks, especially in understanding and following modification instructions.

### Strengths
A new embedding strategy based on instruction-tuned MLLMs.

A two-stage training strategy that can transforms an MLLM’s strong text generation capabilities to effective embedding extraction.

Strong results on four datasets:  FashionIQ, CIRR, GeneCIS, and CIRCO compared with many other baselines.

### Weaknesses
The novelty of this paper is limited. There are already many existing works on image/text retrieval with MLLMs and finetuning MLLMs with instruction tuning data. [1][2][3] This paper is more like a combing of these two.

Using GPT4o to process and generate triplet data may bring additional biases. Additional evaluation such as human evaluation is needed to validated the approach. For example, asking humans to rate the quality or relevance of a sample of the generated triplets, or compare them to manually created triplets or trained a discriminator to filter biased data.

The comparison between different methods may be not fair as they also needed to finetuned on the datasets, e.g. CIReVL, MCL.

### Questions
Can the proposed two-strage training pipeline applied to other baseline models?

The potential scaling law for the propsed approach. For example, when the llm backbone is replaced with larger phi models.

### Soundness
3

### Presentation
3

### Contribution
2
