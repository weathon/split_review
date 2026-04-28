# Real-World Benchmarks Make Membership Inference Attacks Fail on Diffusion Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Membership inference attacks (MIAs) on diffusion models have emerged as potential evidence of unauthorized data usage in training pre-trained diffusion models. These attacks aim to detect the presence of specific images in training datasets of diffusion models. Our study delves into the evaluation of state-of-the-art MIAs on diffusion models and reveals critical flaws and overly optimistic performance estimates in existing MIA evaluation. We introduce CopyMark, a more realistic MIA benchmark that distinguishes itself through the support for pre-trained diffusion models, unbiased datasets, and fair evaluation pipelines. Through extensive experiments, we demonstrate that the effectiveness of current MIA methods significantly degrades under these more practical conditions. Based on our results, we alert that MIA, in its current state, is not a reliable approach for identifying unauthorized data usage in pre-trained diffusion models. To the best of our knowledge, we are the first to discover the performance overestimation of MIAs on diffusion models and present a unified benchmark for more realistic evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a straightforward yet powerful benchmark to assess the performance of existing Membership Inference Attacks (MIA) on pre-trained diffusion models within the context of data authorization. The authors identified "overtraining" and "dataset shifts" as two significant limitations of current MIA methods. To address these issues, they developed a benchmark featuring five experimental setups.

### Strengths
- The writing is clear
- The structure is easy to follow
- The paper considered comprehensive comparison with the relate works

### Weaknesses
 - I am unsure about the input for the membership inference attacks. In Lines 113-116, does x refer solely to the image, or is it a combination of the image and its prompt? I recommend that the authors clarify this in the problem setup.

- In Table 1, why does "LDM + CelebA" have $\times$ for both “Over-training” and “Shifted Datasets,” while in the bottom table, "LDM + CelebA" (i.e., the third row) has $\checkmark$ for both? Is this a typo, or have I misunderstood the notation?

- While I appreciate the authors’ efforts in benchmarking MIA methods in practical scenarios, I believe the paper’s analysis of the two challenges, “Over-training” and “Shifted Datasets,” could be more in-depth. For example, I recommend adding an analysis of how shifted datasets impact MIA performance based on the distance of non-members from the target data (e.g., considering extremely close, moderately distant, and far distant non-members).

### Questions
See Weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposed a simple but effective benchmark for evaluating the existing MIA’s performance on the pre-trained diffusion models for the data authorization problem. The authors first found that “overtraining” and “dataset shifts” are two major defects of the existing MIA methods. Then, to overcome the two challenges, the authors proposed a benchmark that incorporates five different experimental setups, where the last three avoids the dataset shifting problem by using members and non-members from the same distributions, and over-training problem by only considering pre-trained models training for 1 epoch.

### Strengths
- Presentation is good and easy to follow.
- The addressed problem is meaningful.

### Weaknesses
 - I am confused about the upper part of Table 1. What do the “✅” and “❌” symbols represent in each entry? Additionally, are “Over-training” and “Shifted Datasets” considered issues in each experimental setup (e.g., is over-training a problem in the DDPM + CIFAR10 setup)? If so, why is over-training necessarily a problem for DDPM + CIFAR10? I believe this only holds when certain factors, like training epochs, are fixed as you reported in the common setting; otherwise, this claim seems overstated.

- Could the benchmark allow for more varied experimental setups—for instance, having no dataset shift but including over-training? A simple example could involve training a DDPM on the CIFAR10 training set and using the CIFAR10 test set as non-members, which would meet the no-shift criterion.

- Furthermore, the concept of “dataset shift” is somewhat unclear to me. The benchmark assumes there’s no distribution shift when two datasets come from the same source. I suggest the authors delve deeper into this by considering metrics to quantify dataset distance (distribution distance), such as the Wasserstein distance.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel approach to assessing MIA on diffusion models by introducing a new benchmark called CopyMark. This benchmark aims to provide a realistic and unbiased environment for testing the effectiveness of MIAs against these models. The study underscores the potential overestimation of MIA effectiveness due to biased experimental setups in previous research and argues for a more nuanced understanding and evaluation of MIAs in practical applications. The paper pinpoints that current MIAs on diffusion models are not trustworthy tool to provide evidence for unauthorized data usage in diffusion models.

### Strengths
1. Good and significant topic. The paper identifies a critical gap in the evaluation of MIAs, offering a novel approach to benchmarking that could reshape how these attacks are studied, and providing valuable insights that can influence the future research.
2. Comprehensive experiment. The experiments conducted are extensive, providing evidence that challenges the overestimation of MIA effectiveness on diffusion models.

### Weaknesses
1. Lack of discussion. The discussion on the practical implications of the findings is somewhat superficial and lacks depth in Section 6, particularly in how these results could influence real-world security strategies.



### Questions
The paper aims to construct a real-world benchmark, pinpointing the current limitation of MIA setups, specifically the unknown distribution of members and non-members in real-world MIAs. It is reasonable that a newly proposed benchmark can cause current methods to yield poor performance. However, I find the discussion lacking in adequately demonstrating how this benchmark accurately reflects real-world settings from my perspective. In my opinion, additional evidence and a more thorough discussion would strengthen this aspect.

In the evaluation setup part, the paper mentions that (d) has a slight data shift but is more minor than other settings. Can you provide further insight into how minor dataset shifts were quantified and their potential impact on the validity of MIA results? It would be beneficial to have a more detailed analysis of how significant these shifts need to be in impacting the effectiveness of MIAs. What thresholds for dataset similarity were considered, and how were they determined?

The paper demonstrates that current MIAs are less effective under realistic conditions on diffusion models. How do you envision these findings being applicable to other types of generative models? Are there specific characteristics of diffusion models that may limit the generalizability of the results? A discussion on this could clarify potential broader applications of your findings.

This paper conducts a comprehensive experiment and concludes that the current MIAs on diffusion models do not perform well in real-world scenarios. However, I think the discussion part is relatively superficial and requires a deeper analysis based on the experimental results. Can you provide more implications and extend the discussion to promote future research?

### Soundness
3

### Presentation
3

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
This paper investigates the evaluation of state-of-the-art membership inference attacks (MIAs) on diffusion models in real-world scenarios. Specifically, it highlights flaws in current MIA evaluations, where over-training and dataset shifts lead to overestimated performance of the membership detection. To address this, the paper introduces a unified benchmark for MIAs on diffusion models, named CopyMark, which is built without over-training, using non-shifted datasets and blind testing. The experiments cover the recent loss-based MIA methods and classifier-based MIA methods, conducted on both defective setups and real-world setups. The results reveal that existing MIAs perform poorly on diffusion models in realistic scenarios.

### Strengths
1. The paper is well-written and easy to follow. It explains the flaws in existing MIA evaluations, i.e., over-training and dataset shifts, and is structured to understand these two problems through quantitative and qualitative analyses. 

2. This paper makes valuable thoughts about the limitations of current MIA evaluations on diffusion models. The significance of the proposed realistic evaluation for MIA is substantial, particularly in the context of AI copyright lawsuits and data privacy.

### Weaknesses
1. The originality of these two flaws, i.e., over-training and dataset shifts, remains a concern. Similar concepts like over-fitting and distribution shifts have been discussed in previous works (Carlini et al., 2022; Maini et al., 2024) on traditional deep learning models and large language models. This paper may potentially adapt the MIA setting to diffusion models while providing more assessments. Specifically, while the paper identifies over-training as a problem, it does not sufficiently explore the nuances of how over-training manifests differently in diffusion models compared to discriminative models. The paper should delve deeper into the specific mechanisms that make diffusion models susceptible to over-training in the context of MIA, such as the impact of extended training on the model's ability to memorize training data distributions versus learning generalizable features. Furthermore, the paper could benefit from a more thorough discussion on how dataset shifts in the context of diffusion models affect the generation process and how this differs from the impact of dataset shifts on classification or regression tasks in traditional deep learning. 

2. Although the paper assesses existing MIA methods on diffusion models, it does not explore possible adjustments to improve MIA performance on CopyMark. For example, how to address the challenges identified on existing loss-based and classifier-based MIA methods and how to achieve better results under realistic scenarios. The paper should investigate potential modifications to existing MIA techniques that could make them more effective in the realistic scenarios presented by CopyMark. This could involve exploring different loss functions, classifier architectures, or data augmentation strategies specifically tailored to the characteristics of diffusion models. The paper should also consider the computational cost and practicality of these adjustments, ensuring that they are feasible for real-world applications. 

3. The evaluation may lack comprehensiveness as a benchmark, as the experiments are limited to loss-based and classifier-based MIA methods on diffusion models. Other types of MIAs, such as likelihood-based MIAs (Hu & Pang, 2023) and MIAs using Quantile Regression (Tang et al., 2024), are not included. The paper should include a broader range of MIA techniques to provide a more complete picture of the strengths and weaknesses of different approaches in the context of diffusion models. This would involve implementing and evaluating likelihood-based methods and quantile regression methods, and comparing their performance to the existing baselines. The paper should also discuss the theoretical underpinnings of these different MIA methods and how they relate to the specific characteristics of diffusion models.

### Questions
1. How do the issues of over-training and dataset shifts differ between diffusion models and traditional deep learning models or large language models? Will the proposed realistic scenarios similarly reduce MIA effectiveness on these other model types?

2. How do MIA methods based on likelihood and quantile regression perform on diffusion models in the proposed realistic scenarios? Will their performance also see a significant reduction?

3. Minor point: a typo “randomlyy” in the third paragraph of section 4.3.

### Soundness
3

### Presentation
3

### Contribution
2
