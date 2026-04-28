# What Matters for In-Context Learning: A Balancing Act of Look-up and In-Weight Learning

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
Large Language Models (LLMs) have demonstrated impressive performance in various tasks, including In-Context Learning (ICL), where the model performs new tasks by conditioning solely on the examples provided in the context, without updating the model's weights. While prior research has explored the roles of pretraining data and model architecture, the key mechanism behind ICL remains unclear. In this work, we systematically uncover properties present in LLMs that support the emergence of ICL. To disambiguate these factors, we conduct a study with a controlled dataset and data sequences using a deep autoregressive model. We show that conceptual repetitions in the data sequences are crucial for ICL, more so than previously indicated training data properties like burstiness or long-tail distribution. Conceptual repetitions could refer to $n$-gram repetitions in textual data or exact image copies in image sequence data. Such repetitions also offer other previously overlooked benefits such as reduced transiency in ICL performance. Furthermore, we show that the emergence of ICL depends on balancing the in-weight learning objective with the in-context solving ability during training.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies the origins of in-context learning (ICL) in a toy setup. Authors find that:

1. The presence of almost exact copies of a given sample in the model's context substantially promotes ICL.

2. ICL is diminished when the in-weight learning task is easy (as the model can solve the task without using context). On the other hand, harder tasks require both IWL and ICL, and hence the commonly observed ICL transiency (ICL disappearing as IWL performance increases) diminishes in harder tasks.

### Strengths
1. Timely topic and a relatively straightforward methodology for studying it.

2. I liked Figure 1 with plots of n-gram repetition in real corpora -- it's a good motivation for the toy setup in the paper. (I was keen to see a deeper investigation along those lines but only found toy experiments.)

3. The related work section is comprehensive, and I found it useful.

4. I liked the experiments in Section 5, though I'm not familiar enough with prior work to assess novelty.

### Weaknesses
The main weakness is that the core experiment in Section 4 is presented poorly, to the extent where I'm still not sure what precisely is going on even after going through the paper several times.

1. I don't get the difference between (3xQ-3xA-B-C) and (3xQ-3xA-B-C iCopy). Is the difference that in the iCopy setup, the three A and the three Q images in the context are copies of one another, whereas in the setting without iCopy they're different images with the same label? Also, does this only apply to the training data, or are test datasets also different between iCopy and no-iCopy?
    - a) More questions about iCopy description: What is conceptual repetition -- is it just different images of the same class, or is that exact repetition? What kinds of augmented versions of the images are used in iCopy?


    - b) It'd be helpful to clearly describe the difference between the baseline and iCopy settings -- perhaps by moving the baseline subsection into Section 4, or by adding a figure illustrating the difference.
    - c) Relatedly, I did not get an explanation in the Baseline subsection, from *>We think this happens ...* until the end of the paragraph.

2. I did not understand Figure 5: I'm not sure what to look for in these plots re induction heads -- how can the authors tell the induction head from the attention maps? I assume this has to do with the darker "columns" in subplot d? Also, I think it'd be helpful to add a description of induction heads to the related work section, as opposed to just mentioning them.


3. How is IWL performance measured? Is it zero shot?

### Questions
>In our setup, ICL transiency is eliminated by using repetitions in the data sequences and using a complex in-weight learning objective.

This sentence (with the context of the rest of the paper) makes me think that repetitions make ICL a relatively easier way to get low training loss compared to IWL. So you can get more ICL either by making ICL itself easier (repetition), or making IWL harder (your section 5) -- either way what matters is the balance of ease of ICL vs ease of IWL, and the usefulness of each for reducing the training loss. 

Does the above seem right to the authors? If so, highlighting this point about the balance between ICL and IWL difficulty could be helpful, as it seems to unify many of your findings.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
- The authors analyze the relationship between conceptual repetition (e.g., burstiness, skewness) and ICL performance on vision-language few-shot learning tasks.
- The key take-aways are:
    - Simple repetition of the query (i.e. iCopy) in the given prompt/sequence of examples is sufficient for allowing ICL to emerge by developing in-context look up ability
    - Skewness, although helpful because they help create a more difficult IWL task, may not be necessary
    - A possible explanation of this phenomenon is through better construction of induction heads
- Given these key take-aways, the authors attempt to build on the data distributional properties for the emergence of ICL [1] and try to generalize these findings to the general LLM domain. However, this connection is weak and not supported by any experiments in the paper. it is not clear what iCopy may be equivalent to in the language domain and how these insights carry over to helping us understand the important properties of language pretraining.

[1] Chan, Stephanie, et al. "Data distributional properties drive emergent in-context learning in transformers." Advances in Neural Information Processing Systems 35 (2022): 18878-18891.

### Strengths
- The authors expand on the work of Chan et al. 2022 [1] to not only confirm their findings on the importance of the skewness and burstiness in the pretraining distribution for language, but also show that under the iCopy data construction regime, skewness may not be important and attempt to analyze why it is so (from the induction head perspective).

### Weaknesses
 - The authors run experiments to investigate the relationship between conceptual repetition (e.g., burstiness, iCopy, etc) and ICL performance on vision-language few-shot learning tasks and try to generalize the observations to the LLM domain. However
- Some of the design choices for the experiments (like the baseline configuration, the objective function that only computes/backpropagates the loss on the query pair) are not justified and require clear explanation or empirical analysis. These questions are further expanded in the questions section.

### Questions
- How are the evaluation data samples constructed? (in both of the 2-shot and 4-shot settings)
- What’s the rationale behind why the authors choose the baseline model to be a mix of 10% and 90% of standard and in-context sequences? Is there perhaps an ablation on changing this ratio?
- When autoregressively trained on the Omniglot few-shot learning dataset, my understanding from the paper is that only the loss after 2L pairs of image-label examples is computed and used for training. Why do the authors choose this paradigm, instead of backpropagating the losses on all y_i along the sequence like in standard language modeling? How do the results change if we change the training objective to be autoregressive as well?
- In the experiments for Figure 6, with smaller # of classes, to achieve the same number of training steps, do you train over multiple epochs of the same dataset? Is it possible that these models are perhaps overfitting? Are there any training curves that we can analyze for this? Overall, it would be important to illustrate the validation performance on the IWL task and have that in the context of analyzing the ICL performance.
- This may be an experiment hard to run during the rebuttal, but how does the model size interplay in the ICL emergence with these different variables of burstiness, skewness, complexity of data (# of classes), etc, given that people have observed that ICL only emerges at some scale of model size?

### Soundness
2

### Presentation
3

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
In this paper the authors investigate the mechanisms behind In-Context Learning (ICL) in Large Language Models (LLMs). They argue that conceptual repetitions within training data sequences play a crucial role in enabling ICL. This view is contrasted to other explanations including the importance of data distribution and burstiness. The repetitions facilitate a "look-up" mechanism (essentially a copying mechanism performed by an inductive head) where the model learns to solve the task by recognizing the same pattern in the sequence and copying its associated label. The authors also highlight the significance of a complex in-weight learning objective in achieving stable and non-transient ICL performance. This complexity prevents the model from overfitting to simple patterns and encourages robust generalization.

### Strengths
1. The publication is sufficiently clearly written. While it does occasionally make qualitative statements without referring to any specific figure, section or result (for example, “We observe that it is not possible to obtain a clear ICL performance with the same architecture using only the high-burstiness strategy…”), it generally refers to empirical evaluations and has a sufficiently well thought out experimental section.
2. While being quite simple, the proposed techniques and ideas are sound. For example, it is entirely believable (even obvious and in the absence of careful experimental evidence) that copying a query example into the context would jump-start and incentivize the model to rely more on a simple “lookup” ICL mechanism. 
3. The authors designed a reasonable set of experiments to study their proposed iCopy mechanism (as well as the effect of the label distribution, label noise and an instance discriminative task).

### Weaknesses
1. _Novelty_. In my opinion, this publication is quite incremental and it does not seem to make any significant conceptual leaps on top of the pre-existing work. The importance of the copying mechanism and understanding the role of inductive heads has been the subject of many prior publications. The central idea of the paper that label copying mechanism can be incentivized by directly copying the query sample is in my opinion too obvious. As one example, (Chan et al., 2022) has arguably made an intermediate step towards the iCopy setup by considering a dataset with a single Omniglot exemplar image. The present paper, among other things, does in some sense generalize this setup by allowing the context to contain the same exemplar image, while using many more exemplar images overall. However, I do not see this as a major leap.
2. It is hard to extend the proposed mechanisms beyond this simple few-shot learning setup. The proposed idea can be viewed as a form of data augmentation, where the sequence is enriched with the information necessary to promote a particular lookup mechanism. However, for real applications including most natural language tasks, this data augmentation (and in-context learning mechanism it empowers) are too naive. For example, rephrasing natural language sentences, changing their attributes, adding reasoning steps, etc. typically requires a separate teacher/oracle model and can be quite non-trivial and noisy [(Arthaud, 2021, Few-shot learning through contextual data augmentation), (Peng, 2023, Controllable Data Augmentation) and many more].
3. The simple copying mechanism studied here can actually be even damaging beyond the simple few-shot learning setup. In fact, there is ongoing work on “mitigating  the copying bias” (Ali, 2024, Mitigating Copy Bias in In-Context Learning through Neuron Pruning). Points 2 and 3 suggest to me that the iCopy mechanism may be a proper conceptual step for studying ICL in a simple few-shot learning setup, but may be inappropriate and difficult to re-interpret for most other complex in-context learning mechanisms.

### Questions
1. The core iCopy mechanism employed by the authors relies on a simple strategy: directly copying query examples and putting them into the context. This encourages the embedding model to produce reasonable sample embeddings and the Transformer model to perform ICL by attending to similar embeddings and replicating their associated labels. This may be suitable for some few-shot learning tasks with clearly defined sample embeddings, but this mechanism may be too simplistic for more complex forms of in-context learning including those necessary for most natural language tasks. There much more complex sequence processing and reasoning appears to be important. Relying on simple copying could even be damaging in these applications. In this light, what are potential tasks or applications where iCopy mechanism could actually be utilized to improve complex in-context learning capabilities?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
LLMs have shown the capability to learn from context examples, while the mechanism behind ICL remains a black box. This paper explores the emergence of In-Context Learning capability of LLMs by introducing a controlled dataset and data sequences for the training process of a deep autoregressive model like GPT-2. The results show that conceptual repetitions in the data sequences are crucial for the ICL capability. Besides, the emergence of ICL also depends on balancing the in-weight learning objective with the in-context solving ability.

### Strengths
1.	The authors provide a new perspective for viewing the emergence of in-context learning capability, revealing the importance of conceptual repetition and IWL objectives.

2.	The proposed iCopy has proved effective in enhancing the in-context learning capability.

3.	The experiments are carried out across various vision datasets, which makes this paper more convincing.

### Weaknesses
1.	The presentation of this paper is not clear enough. For example, the sequence 3xQ-3xA-B-C is confusing initially. And the sequence (Q-A-B-C-D-E-F-G iCopy) also does not show which character symbol is repeated. Meanwhile, the use of “Q” and “A” could hint at the Q-A pairs, also increasing the difficulty of reading.

2.	Although the authors claim “conceptual repetitions” is crucial for the in-context learning capability, considering that “conceptual” also includes pure textual tokens, this paper does not conduct experiments on pure text tasks.

3.	Meanwhile, the real in-context learning tasks are much more complex compared to the settings in this paper. Actually, the selection of the examples will also influence the results due to the correlation between the examples and the current query.

### Questions
1.	Could the authors explain more about the formation of the sequences?

2.	Is there any experiments or evidence for reaching the same conclusions on pure text tasks?

3.	I am still concerned about the correlation between examples, which could influence the ICL prediction results. Do the authors agree with this point? If so, is there any method to evaluate the influence and try to relieve it?

### Soundness
3

### Presentation
3

### Contribution
3
