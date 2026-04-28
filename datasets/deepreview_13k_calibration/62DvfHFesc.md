# Longitudinal Latent Diffusion Models

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 6, 5

## Abstract
Longitudinal data are crucial in several fields, but collecting them is a challenging process, often hindered by concerns such as individual privacy. Extrapolating in time initial trajectories or generating fully synthetic sequences could address these issues and prove valuable in clinical trials, drug design, and even public policy evaluation. We propose a generative statistical model for longitudinal data that links the temporal dependence of a sequence to a latent diffusion model and leverages the geometry of the autoencoder latent space. This versatile method can be used for several tasks - prediction, generation, oversampling - effectively handling high-dimensional data such as images and irregularly-measured sequences, needing only relatively few training samples. Thanks to its ability to generate sequences with controlled variability, it outperforms previously proposed methods on datasets of varying complexity, while remaining interpretable.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes the Longitudinal Latent Diffusion Model (LLDM), a general framework for modeling longitudinal data. LLDM incorporates a diffusion process in the latent space and generates samples with a co-trained LVAE. Experiments on three datasets with different modalities demonstrate LLDM's effectiveness.

### Strengths
1. LLDM presents a general framework for modeling longitudinal data applicable across various modalities.
2. The motivation for the LLDM framework is novel and well-conceived.
3. Experiments are well-structured and thoughtfully designed.

### Weaknesses
1. The paper is confusingly written, particularly in the methods section, and does not meet the standards expected of a polished academic article.  
The authors include unrelated information without a clear structure or logical flow, as exemplified below:
   - **Undefined task objective:** In Line 169, the authors mention probabilistic modeling of $ p(x^i_1,...,x^i_{T_i}|z^i_j) $, yet they do not explain how this relates to the task objective. They should define the task as a generative model conditioned on the latent variable $ z^i_j $ extracted from preceding observations $ (x_1^i,...,x_j^i) $. The current formulation lacks clarity on whether the model aims to generate future sequences, impute missing data, or perform other tasks, and how the proposed probabilistic modeling aligns with these goals.
   - **Unclear method structure:** The authors should clarify the model by clearly explaining how VAE, LDM, and LVAE interact and how they are interconnected within the model. The paper lacks a cohesive explanation of how these components are integrated, making it difficult to grasp the overall architecture and data flow. For instance, it's unclear how the latent space of the VAE is utilized by the LDM and subsequently by the LVAE, and how these different latent spaces are related.
   - **Ambiguous statements:** Numerous unclear statements in the methods section could lead to misunderstanding, such as “Weights are shared across all j” (Line 167), “only keep the last observations’ embeddings” (Line 191), and the inconsistency in using “latent” versus “embedding” for $ z_j^i $. The statement about shared weights needs more detail: are the encoder and decoder weights shared, or only specific layers? The explanation regarding the last observations' embeddings is also vague: does this mean the LDM is only trained on the final time step, and if so, how does it capture the temporal dynamics? The inconsistent terminology further adds to the confusion, making it difficult to follow the technical details.
   - **Non-vector graphics:** Figures 1 and 2 are not vector graphics, which makes them difficult to read.
   - **Non-academic language:** The paper includes informal language, for example:
     - Line 180: “we **want** to model”
     - Line 232: “we **can** sample”
     - Line 318: “**unfortunately**, Kanaa et al. (2021) **do not provide any code**”
   - **Other issues:**
     - Line 169: unclear notation with “$ (x_j)^i_j $”.
     - Lines 212-213: redundant phrase “we set”.
     - Line 254: missing definition of $ \theta_{\text{diff}}^* $.

   Given these issues, the paper reads more like a course project than a mature academic article, with significant room for improvement in readability.

2. The LVAE method lacks motivation and theoretical support.  
   In Section 3.3, the authors propose LVAE to align the diffusion process over the *diffusion timeline* with the generation process over the *real timeline*. However, they do not provide sufficient motivation or theoretical justification for this approach. Any theoretical backing or empirical evidence supporting LVAE’s effectiveness would strengthen the work. Furthermore, the concept of aligning the diffusion timeline with the real timeline is introduced abruptly in the methods section, without prior discussion, making LVAE’s motivation difficult to grasp. The authors should elaborate on what specific advantages this alignment provides, and why this is a better approach than alternative methods for modeling temporal dependencies. The lack of a clear explanation makes the LVAE seem ad-hoc and less convincing.

### Questions
1. How does the diffusion process align with the real timeline?  
   In LVAE, the authors introduce the (un-noisy) latent $ z_i^j $ into both the forward and reverse diffusion processes $ q $ and $ p_{\theta_{\text{diff}}^*} $. This is unclear. For example, in a diffusion process, $ q(z_{t+1}|z_t) $ requires a noisy $ z_t $, which follows a different distribution from $ z_i^j $ (corresponding to $ z_0 $). However, the authors use $ q(z_l^i|z_{l+1}^i) $ in the forward process, where initially the un-noisy $ z_j^i $ is incorporated. The reverse process encounters the same issue. Could the authors clarify the reasoning behind this design?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This manuscript proposes a latent variable model for generating (potentially high-dimensional) longitudinal data. The proposed method combines 1) a standard static variational autoencoder (VAE) for learning a lower dimensional variational approximations (or embeddings) of the high-dimensional data objects as well as generating them high-dimensional data objects from low-dimensional embeddings, and 2) a diffusion model in the latent space that, given the embedding for a specific time point, can generate the embeddings for the previous or next time points. The proposed method can be used for longitudinal data generation, missing data imputation, prediction and over-sampling of time.

### Strengths
Longitudinal data arise naturally in numerous fields and applications, where the healthcare represents arguably the most important application field.  Consequently, longitudinal data modeling is an important task in probabilistic machine learning and generative modeling. Longitudinal data analysis is extensively studied, and recent machine learning literature has also proposed novel methods that contribute especially to high-dimensional data modeling. Apart from recent generative models for video generation, such as sora, fewer diffusion-based models have been proposed for longitudinal data: the proposed method has novelty and originality in that regards, although the proposed method essentially combines two main building blocks, standard VAE and DDPM diffusion models. While this manuscript has some novelty, I also have several concerns about the quality of the work in terms of validity of the method, and quality of the presentation could be also improved - overall lowering the significance.

### Weaknesses
General design choices.  In Introduction, authors motivate the importance of longitudinal data modeling by listing important applications in healthcare, treatment response modeling/estimation and econometrics. All these applications, as well as generally all applications that involve longitudinal data collections, are fundamentally problems where additional predictors for each unit (or individual, or patient, or customer) are known, and therefore a widely accepted goal is to develop conditional generative models, whereas the proposed method belongs to the class of unconditional models. 

Related works. Authors describe related works that cover many different modeling frameworks. In VAE framework, Gaussian process based VAE models have been extensively studied. While they are generally conditional models, they can be obviously applied without any conditioning too (e.g. only time as considered in this work). This manuscript list only two recent papers on GP based VAE model, but the literature features even more recent models: 

1. Ashman et al, Sparse gaussian process variational autoencoders. 
2. Jazbec et al, Scalable gaussian process variational autoencoders.
3. Zhu et al, Markovian gaussian process variational autoencoders. 
4. Tran et al, Fully Bayesian autoencoders with latent sparse Gaussian processes. 

ODE / SDE models. Authors claim that latent ODE models are completely deterministic in the latent space. That is not true. Latent variables in latent neural ODES are, well, latent variables that are unobserved.  Latent neural ODE field has also developed rapidly and the citations authors have are outdated.  It is difficult to list all relevant papers, but her are some, that I think would be directly relevant here:

5. Lagemann et al, Invariance-based Learning of Latent Dynamics. 
6. Iakovlev et al, Latent neural ODEs with sparse bayesian multiple shooting. 

Latent SDE models are fewer. Authors site an important paper that develops scalable and stable gradients for latent neural SDEs. Unfortunately, the citation is to an older workshop paper. At least the final published version of paper applies the model to 50-dimensional data. Also other papers have been published on neural SDEs.  The proposed method is closely related to latent neural ODEs and SDEs, but also to GP based VAEs, so these references are important. 

Experimental results. The baseline methods are weak and not SOTA. Authors claim that other models cannot do oversampling. For example, latent neural ODEs and SDEs are continuous in time and can inherently be evaluated, and decoded back to the data domain, at any time point. Similarly, GP based models can be evaluated at any time. 

Method. Figure 1 summarises the proposed model. The presentation lacks a clear, unified description of the underlying generative model, and its variational inference method, and for this reason it is not straightforward to see if the proposed method is a valid model in probabilistic modeling sense. For example, objective is described in Algorithm 1. Validity of the objective needs to be clearly demonstrated. As an example, the first term that looks like the standard reconstruction loss of the ELBo is now evaluated using the decoded samples. Regarding the description of time points in rows 211-> I doubt if this makes works for irregular sampling.  Sampling from a generative model is typically implemented by following the steps of the generative model.  I could not follow authors reasoning why the sampling needs to be modified to be geometry aware: if authors want to use geometry aware sampling, aren’t they training a geometry aware generative model that they would use when sampling.


### Questions
Row 175: Equation 6 indicates that the data points are independent. Either the equation is wrong, or the description of the method is incomplete.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the Longitudinal Latent Diffusion Model (LLDM) which leverages a latent diffusion process to model the temporal dependencies between observations in a sequence. ​ This approach allows for the generation of synthetic longitudinal data, which can be used for prediction, generation, and oversampling tasks. ​ LLDM is particularly effective in handling high-dimensional data, such as images, and can generate sequences with controlled variability, outperforming previous methods in terms of diversity and fidelity. ​ The model's capabilities are demonstrated through experiments on synthetic and real-world datasets, showing its robustness and versatility in generating realistic longitudinal trajectories.

### Strengths
- The introduction of a latent diffusion process within a VAE framework to model temporal dependencies in longitudinal data is novel and interesting. ​
- The model is capable of effectively managing high-dimensional data. ​
- The model outperforms previous methods in terms of generating diverse and high-fidelity synthetic data, as evidenced by lower FID scores.
- LLDM demonstrates robustness to missing data, maintaining performance even when a significant portion of the training data is missing. ​
- The model's latent space is interpretable, reflecting the characteristics of the training dataset and providing insights into the data structure. ​
- LLDM excels in future prediction tasks and can generate oversampled sequences, increasing the frequency of observations in a sequence.

### Weaknesses
 - The model requires significant computational resources for training, which might not be accessible to all researchers or practitioners, especially those working with limited hardware.
- The experiments are conducted on a limited number of datasets, which may not fully represent the diversity of real-world longitudinal data. Additional validation on a wider range of datasets would strengthen the claims of the paper.
- The randomness in the diffusion process is great for creating varied samples, but it can also lead to some inconsistency in results. This can be an issue for applications where steady, reliable outputs are essential. In tasks that track changes over time (like monitoring tumors in medical imaging) keeping things consistent is key. For instance, in oncology or radiology, doctors look at scans over time to see if a lesion or tumor is growing or shrinking. If the images vary too much because of the generation process, it could hide small but important changes, making it tougher to get a clear picture of the patient’s condition.

### Questions
- In lines 169-172, the authors mention that the joint likelihood is not factorizable because the observations ( $x_j^i$ ) are not independent when conditioned on a single latent variable ( $x_j^i$ ). ​ However, you state that when all the latent variables are observed, the observations become conditionally independent. ​ Could you please elaborate on why the assumption of joint likelihood not being factorizable holds in the first case and why it becomes factorizable when all latent variables are observed? 
- On line 187, the meaning of “a set of $\sum_{i=1}^{N} T_i$ is not clear? Are the timesteps summed up? Why?
- In general, the LDM is supposed to generate a sample within a trajectory; please explain the rationale for training the LDM in isolation and how this approach contributes to the overall performance of the LLDM.
- How does the complexity of LLDM compare to simpler models in terms of implementation and computational cost? Are there any specific scenarios where the added complexity of LLDM is justified over simpler models?

### Soundness
2

### Presentation
2

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
The authors add longitudinal component to traditional diffusion models. This requires modeling sequences of images, but unlike in say video, the observations can be far apart in time. The sequence dimension in general is expected to be sparse. The authors tailor a specific pipeline to the setting: the "inner loop" (image generation essentially) is a standard VAE, and the "outer loop" - sequence dimension - trains diffusion in the latent space of the first VAE. The two are combined using so-called Longitudinal VAE (LVAE), which uses the same architecture as the first stage VAE and uses both forward and backward diffusion.

### Strengths
I find the setting compelling and useful for real world applications. I like how every design choice is well motivated. Anecdotal results in Figure 2 look persuasive, which makes me believe that the proposed method does work.

### Weaknesses
My main concern is about the benchmarks. The authors admit that they couldn't make some of the relevant models work. The ones for which the numbers are reported still appear undertuned: in Table 3, for instance, the proposed model exhibits a strong - and sensible! - pattern, while the other 2 models show no pattern that I can discern. This tells me that the other 2 models fail to capture the underlying interaction, which in turn makes me doubt their validity as benchmarks. Specifically, the lack of any discernible pattern in the baselines' results suggests a fundamental flaw in their training or architecture for this specific longitudinal task. The fact that the proposed model shows a clear, expected pattern only exacerbates this concern, as it highlights the inadequacy of the chosen baselines. It's not simply a matter of the baselines performing worse; they seem to be failing to learn the core longitudinal dynamics at all, making any comparison questionable.

### Questions
Fixing benchmarks is the biggest priority in my opinion. But I would also be interested in the usual details of diffusion model training, like the numerical stability issues. Reported training times are very fast on a not particularly powerful GPU - I would be curious in hearing even a speculation for why. HW could be the reason why the authors couldn't make the competitive benchmarks work. So maybe getting on a more powerful machine would help what is a purely empirical paper.

### Soundness
3

### Presentation
3

### Contribution
3
