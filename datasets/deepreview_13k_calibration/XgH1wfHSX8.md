# Algorithmic Phases of In-Context Learning

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 6, 8, 10

## Abstract
In-Context Learning (ICL) has significantly expanded the general-purpose nature of large language models, allowing them to adapt to novel tasks using merely the inputted context. This has motivated a series of papers that analyze tractable synthetic domains and postulate precise mechanisms that may underlie ICL. However, the use of relatively distinct setups that often lack a sequence modeling nature to them makes it unclear how general the reported insights from such studies are. Motivated by this, we propose a synthetic sequence modeling task that involves learning to simulate a finite mixture of Markov chains. As we show, models trained on this task reproduce most well-known results on ICL, hence offering a unified setting for studying the concept. Building on this setup, we demonstrate we can explain a model’s behavior by decomposing it into four broad algorithms that combine a fuzzy retrieval vs. inference approach with either unigram or bigram statistics of the context. These algorithms engage in a competitive dynamics to dominate model behavior, with the precise experimental conditions dictating which algorithm ends up superseding others: e.g., we find merely varying context size or amount of training yields (at times sharp) transitions between which algorithm dictates the model behavior, revealing a mechanism that explains the transient nature of ICL. In this sense, we argue ICL is best thought of as a mixture of different algorithms, each with its own peculiarities, instead of a monolithic capability. This also implies that making general claims about ICL that hold universally across all settings may be infeasible.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new synthetic task, namely finite Markov mixtures, to study the properties of in-context learning (ICL) in Transformers. The authors present several analyses on top of finite Markov mixtures. First they show that this task alone can effectively recover known phenomena which were originally discovered on several different tasks like linear regression, classification, and finite automata. Then they contribute new insights, and argue that ICL is best thought of as a convex combination of several learning algorithms which emerge or vanish during training.

Overall I found this work a well-written and interesting read, with several novel observations which are very relevant to the ICLR community. In particular, I appreciated the insight that ICL is best thought of as a mixture of learning algorithms, and that these algorithms are transient throughout training. It’s main weakness is that It lacks a clear takeaway message for readers to act upon — see my questions below.

### Strengths
- **Well-written**. This expository work is well written and enjoyable to read. The authors do a good job at holding the reader by the hand through their analyses and provide adequate context even for non-ICL experts. The figure are easily understandable (mostly, see below for a nit) and the flow of the paper makes sense.
- **Sound, novel, and unifying benchmark.** The benchmark is novel in the context of ICL studies and it is soundly derived (eg, using the expected KL as quality measure in Eq. 1). Some of the choices are arguable (eg, why Dirichlet?) but that’s splitting hair. What’s more interesting is that it reproduces known phenomena from the literature while also uncovering novel insights.
- **Strong analysis revealing new insights**. The insight that ICL can be decomposed into several algorithms *at any point in training* is novel and deserves further thinking. Some may argue that the transient nature of ICL was known (the authors say so themselves) but this work goes one step further, showing the algorithms are not forgotten but rather superposed with different weighting coefficients (Fig. 6.b).

### Weaknesses
 - **Lack of actionable takeaway message**. Because the benchmark is synthetic, it’s unclear how much it says about ICL for real-world LLMs. This is the main flaw of the paper. For example, l.81: it’s good to know that Transformers can learn different algorithms — but which is it for LLMs / VLMs? Certainly not the unigram or bigram of l. 301, right? Similarly, I liked the flavor of paragraph on l. 301 but it’s unclear how to replicate this study on real-world LLMs. This limits the insights into how real-world ICL really works, and so we’re left with the question: what do we do with the discovery that ICL is best thought of as a mixture of algorithms? This work doesn’t say which are the algorithms for real-world ICL, so we can’t, e.g., prescribe which algorithm to surface and when.
- **The Bayesian vs non-Bayesian discussion is unclear**. On l. 226 the authors argue that ICL first has a Bayesian and then a non-Bayesian behavior (they intentionally don’t use the term frequentist), and that the Bayesian overfits to the training Markov mixtures. I think this distinction could be explained better. For example, one could make the argument that ICL is always Bayesian — otherwise what is transferred? — but the prior weakens as the model sees more diverse chains. In fact, the experiments support this line of thought: Fig. 5.b shows that as we increase the number of training chains, the prior weakens. In fact, I think believe this weakening of the prior is a property of how the Markov mixtures are constructed, and we would see a different behavior if the test chains where chosen differently. Note that this point  doesn’t take away from the superposition analysis but it needs clearer explanations.
- **Minor presentation issues**. The paragraph on l. 341 is not detailed enough, and doesn’t explain what the Fig. 5 shows. It also doesn’t help that Fig. 5 doesn’t have clear legend on the heat map scales — is darker more Bayesian or less Bayesian for 5.b? Finally, some parameter choices in the analysis are weird: l. 187, why plot at train step 839 specifically? l. 192, why at n = 2^7? Can we have similar figures for later training steps and for larger n’s in the Appendix?

### Questions
See my questions in the weaknesses section above.

### Soundness
4

### Presentation
4

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
This paper investigates the mechanisms of ICL under a unified framework. The authors developed a synthetic sequence modeling task using finite mixtures of MCs and studied various phenomena in this setting, including the task retrieval vs. learning dichotomy and emergence of induction heads. They were able to simultaneously reproduce most of these well-known results. Additionally, the authors proposed that ICL is best understood as a combination of different algorithms rather than a single capability -- model configurations and data diversity impact transitions between these algorithms. This shows that ICL behavior can shift based on training data properties.

### Strengths
1. Very detailed and sound study of the ICL mechanism: varying task diversity, training steps, context length, and evaluating on various metrics. This is a very empirically rigorous study that verifies previous literature by reproducing various well-known results within a single setting.

2. Some analysis on how model design affects downstream performance on various metrics.

### Weaknesses
My main concern with this paper is its novelty: as the authors have correctly noted, many of the results presented here have already been explored in existing literature. While this paper offers a valuable unifying study that synthesizes and reproduces previous findings in a single framework, the setting itself has also been examined in prior work (e.g., Edelman et al.). Consequently, the overall message lacks new insights.

### Questions
The Bayesian vs. Non-Bayesian comparison: Generally, I think of Bayesian learning as a form of "learning to learn," where a posterior is updated based on observed data according to Bayes' rule, with a prior typically established during pre-training. Therefore, it is unclear why the comparison between ID and OOD performance specifically reflects a shift between Bayesian and non-Bayesian paradigms. In particular, the analogy between "task-retrieval" vs. "task-learning" and Bayesian vs. non-Bayesian, in my view, does not fully capture the essence of Bayesian inference.

In a Bayesian approach, one would ideally follow Bayes' rule to update an implicit or explicit posterior or posterior predictive distribution. Given this, shouldn’t the KL divergence be examined between the model prediction and the true posterior or posterior predictive distribution (according to Bayes' rule and the correct prior) at each context length (so given the same context of length $l$, examine at each step from $1,\dots, l$)?

I understand that you may be viewing task-retrieval vs. task-learning as a contrast between in-weight learning (IWL) and meta-learning. However, this distinction could also be seen as reflecting a finite, discrete prior versus a continuous or uniform prior. The true Bayesian vs. non-Bayesian distinction, perhaps, is whether the model has learned to correctly update a posterior (i.e., learned Bayes' rule) and has fitted an accurate prior.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce a new ICL synthetic task that consists of sampling from a finite mixture of Markov chains. Their setting reproduces several ICL phenomena, and through extensive analyses, the authors also report results on phase transitions between different algorithms.

### Strengths
I think this is a nice, comprehensive paper that introduces a simple setting that unifies many recent papers on ICL and captures analogous phenomena (task diversity thresholds, transience of ICL). For example, Figure 3 basically reproduces the results of two previous papers. 

The experimental protocols for assessing bigram utilization and proximity to the Bayesian solution were thoughtful and creative.

I like the idea of approximating the transformer’s behavior as a mixture of algorithms. It’s interesting that this can be used to predict OOD and that it highlights a sort of “persistent competition” between implementing different algorithms. This potentially provides a compelling explanation for phenomena like transience. 

There’s also a comprehensive set of ablations that study the impact of width and data complexity etc…

Overall, the paper was fairly clear.

### Weaknesses
First of all, I want to emphasize that I think this line of work is valuable and scientifically meaningful. However, it would be nice to discuss how these insights translate into practical design choices (e.g., predicting OOD performance using a similar approach to this paper). 

I think one major premise of the paper is that there’s a transition between different algorithms. 
I think this is convincing. However, I think I want some kind of control condition where you use 3 or 4 different “silly” algorithms just to confirm that these kinds of phase transitions aren’t some artifact of fitting some linear combination of algorithms and that, if your algorithms are not related to the task, you don’t always see these interesting algorithm phase transitions.  For instance, it would be useful to see if random algorithms, such as predicting the next token uniformly or based on a fixed, arbitrary mapping, would also exhibit similar phase transitions when used in the linear combination analysis. This would help isolate whether the observed transitions are specific to the proposed task-relevant algorithms.

I think I also wanted a bit of better understanding on how well LCA predicts the performance of the transformer relative to some naive baselines just to confirm that LCM well approximate the transformer. For example, it would be useful to compare the performance of the linear combination of algorithms (LCA) to a baseline where the weights are fixed across all training checkpoints. This would help demonstrate that the dynamic weighting of algorithms is necessary to capture the transformer's behavior, rather than just a static combination.

### Questions
This paper identifies a number of these interesting phenomena, but it would be nice if the authors could discuss a bit more about why these phase transitions occur. For example in the LCA analysis, why is there rich structure in these phase transitions when you might (naively) expect a smooth increase in the weights on the optimal solution (e.g., Bi-ICL) and roughly uniform weight on the other solutions? Can you study the properties of the loss function (e.g., Hessian) at these different phase transition points?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
With this paper the authors contribute the following:

* The authors propose a new sequence modelling setting, namely learning to
  predict sequences sampled from a Markov chain sampled from a finite mixture
  of Markov chains.
  * This is similar to the variable 'task-diversity' in-context linear
    regression setting from Raventos et al., but using Markov chains rather
    than a regression model to generate sequences following Edelman et al.

* The authors list four idealised algorithms for solving this sequence
  modelling setting, along two axes of variation, namely:
  * observing either unigram statistics (states) or bigram statistics
    (transitions), and then
  * making predictions by leveraging knowledge of the latent mixture of
    Markov chains, or based solely on the observed frequencies in the
    context.

* The authors devise a pair of tests for distinguishing a learned predictor
  along these two axes, and in doing so reveal that depending on the degree
  of task diversity, the sequence length, and the number of training steps,
  small transformers trained for this task will behaviourally resemble each
  of these four algorithms. This creates the titular 'algorithmic phases'.

* The authors propose a behavioural analysis method, "Linear Combination of
  Algorithms (LCA)" whereby they decompose a transformer's outputs (given
  in-distribution inputs) into a mixture of the outputs of the four idealised
  algorithms. The decomposition is made by projecting the outputs onto the
  probability simplex spanned by the four algorithms in function space.
  The authors track this decomposition over training and observe a close
  alignment between trends in the weight of certain algorithms and trends in
  out-of-distribution generalisation including the "transience" phenomenon.

* This phase isolation methodology and auxiliary metrics replicates a number
  of phenomena reported in prior works on ICL in similar and disparate
  settings, and some new phenomena. In the main text, the emphasis is on the
  following three phenomena:
  * The authors find a 'task diversity threshold' at which transformers
    switch from learning to leverage knowledge of the pre-training task
    distribution to learning to generalises to unseen Markov chains. This
    finding is analogous to that of Raventos et al. for in-context linear
    regression.
  * The authors find that in certain phases transformers develop statistical
    induction heads, replicating the finding of Edelman et al. in a similar
    setting based on infinite mixtures of Markov chains, but for finite
    mixtures of Markov chains.
  * The authors show that with increased training time individual
    transformers shift from initially adopting a generalising method to
    eventually preferring one that leverages information of the training
    mixture. This is somewhat analogous to the "transience" phenomenon
    reported by Singh et al.
  * The authors also claim to replicate other phenomena, but I am less
    familiar with these other phenomena and the details are excluded from the
    main text, so I have not been able to evaluate them.

* The authors argue that their finite mixture of Markov chains setting
  offers a unified setting in which to study the emergence of in-context
  learning, which has previously been studied in disparate settings.

**Summary of my review:**
I was impelled to write a long review. So, I also include a summary of my
review here.

* I think the authors have made a strong contribution in an important area of
  the science of deep learning. Their setting is elegant, expressive, and
  permits an interesting variety of idealised solutions. The results from
  their phase isolation and LCA analyses are interesting and informative.

* However, I think the claims made in the paper at times overstate the
  results or are overly confident given the limitations of the methodology,
  which are not adequately discussed. In particular:
  * The phase isolation methodology is incapable of ruling out plausible
    alternative algorithms undermining the authors' claims that they have
    knowledge of what algorithms the transformer is implementing.
  * The "linear combination of algorithms" methodology, while revealing
    interesting behavioural dynamics, does not seem to me to be worthy of
    being called "mechanistic" nor an "explanation" of the transience of
    particular algorithms or other phenomena.
  * The motivation for proposing a new setting is to unify disparate studies
    on the emergence of ICL, however the proposed setting is not uniquely more
    appropriate for this purpose than alternative settings.

* I believe that the framing is sufficiently misleading that I cannot
  recommend the paper for acceptance in its current state. However, if the
  authors are able to back up their confidence or if they commit to tempering
  their claims then I would be happy to recommend the paper for acceptance
  because I didn't note any major technical flaws and I think the work is
  important and interesting.

* In addition, I note a number of additional questions and more minor
  concerns including about the naming of the "-ICL" algorithms and some
  details of the setting and results, detailed in the questions section of
  this review.

I look forward to the discussion period.

**EDIT TO ADD:** Summary of discussion:

* The authors addressed all of my concerns about the paper's framing.
  * The authors no longer claim that the phase isolation methodology rules out alternative similar algorithms or identifies the precise mechanisms of the learned transformer implements.
  * The authors talk more precisely about the LCA (now: LIA) methodology as revealing only behavioural dynamics.
  * The authors now motivate their work in more moderate terms.
* In addition, the authors added new preliminary mechanistic experiments providing further interesting insight into learning dynamics in their rich setting.
* I believe that the framing is now acceptably accurate. Therefore because of the paper's strengths I am pleased to raise my rating from 5 to 10.

### Strengths
As I said I think this is a strong paper. I note at least the following
strengths.

1. The paper is well-motivated by the importance of of understanding the
   emergence of algorithmic structure inside transformer sequence models,
   which is a priority for the science of deep learning.

2. To this end the authors contribute a neat setting with a clean and flexible
   data generating process and an interesting and rich collection of idealised
   solutions.
   * This setting can also serve as a solid basis for future work, experimenting
     in the same setting or extending it to (for example) higher-order,
     non-Markovian sequence modelling tasks, hidden Markov models, etc., all
     of which are immediately suggested by the authors' framework.

3. The authors have also conducted a comprehensive study of the numerous axes
   of variation in this setting.
   * The replications of phenomena found in prior work is valuable.
   * The classification of the configuration space into qualitatively distinct
     behavioural 'phases' is quite striking.
   * The LCA analysis is thought-provoking.
 
4. The LCA technique, carefully interpreted, is an elegant idea for
   behavioural analysis of models in general, when plausible candidate
   algorithms are known. I like it and I think I would use it (I have noticed
   several opportunities to use this in my research since seeing it in this
   paper.)

Overall I think the paper makes a valuable contribution that enriches our
understanding of ICL phenomenology and creates a rich framework for future
research that can continue exploring this important topic.

### Weaknesses
### W1. Insufficient evidence for confidence in algorithmic phase identification

The authors chose to name their paper 'algorithmic phases of in-context
learning'. I am a believer in the importance of names and I think this gives
me grounds to assume that the authors view their labelled phase diagrams as a
major element of their contribution.

I consider this labelled phase diagram to have two distinct parts. The first
of which is the division of the hyperparameter space into regions where a
trained transformer displays distinct modes of behaviour as quantified by the
behavioural classification metrics outlined in section 4.2 'isolating
algorithmic phases'. I am impressed by this part of the contribution.

I am concerned about the second part, namely the labelling of phases with
specific algorithms. The authors confidently association of each of the four
behavioural phases with one of the four algorithms described in section 4.1
'the Bayesian and non-Bayesian solutions of finite Markov mixtures'. I am
concerned that the authors have not secured sufficient ground from which to
confidently present these algorithms as uniquely accurate descriptions of the
transformer's behaviour in each phase.

**Phase isolation is not exhaustive:**
The phase identification methodology appears to assume a priori that these
are the only plausible algorithms, as if that were the case, then it would be
sufficient to associate these algorithms to each phase. However, these
algorithms do not appear to me to be *uniquely* principled ideal models of
how a sequence model might solve the Markovian prediction task, so I do not
think it appropriate to rule out *a priori* the many other possible
algorithms that could explain similar behavioural patterns and would be a
better 'label' for each phase.

A short list of other algorithms I can think of is as follows:

*   **Unigram- or Bigram-likelihood Bayesian Averaging with a different
  prior:** An algorithm that functions like Uni-Bayes or Bi-Bayes, but uses a
  different task prior probability vector as a starting point for formulating
  its posterior predictive distribution.

*   **Unigram- or Bigram-likelihood MLE or MAP:** An algorithm that functions
  like Uni-Bayes or Bi-Bayes in weighing the likelihood of each task for
  describing the sequence in front of it, but then rather than performing
  Bayesian averaging to make predictions, simply predicts based on the
  most likely task (possibly accounting for the task prior).

*   **Slight modifications of frequency counting approaches:** An algorithm
  that functions like Uni-ICL or Bi-ICL but uses slight modifications to
  frequency counting such as starting the count for each unigram from epsilon
  instead of zero or similar for bigrams, or increasing the predicted
  proportions non-linearly in the counts.

These algorithms are close in function space to the proposed algorithms so
that it were the case that these were more accurate descriptions of a
transformer's behaviour, this would not show up in the phase isolation
metrics (nor in the LCA analysis which is based on projections in function
space---the above algorithms would be nearby in function space and so
projections would be similar). The only ways to rule out these alternatives,
along with every other algorithm, would be to devise specific tests to probe
the behavioural differences between these algorithms and the proposed
algorithms, or to probe the internal computational structure of the
transformers to seek to distinguish the mechanisms underlying their
behaviour.

**On appendix E and mechanistic analysis:** I did notice that the authors
also include additional experiments in appendix E that investigate the
activation patterns in various locations inside the transformer. However,
these experiments are insufficient to rule out the alternatives to Bi-Bayes
and Uni-ICL I have listed above, since for example counting transitions is
also consistent with these alternative algorithms. There are no mechanistic
experiments into Uni-Bayes. It appears the authors have more evidence
consistent with Bi-ICL than the other algorithms including the presence of
statistical induction heads, but the broader point stands.

**Overall:**
To be clear, I believe that the algorithms proposed by the authors and their
experiments are novel and significant. Given the infeasibility of uniquely
associating a particular principled algorithm with a phase, it seems fine to
me to start with approximate behavioural resemblance. I think this is what
the authors have grounds to claim they have contributed---a 'fuzzy' label for
each phase that serves as an initial proxy for what the transformer is going,
and this is worth sharing with the research community.

However, I also strongly believe that the authors have an essential
responsibility to clearly articulate the status of their labels. I am
concerned that in the current form the reader will draw the as-yet
unwarranted conclusion that, for example, transformers perform Bayesian model
averaging (in the appropriate phases). While the algorithmic variations I am
proposing are also deviations from 'optimality' as the authors have framed
the problem, it seems an open question to what extent transformers implement
'optimal' algorithms and to me, modelling the specific variations from
optimality in the pre-trained transformer is an important direction for
future work and it is not yet time to declare that the algorithms have been
definitively identified even in this simple setting.

**Requested revisions:**
I would be welcome the authors to correct my understanding of their
methodology and its limitations, or correct my reading of their confidence.
Otherwise, until this framing issue has been addressed the paper is unfit for
publication in my judgement. I would suggest that the authors commit to the
following revisions.

1.  The authors should amend their presentation to refrain from claiming that
   the transformer implements these particular algorithms. Some examples of
   language I think is unwarranted include (not exhaustive):
   *   Generally in the abstract and introduction any mention of the finding
     that the transformer uses specific mechanisms such as "use of unigram
     vs. bigram context statistics", though it is unavoidable that some
     qualifications must be left to subsequent pages and this is not
     necessarily a sufficient priority in the introduction.
   *   Line 222 "we ... show ... the model selects between these solutions ..."
   *   Line 295 "We now demonstrate the four algorithms proposed above
     perfectly delineate models trained on our task into explicit phases".
   *   Line 345 (emphasis in original) "*Based on these results, we claim our
     proposed algorithmic solutions successfully explain the different
     mechanisms employed by the model to solve our finite mixture of Markov
     chains task.*"
   *   Generally section 5 continues under the presumption that the transformer
     "is implementing" the algorithms from section 4.
   *   Line 527/528: "to write down four algorithmic solutions ... and identify
     their existence in a trained model".

2.  The authors should note prominently and explicitly in the paper (for
   example when introducing their methodology, in the conclusion, or in a
   dedicated 'limitations' section) that their methodology is insufficient to
   rule out other algorithms as being a more accurate description of each
   phase.



### W2. LCA is not mechanistic and does not offer a new explanation

The proposed LCA techniques is described in the abstract, introduction and
figure 1 caption as a "mechanistic analysis" offering a "new" "causal
explanation" of transient OOD generalisation. The terms "mechanistic" and
"explanation" are repeated throughout section 5. I do not see grounds for any
of the terms "mechanistic", "causal explanation", or "new explanation" to be
used in describing this methodology.

**On "mechanistic":** It is inappropriate to call LCA a mechanistic
decomposition. The tool is clearly based on analysing (in-distribution)
behaviour, and it does not reliably reveal internal mechanisms (though it may
do so, or approximately so, in this case). Accordingly, this analysis should
be called "behavioural" rather than "mechanistic".
   
I suppose the authors are using the word "mechanistic" because they believe
that LCA has identified the algorithm implemented by the transformer, and
that this is confirmed by the fact that the in-distribution behavioural
decomposition is predictive of out-of-distribution behaviour. It may very
well be the case that the transformer implements a coherent mechanism and
that LCA has, in this case, identified it (or approximately identified it).
However, LCA is incapable of revealing the mechanistic nature of a general
transformer, and so this reasoning is not sound.

1.  As I argue in the previous section I do not believe they have grounds for
   this, and have only roughly categorised the behaviour rather than
   identified the precise algorithm. LCA will find a decomposition in terms
   of any list of algorithms given to it. If the true mechanisms inside the
   transformer are not represented, it will identify the behaviourally
   closest algorithms as comprising the behaviour.

2.  LCA actually makes it clear that the transformer in some sense implements
   multiple algorithms, not one algorithm, at many points during training,
   since the mixtures are not concentrated. While the authors call this a
   'competition' between algorithms, they have not given any mechanistic
   model of this apparent competition. There are many possible internal
   mechanisms that would lead to such an apparent 'competition' appearing in
   the LCA decomposition, some of which would not even correspond to a proper
   competition but would rather be artefacts of the projection in function
   space.

3.  In this case that the transformer's (lack of) reliance on pre-training
   task statistics is recoverable from in-distribution behaviour and then
   this prediction is validated on out of distribution behaviour, this does
   indicate that the tool happens to have uncovered part of the transformer's
   mechanism in this case. However, LCA would make the same predictions for a
   transformer constructed or trained to follow one mechanism in-distribution
   while following another mechanism out of distribution.

Because it only measures behaviour, LCA should not be called mechanistic. The
predictive power in this case is not coming from LCA but rather from the
apparent fact that the transformer happens to have roughly the mechanism the
authors expect.

**On "new explanation":** The authors also claim that tracking the LCA
decomposition over training reveals an explanation of the phenomenon of the
transience of out-of-distribution generalisation posed by Singh et al. This
explanation is described in the abstract as a "new insight".

As far as I can tell (the authors can correct me here if I have missed
something), by "explanation", the authors refer to their observation that
the shift in generalisation coincides with a shift in the transformer's
algorithm from predominantly resembling Bi-ICL to gradually increasingly
resembling Bi-Bayes later in training. The authors also observe that Bi-Bayes
is a better solution according to the training distribution, so this shift is
in turn explained by the learning algorithm pursuing better on-distribution
performance.

I think there are a number of problems with the framing of these observations
as a new explanation of Singh et al.'s transience derived from LCA.

1.  First, it is not clear to me that the observations go beyond what was
   already reached in Singh et al.'s original paper. In that paper, they
   already talk about one algorithm, ICL, being replaced with a different
   algorithm, "in weight learning" (IWL) with worse generalisation
   performance. The authors of the present paper are pointing to a similar
   trend arising in their replication, but they now have slightly more
   specific models of the algorithms.

2.  Second, note that actually there is an important difference between this
   setting and that of Singh et al.'s transience. Namely, in Singh et al.,
   the ICL and IWL algorithms by construction are equally performant on the
   training distribution. This is a crucial difference in this case. As the
   authors note, in this case, Bi-ICL giving way to Bi-Bayes is even less
mysterious than ICL giving way to IWL in Singh et al., beacause this is
driven by the in-distribution performance.

   A closer analogy to the setting proposed in the present paper comes from
   related work on in-context linear regression. Hoogland et al. (cited by
   the authors) and (slightly earlier and in more detail under the name of
   "forgetting") in the paper by Panwar et al. "In-context learning through
   the Bayesian prism" (from 2023, on arXiv before Singh et al. was published
   actually). These works observe that in the Raventos et al. setting, a
   generalising algorithm gives way in favour of a training-task-dependent
   algorithm, driven by improved in-distribution performance and with a
   concomitant drop in out-of-distribution generalisation performance.

3.  Third, given this prior work, upon reading the abstract I was expecting
   perhaps some deeper explanation for what actually drives this phenomenon.
   For example, some insight into why the transition occurs at a given period
   during training or at a given rate, or why the generalising performance
   was preferred in the first place. I could not find any such deeper result
   in this paper.

4.  Finally, I do not see a connection between LCA specifically and this
   explanation. The transition from Bi-ICL to Bi-Bayes would also show up as
   a shift in the proximity to Bayesian solution metric from the phase
   isolation methodology in section 4. I see no reason to attribute this
   explanation to LCA.

I certainly believe LCA offers a particularly crisp behavioural perspective
on this transition. But given all this, I think a more appropriate framing
for the authors' contribution would be to say that in addition to replicating
the transience phenomenon, the authors have used LCA to offer a new and
detailed perspective on the (behavioural) competition between algorithms
already thought to underlie the phenomenon of transient generalisation.

**On "causal explanation":** As far as I can tell, "causal" is only mentioned
in the introduction. I don't see any grounds for its inclusion here at all. I
suggest it should be removed.

**Overall:** I believe LCA is an interesting and useful behavioural
technique, but unless the authors can persuade me otherwise I am strongly
opposed to the framing in the introduction and throughout section 5 that the
technique is capable of offering mechanistic insights or that it has offered
a new explanation of the phenomenon of transient generalisation in in-context
learning.


### W3. The motivation in terms of unifying and generalising phenomena is inaccurate

Upon first reading the abstract and introduction I understood this paper to
be claiming that there is a need for:

1.  an assessment of whether existing phenomenology are specific to the
   settings in which they were first found or whether they generalise to
   other settings and are thus more likely to be inherent features of ICL,
   and 
2.  a unified setting in which the various phenomena of ICL that have been
   studied in prior work can all be studied in one place.

The authors don't seem to be positioning this as a motivating vision toward
which they are contributing a 'first step' or something 'in this direction'.
Rather, they say for example in the abstract that their work "enables a
unified framework for studying" ICL. In the introduction they claim that
findings from prior work may be "disparate findings that manifest in specific
scenarios".

I think this motivating story is not an accurate description of the state of
the field and I think the degree of unification achieved in the paper is
strong but not as strong as the authors claim on this first page.

**On generalisation:** It appears to me that the authors have indeed provided
a novel contribution by 'generalising' several prior phenomena by exhibiting
them in a new setting. This is indeed a valuable contribution. However, it
appears that most of these phenomena have already been exhibited in multiple
settings, so it is inaccurate to claim that the phenomena were previously
only known to hold in isolated settings.

*   In the case of the task diversity threshold, the authors have generalised
  this to the Markovian sequence modelling setting. Previously, it was shown
  for in-context linear regression (Raventos et al.), along with image
  classification (Kirsch et al.) as cited by the authors. The same phenomenon
  has recently been shown in a multi-task modular addition setting by He at
  al. in a recent preprint "Learning to Grok: Emergence of in-context
  learning and skill composition in modular arithmetic tasks".

*   In the case of the emergence of statistical induction heads, there is only
  a very minor generalisation taking place since statistical induction heads
  were already shown by Edelman et al. to arise in Markovian sequence
  modelling with infinite mixtures of Markov chains. The generalisation to
  finite mixtures of Markov chains is, in my opinion, valuable but not very
  surprising especially given that the original exhibition of induction heads
  by Elhage et al. and Olsson et al. was in the completely distinct setting
  of language modelling.

  Moreover, I am not aware of induction heads being found in other settings
  such as in-context linear regression. If any ICL phenomenon is isolated to
  certain settings, this suggests that induction heads represent such a
  phenomenon.

*   In the case of transience, it's true that Singh et al. study a specific
  scenario that is designed specifically to isolate this phenomenon, but it's
  not true that their findings have not been replicated in other settings.
  In the previous section I already noted work noting transient
  generalisation for in-context linear regression including Hoogland et al.
  (already cited by the authors) and the earlier work by Panwar et al.
  Beyond in-context linear regression, He et al. "Learning to grok"
  (mentioned above) have also demonstrated transience in in-context modular
  arithmetic.

  These examples actually seem more relevant to the present work than Singh
  et al., as they concern transitions between two different ICL algorithms,
  rather than between ICL and pure memorisation as in Singh et al.

*   (I have not evaluated the novelty of generalising the other phenomena, as I
  am less familiar with these parts of the literature, and moreover the above
  three phenomena are the ones the authors discuss in the main text.)

Once again, I believe the authors have made a strong contribution, but my
concern is that they have not accurately described it in their abstract and
introduction, and they need to reframe their contribution in a more accurate
manner in my opinion.

**On unification:** Moreover, I did not find the motivation in terms of
unification compelling.

To me it seems like the extent of a 'unification' achieved by the authors is
that they have combined multiple interesting axes of experimental variation
(e.g. studying models at varying task diversity and training time) previously
varied individually in prior work. They have created one setting rich enough
to include these axes of variation, and they have demonstrated that along
each of these axes previously studied phenomena are replicated in their
experiments. I will repeat that I find this comprehensive investigation of
the axes and their combinations is a strong contribution.

However, in describing this contribution, 'unification' seems too strong of a
word. When I read the word unification, I think the prior settings should be
recoverable as special cases of a more general setting. Operationally, the
field should be able to continue forward by discarding previous settings in
favour of using a truly 'unified' setting. I think this standard has not been
met by the proposed setting. Rather, if the field universally adopted the
proposed setting, at least the following research directions would be
precluded.

1.  Different settings encourage different mechanistic solutions in the
   transformer's internals. For example, while the Markovian setting allows
   one to study statistical induction heads, one does not have the ability to
   study the particular mechanisms that emerge in order to perform in-context
   linear regression or modular arithmetic. For the field to make progress on
   mechanistic analysis of in-context learning in transformers, it seems
   useful to be able to take advantage of the various constructions that have
   been proposed for specific implementations of in-context linear
   regression, for example. I don't see why we shouldn't try to keep our
   range of interesting synthetic settings as broad as possible.

2.  Another example comes from the quite specialised setting studied by Singh
   et al., where, by construction, ICL and IWL are equally performant on the
   training distribution. Nevertheless, there is still an algorithmic
   transition between these algorithms at some point in training. This gives
   rise to questions that can't be asked or answered in a setting where the
   main four algorithms achieve quite different performance in-distribution,
   such as what drives the transition even in this case (when the need for
   better in-distribution performance is ruled out as an explanation for
   driving this transition).

The authors have included appendix G with some discussion on the perceived
benefits of studying Markovian sequence modelling tasks rather than modular
arithmetic or linear regression due to the lack of "sequence space structure"
in these alternative settings.
I must admit unfortunately I did not follow the discussion despite trying to
see their point of view. It is not immediately clear to me what sequence
space structure means. But if the authors refer to the fact that in Markovian
sequence modelling in order to count bigrams the transformer must look at
pairs of tokens, I note that even though modular arithmetic and linear
regression are usually formulated in-context using an i.i.d. sequence of
inputs, it is still necessary for example in Raventos et al.'s setting for
the transformer to look at pairs of sequence items (one containing the x and
the next the corresponding y). It is not clear to me how this is less rich
than looking at bigrams.

**Overall:** I can't emphasise enough, I really like the setting and the
comprehensive analysis along multiple axes. I am only concerned that the
introduction does not provide an accurate motivation for the work, and I
would like to respectfully challenge the authors to lay out a stronger case
for their contributions in their introduction. Doing so, in my opinion,
should not be too hard, because the authors have made some strong
contributions on an important topic.


### Questions
I collect various questions, minor concerns, or suggestions that occurred to
me while reading the paper. Given the length of my review I don't expect the
authors to respond to all of these questions (though I would be happy for
them to do so). If the authors are interested in me revising my decision and
have limited capacity in the discussion period I would recommend that they
engage with me on the three weaknesses before the contents of this section.
More importantly I hope that they might consider my questions and suggestions
and consider revising the paper to improve the presentation as they find most
appropriate.

**Q1. The four algorithms have unclear and misleading names.**
As I said, I am a believer in the importance of names. I felt strongly that
the choice to use '-ICL' as a suffix in the names of 'Uni-ICL' and 'Bi-ICL'
is a mistake that undermines the quality of the paper. By selecting these
names the authors have at the same time created the following two problems.

1. They have conflated one half of their list of algorithms with the concept
   of in-context learning, entrenching a false connotation that these two
   algorithms are more exemplary instances of ICL algorithms than others, in
   fact that the Bayesian solutions are not classified as ICL.
   This contradicts the authors' stated message in the abstract and
   conclusion, that ICL is an umbrella concept that encompasses multiple
   concrete algorithmic instantiations. Recalling again the paper's title,
   all four phases are supposedly 'of in-context learning'.
   I do not think that the authors mean to hold up Uni-ICL and Bi-ICL as
   'truer' examples of ICL than the 'Bayesian' algorithms, yet this is what
   their naming choice achieves.

2. They have missed an opportunity to communicate what is unique about these
   particular ICL algorithms. This is the role played by 'Bayes' in the names
   'Uni-Bayes' and 'Bi-Bayes' (in my reading this helpfully conveys that the
   methods use Bayesian averaging). I leave it to the authors to decide what
   would be an appropriate analogue of 'Bayes', but I invite them to consider
   using the term 'frequencies' or 'induction' and I urge them to avoid
   anchoring on induction *heads* themselves (a feature of transformers
   rather than ideal algorithms) or using the misleading 'non-Bayesian'
   terminology of Raventos et al.

I respect the right of the authors to name the algorithms. I can't say this
concern alone would prevent me from recommending the paper's acceptance.
However, in this case I feel strongly enough to register my protestation
about the names given my fresh perspective on the algorithms and the authors'
chosen takeaway message.


**Q2. Inconsistent summary of algorithms between main text and figure 4
caption:** In the figure caption, the Uni-Bayes and Bi-Bayes descriptions
talk about selecting a 'closest task' from the mixture. Based on the main
text, my understanding is that they do not select a single task but rather
they form a posterior distribution over all tasks and use the posterior
predictive distribution to make their prediction. Using the 'closest
distribution' sounds more akin to using a maximum likelihood distribution,
rather than using the posterior predictive distribution.

**Q3. Questionable choice to use a nonuniform task prior:** If I understand
correctly from the setting description, the authors sample a prior vector
from a uniform Dirichlet distribution over task priors. The resulting prior
will be almost certainly non-uniform and with high likelihood for high task
diversity it will have a small number of tasks with quite large
probabilities and a large number of tasks with very small probabilities. It
follows that after a reasonable amount of pre-training there may be some
tasks that have barely been sampled at all.

This seems to me to be a significant departure from the use of task diversity
by of Raventos et al., for whom, if I remember correctly, the task prior is
always uniform. I believe that having a skewed task distribution may confound
experiments since what I would call the 'effective task diversity', meaning
roughly the number of tasks the transformer has to 'memorise' in order to get
good performance on in-distribution evaluation (assuming tasks are sampled
from the same skewed prior for ID evaluation) will be smaller than the
specified task diversity, since the transformer can get away with not
remembering low-probability tasks.

The inclusion of this additional complication appears to be unjustified by
any particular argument in the manuscript. I would be curious if the authors
have a strong reason for including this detail. Of course, it is a virtue of
the setting that one can consider different distributions of tasks, since
this might be an interesting direction for future work, but such work would
surely involve *systematically* varying the prior rather than abdicating
control over the prior by sampling it from a high-dimensional Dirichlet
distribution.

Finally I note that it is regrettable that this detail appears to be
documented only in the appendix.

**Q4. Convoluted phase isolation tests:** These test seems very intricate. It
is not clear to me that they are the clearest ways of isolating phases, and I
wonder if you have considered and ruled out simpler alternatives.

1. For the bigram utilisation test, it occurs to me that the predictions of a
   model paying attention exclusively to unigram patterns would not vary much
   depending on the current state (at least late in the sequence). On the
   other hand, bigram-based models would vary their prediction based on the
   state. Therefore, I wonder if you have considered a simpler test of
   somehow quantifying uniformity in the set of rows of the revealed
   transition matrix?
2. For the proximity test, I wasn't able to think of a simpler test, beyond
   the idea that perhaps something with generalisation performance could be
   used.

**Q5. Missing details for proximity test:** I was left wondering about some
details of the proximity test. Unless I missed something, I would recommend
clarifying the following points, if possible in the main text or otherwise by
expanding on the 'additional details' in the appendix.

1. How is distance to a set of tasks defined? Is it the distance to the
   closest member of the set?
2. Does the measurement of distance to the training task set account for the
   task prior at all? I am concerned that for example if the closest task in
   the training set happens to be a task with very low prior probability,
   then this task will not draw the model's posterior towards that closest
   task, and the posterior may be more likely to be falsely detected as
   closer to a random task than if the closest training task happened to be
   one with higher prior probability.
3. How is the chain that is not part of the training set or the control set
   sampled?
4. I think I can guess how you turn the procedure you outlined into a single
   number used to colour your phase diagram, perhaps it involves repeating
   this procedure several times, and estimating an empirical probability of
   the closest task being from the training set, giving a number between 0
   and 1. If this is correct, I think it is worth spelling out in the text,
   as well as noting somewhere how many trials you take. If this is wrong
   then it's definitely worth spelling out in the text.

**Q6. Missing details about figure colour schemes:** 
The phase isolation methodology and the LCA analysis are two distinct methods
for colouring a point on a phase diagram. I realised that it is not always
clear which of these methods you are using in each of the diagrams. It is
clear in Figure 4 and figure 5 where these techniques are explicated. For the
remaining figures, I am not sure which methodology you use, and I couldn't
find it documented anywhere. Please consider clarifying this in each figure's
caption.


**Q7. Why is LCA formulated in terms of L2 distance for probabilities?** It
would seem more natural to minimise cross entropy or KL as is used elsewhere
in the paper, and this would allow a clearer comparison to other quantities
such as model KL vs. LCA KL and so on. I don't think this is necessarily a
major issue but I just wondered if the authors had a good reason for it.


**Q8. What is the relationship between LCA and delta metrics from Raventos et
al.?** Raventos et al. consider two setting-specific metrics, they denote
them 'delta ridge' and 'delta dMMSE', measuring the L2 distance between the
predictions of their pre-trained transformer and those of their idealised
linear regression algorithms (ridge regression and dMMSE). These are
essentially measures of how close in function space the transformer is to one
of the algorithms. Have you thought about the relationship between these
metrics and LCA?


**Q9. How close is the LCA fit?** LCA weights are defined via a least squares
optimisation problem. In figures 6 and 7 the authors plot the argmin weights.
What is the min? In other words, how large is the irreducible component of
the least squares loss representing the distance of the transformer from the
simplex spanned by the four algorithms in function space?

It is important that this metric remains low in order to believe that the LCA
has captured something meaningful about the behaviour, rather than a very
lossy projection of the behaviour. Therefore I believe the authors should
report this metric in the paper, if not in the main text then at least in an
appendix.

A somewhat related metric appears to be the comparison between the LCA KL and
the Model KL in figure 6. However, if two models have similar KL from the
ground truth sequence that does not necessarily imply that they have low KL
between them. It would be informative to add the KL between the LCA and the
model to the two lines in these figures. This would play a similar role to
the residual.


**Q10. Non-ICL algorithms early in training:** Figure 6 shows shifts in the
model's development across training. One lesson from Hoogland et al. (a paper
cited by the authors in the appendix) is that the choice of algorithms early
in training might be even more unsophisticated than those that eventually
arise at convergence for a given task diversity and sequence length
configuration.

For example, early in training, I hypothesise that some of these transformers
might behave in a way that is well-described by an algorithm that does not
involve any in-context learning at all. Some particular algorithms that I
would consider searching for include the following:

* **Unigram prior:** Learning the average stationary distribution from all
  tasks and predicting tokens based on this distribution without looking at
  context.
* **Bigram prior:** Learning the average transition matrix and predicting
  based on this without looking at context.

Have the authors considered adding such non-ICL algorithms into the LCA
analysis? I would be curious whether doing so reduces the residual at all.


**Q11. Questions about evaluation:** Two small questions about the methodology
for evaluation.

1. During ID evaluation, what prior do you use for sampling the tasks from
   the set of tasks? Do you use the training prior or a uniform prior? You
   just say you 'choose one from a set.'
2. During evaluation (for both ID evaluation and OOD evaluation), how many
   tasks do you sample?

**Q12. Sample implementation of data generating process:**
Could the authors please clarify the relationship between the sample
implementation of the data generating process and the actual code used in
experiments?

I take the description of the implementation to imply that this is not the
implementation used in the experiments. This opens the possibility that it
may actually differ in important ways from the actual methodology used in the
experiments. There are certain details, such as the fact that the sequences
drawn from each chain are initialised with a sample from the stationary
distribution of the chain, do not appear to be noted in the
manuscript in any form other than in the reference implementation.

If the authors intend to open source their codebase after the peer review
process as noted in appendix J then I wonder if they intend to keep this
reference implementation in the paper?

Have the authors considered mentioning any details such as the initialisation
of sequences in text form as well as in code form?



**Q13. Paper structure:** On first read I found it slightly difficult to
follow the paper's first few sections. There is a lot going on in the paper,
between the problem, the phenomena, the phases, and the explanations.

I personally found understanding the phases helpful to my understanding of
the remainder of the paper. I wonder if the authors have considered promoting
section 4 to come before section 3? Of course, this is up to the authors.


**Q14. Terminology and notation:** A small number of minor notes.

1. Have you thought about whether the 'phases' are indeed phases in the sense
   of physics?
2. A bold "1" is overloaded as both a vector of ones (when describing the
   configuration of the Dirichlet distribution) and also an indicator
   function (line 232). I wonder if the authors have considered for example
   using blackboard bold for indicators, to avoid any potential confusion,
   not that I think the risk of confusion is particularly severe.

**Q15. Typos:** (just the ones I happened to notice):

1. Line 186/187: I think there is a stray closing parenthesis.
2. Line 422: "more experiments on this sorts".
3. Line 870--: The variables in this list look like they should be typeset in
  math mode.
4. Line 1638: unfinished sentence.
5. Line 2024: "BICL", is this meant to be Bi-ICL?

### Soundness
4

### Presentation
3

### Contribution
4
