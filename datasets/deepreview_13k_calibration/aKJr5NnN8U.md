# Toward Understanding In-context vs. In-weight Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
It has recently been demonstrated empirically that in-context learning  emerges in transformers when certain distributional properties are present in the training data, but this ability can also diminish upon further training.
We provide a new theoretical understanding of these phenomena by identifying simplified distributional properties that give rise to the emergence and eventual disappearance of in-context learning.
We do so by first analyzing a simplified 
model that uses a gating mechanism to choose between an in-weight and an in-context predictor.
Through a combination of a generalization error and regret analysis we identify conditions where in-context and in-weight learning emerge.
These theoretical findings are then corroborated experimentally by comparing the behaviour of a full transformer on the simplified distributions to that of the stylized model, demonstrating aligned results.
We then extend the study to a full large language model,
showing how fine-tuning on various collections of natural language prompts can elicit similar in-context and in-weight learning behaviour.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper provides a theotical framework which studies in-context learning's emgerence and transient nature through a simple model which can adapatively switching between an in-weight predictor and an in-context predictor. The key insights from this paper shows that when the training data has long-tail, containg rare classes that appear infrequently, ICL tends to emerge. And if there are enough training data, IWL tends to dominate. Their experiments on both synthetic data and Ominiglot daat shows that ICL exhibit for rare classes and IWL for common ones.

### Strengths
1. The paper introduces a novel theoretical framework that investigates how a model selects between ICL and IWL. This framework offers insights into the conditions under which ICL emerges, especially highlighting the role of rare labels in promoting ICL.
2. The writing and presentation is clear.
3. this paper includes experiments in both synthetic and natural few-shot learning dataset and validated their findings.

### Weaknesses
1. This paper assumes a simple switch between the IWL and ICL based on error minimization but in real world LLM the transition may not be instantaneous and involves more complexities. Specifically, the model's reliance on a hard switch based on a simple error minimization might not capture the nuanced, gradual transitions observed in real-world LLMs. The model does not account for the potential for a more complex interplay between ICL and IWL, where both mechanisms might be active simultaneously, with their relative contributions changing dynamically based on the context and the training data.
2. The in-context predictor is modeled as a convex combination of the labels in the context, weighted by input similarity. This raises questions because more commonly the in-context predictor should learn the relationship between inputs and outputs (i.e., the mapping from x to y rather than combining labels. This simplification might limit the applicability of the theoretical findings to real-world scenarios where the input-output relations are more complex. The model's approach of directly combining labels based on input similarity overlooks the critical aspect of learning input-output mappings, which is a core function of in-context learning. This simplification might not fully capture the complexities of how LLMs learn from context, where the relationship between inputs and outputs is often non-linear and requires more sophisticated modeling.
3. The experiment with the real LLM, Gemini Nano 1 seems somewhat limited. It primarily tests the LLM's ability to follow in-context labels versus trained labels, which may be influenced by how different LLMs are instructed to trust new labels versus their trained knowledge. A more comprehensive and persuasive experiments could include various LLMs to assess the generality of the findings and provide deeper insights across different architectures and scales. The current experiment does not explore the full range of LLM behaviors, particularly how different architectures and training regimes affect the balance between ICL and IWL. The study could benefit from testing a wider array of models to see if the observed trends are consistent across different LLM types and scales.

### Questions
A recent work[1] shows that ICL exhibits dual operating modes: task retrieval and task learning. As the number of correctly labeled examples grows, the model transitions from task retrieval to task learning, but initially, even with correct labels, it may retrieve the wrong task, leading to errors. Wondering how does your finding explain this dual-mode behavior?

[1]Dual Operating Modes of In-Context Learning. https://arxiv.org/abs/2402.18819

### Soundness
2

### Presentation
3

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
[update: in response to the revision and author responses I have updated my score]

The study of in-context learning (ICL) has emerged in recent years as a tractable and yet important piece of the puzzle for understanding how transformers are able to achieve such good performance across such a wide range of data distributions. There is now a growing literature combining theoretical models with empirical study of ICL in synthetic settings, with the aim of understanding the mechanism by which ICL works, and why it emerges in the first place. 

The present paper adds to this literature, by studying the tradeoff between memorisation (or in-weight learning) and ICL in a simple theoretical model and associated experiments, and how this tradeoff varies with the nature of the data distribution.

### Strengths
- Reasonable theoretical foundation for their arguments
- Well-designed experiments to test these theoretical predictions

Overall I think this has the makings of a good paper that makes a significant and original contribution to an important thread of research in the science of transformer generalization.

### Weaknesses
 - At the moment I am not convinced that the experiments reported in Fig 2 really do support the theoretical predictions. I hope this is just my misunderstanding and that the authors can explain what I missed, and perhaps provide a clearer explanation in the paper.
- While I am pretty well-versed in this corner of the literature and so prepared to care about the contents of Fig 2, it still took me a while to process all the acronyms and setup.

- The main theoretical results seems to be that “ICL will first emerge on rare classes, and will eventually be replaced by the IW predictor on those classes” (line 207,208). This prediction is studied experimentally in the setting described in Figure 2, where three models are trained for 100K gradient steps (Appendix B.1.1) across a number of sample sizes N. The three models are all trained with a single (x,y) pair in the context (L = 1) and for the IW predictor the context is always “relevant” (so if I understand correctly the correct output given (x,y), x’ is to simply ignore x’ and copy the input y to the output) and for the IC predictor the context is always “irrelevant” (so given (x,y), x’ the correct output cannot be learned from the context, which should be ignored). The main transformer is trained to have 90% of its contexts relevant.

My reading of Fig 2 is that on the rare classes where IC is possible (second column, top row) the transformer behaves very similarly to the IC predictor from the beginning, and only converges to the IW predictor when the IC predictor does. The behavior on high-frequency classes seems qualitatively similar, and so I don’t see on what basis this is evidence for the “first emerge” part of the claim. Nor do I see how these experiments really support the idea that for large N the transformer switches to the IW predictor. A simpler explanation for this experimental data seems to be that, by construction, the transformer should be somewhere between the IC and IW predictor since its training distribution is between theirs, and for large N the IW and IC predictor behave similarly on relevant contexts.

It seems therefore that the crux of the argument might lie in the OOBD plots (Fig 2 second row). My reading here is that on the low-frequency classes OOBD performance of the general transformer is initially bad, improves, and then degrades, whereas for high-frequency classes the OOBD performance is initially roughly as good as it ever gets on the low-frequency classes, and then degrades. I do not see here the evidence for “ICL emerges first on rare classes”? The degradation of OOBD performance also seems to be much slower on the low-frequency classes than the high-frequency classes, which makes me unsure if the OOBD data shows any evidence for the “replaced by the IW predictor on those classes” claim either.

In short, I’m not sure how to read Fig 2 as evidence for the theoretical claims. This leaves me unsure of the soundness of the main experimental contribution of the paper.

Minor issues:

- “Cdot” line 149
- “Transient” -> “transience” line 303
- It’s a bit strange to see H defined twice in quick succession (differently) in 130 and 158

- Compared to the other literature in this area the models are rather small (two layers, one head per layer) and the contexts are very short (e.g. L = 1 in Fig 2). Overall I am left with the sense that maybe these models are just not capable of learning the ICL solution the theory is talking about, and this could be confounding some of the other aspects of the paper. This is actually how I read Fig 6. To what extent is the choice of L = 1 to illustrate something theoretically, and to what extent is it just “the only length that works” as a result of the small model?

### Questions
The main theoretical results seems to be that “ICL will first emerge on rare classes, and will eventually be replaced by the IW predictor on those classes” (line 207,208). This prediction is studied experimentally in the setting described in Figure 2, where three models are trained for 100K gradient steps (Appendix B.1.1) across a number of sample sizes N. The three models are all trained with a single (x,y) pair in the context (L = 1) and for the IW predictor the context is always “relevant” (so if I understand correctly the correct output given (x,y), x’ is to simply ignore x’ and copy the input y to the output) and for the IC predictor the context is always “irrelevant” (so given (x,y), x’ the correct output cannot be learned from the context, which should be ignored). The main transformer is trained to have 90% of its contexts relevant.

My reading of Fig 2 is that on the rare classes where IC is possible (second column, top row) the transformer behaves very similarly to the IC predictor from the beginning, and only converges to the IW predictor when the IC predictor does. The behavior on high-frequency classes seems qualitatively similar, and so I don’t see on what basis this is evidence for the “first emerge” part of the claim. Nor do I see how these experiments really support the idea that for large N the transformer switches to the IW predictor. A simpler explanation for this experimental data seems to be that, by construction, the transformer should be somewhere between the IC and IW predictor since its training distribution is between theirs, and for large N the IW and IC predictor behave similarly on relevant contexts.

It seems therefore that the crux of the argument might lie in the OOBD plots (Fig 2 second row). My reading here is that on the low-frequency classes OOBD performance of the general transformer is initially bad, improves, and then degrades, whereas for high-frequency classes the OOBD performance is initially roughly as good as it ever gets on the low-frequency classes, and then degrades. I do not see here the evidence for “ICL emerges first on rare classes”? The degradation of OOBD performance also seems to be much slower on the low-frequency classes than the high-frequency classes, which makes me unsure if the OOBD data shows any evidence for the “replaced by the IW predictor on those classes” claim either.

In short, I’m not sure how to read Fig 2 as evidence for the theoretical claims. This leaves me unsure of the soundness of the main experimental contribution of the paper.

Minor issues:

- “Cdot” line 149
- “Transient” -> “transience” line 303
- It’s a bit strange to see H defined twice in quick succession (differently) in 130 and 158

Factors that would improve my score:

- As already mentioned, clarifying the link between Fig 2 and the theoretical prediction.
- Compared to the other literature in this area the models are rather small (two layers, one head per layer) and the contexts are very short (e.g. L = 1 in Fig 2). Overall I am left with the sense that maybe these models are just not capable of learning the ICL solution the theory is talking about, and this could be confounding some of the other aspects of the paper. This is actually how I read Fig 6. To what extent is the choice of L = 1 to illustrate something theoretically, and to what extent is it just “the only length that works” as a result of the small model?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Summary of the paper:

* The paper defines a sequential, tabular supervised classification task as a
  simplified setting in which to study the dynamics of in-context vs.
  in-weight learning.
* The paper considers three models in this setting:
  1. An 'in-weight learner' model capable of predicting labels based only on
     the most recent query.
  2. An 'in-context learner' model that predicts labels based instead on a
     sequence-dependent weighted combination of previous labels appearing in
     the sequence (specifically, the weights are given by a softmax
     distribution based on similarity to the previous queries).
  3. A contextual mixture model that can (learn to) choose based on the input
     sequence whether to predict according to the first model or the second
     model, or interpolate between the two.
* The paper describes a theoretical analysis of the performance of these
  three models in the synthetic task:
  * Deriving an upper bound on the expected test loss of the in-weight
    learner.
  * Deriving an upper and lower bound on the loss for a particular input of
    the in-context learner.
  * Giving a family of algorithms for learning all three models and bounding
    the regret of the combination model in terms of the regret of the
    learning algorithms used for learning some of the components.
* Based on the nature of these bounds, the paper argues that this model
  captures phenomena observed in prior empirical work on in-context learning
  and in-weight learning, namely that rare classes drive the emergence of
  in-context learning (Chan et al.) and that ICL disappears after enough
  training (Singh et al.).
* The paper also includes some experiments with small transformers on
  synthetic data and natural language data and comparisons of the theoretical
  model's qualitative predictions to the resulting empirical observations.
* There is also a small qualitative study of a LLM's dependence on knowledge
  from fine-tuning versus knowledge from its context.

I wrote a somewhat long review. Therefore, I also include a summary of my
review as follows.

* I think this paper presents some interesting ideas and results. For
  example, I like the sequential supervised classification task and I like
  the three-part model.
* However, I find the results do not achieve the paper's stated aims of
  capturing empirical phenomena to the degree claimed, due to what appear to
  me to be several issues, namely:
  * fundamental mismatches between the theoretical framework and results and
    the phenomena studied in prior work,
  * some limitations in the theoretical results that do not appear to have
    been acknowledged, and
  * a lack of connection between the theoretical results and the experiments.
* Overall, I consider the framing of the paper to be inaccurate and therefore
  in my judgement the paper should not be accepted in its current form,
  though I am certainly open to discussion and revisions to the framing to
  acknowledge and address these gaps as I think the work does have value.
* I also noted several questions and minor corrections, mainly regarding the
  theoretical sections.

**EDIT TO ADD:** Summary of discussion.

* The authors addressed my concerns about the framing through their responses and revisions:
  * They refined their claims about connections to prior work, resolving my concern about the mismatch between their theory and prior work.
  * They strengthened their theoretical results and acknowledged the remaining limitations, resolving my concern about the limitations of their theory.
  * They clarified the connection between their theory and experiments and added new synthetic experiments with a more direct connection, resolving my concern about the connection between their theory and experiments.
* With the authors having resolved all of my concerns, I am now pleased to be able to recommend the paper for acceptance, and raised my rating from 5 to 8.

### Strengths
The paper addresses an important topic in the science of deep learning,
namely the phenomena of the emergence and transience of in-context learning
(versus in-weight learning).

On this topic the paper presents an interesting learning setting involving an
in-context supervised classification task that captures several important
elements of in-context learning. At the same time, this setting is simpler in
some ways than in-context linear regression or other comparable synthetic
learning settings.

I think the overarching story developed in the paper (roughly, in my
understanding, that in-context learning arises as a heuristic that can reduce
loss in areas of the input distribution where in-weight learning has not
gathered enough experience to provide a specialised and more accurate
prediction) is an interesting and thought-provoking perspective.

I think the three-part model is an interesting and thought-provoking toy
model of in-context learning versus in-weight learning, and I think the
theoretical analysis is informative and supports the aforementioned
overarching story.

### Weaknesses
**W1. Mismatch with Singh et al.'s setting.**
In the introduction you write that your analysis "explains the findings of
Singh et al. (2023)," namely the transience of in-context learning, giving
way to in-weight learning. It doesn't seem to me that your model captures the
phenomenon observed by Singh et al. In my understanding, a fundamental
feature of the setting of Singh et al. is that there is no train-loss
incentive for an ICL solution over an IWL solution, because both paradigms
are equally capable of solving the task (yet, they observe, ICL still emerges
and still gives way to IWL in the end). In contrast, in your model, as you
show, based on your formulation of ICL and IWL there is a performance lower
bound to ICL which the upper bound on IWL performance is eventually able to
surpass.


**W2. Incomplete characterisation of the emergence of ICL for rare classes.**
On lines 207--209, you write "Under this [oracle] algorithm, ICL will first
emerge on rare classes ... This phenomenon is consistent with the empirical
observation that in-context learning emerges with rare classes in the
training data...".

It appears that this characterisation of the oracle algorithm is based on the
observation that, for some specific values, the IW upper bound starts higher
than the IC upper bound (figure 1), suggesting that in these cases the simple
model will use the IC sub-model rather than IW sub-model. However, this is
not implied by the theory as the IW bound is merely an upper bound on the IW
risk (I also note in a question below that the IC bounds are not of the IC
risk but of a particular sample of the risk).

I believe a more accurate characterisation would require the stronger
assumption that the IW risk happens to be higher than the IC risk for the
rare classes in question. This arrangement is permitted but not implied by
the comparison between upper bounds. It would be implied if you had a lower
bound on the IW risk and this was higher than an upper bound on the IC risk.
I am unsure whether such a bound is plausible. In my opinion this gap between
the model and the phenomenon should be noted explicitly as a limitation of
the analysis.

(Note that this issue is not localised to lines 207--209, but that appears to
be the most explicit discussion of the comparison between the phenomenon and
the theoretical framework. The favourable result of the comparison is a theme
throughout the rest of the paper.)


**W3. Incompletely addressed limitation of tabular analysis.**
There are several details in the theoretical framework and analysis that
assume a tabular setting. In footnote 1 you claim that the results can be
easily be extended to a continuous input space. It is not clear to me that
this extension would be easy, since, beyond (yes) easily extending the
definition of the task and the models, the bounds and the proofs seem to be
tightly coupled to the tabular setting. It is unclear to me whether
qualitatively similar bounds could be achieved in a continuous input setting.
On what basis have you made this assertion?


**W4. Specific model of in-context learning appears quite restrictive.**
The paper talks generally about in-context learning in transformers, but for
the three-part model your formulation of in-context learning appears
surprisingly restrictive, namely at first limiting the prediction to a convex
combination of context labels and then by the relevant theorem further
limiting to the specific modelling choice of using a softmax distribution
based on query similarity for weighting the labels.

It seems to me that mechanisms for in-context learning in a transformer are
unlikely to be limited in this way, and the ability to use alternative
mechanisms would generally serve to broaden the model class under
consideration and therefore put your performance lower bounds into question.
In other words, these restrictions on the ICL sub-model seem to be the source
of the conclusion that IWL is eventually preferable to ICL, which does not so
much answer the question of why IWL is eventually preferred as raise the
question of why we should believe that ICL is limited in this specific way.

**W5. Gap between theory and experimental study.**
The experimental methodology involves comparing one transformer's performance
with that of two other 'baseline' transformers, one trained on data that is
supposed to incentivise ICL and another trained on data that is supposed to
incentivise IWL. The comparisons between the 'middle' transformer and these
baselines are then used to corroborate the predictions of the theory.
However, the use of pretrained transformers as baselines creates a confound
that the 'IWL transformer' may not resemble the IWL model in the theory and
(even more plausibly) the 'ICL transformer' may not resemble the ICL model in
the theory. This would potentially undermine the connection between the
theory and the experimental results (and, in turn, the relevance of the
theory). This gap appears not to have been acknowledged in the paper.

Given that you have details models of these learners and have posited
specific training algorithms capable of achieving your regret bounds, and in
the synthetic data experiments your set up seems to match the theoretical
assumptions (apart from the tabular input space, though presumably the
synthetic data setting could be modified to satisfy this assumption along
with any others I have overlooked), it seems like it would have been possible
to implement your theoretical models directly and compare the performance of
these models to the baseline transformer (or the middle transformer).


**W6. Unclear relevance and novelty of LLM experiments.**
The LLM experiments are interesting in their own right, however I came away
feeling unimpressed for several reasons:

1.  I felt you could have done more to connect these experiments and their
   results to the theoretical framework developed in section 2. At the moment
   I don't see what the LLM experiments say about the theory and I don't see
   what the theory says about the LLM experiments.

2.  The total number of examples tested is small (if my understanding is
   correct and all examples are listed in the appendices). No statistical
   analysis has been performed on any specific questions about the results to
   see if the trends reported are statistically significant.

3.  Though it is not my area, I have the feeling that there exists at least
   a small number of papers having already studied the topic of the
   competition between knowledge from fine-tuning and knowledge from contexts
   in determining the predictions of LLMs. (I regret I have not been able to
   locate any examples, but one that comes somewhat close is Wei et al.,
   2023, arXiv:2303.03846, which is actually cited in passing in the
   introduction but is not discussed in any detail). I would have liked to
   see you contextualise their experiment and results within this literature.

### Questions
Theory:

1. What parameterisation of $\alpha$ do you have in mind? Simply to learn a
   value for every $\tilde x$ (i.e., again tabular)?
   * If so, how can you expect it to know to route to the IC model when you
     haven't seen enough of an example for $g$ to be useful? Is it supposed to
     be initialised as biased towards routing to $h$?

2. In Proposition 1 (for example), over which distribution are the
   expectations of $y$ taken? Is $y \sim y^\ast(x)$?

3. In Proposition 2 and Corollary 1, if I am not mistaken, your bounds apply
   to a given sample of the expected risk, and they depend on the sample. For
   example, in corollary 1, you bound $\mathrm{CE}(h(\tilde x), y)$ for a
   particular $\tilde x$ and $y$. Since you later compare these bounds to the
   IW upper bound which is of the expected risk, could you comment on the
   relationship between these bounds and the expected risk for the IC learner?

4. In Corollary 1, I was confused by the line "Assume the labels $y^\ast$ are
   one-hot (deterministic)".
   * If I understand correctly, in the data generating process, the concrete
     *labels* $y$ in any given example are *already* one-hot, as stated on
     lines 120--121 "When we sample $x$ in the context of as the query, we
     sample $y=e_i$, the $i$-th standard basis vector, ..."
   * I thought, possibly you meant that the ground truth labelling *function*
     $y^\ast$ is assumed to be such that the ground truth label $y^\ast(x)$
     is deterministic? But this seems like too strong of an assumption, since
     you go on to talk about IWL being better with enough samples *if* the
     variance is sufficiently low, and if you were assuming the variance was
     zero for your ICL bound then it wouldn't make sense to say this.
   * In fact, the assumption that $y$ is one-hot appears to be used in the
     proof for proposition 2, whereas no additional assumption on $y$ or
     $y^\ast$ seems to be used in the proof of corollary 1.
   * So, I think this assumption is redundant. Is that correct?

5. In Corollary 1, you give both a lower bound in terms of $k$ and also an
   exact value in the case where $k=L$. There is no restriction on $k$ in the
   general case and so I assumed that if I put $k=L$ the lower bound
   should lower bound the exact value. However, if I am not mistaken, if $k=L$
   then the lower bound simplifies to $1-\epsilon$, which is larger than the
   exact value $-\log(\epsilon)$ for some values of $\epsilon$. Is there a
   mistake in the lower bound?

6. In the figure 1 caption, what is the "Big-O constant of the IW risk"? I saw
   no asymptotic analysis in the IW bound.

Notation and terminology:

1. Corollary 1: I invite you to consider using a roman font to denote cross
   entropy loss (as in "$\mathrm{CE}$") so as to prevent lexical ambiguity
   with the variable $C$ and an undefined variable $E$ for readers parsing
   the result statement.

Typos:

1. There are two separate reference list entries for Edelman et al. (2024).
2. There are two separate reference list entries for Zhang et al. (2024).
3. Line 90 "attention attention"
4. Line 148 "cdot" presumably should be "\cdot"
5. Line 304 "transient of ICL"
6. Line 345: It says "A generic model trained on data with $p_{high}$ is
   referred to as the *transformer.*" Is that meant to be $p_{relevant}$?
7. The proof of Proposition 1 uses notation $R_x$ for expected risk without
   having introduced this notation anywhere (as far as I can see).

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tries to understand how trained Transformers choose between in-weights learning (IWL) and in-context learning (ICL). The paper is well grounded in recent literature studying the contrast of phenomenology and inference time behavior of IWL and ICL, especially with Singh et al. 2024’s finding that ICL can be transient. The paper first sets up a mathematical framework where vectors are input and noisy labels are used in a classification setup. The paper then discusses analytic predictors using ICL and IWL, and explains why IWL is asymptotically superior and why a neural network can find the optimal solution by gradient descent. The paper conducts experiments comparing a transformer’s validation loss to the ICL and IWL predictors to identify that noise level and fraction of rare tasks are critical variables deciding ICL/IWL. Finally, the paper shows, by fine tuning Gemini Nano 1, that fine tuning can induce loss of ICL abilities in real LLMs

### Strengths
Overall, the paper’s motivation is clear and the flow is consistent. Here is a list of strengths:

S1: The paper connects an observed phenomenon (ICL’s transience into IWL) with a synthetic model and theory.

S2: The intuitive interpretation that new training samples are effectively test samples under the assumptions made in Sec. 2 is useful.

S3: This work clearly demonstrates how noise level and the fraction of rare tasks can affect the ICL versus IWL.

S4: Unlike concurrent work exploring similar phenomena with similar methodology (https://openreview.net/forum?id=XgH1wfHSX8, https://openreview.net/forum?id=INyi7qUdjZ, https://openreview.net/forum?id=LbceJJc9h2), this work provides experiments with real language models. However see below for some criticism as well. Despite the criticism, the investigation of how well findings on synthetic data generalize to real models is valuable.

### Weaknesses
The paper has some weaknesses, listed below:

W1: Theory seems to rely on assumptions not met in realistic applications of ICL. The theory assumes that the data are drawn i.i.d, while this is usually not met in many realistic applications of ICL. Thus it is quite unclear whether new training samples can safely assumed as test samples in real LLM training. Specifically, the assumption that the entire context-query pair is drawn i.i.d. is problematic. In few-shot learning, for example, the context examples are often carefully curated and highly correlated, designed to elicit a specific behavior from the model, rather than being independently drawn from the pretraining distribution. This discrepancy between the theoretical setup and practical use cases limits the generalizability of the findings.

W2: The setup seems to perform a classification task where x,y are given in pairs. However, this *might* be not a good model of ICL in real LLMs as it does not involve a complex sequence-space computational structure. Recent works, e.g. Akurek et al. 2024 (https://arxiv.org/abs/2401.12973), seems to model the sequence space nature of ICL better. It seems like this seems important to understand ICL \textit{in Transformers} as Tong et al. 2024 (https://arxiv.org/abs/2405.15618 ) points out that MLPs can learn in context.

W3: I was not able to draw these conclusions in line 484 from the given Figure 7: “in line with our theory, the IBD error of the “selected” IC learner is significantly lower for low-frequency classes. Furthermore, both the IC and IW predictors achieve similar IBD errors on CH, suggesting that IWL more easily emerges on common classes even with larger input noise (Figure 7, right).” It would be great if this can be explained further. The connection between the observed error differences and the theoretical predictions is not clearly articulated, and the claim about IWL emerging more easily on common classes needs more explicit justification from the figure.

W4: While I agree with most conclusions drawn from the plots, it would be better to compute explicitly a ICL_vs_IWL ratio as a metric since currently it seems like these conclusions are drawn by matching the experiment curves with predictors by eye. The lack of a quantitative metric makes it difficult to objectively assess the relative dominance of ICL versus IWL, and introduces a degree of subjectivity in the analysis.

W5: It is intuitively hard to grasp the experiment. This is solely a presentation issue, it would be very helpful if there was a schematic diagram which describes all of $p_{relevant}$, $p_{high}$, OOBD, IBD, IC model, IW model, etc. The figures could also be improved, as mentioned below in questions.

W6: It is unclear how well the real LLM experiments justify the claims in the main text and the claim in Singh et al. 2024 that ICL can be transient *during pretraining*. The current experiments seem to suggest that fine-tuning can override ICL abilities, but it is very probable that the ability itself is still there while it is simply suppressed superficially. (See Jain et al 2023 (https://arxiv.org/abs/2311.12786, https://arxiv.org/abs/2410.1653 ). This would not be corresponding to the claim in the main text and in Singh et al. 2024, which I believe discusses a pre-training stage transience requiring orders of magnitude more steps than fine tuning.

### Questions
Questions
1. How could the real vs invented (name, city) pair result be explained? If the model is being fine-tuned, why can’t it memorize invented (name, city) pairs? Is there an intuition or is this simply the case?
2. How applicable is the theory to real LLMs?

Suggestions:
1. The current figures were quite confusing for me, the axis and plot labeling constantly changed through Fig 2,3,7,8. It would be great if the plot colors/style can be improved so that they can be better understood.
2. I think Figure 16 is main-text material, perhaps more so than Figure 8.

### Soundness
3

### Presentation
1

### Contribution
3
