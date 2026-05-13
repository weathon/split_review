# Multi-Scale Fusion for Object Representation

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
Representing images or videos as object-level feature vectors, rather than pixel-level feature maps, facilitates advanced visual tasks.
Object-Centric Learning (OCL) primarily achieves this by reconstructing the input under the guidance of Variational Autoencoder (VAE) intermediate representation to drive so-called \textit{slots} to aggregate as much object information as possible.
However, existing VAE guidance does not explicitly address that objects can vary in pixel sizes while models typically excel at specific pattern scales.
We propose \textit{Multi-Scale Fusion} (MSF) to enhance VAE guidance for OCL training. 
To ensure objects of all sizes fall within VAE's comfort zone, we adopt the \textit{image pyramid}, which produces intermediate representations at multiple scales;
To foster scale-invariance/variance in object super-pixels, we devise \textit{inter}/\textit{intra-scale fusion}, which augments low-quality object super-pixels of one scale with corresponding high-quality super-pixels from another scale.
On standard OCL benchmarks, our technique improves mainstream methods, including state-of-the-art diffusion-based ones.
The source code is available in the supplemental material.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes multi-scale fusion (MSF) for object-centric learning. Specifically, MSF extracts VAE representations corresponding to the same input, downsampled to varying resolutions. The output representations are then upsampled and downsampled as necessary and then combined as a way to augment each set of features. The augmented features can then be fed as input to the general OCL decoder (along with the slot attention outputs and the matching entries from the discrete codebook). This intends to allow for better, more separable, semantically distinct representations of objects at varying scales. The quality is demonstrated with varying metrics corresponding to unsupervised segmentation on the masks that are generated as a byproduct of this OCL pipeline.

### Strengths
[S1] The method seems to consistently outperform competitors for the OCL benchmarks, and is even somewhat competitive with the foundation model baseline (DINOSAUR).

[S2] The approach is well-motivated.

[S3] Figure 3 effectively demonstrates, qualitatively, how the MSF accomplishes better OCL, that is, features that are better connected to the objects themselves.

### Weaknesses
[W1] The impact of the work seems limited. The ideas about multi-scale representation and fusion themselves are not novel (see for example FPN in object detection literature), but the implementation and application to this task are. However, the implementation neglects potentially more impactfully redesigns of the primary encoder-decoder pipeline or the slot attention mechanism itself. The core idea of fusing multi-scale features is not new, and while the application to VAE representations within an object-centric learning framework is a specific contribution, the overall impact is somewhat incremental. The method's novelty lies in the specific way multi-scale features are fused within the VAE, rather than a fundamental shift in the OCL paradigm. This raises questions about the broader applicability and long-term significance of the approach. 

[W2] Additionally, there are no results for any downstream tasks. Thus, while interesting, it is hard to project the impact of the work beyond this niche. The lack of downstream task evaluation makes it difficult to assess the practical utility of the learned representations. While the unsupervised segmentation results are promising, it remains unclear how well these representations would generalize to tasks such as visual reasoning, planning, or manipulation. The absence of such results limits the potential impact of the work.

Minor: The notation and its interaction with Figure 3 is unpleasant and difficult to follow. In particular, the differences between scale-variant, scale-invariant, and representation before inter-scale fusion are quite slight and seem slightly arbitrary. 

Minor: Algorithm 1 would fit in the main paper, and help add clarity in the flow.

### Questions
What downstream tasks could this method help with? It doesn't seem to be a SAM alternative, so what is the potential practical impact?

What would change were this applied to higher-resolution images? MSF would seem to have some promise for small objects, but those are essentially all filtered out by the pre-processing.

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
This paper addresses Object-Centric Learning (OCL), which aims to capture comprehensive object information by reconstructing inputs using intermediate representations from a Variational Autoencoder (VAE). The focus is on multi-scale training, acknowledging that objects may appear at various scales in images or videos due to changes in imaging distance or intrinsic size differences. The authors propose Multi-Scale Fusion (MSF) applied to VAE representations to guide OCL for both transformer-based approaches and state-of-the-art diffusion models. The method demonstrates promising performance on datasets such as COCO, ClevrTex, and VOC.

### Strengths
1) The overall intuition and direction of the paper is good and deal with important problems of Object-Centric Learning.
2) The multi-scale training makes a lot sense since dealing with objects is an important problem and generally has not been solved fully in the field.
3) The paper shows good analysis and shows object separability of VAE guidance in Fig3. Fig2 quantitative results also look good.

### Weaknesses
1) Results on real world datasets especially COCO in Table 1 are really incremental. It’s not really clear how much advantage is by adding MSF.
2) Analysis of varying object sizes can show results on scale understanding better than overall IoU improvement.
3) Is there any intuition as to why the value of n is 3? Can we do a similar experiment on OpenImages and see if this holds true across datasets? For Openimages, if it’s easier you can try using the smaller subset of open images curated in this paper [1].
4) Discussion on the area of unsupervised semantic segmentation and object detection using SSL methods should be added. Papers like [1,2,3] should be discussed.

### Questions
Overall the paper is good, but the results specially on COCO seems a bit incremental.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses the lack of multi-scale object representation in VAE-guided OCL problems by constructing a multi-scale VAE model. This enables the VAE-generated results to represent multi-scale objects, thereby improving performance across various tasks.

### Strengths
1. The paper is clear writing and easy to follow.

### Weaknesses
1. I think the paper's novelty is very limited. Although I am not familiar with object-centric learning, I believe that constructing multi-scale VAE features has already been applied in many generative tasks[1, 2]. Therefore, the core innovation of this paper, in my opinion, does not warrant a standalone publication. Can the author tell me about the difference between MSF and other methods?

2. Since I am not familiar with this field, the Area Chair (AC) and the authors may disregard my opinion if it appears to be biased.

### Questions
I am not familiar with this field, so please refer to the weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper is motivated by Object-Centric Learning (OCL) AND introduces a multi-scale fusion scheme to vanilla VAE and improves its representation of different scales of objects. The motivation is convincing, but the technical novelty is limited and multi-scale fusion is a widely used technique in many models and computer vision tasks. Though this paper proposes some specific design modules, like multi-scale features augmentation, they are straightforward and improvements are limited according to the ablation study.
Though the technical novelty is limited, this paper investigate an interesting view, OCL, to VAE, should be benefit the comunity.

### Strengths
The MSF is straightforward and easy to understand. According to the experimental results, it works well and improves a strong basline model DINO.
OCL is an interesting and promising direction and this paper outperform previous OCL methods.
The method can be generalized to virous computer tasks and model to improve their representation of objects.

### Weaknesses
According to Sec. 4.1, the improvements from MSF are limited, just 1-2 points in many metrics. 
The overall presentation is not satisfactory and difficult to understand for readers not familiar with OCL.

### Questions
Can the proposed method be applied to state-of-the instance segmentation models, like MaskDINO, to improve their results (~50 mask AP) on MS-COCO for instance segmentation.

### Soundness
2

### Presentation
2

### Contribution
2
