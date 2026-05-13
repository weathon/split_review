# Critical Learning Periods Emerge Even in Deep Linear Networks

- Decision: Accept
- Scores: 5, 1, 6, 8

## Abstract
Critical learning periods are periods early in development where temporary sensory deficits can have a permanent effect on behavior and learned representations. 
Despite the radical differences between biological and artificial networks, critical learning periods have been empirically observed in both systems. This suggests that critical periods may be fundamental to learning and not an accident of biology.
Yet, why exactly critical periods emerge in deep networks is still an open question, and in particular it is unclear whether the critical periods observed in both systems depend on particular architectural or optimization details. To isolate the key underlying factors, we focus on deep linear network models, and show that, surprisingly, such networks also display much of the behavior seen in biology and artificial networks, while being amenable to analytical treatment. We show that critical periods depend on the depth of the model and structure of the data distribution. We also show analytically and in simulations that the learning of features is tied to competition between sources. Finally, we extend our analysis to multi-task learning to show that pre-training on certain tasks can damage the transfer performance on new tasks, and show how this depends on the relationship between tasks and the duration of the pre-training stage. To the best of our knowledge, our work provides the first analytically tractable model that sheds light into why critical learning periods emerge in biological and artificial networks\footnote{Code available at: \codelink}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is a continuation of the study of critical learning periods in deep learning. This work focuses on why critical learning periods emerge in deep linear network models. The paper investigates the critical learning period that depends on the depth of the model and structure of the data distribution, with supporting experiments. Meanwhile, they also show the learning of features is tied to competition between sources. They analyze the impact of pre-training on some tasks, and there are some simple experiments used to prove the “critical learning periods”. This work provides analytical understanding of critical periods in deep linear networks and draws connections between artificial and biological learning.

### Strengths
1. This paper continues previous work (on the deep network), the experiments correspond to research on the depth of the network, data distribution, competition between sources, and pre-training.
2. This work on studying the competition of different data sources is solid, and it seems to be a relatively good job through the linear multi-pathway network.
3. Analytical and minimal models provide fundamental insight. Intuition and empirical observations match well.

### Weaknesses
1. The paper is less readable and requires a higher theoretical foundation. The description of the “linear multi-pathway framework” (Sec.3.1.) is not clear enough and lacks corresponding details. Specifically, the paper does not clearly define the dimensions of the weight matrices and input/output vectors, making it difficult to follow the mathematical derivations. The explanation of how the different pathways interact and compete is also vague, and it would benefit from a more detailed explanation of the underlying assumptions and constraints.
2. Only studying deep linear networks seems not enough to clearly understand why deep networks have critical periods, and network depth and data sources cannot guarantee sufficient persuasiveness. While linear networks provide a simplified model, they may not capture the complexities of non-linear activation functions and their impact on critical periods. The claim that network depth and data source competition are sufficient to explain critical periods requires more rigorous justification, especially considering the role of other factors such as optimization algorithms and regularization techniques.
3. There are fewer categories of experiments, and it would be better if the authors could provide more types of experiments to prove their claims. The experiments are primarily focused on linear networks and matrix completion tasks. It would be beneficial to include experiments on more complex tasks and datasets, such as image classification or natural language processing, to demonstrate the generalizability of the findings. The current experiments do not fully explore the range of scenarios where critical periods might emerge.
4. For the experiments related to pre-training, I cannot guarantee sufficient correlation with key learning practices. I hope I can explain the motivation for doing this part of the experiment. By the way, this is not to say that this is an obvious weakness. The connection between the pre-training setup and real-world pre-training scenarios is not clearly established. The paper should provide a more detailed explanation of how the chosen pre-training method relates to common practices and what specific aspects of critical periods it aims to investigate. The motivation behind the specific pre-training task should be more clearly articulated.
5. I don’t find any support in the paper for what the abstract said: “Why critical learning periods emerge in biological and artificial networks”. The paper does not provide sufficient evidence to support the claim that the findings are relevant to biological systems. The connection between the observed critical periods in linear networks and the critical periods observed in biological systems is not clearly established. More discussion is needed to bridge the gap between the artificial and biological domains.

### Questions
Please see the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Noting the anecdotal and empirical evidence of critical periods in both biological and artificial learning agents, the authors hypothesize that critical learning periods are a general feature of learning, and not an accident of biology or training, They investigate this hypothesis analytically via deep linear networks, which retain many characteristics of typical neural networks while being amenable to tractable analysis. They perform a variety of analyses and experiments, largely inspired by work on critical periods in biological systems, demonstrating that depth and data distribution provide information processing constraints that give rise to the critical periods.

### Strengths
Well written, interesting avenue of research. Results well explained early in the text, with clear examples and clear explanations of experimental settings and technical details. Particularly nice clarity given the cross-disciplinary nature of the work.
Related work is well written, reasonably thorough (to my knowledge), and well-explained.
Nice phase portraits.
Captions are mostly well-explained and self contained! (I don't know why this is so rare, but good job)

### Weaknesses
It's a bit of a tradeoff with having a clear hypothesis, but I find the case oversimplified/misframed  in the beginning and conclusion. Sure the literal biochemical explanation doesn't hold in an artificial setting, but analogies of this (reduced plasticity) could well occur. I don't think these are 'competing' hypotheses as they are framed; plasticity, imperfect optimization, etc. are *mechanisms* by which critical periods could arise in both artificial and biological systems; it doesn't tell us the reason   (inherent to learning, quirks of substrate, something else, etc.). In the conclusion "natural information processing constraints" are contrasted with biochemical processes like plasticity as an alternative hypothesis, but what is (decreased) plasticity buyt a natural information processing constraint? Demonstrating presence in artificial systems doesn't estabilsh it as a general feature of learning, except insofar as we've defined learning narrowly to be done by biological and ANNs (does naive bayes learn? does it exhibit critical periods?). It becomes sort of a circular argument about what does "learning" even mean. This commonality is actually supported by your experiments in Fig 3 recreating Guillery's. Anyway, I think the key sentences/claims (e.g. last of the abs) and results stand and are extremely interesting,  I would just like to see this framed around mechanisms or instantiations of information processing constraints, or something, rather than competing hypotheses. and maybe acknowledge more of the ambiguity of what "learning systems in general" means/ (without compromising clarity and narrative, which I believe are strong points of the paper).

Terms used in equations are not explained when introduced  in 3.1 -- I know it's from a citation and you might be short on space, but you will lose a lot of readers here and it's a shame not to continue the clear prose you've had thus far.

Around eqn 9, connection of matric completion to what you're trying to do is not clear -- be explicit about how imputing missing values is the same as / allows us to specify  task relationships with flexibility. 

While the relationship of experiments to showing dependence on depth is very clear and well-explained, the insights and relationship of experiments to data distribution is much less clear.



### Questions
See "weaknesses" for some less concrete suggestions (feel free to tell me what you plan to write if you address them and I'm happy to provide feedback!)

The main other thing I'd like to see is connections made/discussed with nonlinear networks -- what should we expect to change vs. hold? maybe according to the sources you cite (e.g. Saxe), or ideally, a suite of experiments with e.g. MLPs of increasing depth. 
Another specific link could be made in Fig. 6 to scaling laws.

small things:
 - first sentence shouldnt repeat abstract
 - 'competition between pathways affect' -> affects
- inconsistent use of "artificial neural network", "deep net", "neural net", et al. For me it's fine, but could be confusing for someone outside the field; better to be consistent 
- title for plot should be removed (conflicts/causes potential confusion vs caption and X axis label, nonstandard for technical works to have an embedded title)
 - remind us what "Path Singular Value" is in the caption/change caption e.g .singular value dimensions (confusing that its referred to as 1-5 but labelled 0-4 on plot and called something different). All this stuff explaining the axis and basics of the plots should go first, before the interpretation. - I didn't understand the comment "and do not affect performance on the final gask" in fig $. Does it mean they have equal performance?

### Soundness
4 excellent

### Presentation
4 excellent

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
This paper demonstrates that critical learning periods in deep learning models depend on the depth of the model and the structure of the data distribution, offering an analytical perspective on the learning dynamics. This study provides both analytical and simulation evidence that the learning of features is closely tied to the competition between different sources of information, highlighting the competitive dynamics within the learning process.

### Strengths
1. This paper is well-written, technically solid and has a concrete flow.
2. This work offers insights into the reasons behind the emergence of critical learning periods in both biological and artificial networks.

### Weaknesses
1. I think the assumption of the deep linear network is a bit strong. Since in real-world applications, most neural networks require non-linear activations. A deep linear network can be actually approximated by a single-layer linear network. The analysis might not fully capture the complexities of learning dynamics in networks with non-linearities, which are crucial for many real-world tasks. Specifically, the interaction between different layers through non-linear activations can lead to emergent behaviors not present in linear networks, such as feature specialization and hierarchical representations. These aspects are not addressed in the current analysis.
2. Critical periods in artificial deep neural networks (DNNs) may be due to specificities of the optimization process, such as an annealing learning rate, or from defects in the artificial implementation and training, like ReLU units becoming frozen or gradients vanishing. The paper does not sufficiently address how these factors might interact with or confound the observed critical periods. It would be beneficial to explore how different optimization techniques and activation functions influence the emergence and characteristics of critical periods. For example, the effect of batch size, momentum, and weight initialization strategies could be considered.
3. What's the model's generalization ability on more sparse data settings? The paper needs to provide more details on the performance of the proposed model under different levels of data sparsity. It would be important to understand how the model's ability to learn and generalize is affected when the input data has a significant amount of missing or unobserved values. This is crucial for understanding the practical applicability of the model in real-world scenarios where data is often incomplete.

### Questions
Please consider the things listed in the “Weaknesses” section.
Also please consider providing information regarding the limitation and future work of this paper.

### Soundness
3 good

### Presentation
2 fair

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
This paper reveals that critical learning periods are not limited to biological learners
but are fundamental to the learning itself. Through well-written experiments, the
authors show how deep linear networks display critical learning periods. They
conducted two experiments: one focused on competition in a multi-path model
(similar to our eyes), and the other focused on the effect of critical periods on transfer
learning.

The first experiment reveals that a deprivation deficit in one pathway will result in the
other pathway to winning the competition and learning all the corresponding features.
The deprivation only has an effect if applied in the early epochs. This reinforces the
critical learning period claim. The authors also show, by permanently lesioning the
dominant pathway, that the deprived pathway isn’t dead and will pick up features that
the dominant pathway has missed.

The second experiment highlights the effect of depth and data distribution on the
impact that deprivation during the critical period has. It reveals that deeper networks
are more sensitive to deprivations in the critical period, and the structure of the data
distribution also dictates the impact of the deprivation.

### Strengths
1. The paper provides a mathematical understanding of the psychological concept of the “critical learning period”.
2. The paper reveals that critical learning is not restricted to biological learners but is inherent to learning itself!
3. Theoretically strong.
4. Well-thought-out and well-delivered experiments.
5. The paper neatly highlights the pros and cons of competition between a model’s branches.
6. By introducing a permanent lesion in the dominant branch, the authors show that the deprived branch isn’t dead for the rest of the training.
7. The authors draw convincing insights from the transfer learning experiments, both low-to-high rank and high-to-low rank. In the appendix, the authors have also covered (both theoretically and experimentally) the case where two different matrices are involved.

### Weaknesses
 > …our analysis shows that critical periods only depend on two main factors: the depth of the model and the structure of the data
distribution, as opposed to details of the architecture and optimization problem.
1. The authors prove the dependence on depth and data distribution. But how can
they claim independence from other factors, like architecture and non-linearities,
especially when considering models other than deep linear networks?

2. Figure 2’s markers should be changed. It is difficult to differentiate between a
circle and a circle-triangle overlap. Try plus (+) and cross (x) as markers or a
straight line (|) and an oblique line (/).

3. Codebase not provided.

4. Typos:
* Page 3: had minimum the → had the minimum
* Page 6: training has only affects → training only affects

### Questions
> In the multi-pathway experiments, when we applied the deficit to
a pathway, which we refer to as “blocking” or “gating” an input to
a pathway in the paper, the desired target output was also shifted
by a baseline amount corresponding the deprived pathway’s
output. This was to ensure that the normal pathway was only
required to learn the unexplained component of the output, and
not the entire output.

I understood the use of PyTorch’s “.detch()” for blocking the flow of gradients in the
deprived branch. However, shifting the desired target output to ensure learning the
unexplained component did not make sense to me. Please elaborate.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
