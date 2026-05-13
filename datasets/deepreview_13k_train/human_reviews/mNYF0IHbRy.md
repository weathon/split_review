# LLM Blueprint: Enabling Text-to-Image Generation with Complex and Detailed Prompts

- Decision: Accept
- Scores: 5, 6, 5, 6

## Abstract
Diffusion-based generative models have significantly advanced text-to-image generation but encounter challenges when processing lengthy and intricate text prompts describing complex scenes with multiple objects. While excelling in generating images from short, single-object descriptions, these models often struggle to faithfully capture all the nuanced details within longer and more elaborate textual inputs. In response, we present a novel approach leveraging Large Language Models (LLMs) to extract critical components from text prompts, including bounding box coordinates for foreground objects, detailed textual descriptions for individual objects, and a succinct background context. These components form the foundation of our layout-to-image generation model, which operates in two phases. The initial \textit{Global Scene Generation} utilizes object layouts and background context to create an initial scene but often falls short in faithfully representing object characteristics as specified in the prompts. To address this limitation, we introduce an \textit{Iterative Refinement Scheme} that iteratively evaluates and refines box-level content to align them with their textual descriptions, recomposing objects as needed to ensure consistency. Our evaluation on complex prompts featuring multiple objects demonstrates a substantial improvement in recall compared to baseline diffusion models. This is further validated by a user study, underscoring the efficacy of our approach in generating coherent and detailed scenes from intricate textual inputs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper extends recent works which leverages layouts to generate scenes corresponding to complex text-prompts. This work first shows that for complex prompts, existing layout to image generation methods have certain failure modes and proposes some practical modifications which are augmented with existing layout to scene generation methods.  First, the authors propose a scene blueprint to represent complex text-prompts; Secondly the authors design an iterative refinement process which improves the alignment of generated images with the complex text-prompts.

### Strengths
- The research question is a very practical problem — usually most of the text-to-image generation models are not good at coherent images corresponding to complex prompts, so providing a solution for it is important.
- The method consists of various components (a lot of these components are existing though) and is conceptually intuitive!
- The framework obtains strong results on human-study for fidelity of images generated for long prompts.

### Weaknesses
Cons / Questions

- While the writing is satisfactory, it can still be improved! The authors should provide more information in the paper on how Eq. (5) is used to guide the sampling process.
- Can the authors provide more intuition on the interpolation step? 
- Given that there are stronger open-source diffusion models (e.g., DeepFloyd) — the authors should provide some context on how long prompts work in those cases, as they use a stronger text-encoder like T5. 
- While the authors comment that the size of the tokens (77 in CLIP) is one of the potential reasons on why SD cannot generate compositional prompts — I believe this is only partially true. Even for non-complex compositional prompts, SD is not able to generate coherent images. Can the authors comment in general on some potential reasons why these text-to-image models are not able to generate images corresponding to simple compositional or complex prompts? I think both are related somehow and it will be beneficial to provide some context regarding it.

### Questions
See Cons/Questions;
Overall, the paper is practical, but the various components though intuitive are not technically novel. While I do agree that not everything in a paper needs to be novel — the authors should provide solid justifications on the design of each component.  

I am happy to revisit my scores after the rebuttal!

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel approach for improving text-to-image generation in diffusion-based models when processing complex scenes with multiple objects and intricate text prompts. The authors leverage Large Language Models (LLMs) to extract the layout information, detailed text descriptions, and background information from text prompts. Then the proposed layout-to-image generation model is composed of two stages: Global Scene Generation and Iterative Refinement Scheme. The Global Scene Generation phase uses object layouts and background context to create an initial scene which roughly represents the target image layout but not very accurate. Then the Iterative Refinement Scheme iteratively evaluates and refines box-level content to align them with their textual descriptions and recompose objects to ensure consistency. Extensive experiments are conducted to validate the effectiveness of the proposed approach.

### Strengths
1. The proposed approach can handle the complex scenarios of text-to-image generation with long text prompts very well.
2. The paper is well-written and easy to follow.
3. The iterative refinement loop provides a possible solution to generating images of complex scenes.

### Weaknesses
1. I think the major limitation of the proposed approach is efficiency. The complexity of the proposed approach increases as the number of objects increases for complex scenes. This might also be the major issue presenting this approach to be applied in real usage.
2. It seems that although the generation of objects can be iteratively refined, the bounding box locations cannot be refined. If the LLM predicts unreasonable bounding box layouts at the first stage, it cannot be corrected. Have the authors think of introducing the refinement of bounding box locations into the pipeline?
3. How many layouts are needed to interpolate? How does the number of layouts for interpolation affect the results?

### Questions
Please refer to the weakness section.

Post-rebuttal: I have read the author response and other reviewers' comments. I decide to keep my initial rating unchanged, but I won't fight for acceptance of this paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work aims to solve the problem that prior text-to-image models cannot accurately follow the object specifications in lengthy prompts. The work proposes a novel two-step pipeline that first uses a scene blueprint, which is an LLM-generated layout with object descriptions, to generate the overall image. A CLIP-based guidance is then applied to perform iterative refinement in order to make sure the content of each box is correct. The method enables accurate and diverse image generation with intricate and lengthy input text prompts. The user study and qualitative comparison indicate a non-trivial improvement over baseline methods.

### Strengths
1. In addition to previous methods using the layouts for initial image generation, the method further proposes box-based refinement to improve the ability to generate all the objects mentioned in a lengthy and intricate prompt.
2. The method points out the fact that there currently lacks a pipeline for benchmarking text-to-image methods with lengthy prompts and proposes a metric called prompt adherence recall (PAR) to evaluate their method and several baselines.
3. Their method has better prompt adherence compared to baselines in prompt generation. The user study also confirms that the method can faithfully generate objects in the prompt.

### Weaknesses
 - Missing information on human study. Detailed information on human study could be provided to assess the reliability of the outcome. How do you recruit and select them based on what qualification? Isn't there any conflict of interest for the subjects and authors? How many subjects are recruited? What was the confidence of the votes? This issue is the major reason for leaning toward rejection. I am eager to see the author's feedback for reassessment.

- This framework relies on recently proposed models like a strong LLM, CLIP, and an image composition model. The collection of previous works provides shallow techniques compared with them.

- A missing related work. DenseDiffusion [1] may be worth being included in the layout-to-image generation subsection in Sec. 2 and the box-level multi-modal guidance in Sec. 3.4. DenseDiffusion tried to manipulate attentional weights to control the regions for layout guidance selectively. It would be appreciated if you could compare your method with it for readers in the upcoming revised manuscript. Note that, due to the narrow accessibility to this work at the time of submission, this is not considered in the score evaluation.



### Questions
The authors are encouraged to respond to and address the weaknesses in the section above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This proposed a framework for generating images from complex and detailed prompts, which took more work for previous models or frameworks. They utilize LLM's capability to generate augmented textual and visual prompts for better generations. And the framework comprises global scene generation and an iterative refinement scheme to align with conditional cues.

### Strengths
- This work steps toward longer textual descriptions for image generations to ensure the fidelity of complex textual prompts. 

- Scene blueprints with the iterative refinement step ensure high prompt adherence recall, quantitatively validating its effectiveness.

### Weaknesses
- Missing information on human study. Detailed information on human study could be provided to assess the reliability of the outcome. How do you recruit and select them based on what qualification? Isn't there any conflict of interest for the subjects and authors? How many subjects are recruited? What was the confidence of the votes? This issue is the major reason for leaning toward rejection. I am eager to see the author's feedback for reassessment.

- This framework relies on recently proposed models like a strong LLM, CLIP, and an image composition model. The collection of previous works provides shallow techniques compared with them.

- A missing related work. DenseDiffusion [1] may be worth being included in the layout-to-image generation subsection in Sec. 2 and the box-level multi-modal guidance in Sec. 3.4. DenseDiffusion tried to manipulate attentional weights to control the regions for layout guidance selectively. It would be appreciated if you could compare your method with it for readers in the upcoming revised manuscript. Note that, due to the narrow accessibility to this work at the time of submission, this is not considered in the score evaluation.

[1] Kim, Y. et al. (2023). Dense Text-to-Image Generation with Attention Modulation. http://arxiv.org/abs/2308.12964

### Questions
- Minors:
  - In Sec. 3.1, Models. -> Models (Please exclude the period in the section title.)
  - In Fig. 2, it would be inappropriate to include the logo of a commercial product (ChatGPT from OpenAI) in an academic paper. And the company may not allow the usage of their logo to promote the work.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
