# Context-Aware Kernel Search for Bayesian Optimization with Large Language Models

- Decision: Reject
- Scores: 5, 6, 5, 8

## Abstract
The efficiency of Bayesian optimization (BO) relies on careful selection of the surrogate model to balance exploration and exploitation under limited budget. Traditional BO methods often struggle with sub-optimal kernel choices when using Gaussian processes (GPs) as the surrogate model. When the kernel is inadequately chosen, BO may converge slowly or even get stuck at an undesired local minimum. To address such drawback, we propose the novel Context-Aware Kernel Search (CAKES) to automate optimal kernel design in BO with large language models (LLMs). Concretely, CAKES exploits LLMs as crossover and mutation operators to adaptively generate and refine GP kernels based on the observed data. CAKES works entirely in-context and can be easily integrated into existing systems without requiring any fine-tuning. We further present a theoretical analysis demonstrating that our method achieves sub-linear regret relative to the budget for any input dimension. Experimental results demonstrate that CAKES outperforms various salient baseline methods in numerous synthetic and real-world optimization tasks. Notably, CAKES improves the overall performance on benchmark functions by roughly 36\%. In hyperparameter tuning tasks, CAKES can effectively leverage fewer data samples to quickly identify high-performing configurations and consistently ranks first across various datasets. As an encouraging real application, we successfully applied CAKES to design photonic chips,  achieving significant improvements in key performance indicators while speeding up the design cycle by a factor of ten compared to the baselines. Our code is accessible at https://github.com/cakes4bo/cakes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- This work proposes a large language model-based kernel design method for Bayesian optimization.
- Since the performance of Bayesian optimization depends on kernel choice, the kernel search is crucial.
- This work utilizes a large language model to select kernel design.
- The authors test their method in diverse benchmark functions.

### Strengths
- It shows an ability of large language models to understand natural language description in the problem of kernel search.
- Paper is generally well-written.

### Weaknesses
- More real-world benchmarks are missing.
- Some baseline results of photonic chip design might be missing.
- More recent baselines are missing.

### Questions
- My concerns are all related to experiments.
- I think that hyperparameter tuning tasks are involved with small simple models.  If more sophisticated models are tuned, it would be better.
- I don't know why only two baseline methods are compared to CAKES in photonic chip design.
- Some baselines such as (Malkomes and Garnett, 2018) should be compared.
- I think that few-shot learning is not correct in this context.  The authors didn't fine-tune large language models.  It should be few-shot prompting.
- Why did you use gpt-4o-mini only?  If other large language models such as gpt-4o and llama-3 are used, can the empirical results change?  And why did you choose a temperature of 0.7 and a top_p of 0.95 specifically?

### Soundness
2

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
The paper presents Context-Aware Kernel Search (CAKES), a novel method for optimizing Bayesian optimization (BO) by leveraging large language models (LLMs) to automate the design of Gaussian process (GP) kernels. CAKES addresses the challenge of sub-optimal kernel selection, which can hinder the efficiency of BO, by using LLMs as genetic operators to adaptively generate and refine kernels based on observed data. Theoretical analysis shows that CAKES achieves sub-linear regret, and experimental results indicate it outperforms existing methods across various optimization tasks, including hyperparameter tuning and photonic chip design, significantly improving performance and reducing design cycle times.

### Strengths
One of the key strengths of this paper is its innovative use of large language models (LLMs) for in-context learning to improve Bayesian optimization (BO). The Context-Aware Kernel Search (CAKES) method leverages LLMs' few-shot learning capabilities to adaptively generate and refine Gaussian process kernels based on observed data, without requiring any fine-tuning. 

Theoretical analysis indicates that CAKES achieves sub-linear regret relative to the budget for any input dimension. Experimental results demonstrate its superiority over baseline methods in various optimization tasks, including benchmark functions and hyperparameter tuning and photonic chip design.

### Weaknesses
Limited testing in high-dimensional spaces: The paper does not demonstrate the effectiveness of CAKES on high-dimensional optimization problems. This leaves uncertainty about how well the method scales to more complex search spaces with many variables.

### Questions
Same in weaknesses part

### Soundness
2

### Presentation
3

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
This submission proposes a novel context-aware kernel search (CAKES) for constructing surrogate models in Bayesian Optimization. CAKES replies on LLM to operate the proposed crossover and mutation method for kernel design. Evolutionary approach is adapted to construct new kernels for the GP models. Some theoretical analysis is presented to show a sub-linear regret bound of the proposed method. Experiments on benchmarks and real-world applications are performed to show CAKES outperforms other surrogate models in BO.

### Strengths
The paper is well structured and fluent to read. The idea of CAKES is well explained in this submission. Motivation for a novel surrogate model design method in BO is convincing. The usage of a developed and trained LLM without any fine-tuning in the few-shot learning setting of BO is new. Experiments consider both synthetic functions and real-world application that shows practical potential of CAKES.

### Weaknesses
1. This submission does not present adequate contributions in my opinion. The idea of kernel design using transformers and language models has been studied in the field. For example, Simpson et al. (https://proceedings.neurips.cc/paper/2021/hash/56c3b2c6ea3a83aaeeff35eeb45d700d-Abstract.html) proposed their transformer-based architecture for kernel design, and their model is specifically trained using a vocabulary of known kernels. The authors claim the "no need for fine tuning" as an advantage for their method, but feels more like the key weakness to me. Considering all the conditioning (line 193-194, 198-199) and numerical information (such as observations and kernel's characteristic) are fed to the LLM model purely through text prompt, CAKES's performance highly (or even entirely) depends on how familiar the chosen LLM model is with GP and kernel design. In addition, the crossover and mutation operators (line 227-234) utilize very standard kernel grammar and simple replacement, which are already well-developed techniques. 

2.  Experiments design is not very consistent. In section 6, the authors use 5 different metrics to measure the performance of methods in different experiments. Given the BO settings, I don't see a good reason for varying performance metric between different experiments when the authors could just simply select one. Simple regret is commonly used and more importantly consistent with the regret bound proven in section 4. The "average rank" metric presented in Table 2 seems to highlight the same information as the "average regret" plots in Figure 2.

### Questions
1. In line 406-408, the authors mention SE and Matern-5/2 as the two most commonly-used kernels. Why is Matern-5/2 kernel not included in the four base kernels defined in line 203 then?

2.  How do the authors define the values of number of crossovers $n_c$, probability of mutation $p_m$ and population size $n_p$ (line 163-165 in Algorithm 1) in final implementation?

3.  In line 235-236, the authors mention a brief analysis will be returned by the LLM model. Can the authors provide one actual example of such analysis?

4.  I'm a bit confused by the weighting strategy explained in line 242-243. Does it mean the most ideal kernel with very low BIC (thus low weight) and high acquisition value might not be selected while some worse kernel (higher BIC, lower acquisition value) might? Could the authors further justify the intuition behind such strategy?

5.  In Figure 2, what is "Best" (the fourth method in legend)? Does it refer to the "Utility" method in line 411?

6.  I notice the authors set the maximum number of function evaluation $T$ and number of replications using different random seeds quite small for their experiments. For the benchmark functions (section 6.1), $T = 10 d \leq 50$ since $\max d = 5$ for the chosen test functions. For the hyperparameter tuning tasks (section 6.2), $T=25$. Usually the value of $T$ will be larger (e.g. $50$, $100$) in BO experiments. Similarly the number of random seeds for each experiment (10 for section 6.1, 5 for section 6.2 and not mentioned for section 6.3) is relatively less than what people usually use (e.g. $20$, $25$). How many random seeds did the author use for experiment in section 6.3? Is the reason for such not very generous setting due to long generation time of kernel design?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Gaussian processes play a key role in Bayesian optimization, where the quality of the model heavily depends on the selection of the kernel type. This paper aims to address this selection issue with the assistance of large language models. Extensive experiments are conducted to verify the superior performance of their proposed framework.

### Strengths
The topic is compelling, as kernel design is crucial in Gaussian process modeling. The paper is well-written and easy to follow. The method's performance is excellent, potentially reducing the selection cost for BO practitioners.

### Weaknesses
- The presentation of the algorithm places too much emphasis on kernel search. However, BO is just one application of kernel design in Machine Learning. Therefore, I recommend the authors refine the presentation of this BO-specific method.
- The theoretical analysis is too simplistic and could apply to any adaptation method of kernel design, such as symbolic regression. LLM-related analysis may better describe the performance.

### Questions
- I am curious whether the setting of weights in photonic chip design, where the last three objectives are much more important than the first two, is a commonly recognized practice or carefully designed. This is particularly relevant as CAKES performs outstandingly well on the fourth objective but only fairly on the other objectives.

### Soundness
4

### Presentation
3

### Contribution
3
