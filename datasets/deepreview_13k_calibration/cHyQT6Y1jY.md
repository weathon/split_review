# In Praise of Stubbornness: The Case for Cognitive-Dissonance Aware Continual Update of Knowledge in LLMs

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 8, 3, 6

## Abstract
Despite remarkable capabilities, large language models (LLMs) struggle to continually update their knowledge without catastrophic forgetting. In contrast, humans effortlessly integrate new information, detect conflicts with existing beliefs, and selectively update their mental models. This paper introduces a cognitive-inspired investigation paradigm to study knowledge updating in LLMs. We implement two key components inspired by human cognition: (1) *Dissonance and Familiarity Awareness*, analyzing model behavior to classify information as novel, familiar, or dissonant; and (2) *Targeted Network Updates*, which track neural activity to identify frequently used (*stubborn*) and rarely used (*plastic*) neurons.

Through carefully designed experiments in controlled settings, we uncover a number of empirical findings demonstrating the potential of this approach. First, dissonance detection is feasible using simple activation and gradient features, suggesting potential for cognitive-inspired training. Second, we find that non-dissonant updates largely preserve prior knowledge regardless of targeting strategy, revealing inherent robustness in LLM knowledge integration. Most critically, we discover that dissonant updates prove catastrophically destructive to the model's knowledge base, indiscriminately affecting even information unrelated to the current updates. This suggests fundamental limitations in how neural networks handle contradictions and motivates the need for new approaches to knowledge updating that better mirror human cognitive mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present a detailed framework for continual learning in LLMs through targeted neuron updates. Their framework incorporates an external dissonance-aware classifier that uses neuron activations and gradients based features to categorize input text as familiar, novel, or contradictory. They introduce various strategies — plastic neurons, stubborn neurons, candidate neurons, and specific neurons — to select neurons for targeted LLM updates.

Experimental results on the COUNTERFACT dataset using GPT-2-small and GPT-2-xl demonstrate that the proposed framework can accurately classify input data as familiar, novel, or contradictory using simple classifiers like SVM and Random Forest. Detailed experiments on targeted updates show that the framework effectively updates LLMs for both conflicting and non-conflicting data, outperforming baseline methods.

An anonymized codebase is provided for reproducibility.

### Strengths
- The method, inspired by high-level human brain mechanisms for knowledge updates, is novel and well-suited for LLMs.
- The paper is well-written, with a clear motivation and goal, along with thorough explanations of the framework's technical details.
- Experimental results on GPT-2-small and GPT-2-xl provide valuable insights, highlighting the advantages of considering plastic and stubborn neurons for continual LLM updates.

### Weaknesses
 - The experimental scope is limited to two relatively small LLMs — GPT-2-small and GPT-2-xl. As mentioned in the paper, the framework performs better on the smaller GPT-2-small model compared to GPT-2-xl. Results on larger models, such as 7B or 8B parameter LLMs, would provide a more comprehensive evaluation of the framework's effectiveness. The performance difference between the two model sizes raises concerns about the framework's scalability and generalizability to more complex models. It is unclear if the observed benefits on smaller models would translate to larger models with significantly different architectures and training regimes. This limitation makes it difficult to assess the practical applicability of the proposed approach in real-world scenarios where larger models are typically employed.
- The conflicting information update experiments (Section 3.4) include only a few baseline comparisons. Expanding the evaluation with additional baselines, such as PMET or GRACE, would strengthen the analysis. The current evaluation lacks a thorough comparison against state-of-the-art methods for knowledge editing and continual learning in LLMs. Without a more comprehensive set of baselines, it is difficult to determine the relative advantages and disadvantages of the proposed approach. The limited number of baselines makes it challenging to contextualize the results and assess the true impact of the proposed framework.

### Questions
See the Weakness part

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates categorizing neurons within large networks based on how often they are used, i.e. how much information they process. Based on this identification the authors propose to target learning novel information, e.g. in a continual setting, to specific sets of these neurons.

### Strengths
The paper is refreshingly well written and structured. it is concise and on the point. The idea is very intuitive, however I am not an expert of this field to be able to assess its novelity or relation to previous work.

### Weaknesses
I consider it helpful to have a more explicit section dedicated towards relation to previous works. Currently, only the paragraph at ll 78 seems to hint at related works. I think expanding this more (if this is applicable) would help better assess the proposed approach to others and in this way better evaluate its significance. Unfortunately, I can not make real suggestions on what to add though as I am not an expert on this topic.

In ll 494 the authors write "Language models can classify new information as novel, familiar, or dissonant ...". I am a little confused by this statement. I understood that rather a seperate classifier learns the classification. So it is not the LLMs that can classify. Additionally, (correct me if I'm wrong) the classifier is trained via supervision right? Then this claim/sentence seems a little unspecific.

I am a little concerned about the very different results with the xl model. Do the authors have an intuition on why they are observing these differences? It would be good to add this intuition into the paper more explicitly.

### Questions
In ll 494 the authors write "Language models can classify new information as novel, familiar, or dissonant ...". I am a little confused by this statement. I understood that rather a seperate classifier learns the classification. So it is not the LLMs that can classify. Additionally, (correct me if I'm wrong) the classifier is trained via supervision right? Then this claim/sentence seems a little unspecific.

I am a little concerned about the very different results with the xl model. Do the authors have an intuition on why they are observing these differences? It would be good to add this intuition into the paper more explicitly.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies how new information can be learned by different sets of neurons in LMs. The paper divides facts a model might encounter into novel, familiar, and dissonant categories. These categories can be automatically detected via classifiers that take in statistics about model activations/gradients on the new data as well as historical activations/gradients from earlier model training. Once a new fact's category is identified, the same activation/gradient statistics can be used to categorize model neurons into stubborn or plastic categories. In particular, the paper proposes to learn new facts in plastic neurons (neurons with high gradients for the new fact) that are not already in the “stubborn” category (neurons with high gradients historically). Experiments aim to show how limiting optimized model parameters to these neurons (weights corresponding to these neurons?) leads to more effective learning of new information while retaining old known information. Experiments are conducted with GPT2-small and GPT2-xl on CounterFact data augmented with LLM-generated data. Results show that it is good to avoid using stubborn neurons to learn new facts, although randomly selecting neurons performs about as well as any other method in practice.

### Strengths
- Important: The core ideas in the paper are quite interesting. Model editing and continual learning may benefit from first classifying information as novel/familiar/counterfactual in order to decide how to best handle incorporating it into the model. Localizing gradient updates into particular weights or subspaces has proved successful historically, and it stands to reason that more interpretability results could help improve the localization further.
- Important: The choice of datasets is reasonable, and the plots communicate the results well. The experiments properly test the main claims in the paper.

### Weaknesses
 - Very important: The results sections, as well as the abstract/into/discussion, tend to gloss over the fact that the random neuron selection does quite well compared to any other selection method. I can buy that one should be avoiding stubborn neurons — that seems empirically supported. But it seems like the rest of the positive claims in the paper fall through based on this result regarding random selection. In particular, both Fig 3 and Fig 4 show that random neuron selection does very well, and I feel like this undermines the core claims of the paper. My remaining uncertainty here concerns the fact that you can do well with fewer neurons. But then eventually the random neurons selection catches up, and can even perform favorably to specific/candidate neurons in some respects (like maintaining old knowledge, in some subplots). What are we to make of this? 
- Important: Why try to do activation/gradient classification to determine what facts are new or old to the model? There is a simple missing strategy here, which is to use model probabilities for p(o|s,r) and p(”s r o”), obtained from the LM. These features should be sufficient to distinguish between novel, dissonant, and familiar statements. Now, one might say that the strategy in this paper is reasonable, and this is simply an alternative. But the issue is that using model probabilities as features is much easier and more scalable than using (historical) activation and gradient statistics. And it undermines the surprise of the main claim, which is that these properties of the facts are detectable from model internals. It can be entirely unsurprising that these fact properties are detectable from model internals when some of the entities in the facts are made-up, like made-up names, languages, or places. These properties would be detectable from surface features of the text alone, and therefore would likely be detectable based on hidden representations as well. Do the models represent things that a simple probe would not? I am not sure (see: https://aclanthology.org/2021.emnlp-main.122/).
- Important: The paper conducts most of its analysis on GPT-2 small and GPT-2XL, which are not very representative models these days for work on knowledge editing. 
- Important: There’s another overclaim in the Discussion, about MEMIT. One of the proposed methods gets a better harmonic mean score than MEMIT. These results aren’t really comparable because they are at very different points on the Pareto curve of new vs old knowledge accuracy. It is hard to say this is an apples to apples comparison. Different scales of the metrics would produce different harmonic means favoring one method or the other. 
- Of some importance: The paper is unclear about some details. See questions.

### Questions
- Where do the labels for novel/familiar/counterfactual data come from? More information on this dataset for classifier training would be helpful.
    - Can you specify whether the novel facts use new subjects, relations, and/or objects?
- I feel that the feature importance section doesn’t add much to the current draft (and it seems like the authors might agree it is not central).
- The abstract doesn’t really need to mention future work.
- I feel that the limitations section in the introduction does not add much to the paper, besides trying to pull back some of the confident claims in the abstract/intro.
- In 2.1 you could specify what training process you’re talking about. Is it pretraining?
- To select plastic neurons, do you look for HG near 0, or very negative? I think this is not clear from the notation.
- L.150 - is this a typo “eventually first”?
- L.258 typo: “famliar”
- L.323: “traiend”
- L.506: “outperfors”
- For reference, here is another early work on model editing and continual learning in LMs: https://arxiv.org/abs/2012.00363

### Soundness
2

### Presentation
3

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
This paper introduces a novel approach to help large language models (LLMs) update their knowledge without catastrophic forgetting, inspired by human cognitive processes. The authors propose two main components: (1) a mechanism to classify new information as novel, familiar, or dissonant using activation and gradient patterns, and (2) a targeted update strategy that identifies "stubborn" (frequently used) and "plastic" (rarely used) neurons based on historical gradient information. Through experiments on GPT-2 models, they show that their approach can effectively classify information types and that targeted updates help preserve existing knowledge when incorporating non-conflicting information. However, they find that updating with conflicting (dissonant) information remains challenging and destructive to prior knowledge, even with their targeted approach.

### Strengths
The paper introduces several ideas that are quite original; they make insightful use of inspiration from human cognitive abilities, such as dissonance and familiarity awareness, and the innovative application of these ideas to LLMs for continual updates. The introduction of dissonance awareness as a mechanism for classifying information into novel, familiar, or conflicting is cool.

 The use of historical activation and gradient information to classify neurons into "plastic" or "stubborn" is interesting. The use of activation and gradient patterns for dissonance detection is also interesting.

Altogether, this study aims to contribute to a critical challenge in LLM deployment (continual knowledge updates).

### Weaknesses
Nevertheless, this paper has a number of major shortcomings.

First and foremost was that their paper was at times quite unclear and difficult to read. Procedures for their analysis e.g. how they classified input information, were disconnected and took a substantial amount of time to piece together. The authors should be encouraged to better organize their methods in a more optimal way so that the readers can have a more crystal clear picture of what they did.

1. Assuming I have pieced together their method correctly: their definition of dissonance awareness does not actually come from some unsupervised procedure on the activation / gradient patterns alone. They use the COUNTERFACT dataset which already contains labeled pairs of facts and their contradictions to train their classifier. To what extent is such a classifier works at all, out of distribution, is uninvestigated and is a limitation if further experimentation is not done. I highly encourage the authors to do this because their idea of this classifier is one of the main novelties of their paper.

From what I can gather: the authors did generate "new" facts using GPT-3.5 but this, too, was done by modifying COUNTERFACT facts and is therefore quite in-distribution.

2. From the paper, they developed 4 different strategies for selecting which neurons to update when learning new inputs. The authors claim that their strategies beat state of the art, but it is apparently from the results that the baseline results are already quite saturating even without any careful selection of neurons to update.

Moreover, all 4 strategies struggle in the dissonant information case, the most interesting learning scenario by far, so this scenario remains unsolved even with their 4 strategies.

Is there a non-saturated scenario in which the 4 strategies outperform other methods?

### Questions
Please address the 2 points in weakness above.

### Soundness
4

### Presentation
2

### Contribution
3
