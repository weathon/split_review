# CityGPT: Generative Transformer for City Layout of Arbitrary Building Shape

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 6

## Abstract
City layout generation has gained substantial attention in the research community with applications in urban planning and gaming. 
We introduce CityGPT, the generative pre-trained transformers for modeling city layout distributions from large-scale layout datasets without requiring priors like satellite images, road networks, or layout graphs. Inspired by masked autoencoders (MAE), our key idea is to decompose this model into two conditional ones: first a distribution of buildings' center positions conditioned on unmasked layouts, and then a distribution of masked layouts conditioned on their sampled center positions and unmasked layouts. These two conditional models are learned sequentially as two transformer-based masked autoencoders. Moreover, by adding an autoregressive polygon model after the second autoencoder, CityGPT can generate city layouts with arbitrary building footprint shapes instead of boxes or predefined shape sets.
CityGPT exhibits strong performance gains over baseline methods and supports a diverse range of generation tasks, including 2.5D city generation, city completion, infinite city generation, and conditional layout generation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a transformer-based generative model of city layouts. The model has two phases, based on masked autoencoders: the first phase learns to predict a probability distribution over likely locations for building centroids; the second phase takes the position information and autoregressively predicts the vertices of the buildings. At test time, the two phases are alternated to allow autoregressive sampling of a city layout. Experiment shows that the proposed method generates reasonable layouts, and outperforms prior works (either for this task or for more general layout generation) over multiple metrics, including a human perceptual study.

### Strengths
- An interesting problem that can probably provide some insight to the more general layout generation problem as well.
- Can enable a range of applications, as illustrated in the paper.
- Reasonable results that clearly work better than some of the baselines
- The two-stage pipeline where a location distribution is used to directly condition polygon generation is rather new.

### Weaknesses
 - Not too much novelty: the idea of predicting a probability distribution over building, the idea of autoregressive generation of polygons and the idea of transformer based layout generation can all be traced to prior works. While the domain (city generation) and the combination of techniques are novel (conditioning polygon generation directly on the location distribution), such novelty are likely not directly useful for people who are not interested in this particular problem. Subsequently, results quality would matter much more and
- The evaluation is underwhelming. Most baselines are for general layout problems that has much weaker constraints than the specific problem. The one baseline that addresses this problem (AETree) is a weak one the doesn't even compete with more general methods. Even with this set of baselines, I am not sure whether the proposed method really generates better layout, based on the qualitative results. The quantitative metrics are too generic (FID is too general for evaluating such layout visualizations, WD over edge/area/ratio doesn't really evaluate layout quality), the user/perceptual study is also not well conducted (ground truth shouldn't have minor noises, visualizations of layout should be better so humans can actually judge if the layouts are good i.e. not just with blue boxes/meshlab screenshots).
- Lack of evaluation over whether the method can generate novel and diverse layouts that are different from the training set. I am not convinced that the model is not overfitting to some training samples. 
- The problem setting isn't particularly useful: without streets, roads, building types and other city elements, I can't see how this can be helpful in any real city planning / modeling tasks. I am also not sure whether representing buildings as 2D polygon contours adds much over just specifying the location and size of buildings: one would need to model the 3D building in some other ways anyways.
- A few technical issues that need to be addressed: see questions below.

### Questions
As mentioned in the weakness section, I have concerns over the evaluation protocol, providing more evidence that the model can generate realistic layout (i.e. with more proper metrics and user studies) and is not just overfitting will change my opinion on this paper siginificantly.

Additional questions:
- It is mentioned that the position set P models the buildings by their mean centers, however, judged by later sections, it seems that phase 1 is instead generating an occupancy map over locations, instead of a map over the building centers. Could the authors clarify what exactly happens in phase 1? If the model indeed predicts occupancy, then more analysis is needed on how it is converted into positions (as mentioned in Appendix D)
- The distribution predicted by phase 1 also seems extremely blurry and doesn't really resemble a probability distribution. It almost seems to me that the method is just attempting to memorize the silhouettes of buildings. A bit more analysis would be great here.
- In section 4, it mentioned that weights need to be applied to BCE to address class imbalance, this shouldn't happen if the model can actually learn the distribution. It seems that after applying such weights, there isn't really too much difference between high/low likelihood, which is not ideal.
- Finally, I am not sure if it make sense to learn the entire distribution over many buildings: shouldn't the distribution just be completely uniform since all buildings can take all locations without additional constraints? Shouldn't the probability be zero over locations with existing buildings? Some clarifications are again needed.

### Soundness
2 fair

### Presentation
2 fair

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
This paper focuses on the city layout generation task. A generative pre-trained transformer, i.e., CityGPT, is proposed for modeling city layout distributions from large-scale layout datasets. The distribution of buildings’ center positions is first learned. The distribution of masked layouts is then learned based on the sampled center positions and unmasked layouts. The city layouts are represented as arbitrary shapes instead of boxes. The experimental results demonstrate the effectiveness of the proposed method on several generation tasks.

### Strengths
This paper is the first to represent layouts of arbitrary scales and shapes without any prior conditions. The proposed two-stage decomposition modeling approach for city layout can accomplish various layout generation tasks. The experimental results demonstrate superior performance compared to existing works.

### Weaknesses
1. The runtime performance analysis should be conducted, including both the 2D and 2.5D generation. It is important to understand the computational cost associated with the proposed method, especially when dealing with complex city layouts and the added dimension in 2.5D generation. A detailed breakdown of the time taken for each stage of the generation process, such as center position sampling and masked layout generation, would be beneficial. This should also include a comparison with existing methods to contextualize the efficiency of the proposed approach.
2. Several layout generation works [1-4] should be cited and discussed in the paper. The current literature review seems incomplete, and the paper would benefit from a more thorough discussion of related works, particularly those focusing on generative layout modeling. Specifically, the paper should discuss how the proposed method compares to and differs from these works in terms of methodology, performance, and limitations.
3. Some details in the further experiments are missing. For the classification task, the architecture of the classification model used here is unclear. The paper should specify the type of model (e.g., CNN, Transformer), the number of layers, and the activation functions. For the 2.5D generation, the training details after adding the additional height dimension are unclear. The paper should explain how the height information is incorporated into the model and if the training process is different from the 2D case. For the generated based on the road network, why choose the latter approach, rather than concatenating the condition embedding with the mask tokens? The rationale behind this design choice should be clearly explained, including the potential benefits and drawbacks compared to the concatenation approach.
4. There are some typos in the paper. For example, “in f city layout generation” in the last paragraph of the introduction section. “our results demonstrate” in the first paragraph of the conclusion section.

### Questions
1. For the user study, why the results of the proposed model are more realistic than the ground-truth layouts?
2. Will the dataset be released to facilitate future research in the community?

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
The paper introduces CityGPT, a novel approach for generating city layouts without relying on prior information like satellite images or layout graphs. This model leverages transformer-based masked autoencoders to sequentially learn two conditional models: one for building center positions given unmasked layouts, and the other for masked layouts given sampled center positions and unmasked layouts. Additionally, CityGPT incorporates an autoregressive polygon model, enabling it to generate city layouts with diverse building footprint shapes. The results demonstrate significant performance improvements over baseline methods, and CityGPT proves versatile in various generation tasks, including 2.5D city generation, city completion, infinite city generation, and conditional layout generation.

### Strengths
1. The paper is well organized.
2. The experiments somehow proves the effectiveness of the proposed method.

### Weaknesses
1. Recent studies, such as InfiniCity and CityDreamer, have focused on creating city layouts, incorporating both roads and buildings. However, this particular work only generates buildings without roads, which may limit its practical applicability in real-world scenarios.
2. The paper is not clearly written, missing too many details in Sections 3.2 and 3.3. After reading the two sections, it is still unclear how to convert the "Predicted Position Map" to "Reconstructed Building Layout".


### Questions
1. What is "in f city layout generation" mentioned in the third contribution?
2. The first phase should undergo a comparison with InfiniteGAN, employed in InfiniCity, and MaskGIT, utilized in CityDreamer. Additionally, if feasible, it should be contrasted with Diffusion models, as all of these models are applicable to both inpainting and outpainting tasks. Furthermore, all three models have the capability to directly generate footprint masks. In comparison to these three models, what specific advantages does the proposed model bring?
3. It is unclear how to generate the height of the buildings. According to the definitions in Section 3.1, the buildings only contains the coordinates of footprints.

### Soundness
2 fair

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
Authors proposed a two-stage transformer-based generative model for modeling city layout with arbitrary polygon building shape. The pipeline first generate center position for each building, and then autoregressively generate the polygon shapes of the building. The model is trained in a MAE fashion, and at inference time iteratively generates the masked building position and shape conditioned on existing unmasked ones. Results demonstrate the effectiveness of this two-stage approach. Further experiments on generating buildings with extruded height are also shown for completeness.

### Strengths
Writing is clear and easy to understand. The two-stage approach with MAE-like training is novel and breaks down a hard problem into iterative generation of layout and geometry. The autoregressive transformer is also more capable as it can generate arbitrary polygon shapes as opposed to just the 2D bounding boxes. Results are very extensive including ablation studies of the two-stage versus one-stage. Overall I am satisfied with the quality and novelty of this work.

### Weaknesses
Section 3.4 inference stage needs more detailed explanation. It is not very clear how the full building blocks are generated unconditionally from nothing. Some important evaluation metrics are also missing. A large autoregressive transformer (e.g. 12 layers) is prone to overfitting to the training set. Since the generated output are vector sequences, it should be easy to evaluate the novelness and uniqueness scores as in SkexGen (Autoregressive generation of CAD construction sequences) or CurveGen (Engineering sketch generation for computer-aided design). That way we will know the model is not simply remembering the training set. Specifically, the inference process lacks clarity on how the iterative masking and generation are initialized. It's unclear whether the process starts with a completely empty scene or if there's a prior or initial seed used. The paper also needs to specify the exact metrics used for evaluation. While the paper mentions that it is using a MAE-like approach, it does not specify the loss function and how it is calculated. Furthermore, the paper should include metrics that directly measure the quality of the generated polygons, such as the area overlap, shape similarity, and the number of vertices, in addition to metrics that measure the layout quality. The risk of overfitting is high with a 12-layer transformer, and the paper should provide more evidence to show that the model is generalizing well and not simply memorizing the training data. The authors should provide a nearest neighbor analysis, showing the closest training example to each generated sample. This would provide a clearer indication of whether the model is generating truly novel outputs.

### Questions
I would appreciate if authors can explain a bit more details about how the inference stage is conducted. Authors should also provide some proof that the trained model is not over-fitting to the training set. Novel and Uniqueness scores are a good benchmark as I mentioned. Given a generated result, authors can also illustrate the nearest neighbour search from the training set and compare their similarity.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
