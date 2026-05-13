# Chain-of-Symbol Prompting for Spatial Relationships in Large Language Models

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
While conventional Chain-of-Thought prompting shows promising performance on various language tasks for LLMs, the spatial scenarios are nearly unexplored. In this paper, we first investigate the performance of LLMs on complex spatial planning and understanding tasks that require LLMs to understand a virtual spatial environment simulated via natural language and act or reason correspondingly in text. By evaluating on classic spatial planning scenarios through natural language descriptions, we found that current popular LLMs such as ChatGPT still lack abilities to handle spatial relationships in texts. This arises a question -- do the natural language is the best way to represent complex spatial environments for LLMs, or maybe other alternatives such as symbolic representations are both more efficient and effective for LLMs? To this end, we propose a novel method called **CoS** (**C**hain-**o**f-**S**ymbol Prompting) that represents the spatial relationships with condensed symbols during the chained intermediate thinking steps. CoS is easy to use and does not need additional training on LLMs. Extensive experiments indicate that CoS clearly surpasses the performance of the Chain-of-Thought (CoT) Prompting described in natural langauge in all three spatial planning tasks and existing spatial QA benchmark, with even fewer tokens used in the inputs compared with CoT. The performance gain is strong, by up to 60.8\% accuracy (from 31.8\% to 92.6\%) on Brick World scenarios for ChatGPT. CoS also reduces the number of tokens in the prompt obviously, by up to 65.8\% of the tokens (from 407 to 139) for the intermediate steps from demonstrations on the Brick World task.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors first investigated the performance of ChatGPT on spatial relationship tasks. They find that it still struggles, and proposed a novel prompting method called Chain-of-Symbols (CoS), which converts Chain-of-Thought (CoT) prompts into a sequence of symbols that represent spatial relationship described in the problem of interest. They experimented with synthetic datasets (Brick World, NLVR-based Manipulation, and Natural Language Navigation) and more realistic dataset (SPARTUN), and showed that CoS improves over CoT.

### Strengths
- Show that LLMs still struggle with spatial relationship understanding from natural language
- Proposed a new prompting method called Chain-of-Symbol to improve the performance on spatial relationship tasks.

### Weaknesses
 - The paper focuses only on Text-Davinci-003 and GPT-3.5-turbo. However, it would be beneficial to include other promising open-source large language models like the Llama-2 series in their study to see the effect of model size, different base models, etc.
- The authors claim that they achieved a significant improvement of up to 60.8% in accuracy (from 31.8% to 92.6%) on the Brick World dataset. While this is technically correct given the results, the reported improvement is a little misleading because it's comparing zs-CoT vs. CoS and also such a dramatic gain isn't seen in most cases, especially when comparing the performance of CoS to CoT. In more realistic datasets like SPARTUN, the improvement is marginal. This suggests that the impressive gains are more about the simplicity of the Brick World dataset than any substantial leap in CoS performance. Thus, I believe the claim should be more moderate.
- Apart from the previously mentioned issues, I find the contribution is limited for the following reason: the paper does demonstrate how you can condense the chain of thought (CoT) into a series of symbols, and that this is enough for tasks involving spatial relationships. However, this method of prompting might only be effective for spatial relationship tasks. Also, when you look at the final experiment (Table 5), it suggests that this method might not work as well in real-life situations. It seems that the success of this method, referred to as CoS, might be limited to simpler, more straightforward spatial tasks.

### Questions
- The authors used GPT-4 exclusively for the final experiment. Why not present GPT-4 results in the other sections as well?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an exploration into the capabilities of large language models (LLMs) to understand and process spatial relationships, a relatively unexplored domain for such models. They propose a new method termed Chain-of-Symbol (CoS) prompting. This approach aims to improve the spatial reasoning capabilities of LLMs. They observe notable performance gains in tasks that involve spatial planning and understanding. For instance, in the Brick World task, which involves a series of steps to achieve a final goal, CoS considerably outperformed traditional CoT. The findings could have broad implications for tasks that reuiqre advanced spatial understanding.

### Strengths
1. The paper presents a novel method, CoS, which addresses the limitations of existing techniques in spatial understanding.
2. Multiple spatial tasks such as Brick World, Natural Language Navigation, and NLVR-based Manipulation were used to validate the efficacy of the proposed method.
3. CoS consistently outperformed traditional CoT, showcasing its potential as a superior method for spatial reasoning tasks. In addition, a thorough analysis of the results, considering different configurations are also provided.

### Weaknesses
1. The heavy reliance on symbolic representations might limit the model's flexibility in real-world scenarios where such symbols might not be explicitly available. There also lack a clear definition or universal guideline to convert tasks into condensed symbols. The method's effectiveness is highly dependent on a pre-defined set of symbols and a mapping strategy, which may not generalize well across diverse spatial reasoning tasks. The process of creating these symbolic representations is not well-defined, raising concerns about the method's practical applicability and the potential for human bias in symbol design.
2. The process of converting spatial tasks into symbolic representations could introduce additional complexity and computational overhead. Besides, it require annotations, which seems more difficult to obtain compared with natural language based chain-of-thought or program-based program-of-thought. The need for manual conversion to symbolic representations also raises concerns about scalability and the potential for error introduction. The lack of an automated approach for this conversion makes the method less practical for large-scale applications. Furthermore, the need for task-specific annotations could limit the method's adaptability to new scenarios without significant effort.
3. The open-source LLM remain under-explored, only ChatGPT series are tested in the experiments. It could have been more solid if the same trend can be observed in other LLMs. Besides, the design of prompt may also influence the results a lot, perhaps a through comparison on the robustness of the prompt should also be included, so that the CoT performance is really revealed in terms of capturing spatial relationship.

### Questions
1. How scalable is the CoS method, especially for larger and more complex spatial environments? Is there an automatic way to converse into chain of symbols, or does it require manual rules and symbols design for each task and even each in-context sample?
2. How does CoS perform when compared to other potential solutions or methods that might address spatial reasoning in LLMs? Such as program-based CoT that involve symbolic reasoning?
3. How is the computation required to further convert to chain of symbols? And how about the tasks that do not have manually annotated symbols, how to extend your CoS method to a broader range of tasks?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new prompting approach, called chain-of-symbol. The idea is simple, instead of providing a language description about spatial relation of objects, this paper proposes to use symbols to represent the object relationship. By doing this, this method improves the off-the-shelf LLMs capability to reason about the spatial relationship. Five tasks are evaluated. The first task is called natural language spatial planning, in which the LLM is asked to move the object so that this location of objects will be in the desirable location. The second task is brick world, which is similar to the first task. And the third task is NLVR-based manipulation, in which the agent again needs to rearrange the object based on the textual instruction. And the fourth task is natura language navigation, in which the agent needs to navigate to different landmarks given the instructions. Finally, the spatial QA is a traditional benchmark for testing reasoning capability of LLMs. Table 1 and Table 2 show that CoS significantly improves the performance over CoT. And from Figure 3, the performance does not affect by the symbols that are used, which leads to that this method is robust to the symbols chosen. Overall, the paper demonstrates a nice result to verify the idea.

### Strengths
- The paper is easy to understand. All the sections are easy to read
- The proposed method is very simple, but the results show a significant improvement over CoT.

### Weaknesses
 - This is another prompting paper in the era of LLMs, and there is no new algorithm, but a trick (finding) to make the LLMs more robust.


### Questions
- How about other tasks such as problems concerning the "sequential relation"? For instance, Alice was doing cooking this morning, and in the afternoon, Alice was working, and during the night, Alice was relaxing with the family. Question: what did Alice do between 12:00 PM to 6:00 PM? something like this type of question.
- What is the fundamental explanation that this method works well?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel prompting paradigm called Chain-of-Symbol (CoS) Prompting that represents the spatial relations in the symbol chain. The authors claim that the proposed CoS outperforms CoT in all existing spatial QA benchmarks, with fewer tokens compared to CoT.

### Strengths
1. The proposed CoS prompting and findings are very interesting!
2. The paper is overall well-organized and easy to read.
3. The experimental results are strong.

### Weaknesses
1. The step (ii) in CoS prompting is not clear enough. How do authors correct the zero-shot CoT’s output, is it manually checking or prompting LLMs to do so?
2. There is an overlap between “Natural Language Navigation” and the text in the box in Figure 2.
3. I am curious about the generalization ability of the proposed CoS prompting. I would encourage authors to report performance in more general domains rather than just spatial question answering, such as some open-domain QA tasks.
4. This paper presents very interesting findings, I would encourage authors to discuss more about its mechanisms and give some insights.
5. Though authors list some advantages of the proposed CoS, at the same time, CoS is more difficult to track LLMs reasoning path. I would encourage authors to discuss some limitations of this work.
6. The CoS prompting exemplars are generated with zero-shot CoT. I would encourage authors to discuss the motivation of selecting 0-shot CoT and its implications on CoS performance.

### Questions
N/A

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
