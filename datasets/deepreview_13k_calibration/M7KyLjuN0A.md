# DynamicCity: Large-Scale LiDAR Generation from Dynamic Scenes

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
\vspace{-0.25cm}
LiDAR scene generation has been developing rapidly recently. However, existing methods primarily focus on generating static and single-frame scenes, overlooking the inherently dynamic nature of real-world driving environments. In this work, we introduce \textsf{\textcolor{citypink}{Dynamic}\textcolor{cityblue}{City}}, a novel 4D LiDAR generation framework capable of generating large-scale, high-quality LiDAR scenes that capture the temporal evolution of dynamic environments. \OM{} mainly consists of two key models. \textbf{1)} A VAE model for learning HexPlane as the compact 4D representation. Instead of using naive averaging operations, \OM{} employs a novel \textbf{Projection Module} to effectively compress 4D LiDAR features into six 2D feature maps for HexPlane construction, which significantly enhances HexPlane fitting quality (up to $\mathbf{12.56}$ mIoU gain). Furthermore, we utilize an \textbf{Expansion \& Squeeze Strategy} to reconstruct 3D feature volumes in parallel, which improves both network training efficiency and reconstruction accuracy than naively querying each 3D point (up to $\mathbf{7.05}$ mIoU gain, $\mathbf{2.06x}$ training speedup, and $\mathbf{70.84\%}$ memory reduction). \textbf{2)} A DiT-based diffusion model for HexPlane generation. To make HexPlane feasible for DiT generation, a \textbf{Padded Rollout Operation} is proposed to reorganize all six feature planes of the HexPlane as a squared 2D feature map. In particular, various conditions could be introduced in the diffusion or sampling process, supporting \textbf{versatile 4D generation applications}, such as trajectory- and command-driven generation, inpainting, and layout-conditioned generation. Extensive experiments on the CarlaSC and Waymo datasets demonstrate that \OM{} significantly outperforms existing state-of-the-art 4D LiDAR generation methods across multiple metrics. The code will be released to facilitate future research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes DynamicCity, a novel 4D LiDAR scene generation framework that supports large-scale dynamic reconstruction and generation. It introduces HexPlane as the compact 4D representation with effective decomposition to enhance the reconstruction quality. In order to improve the query efficiency, the authors further employ an expansion & squeeze strategy (ESS) to decode features in parallel. During the generation stage, this paper proposes a padded rollout operation to reorganize the six feature planes into a square feature map for better spatial and temporal awareness. Based on the VAE and DiT pipeline, DynamicCity achieves leading performance on both 4D reconstruction and generation, which also enables long sequential modeling and diverse conditional generation.

### Strengths
- Compared to existing methods that lack the ability of long-term dynamic generation, this paper utilizes Hexplane as the compact 4D representation and reorganizes into one feature map to achieve efficient reconstruction and generation. 

- The decoding manner in parallel proposed in Expansion & Squeeze Strategy (ESS) alleviates the problem of dense queries and further improves the generation efficiency.

- Based on the VAE and DiT pipeline, the authors introduce diverse conditions for generation (e.g., command, trajectory and layout), demonstrating the potential of the model and its broad applications.

- The overall paper is easy to follow with excellent illustration and clear statements of contributions, making it very comfortable to read.

### Weaknesses
 - Despite the compact HexPlane and parallel decoder, the dense feature volume and projection module of autoencoder are still very heavy, which limits its efficiency and scalability. The use of dense 3D convolutions, even if preceded by a light 3D convolution, introduces significant computational overhead, especially when dealing with high-resolution 4D data. The projection module, while having a relatively small parameter count, still contributes to the overall computational cost, particularly during the training phase.

- The sample of the dataset is quite limited, which may lead to overfitting and memorization of the data by the generation model. This paper also lacks clarification of the division of training and test sets, as well as experiments and comparative results for their generalization ability and generative diversity. The limited dataset size raises concerns about the model's ability to generalize to unseen scenarios and its potential to simply memorize the training data rather than learning underlying patterns. Without a clear split and rigorous testing, it's difficult to assess the true capabilities of the model.

- Although the authors provide diverse control conditions for generation, there is a lack of some more simple and practical conditions such as images, text or single-frame point clouds that are easily accessible. The absence of these readily available conditions limits the practical applicability of the model and makes it harder to integrate into existing workflows. The current conditions, while diverse, may not be as intuitive or straightforward for users to leverage.

### Questions
According to the weaknesses above, there are some concerns to be addressed:

1. It's noted that there are some recent works like XCube using advanced 3D sparse structure to improve the efficiency. Thus, it needs more explanation and comparison for the 3D backbone.  

2. Does the model have the generalization ability and generative diversity? Overfitting to a few samples may reduce its significance. It would be better to provide more (conditional) generation results on the test set and multiple sampling results.

3. It would be much more beneficial to incorporate more practical conditions such as images, text or single-frame point clouds, which is also helpful for the assessment of generalization ability.

4. Given that the title is LARGE-SCALE LIDAR GENERATION, it may be plausible to include the generation or simulation of LiDAR point clouds (beyond occupancy) in the application. Or to avoid ambiguity.

5. How to better demonstrate temporal consistency compared to baselines, which is difficult to reflect in current metrics?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a diffusion-based 4D LiDAR scene generation method. This task
is sometimes referred to as "LiDAR world modeling". The approach performs
diffusion in a HexPlane latent space, and the diffusion can be conditioned on
past data in order to perform autoregressive synthesis, or on semantics in order
to perform layout-guided generation. This makes the approach amenable to
closed-loop simulation.

The encoding stage follows a VAE framework, leveraging a LiDAR backbone followed
by a novel projection module which produces spatio-temporal HexPlanes as the
output.

The decoding stage starts with HexPlanes, decodes them into spatio-temporal
feature volumes, and then finally into 4D semantic occupancy. The tokenization
and diffusion-based generative modeling is performed in this HexPlane latent
space.

At generation time, the diffusion transformer (DiT) component generates new
scenes by performing diffusion in the HexPlane space, optionally conditioning
the generation on a semantic map, or on past generation results to achieve
autoregressive synthesis. These samples then get decoded into 4D semantic
occupancy using the method described above.

The authors compare the approach to OccSora, another recent 4D generative
modeling technique, and show improved results on synthetic (CARLA-based) and
real (Waymo- and nuScenes-based) datasets.

### Strengths
- [S0] Flexible modeling approach which seems to scale well to large scenes while
  still allowing a wide range of rich conditioning methods.
- [S1] The proposed approach outperforms OccSora, a very modern competitor, in a
  wide range of metrics, including FID, precision, and recall.
- [S2] Some interesting implementation tricks could potentially be applied to
  other related tasks. For example, diffusion runs on a 2D setting with a clever
  tiling of the six HexPlanes into a single plane (Fig 4 - the "Padded Rollout").
- [S3] Overall, the paper is very well-written and provides thorough experiments,
  architectural details, and discussions. The appendix is likewise
  well-structured and I found it very easy to navigate.

### Weaknesses
 - [W0] The pretrained networks used to calculate IS, FID, and KID should be motivated more thoroughly, especially in the 2D case.
  - For example, it is not clear why it is meaningful to use a CNN presumably
    trained on ImageNet or COCO to reason about samples consisting of semantic
    color maps. Unless this 2D CNN is trained to process semantic color maps as
    inputs, passing semantic color maps to such a CNN would produce OOD feature
    maps. Furthermore, the spatial resolution of the input images to these networks is not discussed, and this could have a significant impact on the resulting metric values. For example, if the input images are resized to a very small size, the resulting feature maps may not capture the fine-grained details of the semantic maps.
- [W1] One conceptual limitation is the fact that the method does not explicitly
  model uncertainty when forecasting a future scene conditioned on the present.
  Is this something that can be modeled by sampling multiple futures from the
  latent space? It is unclear how the method handles the inherent stochasticity of future events, and how this is reflected in the generated outputs. The paper should discuss the implications of this limitation for real-world applications, where uncertainty is a critical factor.
- [W2] The core applications of 4D world modeling are tasks like simulation and
  motion forecasting. Presenting some results in this area could strengthen the
  paper. For example, this could include demonstrating that the world model
  performs well on a motion forecasting benchmark, or that it can be used to
  supplement training data for an end-to-end autonomous driving model. Without such results, it is difficult to assess the practical utility of the proposed approach.
- [W3] No source code seems to be promised.
- [W4] In the current stage, the approach is LiDAR-only. This is a minor
  limitation, though, and I am primarily mentioning it for completeness.
- Minor suggestions:
  - L245: "first generate" -> "first generates"
  - L866: Missing parentheses around the PyTorch citation.

### Questions
- [Q0] How do you calculate metrics like FID in 2D? What specific features do
  you use for the computation? BEV? What is the network used in these metrics
  originally trained on? I could not find this info in the references provided
  at the end of Section 5.1. If the pre-trained InceptionV3 and VGG-16 networks
  from A.2. are pre-trained on natural images, are they a good fit for comparing
  (what I assume to be) BEV semantic images?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents DynamicCity, a novel 4D scene generation method for driving environments. DynamicCity utilizes a VAE model to compress 4D scenes into a HexPlane, integrating strategies such as a Projection Module and an Expansion & Squeeze Strategy to enhance performance and efficiency. A DiT-based diffusion model is then employed for generating the HexPlane. The method supports various 4D scene generation applications, including trajectory, command, and layout conditions. Basically this is a strong submission with impressive results, while I have several further concerns.

### Strengths
1. The paper is well-structured and easy to follow.
2. The generated results are impressive, with an accompanying demonstration video that effectively showcases the method’s capabilities.
3. The proposed method has a clear motivation and presents a well-reasoned pipeline.

### Weaknesses
1. I’m a little confused by the title and the task definition. While the authors state that the proposed method is designed for “LiDAR” generation, the results seem more akin to “occupancy” generation. These concepts are distinct, despite both representing the scene’s geometry. For true LiDAR generation [1][2], the outputs should be LiDAR point clouds that reflect the sampling properties of LiDAR sensors (e.g., ray drop, ray-based sampling, etc).
2. The authors note that the method can support long sequential modeling of up to 128 frames, but the factors limiting sequence length (e.g., GPU memory) are not discussed. Additionally, the inference running time is not mentioned.
3. Can the proposed method support outpainting similar to SemCity? While inpainting results are shown to demonstrate the spatial significance of the HexPlane, outpainting results could further demonstrate the method’s ability to expand scenes. Furthermore, the inpainting examples in the paper are confined to small regions.
4. Regarding the experimental results, I suggest to provide quantitative comparison with SemCity in static scenes. The caption of Table 2 points out the authors compare the method with SemCIty, but I do not see results in the table.

### Questions
Please refer to the Weaknesses.

### Soundness
3

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
2

### Summary
This paper proposes DynamicCity for large-scale driving environments for 4D generation. The paper proposes a Projection Module to efficiently 4D features into six 2D feature maps and an Expansion & Squeeze Strategy to reconstruct 3D feature volumes in parallel. A Padded Rollout Operation is also proposed to reorganize all six feature planes of the HexPlane as a squared 2D feature map.

### Strengths
1. The writing is easy to follow.

2. The ablation is comprehensive and validates the efficiency of Padded Rollout, Projection Module, and ESS in Table 3 and Table 5.

3. The results are good compared to the baseline method over different datasets.

4. The trajectory-guided generation, dynamic scene inpainting, and layout-conditioned generation show various downstream applications.

### Weaknesses
1. The Dynamic Object Inpainting Results seem to make the ground have holes(Figure 1). Could you please explain this phenomenon and discuss any potential limitations or artifacts of this inpainting approach?

2. The results seem to reflect semantic occupancy, with training data voxelized into occupancy format using LiDAR point clouds. Could you clarify why "LiDAR generation" is used in the title, abstract, and introduction? It would be helpful to explain the distinction between "LiDAR generation" and "semantic occupancy generation" as used throughout the paper, as well as the relationship between LiDAR data and the voxelized occupancy representation. This clarification would help ensure that the terminology accurately represents the method and results.

3. It’s recommended to add a comparison of model size across different methods, as the proposed approach appears to require substantial training resources.

4. While a training time comparison is provided in the ablation study, it’s still suggested to include a comparison of training time and GPU requirements specifically against the baseline method, like Occ-sora. These comparisons could help readers better understand how much computational power the proposed method needs compared to other established methods.

### Questions
Same as Weakness.

### Soundness
3

### Presentation
3

### Contribution
3
