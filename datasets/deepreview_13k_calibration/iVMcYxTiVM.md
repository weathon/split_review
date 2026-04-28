# Can we talk models into seeing the world differently?

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Unlike traditional vision-only models, vision language models (VLMs) offer an intuitive way to access visual content through language prompting by combining a large language model (LLM) with a vision encoder. However, both the LLM and the vision encoder come with their own set of biases, cue preferences, and shortcuts, which have been rigorously studied in uni-modal models. A timely question is how such (potentially misaligned) biases and cue preferences behave under multi-modal fusion in VLMs. 
As a first step towards a better understanding, we investigate a particularly well-studied vision-only bias - the texture vs. shape bias and the dominance of local over global information. 
As expected, we find that VLMs inherit this bias to some extent from their vision encoders. Surprisingly, the multi-modality alone proves to have important effects on the model behavior, i.e., the joint training and the language querying change the way visual cues are processed. 
While this direct impact of language-informed training on a model's visual perception is intriguing, it raises further questions on our ability to actively steer a model's output so that its prediction is based on particular visual cues of the user's choice. 
Interestingly, VLMs have an inherent tendency to recognize objects based on shape information, which is different from what a plain vision encoder would do. Further active steering towards shape-based classifications through language prompts is however limited. In contrast, active VLM steering towards texture-based decisions through simple natural language prompts is often more successful.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies vision-only biases in texture vs. shape and the preference for local over global information in recent vision-language models (VLMs). The paper reveals that VLMs partially preserve the shape bias from their vision encoders, though they do not reach human levels of shape reliance. The vision encoder produces a biased representation containing both texture and shape cues, which the LLM often suppresses, leading to recognition based on either shape or texture alone. At the last part, this paper shows that VLMs enable steering of visual biases through language prompt, allowing shape bias to be adjusted significantly.

### Strengths
- The paper is well-written with extensive analysis.

- The motivation is clear, and the problem is well-defined. It’s a pleasure to read.

- A comprehensive study is included, with inspiring and interesting findings.

### Weaknesses
 - Class-wise analysis: For VQA classification, where tasks involve multiple classes, a class-wise analysis to examine texture and shape bias for each class would be helpful. Questions to explore include whether this texture and shape bias is consistent across all classes and whether there are differences between classes with simple vs. complex shapes. Specifically, it would be beneficial to see a breakdown of performance on classes with inherently strong shape cues (e.g., cars, bicycles) versus those where texture might be more salient (e.g., fabrics, foliage). This analysis should also consider the interaction between object complexity and bias, as objects with intricate shapes might be more susceptible to texture interference.

- Additional qualitative results and examples: This paper provides quantitative results across various aspects; however, it lacks qualitative results and examples, which would help clarify the concepts through visual examples. For instance, the reviewer suggests including examples from the target dataset with texture and shape splits. Additionally, presenting qualitative examples of both correct and incorrect predictions could further enhance the paper’s clarity and impact. It would be particularly useful to see examples where the model's prediction aligns with the shape cue, the texture cue, and cases where the model fails to correctly identify the object due to a conflict between these cues. This would provide a more intuitive understanding of the model's behavior.

### Questions
- The results of steering the texture/shape bias via language prompts are interesting. The reviewer observes that steering towards a texture bias can lead to completely different model behaviors for different models. For example, the performance of Gemini increases by 1%, while LLaVA-NeXT-7B decreases by 2%. However, in the study of prioritizing shapes over texture cues in VLMs, LLaVA-NeXT-7B actually shows a stronger texture bias than Gemini. Do the authors have any comments or findings in this direction?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
- The paper investigates how visual biases in vision-language models (VLMs), specifically the shape vs. texture bias, are affected by integrating a large language model (LLM) with a vision encoder.
- It highlights that VLMs inherently inherit some biases from their vision encoders but exhibit unique behaviors when processing visual cues, influenced by the multi-modal fusion of vision and language.
- The study shows that VLMs tend to favor shape-based recognition over texture, unlike traditional vision-only models, but do not match the high shape bias seen in human perception.
- The authors demonstrate that these biases can be steered using natural language prompts without retraining, allowing adjustments in model behavior to prioritize shape or texture-based decisions.
- The research provides insight into the potential of language prompting to align model outputs with user preferences, showcasing a new, efficient method to adjust visual biases in multi-modal models.

### Strengths
- Introduces a new investigation into steering visual biases in VLMs using natural language prompts, extending beyond traditional uni-modal bias studies.
- Comprehensive experiments using the texture/shape cue-conflict dataset validate findings and provide robust evidence for claims.
- Clear organization with effective figures and tables to illustrate results, making complex concepts more understandable.
- Demonstrates that visual biases can be influenced through prompts without retraining, offering practical implications for user-aligned AI outputs.
- Opens pathways for further research on user-driven customization and bias control in multi-modal AI, enhancing model adaptability and transparency.

### Weaknesses
 - Focus on shape and texture biases limits the study; exploring other biases (e.g., color, spatial attention) would give a fuller understanding of VLM behavior.
- Limited discussion on prompt selection; more detail on prompt strategies and robustness would enhance the study's depth.
- Prompt-based bias steering is constrained; deeper analysis on why some models are less responsive and how to improve steerability is needed.

### Questions
- Have you considered extending the study to include other visual biases such as color or spatial attention for a broader understanding of VLM behavior?
- Can you share additional examples or analyses of failure cases where the model showed unexpected behavior or limited steering?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper shows that VLMs still preserve the texture and shape biases of image encoders, however, VLMs are more biased in shape rather than texture.
It also shows the results compared to the image encoder including ReSNet-50, and CLIP.
Also, this paper presents the methodology for controlling those biases through steering prompts.

### Strengths
- This paper is well-written and well-organized.
- Extensive study to study textual and shape biases in VLMs.
- Also, this paper presents a steering prompt that may change the bias.
- This paper supplements detailed analysis and implementation details.

### Weaknesses
 - In section 5.2, spectral biases or critical bands that are difficult to control in language, I ask for more of  the authors' opinions on why the language prompt influenced this bias and what it means when the performance decreases even if the bias value changes.

- According to the results of Figure 4, steering can slightly control textual/shape biases, but it seems to have a slight impact on overall performance, so what is the point of controlling these biases?

### Questions
- What is the base performance of the original image encoder in Table 2?

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
This paper investigates the shape-texture biases in recent vision-language models (VLMs). The author discovered that training with LLMs and vision-language tasks change the shape-texture biases, using the tasks of VQA and image captioning. However, the shape-texture bias is still influenced by the upstream vision-only encoders (e.g., CLIP). Based on such observations, the authors proposed both manual prompts and LLM-generated prompts to elicit the models' biases toward either shape or texture without significantly degrading the accuracy.

### Strengths
* S1: Overall, I think the paper is written clearly and highlights several key contributions.

* S2: The authors have conducted experiments on a wide range of VLMs and reach the interesting conclusion that -- VLMs influences the shape texture biases compared with their upstream vision-only encoders. I think the analysis is thorough and detailed in this part, covering multiple scenarios (VQA and image captioning), diverse models, and several comparative experiments (e.g., in Table 1). I am not an expert in explainability research, but this paper is the first to study VLMs' shape-texture biases to the best of my knowledge.

* S3: The authors demonstrate the stability of VLMs' biases towards either shape or texture (Figure 3) and how to steer their behaviors (Figure 4 and Figure 5). Both manual prompt tuning and automatic LLM optimization can achieve such steering. According to the authors' claim, this might be potentially useful.

* S4: The analysis and experiments in this paper are detailed and comprehensive.

### Weaknesses
 * W1: After reading the paper, it is still unclear to me **what the significance of studying shape and texture biases is**, primarily when MLLMs can already address more complicated tasks than object recognition nowadays. This concern limits the significance of this paper. Perhaps this point sounds biased, but I wish the authors had provided more arguments or examples of how studying shape-texture biases benefits the development or applications of VLMs. Such contexts would help the readers not to focus specifically on shape-texture biases.

* W2: The conclusions mentioned in the paper did not seem explicit from the quantitative results. For example, Table 1 does not show conclusive observations. If the goal of this table is to show that VLMs can behave very differently than their original visual encoder, this does not seem to be a surprising discovery since VLMs are trained on different datasets with different recipes compared with the original vision encoder.

* W3: More clarifications are needed on the steering part, where I have similar concerns with W1 -- the authors might want to clarify the usefulness of the potential contribution of steering such biases. (1) The claim in L448-449, "overall accuracy does not change considerably," might indicate that shape-texture bias is not a significant factor for accurate models. (2) With the recent progress in prompt engineering, the authors might want to explain better "why prompts change the model behaviors," which is non-trivial.

* W4: With this paper focusing on analysis, a crucial yet missing analysis is to rule out the biases from LLMs. For example, if the prompt mentioned in the paper contains the words of "textures" or "shapes," will the shape/texture biases observed related to the prior knowledge in the LLMs. It would strengthen the paper if authors can assist the analysis with some attention maps or other preferred measure to show that the **visual representation indeed changes** under such shape/texture steering.

### Questions
Please see above for questions. The importance would be W1 --> W3 --> W4 --> W2. Overall, better clarifying the significance of this study would improve my scoring.

### Soundness
3

### Presentation
3

### Contribution
2
