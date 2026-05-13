# Scalable Influence and Fact Tracing for Large Language Model Pretraining

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Training data attribution (TDA) methods aim to attribute model outputs back to specific training examples, and the application of these methods to large language model (LLM) outputs could significantly advance model transparency and data curation. However, it has been challenging to date to apply these methods to the full scale of LLM pretraining.
In this paper, we refine existing gradient-based methods to work effectively at scale, allowing us to retrieve influential examples for an 8B-parameter language model from a pretraining corpus of over 160B tokens with no need for subsampling or pre-filtering.
Our method combines several techniques, including optimizer state correction, a task-specific Hessian approximation, and normalized encodings, which we find to be critical for performance at scale.
In quantitative evaluations on a fact tracing task, our method performs best at identifying examples that \textit{influence} model predictions, but classical, model-agnostic retrieval methods such as BM25 still perform better at finding passages which explicitly contain relevant facts.
These results demonstrate a misalignment between factual \textit{attribution} and causal \textit{influence}.
With increasing model size and training tokens, we find that influence more closely aligns with factual attribution. Finally, we examine different types of examples identified as influential by our method, finding that while many directly entail a particular fact, others support the same output by reinforcing priors on relation types, common entities, and names.
We release our prompt set and model outputs, along with a web-based visualization tool to explore influential examples for factual predictions, commonsense reasoning, arithmetic, and open-ended generation for an 8B-parameter LLM.\footnote{\demourl{}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose TrackStar, a gradient-based influence method which works effectively on a 8B LM pretrained on 160B tokens, without the need for filtering or subsampling. The proposed method performs well at identifying instances which influence the model prediction, but model agnostic methods suc as BM25 still outperform it at finding passages which contain explicitly relevant facts. The paper delves into the problem of misalignment between factual attribution and causal influence, which they show becomes a smaller issue when scaling models.

### Strengths
- Well written and motivated, easy to follow, very comprehensive exprimental evaluation with ablations and subsequent error analyses
- Scales up TDA to large models, corpora and number of targets
- Identifies and demonstrates a misalignment between attribution and influence
- Empirically shows that influence becomes closer to attribution when scaling models

### Weaknesses
The only drawback I see is not delving deeper into the mismatch between infuelnce and attribution, however this is understandable as it is worthy of a separate paper.

### Questions
Tail-patch probability increase works worse with model scale (Fig 2). Do you believe this to be caused by a single instance mattering less for a larger model, or due to the inherent better performance of the underlying model? It would be interesting to distribute these scores for cases where the underlying model was right/wrong in its prediction.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a method for training data attribution that works effectively at scale. The proposed method relies on gradient-based estimations, where the authors combine several techniques such as optimizer state correction and normalized encodings to improve its attribution performance. Experiments on an 8B model pretrained on a corpus of over 160 billion tokens show the effectiveness of the proposed method and its different design choices. There are also some other interesting findings such as the misalignment between examples that can fully entail the target and examples that have actual high influence on model prediction.

### Strengths
- Training data attribution is very important for understanding the connection between training data and the model's learned behaviors, and scalability is one key criterion especially nowadays when the model/data are large. The method this paper introduces is shown to be both more scalable and more effective than previous methods.

- The ablation experiments are thorough and clearly show the effectiveness of the various design components of the proposed method.

- The findings/analysis on the misalignment between factual attribution and causal influence are very interesting and could be a good inspiration for the community to understand LLM's behaviors around factual prediction.

### Weaknesses
- The different design components of the proposed method are mostly adaptations of previously proposed ones, whereas the proposed method is a combination of them. Hence, the technical novelty of this work is a bit limited.

- Overall, the proposed designs are quite heuristical and not very solidly justified. For example, why *can* we enforce a block-diagonal structure for the auto-correlation matrix or perform unit normalization on the input vectors? What are the assumptions for doing these and are there some theoretical basis for them?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies extending influence functions to LLMs by modifying key components of TRAK (Park et al., 2023) such gradient computation, correction, and input processing (e.g., vector normalization). The authors applied their approach, dubbed TRAKSTAR, to a decoder-only model with 3 different sizes pretrained on the C4 dataset and compare to TRAK and other retrieval based approach. They found their approach to perform better than influence-based method, but to perform much worse compared to retrieval-based approaches. 

This leads them to investigate the mist-alignment between attribution and influence (Section 7, the part that I find most interesting in the paper) and show that LLMs rely on priors for predictions---not just entailment. They perform an analysis on error cases.

### Strengths
* I like how the paper discusses difference/discrepancy between attribution and influence. I think this discussion could be useful to future work. 
* I found the error analysis in section 7 to be interesting.
* Different design choices are well-ablated. 
* The proposed approach outperforms influence-based baselines at retrieving influential examples.

### Weaknesses
* The tail-patch metric used to evaluate influence will probably depend on the templates used. It is unclear how reliable such metric is.
* If I understood correctly, the hessian approximation proposed requires access to an evaluation dataset. The authors should explain how this would work in the case of no have access to the full evaluation dataset. 
* It seems to me that lots of "hacks" are needed to get the approach to work (e.g., gradient correction, normalization, gradient compression via projection etc.) But I suppose this is a limitation of influence functions rather than of the proposed technique.
* It is unclear to me that scaling influence functions to LLM is practical/reliable at all, as it seems that spurious correlations between the input fact and the pretraining examples to play a big role. For instance, looking at the errors provided in the Appendix, many of the retrieved proponents seem to completely unrelated to the fact-- some don't even have any word overlap such as example ID 862.

### Questions
* You mention that you manually write natural language templates for all 97 relation types. I wonder how much will the results rely on these templates? Do you have experiments with different template variations? 
* Could you provide a discussion on real-world scenarios where scaling influence functions to LLM would be helpful/practical?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes TrackStar, a scalable, gradient-based influence tracing method for large language model (LLM) pretraining. It aims to identify influential training data examples for model predictions, enhancing model transparency. To achieve TrackStar, the authors compute the influence between two examples as the dot product between the projected and
corrected model gradients for those examples. TrackStar outperforms prior influence methods in identifying examples that entail a fact (attribution) and influence predictions (causal impact), though classical retrieval methods like BM25 still excel at attribution. They further analyze the effectiveness of TrackStar using extensive experiments.

### Strengths
- The paper addresses a critical gap in training data attribution (TDA) by scaling to pretraining setups, which may be further used for efficient pre-training or transparent training.
- Experiments are well-designed, covering a range of models (up to 8B parameters) and extensive datasets, including T-REx and C4, to validate TrackStar’s effectiveness.
- The authors offer a detailed analysis of the distinction between influence and attribution, adding clarity to how models use training data.

### Weaknesses
- ''For each fact, there are an average of 2.5 “ground-truth” sentences out of 19.6M sentences total''. Does this mean any training or testing examples contain 2.5 relations? The statement needs further clarity.
- In the experiments, although the pass rate of records extracted by StarTrack is lower than that of BM25, training a model on StarTrack's examples leads to greater improvement. I wonder if limiting the selection to only the top 3 or top 5 examples—or even just the top example—would reverse this outcome.
- For C4 evaluation, an NLI model is used. However, the accuracy cannot be fully guaranteed since C4 consists of longer documents. Human annotation of a subset is needed.

### Questions
Please see the weaknesses. I have no more questions. I will improve my rate if you can address my concerns

### Soundness
4

### Presentation
4

### Contribution
3
