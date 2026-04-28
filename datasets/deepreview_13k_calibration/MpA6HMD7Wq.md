# Do Symbolic or Black-Box Representations Generalise Better In Learned Optimisation?

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
Until recently, behind every algorithmic advance in machine learning was a human researcher. Now, however, algorithms can be meta-learned automatically, with little human input. However, to be truly useful, such algorithms must generalise beyond their training distribution. This is especially challenging in reinforcement learning (RL), where transferring algorithms between environments with vastly different dynamics is difficult and training on diverse environments often requires prohibitively expensive large-scale data collection.Learned optimisation is a branch of algorithmic discovery that meta-learns optimiser update rules. Learned optimisers can be classified into two groups: black-box algorithms, where the optimiser is a neural network; or symbolic algorithms, where the optimiser is represented using mathematical functions or code. While some claim that symbolic algorithms generalise better than black-box ones, testing such assertions is complicated by the fact that symbolic algorithms typically include additional hyperparameters, and thus their evaluation is done many-shot. This is an unfair comparison with the zero-shot evaluation of black-box optimisers. In this work, we build a pipeline to discover symbolic optimisers which are hyperparameter-free, enabling a fair comparison of the generalisation of symbolic optimisers with that of an open-source state-of-the-art black-box optimiser trained for RL. Based on our analysis, we propose suggestions to improve the symbolic optimiser discovery pipeline for RL, with an overall objective of reducing the need for hyperparameter tuning to train an agent.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Optimizers are key algorithmic components in machine learning. In addition to man-made optimizers such as Adam, they can be learned automatically with little human guidance, which is the topic of the so called learned optimization. There are two types of learned optimizers: black-box algorithms and symbolic algorithms, in which a black-box optimizer is presented by a neural network while a symbolic optimizer is presented by math or code. For being truly useful, a learned optimizer should be generalized well to unseen settings beyond the ones it was learned. Therefore, it makes sense to study the generalization of the meta-learned optimizers. This manuscript contrasts the generalizability of the auto-learned black-box optimizers and the symbolic optimizers based on some reinforcement learning settings.

The authors use an existing black-box optimizer OPEN as its black-box baseline and they devise a symbolic optimizer discovery pipeline. This pipeline takes an evolutionary paradigm which includes the initialization, selection, mutation, and evaluation phases. What interesting is that it employs LLMs in the mutation phase and split it into the thinker step and the coder step for clearer interpretations.

The authors investigated several aspects as the generalizability, including the training lengths, the model sizes, the activation functions, and the environments. Experimental results show that although the black-box optimizer outperforms the symbolic optimizers in-distribution, the symbolic optimizers surpass the black-box optimizer generally, demonstrating better generalizability.

### Strengths
Although the literature claimed that black-box algorithms may be easier to work with while symbolic algorithms may generalize better, there is no strong justification. This manuscript conducts an empirical study to compare these two ideas to justify the assertion.

The designed symbolic optimizer discovery pipeline is inspirational and especially the idea of adopting LLMs is interesting and hot.

### Weaknesses
I am concerning about the significance of the learned optimization. As showed in the experiment, Adam outperforms other methods significantly in new environments. Although in the in-distribution settings, Adam performs better or closely to the symbolic optimizers. So what is the value of the learned optimizers since they need much more additional cost to do the meta learning?

Another main weakness of this manuscript is its presentation. It is not so well written and a little difficult to follow. First of all, the research problem is not clearly stated. What is an optimizer and how is it used in machine learning algorithms, at least in RL this manuscript studies? What is the definition of the core concept generalizability in this manuscript? What is the metric and how to evaluate the generalizability? I get these information from the late parts of the manuscript and they should be promoted to the early parts to be reader friendly. Second, a few key terms occur suddenly without any introduction. For instance, the term OPEN firstly appears in line 112 without mentioning before. A reader unfamiliar with this topic would be confused about what it is and where it is from. In the figures, what do the terms discopt1, discopt2, and discopt3 stand for? Third, there are some typos or grammatical errors. I name a few. Line 045: outer-loop -> outer loop; Line 063: usesw -> uses; Line 300: set of -> a set of; Line 358: the full stop is missing; Line 264: they don’t faily catastrophically in the training environments: typo or grammatical error. Anyway, at least regarding the writing and presentation, this manuscript is in a draft state and not ready for publication.

### Questions
See the part of weaknesses.

One additional question is that what is the use of the context optimizers in the evolution phase?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
To meta-learn RL-specific gradient optimizers, existing work explores two ways, learning a black-box model that outputs parameter updates, or using a symbolic algorithm to discover update equations/codes. This paper first argues that fair comparison among the above two ways is challenging because black-box methods often generalize in a zero-shot manner, while symbolic methods often rely on tunable hyperparameters for each task. Using OPEN [Goldie et al., 2024] as a key baseline, the authors propose a symbolic optimizer discovery pipeline and design a comparison to evaluate which of the above two ways better generalizes in training RL agents. Results indicate that while LLM-based symbolic learning underperforms on in-distribution tasks, it can have better generalization on out-of-distribution ones.

### Strengths
* The background and motivation are clearly introduced.
* The LLM-based framework is well-developed.
* The experiments in Section 8, conducted under various conditions/setups, are helpful and valuable.

### Weaknesses
 * While the paper asks a broad research question regarding the generalization comparison between symbolic and black-box optimizers for learned RL optimizers, its actual study scope is limited, as it primarily compares the proposed LLM-based discovery method with OPEN, a single and particular black-box optimizer. This raises concerns about the generalizability of the conclusions. Additionally, many other methods reviewed and cited in the paper are not included as baselines, which makes the comparison weak.

* Moreover, substantial domain knowledge and successful practices from OPEN are embedded into the prompts (in Appendix C). This reliance makes the discussion highly specific to and dependent on OPEN, also making the method hand-crafted. This seems to diverge from the stated goal of reducing human input, as significant input is now provided through the LLM prompts.

* Running only a single discovery run is indeed a limitation as acknowledged by the authors in Section 10. Also, it is unclear why focusing on a small number of environments during training would be beneficial or not.

* The clarity and organization of this paper could be improved. Providing examples and a clear explanation of what hyperparameters typically represent in the discovered optimizer would be beneficial. Many technical details are either insufficiently explained (e.g., what is meant by “small" relative changes to weights in line 287, what exactly constitutes the multi-task learning setting) or lack sufficient justification (e.g., in line 317, why p=0.8?). Additionally, some details are poorly organized (e.g., technical details of this work in lines 162–165 appear in the related work section rather than in the main methods section).  The “usesw” in line 63 is a typo error.

* More related work can be leveraged and discussed, e.g., [1-2]. Also, the idea of leveraging two LLMs to act as a "thinker" and a "coder" has also been explored in recent LLM-based optimizer discovery studies [3-4].

### Questions
* Is the “m=0.9” term in the discovered optimizers treated as a fixed hyperparameter?

* Can the discovered optimizers generalize effectively to complex RL tasks, such as continuous-action or high-dimensional control tasks?

* How sensitive are the symbolic optimizer outcomes to changes in prompt design?

* Is the discovery process sensitive to the used meta-training task?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a symbolic discovery pipeline which prompts a LLM-based thinker and a LLM-based coder to iteratively produce new optimizers based on an optimizer archive for RL training. Experimental results show that the discovered optimizers outperform Adam and OPEN on the training RL tasks.

### Strengths
1. The presentation in the paper is very clear.

2. The proposed LLM-based algorithm generation pipeline needs less hyper-parameter and expertise.

### Weaknesses
 1. The pipeline requires a large number of LLM conversations and RL inner training loops, which is time and resource consuming.

 2. The compared baselines are limited, in the experiment authors only compare two baselines, OPEN and Adam, advanced baselines such as SGD, Lion and AdamW are not included, the performance differences between the discovered optimizers and the optimizers in the archive are also omitted.

 3. The generalization performance of the discovered optimizers does not significantly outperform Adam, especially in the generalization to different environments.

### Questions
1. How to select optimizers for the archive, and why are these 4 optimizers chosen? Will archive with more or less optimizers affect the performance? Will optimizers with different implementations affect the searching?

2. The codes generated by LLMs may not always be correct, is there any code review and recover (if errors occur) mechanisms?

3. What is the adventage of using 2 LLMs as thinker and coder, instead of using a single LLM to directly generate the optimizer? How thinker LLM help coder LLM to obtain better optimizer?

4. Can the discovered optimizers generalize to other RL methods (i.e., DQN or REINFORCE) or non-RL learning paradigms (i.e., supervised learning), since the experiments only include PPO paradigm?

### Soundness
2

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
The paper presents a method leveraging Large Language Models (LLMs) to improve symbolic optimizers for reinforcement learning (RL) sequentially. It addresses the generalization abilities of symbolic versus black-box optimizers in learned optimization, where the goal is to automate the development of optimization algorithms that perform effectively across varied environments. Specifically, the paper builds a pipeline that discovers hyperparameter-free symbolic optimizers, facilitating a comparison with black-box methods, particularly the open-source black-box optimizer OPEN. The authors run evaluations on 4 datasets and the generalization to out-of-distribution datasets, and other hyparapemters (such as activations, sizes, and training lengths).

### Strengths
* The paper addresses a crucial issue in RL optimization by exploring which type of optimizer—symbolic or black-box—offers better generalization. This topic is particularly relevant as RL optimization algorithms are costly to meta-learn and difficult to generalize across environments.
*  The background and related work sections provide a well-rounded introduction, grounding readers in the context of learned optimization and its challenges in RL.
*  The paper offers a thoughtful discussion of results and future research directions to improve symbolic optimizers and integrate findings from black-box optimization literature.

### Weaknesses
 * The approach relies on a specific LLM, GPT-4o, making the results dependent on the capabilities and limitations of that model. This dependency may reduce the robustness and reproducibility of the approach, as outcomes may differ with other LLMs. Moreover, the dependency on LLMs makes this idea difficult to scale.

* The study uses only one black-box optimizer (OPEN) and limited baselines, evaluating across only four RL environments. The restricted dataset and baselines' choice may limit the findings' generalizability and impact.

* A core issue in meta-learning is achieving strong performance across diverse tasks. While symbolic optimizers demonstrate some benefits, they struggle in certain out-of-distribution tasks, underscoring the primary challenge the paper seeks to address. Additional insights on generalization could further strengthen the work.

* The paper contains numerous typos and moments of complex or unclear writing, making it occasionally challenging to follow. Moreover, more than half of the paper is spent discussing background, motivation, and future directions, while experimental sections, crucial for substantiating claims, could be expanded and discussed in greater depth.

### Questions
* The authors assume that the results on open-source models will be equally good. Is there any solid empirical evidence for this?
* Why the optimiser does not transfer to new tasks?
* Is there a possibility of overfitting? How can the current model avoid overfitting?

### Soundness
2

### Presentation
2

### Contribution
1
