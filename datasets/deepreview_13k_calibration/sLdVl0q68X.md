# NuwaDynamics: Discovering and Updating in Causal Spatio-Temporal Modeling

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 8, 1

## Abstract
Spatio-temporal (ST) prediction plays a pivotal role in earth sciences, such as meteorological prediction, urban computing. Adequate high-quality data, coupled with deep models capable of inference, are both indispensable and prerequisite for achieving meaningful results. However, the sparsity of data and the high costs associated with deploying sensors lead to significant data imbalances. Models that are overly tailored and lack causal relationships further compromise the generalizabilities of inference methods. Towards this end, we first establish a causal concept for ST predictions, named  NuwaDynamics, which targets to identify causal regions in data and endow model with causal reasoning ability in a two-stage process. Concretely, we initially leverage upstream self-supervision to discern causal important patches, imbuing the model with generalized information and conducting informed interventions on complementary trivial patches to extrapolate potential test distributions. This phase is referred to as the discovery step. Advancing beyond discovery step, we transfer the data to downstream tasks for targeted ST objectives, aiding the model in recognizing a broader potential distribution and fostering its causal perceptual capabilities (refer as Update step). Our concept aligns seamlessly with the contemporary backdoor adjustment mechanism in causality theory. Extensive experiments on six real-world ST benchmarks showcase that models can gain outcomes upon the integration of the NuwaDynamics concept. NuwaDynamics also can significantly benefit a wide range of changeable ST tasks like extreme weather and long temporal step super-resolution predictions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel causal framework called NuwaDynamics for spatio-temporal (ST) prediction tasks. The key idea is to leverage self-supervised reconstruction tasks to identify causal regions in the input data, and perform interventions on non-causal regions to expose the model to a broader distribution of data. The framework consists of two main stages: 1) Causal patch discovery, where a Vision Transformer is trained on a reconstruction task and attention maps are used to localize causal patches. 2) Causal model update, where environmental patches are modified through interventions and used to train the downstream model. Experiments on 6 benchmarks demonstrate improved performance over strong baselines.

### Strengths
1. This paper is well-organized and clearly written.
2. Introducing causality concepts into spatio-temporal modeling is novel.
3. The motivation is clear and reasonable.
4. Visualizations demonstrate improved detail and extreme weather perception.
5. The experiments across multiple datasets are thorough.

### Weaknesses
1. It seems that the computational complexity is high due to generating many intervened sequences. The paper lacks a detailed analysis of the computational overhead introduced by the intervention process, especially concerning the number of augmented sequences and their impact on training time and memory usage. A more rigorous analysis, including a breakdown of time complexity for both the causal discovery and model update phases, would be beneficial.
2. Lack of ablation studies to validate design choices. The paper would benefit from more extensive ablation studies to justify the specific design choices, such as the selection of the Vision Transformer for causal patch discovery, the specific intervention strategy (mixup), and the method for aggregating attention maps. The impact of these choices on the overall performance and the sensitivity of the model to these design parameters should be thoroughly investigated.
3. Except for the KTH dataset, the performance gains are relatively low. While the paper demonstrates improvements on several datasets, the magnitude of these gains, particularly on datasets other than KTH, is not substantial. The paper should provide a more in-depth discussion of why the proposed method is more effective on some datasets than others, and whether there are specific characteristics of the KTH dataset that make it particularly suitable for this approach. The lack of significant improvements on other datasets raises questions about the general applicability of the method.
4. Lacks of the comparison on computational complexity. The paper does not provide a direct comparison of the computational cost of the proposed method with existing approaches. A detailed comparison, including training time, memory usage, and inference speed, would be necessary to assess the practical viability of the method.

### Questions
1. What are the limitations of current attention map methods for identifying causal regions?
2. How sensitive is the approach to the choice of interventions?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper established a causal concept for spatio-temporal predictions. In particular, it firstly identifies causal regions at the Discovery step. It then augments non-causal patches at the Update stage. By doing so, the model is able to see a broader potential distribution of data, achieving improved downstream performance. Extensive experiments show that the proposed model can benefit many existing frameworks on various tasks.

### Strengths
**Originality:** This paper established a causal concept for spatio-temporal predictions and introduced a novel philosophical framework. Its causal perspective is interesting and original. It is also addressing an important challenge faced by AI community which is the interpretability and generalizability. 

**Presentation:** This paper is well written. The flow of the paper is smooth and easy to follow. Figure 1 and Figure 2 are very helpful to illustrate the central idea of the paper. 

**Experiments:** the experiments are extensive, covering a wide range of backbones and tasks. The experimental analysis is well organized with key questions and itemized observations.

### Weaknesses
 **The experiments are insufficient.** The performed experiments are focused on the comparison between the performance of an original backbone and the performance of adding NuWa. There is a lack of comparison to SOTA performance on the evaluated tasks. Besides, it is also important to compare to other data-augmentation methods (even though they are not using causality), which is also missing in the paper.  

Besides, there is a lack of evaluation on the causal discovery accuracy. Causal discovery always requires a large amount of data to ensure accurate discovery of causal relationships, and it can suffer from highly imbalanced data. How does your model address this issue as you are particularly interested in such regime?

### Questions
Please see the weakness section for my major concerns. In addition,

1.	How many augmented samples are required to achieve reasonable performance? Does the downstream performance sensitive to the number of augmented samples?
2.	What if we directly perform data enhancement using the attention map? 
3.	Can you show the visualization of the identified causal regions and the augmented samples?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper explores the application of deep learning to dynamical systems and proposes a new philosophical framework called "NuwaDynamics", which aims to mine data for causal patterns to enhance the explanatory and generalization capabilities of models.  The approach is divided into two phases: Discovery, which identifies the causal components of the data, and Update, which applies the causal model to downstream tasks.  In addition, NuwaDynamics enhances the model's performance in sparse and extreme situations.  Experimental results in the article show that the framework achieves excellent results in several benchmark tests.

### Strengths
(1) A conceptually and technically highly innovative paper which seamlessly integrates causal theory with spatio-temporal data mining. The integration of causal theory's environment discovery and augmentation into the popular vision transformer's attention map is ingenious. Coupled with a straightforward mixup augmentation, it achieves a very refined alignment. From my perspective, NuwaDynamics has the potential to revolutionize how models recognize causality in ST data mining realm. This may provide a new approach to solving such problems (data scarcity and the high cost of deploying sensors). 

(2) The paper reads very well, and hardly has any errors or inconsistencies. Information is provided at the right point, is complete and accurate. The split between main paper and supplementary material is good. The narrative and exposition flow well. Meanwhile, the paper is well-structured, I appreciate its visual aids.

(3) Providing a causal intervention perspective for data augmentation seems interesting. In terms of practical implementation, utilizing attention scores without introducing additional complex designs seems both simple and effective. Additionally, I believe the backdoor adjustment mechanism proposed by the authors serves as a robust theoretical foundation. This contributes significantly to enhancing generalization, especially in out-of-distribution scenarios.

(4) Baselines are strong, relevant, discussed well and evaluated fairly. A large number of analytic experiments complete the main findings. Meanwhile, experimental setups are presented accurately and consistently, at an adequate level of detail.

### Weaknesses
(1) The paper does not seem to make it clear exactly how the process of obtaining the importance rankings in the patches is done, and it is hoped that the authors will add that detail.

(2) In referring to the fact that DL methods often forgo an explicit understanding of the rules of physics, the practical implications and potential risks of this sacrifice are not explained in detail. More discussion or explanation might have given the reader a better understanding of the consequences of this choice.

### Questions
(1) Despite the extensive experiments presented in this paper, I'm still curious about the effectiveness of this method on certain spatio-temporal datasets, such as [1-2]. These real pedestrian movement datasets could offer a more convincing validation of the model's efficacy.  However, an intriguing question arises: given that Nuwa's environment is populated with causal patches, is its performance reliable on pedestrian movement datasets that have clear divisions between causal and non-causal segments?


[1] Pedestrian detection: A benchmark  **Conference on Computer Vision and Pattern Recognition**
[2] Human3. 6m: Large scale datasets and predictive methods for 3d human sensing in natural environments **IEEE transactions on pattern analysis and machine intelligence**

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper delves into the spatio-temporal challenges inherent in earth sciences, encompassing areas like meteorological forecasting and urban computing. Given the hurdles of data sparsity and imbalance, the authors put forth a novel causal prediction framework dubbed "NuwaDynamics". Operating through two phases - "Discovery" and "Update" - this paradigm pinpoints causal regions within datasets and endows the model with causal reasoning prowess. The authors also substantiate their methodology with proofs drawn from causal theory and employ a myriad of experimental results to demonstrate its efficacy across various spatio-temporal benchmark tests, especially in tasks like extreme weather forecasting and long-term temporal predictions. In a nod to fostering collaboration and transparency, the code from this research has been shared with the public, marking a valuable contribution to the open-source arena.

### Strengths
1. The paper is well-written and exhibits a commendable layout; the motivation is intuitive and clear.

2. It is interesting to employ ViT and Mixup in spatiotemporal data for causal environmental discovery and augmentation, and the work can potentially expand the model's latent observational space in many scarce scenarios.

3. Extensive experiments demonstrate the effectiveness of the framework. The authors introduced architectures tailored for both ViT and non-ViT, while also including control experiments across frameworks such as RNN and CNN. Comparisons across multiple mainstream tasks, including transfer learning and super-resolution prediction, further demonstrates its capabilities in tasks like extreme event prediction.

4. Detailed theoretical validation based on causal manipulation is provided to demonstrate the feasibility of the framework. Interestingly, in real-world scenarios, the author doesn't explore all possible environments but instead introduces partial perturbations, which conveniently addresses the computational constraints and limited data availability in practice.

### Weaknesses
1. I am concerned about whether there are clear guiding principles for environmental augmentation. Especially when it comes to the mixup technique, is it possible to automatically adjust the fusion hyperparameters of each environmental patch based on a specific dataset? If this cannot be achieved at the moment, I hope the authors will offer potential solutions in their section of future work .

2. I also have a keen interest in environmental perturbation methods. In fact, environmental perturbation can be considered a form of data augmentation. I wonder, are there any generative methods in computer vision (CV) that can be integrated into this? If the answer is affirmative, I hope the authors delve deeper into this in the "Related Work" and "Model" sections.

3. The experimental section of the paper is rich in content, and I am particularly interested in spatio-temporal system modeling. Current research literature mainly focuses on datasets with lower resolution, for example, roughly 256x256 in size. I hope the authors can consider more experiments to explore whether these methods remain competitive on high-resolution datasets. If the authors can achieve superior results on higher-resolution datasets, I might consider further raising my score.

### Questions
See weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
