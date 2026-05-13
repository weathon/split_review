# DualContrast: Unsupervised Disentangling of Content and Transformations with Implicit Parameterization

- Decision: Reject
- Scores: 5, 6, 3

## Abstract
Unsupervised disentanglement of content and transformation has recently drawn much research, given their efficacy in solving downstream unsupervised tasks like clustering, alignment, and shape analysis. This problem is particularly important for analyzing shape-focused real-world scientific image datasets, given their significant relevance to downstream tasks. The existing works address the problem by explicitly parameterizing the transformation factors, significantly reducing their expressiveness. Moreover, they are not applicable in cases where transformations can not be readily parametrized. An alternative to such explicit approaches is self-supervised methods with data augmentation, which implicitly disentangles transformations and content. We demonstrate that the existing self-supervised methods with data augmentation result in the poor disentanglement of content and transformations in real-world scenarios. Therefore, we developed a novel self-supervised method, DualContrast, specifically for unsupervised disentanglement of content and transformations in shape-focused image datasets. Our extensive experiments showcase the superiority of DualContrast over existing self-supervised and explicit parameterization approaches. We leveraged DualContrast to disentangle protein identities and protein conformations in cellular 3D protein images. Moreover, we also disentangled transformations in MNIST, viewpoint in the Linemod Object dataset, and human movement deformation in the Starmen dataset as transformations using DualContrast.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an unsupervised disentangling method to disentangle content and transformation of the input. Specifically, this paper first proposes two conditions that disentanglement of content and transformation should satisfy. Then, this paper proposes a method to construct positive and negative samples with respect to both content and transformation. The key idea is to utilize a variational autoencoder to construct these samples. The experiments are conducted on four datasets, i.e., three of them (mnist, linemod, and starmen) are pure images, and one is protein subtomogram. One quantitative result and several qualitative results are shown to prove the effectiveness of the proposed method.

### Strengths
1. This paper proposes well-defined conditions for the disentanglement of content and transformation. 
2. The experiments are conducted on four datasets, and comprehensive qualitative results are shown.

### Weaknesses
The main concern of this paper is evaluation, which is insufficient and less significant.
1. The first three datasets (mnist, linemod, starmen) are somehow toy datasets, which is less significant in real-world applications.
2. I agree that protein conformation is one meaningful real-world application, but other than map visualizations, it fails to produce convincing evaluation results. Specifically, the paper lacks quantitative metrics demonstrating the disentanglement of content and transformation in the protein dataset. The qualitative results, while visually appealing, are not sufficient to validate the method's effectiveness in a complex real-world scenario. The paper needs to show that the disentangled representations are actually useful for downstream tasks or analysis in the protein domain.
3. There lacks some widely used evaluating metrics in Table 1 to demonstrate the application of the disentanglement. For example, metrics that quantify the independence of the disentangled latent spaces or the ability to manipulate one factor while keeping others constant would be beneficial.
4. This paper also does not provide comparisons with other baseline methods or state-of-the-art methods. The lack of comparison makes it difficult to assess the relative performance of the proposed method.

### Questions
Please refer to the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Unsupervised disentanglement of transformations and content is a challenging task that was previously approached primarily through using separate ad-hoc transformation methods, or by self-supervised contrastive-based methods. Ad-hoc transformations suffer from being limited to the given parameterization chosen, while self-supervised methods do not tackle this disentanglement problem directly. In this work, DualContrast is proposed, which consists of a VAE with additional contrastive losses designed to disentangle content and transformation. The hardest challenge is obtaining positive pairs of samples with respect to transformations: changing the content while keeping the transformation constant. In this work, this has been done by decoding two random samples from the prior of the transformation latent space while feeding different permutations of the content latent representation to obtain similar transformations with different content. The method is applied to MNIST, LineMod, Starmen Shapes, and Cryo-ET subtomograms with positive results.

### Strengths
Originality.
In this work, a novel method to address the problem of creating positive pairs of transformations under content change has been proposed. The core of this work is original.

Quality.
The method proposed was evaluated on a sufficient number of datasets. Although not very complex, they could suffice in showing the potential for this approach. The baselines chosen are also relevant to the method proposed.

Clarity.
The figures in the experiment section allow for a quick qualitative assessment of the performance of the methods. The method explanation is quite clear.

Significance.
This work and the proposed method have shown some potential for successful applications.

### Weaknesses
The explanation of the method in the abstract and introduction is especially unclear. This is also a problem because Figure 2 fails to properly and intuitively show the method. Reading the method section explains this more. To improve, I would suggest clearly highlighting  the role of the latent space in the creation of the positive pair that would otherwise be impossible. This could be done similarly to how it was done in Figure 3. Figure 2 would then become useful. Additionally, Figure 2 lacks proper annotations such as labeling of all elements present, and proper caption explaining what happens in the figure in a more complete way. There is some inconsistency in how things are called. In the figure, style, and content are mentioned, however, in the text it is clear that "style" is supposed to be "transformation", please pick one and stick with it in the whole manuscript, either one would suffice, however, transformation is likely to be more accurate.

The contributions are a bit bold. The first contribution, especially, is more context for the work than a contribution and could be removed entirely. Please consider reworking the contributions to be more reflective of the actual content.

The related work section should expand a bit more on the protein part, which is currently very unclear for somebody who is not a practitioner. Please provide more examples, even referring to the appendix to understand the data and the context better.

The method section has a few mistakes and the explanation is very wordy, which makes it hard to follow. I wrote a few observations in the questions section of this review.

The manuscript should include the limitations of this method, especially regarding the latent space-based approach to creating positive transformation pairs. For example, the limitations should address whether this approach could be extended to real-world datasets or whether this approach should be limited to specific types of datasets. 

The experiments lack in quantitative results. Although disentanglement is very hard to measure, given the ability to choose datasets, it would be much more convincing to have datasets where a quantitative assessment is possible either in the form of direct supervision (similar to what the disentanglement metric is currently doing), or through some downstream tasks where the disentanglement would be useful. Such tasks could be segmentation, or visual question answer. The choice of the "human deformation" as a dataset is very confusing, and the results reported are also very underwhelming. Although the generated shapes are better, the data appears to be very trivial, so some more information on the training and the difficulty of fitting such samples would be more convincing. The number of parameters, ablation performed, and results from more baselines would be a step in the right direction. It is especially important to keep including all baselines for all datasets used, the results on human deformation appear to be unfinished. If so, it would have been better to simply exclude the dataset from the manuscript. Additionally, plots of the latent space are only available for the cellular dataset

### Questions
In the method section, condition 1 is very confusing. I think it was meant to be "for all $T \in T$ and $x \in X, h_c(T(x)) = h_c(x)$", but please correct me if I misunderstood this.

In the method section, many terms are used seemingly interchangeably, such as "latent space", "factor", "representation", "transformation", "content". Please clarify these terms. For example, at line 206, "transformation" is used, however, I think it was meant to be "transformation representation" or "transformation factor", unless I misunderstood.

There are a few grammatical and syntactical mistakes, such as inconsistencies in the use of uppercase and lowercase, sometimes writing "shape focused" while other times "shape-focused".

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors propose a model that learn unsupervised representation for  "shape-focused images". In particular, their method, DualContrast, learn to disentangle "content" and "transformation" in an unsupervised fashion. The model is trained with an a combination of 2 contrastive losses (one for context, one for transformations) and a VAE loss (the VAE is used to sample positive samples for the CL of transformations). The authors show results of the proposed model on multiple small/toysh datasets.

### Strengths
+ The paper is well written and easy to follow
+ The idea of disentangling features is an important problem in many applications of machine learning
+ The proposed approach is simple and well motivated

### Weaknesses
 -  The author often mention that the work focus on "shape-focused real-world images", but they only applied in very simplified, toysh settings, very far from "real-world images". Even the CryoEM task is a very simplified task. The experiments on CryoET, while more complex than MNIST or LineMod, still do not fully represent the challenges of real-world applications in this domain. The use of simulated data, while convenient, lacks the noise and artifacts present in experimental data, which could significantly impact the performance and generalizability of the proposed method.
- The choice of positive/negative samples for each factor is very ad-hoc. The paper lacks explanation and empirical validation on why this choice makes sense versus others. The contrastive learning setup relies on a specific pairing strategy, but the authors do not explore alternative pairing strategies or provide a clear justification for their particular choice. For example, using different transformations or combinations of transformations to create positive/negative pairs could lead to different disentanglement properties, and this is not explored.
- I found very strange the choice of using VAE generated samples as data to train the contrastive loss. This idea of using generated smples to train a model is not well understood. This approach might have worked in the very simplified tasks tested on the paper, but It is very unlikely that the proposed model would work on any real-world dataset. The use of VAE-generated samples introduces a potential bias, as the VAE's generative capabilities might not fully capture the true data distribution. This could lead to the model learning to disentangle factors within the VAE's representation space rather than the actual data space, limiting its applicability to real-world scenarios.
- I also find the experimental results a bit weak. First, the datasets utilized in this work are very simple and results on them probably wont guarantee their utility on real-world problems. Second, the metrics utilized on Table 1 are not particularly significant. Third, most of the results are qualitative and based on one or two images that can potentially be cherry picked. The qualitative results, such as UMAP plots and image grids, lack quantitative validation. The conclusions drawn from these qualitative results are not robust, as they could be influenced by cherry-picking or other biases. The lack of quantitative metrics makes it difficult to assess the true performance of the proposed method.

### Questions
- On L147, the authors say that they model "is highly effective in disentangling wide range of transformations from the content in various shape-focused image datasets by only using simple rotation for creating contrastive pairs since the representation for disentangled rotation generalizes over other shape transformations." Could they elaborate on this? Why is it the case? Where is it shown on the paper? How can we be sure it will work to other modalities besides the toy tasks tested?
- Is the VAE trained at the smae time as the contrastive losses? Since the VAE is used to generated samples for the CLs, how do training jointly vs training in two stages (VAE followed by CLs) change the performance?

### Soundness
2

### Presentation
3

### Contribution
2
