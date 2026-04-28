# Tool-Augmented Reward Modeling

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
Reward modeling (\emph{a.k.a.}, preference modeling) is instrumental for aligning large language models with human preferences, particularly within the context of reinforcement learning from human feedback (RLHF). While conventional reward models (RMs) have exhibited remarkable scalability, they oft struggle with fundamental functionality such as arithmetic computation, code execution, and factual lookup. In this paper, we propose a tool-augmented preference modeling approach, named \name, to address these limitations by empowering RMs with access to external environments, including calculators and search engines. 
This approach not only fosters synergy between tool utilization and reward grading but also enhances interpretive capacity and scoring reliability.
Our study delves into the integration of external tools into RMs, enabling them to interact with diverse external sources and construct task-specific tool engagement and reasoning traces in an autoregressive manner. We validate our approach across a wide range of domains, incorporating seven distinct external tools. Our experimental results demonstrate a noteworthy overall improvement of 17.7\% across eight tasks in preference ranking. Furthermore, our approach outperforms Gopher 280B by 7.3\% on TruthfulQA task in zero-shot evaluation. In human evaluations, RLHF trained with {\name} attains an average win rate of 32\% when compared to baselines across four distinct tasks. Additionally, we provide a comprehensive collection of tool-related RM datasets, incorporating data from seven distinct tool APIs, totaling 15,000 instances.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a tool-augmented preference modeling approach, named Themis, to address the limitations of conventional reward models (RMs) in aligning language models with human preferences. The approach integrates external tools into RMs, enabling them to interact with diverse external sources and construct task-specific tool engagement and reasoning traces. The paper presents experimental results demonstrating the effectiveness of Themis in enhancing the performance of RMs across various tasks. The authors also provide a comprehensive tool-augmented reward dataset (TARA) for further research.

### Strengths
(1) The paper addresses an important issue in reward modeling by introducing a tool-augmented approach to enhance the effectiveness of RMs.

(2) The proposed methodology of integrating external tools into RMs is innovative and practical, allowing for dynamic decision-making and reasoning processes.

(3) The experimental results demonstrate significant improvements in preference ranking and outperformance of Themis compared to baseline RMs, validating the effectiveness of the approach.

### Weaknesses
The description of the method is not very clear. My understanding is that the reward model first generates some explanations based on the inputted question and answer, and then connects a fully connected layer to the final hidden state to produce a scalar reward. The explanation generation process and how it is integrated with tool use is not sufficiently detailed. It's unclear whether the explanations are generated before or after tool use, and how the tool-use information is incorporated into the explanation. The paper also needs to clarify the specific architecture of the fully connected layer and how the hidden state is processed to generate the scalar reward. There is a lack of clarity on whether the model is trained end-to-end or if there are separate training stages for explanation generation and reward prediction. Furthermore, the paper does not provide sufficient information about the training data used, including its size and composition, which makes it difficult to assess the generalizability of the approach.

### Questions
1. Why is there a significant difference between the results of Themis (Vicuna-7B + LoRA) and Themis in table1?
2. Does beta=0, w=0 in table1 mean RM (Vicuna-7B)?
3. I understand that all the values in table2 are accuracies, so why is the binary classification accuracy lower than 50 for RM (Vicuna-7B, Zero-shot)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper suggests leveraging primitive tools in the reward model to enhance reward estimation for RLHF settings. The authors conducted extensive experiments to show that by having tool-grounded reward models, it is possible to boost the reward model accuracy and translate them to RLHF gains.

Use of tools such as web search or calculator to improve the performance of an LLM is not particularly new. I understand that the current literature has mostly focused on inherent knowledge in the models at the alignment training.

** updated score after reading the response and revisions

### Strengths
- Having a level of reasoning and interpretability is great feature to have for reward models
- The experiments and provided implementation details look comprehensive

### Weaknesses
1- How to trust tools is an important aspect to consider here. At least in the examples, it looks like there is a risk of biasing the reward model and generative model to outputs of specific tools being used. This could be concerning as tools are not necessarily unbiased.

2- It is not entirely clear how GPT-4 is used to generate RM training data. Note that GPT-4 itself is a system if the proposal is to use GPT-4 to train RM, one can argue why not directly train RM on GPT-4 data or use GPT-4 directly as reward model.

3- When alpha in eq. 2 is set to zero, we converge to typical tool use via simple prompting right? the RM is still a pretrained model and can be prompted to use tools even without explicit loss terms on tool use. Is this understanding correct?

4- Model size of 7B is quite small to capture knowledge to compete with the tools used in this paper. I think a more realistic setup would be to take a larger model and the gap between say Wiki tool and that result could look very different.

5- I think the write-up could improve, especially for Sec 3.1, I had difficulty understanding exactly how GPT-4 was used and how training data was prepared

### Questions
(see above)

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates how to augment reward models with tools and proposes a new training framework, THEMIS, to do so. The Themis approach trains the model to select the correct tool for a given prompt and completion and reason about how the tools used should impact the assigned preference. In addition, the authors provide a tool-related RM dataset.

### Strengths
**Strength 1**: The idea of augmenting reward models with tools is very interesting, novel, and timely.

**Strength 2**: The proposed method provides a nice and logical way for tools to be included in the reward design process.

**Strength 3**: This paper provides some interesting experiments such as application to RLHF and scaling experiments.

### Weaknesses
 **Weakness 1**: One of my main concerns is lack of experiments on standard reward modeling datasets. There are many datasets not included in the paper such as the Anthropic HH dataset, Stack Overflow, OpenAI WebGPT, and ChatGPT comparisons datasets. They do conduct analysis on a small portion of the HH dataset, but not on the provided testing set. In addition, they show worst test accuracy than is reported in some other papers that only use conventional reward modeling [1]. Since the main claim of the paper is that by using tools they can improve the accuracy of reward models, I think their method should be validated on these popular datasets.

[1] Dong, Hanze, et al. "Raft: Reward ranked finetuning for generative foundation model alignment." arXiv preprint arXiv:2304.06767 (2023).

**Weakness 2**: Little Hyperparameter study. THEMIS introduces various hyperparameters, but the sensitivity of model performance to these hyperparameters is not discussed.

**Weakness 3**: This paper does not discuss a significant limitation of this method: the difficulty of creating the dataset. The dataset creation process consists of various complex steps, involves tool selection and design of heuristics. This seems to be difficult to scale to large scale preference datasets.


**Weakness 4**: I think that this paper could use a more in depth discussion of related works. In particular, various works have attempted to use similar tools such as a compiler in the reward design process [2,3,4,5] and [4] use it to guide the reward model training. Discussing these works could help better frame the contribution of this work.

[2] Le, Hung, et al. "Coderl: Mastering code generation through pretrained models and deep reinforcement learning." Advances in Neural Information Processing Systems 35 (2022): 21314-21328.

[3] Shen, Bo, et al. "Pangu-coder2: Boosting large language models for code with ranking feedback." arXiv preprint arXiv:2307.14936 (2023).

[4] Bukharin, Alexander, et al. "Deep Reinforcement Learning from Hierarchical Weak Preference Feedback." arXiv preprint arXiv:2309.02632 (2023).

[5] Shojaee, Parshin, et al. "Execution-based code generation using deep reinforcement learning." arXiv preprint arXiv:2301.13816 (2023).

### Questions
How exactly do you get the scalar reward from the reward model? Is this done with a separate output layer?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
4 excellent
