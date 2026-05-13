# A Drop-In Solution for On-the-Fly Adaptation of Speculative Decoding in Large Language Models

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Large Language Models (LLMs) are cutting-edge generative AI models built on transformer architecture, which tend to be highly memory-intensive when performing real-time inference. Various strategies have been developed to enhance the end-to-end inference speed for LLMs, one of which is speculative decoding. This technique involves running a smaller LLM (draft model) for inference over a defined window size, denoted as $\gamma$, while simultaneously being validated by the larger LLM (target model). Choosing the optimal $\gamma$ value and the draft model is essential for unlocking the potential of speculative decoding. But it is difficult to do due to the complicated influence from various factors, including the nature of the task, the hardware in use, and the combination of the large and small models. 
This paper introduces *on-the-fly adaption of speculative decoding*, a solution that dynamically adapts the choices to maximize the efficiency of speculative decoding for LLM inferences. As a drop-in solution, it needs no offline benchmarking or training. 
Experiments show that the solution can lead to 3.55-16.48\% speed improvement over the standard speculative decoding, and 1.2-3.4$\times$ over the default LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces an "on-the-fly" adaptation technique for speculative decoding in large language models (LLMs), aiming to reduce inference latency dynamically without requiring prior model-specific training or offline benchmarking. The authors propose a framework that selects optimal parameters for speculative decoding during runtime, specifically the draft model and speculation window size γ. By leveraging adaptive techniques such as online optimization, finite state machines, cache-enhanced FSMs, and reinforcement learning, the approach achieves up to 3.4× speed improvements over default autoregressive decoding and outperforms standard speculative decoding methods by 3.55% to 16.48%.

### Strengths
1. Practical Contribution: The paper presents a solution for a well-acknowledged challenge in LLM inference—latency. By offering a drop-in solution for dynamic adaptation, this work has significant practical value, especially for real-time applications in large-scale deployment scenarios.

2. The adaptive approach bypasses the need for extensive offline training and tuning, unlike some previous methods. This makes it easier to adopt in diverse settings where the underlying hardware, model, and task configurations may vary frequently.

3. The paper effectively articulates the limitations of static speculative decoding parameters and demonstrates the need for an adaptive, flexible approach to speculative decoding.

### Weaknesses
Scope for Enhanced Comparative Analysis: The paper covers multiple adaptive techniques to optimize speculative decoding, but a broader comparative analysis could provide more clarity. Highlighting conditions where each method performs best would further aid in understanding the practical strengths and limitations of each approach, helping readers assess their applicability across diverse scenarios.

### Questions
How scalable are the adaptive methods presented, Further clarification on scalability could help evaluate the practicality of these techniques in diverse deployment scenarios.

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
3

### Summary
This paper introduces solutions to optimize speculative decoding configurations on the fly. For window size, the paper proposes online window size optimization based on speculative accuracy estimation, FSM, or RL. For the choice of the draft model, the paper proposes the estimation of speculative accuracy estimation from various factors. Therefore, the configurations can be dynamically adjusted between speculative decoding steps based on history.

Experimental results over various devices and benchmarks demonstrate speed improvements compared with the standard speculative decoding and a speed-up compared with default decoding procedures.

### Strengths
1. The idea of adjusting window size and draft model dynamically in the decoding process is novel and can be helpful in maximizing the decoding speed, especially when the speculation accuracy varies in the generation process. 

2. The cost of the estimation method is rather small, making it easy to integrate with existing speculative decoding methods.

### Weaknesses
1. The improvement is somehow marginal. The window size selection method generally achieves improvements of less than 10% and less than 1% in some cases. The proposed draft model choice method leads to less than 1% improvement in many cases.

2. The method is only tested in domain-specific tasks (math/code/finance QA/summarization) and is not evaluated on comprehensive chat datasets like `ShareGPT`, which raises questions about its applicability to realistic chat scenarios.

### Questions
1.  What is the value of window size $\gamma$ for the standard speculative decoding baseline? Is the window size $\gamma$ for the standard speculative decoding baseline in each dataset set as the optimal value obtained by searching through all possible fixed $\gamma$ values?

2. `BLOOM` models achieve \~70% throughput improvement in `xsum` dataset, while having no speed-up compared with default LLMs without speculative decoding. Why is this throughput improvement so high compared with others (\~10%)?

3. Is it possible to provide results on a comprehensive chat dataset?

Minor:

4. How is the vector embedding of a prompt calculated (like $u$ in line 321 and $b$ in line 347)?

5. What is `online predictive model construction` in line 382?

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
This article primarily focuses on accelerating inference for LLMs. It represents an improvement over existing speculative decoding methods by dynamically adjusting the speculation window length and selecting different draft models.

### Strengths
1. This paper is well-written; the author has explained their motivation and methods in detail.
2.The article analyzes the factors influencing the acceleration of large models through speculative decoding, using rigorous formula derivation, and demonstrates the importance of employing dynamic sampling windows and dynamically selecting the draft model.
3. The article conducted ample experiments to demonstrate the effectiveness of their method.

### Weaknesses
1. Baselines seem especially weak and some other baselines are not compared. For example, Medusa and EAGLE, they are currently popular approaches that has been compared in numerous papers; all of these methods utilize speculative decoding techniques and demonstrate strong performance.
2. Although I find the concept of a dynamic speculation window size intriguing, I am skeptical about its practical application value. Recent studies have already adopted tree attention or tree decoding-related technologies, they do not require a speculation window size and have achieved significant speedup. Could you discuss how your approach compares with, or could potentially be integrated into, tree attention or tree decoding technologies?   
3. In my understanding, Table 2 presents the results using adaptive window size selection, and Table 3 presents the results using draft model selection. Why not conduct an experiment to show the results of using both techniques simultaneously? Additionally, could you specify which draft model was used for the 'w/o draft selection' condition in Table 3?

### Questions
1. Baselines seem especially weak and some other baselines are not compared. For example, Medusa and EAGLE, they are currently popular approaches that has been compared in numerous papers; all of these methods utilize speculative decoding techniques and demonstrate strong performance.
2. Although I find the concept of a dynamic speculation window size intriguing, I am skeptical about its practical application value. Recent studies have already adopted tree attention or tree decoding-related technologies, they do not require a speculation window size and have achieved significant speedup. Could you discuss how your approach compares with, or could potentially be integrated into, tree attention or tree decoding technologies?   
3. In my understanding, Table 2 presents the results using adaptive window size selection, and Table 3 presents the results using draft model selection. Why not conduct an experiment to show the results of using both techniques simultaneously? Additionally, could you specify which draft model was used for the 'w/o draft selection' condition in Table 3?

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
4

### Summary
The paper introduced an online optimal speculation length scheduling approach for efficient speculative decoding. It first proposes an objective, as in Eq. 1, to formally capture the speculation accuracy and latency tradeoff. Given the objective, an accurate estimation of speculative/verification latency and speculation accuracy is required. For a single draft model, the authors propose to use a history window to estimate the latency through online profiling and the speculation accuracy through MLE. For selection among multiple draft models, the authors further propose a parametric method with a linear model to predict the speculation accuracy for different draft models. Empirically, the paper shows that their approach can consistently outperform SpecDec++ over various target models and datasets.

### Strengths
1. The problem of adaptive speculation length is well-motivated as the overhead of speculation is non-negligible. As the paper indicated, an over-optimistic speculation length would have a high overhead if there is an early mismatch, and an over-conservative speculation length would result in fewer speed-up potentials. 
2. Though the objective formulation and history-based parameter estimation are not new and similar as in [1], the problem focus is slightly different ([1] is not focusing on the general LLM speculative decoding), so the formulation can be of interest to the general LLM speculative decoding audience. 
3. Using a linear system to model the speculation accuracy across different draft models is new.

**reference**

[1]. Zhang, Z., Zhu, A., Yang, L., Xu, Y., Li, L., Phothilimthana, P. M., & Jia, Z. Accelerating Iterative Retrieval-augmented Language Model Serving with Speculation. In Forty-first International Conference on Machine Learning.

### Weaknesses
1. The paper's approach only works for speculative decoding with a single sequence, while the current state-of-the-art practice is doing speculation with a **tree-based** structure. More specifically, [1] can achieve up to 3.01x speed-up for LLaMA-2-70B and 3.51x speed-up if dynamically adjusting the draft tree structure is further incorporated as in [2], both of which have outperformed the speed-ups claimed in the paper. The single-sequence approach inherently limits the potential speedup compared to tree-based methods, which can explore multiple speculative paths concurrently. This is a major limitation as it does not address the most performant methods currently used in practice.
2. In practice, the verification latency is usually not constant but depends on the speculation structure to be verified, so it would be more accurate to verify the property of verification latency under various speculation structures and formulate the latency of verification as a function of the speculation structure, e.g., sequence length in a single-sequence speculation structure or width and depth for a tree-based speculation structure. The verification latency can be influenced by factors such as the number of tokens being verified, the depth of the tree, and the specific hardware being used. Ignoring these factors can lead to inaccurate latency estimations and suboptimal performance.
3. As the prediction accuracy for the linear system to estimate draft model speculation accuracy is pretty critical, a more comprehensive ablation study on the choices of different linear models (e.g., different random variables or different vector lengths) is crucial for understanding how you chose the optimal linear system among different possible configurations. The choice of features and model complexity can significantly impact the accuracy of the speculation accuracy estimator, and a thorough investigation is needed to justify the chosen configuration.

### Questions
My main question is why focusing only on single-sequence speculation rather than the tree-based speculation structure, which is the current best practice for speculative decoding. More specifically, how does your approach compare with **EAGLE-2**, which leverages a similar idea (adaptive speculation) but on draft trees rather than a single speculation sequence, which results in a much higher speed-up rate? The simplicity of your solution can be a bonus if it can be generalized to tree-based speculation and achieve a higher speed-up than EAGLE-2. 

Some minor suggestions:

1. Try formulating the verification latency as a function of the speculation structure from a more systematic perspective. For example, make it a function of the speculation sequence length or speculation tree structure, this may also depend on the underlying hardwares' specifications.
2. Include some ablation studies to show how different configurations affect the effectiveness of the speculation accuracy estimator. For example, how different $h$ (recent history length) values can affect your speculation accuracy prediction for online window size optimization, and how different linear model (different vector lengths or random variables) can affect your speculation accuracy prediction for estimating the speculation accuracy for different draft models.

### Soundness
3

### Presentation
2

### Contribution
1
