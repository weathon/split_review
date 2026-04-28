# Diffusion Active Learning: Towards Data-Driven Experimental Design in Computed Tomography

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 8, 5

## Abstract
We introduce _Diffusion Active Learning_, a novel approach that integrates a generative diffusion model with sequential experimental design to adaptively acquire data for solving inverse problems in imaging. We first pre-train an unconditional diffusion model on domain-specific data. The diffusion model is aimed to capture the structure of the underlying data distribution, which is then leveraged in the active learning process. During the active learning loop, we use the forward model of the inverse problem together with the diffusion model to generate conditional data samples from the posterior distribution, all consistent with the current measurements. Based on the generated samples we quantify the uncertainty in the current estimate in order to select the most informative next measurement. We showcase the proposed approach for its application in X-ray computed tomography imaging. Our results demonstrate significant reductions in data acquisition requirements (_i.e._, lower X-ray dose) and improved image reconstruction quality across several real-world tomography datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Context for those unfamiliar: Computed tomography (CT) acquires multiple X-ray _projection_ images of an object to reconstruct the 3D object. Due to ionizing radiation, there are significant risks associated with acquiring multiple X-ray viewing angles, leading to an undersampled ill-posed inverse problem. Many lines of work aim to reconstruct 3D CT using as few X-ray projections as possible.

Submission 10594 presents an active learning strategy to adaptively sample viewing angles most informative to the reconstruction, to reduce overall X-ray dosage. It first pretrains a diffusion model on fully sampled CTs from the same domain. Then, during inference, it uses the uncertainty of the posterior samples of the diffusion model to adaptively sample new angles.

Experiments are presented on three simulated datasets, where the proposed diffusion-based method compares favorably to other generative models.

### Strengths
- The submission tackles an important yet rarely-trodden inverse imaging problem. 
- The submission is very open with its limitations which is an absolute breath of fresh air in modern papers. For example, L078 gives a much needed disclaimer about the risk of hallucinations from generative models in ill-posed medical image reconstruction problems. The submission’s discussion does a great job of listing limitations as well.
- Overall, the submission is very clearly and straightforwardly presented and was a very easy read.

### Weaknesses
I am open to changing my score and look forward to the rebuttal. As of now I see the following areas that should be addressed,

## 1. The same method was presented in Elata, et al ECCV 2024

The submission has the same idea, methods, and subject matter as [Elata, et al ECCV 2024](https://arxiv.org/abs/2407.08256). **This overlap does not affect my rating** as ICLR’s reviewer guide states that papers that came online after Jul 1 count as contemporaneous and Elata et al first appeared on Jul 11. 

However, could the authors please enumerate the technical differences between the works such that readers can have clear takeaways from this paper? 

For example, the acquisition function is different between the two papers, but their covariance-based acquisition function does seem to be inadvertently benchmarked in the Appendix of this submission as well and they perform identically.

## 2. Limited experiments

My biggest reservation is w.r.t. the submission’s limited experimental depth from the following aspects.

### 2.1. Missing Active CT baselines

While somewhat niche, active learning for CT reconstruction has been studied by previous works as well. For example,
- https://arxiv.org/abs/2006.02420
- https://arxiv.org/abs/2211.01670
- https://dl.acm.org/doi/10.1145/3503161.3548204

Could the authors please describe why these works were not discussed and/or benchmarked against in this submission? If it is feasible, it would be good to see experiments comparing the submission against them. Of course, it is understandable if this is not feasible given the limited discussion period.

### 2.2. Only CT experiments

As the submission itself states, nothing in the submission is particularly specific to CT and it could just as well be used for other sensor-domain reconstruction problems such as MRI. As MRI is widely used, has a clear case for acceleration (patient comfort, time costs, etc.), and MRI active learning is more widely studied than CT active learning, is there a specific reason why it is not studied in this submission?

Further, there are several reinforcement learning methods cited in the paper for MRI active learning. Could any of them be also adapted for CT active learning to form benchmarks for this submission?

### 2.3. No low-dose / sparse-view baseline(s)

The submission motivates itself by potentially reducing CT dosage. Low-dose and/or sparse-view CT reconstruction are immensely popular topics with both learned and hand-crafted priors used. However, the paper does not benchmark against any of the work within this field and instead only benchmarks against other sampling-based methods specifically constructed for this submission. 

While I understand that sampling view prediction and low-dose reconstruction are somewhat orthogonal and can be combined, the method in this paper _requires_ the use of a diffusion model. This then precludes the use of useful low-dose reconstruction methods based on priors such as total variation. 

Could the authors please discuss the differences between the proposed method and existing methods for low-dose reconstruction and whether regularizers such as TV can also be used in the proposed setup?

### 2.4. Only simulated data

While this is endemic across the field, the submission uses _only_ simulated synthetic X-ray projection data in its experiments, simulating it using the same exact forward model as it does in its model. As per the “inverse crime” phenomenon, this can create highly optimistic results and exaggerate differences between methods.

Within CT, there is a small set of datasets that provide both CT and raw _measured_ projection data. For example, please see:
- https://www.cancerimagingarchive.net/collection/ldct-and-projection-data/ (they provide scripts to rebin to fanbeam if necessary)
- https://www.nature.com/articles/s41597-019-0235-y
- https://www.nature.com/articles/s41597-023-02484-6

As detailed above, the paper could have also used active learning baselines for MRI and there are large datasets of real k-space measurements for MRI.

Could the authors please detail why the experiments only use simulated projections?

## 3. Technical contribution

Reductively speaking, the paper can be viewed as a combination of Hard Data Consistency (Song et al 2023) and uncertainty sampling. The submission instead proposes to use “soft” data consistency which is hard DC + early stopping, but it does not perform an ablation of this choice (please correct me if I missed it). As this is the primary technical delta, please perform an ablation if possible.

## 4. Minor
- Runtime requirements are not reported at all. As the paper is motivated by accelerating scans, it should quantify what the additional computational overhead boils down to.
- L462: “on pair” → “on par”

### Questions
- Could the authors please enumerate the technical differences between the submission and Elata24 such that readers can have clear takeaways from this paper? 
- Could the authors please describe why active CT baselines were not discussed and/or benchmarked against in this submission? 
- Why are the experiments limited to just CT if the method is generically applicable?
- Could the authors please discuss the differences between the proposed method and existing methods for low-dose reconstruction and whether regularizers such as TV can also be used in the proposed setup?
- Could the authors please detail why the experiments only use simulated projections?
- An ablation from hard to soft data consistency would be nice.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposed Diffusion Active Learning that integrates a generative diffusion model with active learning to select projection angles. Based on the pretrained  unconditional diffusion model,  the proposed model using the sampled images to select the most informative next measurement.

### Strengths
The proposed method use half or less measurement to achieve the same performance with the compared methods.

### Weaknesses
(1)	Comparison with activate learning method is preferred, such as the method proposed in [1]. Please compare the reconstruction result and inference time  with use the same number of projection angle.
(2)	The experiment is performed with parallel radon transform. More complex setting, such as fan-beam or 3D Cone beam, can verify the effectiveness of the Proposed method.  
(3)	The inference time is a huge disadvantage for you need n round k times sampling and n times full view projection. During, the n\times k sampling, the inversion problem cannot be avoided.  Please discuss potential ways to mitigate the computational cost. Please give  a more detailed analysis of the trade-off between computational cost and reconstruction quality.
(4)	 The improvement of the result may come from the diffusion model.  Comparison with DPS or proposed method without active loop using sparse view projection data, i.e. uniform projection angles (27,15,18 angles), is necessary.  This can  help give the explanation of the benefits of  proposed method  from the active learning component or the diffusion model

### Questions
(1)	Plot the distribution of selected angle of different datasets.
(2)	The shape of the objection has influence of the selected angel,  
(3)	The setting of projection geometry must be given.
(4)	The definition of the notation must be given such as x^* in algorithm 1.
(5)	Testing on real projection data can verify the value of the proposed method.

### Soundness
3

### Presentation
3

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
This paper utilizes a generative model which is then used in the active learning process to choose the next, most informative measurement. First, the authors train an unconditional diffusion model on a specific-dataset. In the second step, samples are generated whereby the diffusion model is conditioned on the measurements. With these samples the next measurement angle is chosen which has the highest posterior variance. According to this the total dose and acquisition time can be reduced.

### Strengths
* The paper contains a really good explanation of the novel approach. 
* The approaches, results and limitations of already existing work is well discussed. 
* Reducing the dose or measurement time during the CT measurement is an essential problem.
* Novel combination of diffusion models with active learning.
* The results are well discussed and compared to different baselines.

### Weaknesses
 * Pre-training of the diffusion model is necessary. Further steps depend on this, and the computational cost of training such models can be substantial, potentially limiting the practical applicability of the approach, especially when datasets are small or frequently changing. The dependence on a pre-trained model also introduces a potential bottleneck in the workflow.
* The diffusion model is highly dependent on the trained data. This dependence raises concerns about the generalizability of the method to datasets that differ significantly from the training data. The model's performance could degrade considerably when applied to samples with different characteristics or distributions.
* The diffusion model could introduce undesirable biases. This is a critical concern, as biases in the generative model could lead to systematic errors in the reconstruction process, potentially skewing the results and leading to inaccurate conclusions. The nature and impact of these biases need to be carefully evaluated and mitigated.
* How to get the posterior distribution could be discussed in more detail. The method for obtaining the posterior distribution, which is crucial for the active learning strategy, is not sufficiently elaborated. The specific steps, approximations, and assumptions involved in this process should be clearly explained to ensure reproducibility and allow for a thorough understanding of the approach.

### Questions
* Why are medical images not suited for this approach? In the paper it is stated because they are acquired very fast and therefore sparse but the goal is to have fewer measurements while keeping the resolution high?
* How does this model perform with samples that are slightly out of the distribution the diffusion model was trained on?
* Samples can be destroyed when a high dose or a long-time measurement is taken. How would this approach reconstruct the image? Would it automatically reduce the distortions which could be undesirable?
* Why are the smaller images first cropped and then rescaled? The distribution changes when rescaling images.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a framework for adaptive-sampling in the context of limited-angle X-ray/computed tomography (CT). Using measurements collected from a subset of angles, a diffusion model is used to generate approximate posterior samples. Then, the forward model is applied to each posterior sample to obtain the corresponding measurement at different angles. The uncertainty is represented as the variation in the measurements at each angle. Finally, the angle with the largest variation is selected as the next angle to collect measurements for. The paper shows that the active learning approach provides higher PSNR with fewer measurement steps compared to uniform sampling.

### Strengths
- The paper tackles an important problem in the field of limited-angle CT. Long-scan times and high radiation doses clearly pose hurdles in all applications from medical tests to chip analysis.
- The solution is well-motivated. By identifying the angles with the most uncertainty, the proposed method promises to select the next angle with the most information. 
- The experiments demonstrate notable gains in PSNR using the active learning approach versus the uniform sampling.

### Weaknesses
 - The contributions of the paper were not explicitly clear to me. From the experiments, there were two independent variables that were changed: 1) the method used to generate samples and 2) the use of the active learning procedure. Is the main contribution the use of a diffusion model for the sampling procedure? Or is the main contribution the active learning procedure? Or is the combination of the two the main contribution? The diffusion sampling is based on an existing approach (Song et al. 2023), and it seems like the active sampling approach is based on existing uncertainty sampling. Thus, it is difficult to see where the novelty/contribution of the paper lies. It would be helpful if you could explicitly stated the contributions in a set of bullet points in the introduction. 
- The structure of the experimental section is confusing, particularly section 4.2. There is not any context as to what the methods (SWAG, Bootstrap, etc). are used for. Before introducing them, it would be helpful to identify where they are utilized in the framework. It was not clear to me until the results section that they would be substituted in for the diffusion sampling. Also, "Comparison Methods" would be a better suited title for the subsection.
- In a similarly light, the paragraph from lines 468-473 lacks context. It is unclear which Table/Figure the analysis is discussing.
- I'm not fully convinced about the practical advantage of the active sampling with the diffusion approach. As stated in the conclusion, diffusion models are inherently computationally heavy and slow. Thus, while you may need fewer measurements overall, the collection of each measurement would take much longer. For example, if it takes x times as long to choose the next angle than it does to just sample the next uniform angle, then you would want to show that your method allows you to collect at least x times fewer samples.
- In Line 300-301, it would be useful to use a different variable rather than t in order to avoid confusion with the diffusion time steps.

### Questions
- In Eq 3, why do you take the mean of the posterior samples first and then apply the forward operator? Would it make more sense to take the mean of the measurements (i.e. apply the forward operator first and then take the mean)?

### Soundness
2

### Presentation
2

### Contribution
2
