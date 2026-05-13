# Language Agents Meet Causality -- Bridging LLMs and Causal World Models

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Large Language Models (LLMs) have recently shown great promise in planning and reasoning applications. These tasks demand robust systems, which arguably require a causal understanding of the environment. While LLMs can acquire and reflect common sense causal knowledge from their pretraining data, this information is often incomplete, incorrect, or inapplicable to a specific environment. In contrast, causal representation learning (CRL) focuses on identifying the underlying causal structure within a given environment. We propose a framework that integrates CRLs with LLMs to enable causally-aware reasoning and planning. This framework learns a causal world model, with causal variables linked to natural language expressions. This mapping provides LLMs with a flexible interface to process and generate descriptions of actions and states in text form. Effectively, the causal world model acts as a simulator that the LLM can query and interact with. We evaluate the framework on causal inference and planning tasks across temporal scales and environmental complexities. Our experiments demonstrate the effectiveness of the approach, with the causally-aware method outperforming LLM-based reasoners, especially for longer planning horizons. Project page: \href{https://j0hngou.io/LLMCWM/}{\textcolor{magenta}{https://j0hngou.io/LLMCWM/}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a framework that combines LLMs with CRL to improve reasoning and planning tasks. The framework leverages both LLMs' common sense knowledge and CRL's "look-ahead" ability on causal structures in environments. During inference, LLMs use a causal world model as a simulator for generating and processing action and state descriptions in natural language. This can be well integrated with MCTS algorithm from previous work. Tests on causal inference and planning tasks reveal that this causally-aware approach outperforms traditional LLM methods in complex, long-term planning scenarios.

### Strengths
- The integration of CRL and LLM planning is novel and interesting, it is straight forward to integrate it with multiple other LLM-based search algorithms, not only RAP.
- The paper investigates the form of action representation in the casual world model, and provides detailed results on them.

### Weaknesses
 -  Reasoning via Planning is not the sota method, [1] combines LLM as a world model and LLM as a policy model, with MCTS, should be better than RAP
- Though not discussed in RAP, other literature [2] [3] suggest increasing the number of LLM calls will substantially improve the search algorithm results. How is the overhead and accuracy of LLM+CRL planning vs. increasing LLM calls with tree-search or iterative prompting?
- I'm concerned about the ability of the system to work on more complex visual environment. For example, if the accuracy of the casual world model on look-ahead is limited, we should still rely on executing the actions in the real simulator and extract observation there. Related to this concern, a comparison with RAP+the real simulator execution (some oracle) is missing.
- How do you make sure the objects in the image X are identified with the Auto Encoder? if some objects are missing the casual model cannot run properly right?
- How does the baseline RAP work with LLama? LLama 8B does not take vision input.
- L285: the description is confusing, why causal mapper is trained using image input?
- Is LLM baseline just RAP? should just say RAP it in the table. Baseline LM is super confusing, there are many other simpler LLM prompting baselines in planning.

Typos:
- L269: p_\phi(E_t | z_t) not p_\phi(X_t | z_t)

### Questions
Questions:
- How do you make sure the objects in the image X are identified with the Auto Encoder? if some objects are missing the casual model cannot run properly right?
- How does the baseline RAP work with LLama? LLama 8B does not take vision input.
- L285: the description is confusing, why causal mapper is trained using image input?
- Is LLM baseline just RAP? should just say RAP it in the table. Baseline LM is super confusing, there are many other simpler LLM prompting baselines in planning.

Typos:
- L269: p_\phi(E_t | z_t) not p_\phi(X_t | z_t)

### Soundness
2

### Presentation
2

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
The paper proposed to learn a causal world model from a sequence of states and actions, where the states are images and actions are described in natural language. The proposed method builds upon BISCUIT and proposes representing the actions in natural language. The paper conducted experiments in GridWorld and iTHOR environment and the R^2 scores of the learned representation are claimed to be higher in low-data regimes. Experiments also show that the learned causal world model is more accurate at predicting the next state, and improves planning performance when compared to a general LLM (Llama 3).

### Strengths
- The paper proposed a method to learn a causal world model from a sequence of image states and text action descriptions, and demonstrated superior performance in the accuracy of the learned world model.
- Presentation of the paper is clear and easy to follow.

### Weaknesses
1. Some components of the framework would not be available in more realistic environments, e.g. 1) a set of annotated images with ground-truth causal variables is used in training, which is likely not available as we may not know the causal variables for more realistic environments; 2) a rule-based state description generator may not be available for complex environments where we don't know what are the true causal variables.
2. Given the simplicity of the environments, and that the proposed method is trained on these particular domains while the baseline is a general LM, the superior performance of the learned causal world model is less convincing. I would suggest comparing with a supervised fine-tuned version of the baseline LM. Since the proposed method uses a set of annotated images to train the causal mapper, supervised fine-tuning is possible with these annotated data: use the state description generator to convert the ground-truth causal variables of the states to natural language, and we can obtain a sequence of natural language action and natural language description of the states.

### Questions
1. How is coordinate-based action representation implemented? A 2-d vector, or simple text like “(2,3)” encoded by the encoder?
2. What does HB action representation look like and how does it differ from TB? An example of CB, TB, and HB would help to explain.
3. line 377, “better sample efficiency” would allow TB to perform well in extremely low-data scenarios as well, the reviewer think the experimental results doesn’t support the claim of “better sample efficiency” of TB.
4. In table 2, the baseline language model and the causal world model both predicts the next state in natural language, how is it evaluated against the ground-truth next state?
5. How big is the set of annotated images used to train the causal mapper m_\theta?

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
2

### Summary
The paper proposes a novel framework that integrates Causal Representation Learning (CRL) with Large Language Models (LLMs) to enhance reasoning and planning capabilities in interactive environments. The framework utilizes a causal world model that maps high-dimensional state representations to causal variables, which are linked to natural language expressions. This integration allows the LLM to interact with the causal world model, effectively simulating multiple possible futures before taking actions. The approach is evaluated on causal inference and planning tasks across different environments and temporal scales, demonstrating that the causally-aware method outperforms traditional LLM-based reasoners, especially for longer planning horizons.

### Strengths
The exploration of text-based action representations is particularly interesting, as it shows potential advantages in low-data regimes. I particularly liked the connection to the RL decision making problem. The results indicate that the proposed framework can potentially improve performance in causal inference and planning tasks, which is valuable for the broader ICLR community.

### Weaknesses
Can the authors elaborate on how the framework handles situations where the causal factors are not easily identifiable or where the causal relationships are highly complex?

Following on the above point, how were the parameters chosen for the various components of the framework, and how sensitive are the results to these parameters?

### Questions
Can the authors elaborate on how the framework handles situations where the causal factors are not easily identifiable or where the causal relationships are highly complex?

Following on the above point, how were the parameters chosen for the various components of the framework, and how sensitive are the results to these parameters?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The author proposed to introduce causal representation learning (CRL) to better understand the causal structure of a environment, and they incorporate such CRL with LLM to enable causally-aware planning by mapping causal representations to natural language.

### Strengths
The paper proposes to introduce CRL for world model to better understand the causal structure of environments. This intuitive idea provides a solid future approach to further improve the performance of world models, which is essential to build with intelligent agent with System 2 reasoning abilities.
The author analyzes the underlying math principles of the proposed CRL model and shows with experiments of the performance in metrics of comparison between induced state variables and ground-truth, and multi-step high-level accuracy of the predicted states. The experiments show large performance increase than baseline pure language model.
The author also use the result causal world model to do experiments on synthetic planning tasks. The results show consistent superior performance to baseline LM, especially on longer planning horizons.

### Weaknesses
 + It's not clear how much the text decoded from CRL model helps the LLM reasoning. It would be clearer if the author can show some examples and/or conduct ablation experiment on this. (also see questions)
+ The experiments compare **CB**, **TB**, and **HB** are based on the low-data scenarios, but the decision to use **TB** in subsequent experiments is for 100% data. This decision lacks a continuity of experiment settings, and it's unclear which setting would be the best for subsequent experiments. (also see questions)
+ The paper is a good starting of causal world model studies, but I have to mention that the experiment environment is synthetic and relatively easy. It would be more fascinating to use more general environments, and there leaves doubt whether the method can be easily scaling up to more general or even real world scenarios.

### Questions
+ Do we have examples of decoded text (from CRL to LLM)? Is that human-readable? Is there any possible insights with analysis of the decoded text?
+ (Clarification) In my understanding, the performance increase comes from (1) the text decoded from CRL makes it easier for LLM to reason and plan (2) the CRL model has a higher accuracy in predicting future states. If my understanding is correct, do we have ablation experiments on the effect of the two aspects?
+ (Clarification) Does the Baseline LM refer to RAP + LLaMA 3 or LLaMA3 with other prompting methods?
+ In Table 1, **TB** outperforms **HB** starting from 1.0%, outperforming **HB** much at **1.5%**, but performs weaker than **HB** in 100%. What are the trend between 1.5% and 100% subsample rate? Does it mean the necessity of **TB** decreases when the data scales up enough?
+ The **HB** settings shall contain all information in the **TB** settings. Why would the model performs worse than **TB** with increased subsample percentage? Since **HB** performs better in 100% ($10^6$ image states), would it be better to use **HB** in subsequent experiments?
+ Can you include SNA (success weighted by number of actions) in the planning results? It's a common metric to combine success and # of steps.
+ (Typo) Page 4 footnote, prioi -> prior
+ (Typo) Figure 1, missing an arrow from $\bf C^1$ to Text Decoder.

### Soundness
3

### Presentation
3

### Contribution
3
