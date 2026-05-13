# Understanding Mistakes in Transformers through Token-level Semantic Dependencies

- Decision: Reject
- Scores: 3, 3, 5, 6, 3

## Abstract
Despite the high performance of the transformer model, it sometimes produces incorrect information. To understand the cause of this issue, we explore how semantic dependency is learned within the model. Specifically, we investigate how tokens in multi-head self-attention transformer models encode semantically dependent information.
To help us identify semantic information encoded within a token, intuitively, our method analyzes how a token's value shifts in response to changes in semantics. BERT, LLaMA, and GPT models are analyzed.
We have observed some interesting and similar behaviors in their mechanisms for encoding semantically dependent information:
1). Most tokens primarily retain their original semantic information, even as they pass through multiple layers.
2). A token in the final layer usually encodes truthful semantic dependencies.
3). The semantic dependency within a token is sensitive to both irrelevant context changes and the order of contexts.
4). Mistakes made by the model can be attributed to some tokens that falsely encode semantic dependencies.
Our findings potentially can help develop more robust and accurate transformer models by pinpointing the mechanisms behind semantic encoding.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates how the semantic dependency encoded by tokens change within the model architecture, and how it influences the prediction of the model. The authors discuss that (1) many tokens' semantics do not change with deeper layers; (2) a token also encode information of semantically related words; (3) changes of context, even irrelevant, can change the semantic dependency; (4) when models make mistakes, there are erroneous semantic dependency.

### Strengths
This paper tackles an important problem about understanding the model’s erroneous behavior by looking into the internal activations. The authors’ attempt to attribute the model’s prediction to semantic dependency can be a meaningful trial towards a more broad mechanistic understanding of the connections between internal activation and model behavior.

### Weaknesses
I feel the conclusions draw by the authors are in general discussed by existing literature and known by the overall language model community, and may not be strong enough to make a ICLR paper. Specifically:

- The conclusion that the model’s activation does not change much through layers is already observed by a thread of work, based on which there are techniques derived like early exist: Liao et. al. 2021, Schuster et. al. 2022, Elhoushi et. al. 2024.
- The conclusion that language models behavior changes with perturbation by irrelevant context is observed in Shi et. al. 2024.
- The conclusion that model mistakes can be attributed to incorrect dependency is also observed in Wu et. al. 2024.

Given the listed works, I tend to feel that this work is more or less describing the conclusions that are already aware by the community (though with their own metrics).

In addition, I find it difficult to read and navigate notations from line 265, page 5 to line 347, page 7, mostly because the authors use a large set of symbols without clearly state their definition and the motivation of using them. This part of the paper may require significant rewrite and clarification. I would suggest the authors may compile a list of symbols to clarify the meaning of all symbols and the motivation of using them, and maybe use diagrams and specific examples to illustrate the procedure described in Section 3.

### Questions
See above weakness section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies how semantic information from a sequence is encoded and aggregated in a single token position. They find that the information initially contained in a token is mostly retained at that position, that how the context information is aggregated in a token can be influenced by irrelevant context, and how some mistakes can be attributed to incorrect information propagation in a token.

### Strengths
* The paper does its experiments on different models across several model families (BERT, Llama, GPT).
* The framework of understanding mistakes are caused by erroneous information propagation is interesting. While it is likely that not all mistakes are caused by this type of error, this mechanism seems to be a promising way of understanding how transformers can get answers wrong.

### Weaknesses
 * The paper is hard to follow and read. For example, the key terms 'semantic information' and 'semantic dependence' is not defined. Semantic dependency seems to be defined later in section 3 at L273, but it seems to be a pretty general definition that makes categorising false dependencies in Section 4 based on a post-hoc 'dependency is false if the answer is wrong'.
* There seems to be not much applications or possible interventions based on these findings. For example, we already know that LMs can be distracted by irrelevant contexts or context changes [2].
* The claim of 'understanding mistakes' is too broad, as they study only question-answering tasks where the answer already exists verbatim in the context.
* The paper does not discuss any related works on interpreting how information flow in transformers to answer questions, such as [1].

### Questions
* In L303, are the 10,000 cases described a subset of the 600,000 token cases described in L249? If so, how were these cases chosen?
* Detecting errors require you to know which tokens are incorrect to begin with. Do you have any potential application of detecting potential QA errors at scale without prior knowledge of the ground truth?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines where information is stored in transformer language model tokens, and how it moves through the layers. For example, how "white" gets attached to rhinos in "white rhinos". The authors use minimal pair counterfactuals to judge how changing one token in the input of the model changes the value in a later layer. The authors use this to show that individual tokens contain mostly their own info ('rhinos' contains 'rhinos' information) and when models make mistakes when making predictions about some token, it is because the wrong information from context gets attached to that token.

### Strengths
The authors outline several interesting research questions related to the movement of information within individual tokens and explain cases of irrelevant information moving into the representations of key tokens that cause incorrect answers. I think the questions are interesting and the problems being addressed have been observed for some time, although there has not been a principled study on movement of semantically dependent information across layers to my knowledge.

This work connects nicely to previous work on "attention is not explanation" (e.g.,  https://dl.acm.org/doi/10.1145/3447548.3467307 ), but i think it does not expand enough on this body of work

The authors consider a range of models, including encoder-only models like BERT, which I think is a strength for this kind of study

### Weaknesses
While this work is original, I'm not sure how much the findings weren't already understood to be the case. For example, distracting text causing performance drops is well known. The authors show that this is due to semantic information from other tokens being encoded in the correct token, but the methods that show the extent to which this is true do not explain enough about how this information is stored in the model. If we really understood how this was represented in (and intruding on) a given token, we would be able to remove it. This information belongs to some value vector(s) that copied the information in some attention operation. Can that be localized? I am generally positive about this paper, but I believe it could go a bit deeper in its analysis to better quantify why certain failure modes take hold.

The figures are unclear and sometimes poorly annotated. For example, figure 2 text should be much larger and it should be more apparent what "score" is. Figure 3, it is unclear what the numbers are next to the arrows

Typos and suggestions:

* L15: semantic dependency is redundant. I would suggest rewriting parts of the abstract to be a bit more descriptive

### Questions
Can MLPs introduce erroneous semantic information in the early layers? for example, see https://arxiv.org/abs/2304.14767

### Soundness
3

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
This paper delves into the internal mechanisms of transformer models to explore how semantic information is propagated and aggregated across tokens, which can contribute to the errors produced by large language models (LLMs). Experimental results under four settings have illustrated several useful findings.

### Strengths
1. The motivation and flow of this paper is clear.
2. Experimental results have demonstrated several useful findings.

### Weaknesses
1. Figure 1 is not illustrative enough. For example, in Figure 1c, it is hard to understand the key idea, why the two arrows are in the opposite direction? Why one sequence has green followings and the other does not? The answers cannot be found until reading line 112-120 (and still confusing).
2. Line 184: if the perturbation token is sampled randomly, it is possible that the semantic information of the original sentence does change a lot due to the perturbation token, meaning that the semantic information change may due to the dependency between this perturbation token and the other token in the original input. Thus, the authors may need to consider all the tokens in each sequence when calculating the average change of the jth token.
3. The experiment results in Table3 also reflects what I have mentioned in point 2.
4. The notations can be clearer.
5. It seems that only one NLP task (QA) has been investigated. It seems that wrongly aggregate information may affect tasks like reasoning and in-context learning. Maybe the authors can investigate more tasks to obtain more comprehensive results.

### Questions
Please see the above weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper uses perturbation analysis to understand how individual tokens in the input of a Transformer affect the contextualized representations at the output of a Transformer. Essentially, they randomly replace various input tokens and measure the L2 difference on the encoded token representations. The paper studies how these dependencies relate to linguistic notions of semantic dependency. The paper also studies how seemingly irrelevant context affects the contextualized representations. Finally, the paper studies the correlation in prediction errors with deviations from the expected dependency relations.

### Strengths
* It was nice to see comparisons across models spanning from BERT to LLama3. It was interesting to see trends across the various analyses with respect to modeling advancements across time.

* It’s potentially interesting to connect errors in model predictions to errors in propagating information correctly between tokens.

### Weaknesses
Overall weaknesses:

* The paper is structured as a sequence of loosely related experiments and analysis. It was a bit difficult to understand which findings were new and interesting. I think the paper could be improved by *removing* some content or deferring it to the appendix in order to focus and expand on the most interesting results.
* It would have been nice to contextualize the methods and findings more in prior work, e.g. probing studies (e.g. summarized in Rogers et al. 2020, https://arxiv.org/abs/2002.12327) and studies related to robustness to adversarial changes in context (e.g. Jia & Liang 2017, https://arxiv.org/abs/1707.07328). It would have been nice to have included discussion of in what cases the authors' findings are validating those of prior work vs. contradicting.
* Additionally, in many cases it seems the authors invent new metrics or experimental methodologies without discussing how such metrics or methods compare with those proposed by prior work.

Section 2

* The definition of `P(f_\theta)` was difficult to parse. Should `M` be `N` and `m` be `i`? It might also be helpful to remind the reader of the indicator function notation being used.
* It seems like it would make more sense to refer to this quantity as a “percentage” than a “probability”? (Here and elsewhere in the paper, too)
* Are there metrics from prior work that could have been chosen instead to measure the saliency of various input tokens on contextualized representations in the output?
* It wasn’t clear what the take-away was for the finding here. Should we be surprised that the most salient input for a given output token is the corresponding input token?
* Given the significance of casual attention mask on the analysis, it might be worth explicitly denoting in Tables 1 and 2 which models are decoder-only vs. encoder-only.

Section 3

* This analysis relies on a neural dependency parser, so although the analysis is presented as analyzing the degree to which dependencies in contextualized representations encode “semantic dependencies”, it might be helpful to clarify that the analysis is actual measuring agreement with a neural dependency parser model rather than some "ground truth" notion.
* It would have been useful to connect the methodology and findings with prior work that has studied the degree to which Transformer representations capture linguistic notions of syntactic or semantic dependencies.
* Prior work on probing could provide an alternative to the perturbation-based analysis, which has some limitations (as discussed by the authors towards the end of the paper).

Section 4

* I think this section is potentially the most interesting, because it could be interesting to attribute prediction errors to cases where the model appears to misunderstand the syntactic or semantic dependencies between tokens. However, I have some concerns about the methodology.
* It would be useful to show the % of cases where the incorrect answer has higher saliency than the correct answer for “correct cases” as a comparison point for Table 4.
* The experimental methodology seems a bit circular. The intended conclusion is that for cases where the model chooses the incorrect answer, the incorrect answer has higher saliency towards the question tokens than the correct answer. This doesn’t necessarily seem to be surprising, and it’s not clear what is actionable about this finding.

Nits
 
* The terms “unfaithful” and “semantically dependent information” appear in the abstract without clear definitions. It wasn’t clear to me what their meaning was in this context. Perhaps this could be clarified to improve readability of the abstract.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
