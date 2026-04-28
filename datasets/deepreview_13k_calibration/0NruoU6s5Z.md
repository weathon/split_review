# CompoDiff: Versatile Composed Image Retrieval With Latent Diffusion

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
This paper proposes a novel diffusion-based model, CompoDiff, for solving zero-shot Composed Image Retrieval (ZS-CIR) with latent diffusion. This paper also introduces a new synthetic dataset, named SynthTriplets18M, with 18.8 million reference images, conditions, and corresponding target image triplets to train CIR models. CompoDiff and SynthTriplets18M tackle the shortages of the previous CIR approaches, such as poor generalizability due to the small dataset scale and the limited types of conditions. CompoDiff not only achieves a new state-of-the-art on four ZS-CIR benchmarks, including FashionIQ, CIRR, CIRCO, and GeneCIS, but also enables a more versatile and controllable CIR by accepting various conditions, such as negative text, and image mask conditions. CompoDiff also shows the controllability of the condition strength between text and image queries and the trade-off between inference speed and performance, which are unavailable with existing CIR methods.
\ifx\preprint\undefined
The code and dataset samples are available at \texttt{Supplementary Materials}.
\fi

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the limitation of the small dataset and small categories of conditions on the Composed Image Retrieval (CIR) task through a new diffusion-based model (CompoDiff) and a large-scale CIR dataset (SynthTriplets18M). They show the generalizability of their dataset training CompoDiff on the existing CIR benchmarks.

### Strengths
- Clear presentation of their approach\
This paper tackles the lack of a dataset for this task, which raises the generalizability of this task. It is a clear objective to present a large-scale dataset. To construct on a large scale, they utilize a large generative model such as Stable Diffusion to produce a synthetic dataset. This reviewer can agree with the direction of their approach, and it contributes to this community.


- Flexibility of their model\
Not only improving the performance on the existing benchmarks of CIR, they also suggest a more flexible manner of CIR including negative texts or masks, which give a large potential for its application.

### Weaknesses
 - A small improvement using better backbone architecture
For a fair comparison, it is hard to agree that their model (ViT-L) performs better than the previous arts whose backbones (RN50) are much lighter (Table. 2). Therefore, this reviewer recommends comparing them in the backbone with similar capacity (same backbone is the best option) as much as possible.
- Efficiency comparison with the previous arts
Even though they show inference time varying the diffusion steps, this reviewer suggests the comparison of latency or flops with the previous arts. Their intra-model analysis is also w
- An insufficient contribution of CompoDiff
As far as this reviewer’s understanding, COmpoDiff is a minor modified version of Stable Diffusion. This reviewer considers their flexibility for the conditions also stems from the power of Stable Diffusion. Also, this reviewer wonders what the performance of the Stable Diffusion trained on SynthTriplets18M is on the CIR benchmark.

### Questions
The questions are naturally raised in the weaknesses section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a composed image retrieval method, called CompoDiff, based on the diffusion model and proposes a large-scale dataset, called SynthTriplets18M, for the composed image retrieval task. In the experiments, the qualitative and quantitative results demonstrated that the performance of the proposed CompoDiff in terms of composed image retrieval exceeds the comparison method. Comparing the results of the model trained with different scales of data, it shows that a large amount of training data can improve the model effect.

### Strengths
1. This paper proposes a novel CIR method that can additionally limit the scope of the search image based on the input mask and other conditions.
2. This method can also control the balance between retrieval accuracy and retrieval efficiency without training, as well as control the impact of each condition on the retrieval results.
3. This paper proposes a dataset that promotes the development of CIR-related research and illustrates, to a certain extent, the impact of dataset size on methods.

### Weaknesses
1. The authors raised the problem of requiring triples for training: but it was not solved well, and the authors just proposed a larger data set. The core issue of needing pre-collected, human-verified triplets remains, and simply scaling up a synthetic dataset does not inherently address the labor-intensive nature of obtaining high-quality, real-world triplets. The method still relies on a form of triplet data, albeit synthetically generated, which doesn't circumvent the fundamental challenge of needing such structured data for training.
2. The experimental results show that the effect of the proposed data set and other data sets are similar at the same level, and after the data volume reaches a certain level, continuing to increase the size of the data set may not significantly improve the model performance. It negates the value of the data set to a certain extent. The saturation in performance gains with increasing dataset size, particularly beyond 10M, suggests diminishing returns. This raises questions about the practical utility of the 18M dataset, especially if the gains are marginal compared to a smaller, more manageable dataset. The lack of substantial improvement beyond a certain scale undermines the claim that dataset size is a primary driver of performance.
3. The data set used by the comparison method is inconsistent with the data set used by the proposed method, which is not quite fair. The comparison methods, particularly those not designed for triplet-based training, are evaluated on different datasets than the proposed method, making it difficult to draw direct and fair conclusions about the relative effectiveness of CompoDiff. This inconsistency in training data introduces a confounding variable, making it unclear whether the observed performance differences are due to the method itself or the training data.

### Questions
1. Can additional comparison experiments be conducted, for example, both the proposed method and the comparison method are trained on SynthTriplets18M to illustrate the effectiveness of the proposed method?
2. The paper mentions that the size of the data set is very important. Can experiments regarding the size of the data set be conducted in other methods to illustrate the effectiveness of the data set?

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
The authors introduces CompoDiff, a novel diffusion-based model, for the task of Composed Image Retrieval (CIR) with latent diffusion. It also proposes a new dataset named SynthTriplets18M. Importantly, it supports diverse conditions like negative text and image masks, offers control over query importance, and allows trade-offs between inference speed and performance, improving the overall CIR process.

### Strengths
- The concept introduced here is really interesting, although the components used here carry less novelty.

- The writing of introduction, and the overall paper is quite fluid and easy to understand.

- The synopsis of every topic is provided in a self-contained manner.

- Qualitative Figures are well portrayed.

### Weaknesses
 - Although the experiments are extensive, little reasoning is provided as to why the methods perform (low/high) in the way they do. More analytical reasoning would be encouraged.

- The paper could've been written in a more self-contained manner. A basic background of unCLIP, segCLIP and other components could have been provided instead of simply citing the paper, even 2-3 lines would enhance the readability of the paper.

- The training paradigm seems a bit convoluted. Rephrasing of certain sentences could bring about clarity in the understanding, for instance, discussing a small background on diffusion models first, then bringing in text-image composite part.

- Although not intuitive in this respect it makes me wonder what would be the effect if a learnable text prompt is used in the CLIP-text branch?

- Despite having a few competitors, it would have been better to provide a few baselines focussing on variations of design components used for the proposed method.

### Questions
- Does this retrieval include images containing multiple target objects for retrieval as well?
- Although not intuitive in this respect it makes me wonder what would be the effect if a learnable text prompt is used in the CLIP-text branch?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel diffusion-based model, named CompoDiff, which could merge the multimodal conditional information, for solving composed image retrieval (CIR) task. It also proposes a newly created synthetic dataset, named SynthTriplet18M, of 18 million training triplets (reference image, conditions, and target image). The proposed model and dataset address the poor generalizability of existing CIR methods, due to the small training dataset scale and limited types of conditions. The experimental results show the proposed method achieves better results on four public CIR benchmarks.

### Strengths
1. The idea of leveraging the synthetic data for training of CIR task is pertinent, since the triplet-labeled training data required for CIR task is laborious to collect. 
2. Borrowing the idea from the diffusion of generative task, the authors also explore the possibility of adopting the diffusion mechanism for latent feature extraction in discrimination task, and prove it has the potential to achieve good retrieval accuracy. 
3. It is interesting that the adoption of diffusion enables negative text for CIR task.

### Weaknesses
1. The section 3.1 needs to be written more clearly, it is preferable to annotate the letters and variables that appear in Eq. (1), (2), (3) in Figure 3, for example, $z_{i,masked}$; what is the relationship between $e_{t}$ and $z_{i}^{t+1}$? It is difficult to understand from Figure 3 and Eq.(1), (2), and (3). Specifically, the role of the time embedding, which is crucial in diffusion models, is not clearly explained in the context of feature extraction. The lack of explicit annotation of variables in Figure 3 makes it hard to follow the mathematical formulation and the overall process.
2. The diffusion part for feature extraction is very opaque. In Figure 3, what is the intuition of forward diffusion (adding noise T times) and denoise diffusion? In the generation task, the output of the diffusion process consists of pixel values, which have a clear and explicit meaning, while in the retrieval task, the output of the diffusion process is latent variables that do not have a clear and explicit meaning. The paper does not adequately explain why a diffusion process is suitable for feature extraction, especially when the output is not a tangible entity like an image but rather a latent representation. The connection between the diffusion process and the semantic meaning of the extracted features is unclear.
3. I think the authors should consider the time and resource consumption carefully. The training stage is very complex, since the framework involves two stages that both require massive data, and the stage 2 requires some tricks such as alternative strategy, which is unstable, and resource-consuming. For the inference stage, it requires 5 diffusion processes for each query sample while each diffusion process still needs multiple steps, which is very time-consuming since the diffusion process is very slow. It is necessary to compare the inference time with previous methods. In section 4, when collecting the synthesized caption, fine-tuning the OPT-6.7B model is very time-consuming and resource-consuming. The paper lacks a detailed analysis of the computational cost associated with each stage of the proposed method, making it difficult to assess its practical applicability.
4. I think there is some mistake on the left side of Eq.(4). Besides, in section 4, x_c is used in the fourth and sixth rows, while x_{c_T} is used in the fifth row. The inconsistency in notation introduces confusion and raises concerns about the correctness of the equations and the overall methodology.

### Questions
In keyword-based diverse caption generation of Figure 5, according to my knowledge, it is not quite reliable to collect the alternative keywords using the CLIP feature similarity. Firstly, some alternative keywords may share a similar concept with the target keyword, but the synthesized caption may not be reasonable. For example, “plants”, “flora” share similar concept with “strawberry”, but “plants tart” and “flora tart” is ridiculous. Even if frequency filtering is used and restricting the CLIP similarity within 0.5~0.7, this phenomenon still exists. Moreover, keywords such as “portrait, figure, image” have consistently high similarity with most keywords, but they do not have specific meanings; keywords such as “painting, drawing, walk, hiking” may have different parts of speech (verb and noun), and some keywords such as “light, chair, season” may involve different meanings in different context. Note that what I'm referring to is not limited to the examples mentioned above, but it's a general issue, and all these problems can lead to the generation of very strange modified captions. I am curious how these problems are considered and solved.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
