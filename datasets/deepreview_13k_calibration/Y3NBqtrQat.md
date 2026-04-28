# Learning Object-Centric Representation via Reverse Hierarchy Guidance

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Object-Centric Learning (OCL) seeks to enable Neural Networks to identify individual objects in visual scenes, which is crucial for interpretable visual comprehension and reasoning. Most existing OCL models adopt auto-encoding structures and learn to decompose visual scenes through specially designed inductive bias, which causes the model to miss small objects during reconstruction. Reverse hierarchy theory proposes that human vision corrects perception errors through a top-down visual pathway that returns to bottom-level neurons and acquires more detailed information, inspired by which we propose Reverse Hierarchy Guided Network (RHGNet) that introduces a top-down pathway that works in different ways in the training and inference processes. This pathway allows for guiding bottom-level features with top-level object representations during training, as well as encompassing information from bottom-level features into perception during inference. Our model achieves SOTA performance on several commonly used datasets including CLEVR, CLEVRTex and MOVi-C. We demonstrate with experiments that our method promotes the discovery of small objects and also generalizes well on complex real-world scenes. Code will be available at \href{https://anonymous.4open.science/r/RHGNet-6CEF}{https://anonymous.4open.science/r/RHGNet-6CEF}.
        \vspace{-0.5em}
		\keywords{Object-Centric Learning \and Self-Supervised Learning}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to add a top-down attention mechanism in current standard Object Oriented Learning models to overcome a blindness issue that occurs for occluded and small objects in crowded scenarios.

### Strengths
The method introduced for using the top down guidance adds a loss function during training that is based on minimising a consistency measurement that evaluates the match of low features extracted with the object slots using KL divergence between these two factors.
At inference time, the number of iterations for the refinement with the top down consistency approach has an impact on the final performance, and it might be a nice way to having a compromise between inference computational time and final performance.

A thorough experimental set-up with ablation studies is reported, demonstrating the higher accuracy of the model in comparision to state-of-the art and the contribution to each of the components.

### Weaknesses
The connection to human visual system is rather weak, and even though it can serve as inspiration, there is no evidence that this could be a computational model for human computations of top down signals. There are other works that point to recurrent connections and other mechanisms for human brain modeling.

### Questions
See weaknesses points

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper's major contribution is introducing idea of top-down modulation in Reverse Hierarchy Theory to the standard slot-attention model aimed for object-centric learning. The major architecture novelty is  a top-down path from the slots of slot attention model to attend the image features and directly generate an attention map by a CNN decoder. This attention map is in turn used to compute a conflict map against the original object mask produced directly by the slot representation through a spatial broadcasting. The conflict loss appears to be the major driving force for the model to improve its ability of discovering small objects, which other models often fail to detect. The model demonstrates superior performance to other models on several benchmark datasets with pure colors, but also generalizes to CLEVRTex which introduces some texture within each object with a dominant distinct color.

### Strengths
(1) All the benchmark result show that the proposed model outperform previous models.

(2) The idea of conflict loss between the two object mask maps appear novel.

(3) Analysis of the representation of objects in CLEVRTex dataset shows that the model learned a representation that has smaller variance in intra-object feature (locked to image grids) than inter-object feature, which may help better group pixels within an object into a same slot. Such analysis is helpful for partially understanding why a model learns better (but I still remain somewhat puzzled, please see my comment in Questions)

### Weaknesses
(1) At inference, the model needs to be run for multiple times to get a performance gain. This increases computational time. 

(2) I think it is worth acknowledging some limitation observed in the visualization. One of the examples in ObjectsRoom of Figure 4 actually shows the proposed model is the only one that hallucinates the yellow color of the floor seen through the hollow part of the triangle shape. From the supplementary material, it seems often "fill in" the hollow part o the triangle in the segmentation mask, which should actually be background. From visual inspection, it seems that for the more challenging datasets such as CLEVRTex, missing small and partial objects is still frequent. And the model appears to often ignore the detailed texture in reconstruction but only captures the average color. Of course all models have limitations, I think it is worth pointing these out in discussion, and it will be interesting to postulate why texture often gets ignored.

(3) It is more of a question but also a weakness (only for the sake of gaining insight): I still lack full understanding of where the teaching signal or inductive bias comes from to get the improvement. See my comment (1) in Questions.

### Questions
(1) Although conceptually it makes sense that top-down modulation should help in object perception, because obviously the brain uses it, the computational mechanism of why it helps in the experiments presented in the paper still remains puzzling to me. I am happy to see the analysis in Figure 7 of the intra-object vs. inter-object feature variance and Figure 6 illustrates the failure of bottom-up only network. But my question is: what even caused these improvement. My guess is that "in-principle", when the top-down attention from the slot includes some aggregated information over pixels of the objects, it is possible for the low-level features to be biased towards such aggregated information. But "in-principle" does not mean this is guaranteed. Moreover, what drives the network being able to learn to detect small objects better? It sounds that the paper indicates that the conflict loss term is the guidance, but the conflict term is simply the conflict between two masks that are both internally generated and to be learned, with no additional inductive bias or teaching signals by introducing the top-down pathway. 

To illustrate my point in more detail: if the slot representation has already lost one small object in the object masks M as in Figure 2, why would it necessarily produce the mask of the missing object through the attention to low-level feature and eventually show in the attention map A? Why would not minimizing the conflict loss C drive A to be more close to M (which will remove the small object) instead of vice versa? There seems to be no teaching signal directly from the image to constrain the attention map A, so I would guess that A is initially random in early stage of learning and is taught by M. Is that the case? If indeed A starts being better than M (it includes the missing objects while M does not), then why not just include A alone in the model? Why bother introducing M? 

One guess is that the major contributor for the better ability of detecting small objects is just the extra depth in the attention map pathway introduced by the top-down attention. If so, would introducing more iterations in the original slot attention model achieve similar improvement? I wonder if the authors can elucidate the actual mechanism.

(2) I would like to get a confirmation that no component of the network is pretrained on other tasks. If some of them are pre-trained, please explain.

(3) At inference time, the model is run N times and the one with the smallest conflict C is chosen. I wonder whether the performance improvement mainly comes from this selection process. What happens to the performance if you set N to 1? I wonder if the authors think that this variation has some similarity to the brain? Perhaps the brain does not always detect all objects with one (or two) glances. The ones being missed by the brain depends on what a person's initial top down attention is on.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Inspired by Reverse Hierarchy Guidance, a theory related to human vision, the authors
propose an improvement for object-centric models based on clustering features into
slots. Central to the approach is measurement of conflicts between spatial feature
similarities and the clustering predicted by the model. The paper shows that established
object-centric models can be improved by minimizing conflicts during training and/or by
chosing the sampled segmentation with the least conflicts during inference. In
particular, the segmentation of small objects is improved which are more frequently
missed by existing methods.

### Strengths
- Existing methods are consistently improved on established, synthetic datasets.
- The authors provide an analysis that explains *why* the proposed method works by
  qualitatively and quantitatively inspecting segmentation performance for objects of
  different sizes. Beyond providing an improvemend model, the paper therefore also
  improves the understanding of object-centric modeling approaches.
- The Figures provided by the authors are helpful to understand the contribution. Beyond
  aggregated quantitative evaluation, the authors present figures that qualitatively
  showcase the improvements of the proposed method.

### Weaknesses
 - In the main text, the proposed method is only evaluated on relatively simple, synthetic datasets. As shown in the supplement, the method can be combined with state-of-the-art object-centric models that scale to natural images, but the performance improvements do not seem to be significant.
- The mathematical description of the method in Section 3 is imprecise at several places. How exactly are the mappings $\mathcal{K}$ and $\mathcal{Q}$ defined? I.e., what are the dimensionalities of the quantities involved in equation 3? In equation 4, the term in the summation does not depend on the summation index $K$.
- The performance comparison in Table 1 uses FG-ARI to quantify segmentation performance. It has been pointed out several times in the literature that this metric is problematic (e.g., Engelcke et al 2020, Karazija et al. 2021, Monnier et al. 2021). How do the proposed methods perform in terms of the Object IoU metric?
- Does the Object IoU metric include evaluating IoU for the background segment?
- How were the object sizes chosen that where used to differentiate small, medium and large objects? Which fraction of the objects is small, medium and large, respectively? Beyond the agregated evaluation, it could be helpful to present a scatter plot of object size vs IoU for all objects in the evaluation set.
- How were the hyperparameters selected?
- Which performance is achieved when the features are clustered using a conventional approach such as normalized cuts instead of Slot Attention?

### Questions
- The performance comparison in Table 1 uses FG-ARI to quantify segmentation
  performance. It has been pointed out several times in the literature that this metric
  is problematic (e.g., Engelcke et al 2020, Karazija et al. 2021, Monnier et al. 2021). 
  How do the proposed methods perform in terms of the Object IoU metric?
- Does the Object IoU metric include evaluating IoU for the background segment?
- How were the object sizes chosen that where used to differentiate small, medium and
  large objects? Which fraction of the objects is small, medium and large, respectively?
  Beyond the agregated evaluation, it could be helpful to present a scatter plot of
  object size vs IoU for all objects in the evaluation set.
- How were the hyperparameters selected?
- Which performance is achieved when the features are clustered using a conventional
  approach such as normalized cuts instead of Slot Attention?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method to improve on existing methods to parse scenes into object representations to better detect small/occluded objects. The method combines a bottom-up mechanism which tries to parse the scene into K object slots and a top-down mechanism which detects conflicts between the slot-based reconstruction and the original image and searches for a slot assignment which reduces conflicts. The approach gives improved results over benchmark algorithms on synthetic datasets.

### Strengths
The paper is mostly clearly written (there is some awkward grammar/wording) and makes excellent use of figures to illustrate results.

The proposed method is simple and effective.

There is a good amount of analysis and visualisation to explain the method.

### Weaknesses
The proposed method outperforms older SOTA models but does not clearly outperform some more recent work which incorporate different forms of “object” guidance into a bottom-up model:
https://openaccess.thecvf.com/content/WACV2023/papers/Sauvalle_Unsupervised_Multi-Object_Segmentation_Using_Attention_and_Soft-Argmax_WACV_2023_paper.pdf
https://arxiv.org/pdf/2305.19550.pdf
Given that these works involve some similar ideas to the current paper, it seems worthwhile to address them.

The section on "generalization to real-world scenarios" contains almost no information about what experiments were run or what the results were. If these results are important to evaluate the proposed method they should be explained in the paper.

### Questions
How does this method differ from other recent work with similar performance? What are the advantages of this proposed approach?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
