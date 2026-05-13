# Linearity of Relation Decoding in Transformer Language Models

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
\looseness=-1
    Much of the knowledge encoded in transformer language models (LMs) may be expressed in terms of relations: relations between words and their synonyms, entities and their attributes, etc.
    We show that, for a subset of relations, this computation is well-approximated by a single linear transformation on the subject representation.
    Linear relation representations may be obtained by constructing a first-order approximation to the LM from a single prompt, and they exist for a variety of factual, commonsense, and linguistic relations. However, we also identify many cases in which LM predictions capture relational knowledge accurately, but this knowledge is not linearly encoded in their representations.
    Our results thus reveal a simple, interpretable, but heterogeneously deployed knowledge representation strategy in %
    LMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work focuses on analyzing the computation of LLM in the tasks of knowledge decoding. The authors find that a certain kind of computation in relation decoding can be approximated by linear relational embeddings such that R(s) = \beta Ws + b. Specifically, the intermediate hidden representation of subject is used in this linear transformation. With experiments on 47 different relations, the authors find that for some relations the linear approximation hold. However, this linear attribute is not universal. Furthermore, the authors conducted experiments to show the causality of the linearity of relation decoding. Finally, a visualization tool called attribute lens is proposed to show where and when the LM finishes retrieving knowledge about a specific relation.

### Strengths
This work focused on an interesting question about what computations the LMs perfrom while resolving relations. The authors smartly use the local derivative to obtain the affine transformation approximation. This is aligned with the traditional design in training knowledge graph embedding. Also, it is very useful to show that causality of the linearly decoding behavior, by using a low-rank pseudoinverse to obtain the perturbation of subject.

### Weaknesses
It is unknown that how the context prompt (e.g., [s] plays the) affects the conclusion. For example, will the conclusion hold if we change some other contexts that express same meaning of relation? Though it is interesting to show that some relations matches the linearity hypothesis (e.g., occupation gender, adjective comparative) which aligning traditional methods of training knowledge graph embedding, my concern is that the faithfulness is not very high for most of relations. This paper is more like a case study instead of a systematic measurement which covers a broader range of relations. It is hard to conclude how much percent of relations match the hypothesis. 
Furthermore, it is unclear, if I did not miss some texts, why the causality is usually higher than faithfulness.

In term of handling objects that have multiple tokens, I saw in Table 4: only the first token was used to determine correctness. Do we apply this strategy to all experiments? Will this lead to false positive? For causality experiment, do we also use the first token of o’ for experiment?

### Questions
In term of handling objects that have multiple tokens, I saw in Table 4: only the first token was used to determine correctness. Do we apply this strategy to all experiments? Will this lead to false positive? For causality experiment, do we also use the first token of o’ for experiment?
Do we have some examples showing that `when LRE can not fully capture the LM's computation of the relation, the linear approximation can still perform a successful edit`?
In which level of faithfulness, we can say that the linearity holds for the relation?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes how the knowledge of relational triples (i.e., subject-relation-object) can be decoded in large language models (LLMs). Specifically, the authors hypothesize that the object embedding can be computed using an affine function (i.e. LRE) from the subject embedding and show that this holds for the majority of relations tested in this work. They also show the causality of the relationship through intervention experiments where a different object can be obtained by changing the subject embedding according to the LRE.  The authors also present the Attribute Lengs, an interesting application of their observation similar to the Logit Lens, which allows one to examine what entities are predicted to be the object in intermediate layers of a transformer model.

### Strengths
- The paper presents a novel insight into how relational knowledge is represented in an LLM, which should contribute to a deeper understanding of LLMs in the field.
- Extensive experiments are carried out to confirm the findings.
- The paper is well written and easy to follow

### Weaknesses
 - The configuration for estimating the parameters of the affine functions could be further explored.


### Questions
- In experiments, n = 8 examples are used to estimate W and b. Would it be difficult to use more examples?  They seem to be too few to reliably estimate W and b.  I would also be interested in the variance as well as the mean.  
- Does a “sample” mean a single example?  In statistics, a sample usually means a collection of examples (data points).
- p. 4: of LM’s decoding -> of the LM’s decoding?
- p. 5: by (Merullo et al., 2023) -> by Merullo et al. (2023)?
- p. 7: is a higher -> is higher?
- p. 8: visualizes a next -> visualizes next?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
*update* The authors have addressed most weaknesses/errors that I have raised. I updated my score upwards as a result. */update*

It is well known that language models acquire knowledge of subjects, objects and their relations. However, to date, it is not well understood how these relations are represented in the model. The paper posits that relations are implemented as Linear Relational Embeddings, that is, affine transformations mapping from the embedding of the subject to the embedding of the object. The paper proposes to compute these mappings from the Jacobian $\delta o / \delta s$, where o and s are object and subject embeddings at certain layers, respectively.
The paper validates this approach by measuring a) faithfulness, i.e., whether decoding from the LRE mapping matches decoding from the true model when given a prompt expressing the relation, and b) to what extend this mapping is a causal explanation by providing an inverse of the LRE capable to change s such that a different, desired o results.
The experiments show that the method results in relatively high, but far from perfect, faithfulness and causality scores. The method is compared to number of reasonable baselines/ablations. Finally, the method is applied to the use case of detecting when the language model outputs false relationships despite knowing the true relationship.

### Strengths
* the paper covers an important topic that will certainly raise interest among the ICLR attendees
* the methods and results are interesting - I learned something.
* the presentation is excellent. The paper is easy to follow and results are presented in a comprehensive fashion.

### Weaknesses
 *update* The authors have addressed most weaknesses/errors that I have raised. I updated my score upwards as a result. */update*

It is well known that language models acquire knowledge of subjects, objects and their relations. However, to date, it is not well understood how these relations are represented in the model. The paper posits that relations are implemented as Linear Relational Embeddings, that is, affine transformations mapping from the embedding of the subject to the embedding of the object. The paper proposes to compute these mappings from the Jacobian $\delta o / \delta s$, where o and s are object and subject embeddings at certain layers, respectively.
The paper validates this approach by measuring a) faithfulness, i.e., whether decoding from the LRE mapping matches decoding from the true model when given a prompt expressing the relation, and b) to what extend this mapping is a causal explanation by providing an inverse of the LRE capable to change s such that a different, desired o results.
The experiments show that the method results in relatively high, but far from perfect, faithfulness and causality scores. The method is compared to number of reasonable baselines/ablations. Finally, the method is applied to the use case of detecting when the language model outputs false relationships despite knowing the true relationship.

### soundness:
 3 good

### presentation:
 4 excellent

### contribution:
 4 excellent

### strengths:
 * the paper covers an important topic that will certainly raise interest among the ICLR attendees
* the methods and results are interesting - I learned something.
* the presentation is excellent. The paper is easy to follow and results are presented in a comprehensive fashion.

### weaknesses:
 * Limitations are not discussed in enough detail. For example, given a fixed subject and relation, it is possible that there are multiple true objects. This has consequences both for the generation of the datasets (where examples are filtered out if they're not generated by the model) and questions to what extend an invertible function can be a reasonable approximation of the true function, since invertibility implies that the function/relation is injective. Discussing these aspects would improve the paper.

I am a bit skeptical with regards to some results:
* Table 4 (Appendix A) shows the number of correctly predicted relations per language model. It is quite remarkable that some models in some categories get zero percent of the facts right, whereas other models get a much larger percentage right. Zero percent hints at systematic errors that remain undiscussed in the paper. For example, the LLaMA-13B achieves zero percent on the task of predicting president's birth year and election year. This is quite curious, given that these are quite well-known facts that appear a lot in the pretraining data, and the other models get them right. There is a reason for the poor performance of LLaMA on this particular task: Their tokenizer represents every digit as its own token. However, the caption of Table 4 states that only the first token was used to determine correctness. Since the LLaMa model would require 4 tokens, it had no chance of predicting the "correct" token. IMO, this is shortcoming of the proposed measurement, and accepting this bias should at least be discussed. I suspect that similar reasons might cause zero percent accuracy on some of the other tasks.
* Table 4 (Appendix A) shows that GPT-J gets zero examples from the "occupation gender" category right. Hence, none of these examples from this category should remain in the dataset for GPT-J according to the description in Section 4 (Dataset). Curiously, Figure 3 shows that "occupation gender" has a near 100% faithfulness success rate. How can that be if there are no such examples?

### questions:
 Please respond to the weaknesses raised. I am happy to raise my score if the explanations are satisfactory.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 8: accept, good paper

### confidence:
 3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### code_of_conduct:
 Yes

### Questions
Please respond to the weaknesses raised. I am happy to raise my score if the explanations are satisfactory.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
