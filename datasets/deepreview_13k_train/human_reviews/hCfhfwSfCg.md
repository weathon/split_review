# Generate explorative goals with large language model guidance

- Decision: Reject
- Scores: 1, 1, 3, 3

## Abstract
Reinforcement learning (RL) struggles with sparse reward environments.
Recent developments in intrinsic motivation have revealed the potential of language models to guide agents in exploring the environment.
However, the mismatch between the granularity of environment transitions and natural language descriptions hinders effective exploration for current methods.
To address this problem, we introduce a model-based RL method named Language-Guided Explorative Goal Generation (LanGoal), which combines large language model (LLM) guidance with intrinsic exploration reward by learning to propose meaningful goals.
LanGoal learns a hierarchical policy together with a world model. The high-level policy learns to propose  goals based on LLM guidance to explore the environment, and the low-level policy learns to achieve the goals.
Extensive results on Crafter demonstrate the effectiveness of LanGoal compared to recent methods.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces a model-based RL method named Language-Guided Explorative Goal Generation (LanGoal) that combines large language model (LLM) guidance with intrinsic exploration reward to propose meaningful goals for exploration in sparse reward environments. LanGoal consists of a hierarchical policy that generates goals based on LLM guidance and a world model that learns the dynamics of the environment. The paper provides extensive experimental results on the Crafter environment to demonstrate the effectiveness of LanGoal compared to other methods.

**This paper shows significant similarities to the arXiv article "World Models with Hints of Large Language Models for Goal Achievement" (DLLM), available at https://arxiv.org/abs/2406.07381, raising concerns about potential plagiarism.**

### Strengths
none

### Weaknesses
 **This paper shows significant similarities to the arXiv article "World Models with Hints of Large Language Models for Goal Achievement" (DLLM), available at https://arxiv.org/abs/2406.07381, raising concerns about potential plagiarism.**
- The equations in Section 4.2 of "LanGoal" are identical or nearly identical to those in Section 4.3 of the DLLM paper, including specific terms like "catxent" and "binxent."
- The "reward design" section of "LanGoal" only differs from DLLM by a slight change in the threshold hyperparameter from 0.5 to 0.6.
- Appendix D of "LanGoal" merely replicates part of Section 4.3 from DLLM without any additional information or changes.
- The description of a high-level policy generating a hidden state and a low-level policy producing actions in "LanGoal" closely mirrors the encoder concept in DreamerV3, the backbone of DLLM, with minimal differences.
- In Section 4.4, "LanGoal" mentions implementing a classifier-free guidance (CFG) policy but fails to provide specific details about the implementation or relevant hyperparameters.
- The results for baseline experiments in "LanGoal" match those in DLLM without proper citation.

### Questions
none

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes LanGoal.

### Strengths
None

### Weaknesses
This article bears a strong resemblance to an article on arXiv: "World Models with Hints of Large Language Models for Goal Achievement" (DLLM), https://arxiv.org/abs/2406.07381. I suspect there is plagiarism involved.

The most evident similarity lies in the methodology and the corresponding equations. In Section 4.2 of "LanGoal," all the equations are identical or nearly identical to those in Section 4.3 of DLLM, including specific abbreviations such as "catxent" (categorical cross-entropy loss) and "binxent" (binary cross-entropy loss), which are not conventional in machine learning. In the "reward design" section of 4.3 in "LanGoal," the only apparent modification from Section 4.2 of DLLM is changing the threshold hyperparameter M from 0.5 to 0.6.

"LanGoal" claims to provide further details about the high-level and low-level critics in Appendix D, but the appendix only replicates the latter part of Section 4.3 from DLLM paper, without any changes or additional information. In Section 4.3 and Figure 1, "LanGoal" introduces a high-level policy that generates a hidden state and a low-level policy that produces the actual action. However, this is essentially the same as the encoder in the world model of DreamerV3, the backbone algorithm of DLLM, with the only difference being that "LanGoal" treats the hidden state as an action, while it is viewed as a latent variable that captures information from both the history and current state.

In Section 4.4 of "LanGoal," the authors cite two papers on diffusion models to introduce the concept of guidance, claiming to have implemented a related classifier-free guidance (CFG) policy. However, they do not provide any details about the method or its implementation, such as the models used or relevant hyperparameters. Since their approach essentially replicates DLLM,  this method does not require diffusion models, as RSSM and diffusion are fundamentally different frameworks. This seems like an awkward attempt to artificially broaden the scope of their work.

Moreover, the structure of "LanGoal" bears a strong resemblance to DLLM paper, including a similar depiction of the algorithm (Figure 1), a nearly identical format for presenting prompt details in the appendix, and comparable content and formatting in the experimental section, particularly in Table 1 (Section 5.2).

Besides, all baselines experiment results are the same as DLLM paper without citing that paper.

### Questions
None

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces LanGoal, a model-based reinforcement learning (RL) framework that combines large language model (LLM) guidance with intrinsic exploration rewards to address the challenge of sparse rewards in reinforcement learning environments. LanGoal's hierarchical policy structure allows the high-level policy, informed by LLM guidance, to generate meaningful exploration goals, while the low-level policy aims to achieve these goals. The paper presents extensive experimental results on the Crafter environment, showing that LanGoal outperforms other methods in goal-reaching and exploratory efficiency, indicating its potential to enhance RL agents' performance in complex, sparse-reward tasks.

### Strengths
It is an interesting paper which combines large language model (LLM) guidance with model-based reinforcement learning (RL) to tackle sparse-reward environments. The strengths of this paper include:
   - This approach provides a novel perspective by using LLMs to guide exploration goals, addressing sparse reward in RL.
   - LanGoal’s hierarchical policy structure allows for LLM-guided high-level goal generation and low-level goal achievement, offering a well-structured and adaptable approach that brings interpretability to RL through language-based goals.
- The hierarchical approach, where the high-level policy sets goals based on LLM guidance and the low-level policy works to achieve them, is well-articulated and theoretically sound. The paper’s clear structure and mathematical formulations make it easy to follow and reproduce.
   - The authors provide thorough experiments in the Crafter environment, comparing LanGoal with state-of-the-art methods in terms of success rate and goal achievement along with ablation studies.
   - By focusing on sparse-reward settings, LanGoal has implications for applications requiring efficient exploration in large state spaces, such as robotics, autonomous navigation, and open-world gaming. The use of language guidance could provide intuitive and adaptable control strategies for these domains.

### Weaknesses
While the paper introduces a promising framework with LanGoal, there are still some major weaknesses which need to be resolved:

-  **Limited Novelty:** One major weaknesses is the paper lacks of novelty. While the paper provides a well-executed framework, its novelty may be limited due to reliance on existing concepts within reinforcement learning and large language model (LLM) integration. Specifically:
   - The hierarchical structure that combines high-level goal-setting with low-level goal-reaching policies is a common technique in reinforcement learning, and several works have explored using language guidance for RL exploration. LanGoal’s approach, while effective, primarily extends these existing ideas without introducing fundamentally new mechanisms or problem formulations.
   - The combination of model-based RL with LLM-guided exploration goals appears to be an incremental improvement, building upon previously proposed methods rather than proposing a substantially different or unique approach.

- **Limited Environment Generalizability:** The experiments are conducted solely on the Crafter environment, which, while relevant, may not fully represent the diversity and complexity of sparse-reward or open-world environments. The reliance on a single environment limits the ability to generalize the findings and assess the robustness of LanGoal. This is one of the major weaknesses of this paper. Including additional environments, such as navigation-based tasks or open-world settings (e.g., Minecraft or other 3D environments), could provide stronger evidence for LanGoal’s adaptability and effectiveness.

- **Dependency on Predefined Language Goals:** The method depends heavily on predefined language-based goals generated by an LLM, which may not fully align with the agent’s state or context in more dynamic environments. If the LLM fails to propose contextually appropriate goals, it could reduce the model's efficiency and reliability. Incorporating a feedback mechanism where the agent’s exploration results influence subsequent goal generation could make the approach more adaptive. Alternatively, investigating the LLM’s goal adaptability across different environments could clarify its limitations.

- **Writing and Layout Issues:** The paper’s readability is compromised by several writing and layout issues, affecting its clarity and overall presentation. Frequent instances of excessive blank spaces between figures and equations disrupt the reading flow, making the document appear less polished and professional. 

- **Clarity on Hierarchical Policy Learning:** The hierarchical policy’s training process, particularly the interaction between high-level and low-level policies, could be clarified further. It is not fully clear how the policies handle conflicting objectives between goal exploration and goal-reaching under varying reward structures. Providing a more detailed breakdown of the policy training dynamics, possibly with ablation studies on the hierarchical structure itself, could enhance understanding and reproducibility.


- **Limited Discussion on Failures or Negative Results:** The paper predominantly presents positive findings but lacks an in-depth analysis of failure cases or scenarios where LanGoal may struggle, such as instances where LLM guidance contradicts optimal exploration paths. Adding a section on observed limitations or failure modes, and discussing potential mitigations, would improve transparency and provide a balanced perspective on the framework’s performance.

- **Scalability Concerns with LLM Use:** The use of an LLM for continual goal guidance raises potential scalability and efficiency concerns, particularly in larger or real-time environments where frequent LLM queries could lead to computational bottlenecks. Exploring lightweight alternatives, such as using distilled or smaller models that capture core semantic information, or reducing the query frequency with effective goal-persistence strategies, may mitigate scalability issues.

**Summary of Weaknesses**

While the paper introduces a promising framework with LanGoal, it faces significant challenges that limit its readiness for publication. The most critical issue is limited novelty; the approach largely builds on established techniques in reinforcement learning (RL) and large language model (LLM) guidance without offering new problem definitions or mechanisms. Additionally, limited environment generalizability is a concern, as the experiments are conducted solely on the Crafter environment, restricting the evidence for LanGoal's broader applicability. Along with other weaknesses, it collectively suggests that the paper requires substantial revisions. It is not ready for publication.

### Questions
See above sections.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a new combination of goal-directed exploration supported by LLMs and Dreamer-like model-based deep RL. It shows impressive performance improvement in Crafter, a hard exploration RL task.

In its current state, the paper is poorly written and hard to parse. The text should be passed into a grammar checker, there are a lot of language errors throughout, which often makes comprehension difficult (some errors listed below but many more in the text). I suggest you use language tools and/or ask for the help of a native speaker colleague because I suspect improving the language would make the contribution a lot clearer. 

I also find the approach to not be clearly motivated and not clearly situated in the space of the closest existing methods (Dreamer, ELLM, OMNI), see comments below. The novelty of the contribution could be made more explicit, because in the current state the approach seems to be a rather simple combination of Dreamer and goal-directed exploration with LLMs like Omni or ELLM. 

The methods could also be more clearly explained with better descriptions of each of the variables involved in the many equations and losses presented here. Each should also be intuitively motivated. I'm not sure what the goal encoder is doing, how the high-level policy is trained here and how the LLM suggested goals are incorporated into the architecture.

I strongly encourage the authors to make considerable efforts in improving on the points listed above over the rebuttal period. I am inclined to augment my rating based on improvements on writing, motivations / positioning and methods descriptions.

### Strengths
The results seem impressive, Crafter is a hard task.

### Weaknesses
My questions and comments are listed below, but generally:
* the paper is poorly written with many grammatical errors which make comprehension hard
* methods not always clearly described, in particular about the high-level policy, the goal encoder and how the LLM-generated goals influence the architecture
* unsupported claim that the test-time technique help performance -- they do not seem to help
* only tested in one environment. If this paper is an extension of Dreamer then it would be good to test on a similar range of environments

Related work:
* it's not so clear in the text why HRL or world models would help exploration, could this be explained in more details?
* Goal-based exploration is a whole field, not limited to its use in hierarchical RL. It's also a kind of intrinsic motivation (called competence-based in Oudeyer and Kaplan's framework (https://pubmed.ncbi.nlm.nih.gov/18958277/)), see a recent review of these approaches in https://arxiv.org/pdf/2012.09830
* In addition to ELLM there is another work using LLMs to generate exploration goals for RL in Crafter: OMNI (https://arxiv.org/pdf/2306.01711).  As far as I understand, the contribution of this paper is to combine this approach with a Dreamer-like model-based RL.
* It would be good to have a paragraph clearly listing similarities and differences between the proposed approach and the closest existing ones like Dreamer, Omni and ELLM. What are the real contributions and novelty here?
* Intrinsic motivation literature:
  * the list in the second paragraph is very sparse, all these methods are "intrinsic motivation," "curiosity-driven" could also apply to all methods cited here, and I think should be defined as "intrinsic motivation driving to explore" in opposition with intrinsic motivations driving to homeostasis (eg minimizing surprise).
  * Not all intrinsic reward methods are susceptible to the noisy TV issue.

Motivations:
* I'm not sure I understand the 4th paragraph of the intro. What is meant by "Existing works learn model-free policy with guidance from LLM, but lack of understanding of the semantic meaning" or "make a balance between reaching the LLM goals and exploration during the online training, which leads to the inefficiency of the method"?
* what is a "semantic guidance"? By the end of the intro, this term has still not been defined. Maybe an example could help the reader understand what is meant by this term?
* The second contribution also sounds vague, I'm not sure I understand what it refers to.
* Overall I think the text doesn't motivate the approach very well because it does not clearly link the contributions of this paper (not very clear in the intro) to the challenges posed by hard exploration problems and doesn't explain how the proposed approach aims to tackle them. This discussion should be made in light of existing approaches using LLMs for exploration like OMNI (see above) and ELLM. The first is not discussed at all while the second is only mentioned in the baseline but does not appear neither in the related work nor in the introduction.

Methods:
* h_t is not defined anywhere and does not appear in the graph, I assume it's the memory state from the RSSM?
* o_t appears as x_t in the Figure
* One of the appeals of model-based RL is that it's goal agnostic and thus can be reused for new goals. But here it seems like the world model is made goal-dependent by adding the auxiliary loss of predicting the agent's goal v_t from the internal states? Could you say more about why it's important to do that?
* the multi-modal decoder seems to be split in two networks with different inputs but that have the same weights theta, what is going on here? * Maybe these are different networks with different weights?
* Algorithm 1: to define a new variable it's either x ~ distrib(x | y) or x = f(y), but here the authors use a combination of the two that seems odd: eg, v_t = txt_enc(v_t | LLM(g_t |o_l)), here txt_enc is just a function and the LLM can be sampled so maybe g_t ~LLM(g_t | o_l)  and then v_t = txt_end(g_t)?
* I'm not sure I understand what's going on with the Classifier-free guidance, but I also think it should be removed from the paper since it doesn't bring any significant performance improvement here.


Results
* Contrary to what is claimed in section 5.2, the addition of the test-time technique doesn't seem to add any significant boost (biggest difference is .7 with an std of 3.6). If the method doesn't help, what is a good reason to keep it in the paper? Should it be moved to the appendix?

Goal encoder:
* I do not understand what is being implemented here.
* "we use an autoencoder to transform the goal state into a discrete action space with lower dimension." → up to now the goal was a semantic embedding, and I don't understand why we would compress a goal into an action?
* the following sentence refers to the inner state representation of the RSSM (s_t), which is not the goal?
* The equation refers to z_t as the latent code, and s_t as the input, so I'm confused about what the "goal" is here.
* In the following equation 5, now z_t is replaced by u_t?
* I'm not sure what is going on here and this seems to be a key point in the algorithm.

### Questions
Related work:
* it's not so clear in the text why HRL or world models would help exploration, could this be explained in more details? 
* Goal-based exploration is a whole field, not limited to its use in hierarchical RL. It's also a kind of intrinsic motivation (called competence-based in Oudeyer and Kaplan's framework (https://pubmed.ncbi.nlm.nih.gov/18958277/)), see a recent review of these approaches in https://arxiv.org/pdf/2012.09830
* In addition to ELLM there is another work using LLMs to generate exploration goals for RL in Crafter: OMNI (https://arxiv.org/pdf/2306.01711).  As far as I understand, the contribution of this paper is to combine this approach with a Dreamer-like model-based RL. 
* It would be good to have a paragraph clearly listing similarities and differences between the proposed approach and the closest existing ones like Dreamer, Omni and ELLM. What are the real contributions and novelty here?
* Intrinsic motivation literature:
  * the list in the second paragraph is very sparse, all these methods are "intrinsic motivation," "curiosity-driven" could also apply to all methods cited here, and I think should be defined as "intrinsic motivation driving to explore" in opposition with intrinsic motivations driving to homeostasis (eg minimizing surprise).
  * Not all intrinsic reward methods are susceptible to the noisy TV issue.

Motivations:
* I'm not sure I understand the 4th paragraph of the intro. What is meant by "Existing works learn model-free policy with guidance from LLM, but lack of understanding of the semantic meaning" or "make a balance between reaching the LLM goals and exploration during the online training, which leads to the inefficiency of the method"?
* what is a "semantic guidance"? By the end of the intro, this term has still not been defined. Maybe an example could help the reader understand what is meant by this term?
* The second contribution also sounds vague, I'm not sure I understand what it refers to.
* Overall I think the text doesn't motivate the approach very well because it does not clearly link the contributions of this paper (not very clear in the intro) to the challenges posed by hard exploration problems and doesn't explain how the proposed approach aims to tackle them. This discussion should be made in light of existing approaches using LLMs for exploration like OMNI (see above) and ELLM. The first is not discussed at all while the second is only mentioned in the baseline but does not appear neither in the related work nor in the introduction. 

Methods:
* h_t is not defined anywhere and does not appear in the graph, I assume it's the memory state from the RSSM?
* o_t appears as x_t in the Figure
* One of the appeals of model-based RL is that it's goal agnostic and thus can be reused for new goals. But here it seems like the world model is made goal-dependent by adding the auxiliary loss of predicting the agent's goal v_t from the internal states? Could you say more about why it's important to do that?
the multi-modal decoder seems to be split in two networks with different inputs but that have the same weights theta, what is going on here? * Maybe these are different networks with different weights?
* Algorithm 1: to define a new variable it's either x ~ distrib(x | y) or x = f(y), but here the authors use a combination of the two that seems odd: eg, v_t = txt_enc(v_t | LLM(g_t |o_l)), here txt_enc is just a function and the LLM can be sampled so maybe g_t ~LLM(g_t | o_l)  and then v_t = txt_end(g_t)?
* I'm not sure I understand what's going on with the Classifier-free guidance, but I also think it should be removed from the paper since it doesn't bring any significant performance improvement here. 


Results
* Contrary to what is claimed in section 5.2, the addition of the test-time technique doesn't seem to add any significant boost (biggest difference is .7 with an std of 3.6). If the method doesn't help, what is a good reason to keep it in the paper? Should it be moved to the appendix? 

Goal encoder: 
* I do not understand what is being implemented here. 
* "we use an autoencoder to transform the goal state into a discrete action space with lower dimension." → up to now the goal was a semantic embedding, and I don't understand why we would compress a goal into an action?
* the following sentence refers to the inner state representation of the RSSM (s_t), which is not the goal?
* The equation refers to z_t as the latent code, and s_t as the input, so I'm confused about what the "goal" is here.
* In the following equation 5, now z_t is replaced by u_t?
* I'm not sure what is going on here and this seems to be a key point in the algorithm.

### Soundness
2

### Presentation
1

### Contribution
3
