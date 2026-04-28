# Grounded Object-Centric Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The extraction of modular object-centric representations for downstream tasks is an emerging area of research. Learning grounded representations of objects that are guaranteed to be stable and invariant promises robust performance across different tasks and environments. Slot Attention (SA) learns %composable representations using a dynamic inference-level binding scheme for 
object-centric representations by assigning objects to \textit{slots}, but presupposes a \textit{single} distribution from which all slots are randomly initialised. This results in an inability to learn \textit{specialized} slots which bind to specific object types and remain invariant to identity-preserving changes in object appearance. To address this, we present \emph{\textsc{Co}nditional \textsc{S}lot \textsc{A}ttention} (\textsc{CoSA}) using a novel concept of \emph{Grounded Slot Dictionary} (GSD) inspired by vector quantization. Our proposed GSD comprises (i) canonical object-level property vectors and (ii) parametric Gaussian distributions, which define a prior over the slots. We demonstrate the benefits of %grounded slot representations 
our method
in multiple downstream tasks such as scene generation, composition, and task adaptation, whilst remaining competitive with SA in popular object discovery benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Conditional Slot Attention (CoSA) that uses a Grounded Slot Dictionary (GSD) to sample initial slots from a shared library of canonical object-level property vectors. Spectral decomposition is used to estimate the number of initial slots $K$ and vector quantization is used to select initial slot distributions from the GSD. The authors run experiments on object discovery, scene composition and generation, and downstream task adaptation showing benefits over previous methods.

### Strengths
This paper is well-motivated and the approach is novel, as far as I know. The authors show improvements over previous methods in terms of FG-ARI and downstream task performance and include additional experiments and analyses in the Appendix.

### Weaknesses
- The paper is missing some ablations that I think would be important in evaluating the significance of the method:
    - How much of the improved performance is from just predicting the number of slots instead of using a fixed $K$? What if we use the predicted number of slots without the GSD?
    - Conversely, how much is attributed to the GSD? What if we used a fixed $K$ with GSD?
- What is the distribution of the number of objects for the different datasets? This would be important to interpreting the MAE values.
- While I can appreciate the probabilistic interpretation of the model, I feel it does not add to the clarity of the paper and may be more appropriate for the appendix. Specifically, if I understand correctly, if $q(\tilde{z}|x)$ is deterministic and $p(\tilde{z})$ is uniform as in VQ-VAE, then the KL term is just a constant and not actually used to optimize the model?
- The discussion of the different sampling strategies (Euclidean, Cosine, Gumbel) does not seem necessary for the main text since (from my understanding) the experiments in the main text are only done with the Cosine version? I do see additional experiments on other sampling strategies in the appendix, but if that is the case, this discussion can be removed from the main text.

### Questions
- The codebook size seems like a potentially important parameter. What size do you choose for the different experiments? How sensitive are the results to codebook size?
- I want to confirm that the Abstraction Module is not differentiable and just uses the output of the encoder, which is trained through the Slot Attention path. Then, there are similarly no gradients flowing through the GSD and it is only updated with EMA (Appendix F). Is this understanding correct? If so, I think this could be stated more explicitly for clarity in the main text.
- How are the dynamic number of slots $K$ actually implemented during training? From my understanding, different images in a batch may have different $K$, so this may need to be done with some masking of the softmax in Slot Attention, in which case a max number of slots still needs to be used. In that case, is the benefit in FLOPS only during inference for a single image?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on grounded object-centric learning which can bind to specific object types. To achieve this goal, the authors take inspiration from Slot Attention, and introduce a Grounded Slot Dictionary to encode object properties and bind to different object types. This dictionary enables the model to conditionally sample the slots from different distributions. And the reasoning module with property transformation module enhances the interpretability of object property binding. The experiments show improvements on various object discovery benchmarks.

### Strengths
1. The motivation is clear and makes sense. It takes inspiration from the recent research in binding problem and concludes three major challenges in unsupervised object discovery. And it takes the binding to canonical object properties and types as the primary problem to help simultaneously solve all three challenges.
2. The design of conditional slot attention is novel. It employs the spectral decomposition for discrete mapping and enables the model to sample from different distributions corresponding to different object properties.
3. The visualization of the separated object properties are interesting and shows interpretable Ground Slot Dictionary.

### Weaknesses
1. The experiments on more complex scenes are required. For example, multiple instances of the same object category, it would be interesting to show the property binding ability in this case. Specifically, the ability to discriminate between different instances of the same semantic category in realistic scenes is not sufficiently demonstrated. The current experiments primarily focus on relatively simple scenes, which do not fully capture the challenges of real-world scenarios with multiple objects of the same type.
2. Does the model build on pre-trained backbones? Or a randomly initialized encoder $\Phi$ is also sufficient to provide cues for spectral decomposition and discritization? It's unclear how much the spectral decomposition and discretization rely on the initialization of the encoder, and whether the model can learn meaningful object representations from scratch.
3. I suggest authors to run the trained conditional slot attention with grounded slot dictionary on some video data, e.g., DAVIS-2017, to validate whether the slot dictionary can track objects across time and more vividly show the binding ability to object types. The current evaluation lacks a demonstration of temporal consistency in object binding, which is crucial for real-world applications. It is important to evaluate the model's ability to maintain consistent binding of slots to specific objects across consecutive frames, especially when dealing with multiple instances of the same object category.

### Questions
The conventional slot attention based methods use reconstruction loss as the self-supervised objective to guide object decomposition. What is the relationship between the objectives used in this work and the recounstruction loss?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces Conditional Slot Attention (CoSA), a novel variant of Slot Attention that incorporates the concept of grounded representations. Unlike the original Slot Attention, CoSA utilizes a dynamic binding scheme using canonical object-level property vectors and parametric Gaussian distributions. This approach enables specialized slots that remain invariant to identity-preserving changes in object appearance. The proposed method is evaluated on multiple downstream tasks, including scene generation, composition, and task adaptation, and achieves competitive performance compared to Slot Attention in object discovery benchmarks.

### Strengths
1. Unsupervised object discovery remains a challenge and an open question in the research community.
2. The concept of the Grounded Slot Dictionary (GSD) module is logical, particularly the construction of a dictionary as outlined in Definition 1.
3. The visualization of GSD binding in Figure 3 is both interesting and insightful for the community, providing evidence of the effectiveness of the GSD approach.

### Weaknesses
1. I would appreciate more ablation studies in the experiments section. The current version primarily presents the state-of-the-art (SOTA) performance for two case studies, but additional ablation studies would provide further insights into the specific contributions and the impact of different components or techniques employed in the proposed method. For instance, it would be beneficial to see how performance varies with different sizes of the Grounded Slot Dictionary (GSD) or with different choices of the spectral decomposition method used to construct the dictionary. Furthermore, ablating the effect of the object-level property vector, by say, removing it or using a simpler representation, would help to isolate its contribution.
2. The author mentions that the method incorporates the object-level property vector, but there is a lack of evidence regarding how it functions. For instance, it is unclear whether the method can effectively discriminate between multiple instances with similar appearances. The paper does not provide sufficient analysis on the sensitivity of the method to variations in object appearance, such as changes in lighting, viewpoint, or partial occlusions. It would be valuable to see experiments that specifically test the method's ability to handle these variations and how the object-level property vector contributes to this robustness.
3. The visualization of the COCO results does not appear to be accurate, and it seems that the method may not be as applicable to real-world scenarios. The segmentation masks in the COCO results seem to lack precision and often do not align well with the object boundaries. This raises concerns about the practical applicability of the method to complex real-world scenes, where accurate object segmentation is crucial.

### Questions
1. Besides performance gains, what evidence does the paper provide to show that the object-level property vectors are working effectively?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
