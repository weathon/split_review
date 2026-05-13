# Diffree: Text-Guided Shape Free Object Inpainting with Diffusion Model

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
This paper addresses an important problem of object addition for images with only text guidance. It is challenging because the new object must be integrated seamlessly into the image with consistent visual context, such as lighting, texture, and spatial location. While existing text-guided image inpainting methods can add objects, they either fail to preserve the background consistency or involve cumbersome human intervention in specifying bounding boxes or user-scribbled masks. To tackle this challenge, we introduce Diffree, a Text-to-Image (T2I) model that facilitates text-guided object addition with only text control. To this end, we curate OABench, an exquisite synthetic dataset by removing objects with advanced image inpainting techniques. OABench comprises 74K real-world tuples of an original image, an inpainted image with the object removed, an object mask, and object descriptions. Trained on OABench using the Stable Diffusion model with an additional mask prediction module, Diffree uniquely predicts the position of the new object and achieves object addition with guidance from only text. Extensive experiments demonstrate that Diffree excels in adding new objects with a high success rate while maintaining background consistency, spatial appropriateness, and object relevance and quality.
\keywords{Image inpainting \and Text-guided image editing}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes solving the object painting problem with only text as guidance and does not rely on other constraints, e.g., shape mask. The authors first construct a synthetic dataset, called OABench, to facilitate the model’s training with the help of the existing SOTA inpainting model. Then, a diffusion-based model named Diffree is proposed to train on this OABench that can simultaneously output the image with the added object and the object mask. Finally, the authors also conduct comparisons to validate the superiority of their method.

### Strengths
- Object inpainting using only text without relying on shape constraints.
- The authors built an OABench to facilitate text-guided object inpainting.
- The results are attractive and the supported applications are interesting.

### Weaknesses
 - Lack of ablation of the validation model design. For example, what happens to the output if the OMP is removed? BTW, integrating a mask head in the diffusion process is not new, e.g. in [1].
- The comparison is slightly unfair. In Figure-A10, comparing the model you trained on the curated dataset to other methods that were not retrained or fine-tuned is unfair.
- This paper is poorly written, especially the explanation of the charts. For example, in line 50 of the description section, the author provides links to three figures for the reader to view. However, these figures lack sufficient detail to explain what the figure depicts and what the symbols within the figures/captions represent.

### Questions
- How well does the model generalize? Since the model was trained on a synthetic dataset generated from an inpainting model, it is not surprising that the model may overfit the artifacts introduced by the inpainting model.
- In Line 468, the authors argue that their Local CLIP Score is slightly inferior to the InstructPixel2Pixel due to the latter considers only the successful results are taken into consideration. I wonder what the results will be if you combine both the successful and failure cases.
- Regarding the generalization problem, assuming that a real image contains two dogs, and I first use PowerPaint to delete the two dogs, and then let the proposed Diffree generate one dog, what will the output image show? Will the position of the new dog duplicate the position of the previously removed one?
- Were the compared methods (e.g., InstructPix2Pix) trained on the proposed dataset as well? or just directly copied their pre-trained weights for use?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents a novel model, Diffree, which facilitates the addition of objects to images. The authors have constructed a synthetic dataset named OABench, consisting of 74K real-world tuples, to train Diffree using a Stable Diffusion model augmented with an additional mask prediction module. Diffree predicts the target mask and generates inpainting results simultaneously. Extensive experiments demonstrate Diffree's good performance in adding new objects with high success rates while preserving background consistency, spatial appropriateness, and object relevance and quality.

### Strengths
1. Diffree offers a user-friendly approach to inserting objects into images. The mask-free object insertion is particularly useful in practical applications.
2. The creation of OABench, a large-scale synthetic dataset, is a significant contribution, providing a rich resource for training and evaluating object addition models.
3. The OMP module's ability to predict the target mask and generate inpainting results simultaneously is a novel architectural advancement in this field.

### Weaknesses
1. [1] proposed a method for mask prediction closely related to Diffree. An in-depth analysis and comparison with this work would be beneficial. Specifically, the paper should discuss how Diffree's mask prediction module differs in architecture and training methodology from [1], and whether it achieves comparable or superior performance in terms of mask quality and object insertion accuracy.
2. All the prompts used in this paper are in the form "add {object}". It is unclear how Diffree generalizes to more precise control, such as "add a dragon in the room". The paper needs to demonstrate the model's ability to handle complex spatial relationships and object attributes specified in the prompt, such as object size, pose, and orientation, and how these are reflected in the generated image.
3. While user-friendly for object insertion, it restricts users from adjusting the mask. In standard image processing, users or designers often need to make adjustments to achieve their desired results. The paper should discuss the limitations of not allowing mask adjustments, and how this impacts the flexibility and control users have over the object insertion process. It should also consider how the generated masks could be used as a starting point for further refinement using standard image editing tools.

### Questions
1. In Fig. 1, the "add dragon" prompt results in "a dragon painting in the frame". Is this behavior as expected?
2. How does Diffree perform with out-of-distribution (OOD) objects not included in OABench?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces Diffree, a text-to-image (T2I) model aimed at text-guided object addition within images, a process where new objects are integrated into a scene while maintaining visual consistency in lighting, texture, and spatial orientation. Unlike previous approaches, Diffree avoids the need for manually defined masks, instead using a synthetic dataset (OABench) for training. OABench, composed of image pairs with and without specified objects, is created by advanced image inpainting techniques. Trained on OABench, Diffree incorporates a Stable Diffusion backbone with an Object Mask Predictor (OMP) module to predict object placement. Results indicate that Diffree achieves high success in preserving background coherence, achieving spatially plausible integration, and producing visually realistic objects.

### Strengths
- **Originality**: Diffree’s approach of shape-free object addition guided solely by text is novel, significantly enhancing usability by eliminating the need for manual mask definitions. This innovation in user experience represents a unique contribution.
- **Clarity**: Overall, the dataset creation process, and evaluation metrics are well-described, with figures that aid understanding of Diffree’s operational and comparative performance.

### Weaknesses
 - **Minor Typographical Issue**: There is a missing period at the end of line 101, which should be corrected for clarity.
- **Dataset Limitation in Prompt Detail**: Since the dataset primarily relies on the COCO dataset, prompts are often generic object labels rather than detailed, fine-grained descriptions. This limitation can hinder the model's ability to respond to nuanced or interactive prompts, such as requests for specific object attributes or context-based interactions.
- **Methodology Clarity**: The description of the proposed methodology, especially the Object Mask Predictor (OMP) module, could benefit from further clarification. For example, more detail on why the image latent and latent noise are concatenated as inputs for the OMP module during both training and inference phases would help improve comprehension.
- **Figure 6 Presentation**: Figure 6 needs a more detailed caption to allow readers to follow the workflow easily by reading only the figure caption. The current figure layout lacks clarity, making it challenging for readers to understand the process.
- **Inconsistency in Visuals (Figure 1)**: In Figure 1, example 2 appears visually inconsistent, with an unrealistic rendering of the added object. This raises questions about the model's object realism under certain conditions.
- **Lack of User Study**: Including a user study would strengthen the evaluation of the model, particularly to capture subjective aspects of user satisfaction and perceived realism in object integration.
- **Limited Comparative Evaluation**: The model is only compared against PowerPaint and InstructPix2Pix. Including additional comparison baselines, such as recent text-guided inpainting methods or general object addition approaches, would provide a more comprehensive assessment.
- **Ambiguity in Object Placement in Complex Scenes**: The method struggles with complex images involving multiple entities (e.g., two people). When required to add an object to one specific entity, the model may face ambiguity, as there is limited functionality for users to adjust the mask and specify the target placement.

### Questions
1. How does Diffree handle ambiguities in scenes with multiple entities (e.g., if there are two people in an image, how does it decide which one to add the object to)? Could user input be incorporated to clarify target placement in such cases?
2. Could more fine-grained prompts be incorporated or generated to enhance the model's ability to handle specific requests for object details and interactions within a scene?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an object addition method called Diffree. Diffree comprises an object mask prediction (OMP) module, which could be used to generate masks through textual inputs. Thus Diffree can be regarded as a mask-free inpainting model. The authors also provide a synthetic dataset called OABench with 74k real-world object removal tuples built by PowerPaint. Extensive experiments verify the effectiveness of Diffree.

### Strengths
1. This paper proposed a sophisticated and reliable data collection process to achieve high-quality image removal tuples, which would potentially strengthen many other inpainting-based tasks. 

2. The authors show some promising and impressive object addition results in the appendix, including both real-world and AI-generated images.

### Weaknesses
1. As mentioned in the main paper, Diffree is trained to predict precise object masks, which is not convincing for both object removal and object addition. Because most objects contain shadows or reflections, which are not included in object masks. Without proper shadow and reflection generation, the inserted objects suffer from "copy and paste" artifacts. For example, no shadows are generated in the "Coconut palm" of Figure 3, and no reflections are generated in the "boat" of Figure A2. The metric of background consistency is also problematic. I think this is the main drawback of this method. The method's reliance on precise masks is a significant limitation, as real-world objects often have complex interactions with their environment, including cast shadows, reflections, and subtle lighting effects. These are not captured by a simple object mask, leading to unrealistic insertions. The evaluation of background consistency using LPIPS is also questionable, as it may not fully capture the perceptual differences caused by inconsistent lighting or shadows. A more robust metric that considers these factors is needed.

2. Missing discussion and ablation about the necessity of the joint training of OMP and diffusion model. Why not independently train OMP to predict the mask. The paper lacks a thorough analysis of the necessity of joint training for the Object Mask Prediction (OMP) module and the diffusion model. An ablation study should be included to demonstrate the performance of independently training the OMP module and comparing it to the joint training approach. This would provide a clearer understanding of the benefits of the proposed training strategy.

3. The generalization of the Diffree should be concerned. As shown in Figure 9 (a), the generation failed while the mask was very small. The paper does not adequately address the generalization capabilities of Diffree, particularly when dealing with very small objects. The failure case in Figure 9(a) highlights a potential limitation of the method, suggesting that it may struggle with objects that have a small spatial footprint. Further analysis is needed to understand the limitations of the method in such scenarios.

4. For the object addition guided completely by texts, the authors should provide more results to verify whether the proposed method could handle different orientational descriptions. For example, these prompts should be considered: "on left/right/up/bottom of...". The paper lacks sufficient results demonstrating the method's ability to handle different orientational descriptions in text prompts. The authors should include more examples that showcase the model's performance with prompts that specify the location of the object relative to other objects in the scene, such as "on the left of," "on the right of," "above," or "below."

### Questions
1. Why not use Diffree to address mask-free removal? This should also be addressed by OABench.

2. What did "with/without mix with previous image" mean in Figure 8?

### Soundness
2

### Presentation
2

### Contribution
2
