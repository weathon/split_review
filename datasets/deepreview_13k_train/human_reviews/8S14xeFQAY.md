# Segmenting the Unknown: Discrete Diffusion Models for Non-Deterministic Segmentation

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
Safety critical applications of deep-learning require models able to handle ambiguity and uncertainty.
We introduce discrete diffusion models to capture uncertainty in semantic segmentation, with application in both oncology and autonomous driving.
Unlike prior approaches that tackle these tasks in distinct ways, we formulate both as estimating a complex posterior distribution over images, and present a unified solution that leverages the discrete diffusion framework.
Our contributions include the adaptation of discrete diffusion for semantic segmentation to model uncertainty and the introduction of an auto-regressive diffusion framework for future forecasting.
Experimental evaluation on medical imaging data and real-world future prediction tasks demonstrates the superiority of our generative framework over deterministic models and its competitive performance compared to methods specific to these domains separately.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an approach to apply discrete diffusion models to model uncertainty for both semantic segmentation and future forecasting semantic segmentation. The authors evaluate their method on both simulated data an real data and claim competitive performance.

### Strengths
The work mostly clearly contextualizes and motivates its approach in relation to prior work. The work cleverly transfers existing methods to new problems. \
The method is evaluated for multiple settings, showing that it is versatile and not restricted to a single problem setting, and for multiple datasets. The selection is motivated well. \
The supplement provides thorough information regarding experimental details.

### Weaknesses
A number of results with better performance for the LIDC dataset are missing, giving the impression that the results are sota (see Table 1 in [1]) 
A prior work [1] has previously proposed the use of discrete diffusion for handling uncertainty in semantic segmentation. This somewhat limits the novelty, however I think the two works can still be counted as concurrent work. 
A more detailed qualitative evaluation for Cityscapes would have been interesting. Where does the method perform well, where does it show weaknesses, does it learn something about the movement of other entities in the scene, where does the performance improvement from 1 to 100 samples evaluation come from? 
The work shows in the car simulator dataset that the method does generate a variety of future scenarios, however it is not shown for the more complex Cityscapes dataset. Showing it quantitatively is of course difficult with the existing data, however it is also not clearly shown qualitatively. 
For scenarios like the mentioned "Is there a scenario in which the child crosses the road?" to be applicable real-time performance is essential. The inference time for the method on the Cityscapes data is not mentioned. 

If there is not a lot of ambiguity in the CityScapes dataset, maybe it is not a good choice for this paper? 
I am still not sure what a mean FDE of 68 or 11.9 is supposed to tell me. Yes, higher is worse, but beyond that? Even for the deterministic model with a mean of 68 the median is still ~2. In addition, why is it better to choose a wrong exit that is closer than one that is further away? (wrt to the question how well the ambiguity is modeled) Which wrong exit is chosen has a strong impact on the mean. 
Wrt Chen et al. (2022a), panoptic segmentation is in the end just semantic+instance, not using the instance part should be trivial. It would still be interesting if there are pros and cons to your approach vs their approach or if there is no difference.

### Questions
Questions 

Regarding the motivating example, how is it defined which rectangle is "rectangle 1" and which is "rectangle 2"? In other words, given an image, how can I distinguish the two categories of "the rectangles have different classes"? Secondly, what are the two categories the deterministic model predicts? \
[1] was made public earlier this year. Can you please elaborate on the differences to the work at hand? \
Chen et al. (2022a) (referenced by you) was made public last year. While they do not show results regarding handling ambiguity, at first glance it seems to be applicable. Does the approach at hand have specific properties that would make it more advantageous for this task compared to their approach? \
For clarification, in 4.2.2: For each car in each validation example 10 samples are generated. The best of the 10 samples is selected according to FDE. 84% of those FDE values are less then 2 (a "hit"). And then the mean of the best FDE values (hit and miss) is computed. Is this correct? I am not sure the mean is very informative then as the distribution seems to be quite skewed.
 
General Notes 

There seems to be quite a bit of interesting information in the supplement that is never referenced in the main paper, e.g., the MO results for Cityscapes, making it difficult for the reader to be aware of it. \
In Sec 3.1/2 it is not always fully clear to me what parts are from Austin et al. and what parts are adaptations by the authors.

Most issues have been addressed satisfactorily in the Discussion Phase, thus I've updated my rating from 5 to 6.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces discrete diffusion models to capture uncertainty in semantic segmentation, with application in both oncology and autonomous driving. Unlike prior approaches that tackle these tasks in distinct ways, the proposed method formulates both as estimating a complex posterior distribution over images, and presents a unified solution that leverages the discrete diffusion framework. The contributions include the adaptation of discrete diffusion for semantic segmentation to model uncertainty and the introduction of an auto-regressive diffusion framework for future forecasting. Experiments have been conducted on both medical imaging data and real-world future prediction tasks to demonstrate the superiority of the proposed generative framework over deterministic models and its competitive performance compared to methods specific to these domains separately.

### Strengths
- The idea of presenting a unified solution for both future prediction and medical image segmentation is interesting, by leveraging diffusion models.
- This paper proposes the first method to model the uncertainty of predictions using discrete diffusion models in semantic segmentation.
- The proposed method is quite straightforward to follow.

### Weaknesses
 - The experimental section is limited. I expect to see the results of more baselines. For example, how the proposed method is compared with GAN-based methods? Specifically, given that GANs are also generative models, a comparison is needed to understand the relative strengths and weaknesses of the proposed diffusion approach versus GANs in this segmentation context. The lack of comparison with GANs, especially in the context of ambiguous segmentation, is a significant gap.
- There are lots of works regarding uncertainty estimation in (semantic) segmentation [1,2,3], just list a few. I would like to see the authors do a thorough review of these kinds of methods and provide a comprehensive comparison with the proposed method. The current literature review is insufficient, and a more thorough analysis is required to position this work within the broader field of uncertainty-aware segmentation. The absence of a detailed comparison makes it difficult to assess the novelty and contribution of the proposed method.
- Beyond the segmentation evaluation metrics, I am expecting the see more empirical results regarding uncertainty estimation. Some of the metrics can be found in [4,5]. The paper needs to demonstrate the quality of the uncertainty estimates, not just the segmentation performance. Metrics such as calibration error, expected calibration error, or sharpness of the predictive distribution should be included to validate the uncertainty modeling capabilities of the proposed method. Without these metrics, it is difficult to assess the quality of the uncertainty estimates.

### Questions
N/A

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces discrete diffusion models to address ambiguity and uncertainty in semantic segmentation, specifically for applications in oncology and autonomous driving. The authors propose a unified solution for two tasks: future prediction and medical image segmentation. This solution leverages the discrete diffusion framework to model segmentation annd prediction uncertainty. They also introduce an auto-regressive diffusion framework for future forecasting. Experimental evaluations were conducted on a Lung Cancer medical Imaging Dataset (LIDC) and two future prediction tasks, demonstrating the efficacy of their proposed generative framework.

### Strengths
- The paper presents a unified approach to handle future prediction and image segmentation, reducing the need for distinct solutions for each task.

- Experimental evaluations show that their model consistently outperforms equivalent deterministic models in all tasks. Additionally, the proposed generative framework surpasses existing VAE-based methods on LIDC and is on par with state-of-the-art methods on Cityscapes future prediction.

### Weaknesses
 - There is a heavy reliance on existing ideas, with incremental adaptation to an existing discrete diffusion model. The paper simply employs input conditioning via concatenation to adapt the generative model for segmentation. Moreover, autoregression for future prediction is just conditioned on past segmentations, leaving out crucial technical details that would illuminate the depth of the contribution.

- The paper did not explicitly define the type of uncertainty being captured, leaving ambiguity between aleatoric (data) and epistemic (model) uncertainty.

- While the paper compares its approach to deterministic methods, it lacks comprehensive comparisons with existing work in uncertainty quantification in semantic segmentation.

- Results show samples of the posterior, yet uncertainty is not explicitly quantified.

### Questions
- Given the lack of clarity on the type of uncertainty captured, can the authors specify whether it is aleatoric or epistemic uncertainty?

- The title suggests the capability to segment unknown classes. Can the authors clarify this claim?

- The paper discusses the potential for forcing diversity in the sampling process. Can the authors elaborate on possible methods to achieve this?

- Why is there a lack of comprehensive comparisons with existing uncertainty quantification methods in semantic segmentation?

- With the heavy reliance on existing ideas, can the authors provide further technical details or novel contributions that differentiate their approach from previous work?

- Considering the importance of understanding and reporting both types of uncertainties, why was this aspect not heavily emphasized in the paper? Furthermore, can the authors shed light on how uncertainty is being evaluated and calibrated?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
