# Neural Exploratory Landscape Analysis

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 3, 8

## Abstract
Recent research in Meta-Black-Box Optimization (MetaBBO) have shown that meta-trained neural networks can effectively guide the design of black-box optimizers, significantly reducing the need for expert tuning and delivering robust performance across complex problem distributions. Despite their success, a paradox remains: MetaBBO still rely on human-crafted Exploratory Landscape Analysis features to inform the meta-level agent about the low-level optimization progress. To address the gap, this paper proposes Neural Exploratory Landscape Analysis (NeurELA), a novel framework that dynamically profiles landscape features through a two-stage, attention-based neural network, executed in an entirely end-to-end fashion. NeurELA is pre-trained over a variety of MetaBBO algorithms using a multi-task neuroevolution strategy. Extensive experiments show that NeurELA achieves consistently superior performance when integrated into different and even unseen MetaBBO tasks and can be efficiently fine-tuned for further performance boost. This advancement marks a pivotal step in making MetaBBO algorithms more autonomous and broadly applicable. The source code of NeurELA can be accessed at \url{https://anonymous.4open.science/r/Neur-ELA-303C}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an automatic construction method of landscape features for meta black-box optimization (MetaBBO). The proposed approach, termed neural exploratory landscape analysis (NeurELA), trains the attention-based neural network extracting landscape features to improve the MetaBBO algorithms. While existing MetaBBO methods rely on human-crafted landscape features, the proposed NeurELA can automate the design process for landscape features in MetaBBO. The experimental result demonstrates that the proposed NeurELA outperforms existing MetaBBO methods on unseen MetaBBO tasks. In addition, the authors show that fine-tuning process can lead to further performance improvement.

### Strengths
- The motivation for optimizing the feature extractor in MetaBBO is reasonable.
- The technical novelty of this paper is to present automating approach for extracting landscape features in MetaBBO.
- The effectiveness of the proposed NeurELA is experimentally demonstrated for several MetaBBO and BBO problems.

### Weaknesses
 - The proposed formulation seems to be a tri-level optimization problem of training landscape feature extractor, training meta-level policy, and optimizing a target objective function. Therefore, using the proposed NeurELA increases the whole computational cost compared to existing MetaBBO methods.
- Training the landscape feature extractor is performed in a neuroevolution manner. It seems hard to scale for a large neural network as the feature extractor. In addition, it is not clear that the current setting, i.e., optimizing 3,296 parameters for 500 evaluations by the evolution strategy, is sufficient for convergence. The use of a simple evolution strategy, like CMA-ES, might not be the most efficient approach for optimizing the weights of a neural network, especially given the high dimensionality of the parameter space and the limited number of evaluations. This raises concerns about the quality of the learned feature extractor.


### Questions
1. I suppose that the computational cost of the proposed approach is larger than the existing MetaBBO because it requires the training of a landscape feature extractor as the outer loop for MetaBBO. What is the exact computational time/cost for the proposed method compared to existing MetaBBO methods?
1. If the baseline methods can use the same computational budgets, how is the performance gain of the proposed approach? For instance, extra budgets may be used to optimize hyperparameters or to select traditional ELA features in the baseline MetaBBO.
1. Training the landscape feature extractor in the current setting seems challenging because it should optimize the high-dimensional parameters by the evolution strategy. Is there any empirical evidence for the convergence of ES as the outer loop optimizer?
1. What kind of BBO or MetaBBO algorithms can be used with the proposed NeurELA? The authors might assume the population-based BBO algorithms or evolutionary algorithms. Is it possible to combine the NeurELA with other kinds of BBO methods?
1. What is the exact number of dimensions of the NeurELA features in the experiment? What is the impact of the dimensionality of the EeurELA features on the performance?
1. I could not find the definition of the performance metric in the experimental evaluation, e.g., in Figure 3. Could you provide a detailed definition of the performance metric in the experimental results?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Neural Exploratory Landscape Analysis (NeurELA), a novel framework designed to improve Meta-Black-Box Optimization (MetaBBO) by dynamically profiling optimization landscape features through a two-stage, attention-based neural network. Unlike traditional approaches that rely on human-crafted features, NeurELA learns these features automatically in an end-to-end manner. This is aimed at overcoming the limitations of existing Exploratory Landscape Analysis (ELA) methods, such as computational overhead and reliance on expert knowledge. The authors propose a novel neural-network based landscape analyzer, and propose a two-stage attention mechanism: this architecture facilitates robust feature extraction, capable of generalizing to various MetaBBO algorithms without manual adjustments. The novel framework is tested in three MetaBBO tasks against several baselines and ablations.

### Strengths
- The new end-to-end pipeline is (imho) novel and interesting
- NeurELA consistently outperforms the baselines
- Many ablations are performed and thus we better understand the effectiveness of the approach and its parts
- The sharing of the code is appreciated

### Weaknesses
 - The presentation of the paper needs quite some work. Many typos are present and a few paragraphs are hard to read. Overall, the authors need to spend a bit more time in improving the presentation.
- I believe that a more detailed description of the MetaBBO tasks would greatly help the reader understand and appreciate the performance of the proposed framework.
- In Section 4.2 and Fig. 4 it is not clear to what "one epoch" corresponds to. For example, I do not understand how we can compare "ZeroShot" with "Finetune" in the same scale. If I understand correctly, the "ZeroShot" variant just uses the learned $\Lambda_{\theta}$ to select at each generation of the low-level optimizer the appropriate feature vector and configuration. On the contrary, the "Finetune" variant should run the whole meta-learning pipeline. Thus, how can we compare "epochs" of one to the other? We need more explanation here to appreciate the results.
- The computational overhead of NeurELA framework is quite big. Also compared to the original variant ($\Lambda_0$) the gains are not big even when a big number of samples ($m$) is used.

### Questions
See weaknesses..

### Soundness
4

### Presentation
4

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
The paper introduces Neural Exploratory Landscape Analysis (NeurELA), a framework for Meta-Black-Box Optimization (MetaBBO) that replaces traditional, human-crafted Exploratory Landscape Analysis (ELA) features with a fully neural network-based approach. NeurELA employs a two-stage, attention-based neural network trained via a neuroevolution to dynamically profile optimization landscapes, adapting its features in real time. The authors show that NeurELA enhances performance across various MetaBBO algorithms and generalizes effectively to unseen tasks for zero-shot generalization and fine-tuning.

### Strengths
1. Quality: The paper validates the proposed method in detail by answering research questions, not only on the method's performance but also its adaptability, computational efficiency, and generalization capacity. 

2. Clarity: The paper is well-structured, with clear explanations of NeurELA’s architecture, training, and integration within MetaBBO tasks.

### Weaknesses
1. Originality: The proposed work is very similar to Seiler et al., 2024 (Deep-ELA), which also uses multi-head attention as the main component in the architecture. The only difference seems to be that Deep-ELA uses kNN embedding, while the proposed method uses a linear transformation to encode the population information, which is widely used in LLMs to generate embedding from tokens. 

2. Limited comparisons in experiments: The proposed work does not compare to any recent methods, e.g., Deep-ELA. 

3. Limited tasks: Although NeurELA is tested across a variety of MetaBBO algorithms and optimization problems, the experiments lack a detailed analysis of its performance in higher-dimensional optimization scenarios, where many MetaBBO algorithms struggle.

4. Interpretability and feature analysis: Although NeurELA shows promise in dynamically adapting landscape features, there is limited discussion on the interpretability of these features in relation to traditional ELA metrics.

### Questions
1. What's the major difference between the proposed method and Deep-ELA? A more detailed explanation and corresponding experiments and/or ablation studies will help better support the paper's novelty and contribution.

2. Line 479: "This is primarily owning to the two-stage attention architecture in our NeurELA, which can be efficiently computed on GPUs in parallel." Was the training done on GPU? It was mentioned in line 356 that the training uses a Slurm CPU cluster. 

3. The wall time is too short to really tell a difference between algorithms since programming/system processing could have a larger effect if it's in milliseconds. Please consider using a more complicate benchmark or increasing the dimensions.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes Neural Exploratory Landscape Analysis (NeurELA), a framework to replace hand-crafted landscape analysis features in Meta Black-Box Optimization (MetaBBO) with a learned neural network approach.

The key contributions are:
- making the MetaBBO paradigm entirely end-to-end
- A two-stage attention-based neural network architecture for dynamic landscape feature extraction
- A multi-task training framework to learn from multiple MetaBBO algorithms simultaneously
- Demonstration of zero-shot generalization to unseen algorithms and problem sets
- Ability to fine-tune the pre-trained analyzer for specific tasks

### Strengths
- The approach is well-motivated and builds on established MetaBBO literature
- The experimental methodology is rigorous with proper baselines and ablations
- Results demonstrate clear improvements over traditional ELA features
- Comprehensive experiments across multiple MetaBBO algorithms
- Testing on both synthetic benchmarks and real-world problems (protein docking)

### Weaknesses
 - Could better analyze when/why zero-shot generalization fails
- The authors acknowledge training efficiency issues with larger models
- Lacks theoretical justification for why the two-stage attention architecture works well

### Questions
- What is the minimum number of training tasks needed for good zero-shot generalization?
- Could you provide more insight into what features the network learns compared to traditional ELA?

### Nitpicking
- L110: an universal neural landscape analyser... -> a universal
- L176: (Prager et al., 2021b) first proposed... -> wrong citation type, should use \citet instead of \citep
- L318: We hence introduce Ray Moritz et al. (2018), an open-source... -> wrong citation type + you don't introduce Ray, you "employ" Ray
- L350: functiona... -> funtion
- L367: Recall that an MetaBBO task is... -> that a MetaBBO

### Soundness
3

### Presentation
3

### Contribution
3
