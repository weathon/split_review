# Learning Loss Landscapes in Preference Optimization

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
We present an empirical study investigating how specific properties of preference datasets, such as mixed-quality or noisy data, affect the performance of Preference Optimization (PO) algorithms. Our experiments, conducted in MuJoCo environments, reveal several scenarios where state-of-the-art PO methods experience significant drops in performance. To address this issue, we introduce a novel PO framework based on mirror descent, which can recover existing methods like Direct Preference Optimization (DPO) and Odds-Ratio Preference Optimization (ORPO) for specific choices of the mirror map. Within this framework, we employ evolutionary strategies to discover new loss functions capable of handling the identified problematic scenarios. These new loss functions lead to significant performance improvements over DPO and ORPO across several tasks. Additionally, we demonstrate the generalization capability of our approach by applying the discovered loss functions to fine-tuning large language models using mixed-quality data, where they outperform ORPO.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates how preference optimization (PO) algorithms perform under varying conditions of data quality. Through empirical experiments primarily in MuJoCo environments, the authors examine the weaknesses of state-of-the-art PO methods like Direct Preference Optimization (DPO) and Odds-Ratio Preference Optimization (ORPO) when working with noisy or low-quality data. They propose a novel PO framework based on mirror descent to generalize existing PO methods and employ evolutionary strategies to identify optimal loss functions that could address identified performance issues. Results demonstrate that these new loss functions improve PO algorithm performance, even in fine-tuning tasks with large language models (LLMs).

### Strengths
1. The paper introduces a novel framework for loss optimization using mirror descent, which effectively addresses common issues in preference datasets.
2. The study includes well-designed experiments across various data settings.
3. The flexibility of the method across different application domains.

### Weaknesses
1. While the methodology is empirically validated, a deeper theoretical analysis, particularly around robustness and generalizability, would strengthen the findings. Specifically, the paper lacks a rigorous analysis of the convergence properties of the mirror descent framework under different noise conditions and how the choice of mirror map affects the stability of the optimization process. Furthermore, the theoretical underpinnings of the discovered loss functions are not fully explored, leaving open questions about their behavior in unseen scenarios.
2. The paper lacks a discussion on the computational cost of training with evolutionary strategies, especially for large models or in settings where data or compute resources may be constrained. The framework鈥檚 reliance on the computational complexity of evolutionary strategies might make it less practical. The paper should include a detailed analysis of the time and memory requirements for the evolutionary search, particularly in relation to the dimensionality of the loss function space and the number of parameters in the policy network. This is crucial for assessing the scalability of the approach.
3. The experimental settings focus primarily on MuJoCo, which, while diverse, may limit insights into real-world applications. Expanding beyond MuJoCo could improve the generalizability of results. The paper should include experiments on more complex and diverse environments, such as those involving visual inputs or more intricate reward structures, to demonstrate the robustness of the proposed approach. The current focus on MuJoCo may not fully capture the challenges of real-world preference learning tasks.


### Questions
1. How does the computational cost of this new framework compare with conventional PO methods in large-scale settings? Could efficiency trade-offs limit practical applications?
2. Are there specific criteria for choosing mirror maps or evolutionary strategies based on the characteristics of the preference dataset?
3. Could the approach be extended or adapted to reinforcement learning tasks beyond MuJoCo and language model fine-tuning? How would it perform in such settings?
4. More peer algorithms should be included for experimental comparison.

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
This paper proposed a new Preference Optimization (PO) framework . 

Overall, I think the novelty of this paper is limited.

### Strengths
This paper provide a theoretical way to study preference optimization (PO) and give both theoretical and empirical results.

### Weaknesses
This paper proposed a new Preference Optimization (PO) framework. 

Overall, I think the novelty of this paper is limited.

### soundness:
 3

### presentation:
 3

### contribution:
 3

### strengths:
 This paper provide a theoretical way to study preference optimization (PO) and give both theoretical and empirical results.

### weaknesses:
 Experimental results are a bit too weak. Others see questions.

### questions:
 1. Line 144. "A known issue of DPO is that it pushes probability mass away from the preference dataset and to
unseen responses". Is that true?

2. Line 133. Besides it computational costs, PPO is known to be prone to reward overoptimization. Is that true?

3. In which case DPO is better than RLHF, and which case RLHF is better than DPO. Is there an affirmative answer?

4. Line 240 to 242. Why these functions are considered?

5. As far as I understand, the proposed work try to change different Bregman distance. This is very similar to an ICLR work called "f-PO: Generalizing Preference Optimization with f-divergence Minimization". So, is there equivalence between each other? For example, by choosing a propose f divergence will yield a corresponding Bregman distance. I admit that choosing the Bregman distance is a clever idea.  However, what is the novelty becomes compared with FPO?

6. This paper mention "online " occurs a lot of times. What does it mean in preference optimization?

7. The experiments seems a bit weak. What is the performance on multi-modal model or 3B model?

### flag_for_ethics_review:
 ['No ethics review needed.']

### details_of_ethics_concerns:
 NA.

### rating:
 6

### confidence:
 3

### code_of_conduct:
 Yes

### Questions
1. Line 144. "A known issue of DPO is that it pushes probability mass away from the preference dataset and to
unseen responses". Is that true?

2. Line 133. Besides it computational costs, PPO is known to be prone to reward overoptimization. Is that true?

3. In which case DPO is better than RLHF, and which case RLHF is better than DPO. Is there an affirmative answer?

4. Line 240 to 242. Why these functions are considered?

5. As far as I understand, the proposed work try to change different Bregman distance. This is very similar to an ICLR work called "f-PO: Generalizing Preference Optimization with f-divergence Minimization". So, is there equivalence between each other? For example, by choosing a propose f divergence will yield a corresponding Bregman distance. I admit that choosing the Bregman distance is a clever idea.  However, what is the novelty becomes compared with FPO?

6. This paper mention "online " occurs a lot of times. What does it mean in preference optimization?

7. The experiments seems a bit weak. What is the performance on multi-modal model or 3B model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents an empirical study on preference optimization (PO) algorithms, focusing on how preference dataset properties affect performance. The authors introduce a novel PO framework based on mirror descent, which generalizes existing methods like DPO and ORPO. A new framework for algorithm discovery, and the demonstration of generalization to LLM tasks have been proposed.

### Strengths
The paper proposes a novel framework for preference optimization (PO) based on mirror descent, which generalizes existing methods like DPO and ORPO. This approach of using mirror maps to explore the space of PO algorithms and discover new loss functions is relatively new in the field.
The idea of using evolutionary strategies to search for the best mirror maps and thus new PO algorithms allows for an automated and potentially more efficient way of finding algorithms that can handle different dataset properties compared to traditional methods of manually designing algorithms.
The application of the discovered PO algorithms from MuJoCo environments to LLM fine-tuning tasks shows the potential and generalization of algorithms discovered in a simpler, more computationally tractable environment to a more complex and practical domain like LLM tuning.

### Weaknesses
The discovered loss functions are complex and parametrized by neural networks. There is no attempt to provide an intuitive interpretation of what these functions represent or how they relate to the properties of the preference datasets. This lack of interpretability makes it difficult to understand and potentially modify the algorithms for specific applications.
The theoretical derivations, such as Theorem 3.1, are based on simplified assumptions. The impact of relaxing these assumptions or considering more complex scenarios where they may not hold is not explored.
The LLM fine-tuning experiment uses a modified dataset to simulate mixed-quality data, but it would be beneficial to validate the proposed algorithms on real-world, large-scale LLM datasets.
While the paper identifies certain failure modes of ORPO and shows how the proposed algorithms address them, the discussion could be more comprehensive. For example, exploring why these failure modes occur in the first place and what implications they have for the broader field of preference optimization could provide deeper insights.

### Questions
1) In the Hopper and Ant/TLA environments, why were the specific numbers of rows chosen for the datasets (5120 for Hopper and 1280 for TLA)? How do these choices impact the representativeness and generalizability of the results?
2) The evolutionary strategies used to search for the best mirror maps and loss functions are computationally expensive. Have you considered any techniques to speed up this process or approximate the optimal solutions more efficiently?
3) The discovered loss functions are complex and parametrized by neural networks. How can we ensure the stability and reliability of these functions in different application scenarios?
4) The generalization of the discovered PO algorithms from MuJoCo to LLM tasks is demonstrated, but it is not clear how the differences in the nature of the two domains (e.g., discrete vs. continuous actions, different data distributions) are accounted for. Can you provide more insights into this?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper generalizes a recent variant of DPO, namely ORPO, by introducing two maps into the problem definition of ORPO. Then these maps are parametrized by a neural network that is trained by OpenAI-ES approach. An empirical study shows better performance than the original ORPO in some settings of noisy preference datasets and competitive performance in other settings.

### Strengths
It generalizes a recent and promising variant of DPO, namely ORPO, by introducing mirror maps.

Empirical evaluation shows that optimizing the parameterized mirror maps by OpenAI-ES sometimes results in better performance.

### Weaknesses
The position of this study among related studies has not been clarified. Several studies have investigated the preference optimization under noisy preferences and proposed variants of DPO, such as cDPO and rDPO. I see that the current paper is based on ORPO and hence the direct comparison may not be fully fair, but at the same time, I do not see the advantages of the current approach. On the other hand, there are several studies modifying the loss or the divergence in DPO such as IPO and f-DPO. The novelty of this study is not clearly stated among these related works. The literature review should cover these topics, however, in this paper, only f-DPO is mentioned in the related work as a generalization of DPO.

The motivation is not stated clearly. Why is the generalization of ORPO as in (10) and searching the introduced maps expected to improve the performance of ORPO for noisy preference datasets? I could not see the logic behind it. Because the logic is not provided, I do not see whether the experimental results are really associated with the generalization. Does this generalization contribute to the good performance? From the current experiments, I do not see whether the proposed approach is better than simply introducing some scalar factors to all terms in ORPO and optimizing them.

Reproducibility is not high. First, the proposed learning scheme for mirror maps is not clearly stated. It requires estimating the cumulative reward for each obtained policy, but how is it estimated in an offline manner (stated in Line 102)? Second, the code to reproduce the experiments is not available. Some details, such as the architecture of the policy network and temperature parameters.

Comparison to other approaches is missing. The proposed approach is compared only to the original ORPO, which is not designed to address noisy preference datasets. No comparisons with DPO variants such as rDPO specialized for noisy preference datasets are provided.

The overall framework of the proposed approach is still not clear. If I understand the response correctly, the agent can not access to the underlying MDP during the training. All it can access is the offline dataset. However, at the same time, the authors mentioned that the cumulative rewards were estimated online, meaning that it requires access to the underlying MDP. The estimation of the cumulative reward is required during the training phase to update the neural mirror maps. Therefore, it looks contradictory. Please correct me if it is wrong. If it requires both online and offline training, it will significantly limit the applicability of the proposed approach and providing example situations where the current setting is reasonable is required.

For the analysis of the obtained loss function, first, I would like to thank you for addressing my comment. However, no evidence for the statement “this closed-form expression effectively captures the behavior and …” was given and the reason for a good performance, in particular compared to ORPO, is not discussed. To claim the transferability, I suggest the authors to perform deeper analysis on the obtained loss function.

### Questions
Please address the questions given in the weaknesses section.

Additional comments are listed here:

Additional comments are listed here:

In the experiments in Table 1, what is the difference between setting a high temperature and adding a noise in this setting? They look like the same.

How is the temperature parameter in Table 2 set?

How are the obtained mirror maps interpreted? If it is transferable, shouldn’t the result be analyzed?

In line 222, it was not clear to me how these terms canceled out. Could you elaborate on the derivation?

### Soundness
1

### Presentation
2

### Contribution
1
