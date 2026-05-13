# IFAdapter: Instance feature control for grounded Text-to-Image Generation

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
While Text-to-Image (T2I) diffusion models excel at generating visually appealing images of individual instances, they struggle to accurately position and control the features generation of multiple instances. The Layout-to-Image (L2I) task was introduced to address the positioning challenges by incorporating bounding boxes as spatial control signals, but it still falls short in generating precise instance features.
In response, we propose the Instance Feature Generation (IFG) task, which aims to ensure both positional accuracy and feature fidelity in generated instances.
To address the IFG task, we introduce the Instance Feature Adapter (IFAdapter). The IFAdapter enhances feature depiction by incorporating additional appearance tokens and utilizing an Instance Semantic Map to align instance-level features with spatial locations. The IFAdapter guides the diffusion process as a plug-and-play module, making it adaptable to various community models.
For evaluation, we contribute an IFG benchmark and develop a verification pipeline to objectively compare models' abilities to generate instances with accurate positioning and features.
Experimental results demonstrate that IFAdapter outperforms other models in both quantitative and qualitative evaluations.
Project Page: \url{https://ifadapter.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper aims to improve the capability of Text-to-Image diffusion models in generating precise features and positioning multiple instances in images. The proposed IFAdapter enhances feature accuracy by integrating additional appearance tokens and constructing an instance semantic map, ensuring that each instance's features align accurately with its spatial location. The IFAdapter is designed as a flexible, plug-and-play module, allowing enhanced control without retraining.

### Strengths
+ The authors propose an important task, namely Instance Feature Generation. In addition, the authors also provide a benchmark and a verification pipeline
+ The proposed method seems to achieve good results. Qualitative and quantitative experiments demonstrate the effectiveness of the proposed method.

### Weaknesses
- Compared with instance diffusion and dense diffusion, this paper shows a small number of objects and does not show the situation where the object is denser.
- The details of the method are not explained clearly. The details of the dataset construction and the baseline setting are not presented clearly. Ablation experiments lack a basic baseline presentation.
- Authors should carefully check for errors in the text. For example, a sentence appears twice in succession in Introduction.

### Questions
1. Why IFAdapter enables it to be seamlessly applied to various community models. For example, appearance queries are trained , how do the authors ensure that the feature has sufficient generalization capabilities.
2. Why can appearance-related features be extracted from the bounding box through Fourier and MLP, especially when the model inference cannot obtain image input?
3. Is the model-free method based on the same backbone as the proposed method? Are all the comparison methods that require training trained on the provided dataset? The VLM used to annotate the proposed dataset is the same as the VLM used in the evaluation metric, which may be unfair to methods that are not trained on the proposed dataset.
4. VLMs are likely to produce hallucinations. How do the authors ensure that the annotations of the provided dataset are free of hallucinations?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Instance Feature Adapter (IFA) for layout-to-image generation. The key insight of IFA is to incorporate additional appearance tokens corresponded to different objects, so as to steer the T2I models to generate images that convey precise layout information and text semantics. To achieve this, IFA first leverages learnable instance tokens to aggregate the textual and bounding box information of the specific objects. To cope with the feature leakage problems, IFA further introduce Instance Semantic Map strategy to reallocate the spatial area for different semantics, so as to alleviate the feature conflicts between different objects during external feature tokens injection process. A new benchmark is proposed, the visual improvement over different baselines is significant. Further, the proposed method is a plug-and-play module, which can be adapted to various community models.

### Strengths
1. The paper is well written and easy to follow. 
2. The designed approaches efficiently incorporate the external object semantics and layout information into the generation process. The proposed Appearance Tokens aggregate the textual semantic and bbox information with learnable tokens. The proposed Instance Semantic Map accurately reallocates the spatial area of different objects, and solves the semantic fusion and feature leakage problem. 
3. The illustrated visual results are impressive, which shows clear superiority against competing baselines.
4. The proposed method is compatible with various community models.

### Weaknesses
1. The design module is supposed to interface with the text encoders, and both Appearance Tokens and Instance Semantic Map introduce the attention mechanism. Will it be computational costly during the inference process. There should be a detailed discussion. Specifically, the paper should analyze the computational overhead introduced by the additional attention layers in terms of both memory usage and inference time, and compare it to the base models. The analysis should also consider the scaling of computational cost with the number of instances.
2. The size and shape of different objects seem unstable when applying IFA to different community models (Fig. 4), is it caused by the re-weight strategy from Instance Semantic Maps? This instability raises concerns about the robustness of the method across different model architectures and datasets. It is important to investigate whether the re-weighting strategy introduces any bias towards specific object shapes or sizes, and how this bias interacts with the pre-trained biases of different community models.
3. The L2I problem is not a novel task, and the main novelty mainly lies in the implementation detail of the layout incorporation strategy, which may not bring significantly inspirations to the community. While the specific implementation details are important, the paper should also discuss the limitations of the proposed approach in terms of its ability to handle complex spatial relationships between objects, and how it compares to other layout-to-image generation methods in this regard.

### Questions
Is the proposed model able to generate images with some intricate prompts. For example, a blue dog with red legs running on a colorful river, (with dog, legs, river assigned to different boxes). I want to see some limitations of the proposed method, or in other words, I want to know how IFA copes with the semantic issues which may inherit from the base model given out-of-domain prompts and instructions. I would love to revise my rating after further discussion with the authors.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
- This work tackles instance Instance Feature Generation (IFG) task, i.e. train a model that can generate images given a global caption, spatial locations and detailed local captions as conditioning.
- Authors introduce IFAdapter, a plug-and-play module for improving IFG.
- The IFAdapter first extracts a fixed number of appearance tokens from a detailed instance caption and its spatial location. Next, a 2D map called Instance Semantic Map (ISM) is constructed using the bounding boxes of instances to aid the adherence of the model to spatial location conditions.
- IFAdapter is architecture agnostic and can be incorporated into existing open-source text to image models and authors show its effectiveness on the newly introduced IFG Benchmark constructed from the COCO dataset.

### Strengths
- The perceiver like Resampler design to extract fixed set of appearance tokens is novel and effective. This addresses the problem of only utilizing the EoT token from the text encoders. 
- The gated semantic fusion to address multiple overlapping instances is very useful for layout to image generation methods. 
- The proposed method is simple and is architecture agnostic.

### Weaknesses
 - Authors claim IFG as their first contribution. But this task has already been introduced in InstanceDiffusion [Wang et. al 2024c]. InstanceDiffusion uses detailed instance captions in addition to the global caption. What is the difference between their setup and IFG?
- The experimental section needs heavy work to make this work ready for publication. With exponential progress in generative modeling, it is hard to control the experimental settings with other models, especially the training data. But that doesn't mean all other settings can be held constant to properly understand the contributions. InstanceDiffusion and GLIGEN use SD1.5 as their base generation model but authors use SDXL an already powerful base generator. This makes it hard to understand the improvements in Table 1 and 2. I recommend authors report numbers with SD1.5 as the base generator or retrain InstanceDiffusion with SDXL (since their code is available) to properly support their claims.
- Authors introduce a new benchmark and evaluation metric for this task. Why can't they use the evaluation setup and metrics as InstanceDiffusion? If authors find flaws in InstanceDiffusion's setup, I recommend authors point it out and discuss the advantages of the IFG Benchmark (setup) and IFS Rate (metric). There is no point in creating multiple new benchmarks when existing ones are already rigorous. For IFS Rate authors use Grounding DINO whereas InstanceDiffusion uses YOLO. Please compare with InstanceDiffusion using their exact setup (COCO and LVIS val set and their metrics) to support your claims.
- Authors claim that the a lightweight network $f$ provides an "importance" score for location (x,y) in the ISM construction and use it to compute $D(x,y)$. Please show qualitative or quantitative evidence that the network $f$ infact does what is claimed in the paper. While the idea sounds reasonable, I suspect how $f$ learns to predict the right "importance" scores without supervision.


### Questions
A few suggestions to improve the paper. 
- Please remove point 3 in contributions. Comprehensive experiments are not a contribution but are rather required to support the claims made in the paper. 
- The related works section has not been used correctly in this work according to my opinion. Authors just cite all relevant work but fail to differentiate their work from the literature. Please discuss how IFG is different from prior work and how their method is different from previously proposed methods in the related works section.
- If authors believe local CLIP score is suboptimal. I would recommend authors show (quantiatively) why VLMs are better than CLIP for this task. Please refrain from introducing a new metric and benchmark unless absolutely necessary.
- L77-78 is a repetition. 

I'm willing to improve my rating if authors address the weakness section satisfactorily.

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
The authors aim to tackle the challenge of achieving controllability in generating precise instance features. To do this, they introduce the Instance Feature Adapter (IFAdapter), designed for instance-level positioning and feature representation. Specifically, the IFAdapter employs learnable appearance queries that extract instance-specific feature information from descriptions, creating appearance tokens that complement EoT tokens. Additionally, the IFAdapter constructs a 2D semantic map to link instance features with designated spatial locations, providing enhanced spatial guidance. In areas where multiple instances overlap, a gated semantic fusion mechanism is utilized to mitigate feature confusion.

To validate their approach, the authors have created a new dataset, referred to as the COCO IFG benchmark. They leverage existing state-of-the-art Vision Language Models (VLMs) for annotation, resulting in a dataset with detailed instance-level descriptions. Experimental results indicate that the proposed plug-and-play component surpasses baseline models in both quantitative and qualitative assessments.

### Strengths
1. A plug-and-play component that can be integrated with various existing models to enhance layout control capabilities.
2. The paper also includes a user study, offering valuable insights into the proposed method.

### Weaknesses
1. The quality of the proposed dataset has not been evaluated. It appears that all ground truths (GTs) are generated by existing Vision Language Models (VLMs). A human-level quality assessment would be beneficial for greater impact within the community. Specifically, the reliance on VLMs for GT generation introduces potential biases and inaccuracies inherent in these models, which could propagate through the training process and limit the reliability of the benchmark. A detailed analysis of the types and frequencies of errors introduced by the VLMs would be necessary to understand the dataset's limitations.
2. The assertion that the proposed component can “seamlessly empower various community models with layout control capabilities without retraining” (l.113) may be misleading. The IFAdapter is fundamentally a training-based method, and the phrase “without retraining” only holds true when applied to spaces closely aligned with COCO IFG, as the IFAdapter does not demonstrate zero-shot capabilities in this paper. The claim of seamless integration is not fully supported by the presented results, which primarily focus on performance within the confines of the training data distribution.
3. The semantic-instance map does not appear to be novel. Please refer to "BoxDiff: Text-to-Image Synthesis with Training-Free Box-Constrained Diffusion" (ICCV 2023) and other zero-shot L2I methods for comparison. The use of a 2D semantic map to link instance features to spatial locations is a common technique in layout-to-image generation, and the paper does not adequately highlight the novelty of their specific implementation compared to existing methods. A more detailed comparison of the technical differences and advantages of their approach is necessary.
4. The appearance tokens show only minor improvements in Table 3. Additional explanations regarding this observation would be appreciated. The small improvement raises questions about the effectiveness of the appearance tokens and whether they justify the added complexity. A more detailed analysis of the cases where appearance tokens do and do not contribute to performance gains is needed to understand their limitations.

### Questions
Please kindly provide visual comparisons between the ground truth (GT) and the generated images.

### Soundness
3

### Presentation
3

### Contribution
3
