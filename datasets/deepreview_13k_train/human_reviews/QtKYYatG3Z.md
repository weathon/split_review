# Evaluating the World Models Used by Pretrained Learners

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
A common approach for assessing whether generative models develop world models is by studying the behavior of fixed models. However, many of the benefits of having a world model arise when transferring a model to new tasks (e.g. few- shot learning). In this paper, we ask: what does it mean to test if a _learner_ has a world model embodied in it? We consider a simple definition of a true world model: a mapping from inputs to states. We introduce a procedure that assesses a learner’s world model by measuring its inductive bias when transferring to new tasks. This inductive bias can be measured in two distinct dimensions: does a learner extrapolate to new data by building functions of state, and to what degree do these functions capture the full state? We use this procedure to study the degree to which pretrained models extrapolate to new tasks based on state. We find that models that perform very well on next-token prediction can extrapolate to new tasks with very little inductive bias toward state. We conclude by assessing the possibility that these models learn bundles of heuristics that enable them to perform well on next-token prediction despite preserving little of state.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a framework for evaluating whether learning algorithms develop world models using two measurements: i) inductive bias toward “state” and ii) state recovery. These metrics are used across various model architectures and a handful of domains to highlight that high performance on next-token prediction does not imply inductive bias toward state.

### Strengths
1. **Originality**. I think the overall question is interesting.

2. **Quality**. I like that the authors choose simple testbeds to investigate potentially interesting phenomenon. 

3. **Clarity**. I think the structural choice of first introducing the theoretical framework then moving to the exact implementation makes sense.

4. **Significance**. The paper provides framework for understanding why models might perform well on pretraining tasks without developing true world modelsI. I like that the paper includes evaluations of multiple modern architectures, and this investigation appears to reveal interesting patterns. For example, Mamba models perform better with state supervision but worse with next-token pretraining vs. transformers (Table 1).

### Weaknesses
1. **Lack of clear, grounded definitions.** The paper defines a world model as a mapping from inputs to “state” (page 1); however, this mapping is clearly insufficient. Without a precise, formal definition of what a world model is and ought to achieve, the two metrics for measuring world model quality are not well justified. For example, a lookup table mapping inputs to states would satisfy this definition but isn't what we typically mean by a "world model". As another example, a useful world model might abstract away irrelevant state details while capturing key dynamics. I suggest i) a more precise definition of a good world model and its properties and ii) a discussion of how these properties relate to the extensive world model literature. This lack of definition is confusing given existing definitions in the literature [1-3].

2. **Confusing writing.** Continuing with W1, the paper uses terms like "state" without grounding in established frameworks (e.g., MDPs). This lack of clarity made the paper very hard to follow. I also found it difficult to understand the motivation and premise behind the work.


3. **Lack of engagement with relevant literature.** Given the usage of reinforcement learning terminology, I am surprised by the lack of engagement with the relevant literature. For example, this work does not engage with the extensive literature on state abstractions, which seeks to address similar research questions. The state abstraction literature in reinforcement learning [4-7] has extensively studied questions like: i) What makes a good state representation?, ii) When can we compress states while preserving important properties?, and iii) How do different types of state abstractions affect learning and transfer? The "partial reconstruction of state" metric, defined in Definition 2.2, seems related to concepts like bisimulation metrics (how can we cluster states that behave similarly?) and MDP homomorphisms (what state mappings preserve the essential dynamics?).

4. **Unnecessary “mathiness”**. Proposition 2.3 is tautological. 

5. **Unclear methodological decisions**. I don’t understand the synthetic dataset construction part in Section 2.2. If one constructs a dataset that is generated from some behavior policy, there is no reason that assigning random outputs would map to any meaningful task. The lack of a clear objective function for the synthetic datasets makes it difficult to interpret the results.


6. **Results presentation**. Results lack significance testing or even any error bars. The lack of statistical analysis makes it difficult to assess the robustness of the findings.

7. **Wrong format**. The paper is missing the line numbers that are standard in the ICLR template.

### Questions
1. Could the authors please clarify and motivate this instantiation of a world model?

2. Could the authors please justify why these choices of metrics are connected to desirable properties of a world model?

3. I don’t think the finding that incorrect board position still yields correct predictions of legal moves is that surprising from the state abstraction perspective. What seems to be happening is that the internal learned representation is lossy; model-based RL typically works with imperfect models that learn sufficient dynamics for good policy learning. In essence, one doesn't need a perfect world model for decision making. Could the authors clarify why this is undesirable?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper aims to test if a learner has a world model embodied in it.
To assess a learner’s world model, the paper measures its inductive bias when transferring to new tasks and proposes two metrics to measure the inductive bias: inductive bias (IB) and state recovery (SR).

Experiments on five pretrained models (RNN, LSTM, Transformer, Mamba, Mamba-2) in areas where the true world model is known (orbital mechanics, lattice problems and Othello games) show that these models learn bundles of heuristics that enable them to perform well on next-token prediction despite preserving little of state and having poor transfer properties for new problems.

### Strengths
1. The paper proposes a new procedure to test if a learner has a world model embodied in it by measuring its inductive bias when transferring to new tasks, instead of studying the behavior of fixed models.
This procedure provides a novel perspective to investigate whether pretrained models develop world
models.
2. The test models and scenarios in the experiments are representative, and results are inspiring.

### Weaknesses
1. Experiment results may not generalize to large pretrained models, such as LLMs, which are pretrained in a vast amount of data and have billions of parameters. I wonder if authors have plans to scale up the experiments to larger models, or if they could discuss potential limitations in generalizing their findings to LLMs. The current experiments focus on relatively small models and synthetic datasets, which may not fully capture the complexities of real-world scenarios where LLMs are deployed. The inductive biases observed in smaller models might not directly translate to the emergent behaviors seen in LLMs, which often exhibit different learning dynamics due to their scale and training data.
2. The title for Table 1 and Table 2 should be more detailed and include result analysis, including key trends that are highlighted in the tables and why the trend exits. The current titles lack sufficient context to understand the significance of the results presented in the tables. For example, it is unclear what specific metrics are being compared across different models and tasks, and what the implications of these comparisons are. Without a more detailed analysis in the table titles, it is difficult to grasp the key findings and their relevance to the paper's claims.

### Questions
1. Please provide a more explicit explanation of the question "what does it mean to test if a learner has
a world model embodied in it?", and how experiment findings relate to this question. And please state the motivation behind this question.
2. What are the advantages of the proposed measuring procedure over other studies to assess whether pretrained models develop world models (e.g., studying the behavior of fixed models)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a new framework to evaluate whether the learning algorithms utilizes world models to make predictions. Basically, it develops two metrics that captures the model's world modeling capabilities, one is inductive bias towards world state when it transfers into new tasks; the other is the degree to which a learner recovers state, such as whether the new prediction function utilizes information of all the state, or some aspects of them. Experiments are done under controlled setup, the results are kind of interesting, it shows that although most of the models perform well on next-token predictions, they have poor inductive bias towards world state, hence transfer properties, and the authors hypothesized that the models might rely on bundles of heuristics.

### Strengths
- The paper is well-written and easy to follow. The evaluation framework is described in a clear manner, from the definition of inductive bias and state recovery, towards on how to measure them via the lens of transfer learning, etc.
- This paper does show some valuable insights on whether or not the models are utilizing world models to do the prediction, I do find the empirical observations about the model's limited inductive bias and poor transfer properties interesting. For example, the case listed in Bundles of Heuristics about the model does not need to understand the board correctly in order to make the legal moves is kind of surprising. 
- The controlled synthetic experiments is well-done and it shows very clear evaluation and understanding on the world-modeling capabilities of current models that good at next-token prediction.

### Weaknesses
 - I’m curious whether the measurement of inductive bias is highly dependent on the distribution of the training data. For instance, if the data distribution is more uniform and not covers only a small subspace, would this significantly alter the conclusions? In the case of orbital mechanics, would a model trained on a more uniform distribution still capture universal laws?
- In the cases of Lattice and Othello, do the ground-truth states represent the minimal information needed for next-token prediction? I’m particularly considering the results shown in Figure 2.
- I appreciate the 'empirical' evaluation framework, but it seems to depend on various factors, like the IB loss function, reconstruction loss, transfer setup, data distribution, and so on. How sensitive are the conclusions in the paper to these parameters, and how well do they generalize? Specifically, the choice of the IB loss function seems crucial; a different loss might lead to different conclusions about the inductive bias. Similarly, the reconstruction loss and the specific architecture used for state recovery could influence the results. A more thorough sensitivity analysis is needed to understand the robustness of the findings.
- Could you comment more on how these world models connect with the memorization and reasoning concepts in the LLM community if possible?

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents new methods to study whether a trained model’s performance is made possible by an internal “world model”, meaning representations of the underlying “state” which generates the data. For example, in their gravitational trajectories example, the data itself is the observed position of the planets at different time-steps, while the underlying state includes their velocities and masses (which determine future positions). To that end, the authors present and motivate two metrics (IB and SR) meant to capture the extent to which a learned model’s behavior can be understood as depending only on the (unseen) states, and as depending on all such states (instead of a coarser classification). Experiments are run on several different sequential datasets with a known underlying state, testing how different architectures score on these metrics against random baselines, as well as a baseline directly trained on state observations. In some cases, other methods are used to interpret model behavior, like regression. The authors indeed find that different architecture and task pairs score differently on these metrics, and discuss their interpretation.

### Strengths
The topic is pertinent and of broad scientific interest and the work is ambitious. They propose a set of concepts and formal metrics that (to my knowledge) are novel and are a potentially valuable contribution. These metrics are connected to empirical experiments in a potentially fruitful way. The baselines seem reasonable. 

The discussion of related work seems adequate (although it would be hard for me to tell whether it’s missing something important). The orbital mechanics domain is elegant and seems like a good toy domain for future work. The other domains have appeared in previous related work, and so seem like a reasonable choice. The empirical observation in Section 4.3 that the learned model fine-tuned on state prediction is correct about legal moves but not the whole board is interesting.

### Weaknesses
Unfortunately, I believe there are several important weaknesses with the paper’s main contributions (which might or might not be easy to address), as well as its presentation.

The main contribution of the paper are the metrics defined in Section 2.1. While their motivation is understandable, it is not immediately clear, nor in my opinion sufficiently justified, why these metrics are tracking what the authors propose they are tracking (i.e. the extent to which a model’s internal mechanisms correspond to the world-model generating the data). While the binary definitions (2.1 and 2.2) make intuitive sense (modulo some presentation problems which I discuss below), there’s no explanation for why their quantitative extension is appropriate for the author’s purposes. For example, even when dividing by the random baseline, it is hard to interpret what different scales correspond to. For example, whether a 0.6 IB represents, intuitively speaking, a model clearly using a pretty accurate state-model (albeit still short of a perfect one), or instead a 0.6 IB can be attained “quite easily” even when the model is just using a bunch of heuristics, and very far away from having a coherent world model. Of course, I understand the results in Tables 1 and 2 are interpreted as evidence that these metrics are tracking the desired concepts. But I do think deeper discussion is required on why this intuition is warranted, and what these metrics in particular add to the picture. For example, on the gravitational orbits experiments, the authors also turn to symbolic regression to elucidate whether the model can or cannot be understood as comprehensively applying the generating laws, and this seems like a much more straightforwardly interpretable result.

On a similar note, my understanding is that the calculated metrics only provide potentially interesting information when the states used to compute them are the real states used to generate the data. This of course reduces the direct applicability of this technique in cases of particular importance, like the LLM-related examples which the authors present as motivation. The technique might still be useful in several contexts or more indirect ways, but I’d like to see more explicit discussion of them -- otherwise the reader might be led to believe they don’t exist.

The settings the authors choose for their experiments make sense, but my understanding is that they are not necessarily an important contribution: we don’t really care that much whether a specific architecture, run on a setting with a specific encoding, does or doesn’t recover a particular functional form. Rather, they serve mostly as exemplifications and explorations of the use of the proposed metrics, which are indeed the main contribution (and are ultimately aimed at applications to practical models of the kind referred to in the opening paragraph).

The observation in Section 4.3 that models reconstruct the board well enough to match legal moves, but not perfectly, is very interesting, and hints towards some frugal, partial construction of a world-model shaped by the immediate training incentives. Especially since this is so interesting, it would have been useful to include in the main text a more detailed discussion on what it could mean, as well as possibly point to empirical follow-ups in settings other than Othello. (Such an addition is not possible at this stage). 
Finally, I also have some major reservations about mathematical presentation and writing, which I present below.

### Questions
I start with some other major conceptual considerations:

The mathematical presentation in Section 2 seems convoluted and unclear.
If my understanding is correct, it can be easily proven that Definition 2.1 is equivalent to a very simple mathematical property: m decomposing through /phi (in the support of P). That is, the existence of a function f such that m = f o /phi. Stating this explicitly as the definition would be easier for the reader, as opposed to going through s*. On a similar note, the name “inductive bias towards state” seems like a strange one for this property, especially because it sounds quantitative (L could have more or less inductive bias) when the definition is in fact binary. It would seem better to call the definition “L learns functions of state” (or something like that), and reserve discussions of inductive bias for the latter quantitative versions.

If my understanding is correct, it can be easily proven that Definition 2.2 is equivalent to another very simple mathematical property: the fact that the function f from the previous definition is not injective. This again is easier to understand. Here again the name doesn’t seem as representative as it could be. To me, it would seem more intuitive to name the positive property (f being injective) as “L fully uses state” (or “fully separates states”, or something like that), and then refer to the negation as “L doesn’t fully use state”.
In fact, these names seem not only like suboptimal choices, but also possibly misleading. Consider, for example, a learning algorithm L that, for any dataset D, creates a model m which maps every input to a single constant output. This would satisfy Definition 2.1. Yet it seems misguided to say that this useless L has “inductive bias towards state”. I think similarly counterintuitive edge cases exist for Definition 2.2.

I understand you might want to introduce other terms, like s*, to make your quantitative definitions in Section 2.1 possible. But in any event this should come in Section 2.1, after the simple binary definitions are transparently expressed. Although I also suspect there could be cleaner ways to phrase them that become obvious once you rewrite Definitions 2.1 and 2.2 as above, or even better quantitative definitions altogether.

On a different important note, in several places the authors mention that this paper studies whether a “learner” has a world-model, which sets the work apart from more extensive existing work on whether a fixed model has learned a world-model. Nowhere in the text is it particularly clear what they mean by this, but my interpretation is that their metrics are defined for learning algorithms L (plus distributions over data Q, etc.), as opposed to a single learned model m. If this is indeed the motive for their words, then I’m not sure this really grants a substantive distinction, or sets the work apart from other work in an important way. The reason is that the interesting parts of their definitions all pertain to a single model m, trained on a single dataset D. And then, they simply average in a certain way over datasets D to come up with a metric for the whole learning algorithm L. While this is a natural step, it doesn’t seem like a substantive contribution, and I would have appreciated more thorough discussion of how this new level can open new possibilities for the study of world-model construction.

On another note, Section 3 mentions that (for the models trained on the general dataset as opposed to the narrow slices) the law recovered through regression is not the generating one, and this implies that “the model extrapolates based on piecemeal heuristics; it constructs different laws for different sequences”. This implication doesn’t seem justified enough in the main text. Most notably, how do the authors know that the reason regression finds the wrong law is that “the model constructs different laws for different sequences”, as opposed to something like, “the model constructs the same law for all sequences, but it is simply the wrong law”? The fact that training on narrow slices does recover the correct law doesn’t seem to imply the former over the latter. I can imagine that through experimentation, or also through observing the next-token performance of these models, the authors have developed robust intuitions about which of the two is happening. But if so they are not sufficiently transmitted in the main text.

Now a less important conceptual consideration:
Given your observation that models trained on the general dataset for Orbital Mechanics don’t recover the correct law, it would be positive to include some discussion of the extent to which such architectures can computationally reproduce such laws. That is, the extent to which this failure is due to inductive training bias, or to fundamental limitations of the computational architecture. I understand state-trained models provide some (possibly conclusive) evidence in the direction of “the model architecture can perfectly compute the correct law in a forward pass if the learned model is the correct one”. Or maybe it is obvious that the architecture can implement this computation, or some existing literature has studied this in-depth. But I would have benefitted from making this explicit.

Finally, some stylistic points:
In a few places (mostly the introduction), the authors mention they study world-modelling capabilities along two distinct dimensions: “inductive bias towards state” and “recovering of state”. Of course, these terms refer to Definitions 2.1 and 2.2, but their intuitive meaning was not at all clear to me from reading just their short descriptions in the introduction (and not even immediately upon reading the Definitions, as I’ve explained above), and again I believe they could be made immediately precise by just using the right words: whether the learned model decomposes through states, and whether it makes use of all state distinctions.

In a few places the authors mention new functions (for example, “how much do new functions depend solely on state versus non-state functions of input?”), but to my understanding these “new functions” are simply “the learned model”, and should better be called that.
It seems unnecessary to introduce the variable L, since m\hat ( · ; · ) can already be seen as the learning algorithm, which provides a learned model m\hat( · ; D) for every dataset D, which provides an output m\hat(x ; D) for every input x.
(If for some reason the authors don’t want to incorporate this change, then at least they should introduce the variable L earlier, when the term “learning algorithm” is introduced.)

The variable you introduce for the state space is /Phi, but you later use \mathcal{Q}, for example in equation 1 and Definition 2.2.
Definitions 2.1 and 2.2 depend on /phi, and this should be made explicit in their names (for example, “inductive bias towards state /phi”).
The quantitative metrics should be definitions, since they are more central to the paper (or non-trivial) than the binary definitions 2.1 and 2.2.

A large value of IB(Q), that is, a high “inductive bias towards state”, indicates that the learned model cannot be well-approximated as decomposing through state. This is intuitively backwards: a high “inductive bias towards state” intuitively corresponds to the model being likely to behave in terms of those states, and not the other way around.

I understand that the function /phi is supposed to be the “real” state function throughout, meaning the one actually used to generate the data. This is especially obvious in the experimental sections, but should somewhere be mentioned explicitly, especially because otherwise the definitions in Section 2 don’t necessarily have the same intuitive meaning or motivation that you discuss.
In a couple places, you introduce the Orbital mechanics setting with the sentence “The true world model is the world”, meaning, of course, that the data is generated from Newton’s law, and this is a physical law that approximately describes the real world. But I find this sentence doesn’t add anything, adds unnecessary pomp, and in fact slightly misleads: my first reaction to such a sentence (especially given your motivating examples with GPT-2) was that you would have found a way to extract world models from “messy, complex, real-world data” (like GPT-2’s training corpus). But that is not the case, and your use of Orbital mechanics as an experimental setting is not necessarily different or more interesting than other latent-function-approximation tasks.

Probably the footnote of Figure 1 should quickly mention how these laws are extracted from model behavior, which is, of course, through symbolic regression.
Finally, there are numerous infelicities or mistakes in the text, and I present here just a few representative ones:
- First sentence in the introduction is awkwardly phrased
- End of page 1: “studied by studying”.
- The introduction seems too short to make some of the ideas clear (see especially my comment above about the descriptions of “inductive bias towards state” and “recovering state”).
- When defining what it means for a dataset D to be consistent, you say “with_then_”, which should instead be either “if_then_” or “with_we have_”.
- Introducing /epsilon is probably not necessary.
- Right before Section 2.1, you say “s* has an inductive bias towards state”, which should be “L” instead.
- Before equation 3: “for any chosen distribution over Q over dataset D”.
- “Build multi-task learner to model extrapolations” -- typo in first sentence of this paragraph
- “A symbolic regression is a method…” typo in this sentence”
- “piece-meal” -- inconsistent use of hyphen
- In the reproducibility statement: “All other datasets used in the paper already publicly available.”

### Soundness
2

### Presentation
2

### Contribution
2
