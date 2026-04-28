# SHINE: Shielding Backdoors in Deep Reinforcement Learning

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Recent studies have discovered that similar to supervised classifiers, a deep reinforcement learning (DRL) policy is also vulnerable to backdoor attacks. Existing defenses against backdoor attacks either do not consider RL's unique mechanism or make unrealistic assumptions, resulting in limited defense efficacy, practicability, and generalizability. In this work, we propose SHINE, a novel backdoor shielding method for DRL. SHINE first leverages policy explanation techniques to identify the backdoor triggers and then designs a policy retraining algorithm to eliminate the negative impact of the triggers on backdoored agents. We theoretically prove that SHINE guarantees to improve a backdoored agent's performance in a poisoned environment while ensuring its performance difference in the clean environment before and after shielding is bounded. We further conduct extensive experiments that evaluate SHINE against three mainstream DRL backdoor attacks in various benchmark RL environments. Our results show that SHINE significantly outperforms existing defenses in mitigating these backdoor attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed an algorithm dubbed 'SHINE', which is a testing-phase shielding method against backdoor attacks in the context of Deep Reinforcement Learning (DRL). SHINE first captures the critical states related to the backdoor trigger based on DRL explanation methods, then identifies a subset of features using the proposed feature-level interpretor. The agent policy is re-trained after trigger identification. Empirical evaluation verifies the efficacy of SHINE in shielding backdoored agents against different backdoor attacks.

### Strengths
\+ This paper tackles a challenging and important topic of shielding DRL agents.

\+ Wide applicability: the proposed approach can defense against both perturbation-based attacks and the adversarial agent attacks, for either single-agent or multi-agent RL.  

\+ The idea of pinpointing crucial states -> identifying triggered features -> retraining policy is well motivated and technically sound.

\+ Experimental design is comprehensive regarding trigger identification, shielding effectiveness, and performance impacts on clean environments. Sensitivity analysis is well designed.

### Weaknesses
 - This method hinges on the access to corrupted trajectories and environments for identifying the trigger. Sensitivity analysis is necessary to investigate whether the number or distribution of of those trajectories affect the efficacy of the proposed method. Specifically, the paper should explore how the ratio of successful to failed trajectories impacts the trigger identification and subsequent shielding performance. It is also unclear how the method would perform if the trigger is not consistently present in all failed trajectories, or if the trigger is stochastic in nature.

- Related work: The related work section could use some more efforts in elaborating how adversarial based attack works, as well as more prior work on the DRL explanation. The paper needs to clarify the specific mechanisms of different adversarial attacks, such as those based on policy manipulation or reward poisoning, and how they differ from the backdoor attacks considered. Furthermore, the discussion of DRL explanation methods should include a more detailed overview of the techniques used, such as saliency maps or attention mechanisms, and how they are adapted for the specific needs of backdoor detection in DRL.

- Need more elaboration on how step and feature-level explanation would be applied if attack is adversarial based, and how multi-agent RL can benefit from this approach. It is not clear how the feature-level interpretor would be applied to adversarial attacks that manipulate the environment or reward function, rather than directly injecting triggers into the state space. The paper should also provide a more detailed explanation of how the proposed method handles the complexities of multi-agent scenarios, such as the need to identify and shield multiple agents simultaneously, and how the method scales with the number of agents.

- Need more explanation on the two constraints in Eq (4), which is the key of the re-training process. In general the writing of the Sec 3.3 is too abstract to derive to the final objective. The paper should provide a more intuitive explanation of the constraints, and how they relate to the objective of removing the backdoor while maintaining performance in clean environments. The connection between the theoretical formulation and the practical implementation is not clear, and the paper should provide a more detailed explanation of how the constraints are implemented in the PPO algorithm.

### Questions
-  Does the number of pre-trained trajectories matter to the shielding capability?
- How this method applies to Multi-agent DRL scenarios? 
- It is not clear to me why $M_\pi(\hat{\pi}) \geq M_\pi(\pi)=\hat{\eta}(\pi)$.

### Soundness
3 good

### Presentation
2 fair

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
This paper addresses the vulnerability of deep reinforcement learning (DRL) policies to backdoor attacks. It introduces SHINE, a method that combines policy explanation techniques and policy retraining to mitigate these attacks effectively. The proposed method is theoretically proven to enhance the performance of backdoored agents in poisoned environments while maintaining performance in clean environments. Experiments demonstrate its superiority over existing defenses in countering DRL backdoor attacks.

### Strengths
- This paper studies the problem of backdoor threats in reinforcement learning. The authors leveraged several techniques to identify the backdoor triggers and designs a policy retraining algorithm to eliminate the impact of the triggers on backdoored agents.
- Theoretical guarantees in terms of the performance are provided.
- Empirical evaluations are promising.

### Weaknesses
 - It would be helpful to test the proposed methods against a broader set of backdoor attacks.
- Could you also compare your method with other types of defenses, e.g. non-trigger-inversion?

### Questions
-

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this In this paper, the authors study the problem of defense against backdoor attack in deep reinforcement learning. They present a practical algorithm called SHINE that first identifies backdoored features in attacked states and then sanitizes them in the hope of rendering the backdoor behavior ineffective on the agent. They claim that their methods theoretically improves the backdoored agent’s performance under attack while still retaining its performance in clean environment. They also test their method on three benchmark deep RL environments and show its effectiveness in eliminating backdoor attacks.

### Strengths
1. This paper studies an important problem of safeguarding against adversarial attacks in deep RL.
2. Their algorithm is well motivated and the authors claim it to work against tested benchmark environment.

### Weaknesses
1. No formal definition of attack and defense is provided. It is not even clear when does attacker attack, does it use any attack policy? The notations used in section 3.3 is not sufficiently clear.
    
2. In adversarial agent attack, how are actions embedded in state as you claim in the beginning of page 5? Actions usually come from a different space of discrete state than states.
    
3. This is perhas a good empirical paper, but it is not sound theoretically. I would formulate the problem properly and tune down the emphasis to adversarial agent attack part and theoretical claims to make a good case for it. It is necessary to define the assumptions under which the theoretical claims are guaranteed to work.

4. I believe for sanitization using masking approach to work, it needs certain assumption on kind of triggers that adversary can be put in environment and it is not clear from the paper why your approach would work in a general case. See question 4 for an example.

### Questions
1. Learning a feature explanation mask for each pixel in a state does not look very scalable especially in environments like Atari games where state space could get really large. How do you address this problem?
    
2. What is local linear constraint in line above Feature-level explaination paragraph? How does it help?
    
3. Without any assumption, it may happen that the adversary may not attack when the algorithm is run. Does the algorithm still work?
    
4. As a case study, let say the adversary designs a patch trigger to be put on top right corner of the state image(say in ping pong game). Normally, the pixel value is uniformly 100 and the adversary has trained the policy so that when pixel value is 255 or 0, it takes backdoor action. While attacking the adversary only inject 255 pixel patch. Your method of simply deleting the feature would lead to a zero patch which is adversarial as well. How would you fix this?

### Soundness
2 fair

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
The paper proposes an explanation-based approach to defend against backdoor attacks in deep reinforcement learning. The main observation is that a backdoor attack aims to cause an RL agent to fail a game or get a very low total reward, which can be explained using the triggers present in the environment. To this end, the paper applies the self-explainable framework of Guo et al., 2021b, called EDGE, to identify a set of time steps where triggers are most likely to present and then extract a set of features from the state vector of these time steps and treat their average as triggers. The paper applies their approach to detect both perturbation-based backdoor attacks in single and multi-agent settings, where triggers are injected into states, and adversarial agent attacks, where a sequence of actions serves as triggers. It further proposes a backdoor shielding method to retrain the agent in the operating environment. The approach is evaluated using Atari games and the SMC environment for perturbation-based attacks and the MuJoCo environments for adversarial agent attacks.

### Strengths
Although various explanation-based defenses have been proposed for protecting deep learning, applying policy explanation techniques to protect RL agents from backdoor attacks seems new and promising. The approach does not require access to a clean environment or a set of clean trajectories. 

The proposed approach applies to both perturbation-based attacks and adversarial agent attacks, outperforms several baselines in the former case, and obtains reasonable performance in the latter under some simple backdoor attacks against RL.

### Weaknesses
The paper is a direct application of the self-explainable framework for RL in Guo et al., 2021b, where the framework has already been applied to identify critical time steps associated with adversarial agent attacks. The technical contribution seems limited. 

The proposed method relies on reward signals in the actual environment in its explanation component, which requires many failure trajectories to identify triggers. Hence, it is not applicable in security-critical domains.

I am not convinced that the approach can work in more challenging settings. To identify critical time steps associated with triggers using the EDGE framework, two assumptions are needed. First, there is a set of failure trajectories available. Second, the agent is supposed to win the game if the triggers are removed. However, a successful attack does not necessarily lead to a clear failure, especially in the case of stealthy attacks, where the goal could be reducing the agent's reward. Without domain knowledge of the expected performance of the agent in the target environment, it is hard to define what is considered a failure. Further, the evaluation considers a backdoor attack with a single fixed trigger placed at a fixed location, which is rather limited.

### Questions
How is (4) solved? Algorithm 1 only shows how to estimate the constraint but not how the shielding policy is optimized. 

How are the set of trajectories used to train SHINE generated in the experiments? Are these all known to be failures? 

The trigger detection stage of SHINE takes 12 hours, with an additional 5 hours used to retrain the policy. Is this comparable with other baselines? Since the approach requires many interactions with an infected environment, the agent will suffer from a significant loss until the trigger is mitigated. Hence, it seems unfair to only consider the reward after retraining when comparing the approach with other baselines. 

Guo et al., 2021b show that significant improvement can already be achieved by partially blinding the victim agent's observation at the critical time steps in losing episodes. Thus, it would help to have an ablation study demonstrating the advantage of feature-level explanation and policy retraining.  

In the experiment, it is assumed that there is a trigger in the environment with a probability of 0.1, 0.2, or 0.3. I wonder what would happen if triggers were present most of the time.  

The evaluation uses a single fixed trigger pattern across RL training and testing. I wonder what would happen if the attacker varies the trigger used over rounds/episodes. 

Table 2 shows that SHINE performs better than the original PPO in a clean environment. Why is this the case?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
