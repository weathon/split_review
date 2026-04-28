# Learning from Preferences and Mixed Demonstrations in General Settings

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5

## Abstract
Reinforcement learning is a general method for learning in sequential settings, but it can often be difficult to specify a good reward function when the task is complex.
In these cases, preference feedback or expert demonstrations can be used instead.
However, existing approaches utilising both together are either ad-hoc or rely on domain-specific properties.
Building upon previous work, we develop a novel theoretical framework for learning from human data.
Based on this we introduce LEOPARD: Learning Estimated Objectives from Preferences And Ranked Demonstrations.
LEOPARD can simultaneously learn from a broad range of data, including negative/failed demonstrations, to effectively learn reward functions in general domains.
It does this by modelling the human feedback as reward-rational partial orderings over available trajectories.
We find that when a limited amount of human feedback is available, LEOPARD outperforms the current standard practice of pre-training on demonstrations and finetuning on preferences, as well as other baselines.
Furthermore, we show that LEOPARD learns faster when given many types of feedback, rather than just a single one.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces LEOPARD, a framework capable of learning from a diverse range of data types, including preferences and ranked demonstrations. Results on the control experiment indicate that LEOPARD converges more quickly than approaches that rely solely on Inverse Reinforcement Learning (IRL) or Reinforcement Learning from Human Feedback (RLHF).

### Strengths
* The framework’s ability to learn from negative or failed demonstrations is intriguing.

### Weaknesses
 * The evaluation of the proposed algorithm is limited in scope.
* The improvement achieved by LEOPARD is modest compared to the IRL method.

### Questions
* Could the authors provide or plot the mean ground truth reward for both the demonstration data and preference data in Figures 1 and 2? I am uncertain about the quality of the final policy, as the optimal policy for the HalfCheetah-v4 environment in Gym typically reaches a score of around 12000.

* Are there any differences between applying IRL first, followed by RLHF, and the reverse order? Could the authors also provide results comparing the policy’s quality of applying RLHF first, then IRL?

* For the stopping conditions, LEOPARD checks the value of the training loss to determine when to stop. However, if the environment changes, this threshold would also need adjustment. Are there any more effective methods to establish this threshold?

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
This paper introduces LEOPARD, a new algorithm for reinforcement learning from mixed types of feedback. This approach is based on the theoretical framework of reward-rational (implicit) choice (RRC). Based on that, they develop a general theoretical framework, namely reward-rational partial ordering (RRPO). Then it proposed an algorithm to construct preference rankings from positive, negative and preference ranking data and then feed it to the RRPO objective, namely the LEOPARD method. Through experiments on three environments from the Gymnasium, it demonstrates that LEOPARD outperforms traditional methods that sequentially apply IRL on demonstrations and RLHF on preferences.

### Strengths
1. The RRPO framework allows it to handle partial rankings across multiple types of feedback.
2. The author shows that RRPO faithfully represents the partial orderings in appendix D.

### Weaknesses
1. The actual algorithm is a simple combination of well-known existing approaches. Though the RRC and RRPO framework is very general. The proposed method LEOPARD only use trajectory-level pairwise preference rankings. LEOPARD is essentially just RLHF with some synthetic data augmentation when positive and negative demonstration data are available. 

2. The experiment is limited to 3 Gymnasium environments. These domains are relatively low-dimensional and may not represent more complex real-world applications, such as high-dimensional robotics or language model finetuning.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces LEOPARD: Learning Estimated Objectives from Preferences And Ranked Demonstrations. LEOPARD is a method from learning from diverse types of feedback including negative or failed demonstrations, rankings, and positive demonstrations. LEOPARD is based on a new framework that this paper introduces called reward-rational partial ordering (RRPO). LEOPARD is primarily compared against methods that pretrain through IRL on demonstrations and then finetune on preferences. The comparisons occur in 3 environments: HalfCheetah, Cliff Walking, and Lunar Lander.

### Strengths
I think the paper is clear, well-written, and to my knowledge, technically correct. The paper also is thoughtful in its experimentation, mostly recognizes the prior literature, and does not overclaim.

### Weaknesses
 - I do think a preference-based IRL baseline rather than DeepIRL + finetuning can bolster the paper. I realize that preference-based inverse RL baselines aren't easy to compare against. However, nonetheless I think it can improve the paper.
- Unfortunately, only 3 environments are tested, and the results are not that strong. In HalfCheetah the confidence intervals overlap in Figure 1. Moreover, it seems the benefit primarily lies when both demonstrations and preferences are available, when the baseline methods do IRL then finetuning. To a certain degree, their method is built to be successful in this scenario. Of course, it is a good sanity check, but nonetheless limits the scope of the results.
- Another concern of mine is the scalability of the method given the relatively small environments. HalfCheetah, Lunar Lander, and Cliff Walking are not the most testing environments. Preference-based IRL methods are tricky and finicky to get to work, and doing so is part of the contributions of such papers. Unfortunately it does beg the question of whether it does scale, and what challenges LEOPARD may face when scaling.
- I appreciate the authors' noting the limitations of their work, but I do feel some of these limitations should be addressed by the paper itself to meet the bar of ICLR. In particular testing on a few more environments that are more challenging would bolster these results.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors present LEOPARD, a novel method for learning from preferences and mixed demonstrations. LEOPARD is built upon the proposed framework that models human feedback as reward-rational partial orderings over trajectories. The method's effectiveness is evaluated across three diverse tasks, encompassing both discrete and continuous observation and action spaces.

### Strengths
Learning from preferences and mixed demonstrations addresses a important and highly relevant problem for the community.

### Weaknesses
 - **Lack of Baseline Comparisons**: The paper does not provide comparisons to existing preference learning methods. Incorporating baselines from recent work, such as [1][2][3], would strengthen the empirical evaluation. Specifically, the absence of comparisons to methods that explicitly handle partial orderings or rankings derived from preferences is a significant oversight. The current evaluation only demonstrates the method's performance in isolation, without establishing its relative effectiveness against state-of-the-art techniques.
- **Simplistic Environments**: The evaluation is conducted on relatively simple environments. In contrast, other preference learning studies have utilized a broader range of tasks, such as Meta-World[4] and [5], which could better demonstrate the robustness of the method. The current environments, with their limited complexity, do not adequately test the method's ability to generalize to more challenging scenarios with higher dimensional state and action spaces, and more complex reward structures.
- **Unclear Novelty in Relation to RRL[6]**: The authors claim that their Reward-Rational Partial Orderings framework is a novel advancement compared to RRP. However, the novelty is not convincingly articulated, and the distinction remains unclear when directly compared to the RRP paper. The paper fails to clearly delineate the mathematical and conceptual differences, leaving the reader unsure of the specific contributions beyond a re-framing of existing concepts. A more rigorous comparison, highlighting the unique aspects of the proposed framework, is needed.
- **Writing and Clarity**: The paper’s writing can be improved in several areas:
    - The abstract does not provide a clear explanation of how LEOPARD works. Mentioning the concept of reward-rational partial orderings upfront would give readers a better understanding. The abstract should clearly state the core mechanism of the method, including how partial orderings are used to learn from preferences and demonstrations.
    - Equations, such as Eq. 1 and 2, are not well integrated into the text, making it difficult to follow the technical details. The equations should be introduced with clear explanations of the variables and their roles within the model. The text should also provide a step-by-step breakdown of how these equations are used in the algorithm.
    - Including a comprehensive illustrative figure to outline the entire algorithm would enhance clarity and reader comprehension. A visual representation of the algorithm's flow, including the input data, processing steps, and output, would greatly improve understanding.
    - The description of algorithm iterations in Figures 1-3 is ambiguous, and it is unclear what exactly they represent. Providing more detail or clearer labels would be helpful. The figures should include clear labels for each step, and the accompanying text should provide a detailed explanation of the iterative process.

### Questions
Could you please further clarify the proposed differences to RRL[1]?

Will authors make the code available?

[1]Jeon, H. J., Milli, S., & Dragan, A. (2024). *Reward-Rational (Implicit) Choice: A Unifying Formalism for Reward Learning*. In *Advances in Neural Information Processing Systems (NeurIPS)*

### Soundness
2

### Presentation
2

### Contribution
2
