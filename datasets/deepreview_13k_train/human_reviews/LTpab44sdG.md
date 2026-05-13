# Practical alignment requires more than learning from human feedback

- Decision: Reject
- Scores: 5, 8, 5, 8

## Abstract
Ensuring the alignment of artificial intelligence (AI) systems with human objectives is a critical challenge in the development of safe and effective AI technologies. Reinforcement learning from human feedback (RLHF) has been a predominant method to tackle this challenge. However, this framework operates under the unrealistic assumptions that human preferences are accurate reflections of their desires and that they remain constant over time. This paper identifies and challenges these assumptions by illustrating how they can lead to undesirable consequences, particularly when human beliefs about the environment are incorrect or mutate over time. To address these challenges, we introduce a novel framework termed practical alignment. This framework redefines the alignment objective to accommodate the variability and irrationality of human beliefs, emphasizing the need for AI systems not only to learn from but also to teach humans about the world. We discuss the theoretical underpinnings of practical alignment and introduce MindGrid, a toolkit designed to simulate and evaluate alignment scenarios. Our experimental results using large language models in teaching scenarios underscore the importance of teaching skills as a requisite capability to achieve alignment.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a formalization of the AI alignment problem that distinguishes ostensible alignment (where human and AI agree on a target and the AI follows it) and practical alignment (where the target is additionally normatively correct). The paper proposes a few theoretical results in this framework as well as experiments in a Gridworld environment with simulated human language feedback to illustrate the proposed framework.

### Strengths
The paper is addressing an important problem: clarifying and formalizing the target of "AI alignment". The proposed distinction between ostensible alignment, inner alignment, and normative alignment is clear and adds conceptual clarity. The insight that humans can be mistaken when giving feedback to AI agents is importantly correct and the paper has some useful ideas for addressing this.

The proposed environment is interesting because it combines an agentic task with a language interface, which allows to test agentic alignment concepts with current language model agents.

### Weaknesses
I don't think the proposed framework is very insightful on it's own and the paper did not convince me that it is a useful formalization. The essential new component (that is not covered by previous formalizations like CIRL) seems to be that humans can be uncertain about their own preferences. This uncertainty can lead to the agent being "ostensibly aligned" but not practically aligned and this gap can get worse over time. While I agree that this is an important problem, the formalization does not seem to add anything that helps to solve this problem.

To be convinced that the formalization is useful, it would have to result in new insights that are not clear from the problem definition, or it would have to allow deriving quantitative bounds on the different misalignment gaps, and compare different methods. Both of these are missing from the current paper.

I also find the way the framework is set up not really mirrors how eg. RLHF is used in practice. The preference learning setting considered in the paper has a human pick between plans proposed by the agent (Figure 1). However, RLHF more commonly has humans pick between actual trajectories (eg., in Christiano 2017). If the human picked between two trajectories from the real world, the problems in eg. Fig 1 would not occur in this way. The paper discusses the human world model being wrong as a fundamental problem, but does not acknowledge that the extend to which this is problematic has a lot to do with the specific RLHF setup that is chosen.

While the experiment setup is interesting, the environments are very limited. There are two basic gridworld environments with a language interface. The experiments are not surprising and do not seem to be answering research questions posed by the practical alignment terminology. Rather, the experiments seem closer to the start of a benchmark. I think a benchmark built on these environments could be interesting, but the current setup is too limited.

So in summary, I don't think the contribution in this paper is large enough to warrant acceptance. I could reconsider my assessment if I am convinced the proposed framework is more useful, for example because I did not understand an important aspect of it.

### Questions
* Could you elaborate on why you find the proposed framework useful compared to prior frameworks for formalizing alignment?
  * What kind of results does your framework allow you to derive that prior work cannot study?
  * How could this work help to solve the proposed alignment problems?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This work presents a theoretical framework called practical alignment, which aims to address some of the limitations of the standard RLHF paradigm. Specifically, the standard RLHF framework assumes that human preferences accurately reflect human desires and that preferences remain constant over time. In contrast, this work presents a framework that does not assume that human preferences are static but are influenced by human beliefs about the world. This allows modeling scenarios where human beliefs are false or subject to change over time. By explicitly differentiating between human beliefs (mutable) and desires, this work introduces an optimization problem that naturally encourages an AI system to not only learn from a human, but also to correct their beliefs. Finally, this work presents an experimental framework called MindGrid to evaluate alignment scenarios. Here, results show that while LLMs can outperform naïve baselines, there is still significant scope for improvement.

### Strengths
1. **Clear writing**: The paper is well-written and generally easy to follow. The related work is thorough, and the overall flow is smooth. 
2. **Novel Framework**: This paper presents a novel framework for alignment that aims to fix some of the well-known issues with the standard RLHF paradigms. Although there are limitations with the new framework, it presents an interesting lens on alignment. Notably, the work presents an example of how deceptive/manipulative AI agents can emerge from ostensible alignment, which is a key topic of interest in the community.

### Weaknesses
1. **Mathematical notation**: The mathematical notation at times can be more complicated than needed and I believe that mathematical clarity can be improved.


### Questions
1. In the practical alignment framework, it is assumed that the humans know $\psi^H$, the parameters for their desire function. If this is the case, then what prevents the AI agent from directly learning the desire function and optimizing that. In other words, what is the difference between the descriptive reward function of the ostensible framework and the desire reward function of the practical framework? I think giving more concrete examples here can be very helpful. 
2. The presented framework assumes that human preferences might change with their belief about the world, but their desires stay constant. Although this is very abstract, it is possible for desires to change with beliefs about the world. I think it comes down to the modeling assumptions and there might not be one right answer, but I am curious to know the authors’ thoughts on this. 
3. I see this framework as being more applicable to embodied AI systems that are interacting with the real world. These settings would naturally have many instances where a human’s internal world model is different from the real world. However, is this framework also applicable in the digital setting (such as AI chatbots)? What do the authors consider to be a world model here, what are concrete instances where the human’s model is incorrect? 
4. The LLMs are specifically prompted that the human’s plan is outdated and that changes have been made to the grid. An ideal benchmark would be one where the LLM uses the human’s plan, infers that the world has changed and proceeds to correct the human’s belief about the world. What were the motivations behind the design decisions of this benchmark? 
5. Is the communication model (discussion phase) described in this work new or has it been used in standard practice? 
6. Why is it assumed that a human is also optimizing their communication policy? Does anything change if it is assumed that the human has a fixed policy? It might make notation simpler if it is not a necessary part of the framework.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides conceptual frameworks for 'ostensible' and 'practical' alignment. It shows that techniques like RLHF promote ostensible alignment as they incentivize performing best with respect to the world model of the human principal. However, the practical alignment objective which optimizes human desire function in the real world environment is more robust.

### Strengths
The topic of the paper is very interesting and challenging. I think the authors did a good job at developing conceptual frameworks that are insightful. The main strength of the paper is that it has done an excellent job at formalizing lots of informal intutitions that people who think about and work on AI alignment have. If I did not have concerns around the presentation of the paper, I would have likely recommended a strong accept (my current recommendation is weak reject).

### Weaknesses
- The paper is hard to follow. This is my major issue imo. This paper is very interesting, but I am afraid that if the presentation is not accessible, it will fail to have much impact. See my notes on presentation below.
- The discussion of related works is quite shallow, and an important related work in my opinion is not covered (https://arxiv.org/abs/1711.02827).
- The paper does not propose a method for 'practical' alignment; this is not strictly a weakness but lack of a method does weaken the contributions the paper is making a little.

#### Partial notes on presentation (these also double as questions in some cases)
*Section 3.1*
- The paper directly dives into describing what the ostensible alignment is without presenting the setup being assumed. Is it an MDP, POMDP, CIRL like Dec-POMDP setup? My sense is it is CIRL like Dec-POMDP setup but I am not super confident in that.
- The paper is often introducing terminology without properly defining them. For example, second para of section 3.1 introduces the concept of plan without defining what the plan is.
- In description of ostensible alignment process, it is not clear to me how to think about 'conversation context'. Is it something like 'initial state' in MDP framework?
- Bold p is used for joint policy, but for individual policies $p^A$, $p^H$, the p used is not bold. Authors should be consistent in their use of bold. I would also suggest avoiding the use of p and using some greek/latin symbol for policy as p is sort of a universal symbol for policy distribution. The convention in RL is to use \pi, but the authors are using it already.
- Equation 1 was highly confusing for me, RHS is the definition of J^H(p) but it looks as the definition of max J^H(p)..
- \mathcal{U^H}, \mathcal{U^A} are never defined.. presumably they are the sets from which utterances are sampled?
- I think if the authors lead the discussion with some sort of example that grounds these concepts, that would make it much easier for the reader to understand them.
- Would not it make sense to start by introducing practical alignment; and then discussing 'ostensible' alignment as a simpler case? Seems like the main (only?) diff btw ostensible and practical alignment is whether the $\theta$ used in the reward function is $\theta^*$ or $\theta^H$.

*Section 3.2*
- Defining $(\psi^H, w^*)$ to be $theta^*$ does not seem like a great choice to me; it is probably not saving you much space so why not just have $\psi^H, w^*$ directly in the expressions?
- Definition 3.1 should be a lemma.

### Questions
1. Are the authors aware of inverse reward design (https://arxiv.org/abs/1711.02827)? It is probably the most related work to this paper that I can think of; but has not been cited in the paper. I would like authors to include discussion on novelty of this work relative to IRD. In general, the related works section is relatively thin for my liking with most citations after 2020. The 'teaching' aspect of the framework is also related to works on 'eliciting latent knowledge' (https://www.lesswrong.com/posts/qHCDysDnvhteW7kRd/arc-s-first-technical-report-eliciting-latent-knowledge), debate between agents (https://arxiv.org/abs/2402.06782) and eliciting human preferences better (https://arxiv.org/abs/2310.11589).

2. I don't think 'practical alignment' is a great name for the concept/framework being introduced in the paper. In fact, it seems to be harder to implement and thus seems a bit impractical. Authors should rename it to something like 'idealized alignment'.

3. In practical alignment, does the agent observe $\omega^*$? This is not explicitly stated but based on the description of the experiments, seems to be assumed. This seems like a very strong assumption and should be made explicit and acknowledged as such.

4. In equation 4 the meaning of $\theta^A$ is not obvious to me. Similarly, the meaning of subscript of T in $\theta_T^Z$ is also not clear.

5. Can you give a scaling curve for this? My guess is that performance would change abruptly past some threshold.
>Interestingly, adding training examples generally worsens model performance.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce "practical alignment," an AI framework designed to address limitations in current alignment methods, especially Reinforcement Learning from Human Feedback (RLHF). RLHF assumes that human feedback accurately reflects true desires and remains stable, leading to potential misalignment when human beliefs are flawed or change over time. The authors argue that effective AI alignment should adapt to these variabilities and that AI should not only learn from but also educate humans to correct misunderstandings. They introduce the MindGrid toolkit, which allows simulation of practical alignment scenarios, including a teaching component where the AI informs humans about reality to adjust their beliefs. Experimental results on language models demonstrate the importance of teaching in achieving alignment and reveal current limitations in language models' teaching abilities.

### Strengths
-The practical alignment framework is an innovative approach that considers human belief variability, introducing a more realistic and dynamic model for AI-human alignment.
- The MindGrid toolkit is a valuable contribution, providing researchers with a means to simulate complex alignment scenarios that involve misunderstandings and belief updates.
-The paper advances AI alignment by emphasizing the importance of an AI’s teaching role, which could make AI systems more effective collaborators.
- The authors conduct extensive tests with different language models, showing the practical challenges and gaps in current alignment techniques.

### Weaknesses
 - While addressing variability in beliefs, the model assumes a static "real world" that may not hold in all domains, such as those influenced by subjective or evolving truths. This is a significant limitation, as many real-world scenarios involve dynamic and contested facts, where the very definition of 'truth' can be fluid. For instance, in social sciences or political contexts, the 'real world' is often a construct of collective beliefs and narratives, which can shift dramatically over time. The model's reliance on a fixed objective reality limits its applicability in these complex domains.
- The experiments are limited to simulated environments, which might not fully capture the complexity of real-world human-AI interactions, particularly where human beliefs vary significantly. The simulations, while useful for initial testing, may not adequately represent the nuances of human cognition and the diverse ways in which individuals form and update their beliefs. The simplified scenarios might not account for the influence of emotional factors, social biases, or cognitive limitations that can significantly impact human feedback and learning processes. Furthermore, the simulated teaching interactions might not reflect the challenges of real-world communication, where ambiguity and misinterpretation are common.

### Questions
- How would practical alignment handle environments where the "real world" is itself subjective or dynamic, such as in social or cultural contexts?
- How does the model account for situations where human feedback may be influenced by biases or lack of knowledge rather than misunderstandings about objective facts?

### Soundness
3

### Presentation
3

### Contribution
3
