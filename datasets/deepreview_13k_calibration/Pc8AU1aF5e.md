# Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
Building agents with large language models (LLMs) for computer control is a burgeoning research area, where the agent receives computer states and performs actions to complete complex tasks. Previous computer agents have demonstrated the benefits of in-context learning (ICL); however, their performance is hindered by several issues. First, the limited context length of LLMs and complex computer states restrict the number of exemplars, as a single webpage can consume the entire context. Second, the exemplars in current methods, such as high-level plans and multi-choice questions, cannot represent complete trajectories, leading to suboptimal performance in long-horizon tasks. Third, existing computer agents rely on task-specific exemplars and overlook the similarity among tasks, resulting in poor generalization to novel tasks. To address these challenges, we introduce \model, a computer agent featuring three key components: i) state abstraction, which filters out task-irrelevant information from raw states, allowing more exemplars within the limited context, ii) trajectory-as-exemplar prompting, which prompts the LLM with complete trajectories of the abstracted states and actions to improve multi-step decision-making, and iii) exemplar memory, which stores the embeddings of exemplars and retrieves them via similarity search for generalization to novel tasks. We evaluate \model on \wob, a standard task suite, and Mind2Web, a real-world website benchmark. In \wob, \model achieves a 99.2\% average success rate (a 10\% relative improvement) across 64 tasks using demonstrations from only 48 tasks. Notably, \model is the first ICL method to solve the book-flight task in \wob. \model also exhibits a 56\% relative improvement in average step success rate over the previous state-of-the-art prompting scheme in Mind2Web.\footnote{Code available at~\url{https://ltzheng.io/Synapse}.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a prompting-based method (SYNAPSE) for computer control that takes in states and outputs actions in a discrete, human-computer-interaction-like action space. The paper is motivated by gaps in existing computer control methods: in-context learning, which struggles with long-horizon tasks and generalization and often needs post-hoc correction; and trained/fine-tuned methods, which are data- and compute-inefficient.

SYNAPSE consists of three components: a state abstraction procedure in which an LLM is used to extract important information from the raw state, thereby significantly reducing token length; "trajectories as exemplars" (TaE) prompting, in which full, relevant trajectories (sequences of clean states and actions) are added to the prompt for generating each new action; and exemplar memory in which trajectories and their associated tasks are encoded and stored, to be used as exemplar trajectories when a related task is being planned. 

Experiments are conducted on MiniWoB++ and Mind2Web. The MiniWoB++ experiments show SYNAPSE's major data efficiency (and moderate performance) gains over BC+RL and finetuning baselines, as well as performance and simplicity gains over ICL baselines. The Mind2Web experiments demonstrate the same, along with its generalization capability across tasks, websites, and domains. SYNAPSE beats SOTA on various tasks from MiniWoB++, including notably difficult ones for which human-level performance is not achieved by prior work.

### Strengths
#### Quality
- Method is intuitive and effective
- Experimental setup is useful. It is useful to have one standard benchmark with extensive comparison to baselines and one realistic benchmark on which more qualitative advantages like generalization are shown. 
- Results are promising - the similarity to human performance on MiniWoB++ and the significant increases on generalization show the power of SYNAPSE's TaE and exemplar memory components. 
- Ablations are useful as well to concretely break down each component of the approach. 
- Overall a well-constructed, well-executed paper. 

#### Clarity
- Very well written!
- Figures are especially useful compared to a lot of papers. Tables as well. Overall, results are not only promising but well-communicated. 

#### Originality
The paper positions itself well in prior work. As far as I am aware, the specific three components used here have not been combined elsewhere. 

#### Significance
The performance on existing computer control benchmarks is impressive, especially when comparing to human baselines. Figure 4 particularly tells a story of a significant improvement in capability. The results on MiniWoB++ show only some improvement, so it's unclear how significantly SYNAPSE distinguishes itself, but the results on Mind2Web show a lot of improvement margin.

### Weaknesses
#### Quality
- The same ideas (gaps in prior work, the three components and their descriptions, the benchmarks being used) are repeated several times throughout the paper. While I very much agree that some amount of repetition is crucial to get a reader to understand what you are saying, in this case it's not just two or three times but four or five, or even if it's three, there's lots of detail every time. It feels as though the repetition is there to fill up space, even if that's not really the case. It gets tiring to read the same high-level concepts over and over.

#### Clarity
- I don't quite understand what "step success rate" is as opposed to "success rate" - it's brought up several times as the metric for Mind2Act, but not defined as far as I'm aware.
- It doesn't seem to be made clear what exactly the state abstraction entails. In figure 1, the only difference between "raw state" and "clean state" is `<body><h1>…</h1></body>” --> <input id=”where” type=”text”>`. There aren't clear examples in the main text, but intuition about this would be very useful.
- Not clear how SYNAPSE's history-in-prompt approach is significantly different from Mind2Act's (or lots of other works') to the point of being novel. While Mind2Act provides the trajectory-so-far to the LLM, SYNAPSE provides the observation as well, which is an incremental but not fundamentally novel change. The core idea of providing history to the LLM for context is not unique.
- From both Fig 1 and the text, it's unclear when new trajectory exemplars and example state abstractions are generated - is it per task (that's what I'd think) or per step?
- Fig 3: might help to have clearer visual distinction of SYNAPSE and the human baseline, especially since the colors aren't always visible. Lines/shading/callout boxes could help.

#### Originality
Though the approach is technically unique and clearly effective, there are some originality concerns in terms of what the paper claims. For example, the paper positions itself against works like Inner Monologues and SayCan by saying that they focus on high-level planning; however, though RCI uses *even higher* level planning, SYNAPSE is still working with a discrete, abstract action space. Meanwhile, the low-level BC/RL/motion planning+control used for the robotics papers cited are operating in a much more granular, potentially continuous, action space. For another example, the paper spends considerable space discussing how it is unique compared to other prompting-based methods in helping the LLM understand the current state. However, MindAct gives trajectory-so-far back to the LLM when prompting for the next step. SYNAPSE gives observation as well, thereby informing the LLM in more detail about the current state, this just isn't a very original idea. It's an important step past MindAct, but not a big one, especially relative to how much it's discussed as a unique contribution.


Nits:
- Page 5, last paragraph: `Obseravtion` is a misspelling

### Questions
- What exactly is step success rate vs. success rate?
- It is inherently interesting that this approach does not need self-correction unlike other prompting-based approaches, but does that offer any significant performance/efficiency gain?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new technique to prompt language models with example trajectories for computer control tasks. It utilizes language models to abstract clean states for long-context conditioning, and design a retrieval module to improve generalization.

### Strengths
1. The writing and presentation is clear in general
2. The proposed method surpassed baselines like CC-Net, RCI on various benchmark like MiniWoB++ and Mind2Web

### Weaknesses
1. Some details are not well explained, see questions.

2. SYNAPSE uses state abstraction to make sure LLM can learn from compact information while ensuring the context length is well utilized. However, in the experiments, SYNAPSE sets k=5 for retrieval. It's unclear how the performance changes if k grows, and why longer context is not helping here. The paper should explore the impact of varying k on performance and provide a more detailed analysis of why increasing context length does not lead to improved results.

3. Table 1 is confusing. It's non-standard to use "SYNAPSE w/ state abstraction, SYNAPSE w/ trajectory-as-exemplar, SYNAPSE w/ training set as memory" to indicate gradually adding "state abstraction, trajectory-as-exemplar, training set as memory" 3 components. To demonstrate a component *A*'s usefulness, it would be clearer to present results as "SYNAPSE w/o *A*", since SYNAPSE is a method that combines all components. This makes it difficult to isolate the contribution of each component.

4. For Table 1 training set as memory experiments, it's not clear whether all the training data for 3 scenarios ("cross-task, cross-web, and cross-domain") are added, or only the corresponding training data (e.g. cross-task but same web when evaluated on cross-task setting). The paper should explicitly state how the training data is used for each evaluation scenario.

5. For tasks that need code to abstract state information, it's unclear how to examine if a code can successfully extract desired information. Examining this from task success is problematic because it can be influenced by suboptimal policy execution. A more direct method for evaluating the state abstraction code is needed, separate from the overall task success.

6. For the cross-domain tasks, retrieval doesn't seem to help, and the paper doesn't provide a strong explanation for this result. The retrieval number is set to 5, which is a small number. It's unclear if the retriever is failing to return relevant examples. Showing some retrieved examples would be more intuitive and help understand this behavior.

7. "The action generation starts from prompting LLMs with successful trajectories to warm up LLMs with the dynamics of the current environment". It's unclear if this describes prompting with retrieved trajectories, or some other warmup procedure. If it's cross-task/cross-web/cross-domain setting, how's current environment defined?

### Questions
1. SYNAPSE uses state abstraction to make sure LLM can learn from compact information while ensuring the context length is well utilized. However, in the experiments, SYNAPSE sets k=5 for retrieval. How does the performance change if k grows? And why longer context is not helping here?

2. Table 1 seems confusing. It's non-standard to use "SYNAPSE w/ state abstraction, SYNAPSE w/ trajectory-as-exemplar, SYNAPSE w/ training set as memory" to indicate gradually adding "state abstraction, trajectory-as-exemplar, training set as memory" 3 components. If you want to demonstrate a component *A* is useful, better to write it in "SYNAPSE w/o *A*", as SYNAPSE is a method that combines all components

3. For Table 1 training set as memory experiments, do you add all the training data for 3 scenarios ("cross-task, cross-web, and cross-domain)? Or only the corresponding training data (e.g. cross-task but same web when evaluated on cross-task setting).

4. For tasks that need code to abstract state information, how can you examine if a code can successfully extract desired information? if examined from task success, it can be because of the suboptimal execution of policy.

5. For the cross-domain tasks, retrieval doesn't seem to help, can you give a better explanation about this result? The retrieval number is set to 5, which is a small number. Is it because the retriever doesn't return the desired examples? Maybe showing some retrieved examples can be more intuitive.

6. "The action generation starts from prompting LLMs with successful trajectories to warm up LLMs
with the dynamics of the current environment". Is it describing prompting with retrieved trajectories? Or that's some other warmup procedure? If it's cross-task/cross-web/cross-domain setting, how's current environment defined?

### Soundness
3 good

### Presentation
3 good

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
This paper studies the problem of data driven computer control using large language models (LLM's). It adds three components to improve capabilities of current approaches. It abstracts from the state of the environment by parsing it via an LLM such that only information necessary for the task is kept. It conditions on complete trajectories of similar tasks. It keeps a memory from which similar example trajectories are sampled.  The method is compared against strong baselines on two current benchmarks in the field of data-driven computer control. It shows improved task success rate on both, while often needing less data. Ablations on each component of the method show that the state abstraction procedure is the main reason for the improved performance.

### Strengths
The method is mostly explained well and it is easy to follow the explanation. Experiments and results are presented well.

Improved task success rate on two benchmarks in the field of data driven computer control.

Competitive baselines from a variety of recent approaches in the domain of data driven computer control.

Ablations investigate the effect of each component of the method. 

The state abstraction approach allows the method to be tested on tasks that were infeasible for prior methods.

### Weaknesses
 - From the results in the MindAct task it seems that adding any trajectories helps but it does not matter which ones.

- Have you studied the effect on performance on the MiniWob++ environment for different amount of tasks in the memory. The comparison to RCI does not seem fair at the moment (Figure 3)?

- It would be helpful to have an illustrating example of the result of the state abstraction procedure (i.e. a figure of a (state,observation)-pair) as well as an example prompt (maybe in the Appendix). Figure 1 only shows that some <body> and <h1> tag got removed but it's not yet clear to me what the result of the state abstraction procedure looks like. Its also not clear to me where the examples from the state abstraction prompt come from. Are they designed a-priori? If yes how and how difficult is that? Are the same examples reused for all states or also taken from the memory?

- The text states (last paragraph of 4.3) that failed trajectories are displayed in Appendix C, but Appendix C only refers to the supplementary material?

- In the original paper of MindAct, they used 3 in-context exemplars for GPT3.5  but Synapse uses 5, so the comparison favours Synapse. In general I would maybe add a sentence that clarifies that results are SOTA, conditioned on the fact that GPT3.5 was used as the underlying LLM.

### Questions
- Have you considered building up the memory from scratch by adding successful trajectories over the course of training?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
