# Interpreting and Editing Vision-Language Representations to Mitigate Hallucinations

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 6, 5

## Abstract
We investigate the internal representations of vision-language models (VLMs) to address hallucinations, a persistent challenge despite advances in model size and training. We project VLMs' internal image representations to their language vocabulary and observe more confident output probabilities on real objects than hallucinated objects. We additionally use these output probabilities to spatially localize real objects. Building on this approach, we introduce a knowledge erasure algorithm that removes hallucinations by linearly orthogonalizing image features with respect to hallucinated object features. We show that targeted edits to a model's latent representations can reduce hallucinations by up to 25.7\% on the COCO2014 dataset while preserving performance. Our findings demonstrate how a deeper understanding of VLMs' latent representations can enhance reliability and enable novel capabilities, such as zero-shot segmentation

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the issue of hallucinations in Vision-Language Models (VLMs) by interpreting and editing their internal representations. The authors apply the logit lens technique to project image representations onto the language vocabulary, discovering that objects present in the image have higher internal confidence scores compared to hallucinated objects. Utilizing this insight, they propose a method to detect hallucinations within VLMs. Furthermore, they introduce a knowledge erasure algorithm called PROJECTAWAY, which linearly orthogonalizes image features with respect to hallucinated object features to remove hallucinations from the model's output. The method is evaluated on two state-of-the-art VLMs, LLaVA 1.5 and InstructBLIP, showing a reduction in hallucinations by up to 25.7% on the COCO2014 dataset while preserving overall performance. Additionally, the authors demonstrate that their approach enables zero-shot segmentation by spatially localizing objects using internal confidence scores.

### Strengths
- The paper introduces a novel application of the logit lens technique to interpret the internal image representations of VLMs, providing new insights into how these models process visual information.
- The proposed knowledge erasure algorithm, PROJECTAWAY, is a simple yet effective method that relies solely on manipulating the internal features of the VLMs without requiring additional training or external modules.
- The approach enables zero-shot segmentation by leveraging internal confidence scores to spatially localize objects
- The paper seems clear and well-written.

### Weaknesses
 - The proposed method requires specifying weight factors and selecting specific layers to retrieve text representations and apply edits. These hyperparameters are determined through ablation studies and do vary between models, and likely between datasets as well, requiring cumbersome ablation process to find good numbers.
- The experiments focus primarily on object hallucinations in image captioning tasks. It is unclear how the method performs on other types of hallucinations (e.g., action or attribute hallucinations) or on other tasks such as visual question answering (VQA).
- The impact of the method on overall caption quality is not thoroughly evaluated quantitatively. While the authors mention that the method preserves performance and provide some qualitative examples, additional quantitative evaluations would be interesting to see.
- The authors only seem to test their model on COCO2014.

### Questions
- How sensitive is the proposed method to the selection of weight factors and layers across different models and datasets? Is there a way to generalize these hyperparameters or make the method more robust to their selection?
- How does the method perform on other tasks, such as visual question answering (VQA) or on other datasets beyond COCO2014? Have you considered testing the method on benchmarks like LLaVA Bench or MM-Vet?
- Is there a way to automate or simplify the selection of hyperparameters (e.g., layers, weight factors) to make the method more practical for real-world applications?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors use Logit Lens to interpret the intermediate image representations in LVLMs. For a given image embedding, they extract the latent representation of the image embedding at a specific layer, taking the logit lens to get the probability distribution over the vocabulary. 
- The highest probability of an object across image representations and layers, can act as the internal confidence of VLMs. The confidences for objects present are significantly higher than those of objects not present in the image.
- The authors propose an algorithm, ProjectAway, erasing objects from image representations.
- Moreover, they find that, using the internal confidence values, they can localize the objects in the image patches.

The authors show three applications of their findings and the algorithm: hallucination detection, hallucination mitigation, and zero-shot segmentation.

### Strengths
- The findings are well-written and easy to understand.
- The experiments are comprehensive, exploring different aspects of internal visual information and covering different tasks.
- The proposed approach achieves significant improvements or comparable performance to SoTA on three applications.

### Weaknesses
### Major
- Is the unembedding matrix for image representations directly from the LVLM last layer, or trained by the authors?
- Previous papers report the modality gap between language and vision in VLMs. In my experiments, I also notice that the distribution of vision tokens are significantly different from that of textual tokens. So I’m surprised that the logit lens can be directly used in image representations. 
I’m curious about the classification accuracy of logit lens. For example, if we feed a patch of cat, how accurate is the logit lens method to identify it is cat.
- Lines 200-202, the authors “randomly sample a subset of” objects not present. I’m wondering if this random sampling will choose some objects “obviously” not present in the image, making the comparison of the internal confidence too easy. It might be better if the authors can show: the confidence distribution of objects that commonly appear with objects in the image but not present this time.
- Section 5.3, I think LLaVA tends to generate some very general class when classifying an image, like predicting "dog" instead of “husky”. Are the authors using the generated class name from LLaVA no matter what it is or using the ground truth label?

### Minor
- InstructBLIP and LLaVA are representative LVLMs, but recent LVLMs are using more complicated vision embedding techniques [1, 2]. I’m wondering if the proposed method can still work with these new architectures.
- If we want to detect or remove the hallucinated objects, the propose method needs to know the object name. I'm wondering if the proposed method can work on a popular hallucination benchmark POPE [3]? In POPE, every sample is a "yes or no" question, like "Is there a person in the image?"
- Other limitations like handling multi-token classes have been mentioned in the paper.

### Questions
Please see the Weaknesses section.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach to understanding and editing vision-language models' (VLMs) internal representations through vocabulary projection and linear orthogonalization. By introducing a knowledge erasure algorithm PROJECTAWAY, the authors demonstrate significant improvements in hallucination reduction (up to 25.7%) and achieve competitive performance in zero-shot segmentation, while providing new insights into how VLMs process visual information.

### Strengths
1. The paper presents a novel approach to interpreting and editing VLM representations through vocabulary projection and linear orthogonalization, requiring no model retraining or external components.
2. The work provides insights into VLM behavior by revealing the relationship between internal confidence scores and object presence.

### Weaknesses
1. The paper's main analysis and evaluations (Sections 3 and 4) are predominantly conducted under the assumption that hallucinated objects are known beforehand using ground truth annotations. While Section 5 addresses this limitation with a more realistic approach using internal confidence thresholds, this should have been the primary evaluation framework. The current structure potentially overestimates the method's effectiveness by evaluating under idealized conditions.
2. The paper's structure is suboptimal, with the main analysis focusing on scenarios using ground truth annotations while relegating the more realistic approach to the applications section. 
3. The choice to use the last token for multi-token object representations (e.g., "hot dog", "dining table") lacks sufficient justification and empirical validation. The paper does not analyze potential issues with this approach, such as cases where the last token might not be the most semantically meaningful (e.g., "traffic light" where "light" alone might be ambiguous) or how this choice affects the method's performance compared to alternatives like averaging all tokens or using the first token.

### Questions
1. The paper uses the model's unembedding matrix to interpret intermediate layer representations, but this matrix is trained for the final output layer. Have you conducted any layerwise probing or training of separate unembedding matrices for intermediate layers? This could affect the reliability of interpreting earlier layer representations.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper explores the internal representations of Vision-Language Models (VLMs) to address the persistent issue of hallucinations. The authors project VLMs' internal image representations onto their language vocabulary to identify differences in token output probabilities between real and hallucinated objects. They introduce a knowledge erasure algorithm, PROJECTAWAY, which removes hallucinations by linearly orthogonalizing image features with respect to hallucinated object features. The study demonstrates that targeted edits to a model's latent representations can reduce hallucinations while preserving performance. Additionally, the paper presents a method for zero-shot segmentation using the logit lens technique, showing comparable performance to state-of-the-art methods.

### Strengths
- The paper presents a newmethod for reducing object hallucinations in VLMs by editing their latent representations and the introduction of PROJECTAWAY offers a new technique for selectively removing hallucinated objects from VLMs' outputs.

- The authors provide a thorough analysis of the internal confidence values for object presence and absence, offering empirical evidence that supports their claims.

### Weaknesses
 - While the paper focuses on object hallucinations, it does not explore the applicability of the methods to other elements of visual scenes, such as people, attributes, or actions. The editing approach may struggle with abstract or complex sentences involving object attributes or interactions, which are not explicitly addressed in the paper.

- Could the authors elaborate on the potential impact of their editing techniques on other aspects of model performance, such as accuracy in non-hallucination tasks?

- The paper's reliance on LLaVA and InstructBLIP as baseline MLLMs does not provide a comprehensive comparison with the latest state-of-the-art models.

### Questions
-  Would the authors consider including comparisons with the latest MLLMs, such as those incorporating more advanced architectures or larger datasets, to validate the robustness of their approach?

### Soundness
3

### Presentation
3

### Contribution
2
