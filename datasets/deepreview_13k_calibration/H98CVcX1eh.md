# Discovering modular solutions that generalize compositionally

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Many complex tasks can be decomposed into simpler, independent parts.
Discovering such underlying compositional structure has the potential to enable \textit{compositional generalization}.
Despite progress, our most powerful systems struggle to compose flexibly.
It therefore seems natural to make models more modular to help capture the compositional nature of many tasks.
However, it is unclear under which circumstances modular systems can discover hidden compositional structure.
To shed light on this question, we study a teacher-student setting with a modular teacher where we have full control over the composition of ground truth modules.
This allows us to relate the problem of compositional generalization to that of identification of the underlying modules.
In particular we study modularity in hypernetworks representing a general class of multiplicative interactions.
We show theoretically that identification up to linear transformation purely from demonstrations is possible without having to learn an exponential number of module combinations.
We further demonstrate empirically that under the theoretically identified conditions, meta-learning from finite data can discover modular policies that generalize compositionally in a number of complex environments

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of compositional generalization in modular architectures. The authors show that in the teacher-student setting, it is possible to identify the underlying modules up to linear transformations purely from demonstrations. They further show that meta-learning from finite data can discover modular solutions that generalize compositionally in modular but not monolithic architectures. The authors also demonstrate how modularity implemented by hypernetworks allows discovering compositional behavior policies and action-value functions.

### Strengths
1. The paper theoretically shows that students can learn the underlying modules from the teachers under certain conditions.
2. The results are supported by empirical experiments.

### Weaknesses
1. The paper is not very well written and is hard to follow. There are no simple examples explaining the problems the authors are trying to solve. The theoretical exposition, particularly in section 3.2, lacks clarity. For example, the connection between the concrete example and the formal definitions and theorems is not immediately obvious, making it difficult to grasp the significance of the theoretical results. The paper would benefit from a more intuitive explanation of the problem setup before diving into the mathematical details.
2. There is no section that explicitly discusses related work. The current discussion section does not adequately cover the relevant literature, making it difficult to contextualize the contributions of this work. A dedicated related work section is needed to clearly position the paper within the existing body of research and highlight its novelty.

### Questions
1. Could you rearrange the paper to have a background section explaining things like MAML, hypernetworks, etc, for readers who are not familiar with these concepts?
2. Could you explain why the network modules have to be hypernetworks in your setting?


-----------
update: raised to 6.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work explores the ability of hyper-networks to detect the ground-truth task generating functions and have modules (rows of the linear hyper-network weights) specialise to these underlying factors of variation. Moreover these modules can then be composed in previously unused combinations to generalise to new tasks. Experiments demonstrating the benefit of modular meta-learning algorithms over monolithic meta-learners are also shown.

### Strengths
## Originality
This paper uses an established technique, the teacher-student setup, to understand the necessary conditions for a dataset to promote systematic generalisation. Moreover, a connection between the teach-student setup and meta-learners is drawn, which I have not seen been made frequently before. Also considering ANIL, MAML and hyper-networks as the class of monolithic and modular meta-learners is interesting a new. Thus, the combination of concepts, theoretical technique and models considered in this work is  new.

## Quality
The theoretical setup of this work seems appropriate for addressing the main concerns of this work - under what dataset conditions do meta-learners naturally generalise compositionally. The overall structure and logical setup of the work is good and sections naturally lead from one to the next. Section 3.3 directly tests the theory which is presented and in the case of Discrete task distributions the experiments support the theoretical findings. As far as I can tell the assumptions of the setup are clearly stated and the setup is clearly defined.

## Clarity
Figures are visually clear and well designed.

## Significance
I reiterate here that I think this work uses a very interesting combination of previous ideas. As a result the reported findings are interesting and I could certainly see the results leading to future work and guiding research on meta learning. Thus, I think this work does have the potential for high significance. I would say this is contingent on some of the weaknesses discussed below being mitigated.

### Weaknesses
I have two broad concerns for this work. One is on clarity and the other is on quality. I will begin with clarity as I think this may be a factor in the concerns on quality.

## Clarity
Overall I found this work to be relatively unclear. Notation is used but not properly introduced, for example $(U_k)$ where it is not mentioned what the double subscript $k$ refers to, or why the second subscript is necessary. Another example is where it is said $\forall k,l$ where it is necessary to infer from context what $k,l$ is referring to. Also where it says $U_{k_i}$ what does the $i$ or $k$ refer to and why is this necessary. Similarly in Theorem 3.1 where it says "The if $\mathcal{L}(W_2,\Theta)$...", what is this new $\mathcal{L}$ referring to? Is it the loss and this is just a mistake in the font? If so, why does this loss function not accept the same  parameters as previous loss functions. Finally, the notation introduced in the paragraph beginning "We can now present our main result" is particularly confusing because the superscript $(i)$ is overloaded three times, once referring to a row, the other referring to a column and the third for a full matrix sliced out from a tensor.

Secondly, Definitions 3.1,3.2 and 3.3 are not clear and no intuition or interpretation is provided. For example, where defining irreducibility, the fact that all rows of $W_1$ are pairwise different means that each hidden neuron will be activated for a different feature - and extremely important point for a work concerned with whether meta-learners can extract ground-truth features from a "metateacher". This is not stated. Similarly, how this interacts with nonlinearities on the hidden neurons is ignored and what it means for no columns of $W_2$ to be $0$ is also not mentioned. Why would a full column of $W_2$ be $0$? Similarly, "Compositional Support" seems to just be saying that $U$ is a basis of $\mathbf{R}^M$ and so I am not certain of how this new terminology is necessary. Is compositional support a weaker case of having a basis as $U$ does not need to be the **minimal** spanning set? Would Definition 3.1 and 3.2 together then imply that $U$ is a basis? Definition 3.3 is just extremely difficult to parse in general and so is Theorem 3.1. This is due to a lot of terminology being mentioned without definition and needing to be inferred based on context. For example, what is $\hat{M}$ and why is Theorem 3.1 making a distinction between even and odd values of $n$? The difficulty in following these definitions alone makes the rest of the work difficult to follow.

My final point on clarity is that the figures, while visually neat and well done, are vague and their captions unhelpful. This is particularly bad when the figures are relied on heavily to explain concepts. For example, where it is said "See Figure 2B for an illustration of a connected support" and then the caption does not explain what a connected support is or how the connected vs disconnected task families connects to the actual Definition 3.3. Essentially, every figure caption should be elaborated on and potentially more information be placed in the figures to depict what is actually going on. For example, in Figure 1B, the tiling of the $x,y$ space is not connected at all to the rest of the work beyond the notation of $p(\tau)$.

## Quality
My concerns on quality are likely due to misunderstanding from the above. I would like to reiterate that I do believe this work has potential significance. I am, however, struggling to connect this work to the general literature on compositional generalisation. For example, assuming that $P_x$ has full support over the input space. I see how the learned weights of the linear hyper-network are compositional, in the sense that they operate similar to a set of basis vectors, which in the case of a linear mapping is also features for the network. However, this is then more similar to feature learning rather than exact modules. Or is the idea here that the features being learned which align with ground truth is the same as identifying a composable module? How would this then tie in with disentanglement, which implies compositionality. While I would be open to such claims - the most obvious on to me here being that feature learning and module learning in the limited setting you study are the same thing - I think that argument needs to be made explicit. This would be a different take on modularity in general though and systematic generalisation which tends to focus more on how separate pieces are learned to be separate in spite of covariances and this makes the problem easier [1]. In your case it seems more like a claim that if the input space is sufficiently explored then the network will learn the ground truth features but just because this is the only way to learn the task (to learn a full-rank basis set) and is not in fact learning to identify or solve a smaller problem which is then composable.

The experiments of Section 4 seem to be more in line with the standard notions of compositionality [2], however due to the above issues grounding the theory to larger scale models of compositionality I also struggle to see how Section 4 fits in with the rest of the work, beyond just demonstrating that hyper-networks are better in compositional domains than ANIL and MAML. Is there a greater connection beyond this (I do think this result is important in its own right though)?

I would be open to increasing my score quite substantially if it is shown that I have indeed missed something crucial. Alternatively if the clarity issues are addressed and the connection to prior work made more explicit I would also increase my score. Likely to a 7. I would certainly prioritise improving the clarity, with the figures being particularly low hanging fruit which would make quite a big difference if improved upon.

## Minor Points
1. "with each row representing one parameter module" - I believe I understood what you were saying, but this was not an easily understandable sentence.

### Questions
I have raised a number of questions in my discussion above. I think the only outstanding question or point of clarification I have at this point is the following:
Could the authors please explain what Figure 2A is aiming to show with the permutation invariance? It is only referenced in condition (ii) but then not explained in the figure. I think I would benefit from understanding this point better.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a multi-task teacher-student approach with modular architecture for compositional generalization.
It uses hypernetworks to convert the generalization to the identification of modules and theoretically show the result up to linear transformation.
Experiments also support the ability.

### Strengths
- It focuses on an important question of how to learn modular structure for compositional generalization.
- The hypernetwork and modularity approach cast the generalization problem into an identification
problem.
- Both theory and experiments support the result.
- It proposes connected support to address permutation invariance.

### Weaknesses
My largest concern is that the framework is very constrained, and some constraints, e.g., linearity, may be essential to deriving the results.
It indicates that there may be difficulty when generalizing the result to more complex situations.

(1) Linear assumption in hypernetwork.

(2) It uses two two-layer neural networks.

(3) It assumes knowing the correct (teacher) architecture.

(4) The theory assumes knowing the number of modules (M) and hidden units (h).

### Questions
Please respond to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors provide a theoretical analysis of the compositional generalization capabilities of linear hypernetworks under a teacher-student setup where the teacher network is the ground-truth data-generating model, and is itself a linear hypernetwork. The key result is that under 3 assumptions (compositional support, connected support, and no over-parameterization), the student can provably _identify_ the modules of the teacher. This identification is further demonstrated to be a necessary and sufficient condition for compositional generalization. The authors provide a series of experiments to validate their theoretical findings and test how sensitive the empirical results are to various violations of the assumptions.

######## Post-rebuttal update ########

Given the authors' response and updated manuscript, I am updating my score to an 8 (this 8 should be considered closer to a 7, but 7 is not an option).

### Strengths
######## Strengths ########
- The problem of compositional generalization is of great interest to the ML/AI communities, and there are very few theoretical treatments of the problem
- The combination of theoretical results and empirical evidence that tests beyond the bounds of the theory is well balanced

### Weaknesses
######## Weaknesses ########
- The experimental setting is unclear, especially the sequential decision-making portion, which makes it hard to assess its impact. Specifically, the description of how the agent learns in the sequential decision-making tasks is vague. It's not clear if a teacher provides demonstrations, or if the agent learns through trial-and-error. Furthermore, the use of 'accuracy' as a metric in a sequential decision-making problem is questionable, as it doesn't directly reflect the cumulative reward obtained by the agent. The connection between this accuracy and actual task performance is not established, making it difficult to evaluate the effectiveness of the proposed method in this setting.
- It is unclear whether the three assumptions (compositional support, connected support, and no over-parameterization) are necessary conditions or just sufficient. The paper states these as sufficient conditions for module identification, but it's not clear if these conditions are also necessary. This limits the understanding of the fundamental properties that enable compositional generalization. The authors should provide examples or counterexamples to demonstrate whether violating these assumptions would prevent module identification.
- The choice of linear hypernetworks as the base modular model somewhat limits the intepretability of the compositionality. While linear hypernetworks offer a way to combine parameters, the resulting modules lack intuitive explanations of what each module does and how they compose. Unlike other modular approaches, such as neural module networks [2], it's difficult to understand the functional role of each module and their interactions. The experiments in Sec 4.2 attempt to address this, but the lack of clarity in the experimental setup makes it hard to gain any intuition about the learned compositionality.

### Questions
######## Additional feedback ########

The following points are provided as feedback to hopefully help better shape the submitted manuscript, but did not impact my recommendation in a major way.

Abstract
- Throughout the abstract and much of the text, it's unclear what types of problems the authors are tackling. There's a mention of "demonstrations" and "action-value functions", which somewhat hints at a solution geared toward RL. Much later, it becomes clear that a "demonstration" is the output of the teacher network, and that action-value prediction is just one application of the linear hypernets.

Sec 3
- Up to this point, it was still unclear to me what the authors meant by identification of modules
    - Is it that the student can determine which modules to use, or that it can find the right set of modules?
    - Is this in a setting where the student knows the latent codes?
    - These are later clarified, but it might be worth doing so earlier on

Sec 5
- It's odd that the authors combined a related work section with the discussion, but I think it works okay. 

Typos/style/grammar
- Intro, page 1 first paragraph: series of tasks --> set of tasks [a series is sequential]

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
