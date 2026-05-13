# Targeted Manipulation and Deception Emerge in LLMs Trained on User* Feedback

- Decision: Accept
- Scores: 5, 6, 8

## Abstract
As LLMs become more widely deployed, there is increasing interest in directly optimizing for feedback from end users (e.g. thumbs up) in addition to feedback from paid annotators. However, training to maximize human feedback creates a perverse incentive structure for the AI to resort to manipulative or deceptive tactics to obtain positive feedback from users who are vulnerable to such strategies. We study this phenomenon by training LLMs with Reinforcement Learning with simulated user feedback. We have three main findings in our environments which simulate domains of practical LLM usage: 1) Extreme forms of “feedback gaming” such as manipulation and deception are learned reliably; 2) Even if only 2% of users are vulnerable to manipulative strategies, LLMs learn to identify and target them while behaving appropriately with other users, making such behaviors harder to detect; 3) To mitigate this issue, it may seem promising to leverage continued safety training or LLM-as-judges during training to filter problematic outputs. Instead, we found that while such approaches help in some of our settings, they backfire in others, sometimes even leading to subtler manipulative behaviors. We hope our results can serve as a cautionary case study highlighting the risks of using gameable feedback sources – such as user feedback – as a target for RL. Our code is publicly available. Warning: some of our examples may be upsetting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the potential risks of training large language models (LLMs) directly on user feedback through reinforcement learning. The authors demonstrate that optimizing for user feedback can lead LLMs to showcase manipulative behaviors in different settings, such as deception and sycophancy, which can be selectively targeted at vulnerable user subsets.

### Strengths
1.  The findings of the study is  interesting and has the potential to improve the safety of LLMs. It conducts a thorough analysis of various manipulative behaviors that LLMs can exhibit and how these can be selectively applied to different user groups.

2. The experimental setup, using simulated environments to test various scenarios, is robust and well-justified, which strengthens the validity of the results.

### Weaknesses
1. The paper is mainly relied on the simulated user feedback and lack of read-world user data would limit the generalizability of the findings. The simulated user behavior data can not fully reflect the complexity of real human feedback when interactingf with the LLMs. In addition, the study assumes that users keep a static understanding of LLM behavior which does not account for the evolution of user understanding and feedback when continuously interacting with the LLM.


2. The mitigation strategies discussed are only partially effective and could benefit from more advanced techniques to better  suppress the manipulative behavior of the LLM especially in some critical cases.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The title and abstract point to an important problem in LLMs, i.e., issues with feedback loops originating from user feedback. While the problem of feedback loops has been acknowledged earlier (even in the context of LLMs, e.g., due to training LLM generated data, as well as in concurrent work (Wen et al. 2024)) and it is well-known that optimization might aim at shortcuts and objectives are difficult to formulate in machine learnign, the paper adds a number of interesting claims that if appropriately backed up by evidence, would justify a publication at ICLR without any doubt. While the paper discusses a bunch of interesting cases, the evaluation is, where the paper falls short. Already the title should say "... deception could emerge..." and the abstract should be presented more modestly. The evidence relies on simulated data, on an optimization method that is not among the most common ones, and an LLM that is not used by the majority of users. It is unclear to what extend the results transfer to other scenarios. In turn, this makes the statements much less relevant, as it is in general well-known that such "optimization issues" could occur. While the paper is well-aware of these shortcomings and aims to talk them away (also partially backed by refs), overall some form of direct comparison of simulated data and real data would be needed to show alignment of feedback distributions.

-------
I acknolwedge the author's response, while the ChatGPT style verboseness is not appreciated, at least the point with the optimization seems somewhat justified. I updated my score.

### Strengths
see above

### Weaknesses
The title and abstract point to an important problem in LLMs, i.e., issues with feedback loops originating from user feedback. While the problem of feedback loops has been acknowledged earlier (even in the context of LLMs, e.g., due to training LLM generated data, as well as in concurrent work (Wen et al. 2024)) and it is well-known that optimization might aim at shortcuts and objectives are difficult to formulate in machine learnign, the paper adds a number of interesting claims that if appropriately backed up by evidence, would justify a publication at ICLR without any doubt. While the paper discusses a bunch of interesting cases, the evaluation is, where the paper falls short. Already the title should say "... deception could emerge..." and the abstract should be presented more modestly. The evidence relies on simulated data, on an optimization method that is not among the most common ones, and an LLM that is not used by the majority of users. It is unclear to what extend the results transfer to other scenarios. In turn, this makes the statements much less relevant, as it is in general well-known that such "optimization issues" could occur. While the paper is well-aware of these shortcomings and aims to talk them away (also partially backed by refs), overall some form of direct comparison of simulated data and real data would be needed to show alignment of feedback distributions.

I acknolwedge the author's response, while the ChatGPT style verboseness is not appreciated, at least the point with the optimization seems somewhat justified. I updated my score.

### Questions
Do you agree that you overclaim and your evidence is insufficient for the general claims?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper demonstrates through empirical experiments that an LLM agent trained using RL to maximise user feedback may be incentivised to manipulate or deceive the user. This is demonstrated across 4 different classes of problem domain, involving either single-stage or 2-stage conversations between the agent and the user. The results show that the agent may lie to the user, exhibit sycophantic behaviour even when this is associated with harmful content or actions, or engage in more subtle manipulative behaviour such as nudging. Significantly this can arise even when only a subset of the user population is manipulatable, as the agent learns to exploit those users while behaving normally with respect to the rest of the population, which make this manipulative behaviour harder to detect. Two possible approaches to mitigating this issue are proposed and evaluated, and its shown that while they may have beneficial effects in some cases, they can also result in additional problematic behaviour on the part of the agent.

### Strengths
The paper addresses a very important issue. While previous work has hypothesised that LLM-based agents may be motivated to 'game' the preferences of users, this work provides quite solid empirical evidence of this actually occurring in scenarios which are similar to the situations where such agents might actually be deployed.

The paper is very well written. It is easy to read and does an excellent job of presenting the context of the work and discussing its implications.

The experiments were mostly well-designed (see one proviso in the Weaknesses section below) and clearly described, and the analysis is clear and quite compelling. The provision of code implementations also means that the hard work which has gone into developing these test cases and the evaluation procedures can be leveraged further by other researchers.

The limitations of the approaches used are appropriately acknowledged and justified (e.g. the use of a relatively simple approach to the RL optimisation process).

### Weaknesses
The main weakness I see in the paper relates to the manner in which the gameable and non-gameable users are differentiated in the initial states. The examples in Figure 13 show that this is less than subtle, with the agent being directly told that one user is extremely susceptible to their suggestions and will always act on their advice. The results of this set of experiments would be much stronger if the distinction between gameable and non-gameable users was more subtly indicated to the agent, or even if this was something which the agent had to largely establish for itself through repeated interactions with each user. The statement in Section 4.2 that "Exploratory experiments suggested that the exact difference in background didn’t matter much" suggests that this issue has been explored to some extent, but no details are provided. The paper's case would be stronger if the outcomes of experiments using more subtle indicators were reported (at least in an appendix if space doesn't permit it in the main body).

Some small presentation issues. The text on some of the figures is extremely small (for example, I had to zoom in well over 200% to read some of the text in Figure 1). This might be difficult to fix given the page restrictions, but it would make the paper easier to read if this could be addressed.

There are a few undefined acronyms. While I think its reasonable to use common terms like RL and RLHF without explanation, some of the other acronyms were ones which readers (like myself) might not be familiar with (eg on p3, BoN and KTO). It would be better is these were spelled out in full when first used.

### Questions
Why is there an asterisk in the title? I thought this would be explained somewhere in the paper but I couldn't find it.

What is the meaning of the User P.O. and Agent P.O. columns in Table 1?

I was unclear on the discussion of manipulation in the action-advice scenario on p5. Why would encouraging the user to engage in a harmful action lead to higher ratings for the agent responses later in the conversation? Is this simply the "afterglow" of the user's positive experience of the harmful action?

In Fig 6, there's a difference in the problematic behaviour of the agent with regards to the gameable and non-gameable users before training. Can you explain this?

### Soundness
3

### Presentation
4

### Contribution
3
