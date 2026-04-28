# Cross-Attention Head Position Patterns Can Align with Human Visual Concepts in Text-to-Image Generative Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Recent text-to-image diffusion models leverage cross-attention layers, which have been effectively utilized to enhance a range of visual generative tasks. However, our understanding of cross-attention layers remains somewhat limited. In this study, we present a method for constructing Head Relevance Vectors~(HRVs) that align with useful visual concepts. An HRV for a given visual concept is a vector with a length equal to the total number of cross-attention heads, where each element represents the importance of the corresponding head for the given visual concept. We develop and employ an ordered weakening analysis to demonstrate the effectiveness of HRVs as interpretable features. To demonstrate the utility of HRVs, we propose \emph{concept strengthening} and \emph{concept adjusting} methods and apply them to enhance three visual generative tasks. We show that misinterpretations of polysemous words in image generation can be corrected in most cases, five challenging attributes in image editing can be successfully modified, and catastrophic neglect in multi-concept generation can be mitigated.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work proposes Head Relevance Vectors (HRVs). HRs are an extension of the findings from previous works such as Hertz et al.'s P2P where cross attention maps were used to better understand t2i models and to edit images via prompts. HRV proposes using multiple concept words and concatenating them into a concept embedding matrix K which can then be applied to different heads of the cross-attention and by doing so, disentangle the different heads based on the concept they seem to be focusing on. The authors show this disentanglement of heads based on the concepts learned improved editing of images.

### Strengths
The motivation of the paper is clear and build on a well studied problem of understanding the role of cross-attention and what they learn in editing T2I models. The experiments are visually appealing and tell the story of the paper well, especially the weakening of HRVs that shows weakening based on the most and least relevant concepts / heads. The authors show that using HRVs to edit images works better than SDEdit,P2P, etc. They also show improvement over Attend and Excite for the problem of catastrophic forgetting in T2I models.

 While in the weaknesses, I do mention my thoughts on the originality of this work, I believe using previous findings around CAs and targeting different heads and their roles in generating different concepts would be interesting to the community.

### Weaknesses
I would argue that the work, while interesting, does not have new insight compared to what previous works such as P2P and Diffusion Self-Guidance have already already shown in regards to the role of cross-attentions. Specifically, the idea of manipulating cross-attention maps to control image generation is well-established, and this work seems to primarily extend that by focusing on individual attention heads. While the authors demonstrate that different heads respond to different concepts, the core mechanism of using attention maps for editing remains similar to prior work. The disentanglement of heads based on concepts, while useful, feels like a logical progression rather than a fundamentally new insight into the workings of T2I models. It goes without saying that T2I models could benefit from more comprehensive evaluation on larger set of generated images / human evaluation. However, I do understand the challenges this poses as well.

### Questions
There have been recent works that show the <SOT> and <EOT> CAs capture different concepts. I would be interested to see if the authors found anything interesting regarding HRV and these tokens. I am also curious as to how the weakening and strengthening would work on more complex images that share entangled objects and concepts. For instance, what would weakening of "melting" look like for "a plastic car melting". I think this would be an interesting experiment since adjective and verb concepts are entangled with an object in a given image and HRV might to better in these cases than the counterparts.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a method of constructing so called "HRV" vectors, which align with visual concepts. The authors leverage cross-attention layers of Stable Diffusion model to learn those vectors for predefined concepts. The proposed method helps to solve three known issues of the image synthesis task.

### Strengths
1. Good motivation and a clear idea
2. Comprehensive quantitative and qualitative comparisons with many other solutions
3. The experiments, settings, and other details are mainly clearly explained

### Weaknesses
1. It requires fixing a set of concepts beforehand for every HRV construction. Does not have a study of how the HRV matrix will be changed when some concepts are changed or replaced after the construction. The method's reliance on a fixed concept set limits its adaptability to dynamic scenarios where concepts might need to be added, removed, or modified. A more robust approach would ideally allow for incremental updates to the HRV matrix without requiring a complete reconstruction.
2. Manual settings, choice, and configuration are required for every concept (case) during inference (Sec 5.1, Fig 5). The need for manual intervention for each concept during inference introduces a significant practical limitation. This lack of automation hinders the scalability and usability of the method, especially when dealing with a large number of concepts or when real-time adjustments are needed. The process should be streamlined to reduce user burden and improve efficiency.
3. Lack of failed cases, there are no details about the limitations of this method. The absence of a thorough analysis of failure cases makes it difficult to assess the robustness and reliability of the method. A comprehensive evaluation should include examples where the method fails, along with an explanation of why these failures occur. This would provide a more balanced view of the method's capabilities and limitations.
4. Even though there is a section for bigger / novel models (SDXL), all experiments, studies, and comparisons are based on SD v1. New models might eliminate many issues the proposed method tries to solve. The exclusive reliance on SD v1 for experiments and comparisons raises concerns about the generalizability of the findings to more advanced models like SDXL. Given the significant improvements in SDXL, it is crucial to evaluate the proposed method on these newer models to determine its relevance and effectiveness in the current landscape of image synthesis.

### Questions
1. Could you give more details about why there are some irrelevant concepts after a certain point of ordered weakening (Fig 9)?
2. Could you give more details about how the "h" is chosen/computed in the method of HRV updates?

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
5

### Summary
This paper tries to understand cross-attention (CA) layers *regarding attention heads*.
* The authors introduce N head relevance vectors (HRV) for N visual concepts.
* The strength of an attention head to the HRVs represent the relevance of the head to the concept.

Above properties are interpreted by *ordered weakening analysis*.
* Sequentially weaken the activations of CA heads to observe weakened visual concepts.

Boosting and reducing the strength of different heads control the strength of visual concepts. It helps three applications: 1) correcting mis-interpretation of words in t2i generation, 2) boosting prompt-to-prompt, 3) reducing neglect in multi-object generation.

### Strengths
1. This paper provides a new perspective in understanding the features in text-to-image generation: different heads.
2. Qualitative examples (Figure 3a) and CLIP similarities (Figure3b) along weakening MoRHF and LeRHF clearly show the effect of weakening different heads.
3. The appendix provides extensive qualitative results to remove doubt for cherry-picked results.
4. The proposed method is useful for three applications: 1) correcting mis-interpretation of words in t2i generation, 2) boosting prompt-to-prompt, 3) reducing neglect in multi-object generation.
5. Discussions resolve natural questions: extension to SDXL and effect across different timesteps.

### Weaknesses
1. The paper should provide principles of the proposed approaches.
    * L224 Why should we count each visual concept having the largest value to update the HRVs?
    * This is the most critical weakness for not giving a higher rating. I think the perspective is worth noticing but a solid paper should provide why/how it works.
    * Answering this question with theoretical justifications or intuition would strengthen the paper.
2. HRV should be described more clearly.
    * L205 a concatenation of token embeddings // concat along which axis? I guess the result of concatenation is $N \times (d + H)$. Then the query Q does not match the cross-attention operation because $Q\in R^d$. Am I missing something?
    * L210 K1, ..., KN should be denoted in Figure 2.
    * Adding equations and proper notations would help readers to understand the operation.
3. Human evaluation should be explained in more detail.  Appendix C.2 is not enough. Adding a table with Number of participants, Number and types of questions, Number of questions per participant, and Any quality control measures used would strengthen the user study.

### Questions
I wonder the interpolation between different strengths of a head. For example, interpolating  material=[-2, 2]?

### Soundness
2

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
4

### Summary
This paper mainly focuses on the explainability of text-to-image diffusion model. The authors propose a new metric based on the cross-attention heads in the diffusion UNet to illustrate the correlation between each attention head and visual concepts. Based on the proposed Head Relevance Vectors, the authors further propose several applications including solving polysemous words problems and image editing.

### Strengths
1. The idea of correlating visual concepts with diffusion models is interesting.

### Weaknesses
1. I suggest the authors add textual description of the proposed HRV instead of directly showing Fig. 2 and Fig. 4 for better understanding. The current presentation makes it difficult to grasp the precise mathematical formulation and the underlying intuition behind the Head Relevance Vectors. A more detailed explanation of how the cross-attention maps are processed and aggregated to form the HRV would be beneficial. For example, clarifying how the attention weights are normalized and combined across different layers and heads would greatly improve clarity.
2. I wonder why <SOT> and many <EOT> are required during update of HRV? It's unclear why these specific tokens are necessary for the HRV update process. The role of these tokens in the CLIP text encoder and how they interact with the attention mechanism needs further explanation. Specifically, it's not clear if these tokens are used as padding or if they have some semantic meaning in the context of HRV calculation. 
3. It would be better to used SDXL or some more recent models such as SD3 as primary model, given that SD1.5 is kind of outdated. The choice of SD1.5 limits the applicability of the proposed method to more recent and advanced diffusion models. The performance and effectiveness of the proposed method on models like SDXL or SD3, which have different architectures and training procedures, remains unclear. It's important to demonstrate the generalizability of the method to these more contemporary models.
4. It would be better to add a random weakening baseline in Fig.3. The absence of a random weakening baseline makes it difficult to assess the effectiveness of the proposed ordered weakening method. It is crucial to compare the performance of the proposed method with a baseline that randomly weakens attention heads to demonstrate that the observed performance gains are not simply due to weakening any set of attention heads.
5. In Sec.5.1 the authors show that by utilizing HRV the SD can generate more proper concepts. I wonder if this method can be compared with using classifier guidance, where the model is encouraged to align the generated image with wanted concepts in terms of CLIP score. The lack of comparison with classifier guidance makes it difficult to assess the relative advantages and disadvantages of the proposed method. A comparison with classifier guidance, which is a well-established method for guiding image generation, would provide a more comprehensive evaluation of the proposed method's effectiveness.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
