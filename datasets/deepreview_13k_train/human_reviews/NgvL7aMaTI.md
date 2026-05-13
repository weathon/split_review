# Predicting episodic structure from overlapping input in binary networks with homeostasis

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
How neural networks process overlapping input patterns is a fundamental question in both neuroscience and artificial intelligence. Traditionally, overlaps in neural activity are viewed as interference, requiring separation for better performance. However, an alternative perspective suggests that these overlaps may encode meaningful semantic relationships between concepts. In this paper, we propose a framework where persistent overlap between episodic patterns represent semantic components across episodic experiences, and the statistics of these overlaps how each semantic concept relates to others.

To explore this idea, we introduce an Episode Generation Protocol (EGP) that defines a mapping between the semantic structure of episodes and  input pattern generation. Paired with our EGP, we use Homeostatic Binary Networks (HBNs), a simplified yet biologically-inspired model incorporating key features such as adjustable inhibition, Hebbian learning, and homeostatic plasticity.

Our contributions are threefold: (1) We formalize a link between episodic semantics and neural patterns through our EGP. This EGP can be used for systematic study of semantic learning in artificial neural networks. (2) We introduce HBNs as an analytically tractable network that extracts semantic structure in its internal model (3) We show that HBNs align their performance with Maximum A Posteriori and Maximum Likelihood Estimation strategies depending on the homeostatic regime. Similarly, we provide an example of how our EGP can be used as an experimental protocol in neuroscience to make different models of learning compete.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The literature suggests the overlap in neural activity as a separation of meaningful semantic concepts, where the overlap is defined to be between episodic patterns. The literature proposed here considers activity patterns to correspond to the full content of episodes, and the overlaps between patterns represent common concepts in the episodes encoded by both patterns. Thus, the Episode Generation Protocol (EGP) system is introduced to map the semantic structures of episodes to input pattern generation. By using the inputs produced by the EGP, the literature uses a Homeostatic Binary Network as a method to train and recall episodes. These are motivated by the fact that the trained network will be capable of recalling even if the episode has concepts that are overlapping towards other attributes due to the semantic structure provided by the EGP.

### Strengths
The idea of using a semantic structure to define episodes based on a structure of concepts and attributes is great. What I really like about the paper is how this structure is used to train a network for recalling patterns, which points its focus towards the structure of the input rather than training the network to learn. This key idea is novel.

### Weaknesses
I do understand that some of the technical details to appendix helps shorten and simplify the explanation in the main text. I believe some of them are way too shortened on formal explanation and way too lengthened on an intuitive explanation, e.g. key concepts such as explanation of EGP is good but it would benefit from having explanations such as how the episode is mapped to an input would help. Another thing to note here is that instead of giving an intuitive explanation, it would be better to connect a formal explanation to some extent that refers to both the appendix and an intuitive explanation would provide a better understanding of the topic.
Section structured for 2 is confusing. I find the methodology and results to be mixed. The issue with the section is it is difficult to understand the motivation of the paper and its concept if I have not read the paper fully. I believe the paper would benefit if these are laid out in the methodology with the results (probably 2.4 and 2.5?) in a separate section. The issue mainly persists in the methodology part of it.

### Questions
Figure 1C (middle): I believe that the probability for the attribute relation between italy and pizza may have an error? (should be 0.25?)
I do understand that to add some extra variability, $N_swap/2$ neurons are swapped active neurons with the inactive neurons. What does $N_swap$ in this case?
A.1: During explanation of eq (11),  does ‘a’ here represent an episode concept? Since an episode contains one episode concept per episode attribute, A is an episode attribute and thus ‘a’ is one episode concept rather than ‘a’ being a set of episode concepts. This may need clarification.
A.2 The definition of i is a population of associated neurons as SEN_a as per episode-input mapping. Here, you define it as an episode concept? I believe the terms here need to be further clarified since it is very confusing.
A.3.1: The definition of satellite objects and its relation to its features is key here. This needs to be cleared out to better explain the readers on EGP.
Consider explaining the input mapping at the start. In my opinion it seems unclear until after going through the appendix.
Section 2.2: The definition of top-K activation should define what region specifically means (neurons associated to attribute?)
Although the experiment shown here considers a short episode, I would also evaluate its performance on longer episodes (with more swaps) and consider how this system may perform.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a method to encode the statistics of episodes in a memory network composed of binary units, connected with weights whose dynamics include Hebbian learning, homeostasis and synaptic depression. The first contribution is a method to  generate binary patterns encoding some semantic relationships defined as conditional probabilities on some finite space composed of concepts grouped in supersets called attributes (both constituting the episodes). The generation procedure consists of sampling the given concepts (one per attribute) and encoding them in a disjoint population of neurons. The network is then trained using some bespoke mechanisms for activity and synaptic homeostasis. The authors show how this process recovers the original semantic structure (defined as the conditional probabilities of concepts), performs pattern completion of concepts subject to noise; and claim that this process performs statistical estimation of missing or corrupted concepts in a given episode. They also present some mean field theory for the weights.

### Strengths
The paper shows an elegant reinterpretation of the semantic structure in episodes to be stored in memory. There are a variety of analyses that show the different, claimed results while keeping the explanatory complexity to the minimum. This makes this an attractive potential scientific theory that is interpretable from the beginning. The different mechanisms of the neural network are explained and length. The simplicity of the model is attractive but could be misleading in ways that I will explain later. I congratulate the authors for a great work, and the comments that follow are intended as my contribution to make this work stronger.

### Weaknesses
I will expose my concerns in no particular order:

- I am worried about the lack of explanation about what K is (I mean, the actual value). It seems to be the size of each of the groups that encode the concepts. In this sense, this might be very restrictive to make this model useful. I imagine that, if K < N, the pattern completion might not work as expected. It would be useful to show how the model behaves for different Ks
- I don't think the model contradicts Gastaldi et. al (2021). You still have a minimum amount of noise (which I interpret as the overlap), above which, the network can not recover. In this sense, I am not that sure the two schemas shown in figure 1A and 1B are that different, it seems that we have just renamed what the overlap is buy making those overlaps atomic units. This might be too strong of a constraint on the whole model, limiting the scalability. The model's reliance on disjoint neuron populations for each concept, while simplifying analysis, may not reflect biological reality and could severely limit the model's capacity to handle more complex, overlapping semantic representations. This approach essentially predefines the semantic space, rather than allowing it to emerge from the data itself. The model's ability to handle situations where concepts are not neatly separable into disjoint groups is unclear.
- Regarding scalability, the simplicity of the exposition leaves some doubts about how much the model is able to scale (and therefore be of any scientific or engineering use), both in the complexity of the semantic structure (nested relations, higher order correlation?) and the complexity of the patterns (would that support different encodings). The model's architecture, with its reliance on binary units and fixed-size concept encodings, raises concerns about its ability to scale to more complex semantic structures. The model does not address how it would handle nested relationships or higher-order correlations between concepts, which are common in real-world scenarios. Furthermore, the use of disjoint neuron populations for each concept may limit the model's ability to represent nuanced or overlapping semantic relationships.
- I have doubts about the strength of the conclusions drawn from the work in general, It is clear that the authors have a strong grasp of mathematics, however, I see no justification about the importance of each of the different mechanisms in achieving the ultimate result (homeostasis, depression). Even more, it seems that the Hebbian rule plus the top-K activation would unavoidably compute the covariance matrix of the input! (XX^T_ij = sum(d*xidxj))
- Connected to this, some of the mechanisms are not well justified, why is homeostasis and depression important? I suppose it is the renormalization of the weights but the theoretical justification (necessity and sufficiency) are week. The specific form of homeostasis and synaptic depression implemented in the model lacks clear justification. While these mechanisms may contribute to weight normalization, the paper does not provide a strong theoretical argument for why these particular forms are necessary or sufficient for achieving the claimed results. It is unclear if other forms of normalization could achieve similar results, or if these specific mechanisms are crucial for the model's performance.
- The mean field analysis is interesting but also confusing. First, there is no coherent naming of the variables (sometimes Tout, Tpre), second it is not clear what the contribution to this analysis is to the full narrative of the paper (I can see the paper without the analysis and it would not change the end result). More on this later.
- There are a fair amount of typos in notation and in the text in general
- Figure 4 shows only 2 concepts for the attribute food but the caption says it is 4?
- Labels are wrong in figure 5D
- I disagree with the network performing MLE or MAP, or at least this claim should be qualified. Indeed, the model seems to oscillate! so, when do you know when to stop?
- Finally, a general comment. It would be nice to have a discussion about how plausible this model is based on what is known from the structure of memory.

In general, I am unsure about the relevance of the work in the context put forward by the authors.

### Questions
- One of the properties of episodic memory is the ordering of events and creation of chains. It is not immediately clear to me how this could be implemented (is, I think, what differentiate the problem from mere pattern completion/storage). I suggest including an experiment in this regard as your results (in order to justify calling it episodic, and to show that the model agrees with observations from the literature)

- The mean field theory seems to assume that the neurons are tracking the input statistics perfectly. I do not think you show that in the first place. The probability distribution you derive also seems to assume independence and disconnected neurons. Can you show this is a valid assumption, what are the implications of this assumptions for the rest of the claims of the paper.

- I did not see the phase transition in the weights that you mentioned explained in detail.

- The behaviour of the weights for the regimes with homeostasis does not seem to apply to the model (the dynamics are never reaching this regime). Can you explain your reasoning in more detail?



-

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes an Episode Generation Protocol (EGP) to generate vectors of binary numbers (each vector is an “episode”) such that every episode contains one concept per episode attribute. As a clarifying example, the authors consider the attributes to be place and food, and the concepts to be Italy, France, pizza, and croissant. The overlap between different binary episode-vectors is a key feature of these synthetically generated episodes and corresponds to shared concepts across episodes. The authors study how these episodes are learned by a model that includes adjustable inhibition, Hebbian learning, homeostatic plasticity, and short-term synaptic depression; and then study how these episodes are recalled from noisy inputs (pattern completion).

### Strengths
The authors propose a neural network model that touches on many areas of research across both biological and artificial systems. They write about its ability to perform pattern completion, Maximum A Priori Estimation (MAP), and Maximum Likelihood Estimation (MLE); while doing this with biologically inspired elements such as adjustable inhibition, Hebbian learning, homeostatic plasticity, and short-term synaptic depression. Given this breadth of scope, there are many connections that could be developed to either contribute to machine learning or to a better understanding of the brain.

### Weaknesses
The paper aims to make contributions across both biological and artificial systems but, while it is a good start, doesn’t fully connect to modern machine learning or to the brain through, for example, neural or behavioral data.

On the biological side, the authors propose a model that incorporates adjustable inhibition, Hebbian learning, homeostatic plasticity, and short-term synaptic depression. Given all of these ingredients are there predictions that can be made about behavior or neural activity? Or can the model recapitulate known experimental findings? For example, the authors referenced papers by Anna Schapiro so this may be a good contact point to compare the model and experimental findings. Specifically, the model could be tested against findings related to the neural correlates of episodic memory, such as those found in the hippocampus and related structures. The current model does not seem to make specific predictions that could be tested with neural data, for example, by comparing the model's activity patterns with neural recordings during similar tasks.

On the machine learning side, the model as it is currently implemented seems more like a proof of principle. So I’m left wondering if this model can be applied to more realistic tasks or used to gain insight into modern machine learning models. Below are some suggestions.

* The authors compare the pattern completion abilities of their model to the Hopfield-Tsodyks model from 1988. How does the model connect to other more recent literature on pattern completion? For example, modern Hopfield networks. See, for example, Krotov 2023 “A new frontier for Hopfield networks” and Krotov & Hopfield 2016 “Dense associative memory for pattern recognition”. The comparison to the Hopfield-Tsodyks model is limited given the significant advancements in associative memory models since then. A more thorough comparison to modern Hopfield networks and other contemporary models of pattern completion would be necessary to assess the true novelty and performance of the proposed model.

* In the Introduction, the authors highlight an interesting distinction between 1) models where “each pattern separately represents a concept, and the overlap is a consequence of the concepts being semantically related”, and 2) models where “activity patterns correspond to the full content of episodes, and the overlaps between patterns represent common concepts in the episodes encoded by both patterns.”
My interpretation is that models in class 1 might correspond to neural networks trained on image classification datasets like MNIST or ImageNet where there is generally only a single central object in the image and the pixel values between different images encode some sense of similarity. Models in class 2 might correspond to neural networks trained on semantic segmentation where different images share common objects or “concepts” to use the terminology of the paper. Can the model in this paper be productively applied to datasets used to study semantic segmentation, and not just the toy dataset considered in the paper? Or, relatedly, can the ideas introduced in this paper be applied to networks that are used for semantic segmentation, for example, as a way of understanding the activity patterns in later layers of the network? At a more general level what I would like to see is some path forward for this model, to see the relevance on more realistic tasks. The current evaluation is limited to a synthetic dataset, and it is unclear how the model would perform on more complex, real-world datasets. The authors should consider evaluating their model on established benchmarks in semantic segmentation or other relevant tasks to demonstrate its practical applicability.

* The authors make an interesting claim that their model performs Maximum A Priori Estimation (MAP) and Maximum Likelihood Estimation (MLE). It seems to me that demonstrating this would require more work in showing the neural network recapitulates the Bayesian computation. Specifically, a more detailed mathematical analysis is needed to demonstrate that the network's dynamics truly implement MAP and MLE. It is not sufficient to simply claim that the network performs these computations; a rigorous derivation is needed to show how the network's parameters and update rules correspond to the mathematical formulations of MAP and MLE.

### Questions
Please see the previous section for a number of questions and suggestions for improving the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In their paper “Predicting episodic structure from overlapping input in binary networks with homeostasis” authors develop a new neural network, the Homeostatic Binary Network (HBN) which, through local leaning / updating rules learn to pattern complete noisy inputs. In the context of their investigations, they also develop a dataset that can construct multiple data examples from a fixed semantic relationship, by allowing for the representation of noise on top of class representations. They show that specific implementations of their model follow the principles of either Maximum A Posteriori (MAP) or Maximum Likelihood Estimation (MLE) when completing and unseen pattern.

### Strengths
The topic of Hopfield networks and other related architectures have regained in popularity in recent years, and it seems that in principle this paper might make an interesting contribution by introducing a new architecture which matches existing algorithms in performance but also allows for understanding of the networks internal mechanisms used for pattern completion. Additionally, their architecture can be configured to follow different pattern completion strategies.

### Weaknesses
I personally find that the presentation of findings and the contextualisation of finding is quite poor in this paper. I provide a detailed list of suggested changes below which I think will help to improve the author’s work.

*Major: description of their new methods*

When introducing both their dataset and their model, I think it would help the general reader if they described their methodological advancements in context of established works that readers are likely familiar with. For example, their new dataset generation methods seem to essentially code for semantic relationships in a One-Hot coding way but instead of having each feature represented by a binary, it is represented by a list of binaries, which allows the authors to add noise to the representation of concepts? If I got that right, I think an explanation like that is going to make it easier to understand what the authors do and also what is new about their methods. This is also true when introducing their network. Authors discuss the whole idea of homeostasis in great detail but do not explain how their network is different from related (but well-known) network classes. In fact, the first time Hopefield networks are even mentioned is on page 6, even though they seem very relevant to the authors introduced architecture?

*Major: contextualisation of results*

The point above leads to an additional related issue that the authors should highlight in more detail how their findings actually go beyond the existing literature. I am not an expert in this class of networks, but their task seems to be very related to tasks already used since the early days of PDP (e.g. see McClelland and Rogers, Nat Revs Neuro, 2003) but they represented each feature through a list of binaries? At the same time for their findings in networks, I am under the impression that Hopfield networks and Boltzmann machines can also be configured to use either MLE or MAP (please correct me if I am wrong about this, as that might very well be the case)? As authors do not provide a description of what they think makes their model stand out against established alternatives, I find it difficult to judge how observing this in their model is special. My hunch would be that in Boltzmann machines one would have to bring in a prior through the weights but for the paper here it is induced by the updating, but authors should really clarify this themselves in the text and not leave it to the reader to figure this out.

*Major: presentation of results*

I would recommend the following changes to make it easier to follow / interpret results:
- Clearly state how many networks you train and what the dataset structure is
- Where variances are presented (like Fig4C), state whether these are standard errors / deviations or else
- Related to the deviation in 4C, in the text you seem to be interpreting the red line in 4C (Outgoing Dom) as being significantly different from the other lines, but the plotted variance suggest they might not be significantly different?
- Generally, results plots like 4D and 5E should report standard errors and significance tests
- Fig 5E seems to be a key analysis but the figure legend does not explain what the dots or bars actually refer to? I understand that authors want to argue that under different setup the different models mirror either the MAP or MLE prediction but to support that conclusion with a figure, they should present the expected pattern under each of these inference modes and then show how each of the models looks like either of these inference modes. As states above, the similarity should ideally be test for significance.

*Minor: stylistic changes / corrections*

- The in-text references should be in brackets, i.e. (O’Reilly, 2000) instead of O’Reilly (2000). The ICLR Latex file provides this as a citation option.
- Generally speaking, across all figures, I think authors could increase the font size relative to other visual elements and could then make the figures overall smaller to save space. Additional space could be used to explain the ideas better and contextualise findings, as discussed above. 
- Figure 2B is already data / results recorded from the model, is that correct? In that case I find it confusing that it is labelled as ‘B’ and as such listed above the description of the actual network algorithm.
- Line 417: “are be asymmetric”, seems like there is an error there
- Line 303: “Now, we test whether these learnt weights can, during Test (recall) help recall during the test phase of the network.”, that sentence seems off?

### Questions
I am voting against acceptance for the manuscript in its current form but if the writing and presentation is improved substantially, as suggested below, then I think the results should be worthwhile to be presented at the conference.

*Major: description of their new methods*

When introducing both their dataset and their model, I think it would help the general reader if they described their methodological advancements in context of established works that readers are likely familiar with. For example, their new dataset generation methods seem to essentially code for semantic relationships in a One-Hot coding way but instead of having each feature represented by a binary, it is represented by a list of binaries, which allows the authors to add noise to the representation of concepts? If I got that right, I think an explanation like that is going to make it easier to understand what the authors do and also what is new about their methods. This is also true when introducing their network. Authors discuss the whole idea of homeostasis in great detail but do not explain how their network is different from related (but well-known) network classes. In fact, the first time Hopefield networks are even mentioned is on page 6, even though they seem very relevant to the authors introduced architecture?

*Major: contextualisation of results*

The point above leads to an additional related issue that the authors should highlight in more detail how their findings actually go beyond the existing literature. I am not an expert in this class of networks, but their task seems to be very related to tasks already used since the early days of PDP (e.g. see McClelland and Rogers, Nat Revs Neuro, 2003) but they represented each feature through a list of binaries? At the same time for their findings in networks, I am under the impression that Hopfield networks and Boltzmann machines can also be configured to use either MLE or MAP (please correct me if I am wrong about this, as that might very well be the case)? As authors do not provide a description of what they think makes their model stand out against established alternatives, I find it difficult to judge how observing this in their model is special. My hunch would be that in Boltzmann machines one would have to bring in a prior through the weights but for the paper here it is induced by the updating, but authors should really clarify this themselves in the text and not leave it to the reader to figure this out.

*Major: presentation of results*

I would recommend the following changes to make it easier to follow / interpret results:
- Clearly state how many networks you train and what the dataset structure is
- Where variances are presented (like Fig4C), state whether these are standard errors / deviations or else
- Related to the deviation in 4C, in the text you seem to be interpreting the red line in 4C (Outgoing Dom) as being significantly different from the other lines, but the plotted variance suggest they might not be significantly different?
- Generally, results plots like 4D and 5E should report standard errors and significance tests
- Fig 5E seems to be a key analysis but the figure legend does not explain what the dots or bars actually refer to? I understand that authors want to argue that under different setup the different models mirror either the MAP or MLE prediction but to support that conclusion with a figure, they should present the expected pattern under each of these inference modes and then show how each of the models looks like either of these inference modes. As states above, the similarity should ideally be test for significance.

*Minor: stylistic changes / corrections*

- The in-text references should be in brackets, i.e. (O’Reilly, 2000) instead of O’Reilly (2000). The ICLR Latex file provides this as a citation option.
- Generally speaking, across all figures, I think authors could increase the font size relative to other visual elements and could then make the figures overall smaller to save space. Additional space could be used to explain the ideas better and contextualise findings, as discussed above. 
- Figure 2B is already data / results recorded from the model, is that correct? In that case I find it confusing that it is labelled as ‘B’ and as such listed above the description of the actual network algorithm.
- Line 417: “are be asymmetric”, seems like there is an error there
- Line 303: “Now, we test whether these learnt weights can, during Test (recall) help recall during the test phase of the network.”, that sentence seems off?

### Soundness
2

### Presentation
1

### Contribution
3
