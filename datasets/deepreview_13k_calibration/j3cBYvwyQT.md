# TapWeight: Reweighting Pretraining Objectives for Task-Adaptive Pretraining

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Large-scale general domain pretraining followed by downstream-specific finetuning has become a predominant paradigm in machine learning. However, discrepancies between the pretraining and target domains can still lead to performance degradation in certain cases, underscoring the need for task-adaptive continued pretraining (TAP). TAP methods typically involve continued pretraining on task-specific unlabeled datasets or introducing additional unsupervised learning objectives to enhance model capabilities. While many TAP methods perform continued pretraining with multiple pretraining objectives, they often determine the tradeoff parameters between objectives manually, resulting in suboptimal outcomes and higher computational costs. In this paper, we propose TapWeight, a task-adaptive pretraining framework which automatically determines the optimal importance of each pretraining objective based on downstream feedback. TapWeight reweights each pretraining objective by solving a multi-level optimization problem. We applied TapWeight to both molecular property prediction and natural language understanding tasks, significantly surpassing baseline methods. Experimental results validate the effectiveness and generalizability of TapWeight. Our code is publicly available at \url{https://anonymous.4open.science/r/TapWeight-9A2E}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes TapWeight, which automatically determines optimal loss weights for different pretraining objectives through a three-level optimization approach.

### Strengths
* The proposed three-level approach is flexible and demonstrates transparent performance improvements.
* The qualitative analysis effectively shows how different downstream tasks require different weights for pretraining objectives, justifying the need for adaptive weighting.

### Weaknesses
Major weakness: 
* The evaluation on GLUE benchmark, which has been saturated in recent years, would benefit from including more challenging datasets. E.g., Crossfit (160 downstream tasks) https://arxiv.org/pdf/2104.08835
* The effectiveness of the pretraining objectives on more powerful generative models or LLMs remains unexplored. For example 1.  gpt3.5 result on more challenging glue-x: https://aclanthology.org/2023.findings-acl.806.pdf 2. three-stage LLM method for task adaptive pretraining: https://arxiv.org/abs/2402.05140
* Missing reference and comparison with other recent MLM models (they have higher performance on the GLUE benchmark): e.g., Pre-training Language Model as a Multi-perspective Course Learner https://arxiv.org/pdf/2305.03981

Other weakness:
* The selection criteria for multi-objective pretraining tasks in Level I needs justification, particularly why certain tasks were chosen over alternatives like token detection or swap detection.
* line 452-457: The effects of pretraining task to downstream tasks need a more in-depth investigation. Particularly, according to the trade-off score result, how will these findings better inform us on designing new or matching existing pretraining tasks with downstream tasks?

### Questions
see weakness section

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes TapWeight, an approach to adapt weights for different pre-training objectives according to downstream tasks. The authors propose a three-level optimization, where the first level is the traditional pre-training level, the second level is the downstream fine-tuning level, and the third-level is downstream validation level to finally provide signals for weight updates. In the experiments, the authors demonstrate that TapWeight can outperform baselines on molecular tasks, and outperform the pre-train fine-tuning pipeline on NLU tasks. They also conduct a few ablation studies to show the importance of reweighting and multi-level optimization.

### Strengths
- The proposed TapWeight method can effectively increase model performance on targeted downstream tasks that are different from the pre-training domain.
- The authors also conduct a few ablation studies to show the importance of reweighting and multi-level optimization.
- The code is released for reproducibility.

### Weaknesses
 - The proposed multi-level optimization is not new, and can actually be seen as meta-learning.
- The experiment results are not well presented. For example, table 2 is about "results" of molecular prediction, but the authors do not explain the metrics in the table, and do not use up-arrow or down-arrow to show whether the numbers should be bigger or smaller.
- The novelty of the method is not clearly articulated. While the authors claim a three-level optimization, the core idea of adapting pre-training objectives based on downstream task performance is conceptually similar to existing meta-learning techniques. The distinction between their approach and established methods needs further clarification, especially regarding the specific optimization algorithms used at each level and how they interact.

### Questions
- Can the authors include experiment results of more types of tasks other than NLU and molecular prediction tasks? E.g., legal domain, financial domain, etc. Otherwise, I don't think this method has wide applications.

### Soundness
3

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
This paper introduced a method called TapWeight, to automatically tune the loss weights of multiple pretraining objectives during task-adapted continued pretraining. In task adapted continued pretraining, a new mixture of pretraining objectives is introduced, targeted to improve a specific suite of downstream tasks. Downstream task performance is measured by applying SFT to the new pretraining checkpoint, and evaluating on the validation or test split. The main problem the paper aims to solve is how to balance the pretraining objectives in the continued pretraining mixture in order to maximize downstream task suite performance.

TapWeight tackles this problem by formally framing this as a three tiered multi-level optimization (MLO) problem, where Tier 1: Continued Pretraining given some loss weights, Tier 2: SFT, Tier 3: Optimizing pretraining loss weights to maximize validation performance. Note that this paper only studies the work as applied to Encoder-only models, and SFT finetuning (until convergence.) The SFT phase is slightly altered in the training setup to deduce dependence with other tiers (using the continued pretrain weights as regularization instead of initialization), and the MLO optimization employs the Betty library to solve (with some tricks to approximate the inverted Hessian, as noted in the Appendix).

The approach is evaluated on a popular, standard, molecular property prediction model, Imagemol, as well as on NLP tasks (GLUE), via RoBERTa. In both domains, the method outperforms compared baselines. The authors also provide ablation result for each component of their method.

### Strengths
1. Finding effective ways of optimizing the choice of pretraining objective to optimize downstream performance is an important problem that would be of interest to the greater community. The authors provide a novel connection to MLO in this work, and the formal solving of this problem is valuable and welcome given the amount of empirical hillclimbing typically done in this space. 

2. The paper shows convincing results that their formal optimization of the whole MLO objective works from a quality perspective, and yields results that improves over the baselines they consider. Given the complexity of solving such an MLO problem, these results are promising and this technique may be of interest to the community. 

3. The presentation of the work is nice. It is well written, structured, and easy to follow, free of any grammatical mistakes. There are some aspects about the method that could be clearer, but overall this does not detract from the presentation of the paper.

4. Evaluation of the method on both molecular biology and language demonstrate well the generality of the method. Especially as many (5) pretraining objectives are considered for the molecular image model. 

5. Reproducibility is excellent. The authors have already open sourced the code, and provide all information needed to reproduce their experiment.

### Weaknesses
1.) Soundess: Most of the experiments in this work compare against baselines that do not apply task-adaptive continued pretraining. It is only in Table 4 that the authors show this ablation result for the molecular results (but not the NLP results.) In Table 3, it is unclear whether the method is gaining because of continued pretraining in general or because of TapWeight. TAPT represents a continued pretraining comparison, but from a different data distribution.

This work would benefit from having more baselines that represent basic ways of hillclimbing the pretraining mixture. Some examples:
- All pretraining objectives weighted evenly in the mixture.
- Leave-one-out or one-at-a-time ablations for the pretraining mixture. 
- Even weighting of only the objectives that maximize certain tasks in the eval suite + any other grid-search like approach.
- This dataset ablation can take place over smaller models (to use less compute), before being applied to the final model size.

In Table 5, TapWeight is 1.5x the cost of normal training, so it is possible that TapWeight may be a way to save compute over traditional hillclimbing, but having these explicit compute & quality comparisons against more baselines would largely strengthen the paper.

2.) Contribution: The contribution of this work is solid for the targeted application: continued pretraining (CP) of encoder-only models to maximize SFT tasks. However, there there is also a implicit assumption that the continued pretraining computation budget is small. In Table 5, the training budget of CP is only a little bit more expensive than that of SFT. It is unclear how true this assumption is for most modern models. It is unclear also how TapWeight would perform or handle much longer training horizons, or where CP>>SFT in terms of computational budget and they need to see a different budget of tokens.

Also note: Table 5 also only reports time rather than FLOPs, and its not possible for the reader to understand whether each phase occurs on the same amount of hardware.

The paper is missing a crucial baseline that might help the reader understand the wider applicability of the technique: training CP+SFT (Table 5) for the same time / FLOPs as TapWeight, to observe if the gains from TapWeight outweight the computation cost. (e.g. If you make the cheaper alternatives use as much compute, would they do better? Is TapWeight yield training compute efficiency gains?)

Note however that the authors are relatively upfront about limitations here.

3.) Presentation: The description of the method relies on an understanding of MLO, which is OK, but the paper would be clearer if more descriptions were provided, especially as it applies to CP. For example: it seems like MLO does CP and SFT in a single phase, as implied by Table 5, and the optimization equations. However, Figure 1 somewhat suggests that CP is done then an entire SFT run is done, before updating the loss weights. Exactly how many tokens of CP vs. SFT is seen per step is also unclear (or is it assumed they see the same number of tokens, 1:1 for each step?)

There's also some work that may be relevant, but missing from related works:
- UL2: https://arxiv.org/pdf/2205.05131
- U-PaLM: https://arxiv.org/abs/2210.11399 (CP version)
A lot of manual ablation was done for the construction of UL2 and UL2R in U-PaLM. These would serve as very natural candidates for a more learned continual pretraining approach. 

4.) Soundness: The authors make the claim Line 88 “Moreover, TapWeight is applicable to any pretrained model with multiple pretraining objectives”. This is likely true in theory, but the authors lack empirical evidence for this given their limited setting (e.g. how about decoder-only models?). 

TapWeight as described also is only defined over loss weights of multiple pretraining objectives, but this is not well defined for pretraining objectives that need to see different amounts of different pretraining objectives, like UL2 mentioned above. Please correct me if I am wrong here.

### Questions
Could the authors provide more information about how the TapWeight update work? What is the granuarly? How many tokens of CP vs. SFT is seen per-step? Is it equal? Is my understanding correct that CP+SFT is jointly optimized in TapWeight? 

If above is true, is it true then that the loss weights adaptively update during training? Have you tried taking the final weights and doing another run with the final weights, fixed?

Is extra SFT applied after TapWeight?

How many A100s are used in each phase of training, and for how long? (More information about Table 5).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a new task-adaptive pretraining (TAP) framework, called TapWeight, designed to improve downstream model performance by automatically optimizing the importance of each pretraining objective. Unlike traditional TAP methods that rely on manually set tradeoff parameters between multiple pretraining objectives, TapWeight dynamically learns these parameters by solving a multi-level optimization (MLO) problem. The authors report empirical results from the domain of molecular property prediction and natural language understanding, demonstrating its performance across 13 molecular and 8 language datasets compared to baseline TAP methods.

### Strengths
1. The proposed framework automates the weighting of pretraining objectives, by optimizing the importance of each pretraining objective in a dynamic, data-driven manner.

2. The authors showcase experiments across two domains - molecular property prediction, and NLU

3. The authors provide an open-source implementation for their approach, adding transparency and reproducibility.

### Weaknesses
1. The tasks chosen for evaluation are primarily classification. Given the current state-of-the-art LLMs, and VLMs, and the corresponding benchmarks, no analysis in that regard has been shown. For example, some maths problem solving tasks such as Math QA, MetaMath etc. can be used to constitute the pre-training tasks, and evaluated on a task such as GSM8K.

2. The number of baselines used for comparison is limited. For example, the paper "Don’t Stop Pretraining? Make Prompt-based Fine-tuning Powerful Learner", is a strong baseline candidate for the proposed method, as the paper builds further upon the TAP method.

3. Increased computational complexity limits the scalability of the method to larger models. Specifically, the multi-level optimization (MLO) approach introduces a significant computational overhead, potentially making it impractical for very large models with billions of parameters. The paper lacks a detailed analysis of this computational cost in terms of training time and memory requirements, especially when compared to simpler, fixed-weight pretraining methods.

4. The paper does not discuss or provide an empirical analysis of how quickly the model converges compared to fixed-weight pretraining methods. The absence of convergence analysis makes it difficult to assess the practical benefits of the proposed method, especially in resource-constrained settings. It is unclear whether the dynamic weighting approach leads to faster or slower convergence compared to static weighting strategies.

### Questions
1. Could you provide more details on the convergence rate of TapWeight, especially compared to traditional pretraining methods with fixed weights? How does the computational overhead impact practical training times on large-scale datasets?

2. I am curious to know whether there are any patterns observed in the reweighting behavior across tasks, such as prioritizing certain objectives over others based on task type. Were there some pre-training tasks that were given negligible weights? 

3. If possible, can you provide an analysis using larger models, and generative tasks, instead of classification? Additionally, a framework would be considered stable if an ablation could be shown across model families and varying scales. 

4. To obtain the robustness of the approach, a random task which has no relation with the downstream task can be augmented with the set of other pre-training tasks, just to see of TapWeight assigns a very low weightage to the random task. 

5. **A suggestion, please keep the tables in the page where the corresponding description is present, improves the readability of the paper.

### Soundness
3

### Presentation
3

### Contribution
2
