# Intention Model: A Novel Explanation for In-context Learning

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
In-context learning (ICL) has demonstrated remarkable success in enabling large language models (LLMs) to learn to do a downstream task by simply conditioning on a few input-output demonstrations. Distinct from traditional learning paradigms, ICL does not require model updates, thus attracting significant interest in understanding the mechanisms behind LLMs’ ICL capabilities. Advanced works aim to understand ICL through an empirical viewpoint to provide the multifaceted nature of ICL, while some works aim to explain how ICL can emerge theoretically. However, the current theoretical analysis exhibits a weak connection to empirical explorations due to strong assumptions, e.g., perfect LLMs and ideal demonstrations. This work proposes an intention model, providing a novel theoretical framework for explaining ICL. With mild assumptions, we present a ``no-free-lunch'' theorem for ICL: whether ICL emerges depends on the prediction error and prediction noise, which are determined by \emph{\textbf{i)}} LLMs' error of next-token prediction, \emph{\textbf{ii)}} LLMs' prediction smoothness, and \emph{\textbf{iii)}} the quality of demonstrations. Moreover, our intention model provides a novel explanation for the learning behavior of ICL under various input-output relations, e.g., learning with flipped labels. This is fortunately consistent with our experimental observations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The current paper attempts development of a unified theoretical model of in-context learning that can help reconcile the incoherent empirical results seen in prior literature (e.g., the effect of data to label map randomization). To achieve this, the authors explicitly model the notion of "intention", i.e., the task the user wants the model to perform on a given datapoint, and assess what conditions lead to the inferred task from the model matching the intended task. This leads to a three-part decomposition of ICL error: (i) error of next-token prediction (essentially the autoregressive training loss); (ii) smoothness of predictions (how drastically they change if context is altered); and (iii) "quality" of demonstrations. All terms have intuitively expected effects and hence reconcile past empirical results.

### Strengths
The prime contribution from a theoretical standpoint in this paper is introduction of the user intent as a first-class citizen in theory. This helps accommodate phenomenology around experiments where alteration of the context lead to the same outputs---if the user intent remains the same, the model is likely to produce the same output. That said, I have some apprehensions on relation to past work and general presentation / experimentation.

### Weaknesses
- **Relation to past work.** A crucial missing reference seems to be Lin and Lee ("Dual operating model of ICL", ICML 2024). Therein, authors define a prior over tasks the model can solve and assess the effect of context size scaling to reconcile prior empirical results. It would help if authors can delineate how their contributions differ from that of Lin and Lee.

- **Experiments.** I understand the paper is theoretically driven, but there are several papers on the theory of ICL at this point and it is unclear which theoretical framework is in fact correct. I hence encourage authors to take a prediction-centric perspective: what predictive claim does your theory offer, and can you demonstrate that said claim checks out experimentally? I am happy with an entirely synthetic experiment. The currently existing experiments suggest induction heads may be the mechanism for intention inference, but that claim is mostly speculative and is not well corroborated by the current induction head knockout experiments (by knocking out induction heads, you might be removing general ICL ability, and it is unclear if where the model is failing is inference of the correct intent).

- **General presentation.** I found the writing quite convoluted in several parts of the paper. For example, the introduction has several typos and grammatical errors, and at times has unnecessarily complicated phrasing (e.g., "Numerous outstanding works have revealed the enigmatic characteristics inherent to ICL"). The citation commands are also incorrectly used---only \citet was used, with no \citep usage. If citations are to go in parentheses, then \citep should be used.

### Questions
- In Section 4.2, it is mentioned that the effect of high quality demonstrations is multiplicative on ICL error; however, other terms like next-token prediction accuracy and prediction smoothness have an additive effect. Intuitively, I don't follow why this would be the case. It seems to me the first factor in equation 13 (i.e., the factor with several additive terms) is merely assessing how well the model is at pretraining and modeling the distribution at hand, and the second factor (i.e., demonstration shift) assesses how good the demonstrations are at eliciting the desired capabilities. Is this the right interpretation? If not, can you better explain why the first term has additive influence of next-token error and prediction smoothness (which I would have expected to themselves have a multiplicative effect)?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a latent variable model to study in-context learning (ICL) of large language models (LLM). It contributes a theoretical framework based on hidden “intentions” which are sampled during LLM generation. A hidden Markov model is used to model the overall generation process of tokens from an intent. The paper proves a novel no free-lunch theorem for the intent model which describes the conditions for when ICL emerges in an LLM (small next-token prediction error and prediction noise). In addition, the paper relates the selection of demonstrations for ICL to matching the original intent, and provides theoretical insights for the process. Empirically, the paper reports experiments on the ability of LLMs to adapt to randomized labels in-context, linear probing for intents, and identifying induction heads for intent inference.

### Strengths
This work introduces a latent variable “intent” based model for understanding ICL. The model is a reasonable plausible model for ICL in LLMs, outlining the weak assumption used in the theoretical analysis. Based on the intent model, several theoretical results are given, including conditions for when ICL can emerge in LLMs, under the intent model. The model also provides theoretical understanding  to explain the phenomenon of demonstration selection for ICL, and adapting to random label changes (or other task shifts) using ICL. 

The paper provides some experimental confirmation of their intent model and theoretical analysis. The experiments show the performance of LLMs under task shifts which appear to support the analysis. Moreover, experiments that use (2-layer) probes to classify intents and isolation inductions heads for intents are included, which provide some justification for their model.

The idea of changing the value of isolated induction heads for intent and observing its effect on the LLM is interesting. The results appear to confirm the importance of the identified heads.

### Weaknesses
The amount of detailed mathematical analysis in Sections 3 and 4 is dense and obscures the key take away messages from the theory. For example, after detailing the many assumptions for the intent model and deriving the no-lunch theorem in 4.2, the conclusion of the theorem appears to be “LLMs with weak capability in prediction the next token and non-qualified (?) demonstrations fail to exhibit ICL capability.” This is very well-known from empirical evidence (since GPT4), so it is not very surprising that the intent model, under reasonable assumptions, arrived at this result. As a key result of this paper, its relevance to a broader ICLR audience is unclear. One suggestion to the authors is to reconsider whether to keep all of the technical details in the main paper, or describe the main takeaways and the theorem, but move the rest into the appendix.

The paper lacks direct empirical confirmation of its theoretical findings. In 5.2 it states that “it is challenging to calculate or estimate these values (values predicted as necessary for ICL in Theorem 1)” hence indirect experiments must be done. This is a significant weakness for the theory, as it essentially cannot be experimentally confirmed or falsified. Can the values be estimated in a toy setting? 

The intent recognition experiment is not totally convincing. It sets up an intent prediction task and uses features extracts from different layers of LLMs’, along with a 2-layer network to predict intent. Can this task be solved without using an intent model? Please consider including a baseline that plausibly does not implement an intent model. Details of the task setup are also missing. For example, what are some of the 50 intents? Are they instructions or tasks? How are train/test splits done?

A lot of the content in the appendix is highly relevant to the paper. For example, Appendix D which discusses the theoretical and empirical challenges. Moreover, the experiments that actually try to confirm the plausibility of the intent model within real LLMs are in Appendix F. Please discuss these experiments in the main body of the paper, state their conclusions and how they support the theory.

Writing of the paper needs significant editing and proofreading. 
Just a few examples:
L076 “Introducing an external to modify” external what?
L225 “error of next-token predicting”
L375 “It shows that ICL” what is “it”? 
L385 “can be wrapped in the way” what does “wrapped” mean?
L498 “GTP-4”, “achieves exciting performance” what does “exciting” mean?
L501 “matrixes”

What is “n” in Table 1?
How does Table 1 “show that larger LLMs can capture the intention”? Isn’t the result just scaling?
L1182 “group them into 2 to 5 categories” which ones? Can you provide more details or samples for the dataset preparation?
F.2 do the induction heads identified here affect intent recognition in section F.1? I.e, if you “knock out” the heads then extract features, does the intent prediction performance degrade?

### Questions
What is “n” in Table 1?
How does Table 1 “show that larger LLMs can capture the intention”? Isn’t the result just scaling?
L1182 “group them into 2 to 5 categories” which ones? Can you provide more details or samples for the dataset preparation?
F.2 do the induction heads identified here affect intent recognition in section F.1? I.e, if you “knock out” the heads then extract features, does the intent prediction performance degrade?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
A theory about In-Context Learning similar to Xie et al's Bayesian Inference theory. Aims to explain some characteristics of ICL noted but not explained by prior works, for example perturbations in the label space. Aims to break down the error in predictions to interpretable quantities like LLMs' performance, quality of demonstrations.

### Strengths
- The theory is very similar to Xie et al's Bayesian Inference theory with some modifications like neighbourhood of an intention, etc.
- The authors provide an interpretable way to connect LLM performance on next work prediction and the quality of demonstrations to the performance on ICL tasks (under their theory), which is nice.

### Weaknesses
### weaknesses:
 - Next token error is conditioned on \theta in assumption 4. Even if the LLM infers intention, that would be solely determined by o_1:i-1, say \theta_inferred. If the LLM is well trained, we can assume that it mostly infers the right intention and hence the condition with \delta_4,1 can be satisfied. But in cases when it fails to infer the right intention, this error may be quite large. So the assumption is strong. Moreover, there is no way to get predictions from the LLM given the same context and some different intention \theta_different, as the intention inference (if that is what happens in LLMs) is implicit and can not be disentangled. The LLM will always infer the same distribution over intentions given the same context, so I don’t understand assumption 4. Specifically, the assumption seems to conflate the inferred intention with the ground truth intention. While a well-trained LLM might infer the correct intention with high probability, the error in cases of incorrect inference needs more rigorous bounding. The inability to manipulate the LLM's inferred intention for a given context further complicates the verification of this assumption.

- Like Xie et al, the no free lunch theorem in this paper does not explain task learning capabilities of LLMs, on completely novel tasks (\theta not in the intention family) unrelated to pretraining text.

- The whole external mapping thing does not make much sense to me. Users do not provide an external mapping when getting the model outputs; they directly present demonstrations with this transformation. If the LLM infers this mapping, it can only be implicit. Making it a part of the original intention family. It is hard to tell if a mapping like flipped labels is present in the intention family learnt by the model during pretraining. If the mapping is randomly generated, this becomes a contradiction as it is surely not present in the pretraining corpus. The authors say that they will explore this in future work, but it is an important point that makes Xie et al’s theory and this paper’s theory inconsistent with Min et al’s results where the model is able to infer the right intention with randomly generated labels.

- Experiment section is too small and severely cut (defered to the appendix). Which model? What ICL task? It is an important part of the paper and needs to be put in the main text. Also, the evidence is circumstantial. Intervening on model activations can imply so many things related to completely different theories. How can we claim that these results imply anything specifically about the intention model? This also highlights the difference between theory and practice, as the presented theory does not elicit easily verifiable causal experiments. The lack of detail regarding the experimental setup (specific model, ICL task) makes it difficult to assess the validity of the claims. Furthermore, the reliance on circumstantial evidence weakens the connection between the theoretical framework and empirical results.

- The paper is very hard to read and follow. Like
  - section 3.3, should define \delta_1,1, 1,2, 4,1, etc. What do forbidden tokens mean, what are forbidden transitions?
  - citations are placed very poorly. Sometimes before the sentence, sometimes after, sometimes unrelated; without proper usage of citet/citep.
  - [nitpicky] “Advanced works”: what is advanced, and compared to what?  “fortunately consistent”: while good to know that the authors felt relieved that the method worked, it maybe inappropriate in a technical report. Some words feel too artificially placed like “enigmatic characteristics”.
  - “These intriguing phenomena highlight the difference between traditional learning and ICL Kossen et al. (2024). These seminal explorations provide a fruitful guide for understanding and explaining ICL.”  These sentences don’t flow well. which works?

  - “a relatively weak connection to empirical investigations, potentially due to strong assumptions” [ICML 2024 paper] illustrates this and may be appropriately cited.

  - Line 77: “Introducing an external to modify …”, external what?
  - Line 116: definition of Sn can be confusing to read.
  - o is used for both delimiter and document tokens. confusing.
  - Line 297: \theta_g is now called inferred intention, previously it was ground truth. confusing.
  - Line 292: where does m come from? What does it mean? Unclear.
  - Table 1 is referred to as Table 2 in the text.
  - Many more ...

  Although I don't believe in reducing review scores for small clarity and writing issues, this paper seriously suffers from them and hampers the readers ability to understand the concepts conveyed. I would recommend a clear rewrite with more help from experienced co-authors.

### Questions
- Why is it called the no-free lunch theorem? No one expects ICL to emerge in models with high next-token prediction errors, or models to perform well on under-specified ICL tasks.

- Why do we need to have a neighborhood of intentions, which are exactly modeled; compared to Xie et al’s exact intention which may have some modeling error (as is generally the case with all ML models).

- What is the difference between Assumption 3 and 5?

- Section 5.2: Why is it difficult to estimate next-token error of LLMs? And the results of this section don't mean much. Everyone would expect the ICL performance to go down with a more complex task. This does not imply that the model is performing inference of a complex intention as presented by the theory. There is no "introduction of an external matrix T”, it is all in the theory. Where is the causal link that implies that the model is figuring out this new matrix T?

In all, I find it hard to justify this paper because the theory it presents does not make any verifiable new predictions that Xie et al did not already make, and in my opinion does not explain the previously unexplained phenomena like Min et al.

I will increase the score if the paper is clearly rewritten. I know that this is a long paper and hard to put concisely in 10 pages, but in this sort of work, the paper would greatly benefit if some of the underspecified theory (which makes it hard to understand) is moved completely to the appendix, and some more readable results like the experiments are moved to the front. The distinction between the results presented in this paper and Xie et al are unclear which could have been greatly improved in the introduction section. These are just some of my personal suggestions.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a theoretical framework called the "intention model" to explain ICL behaviors. The authors present a "no-free-lunch" theorem for ICL, showing that its emergence depends on prediction error, prediction noise, the model's smoothness, and demonstration quality. Unlike previous approaches with strong assumptions, this work relaxes the assumptions on perfect model alignment and demonstration representation. The intention model helps bridge the gap between theoretical explanations and empirical observations.

### Strengths
1. The theoretical analysis breaks away from the typical assumptions about perfect model alignment. It feels like it’s providing a more grounded explanation, making it easier to connect theory with the real behaviors of LLMs.

2. The writing is generally clear, and the mathematical notation is thoroughly defined, which makes it easier for readers to follow.

### Weaknesses
1. The paper's theoretical framework largely follows the derivation approach from Xie et al. (2022), particularly leveraging Bayesian Inference. Although it extends the original work by adding an error term between the LLM and the real distribution, this extension doesn’t feel groundbreaking. The contribution seems more like an incremental step rather than a major theoretical innovation.

2. The use of the term "No Free Lunch" for the presented theorem seems a bit off. The typical connotation of "No Free Lunch" is about the impossibility of a universal solution that works optimally in all scenarios. Here, the theorem implies that LLM performance depends on factors like prediction error, prediction noise, and demonstration quality. While there is indeed an implication of trade-offs, if the theorem isn’t emphasizing a broad, universal limitation but rather a specific condition for ICL, then this choice of terminology could easily confuse readers.

3. The experimental section lacks clarity on how each of the theoretical components, particularly the terms in Equation (13), manifests in practice. It’s unclear how specific terms like "error in predicting the next token," "prediction smoothness," and "distribution smoothness" are reflected in the real experimental observations. This disconnect makes it difficult for readers to see how well the theory aligns with the empirical results, and it weakens the overall support for the claims made in the theoretical part.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
2
