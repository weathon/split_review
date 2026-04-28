# HyperPg - Prototypical Gaussians on the Hypersphere for Interpretable Deep Learning

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 5, 3, 1

## Abstract
Prototype Learning methods provide an interpretable alternative to black-box deep learning models. Approaches such as ProtoPNet learn, which part of a test image ``look like'' known prototypical parts from training images, combining predictive power with the inherent interpretability of case-based reasoning. 
However, existing approaches have two main drawbacks: A) They rely solely on deterministic similarity scores without statistical confidence. B) The prototypes are learned in a black-box manner without human input.
This work introduces HyperPg, a new prototype representation leveraging Gaussian distributions on a hypersphere in latent space, with learnable mean and variance. HyperPg prototypes adapt to the spread of clusters in the latent space and output likelihood scores.
The new architecture, HyperPgNet, leverages HyperPg to learn prototypes aligned with human concepts from pixel-level annotations. Consequently, each prototype represents a specific concept such as color, image texture, or part of the image subject. 
A concept extraction pipeline built on foundation models provides pixel-level annotations, significantly reducing human labeling effort.
Experiments on CUB-200-2011 and Stanford Cars datasets demonstrate that HyperPgNet outperforms other prototype learning architectures while using fewer parameters and training steps. Additionally, the concept-aligned HyperPg prototypes are learned transparently, enhancing model interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper argues that conventional prototype methods often capture latent prototypes without human control, resulting in unstable and less transparent prototype generation. To address these issues, the paper introduces Gaussian distribution into the prototypes and proposes a novel optimization mechanism for refining them, enabling more reasonable and interpretable results.

### Strengths
1. The idea presented in this paper is both motivated and novel, with the proposed method aligning well with the underlying motivation.
2. The quantitative and qualitative results demonstrate the effectiveness of the proposed method to some extent.

### Weaknesses
1. The organization of this paper requires significant improvement, as the content's logic is disjointed. For instance, in the methodology section, the paper introduces the training loss first, then unexpectedly shifts to the model structure before resuming the discussion on the loss and proposed improvements. Additionally, when describing traditional prototype methods, the paper does not seamlessly explain the necessity of the Gaussian distribution, making the argument unconvincing.
2. The paper should include more quantitative and qualitative results in the experimental section. Currently, it dedicates too many pages to the method description while lacking sufficient experimental outcomes. It is recommended to present additional qualitative results in the Appendix.
3. This paper should provide a more detailed discussion on the challenges of training the proposed prototype generation method. Prototype learning is known as difficult to train, yet the paper only briefly mentions the complexity of the proposed method without offering in-depth analysis.

### Questions
See the weakness part.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose HyperPg, , a new prototype representation leveraging Gaussian distributions on a hypersphere in latent space, with learnable mean and variance for adapting to the spread of clusters in the latent space and outputs likelihood scores. Additionally, the authors propose HyperPgNet, which leverages HyperPg to learn prototypes aligned with human concepts from pixel-level annotations. Experiments on CUB-200-2011 and Stanford Cars datasets demonstrate that HyperPgNet outperforms other
prototype learning architectures while using fewer parameters and training steps.

### Strengths
1. The idea of learning explainable and interpretable prototypes is interesting and well-motivated.
2. The paper is generally well-written and well organized.

### Weaknesses
1. The novelty of the paper is somewhat limited. The idea of using Gaussian distribution for prototype learning has been extensively studied before in computer vision. Please see [1] for an example. The authors need to clarify the difference of the proposed method with these existing works.

2. The experiments are limited. Only two datasets are included. Also, the authors leverage the Grounding DINO model and SAM for auto-labelling, it is not clear if the labels obtained in this manner are actually accurate enough to learn the prototype. Therefore, the authors need to clarify if the conclusions are supported by the results.

### Questions
1. What are the main benefits of the proposed method? In Table 1, it can be observed that the proposed method is better than black box methods on Stanford cars, but actually comparable on CUB-200-2011. Also, qualitative results are rather limited. Therefore, it is not clear why the proposed method can increase interpretability of the model.

2. How are the hyperparameters selected in the proposed loss?

3. Can the authors provide more analysis on the  interpretability of the model? Seems like the propose method can locate the meaningful regions from the images, what is the difference of this compared with the attention mechanism in transformer architecture which can also achieve similar effects.

4. In Table 1, why the segformer baseline achieve much worse results compared with other methods?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper builds on top of the prototype-based learning literature and proposes to combine the usage of Gaussian and hyperspherical prototypes by learning prototypes that are defined as Gaussians on a hypersphere. The combine this with the loss from Ross et al. In order to make the prototype maps more faithful to available segmentation maps.

### Strengths
The paper is written in a clear manner and is easy to follow. The method is simple.

### Weaknesses
I’m under the impression that the authors don’t really manage to drive the message that the proposed method results in any advantage:

The experimental setup is rather limited:
1) Only two datasets with one single setting, no ablations nor tests with different number of prototypes.
2) Very few competitors, and rather outdated (2019 and 2020). Many other works are mentioned in Section 2. What is the reason not to include more of them?
3) The baselines are rather weak. ConvNext-tiny is far from a model that can obtain sota results, and a more adapted baseline would dramatically improve these results. SegFormer is a segmentation model. I’m not sure how the authors trained it for classification, but it sort of makes
4) For an inpteretability-focused paper, there are very few qualitative results. On top of that, the few that are available suggest that the prototype gradient maps are not particularly interpretable. How do there compare to competing methods?
5) Fig 5 seems to suggest that some of the baselines did not yet reach convergence.

6) Other than the lack of empirical evidence, the authors don’t provide a convincing argument of why Gaussians in a hyperphere should be better prototype representations.

### Questions
I think a lot more experimental evidence, along with a clearer rationale, is needed for this paper to be convincing.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper presents a comprehensive approach to advancing prototype-based learning by introducing prototypes modeled as Gaussian mixtures and aligning them closely with underlying semantic concepts in the data. To achieve this, the authors propose a novel architecture built upon the SegFormer backbone. This architecture is enhanced by incorporating the "right for the right reasons" loss function, which emphasizes alignment between model predictions and human-understandable reasons behind those predictions, ensuring that the model learns interpretable and robust representations.

The effectiveness of the proposed approach is evaluated on well-established benchmark datasets, specifically CUB and Stanford Cars, which provide challenging tasks for fine-grained visual categorization. Moreover, to emulate realistic conditions where user interaction might guide the discovery of underlying concepts within the dataset, the authors simulate user input.

### Strengths
The methodology introduced in this paper is both novel and compelling. The core idea of representing prototypical parts as Gaussian mixtures stands out as an innovative approach. 

The motivation behind this work is well-articulated, addressing key challenges in interpretable and concept-aligned machine learning. 

Furthermore, the paper is carefully organized, with a logical progression of ideas that guides the reader through the technical details and innovations. Each section is clearly written, making complex concepts accessible and enhancing the paper's overall readability.

### Weaknesses
I have significant reservations regarding the evaluation methodology presented in this paper. First, the ProtoPNet model, which uses a CNN backbone, achieves notably better results than the model with the SegFormer backbone. This discrepancy is unexpected and calls for further investigation. I recommend that the authors consider using the same backbone for a more consistent comparison with ProtoPNet, as differences in backbones could introduce confounding variables that obscure the real advantages of the proposed method. Specifically, the feature extraction capabilities of the SegFormer might not be as well-suited for this task as a CNN, or the training regime might need to be adapted to the transformer architecture. It is crucial to isolate the impact of the Gaussian mixture prototypes from the backbone architecture itself.

Secondly, I would like to direct the authors to two relevant publications, [1] and [2], which address crucial aspects of prototypical part learning. Publication [1] introduces a benchmark specifically designed for prototypical parts, which could help in assessing the robustness of prototypical parts learned through transformer-based architectures like SegFormer. Due to SegFormer's global attention mechanism, it may be prone to spatial misalignment. The benchmark could reveal if the learned prototypes are indeed localized to meaningful object parts or if the attention is scattered across the image. Additionally, publication [2] presents a model that effectively disentangles visual features—such as color, shape, and texture—within prototypical parts. With the current approach, I am not convinced that the proposed model achieves this level of separation. Conducting further experiments or introducing additional benchmarks could help verify it. For instance, a targeted experiment could involve manipulating the color of an object while keeping the shape constant, and assessing if the learned prototypes respond accordingly. 

Finally, I suggest that the authors compare their approach to concept bottleneck models [3]. Given that the current work intersects both concept learning and prototype alignment, a comparison with these models would provide a more comprehensive evaluation and clarify the unique contributions of the proposed method in relation to established approaches. Specifically, a comparison should focus on the interpretability of the learned concepts and the ability of the model to generalize to unseen combinations of concepts.

### Questions
1. Why not compare with CNN-based ProtoPNet?

2. Reference to papers mentioned in weaknesses.

3. Discussion and comparison to CBM models.

### Soundness
1

### Presentation
3

### Contribution
3
