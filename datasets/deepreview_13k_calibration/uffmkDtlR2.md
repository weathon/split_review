# MIMOSA: Multimodal Concept-based representations

- Decision: Reject
- Avg Score: 2.60
- Scores: 5, 3, 1, 1, 3

## Abstract
In recent years, deep learning-based architectures have significantly improved multimodal representation. However, interpretability remains challenging with traditional attention and gradient-based methods, offering limited insights into decision-making processes. Concept-based explainability provides intrinsic model interpretability by mapping raw data to higher-level abstractions, yet it has only been applied to unimodal data. 
We present MIMOSA (MultIMOdal concept-based repreSentAtion), a unified multimodal model that integrates concept-based interpretability. Our research shows that exploiting a joint multimodal conceptual representation achieves comparable accuracy with multimodal black-box models, surpassing approaches based on unimodal concepts. This unified representation also prevents misclassification of concepts between modalities and improves concept interventions. Through a concept decoder, MIMOSA can extract concept visualizations for each modality. 
Experimental results obtained from three distinct multimodal datasets substantiate the efficacy of our approach, showcasing enhanced interpretability in multimodal models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a new method - MIMOSA to interpret multimodal models.  It builds upon the success of using concept-based representations in unimodal settings. The authors propose that a shared concept representation across all modalities offers better insights into the model’s decision making process instead of having a concept representation for each modality. With the help of three different datasets - MNIST+, cdSprites+, CUB, the authors prove the accuracy of such a model. The authors also use individual modality decoders to extract information from the shared concept embedding.

### Strengths
1. Originality: The paper presents a new method to interpret multimodal models. The concept of using a single concept embedding with individual concept decoders is novel. 

2. Quality: The paper provides a detailed analysis of the results, acknowledging that the model's task accuracy is suboptimal for certain datasets. The authors later also discuss why this is the case. Specifically, the sections “COMPARING SHARED AND SEPARATE EMBEDDINGS”, “EFFICACY OF INTERVENTION IN MULTIMODAL CONCEPT-BASED MODELS”, and “QUALITATIVE ANALYSIS OF REPRESENTATIVE CONCEPT EXAMPLES” are rife with information. These sections are also easy to follow as they have examples wherever needed. The example where the model interprets the 4 in an image as 3, shows the potential this method has. 

3. Clarity: The paper is very well structured. The paper provides good context prior to the main methodology. Placing the related work section at the end helps maintain focus on this paper's contribution without disrupting the flow. The authors used good and relevant datasets for this work. 

4. Significance: Multimodal interpretability has always been a challenging problem. There is a lot of research producing new black box models but very few talk about their interpretability. The paper correctly highlights that attention-based interpretability methods only show where the model is looking and not necessarily what the model is understanding. Knowing what the models are understanding can help us delve deeper into model performance. It would also help us identify biases in the models.
Overall, the paper shows a good promise towards interpreting multimodal models better.

### Weaknesses
1. Lack of clarity in the initial sections: The structure of the paper, particularly the ordering of the sections, is well-organized. The initial sections are very generic. Specifically, section 2 - Background and section 3 - Methodology. Concept-based representation is the key contribution of this paper. However, very little is mentioned about what that embedding could look like. The background section very briefly discusses concept based representations but those definitions are a little lacking and need to provide more insights. Understanding subsequent sections is challenging without prior knowledge of related work.. The section on multimodal representations does not offer much except the definitions of early and late fusion strategies in generic multimodal models. A lot of this section can be removed. Section 3 talks about the main methodology and is very brief and doesn’t provide enough information.

2. No Training Details: The paper talks about all of the models used for experiments but doesn’t provide any details about the training strategies used. Adding details about which models are pre-trained can help understand the paper a little better. Consider adding this information to the appendix of the paper. There are multiple networks in the paper potentially being trained on different objectives. Talking about the loss functions for each is helpful.

### Questions
1. Are all the encoder and decoder networks pre-trained? If not, what training procedure was used?
2. Could you provide a more detailed explanation of concept prediction and its significance within the context of this paper?
3. What training objectives are used for the decoder? How do we make sure that training the decoder doesn’t introduce any biases?
4. Why is the generalization capability of concept based models limited and how is concept embedding improving it?

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
This paper applies concept bottleneck models to multimodal data, proposing the MIMOSA (MultIMOdal concept-based representations) approach. The method is composed of a concept layer and multimodal decoders. The concept layer aggregates the modality-dependent encoders' representations and generates concept prediction scores and embeddings. Decoders reconstruct the inputs and visualize concepts explicitly. The experimental results show enhanced accuracy and interpretability compared to other unimodal methods.

### Strengths
- The paper is well-written and provides a clear exposition of the background, related work and proposed method.
- Concept-based interpretability is a promising research topic. Previous methods mainly focused on visual data. This paper extends the concept-based models to multimodal data, which is interesting and advantageous.
- The method in this paper is very intuitive and easy to understand.

### Weaknesses
 - The proposed method lacks innovation. There is little difference between CEM and MIMOSA, and the decoding-based visualization strategy is also commonly used.
- In this paper, the author only utilizes the limited-scale datasets, not validating the efficiency of large-scale multimodal datasets. I think at least one large dataset should be conducted experiments to demonstrate the scale-up capacity of the proposed method.
- On MNIST+ and cdSprites+, the proposed method's improvements are very few.
- This paper doesn't demonstrate the ablation studies. It needs more discussions on what module contributes to the improvement of accuracy.

### Questions
- I am not sure about the definition of the concept in this paper. The concepts for MNIST+ are more likely a group of descriptions.
- I just see the decoding visualization results at the image level. Decoding at the image level rather than at the single concept level lacks persuasion. I wonder what the results would be if we focused on one single concept.
- CBM and CEM are proposed for only visual data input, so I am unsure whether the comparisons are fair enough.
- This paper seems to apply CEM to multimodal data using a simple sum operator, lacking a delicate design for the specific setting. Moreover, the ablation studies of other pooling operators need to be done.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper introduces MIMOSA (MultIMOdal concept-based repreSentAtions), a novel unified multimodal model that integrates multimodal representation learning with concept-based interpretability techniques. MIMOSA is primarily focused on text and image modalities, aiming to enhance the interpretability of deep learning models by extracting concept prototypes from a shared embedding space.

### Strengths
Based on the traditional interpretable conceptual model, this paper proposes a multi-dimensional interpretable method, which uses image decoding and text decoding strategies to provide multi-dimensional interpretable strategies for the source data, and provides a new interpretable perspective.

### Weaknesses
1) The experimental data are not convincing. In Table 1, the method proposed in this paper does not maintain a high level and cannot reflect the superiority of multidimensional interpretability. Secondly, in terms of multidimensional interpretability, this paper does not make a clear contrast with the existing methods on the interpretation Angle, and does not clearly reflect the meaning of multidimensional.

2) This paper proposes multi-dimensional interpretable methods, the purpose is not clear, is it to improve interpretability, improve robustness, or improve task performance? Purpose 3 should be excluded first, because the proposed method does not outperform the existing models in the data set of this paper. Secondly, the improved interpretability lacks demonstration and fails to well reflect the interpretability perspective. Ultimately, for robustness, there is a lack of a specific description of the intervention. Is the intervention performed on the input image, the input text, or some other input source?

3) Figure 3 should have errors, task accuracy should not rise as the intervention is enhanced, here should be drawing errors.
The training details of this paper need to be further clarified. How is it trained for the added text description? How is it applied against the existing concept data, and how is it aligned against the generated image decoder? Further clarification is needed.

4) For the experiment of intervention, it is necessary to supplement the intervention of image and the intervention of input text, so as to achieve a more comprehensive response robustness. However, this paper lacks relevant descriptions.

5) No ablation experiments were performed in this paper, so the specific role of each module cannot be clarified.

6) For the CUB200 dataset, how to carry out the text supplementary description? Further clarification is needed.

7)How to evaluate the concept accuracy in Table2? The concept structure of interpretable description generated by this method is different from that of data annotation. How to evaluate it?

8) For Table1, why design a txt only benchmark? What does txt alone say? Moreover, for CBM and CEM models, without the input of image, how can the accuracy rate be obtained?

### Questions
see weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
In this paper, the authors presented MIMOSA, a multimodal model that encodes each modality with unimodal encoders, fusion with addition, and has an additional reconstruction loss. MIMOSA was evaluated against baselines on 3 tasks, where MIMOSA achieved top performance in none of the tasks. The authors also evaluated MIMOSA's conceptual accuracy and concept mismatch rate, and qualitatively demonstrated that the decoders can reconstruct the input.

### Strengths
None.

### Weaknesses
This paper has no significant contribution. The proposed method is basically a simple multimodal model with unimodal encoders, fusion by summation, and reconstruction loss with decoders. Multimodal reconstruction loss already exist in many existing papers (e.g. MVAE, which is actually mentioned in the paper). 2 out of 3 datasets used in the experiments are really simple where multiple methods achieve near-perfect performance; and the proposed method did not achieve top performance in any of the datasets. The proposed method also does not improve model explainability at all. Being able to reconstruct inputs from multimodal representation (section 4.4) is not explainability; it just means the reconstruction loss worked. The so-called "concept" generated by MIMOSA is just a vector representation of the multimodal input, with no objective making it any more interpretable than usual autoencoder-generated representation vectors. Therefore, there is no clear takeaway message from the paper.

This paper also has a lot of important details missing, which makes interpretation of results and reproducing the method impossible. The missing information includes (but not limited to):

1. Full training objective; which parts of MIMOSA is trainable and which ones are frozen; how are decoders trained

2. How Stable Diffusion can be used (and trained) as an image reconstruction decoder

3. Evaluation metrics: there is no concrete definition of Concept Accuracy and Concept mismatches, which makes the majority of results in sections 4.1 and 4.2 uninterpretable. 

4. How the experiments were repeated (to get the Standard Deviations in the tables), and what learning rate/optimizer was used

5. Baseline details: there is no description of what exactly E2E is at all, even though it got highest performance on CUB by a large margin. There is also no detailed hyperparameters about any of the baselines.

The paper also has the following additional presentation issues:

1. Inconsistent notations: the decoders are notes as $\Psi_i$ in text and $\bar{h_i}$ in Fig 1. Also, in line 183, the exact same variable is written differently ($\Psi(c)$ and $\Psi_i(c)$)

2. Dataset name inconsistency: the second dataset is called differently ("cdSprites" and "cdSprites+") multiple times across many locations in the paper ("cdSprites" in Fig 3 caption and Fig 6 caption and line 242, "cdSprites+" for other 13 occurrences)

3. It is unclear why the text is aligned in different directions among the subfigures in Fig 4

4. In Fig 2, it is really strange to draw both models and vectors with identical circles

### Questions
1. What is the overall training objective of MIMOSA? The only objective mentioned in the paper is $L_{dec}$, which can't possibly be the only objective used to train the model. You at least need the supervised task objective. How is $L_{dec}$ combined with the supervised objective?

2. Which parts of MIMOSA is being trained and which parts are frozen? Do you jointly train all your unimodal encoders with the rest of the model? How do you jointly train a Stable Diffusion model with the other parts of your model?

3. How exactly are the standard deviations obtained for your experiments? Please provide details on whether you repeated your experiments with different seeds, and for how many times. The standard deviations for a lot of entries in the table looks unreasonably low.

4. Please also provide the other hyperparameters for your experiments, such as learning rates and baseline implementations.

5. In Eq(1), how does a summation of unimodal representations (since $\Phi$ is simple summation operator) yield 2 outputs? And what exactly do you do with $\hat{c}$?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces MIMOSA (MultIMOdal concept-based repreSentAtions), a novel multimodal framework that leverages concept bottleneck models (CBMs) to address interpretability challenges in multimodal tasks. By jointly learning shared concepts from image and text data, MIMOSA offers a unified representation that enhances transparency in multimodal decision-making, overcoming trade-offs inherent in traditional CBMs. Experimental results demonstrate that MIMOSA outperforms state-of-the-art methods on various benchmarks, providing a promising approach for interpretable multimodal learning.

### Strengths
1. Improved Multimodal CBM: The paper successfully extends Concept Bottleneck Models (CBMs) to the multimodal domain, addressing limitations and trade-offs inherent in traditional CBM approaches. MIMOSA demonstrates improved performance and a better balance of interpretability and accuracy. 
2. Consistent Multimodal Representation: MIMOSA introduces a shared concept representation to ensure consistent representation of concepts across different modalities, enhancing transparency and interpretability in multimodal models. 
3. Independent concept decoding: The model's independent concept decoding enables detailed visualization of modality-specific concepts, providing valuable insights into the decision-making process and boosting model trustworthiness. 
4. Demonstrated Performance on Benchmark Datasets: The paper provides strong empirical evidence of MIMOSA's effectiveness through experiments on well-established benchmark datasets like MNIST++ and CUB.

### Weaknesses
1. Detailed Model Architecture: A more detailed explanation of the model architecture, including the specific structure of the function 𝑓 and decoder, would enhance the clarity of the technical implementation. Specifically, the paper lacks details on the specific layers, activation functions, and parameters used within the encoders, the concept embedding layer, the task predictor f, and the decoders for both image and text modalities. The absence of this information makes it difficult to reproduce the results and assess the model's complexity and computational requirements.
2. Figure 1 Alignment: In Figure 1, it is unclear where the network 𝜓 is located. Aligning Figure 1 with the main text for consistency and clarity would improve readability and understanding of the model components. The current diagram does not clearly show how the different encoders, concept embedding layer, and decoders interact, leading to ambiguity in the overall architecture.
3. Inclusion of Recent References: The references section should include recent relevant papers such as (1) LaBO, (2) BotCL, and (3) ResCBM to provide a comprehensive review of the state-of-the-art.

   (1) Oikarinen, T., Das, S., Nguyen, L. M., & Weng, T. W. Label-free Concept Bottleneck Models. In The Eleventh International Conference on Learning Representations.

   (2) Wang, B., Li, L., Nakashima, Y., & Nagahara, H. (2023). Learning bottleneck concepts in image classification. In Proceedings of the ieee/cvf conference on computer vision and pattern recognition (pp. 10962-10971).

   (3) Shang, C., Zhou, S., Zhang, H., Ni, X., Yang, Y., & Wang, Y. (2024). Incremental residual concept bottleneck models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 11030-11040).

4. Clear Novelty Distinction: A clearer delineation of MIMOSA's novelty, particularly in relation to recent label-free CBMs (LaBO) and ResCBM (as suggested in item 3) approaches, would strengthen the paper's contribution. The paper needs to articulate how MIMOSA's approach differs from these methods, especially in terms of the training process, concept representation, and handling of multimodal inputs.
5. Limited Dataset Scope: The paper uses a limited number of datasets for the experiments. Expanding the experimental evaluation to include additional datasets like CUB, CelebA, CheXpert, and AWA2 would provide a more comprehensive performance assessment. The current evaluation does not sufficiently demonstrate the generalizability of the proposed method across different types of multimodal data and tasks.
6. Text Data Source Clarification: Specifying the source of the text data used in the experiments would enhance the contextual understanding of the dataset. The paper should clarify how the text data was generated or collected, and if any preprocessing steps were applied.
7. Expanded Model Comparisons: The experimental section includes a limited number of comparative models, primarily CBM and CEM. To provide a more comprehensive evaluation, it is recommended to incorporate recent CBM models such as Post-hoc CBM, LaBO, and ECBM, as suggested in item 3. The current comparisons do not provide a complete picture of MIMOSA's performance relative to state-of-the-art methods.
8. Negative Intervention Experiments: Incorporating negative intervention experiments would provide a more complete assessment of MIMOSA's behavior under different intervention scenarios.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
