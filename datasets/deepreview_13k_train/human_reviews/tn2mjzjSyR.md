# DOTS: Learning to Reason Dynamically in LLMs via Optimal Reasoning Trajectories Search

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Enhancing complex reasoning capabilities of large language models (LLMs) has gained significant attention in recent years. 
Previous studies have demonstrated the effectiveness of incorporating prompting strategies to guide LLMs in performing reasoning actions, such as step-by-step thinking, reflecting before answering, and solving with programs, etc. 
However, these approaches often rely on static, predefined reasoning actions that are applied uniformly to all questions, without considering the specific characteristics of each question or the varying capabilities of different LLMs.
In this paper, we propose a novel method that enables LLMs to dynamically select the optimal reasoning action trajectory tailored to the specific characteristics of each question and inherent capabilities of different LLMs. 
Our approach involves three key steps: 1) defining atomic reasoning action modules that can be composed into various reasoning trajectories; 2) searching for the optimal action trajectory for each training question through iterative exploration and evaluation; and 3) fine-tuning the LLM to predict the best trajectory for new questions, by either using an external lightweight planner LLM or internalizing the planning capability into the solver LLM itself.
Extensive experiments across multiple reasoning tasks show that our method consistently outperforms static reasoning techniques and vanilla instruction tuning approaches. Further analysis reveals that our method enables LLMs to adjust their computation based on problem complexity, allocating deeper thinking and reasoning to harder problems. Overall, our work demonstrates the potential of empowering LLMs with dynamic reasoning capabilities to enhance their performance and adaptability on complex reasoning.

Enhancing the capability of large language models (LLMs) in reasoning has gained significant attention in recent years. Previous studies have demonstrated the effectiveness of various prompting strategies in aiding LLMs in reasoning (called ``reasoning actions''), such as step-by-step thinking, reflecting before answering, solving with programs, and their combinations. However, these approaches often applied static, predefined reasoning actions uniformly to all questions, without considering the specific characteristics of each question or the capability of the task-solving LLM. In this paper, we propose 
\textbf{\method}, an approach enabling LLMs to reason \underline{D}ynamically via \underline{O}ptimal reasoning \underline{T}rajectories \underline{S}earch, 
tailored to the specific characteristics of each question and the inherent capability of the task-solving LLM. 
Our approach involves three key steps: i) defining atomic reasoning action modules that can be composed into various reasoning action trajectories; ii) searching for the optimal action trajectory for each training question through iterative exploration and evaluation for the specific task-solving LLM; and iii) using the collected optimal trajectories to train an LLM to plan for the reasoning trajectories of unseen questions. In particular, we propose two learning paradigms, i.e., fine-tuning an external LLM as a planner to guide the task-solving LLM, or directly fine-tuning the task-solving LLM with an internalized capability for reasoning actions planning.
Our experiments across eight reasoning tasks show that our method consistently outperforms static reasoning techniques and the vanilla instruction tuning approach. Further analysis reveals that our method enables LLMs to adjust their computation based on problem complexity, allocating deeper thinking and reasoning to harder problems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes DOTS, an approach enabling LLMs to reason dynamically via optimal reasoning trajectories search, tailored to the specific characteristics of each question. DOTS first defines atomic reasoning action modules, then searches for the optimal action trajectory for each training question through iterative exploration and evaluation for the specific task-solving LLM, and uses the collected trajectories to train a model to plan for the reasoning trajectories of unseen questions.

### Strengths
1. The authors propose a dynamic reasoning method which can enable the model to decide the appropriate atomic actions based on the characteristics of the input question.
2. The authors conduct comprehensive experiments to prove the effectiveness of the proposed method, containing in distribution, few-shot, and out-of-distribution settings.
3. The proposed method can be used on both open-source and close-source models.

### Weaknesses
1. The method proposed in this paper does not show significant improvement on out-of-distribution (OOD) tasks, and it incurs additional computational overhead compared to prompt engineering methods. Specifically, the computational cost during the search phase, which involves iterative exploration and evaluation of reasoning trajectories, is not negligible. While the inference cost might be low, the training phase is computationally expensive. Furthermore, the lack of substantial OOD performance gains raises questions about the generalization capabilities of the learned planning model.
2. The baseline for Vanilla SFT only used the training data from CoT. I believe it should be compared with baselines from other reasoning formats to demonstrate the effectiveness of the proposed method, such as using the program reasoning format and mixed training data from CoT and Program. The absence of these comparisons makes it difficult to ascertain whether the proposed method's performance gain is solely due to the dynamic reasoning approach or if it also benefits from the specific training data format.
3. The experiments demonstrating the effectiveness of the Search section are compared with randomly selected reasoning paths. I am curious about how the results would compare if we contrasted it with reasoning paths generated by combining non-empty actions from each layer. This comparison is crucial to understand if the search algorithm is truly finding optimal paths or if it's simply outperforming random selection. The current comparison does not fully isolate the effectiveness of the search strategy.
4. Using PoT prompts on non-code models may yield suboptimal results. Would combining PoT with code models improve the results of the PoT baseline? The potential mismatch between the prompt format and the model architecture could be a confounding factor in the evaluation.

### Questions
See weaknesses.

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
The paper proposes a new way to learn reasoning through two learning paradigms. The paper (DOTS) proposes both a way to FT an planner LLM and in directly FT-ing the task solver.

### Strengths
1. Adaptability of the method: The method can be used either on the planner or on the task solver.

2. The method shows lower cost than non-CoT methods.

3. Improved Reasoning ability: The paper demonstrates improved reasoning ability by allowing for dynamic selection for a given question, outperforming static methods as well as self refinement (most but not all scenarios).

### Weaknesses
1. The proposed method is complex and involves several steps. It is not clear if the complexity is warranted and ablation studies on the various aspects can help.

2. The paper does not explore decomposition or tool use which would be crucial for complex tasks.

3. The paper glosses over how the atomic trajectories are collected.

### Questions
Q1. How many trajectories are required to improve performance substantially at FT-time? A more thorough discussion would be useful.

Q2. How does the proposed approach scale to more complex problems where process rewards would be beneficial?

### Soundness
3

### Presentation
3

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
The paper proposes DOTS, which can dynamically choose prompting methods to do reasoning, by dividing reasoning into analysis, solution, and verification modules, and choosing from recent popular methods for each module.

The dynamic planner can be either external or internal to incorporate various LLMs with difference sizes and openness.

Experiments are conducted on in-distribution, near-distribution, and out-of-distribution settings, and zero-shot and few-shot evaluations, where DOTS outperforms most recent LLM prompting reasoning methods.

### Strengths
DOTS unifies many of recent LLM prompting reasoning methods, and can dynamically choose better method for each module for each data sample. It borrows the strength of various solutions in literature, and can possibly incorporate future works.

The paper contains comprehensive experimental results, on various datasets across domain, and in/near/out-of-distribution experiments. The experiments show superior performance of DOT to previous prompting methods consistently.

The paper also includes ablation studies to verify the importance of each of the breakdown modules.

It also includes analysis of preferences of DOTS on different tasks, with insightful explanations. It also includes an analysis of efficiency, showing comparable computing costs to other advanced prompting techniques.

### Weaknesses
Although DOTS has higher average performance, DOTS cannot consistently beat baselines in all tasks. This is a little surprising as DOTS should be able to be considered as superset of all baselines. On those dataset DOTS fall behind baselines, it would mean it's not necessary to do dynamical reasoning (as one can choose the baseline instead of choosing different modules for each data sample).

This phenomenon is more often in out-of-distribution settings. The average score on out-of-distribution also shows smaller margin. This means lack of training (in a domain) can lead to much worse performance of DOTS. However, as also mentioned by author, such training set may be not available, casting generalizability concern on DOTS.

It would be beneficial to show the comparison on near-distribution zero-shot settings (e.g. the few-shot datasets in the paper) to verify that only near-distribution training is needed, but the paper only includes few-shot settings on these datasets. (also see questions)

To clarify, the few-shot experiments with consistent outperformance can partly address the point, but I would expect better zero-shot performance since training is involved.

### Questions
+ (Type) Equation 2: $T$ has not been defined.
+ (Clarification) For the "few-shot" settings, do you use the planner trained on MATH dataset? If so, they should be "near-distribution + few-shot", since those "few-shot" datasets are math-related.
+ Since DOTS has marginal performance on OOD tasks (despite DOTS need additional training), what's the performance on near-distribution (e.g. the few-shot datasets in the paper) but zero-shot settings?
+ In Table 3, 4, 5, on a few datasets DOTS is not the best among methods. Does it mean in some datasets, it's better to choose one single baseline method instead of choosing modules dynamically as in DOTS?
+ DOTS select one reasoning method (one choice for each module). Would it be better to attempt multiple choices and choose the best one (and this would align more with "trajectory search")?
+ (Minor) It would be beneficial to also include the computing efficiency of external DOTS.

### Soundness
3

### Presentation
2

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
The author creates a planning prompt strategy named DOTS. It can choose the path to solve the problem via a small model (as the planner) and prompt the large model to solve the problem. The path contains 3 parts: the Analysis Layer, the Solution Layer, and the Solution Layer. The experiment shows that both external and internalized planner can help the large model to solve the problem more effectively and efficiently. The ablation study also shows that the searching and explanation in planner's plan is useful.

### Strengths
1. The paper is easy to read and follow. Its ideas are presented straightforwardly along with illustrations.

2. It simplifies the planning prompt construction process. 

3. The authors study the DOTS over a wide range of benchmarks.

### Weaknesses
1. The comparison between the DOTS and other methods is not fair. The DOTS's prompt contains 3 layers, however, the baselines only contain 1/2 layer. The authors should compare the baseline with 3 layers (for example compulsory use of Decomposition + POT + self-verifications at the same time in MATH) to make the comparison more fair.

2. The method is not generalizable enough. It needs to SFT a new model for each large model / new atomic action in layers / new layers. (Although the authors claim that this is an advantage to make the prompt more suitable for a given model, it is still a limitation for the method.)

3. The improvement of the DOTS is not significant, especially in the OOD dataset. 

4. The ablation study only shows the result in the IND benchmark 

5. The ablation study in Table 6 does not explain the inherent reason that DOTS can improve performance, it's not enough for ICLR. (For example, can a large model have a similar performance with DOTS by only adding prior knowledge in the explanation?). (see question 3,4,6 below for more details)



### Questions
1. could you present the distribution of the path the planner will choose in the experiment? (i.e. x% of the path will choose Empty + POT + self-verifications, y % of the path will choose Decomposition + COT + Empty, etc.) (This is different from Table 7 in 2 parts: 1. It shows the distribution of the 12 types of combination of 3 layers in the path, 2. It needs to contain more benchmarks besides the MATH dataset)

2. Can 2 findings in Section 3.7 be generalized to other datasets?  

3. (From weakness 1) The authors should add a comparison with the baseline with 3 layers (and the choice of the layer should be reasonable towards a given benchmark) to make the comparison more fair.

4. From my perspective, the OOD benchmark is more important than the IND benchmark, however, the authors only show the ablation study in the IND benchmark. Why?

5. The improvement of the DOTS seems to come from the explanation (if you compare the result in Table 6's "-w/o Explanation" line with the second to the last line in Tables 3 and 4). So, does the prior knowledge in the prompt cause the improvement? 

6. (minor) The author claims that "the fine-tuned LLMs are constrained to follow the same reasoning format of the training data (e.g., CoT (Luo et al., 2023)) and lack the flexibility to adopt other reasoning strategies" (in line 53,77-78). However, FireAct[1], shows that the fine-tuned LLMs can change the reasoning strategies (COT or ReAct) by itself without any additional prompt. Maybe training COT and POT at the same time can help the model to be more flexible. The authors should revise this point to make it more accurate.

7. In Internalized setting, I'm curious that if llama3-8b is trained only in the Reasoning Process and Answer (like FireAct), what performance will be, will the trained model choose the Reasoning Process automatically? (It should also be a baseline), although I admit this can't be used in external setting.

8. (minor) In Table 2, "Few-shot" is not a kind of Distribution, maybe 4 columns (add example number column) can be more clear.

[1] FIREACT: TOWARD LANGUAGE AGENT FINE-TUNING

### Soundness
4

### Presentation
4

### Contribution
2
