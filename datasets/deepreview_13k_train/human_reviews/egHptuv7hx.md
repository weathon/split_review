# How does controllability emerge in language models during pretraining?

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Language models can intervened upon by steering their internal representations, which alters the degree to which concepts such as emotional tone, style, truthfulness, and safety are expressed in their generative outputs.  This paper demonstrates that intervention efficacy, measured by linear steerability (the ability to adjust outputs via linear transformations of hidden states), emerges abruptly during pre-training, and furthermore, even closely-related concepts (e.g. anger and sadness) can emerge at different stages of pre-training. To understand how the steerability of internal representations changes during pre-training, we introduce the "Intervention Detector" (ID), which applies unsupervised learning techniques to hidden states under different stimuli, and generates concept representations that can be used to steer the text generation of language models. The extracted concept representations are used to compute an ID score, measuring their alignment with the model’s hidden states. This ID score can be used to approximately predict the time of emergence of effective intervention by steering different concepts, and the degree to which each concept is able to intervene.
By analyzing ID scores across a longitudinal series of models taken at different stages of pre-training, we demonstrate that, as pre-training progresses, concepts become increasingly easier to extract via linear methods, which correlates with the emergence of steerability. For instance, in the CrystalCoder model, the linear steerability of the concept "anger" emerges at 68\% of pre-training, whereas the linear steerability of the concept ``sadness" emerges at 93\% of the pre-training process. We use heatmap visualizations and other metrics (eg., entropy, cosine similarity, tSNE) to study these differences and validate the reliability and generalizability of ID scores through model interventions using the extracted concept representations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The current paper investigates the development of controllability in language models's pre-training. It focuses on a very specific type of control, i.e., intervention, and the control of a very specific kind of factors, i.e., concepts related to emotions. The authors introduce the "Intervention Detector" (ID) as a method to track how control over specific concepts emerges and solidifies during pre-training. By using dimensionality reduction techniques on hidden states, ID identifies points at which different concepts—such as emotions and reasoning—become extractable and controllable.

The study reveals that concepts don’t become controllable simultaneously; for example, anger is controllable earlier in pre-training than sadness. The authors validate these findings with metrics like ID scores and heatmap visualizations, showing that as pre-training progresses, the model's hidden states align more with the extracted concepts, allowing for more effective intervention.

### Strengths
- I find this paper is working on a very interesting topic that is worth investigating, i.e., when the controllability emerges during pre-training. It is not only valuable to people working on tasks like knowledge editing, but also helps us understand the learning procedures of LLMs.
- One interesting finding that I like is how the control of different (emotional) concepts emerge differently from each other. Maybe it is worth check whether this is consistent with human beings.

### Weaknesses
As a paper that investigates the "controllability" (as its title suggests), though the paper has many interesting findings, I expected it to consider more control techniques and factors, whereas the current paper focuses on a very specific type of control, i.e., intervention, and the control of a very specific kind of factors, i.e., concepts related to emotions.

Another major risk of the paper is its writing, making the paper hard to follow. I am saying this with the following concerns:
- The primary ability of LLMs is to generate language, and, in this context, the term "controllability" could have multiple meanings for me and it could be one in many ways, prompting, instruction tuning, etc. It appears that what this paper focuses on is actually the "editability" (instead of the wider controllability) of LLMs. I suggest the authors first define what "controllability" means in this paper. 
- The above point makes many terms, especially in the abstract and introduction, hard to interpret. For example, it is hard to understand how a concept can be controlled. 
- More explanations are needed for the causality between the scores you computed and the controllability, e.g... what is SNR used for?

### Questions
See my comments in "weaknesses".

### Soundness
3

### Presentation
3

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
The authors present the “Intervention Detector” (ID) to detect when the controllability of internal representations changes/emerges in Large Language Models (LLMs). The idea is to use a model’s hidden representations for suitable stimuli, which are inputs related to concepts such as emotions. They calculate an ID score to approximately detect when this controllability emerges during training. Empirically, they analyse the emergence of controllability across several checkpoints of the entire pre-training phase of an open-source model to pinpoint the emergence of concepts such as emotions.

### Strengths
The idea of detecting when high-level concepts, such as a model’s understanding of emotions, can be controlled for the first time during training (by testing when interventions show an effect) is exciting and promising.

The article is rich with graphics that present the results in an intuitive way. The latter are interesting and motivate future work.

### Weaknesses
Unfortunately, the article suffers from technical inaccuracies that make it very difficult to trace what exactly the authors did in their experiments.



Section 3:

Firstly, there are no definitions for $h_+, h_-$, the normalized() function, $S_{test}, A_i$, and checkpoints. The Appendix furthermore lists $H^+$ and $H^-$, which were never defined. Could the authors include a clear (sub)section for definitions, perhaps at the beginning or within an expanded notation subsection, to define all key terms? Could they also ensure consistency between the main text and the appendix regarding notation?

In step 1 of the ID method, there are positive and negative "stimuli". While the authors list a template to create positive and negative stimuli in the Appendix, it is unclear what the "{positive concept scenario}" is. Could the authors provide specific examples of positive and negative scenarios used in their experiments? Additionally, could they explain the source and selection criteria for these scenarios?

In step 2, the $v \in \mathbb{R}^{1 \times 4096}$ is supposed to be the first principal axis, correct? If so, there is no dimensionality reduction. Furthermore, the sets $S_{pos}$ and $S_{neg}$ contain positive and negative "samples", respectively. Are "samples" the stimuli from before?

At the end of step 2, the authors claim that "For a layer $l$, this vector $v_l$ is linked to a specific concept". Why? Could the authors provide empirical evidence or theoretical justification to support this claim? 

In step 3, equation (3), there is a "[-1]" missing, correct?

In Step 4: Is there any theoretical justification for adding $v_l$ to a layer?



Section 4:

Firstly, what is CrystalChat? There is no reference or information. Furthermore, the authors extracted checkpoints (I guess from the pre-trained LLM360 Crystal model) and then "fine-tuned each checkpoint" - do you mean fine-tuning the model based on the weights for these checkpoints? Moreover, why fine-tune the model in the first place? It is also the first step in Figure 3, but–--from my understanding—the ID method's first step is collecting hidden states based on prompting models at different stages of the pre-training phase. Could the authors clarify this process and add a dedicated subsection within Section 4 that outlines the model architecture, training process, and rationale for fine-tuning? If the models are fine-tuned before the analysis, how can it be ensured that whatever is measured did emerge during pre-training (and not fine-tuning)?

Overall, there is no information about the experimental setup in this section. Since this paper focuses on one specific model, it would be nice to have some reference background so readers do not immediately need to consult the LLM360 paper. Furthermore, the authors use ChatGPT to evaluate the model output after intervening and list a template in the Appendix. However, it is very difficult to grasp what the included "{CrystalChat intervention results}" are. It would be helpful to include some concrete examples to showcase the contents of all the templates.

The entropy plots in Figure 5 show variations in the range 4.89 - 4.96 (or smaller). I am wondering whether these variations are significant in absolute terms. Could the authors provide some reference plots or baselines to illustrate why these variations are representative of the described behaviour?

Figure 6 shows notable differences for the checkpoints at 78.11% and sometimes at 62.81% and 93.41%. Why do these occur? What makes these checkpoints unique?

The datasets used for the Supervised Detection Task should be referenced in the text and briefly explained. Also, models are now fine-tuned with different learning rates - however, it is unclear what the other hyperparameters are (learning rate scheduler, number of epochs, batch size, etc.). In addition, how many values of runs with different seeds were averaged to gain these results?

To summarise, while the results seem interesting and the overall approach promising, the paper lacks crucial details regarding how the experiments were conducted, which prevents reproducibility. There is also no code available. However, I am open to improving my rating if the authors provide sufficient details and polish their article.




Minor: 

The papers for specific Algorithms like PCA and t-SNE should be referenced; similarly, the model version (for example, for ChatGPT) should be mentioned.

Grammar and spelling mistakes need to be corrected. For example:

Line 068/069: “on model’s output” -> “[based] on a model’s output”

Line 080/081: “(Crystal (Liu et al., 2023))” -> needs rephrasing

Line 095/096: “be summarized thus:” -> “be summarized as:”

Line 145/146: “assessing model’s” -> “assessing a model’s”

Line 146/147: “figure 3” -> “Figure 3”

Line 161: “Tan et al. (2024) uses” -> “Tan et al. (2024) use”

Line 199/200: “hidden state value” -> “hidden states”

Line 210/211 and 214/215: “Detecting” -> “Detection”

Line 224/225: “at the -1 token position” -> “at the final token[’s] position”

Line 268: “Representation Vector” -> “Representation Vectors”

Line 279/280: “ID scores Across” -> “ID Scores Across”

Line 317: “Figure 4 use” -> “Figure 4 uses”

Line 318/319: “show ID score” -> “show ID scores”

Line 766/767 and 770/771: “Give the statement” -> “Given the statement” (Is this just an error in the article, or is it also present in the code for the experiments?)

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores when controllability (via representation steering) emerges in language model pretraining. To do so, the authors devise the Intervention Detector (ID) method, which, given a set of layer representations, identifies when a certain concept becomes linearly encoded. They find that controllability, for several concepts, emerges suddenly during pre-training.

### Strengths
The idea to explore the emergence of linear steerability over pre-training is quite novel; past works only focus on the final configuration of the LM (but this is for good reason, see weaknesses). Experiments test a broad range of concepts.

### Weaknesses
I have several concerns about the paper, summarized broadly as follows:

**Major weaknesses (impacted score)**
1. __Motivation unclear/unconvincing:__ it was unclear why when controllability emerges should matter. In particular, 
    - While the authors state that past work focuses on steerability of already-trained language models, this is the actual use case of LM steering. In contrast, the authors would need to make a strong case for investigating the emergence of controllability-- to me, it is unclear why one cares about representation steering on a not-fully-trained model, as the model itself would never be deployed. I would suggest to clarify the context in which emergence of controllability is useful.
    - Controllability in and of itself doesn't mean much: what does it mean for concept representations to emerge "early in pretraining" when the LM presumably has not converged to a good distribution of language? 

2. __Imprecise definitions:__ the paper is about ``controllability" at large, yet only addresses a quite narrow domain within _linear_ control, adding an unscaled input to the representation. Controllability is a broad term that spans also nonlinear control-- I would change the emphasis to just additive representation steering. 

3. __Methodological issues__:
    - Even though the authors state it is out of scope, it is important to test on another LM family for generalizability.
    - Did you try different scaling factors? In the literature, the scaling strength is crucial for performance [1-3]. If different scaling factors were not tried, could the authors please provide a justification?
    - Experiments are ideally run with several random seeds. For instance, it is hard to gauge the true effect for ARC Challenge and ARC Easy without error bars-- for OBQA, the gap is also quite small. Could the authors please provide error bars with the plots?

**Minor weaknesses (didn't impact score)**
1. Missing citations: https://arxiv.org/abs/2310.04444v3 https://arxiv.org/abs/2405.15454
2. l205: summarize the RepE method (e.g., are you referring to RepE linear combination, piece-wise operation, or projection?)
3. l210: the algorithm used for the Unsupervised task is unclear. What does it mean to obtain hidden values? If you mean the hidden states of the LM, which state are we using (e.g., last token)?

### Questions
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores how controllability emerges during the pretraining process of language models. The authors propose a novel framework, named Intervention Detector (ID), which applies dimensionality reduction techniques (like PCA) to the hidden states of models under different stimuli, allowing for the extraction of concept-specific representations. This method allows for targeted interventions, helping models respond more predictably to specific prompts.
The paper finds that controllability in language models is an emergent property that develops as pre-training progresses.

### Strengths
1. The idea of investigating the concept of controllability within pre-trained language models is novel and interesting.
2. The paper has been experimented with fairly extensively, and the results show good potential.

### Weaknesses
The paper lacks clarity and most of the practical details and its design principles remain vague or unresolved. Please see the Questions.

1. I think there are some operations that you need to explain why:
- In Hidden States Collection, why do you collect the hidden states at the -1 token position?
- In Dimensionality Reduction, why do you compute the difference of hidden activations and compute PCA? How is this related to the latent concept?
- Where is the definition of $A_i$ in Analyzing ID scores Across Layers?

2. Have you considered other methods of selecting stimuli? For example, based on perplexity.

3. You just randomly selected 256 stimuli, which is heavily influenced by the random seed, so I think you need to run different tests to see how different seeds affect the random selection.

### Questions
1. I think there are some operations that you need to explain why:
- In Hidden States Collection, why do you collect the hidden states at the -1 token position?
- In Dimensionality Reduction, why do you compute the difference of hidden activations and compute PCA? How is this related to the latent concept?
- Where is the definition of $A_i$ in Analyzing ID scores Across Layers?

2. Have you considered other methods of selecting stimuli? For example, based on perplexity. 

3. You just randomly selected 256 stimuli, which is heavily influenced by the random seed, so I think you need to run different tests to see how different seeds affect the random selection.

### Soundness
3

### Presentation
2

### Contribution
3
