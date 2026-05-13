# Approaching an unknown communication system by latent space exploration and causal inference

- Decision: Reject
- Scores: 8, 3, 5, 6

## Abstract
This paper proposes a methodology for discovering meaningful properties in data by exploring the latent space of unsupervised deep generative models. We combine manipulation of individual latent variables to extreme values with methods inspired by causal inference into an approach we call \textit{causal disentanglement with extreme values} (CDEV) and show that this method yields insights for model interpretability. With this, we can test for what properties of unknown data the model encodes as meaningful, using it to glean insight into the communication system of sperm whales (\textit{Physeter macrocephalus}), one of the most intriguing and understudied animal communication systems. The network architecture used has been shown to learn meaningful representations of speech; here, it is used as a learning mechanism to decipher the properties of another vocal communication system in which case we have no ground truth. The proposed methodology suggests that sperm whales encode information using the number of clicks in a sequence, the regularity of their timing, and audio properties such as the spectral mean and the acoustic regularity of the sequences. Some of these findings are consistent with existing hypotheses, while others are proposed for the first time. We also argue that our models uncover rules that govern the structure of units in the communication system and apply them while generating innovative data not shown during training. This paper suggests that an interpretation of the outputs of deep neural networks with causal inference methodology can be a viable strategy for approaching data about which little is known and presents another case of how deep learning can limit the hypothesis space. Finally, the proposed approach can be extended to other architectures and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper reports a very fascinating application of the use of machine learning and data mining for scientific knowledge discovery, using the example of understanding the communication systems of non-human organisms.
Specifically, the authors extract the latent structure of the target data based on the fiwGAN architecture, a state-of-the-art method of the WaveGAN model's genealogy of methods without information loss (e.g., loss of phase information when turned into a power spectrogram), manipulate individual units of the network inputs to extreme values and The proposed approach is to manipulate individual units of the network's inputs to extreme values and estimate their impact on the observable properties of the outputs using causal inference methods.
Section 2 describes the latent structure learning method. The paper then investigates the latent causal structure of three human-interpretable acoustic features. Following this, Section 3 focuses on the number of clicks, Section 4 on the click interval and its standard deviation, and Section 5 on the timbre (spectrum) itself and its variation (standard deviation).
Finally, the paper summarizes new scientific findings derived from machine learning in Section 6.

### Strengths
In response to the challenging task of unraveling the communication system of whales, this paper proposes a new causal analysis method for state-of-the-art machine learning methods for acoustic signal analysis, inspired by methods for inferring dose-dependent responses in the context of pharmacology. The strengths I perceive in this paper can be summarized as follows.
- The subject matter itself that this paper deals with is of great scientific importance beyond the toy example.
- The presentation of this paper is very excellent. It is well thought out for a diverse audience, especially since it provides sufficient background knowledge and motivation for the research questions, even for the acoustic communication systems of whales, for which many machine learning researchers may not have domain knowledge.
- The methods proposed to gain insight into the causal structure of the target of interest from the latent variable space extracted by machine learning data analysis are very appealing, a new approach to cross-disciplinary thinking inspired by pharmacology dose-response.

### Weaknesses
I have not found any notable weaknesses in this paper. If I had to pick one, I would say that I do not have domain knowledge of how impactful the new findings of this paper on the challenge of elucidating the communication system of whales (the finding that not only clicks but also tones themselves may have important hidden meanings) are in the area of expertise in question.

### Questions
First of all, I would like to thank the authors for sharing this paper with the community. I have enjoyed reading this paper very much. To make sure I understand the value of this paper correctly, let me ask the authors two questions.

(1) The contribution of the explanation to the original data of the latent dimension specified in the 5 dimensions being extracted by fiwGAN. 
My question is: Is it known how much the ATE of the number of clicks contributes to the representation of the observed data?
More specifically, does the fact that the bit with index 1 in the latent variable space (5 dimensions) responds well to ATE mean that ATE is the second principal component (in the sense of, say, principal component analysis)?
If so, I would be very interested in what elements are responding to the first principal component (i.e., the bit with index 0).
I understand the part where the model is limited to 5 bits (32 classes) of characteristic coding space for the 5 coder types present in the data so that constructivity can be captured. Is the index of these bits tied to foresight knowledge such as the index of these 5 coder types? Or does the index of bits reflect some ranking of its expressive power, as in, for example, classical principal component partial analysis?
This may be a simple question that arises because I simply missed the description of the details.

(2) Does the method of identifying causal structures analogous to dose-response, which the current proposed method does, also work for factor combinations?
My understanding is that the current causal structure is investigated separately for each factor, such as number of clicks, tones, etc. Is it not possible, for example, for a combination of those factors to have a new semantic meaning?
Is it possible, for example, that "a constant rhythm of low tones" and "a constant rhythm of high tones" have different meanings? I imagine that it would be difficult to distinguish between the two with only one factor, "constant rhythm," and that it might be difficult to tell without combining factors.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work applies an existing approach called fiwGAN to a “sperm whale communication” dataset in order to extract an interpretable representation. They then assess whether the learned code “aligns” with natural features of whale signals such as “number of clicks”, “clicks regularity” and “click spacing” by perturbing the components of the latent code individually to see if they encode these natural features.

**Review summary:** Although I was glad to see an application of disentangled representation learning to real world data, I found this work unconvincing. I have issues with the motivation, the originality, their use of the term "disentanglement", the use of causal terminology and clarity. I also found the experiments to be unconvincing. I expand on these below. For these reasons, I recommend rejection.

### Strengths
- Original application to whale communication.
- Surprising findings, in Figure 1: “The 9R type was never part of the training data, yet our network learns to generate codas that resemble this type (Sec. 4).”

### Weaknesses
### **Unclear motivation**
I have a general concern. What is the advantage of learning a representation (t,x) using a deep generative model in the hope that $t$ will represent some intuitive features (like number of clicks and click regularity), if these very features can be extracted from the raw data algorithmically (as is done in this work, for evaluation)? I understand that this is only to evaluate the disentanglement of the method, but if these intuitive features can be computed from the raw data, what’s the point of trying to extract them in an unsupervised manner here in this application?

### **Originality**
As I said above, I believe this work present an original application of disentangled representation learning. However, I don't see novel methodological contributions. The authors essentially trained an existing method and applied fairly standard qualitative evaluation strategies to assess disentanglement.

### **Unclear use of the word “disentanglement”**
- The authors should clarify what they mean by disentanglement, since their definition (which I inferred from their experiment) seems different from the one I know and which is widely used: Typically, disentanglement means the following: every component of the latent representation influences one and only one interpretable factor of variation. 
- Figure 4: This does not correspond to the usual notion of “disentanglement”. Here, all the dimensions of t have an impact on the number of clicks. The interesting thing is that it seems only one dimension of $t$ has a positive impact, while all the others have a negative impact. 
- Figure 5: I still believe this does not correspond to the usual notion of disentanglement, since, again, every dimension of t_i have an impact on the “inter-click” interval and the “coda regularity”, it’s just that one of the bits has a monotonic influence while the others are non-monotonic.

### **Concerns with experiments**
The experiments did not convinced me that the fiwGAN algorithm can robustly discover natural factors of variations in the data:
- Are the findings robust to reinitialization? I.e., if you rerun this experiment with multiple seeds, are you always finding similar patterns? I don’t think the experiments show reruns. This is very important for such analysis, to avoid cherry-picking. 
- In Figure 4: the curves that go down seem to go up again after t = 10, do they end up being positive if we extend the range of t even further?
- Surprising findings, in Figure 1: “The 9R type was never part of the training data, yet our network learns to generate codas that resemble this type (Sec. 4).” I would like to see stronger evidence that the model can generate reasonable samples never seen during training. Was this sample cherry-picked?

### **Unnecessary use of causal terminology**
The framing in terms of causal inference feels a bit unjustified, since one has full control over both x and t, so that there is not direct causal effect from x to t, making causal inference trivial.

### **The work lacks clarity at times**
- In intro: “Networks trained on raw speech data are shown to learn to associate lexical items with code values and sublexical structure with individual bits in $t$ …” the variable $t$ was not defined, so it’s hard to follow what is meant here.
- I found the description of fiwGAN a bit imprecise at the beginning of Section 2. I think it would help to write down explicitly the loss that is optimized, even if this is not part of your contribution.
- Figure 2: The code t is binary, but the rest of the paper assumes t is Rademacher, i.e. with support {-1, 1} instead of {0, 1}. Which one is it?
- Section 3: “We observe a high degree of entanglement (4) of the learned encodings within the range seen in training ([−1, 1]).” I don’t understand the meaning of “entanglement” here. I now understand that this paragraph refers to experiments in Figure 4. I feel like the separation between theory/method and experiments is not clear enough here.


### Questions
- $t$ is a vector of 5 bits, to fit the number of coda types in the dataset. Is this for the approach to work? You say other works have shown that having a mismatch doesn’t matter. But does it matter in your specific application?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an approach for uncovering salient properties in an unknown data generating process by leveraging the latent spaces of generative models. Specifically, the authors focus on deepening our understanding of the communication systems of sperm whales using GAN-based generative models. To accomplish this, they propose a method called CDEV which concretely involves setting different latent space variables to extreme values and measuring their effect on observable features using causal inference techniques.

### Strengths
Overall, this is a **fascinating paper and well-written paper**. Generally speaking, the notion of using generative models to drive hypothesis formulation and testing for unknown processes may have profound implications for basic science research, and the particular process studied here (whale communication) is refreshingly off the beaten path for ICLR. The proposed CDEV method is explained clearly and with sufficient information to allow for replication (though the data and model appear to be closed).

### Weaknesses
I have two significant concerns with the work: (1) that the proposed method is applied too narrowly to be of interest to the broader ICLR community, and (2) that insufficient evidence has been provided to support the application-specific claims.

**Narrow application of proposed methods**. The proposed CDEV method is applied to a single model trained on a small amount of data from a single unknown process. The model is even a fairly unconventional one, with (i) modeling assumptions (the specific use of 5 discrete inputs) rooted in rudimentary understanding of the data process (5 general classes of data), and (ii) an unconventional GAN setup called fiwGAN. The authors claim that “the proposed approach can be extended to other architectures and datasets.” This may be true, although it would certainly be more convincing if the authors demonstrated this themselves. For example, corroboration of the CDEV method on a _known_ process (e.g. human speech) would inspire more confidence. The authors allude to related work on human speech, but while that work does inspire confidence in the generative modeling approach (GANs), it does not look at the CDEV algorithm specifically. Moreover, I have my doubts about the generality of the method, as domain knowledge appears to be a substantive input to the CDEV algorithm at several levels: (i) the model itself, specifically the choice of 5 discrete inputs which seems arbitrary without more justification, (ii) the data selection process, which appears to be heavily filtered based on expert knowledge of whale communication, (iii) the determining of appropriate extreme values for the latent space intervention, which lacks a clear, principled approach, and (iv) the outcome functions used to measure average treatment effect, which are also highly dependent on expert knowledge and may introduce bias.

**Insufficient evidence to support claims**. Though I am certainly not an expert in this application domain, the authors appear to be making novel claims about the process they study, e.g., that mean spectral frequency is a salient property of sperm whale communication. It is not clear to me that all confounders have been ruled out to support this claim. For example, could it not be the case that fluctuations in mean spectral frequency have nothing to do with _communication_ but are instead caused by some other random source of noise (as an arbitrary example, changes in water temperature)? If this were true, the GAN would still need to produce such fluctuations to fit the data distribution, despite being irrelevant to communication. Another potential confounder: how do we rule out that the GAN simply failed to fit the underlying data distribution, and any interventional effects are simply a consequence of a poorly fit model? The authors need to provide more evidence that the observed effects are not due to model artifacts or other confounding factors, and that the identified properties are indeed meaningful for whale communication.

### Questions
Other questions and comments:

- Why is the fiwGAN (t, X) structure necessary, as opposed to just training a standard GAN and intervening on the incompressible noise (X)?
- The hypothesis generation seems to be largely expert-driven (i.e., expert codifies hypothesis in outcome function and then tests with model) rather than model-driven (i.e., model conveys some hypothesis that would suggest a particular outcome function). What is the key difference between using a generative model vs. just testing a hypothesis directly on the data distribution (e.g., showing that mean spectral frequency varies across examples in the dataset)?
- How might we extend this method to the particular noise structure of diffusion models, which are more “in vogue” at the moment?
- Figure 1 shows 0, 1 for t codes instead of -1, 1 as in the rest of the paper (this confused me especially w.r.t. choosing low extreme values of -1 rather than 0)

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a method to explore the latent structure of sperm whale's communication system. They combine causal inference and GAN based model into their methodology. They did a thorough analysis of the sperm whale data and proposed some novel insights into the latent structure of the data.

### Strengths
The application is quite novel. The paper introduces an approach for exploring scientific findings from a sperm communication system using deep generative models and causal inference techniques.

### Weaknesses
The experiments are insufficient. I listed some questions in the section below.

1. how do the authors know that the latent generated by the proposed method are the actual latent structures of the data not some artifacts of the model? How do you validate your results?
2. there are other disentangement methods using VAE (e.g. betaVAE). The paper lacks comparisons with the existing approaches. 
3. in figure 4 and 6, it seems that only 1 bit is different while other bits are in general similar to each other?
4. what are the limitations and future research directions for the proposed method?
5. can the proposed method be generalized to other animals' communication systems or other fields? -- the paper could be more solid by including results on another dataset.

### Questions
1. how do the authors know that the latent generated by the proposed method are the actual latent structures of the data not some artifacts of the model? How do you validate your results?
2. there are other disentangement methods using VAE (e.g. betaVAE). The paper lacks comparisons with the existing approaches. 
3. in figure 4 and 6, it seems that only 1 bit is different while other bits are in general similar to each other?
4. what are the limitations and future research directions for the proposed method?
5. can the proposed method be generalized to other animals' communication systems or other fields? -- the paper could be more solid by including results on another dataset.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair
