# PREDICT: Preference Reasoning by Evaluating Decomposed preferences Inferred from Candidate Trajectories

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Accommodating human preferences is essential for creating AI agents that deliver personalized and effective interactions. Recent work has shown the potential for LLMs to infer preferences from user interactions, but they often produce broad and generic preferences, failing to capture the unique and individualized nature of human preferences. This paper introduces PREDICT, a method designed to enhance the precision and adaptability of inferring preferences. PREDICT incorporates three key elements: (1) iterative refinement of inferred preferences, (2) decomposition of preferences into constituent components, and (3) validation of preferences across multiple trajectories. We evaluate PREDICT on two distinct environments: a gridworld setting and a new text-domain environment (PLUME). PREDICT more accurately infers nuanced human preferences improving over existing baselines by 66.2\% (gridworld environment) and 41.0\% (PLUME).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a method called PREDICT which is designed to infer individual user preferences from user interaction trajectories. The proposed approach is evaluated in two settings: a toy gridworld environment designed by the authors in which an agent must pick up objects on a 5x5 grid while maximizing a reward with user preferences unbeknownst to the agent, and PLUME, an assistive writing preference environment developed by the authors by modifying the recently proposed PRELUDE environment.

Update: The discussion has been helpful in improving the clarity and positioning of the work. I have increased the presentation score and overall rating.

### Strengths
The proposed idea is quite interesting. The idea of examining counterfactual trajectories seems novel and is intuitive. Additionally, it appears the proposed PLUME environment addresses valid limitations of prior work. The presented main experimental section also includes several important ablations to consider, and the main results indicate strong improvements over the presented baselines.

### Weaknesses
*The writing is somewhat confusing.* For instance, Figure 2 is pretty underspecified and hard to parse, and many of the important details are not available in the main text (e.g., in L122-139 it is hard to concretely understand what the algorithm is doing; preference aggregation in L165-169 is unclear).

*The overall interaction setting seems unrealistic.* The PICKUP environment is rather toy-ish, and it is difficult to say whether such types of preference identification (determining what colors a user prefers) is actually reflective of real-world personalization settings (e.g., linguistic style, interaction length). While PLUME appears to address some of these concerns, it is actually not clear to me whether the cost function is representative of user preference. The number of users seems quite small (only five for summarization and four for email writing).

*The baseline comparisons are rather limited.* In Figure 3, PREDICT may outperform CIPHER-1, but it underperforms ICL for all LLMs evaluated. While it seems that PREDICT + ICL outperforms ICL alone in Table 1, this raises questions about comparing PREDICT with more sophisticated prompt-based baselines which may involve examining trajectories and requiring similar levels of complexity as PREDICT + ICL (for instance, Monte-Carlo Tree Search). Relatedly, Behavior Cloning is the only baseline for the gridworld environment whereas it may be more expected to compare against standard RL-based baselines in such environments. While the authors also claim that PREDICT is not limited by the issues of fine-tuning, it is not clear to me that it is necessarily advantageous compared to tuning.

### Questions
What setting would you propose in which such learned preferences are actionable?

How do you obtain sufficient user trajectories in practice?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposed a method for personalized LLM assistant that infers implicit user preference. The PREDICT pipeline includes an initial LLM assistant which conducts the same task as the user, a preference-inferring agent which summarizes the difference between the user and the assistant's trajectory, as well as a validation step to generalize the inferred preferences on multiple users. 

The paper conducted experiments in two environment settings, a grid world navigation, and PLUME, a text summarization and email editing environment. The paper proposed two evaluation dimensions, preference quality and action quality, to measure the inferred preference correctness and the overall task completion rate. Both evaluation dimensions are further translated in domain-specific measures.

The paper compared the proposed method against several baselines and conducted ablation studies, and demonstrated improved performance.

### Strengths
- The paper studies an important and challenging problem: how to infer and accommodate user's implicit preferences
- The paper proposed a method to infer user's preference by comparing user VS LLM assistant's action trajectories, decompose into several components, and validate the preferences across users
- The paper conducted experiments in two environments
- The paper conducted thorough experiments with ablation studies and compared against several baselines

### Weaknesses
The paper could largely benefit from a major round of revision:
- It would be helpful to illustrate detailed examples for each of the benchmark environment in the main paper
- Figure 2 is very abstract. It would be helpful to add more details, such as examples of the constituent components, examples of the contrast between user and agent's predictions, examples of validation set, etc.
- It would be helpful to formally define each of the evaluation metrics
- Table 1: how significant are there results as most of the differences fall within the std margin. How would Table 1 support the main claim (Ln 22) that 'PREDICT more accurately infers nuanced human preferences', especially when the Ln 420 concluded that 'PPCM does not show a clear trend' when comparing PREDICT to PREDICT_{CP}
- The paper heavily references Gao et al. 2024 for experiment setups, methods, etc without specifying the necessary details within the paper

### Questions
1. Ln 142 "base components": are they all hand crafted for each task?
2. Ln 156, 173, 260: who are the 'users'? Human? LLM proxy?
3. Ln 233: it is unclear what the relevance/importance it is for the environment to be partially observable

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents PREDICT (Preference Reasoning by Evaluating Decomposed Preferences Inferred from Candidate Trajectories), a novel method aimed at enhancing the inference of human preferences in AI agents. Addressing the limitations of existing Large Language Models (LLMs) that often generate broad and generic preferences, PREDICT introduces three key innovations: iterative refinement of inferred preferences, decomposition of preferences into constituent components, and validation of preferences across multiple user trajectories. The approach is rigorously evaluated in two distinct environments—a gridworld setting (PICK UP) and a newly introduced text-domain environment (PLUME)—demonstrating substantial improvements over baseline methods by 66.2% in PICK UP and 41.0% in PLUME. Additionally, augmenting PREDICT with in-context learning yields a further 17.9% enhancement, underscoring its effectiveness in capturing nuanced human preferences.

### Strengths
1. Good Solution: introduce a thoughtful combination of iterative refinement, preference decomposition, and validation, effectively addressing the generic nature of existing preference inference methods.

2. A new reliable benchmark: LUME environment is a valuable contribution, offering a more reliable benchmark compared to previous setups like PRELUDE.

3. Significant Performance Gains: The method achieves impressive improvements over established baselines, notably outperforming behavioral cloning by 66.2% in PICK UP and CIPHER by 41.0% in PLUME, highlighting the practical efficacy of the proposed components.

### Weaknesses
1. Need investigate how varying iterative refinement steps impacts the performance and efficiency of the method, potentially overlooking optimal configurations.
2. Lack of Real User Case: experiments are primarily based on synthetic users, consider adding some real case analyses to verify the practicality and generalizability of the method.

### Questions
See weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a prompting-based method for inferring and refining user preferences from action trajectories. The proposed method takes an initial set of inferred preferences, asks a language model to refine them (e.g., by collapsing duplicates, breaking down complex preferences into individual preferences) and then validates the preferences by asking a language model whether sampled user examples confirm or contradict the inferred preference. The paper tests the proposed approach in two domains, (1) a gridworld object collection domain and (2) a writing/editing benchmark, finding clear gains, especially in the latter domain.

### Strengths
1. The proposed method is relatively simple but appears to provide clear gains on the preference inference task 
2. The paper provides two new tasks, one toy gridworld (PICK UP) and one modification of an existing assistive writing task (PLUME). These tasks, especially PLUME, seem like good starting points for future modeling work

### Weaknesses
1. The proposed method and benchmark could be a bit more clearly described. In particular, I found the interleaving of contributions and the actual method description in Section 3 to be a bit confusing, and it’s a bit difficult to understand how the iterative refinement step works without looking at the corresponding prompts in the Appendix — perhaps a more detailed Figure 2 could help here? I also think the description of PREDICT is a bit hard to follow for someone not familiar with PLUME (and again, I think figures would help!)
2. Not really a weakness (i.e., does not affect my score): the paper only focuses on inferred preferences, rather than stated preferences. It would be great to see how this approach works in a setting with both stated and inferred preferences

### Questions
1. One concern I had with the preference validation approach is that preferences might only apply in rare circumstances. It seems that the validation stage would then return almost all neutrals, which would result in filtering out, even if the preference was very clear. Is this reasoning accurate and is there a way to address this issue (e.g., by doing some more targeted sampling)?
2. Honestly, I am not sure why performance on the PICK UP task increases, given the simplicity of preferences in that environment. One potential concern would be that if initial inferred preferences are over objects (e.g., “prefers yellow triangles”), then the breaking down of preferences could provide an implicit bias toward the “compositional” preference structure of the task. Can you provide a bit more intuition on whether this is a valid concern, and why you think performance on the PICK UP task improves?
3. Would it be possible to provide some examples of inferred preferences before and after applying your method somewhere in the paper?

### Soundness
3

### Presentation
2

### Contribution
3
