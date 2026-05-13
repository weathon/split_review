# Model Growth Schedule learning via Optimal Path (SLOP) for Efficient LLM Pre-Training

- Decision: Reject
- Scores: 8, 6, 6, 3

## Abstract
Existing training methods for Transformer-based large language models (LLMs) rely on massive amounts of data training from scratch, which requires a high cost in terms of compute and time. Recent studies have demonstrated the great potential of improving the LLM’s training efficiency by growing from small pre-trained models to large ones—a technique known as model growth. There are two main research problems associated with model growth: growth schedule and growth operators. Existing research focuses on growth operators, detailing specific manipulations of potential dimensions to expand Transformer parameters. Few studies have investigated the optimal growth schedule, which involves integrating all possible growth operators to create an optimal multi-staged growth path. This work introduces SLOP, a growth Schedule Learning methodology via Optimal Path, for multi-stage growth of models with minimal experimental training. SLOP utilizes marginal utility as an appropriate measure for an optimal schedule that balances training costs and model performance after multi-stage growth. With this measurement, the objective of determining the optimal model growth path is converted into a dynamic programming problem, which is then addressed mathematically in polynomial time. Empirical results demonstrate SLOP's theoretical validity and show that it is an efficient approach that outperforms alternative schedules in a variety of settings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a method to incrementally grow a larger model from a smaller model. The authors do so by measuring marginal utility at each stage. They test their method on three LLMs on a well known benchmark.

### Strengths
- It is a mature work that seems to be mathematically derived. The proofs are mature and solid and the results are good. 
- putting structure on model growth is an art rather than a science, and the authors have done a good job at trying to propose a good local optimization.

### Weaknesses
 - missing more than one LLM in experiments 
- missing code, limitations, future work sections
- I’m not sure why change in t ⇔ change in params 
- Does this bias your algo towards operators that incur the lowest growth in params?
- Have you considered picking a math symbol for “params”? (It’s not theta, is it?)
- I understand the broad strokes of your proof, but there is enough difficulty in notation and skipped steps that its hard to agree with it outright. Perhaps more explanation or reminders of the terms would be helpful. 
- By your pseudocode, this algo appears greedy to an extent (always choosing the vertex satisfying the minimum distance.) Can you comment on this? Have you considered inserting noise? 
- There are some dimensions that you haven’t considered (whether to train in sparsity to layers, modularity in layers wrt attention type, and perhaps some parameter quantization dimension), does this technique extend to them? 
- I’m not sure what the starting model was and/or architectural decisions were. Are you borrowing an uninitialized Llama structure? Or are you starting so much from scratch that you’re just starting at a basic transformer? 
- You have not included code, as far as I can see 
- Results look good. What are the limitations of your work? Future steps? 
- Overall readability is not so good. I would recommend at least passing this through ChatGPT!

### Questions
- Model growth as a way to lessen the burden of training compute / time. Could be very significant as far as pretraining is concerned.  
- “At each stage, one dimension is expanded to develop an intermediate structure until the 
entire target LLM structure is attained.” – is dimension really the right term for the growth target?  
- I’m not sure why change in t ⇔ change in params 
- Does this bias your algo towards operators that incur the lowest growth in params? 
- Have you considered picking a math symbol for “params”? (It’s not theta, is it?)
- I understand the broad strokes of your proof, but there is enough difficulty in notation and skipped steps that its hard to agree with it outright. Perhaps more explanation or reminders of the terms would be helpful. 
- By your pseudocode, this algo appears greedy to an extent (always choosing the vertex satisfying the minimum distance.) Can you comment on this? Have you considered inserting noise? 
- There are some dimensions that you haven’t considered (whether to train in sparsity to layers, modularity in layers wrt attention type, and perhaps some parameter quantization dimension), does this technique extend to them? 
- I’m not sure what the starting model was and/or architectural decisions were. Are you borrowing an uninitialized Llama structure? Or are you starting so much from scratch that you’re just starting at a basic transformer? 
- You have not included code, as far as I can see 
- Results look good. What are the limitations of your work? Future steps? 
- Overall readability is not so good. I would recommend at least passing this through ChatGPT!

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This study introduces an approach to model growth schedules for transformer-based large language models (LLMs). Unlike existing work that primarily focuses on the growth operators, this approach explores multi-stage growth schedules where each stage systematically expands various dimensions of the model—layer count, multi-head attention, feed-forward network dimensionality, and hidden layer size. The proposed method, Schedule Learning via Optimal Path (SLOP), borrows the concept of marginal utility from economics to determine an optimal schedule that balances training costs and model performance after each growth stage. By applying this measure, the problem of finding the best growth path is framed as a dynamic programming task, which is efficiently solved in polynomial time using an optimal path algorithm. Empirical results demonstrate that SLOP enhances key performance metrics such as loss and perplexity while also reducing overall training time. This suggests that SLOP can lead to more cost-effective training processes without compromising and even improving model performance.

### Strengths
Originality: Unlike traditional approaches that focus on growth operators, this work takes a unique approach by studying growth schedules. By framing model growth as a pathfinding problem guided by the marginal utility of each stage, the study provides a method to expand model size with reduced perplexity and without increasing training costs. This approach offers a fresh perspective on optimizing model development, shifting the focus from how models grow to when and in what order they expand.

Quality: The technical quality is solid, with thorough development and clear analysis of the proposed methods. The empirical results support the authors' claims about the efficiency and effectiveness of their approach in optimizing growth schedules.

Clarity: The paper is well-organized and clearly written, with coherent explanations of the background, literature, methodology, experimental setup, and results. This structure enhances readability and helps convey the research contributions effectively.

Significance: This research is significant for its potential to reduce the computational burden of trial-and-error training in an exponentially large search space. By optimizing growth schedules, the study provides insights that could make model training more cost-effective and accessible, which is particularly impactful for scaling large language models.

### Weaknesses
1) On the Choice of Target Structure in Table 2
It’s unclear why the authors chose only one target structure (2816, 7680, 8) for evaluation. This raises the question of whether the proposed method can be generalized to other target structures with different dimensions. It would be helpful for the authors to either justify this choice or provide additional experiments demonstrating the method's adaptability to a variety of target structures. This would help show that the approach is not limited to a specific configuration and can be applied more broadly.

2) Inflexible Target Structure
The current approach relies on a predefined target structure. Instead, could it be possible to allow the model to grow flexibly within a given duration 𝑇 and without a fixed target structure? This would enable the model to expand within computational budgets while still achieving satisfactory performance.

Minor Comments:
1) Font Size in Figures
The font size in almost all figures is too small, making it difficult for readers to follow the visual data and conclusions. Increasing the font size, especially in key charts and illustrations, would improve readability and accessibility, allowing readers to better understand and interpret the results presented.

### Questions
1) Correlation Between Training Times in Figure 3
The relationships between training times across different schedules in Figure 3 seem unclear, making it challenging to interpret. Providing a more detailed description and analysis would help readers understand how training time varies across different growth schedules and how it correlates with performance. This additional analysis could include specific comparisons or visual indicators to make the trends easier to follow.

2) Possibility of Finer-Granularity Stages
A question remains on whether the current approach supports finer-grained growth stages, such as incrementally increasing the layer count at each stage. Exploring this would add flexibility to the model growth process, potentially allowing smoother transitions and more granular control over resource allocation at each stage. Clarifying whether the method could accommodate such finer stages would help readers understand its adaptability to different training strategies on model growth schedules.

3) Details on Measuring GPU Wall Time
It is unclear how GPU wall time was measured across different stages. Specifically, what are the defined start and end times for each stage? Providing this information will clarify how the measurement was conducted and ensure the results can be reproduced accurately.

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
This paper presents SLOP, a methodology for determining optimal schedules for growing smaller pre-trained language models into larger ones through multi-stage expansion. The key contribution is formulating the schedule optimization as a dynamic programming problem that balances training costs and model performance. The authors show how marginal utility (basically ratio of performance to time spent training) can be used as an appropriate measure for finding optimal schedules theoretically, without requiring extensive experimental training. Specifically, starting from a smaller model, this technique, scales (in stages) the model to a larger size (by altering number of layers layers, multi-head attention , feed-forward network , and hidden states). This is validated by growing the model from 100M to 1B parameters in 5-stages. 

The core idea can be visualized as a graph problem where each "node" represents a possible model configuration (with specific hidden dimensions, FFN dimensions, layers, heads), and the "edges" represent the growth operations to transition between configurations. The "weight" of each edge corresponds to the number of parameters added by that growth operation. The intuition here is that the last numbers of parameter change are proportional to the least compute required.

### Strengths
1. The technical approach has merit in its mathematical formulation, showing how schedule optimization can be reformulated as a dynamic programming problem.
2. Theoretical work for optimizing model growth schedules that moves beyond empirical approaches.
3. Well-motivated use of marginal utility as an optimization metric that effectively connects model performance with training costs.

### Weaknesses
1. Limited number of growth stages (5) constrains the practical applicability of the approach. The current design restricts the exploration of more complex growth trajectories, which might be necessary for optimal scaling in diverse scenarios. This limitation is particularly relevant given the potential for diminishing returns with each stage, making it crucial to investigate more granular growth schedules.
2. Evaluation focused primarily on one architecture (GPT-2) despite broader claims about transformer-based LLMs. The lack of experiments on other architectures, such as encoder-decoder models or models with different attention mechanisms, raises concerns about the generalizability of the findings. The performance of the proposed method may vary significantly across different transformer variants due to architectural differences.
3. Choice of initialization size (100M parameters) may miss important dynamics that could be studied at smaller scales (e.g., starting from 10M parameters). The behavior of model growth might be different at smaller scales, where the initial parameter count could influence the subsequent growth trajectory. Exploring different initialization sizes could reveal interesting insights into the early stages of model growth.
4. Lack of justification for downstream task selection - the paper would benefit from comparing its evaluation tasks with those used in related work (e.g., MSG and ELLE etc). The absence of a clear rationale for the chosen downstream tasks makes it difficult to assess the relevance and impact of the results. A comparison with tasks used in similar studies would provide a better context for evaluating the performance of the proposed approach.
5. Unclear explanation of how Cost/Time relates to number of parameters in the marginal utility calculations. The paper lacks a detailed explanation of how the cost/time relationship is modeled, which is crucial for understanding the marginal utility calculations. The relationship between training time and parameter count is often non-linear and depends on various factors, such as hardware and optimization techniques.
6. Figure 1 needs significant improvement to better illustrate the growth process. The current figure does not effectively convey the growth process, making it difficult for readers to understand the proposed methodology. A more detailed and visually clear representation of the growth stages would be beneficial.
7. The hardcoding of head numbers may limit adaptability to different architectures. The fixed number of attention heads may not be optimal for all architectures, potentially limiting the adaptability of the proposed method. The optimal number of heads can vary depending on the specific architecture and task.

### Questions
1. Why was the number of stages limited to 5? Could the approach be extended to handle more stages?
2. Would the results hold if experiments were conducted starting from smaller models (e.g., 10M parameters)?
3. How does the approach generalize to different transformer architectures beyond GPT-2?
4. Could you provide more details on how the Cost/Time relationship in MUS was determined?
5. What was the rationale for selecting the specific downstream tasks used in evaluation?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
To reduce the computational cost of pre-training LLMs, current methods start with a smaller model and gradually increase its size (e.g., by expanding the hidden size or adding layers) until reaching the target parameter count. This paper addresses how to design an optimal schedule for growing model size within this framework. The authors propose minimizing total marginal utility, specifically focusing on the overall decrease speed in perplexity across stages. After theoretical derivations, they simplify the problem to minimizing total parameter changes. Experimental results suggest that this approach reduces pre-training costs while achieving comparable or better PPL.

While the paper's motivation and approach are novel, there are several concerns regarding the formulation, theoretical derivations, and the main algorithm. In its current form, I hold a negative suggestion.

### Strengths
* This paper explores a significant question, presenting a clear motivation and novel perspective. The authors have conducted a thorough review of related work. Up to Section 3.2, the paper is generally well-written and easy to follow.

### Weaknesses
 * **Formulation**. It is unclear why the authors limit the model to four stages and restrict each stage to only one growth operator. According to the objective in Eq.10, the cost decreases as the number of stages increases. Additionally, applying multiple growth operators in each stage is manageable—if there are four possible growth dimensions, there are only 15 compound operations in total, which is not prohibitively complex. The authors do not justify why they restrict the model growth to a single dimension per stage, which significantly limits the practical applicability of their method. This restriction prevents the method from exploring more complex growth patterns that could potentially lead to better performance or more efficient training. For example, simultaneously increasing the hidden dimension and the number of attention heads might be more beneficial than growing them sequentially. The lack of a rationale for this design choice is a major weakness.

* **Derivation**. I have concerns about the derivation on Page 5. Beyond some notational issues, my main concern is with the equivalence in Eq.3 and Eq.5. I could not understand Eq.3, and the paper or appendix lacks an explanation. In Eq.5, $\arg\max$ yields a $\phi_k$, but the right side subtracts two $\phi_k$s. The subtraction is undefined. Furthermore, maximizing an upper bound does not necessarily optimize the original objective, making the relaxation in Eq.5 questionable. The authors attempt to maximize the marginal utility by maximizing an upper bound, which is not mathematically sound. The derivation of Eq. 5 is flawed because it uses an inequality as an equivalence. The right-hand side of the equation represents an upper bound, and maximizing this upper bound does not guarantee the maximization of the original objective. The paper lacks a clear explanation of why this relaxation is valid, and the use of the equivalence symbol is misleading. The authors should clarify the relationship between the upper bound and the original objective, and justify why optimizing the upper bound is a reasonable approach.

I can hypothesize the authorss intended approach: starting with the RHS in Eq.3, applying a logarithmic function, and leveraging concavity. However, I still find Eq.3 unclear and would appreciate further clarification.

* **Algorithm**. Based on Figure 1, the optimal growth path resembles an application of the Viterbi algorithm, with complexity O(V+E) following the notation in line 286, which is lower than that of Algorithm 1. Additionally, Algorithm 1 may not be a dynamic programming approach, contrary to the claim in the abstract. The authors claim that Algorithm 1 is a dynamic programming approach, but it is not clear how it satisfies the overlapping subproblems property. The algorithm appears to be more akin to a greedy approach, which may not guarantee the global optimum. The authors should provide a more detailed explanation of how Algorithm 1 fits the dynamic programming paradigm, or clarify why a greedy approach is sufficient for this problem. The search space is relatively small, and a brute-force approach would be sufficient, making the use of a more complex algorithm unnecessary.

* **Experiments.** It is challenging to interpret the experimental results, particularly in Figures 2 and 3, where the x and y-axis values and meanings are unclear. While the authors state that they initialized a tiny model configuration randomly, it would be more rigorous to test alternative initial architectures of the same size. Otherwise, the results in Table 1 might appear cherry-picked. The experimental results are difficult to interpret due to the lack of clarity in the figures. The authors should provide more details about the experimental setup, including the specific model architectures, training parameters, and evaluation metrics. The choice of a random initial model configuration is not rigorous, and the authors should consider testing their method with different initial architectures of the same size to ensure the robustness of their results. The results in Table 1 could be biased due to the specific choice of initial model configuration.

In Table 2, the proposed method shows only marginal improvement over MSG, suggesting that the paper's contribution may be limited. The authors should also evaluate baseline models on downstream tasks, as shown in Figure 4.

### Questions
* Definition 1 is unclear. Given a compute budget, why is there a need to minimize compute power? What exactly is the variable in this problem—only the growth operator sequence, or does it also include training time for each stage?

* Please clarify why the number of stages is limited to 4.

* Please explain in detail why Eq.3 is valid.

* Does $\delta t$ represent wall time or GPU time?

* The use of \Leftrightarrow implies total equivalence, which does not seem to hold in Eq.5.

* Given the current formulation, where the search space is limited, why is Algorithm 1 necessary? Brute-force enumeration should be sufficient.

* In Table 1, there is an inconsistency between the calculated $\delta$ parameters and the actual GPU hours, particularly in the 4th and 7th rows. Could you explain this discrepancy?

* The authors state, "It is obviously impractical to traverse each schedule and select the final optimal one." Could you provide a concrete example of the search space (i.e., |V| and |E|) to demonstrate why this is impractical?

### Soundness
2

### Presentation
2

### Contribution
2
