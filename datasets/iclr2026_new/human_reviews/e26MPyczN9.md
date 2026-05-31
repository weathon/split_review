## Human Reviewer 1

### Summary
This paper presents a re-revaluation of the popular claim that "programmatic policies generalize better than neural network policies". The core thesis is that the previously observed generalization gap stems not from fundamental differences in representation, but largely from experimental confounds.

In this paper, authors revisit three benchmarks (TORC, Karel, Parking). They demonstrate that by applying "minor modifications" to the neural policy learning setup, their out-of-distribution (OOD) generalization can match or even exceed that of programmtic policies.

The paper concludes by using a custom Karel task (learning a stack/queue) to highlight the real benefit of programmatic policies. It argues this advantage is not broad generalization, but the specific, superior ability to execute explicit algorithmic logic.

### Strengths
1. Directly challenging a widely acknoweledged conclusion and attributing it to "experimental confounds" is a valuable contribution to the community. Researchers are always encouraged to examine and revisit.
2. The effort to re-evaluate three core benchmarks is convincing w.r.t. corresponding algorithms. Concrete experimental evidence (e.g., sparse observations in Karel) to support its central argument: generalization gap stems not from fundamental differences in representation, but largely from experimental confounds. 
3. I am also a bit surprised that slightly tweaking the experimental settings can achive better performance and generalization ability for neural policies. This may be a good lesson for RL researchers that a better formulation of the policy network (even a simple modification) could help the entire experiment.

### Weaknesses
1. I understand the ambition of this paper but the title seems too "huge". First of all, the claim of programmatic policies generalize better should be explained throughly and more work should be discussed and cited. Programmatic policies are utilized in many other works [1, 2, 3, 4, 5] involving different benchmarks and learning methods. A comprehensive re-evaluation is not realistic and expected, yet discussions are appreciated.
2. I am not fully convinced by the "minor modifications" as tweaking reward function or observation setting are injecting inductive bias, this is not a trivial change to learning of an neural network policy. Also, DSL is a perfect method to inject inductive bias, have you considered tweaking DSL and conduct some experiments? 
3. From my understanding, programatic policies and neural policies are not contradict to each other and can be composed together, this is verified by previous works [1, 6]. Moreover, neural networks are specialized to have better perceptual generalization, yet programmatic policies are suitable for systematic generalization. I believe this aligns many of your research statement, it would be better to discuss this in your revised paper.

[1] Qiu and Zhu, Programmatic Reinforcement Learning without Oracles, ICLR 2022

[2] Cui et al., Reward-guided synthesis of intelligent agents with control structures, PLDI 2024

[3] Kohler et al, Interpretable and Editable Programmatic Tree Policies for Reinforcement Learning, EWRL 2024 Workshop

[4] Guo et al., Efficient Symbolic Policy Learning with Differentiable Symbolic Expression, NeurIPS 2023

[5] Qiu et al., Instructing Goal-Conditioned Reinforcement Learning Agents with Temporal Logic Objectives, NeurIPS 2023

[6] Qureshi et al, Composing Task-Agnostic Policies with Deep Reinforcement Learning, ICLR 2020

### Questions
1. See weaknesses 2
2. The modified synthetic Karel tasks seems too ad-hoc and artificial. Come you come up with other tasks or modifications to strengthen your claims?
2. How much effort did you made to find different tweaking of these neural policies? How easy for FunSearch to find a Python policy that generailzes better?
3. Can you discuss the combination of neural policies and programmatic policies? Can neurosymbolic methods solve the problems from both sides?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper re-evaluates the out-of-distribution (OOD) generalization properties of programmatic policies found by different search algorithms (e.g., NDPS, LEAPS, PSM). In previous literature, these policies were often reported to generalize better than neural policies trained with gradient-based methods (e.g., DDPG, PPO, DQN). This paper demonstrates that in several environments (TORCS, Karel, Parking) , straightforward modifications to the neural policy's training allow them to match or exceed the generalization of programmatic policies.

The paper argues that often both neural and programmatic representations can 
*in principle* encode a generalizing policy (a property the paper later calls "Expressivity"). The reported gap in prior work stemmed from "uncontrolled experimental factors" that made finding this solution _in practice_ (a property called "Discoverability") more difficult for the neural policy's search algorithm (i.e., gradient descent). The paper then argues that a true advantage for programmatic policies exists in environments where neural networks struggle to encode generalizing policies even _in principle_. This often involves tasks requiring algorithmic solutions, such as learning specific data structures like a stack or queue. One such environment ("SparseMaze") is shown as a proof-of-concept : a GRU policy trained with PPO fails to learn or generalize, whereas a programmatic policy found by FunSearch discovers a breadth-first search algorithm and provably generalizes.

### Strengths
- The paper provides a valuable corrective to some claims in the literature about the superior OOD generalization of programmatic policies over neural ones.
- The re-evaluation experiments in TORCS, Karel, and Parking appear sound and clearly demonstrate how the exact experimental setup impacts generalization .
- The distinction between a representation's _expressivity_ (containing a solution) and the _discoverability_ of that solution by a search algorithm can aid further discussion of generalization.

### Weaknesses
While the paper's re-evaluation of prior work is valuable, its main positive claim feels limited. The paper argues that the _true_ advantage of programmatic policies lies in their _expressivity_ for tasks requiring complex algorithmic structures (like memory or data structures), which common neural network architectures lack .

In my view, this is a well-understood distinction, and the "SparseMaze" proof-of-concept serves more to confirm this known limitation of standard recurrent networks than to provide a new, surprising insight. It would be similarly straightforward to design an environment where neural network policies generalize better (e.g., an environment based on classifying handwritten digits, where the task is perceptual and the underlying "program" is unknown).

The paper wants to guide future evaluation of OOD generalization in RL. However, the main take-away message seems to be "programmatic policies are better when the task requires an explicit algorithm," which is not a particularly novel conclusion. For this reason, the contribution feels limited, which is why I vote for a weak reject.

### Questions
Below I list more details in the form of questions and comments:
- Section 5 asks the question, "Can programmatic representations better generalize to OOD problems?". This question seems ill-posed, as I have argued above. Clearly, in some environments, programmatic representations generalize better, and in others, neural representations will. More reasonable questions might be: "What are the properties of environments that make programmatic representations more suitable than neural representations, and vice versa? For a given complex environment, how can we determine in advance which kind of representation will generalize better? What representations will generalize better in relevant real-world problems?" The paper _does_ suggest an answer to the first question—that the key property is the need for algorithmic structures like memory manipulation, stacks, or queues. However, it doesn't provide a general framework for identifying these properties in advance in complex, high-dimensional problems (like NetHack, which it mentions ), which would be a more significant contribution. Do the authors have further insights on this?
- In Section 2, the paper formally introduces Markov Decision Processes (MDPs) . However, for the KAREL environment, it explicitly investigates "the partially observable version" and even shows a classic state-aliasing diagram (Figure 4) where different states lead to the same observation. Shouldn't the Partially Observable MDP (POMDP) formalism also be introduced for completeness?
- The paper introduces the core concepts of its argument—that a representation must (i) include a generalizing policy and (ii) the search algorithm must be able to find it—in the abstract and introduction. However, it only formally names these concepts "Expressivity" and "Discoverability" in Section 5 . It would significantly improve the paper's clarity and impact to use these terms consistently from the introduction onwards.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper challenges the idea that neural policies necessarily generalize worse in out-of-distribution scenarios than programmatic policies. To do so, the authors rerun experiments from three existing papers that previously reported better generalization capabilities from programmatic policies and demonstrate that as good out-of-distribution generalization can be obtained by neural policies if one adds a sparsity metric, alters the reward function or changes the inputs given to the neural policies. Finally the paper concludes by modifying one of the (Maze navigation) tasks to make it more challenging  for neural policies and showing that a search algorithm leveraging an LLM can generate a program that solves any kind of such mazes and outperform neural policies trained with PPO.

### Strengths
The paper revisits existing experimental setups and refutes some of their claims or at the very least provides more complete explanations of why neural policies were not generalizing as well in prior experiments.

### Weaknesses
I am not sure I completely agree with the claim that previously reported advantages of programmatic policies are only due to experimental confounders. I am not sure any of the previous papers claimed that programmatic policies would always generalize better than neural one, only that they can provide a favorable inductive bias for certain tasks. That a similarly efficient inductive bias can be injected to neural policies by adding a sparsity regularization or by modifying the reward function does not necessarily contradicts the previous statement. It only shows that there are multiple ways of injecting prior information that would help generalization beyond the choice of the policy class. 

Along the same line, I find the experiment in Sec. 5 to be too extreme the other way around: while PPO with a GRU seems to fail to learn a good policy for these Maze problems it does not constitute imo conclusive evidence that neural policies cannot generalize to these type of mazes as stated around line 463. It could very well that the neural architecture was ill-chose or the training procedure could be improved. Especially since the programmatic policies on the other side are trained with a completely different algorithm leveraging much large models. 

Overall, I do like the general direction of the paper. Looking at abstracts of referenced material, prior work do tend to put forth the generalization capabilities of programmatic policies (although it is not always the central claim and interpretability is also discussed prominently), and this paper brings nuance to such claims. In the process however, some of the claim in this paper are perhaps a bit too strong (Sec. 4) are lack supporting evidence (Sec. 5). I would be willing to revise my score if the authors can modulate a bit these claims or provide for instance more evidence on why they believe that neural policies will never be able to generalize to problems in Sec. 5.

### Questions
See previous section.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper re-evaluates the claimed out-of-distribution (OOD) generalization of programmatic policies compared to RL-trained neural policies. The paper attempts to answer what causes the generalizability.. The author conducted their experiment on three domains, TORCS, KAREL, and PARKING. In TORCS, the author modified the reward function to test their hypothesis and show DRL algorithms can generalize to OOD environments. In KAREL, the author utilizes the last action and augmentation for policy training, demonstrating better generalization performance compared to existing baselines. In PARKING, RL shows better performance in training against the programmatic state machine, but has similar performance in the testing stage, showing the poor generalization ability of neural policies. The experimental results show that the programmatic representation and neural representation have similar performance in terms of generalization. The authors designed a new task, SparseMaze in KAREL, and utilized FunSearch to search programmatic policies with a large language model, resulting in better generalization against neural-based policies. Based on the evidence, the authors suggest that future benchmarks should consider the advantages and disadvantages of policy representation.

### Strengths
1. Recent programmatic reinforcement learning shows out-of-distribution (OOD) generalization. The paper shows that with carefully curated training techniques, neural-based policies can also generalize to OOD testing sets.
2. The author proposed a new task called SparseMaze that needs search algorithms to find the target. Using an existing search algorithm can find a solution, whereas PPO cannot find a good policy in the training stage.

### Weaknesses
1. In section 5, the author tries to use expressivity and discoverability to define the existence of a generalized solution and a well-developed algorithm for searching the generalized solution. A neural net is a universal function approximator. It is not trivial for a program to have a more generalized solution. Discoverability may be the key advantage for the programmatic policies.
2. The advantage of using a data structure is limited to navigation problems like KAREL. For the control problems like TORCS and PARKING, which data structure is needed to solve these problems more generally?
3. The paper discusses some aspects of the generalization. Clearly state each environment's focus on those kinds of generalization. For instance, the PARKING environment discussed the distribution shift generalization, and the KAREL environment discussed the input-scale generalization.
4. Following 3, Liu et al. [1] compose programs in the KAREL environment to solve the tasks with h reward signal. The compositional generalization of policies is not discussed in the paper.

### Questions
1. In section 4.2 and table 3, there are two versions of the environment, one fully observable and the other partially observable. Which baselines use the fully-observable setting and which baselines use the partially-observable setting?
2. There are six tasks proposed by Trivedi et al. [2], and an additional four tasks proposed by Liu et al. [1]. Why were these five tasks chosen in Table 2?
3. In Table 3, you should add the standard deviation to Successful-on-100 and Success Rate.

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 5

### Summary
Good ideas but poor paper. This paper claims that neural network policies transfer better to new tasks w.r.t programmatic policies than previously shown. They claim that poor transferability compared to programmatic policies was the result of cofounding factors in experiments. However this paper itself is poor.

### Strengths
Good number of environments and baselines. Interesting topic.

### Weaknesses
The most important weakness of this paper is the lack of formalism and rigor.

The claims are not defined and I believe they are tautology. From the abstract ' We argue that a representation enables OOD generalization
if (i) the policy space it induces includes a generalizing policy ', I understand it as: our problem has a solution if there is a solution to our problem.
Similarly, claim (ii) is trivial, 'if an algorithm can find a solution to our problem, our problem has a solution'.

OOD generalization, which is the key metric of this paper is not defined.

Programmatic policies as presented in this paper are mostly non-Markovian, e.g. the programs for the TORCS can query past sensor states in e.g. peek(, -2). This could also be a confounding factor when comparing to Markovian DRL policies.

Authors do not show any convergence curves which is problematic when claiming properties of trained policies.

I don't understand why changing the reward function in the TORCS experiment can explain anything about generalization capabilities of DRL policies. By doing so, you simply changed the problem. In that case you could claim: there exist problems for which DRL policies can generalize as well as programmatic policies. 

I do not understand neither how the other experiments help support the claim that neural network generalize as well or better than programs! what if your training curves did not converge? 

Overall I am not convinced by the problem at hand, the claims, nor the experiments. Key confounding factors include: markovianity of policies (even though it is partially adressed in table 2), potential non-convergence of training, DDPG and PPO were never meant to train policies that generalize OOD so training algorithm choice is also a key confounding factor.

### Questions
Can you show training curves of DDPG , NDPS, PPO, and LEAPS please?

### Soundness
2

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
4