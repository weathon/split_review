# Complexity of Formal Explainability for Sequential  Models

- Decision: Reject
- Avg Score: 5.80
- Scores: 6, 6, 6, 6, 5

## Abstract
This work contributes to formal explainability in AI (FXAI) for sequential
    models, including
    Recurrent Neural Networks (RNN), Transformers, and automata models from
    formal
language theory (e.g.  finite-state automata). We study two common notions
    of explainability in FXAI: (1) abductive explanations (a.k.a.  minimum sufficient 
    reasons), and (2) counterfactual (a.k.a. contrastive) explanations.
    To account for various forms of sequential data (e.g. texts, time series,
    and videos), our models take a sequence of rational numbers as
    input. 
    We first observe that
    simple RNN and Transformers suffer from NP-hard complexity (or sometimes 
undecidability) for both types of explanations. The works on extraction of 
automata from RNN hinge on the assumption that automata are more interpretable
    than RNN. Interestingly, it turns out that generating abductive explanations
    for DFA is computationally intractable (PSPACE-complete), for features that
    are represented by regular languages. On the positive side, 
    we show that deterministic finite automata (DFA) admit polynomial-time 
    complexity for counterfactual explanations. 
    However, DFA are a highly inexpressive model
    for classifying sequences of numbers. To address this limitation,
we provide two expressive extensions of finite automata, while preserving 
    PTIME explainability and admitting automata learning algorithms: (1) 
    deterministic interval automata, and (2) 
    deterministic register automata with a fixed number of registers.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This is a quick review given on a short notice. I did not check in details the
proofs in the appendix.

This paper studies the complexity of two types of interpretability queries, in
the setting of formal interpretable AI (FXAI):
- Computing “minimal sufficient reasons”, also called “abductive explanations”:
  for a given model M and input x over a particular set of features, compute a
  minimal set of features such that setting their values to those of x suffices
  to obtain the same classification as x (i.e., all completions are in the same
  class as x)
- Computing “counterfactual explanations” also called “minimum change required”.
  Here we want to know what is the minimum number of feature values to change
  so that M changes its mind on x. In more generality, given a metric m over
  the possible inputs, one want to find a closest input x to y according to this
  metric so that y and x are not classified the same.

These queries have already been studied, but not for sequential models, which
this paper does. The models that it considers are RNNs, Transformers, and
variants of finite state automata (FSA) for sequences of rational numbers, with
ranges of rationals as transitions (called interval automata), and possibly
with registers that can do comparison (k-DFAs if the automata are
deterministic and k registers, k-NFAs if nondeterministic). The features are
regular languages. Metrics considered are Hamming distance, Edit distance, and
Dynamic Time Warping Distance (DTW).

The results are:

* For RNNs and Transformers
1. minimal sufficient reason is undecidable
2. checking the existence of a counterfactual explanation is undecidable for
   DTW, and NP-complete for Hamming and Edit distance

* For FSAs:
3. Checking the existence of a minimal sufficient reason is PSPACE hard
4. For a fixed k, computing the minimal distance of a counterfactual
   explanation is PTIME over k-DFAs, for all distances mentioned above 
5. computing the minimal distance of a counterfactual explanation over k-NFAs
   is NP-hard for Hamming and edit distance, and PSPACE for DWT.

### Strengths
The idea of using complexity theory to formally compare the interpretability of
various queries over various models is not new, but the originality here is in
studying FXAI interpretability queries for sequential models instead of models
that only accept inputs of a given length. The idea of using regular languages
for the features is interesting, but it is not clear if this is something new
that the authors are the first to propose, or if this has been already
considered elsewhere. The paper is overall well written and relatively easy to
read (modulo the typos). The topic and results are definitely of interest for
ICLR. I found the proof technique for result 4 is interesting.

### Weaknesses
********** Propositon 3 seems to directly contradict Proposition 2: interval automata
are more general than DFA, generating is harder than deciding the
existence... In fact the proof of Proposition 3 stops in the middle, and I could not
locate the proof in the appendix  **************** 
This has to be fixed. This is why I put a soundness score of 2, but if it was only a mistake 
from the authors with their latex files during submission and is corrected the soundness score could go higher
--------> This has been fixed in the updated version

- results 1, 2 and 3 listed above seem to me to be straightforward translations of
  existing folklore results. While I agree that there is value in translating and stating these results
  into the world of FXAI, I find it weird to state these as contribution, theorem, etc, when
  they could simply be observations that derive from existing work

- p2 "the same problems were shown to be solvable in polynomial-time for
  decision trees and perceptrons Barceló et al. (2020)": This is misleading.
  According to Barceló et al. (2020), proposition 6, minimum sufficient reasons
  is NP-hard for decision trees.



### Questions
- Beware that minimUM and minimAL sufficient reasons might no have the same
  complexity: for instance minimUM is NP-hard over decision trees, but minimAL
  is trivially in linear time for decision trees. In the introduction you mention minimUM, but in
  the rest of the paper you seem to use minimAL everywhere. This should be clarified (see also the comment
on NP-hardness of minimum vs ptime of minimal for decision trees)

- p4 why do you forbid an abductive explanation to be empty? I think that your
  definition is broken and should be fixed as follows: it is simply a minimal
  (under inclusion) subset of features such that v satisfies all features and all
  completions are classified the same. If this set turns out to be empty, this
  just means that the model is constant, and so the "empty" explanation simply
  explains this.

- Proposition 2, and in general: you could also consider the setting where the
  set of features is fixed, which would give you PTIME for DFAs. 

I do not really see the point in spending the
  space to define RNNs in the main text since you are not really using it in the
  end... This could be hidden in the appendix

Typos and minors
- In the abstract, first "DFA", then "deterministic finite automata (DFA)": swap 
- p5 "that there exists an RNN over...”: existence is not enough I think, you
  need to be able to compute it.
- p6 "let \Psi be any intervals": you mean the set of intervals?
- p6 definition of a run: P is not and should be quantified
- p6 "An interval automaton": missing verb
- p6 "is a sequence of numbers in the range..." -> "is the set of sequences of numbers in the range..."
- p6 "of interests" -> interest
- p6 "The  complexity of a counterfactual query": what does this mean? checking
  existence? checking if there is one with distance \leq k with k given as
  input?
- p7 "(\infty, \infty)" -> ( - \infty, \infty) 
- p9 "RNN and Transformers are either difficult": English

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the theoretical problem of generating abductive explanations and counterfactual explanations of ML models. The paper establishes negative results for extracting these explanations from RNNs and Transformers and then focuses on automata models, for which some PSPACE results can be extracted.

Overall, this seems like a solid theory contribution, but I don't see the relevance to ICLR.

### Strengths
Solid, clean automata theory.

### Weaknesses
1. The class of explanations here fail to convince me that any of the XAI goals are achieved.
2. Even if explanations could be generated for the purpose of checking them with formal tools, in what applications would it be helpful given the definitions of "abductive" and "counterfactual" explanations. The example on the top of page 2 does not convince me in the slightest, given that in modern applications features are basically never equipped with clean semantics as assumed here.
3. The paper starts with some very simple negative results for RNNs and Transformers and then focuses almost entirely on automata models (DFA, NFA, and Interval Automata) that have an unclear connection to most work in ICLR.

### Questions
The paper focuses on DFAs and Interval Automata. How are they related to machine learning? Could you give examples that also motivate the class of explanations you consider in this work?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the complexity of abductive and counterfactual explanations in sequence models such as RNNs, Transformers, DFAs, interval automata, and register automata. Here an abductive explanation is a form of minimal property test that shows when the output of the sequence model would change. Similarly, a counterfactual example is a "distance" bounded input sequence that results in a different output. 

The results for RNNs and Transformers are mostly negative, following well known issues with Turing completeness. However, motivated by work on extracting automata from neural models, the paper studies the complexity of such explanations in the aforementioned automata classes. They provide a series of theorems and proofs which characterize the complexity.

The key results are the PSPACE completeness of abductive explanations for DFAs and the efficiency of counterfactual explanations for the studied automata classes (DFAs, NFAs, interval, and register).

### Strengths
1. The paper does a good job laying out the theoretical machinery needed to understand the abductive and counterfactual explanations. Further, when present (see below) the technical material seems to be sound, with the proofs being easy to follow.

2. The topic of explainability of sequence models is certainly important.

3. The classes of explanations discussed have utility and are motivated by similar definitions in the corresponding literature.

### Weaknesses
1. The exposition of the paper would greatly benefit from worked examples. It took a bit of studying to fully internalize the definitions presented in the paper and that is given a fair amount of automata theoretic background.

2. Unless I'm missing something, the proof of Prop 3. seems incomplete! The sentence ends with "This is equivalent to checking". I imagine this was an oversight during submission.

3. I'm actually having a hard time reconciling Prop 3. with Prop 2. In particular,  the paper rightfully points out that interval automata strictly generalize DFAs. Then shouldn't the results of PSPACE-hardness transfer? Otherwise, I could lift the properties F and target DFA to the corresponding singleton interval automata, solve. This seems like a polynomial reduction?

4. Regarding the proof Prop 2, isn't DFA intersection / minimization poly time -- intersection is at product construction and minimization is polytime due to hopcroft's algorithm. So testing emptiness should be polytime. Why does the proof imply PSPACE-completeness?

### Questions
Additional questions:

1. See points 3 & 4 in weaknesses.
2. Do the negative results for non-determinism resolve if restricting to residual automata? They have many of the properties of DFAs while still admitting non-determinism.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the computational complexity of explainability questions, both abductive and counterfactuals, over sequential models ranging from finite automata to Transformers.  All questions are computationally hard for RNNs and Transformers, but some are tractable for DFAs, and the paper shows that DFAs can be extended while keeping polynomial time complexity.

### Strengths
- The paper is well written and it is easy to read; the structure flows well and the body presents the right amount of detail about the proofs and technical aspects.
- The appropriate work seems properly referenced and presented.
- The paper presents novel results and focuses on sequential models, which are arguably one of the most important classes of models at the moment, and yet most formal XAI focuses on classification models.
- Proofs seem to be sound; I fully checked a couple of them and skimmed through the rest and they all seemed to be correct.

### Weaknesses
 - In terms of presentation I think a small table summarizing all results would be helpful; the complexity landscape of the different queries is spread through the text right now.
- The main weakness of the paper in my opinion is that the complexity analysis doesn't seem to provide much new insight into the models or the explanations themselves. The counter to this point is that the presented extensions to DFAs seem like an interesting direction inspired by the complexity analysis. Nonetheless, there is no experimental evidence showing that they can be useful in practical prediction tasks, or directions towards making them more practical.

### Questions
I don't have particular questions besides the points mentioned as weaknesses. Perhaps something that could help the evaluation of the paper is some justification for this work being fit for the venue; at least superficially it seems of a slightly different nature than most ICLR work.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This purely theoretical paper is devoted to formal explainability of
sequential ML models, e.g. RNNs and Transformers. Namely, the paper
lifts the apparatus of formal XAI (FXAI) to sequential models and
studies the problem of checking whether there exists a single formal
abductive explanation or a single formal contrastive explanation for
such a model's prediction and offers a few theoretical results
demonstrating the complexity of this problem. Then the authors discuss
the complexity of the same problem for various types of automata
showing some negative (intractability) and some positive (polytime)
results in this domain.

### Strengths
- This paper discusses the complexity of testing whether there exists
  a formal explanation for a sequential ML model. Although this is not
  the first work on the subject (I've already reviewed a few this
  year), but the theoretical contributions seem clearly novel to me.

- The paper looks rigorous in terms of the problems studied and
  propositions claimed. I haven't checked the proofs but the results
  make sense to me.

### Weaknesses
 - This is a purely theoretical paper with a list of propositions and
  proof sketches but with absolutely no practical side of things. No
  experimental evidence is provided either. As a result, whether or
  not FXAI is usable in the context of such models is left unclear.
  (Recall that AXp's and CXp's are known to be in general intractable
  to compute for non-sequential models; so no big deal.) This makes me
  wonder why this line of work can be deemed relevant for a conference
  like ICLR. (KR would be a nice fit but ICLR is hard to justify.)

- On a similar note: overall presentation could and should be
  significantly improved. Definitions of abductive and contrastive
  explanations in the context of sequential models are given in a
  somewhat lazy way. (The models are defined similarly.) Also, the
  paper gives no examples whatsoever that would demonstrate how these
  explanations look like for sequential models. As this paper claims
  to be the first of its kind, such examples should be provided.

- No algorithms to be used for computing such explanations are
  proposed (even in theory). This exacerbates the issue of the venue
  choice above.

- Minor: on p9 there is a sentence: "This type of explainability falls
  within the category of post-hoc local model-agnostic explanations".
  No, it does not. Both abductive and contrastive explanations are
  global. None of them are model-agnostic as you have to reason about
  the model's behavior formally and hence require access to its
  original representation.

### Questions
- Can you show a clear example of an RNN model, some of the instances
  it takes as input and also exemplify abductive and contrastive
  explanations for some of the model's decisions?

- Are the algorithms originally proposed for AXp and CXp computation
  are directly usable in this setting? If not, how should one compute
  them?

- Can you summarize the differences between the complexity of these
  problems for non-sequential and sequential models? This way, can you
  contrast your results with what is already known to hold in general?

- Why do you need 1 ** k in the informal definition of a CXp? It
  doesn't seem to be used anywhere, does it?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
