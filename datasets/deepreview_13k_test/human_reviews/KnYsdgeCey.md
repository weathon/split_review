# Learning to Plan with Personalized Preferences

- Decision: Reject
- Scores: 3, 3, 5, 8

## Abstract
Understanding and adapting to human preferences is essential for the effective integration of artificial agents into daily human life, particularly as AI becomes increasingly involved in collaboration and assistance roles. Previous studies on preference recognition in embodied intelligence have largely adopted a generalized yet non-personalized approach. To fill in this gap, our research focuses on
empowering embodied agents to learn and adapt to individual preferences, a task complicated by the challenges of inferring these preferences from minimal observations and requiring robust few-shot generalization. To facilitate future study, we introduce PbP, an embodied environment that supports hundreds of diverse preferences ranging from complex action sequences to specific sub-actions. Our
experiments on PbP reveal that while symbol-based approaches show promise in terms of effectiveness and scalability, accurately inferring implicit preferences and planning adaptive actions from limited data remain challenging. Nevertheless, preference serves as a valuable abstraction of human behaviors, and incorporating preference as a key intermediary step in planning can significantly enhance the personalization and adaptability of AI agents. We hope our findings can pave the way for future research on more efficient preference learning and personalized planning in dynamic environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces the challenge of developing intelligent embodied agents capable of integrating into daily human life by emphasizing the importance of learning individual user preferences. The authors present PbP, an embodied environment built upon Omniverse and OmniGibson simulation platforms, supporting realistic simulation to facilitate the study of personalized preferences and planning. The experiments reveal that existing algorithms struggle to effectively generalize personalized plans from few-shot learning scenarios. The authors propose this work to lay a foundation for further exploration into more efficient and adaptive preference-based planning systems for dynamic environments.

### Strengths
1. This paper proposes a new dataset and a simulation environment for the learning and evaluation of embodied agents focused on personalization in planning.
1. The emphasis on human preference and personalization addresses a significant topic in the field of human-centered AI.
1. The experimental findings imply significant challenges for existing algorithms when applied to PbP, underscoring the importance of further research in this area.

### Weaknesses
1. The dataset lacks sufficient details and explanation. The definitions and construction of the three levels of preferences are confusing. As demonstrated in Figure 2 and based on my understanding, the preferences are defined as different hierarchical levels of action space, but it is hard to justify how these action spaces relate to human preference or personalization in planning. Without this connection, the dataset appears similar to other few-shot LLM planning datasets. I suggest that the authors include concrete examples of preference-learning tasks and examples for each preference level to better illustrate the dataset's relevance to personalization.

1. According to the prompt format in Appendix D, PbP appears to be a summarization task in which the model classifies a video based on the preference list. Since planning inherently involves predicting future actions, summarizing what has occurred in a video cannot be equated with planning. Please correct me if I have misunderstood this aspect.

1. There is a lack of comparison with state-of-the-art planning methods. The baselines reported are not specialized for planning, and I question whether the prompts have been well-designed for a planning task.

1. The title is somewhat misleading, as it suggests that the paper proposes a new approach for planning. However, it primarily introduces a dataset/benchmark without presenting new algorithms.

1. Other issues: for the reader's convenience, please combine the appendix with the main text into a single PDF file.

### Questions
1. What do $f$, $p$, and $g$ represent in Eq 1 and 2 according to the experiments?
1. Is $l$ a loss function in Eq 2? 
1. How is the representation $p$ inputted into black-box LLMs like GPT-4(V)?
1. How many demonstrations are used for few-shot learning?
1. Line 255 mentions that there are 15,000 preference-learning tasks. How many videos are included in the dataset in total? How many different personalized planning examples are there for each task?
1. What metric is used in Table 4?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a framework for enabling embodied AI agents to adapt their behavior to individual human preferences. The authors propose the "Preference-based Planning" (PbP) environment, built upon OmniGibson, which simulates a diverse set of user preferences in embodied setting. The paper presents a comprehensive evaluation using state-of-the-art models, analyzing their ability to infer preferences through few-shot learning and apply these preferences in dynamic planning tasks.

### Strengths
1) Given the increasing interest in LLM based agents, personalization preference learning is becoming an important problem.
2) The baselines used in the paper are extensive and provide a good understanding of the current state of the area.

### Weaknesses
1) Given that the symbol based LLMs work so well compared to the vision based methods, it undermines the utility of the benchmark for preference learning from visual inputs. The example task in Table A.3 gives you an idea about this. I was able to understand the preference of the user for that task without having access to the video.
2) Some of assumptions made at the task level do not make sense to me:
  a) How would the agent get access to egocentric observations of the user? Ideally the robot should learn to pick up preferences by watching a human perform the task from its own camera. 
  b) What embodiment is used during the preference demonstrations?
  c) Similarly having access to the action sequence of the user.
  It would be good to see a discussion around these questions in the paper. 
3) The decision of using Levenshtein distance as the main metric for the evaluation is arbitrary and penalises the agent for not exactly matching the training data format. Given that the authors have access to a simulator, I would have liked seeing the evaluation of the actions in the simulator. 
4) Figure 2 can be improved:
  a) The text formatting is poor.
  b) The example tasks are not exactly clear from the figure. For example, what does it mean by the cook->cook task in the sequence level?

### Questions
1) What is the difficulty 
2) The authors introduced 3 levels of preferences, including action, option and sequence. In section 3.2 it is also mentioned that there are 75 preference tasks from the action level. Why are there no experiments for the action level preferences in the paper? 
3) What are these strings (eg. “u7cbw”) in the frame-level text annotation?

### Soundness
2

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
3

### Summary
This paper introduces the Preference-based Planning: PbP environment, used for training embodied AI agents to learn and adapt to individual human preferences in household settings, in hope to generalize to more diverse scenarios. PbP constructed a hierarchical preference structure across three levels: action, option, and sequence, within a realistic simulation (based on Omniverse and OmniGibson) and the Behavior-1k activities in 50 scenes. The authors evaluate various models in few-shot preference learning and preference-based planning, highlighting the performance gaps and challenges in modeling human preferences for adaptive action planning. The paper asserts that the inclusion of preference learning in planning could enhance embodied agents’ ability to handle personalized, context-sensitive tasks.

### Strengths
- Originality: The paper introduces a unique PbP environment to challenge current models when integrating personalized preferences into embodied AI planning. 

- Quality: The structured design of PbP, including a comprehensive dataset of diverse (thousands of activities and sample objects items diversly), parameterized preferences, is well-executed and supports rigorous evaluation. The study includes experiments comparing the performance of both video-based and symbol-based models, in both end-to-end and two stage settings, in learning and applying preferences.

- Clarity: The task formulation for PbP is well written and easy to follow.

- Significance: The insights into the current limitations of multimodal models (e.g., GPT-4V, LLaVA) in inferring human preferences is valuable for future model development in embodied AI planning with personalization.

### Weaknesses
Although the paper has a great catch point of personalization in embodied AI planning, created a realistic environment, the PbP environment generation and the paper has following concerns:

- Implicit preference ambiguity: while the hierarchical structure (action, option, and sequence) aims to maintain consistency, the authors didn't adequately ensure that preferences are truly implicit and understood across different scenes. Variability in scene context and object interactions could lead to unintended changes in how a preference is perceived for same person. Clarifying how consistency is validated across scenes would strengthen the methodology.

- Biases in few-shot demonstrations? The reliance on rule-based generation of few-shot examples might introduce potential biases. The scenarios may be constructed in a way that fits the developers' understanding of user preferences, which might not capture the diversity and unpredictability of real-world user behaviors.

- The focus on few-shot learning alone limits the benchmark. Adding fine-tuned policy models for learnt personalized embodied planning such as fine-tuning Video-based models / symbolic based models with Monte Carlo Tree Search for trajectory generation, will largely strengthen the comprehensiveness of the PbP benchmark.

- The ablation study could have explored how each hierarchical preference level (action, option, sequence) specifically impacts the models’ learning and planning performance. This would help in understanding which levels are most challenging or influential for preference learning.

### Questions
Could the authors elaborate on the measures taken to ensure consistency and generalizability of user preferences across different scenes and contexts in the few-shot experiments?

Would additional ablation studies on the impact of varying the number of demonstrations on model performance enhance understanding of personalized planning capabilities? Would incorporating experiments involving fine-tuned models with additional user preference data improve the models' inference capabilities?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper attempts towards building a benchmark/environment for building more personalized agents. In this paper, preferences ext beyond the task of rearrangement (usual in prior works) and the paper contains stronger definitions of what preferences mean. 

They introduce a new embodied environment PbP which supports several preferences at various levels (action - how to handle specific items, option - which items to prefer, sequence - preference on order of tasks), and various range of tasks (not just limited to  preferences in rearrangement like previous works).

The authors use Omniverse/OmniGibson environments/scenes with 50 scenes, with the Fetch robot as their agent in example. The reference dataset is the the Behavior-1K dataset and they build a preference vocabulary with 290 different preferences.

They generate some demonstrations once a preference and scene is sampled using oracle algorithms. The input is then as a top-down map, egocentric view, textual annotation of the current action, and third-person view of the agent. The problem is modeled as few-shot LfD.

The experiments are performed on vision-models (ViViT) VLMs (LLaVA, EILEV, GPT-4V), LLMs (GPT-4), and Symbol-Based models (GPT-4, LLaMa3).  The evaluation is done using Levenshtein distance.

They perform end-to-end and two-stage learning-planning experiments. They find that training the model to predict the preference first is better than end-to-end action prediction.

They show that VLMs struggle with learning preferences compared to LLMs, and also contain ablation study where they test on the generalization ability of their models to different scenes and objects, and same scenes and objects as the demonstration. GPT-4 text model models seem most robust, followed by GPT-4V towards generalization. They also provide an insight that the vision-based models rely on visual context to model preferences and are less robust in comparison.

### Strengths
- The paper introduces a structured approach and definitions towards modeling preferences which is a highly novel contribution.
- In order to support building agents to learn preferences, they provide a new environment and tasks which could serve as a useful benchmark for evaluating personalization.
- They perform useful ablations and add a generalization vs direct experiment which provide an understanding of how robust the baselines are towards novel scenes/objects.
- The figures are very helpful in understanding the main ideas and the approach of the paper.

### Weaknesses
- The preference vocabulary adds limitations to the paper, as it definitely will not cover all possible preferences possible in the real-world. I have doubts about the scalability of the approach to an "open-preference-vocab" scenario. Would love to hear the authors thoughts on this.
- They pass in various kinds of image-based observations - are all these observations necessary? For example, would an agent still work as well if the third-person view is not provided? This ablation seems to be missing.
- Their text-only baselines perform significantly better.  While the argument that perception models are just not good enough might be valid, this could also means that the visual cues are not necessary for modeling their  preferences and add unnecessary observations. This probably needs some investigation or refuting argument in the paper.
- One ablation that is missing is how well do they two-stage models perform when GT preference is provided.
- Minor fixes:
	- Line 183 : "whether them" -> "whether they can"
	- Figure 4: This is a nit but, the top-down map seems to be flipped in comparison to the 3D view. Shouldn't affect the agent, but might help for things to be consistent.
	- Line 345: "socre-based" -> "score-based"

### Questions
How do the authors propose to handle cases when preference for one specific item (say apples) will vary from that of another specific item (say pears) and that is not provided in the demonstrations? Do the evaluations also have this component?
- Table 1/2:  Why are there no results on the action-level data?
- Second stage results are always better, and GPT-4 seems to be the best, does that mean actions are key to understanding preferences?

### Soundness
3

### Presentation
3

### Contribution
3
