# Learning Evolving Tools for Large Language Models

- Decision: Accept
- Scores: 1, 6, 3, 6

## Abstract
Tool learning enables large language models (LLMs) to interact with external tools and APIs, greatly expanding the application scope of LLMs.
However, due to the dynamic nature of external environments, these tools and APIs may become outdated over time, preventing LLMs from correctly invoking tools.
Existing research primarily focuses on static environments and overlooks this issue, limiting the adaptability of LLMs in real-world applications.
In this paper, we propose \modelname, a novel framework designed to enhance the adaptive and reflective capabilities of LLMs against \tooldyna. By leveraging Monte Carlo Tree Search, \modelname facilitates active exploration and interaction of LLMs within dynamic environments, allowing for autonomous self-reflection and self-updating of tool usage based on environmental feedback.
Additionally, we introduce ToolQA-D, a benchmark specifically designed to evaluate the impact of \tooldyna.
Extensive experiments demonstrate the effectiveness and stability of our approach, highlighting the importance of adaptability to \tooldyna for effective tool learning.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
While LLMs have been equipped to interact with external environments, improving their functionality, in many cases, these "tools" or external environments evolve in an unpredictable way inducing incorrectness in the LLM output. This paper presents a framework called ToolEVO that uses MCTS (Monte Carlo Tree Search) to acquire feedback from LLMs through autonomous exploration and interaction. The feedback is then used to adapt the LLM to the changing environment.

### Strengths
1. Considers adaptation of LLMs to the changing environments which is a real problem for existing LLMs

### Weaknesses
1. The method is computationally inefficient and unrealistic in a real-world setting
2. A simple method of accessing the APi's through a proxy can do the same job in a much more efficient way.
3. There have been a lot of work on using design patterns to deal with evolving environments. The authors seem to be unaware of that literature. As a result, they have designed a cumbersome method that is not likely to work in practice.
4. In addition, the LLM itself might be modified. Thus the adaptation module needs to be separate from the LLM (in other words, the LLM does not need tom adapt). Tuning the adaptation module (which will be much smaller) should do the job.
5. The design is flawed.

### Questions
1. Think about a more efficient design. 
2. The LLM should not be adapted. It is the adaptability module (which is the interface) that should be adapted. 
3. Need precise runtime statistics (including response times).

### Soundness
3

### Presentation
2

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
Large language models (LLMs) are typically trained on stationary datasets, but the world is constantly evolving. For example, the API of a programming tool can be updated or deprecated in new releases. An LLM trained on the old version of the API will produce incorrect outputs when interacting with the new API. This paper proposes a framework for adapting large language models to a variable external environment, in particular a variable API / tool. 

For an LLM to adapt to new APIs different from those in the training set, it needs to interact with the environment and receive feedback. To this end, the authors propose to use online Monte-Carlo Tree Search (MCTS) to generate language actions to execute in the environment. The environment then returns the API outputs/error messages as well as a 0/1 reward at the end of the interaction sequence as feedback. In addition to MCTS, the authors propose two more mechanisms to improve adaptation: (1) self-reflection, where the model tries to explain the reason for encountering an error (as opposed to stopping right there); (2) tool-update, where the model generates a description of the updated API and add it to the context.

The authors evaluate their method, ToolEvo, on a curated benchmark of API / tool variability. There are three sets of APIs, $\mathcal P_{c}$, $\mathcal P_{s_\text{in}}$  and $\mathcal P_{s_\text{OOD}}$. $\mathcal P_{c}$ is the API seen in the training set, $\mathcal P_{s_\text{in}}$ is a slightly modified API that uses terminology seen in $\mathcal P_{c}$, and $\mathcal P_{s_\text{OOD}}$ is completely out of domain. Compared to a suite of baselines that are either only pretrained or supervised finetuned on $\mathcal P_{c}$, ToolEvo demonstrates significantly better adaptation capability, achieving higher success rates across the benchmark. 

To summarize, the paper makes two contributions: (1) it proposes a framework for adapting LLMs to variable external environment, (2) it introduces a benchmark to evaluate such adaptation capabilities.

### Strengths
1. This paper addresses an important research problem in the community, i.e., adapting LLMs to an evolving external environment. 
2. The proposed approach based on MCTS is grounded in a rich literature, and the self-reflection and tool-update mechanisms are novel contributions. 
3. ToolEvo exhibits strong empirical results on the benchmark, outperforming a suite of proprietary, open-source, and fine-tuned LLMs.
4. The released benchmark could be useful for future research in this direction.

### Weaknesses
1. The setting is rather contrived. The authors curate three predefined sets of APIs, but the APIs don't change *within an evaluation episode*. So performing well on the test set doesn't necessarily mean the method adapts to a *constantly* evolving environment. In fact, The proposed approach wouldn't apply to a constantly evolving environment, as the Q value in the MCTS is not adaptive.
2. The evaluation is potentially unfair. For a LLM to adapt to a new set of APIs, it needs to receive feedback. The baselines only have access to the API outputs and error messages, but ToolEval also has access to a reward at the end of each episode, which is privileged information. The authors don't compare to methods that make use of the reward information. 
3. The main contribution might not be the reason for the performance gain. According to Table 5, once they remove self-reflection and tool-update, the performance is about the same as supervised fine-tuning. This suggests MCTS may not contribute to the overall performance, despite it being introduced as a main contribution. 
4. The presentation has much room for improvement. To a general reader, too much context is deferred to the appendix, making the initial read particularly rough.

### Questions
1. How much overhead does MCTS add to the inference time?
2. Can you compare ToolEvo to a method that uses online RL to adapt to the new API? If it's not possible, why?
3. Can you compare ToolEvo to a version of the Static-SFT combined with self-improve and tool-update? The goal is to understand if MCTS contributes to the overall performance. According to Table 5, the main performance gain comes from self-improve and tool-update, and the MCTS-only version gets about the same performance as Static-SFT.
4. The overall algorithm is quite vague. I would suggest adding an algorithm box in the main text.
5. In line 275, I would suggest adding a description of $\mathcal P_{s_{\text{in}}}$  and $\mathcal P_{s_{\text{OOD}}}$ right away instead of referring to the appendix.
6. According to Section 5.1 Implementation Details, the models are fine-tuned on a dataset of interactions with $\mathcal P_{S_{in}}$. Can you expand on the reason behind this?

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
3

### Summary
The paper proposes ToolEVO, an algorithm for improving LLM tool use in dynamic environments. Specifically, the paper explores whether LLMs can call APIs to complete tasks, when the APIs can change over time. The change causes the API information in the static prompt to become outdated. The proposed method assumes the static prompt is not changeable and then proceeds to develop techniques to adapt the prompt and / or model using recently observed data. This is done via a combination of techniques (MCTS, Tool update, Self-reflection). The primary contributions of the paper are algorithmic and empirical. The paper also proposes a new dataset, ToolQA-D, constructed by random mutations of the ToolQA dataset. Experiments on ToolQA-D comparing ToolEVO using open-access LLMs to SOTA LLM baselines (closed and open access) are included along with ablation studies and other empirical analyses.

### Strengths
- The paper tackles an important and interesting problem of adapting LLMs to be able to invoke changing APIs correctly. This is a practical and important use case for LLMs. Progress here is likely to be of interest to the community.

- The paper considers a number of strong LLM baselines consisting of SOTA closed and open-access LLMs and performs a large set of computationally intensive experiments. While it's not clear if ToolEVO outperforms these, it's still useful to see relative performance. The results seem to suggest that LLM tool use is rapidly improving.

### Weaknesses
 - Overall, I found the problem setup and proposed methods a little challenging to understand in detail. The implementation details of MCTS and its various enhancements (cached rollout, inference, computational costs) are not clearly described. More on this below. 

- I didn't find the problem setup convincing. Restricting the LLM to only use P_C in the static prompt (Line 296) seems very limiting. Why can't the LLM's prompt be continuously optimized using recent API data in a separate process? That is what the ToolUpdate / SystemTool appears to do anyway. Please discuss this in more detail. Also, is it possible to include a baseline consisting of a proprietary LLM that is allowed to update its static prompt using the latest API invocation data, before each task?

- Given the above, the use of a full anytime planner like MCTS with cached rollouts is an interesting choice. As mentioned above, I'm not sure exactly how MCTS is used at inference time. Given that the state $s_t$ includes a full history, it's unclear to me if any tree node is visited more than once. Please consider including an illustrative example on a single task starting from the root. I wasn't able to find any discussion of computational costs (time, token), hyper-parameters and other standard MCTS implementation details. As a result, I found it very challenging to assess the algorithmic novelty and contributions of the proposed method.

- The methodology used to construct ToolQA-D from ToolQA isn't well motivated. Line 274 states "we employ GPT-4 to randomly modify the collected API usage". How exactly is this done? Why is this a good idea versus other mechanisms (e.g., using actual API versions of existing libraries)? Appendix A.3 doesn't say. Please motivate this choice and provide implementation details, assuming the goal is to propose ToolQA-D as a benchmark dataset for designing and evaluating tool-using LLMs.

- The presentation of the results in Table 2, 3 and 4 is a bit confusing. The bold formatting typically suggests best performance but that doesn't seem to be the case here. For example, on Line 335, ToolEVO's 30.3 score is in bold text but the higher score of 45.3 for Claude-3.5-Sonnet on Line 331 is not. Why is this? More generally, the proprietary LLMs, using only P_C, seem to perform best wrt Average-Hard (rightmost column) in Tables 2, 3 and 4. Is this correct? If yes, does that make the baseline proprietary LLM the best method? Please consider including a detailed discussion of the main results in Tables 2, 3 and 4 with an appropriate caption.

- The presentation and text gets a bit hand-wavy at times. Some examples below.
  - (Line 140) "rather than merely executing rigid tool invocations"
    - What does this mean? How do we know this is what the baseline LLM is doing?
  - (Line 398) "the stereotypes induced by Static SFT"
    - What stereotype is being referred to here?
  - (Line 406) "the model tends to lazily focus on how to use APIs provided in the prompt"
    - What does this mean?

- Overall, the paper seems to have a few major technical issues. As a result, I don't think it's quite ready for publication at this time.

### Questions
1. Using the Average-Hard column in Tables 2, 3 and 4, is it reasonable to claim that Claude-3.5-Sonnet outperforms all methods, including ToolEVO? If yes, why is the ToolEVO result highlighted using the bold formatting in Lines 335, 338, 351, etc.?

2. Assuming the prompts of the proprietary baselines in Tables 2, 3 and 4 are only shown the outdated API names and descriptions (P_C), is it possible to create a baseline that does a quick update of its prompt using the latest API names and descriptions before test-time evaluation / inference? How might this baseline perform?

3. How exactly is MCTS used at inference time? Please consider using an illustrative example task (API invocation).

4. What is the sample complexity and computational considerations (time and token costs) of ToolEVO? How does it compare with those of the proprietary LLMs?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper tackles API usage of LLMs in the context of changing API specifications. First, the paper introduces a new dataset “ToolQA-D”, an adaptation of ToolQA with two new versions of API specifications that can be used to simulate a dynamic API change. Second, the paper proposes a method to improve LLM tool usage in such a setting: ToolEVO. They use pre-trained models to interact with the dynamic environment and then fine-tune their model using successful runs from those pretrained models. Their method also is encouraged to self-reflect and has the option to update the API documentation used in the prompt. They evaluate their model empirically on the ToolQA-D dataset and compare it to static approaches (not trained in a dynamic environment) and non-finetuned models. They also provide an ablation study regarding the self-reflection and tool-update modules of their method.

### Strengths
The paper tackles an important topic and provides promising results. Their method outperforms the presented baselines and could improve API usage for LLM agents in the future.

### Weaknesses
My main concerns are with the presentation and some open questions that i would want to be answered to better judge the results before publication:
- The paper is at times hard to follow, and I found myself constantly looking into the Appendix to be able to follow. Even then some details are still unclear. (See questions)
- The presentation of the results could also be clearer and more convincing. (See questions)

- How was GPT-4 used to modify the API usage, and how is $P_{S_{ood}}$ completely different from $P_{S_{in}}$? Is the change in API different for every training/test example or is there one change in $P_{S_{ood}}$ and on in $P_{S_{in}}$ (is the variable name change same for all examples in each set)? Is it just the same dataset but with a different change in API parameter names?
- What are the numbers in table 2-4 exactly? Are those the number of successful test cases solved (100 according to the appendix)? If so, why is every problem exactly x.0 except for “Coffee hard”. What is different there that there are decimal points? Also the authors talk about significant margins: Are there any statistical tests performed to support that claim? Are those results even from multiple runs?
- How is the tool-update model used during testing? If the method updates the usage of the API in the first test case correctly, can it use the updated API documentation for the consequent tests? Or is it reset per test instance? 
- Does this method also generalize to real out-of-distribution tests? E.g., how would a model be able to adapt to an API that was not included in the training set?  

Minor comments:
- Figure 2: Why is there no drop in performance indicator for your method, but for the others?
- It is unclear from the text and captions of table 2-4 what bold and underlined indicates. I would assume that bold is best performance and underline is second best?
- The abbreviation SFT is never explained.

### Questions
- How was GPT-4 used to modify the API usage, and how is $P_{S_{ood}}$ completely different from $P_{S_{in}}$? Is the change in API different for every training/test example or is there one change in $P_{S_{ood}}$ and on in $P_{S_{in}}$ (is the variable name change same for all examples in each set)? Is it just the same dataset but with a different change in API parameter names?
- What are the numbers in table 2-4 exactly? Are those the number of successful test cases solved (100 according to the appendix)? If so, why is every problem exactly x.0 except for “Coffee hard”. What is different there that there are decimal points? Also the authors talk about significant margins: Are there any statistical tests performed to support that claim? Are those results even from multiple runs?
- How is the tool-update model used during testing? If the method updates the usage of the API in the first test case correctly, can it use the updated API documentation for the consequent tests? Or is it reset per test instance? 
- Does this method also generalize to real out-of-distribution tests? E.g., how would a model be able to adapt to an API that was not included in the training set?  

Minor comments:
- Figure 2: Why is there no drop in performance indicator for your method, but for the others?
- It is unclear from the text and captions of table 2-4 what bold and underlined indicates. I would assume that bold is best performance and underline is second best?
- The abbreviation SFT is never explained.

### Soundness
2

### Presentation
3

### Contribution
3
