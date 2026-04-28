# Provable Length Generalization in Sequence Prediction via Spectral Filtering

- Decision: Reject
- Scores: 6, 3, 5, 8

## Abstract
We consider the problem of length generalization in sequence prediction. We define a new metric of performance in this setting -- the \unfairregrettext -- which measures regret against a benchmark predictor with longer context length than available to the learner. We continue by studying this concept through the lens of the spectral filtering algorithm. We present a gradient-based learning algorithm that provably achieves length generalization for linear dynamical systems. We conclude with proof-of-concept experiments which are consistent with our theory.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper considers the problem of sequence prediction of linear dynamical systems, and studies 
whether it is necessary to remember the entire history of inputs 
to predict optimally. To this end, the paper introduces the notion of asymmetric regret, which 
is the regret of the learner compared with a comparator which uses a longer context than the 
learner. It is shown that the class of spectral filtering algorithms can guarantee $\sqrt{T}$
asymmetric regret, under suitable assumptions, demonstrating that these existing algorithms can 
achieve non-trivial context-length generalization with no modification

### Strengths
- The study of context length generalization is interesting and has a lot 
of practical relevance, especially given the recent surge of interest in 
transformer architectures. 
- The paper is generally well-written and easy to follow

### Weaknesses
- The asymmetric regret seems to be a *weaker* notion than usual regret; often regret guarantees 
hold for an *arbitrary* comparator, which would include comparators that utilize more information 
than the learner as a special case. Yet 
it is claimed on lines 258/259 that "The comparator can observe more information. Thus, this is a stronger, more difficult guarantee to obtain than classical regret."

- The experimental results in figure 5 seem flawed; the shaded regions 
imply that the models can reach accuracy above 100%. I assume the 
shaded region must be $\pm$ some measure of spread (unspecified), 
but this doesn't make sense when it extends outside the domain of the 
measurement.

### Questions
- Why do we necessarily care about competing with the best LDS predictor? 
One receives the input/features before predicting, making it possible to 
make "improper" predictions. For instance, the Vovk-Azoury-Warmuth forecaster 
guarantees logarithmic static regret without any assumptions on the data 
by leveraging improper predictions. Analogously, it could be the case that 
the best LDS predictor is much worse than the best improper predictor.

- I don't understand how the problematic eigenvalues of A are non-extremal ones; what
exactly is special about the upper and lower bounds, that causes problems 
in the range between them?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies length generalization in linear dynamical systems from the perspective of spectral filtering.  Length generalization, the phenomenon by which models trained to conduct algorithmic tasks on short sequences can then accurately apply the same algorithmic principles to longer inputs, has seen much recent interest in language models.  The authors examine a similar problem in the context of noiseless LDSs, where they define length generalization though a new notion of regret they call Asymmetric Regret that allows the comparator policy to incorporate a longer history than the learner can.  The authors leverage recent results on spectral filtering to demonstrate that some marginally stable linear systems can be learned (in the sense of Asymmetric Regret) using a natural online empirical risk minimization algorithm defined by small Frobenius norm linear functions on a basis given by spectral filters.  The authors then demonstrate that this algorithm attains good Asymmetric Regret as long as the spectrum of the eigenvalues of the system matrix A satisfies a certain technical assumption.  Finally, the authors conclude with two experiments: first showing that their assumption on the spectrum of A appears to be necessary by considering synthetic data from randomly generated LDS's and second showing that a certain neural architecture motivated by spectral filtering appears to length generalize when considering induction heads.

### Strengths
This paper sets out to study length generalization and proposes a new definition that formalizes the concept, at least in the task of sequential prediction.  Furthermore, they demonstrate that in the context of noiseless LDS', a natural algorithm based on earlier work in linear control succeeds in length generalization according to their proposed definition.  The proofs are correct as written and clearly presented.

### Weaknesses
I think the work has several major weaknesses:

1. The authors claim their study is motivated by the challenge of length generalization in LLMs, but they did not spend sufficient time justifying the connection between this motivation and their actual results.  I will discuss the empirical aspects below, but on the level of theory, it is not completely clear to me to what extent the study of online prediction in LDS's provides intuition for LLMs.  I think one way of connecting these two disparate concerns would be to note that because LLMs are trained with next token prediction, one may think of generation as an online prediction problem and thus Asymmetric Regret is a natural target notion as the LM is trained to produce algorithms with good `symmetric regret' on algorithmic tasks of interest, but, in order to length-generalize in a meaningful sense, small asymmetric regret (with respect to the longer sequence) is necessary.  If this is the way the authors are thinking about it, it would be helpful if they were to spell this out.  Assuming that this is correct, I guess I am a little confused as to what this means for length generalization in the context of LLMS?  It is not at all obvious to me that the theoretical results necessarily suggest that the Spectral Transform Unit of Agarwal et al 2023 is helpful in length generalization (at least beyond noiseless linear dynamical systems).  What broader intuition are we supposed to glean from the main theorem?

2. I think that the strength of the technical contribution may not quite meet the high bar set by the standards of the conference.  While it is nice that the authors introduce this notion of Asymmetric Regret, it is not entirely clear to what extent it is meaningful beyond the setting of LDS'.  Furthermore, on the level of proof techniques, as said in the paper, Lemma 5 is essentially standard.  Lemma 6 follows from elementary computations on top of earlier work by Hazan et al 2017 and standard results in the field of online control.  Finally, the main theorem is immediate from applying these two lemmata.  Thus, I am a little unclear as to the extent of the technical contribution beyond the introduction of the Asymmetric Regret.  Furthermore, it might be helpful for the authors to discuss alternative notions of regret from the online learning literature, as I think Asymmetric Regret can be thought of as a special case of the $\Phi$-regret introduced in Stolz and Lugosi 2007 and studied in *Online Learning: Beyond Regret* by Rakhlin, Sridharan, and Tewari 2011, where the $\Phi$ functions map a function class allowed to see the entire history to one constrained to seeing the most recent $T^q$ inputs.  

3. The main theorem rests on a fairly unmotivated assumption on the spectrum of a system matrix and there is no theory regarding whether or not this is necessary.

4.  While I am reviewing this paper primarily as a theoretical one, I do wish to mention that I am not entirely convinced by the experiments on the STU networks.  First, the results in Figure 5 appear extremely noisy.  Second, and more importantly, there is no comparison to comparable results with transformers.  My understanding of some recent empirical results in the length generalization literature, such as *What Algorithms can Transformers Learn? A Study in Length Generalization* by Zhou et al 2023, is that induction heads should be relatively easy for transformers to learn due to their ease of representation; why do we expect STUs to improve in this setting?

### Questions
1. Can the authors present some intuition as to the assumption on the spectrum that is required in the main theorem?  The precise union of intervals seems extremely unmotivated to me.  While I understand that it is qualitatively reasonable in the sense that as the amount of data becomes smaller, the assumption becomes stricter, I do not have a lot of intuition beyond that.

2. While I realize that the authors present some empirical evidence suggesting that the main theorem's spectral assumption is necessary, can they provide any theoretical lower bounds for their algorithm?

3. How can the accuracy in Figure 5 be greater than 1?

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
2

### Summary
The paper presents a novel approach to length generalization in sequence prediction using an Asymmetric-Regret metric. This metric measures prediction performance for models constrained to shorter context lengths, compared to a benchmark with access to the full sequence history. The authors apply this metric within spectral filtering for linear dynamical systems (LDS) and introduce a gradient-based learning algorithm that maintains sublinear Asymmetric-Regret bounds, enabling generalization over long sequences even with limited training contexts. 
This work builds on foundational contributions by Hazan and colleagues, who developed algorithms for spectral filtering in LDS under online convex optimization frameworks. The authors extend Hazan’s ideas by focusing specifically on achieving Asymmetric-Regret bounds with shorter context lengths.

### Strengths
1.	The paper extends the Asymmetric-Regret framework by applying it to limited context settings in spectral filtering. This adaptation addresses the relatively unexplored problem of length generalization for sequence prediction with limited context.
2.	Algorithm 1 introduces a modification of spectral filtering using shorter context windows, providing a new approach to minimize regret relative to models using the full sequence.

### Weaknesses
1.	Strong Assumptions:The main result relies on restrictive assumptions about LDS structures and eigenvalue constraints (e.g., eigenvalues must fall within “good” ranges), which may limit the algorithm’s applicability in situations that do not strictly follow LDS dynamics or contain eigenvalues outside these ranges.

2.	Limited Empirical Validation: The empirical scope is narrow, with experiments focused primarily on synthetic LDS data and a single deep learning task. This raises concerns about the method’s practical utility and performance in diverse real-world settings.

3.	Conceptual Novelty and Integration of Existing Ideas: While the application of Asymmetric-Regret bounds to shorter contexts is novel, the overall contribution seems primarily integrative, synthesizing elements from Hazan’s work on spectral filtering, convex optimization, and regret minimization. The empirical and conceptual innovations feel incremental rather than groundbreaking, especially given the limited empirical exploration.

### Questions
1.	Generalizability: Could the authors discuss how their approach might extend to more general settings, especially those where data does not conform strictly to LDS assumptions? 
2.	Handling “Bad” Eigenvalues: Theoretical and empirical results suggest that the approach struggles when eigenvalues fall within certain “bad” ranges. Could the authors elaborate on adjustments to handle such cases?
3.	Comparison with Full-Context Models: In practice, how closely do regret bounds from shorter context lengths compare to those obtained with full sequence contexts? Are the additional comparative metrics that are relevant here? 
4.	Empirical Testing Beyond Synthetic Data: This is needed to provide insights into the approach’s practical feasibility and generalizability.
5.	Alignment with Hazan’s Work: How does the adaptation of the Asymmetric-Regret metric aligns with or diverges from Hazan’s original work? A detailed and systematic discussion is needed to understand the key contributions of this work.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the problem of predicting the outputs of a linear dynamic system using only a truncated history. The paper shows that the regret of a predictor with history length $T^q$ is upper bounded by $\tilde{O}(\sqrt{T})$ compared to the full-length history (i.e., length $T$) experts, provided the data is noiseless and follows some underlying linear dynamic system. This is achieved at the cost of restricting the eigenvalue (depending on $q$) of the leading matrix $A$ of the linear dynamic system.

### Strengths
In my opinion, the primary contribution of the paper is conceptual; it shows that meaningful regret bounds can still be achieved even when the predictor is not exposed to the full history, at least in the context of linear dynamic systems. This may inspire future work to extend this idea to other settings. As the authors point out, this truncated scenario is also inspired by the limited token-length prediction in LLMs (although this is not directly related to the current paper).

### Weaknesses
The proof idea appears to me to be quite simple, essentially involving the application of an online convex optimization predictor on the *truncated* expert. The regret bound follows from the fact that the performance of the optimal truncated expert is close to that of the optimal full-history predictor (using the assumption that the eigenvalues of $A$ are bounded). The final regret bound is essentially a restatement of Hazan et al. (2017b).

As I am not an expert in linear dynamic system theory, I cannot comment on the significance of relating truncated experts to full-history experts in that field. In particular, I am unsure how restrictive it is to constrain the eigenvalues of $A$.

From an online learning perspective, the technical contribution is minimal (both algorithmically and analytically), as the analysis closely follows Hazan et al. (2017b).

### Questions
1. It seems your result holds only in the noiseless setting. What happens if noise is introduced? Does the regret bound of Hazan et al. (2017b) hold in this case as well?

2. What happens if we allow the predictor to compute a "sketch" of the history, rather than a hard truncation?

### Soundness
3

### Presentation
3

### Contribution
2
