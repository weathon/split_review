# SPaR: Self-Play with Tree-Search Refinement to Improve Instruction-Following in Large Language Models

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Instruction-following is a fundamental capability of language models, requiring the model to recognize even the most subtle requirements in the instructions and accurately reflect them in its output.
Such an ability is well-suited for and often optimized by preference learning.
However, existing methods often directly sample multiple independent responses from the model when creating preference pairs.
Such practice can introduce content variations irrelevant to whether the instruction is precisely followed (e.g., different expressions about the same semantic), interfering with the goal of teaching models to recognize the key differences that lead to improved instruction following.
In light of this, we introduce SPaR, a self-play framework integrating tree-search self-refinement to yield valid and comparable preference pairs free from distractions.
By playing against itself, an LLM employs a tree-search strategy to refine its previous responses with respect to the instruction while minimizing unnecessary variations.
Our experiments show that a LLaMA3-8B model, trained over three iterations guided by SPaR, surpasses GPT-4-Turbo on the IFEval benchmark without losing general capabilities. 
Furthermore, SPaR demonstrates promising scalability, greatly enhancing the performance of LLaMA3-70B.
We also identify how inference scaling in tree search would impact model performance.
Code and data will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This study presents SPAR, a self-play framework that enhances LLM‘s instruction-following capabilities by training with refined preference pairs. Unlike traditional methods that rely on independent response sampling, SPAR refines pairs to reduce irrelevant factors, thereby emphasizing critical distinctions, leading to notable improvements in instruction adherence. SPAR’s iterative process enhances instruction-following, judgment, and refinement, offering a pathway for continuous model improvement.

### Strengths
1. The motivation makes sense. The fine-grained refinement is essential for further improving the model's instruction-following abilities.
2. The design of the proposed method is sound, allowing it to effectively achieve its intended motivation.
3. The experiments are comprehensive, demonstrating relatively strong performance.

### Weaknesses
1. The applicability of the method may be limited. It might be suitable primarily for further improvement of models that already possess strong instruction-following capabilities, as the experiments were conducted on models that had already undergone instruction fine-tuning. Additionally, a strong LLM is required for warm-up training before iteration (This also raises concerns about the fairness of comparisons.), and one of the goals of dataset construction is to introduce more complex instructions.
2. Missing comparison with a key baseline：Self-Alignment with Instruction Backtranslation.

### Questions
1. Why are judgment and refinement performed by the same model? What would happen if they were separated, or combined with the actor model, using a single model for all tasks?
2. I haven't closely checked the details of the baselines. Do they use a strong LLM, or do they rely solely on the model being evolved?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces SPAR (Self-Play with Tree-Search Refinement), a self-improvement framework that enhances the instruction-following capabilities of LLMs by minimizing extraneous factors and highlighting key differences in preference pairs. This method involves an iterative training process where a model (actor) performs tasks, and a paired model (refiner) evaluates and refines the imperfect responses using a tree-search algorithm through structured feedback loops. The authors evaluate SPAR with two LLMs on the IFEval and FollowBench benchmarks. Additionally, they contribute a dataset with 43k complex instruction-following prompts and an SFT dataset that can improve the instruction-following capabilities of LLMs.

### Strengths
1. Effective in reducing noise. By minimizing content variations in preference pairs, SPAR helps the model focus on essential elements, which improves its instruction-following accuracy.

2. Comprehensive ablation experiments. The authors conducted extensive ablation studies to verify the impact of interfering factors on preference learning and to assess the rationality of each component in the framework.

3. Generalization without degradation. The approach does not degrade general language model capabilities, suggesting a balanced enhancement in alignment without compromising overall functionality.

4. Contribution of datasets. The authors provide valuable datasets that benefit the development of this research area.

### Weaknesses
1. Limited validation across models. The effectiveness of the method was validated on only three models. Further exploration is needed to assess the framework's applicability to other models.

2. Reliance on complex setup and compute resources. The framework's iterative training, including tree-search refinement and multiple model roles, may require significant computational resources. Therefore, the performance-cost trade-off needs further clarification. 

3. Lack of comparative details. The paper lacks sufficient details in its comparisons with other methods, such as how each baseline initializes the model.

### Questions
1. The paper only lists results from the first three iterations, and the data indicate that the model's performance still has room for improvement. Could you provide a simple analysis of when the model might reach optimal performance?

2. Does the framework heavily depend on the model's initial performance? Can it be directly applied to the raw models provided officially?

3. It is suggested to directly specify the strong LLM used in Section 2.2.2

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel self-play framework (called SPAR) integrating tree-search self-refinement to yield valid and comparable preference pairs free from distractions, so as to teach models to recognize the key differences that lead to improved instruction following. To gain a good start for Actor and Refiner, the authors construct a high-quality dataset with 43K complex instruction-following prompts and an SFT dataset for improving the instruction-following capabilities of LLMs. Through extensive experiments on several LLMs, the authors demonstrate the effectiveness of proposed SPAR.

### Strengths
* The proposed approach is intuitive and has strong motivation.

* This paper is well-written and presents clear ideas.

* The authors conduct extensive experiments to validate the effectiveness of proposed SPAR.

### Weaknesses
* **SPAR introduces additianal training overheads.** SPAR initially requires constructing additional data to train the actor and trainer. Building on this, it needs to incorporate iterative training with tree search and self-consistency, which greatly increases the training cost compared to self-rewarding.

* **Some crucial information is missing in the experiment section.**  For example, what is the average number of search nodes in the tree search, and does it decrease with the iterations? How does LLaMA3-70B perform at different iterations (SPAR-70B-SFT, SPAR-70B-DPO-iter1, SPAR-70B-DPO-iter2)?

### Questions
See weaknesses. 

In addition:

(1) line 527, GPT-4-Turbo or GPT-4o-mini?

(2) Can you compare the training cost of SPAR, Self-Rewarding and Meta-Rewarding?

(3) Does more iteration brings higher performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce SPAR, an automated and scalable approach designed for self-improvement in instruction-following tasks through self-play. The core idea is to create paired responses with minimal irrelevant variations, allowing for precise training of the model's instruction-following capabilities. In the SPAR framework, the authors fully leverage test-time scaling: using tree search to obtain higher-quality data for training the model's instruction-following abilities, and using self-consistency to acquire higher-quality data for training the model's discriminative and refinement abilities. Experimental results show that the SPAR framework significantly outperforms various self-critique baselines.

### Strengths
- Constructing tailored and distinct instruction-following response pairs for the model by eliminating irrelevant content is a strong motivation for enhancing the model's instruction-following abilities.  
- The SPAR framework's proposal to use test-time scaling during the training phase to obtain high-quality data for training the model's 
- The experimental setup is reasonable, and the results appear promising.  
-  The writing in the paper is clear and easy to understand.

### Weaknesses
Using test-time scaling (more accurately, inference-time scaling) during the training phase to obtain high-quality data for self-critique is well-motivated, but it undoubtedly introduces significant training overhead. Therefore, providing a detailed comparison of the training costs of different methods, or comparing the gains when the costs are aligned, would make the paper's conclusions more convincing.

typo: line 239 needs a blank after 'refiner'.

### Questions
See weakness.

### Soundness
3

### Presentation
4

### Contribution
3
