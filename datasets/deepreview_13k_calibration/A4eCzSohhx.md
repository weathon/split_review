# Grounding Continuous Representations in Geometry: Equivariant Neural Fields

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
\textit{Conditional Neural Fields} (CNFs) are increasingly being leveraged as continuous signal representations, by associating each data-sample with a latent variable that conditions a shared backbone Neural Field (NeF) to reconstruct the sample. However, existing CNF architectures face limitations when using this latent \textit{downstream} in tasks requiring fine-grained geometric reasoning, such as classification and segmentation. We posit that this results from lack of explicit modelling of geometric information (e.g. locality in the signal or the orientation of a feature) in the latent space of CNFs. As such, we propose Equivariant Neural Fields (ENFs), a novel CNF architecture which uses a geometry-informed cross-attention to condition the NeF on a geometric variable—a latent point cloud of features—that enables an \textit{equivariant} decoding from latent to field. We show that this approach induces a \textit{steerability} property by which both field and latent are grounded in geometry and amenable to transformation laws: if the field transforms, the latent representation transforms accordingly—and vice versa. Crucially, this equivariance relation ensures that the latent is capable of (1) \textit{representing geometric patterns faitfhully}, allowing for geometric reasoning in latent space, (2) \textit{weight-sharing over similar local patterns}, allowing for efficient learning of datasets of fields. We validate these main properties in a range of tasks including classification, segmentation, forecasting and reconstruction, showing clear improvement over baselines with a geometry-free latent space.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes equivariant conditional neural fields based on steerable networks. Architecture-wise, this paper proposes equivariant  cross-attention layers with Gaussian windowing as the basis of their Equivariant Neural Fields (ENF). The ENF is trained with a two-stage process: in the first stage, the ENF backbone takes in an input signal and outputs a latent point cloud of (pose, context) pairs. Downstream tasks can be accomplished by training a decoder which takes the latent point cloud as input. Experiments are performed on 2D image reconstruction and classification, 3D reconstruction, classification, and part-segmentation, flood map segmentation, and climate forecasting.

### Strengths
This paper creates a novel equivariant neural field based on the notion of steerability from equivariant networks, which has the advantages of weight-sharing, locality, and geometric interpretability.

### Weaknesses
1. The original Functa paper uses a SIREN neural field architecture but this paper uses an attention-based neural network architecture. This seems like a potentially unfair comparison. The architectural differences, specifically the use of a cross-attention mechanism versus a SIREN-based MLP, make it difficult to isolate the impact of the proposed equivariance. The comparison would be more compelling if the baseline also used an attention-based architecture, allowing for a more direct evaluation of the equivariant components.
2. Another weakness of this paper is that there is no way to decide ahead of time whether to train the latent point cloud using MAML or autodecoding. The choice between MAML and autodecoding for training the latent point cloud is not clearly motivated, and the lack of a principled method for selecting between these two approaches introduces a degree of arbitrariness. A more detailed discussion of the trade-offs between these two methods, including computational cost, convergence behavior, and generalization performance, is needed.
3. The only baseline is Functa for most experiments. Is it possible to use NF2vec in Table 2 and Inr2Array [1] for any of the experiments involving downstream tasks? For tasks involving generalization, 
4. ENF performs only comparably to to the baselines on part-segmentation (Table 3), and some experiments (Table 2) don't show the effectiveness of using equivariance. The comparable performance on part-segmentation raises concerns about the practical benefits of the proposed method. Moreover, the lack of a clear performance gain in some experiments (Table 2) suggests that the equivariance may not be consistently beneficial across all tasks. A more thorough analysis of the conditions under which equivariance provides a significant advantage is needed.

### Questions
1. Does it make sense to compare against Inr2Array [1]?
2. Should NF2vec also be a baseline for the shape classification task (Table 2)?
3. Can Functa be trained with a cross-attention-based architecture, similar to that proposed for ENF?
4. For Functa baselines on downstream tasks such as classification, what was the architecture of the decoders used?

[1]: Zhou, Allan, et al. "Neural functional transformers." Advances in neural information processing systems 36 (2024).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces the Equivariant Neural Fields, a variant of conditional neural field that uses a geometry-informed cross-attention to condition the NeF using geometrical point cloud representation. The method was validated using a variety of applications, including classification, segmentation, forecasting, and reconstruction.

### Strengths
***Clear and Professional Presentation***: The paper is well-written, structured effectively, and easy to follow. Its clear motivation, logical organization, and high-quality visualizations contribute to a polished and professional presentation, making the methodology accessible and engaging.

***Introduction of Equivariant Neural Fields Model***: The authors propose a novel model, Equivariant Neural Fields, which combines conditional neural fields with point cloud conditioning and equivariant decoding from latent space to field. This approach creatively integrates Neural Fields with equivariant models designed for point clouds, expanding on existing techniques. Additionally, the paper introduces specialized attention layers and engineering optimizations that enhance the model's efficiency, showcasing an innovative blend of established methods.

***Comprehensive Experimental Validation***: The method is rigorously tested across a wide range of use cases and downstream tasks spanning various domains. This extensive evaluation demonstrates the versatility and potential real-world applicability of the proposed approach, supporting its robustness and utility across diverse applications.

### Weaknesses
 ***High Time Complexity***: The proposed approach appears to be computationally intensive. It would be beneficial for the authors to compare the training time and memory usage of their method against a reference model, such as the Functa method, to provide a clearer assessment of its efficiency. Specifically, a detailed breakdown of the computational cost associated with the attention mechanism, including the scaling behavior with respect to the number of input points and latent variables, would be valuable. Furthermore, it would be helpful to understand the practical implications of this complexity, such as the feasibility of training on large datasets or the real-time performance of the model.

***Lack of Ablation Studies***: The paper would benefit from ablation studies to clarify the contributions of key components, such as Gaussian spatial windowing and the k-nearest neighbors (kNN) efficiency trick. These studies should not only demonstrate the impact on overall performance but also on training efficiency. For example, it would be important to quantify how much each component contributes to the speedup or slowdown of training, and how these changes affect the model's ability to generalize to unseen data. A more granular analysis of the effects of varying the kNN parameter 'k' would also be beneficial.

***Suboptimal Segmentation Performance****: The segmentation results are weaker than those of traditional point cloud segmentation baselines. A deeper investigation and discussion of these performance differences would help in understanding and potentially addressing the gaps in segmentation accuracy. It would be useful to analyze why the proposed method struggles with segmentation tasks compared to methods specifically designed for point cloud segmentation. This analysis should consider factors such as the model's ability to capture local geometric details, the effectiveness of the equivariant representation for segmentation, and the choice of loss function.

### Questions
Please refer to the weakness section

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel class of Conditional Neural Fields (CNFs) called Equivariant Neural Fields (ENFs) which aim to address the limitations of CNFs in tasks requiring geometric reasoning. The authors propose a geometry-informed cross-attention mechanism that conditions on a latent point cloud of features, enabling equivariant decoding from the latents to the field of interest. This approach possess a steerability property where transformations in the field and mirrored in the latent space. Further, this approach ensures that the cross-attention attention operators respond similarly regardless of pose allowing for weight sharing over similar local patterns leading to more efficient learning. These claims are backed with experiments that demonstrate the advantages posed by the formulation and show a clear advantage over the baselines that have a geometry-free latent space.

### Strengths
- The paper introduces a novel and mathematically sound method to incorporating geometric structure to neural fields through the equivariant cross attention. The steerability property is well formulated with proven bi-invariant constraints.
- The experimental details demonstrate an advantage over methods that do not incorporate such geometry informed structure in the latent space. Additionally, the locality and weight-sharing properties discussed are clearly demonstrated.
- The paper is well-written providing clear background on the neural fields, and the motivation for the need for enforcing equivariance in neural fields. The diagrams are informative and highlight the key components of the methodology. Highlighing geometry attributes in Section 3 with a blue text color was particularly helpful in aiding understanding

### Weaknesses
 - While the motivation to compare against other CNF based approaches is clear, the methodology seems to be restricted to a discussion and comparison to the results reported in functa (Dupont et al.) and other CNF-based methods but do not provide a thorough comparison against other equivariant methods or other state of the art methods. Perhaps a comparison of ENFs against more comparisons would strengthen the paper.


### Questions
- I'm particularly curious about the use of these equivariant neural fields as a general backbone for any neural field based task? Are there any situations where it's not helpful to enforce equivariance especially for vision / PDE-based applications?
- Have you considered using this methodology in a generative context? I think the localized latent point clouds are a particularly interesting property that could lead to more structured creation.
- Did you study the sample efficiency of ENFs against other CNF methodologies in tasks such as classification? One would assume that enforcing equivariance should lead to a better sample efficiency throughout all truncations of the training dataset
- I'm curious about the computational cost of your experiments. Does it have a similar run time to the other baselines that were discussed?

Additionally, I believe there are a couple of typos that I may have spotted:
- In the abstract: faitfhully -> faithfulll
- Also, on line 103, posses needs to be possess?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a method for conditioning a neural field using a set of $SE(n)$ equivariant local latents. The aim is to enhance downstream task performance by operating on the neural field’s learned latent representation, rather than on discrete samples from the continuous signal as in conventional approaches. It outlines the necessary conditions for an equivariant latent representation in neural fields and adapts a cross-attention architecture to support these conditions. The approach is evaluated across a wide variety of tasks.

### Strengths
The paper is well-written and organized, with a clearly defined method supported by formal definitions.

The proposed solution is simple and intuitive for enhancing CNFs with local equivariant features.

I appreciate the variety of dataset types used in the experiments.

### Weaknesses
Lack of motivation for using CNF latent encodings in downstream tasks

The paper does not explicitly discuss the motivation for using latent encodings of CNFs for downstream tasks. It seems that one advantage might be the ability to utilize more data for training since the reconstruction training stage does not require labeled data. This raises a follow-up question:
What benefit do latent features learned through continuous reconstruction (decoder) have over latent features learned through reconstructing a discrete sample?  It seems that a continuous decoder could enable the learning of discretization-agnostic features.  Is there another motivation for using latent encodings of CNFs for downstream tasks?  The purpose behind their use in enhancing downstream tasks remains somewhat unclear.

The motivation for using local CNF latent encodings could be framed more clearly.

The paper states that a notable limitation for conventional CNF (ln 51): “each field is encoded by a global variable”. However, this statement about cnfs limitations seems to be partially accurate. In fact, this approach for latent space modeling also has some clear advantages. For example, interpolating between two latents to generate novel signals is far more natural with a global latent structure, whereas a local latent structure requires solving the complex problem of finding correspondences between latent points. Thus, the characterization of a tradeoff rather than a limitation may be more appropriate.
Additionally, to address the limitations of a global latent, why not employ an encoder-decoder architecture with gradually decreasing spatial dependency in the latent representation (similar to a UNet)? This approach would provide a final latent that incorporates both local and global information. The rationale for restricting the model to an auto-decoder-style architecture remains unclear.

Overclaiming on Geometry-Appearance Separation in Neural Fields

The paper claims that the proposed method “separates geometry from appearance” in its representation. My understanding is that this refers to the structure of pose-appearance tuples in the latent space. However, how does the method ensure that only appearance information is captured in  $c_i$ ? This seems to rely solely on  $c_i$  being an $SE(n)$ invariant feature. Yet, some relevant geometric features are also invariant (e.g., shape volume), while some equivariant features can relate to appearance (e.g., how an object’s appearance changes are affected by material reflectance features under rotation). Consequently, enforcing a latent structure of invariant and equivariant features may not be sufficient to achieve true separation. Is there empirical evidence to support the above claim about separation?

Unclear reconstruction results

The paper claims: “Results show that ours as well as the baseline models struggle with accurately reconstructing the underlying shape from the SDF point clouds”. Given the inaccuracies in reconstruction, how can the learned features be effectively used for downstream tasks? Additionally, it’s unclear why this model underperforms in reconstruction compared to [3]. Both architectures appear similar (apart from the equivariant features), yet [3] reports more accurate reconstruction results.

Unclear segmentation results

The choice of ShapeNet as the dataset for segmentation evaluation is questionable, as it is an aligned dataset (line 468). A better alternative might be to use non-aligned datasets, such as those used for human-body segmentation in [4] and [5]. Another option would be to unalign ShapeNet by applying a random $SE(3)$ transformation to each data point. Additionally, it’s unclear if the point cloud-specific architectures were also trained with a reconstruction pretext stage.

Additional comments.

Figure 8 is uninformative on its own without comparison to other methods, showcasing some of the proposed method qualitative benefits/limitations.

Conditioning with k-nearest neighbors appears to restrict the smoothness of the modeled field to be at most continuous, while the data signals are at least differentiable.

The Steerability property for CNFs has also been defined and utilized in prior works, such as [1] and [2].

### Questions
I would appreciate a response regarding the weaknesses and questions mentioned above.

### Soundness
2

### Presentation
3

### Contribution
2
