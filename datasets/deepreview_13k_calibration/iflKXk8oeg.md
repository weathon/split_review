# Interchangeable Token Embeddings for Extendable Vocabulary and Alpha-Equivalence

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
We propose a novel approach for learning interchangeable tokens in language models to obtain an extendable vocabulary that can generalize to new tokens. Our method is designed to address alpha-equivalence, the principle that renaming bound variables in a syntactic expression preserves semantics. This property arises in many formal languages such as temporal logics, in which all proposition symbols represent the same concept but are distinguishable from each other. To handle such tokens, we develop a dual-part embedding approach. The first part is shared across all interchangeable tokens, thereby enforcing that they represent the same core concept. The second part is randomly generated for each token, which enables distinguishability. We evaluate our method in a Transformer encoder-decoder model on two tasks: solving linear temporal logic formulae and copying with extendable vocabulary. Our method demonstrates promising generalization capabilities in addition to introducing a favorable inductive bias for alpha-equivalence.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents an approach to create embeddings for LTL (Linear-time Temporal Logic). The main challenge that is addressed is to represent tokens during inference that are not seen during training. The idea is to represent interchangeable tokens during inference instead of learning the representations during training. A part of the embedding is used to represent the similarities and tie tokens together and a second randomized part distinguishes between interchangeable tokens. Experiments are performed with large vocabularies showing that the proposed approach can learn representations for interchangeable tokens more accurately.

### Strengths
- Generalizing representations to new tokens to represent the alpha equivalence seems like a relevant and significant problem in the domain of LTL
- The method seems to be intuitive and scalable as shown by the experiments

### Weaknesses
 - Most of the contribution is based on empirical results, since the novelty of the algorithmic contribution itself is perhaps not as strong (e.g. generating the random embeddings). Given this, it felt like the experiments were not particularly strong and also presented in a way that is a little hard to follow. Specifically, the first experiment is synthetically designed with random strings. Further, it is not compared to any other method but only on variants of the same approach, so it is hard to judge whether the results are significant or not. The second dataset seems like an existing benchmark and it is not clear what the “baseline” is in the case. Also, there is a perturbed and limited dataset which again is not very clear as to what is the difference is between the two. Regarding the metric, it seems to introduce a new metric, but there is very little context to justify the metric, for e.g. are there other types of metrics, what are the trade-offs etc. In general, there should a bit more discussion on this.
- Regarding the method itself, the randomization may introduce a lot of variance, so how would this variance be accounted for in the results presented? 
- I was not sure what N.D., H.V. ,etc. were showing in one of the tables
- The presentation could be improved with some examples and real-world motivation of LTL and relating them with the empirical results

### Questions
- How significant are the empirical results (please see under weaknesses for details)
- Are there any real-world cases that could be evaluated for showing the value of the alpha-equivalence and the significance of the proposed methods as well as limitations or trade-offs.

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
5

### Summary
Most formal languages, including the lambda calculus, include bound variables, e.g. the variable $X$ in $\forall$ X. human($X$) $\implies$  mammal($X$).  Terms in such languages are held to be equivalent under renaming of bound variables, a principle known as alpha-equivalence.  E.g. we can rename $X$ to $Y$ in the above expression without changing its meaning.  However, even though the actual name does not matter, an LLM which does logical reasoning must still be able to distinguish between different names, e.g. the variables $X$ and $Y$ refer to distinct entities in $\forall X,Y$. parent_of($X$, $Y$) $\implies$ child_of($Y$, $X$).  

The authors propose a novel embedding scheme for handling variables that are subject to alpha-renaming.  For each such variable, one part of the embedding is a normal learned embedding meaning "variable", while the second part is randomly generated for each training example, but is consistent across all uses of that variable within the example.  I.e. the embedding of $X$ is partially random, but all occurrences of $X$ within the training example use the same embedding for $X$.

The authors test their scheme on a synthetic copying task, and on a synthetic LTL (temporal logic) task involving randomly generated formulae.

### Strengths
The issue of alpha-equivalence, and of extensible vocabularies in general, has been underexplored in the literature, and the author's proposed solution seems principled and well-designed.  The authors describe their technique clearly, and cite the relevant literature.

Experimentally, the most interesting results of the paper by far are the generalization results.  The authors proposed solution generalizes to longer sequences and longer vocabulary in the synthetic copying task, and to longer formulae using more variables for the LTL task, whereas the baselines do not.  IMO, these generalization results are important.

### Weaknesses
Unfortunately, most of the authors experiments were not very convincing to me.  The copying task is essentially a unit test; it merely shows that the embeddings are working as intended.  The LTL perturbation task deliberately trains the baseline model in such a way that it is forced to operate out-of-distribution, so there's no surprise that the baseline does poorly.
Some of the other tests, such as different randomization schemes, seem uninteresting and/or irrelevant to me. 

Most importantly, both of the main tasks were entirely synthetic, which means that the variable names had no actual meaning.  In real-world human-written code or logical proofs, names typically do have meaning.  Meaningful names are a double-edged sword.  On the one hand, they may prevent the model from recognizing certain equivalences.  On the other hand, they can also guide the model in reasoning about the proof or code; a variable named "grocery_list", for example, encodes a lot of information about how that variable is likely to be used.  Names are certainly crucial for human reasoning; typical code-obfuscation techniques work by renaming all the variables, which prevents humans from understanding the code.  

To really demonstrate that the author's technique is effective in practice, I would want to see it evaluated on something other than a toy synthetic dataset, such as a code-repair task for actual human-written code.  Unfortunately, the authors do not even bother writing a discussion section about the pros & cons of erasing names from LLM input; the paper would be stronger if it at least had that.

In the short term, a way to improve the paper would be to compare the technique against other alternatives.  For example, DeBruijn indices are another common way of encoding formulae, which eliminate the need for alpha-renaming.

Another potential comparison would be to use a conventional subword vocabulary for variable names, but to train the baseline model on formulae that have already undergone random alpha-renaming of variables, so that the baseline model is robust against renaming -- that would be a more interesting result than the contrived perturbation experiment in this paper.  

Although it would require training a larger model, a good way to show the importance of alpha-equivalence in practice would be to train a conventional model on human-written proofs or code, and then show that the conventional model can be forced to make unsound logical deductions if the variables are renamed.  

Overall, I would say that this is promising work, but publication at this point is perhaps premature.

### Questions
Please see the "weaknesses" section above -- I would be particular interested in hearing the authors response to comparisons against alternative approaches such as DeBruin indices or alpha-renaming-as-part-of-training.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a novel embedding strategy for language models, specifically addressing the challenge of alpha-equivalence in formal languages. The authors introduce a dual-part embedding that combines a learned embedding that is shared between all alpha-equivalent tokens with a random component. The random component allows distinction between different variables without tying the variable symbol to the embedding. This creates an embedding technique that is agnostic to the naming of variables and enables the model to generalize to more (alpha-equivalent) variables easily. The authors evaluate on a toy task (trace copying) to empirically show the effectiveness of their approach. A second evaluation is performed on the trace generation task (from LTL specifications) to show its applicability in more complex tasks. Their results show that such an embedding indeed makes the model robust to renaming and shows the ability to handle more atomic propositions without additional training data.

### Strengths
The dual-part embedding approach is thoughtfully designed. It enforces shared semantics with a learnable component while introducing a random vector for differentiation. This elegantly handles alpha-equivalence, enabling the model to generalize across renamed and unseen variables.

The relevance of their work is understated, as this approach can potentially improve many neuro-symbolic systems. Alpha-equivalence/bounded variables are a core concept of formal languages. This approach can easily transfer to all neuro-symbolic tasks that combine formal languages and language models.

The paper’s structure is clear; the reader is well-guided through the method and experiments. The experiments are thorough and include an extensive ablation study. The trace copying and generation tasks clearly show the effectiveness of this approach.

### Weaknesses
While the experiments are extensive, it would help if the paper clarified the specific contributions of each experiment to the overall findings. The following is more detailed and specific feedback on the individual experiments.

__Baseline__. All experiments (Table 4, Figure 1, and Figure 4) mention a baseline approach. The authors should clarify how this baseline is created and how it relates to related work (Hahn et al.). I assume the authors replicated experiments from Hahn et al., but it would be beneficial if the authors would clarify where and how the replication's performance compares to the related work. Specifically, the baseline's architecture, training procedure, and any specific hyperparameters used should be detailed. Furthermore, a direct comparison of the baseline's performance against the results reported in Hahn et al. is needed to validate the replication.

__Training Steps__. The authors do not provide the training time, hardware, number of epochs/steps, etc., for any of the experiments and baselines. Comparing the training epochs/steps of their approach to the baseline would be especially important to assess the effectiveness of their approach. It is crucial to understand the computational cost of the proposed method relative to the baseline to evaluate its practical applicability. Details on the hardware used, batch sizes, and optimization algorithms are also necessary for reproducibility.

__Hyperparameter Search__.The ablation study on hyperparameter choices (5.1.2) shows thoroughness and dedication. However, the authors themselves note that the results (Table 4) are inconclusive on which hyperparameter choice is the best because of the high variance. They then extensively cross-test the correlation coefficient to see which hyperparameter choices have a positive effect. Contrary to the findings of these extensive experiments, the authors fall back to Table 4 to declare their best model (which partly contradicts the correlation coefficients). Despite the extensive experiments, this feels inconclusive and inconsistent. To improve clarity, it might be beneficial to move the ablation details to the appendix and present the “best” model configuration in the main text, leaving more space to highlight the generalization to additional APs on the trace copying task. The current presentation makes it hard to understand the final model configuration and how it was chosen.

__Immunity to Renaming__. The phrase “empirical proof” (line 398) is misleading since empirical experiments provide evidence rather than proof. Additionally, if understood correctly, the embedding of a variable/token does not depend on the actual variable symbol/token. Therefore, for example, the model cannot distinguish whether a variable is named a or b, only that they are different. This means that the model is - by construction - immune to variable renaming. If the model is - by construction - immune to variable renaming (during training and evaluation), there is no necessity to empirically validate this property. On the contrary, the Alpha-Covariance results on the “Limited” experiment (proposed model) seem to invalidate this property as the Alpha-Covariance seems to degrade with more AP. Can the authors comment on this observation? It is unclear why the alpha-covariance degrades if the model is truly invariant to renaming.

Instead, focusing on other non-obvious generalization aspects would further strengthen the experimental section:

__AP Generalization__. The most important experiment is the generalization to more APs (5.1.2 and 5.2.3). The paper's main contribution is showing that the proposed embedding improves generalization to more APs, especially on a non-trivial task (5.2.3). However, the comparison with the baseline model might be biased. While it does show that the proposed model generalizes, they don’t fully establish that the baseline model can’t generalize in this way. The experiment instead shows that Transformers cannot generalize to unseen tokens, which is a well-known fact. A more balanced comparison could involve ensuring that all 30 (or 10) APs appear in the baseline’s training set. Note that this does not imply that the dataset would contain samples exceeding 5 APs, only that all tokens are seen during training. Since the authors admit that the baseline model performs better on in-distribution evaluation, the outcome of such an experiment is open. The current experimental setup does not isolate the effect of the proposed embedding from the effect of simply seeing all tokens during training.

__Minor Details__:
 - Adding axis legends for edit distance in the heatmaps (Figures 1, 3, 4) and labeling subfigures (e.g., a), b), c)) would improve understanding and make the experiments easier to reference. Placing Figure 1 in the evaluation section, where it has more context, might also enhance the flow as the Figure is hard to understand without the necessary context of the evaluation section.
 - The grey area in Figure 3 represents impossible data points, and the green box (boundaries of the training dataset) overlaps this region. If these data points cannot exist, perhaps the green box boundaries could be adjusted to prevent visual confusion.

__Summary__. Overall, this paper introduces a well-motivated and potentially impactful approach, and it’s clear that substantial engineering effort went into the experiments. However, the experiments do not sufficiently showcase the advantage over the baseline. This does not imply that the results are not good enough but rather that comparisons to the baselines need to be chosen more carefully. Furthermore, a second application from a different formal language domain than LTL would strongly improve the paper’s relevance in the area.

### Questions
Please address the comments above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The subject of the paper is studying a method for using transformers trained to solve a task T on vocabulary V in order to solve the same task on a vocabulary V’ different from V (possibly of larger cardinality).

### Strengths
The main strength of the paper is to put the eye on a problem scarcely studied, namely how could language models be effectively used in vocabularies different from the one they were trained with.

### Weaknesses
The main argument put forward by the authors is that this is needed for dealing with linear temporal logic (LTL) satisfiability where a transformer is trained to output traces that satisfy the formula given as input (the empty trace meaning the formula is not satisfiable). The argument here is that unknown propositional symbols out of vocabulary V used to trained the transformer can be used in formulas at prediction time. The other “abstract” application mentioned is copying with an extendable vocabulary. However, this problem is not related to any concrete one that actually requires handling an a priori unknown vocabulary.

The rationale behind the first application is that propositional symbols not in V could actually be replaced by  others in V without changing satisfiability. This is called interchangeability in the paper. However, this concept is not formally defined but loosely presented in the introduction. Moreover, the paper states that is the same as alpha-conversion. This statement is at least cumbersome since alpha-conversion applies in the case of bound variables, but there are no quantifiers in LTL, nor in the extendable vocabulary case. For LTL, it seems to be renaming under some constraints, but not alpha-conversion. For the second application, it is not even clear where renaming occurs. 

The introduction suggests that the vocabulary V' used at evaluation time is unknown at training time. However, the experiments make clear that the method requires fixing the size of the expected vocabulary at training time as well as the translation from input symbols to tokens. This is never explicitly said in the paper. 

Overall:
- The paper lacks a precise definition and formalization of the problem it intends to solve.
- The experiments are not sufficiently well presented and analyzed.

### Questions
- Formally state the problem in the paper and provide useful examples to illustrate the problem and the intended use cases.

In Sec. 4. the authors refer to the addressed problem as “learning semantically equivalent but distinguishable (alpha-equivalent) token”. However, this problem is actually not precisely defined elsewhere. As we said before, the usual concept of alpha-conversion does not seem to apply for the intended applications foreseen in the paper.

- Justify and explain the need for partitioning the set of tokens.

In Sec. 4.1. the paper presents an embedding matrix where tokens are partitioned into so-called “regular” or “not-interchangeable”, and “interchangeable” ones. The notion of regular token is only used in this section. For the experiments in Sec. 5.1. all tokens are considered interchangeable. No mention at all of any partition of tokens in the case of LTL, though it seems there is none.

- Clarify whether the embedding has the size of the largest expected vocabulary.

The experiments in Sec. 5. (summarized in Table 3) talk about d_beta which is the number of columns of the embedding for the randomly generated part, but there is no specification of the numbers n and m corresponding to the number of regular and interchangeable tokens. The description of the experiments talk about “unique characters” but it is not clear whether they are randomly generated or fixed, or if the training and evaluation sets of characters intersect or not.

The text in L. 275 “next-token predicted probabilities … are expected to align with the input string exactly” is misleading. What do you mean by “align”. In the description of the experiments in Sec. 5.1. it looks like the number of rows of the embedding is the size of the largest expected vocabulary V’, while the transformer is only trained on symbols from V. This is not clearly stated before.

- Justify the evaluation metric in Sec. 5.1.

The evaluation metric “edit distance” is not justified. Since the validation strings are randomly generated and all tokens are interchangeable, while a token different from the one in the validation string would be considered an edit error? Also, I found Figure 3 (as well as Fig. 1 in the introduction) difficult to understand.

- Clarify questions on the perturbed dataset and baseline model of Sec. 5.2.

The experiments on LTL satisfiability are not clear (Sec. 5.2.1, Table 4). 

First, the way the perturbation of the dataset is carried out is very roughly described. Do you rename both input formulas and output traces? Renaming cannot be just random since you have to preserve satisfiability and the validity of the output. Please explain.

Also, I don’t understand why fixing the order of the first occurrence is useful. Please clarify .

The text suggests it is not a model trained by the authors for the purpose of this paper. So, first of all: where does it come from? is it a model publicly available? Also, how is it capable of dealing with propositions which are not in the original set of AP? Or, are you considering the same set of AP? 

The experiments in 5.2.1 and 5.2.3. do not seem to partition the tokens into regular and interchangeable. Please clarify.

- Clarify questions about alpha-covariance.

Sec. 5.2.2. Pg. 9. L 445-450 seems to suggest that there is some relation between the alpha-covariance metric and semantic correctness. It is not clear to me that the experiments in Table 4 evidence that. Please clarify.

Other questions and comments

Pg. 1. Starting Section 1 with a figure is distracting. Also, it is not related at all with the introduction and hard to understand. I think those figures do not help to clarify what is going on.

Pg. 1. The introduction gives the impression that there is no other path to solving the stated problem of satisfiability of LTL modulo alpha-conversion with Transformers than the one proposed by the paper. For instance, it could be possible to just apply a renaming to the Transformer’s alphabet before-hand. Please comment on this.

Pg. 2. endocer -> encoder

Pg. 4. Line 167. Why is it trivial to support multiple sets of different interchangeable tokens and what would be the need for such kind of embedding? Please clarify.

Pg. 5. Line 254. What do you mean by log smearing?

Pg. 5. Line 255. “clamp the scale value..”. I think bound/clip would be preferable.

Pg. 7. Line 324. Why f_bn, f_fn and AdaCos are boolean properties?

Pg. 8. Line 396. I think “empirical evidence” is more appropriate than “empirical proof”.

### Soundness
1

### Presentation
1

### Contribution
1
