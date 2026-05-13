# Few-shot In-context Preference Learning using Large Language Models

- Decision: Reject
- Scores: 5, 8, 6, 5

## Abstract
Designing reward functions is a core component of reinforcement learning but can be challenging for truly complex behavior. Reinforcement Learning from Human Feedback (RLHF) has been used to alleviate this challenge by replacing a hand-coded reward function with a reward function learned from preferences. However, it can be exceedingly inefficient to learn these rewards as they are often learned tabula rasa. We investigate whether Large Language Models (LLMs) can reduce this query inefficiency by converting an iterative series of human preferences into code representing the rewards. We propose In-Context Preference Learning (ICPL), a method that uses the grounding of an LLM to accelerate learning reward functions from preferences. ICPL takes the environment context and task description, synthesizes a set of reward functions, and then repeatedly updates the reward functions using human rankings of videos of the resultant policies. Using synthetic preferences, we demonstrate that ICPL is orders of magnitude more efficient than RLHF and is even competitive with methods that use ground-truth reward functions instead of preferences. Finally, we perform a series of human preference-learning trials and observe that ICPL extends beyond synthetic settings and can work effectively with humans-in-the-loop. Additional information and videos are provided at \url{https://sites.google.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel framework called In-Context Preference Learning (ICPL), which automatically generates dense reward functions by utilizing an LLM capable of querying humans for preference data. The authors find that their method greatly outperforms one baseline, PrefPPO, with respect to sample efficiency (PrefPPO requires far more human preference queries) and task performance. The authors also find performance comparable to that of Eureka, a baseline that also utilizes an LLM for generating dense reward functions but relies upon access to ground-truth sparse reward data rather than human preference data. The authors argue, since ICPL does not require access to a ground-truth sparse reward function, it has a clear advantage for tasks that are less well-defined or require human intuition. Additionally, they argue that training with human preferences will enable greater model alignment.

### Strengths
I appreciated the fact that this paper took steps to optimize their baseline methods within reason. For instance, for Eureka, the authors continued generating candidate reward functions until the LLM had generated 6 executable ones (to make things fair for comparison against their own method).

The comparison against PrefPPO was strong.

### Weaknesses
According to table 1, ICPL performance seems no better than that of Eureka. Furthermore, substituting in the values from table 3, ICPL performance with real human preference queries does not exceed Eureka’s performance on any task except Ant. Since ICPL does not outperform Eureka, ICPL’s benefit relies upon the ease of obtaining human preference queries in comparison with a ground-truth sparse reward function. I’m not convinced that this benefit is significant.

One argument, from the introduction, is an appeal to the success of preference-based training in other domains. I’m not convinced that this success generalizes to the domain of LLM-generated reward functions. 

The other core argument in favor of preference-based training is that human insight—expressed through preference queries—can better align agent behavior with human preferences. The authors motivate this through their custom HumanoidJump task, wherein the task is “to make humanoid jump like a real human.” They argue that this is a domain in which designing a sparse reward function would be difficult due to the nuances/subjectivity of mathematically defining jumping “like a real human.” In my mind, the paper largely hinges on this argument, however the authors only offer one case-study as evidence of the efficacy of human preference data in this domain.

I could be convinced otherwise, but I think there would need to be a more thorough analysis of human preferences in comparison with sparse reward functions in order to be certain.

Also, I found section 5.3.2: Evaluation Metric to be very confusing. I wasn’t sure what an “environment instance” was. I also didn’t understand which set of task metric values was used to compute the maximum for the RTS.

### Questions
On page 1, I was confused by the phrase “tasks are distinct from the training data.” What does this mean?
Are there any other reasons to account for why human preference data might be preferable to sparse reward functions?
How do you actually generate the 6 reward function candidates? Do you randomly sample from the LLM? If so, how?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces ICPL, a method for iteratively improving reward functions for RL problems with human feedback. The method has LLMs generate reward functions specified by code, trains and executes these rewards, and then ranks the final trajectories with human feedback to then update the reward functions again.

------
After author response, my main concern (motivation above EUREKA) was clarified and my more minor concerns were addressed or clarified as well, so I have increased my rating and think the paper should be accepted. On balance I think it's a really interesting problem that's being tacked and the experiments (esp human experiments) are really interesting and compelling.

### Strengths
The idea is generally really interesting and compelling. The idea of having LLMs generate an initial reward function and then iteratively repeat it is really interesting.

The human study was really compelling and thought out. It's really good that this was actually tried and not just assumed it would work with real human feedback.

Paper really well presented, ideas presented very clearly. Motivation clear and compelling.

### Weaknesses
I am struggling to figure out what the compelling advantage is of this method over the baseline Eureka. As far as I understood reading the paper, Eureka operated from the same set of assumptions about the environment as did ICPL. And in the non-human experiment performed very similarly. In the related work it says that EUREKA requires humans to give feedback in text, whereas ICPL only requires ranked preferences. During the description in 5.2 it also says that sparse rewards are used to select the best candidate reward function. Does that mean that this is additional assumptions EUREKA needs. There was also not a comparison to EUREKA in the human study. Was that because it would not work without these other assumptions? I think it's possible I'm just misunderstanding here, so if authors could clarify this point it would really help me understand the paper and potentially improve my rating.

It's stated in the intro and conclusion that ICPL surpasses RLHF is efficiency, but RLHF is not mentioned anywhere in the experiments. Is this an experimental finding of the paper, or are authors just saying based on known findings about the efficiency of RLHF. Could a direct comparison be made in the first (non-human) experiments since you don't need actual humans and can thus potentially run more. More clarity on this point would really help.

Based on 5 iterations, I'm not sure that you can make the claim that it will monotonically improve much past that point. Did authors try past 5 (10, 20).

One sort of undiscussed thing here is that, requiring new models to be trained every iteration does mean that loop is pretty slow. Was 5 iterations chosen for that reason (so it wouldn't take multiple days). This should be maybe discussed as a weakness. E.g. for human studies or using humans, doesn't that mean the humans need to wait hours or else get new humans to provide feedback for every iteration?

### Questions
Please clarify the points mentioned above, that would really help me make a better decision about the paper. In particular explaining why this method would be better in some way that EUREKA
(Either because ICPL doesn't require some assumption made by EUREKA or it's better in some other way).

Minor:
Why GPT-4o for the human experiment only? I'm not sure how much it matters actually, but found it curious.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes In-Context Preference Learning (ICPL), a method using LLMs for more efficient preference-based reinforcement learning. ICPL uses LLMs, such as GPT-4, to synthesize reward functions based on environment context and task descriptions. These generated functions are refined through human feedback iteratively. The approach shows significant efficiency gains, requiring fewer preference queries compared to traditional RLHF and achieving comparable or superior performance to methods using ground-truth reward functions. The experiments validate ICPL's performance across various simulated and real human-in-the-loop RL tasks, showcasing robustness in complex, subjective environments.

### Strengths
* Demonstrates a substantial reduction in the number of human queries needed for preference-based learning which is sorely needed since human-in-the-loop approaches should ideally just require a handful of preferences.

* It's appreciated that the evaluations of the method is done both in synthetic data and with real humans.

* The paper is well written and the provided method is explained well. Even tho generating reward functions from LLMs is not novel, the way the iteratively make use of human preferences to update their prompt is.

### Weaknesses
 * As with all works that uses LLMs to generate reward functions from human feedback I question how well it will perform with more complex tasks which is one of the big reason for using human feedback.

* The synthetic experiment uses completely noiseless preferences while the standard in these kind of control environments are typical a noise of let's say 10%. What is the rationale for using noiseless preferences and what would be the effect of noisy preferences for your method? 

* While the authors uses B-Pref from Kimin et al for some reason they use only the PPO version even tho the repository is more associated with PEBBLE the SAC version. Why is SAC not used as well?

* 6 participants are very low for a study with humans. Still, it is better than some papers that run their method with just the authors feedback. It would be nice with some more information about the experiment like demographic data as well as discussing the limitation of a smaller sample size when it comes to generalizability.

Minor things:
* You introduce the same abbreviation on multiple occassions.

* To make the related work more complete, there is another paper using LLMs with preferences.
1. Holk, S., Marta, D., & Leite, I. (2024, March). PREDILECT: Preferences Delineated with Zero-Shot Language-based Reasoning in Reinforcement Learning. In Proceedings of the 2024 ACM/IEEE International Conference on Human-Robot Interaction (pp. 259-268).

### Questions
* What was the demographic data for the human provided feedback? 

* It seems like Eureka has very similar performance to ICPL, what would you say is the benefit of your method compared to Eureka? Eureka seems to have some constraints but it would be nice to show in experimentation or come up with a scenario where it would fail.

* It would be good to justify the length of the paper. For example, what sections do you believe require the additional space? You are of course free to use all the space but the readability of the paper could improve by making it more crisp.

* Why did you not use PEBBLE as a basline given that you made use of BPref? Also, did you consider any other baselines as there are more recent works [1,2,3] (To name a few)? It would be great if you discuss how you determined which baseline to use and if you considered any others.
1. Kim, C., Park, J., Shin, J., Lee, H., Abbeel, P., & Lee, K. (2023). Preference transformer: Modeling human preferences using transformers for rl. arXiv preprint arXiv:2303.00957.
2. Park, J., Seo, Y., Shin, J., Lee, H., Abbeel, P., & Lee, K. (2022). SURF: Semi-supervised reward learning with data augmentation for feedback-efficient preference-based reinforcement learning. arXiv preprint arXiv:2203.10050.
3. Marta, D., Holk, S., Pek, C., Tumova, J., & Leite, I. (2023, October). VARIQuery: VAE Segment-Based Active Learning for Query Selection in Preference-Based Reinforcement Learning. In 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (pp. 7878-7885). IEEE.

I am more than willing to up the score given reasonable answers to these points.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a reward design method. It uses LLMs to generate reward functions to calculate the reward, and the prompt of the LLM is learned through human feedback of the policy rollouts and other historical information in the loop.

It replaces the implicit reward model in traditional RLHF with an LLM and its output reward function. This enhances the interoperability and capacity of the reward design.

### Strengths
It replaces the implicit reward model in traditional RLHF with an LLM and its output reward function. This enhances the interoperability and capacity of the reward design.

### Weaknesses
(1) ICPL involves human labor, but does not show any significant gain over Eureka, which doesn't require any human feedback.

(3) For challenging tasks, true human feedback does not work better than proxy human feedback. This undermines the necessity of involving humans.

(2) For challenging tasks, like humanoid jump task, ICPL does not have any solid comparisons with other baselines.

### Questions
(1) Why is it necessary to use pair-wise human feedback (a good example and a bad example) if RTS is available? Why not just use all the reward functions with their RTS as prompt (maybe together with other information like reward trace, differences, etc) to generate reward functions?

(2) Could you please explain the counter-intuitive results in Table 2? It seems the more prompt components you remove (from w/o RT, to w/o RTD, to w/o RTDB), the better performance it gets (w/o RT wins 2 tasks, w/o RTD wins 3 tasks, and w/o RTDB wins 4 tasks), but adding all the components back, i.e., ICPL(Ours), it wins all the tasks.

### Soundness
2

### Presentation
3

### Contribution
2
