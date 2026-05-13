# Addressing Long-Horizon Tasks by Integrating Program Synthesis and State Machines

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
Deep reinforcement learning excels in various domains but lacks generalizability and interoperability. Programmatic RL (Trivedi et al., 2021; Liu et al., 2023) methods reformulate solving RL tasks as synthesizing interpretable programs that can be executed in the environments. Despite encouraging results, these methods are limited to short-horizon tasks. On the other hand, representing RL policies using state machines  (Inala et al., 2020) can inductively generalize to long-horizon tasks; however, it struggles to scale up to acquire diverse and complex behaviors and is difficult to be interpreted by human users. This work proposes Program Machine Policies (POMPs), which bridge the advantages of programmatic RL and state machine policies, allowing for representing complex behaviors and addressing long-horizon tasks. Specifically, we introduce a method that can retrieve a set of effective, diverse, compatible programs. Then, we use these programs as modes of a state machine and learn a transition function to transition among mode programs, allowing for capturing long-horizon repetitive behaviors. Our proposed framework outperforms programmatic RL and deep RL baselines on various tasks and demonstrates the ability to inductively generalize to even longer horizons without any fine-tuning. Ablation studies justify the effectiveness of our proposed search algorithm for retrieving a set of programs as modes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes to solve long-horizon tasks by synthesizing programs to accomplish the task. Since existing methods for synthesizing programs struggle with long-horizon tasks, this work proposes to synthesize simple programs and then learn to compose these programs. Specifically, this work takes an approach involving three steps:
(1) An embedding space over programs is learned.
(2) A set of diverse and reusable programs is retrieved by searching over the embedding space.
(3) A function is learned to compose these programs: i.e., to choose which programs to execute one after another.

This work evaluates its proposed approach on a benchmark of Karel tasks, involving picking and placing objects in a grid world and finds that the proposed approach performs favorably compared to prior approaches for program synthesis.

### Strengths
This work investigates an interesting and novel method for solving RL tasks by generating and composing programs. The results indicate improved performance over prior approaches and could be interesting to the RL community.

### Weaknesses
I initially lean toward rejection due to two primary concerns:

(1) *Unclear presentation and missing details.*
- Several key pieces of information are not clearly described in the main text of the paper, which makes it difficult to understand the exact proposed approach and to reproduce the results:
- How are the programs over which the embedding space is learned generated? Are they simply randomly sampled from the Karel DSL? These programs form such a crucial building block for the method that it's worth discussing how they're generated here, and how they might be generated in other domains. The paper should specify the distribution from which these programs are sampled, including any constraints on program length or complexity. Without this, it's difficult to assess the generality of the approach.
- How are the rewards defined in the CEM optimization in the retrieval stage? It seems like one would need many different reward functions to ensure good diversity and coverage in the selected modes. Is it task-specific? This crucial information does not appear to be clearly explained anywhere. The reward function used for CEM should be explicitly stated, including how it incorporates both task-specific rewards and diversity-promoting terms, if any. The paper should also clarify whether this reward is fixed or adapted during the retrieval process.
- How is the transition function f learned? Is this learned via standard RL, where choosing the modes is the action? The paper needs to be more specific about the RL algorithm used to learn the transition function, including the state and action spaces, and the reward function. Details about the exploration strategy and any hyperparameters used are also necessary.
- How do state machine policies differ from other notions of hierarchical reinforcement learning? It seems like the modes can simply be interpreted as "skills" or formally options in a SMDP framework. The paper should clearly articulate the differences between the proposed state machine policy and existing hierarchical RL methods, particularly in terms of how the modes are defined, learned, and composed. A more detailed comparison with options framework would be beneficial.
- Details about the state are missing from the main body of the work, which makes it difficult to understand the task. From what I gather from the Appendix, a N x M array is used as the state for a N x M grid world for the deep RL baseline -- is this the same state that the proposed approach uses for selecting which mode to switch to? The paper should explicitly define the state representation used for both the deep RL baseline and the proposed approach in the main text. It should also clarify whether the state representation is the same for both, and if not, why not. The impact of different state representations on performance should also be discussed.
- The deep RL baseline seems to be surprisingly weak, given that the task is just grid world pick and place. Is there a reason behind this? Is it a result of the state representation? Does e.g., using a different state representation of just the agent's (x, y) coordinates work better? The paper should provide more analysis on the performance of the deep RL baseline, including a discussion of why it performs poorly on certain tasks. The impact of different state representations, such as using only the agent's coordinates, should be investigated and discussed.

(2) *Concerns about the generality of the proposed approach.*
- While the details for how the entire space of programs is generated is missing, it seems difficult to imagine being able to do this well for arbitrary domains. In general, writing programs that can easily compose is challenging, particularly when they have inputs and outputs, whereas this domain is particularly simple and the programs do not need to take arguments or return values. Consequently, I'm concerned that the proposed approach may not be able to be applied to other less toy domains. Discussion about this would be very helpful. The paper should include a more thorough discussion of the limitations of the proposed approach, particularly in terms of its applicability to more complex domains. The challenges of generating composable programs with inputs and outputs should be addressed.
- It also seems generally difficult to span a set of useful behaviors needed in the programs. How can this be achieved without ending up with an intractable space of programs to search over? The paper should discuss the challenges of ensuring that the generated programs span a diverse set of useful behaviors, and how the proposed approach addresses this issue. The potential for ending up with an intractable search space should also be addressed.

### Questions
Please see the many questions in the previous section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a system that combines program synthesis and finite state machines to generate policies for solving reinforcement learning problems. The authors built on the previous work of LEAPS, where one trains a latent space of programs that is used as a search space for policies. The LEAPS space is used to generate a set of diverse behaviors (modes), and later, a reinforcement learning algorithm is trained to learn how to transition from one mode to the next. 

The system is evaluated on novel Karel tasks, which includes the need of repetitions.

### Strengths
The problem of learning policies with programmatic representations is an important one and this paper makes a contribution in this line of research. I also enjoyed the idea of mixing synthesis in the Karel language with finite state machines. Although I find it a little odd the dichotomy used in the paper: programmatic and FSM. I find it odd because a FSM is also a program, but in a language different from the Karel language. Perhaps the main contribution of this work is to show how to combine the inductive biases of two languages, where one is used to learn small functions and the other is used to combine such functions.

### Weaknesses
Although I like many of the ideas in the paper and I also found it very easy to read and understand, I have several important issues with the current submission.

**Interpretability Motivation**

The main motivation of the work is around interpretability. The paper states already in the abstract the separation between FSM and programmatic solutions, where the former allows for repetitive behaviors and the latter for interpretability. The paper specifically cites the work of Inala et al. as being difficult to be interpreted by human users. Similarly to how I can accept that programs in the Karel language can be interpretable, I can also accept that the FSM learned with Inala et al.'s system to also be interpretable. As far as I know, no paper has actually evaluated the interpretability of these systems, so the argument that FSM aren't interpretable is wrong to me.

Even if we accept that the policies the system of Inala et al. generates aren't interpretable and the programs in the Karel language are, I still find it hard to accept that the policies POMP encodes are interpretable. The choices of which mode to execute next are provided by a neural network, which arguably is hard to interpret. While it is easy to accept that the modes are interpretable (although no evidence for it was provided), I would accept that the POMP policies are interpretable only after seeing some strong evidence of the fact.

**Empirical Methodology**

I apologize if I missed this in the paper, but is the process of learning modes accounted for in the curves shown in Figure 6a and in the numbers shown in Table 2? And is the learning of modes performed in the target task? I ask this question because, due to the compatible constrain, learning modes is essentially learning a solution to the problem because it already tries to combine programs such that they can maximize the expected reward. I might have also missed this information, but it isn't clear the number of steps used to train each system.

It is disappointing that POMP was not evaluated on the original Karel problems from LEAPS and HPRL. I was particularly interested in seeing POMP performance in the original DoorKey problem. Since both CEM and CEM+diversity get the reward of 0.50 with 0.0 standard deviation, I can only assume that the system learns how to get the key, but it doesn't open the door. Due to the way POMP is trained, it would not find a mode that knows how to act once the agent picks up the key. I suspect POMP would take much longer to reach the same reward of LEAPS and HPRL. I would like to see results of POMP on the original set of problems, to see how it compares with LEAPS and HPRL.

Since I was not convinced with the interpretability argument against FSM and in favor of POMP, the experiments miss a baseline that learns FSMs. If not Inala et al.'s method, then the method by Koul et al. (Learning Finite State Representations Recurrent Policy Networks).

I also missed a baseline that searches directly in the space of programs, like in genetic programming. For example, Aleixo & Lelis (Show Me the Way! Bilevel Search for Synthesizing Programmatic Strategies) use a two-level search with simulated annealing to search for programmatic policies. How would this method compare? 

What about NDS by Verma et al. (Programmatically interpretable reinforcement learning), can it be used to find programs for Karel?

### Questions
1. Is the process of learning modes accounted for in the curves shown in Figure 6a and in the numbers shown in Table 2? 

2. Is the learning of modes performed in the target task?

3. How does POMP perform in the original DoorKey domain? 

4. Why not consider other baselines such as NDS and Simulated Annealing?

### Soundness
2 fair

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
This work proposes a programmatic RL framework which is both interpretable and capable of inductive generalisation. This is achieved by a three steps process. First the program embedding space is pre-trained using a VAE. This embedding space is then searched using CEM  to obtain programs which are then used to construct a finite state machine in the third step. The transitions between modes is also learned using RL. The primary technical contribution of this work lies particularly in how the programs are retrieved to ensure that they are able to obtain rewards (effective), provide new capabilities to the model (diverse) and also work well when applied in sequence (compatible).

### Strengths
## Originality
This work combines existing ideas in a unique way to achieve the proposed framework. The main originality of this work lies in the construction of the evaluation function which influences how the programs are obtained from the embedding space. Explicitly enforcing sampling of programs which are compatible with the previous and subsequent programs appears original and useful to the RL setting.

## Quality
This work clearly motivates each step in the pipeline and each component of the evaluation function. The figures of this paper are particularly high quality and helpful in presenting the pipeline. Overall the experimental design and setup is appropriate to evaluate the hypothesis of the work and the extension of the benchmarks is clearly able to determine the relative performance of the baseline algorithms and POMP, as well as the effect of the various ablations on POMP. Experimental results are interpreted fairly and presented clearly.

## Clarity
The work is written well and figures are legible and clear. An extremely minor point, in Figure 6a marker ticks aren't used but in Figure 6b they are. Consistency on this would be nice and if possible adding the ticks to 6a would be useful. Once again, I will note that the explanatory figures are particularly useful. The general consistency between them is makes them work together particularly well and presenting the ideas.

## Significance
Interpretability and hierarchical policies are both well established concepts and are important in RL. Thus, the prospect of having a hierarchical and interpretable model is definitely significant. I also agree that in most hierarchical frameworks it is usually the case that some clarity in how a policy achieves a certain goal is lost at the more detailed level. There is, however, a greater degree of clarity at the level of the hierarchical policy which transitions through the state machine or chooses programs/options/value functions. Thus, the proposed pipeline as it is presented would be clearly significant to the field for achieving an interpretable policy across both levels of the policy abstraction. Additionally, the new benchmarks appear challenging and increase the significance of the work. Overall, I can see this work leading to future work in programmatic RL, as well as being of practical use.

### Weaknesses
## Quality
My primary concern for this work is the depth to which the proposed pipeline is considered. I think that all explicit claims in this work are accurate, however I think that the pipeline is not challenged or considered fully. For example, the compatibility regulariser ensures that programs are compatible to the previous and subsequent programs. This does not seem to ensure compatibility across multiple programs. There is almost a markov assumption being implicitly used at the level of the programs. If this is true, it should be stated explicitly as it is an important point. It makes the comparison to Skill Machines less valid and also makes the pipeline resemble an Options framework far more. Moreover, skill machine are primarily used to encode long-horizon tasks where transitions between FSM states corresponds to a meaningful (usually semantic) change in the environment. However, since all all programs here are being sampled from a pre-trained embedding space which is not conditioned on the state or context of the environment, it seems all programs are only usable in the same environment, making them more monolithic in their own right. On the point of this resembling Options, how inaccurate would it be to characterise POMP as being interpretable Options since there is still a high-level neural network being used to pick programs.

Given the above my score is quite low to begin with, but I also acknowledge that some of my criticisms could also be due to me missing a subtle distinction between POMP and other works. So my confidence will also remain relatively low to start. I am certainly willing to increase both following a discussion on the above if it is shown that I have indeed not appreciated a point fully. I also reiterate, the work as proposed seems very significant, I am just not certain POMP goes all the way to achieving what is proposed.

Finally, I am concerned with the baselines which are being compared against. They seem to perform extremely poorly on the benchmarks, except in the cases where they work well and then they beat POMP. For example, DRL on the INF-DOORKEY domain and HPRL on INF_HARVESTER. While it beating POMP is not a problem, I would like to know what about this one particular domain made DRL work and better. Similarly in the ablation study, why are CEM and CEM+diversity capped at 0.5 performance. Why is the performance of CLEAN HOUSE and SNAKE particularly bad for both. Relatively little insight or discussion is given on these points. As a consequence it is difficult to get a good idea of the strength and weaknesses of POMP.

### Questions
I have asked a number of questions above in the weaknesses section which I think would aid my understanding greatly if answered. However, in line with some of what was mentioned there I would like to ask if the authors have a sense of the recursive optimality of POMP? This would also help contextualise or ground POMP in the rest of the hierarchical RL literature.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of solving long-horizon tasks through programmatic RL. Specifically, the authors first learn the program embedding space for sampling the mode programs, and then learn a mode transition function to compose the programs towards the final task goal. Experiments are performed on several tabular tasks to validate the idea.

### Strengths
The paper presents an interesting idea that utilizes state machine representations and program generation for solving long-horizon tasks; 

The performance is on par or better than other baselines from the evaluation perspective; 

The paper is well-written and easily read.

### Weaknesses
The framework utilizes 3 stage design where the learning of the program embeddings and the mode transition function are separated, which could lead to cascading errors;  

The absence of strict constraints to guarantee compatibility between generated programs could result in execution incompatibilities; 

The experiments only consider simple tabular tasks, and only a few baselines are compared. Demonstrating the effectiveness of the framework on more complex tasks would strengthen the paper.

### Questions
In Sec. 4.2.3, the most compatible program is selected by inserting the newly generated program into a randomly chosen program sequence and ranking the returns of the execution, would this design guarantee compatibility? If not, what’s the failure ratio of the case that the generated program cannot be executed due to the compatibility issue? 

It seems the method does not perform very ideally in the INF-DOORKEY and INF-HARVESTER, could authors provide additional explanations on this? Including more analysis of the failure modes would also help readers understand the limitations of the work; 

Some related works also explore state machines for high-level transition abstraction in RL, e.g., integrating symbolic planning and skill policies [1][2][3], please consider discussing or comparing; 

Reference: 
[1] LEAGUE: Guided Skill Learning and Abstraction for Long-Horizon Manipulation, RA-L 2023;   
[2] Leveraging approximate symbolic models for reinforcement learning via skill diversity, ICML 2022; 
[3] PEORL: Integrating Symbolic Planning and Hierarchical Reinforcement Learning for Robust Decision-Making, IJCAI 2018.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
