# Pixelated Instructions: Can Multimodal Large Language Models Follow Printed Instructions in Images?

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Recent multimodal large language models (MLLMs) have shown promising instruction following capabilities on vision-language tasks. In this work, we introduce VISUAL MODALITY INSTRUCTION (VIM), and investigate how well multimodal models can understand textual instructions provided in pixels, despite not being explicitly trained on such data during pretraining or fine-tuning. We adapt VIM to eight benchmarks, including OKVQA, MM-Vet, MathVista, MMMU, and probe diverse MLLMs in both the text-modality instruction (TEM) setting and VIM setting. Notably, we observe a significant performance disparity between the original TEM and VIM settings for open-source MLLMs, indicating that open-source MLLMs face greater challenges when text instruction is presented solely in image form. To address this issue, we train V-MLLM, a generalizable model that is capable to conduct robust instruction following in both text-modality and visual-modality instructions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
this paper investigates how well multimodal models can understand textual instructions in images. propose a new setting named visual modality instruction (VIM) which evaluates the capability of MLLMs following instructions given in images. The results clearly show the performance gap of open-source models in the VIM setting and traditional setting, motivating a training dataset targeting the VIM setting.

### Strengths
1. show interesting findings:
(1) open and closed source VLMs are robust to the position of textual instruction in the image.
(2) Two-stage instruction tuning and mixed instruction tuning have similar performance.

2. After being tuned on the proposed VIM training dataset, open-source models demonstrate better instruction following capability.

3. Comprehensive evaluation of open source and close source VLMs in the VIM setting.

### Weaknesses
1. The main concern is the technical contribution.

(1) The proposed instruction following setting is new but it's similar to the original task of OCR which tests if VLM can read and understand text in the image.

(2) The proposed training data is an augmentation of existing datasets by rendering and adding textual instruction on the images.

(3) The VIM training is a supervised training setting with two variants. The major different between two variants are the data mixing strategies.

### Questions
1. What causes the performance improvement of LLaVA-1.5 3b on the MM-vet with stage-wise tuning in the TEM setting (Table 7)? Do you think it's because of better OCR of VLM learned during VIM instruction tuning.

2. Why models achieve lower performance on TextVQA after VIM tuning in Table 7?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces visual modality instruction to investigate how well multi-modal models can understand textual instructions provided in images. Furthermore, this paper trains a v-MLLM model.

### Strengths
- This paper is easy to read.
- Some figures are good.

### Weaknesses
 - The motivation presented in Figure 1 do not make sense. While LLMs can make plausible or correct predictions in some cases, these predictions do not change with different image inputs and will be incorrect if the image changes. However, the benchmark questions you mentioned seem closely related to the images, suggesting that the final answer depends on both the image and text. So I cannot understand the importance and necessary of designing the VIM task.
- The concept of "embeded instruction" is confusing. I initially thought you were embedding the text instruction using a visual encoder, but it appears you are simply adding the instruction to the image, similar to OCR.
- In my opinion, this benchmark is primarily designed to probe the OCR capability of MLLMs, specifically a certain type of OCR capability. While useful in some scenarios, I think the vision and motivation are somewhat limited.
- It would be better to compare the results to some MLLMs that excel at OCR. Moreover, the training method setups seem a little bit trivial, obtaining seems like a task-specific model.

### Questions
- The citation format is incorrect. You should use \citep{} rather than \citet{}. For the case of "Multimodal Large Language Models (MLLMs)", it would be better to use the following format: Multimodal Large Language Models (MLLMs; citations).

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- The paper introduces an interesting setting, visual modality instruction, to assess the ability of Multimodal Large Language Models (MLLMs) to follow textual instructions presented in visual formats. 
- The paper trains V-MLLM, which demonstrates robust instruction-following abilities in both text-based and visual instruction settings across multiple tasks.

### Strengths
- The paper identifies a gap in existing MLLMs’ capabilities, noting that they struggle to follow text instructions embedded in visual formats. To address this, the authors propose Visual Modality Instruction (VIM), a challenging setting designed to assess MLLMs' ability to interpret instructions delivered through visual modalities.
- The paper constructs VIM-Bench based on eight existing representative benchmarks and trains V-MLLM to following instructions in both text and visual formats.

### Weaknesses
 - Figure 2 is overly complex and contains excessive information, making it difficult to interpret. Simplifying this figure would improve clarity and reader comprehension.
- The conclusion and discussion around the instruction location experiment in Section 2.1.2 is not well established. For example, it’s unclear why the authors omitted a comparison with the "left" position. Additionally, while the paper claims that “GPT-4V and LLaVA-1.5 are robust to the locations of the embedded instruction”, there’s a nearly 10% performance difference between the "bottom" and "top" positions in GPT-4V. Moreover, the paper could also consider constructing the VIM corpus with randomly selected positions for the embedded text instructions
- For the VIM training, it’s unclear if V-MLLM was initialized with pretrained weights from LLaVA-1.5 and whether the model fine-tunes the full model including the image encoder, projector, and language model (LLM) backbone altogether.
- In Table 3, under the TEM setting,  V-MLLM’s performance drops on TextVQA and ChartQA compared to LLaVA-1.5. Since these tasks require an understanding of text within images, this drop appears to contradict the hypothesis that VIM training would help with understanding the text within the image?

### Questions
- The paper states that “we aim to keep the resolution of the raw images, and we add text with the same font size for all images.” However, most MLLMs resize images to a standard size before encoding. Won't this resizing result in inconsistent text instruction resolution?
- Given that the VIM corpus places text instructions primarily at the bottom of images, how would the model perform on instances where the text instructions are embedded in different locations?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the ability of multimodal models to follow textual instructions embedded within visual data. The authors introduce a new benchmark and a custom training dataset to evaluate this capability. Their findings reveal that while open-source multimodal large language models encounter significant challenges, some proprietary models demonstrate effective performance. Additionally, they present a trained model, v-MLLM, capable of following instructions in both text-based and visual modalities.

### Strengths
1.	A new evaluation benchmark for MLLMs is introduced, along with an assessment of several baseline methods.
2.	This paper introduces a new VIM training corpus, shown to be effective for training models with visual instruction-following capabilities.
3.	Extensive evaluations on the VIM benchmark reveal several noteworthy and practical findings.

### Weaknesses
1.	The motivation for developing visual modality instructions is unclear. What specific application scenarios would require instructions to be provided only through printed images?
2.	It may be unfair to evaluate existing open-source MLLMs in the VIM setting and compare them against proprietary models or a specialized model like v-MLLM. First, the VIM setting is likely unfamiliar to open-source models, whereas it may have been accessible to the proprietary and specialized models, making it unsurprising that open-source models struggled with this new setting. This diminishes the experimental results' relevance. Additionally, accurately recognizing text remains a known limitation for most general-purpose MLLMs, making the VIM setting challenging. To accurately assess visual instruction-following capabilities, it is necessary to minimize the impact of these models' text-recognition weaknesses; otherwise, the evaluation risks becoming more of an OCR test.
3.	The paper is missing some key baselines. First, visual instruction-following could potentially be achieved by integrating an OCR front-end with MLLMs, which would be a straightforward approach to the task. Second, since visual instruction processing in MLLMs resembles a two-step process, and the authors find mixed instructions significantly improve performance, using a chain-of-thoughts prompt could help build stronger baseline models.

### Questions
Please see the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2
