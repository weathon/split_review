# SAIL: Self-improving Efficient Online Alignment of Large Language Models

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 8, 3

## Abstract
Reinforcement Learning from Human Feedback (RLHF) is a key method for aligning large language models (LLMs) with human preferences. However, current offline alignment approaches like DPO, IPO, and SLiC rely heavily on fixed preference datasets, which can lead to sub-optimal performance. On the other hand, recent literature has focused on designing online RLHF methods but still lacks a unified conceptual formulation and suffers from distribution shift issues.  To address this, we establish that online LLM alignment is underpinned by bilevel optimization. By reducing this formulation to an efficient single-level first-order method (using the reward-policy equivalence), our approach generates new samples and iteratively refines model alignment by exploring responses and regulating preference labels. In doing so, we permit alignment methods to operate in an online and self-improving manner, as well as generalize prior online RLHF methods as special cases. Compared to state-of-the-art iterative RLHF methods, our approach significantly improves alignment performance on open-sourced datasets with minimal computational overhead.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Compared to offline RLHF methods, online RLHF methods empirically show stronger performance, yet is computationally expensive, vulnerable to distribution shifts and lacks a unified framework. The authors ablate different online RLHF methods based on all possible combinations (namely, SAIL-PR, SAIL-PP, SAIL-DP) which could be useful for future work exploring online RLHF methods. Personally, it was surprising that SAIL-PP generally works on par or slightly better than SAIL-PR, which open up further research questions on what would be the optimal way to obtain preference dataset.

### Strengths
* The authors test of two LLM-as-a-Judge benchmarks as well as on a well-established classification benchmark, and their results are consistent.
* The authors provide a theoretical explanation of why their method works effectively.
* Showing all possible combinations at Figure 2 helped understanding what kind of online RLHF methods one should consider
* The results are consistent across smaller models (0.5B) up to widely used scale models (8B).

### Weaknesses
 * As a practitioner, at least the presentation/writing wasn't clear enough to agree that SAIL provides a unified framework for those who might want to consider using online RLHF in future works. I would personally suggest adding a section explains about how one could use SAIL instead of iterative DPO methods, as well as a huge emphasis on how the provided code could be used.
* There is a huge emphasis on trying to improve reward models (on RewardBench) to mitigated reward model overoptimization & train better LMs. I am curious if given a fixed budget/time limit, whether one should try to employ online RLHF methods or try to enhance reward models in general.
* I would suggest adding an explanation of what is the limitation of online RLHF methods that the paper could not address. For example, it is still unclear on what is the best practice to "whether to discard instances from a preference dataset that have a subtle difference on the preference strength" or "would it be beneficial to employ more models when gathering responses when consisting a preference dataset".

### Questions
* Reward margin and offline-reward evaluation is interesting by itself and could provide information of the effectiveness of the method, but I personally think is not as an important measurement as pairwise winrate. Could you elaborate on Section 6.1 why one should consider looking into it?

* Please check the questions in weaknesses as well!

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors identify three significant challenges in online RLHF algorithms: Challenge 1: the interdependence between models and data in implicit reward learning; Challenge 2: the computational complexity of bi-level optimization; and Challenge 3: the reliance on preference oracles. They propose SAIL to address these challenges. 

The main contributions of the paper can be summarized as follows:

1. **Unified LLM Alignment Mathematical Framework**: The authors have designed a principled online RLHF framework that provides concrete guidance for generating new responses, assuming the existence of a preference oracle.

2. **Adaptive Direct Preference Optimization**: By introducing a DPO-style analysis, the authors present an efficient single-layer solution capable of effectively addressing distribution shifts and providing a scalable online preference optimization method.

3. **Introduction of a Self-Improvement Mechanism**: This mechanism reduces the reliance on preference oracles.

4. **Extensive Experimental Evaluation**: The experiments conducted demonstrate that SAIL significantly outperforms baseline methods.

### Strengths
1. Introducing Bi-level Preference Optimization: The process of bi-level preference optimization is integrated into the modeling of online RLHF. By leveraging the unique correspondence between the reward function and the LLM policy, this approach innovatively transforms the process into an equivalent single-layer form that is easier to solve.

2. Extensive Experiments on SAIL: Comprehensive and rich experiments were conducted to address the three significant challenges in online RLHF and to demonstrate the relevant applications of SAIL.

### Weaknesses
Regarding the three variants of the SAIL method, Table 3 shows that in the Eval-Reward and MT-bench columns, the SAIL method performs worse than the baseline DPO. Please clarify whether these experimental results undermine the assertion that the SAIL method is superior to the baseline DPO.

There is a large amount of blank space below Section 6.1. Is there any missing content in this part of the paper?

### Questions
There is a large amount of blank space below Section 6.1. Is there any missing content in this part of the paper?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces SAIL (Self-improving Efficient Online Alignment), an approach for online reinforcement learning from human feedback (RLHF) that aims to align large language models (LLMs) with human preferences. SAIL addresses limitations in offline RLHF methods by framing online LLM alignment as a bilevel optimization problem, which it reduces to a single-level first-order optimization method to enhance computational efficiency. The approach allows for continuous model improvement by generating samples iteratively, regulating preferences, and exploring online feedback. SAIL's self-improvement mechanism enables it to reduce reliance on preference oracles, thus allowing for more scalable alignment. Empirical evaluations demonstrate significant performance improvements over standard RLHF baselines.

### Strengths
1. **Innovative Formulation**: The paper provides a novel formulation of online RLHF through bilevel optimization, enhancing computational efficiency by reducing this problem to a single-level optimization, which is a significant advancement for practical LLM training.
2. **Effective Self-improvement Mechanism**: SAIL effectively addresses challenges related to reliance on preference oracles, making online alignment more feasible by leveraging the model's self-generated responses for iterative improvement.
3. **Comprehensive Evaluation**: The paper includes extensive experiments that demonstrate substantial improvements in evaluation reward, win rate, and efficiency over other methods like DPO, supporting SAIL's efficacy and computational advantage.
4. **Scalability and Adaptability**: SAIL’s approach to handling distribution shifts and reducing oracle reliance presents a promising method for more scalable RLHF applications, especially for emerging large-scale LLMs.
5. **Detailed Experiment Design and Baselines**: The experiment section is well-structured, covering a range of metrics (reward-margin, eval-reward, win rate) and configurations (SAIL-PR, SAIL-PP, SAIL-DP), providing insights into the trade-offs and performance across different setups.

### Weaknesses
1. **Limited Exploration of Alternative Utility Functions**: The method relies on the Bradley-Terry preference model, which may not be optimal for all RLHF applications. The Bradley-Terry model assumes a specific form of pairwise comparison that might not capture the full complexity of human preferences, particularly in scenarios where preferences are not strictly transitive or where the intensity of preference varies significantly. Future work could benefit from exploring alternative utility models that account for more nuanced preference data, such as models that incorporate context-dependent preferences or those that allow for non-deterministic preference structures.
2. **Scalability Concerns for Larger Models**: Although the paper demonstrates SAIL’s effectiveness on LLMs with up to 8B parameters, additional scaling experiments would strengthen the paper's claims about computational efficiency for significantly larger models. The computational overhead of generating responses and evaluating rewards online could become a bottleneck when scaling to models with hundreds of billions of parameters, potentially negating the efficiency gains from the single-level optimization. Further investigation is needed to quantify these overheads and explore strategies to mitigate them for very large models.
3. **Dependency on Initial Offline Dataset**: While SAIL reduces oracle dependency, it still relies on an initial offline dataset to bootstrap alignment. The quality and diversity of this initial dataset can significantly impact the performance of SAIL, and a poorly constructed dataset could lead to suboptimal alignment. Further discussion on managing this dependency, especially when starting with limited labeled data or data with significant biases, could be beneficial. The paper should also explore the sensitivity of SAIL to the size and quality of the initial dataset.
4. **Potential Overfitting in SAIL-DP**: The paper mentions that SAIL-DP shows signs of overfitting on in-distribution responses, suggesting that the method may benefit from more refined regularization techniques to ensure robust generalization to out-of-distribution samples. The observed overfitting indicates that SAIL-DP might be overly specializing to the training distribution, which could limit its effectiveness in real-world scenarios where the model encounters novel inputs. More sophisticated regularization methods, beyond standard techniques, should be considered to improve generalization.

### Questions
1. The paper demonstrates SAIL's efficiency with models up to 8B parameters. Could you share any considerations or expected challenges for scaling SAIL to significantly larger models, such as those with over 100B parameters?

2. SAIL currently relies on the Bradley-Terry preference model. Have you considered experimenting with other preference models, and do you anticipate any impact on alignment performance if different utility functions are used?

3. SAIL-DP seems to show some overfitting on in-distribution responses. Could you discuss any regularization techniques you considered or plans to mitigate this, particularly to enhance generalization to out-of-distribution data?

4. Given the dependence on an initial offline dataset, how does SAIL perform in situations with minimal or noisy initial data? Are there strategies within the current framework to mitigate issues arising from a limited initial dataset?

5. Could you provide more detail on the computational costs of SAIL, particularly in comparison with other RLHF approaches? How does the single-level optimization approach compare in terms of resource requirements, and what practical considerations should be kept in mind when implementing it?

### Soundness
4

### Presentation
4

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
The paper addresses the limitations of traditional reinforcement learning from human feedback (RLHF) methods for aligning large language models (LLMs) with human preferences. The authors propose a unified framework for online RLHF formulated as a bilevel optimization problem, which they simplify to a single-level method for efficiency. This approach, called SAIL, allows for continuous model improvement through online exploration and iterative refinement of preference labels, mitigating issues related to distribution shifts and reducing reliance on static preference oracles. Experimental results demonstrate significant performance gains, with SAIL outperforming state-of-the-art RLHF methods.

### Strengths
(1) The paper introduces a novel unified framework for online RLHF that effectively addresses the challenges of static datasets and distribution shifts.
(2) By reducing a bilevel optimization problem to a single-level method, SAIL maintains theoretical benefits while significantly lowering computational costs, making it more practical for real-world applications.
(3) The self-improving aspect of SAIL allows models to iteratively enhance alignment without extensive supervision, addressing the challenge of needing constant access to human preference data.
(4) Extensive experiments validate the effectiveness of SAIL, showing substantial improvements in performance metrics compared to existing methods, thus showcasing its applicability across various datasets.

I would consider rescoring if the authors can solve my concern.

### Weaknesses
(1) The method does not improve much in the AlpacaEval 2.0 Score. The author should give a detailed explanation. And why not use metrics like length-controlled win rate?
(2) Authors should compare more advanced preference optimization algorithms like ORPO and SimPO. And current results are not impressive for the alignment community.
(3) Why did the author just include MMLU as the downstream task metric? They should incorporate more tasks (eg., arc-challenge) like the similar self-improvement work SPIN (ICML24) to better illustrate their contribution.
(4) In the alignment area, it's better to conduct experiments in the Arena-Hard benchmark since it's a common metric to evaluate the alignment ability.

### Questions
See the weakness section.

### Soundness
3

### Presentation
2

### Contribution
3
