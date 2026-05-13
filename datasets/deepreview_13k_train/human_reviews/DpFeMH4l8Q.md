# Group Preference Optimization: Few-Shot Alignment of Large Language Models

- Decision: Accept
- Scores: 6, 5, 6

## Abstract
Many applications of large language models (LLMs), ranging from chatbots to creative writing, require nuanced subjective judgments that can differ significantly across different groups.
Existing alignment algorithms can be expensive to align for each group, requiring prohibitive amounts of group-specific preference data and computation for real-world use cases. 
We introduce Group Preference Optimization (GPO), an alignment framework that steers language models to preferences of individual groups in a few-shot manner.
In GPO, we augment the base LLM with an independent transformer module trained to predict the preferences of a group for the LLM generations.
For few-shot learning, we parameterize this module as an in-context autoregressive transformer and train it via meta-learning on several groups. We empirically validate the efficacy of GPO through rigorous evaluations using LLMs with varied sizes on three human opinion adaptation tasks. These tasks involve adapting to the preferences of US demographic groups, global countries, and individual users. Our results demonstrate that GPO not only aligns models more accurately but also requires fewer group-specific preferences, and less training and inference computing resources, outperforming existing strategies such as in-context steering and fine-tuning methods. \footnote{Our code is available at the project website: \href{https://siyan-zhao.io/llm-gpo/}{https://siyan-zhao.io/llm-gpo/}}

\textit{\textcolor{red}{Warning: This paper contains qualitative examples that may be viewed as offensive or harmful.}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework to tackle the preference prediction problem, that is given a question, predict a distribution over all possible answers provided by the format of multiple choice question. The authors propose to view the question as a semi-supervised prediction problem and use LLM to augment the input data x into a (x,r) pair. The final prediction is done by training a shallow Transformer model over the augmented.

### Strengths
The paper proposes a novel idea to augment the data. The final analysis shows that direct tuning on LLM would not also obtain the best qualities on few-shot datasets.

### Weaknesses
While the paper presents a new infra on the problem of preference distribution, the alignment method does not look too much different than a normal semi-supervised framework and there are some caveats in the experiment design and baseline choice to fully justify the acceptance of this submission.

* For the baseline, the authors seem to fail to include one direct method.
  * A simple Transformer model that purely learns from the (q, y) pair and uses them in a semi-supervised fashion as a sequence of inputs. As is pointed out by the author, the Reward Model baseline is underperforming a lot of the other baselines, it would really make sense to add a comparable-sized baseline as in the author’s proposed method to rule out the possibility that overfitting is the only cause of inferior baselines w/o really relying on LLM.
* The PeftConfig configuration seems not consistent with the description of the Reward Model baseline in the paper. The authors argue to use a linear MLP head for the Reward Model baseline. However, in the code, the authors used a LoraConfig which should by default fine-tune every layer of LLM, and might be the major reason for the underperformed score of this baseline.
Also, it makes more sense to use cross-entropy for the loss function instead of MSE as the final output is a distribution.
* The terminology of alignment seems a bit too abused and distracting in this setting. In this work, the authors only tried to learn a separate Transformer architecture that operates upon the output of LLM while the LLM itself does not enjoy any new abilities in its parameters based on the modifications.
* It would also be an interesting point in this work to justify the reason for the output of (r) as input in this work (through ablation studies). My current understanding is that the sampled response would be used as an anchor point for the training of the proposed method, however, it would lead to a natural question: without r, will the model underperform a lot, meaning that LLM would also be the important ingredient? Also, in this case, it seems that the qualities of the response from the model would also seem to be quite important, and it would make more sense to replace it with random strings etc to further make the study more coherent.

### Questions
It would be great to see the authors compare with the very basic baseline, perform ablation studies, and fix some config settings to make the paper more complete.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a method to alignment LLM to group preferences so that a LLM grounded on several shots of preference examples can better predict the group preference for the unseen questions.

### Strengths
1. The problem this work proposes to solve is kind of new and unique.
2. The baselines are quite comprehensive and the proposed method significantly outperforms all of them, which validates the superiority of this method.

### Weaknesses
1. I am not sure about the significance and broadness of the problem this work tries to solve. Alignment of LLMs to group preferences sounds important, however, the evaluation datasets used by this work look quite specific and narrow and I don't think it is of interest to a broad range of research community. 
2. The proposed method look quite trivial and standard, which is a in-context fine-tuning method. There are some changes in the method details but those details are a bit hard to understand, which I will pose some questions on next.



### Questions
1. In the second last paragraph of page 4, it is said that "In particular, we discard the positional encodings commonly found in standard transformer architectures". Wouldn't the removal of positional encodings significantly deteriorate the performance of those pre-trained and fine-tuned LLMs?
2. Still in the second last paragraph of page 4, it is said that "we employ a masking strategy where the context pairs can self-attend to each other". Could you elaborate such a masking strategy?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The study introduces Group Preference Optimization (GPO), an innovative alignment framework designed to tailor large language models (LLMs) to specific group preferences with minimal data. GPO optimizes the model with reduced data, surpassing current methods like in-context steering and fine-tuning. Experiments on OpinionQA exhibit that GPO effectively adjusted the model's preferences on multiple-choice tasks.

### Strengths
1.	The paper commendably focuses on the concept of "Group Preference", introducing an efficient approach for aligning large language models to specific groups. 

2.	Efficient fine-tuning of a few-shot learning scenario, blending both in-context and fine-tuning methods, stands out. This approach offers a practical solution in settings where extensive labeled data might not be available.

3.	The empirical evaluations seem robust and thorough. Not only do the results show clear improvements, but the detailed analysis and discussion also provide insightful opinions.

### Weaknesses
1.	Lack of clarity in the presentation of the method. For instance, it remains ambiguous which specific parameters are subject to training. Incorporating a detailed algorithm diagram or flowchart would greatly enhance the comprehensibility. Besides, more training details would be better.

2.	The absence of evaluation results concerning the generalization capability of the GPO method. As GPO optimizes the parameters, it's crucial to show whether the model retains performance on general benchmarks after tuning.

### Questions
1.	As mentioned, it is ambiguous which part parameters are tunable. Could the authors further clarify the training details?

2.	Could the authors provide examples of generation tasks (QA) to better showcase the model's preference? Demonstrating the model's performance on responses could provide a clearer insight into its practical applications.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
