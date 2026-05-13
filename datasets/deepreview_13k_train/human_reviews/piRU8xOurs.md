# TreeTop: Topology-Aware Fine-Tuning for LLM Conversation Tree Understanding

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
While Large Language Models (LLMs) have dominated a wide diversity of natural language tasks, improving their capabilities on \emph{structured} inputs such as graphs remains an open challenge. We introduce $\texttt{TreeTop}$, a pre-training framework for LLMs that significantly improves their ability to understand and reason over structural relationships in multi-party, threaded discussions, such as those found on social media platforms. $\texttt{TreeTop}$ is a novel set of 17 QA-style tasks specifically designed to allow LLMs to selectively focus on both the structure of and content in discussion graphs. We find that LLMs fine-tuned with $\texttt{TreeTop}$ outperform their counterparts in every setting: zero-shot/few-shot performance on unseen pretraining tasks as well as downstream social media inference tasks (e.g.rumor detection), as well as fine-tuned performance on the downstream tasks, including their challenging "early-detection" variants. In particular, $\texttt{Gemini Pro}$ fine-tuned with $\texttt{TreeTop}$ and further fine-tuned on downstream tasks surpasses both vanilla $\texttt{Gemini Pro}$ and state-of-the-art GNN baselines. Our framework paves the way for LLMs with enhanced capabilities on heavily-structured inputs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces TreeTop, a fine-tuning framework designed to enhance the performance of LLMs in understanding and reasoning over conversation trees—structured, multi-party discussions typically found on social media. The framework provides a collection of 17 structural tasks, aiming to improve LLMs' capacity to process both content and the structure of conversation trees. Experimental results show that LLMs fine-tuned with TreeTop outperform baseline models, including state-of-the-art GNNs, on multiple social media inference tasks, such as controversy and rumor detection.

### Strengths
- The paper tackles a novel challenge by focusing on conversation trees, which have unique characteristics such as directed, acyclic, and temporal structures. This addresses an important gap in LLM capabilities.
- TreeTop shows potential across a range of tasks (e.g., controversy detection, rumor detection) relevant to social media, making the framework broadly useful.

### Weaknesses
 - Some tasks are too easy to be meaningful. This work is proposed as a benchmark for LLMs and what's the point if a LLM can already achieve 100% accuracy?
- Most datasets used in this study are derived from Reddit, which may limit the generalizability of TreeTop’s effectiveness on other social media platforms or discussion types.
- The paper briefly touches on potential issues such as over-moderation or promoting echo chambers but does not provide a detailed discussion on these risks or propose safeguards.
- The paper only includes results from one model (Gemini), which is bluntly telling the authors work for a certain company. Also not including other models fail to set meaningful baselines.
- Format: This paper uses a wrong font.

### Questions
See "Weaknesses."

### Soundness
2

### Presentation
1

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
This paper proposes a fine-tuning method on conversation-tree related tasks. 
Concretely, the conversation-tree for the LLM to understand and the corresponding tasks in the form of yes/no questions are encoded in a structured prompt and used for fine-tuning. This method is named as TreeTop. They show that TreeTop fine-tuned LLMs have better performance than their not fine-tuned counterparts across various tasks.

### Strengths
- a new method is proposed to encode the tree structure of the conversation-trees and is showed to be effective 
- designed some structural tasks to evaluate the topological structure of the conversations trees 
- the proposed fine-tuning method does not only boost the performance on fine-tuned tasks but also on unseen tasks
- extensive experiments were conducted and the ablation studies are also detailed

### Weaknesses
See questions

### Questions
- For the primitive structural tasks, why is TT not compared against the baseline where the LLM is fine-tuned with non TreeTop encoded conversations and tasks? Please point it out if I understand it incorrectly.

### Soundness
3

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
4

### Summary
In this paper, the author proposed TreeTop, a fine-tuning framework improving the reasoning capabilities of LLMs over structured conversation tree data. TreeTop incorporates 17 structural tasks to train LLMs on the unique topological and content-driven aspects of conversation trees. Experimental results show that LLMs fine-tuned with TreeTop outperform traditional GNNs and other baselines on social media inference tasks.

### Strengths
- Adapting LLMs for graph-structured conversation trees are distinct graph problem-solving methods from traditional, static graphs in their directed, acyclic nature and temporal aspects.
- The evaluation on various social media tasks is comprehensive. Fine-tuning on structural tasks and subsequent performance comparisons are sufficient. The ablation analysis is well-set up and indicates the stability of the proposed method.

### Weaknesses
 - This framework may not sufficiently address how to perform with longitudinal data, where multiple conversation trees evolve over time or space.
- The framework could benefit from considering the integration of user characteristics across different conversation trees, especially in social media data where the same user may participate in multiple sessions.
- The details of integrating 17 structural tasks to fine-tune LLMs, such as considering the insightful associations and importance weights between these tasks, are not yet fully clarified.
- In terms of comparisons, only traditional GNNs are used as the main baselines, lacking comparisons with more recent graph-based reasoning methods.
- The reliance on task-specific prompts requires more results to clarify the extent to which various prompt styles across tasks influence TreeTop’s effectiveness.

### Questions
- How are the 17 structural tasks weighted during training? Is their importance dynamically adjusted based on downstream application requirements?
- Can TreeTop model the associations between multiple conversation trees, especially based on longitudinal data or same user scenarios?
- How does TreeTop differentiate between structure- and content-related inferences when solving a reasoning task?
- How does TreeTop compare to other fine-tuning based methods on general graph-based reasoning tasks, such as edge existence prediction or node classification?
- How sensitive are the model outputs to prompt design, and is there a mechanism to automatically adjust prompts for different tasks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
TreeTop is a fine-tuning framework designed to enhance LLMs in understanding structured inputs like conversation trees on social media. Featuring 17 tasks, TreeTop focuses on improving LLMs' ability to reason about structural and content relationships in these discussions. LLMs fine-tuned with TreeTop outperform baseline models, including SOTA GNNs, in generalizing to new tasks and excelling in social media inference tasks, such as controversy detection, even in early-detection scenarios. This framework advances LLMs' capabilities in processing structured data.

### Strengths
1. This work presents a new conversation tree encoding method. It would be beneficial to the field of multi-turn multi-party conversation.

2. It reveals the shortcoming of existing LLMs on understanding such kinds of conversation tree, and also presents a fine-tuning-based solution.

### Weaknesses
1. I think the writing should be improved. For example, I did not catch how you finetune LLMs with the TreeTop framework. It is better to clarify it clearly in the main content.

2. It seems that the baselines and related works are out-of-the-date. Are there any other more recently works of LLM on conversation tree?

3. I wonder how the conversation tree benefits the downstream dialogue tasks, such as dialogue response generation. Generating and understanding the conversation tree should be the endpoints of exploring this technique. Constructing the conversation tree, I think, should facilitate the quality of the response generation in multi-party conversations. So, I think it is important to highlight how the conversation tree will help the field of dialogue system.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2
