# Lost in Translation: Conceptual Blind Spots in Text-to-Image Diffusion Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 6

## Abstract
Advancements in text-to-image diffusion models have broadened both research and practical applications. However, these models frequently struggle with interpreting complex or overlapping constructs like "a tea cup of iced coke", primarily due to biases in their training datasets. We propose a new classification for such visual-textual misalignment errors, termed Conceptual Blind Spots (CBS). In this study, we employ large language models (LLMs) and diffusion models to thoroughly investigate the diagnosis and remediation of CBS. We develop an automated pipeline that leverages the LLM's proficiency in semantic layering to create a Mixture of Concept Experts (MoCE) framework. To disentangle overlapping concepts, we input them into the models sequentially. Our MoCE is specifically designed to alleviate conceptual ambiguities during the diffusion model's denoising stages. Empirical assessments confirm the effectiveness of our approach, substantially reducing CBS errors and enhancing the robustness and versatility of text-to-image diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the misalignment between text and image in text-to-image generation. The paper proposes a mixture-of-concept framework, where given a text prompt that contains multiple objects, diffusion models generate objects one by one following a specific order determined by a language model. The paper also collects a dataset of text prompts for evaluation. Experiments show that the proposed method improves faithfulness of generated images compared to the standard stable diffusion baseline.

### Strengths
1. The paper collects a valuable benchmark of text prompts for evaluating text-to-image models.
2. The proposed idea of composing generation for each object in a specific order provides insights for future research.

### Weaknesses
1. The presentation of the paper is bad. Some important terms such as "conceptual blind spots," "concept pairs," and "Socratic reasoning/questioning" are not clearly defined, which hinders the understanding of the paper. A large portion of the paper is describing the data collection process. However, the overall goal of the dataset is not clearly explained, and the reason behind each round is also not explained. The methodology section is also confusing. How is the proposed metric $D$ used during generation? Why is the binary search algorithm used for generation? Maybe an algorithm table could help explain the method more clearly.
2. The experiment setting is problematic. First, only the standard stable diffusion model is used as baseline. No comparison is provided for related works mentioned in Section 2. Second, the proposed metric $D$ is used during generation as well as for evaluation. So there might be unfair advantages for the proposed method.
3. Some notations are wrong. For example, in Background of Section 4, $I$ shouldn't denote the input image.
4. Several related works are missing, such as [1], [2], [3], [4].

### Questions
Please see weaknesses.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a novel classification for visual-textual misalignment errors called Conceptual Blind Spots. They leverage LLMs and Diffusion Models to detect and correct the CBS.

### Strengths
The conceptual blind spot is a relevant and timely problem. Several text-to-image generation models are posied with this limitation. To this extent, the authors build a novel dataset and show its effectiveness.

### Weaknesses
The paper is difficult to read. For instance:
1. "In this category, one concept (A or B) demonstrates a dominant relationship, either with an underlying C or" -- it is unclear what A,B, and C represent. The explanation lacks clarity on how these concepts interact within the visual-textual generation process. It's not clear if A and B are always present in the text prompt, or if C is inferred by the model, and how this inference leads to the described misalignment. The paper should provide a more concrete example, perhaps with a specific text prompt, to illustrate how A, B, and C manifest and cause the error.
2. How do we come up with the categories and patterns in Table 1. The methodology for deriving these categories and patterns is not sufficiently detailed. It's unclear whether these categories are exhaustive or if they are based on some specific taxonomy of visual-textual errors. The paper needs to explain the process of identifying these categories, including the criteria used to distinguish between them and the rationale behind the specific patterns within each category. A more rigorous explanation would enhance the credibility of the proposed classification.
3. "Initially, 259 concept pairs were identified through the collaborative efforts of human researchers, supported by GPT." -- How does GPT help here? What were the guidelines for human researchers? The paper lacks details on the specific roles of human researchers and GPT in identifying these concept pairs. It’s not clear what prompts or instructions were given to GPT, and what specific tasks were performed by human researchers. The paper should clarify the collaborative process with specific examples of how GPT was used to generate concept pairs and how human researchers validated or modified these pairs.
4. "After rigorous screening, 159 concept pairs attain a Level 5 rating, representing the pinnacle of quality."-- Can use elaborate the screening process? The criteria for the Level 5 rating are not clearly defined. It's unclear what specific metrics or qualitative assessments were used to determine the quality of the concept pairs. The paper needs to provide a more detailed explanation of the screening process, including the specific criteria used to assign the Level 5 rating and how these criteria ensure the quality and relevance of the selected concept pairs.

### Questions
See my comments in Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel framework for addressing misalignment errors between visual and textual elements in Text-to-Image (T2I) generation, referred to as 'Conceptual Blind Spots' (CBS). To spot problematic concept pairings, LLMs are employed. Additionally, the paper presents a method called 'Mixture of Concept Experts' (MoCE) to alleviate these identified conceptual blind spots during the diffusion model’s denoising stages. Experimental results illustrate the effectiveness of the proposed framework in mitigating the occurrence of conceptual blind spots.

### Strengths
The paper is very interesting and addresses an important limitation of T2I models. Evaluation and results look great. Human evaluation and qualitative analysis further strengthen the proposed framework.

### Weaknesses
I do not find any major weaknesses with the proposed work. However, I am curious to know what are the concrete failure cases with the proposed approach. Is there a way to understand the type of prompts the model gets right and the cases the proposed MoCE fails to handle? Another weakness with the paper is the readability. Some of the sections took me multiple readings. Also, in some places, for example in the Human evaluation section, it is not very clear how many test samples are considered. I also find a slight disconnect between the abstract and the three key contributions highlighted in the introduction section. I suggest authors make them more coherent in the final version (for example, there is no mention of dataset contribution in abstract but the dataset is listed as a key contribution in introduction).

### Questions
Please see weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
