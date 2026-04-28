# Beyond Autoregression: Discrete Diffusion for Complex Reasoning and Planning

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Autoregressive language models, despite their impressive capabilities, struggle with complex reasoning and long-term planning tasks. We introduce discrete diffusion models as a novel solution to these challenges. Through the lens of subgoal imbalance, we demonstrate how diffusion models effectively learn difficult subgoals that elude autoregressive approaches. We propose Multi-granularity Diffusion Modeling (MDM), which prioritizes subgoals based on difficulty during learning. On complex tasks like Countdown, Sudoku, and Boolean Satisfiability Problems, MDM significantly outperforms autoregressive models without using search techniques. For instance, MDM achieves 91.5\% and 100\% accuracy on Countdown and Sudoku, respectively, compared to 45.8\% and 20.7\% for autoregressive models. Our work highlights the potential of diffusion-based approaches in advancing AI capabilities for sophisticated language understanding and problem-solving tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Multi-granularity Diffusion Modeling (MDM), a method that prioritizes subgoals by difficulty to improve complex reasoning and planning in tasks where autoregressive models fall short. MDM significantly outperforms autoregressive approaches on challenging tasks like Countdown and Sudoku, achieving accuracy rates of 91.5% and 100%, respectively. The results demonstrate the promise of diffusion-based methods for advancing AI in complex language understanding and problem-solving.

### Strengths
- The authors address a novel and important problem in reinforcement learning (RL): subgoal imbalance in planning tasks. This issue is particularly relevant for the application of deep learning models in RL.
- They propose a new method to tackle subgoal imbalance, which appears to be a reasonable approach to addressing this challenge.
- The authors demonstrate that their method outperforms traditional autoregressive models on complex tasks, including Countdown, Sudoku, and Boolean Satisfiability Problems.

### Weaknesses
 - The evaluation is limited to well-designed, controlled tasks, which may restrict the general applicability of the proposed method. It would be interesting to see if this approach is also practical in more realistic RL scenarios.
- While they extend a diffusion model to handle subgoal imbalance, I wonder if a similar technique could be applied to autoregressive language models.  Extending this work to LLMs could make it more broadly applicable and impactful.
- The authors provide a strong example of subgoal imbalance in Section 3. However, it would be helpful to understand how frequently this issue occurs in real-world RL settings. Including concrete, real-world examples would enhance the appeal of this work.

### Questions
1. How does subgoal imbalance impact performance in real-world RL tasks? Could you provide concrete examples of this issue in practical applications?
2. How does the performance of the proposed method compare to autoregressive models in terms of computational efficiency (i.e., training time and inference time)?

### Soundness
3

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
This paper explores a few popular hard/challenging planning-based reasoning tasks such as Countdown and Sudoku, and whether a discrete diffusion model can solve them better than an autoregressive model. I am fairly unfamiliar with diffusion models and unable to judge whether the proposed method (multi-granularity diffusion modeling) is a significant contribution or a very minor one -- judged by Eq-8, it is a form of loss reweighting. The derivation for Eq (6) seems novel, but again, I am not fully sure if the derivation is a trivial reuse of previous work or a fully novel insight. 

I have a few questions about several of the paper's claims. If properly addressed, I think this would be a good paper for acceptance.

### Strengths
The paper is very well-motivated and well-written.

I especially enjoyed Section 3, where the authors tried to use a simple metric (planning distance) to capture the difference between several methods (AR, Reverse-AR, and Diffusion). This alone is already a novel contribution.

The experimental result is mind-blowing. The proposed method almost completely solves Countdown (CD) and Game of 24, both are major challenges and are under active investigation. It would have been nice if, as reviewers, we had the time, energy, and resources to reproduce and replicate the results of the paper so that we could validate the claim. The authors have provided the code. A quick glance did not raise immediate red flags for me.

### Weaknesses
I do not consider these weaknesses, but any paper can always improve:

The datasets are mostly Countdown, Game of 24, and Sudoku. I think they are sufficient as of right now to show proof of concept. It would obviously be nicer if we saw other larger domains (such as Blocksworld [1]). However, the three datasets/domains investigated are the most popular ones and, therefore, sufficient.




### Questions
1. I want to understand Proposition 1 better: for a sequence $q(x)$, let's take your toy planning task as an example; if that is my true distribution, then I can just do an MC sample from $q(x)$ (by conditioning on previous states). Why would it not follow an autoregressive pattern? Is Proposition 1 as straightforward as thinking because there is an action policy $\pi$, therefore, $p_{\pi_1}(x_n | x_{1:n-1})) \not = p_{\pi_2}(x_n | x_{1:n-1}))$? I fail to see why this is the case.
2. "The regretful compromise" -- I fail to see what the compromise is. Can you tell me if this is you reinventing the concept of "compounding error" in [1]? If so, I am astonished that we seem to be recycling and relearning the same phenomenon every 5-7 years. 
3. Looking at Eq (8), which is a per-token loss reweighting -- it seems that we can apply per-token loss reweighting, too. Can the authors comment on whether per-token loss reweighting can help AR, too (address the issue discussed in Proposition 1)?

[1] Lamb, Alex M., Anirudh Goyal ALIAS PARTH GOYAL, Ying Zhang, Saizheng Zhang, Aaron C. Courville, and Yoshua Bengio. "Professor forcing: A new algorithm for training recurrent networks." Advances in neural information processing systems 29 (2016).

### Soundness
2

### Presentation
4

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
This work proposes to use a form of diffusion models as an alternative to auto-regressive models for reasoning and planning problems. The authors illustrate the weaknesses of auto-regressive models with planning by introducing the notion of subgoal imbalanced or the idea that the true data distribution may not follow an autoregressive pattern. Using the sub-goal learning as a motivation, the authors propose multi-granularity diffusion model which uses a re-weighting procedure for training efficiency. Through a variety of planning tasks including Countdown, Sudoku and the boolean satisfiability problem (SAT), the authors demonstrate both the efficiency of the multi-granularity diffusion model compared to auto-regressive models and much better performance on more difficult tasks.

### Strengths
- Novelty: This work is particularly insightful. Not only does the work show experimentally demonstrate the success of diffusion models, it also provides intuition through the sub-goal problem. As mentioned in the related work, diffusion models have been explored in other domains as alternatives to auto-regressive models but it has not been done so in the planning domain. Given how frequently auto-regressive models are used, using diffusion models successfully for planning is almost by definition novel. 
- Presentation and Clarity:  Related to the point above, by incorporating experiments through  early in the paper and providing intuition, the presentation made it much easier to understand.
- Contribution: There are several strong contributions. First, is replacing auto-regressive models with diffusion models in general. The second is the introduction of the multi-granularity diffusion model. The third, is showing that diffusion models are more efficient (especially with regard to tokens and on cheaper hardware, V100) for planning tasks.

### Weaknesses
 - The main weakness would be on the types of planning tasks that the model is evaluated on. Other works like Tree of Thought evaluate on other planning tasks such as Mini-Crossword (in addition to the game of 24). It would be interesting to see how MDM does on tasks that also require some ‘common sense.’ 
- Scaling of MDM: Part of the advantages of AR models is the ability to scale up due to the ease of generating data with next-token prediction. Could MDMs exhibit such a property? In the results of the CD task, we see that with CD 4 and CD 5, the 85 M does better than the 303 M.

### Questions
In addition to the questions in the weaknesses:
- Could MDM exhibit the properties of in-context learning that AR models are known to have? Could it be possible once there is a sufficient amount of data?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors begin by pointing out that autoregressive (AR) models struggle with reasoning and long-term planning tasks. The authors propose _discrete diffusion (DD)_ as a better modeling approach for these classes of tasks. 

They begin their contributions by providing a theoretical argument for their assertion from the viewpoint of what they deem "subgoal imbalance". Here, they argue that the subgoals faced when attempting reasoning and planning tasks autoregressively are not all necessarily of equal learning difficulty. The authors follow this initial theoretical setup with empirical evidence on a toy synthetic planning task demonstrating that autoregressive models struggle when the subgoals become more difficult, e.g. require longer planning horizons.

The authors pose the same toy task to a DD approach, which they demonstrate does not show similar signs of failure as the AR approach. Given this, they continue their contributions by theoretically outlining _why_ the DD approach does not struggle as much as the AR model on the same toy task. Here, they compare the losses of the AR approach and DD approach, and point out that the DD loss remains low compared to its AR counterpart. Moreover, they show that the unweighted loss of the DD approach reveals the following trend: as the number of timesteps increases, subgoals at smaller timesteps become easier to learn (face lower loss). The authors analyze this from a "multi-view learning" perspective, arguing that each x_t in DD can be interpreted as a different view of x_0. This, they argue, affords more effective learning of challenging subgoals.

Given these insights, the authors develop an extension to discrete diffusion tailored to planning and reasoning where the "subgoal imbalance" problem supposedly emerges. Their extension, dubbed multi-granularity diffusion modeling (MDM) consists in introducing a token-level reweighting mechanism in the Monte-Carlo sampled DD loss equation, designed to adaptively reduce the loss for easy tokens while emphasizing the loss for harder ones. 

The authors then test their method on 3 "real-world scenarios", namely on Countdown, Sudoku and SAT. They compare MDM to existing diffusion models as well as a number of AR baselines. Throughout, the authors empirically demonstrate the superiority of DD approaches to these planning and reasoning tasks, as well as the performance edge gained with MDM over existing DD approaches.

### Strengths
- The paper is very well structured. Ideas are presented in a organised, sequential manner with little to no jumping required. Evidence and explanations are provided soon after assertions. The positioning of every section makes sense.
-  The paper is original in some ways: it contributes this novel concept of "subgoal imbalance" and later links "multi-view learning" as a possible explanation for diffusion's superiority over autoregressive methods when it comes to planning and reasoning tasks. 
- The main contribution of the paper: theoretical argumentation supported by empirical evidence for why diffusion works better than autoregression for planning and reasoning is a significant contribution considering the value of such capabilities, and may provide a further shift towards diffusion methods in the field.

### Weaknesses
 - I found that the definition of "subgoal imbalance" was a bit awkward -- is this something that can only be talked about from an autoregressive perspective or is this a general aspect of multi-step tasks such as planning and reasoning? The more formal proposition at line 160 makes it sound like the former, but throughout the text my understanding leans more to the latter. I recommend trying to make this proposition more rigorous, more carefully outlining when it applies and when it does not. 
- I found the "multi-view learning" perspective a bit underdeveloped. I think it would help to define what "view" means in this context, rather than expecting the reader to refer to Xu et al. 2013. Especially given how well the rest of the paper flows. In general I think this part of the paper (L243-252) could have gone into more depth for readers to get a better understanding of what the authors were intending, because at the moment it reads as a bit vague and non-rigorous.
- Perhaps because I did not fully grasp the "multi-view learning" perspective due to its underdevelopment, it is not 100% clear to me how what is observed in 3.2 led to the insights on which MDM is developed in 3.3. Perhaps it would have been better to drop the "multi-view learning" perspective and focus entirely on the subgoal imbalance idea, which I think transitions naturally to the extension presented in 3.3 without much of the argumentation in 3.2 needed. 
- I am confused by the inconsistency of the baselines in section 4. It would have been nice to always use all the baselines, but for some reason e.g. GPT-4 ToT is only used on Game of 24. 
- Similarly, since there are no claims of the generality of diffusion models which is on the other hand often touted as an emergent property of the autoregressive models, it would have been nice to have other non-general, planning-specific baselines to compare against. E.g. the question I am getting at is, many "real-world" scenarios could be solved analytically a Planning Domain Definition Language (PDDL), so why should one use MDM (or other diffusion methods) instead?

### Questions
- I've already hinted this a little bit above, but one of the properties of these very popular AR models is their emergent generality: they can be successfully applied to a variety of downstream tasks while being trained on a simple autoregressive objective. In the paper you have shown that _when training specifically for planning_ discrete diffusion is a better approach than autoregression. My question is -- should we expect this finding to generalize to "general" diffusion solutions too? I.e. suppose one has some foundation *diffusion* LM -- do we expect such an LM to still be better at planning than an equivalent AR LM? Or is the assertion/result of the paper only for the narrow case of planning specific training? 
- If indeed this paper is about the narrow case, in which way, if any, would you envision incorporating this narrow case into a more general model capable of more than just planning?

### Soundness
2

### Presentation
3

### Contribution
3
