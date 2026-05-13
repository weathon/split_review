# A SIMILARITY-AGNOSTIC REINFORCEMENT LEARNING APPROACH FOR LEAD OPTIMIZATION

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Lead optimization in drug discovery is a pivotal phase in identifying promising drug candidates for further development. Traditionally, lead optimization in the machine learning community has been treated as a constraint optimization problem where methods like generative models and reinforcement learning(RL) have been widely employed. However, these methods often rely on molecular similarity metrics to define constraints, which poses significant challenges due to the inherently ambiguous nature of molecular similarity. In this work, we present a similarity-agnostic approach to lead optimization, which we term "Lead Optimization using Goal-conditioned Reinforcement Learning" or LOGRL. Contrary to conventional methods, LOGRL is uniquely trained on a distinct task: source-to-target path prediction. This allows LOGRL to produce molecules with significantly higher Tanimoto similarity to target molecules, even without direct exposure to this metric during training. Furthermore, we incorporate a beam search strategy during the molecule generation process. This strategy empowers us to generate a substantial number of candidate molecules, facilitating further curation to meet desired properties. Notably, our unique approach permits us to leverage the Euclidean distance between learned action representations as a surrogate for molecular similarity during beam search.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this study, a new lead optimization method, LOGRL, is proposed. This method uses offline reinforcement learning to train the model how to optimize molecular structures to get closer to the target structures (goal-conditioned reinforcement learning). Furthermore, a set of reactions is used to ensure the synthetic accessibility of the generated structures. The beam search algorithm is used, which helps in obtaining a diverse set of modified structures that meet desired properties. LOGRL is compared against two RL baselines and achieves promising results in optimizing molecules towards the target structures, both in terms of similarity and drug-likeness defined by QED.

### Strengths
- The method is presented in a very clear way. The background section provides all the basics that are required to understand the method.
- Offline reinforcement learning is used to avoid sparse rewards when navigating the vast chemical space.
- The goal-conditioned reinforcement learning is used to guide the generative process, which in my opinion is the main novelty of the paper. This way, similarity measures are no longer needed to train the model.
- Reaction rules extracted from the USPTO-MIT dataset are used to ensure the synthesizability of the generated molecules, which is important for proposing high-quality results.

### Weaknesses
 - The significance of the work is not clear. The method is trained to optimize molecules towards the target structures, but I am unsure if I understand how this model could be used in practice. Usually, the goal of lead optimization is to improve a set of molecular properties without impacting binding affinity. In the presented setup, the optimization changes the structure of lead candidates to make them more similar to known drugs, which oftentimes is undesired because only novel structures can remain outside the patented chemical space.
- The experimental section seems very preliminary. Only two RL baselines were trained, and there is no comparison with other state-of-the-art methods in molecular optimization. The evaluation metrics used in the experiments are very simple and do not show if the proposed method can optimize any molecular properties or at least retain high binding affinity. The Authors claim that their search strategy separates property optimization from training, but the results of the optimization are not presented. Additionally, all methods were run only once (if I understand correctly), and the results can be hugely impacted by random initialization, especially for online RL methods like the baselines. I would strongly suggest running these methods multiple times and providing confidence intervals for the evaluation metrics.
- (minor) I think the Authors could consider comparing their approach to the simpler, yet conceptually similar, Molpher model [1]. In Molpher, a trajectory between two molecules is found by an extensive search (not RL-based) of possible reaction-based structure mutations. The motivation of that paper is also different, Molpher was proposed for effective chemical space exploration.

### Questions
1. What is the success rate of molecular optimization using LOGRL? Can you find many well-optimized molecules in the post-training filtering step, or do you think additional RL objectives could improve these properties significantly?
2. What are the real-life applications of this optimization algorithm? Can it be used for other optimization problems besides lead optimization (see the problems I mentioned in the "Weaknesses" section)?
3. In Section 3.2, two GCRL methods are described. Did you try the other method and if so, could you provide the comparison results?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents LOGRL, a unique approach to lead optimization using a goal-conditioned reinforcement learning framework. Given an expert dataset, this work trains a goal-conditioned policy with binary reward shaping, treating reaction rules as actions. Then, LOGRL compares Tanimoto similarity and QED of generated molecules with two baselines using an online RL method, which is PPO.

### Strengths
- The paper is well-written and presents clearly.
- The paper demonstrates comprehensive related work.

### Weaknesses
The experimental comparison in this paper raises some concerns regarding fairness and appropriateness. The authors compare their proposed off-line Reinforcement Learning (RL) policy with on-line RL baselines. This comparison between on-line and off-line RL algorithms seems somewhat unconventional. Moreover, it's unclear whether the on-line RL baselines, such as the S model and Q+S model, employ an expert dataset similar to LOGRL. If they do not utilize expert data, this could introduce an unfair advantage to LOGRL, as it relies on additional expert data. It would be beneficial to see how LOGRL performs when compared to baselines that also use the same expert dataset.

Additionally, I suggest exploring the possibility of supervised learning in this context. The authors assume access to a substantial amount of expert dataset containing high-reward samples. In such a scenario, imitation learning often outperforms offline RL. It would be valuable to understand why the authors chose offline RL over supervised learning, given the abundance of expert data.

The paper employs policy gradient, which typically assumes that the training policy and the behavior policy are aligned, making it an on-policy approach. The suitability of using a policy gradient in an offline RL setup is a point of concern. It would be helpful to see more discussion and justification regarding the use of an on-policy algorithm like policy gradient in this context.

Finally, it would be interesting to know if the proposed method is capable of generating diverse outputs. One potential concern is whether the method might collapse and generate a single output, as there doesn't appear to be a regularizer that can control all possible outputs directed toward the target molecule. Exploring the diversity of outputs and addressing this potential issue would strengthen the paper.
Overall, while the paper presents a promising approach, addressing these concerns and providing more clarity would enhance the quality of the work and its relevance in the field of machine learning and RL.

---

minor

Typo in Section 4.5 line3: in the training batch, batchwe

### Questions
See Weakness section

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tries to tackle a challenging problem in drug discovery, where it is common to optimize a lead compound to remove deficiencies and maintaining the favorable properties. 
They highlight the challenges of using reinforcement learning based on similarity metrics to define certain constrains on the optimized compound, which potentially can introduce a bias in the generative process. 
Therefore, the authors propose a so call similarity agonistic reinforcement learning approach and remove the dependency on the similarity metric as additional constrain for optimization. This is achieved by goal-conditioned reinforcement learning.

### Strengths
In my opinion the paper has the following strengths:

-	To the best of my knowledge the idea of using complete molecules as goal (for goal conditioned reinforcement learning), as the authors propose it, is novel.
-	In general, the method section is well explained with minor exceptions.
-	Using reaction rules partially circumvents a general problem in generative models for drug discovery, namely a significant part of generated molecules are difficult to synthesize in the lab hindering a fast-pace early stage drug discovery program. The use of reaction rules conditions the generative model to generate more chemically plausible molecules with a direct synthesize path. 
-	The method seems to improve upon their baseline on all experiments.

### Weaknesses
Lead optimization in drug discovery is an important and difficult task. I have difficulty accepting the method as an invention or improvement for lead optimization. For my understanding lead optimization is a much more complicated process than purely looking on QED score or a similarity score, which the authors didn’t investigated.

In general, the paper would gain strength if the authors would compare their method against more recent methods in generative design and more properties other than QED. Especially, the baseline seems to be quite weak with all the efforts recently put into improving generative methods. 
For example, the author could have a look at a standardized benchmark, e.g. [1]. 
This would strength their method and would help to better showcase the potential
improvement compared to other methods. 
The authors might also consider comparing their methods against other methods in the domain of scaffold hopping, e.g. [3].

The second contribution of their paper as stated on page 2, says:
“we propose a search strategy…”
Could the authors elaborate more on the search strategy? In case it is just generating thousands of molecules and sorting them based on a score, this seems to me not like a novel strategy.

I very much like the idea of using reaction rules, although not completely novel, e.g. [2]. I think a more detailed description how exactly they mine the reaction rules and a better description of the reaction dataset in general would help the reader to better understand the topic. It doesn’t have to be in the main text. 

I had trouble understanding the last paragraph of section 4.6., “we found that under the condition G(a_t leads to g)…”. Could the authors elaborate a little bit more on the issue they observed?

To summarize, although certain ideas are interesting and in some sense novel, I am hesitant to accept the paper mainly because of in my opinion a weak experiment section. The paper doesn’t showcase a technique for lead optimization, which is much more complicated than what is investigated in the paper. Also, claims like: 
“Though we do not explore comparison with multi-property optimization works in the scope of this work, the results shown induce confidence in our model to be able to generate lead candidates that satisfy multiple properties.” Sec. 6, 
seem to be too strong for the experiments considered.

### Questions
-	Did I understand it correctly that the offline dataset just contains molecules randomly put together using the reaction rules, so potentially not chemically plausible at all? 
-	My understanding of actor-critic reinforcement learning is to use the output of the critic for the loss of the actor. From eq. (1) and (2) this seems not the be the case, could the authors elaborate a little bit?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
