# CPSample: Classifier Protected Sampling for Guarding Training Data During Diffusion

- Decision: Accept
- Scores: 5, 3, 5, 5

## Abstract
\noindent
    Diffusion models have a tendency to exactly replicate their training data, especially when trained on small datasets.  Most prior work has sought to mitigate this problem by imposing differential privacy constraints or masking parts of the training data, resulting in a notable substantial decrease in image quality.
    We present CPSample, a method that modifies the sampling process to prevent training data replication while preserving image quality. 
    CPSample utilizes a classifier that is trained to overfit on random binary labels attached to the training data.
    CPSample then uses classifier guidance to steer the generation process away from the set of points that can be classified with high certainty, a set that includes the training data.
    CPSample achieves FID scores of 4.97 and 2.97 on CIFAR-10 and CelebA-64, respectively, without producing exact replicates of the training data.  
    Unlike prior methods intended to guard the training images, CPSample only requires training a classifier rather than retraining a diffusion model, which is computationally cheaper. 
    Moreover, our technique provides diffusion models with greater robustness against membership inference attacks, wherein an adversary attempts to discern which images were in the model's training dataset.
    We show that CPSample behaves like a built-in rejection sampler, and we demonstrate its capabilities to prevent mode collapse in Stable Diffusion.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes Classifier-Protected Sampling (CPSample), a novel technique to prevent diffusion models from generating training data  duplicates, apart from previous methods such as rejection sampling or other sampling methods that occurs during training phase, CPSample allows the diffusion model to steer away from generating training samples during test time, resolving the problem of privacy leakage.

### Strengths
1. The proposed method presents interesting facet and novelty where a classifier is utilized in remembering the statistics of training distribution and acts as guidance to steer away from the training data.
2. The planned experiments are great in terms of studying the effect of CPSample in a holistic manner. The three different experiments demonstrate different aspect of CPSample which is helpful for understanding the empirical effect.

### Weaknesses
 1. The presented theoretical study seems to be not proven much in terms of CPSample. Specifically, it is not demonstrated as to why assumption 3 holds well empirically as stated in the paper. Furthermore, given the intractable estimation and sometimes large values of Lipschitz constant, I wonder if that would make the possible $\delta$ extremely small which in terms renders the theory results in vain?
 2. Some more experiments on MIA could be carried out to effectively evaluated the information loss caused when CPSample. Particularly, papers such as [1, 2] have devised new MIAs tailored to the settings of diffusion models which also conforms to the past settings in MIA.  It would be great to see if CPSample could also withstand these newly devised attacks.

### Questions
1. As mentioned in the first point of weaknesses, it would be great if the authors could elaborate more on the the third assumptions either empirically or theoretically along with the $\delta$ problem mentioned.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method to prevent the generation of training data during the inference on diffusion models. The way to obtain the result is by modifying the sampling process in diffusion models. The method leverages a classifier that is trained and forced to overfit on random binary labels assigned to the training data of diffusion models. The method uses “classifier guidance” to prevent the generation process from returning the training data points.

### Strengths
1. The paper tries to solve a very important problem: how to prevent the diffusion models from generating the training samples.

### Weaknesses
1. This method is very simple: “Overfit a classifier on random binary labels assigned to the training data and use this classifier during sampling to guide the images away from the training data.” Does it still require training the classifier on the large training dataset of diffusion models? What if we do not have access to the training data any longer?
2.	As stated in Section 2.1: “Currently, the state-of-the-art for guided generation is achieved by models with classifier-free guidance (Ho & Salimans, 2022). However, since CPSample employs a classifier to prevent replication of its training data,” Thus, the CPSample method is not applicable to the SoTA diffusion models. 
3.	The proposed CPSample method is very similar to the AMG guidance method from Chen et al. 2024. It is claimed that AMG requires access to the training data of a diffusion model. How is the classifier trained for the proposed CPSample method without requiring access to the training data? (as stated at the end of Section 3.1)
4.	The qualitative results in Figure 3 clearly show the degradation of quality in the generated images between DDIM and CPSample (especially for the LSUN Church dataset). Additionally, Image C in the last row for the CPSample shows the complete degradation in the quality of the generated images. 
5.	What is the overhead of the method in terms of the inference time? How long does it take to train the classifier? How is the classifier trained? 
6.	The paper only compares the FID score of the CPSample to other methods, however, no comparison is presented in terms of the reduction in the generation of the training data points.

### Questions
1.	The abstract states: “CPSample achieves FID scores of 4.97 and 2.97 on CIFAR-10 and CelebA-64, respectively, without producing exact replicates of the training data.” What is the baseline? What model was it checked on? Without this background and some reference, these results do not have any meaning.
2.	The paper should cite another work that applied DP to diffusion models [1].
3.	Introduction: this method “fortifies against some membership inference attacks” This statement is rather too vague and it should be clearly stated what the goal of the method is. The defenses should not prevent some attacks that can infer the training images because the adversary would simply use the attacks that work and are not prevented by the proposed method.
4.	The fact that better FID scores are achieved than other methods has to be presented with some reference. Is it the trade-off that the higher performance stems simply from the worse protection?
5.	The background of the paper takes 2 pages. It is way too long and should be limited to a single page. For example, DP is not used in this paper so there is no need to provide this background section. Moreover, providing the formula for cosine similarity is really too trivial. The statement about the empirical results from this paper in Section 2.2 is very surprising: “Empirically, for CIFAR-10, we observed that images with similarity scores above 0.97 were nearly identical, whereas for CelebA, the threshold was approximately 0.95, and for LSUN Church, images with similarity above 0.90 were sometimes, though not always, nearly identical.” The same is repeated in Section 4.1.
6.	The definition of Differential privacy does not come from Dwork & Roth 2014. The first paper that proposed the mathematical framework was [2].
7.	Why is only a single membership inference attack used by Matsumoto et al. 2023a? The latest “evaluation of state-of-the-art MIAs on diffusion models reveals critical flaws and overly optimistic performance estimates in existing MIA evaluation” [3]
8.	Why are only the binary labels used and not more labels in the CPSample?
9.	From Section 4.1: Figure 1 does not show the most similar pairs of samples and fine-tuning data points.

**References:**

[1] dp-promise: Differentially Private Diffusion Probabilistic Models for Image Synthesis. Haichen Wang, Shuchao Pang, Zhigang Lu, Yihang Rao, Yongbin Zhou, Minhui Xue. USENIS 2024.

[2] Calibrating noise to sensitivity in private data analysis. Dwork, C., McSherry, F., Nissim, K., & Smith, A. In Theory of Cryptography: Third Theory of Cryptography Conference, TCC 2006. 

[3] Real-World Benchmarks Make Membership Inference Attacks Fail on Diffusion Models. Chumeng Liang, Jiaxuan You 2024: https://arxiv.org/abs/2410.03640

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Diffusion models exhibit a tendency to memorize training images and reproduce these training images during inference, which can pose significant privacy concerns. To address this issue, this paper introduces a sampling strategy (CPSample) guided by a trained classifier. This classifier evaluates the memorization score of current generated image and rectifies the sampling trajectories to diverge from the training images. By adjusting the guidance scale, the proposed method ensures that the generated images possess a memorization score approximating 0.5, thereby mitigating the risk of replicate generation.

### Strengths
1. The issue of replicate generation in diffusion models is critical, and there is an urgent need for a scalable solution to address it.
2. The concept of explicitly training a classifier to measure the memorization score is novel, and subsequent experiments have demonstrated its efficacy.

### Weaknesses
1. The scalability of the strategy to train a classifier is a primary concern. Given that current text-to-image diffusion models, such as Stable Diffusion and Pixart, are trained on large-scale datasets scraped from the Internet, is it a feasible solution to train an overfitted classifier on a large scale dataset? The claim that the parameter scale linearly with the increase in resolution and the size of the dataset is not well supported. The scaling law observed in other deep learning models, such as LLMs, suggests that the relationship between data size and model parameters is not always linear. Therefore, the feasibility of training an overfitted classifier on extremely large datasets, such as LAION-400M or LAION-5B, remains questionable, and more experiments are needed to demonstrate the limitations of this approach.

2. The proposed method assumes that the training member set is available. However, this assumption does not always hold. Specifically, the training member sets of certrain text-to-image diffusion models, such as Pixart, are not publicly accessible, therby limiting the applicability of the proposed approach. The introduction should include a more detailed discussion of practical scenarios where this assumption fails, and a limitation section should elaborate on this issue.

3. While the proposed CPSample method effectively mitigates replicate generation, it also exhibits side effect on the generated images as it manipulates the sampling trajectory. For example, in Figure 4, the generated image by CPSample does not align with the input prompt and sometimes will generate corrupted results. In contrast, although rejection sampling faces challenges with resampling, it tends to produce images that are more closely aligned with the input prompt. Furthermore, the core design of this paper is the classifier, which is utilized to captures the boundary between the member set and hold-out set. However, no experiments are provided to validate the choice of a classifier for this task, given that there are many plausible approaches to capture this boundary. Experiments comparing the classifier approach with other methods, such as training a classifier to differentiate between the member set and hold-out set, or training an overfitted diffusion model to provide memorization gradients, are necessary to justify the proposed approach.

4. There are many typos in notations of DDPM, for example, $\alpha_t \rightarrow \bar{\alpha}_t$ in Equation 2.1&2.2, Line 146. Please check this through the whole manuscripts to ensure the consistency and accuracy of all notations.

5. The experiments on similarity reduction have been conducted on low-resolution and small-scale datasets such as Cifar10 and CelebA. For these datasets, the diffusion model can verbatim memorize each pixel of the training samples. However, in more practical scenarios, diffusion models tend to memorize only the rough structure of the training sample and can only reproduce similar patterns. Consequently, the current experiments (Section 4.1) may not adequately demonstrate the effectiveness of the proposed method for similarity reduction. Structure replication, such as duplications in IP or the art style, is also a significant privacy concern. Additional experiments on large-scale diffusion models are necessary to further validate the method.

6. The current experiments have been mostly conducted on unconditional diffusion models. To fully evaluate the effectiveness of CPSample, additional experiments on conditional diffusion models, such as text-to-image diffusion models, should be conducted to assess whether CPSample can accurately align with the given condition. The current qualitative results are very limited, and more results should be provided, including class label to image models and edge to image models (controlnet). Furthermore, the hyperparameters ($\alpha$, $s$) for CPSample seem dependent on each sampling. How to define these hyperparameters for each sampling?

### Questions
1. In my opinion, the trained overfitted classifier is designed to estimate a memorization score and captures a boundary between the member set and hold-out set to provide a guided gradient. However, various alternative methods exist for estimating this boundary or providing a similar memorization gradient. For instance, training a classifier to differentiate between the member set and hold-out set, or training an overfitted diffusion model to provide memorization gradients, are both plausible approaches. Therefore, why choose to assign random 0/1 labels to the member set? (The reasons provided in Line 238-244 is not very convincing for me) 

2. The scalability of CPSample to diffusion models with larger member sets is uncertain. Current experiments only provide limited examples (Section 4.2). Additional examples are required to further demonstrate the effectiveness of the proposed method. Furthermore, the hyperparameters ($\alpha$, $s$) for CPSample seems dependent on each sampling. How to define these hyperparameters for each sampling? 

3. The experiments on similarity reduction have been conducted on low-resolution and small-scale datasets such as Cifar10 and CelebA. For these datasets, the diffusion model can verbatim memorize each pixel of the training samples. However, in more practical scenarios, diffusion models tend to memorize only the rough structure of the training sample and can only reproduce similar patterns. Consequently, the current experiments (Section 4.1) may not adequately demonstrate the effectiveness of the proposed method for similarity reduction. Additional experiments on large-scale diffusion models are necessary to further validate the method.

4. The current experiments have been mostly conducted on unconditional diffusion models. To fully evaluate the effectiveness of CPSample, additional experiments on conditional diffusion models, such as text-to-image diffusion models, should be conducted to assess whether CPSample can accurately align with the given condition.

### Soundness
3

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
4

### Summary
This paper proposes a rejection sampling method that avoids diffusion models from replicating training data in generated contents. The main idea is to use classifier guidance dependent  on the label of training data / hold-out data. This gets the sampling process away from the region of training data and then preventing diffusion models from generating training data.

### Strengths
1) The method is sound and solid. It implements the idea of rejection sampling by using classifier guidance. This achieves training-free prevention of training data replication.

2) Experiments show that the proposed method can avoid training data replication even if there training setup leads to potential over-fitting. This proves the effectiveness of the proposed method,

### Weaknesses
1) Motivation: the main weakness of this paper lies in its motivation. As shown in existing research, training data replication is not a common phenomena in real-world pre-trained diffusion models. Most training samples are even unable to be inferred as member by membership inference attacks in Stable Diffusion, while the exception ones can be handled case by case. While the proposed method still degrades the generation performance as well as the diversity (potentially), it seems uneconomical to deploy the proposed method on any pre-trained diffusion models. Since privacy issues only happen in pre-trained diffusion models, the significance of the proposed method is moderate.

2) Computation cost & Generalizability: As stated in the paper, we need to train a classifier on all training and some hold-out examples. This could be significantly computationally costly without promising generalizability, since no one has trained such a classifier before. In fact, the training of the classifier in the paper only includes less than 2 thousands images. However, the training datasets of pre-trained diffusion models consist of billions of images. It leaves doubts whether a classifier can effectively give guidance based on these large-scale datasets.

3) OOD generation (minor): One potential drawback, as shown in Figure 4, is that the proposed method may generate images with contents quite different to the description of the text.

### Questions
1) Can you show how your method performs on large-scale datasets?

### Soundness
3

### Presentation
2

### Contribution
2
