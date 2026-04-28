# LLMOPT: Learning to Define and Solve General Optimization Problems from Scratch

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Optimization problems are prevalent across various scenarios. Formulating and then solving optimization problems described by natural language often requires highly specialized human expertise, which could block the widespread application of optimization-based decision making. To make problem formulating and solving automated, leveraging large language models (LLMs) has emerged as a potential way. However, this kind of way suffers from the issue of optimization generalization. Namely, the accuracy of most current LLM-based methods and the generality of optimization problem types that they can model are still limited. In this paper, we propose a unified learning-based framework called LLMOPT to boost optimization generalization. Starting from the natural language descriptions of optimization problems and a pre-trained LLM, LLMOPT constructs the introduced five-element formulation as a universal model for learning to define diverse optimization problem types. Then, LLMOPT employs the multi-instruction tuning to enhance both problem formalization and solver code generation accuracy and generality. After that, to prevent hallucinations in LLMs, such as sacrificing solving accuracy to avoid execution errors, model alignment and self-correction mechanism are adopted in LLMOPT. We evaluate the optimization generalization ability of LLMOPT and compared methods across six real-world datasets covering roughly 20 fields such as health, environment, energy and manufacturing, etc. Extensive experiment results show that LLMOPT is able to model various optimization problem types such as linear/nonlinear programming, mixed integer programming and combinatorial optimization, and achieves a notable 11.08\% average solving accuracy improvement compared with the state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors of this paper introduced **LLMOPT**, a novel learning-based framework designed to enhance large language models' (LLMs) capability to define and solve general optimization problems described in natural language. The key innovation is the **five-element formulization**, which structures optimization problems into sets, parameters, variables, objectives, and constraints, enabling more accurate problem representation and solver code generation. LLMOPT also incorporates **multi-instruction supervised fine-tuning (SFT)** and **model alignment** using the Kahneman-Tversky Optimization (KTO) method to improve both the accuracy and generalization of solutions.

Another significant contribution is the **self-correction mechanism** in the auto-testing process, which automates error analysis and solution refinement during execution, ensuring robust performance without manual intervention in test-time. The framework was evaluated on six real-world datasets, covering diverse optimization types and fields, achieving an **average accuracy improvement of 11.08%** over state-of-the-art methods. This demonstrates LLMOPT's effectiveness in boosting both the accuracy and generalizability of LLMs in solving complex optimization problems.

### Strengths
- The paper introduces a *novel five-element formulization* to define optimization problems, which significantly enhances the ability of large language models (LLMs) to accurately interpret and transform natural language descriptions into solvable optimization problems. This structured approach captures the essential elements of optimization scenarios, ensuring clearer problem representation and facilitating better code generation. The inclusion of elements such as sets, parameters, variables, objectives, and constraints helps the model produce more precise solutions and reduces the risk of omitting implicit problem aspects.

- Another notable feature is the *self-correction in test-time*, an automated process called *Auto-testing* integrated within LLMOPT to identify and rectify errors in generated solver code during execution. This mechanism analyzes output logs and determines if adjustments are necessary, enhancing the robustness and accuracy of problem-solving without manual intervention. By automatically looping back to problem reformulation or code generation when needed, LLMOPT can iteratively improve the accuracy of its solutions and adapt effectively to complex challenges.

- The paper boasts *strong evaluation results*, demonstrated by extensive testing across six real-world datasets encompassing approximately 20 different fields and various optimization problem types, such as linear and nonlinear programming and combinatorial optimization. LLMOPT shows superior performance, achieving a notable 11.08% average improvement in solving accuracy compared to existing state-of-the-art methods. This result underscores the framework’s generalization capabilities and effectiveness in diverse optimization scenarios, validated by comprehensive comparisons and ablation studies.

### Weaknesses
1. **Complexity of Data Labeling**: The proposed five-element formulation and the use of expert labeling for optimization problem formulations and solver code rely significantly on manual validation. While the authors mention the use of GPT-4 to assist in data generation, human experts are still required to verify the correctness of the outputs. This introduces potential scalability issues as extensive human oversight could limit the practicality of the approach, especially in large-scale deployments. Additionally, the authors do not provide a qualitative or quantitative analysis of the labeling quality or reliability performed by the human experts. Evidence demonstrating the expertise and qualifications of these experts should be presented to support the validity of the labeling process.

2. **Insufficient Theoretical Justification for the Five-element Formulation**: The authors claim that the five-element formulation is a universal method for defining optimization problems, but they do not provide sufficient references or theoretical analysis to support this claim of 'universal'. Similarly, in the experimental results, a detailed and decomposed explanation of why the five-element formulation generalizes well and outperforms other models across different types of problems is lacking. Providing theoretical or empirical grounding beyond performance metrics would strengthen the argument for the effectiveness and universality of this approach.

3. **More comparative Analysis of the Self-correction Mechanism**: While the authors compare the performance of LLMOPT with and without the self-correction mechanism, it would be beneficial to include an analysis of the performance gains when self-correction is combined with baseline methods (e.g., GPT-4 directly). Additionally, a longitudinal comparison between the current self-correction design and other correction methods, such as manual debugging, could further elaborate on the advantages and limitations of the self-correction approach.

### Questions
**Questions and Suggestions for the Authors:**

1. **Clarification on Expert Involvement in Data Labeling**:
   - **Question**: Could the authors provide more details on the qualifications, expertise, or at least agreement rates of the human experts involved in the data labeling process? 
   - **Suggestion**: Including a quantitative or qualitative analysis of expert reliability and consistency would strengthen the validity of the data labeling claims. Evidence such as statistics of certifications or relevant experience, and agreement rates among experts would be valuable to better assess the credibility of the labeled data.

2. **Theoretical Justification for the Five-element Formulation**:
   - **Question**: What is the theoretical basis for claiming that the five-element formulation is a universal method for defining optimization problems? 
   - **Suggestion**: Providing additional references or an in-depth theoretical analysis that supports the universality and applicability of the five-element formulation across various optimization scenarios would enhance the argument. Empirical comparisons to alternative problem formulations could also be beneficial.

3. **Comparative Performance Analysis of Self-correction Mechanism**:
   - **Question**: How does the self-correction mechanism in LLMOPT compare with similar correction methods, such as manual debugging or integration with other LLMs or methods like GPT-4 in a correction loop?
   - **Suggestion**: Presenting a detailed comparison of LLMOPT’s self-correction mechanism with existing correction strategies or showing performance metrics of LLMOPT combined with baseline models could provide insights into its relative effectiveness. This would help demonstrate whether the self-correction offers unique advantages or is comparable to simpler, established methods.

4. **Scalability Concerns**:
   - **Question**: How do the authors envision scaling the current framework for large-scale practical deployments given the heavy reliance on expert validation?
   - **Suggestion**: Suggestions for automating or streamlining the expert review process, possibly by incorporating semi-supervised or active learning techniques, could address concerns about scalability and long-term sustainability of the labeling process.

5. **Detailed Explanation of Generalization Capabilities**:
   - **Question**: Can the authors provide more specific examples or case studies where the five-element formulation showed clear advantages in generalization compared to alternative models?
   - **Suggestion**: Adding empirical evidence or a breakdown of performance across different types of optimization problems, particularly ones not included in the training set, would strengthen the claim of its broad applicability and effectiveness.

6. **Addressing Potential Limitations in Self-correction**:
   - **Question**: How does the self-correction mechanism handle potential limitations or biases in repeated corrections, such as overfitting to a specific type of error?
   - **Suggestion**: Discussing safeguards or mechanisms in place to ensure diverse error handling and avoiding biased correction loops would provide more confidence in the robustness of the self-correction feature.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes LLMOPT, which finetunes an LLM to formulate optimization problems (from problem description -> mathematical model/solver model). The finetuning is performed in two stages: SFT stage (where the LLM is finetuned using MLE on ground truth outputs), and KTO-based alignment (where the LLM is finetuned based on desirability labels on LLM generated outputs).

### Strengths
The paper addresses an interesting and timely problem. Optimization modeling is a huge topic, and introducing techniques to automate (partially) this task will have significant impact.

To my knowledge, this is also one of the first works that builds/finetunes LLMs specifically for writing optimization models.

The empirical analysis is comprehensive (spanning many benchmarks) and the resulting performance gains are impressive.

### Weaknesses
1. **Novelty**: The authors mentioned ORLM, which similarly trains an LLM to do optimization modeling, but did not provide a direct comparison. I also read ORLM (not in the most detail), but it appears to do some data augmentation to train an LLM for model formulation. It seems the main difference is the alignment step (using KTO) and the self-reflection step, can the authors explain the novelty of their method compared to ORLM?

2. **KTO alignment**: There are a few comments on this:
* **Writing/clarity**: The writing in S3.3.2 is quite hard to follow, I had to read the original paper to understand what this part is doing. Importantly, Equation (3) is not correct, in the original DPO paper, the optimal reward function has an additional log partition function term. I did not check if this affected the rest of the formulation.
* **KTO dataset**: Based on my understanding: (1) the SFT step does not use the KTO dataset (which contains GPT4 generated responses, and desirability labels), and (2) the alignment step does not use the original dataset (which contains ground truth formulations). Is my understanding correct? If so, what is the motivation for not using the KTO dataset during SFT and original dataset in KTO alignment (where the ground truth are all labeled as 'desirable')? 
* **Purpose of KTO**: The authors state that `KTO loss function encourages the optimal model $\pi^*$ to produce completions that align more closely with expert-labeled data`. **Minor**: this can't be the optimal model, but the learned policy $\pi$? **Major**: This is exactly the same purpose as SFT, so we are back to the above point of why the KTO dataset is not used directly through SFT, it would likely be more stable and have lower variance compared to KTO updates.
* **Ablation study**: Can the authors more comprehensively ablate the importance of the KTO step? I carefully examined the results in Table 3 (ablation study)---which seems to indicate that `w/o KTO` on many benchmarks does not significantly improve SA. I would be interested to also see how LLMOPT performs when the KTO dataset is used directly during SFT.

3. **Questions about results**: 
* **AST**: Can the authors help me understand the big difference in average solution time (AST) plotted in Fig 4? I had a look at some examples in `NLP4LP`, these are very straightforward LP problems. As such, I am very surprised that LLMOPT and GPT4 have almost 2x difference in solution time. Given the simplicity of the problems in this dataset, (1) this difference is unlikely to be explained by clever reformulations that improve solution time, (2) and unlikely to be noise. 
* **Solution accuracy**: Can the authors elaborate on exactly how solution accuracy is calculated? Is this based on some test cases? My intuition is that it is extremely difficult to check the formulation directly, so how is SA computed and is this a robust evaluation method?
* **Performance by problem type**: In L422-L431, the authors claim their method is more general, which I understood as achieving better performance on more types of problems (e.g. LP, MILPs, QPs). To confirm this claim, I would like to see the performance by problem type (similar to the Figure 8 in App G).



### Questions
I also have some minor concerns:

* **Dataset construction**: In L219, the authors mentioned they had 1763 'seed' problems. Did they label formulations for all 1763 problems? If so, this is a pretty big contribution if the authors choose to open-source their dataset.
* **Augmented data**: My understanding is that additional examples were introduced by mutating the original seed problems. Were these also formulated and labeled by human experts? How many examples in total (original + mutated) were used in training? 
* Can the authors describe the procedure of collecting the labelled formulations (if human experts were indeed used). This seems like a huge undertaking especially if they are required to write out the mathematical models and code.
* **Eq(4) and (5)**: The notation $\nu \sim \cdot$ was slightly confusing, since it is not a random variable, which is where this notation is mainly used.
* **Eq (5)**: Are $\lambda_D$ and $\lambda_U$ learnt parameters or hyperparameters?
* **Solver**: What solver did LLMOPT use? Is it `Pyomo` as shown in the method figure? Are the baselines evaluated with the same solvers?
* ps. this is just a suggestion, but the use of the word `alignment` is slightly misleading, the authors are not aligning the LLM to principles, but doing a different stage of finetuning with a different dataset.
* pps. another minor suggestion, but the authors should make more prominent that KTO is an existing method, I saw the citation, but it is slightly buried, and might convey the impression that KTO is an original contribution of this work.

I am going to start with a conservative rating, but open to revising if the authors address my concerns.

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
This paper proposes to finetune LLMs to improve MILP modeling from natural languages. Specifically, from natural language description of a MILP problem, this paper proposes to formulate the MILP problem as a five element formulation, and then generate solver code from the  formulation. It uses data augmentation to expand the data set, and ask domain experts to label the data set to finetune the LLMs. Through extensive empirical study, it shows performance improvement from a variety of competitive baseline methods.

### Strengths
- The authors did a good job benchmarking their method on a variety of benchmarks with many competitive baseline methods. The empirical evaluation seems to be comprehensive.
- To my knowledge, there has not been many works that aim to fine-tune the LLM for MILP modeling tasks, so the task is relatively novel.
- I appreciate the detailed discussion provided by the authors, which I think is valuable and can help guide the community thinking about future steps.

### Weaknesses
 - The fine-tuning data collection requires expert manual labels, which limit the scalability and applicability of applying this method.
- Despite strength 2 mentioned above, the related work ORLM cited by the paper already took an initial step in fine-tuning LLMs for MILP modeling, and RLHF/DPO/KTO has been commonly used in LLM literature to finetune LLMs, so I’m a bit concerned whether the novelty of this work is sufficient, especially the work requires expert manual labors for constructing the fine-tuning data.
- Table 3: it seems like a majority of performance improvement is from self-correction instead of the five element components and KTO. If I understand correctly, the self-correction is prompting the LLM to correct any error it makes and has been used in previous papers such as [1], and it’s not related to the KTO fine-tuning pipeline. Given this, I’m a bit concerned about the contribution of the two main components (five elements and KTO) in this work.
- I find certain parts of the paper missing details and somewhat confusing (see my questions below).

### Questions
- Five-element formulation: to my knowledge, OPTIMUS [1] also identifies components such as variables, constraints, parameters etc in the optimization description before they translate the optimization problem into code. Can the authors comment on the difference between the two modeling approaches?
- Line 222: “experts review the generated problems, removing those with unclear descriptions or infeasible solutions to ensure data diversity and quality.” Can the authors comment on what are the criteria for the experts to determine the descriptions are “unclear”? How long is the expert labeling process? Can experts make mistakes? Can the authors comment on whether there is anyway to consider the expert mistakes to further improve the learning performance?
- Line 276 equation (3): I find the description of KTO confusing. For example, what is the reference model pi_ref used by the authors? Also, what is the optimal model (is it the same thing as the learning model)?
- Table 3: Can the authors comment on what is the setup w/o KTO? Is there still a training / fine-tuning component? what is the alternative loss?

Additional Feedback:

- line 53: The authors provide Wrong citation for ORLM on page 1.
- line 249: “are correct labeled by experts” → “are correctly labeled by experts”

[1] AhmadiTeshnizi, Ali, Wenzhi Gao, and Madeleine Udell. "OptiMUS: Scalable Optimization Modeling with (MI) LP Solvers and Large Language Models." ICML (2024).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a learning-based LLM for solving Optimization Problems. The experimental results demonstrate the effectiveness of the proposed LLMOPT compared with prompt-based methods.

### Strengths
1. The introduction of this manuscript is clear.

2. Some improvement over baseline results.

### Weaknesses
1. It is questionable whether LLMs are capable of solving large-scale optimization problems. If their applicability is limited to small-scale problems, such as the Traveling Salesman Problem with just 10 nodes, the significance of this method is unclear. A problem of this size can even be solved by the Hopfield network proposed in the 1980s. In fact, both traditional heuristics and more recent neural combinatorial optimization methods are capable of handling problems with thousands of nodes [1, 2]. The paper does not provide any evidence that LLMOPT can scale to problems of this size, which raises concerns about its practical utility beyond toy examples. Specifically, the paper lacks experiments on benchmark datasets for large-scale combinatorial optimization problems, such as those found in the literature on vehicle routing or network design, where problem instances can have hundreds or thousands of nodes or edges.

2. In Abstract, the authors mention, "to prevent hallucinations in LLMs, such as sacrificing solving accuracy to avoid execution errors." However, I do not believe this phenomenon should be described as hallucination. Hallucination typically refers to instances where the output of an LLM appears reasonable but is, in fact, fabricated. In this case, reducing solving accuracy to prevent execution errors does not align with the conventional meaning of hallucination. Please provide a more precise explanation or reconsider this terminology. The paper should clarify the specific mechanisms by which the LLM prioritizes avoiding execution errors over solution accuracy, and how this trade-off is managed.

3. As shown in Table 3, the self-correction mechanism plays a decisive role in the performance of LLMOPT. However, this mechanism is not originally proposed in this manuscript. As the authors describe on Page 6, "Inspired by Chen et al. (2024), to enhance optimization generalization, we implement self-correction to automatically analyze the output results and identify errors arising during the execution of the solver code." Furthermore, the prior study [3] has also employed this mechanism to improve the performance of LLMs in solving vehicle routing problems. The paper should provide a more detailed analysis of the novelty of their self-correction approach, highlighting any differences from existing methods and demonstrating how it specifically contributes to the performance of LLMOPT.

4. In Section 4, the authors do not report the training time of LLMOPT, making it unfair to directly compare it with prompt-based methods. The computational cost of training LLMOPT should be clearly stated, including the hardware used, the training time, and the energy consumption. This is crucial for a fair comparison with prompt-based methods, which typically have lower computational overhead. The paper should also discuss the scalability of the training process, and whether it can be efficiently scaled to larger models or datasets.

5. Please provide the code generated by the LLM to solve the optimization problem. I am doubtful that current LLMs are capable of generating code sophisticated enough to solve medium- or large-scale problems. The paper should include examples of the generated code for different types of optimization problems, demonstrating the complexity and correctness of the generated code. This would help to assess the practical applicability of the proposed method.

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2
