# Multi-Student Diffusion Distillation for Better One-Step Generators

- Decision: Reject
- Scores: 3, 8, 3, 3

## Abstract
Diffusion models achieve high-quality sample generation at the cost of a lengthy multistep inference procedure.
To overcome this, diffusion distillation techniques produce student generators capable of matching or surpassing the teacher in a single step.
However, the student model's inference speed is limited by the size of the teacher architecture, preventing real-time generation for computationally heavy applications.
In this work, we introduce \LongMethodName{} (\ShortMethodName{}), a framework to distill a conditional teacher diffusion model into multiple single-step generators. Each student generator is responsible for a subset of the conditioning data, thereby obtaining higher generation quality for the same capacity. 
\ShortMethodName{} trains multiple distilled students, allowing smaller sizes and, therefore, faster inference.
Also, MSD offers a lightweight quality boost over single-student distillation with the same architecture.
We demonstrate \ShortMethodName{} is effective by training multiple same-sized or smaller students on single-step distillation using distribution matching and adversarial distillation techniques. With smaller students, \ShortMethodName{} gets competitive results with faster inference for single-step generation. 
Using $4$ same-sized students, \ShortMethodName{} significantly outperforms single-student baseline counterparts and achieves remarkable FID scores for one-step image generation: $1.20$ on ImageNet-64$\times$64 and \FIDSDADM{} on zero-shot COCO2014. \footnote{Project page: \href{https://research.nvidia.nvidia

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work authors propose a way to distill a pre-trained diffusion model into multiple student where each student is specialized for sub-domain or specific partition of data. To perform distillation authors propose different objectives and also consider smaller architectures for student guided by target from pre-trained diffusion model.

### Strengths
Paper is easy to read and understand the setting, focusing on domain specific student (partition of dataset).
Different objectives and better initialization to perform distillation makes sense and resultant effectiveness is demonstrated empirically. 

Demonstrates finetuning with adversarial training further improves quality of distilled model, which makes sense.

### Weaknesses
Currently this work lacks strong motivation or useful analysis. 
There are previous works like eDiff which specialize different diffusion models per timestep and also works exploring MoE for efficient inferen w.r.t efficiency as motivation more effective pruning, efficient architectures, caching across timesteps etc. have been proposed to achieve smaller models and/or lower latency. 

This work explores splitting student into multiple models w.r.t dataset, while that is practical this work does not provide any novel insights nor significant performance boost.In case of text to image with SD1.5 FID boost only marginal by 0.15 combining all 3 objectives and 4 sets of parameters instead of one, which asks for more memory, more complicated orchestration etc. 

While FID is evaluated, it is unclear how well MSD recovers marginal data distribution i.e., diversity of generation and resultant sampled/recovered distributions (posterior) w.r.t conditional i.e., something like LPIPS_Diversity and aggregated distribution Precision-Recall or other metrics. This helps understand if there is any feature collapse, mode collapse etc?

### Questions
Why is atleast CLIP score not reported on either COCO-2017 or 2014 which could be informative as FID has its deficiencies, could consider HPSv2 or other metrics too for completeness.

What is total training compute required for proposed method? How does it compare to previous methods which do not specialize to sub-sets of data?

To better justify and understand motivation of this work, it might be useful to consider pruning or smaller architecture of already distilled one-step model as a baseline or initialization in their work? How much of training compute can be exploited with better initialization compared to distilling from scratch, such analysis would better benefit community as it currently lacks novel insights to adopt broadly for practical applications too. 

Authors cite EM Distillation as justification to emphasize difficulty of training one-step model from scratch? While it is known from consistency distillation, rectified flow and other works too that training a one-step models is hard not sure why cite distillation method to justify training from scratch as this is also not focus of this work.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a 'Multi-Student Diffusion Distillation' framework. The core idea behind the proposed method stems from Mixture-of-Experts. Particularly, the paper proposes to distill a pre-trained Diffusion model (Teacher model) into multiple  Student model, where each Student is responsible for learning of a subset of conditions. This effectively increases the model capacity by amortizing the set of conditions into smaller subsets where a smaller Student model is responsible for corresponding subset. There are few keypoints pertaining to the proposed method: (a) partitioning/filtering function to partition the set of conditions into subsets, some of the desired features of such function are described in Section 4.1; (b) distillation into multiple Student models, where each Student is responsible for a subset of conditioning variables; (c) support for smaller-sized Student model unlike previous methods which employ same-sized Student model; (d) a teacher score matching phase for smaller-sized Student networks for initialization and better training. The paper primarily deals with Distribution Matching Distillation (DMD) and its extension Adversarial Distribution Matching (ADM). The proposed method SoTA FID on ImageNet 64x64 for one-step generation. The paper is well written and presented. The idea is very intuitive, however, it is interesting to see it working in practice on models like StableDiffusion.

### Strengths
1. The paper is well written and presented. I enjoyed reading the paper. Though MoE is not a new idea, using it for Distillation is new, further using it to accelerate inference is commendable.
2. The idea of using Multiple-Students for distillation for inference time-quality tradeoff is quite intuitive. Moreover, assigning a student to a subset of conditions is a smart choice to increase the capacity of overall model.
3. Authors solve the obvious problem with above choice - initialization from scratch - by introducing an additional TSM stage which gives a good initialization, allowing for further distillation stage.
4. The empirical results are quite strong and encouraging. The proposed method achieves SoTA FID on Imagenet 64x64. Further, it shows encouraging results on distilling StableDiffusion performing better than several one-step generation methods.

### Weaknesses
1. The paper focuses exclusively on DMD (Distribution Matching Distillation) and its extension ADA, which limits the demonstration of the method's generality. While the authors acknowledge this limitation, can the authors demonstrate preliminary results with other distillation approaches, particularly Consistency Distillation [1-3], on simple datasets like Mixture-of-Gaussian. Such experiments would better establish MSD's generality beyond DMD/ADA.
2. There is insufficient clarity regarding the text condition partitioning process in the latent space of the text-encoder during inference.  As I understand, the authors partition the text conditions in latent space of text-encoder. In that case during inference, how is the appropriate Student model selected during inference? Specifically, given that text conditions are not naturally disjoint (unlike ImageNet-style datasets), could the authors provide details on how they determine which Student to use during inference for text-to-image generation? Do they use same text-encoder partitioning technique as in training, or is there a different mechanism?
3. The authors outline several desired properties for the partitioning function in Section 4.1, yet the implemented solution simply uses consecutive classes as partitions (validated in Section 5.4). Could you compare a random partitioning strategy with your current approach? This would be valuable to determine whether the specific partitioning method offers advantages over any balanced data division.
4. The central contribution of the paper is that 'it offers a flexible framework to increase generation speed by reducing student size, and increasing generation quality by training more students. This is seen in Table 3 as well. In fact, in Table 1, the authors show that the Students outperform the Teacher. Does this observation also hold for text-to-image SD models? 
5. Minor:
	1. The partition function notation $F(\cdot) = (\cdot, \cdot | \cdot)$ needs proper definition as it resembles conditional probability notation.
	2. The MSD results appear to use a Student of equal size to the Teacher. Please include results for smaller-sized Students (as used in Fig. 5c) or explain their omission.
	3. Just for clarity: In Table 1, a single Student is used for generation (the Student responsible for a particular prompt), that is why the NFE is 1, right?

### Questions
See Weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the high computational cost associated with multistep inference in diffusion models by focusing on the speed-quality tradeoff in distillation. The authors propose a Multi-Student Distillation (MSD) framework to enhance both generation speed and output quality. In this framework, a teacher model is distilled into several single-step student models, each specialized for generating data under specific input conditions.

### Strengths
Overall, this paper is well-written and easy to follow, with relatively new comparison methods.

### Weaknesses
1. The authors state in Line 257 that 'Conditions within each partition should be more semantically similar than those in other partitions, so networks require less capacity to achieve a set quality on their partition.' However, there are no experiments presented to support this claim. I believe that implementing this idea is challenging and will demand additional computational resources. I recommend including relevant experiments and source code to facilitate a comprehensive review.

2. The statement in Line 15 that 'the student model’s inference speed is limited by the size of the teacher architecture' is misleading, as the inference speed of the student model is independent of the teacher model; the student only depends on the teacher during the distillation training phase. I recommend proofreading the entire paper to ensure clarity and professionalism.

3. The proposed method introduces multiple student models; therefore, comparisons and analyses of the model parameters should be a focal point of the paper.

4. The proposed method leverages adversarial distillation with the expectation of enhancing the distillation effect. However, there is no comparison with standard distillation methods or other variants to validate the adversarial distillation’s anticipated advantages.

5. In the ablation studies section, only a quantitative analysis of the generation effect is presented. I believe that a qualitative analysis should also be included, as the paper aims to enhance generation quality.

6. I can not conduct a comprehensive review of the technological accuracy of this paper, as it is empirical rather than theoretical, and the implementation code is not provided.

### Questions
Please refer to the Weaknesses and Questions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces Multi-Student Distillation (MSD), an approach for diffusion model distillation, which improves existing single-step methods by increasing effective model capacity without added inference latency. MSD uses multiple student models, each optimized for a subset of conditioning inputs, to generate samples in a single step. This framework enhances flexibility by supporting multiple smaller student models to reduce generation time and enables initialization without requiring teacher weights. The authors validate MSD through experiments, achieving improved FID scores on various benchmarks with reduced parameters and comparable generation quality.

### Strengths
+ The organization and writing of the paper are clear, making it easy to understand and follow, and the review of related work is thorough.
+ The discussion on data partitioning is valuable and aligns well with the positioning of the proposed method. I also suggest the authors conduct more comprehensive experimental validation on this aspect.

### Weaknesses
 - The technical novelty is limited, as the approach simply extends the distillation of a teacher diffusion model to multiple student diffusion models. The distillation methods used, DM and ASD, are existing techniques, so the improvement offered by this approach is marginal. The core idea of partitioning the input space and training separate models is not new, and the paper doesn't sufficiently demonstrate how the specific application to diffusion model distillation introduces a significant advancement beyond existing knowledge. The method essentially applies a known strategy to a new domain, but the adaptation lacks substantial technical depth.
- The performance improvement is also marginal. As seen in Tables 1 and 2, the improvement of MSD over DMD2 is small, yet it requires more training and model resources. Although the paper explores smaller student models, Table 1 shows a significant drop in performance, which reduces the practical contribution of this work in terms of lowering inference costs. The gains in FID score are not substantial enough to justify the increased complexity and resource demands of training multiple models, especially when the smaller student models exhibit a notable performance decrease. The trade-off between model size and performance is not adequately addressed, and the practical benefit of using multiple smaller models is questionable given the observed performance drop.

### Questions
Does this method require more model storage for practical deployment? Do the authors have any solutions to address this issue?

### Soundness
2

### Presentation
2

### Contribution
2
