# Cafe-Talk: Generating 3D Talking Face Animation with Multimodal Coarse- and Fine-grained Control

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Speech-driven 3D talking face method should offer both accurate lip synchronization and controllable expressions. Previous methods solely adopt discrete emotion labels to globally control expressions throughout sequences while limiting flexible fine-grained facial control within the spatiotemporal domain. We propose a diffusion-transformer-based 3D talking face generation model, Cafe-Talk, which simultaneously incorporates coarse- and fine-grained multimodal control conditions. Nevertheless, the entanglement of multiple conditions challenges achieving satisfying performance. To disentangle speech audio and fine-grained conditions, we employ a two-stage training pipeline. Specifically, Cafe-Talk is initially trained using only speech audio and coarse-grained conditions. Then, a proposed fine-grained control adapter gradually adds fine-grained instructions represented by action units (AUs), preventing unfavorable speech-lip synchronization. To disentangle coarse- and fine-grained conditions, we design a swap-label training mechanism, which enables the dominance of the fine-grained conditions. We also devise a mask-based CFG technique to regulate the occurrence and intensity of fine-grained control. In addition, a text-based detector is introduced with text-AU alignment to enable natural language user input and further support multimodal control. Extensive experimental results prove that Cafe-Talk achieves state-of-the-art lip synchronization and expressiveness performance and receives wide acceptance in fine-grained control in user studies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes CafeTalk a diffusion-based method for speech driven 3D talking faces with coarse- and fine-grained multimodal control over facial expressions. CafeTalk has a two-stage training process: in the first stage the model is trained with coarse-grained conditions (e.g. emotions, talking style) using a text encoder. In the second stage it incorporates  fine-grained conditions (localized muscle movements using action units) are learned. A swap-label mechanism is proposed in the second stage to add fine-grained conditional control. Experimental results show that CafeTalk achieves state-of-the-art performance in lip synchronization and expression generation compared to existing methods.

### Strengths
1. Novel approach with the use of both coarse- and fine-grained control for 3D talking face generation. This dual-level control allows for more precise and expressive facial animations overcoming the limitations of previous methods that use broader less adaptable controls.
2. Extensive experimentation with evaluations using various datasets and a user study.

### Weaknesses
1. The diffusion-based approach for time series combined with the swap-label mechanism in the second stage of training may require substantial computational resources. Specifically, the memory footprint and training time for the second stage, which involves fine-grained control, could be a bottleneck, especially when scaling to longer sequences or higher resolutions. The paper lacks a detailed analysis of the computational cost, such as GPU memory usage and training time per epoch, making it difficult to assess the practical feasibility of the method.
2. As noted by the authors the model struggles with lower-face action units when they conflict with speech causing difficulties in achieving accurate synchronization between lip movements and expressions. This limitation is significant because the lower face is crucial for both speech articulation and nuanced emotional expression. The paper does not provide a clear strategy for addressing this conflict, which could lead to unnatural or inaccurate facial animations, particularly when the desired expression contradicts the speech content.

### Questions
1. A more in-depth discussion of the results is necessary in Sec. 4.2.2 when comparing with the other approaches. For example, why does your model succeed where other models may fall short? It would be interesting to analyze which specific components of your model (e.g., fine-grained control, diffusion model) contribute most to the performance improvements compared to other approaches.

2. What is the inference speed of your approach compared to the others? Can you provide a table comparing inference speeds across methods for a certain input length (e.g. 10 sec) on common hardware along with the number of parameters for each model?

3. W2v2 embeddings contain emotion information. Did you observe any instability during training if the vision and audio emotions contradict?

4. How important is the intensity embedding and the emotion intensity value? Can you include in your ablation study (Sec. 4.2.3) the impact of removing these components on model performance and expression quality?

5. Sec. 3.1.2: You mention that you mask speech audio and coarse-grained conditions with 20% probability. How is the model’s performance affected with this probability? Similarly in Sec. 3.2 you point out “we randomly drop elements triplets (Fd, Fs, Fe) from the AU sequence F” - with what probability?

6. Sec. 4.1: Are the collected YouTube videos ids going to become publicly available? Also, how do you compute the emotion expression and intensity of the collected data?

7. How long can your approach generate frames continuously without degradation in quality? Are there any limitations on sequence length, and can you provide examples for different animation durations (e.g., 3, 6, and 10 seconds)?

8. Table 1: You present results for 3D-ETF benchmark without describing it first in the text. Can you add a description of the 3D-ETF benchmark in the datasets section (Sec. 4.1)?

Minor

Table 2: Correct “Carse” to “Coarse” in the caption.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes ***Cafe-Talk***, a 3D talking face generation model that excels in multimodal control, enabling both coarse and fine-grained manipulation of facial expressions.

### Strengths
**Ideas**:  
***Cafe-Talk*** can handle both coarse and fine-grained control conditions and ensure the priority of fine-grained control signals during Stage II training and inference.

**Methodology**:
1. Unlike other methods, ***Cafe-Talk*** utilizes binary AU sequences as fine-grained conditions, avoiding the issues of poor controllability and low differentiation of facial details caused by using CLIP features of text prompts.

2. ***Cafe-Talk*** designed a swap-label mechanism to disentangle coarse and fine-grained control signals and analyses in sec. 3.2 is reasonable.

3. The mask-based CFG technique is another standout feature of ***Cafe-Talk***. It addresses the challenge of controlling the influence of fine-grained conditions on the generated facial movements, ensuring that the effects are localized to the intended time intervals. This technique prevents the leakage of fine-grained control into non-controlled intervals, which could lead to unnatural expressions. 

The experiment is quite complete. Good img and charts.

### Weaknesses
Some details are unclear; see the "Questions" section below for more information.

1. In Table 1, why not show the comparison results of syncnet metrics on the MEAD and RAVDESS datasets? On the other hand, there is little point in making comparisons on your own collected dataset. Instead, you need to conduct experiments in the absence of the 157-hour dataset.

2. Some details of the datasets are not fully elaborated. What is the tool for extracting Apple ARKit? The details of the "in-the-house video-based motion-capture model" in L361-362 need to be explained. Did you collect a video dataset using an iPhone depth camera and train a model on it to extract ARKit coeffs?

3. What is the mask $Z_{align}$ used for in L225? What does $i,j$ mean in eq. 2? And how to determine the $Z_{ctrl}^{0:T}$ in eq. 6? Was this derived manually based on FACS AU's and Apple ArKit's semantics?

4. The $CR$ metric defined in eq. 8 is not very reasonable. CR measures the difference in expression coeffs between the fine-grained control period and outside of it. However, it does not assess whether the fine-grained control matches the intended facial expressions accurately. It only indicates the presence of a change, not the correctness of that change relative to expected expressions. Modifying the CR metric or adding additional metrics to describe the accuracy of fine-grained modifications is recommended.

5. What are **Talking Styles** in coarse-grained controls, and what are they used for? In the demo video, talking style is expressed as gender, age, and race, and it is "A senior actor" in Fig. 1. However, ARKit is ID-independent, and talking style is not reflected as an input in the coarse-grained conditional control model in Fig. 2.

6. You have chosen ARKit as your motion representation, so why not use it but AU as the fine-grained control signals? By designing a text-to-ARKit model, you will obtain a fine-grained modifier sequence and can directly use it as a motion prior.

### Questions
1. In Table 1, why not show the comparison results of syncnet metrics on the MEAD and RAVDESS datasets? On the other hand, there is little point in making comparisons on your own collected dataset. Instead, you need to conduct experiments in the absence of the 157-hour dataset.

2. Some details of the datasets are not fully elaborated. What is the tool for extracting Apple ARKit? The details of the "in-the-house video-based motion-capture model" in L361-362 need to be explained. Did you collect a video dataset using an iPhone depth camera and train a model on it to extract ARKit coeffs?

3. What is the mask $Z_{align}$ used for in L225? What does $i,j$ mean in eq. 2? And how to determine the $Z_{ctrl}^{0:T}$ in eq. 6? Was this derived manually based on FACS AU's and Apple ArKit's semantics?

4. The $CR$ metric defined in eq. 8 is not very reasonable. CR measures the difference in expression coeffs between the fine-grained control period and outside of it. However, it does not assess whether the fine-grained control matches the intended facial expressions accurately. It only indicates the presence of a change, not the correctness of that change relative to expected expressions. Modifying the CR metric or adding additional metrics to describe the accuracy of fine-grained modifications is recommended.

5. What are **Talking Styles** in coarse-grained controls, and what are they used for? In the demo video, talking style is expressed as gender, age, and race, and it is "A senior actor" in Fig. 1. However, ARKit is ID-independent, and talking style is not reflected as an input in the coarse-grained conditional control model in Fig. 2.

6. You have chosen ARKit as your motion representation, so why not use it but AU as the fine-grained control signals? By designing a text-to-ARKit model, you will obtain a fine-grained modifier sequence and can directly use it as a motion prior.

### Soundness
2

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
2

### Summary
This paper proposes CAFE-TALK, a 3D talking face generation model enabling coarse- and fine-grained multimodal conditional control. A two-stage training pipeline is designed to incorporate coarse control and fine-grained control. To further disentangle coarse- and fine-grained conditions, a swap-label training mechanism and mask-based CFG technique are introduced. In addition, a text-based AU detector is devised to extract AU fine-grained conditions from user-input natural language descriptions.

### Strengths
1. CAFE-TALK's primary contribution lies in enabling fine-grained, multimodal conditional control over talking faces. This is achieved through a novel two-stage training pipeline incorporating a swap-label training mechanism and a mask-based CFG technique.
2. Extensive experiments and ablation studies demonstrate that the proposed CAFE-TALK model outperforms baseline methods in both lip synchronization and expression generation.
3. The paper is well-structured and easy to follow.

### Weaknesses
1. When fine-grained control is applied to talking faces, we notice abrupt shifts in expression, such as from happy to angry. Such changes can appear unnatural and make the work less appealing if no real-world application scenarios can be found.
2. The authors demonstrate the method using examples of a single individual, raising questions about its generalizability across different faces. Additionally, fine-grained text control is only shown in a limited number of scenarios. Could the authors provide more examples to showcase this control in diverse cases?
3. For facial muscle control, only the Brow Lowerer muscle is demonstrated. How effective is the model at controlling other facial muscles?
4. Beyond fine-grained text-based control, can CAFE-TALK achieve comparable fine-grained control using images as input?

### Questions
Questions are listed in the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2
