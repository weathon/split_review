# Neighborhood-Informed Diffusion Model for Source-Free Domain Adaptation: Retrieving Source Ground Truth from Target Query's Neighbors

- Decision: Reject
- Scores: 3, 8, 5, 3

## Abstract
Diffusion models, empowered as an input augmentation technique, have demonstrated promise in domain adaptation. However, to effectively capture shared characteristics between two data densities, such a diffusion model needs to be trained using both source and target data for its generation. This constraint narrows its application to a more demanding yet authentic scenario where source data remains inaccessible during target adaptation, i.e., source-free domain adaptation (SFDA). In the absence of source data during adaptation, which hinders the analytical quantification of domain shift, can we employ the pre-trained source representation to formulate a diffusion model for facilitating the unsupervised clustering in target adaptation? To answer this question, we introduce a novel method, discriminative neighborhood diffusion (DND). DND transforms the pre-trained source representation into a target-to-source diffusion model by parameterizing the prior densities of the diffusion process, leveraging the smoothness indicated by latent k-nearest neighbors (k-NNs). The samples generated from the diffusion model are then used as positive keys for contrastive clustering during adaptation. This process effectively introduces a form of supervision into unsupervised clustering by incorporating the latent geometries from both the source and target domains' latent k-NN. By evaluating DND against various SFDA methods on multiple benchmark datasets, we demonstrate the discriminative potential of diffusion models in the absence of source data. Moreover, the effectiveness of DND is demonstrated as it successfully solves SFDA problems, achieving state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a new method: discriminative neighborhood diffusion (DND). DND formulates a diffusion model using pre-trained source domain representation and combine it with contrastive learning to promote unsupervised clustering of the target domain in the domain adaptation process.

### Strengths
The paper introduces the diffusion model into the SFDA problem, and the proposed method is simple and effective.

### Weaknesses
1) DND may violate the problem setting of SFDA, i.e., learning a target model with only a pre-trained source model and target data introduced by SHOT. Specifically, the diffusion model in DND is trained using source data, which deviates from the standard SFDA setting where only a pre-trained source model is provided and no further source data access is allowed during target adaptation. This additional training phase with source data during pre-training makes DND more akin to traditional UDA methods that have access to both source and target data during the entire training process.
2) The writing logic of the paper is chaotic and difficult to read, especially in the introduction section. In addition, it is not advisable to use a large space in the method section to introduce existing work: IADB, and a brief explanation is sufficient.
3) This method requires a large number of hyperparameters, and it seems difficult to quickly find suitable parameters. And there is a lack of hyperparameter sensitivity experiments. The paper does not provide sufficient guidance on how to choose the number of diffusion steps, the number of neighbors for source pre-training ($k_s$), and the number of neighbors for target adaptation ($k_t$). The absence of a sensitivity analysis makes it unclear how robust the method is to different hyperparameter settings.
4) The persuasiveness of conducting ablation experiments on a relatively simple dataset, Office-31, is not strong. It is recommended to supplement the results of ablation experiments on the Office-Home or VisDA-C. The ablation study should be performed on a more challenging dataset to demonstrate the effectiveness of each component of the proposed method under more complex domain shifts.

### Questions
1) Does diffusion model learning violate or relax the problem setting of SFDA, because the diffusion model pre-training requires source data. Other SFDA methods only use source data to pre-train a source model, but DND uses source data to train a source model and a diffusion model.
2) You maintain ResNet-101 as the encoder G across all datasets, but ResNet-50 is used as the encoder by other SFDA methods on both Office-31 and Office-Home. So are the performance comparisons on Office-31 and Office-Home unfair (Table 1,2)? And whether the results of other methods in Tables 1,2,3 are your reproduced results? Some of which are different from the results in the original paper (such as NRC++, original paper: 88.1, you reported: 87.8).
3) To our knowledge, the training of the diffusion model is very time-consuming, could you conduct a runtime analysis between DND and other SFDA methods (eg. DaC and NRC++)?
4) The target adaptation part in Figure 1 mistakenly divides the inverted triangles into class 0 and the diamonds into class 1.
5) There is an error in the pseudocode of algorithm 1: if the maximum value of t is T in algorithm 1, then z_{\alpha_{T+1}} is obtained, but in reality, the algorithm should end after z_{\alpha_{T}} is obtained.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an approach to source-free domain adaptation using diffusion models. the diffusion models are built using the intuitive idea that "you are close to your neighbors". Experiments on three standard domain adaptation datasets are provided.

### Strengths
Source-fee domain adaptation is a challenging problem. The proposed solution is novel and effective. Experiments validate the effectiveness of the proposed approach. Overall a good paper.

### Weaknesses
I do not see any.

### Questions
How will your approach work for the domain generalization problem?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper highlights challenges in diffusion models for source-free domain adaptation and introduces discriminative neighborhood diffusion (DND) as a solution. 
By leveraging pre-trained source representations, DND facilitates unsupervised clustering through its latent k-nearest
neighbors and significantly enhances performance in SFDA scenarios.
Extensive evaluations demonstrate the discriminative potential and state-of-the-art effectiveness of DND across various benchmark datasets.

### Strengths
- the idea of using diffusion models for source-free domain adaptation sounds interesting and reasonable

- the paper is overall well-written and easy to follow

- the results on three widely used domain adaptation datasets are impressive

### Weaknesses
 - In source-free domain adaptation, the suggested approach demands an extra diffusion model and necessitates the storage of source data features, leading to substantial efforts in the source domain. This situation renders the term "free" somewhat unrealistic, presenting a major concern.

- A recent work [a] also uses diffusion models for test-time adaptation, which is similar to source-free domain adaptation as depicted in a recent survey [b]. Could the proposed method work for single-epoch target adaptation, and how about the comparison?

- Another concern is that only three small datasets are used to evaluate the performance of the proposed method, large-scale datasets like DomainNet [c] are also important. Also, target adaptation under class shift (e.g., partial-set domain adaptation in SHOT (ICML-2020)) is not studied in the experiment.

- Since previous SFDA methods typically adopt the ResNet-50 backbone, the comparisons are not fair in these tables (the proposed method is based on ResNet-101). And how is the diffusion model used in the source domain, would the pre-trained diffusion model bring additional gains?

### Questions
pls see the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies source-free domain adaptation without accessing the source labelled data when conducting target adaptation. Specifically, the authors propose to utilize diffusion models to generate positive key features for facilitating the unsupervised clustering in target adaptation. The whole framework consists of three key components: 1) the source representation learning; 2) diffusion model learning and 3) target model adaptation. Experimental results on several public datasets demonstrate that the proposed model can outperform recent baselines with different gains.

### Strengths
1)	This paper investigates source-free domain adaptation, which is a much more practical setting compared with source-need domain adaptation.
2)	A diffusion model is employed in the domain adaptation framework, which is less explored in the scenario of source-free DA.
3)	Ablation studies are given to show the effectiveness of the proposed components.

### Weaknesses
1)  Although the diffusion models are less explored in the scenarios of source-free DA, the technical contribution of this paper is quite limited. No new diffusion model is proposed to address the domain shift problem in DA and the authors simply use an existing model in this step. The application of a pre-existing diffusion model, without modification, to this problem lacks significant novelty. The core mechanism of how the diffusion model addresses the domain shift is not clearly articulated, and it's unclear how this approach is superior to simply using the source data directly for training a classifier.

2)  As this paper generates examples in the adaptation procedure, it is not clear what are the advantages of using diffusion model compared with other generative models like GAN. There are also lots of baselines that generate samples in the adaptation process and the authors did not discuss and compare with them. See references below.

[1] Qiu Z, Zhang Y, Lin H, et al. Source-free domain adaptation via avatar prototype generation and adaptation. IJCAI 2021.

[2] Li R, Jiao Q, Cao W, et al. Model adaptation: Unsupervised domain adaptation without source data[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2020: 9641-9650.

3)  The source-free setting is a little different from existing work, as this paper uses source data to train the diffusion model. However, existing source free models do not use any source data to train the generative models. This raises concerns about the practical applicability of the method in true source-free scenarios, where access to source data is restricted even during pre-training of auxiliary components. The reliance on source data to train the diffusion model undermines the claim of a source-free approach.

4)  The experimental results are not convincing. The authors directly copy the results from the baselines; however, their network backbones are different. Thus, the comparisons are not fair. For example, in Table 2, baseline DaC’s results are directly cited from its original paper, and it uses the backbone of ResNet-50. However, the authors use ResNet-101 in this paper. I strongly recommend the authors to rerun the experiments. The lack of consistent experimental setup across all methods makes it impossible to draw any meaningful conclusion about the relative performance of the proposed method.

5)  More ablation studies should be given to verify the effectiveness of the proposed diffusion model. What if we directly use the target’s kNN samples as the positive keys? It is not clear how different number of k-nearest neighbors will affect the model’s performance.

There are lots of typos in the paper. The authors need to carefully read and polish the paper. Some of the typos are listed as follows:
“To transition from $z_0$” should be “To transit from $z_0$”.

“We use an SGD optimizer” should be “We use a SGD”.

In equation (1), the norm should be $\Vert \cdot \Vert_2$.

### Questions
1.)	More ablation studies should be given to verify the effectiveness of the proposed diffusion model. What if we directly use the target’s kNN samples as the positive keys? It is not clear how different number of k-nearest neighbors will affect the model’s performance.

2.)	There are also lots of baselines that generate samples in the adaptation process and the authors did not discuss and compare with them. 

3.)	The experimental results are not convincing.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
