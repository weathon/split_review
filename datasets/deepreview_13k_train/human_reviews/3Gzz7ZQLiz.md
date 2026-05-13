# Learning to Contextualize Web Pages for Enhanced Decision Making by LLM Agents

- Decision: Accept
- Scores: 8, 5, 5, 8

## Abstract
Recent advances in large language models (LLMs) have led to a growing interest in developing LLM-based agents for automating web tasks. However, these agents often struggle with even simple tasks on real-world websites due to their limited capability to understand and process complex web page structures. In this work, we introduce LCoW, a framework for Learning language models to Contextualize complex Web pages into a more comprehensible form, thereby enhancing decision making by LLM agents. LCoW decouples web page understanding from decision making by training a separate contextualization module to transform complex web pages into comprehensible format, which are then utilized by the decision-making agent. We demonstrate that our contextualization module effectively integrates with LLM agents of various scales to significantly enhance their decision-making capabilities in web automation tasks. Notably, LCoW improves the success rates of closed-source LLMs (e.g., Gemini-1.5-flash, GPT-4o, Claude-3.5-Sonnet) by an average of 20%, and demonstrates a 33.5% average improvement in success rates for open-source LMs (e.g., Llama-3.1-8B, Llama-3.1-70B) on the WorkArena benchmark. Moreover, the Gemini-1.5-flash agent with LCoW achieves state-of-the-art results on the WebShop benchmark, outperforming human experts.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
LCoW aims to advance LLM based web agents by adding a contextualization step to the webpage observation in which an LLM reduces the html/raw observation by pruning irrelevant elements and adds contextual descriptive information. This significantly improves the performance of the downstream web agent and sets state of the art results. 

The algorithm works by first collecting successful trajectories as ground truth. Then a contextualizer model (with a prompt instructions) is used to reduce and explain the UI elements. This now contextualized observation is give to a set of LLM agents that produce actions. The contextualized model gets a high reward if the agents give the same action as in the successful trajectory. The best contextualized observation is then collected. Finally the model is trained to produce the "good" contextual observations. This can be repeated for multiple iterations. 

The main contributions are:
- The novel approach to LLM-based contextualization and parsing, enabling state of the art performance on web agent datasets. 
- The algorithm for training the contextualization model
- The prompt for contextualization
- Many experiments

Their results include experiments on
WebShop and WebArena across multiple LLM agents with strong baselines in WebShop (such as AgentQ and LASER). 
They also include ablations/analysis on how the action matching reward improves with iterations, how LCoW affects the number of steps required for each task, and comparisons of the original collected trajectories against behavior cloning,

### Strengths
LCoW shows a very clear benefit and improvement to LLM web agents. 

LCoW shows state of the art improvement on WebShop against strong baselines such as AgentQ and LASER. This is comparable to human expert level on WebShop tasks. 

The experiments are pretty comprehensive showing improvement on different benchmarks with different agents and show continuous benefit for up to 3 iterations of LCoW training. 

This method does not seem like it would add a ton of compute expenses and could be quite practical. 

The paper is also well written.

### Weaknesses
There are a few weaknesses of the proposed method, though some of this is more limitations than reasons to reject. 

1) It is unclear how this method translates across websites, domains, and to some extent tasks. Since this involves training the contextualization model, there is potential to overfit to the data available. It would be nice to have some experiments showing that LCoW trained on a few domains generalizes to many other domains. Perhaps LCoW when generalizing to a task on say LinkedIn after only being trained on a couple benchmarks. 

2) This is also true for generalizing over tasks as well. Perhaps LCoW fails when extending to tasks that require more contextual reasoning. 

3) The training details section notes that action matching based on parsing is infeasible for open-ended actions (such as filling in a text box) and uses GPT-4o to do matching. However, the bigger limitation is on open-ended tasks or tasks that have diverse ways/orders of completing them. How would LCoW when there are many actions that are reasonable? 

4) In real-world situations there may be many rollouts that include individual actions that are actually incorrect. LCoW would treat these as correct and may even train the model to drop the truly relevant areas of the page. 

5) The limitations section only notes novel UI elements as a limitation. It seems the limitation section should be expanded to cover some of the above concerns as well. 

6) This approach also relies on being able to collect successful trajectories, whereas other methods that employ search may be able to extend agent capabilities to new tasks.

7) There are no experiments comparing to code-based html parsers for LLM agents. Though they are undoubtably not as good or there would already be models with performance comparable to LCoW. 

8) How long does the contextual observation generation take? In tasks that rely on parsing large amounts of text (e.g. Write a tweet based on this article), regenerating and contextualizing a whole article could be expensive, time consuming, and not necessary. (This should be addressed)

### Questions
Can you add more description of how self-contextualization works? This is the identical contextualization prompt just uses the LLM agent model  (e.g. Gemini-1.5-flash) instead of the trained Phi-3-instruct model. 

Table 3 in appendix: Data and caption do not match. 33*15 = 495. Are the numbers the number of successful demonstrations collected? Some more information on the demonstration collection would be helpful. 

Does figure 8 include both successful and failed tasks? -> Are the distributions over the same tasks? 

Line 182: “select the one that provides the most relevant context for the LLM agent to accurately predict the next action at as the target.” 
- This could be written more clearly. 

Will the model being released?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces LCoW, a novel framework that addresses the challenge of enhancing decision-making capabilities of Large Language Models (LLMs) in the context of web automation tasks. The method distinguishes the comprehension of web content from the decision-making process by training a dedicated module that creates contextualized representations of intricate web pages.

### Strengths
1.The paper presents comprehensive experiments on popular benchmarks, demonstrating that LCoW significantly improves the performance of LLM agents across various scales. The success rates surpassing human experts are particularly impressive.
2.The paper shows that the contextualization module trained with LCoW can generalize well to different LLMs, including those not involved in the training process, which is a strong indicator of the method's robustness.
3.The proposed iterative algorithm for training the contextualization module is a effective approach that allows for continuous improvement of the module based on real-world interactions and feedback.

### Weaknesses
1.As mentioned in the paper, the contextualization module struggles with web pages containing UI elements not seen during training. This limitation could be a barrier to the framework's real-world applicability, especially given the vast diversity of web page designs. The paper does not provide a clear strategy for handling novel UI elements, which is a significant concern for practical deployment.
2.The contextualization module was trained on a relatively small dataset of fewer than 2,000 self-generated samples. Can the model's ability to generalize to a broader range of web pages and tasks? The limited dataset size raises questions about the robustness of the learned representations and their ability to handle the long-tail of web content variations.
3.The paper does not extensively discuss the potential for overfitting, especially given the iterative training process that relies heavily on self-generated data. There is a risk that the model may perform well on similar tasks but fail to adapt to new, unseen scenarios. The iterative training, while beneficial, could also lead to the model memorizing specific patterns in the training data rather than learning generalizable features.
4.The contextualization module shown in Figure 7 is not intuitive enough.

### Questions
1.The reward obtained from multiple LLMs is only used to judge whether the current step correctly predicts the real action. Should the final expectation of task be used?
2.How does LCoW handle web pages with novel UI elements or layouts that were not encountered during training?
3.Have any measures been taken to prevent overfitting, particularly given the iterative training process that relies on self-generated data?
4.Can the web page be partitioned and analyzed through the prompt function? And there is no comparison with the previous intelligent code analysis work.

### Soundness
3

### Presentation
2

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
The paper proposes to contextualize the observation of LLM-based online shopping agents to improve their performance. It trains a task-observation-reliant contextualization module to help locate the most important information on a page and provides explanations. The idea is clever and shows promising results on two shopping benchmarks. However, it doesn't include code or any playing episodes for the reviewers to verify the outcomes.

### Strengths
- The observation contextualization idea is clever, and the training of the contextualization doesn't require human-labeled data.
- The results reported on the shopping tasks are promising, proving that the idea should work.

### Weaknesses
 - I like the observation contextualization idea, but I've seen a highly ranked paper on the WebArena benchmark, a benchmark with a wider type of websites defined other than mere shopping here, using a similar but more general method that doesn't require task-related inputs. I believe the strong reliance on the web observation's format, as you mention in the limitation section, "it often struggles to provide suitable contextualization for web pages containing UI elements unseen during the training," constrains this work's scope on shopping-related tasks only.
- I would question your results as you didn't include code or episodes for reviewers to verify your conclusions, especially when you only play your agents on a partial WorkArena benchmark, whose results are easily controllable if you only select the tasks where your agents win.
- I think you have sacrificed the agent's generalizability with the contextualization module specifically trained on the shopping tasks, as you put in the appendix.

### Questions
- How do you know the performance gain is enhanced by the LLM's decision-making?
- Figure 1: How do you select the reported tasks from WorkArena?
- How do you ensure that crucial elements are not removed during the contextualization?
- It seems the contextualization module could only be trained with successful trajectories from LLMs. What about those tasks that even those LLMs could not fulfill?
- The WorkArena contains up to 1,000 task instances, why do you evaluate only 115 tasks? How do you select them?
- If the contextualization is shopping relevant, do you believe it's less convenient to write several human oracle rules than to train a contextualization module?
- Figure 8: The mean of the number of steps doesn't seem to differ much. What is the exact number?
- It seems the behavior cloning baseline is trained with fewer demonstrations than the contextualization module.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes training a language model to contextualize complex web pages for improving the success rates of LLM-based web agents. To enable this the proposed method uses the web simulator environments to roll out multiple trajectories and uses multiple LLMs to score the different candidates. This strategy provides a significant improvement over baseline open and closed-sourced models across different benchmarks like WebShop and WebArena.

### Strengths
Pipelines for LLM-based web agents are complex and the proposed approach breaks down "contextualizing" the web pages separately from decision making ability of the agents. The approach of leveraging simulation data across the web environments to train (fine tune) a small model for contextualizing shows good results. The reward model is in essence a LLM-based judge system across multiple powerful LLMs. The qualitative results are interesting as they highlight how the proposed contextualization module works in removing irrelevant components of the web page.

### Weaknesses
 * With respect to generalization capabilities,  the study  can be strengthened by demonstrating performance across the different web environment bechmarks or types of web pages (e.g, instead of picking or holding out 500 examples randomly the type of Web tasks could be  used for creating the train/test held out set).

* Additionally, it is not clear if in the real world environment a simulation environment is available to bootstrap and roll out the candidate sequence of state and action(s).  As listed in the limitations section the power/promise of these agents diminishes given that performance drops when dealing with unseen UI elements. 

* For different web benchmarks, different LLMs were used for training the contextualization module. This needs to be explained or justified.

### Questions
* Explain the performance of different choices of LLM-based contextualization modules
* Discuss the practical efficacy of these said agents given the cost/tokens for using the reward models and the lack of simulation environment for new unseen web sites.

### Soundness
3

### Presentation
3

### Contribution
3
