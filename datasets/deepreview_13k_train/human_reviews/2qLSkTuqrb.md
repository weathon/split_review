# Translating cognitive models into neural and statistical descriptions of real-world multi-agent foraging behavior

- Decision: Reject
- Scores: 5, 3, 6, 5

## Abstract
Foraging is a multi-agent social behavior that has been studied from many perspectives, including cognitive science, neuroscience, and statistics. We start from a specific type of cognitive description -- agents with internal preferences expressed as value functions -- and implement it as a biologically plausible neural network. We also present an equivalent statistical model where statistical predictors correspond to components of the value function. We use the neural network to simulate foraging agents in various environmental conditions and use the statistical model to discover which features in the environment best predict the agent's behavior. Our intended primary application is the study of multi-species groups of birds foraging in real-world environments. To test the viability of the statistical approach, we simulate bird agents with different preferences, and use Bayesian inference to recover what each type of agent values. In the multi-agent context, we investigate how communication of information about reward location affects group foraging behavior. We also test our modeling technique on a previously published locust foraging dataset (Gunzel et al., 2023). After evaluating the effectiveness of our method on both synthetic and previously published data, we analyze new multi-agent foraging bird data we captured through high-resolution video recordings. Our method distinguishes between proximity preferences of ducks and sparrows within foraging groups. This analysis framework provides a principled, interpretable, and parametric approach for reasoning about how birds' preferences relate to their decisions about where to move in a complex multi-agent environment.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes computational and implementational descriptions of foraging multi-agent behavior, employing a cognitive model, a neural network model, and a statistical model. The main focus lies on modeling groups of birds in the real world. They simulate behavioral trajectories based on the neural network model and show that proximity and trace can be inferred using Bayesian inference. Finally, the methodology is applied to a locust foraging dataset, revealing differences in proximity preferences among species.

### Strengths
The topic of explaining foraging behavior in real-world environments is both intriguing and relevant, contributing to the understanding of animal behavior.

The paper strives to bridge the gap between computational and implementational aspects of behavior, providing a comprehensive view.

The use of a real-world dataset to validate the proposed methodology adds value to the research, demonstrating its practical applicability.

### Weaknesses
In general, I found the main point of the paper difficult to grasp and I am still a bit unclear about this. There are different proposals, including different models and their relations, simulated data based on the neural network model, and inferred parameters for the real-world dataset. The experiments as far as I understand only show the relevance of the cognitive model. The implementation as a neural network is used but I would assume that differently designed implementations would yield the same results. So while the implementation may be biologically plausible, it seems to lack concrete evidence to support this type of implementational model if this is what the authors want to claim.

Further, I found section 2.2.2. somewhat unclear in what was done exactly. Do they propose a model and simulate it or do they infer quantities of the model? I did not completely get this from the section but according to the abstract, it seems that Bayesian inference is applied.
For example the sentence "However, some birds also update their expected reward vector at the locations of other birds [...]" could be interpreted in multiple ways, and it's not clear if some birds are modeled differently or if this behavior emerges from uniformly modeled birds. I think the paper would benefit from stating more clearly what was done and what the message of the paper is.

I would also be very careful with formulations such as "When animals decide what action to take, they sample their local environment" or "An animal at state S perceives not only the current state [...]". While these models are often employed in the study of animals, it is unclear whether they represent the actual mechanisms at play in real animals.

### Questions
1. What is the primary contribution of the paper? Is it the introduction of different models, the exploration of their interrelations, or the approach to parameter inference? Do the experiments effectively validate this contribution?

2. For the real-world dataset, has the accuracy of your model been measured? It would be beneficial to see a comparison between the simulated behavior and actual data. While inferring different proximity preferences among species is interesting, it doesn't provide insight into how well the model fits the data.

3. When computing posterior distributions of the parameters, the model requires a stochastic component. How is the stochasticity of the agents modeled, particularly when the policy in the model appears deterministic?

### Soundness
2 fair

### Presentation
1 poor

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
The paper reports on birds and other social species’ foraging behavior in groups. It models three main behavior types, random motion, following food gradients, and following conspecifics.

### Strengths
Refreshing and interesting read about social bird foraging behaviors, their individual differences, and general background. 

Appealingly simple models of individual species behavior. 

The paper shows that the inference of simple behavioral patterns is possible – at least on the simple level parameters are identifiable.

### Weaknesses
The paper reports on birds and other social species’ foraging behavior in groups. It models three main behavior types, random motion, following food gradients, and following conspecifics.

### soundness:
2 fair

### presentation:
2 fair

### contribution:
2 fair

### strengths:
Refreshing and interesting read about social bird foraging behaviors, their individual differences, and general background.

Appealingly simple models of individual species behavior.

The paper shows that the inference of simple behavioral patterns is possible – at least on the simple level parameters are identifiable.

### weaknesses:
The paper does not really have anything novel to offer – or this novelty is at the moment fully hidden. It just reports on how one can generally model multi-agent foraging behavior with very simple techniques. I fully miss any true novelty.

The paper does not really offer any insights. Such as which model may work better to model social foraging behavior etc. There are no ablations etc. The lack of comparison to existing models or standard baselines in the field of foraging behavior makes it difficult to assess the actual contribution of the proposed model. For instance, how does the model's performance compare to a simple proximity-based statistical model, particularly in the context of the duck and songbird observations?

The utility of the presented results is minor. Figure 2 and 3 report performance on simulated data. Parameter identifiability is confirmed, which is good, but also not overly surprising. The actual techniques are reported in the appendix. The results in Figure 3 are summarized but not interpreted. What is the insight of this? Specifically, how does the ability to discriminate between communicating and non-communicating groups translate into a deeper understanding of foraging behavior? Furthermore, the claim that communication improves foraging success, while intuitive, needs more rigorous empirical support beyond simulated data.

Results in 2.3.1 report on the ability to infer that locusts communicate about food locations (or just observe others consuming food – thus tending to look close-by?). The brevity of the paragraph suggests no interesting insights there. A more detailed analysis of the locust data, potentially integrated into the main paper, could provide a more compelling case for the model's ability to uncover communication patterns in real-world scenarios.

Results in 2.3.2 report that ducks and small song birds tend to keep other distances to each other, which is also hardly surprising.. and could probably even be measured simply by a summary statistic – a comparison would be necessary to verify that modeling individual foraging decisions is useful here. The tracking technique is also not part of the contribution. Moreover, Figure 4 lacks clear labeling (4A, 4B, 4C, 4D) as referenced in the text, making it difficult to follow the analysis. The right side of Figure 4, which appears to present inferred posterior distributions, is not adequately explained. Clarifying whether this data is derived from real bird observations or simulations is crucial.

In general, the evaluations do not sell well. I am left puzzled with what your model now really can show – particularly in relation to other models. Ablation studies or baseline models / standard models in the literature on foraging behavior would need to be offered in comparison to your model to enable judging the quality of your model.

Key techniques used – whether novel or just important to succeed in modeling the foraging behavior – remain fully obscured.

### questions:
Note that inverse RL is much older than the work in 2019 that you cite. In this respect the authors write about information that is inferred from other birds… I think it would be useful not to talk about “amounts” of information but “types” of information (like can they distinguish feeding from just moving around sitting etc… or can they just infer the mere presence of other birds?

Your notation in 2.1.1 only considers model-based RL. I would expect that most birds act habitually in a rather model-free manner – as do your policies I believe? The current formulation of the model appears to be overly simplistic, especially considering the complex cognitive abilities of birds. The assumption of a single-step successor representation followed by a winner-takes-all action seems to underestimate the potential for more sophisticated decision-making processes. Exploring alternative policy structures, such as those incorporating elements of model-free RL or hierarchical planning, could significantly enhance the model's realism.

The neural description then is rather reactive it appears. At least a general appeal to the established fact that brains appear to rather implement generative models (and habitual behavior routines within) would be recommendable.

2.2. How are sensors / strategies / ANN models encoded? At least general intuition about this in the main text would be useful, I think. Providing more details on the encoding of sensors, strategies, and ANN models within the main text would improve the paper's clarity and accessibility. Specifically, how are the sensory inputs represented, and how do the agents decide on their actions based on these inputs?

### Questions
Note that inverse RL is much older than the work in 2019 that you cite. 
In this respect the authors write about information that is inferred from other birds… I think it would be useful not to talk about “amounts” of information but “types” of information (like can they distinguish feeding from just moving around sitting etc… or can they just infer the mere presence of other birds? 

Your notation in 2.1.1 only considers model-based RL. I would expect that most birds act habitually in a rather model-free manner – as do your policies I believe?

The neural description then is rather reactive it appears. At least a general appeal to the established fact that brains appear to rather implement generative models (and habitual behavior routines within) would be recommendable. 

2.2. How are sensors / strategies / ANN models encoded? At least general intuition about this in the main text would be useful, I think.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this work, the Authors study multi-agent foraging and using various real and simulated data. To this end, they’ve developed a framework that encompasses reinforcement learning, cognitive priors, and statistical description. The Authors tested their framework on synthetic data and then applied it to two datasets on avian foraging: an existing one and a new one that they’ve collected. Their framework has allowed them to confirm previous observations on the existing dataset and to characterize the difference in foraging of various avian species in their new dataset.

### Strengths
The goal of the paper is highly important and interesting to the computational neuroscience community. While foraging has been an objective of studies since the 70s, recently its focus has moved from lab experiments to (more) naturalistic behaviors of (groups of) animals interacting in the wild (or almost wild) conditions. In that regard, a computational framework to analyze data from such experiments is timely.

The Authors in this paper aimed to build a unified framework spanning several levels of analysis (i.e., cognitive, network, and algorithmic levels), which, I think, is especially important in the field of foraging because conventionally different levels of analysis were treated separately in the field.

The paper describes a new dataset and lays out the plans to collect more data using an even better technology. This is doubly valuable because new data will allow these and other researchers to test their models of foraging, and also, should additional data be needed to test new hypotheses, the Authors do have a set up framework in place to record such data.

The research is perfectly structured starting with the framework that unifies different levels of analysis, then using synthetic data to validate the framework, later applying the framework to existing data and reproducing the findings in a principled manner, and, finally, introducing new data and obtaining new knowledge off of it.

### Weaknesses
I have three small concerns/suggestions. They are intended to suggest some additional analyses, either for the time of the rebuttal (time permitting) or for future research.

First, while the network level of analysis proposed here is indeed biologically plausible, there are no direct links to or mapping onto the brain at this point. An interesting future analysis may involve trying to establish such a mapping (although I do acknowledge that it’s an extremely difficult task if one would like to go beyond high-level similarity). Some prior works have proposed models of how RL models may map onto the brain structure (e.g. see https://www.cell.com/trends/neurosciences/fulltext/S0166-2236(12)00071-9 and https://www.sciencedirect.com/science/article/pii/S0893608002000473 ). It would be interesting to see how the weight matrices proposed in the current work would map onto these previous models and/or onto the brain in general).

Second, the study uses handcrafted features (“proximity”, “trace”) to classify behaviors into handcrafted classes (“random”, “hungry”, “follower”). While both the features and the classes considered here do make sense and are rooted in existing literature, they may mismatch the features and behavioral classes used by the animals and may end up being not expressive enough to describe the observed behavior. A possible way to account for that on the behavioral side is to build a low-dimensional representation of (all available) behavioral readouts and to run any (unsupervised) clustering algorithm on it (e.g. see https://www.cell.com/current-biology/pdf/S0960-9822(17)31604-4.pdf and references therein). On the feature side, a possible strategy is to train an RL model on all available inputs (and/or history thereof), then distill/deduce the relevant (parsimonious) variables (e.g. see https://proceedings.neurips.cc/paper/2020/hash/da97f65bd113e490a5fab20c4a69f586-Abstract.html )

Third, and maybe that’s something I’ve overlooked, but, to my understanding, in the proposed model, as it currently stands, the communication between animals is modeled as a scalar spanning the range from 0 (no communication) to 1 (full reliance on communication). At the same time, animals may transmit signals of different content (e.g. food location vs food quantity); their reliance on the signals of different content may vary (e.g. paying attention to the food location but not to the quantity), and such reliance may be different across species. It looks like this is something that can be analyzed within the existing data and may strengthen the results by discovering the content of the messages passed and received by different species.

While I think that the paper in its current standing is interesting and relevant, updates along the directions outlined above may further expand the scope of the results and strengthen this work.

### Questions
Minor comments:

-Page 2. When referencing “Reinforcement learning agents perform well in a variety of foraging-related tasks”, the Mnih et al ATARI paper is perhaps irrelevant, however, https://link.springer.com/article/10.3758/s13415-015-0350-y would offer good support for the cause.

-Would you consider running your model on mouse data? It would be interesting to see how rodent foraging is different from avian foraging. Hopefully, these differences, combined with the overall knowledge of the conditions that the respective species are exposed to, would provide us additional information on the ways the environment shapes foraging strategies.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors posit that foraging can be expressed as a value-maximizing behavior, where the agent choses the action that maximizes value, i.e. discounted sum of future rewards (for an adequate reward function and transition matrix).

They then show that this strategy can be implemented by a neural network (with some added machinery), and captured by a statistical model based on hand-crafted predictors. IIUC, the hope is that the neural model may possibly guide neurobiological investigations, while the statistical model can be fit to real-world data and provide explanatory power.

As a demonstration, they fit the statistical model to data from both simulated and real-world data, including, apparently, a completely new dataset. The model seems able to capture and differentiate underlying structure in the agent's behaviors.

### Strengths
- The methods seem novel.

- The resulting model(s) seems promising

- The application of the statistical model to real-world data is interesting, and seems to provide some information.

- Basically, the scientific content, as far as I managed to understand it, seems interesting and potentially valuable.

### Weaknesses
 - The paper is clearly unpolished and, frankly, unfinished. The description is extremely confusing and incomplete (see below). It took me a lot of time to understand what the paper was trying to do. (I'm still not sure I got it). More pressingly, it seems impossible to replicate the proposed method from the inadequate description provided in the paper.

- Simply understanding what the authors try to do exactly is a challenge, because the explanation of the various parts of the method are split into multiple parts (and the Appendix), The authors don't explain what they call a "cognitive", "neural" or "statistical model" until page 4, in the Results.

- The introduction and discussion are very lengthy and philosophical, while the figures are absurdly small and the description of the methods either inadequate or just plain missing. The most basic explanation of what is actually going on is largely pushed to the Appendix. Even then, the explanation is not sufficient to reproduce the method. See Questions, below.

- p.4: "f_i are predictors" - what's a "predictor"? A function? Is it linear? Monotonic? The paper lacks a clear definition of these predictors, making it difficult to understand the statistical model. Are these basis functions? What is their functional form? Are they fixed or learned? The lack of specificity makes it impossible to assess the model's validity.

- The successor representation is described as "Discounted expected occupancy" - but this is notoriously policy-dependent. Instead, the authors actually base theiur successor representation M on the iterated transition matrix (action-independent, IIUC). so it's really a distance function! (it might be understood as "occupancy under random policy"). The paper does not clarify the implications of using a random walk policy for the successor representation and how this choice impacts the model's ability to capture goal-directed behavior.

- In the neural model, is M specified by hand or is it learned ? Appendix A.1 seems to indirectly imply that it is learned (whereas it is fixed for the statistical model) - but how? The paper does not provide sufficient detail on how the successor representation is implemented in the neural network. Is it a fixed matrix, or is it learned through some form of Hebbian plasticity? The lack of clarity hinders the assessment of the neural model's biological plausibility.

- The statistical model is only described in the Appendix (and even so inadequately, see below). Before seeing the appendix, we have no idea what predictors are being used, what coefficients are, etc. Yet these are constantly referred to in the rest of the text, and indeed constitute the main target quantities in the experiments! This is clearly not workable. The core components of the statistical model, namely the predictors and coefficients, are not introduced until the appendix, making it impossible to understand the results in the main text. The paper needs a clear and concise description of the statistical model in the main text.

- At no point is the statistical model clearly explained, with a clear description of all the predictors and coefficients and of what, exactly, is fit to the data as opposed to being hand-provided. The paper fails to provide a clear distinction between the parameters that are fit to the data and those that are hand-specified. This lack of clarity makes it difficult to evaluate the model's ability to generalize to new data.

- The authors simulate "hungry, follower and random" birds. How? (It's briefly discussed in the Appendix, which is not referred to in the main text). The simulation details are relegated to the appendix and not properly introduced in the main text, making it difficult for the reader to understand the experimental setup. The paper needs a more comprehensive description of the simulation parameters and procedures in the main text.

- As another example of the inadequate description, it is impossible to get a clear picture of what the proximity function (which is fundamental to the method)  actually looks like. How are the two sine waves and the exponential combined? The description of the proximity function is vague and lacks the necessary details for replication. The paper needs to provide a clear mathematical formulation of the proximity function and how the different components are combined.

- In 2.2.2, where the estimated values of certain parameters are reported, it doesn't tell us what is the true value of the parameters! The results show 0 effect of "food trace" in the communicators' case, and 0 for proximity in the non-communicators. Is that true in the simulation? That is not mentioned in the text.

- What is a "maximum projection of thermal images"? The term "maximum projection of thermal images" is not clearly defined, and the paper needs to provide more context and explanation for this data processing step.

- Figure 4 shows that various values of the preferred proximity parameter give rise to different fitted estimations for the proximity coefficient. This seems to be a very cumbersome way to approximately recover the true underlying proximity-preference function, which could probably better be done with a different parametrization (E.g. a polynomial times decaying exponential, which would allow the model to fit both the peaks and troughs of the proximity function with only a few more additional parameters?)

- Generally, in the figures: "Top", "Bottom", "Left", "Right" is not sufficient (especially in combination). Label individual subplots with letters and reference these in the caption.

### Questions
- p.4: "f_i are predictors" - what's a "predictor"? A function? Is it linear? Monotonic?

- The successor representation is described as "Discounted expected occupancy" - but this is notoriously policy-dependent. Instead, the authors actually base theiur successor representation M on the iterated transition matrix (action-independent, IIUC). so it's really a distance function! (it might be understood as "occupancy under random policy")

- In the neural model, is M specified by hand or is it learned ? Appendix A.1 seems to indirectly imply that it is learned (whereas it is fixed for the statistical model) - but how?

- The statistical model is only described in the Appendix (and even so inadequately, see below). Before seeing the appendix, we have no idea what predictors are being used, what coefficients are, etc. Yet these are constantly referred to in the rest of the text, and indeed constitute the main target quantities in the experiments! This is clearly not workable.

- At no point is the statistical model clearly explained, with a clear description of all the predictors and coefficients and of what, exactly, is fit to the data as opposed to being hand-provided.

- The authors simulate "hungry, follower and random" birds. How? (It's briefly discussed in the Appendix, which is not referred to in the main text).

- As another example of the inadequate description, it is impossible to get a clear picture of what the proximity function (which is fundamental to the method)  actually looks like. How are the two sine waves and the exponential combined?

- In 2.2.2, where the estimated values of certain parameters are reported, it doesn't tell us what is the true value of the parameters! The results show 0 effect of "food trace" in the communicators' case, and 0 for proximity in the non-communicators. Is that true in the simulation? That is not mentioned in the text.

- What is a "maximum projection of thermal images"? 

- Figure 4 shows that various values of the preferred proximity parameter give rise to different fitted estimations for the proximity coefficient. This seems to be a very cumbersome way to approximately recover the true underlying proximity-preference function, which could probably better be done with a different parametrization (E.g. a polynomial times decaying exponential, which would allow the model to fit both the peaks and troughs of the proximity function with only a few more additional parameters?)

- Generally, in the figures: "Top", "Bottom", "Left", "Right" is not sufficient (especially in combination). Label individual subplots with letters and reference these in the caption.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
