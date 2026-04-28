# POMONAG: Pareto-Optimal Many-Objective Neural Architecture Generator

- Decision: Reject
- Scores: 3, 3, 5, 5, 6

## Abstract
Neural Architecture Search (NAS) automates the design of neural network architectures, minimising dependence on human expertise and iterative experimentation. While NAS methods are often computationally intensive and dataset-specific, employing auxiliary predictors to estimate architecture properties has proven extremely beneficial. These predictors substantially reduce the number of models requiring training, thereby decreasing overall search time. This strategy is frequently utilised to generate architectures satisfying multiple computational constraints.
Recently, Transferable Neural Architecture Search (Transferable NAS) has emerged, generalising the search process from being dataset-dependent to task-dependent. In this domain, DiffusionNAG stands as a state-of-the-art method. This diffusion-based method streamlines computation, generating architectures optimised for accuracy on unseen datasets without the need for further adaptation. However, by concentrating exclusively on accuracy, DiffusionNAG neglects other crucial objectives like model complexity, computational efficiency, and inference latency -- factors essential for deploying models in resource-constrained, real-world environments.
This paper introduces the Pareto-Optimal Many-Objective Neural Architecture Generator (POMONAG), extending DiffusionNAG through a many-objective diffusion process. POMONAG simultaneously considers accuracy, the number of parameters, multiply-accumulate operations (MACs), and inference latency. It integrates Performance Predictor models to estimate these secondary metrics and guide the diffusion gradients. POMONAG's optimisation is enhanced by expanding its training Meta-Dataset, applying Pareto Front Filtering to generated architectures, and refining embeddings for conditional generation. These enhancements enable POMONAG to generate Pareto-optimal architectures that outperform the previous state-of-the-art in both performance and efficiency.
Results were validated on two distinct search spaces -- NASBench201 and MobileNetV3 -- and evaluated across 15 image classification datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces POMONAG, an extension to DiffusionNAG that applies a many-objective diffusion model to optimize neural architecture generation for many-objective optimization. By incorporating additional performance predictors for hardware efficiency metrics such as number of parameters, multiply-accumulate operations (MACs), and inference latency, POMONAG aims to provide a more balanced approach to architecture optimization across accuracy and computational efficiency. Experiments validate POMONAG’s efficacy on two major CNN search spaces (NASBench201 and MobileNetV3).

### Strengths
The motivation to extend DiffusionNAG to a many-objective setting is valid and POMONAG does so by incorporating both accuracy and efficiency metrics like latency and MACs, which are critical for resource-constrained environments. The paper provides extensive experimental comparisons with DiffusionNAG, including evaluations across multiple datasets and search spaces, which helps demonstrate the general applicability of POMONAG.
Balancing the different objectives being optimized is also very important in my opinion. The authors do so by proposing a pareto front filtering and stretching subroutine.

### Weaknesses
I have the following main concerns related to this submission, which I believe were crucial in the final decision:

- **Incremental Contributions**: Although POMONAG claims to extend DiffusionNAG’s capabilities by addressing more objectives, the modifications appear incremental and lack substantial theoretical advancement. More specifically, I see the adaptation of diffusion models to accommodate multiple objectives, as described in section 3.1, more as a technical modification rather than a novel conceptual framework. I would recommend the authors to reiterate over their methodology and pinpoint the main contributions of their approach.

- **Experimental Evaluation**: The benchmarks that POMONAG was evaluated contain only CNN spaces. It would be beneficial for the paper if the authors would demonstrate the efficacy of POMONAG in Transformer search spaces, such as the one from HW-GPT-Bench [1]. Most importantly, in the multi-(many-)objective experiments, the proposed method is not compared to any baseline. I would recommend the authors to add baselines in their experimental evaluation and report hypervolume indicator together with the individual objective values, as well as the search time. Ultimately, I would also be interested in visualizing the pareto front plots in the main paper. As for baselines, you can find a non-exhaustive list of simple ones in SyneTune (https://syne-tune.readthedocs.io/en/latest/getting_started.html#supported-multi-objective-optimization-methods). Finally, the experiments lack a thorough ablation study that demonstrates the impact of POMONAG’s unique contributions independently of DiffusionNAG’s foundational structure. 

- **Clarity and Presentation**: The paper seems to have a somehow fragmented structure, making it challenging for readers to follow the main contributions and crucial take-away points. Equations are not thoroughly explained, and there is a heavy reliance on citations from DiffusionNAG rather than a detailed elaboration of POMONAG itself, making the paper not self-contained. One major point here, which I have also pointed out to the AC, is that the authors have used a smaller font size starting from page 4. The guidelines clearly state that the maximum page limit is 10 and that means 10 pages with the default font size, not a smaller one. I suggest the authors that in future submissions they adhere to the submission guidelines.


-- References --

[1] Sukthanker et al. HW-GPT-Bench: Hardware-Aware Architecture Benchmark for Language Models. In NeurIPS 2024 DBT

### Questions
Moreover, I have the following questions:

- Can the authors provide more theoretical or empirical justification for the scaling factors in the Pareto Front Stretching process? How sensitive is the model to these values?

- Can the authors provide more detail on the architecture sampling process, dataset splits, and hyperparameter tuning methods used in the experiments? This is particularly important for the performance predictors.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This study improved DiffusionNAG by introducing a multi-objective approach which modifies DiffusionNAG's reverse diffusion process as a reverse diffusion guidance process.  Other than accuracy, #params, MACs and inference latency are also considered in the multi-objective metrics.  The proposed method POMONAG has been tested on NASBench201 and MobileNetV3 with 15 image classification tasks, showing better performance than DiffusionNAG and a series of other methods.

### Strengths
The motivation of this study, introducing multi-objective evaluation in NAS, is commendable as a task in reality is often not just about accuracy.  Other metrics should be considered simultaneously as well.

The writing is easy to follow. 

It is nice to see equations with highlights of different colours.

### Weaknesses
**First of all**, the work claims to be on Pareto multiobjective search for architectures.  However, that point is not obvious from the paper.  
* What are the benefits of using the proposed POMONAG?  
* How can a Pareto front be generated and utilized? Need to explicitly demonstrate how POMONAG generates and utilizes Pareto fronts.
* How can users select architectures from the Pareto front according to their needs or under different circumstances?  Show examples of such selection based on different priorities, for example prioritizing small-size architectures for portable devices or focusing on latency reduction etc.  
* It seems non-dominated sorting is absent. Explain how non-dominated sorting is incorporated or can be incorporated in POMONAG.
* In its current form, the paper reads like a combination or integration of single-objective evaluations rather than a multi-objective evaluation.  The equation of POMONAG at Line 209/210 is a linear combination of four objectives.  Please clarify if the linear combination of objectives is intended as a scalarization approach.  If so, discuss its limitations.
--- 
**Secondly**, the performance of POMONAG appears better than DiffusionNAG and other methods shown in the paper.  However many SOTA methods, especially zero proxy methods are missing.  Their reported performance is similar or even better, for example, SWAP-NAS by Peng et al, ICLR'24, ZiCo by Li et al, ICLR'23, MeCo by Jiang et al, NeurIPS'23.
* Include a comparison with these SOTA methods. If a direct comparison is not possible, explain why and discuss the limitations of the current evaluation.
* Discuss how POMONAG's approach differs from or improves upon zero-proxy methods. 

--- 
**Thirdly**, the computational cost aspect of POMONAG is weak.  The section "Generation and Training Time" should be better presented.  The method requires a diffusion generation phase which takes extra time.  That itself is a disadvantage.  Also timewise, POMONAG cannot claim superiority as recent methods mentioned earlier are faster.
* Present a detailed table comparing computational costs (including generation and training time) of POMONAG with other methods, including these zero proxy methods mentioned above.  Seemingly these methods are faster. If POMONAG is indeed slower, discuss potential optimization strategies.
* Discuss the trade-offs between the additional diffusion generation phase and the method's performance gains.  Justify why the additional computational cost might be worthwhile.
---   
**Other points:**
 
The link at Line 091 is showing.  Also, including the code and dataset would be helpful for the assessment.

--- 

Fig 1 is not quite readable.  The figure further makes POMONAG look like three single-objective tasks combined rather than a four-objective task.
* Improve readability, especially on the right-hand side.
* Better illustrate the integration of all four objectives in a unified multi-objective framework if these objectives are not just simply added together (*see the first part of my comments*).
 * Provide a clearer visual representation of how POMONAG handles the trade-offs between objectives (*see the first part of my comments*).
--- 
Line 186, the term noisy architecture is not explained.  
* Provide a brief explanation of what "noisy architecture" means in this context and how it relates to the diffusion process in DiffusionNAG.
--- 
Equations and their connection to the processes/algorithms are not numbered and not clearly explained.   
* Number all equations for easy reference
* Clearly label the equation at Line 183. Is this equation for the Reverse Diffusion Process? Clarify that connection.
* Provide a brief explanation of the symbols used in this equation and other key equations.
* Explain the purpose of transformation s_θ(A_t,t).
* Explain the exact differences between the Reverse Diffusion Process and the Reverse Diffusion Guidance Process.
--- 
Line 280, "Four are dedicated to the respective estimation of accuracy, parameters, MACs, and inference latency of noisy architectures during the diffusion phase. " 
* Explain why not use these four metrics for denoised architectures as well.
* Justify the point that the denoised architecture uses accuracy as its only metric.
--- 

Explain the reason why POMONAG utilises Vision Transformer ViT-B-16 instead of other models (Line 286).

--- 
It is good to see the Spearman correlation experiment.  That is very important in NAS studies.  However, for a thorough comparison of correlation, it should be done on a set of tasks like NAS-Bench-Suite-Zero (Krishnakumar et al. NeurIPS'22).
* Perform a similar thorough comparison comparing correlations on different tasks using different search spaces.
--- 
In lines 400-402, the same latex problem appeared several times, ` not ' for the left quotation marks, Accuracy, Params, MACS ... \
* Fix these formatting issues.
--- 
Validity, uniqueness and novelty are nice metrics for a population of solutions but not so critical for tasks that focus on accuracy and speed.  What is the point of being excellent on these points but without good accuracy and speed?
* Explain the significance of these three additional metrics: validity, uniqueness and novelty.
* Show example how these measures can help improve the quality of generated architectures in POMONAG.

### Questions
See above as the questions are mostly addressing the weakness of this paper.

### Soundness
2

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
3

### Summary
This paper is a direct extension based on DiffusionNAG, which can deal with multi-objective optimization in NAS. These objectives include accuracy, the number of parameters, multiply-accumulate operations (MACs), and inference latency. This motivation is good and natural, and the authors expressed their work clearly, from the motivation to the experiments results. Some details need to be clarified.

### Strengths
This paper introduces the ParetoOptimal Many-Objective Neural Architecture Generator (POMONAG), extending DiffusionNAG through a many-objective diffusion process. POMONAG simultaneously considers accuracy, the number of parameters, multiply-accumulate operations (MACs), and inference latency. The experiments validate the performance of the proposed model.

### Weaknesses
1, The multi-objective optimization problem formulation in this work can be given first, which then can be solved by the proposed weighted factors in the reverse diffusion process. But maybe the authors can consider other ways to sovle this. For example, using four single reverse diffusion process each targeting one factor, as DiffusionNAG did, then using multi-objective optimization for further trade-off may also work well.

2, The theoretical analysis should be strehghen. One objective to many objective is a breakthrough, but such process needs more analysis or discussion. Current work lacks such in-depth thinking. 

3, Several predictors are needed in this work, but the detailed information these predictors are missing.

### Questions
I have several questions about this work.

1, How to decide the scaling factors? Since the intervals are [1000,5000], [100,500], [100,500], [100,500], and the values seesm to be integer, then the whole factor space equals 4000 * 400 * 400 * 400, which is quite huge. And the authors present one setting for NASBench201 and other experiments, respectively, so I am wondering whether there is some method or strategy to choose such factors? 

2, This work extends the basic motivation of DiffusionNAG, which is rather good and natural. Such extension include three more factors, including number of parameters, number of MACs, and the inference latency. But I am curious that, how about the performance of POMONAG if just considering adding one factor? 

3, From one factor, say, accuracy, to three more factors seems strenghening the proposed POMONAG, but my question is, the working mechanism of DiffusionNAG and POMONAG the same different? Although the two diffusion processes consider different factors, which is the obvious difference, but the analysis or discussion is important to interpret this issue.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents the POMONAG method to generate neural architectures in the multi-objective manner. Specifically, the overall framework of POMONAG is designed based on that of DiffusionNAG, in order to achieve better performance in terms of number of parameters, MACs, and inference latency beyond the accuracy. There are four key parts designed to achieve this goal, i.e., the many-objective reverse diffusion guidance, the meta-dataset, the score network and performance predictors, and the pareto front filtering and stretching. The experimental results in NAS-Bench-201 and MobileNetV3 search spaces demonstrates the effectiveness of the proposed method.

### Strengths
1) The idea the overall framework of the proposed POMONAG method is simple and easy to understand. 
2) The details of the method and experiments are clearly stated. 
3) Generating neural architectures in the multi-objective manner is an important research topic.

### Weaknesses
1) My major concern is about the motivation of this work. Specifically, there are four objectives considered, i.e., the accuracy, the number of parameters, MACs, and the inference latency. However, the last three objectives do not demonstrate conflict relationship. For instance, the smaller number of parameters seems certain to lead to lower inference latency. In this case, the necessity for adopting multi-objective optimization is limited. 
2) The novelty of the proposed method needs further discussion. Specifically, the proposed method seems to build on DiffusionNAG with the cooperation of the multi-objective optimization. It seems that the POMONAG is just a simple combination of these methods. More discussions in terms of the seminal contribution of POMONAG is needed. 
3) How the hyperparameters $k_{\phi}$, $k_{\pi}$, $k_{\mu}$, and $k_{\lambda}$ determined? It is suggested to provided more details in terms of the hyper-parameter study for these hyperparameters. 
4) The search cost of POMONAG is not well presented. In the pipeline of POMONAG, I think the pre-training process, the training of the score network, and the training for the performance predictors will introduce much additional search cost beyond the architecture generation. However, I cannot find any details about the overall search cost and the search cost for the above components. 
5) I am curious about why only one trained architecture is enough for POMONAG? Maybe more discussions or analysis are helpful to give more insights for this point. 
6) Lack of experimental results on more challenging tasks (i.e., the classification accuracy on ImageNet-1K). More results on such datasets are helpful to enhance the experiments.

### Questions
Please see the weaknesses. If the concerns raised are well addressed, I am glad to increase my rating.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work presents an extension to DiffusionNAG and incorporates multi-objective search.  Model complexity, computational efficiency, and inference latency are key measures captured through number of parameters, MACs, and latency estimation. These measures are recorded in a meta dataset for NASBench201 and MobileNetV3 with 10k and 20k architectures respectively. During search, pareto front filtering segments three regions corresponding to high accuracy, high efficiency, and best balance of the two using the auxiliary metrics from earlier. The experimental results are promising across a sufficiently diverse set of benchmarks.

### Strengths
Strong writing, ideas are explained well and thorough
The experiments are presented well and results are thorough
Novelty is presented in 2 algorithmic improvements and the contribution of a multi-objective meta dataset

### Weaknesses
For transferable NAS, the choice of benchmarks are interesting, TransNASBench provides a NAS dataset specifically for transferability in NAS. Exploring performance on this dataset would have been nice
MobileNetV3 and NB201 are also fairly dated search spaces, performance in more recent search space or architecture styles (vit) should be explored
The specific details of the algorithmic contribution are a bit vague. How is pareto front filtering done? 
ImageNet results are sparse and comparison to modern NAS methods on this benchmark are sparse

### Questions
How did you choose the search spaces to apply POMONAG? 
The algorithmic contribution seems like a limited extension of DiffusionNAG. What complication arose from integrating multi-objective NAS into DIffusionNAG?

### Soundness
3

### Presentation
4

### Contribution
3
