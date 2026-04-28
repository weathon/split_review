# A probablistic automata learning approach for analyzing and sampling constrained LLM

- Decision: Reject
- Avg Score: 4.40
- Scores: 3, 3, 5, 5, 6

## Abstract
We define a congruence that copes with null next-symbol probabilities that arise when the output of a language model is constrained by some means during text generation. We develop an algorithm for efficiently learning the quotient with respect to this congruence and evaluate it on case studies for analyzing statistical properties of LLM.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
# Summary
The paper addresses the problem of language models, where specific symbols during text generation may have a probability of zero. The authors tackle the problem by formalizing the problem in an automata-theoretic setting and defining a congruence relation on sequences that depends on (1) the extension of sequences (as is usual) and (2) the occurrence of symbols with zero probability. Based on the congruence relation, the authors propose an active automata learning called Omit-Zero. They evaluate the runtime of the algorithm in comparison to an existing algorithm called QNT. Finally, they apply the algorithm in case studies where the symbol generation of language models is guided.

### Strengths
+ Systematic analysis of LLMs is a timely topic, and a solid theoretical foundation can benefit the community.
+ The algorithm and the claims seem generally sound.

### Weaknesses
 + The presentation of the paper needs to be significantly improved.
    + There is a lot of notation and terminology, which is not bad per se, but some parts need to be explained better, and it might be possible to skip some parts. For example, the term "quotient" is used already in the second sentence of the abstract, but only on Page 3 (bottom), it becomes clear what a quotient looks like. The definition of the congruence relation, which is central to the paper, is not motivated well enough. It is not clear why the authors chose to define the congruence based on both the extension of sequences and the occurrence of zero-probability symbols, instead of just the extension. This makes the technical development harder to follow.
    + Section 3 can be understood with some knowledge of automata learning, however, I assume that most readers don't immediately know what "sift" means. The relevance of some concepts, like the Hopcroft-Karp algorithm, is unclear. The paper would benefit from a more detailed explanation of how these concepts are used in the context of the proposed algorithm. It seems to me that the paper could benefit from a more stringent focus on the most relevant concept while abstracting away some details.
+ It is unclear how the case studies relate to the main problem considered by the paper. 
    + Case Study 1: Here, we see a difference between different tokenizer settings, but it is unclear what the effect of the 0-probabilities problem would have been. The experiment does not clearly demonstrate the practical relevance of the proposed method in addressing the zero-probability issue. It would be helpful to see a scenario where the zero-probability problem directly impacts the outcome and how the proposed algorithm mitigates it.
    + Case Study 2: This case study examines the fidelity of learned automata, but the problem and its (potential) effect are not mentioned. The connection between the fidelity of the learned automata and the zero-probability problem is not explicitly established. It is unclear why the fidelity of the learned automata is a relevant evaluation metric for the problem being addressed. From the introduction, I would have assumed to see an experiment showing non-termination or some similar effect.

### Questions
1. Would the case study have been possible with QNT?
2. Does Corollary 2.1 hold for all PDFA, or does it require minimality?
3. In the runtime experiment, the probability of a symbol to be 0 is at least 0.9. Is this probability realistic when considering the guiding of an LLM? 
4. Considering the problem of non-termination illustrated in the caption of Fig.1. It seems to me that a simple solution would be to avoid excluding $ using top_r. Am I missing something?

### Soundness
3

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
This submission starts by presenting some background on probabilistic DFAs and describes congruences on these. The congruence of Eq (1) describes strings as equivalent if they agree on the conditional probability of each subsequent letter. The next section presents an algorithm for learning a congruence-minimal DFA based on a previous algorithm from [6]. Finally, the paper ends with a couple of experiments first looking at guiding GPT2 using an automaton, and then comparing sampling between a PDFA and GPT2.

### Strengths
The use of automata in the study of NN-based machine learning is extremely interesting and has led to many new insights and results (e.g. the excellent work of Weiss et al in, inter alia, [13].

### Weaknesses
As a general comment, this paper reads like a rushed and very early draft. I did not see a unifying story/narrative, and both motivation and details are missing

SECTION 2:

Conceptual issue: When going from eq (1) to eq (4), an equivalence relation E is introduced on the simplex \(\Delta(\Sigma_\$)\). Why? There's no motivation, and there are no examples. What are typical examples of equivalence relations on simplices? Whilst (1) is transparent, (4) no longer is. As a consequence, it is hard to understand where the rest of the section is going.

Technical issues: 

a) The definition of \(\mathbf{P}\) is messy and confusing and as a consequence the proof of its existence is incomplete (and perhaps incorrect). With spaces like \(\Sigma^\omega\) you cannot dispense with measure theory. So the first step is to identify the measurable subsets of \(\Sigma^* \cup \Sigma^\omega\). Moreover, since you need to apply Kolmogorov's extension theorem, you in fact need to consider \(\Sigma_\$ ^\omega\). How are the measurable subsets of \(\Sigma^*\) encoded in those of \(\Sigma_\$ ^\omega\)? Next, you need to define your joint probabilities on your cylinder sets. Here you only look at very specific cylinder sets, and this is why you cannot state, let alone prove, the "permutation invariance" property required by Kolmogorov's extension theorem. That it holds is not immediately obvious to me since we're dealing with a family of conditional probabilities over a non-commutative structure (words).But since the final-dimensional distributions aren't even defined it's hard to say.

b) I'm not sure about the proof of 2.1. If we write the definition of the congruence in the better format \(P(uw)P(v)=P(u)P(vw)\) and we assume that \(P(u)=0\), then we could very well have \(P(v)>0\) as long as \(P(uw)=0\) (which seems to hold anyway by the recursive factorisation given on page 2).

c) The normalisation step is missing in the definition of \(\mathsf{samptop}\).

Other issues:
- The notation is sub-optimal. The subscript $ is missing at the beginning of sec 2. Why use semantics brackets [[-]] for equivalence classes? 
- Fig 1: I don't see what is "troublesome" about \(\mathcal{B}\), it does exactly what it's supposed to be able to do if you allow non-termination.
- Either say that all proofs are in the appendix once, or state them all (there's space).
- You don't define \(reach(Q)\)

SECTION 3:

The reader needs some context. Why are you developing this algorithm? What is the learner? What is the teacher? What are the allowed "learning actions" (e.g. membership queries? equivalence queries? any other kind of queries?)? What is the general description of the algorithm of [6]? The reader shouldn't have to read [6] to understand what \(\mathsf{sift}\) is. As it stands Sec 3 cannot realistically be understood by the average reader.

The labelling of the x-axis of the LHS graph in Fig 3 is unfortunate.

SECTION 4: 

This section suffers from the same problems as Sec 3. What exactly are you trying to show and why? In particular, using PDFAs seems completely overkill for the kind of simple experiments carried out in case study 1 and Table 2. 
For case study 2, the guiding automaton allows every digit at ever stage, so it's not doing very much guiding. What precision of floating-point are you using? And how many digits are sampled? (the precision just gives an upper bound) The reader will not know what Outlines [14] means, this must be explained. As it stands the results for this case study mean noting to me.

- \(\kappa\) has not been defined anywhere
- Figs 7(a) and 7(b) are not labelled in this way.

### Questions
1. Should I read \\(\mathcal{L}(\sigma_1\ldots\sigma_n)\\) as \\(P[\sigma_n\mid \sigma_1\ldots\sigma_{n-1}]\\)? I don't understand if the basic model is Markovian (as the DFA model suggests) or not (as the definitions on p2 and in Prop F.1 suggest).

2. How would you define an arbitrary finite-dimensional marginal of \\(\mathbf{P}\\)?

3. What is the motivation for the \\(E\\) introduced before (3)? Can you give an example?

### Soundness
1

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
The paper introduces a new congruence on words w.r.t. a given a language model $\mathcal{L}:\Sigma^*\to\Delta(\Sigma)$, which can be used to learn surrogate probabilistic deterministic finite automata using a Myhill-Nerode type theorem. It builds heavily on ideas introduced in [6], where a similar congruence and a corresponding tree-based learning algorithm have been developed, but addresses the problem of null probabilities, which can occur if the model output is externally constrained, e.g. by an automaton.

More precisely, the congruence is defined relative to an equivalence relation $E$ on the probability simplex $\Delta(\Sigma)$
$$
u\equiv_E v :\Leftrightarrow \mathbb{1}(u) = \mathbb{1}(v) \land \forall w\in\Sigma^*:  \mathbb{1}(uw) = \mathbb{1}(vw) =1 \to \mathcal{L}(uw) =_E \mathcal{L}(vw), 
$$
where $\mathbb{1}(u)$ indicates whether the string $u$ has positive probability under the model.
As mentioned earlier, the main difference to the work done in [6] is the explicit handling of null probabilities. The definition ensures that $0$ probability transitions do not need to be explored while still maintaining a meaningful congruence. As a consequence, the QNT algorithm from [6] can be adopted to avoid $0$-probability transitions as much as possible. This is useful to keep the number of queries to the LLM as low as possible during learning.

The developed algorithm is compared against to other variants of QNT and shows significantly reduced learning times. Finally, the authors conduct experiments to exemplify the use of their algorithm. First, they investigate the influence of the tokenizer on the next token probabilities by learning surrogate automata under the top-k equivalence on $\Delta(\Sigma)$. Second, they restrict the output of a GPT-2 model numbers between 0 and 1 and learn a surrogate automata for the constraint output. They compare the output distribution of the LLM with the one from the automata and demonstrate that the automaton is able to closely approximate the original distribution.

I think the paper presents a meaningful improvement of the approach presented in [6], but I would like to criticize that the paper reads too much like an addendum to [6] in many places. This is especially true for Section 3. Without reading [6], it would not have been possible for me to comprehend this section. Another weakness is that the example use cases are arguably toy experiments. Finally, I have to point out that the submission is not according to the guidelines (missing line numbers). Because of the mentioned weaknesses, I can only give a weak recommendation for acceptance.

[6] F. Mayr, S. Yovine, M. Carrasco, F. Pan, and F. Vilensky. A congruence-based approach to active automata
learning from neural language models. In PMLR, volume 217, pages 250–264, 2023.

### Strengths
- Reduce number of LLM queries during learning by omitting 0-probability transitions

### Weaknesses
The paper introduces a meaningful improvement to the approach in [6], but it reads too much like an addendum. Section 3, in particular, is very difficult to follow without prior knowledge of [6]. The definitions of the congruence and the quotient construction are not self-contained, requiring the reader to constantly refer back to the original paper. For example, the notation and concepts related to the tree structure and the sift operation are not adequately explained, making it hard to grasp the technical details of the algorithm. The paper would benefit from a more thorough explanation of the core concepts, even if it means some redundancy with [6].

Another weakness is that the example use cases, while demonstrating the algorithm's functionality, are not very compelling. The experiments on the tokenizer's influence and the constrained GPT-2 output are somewhat toy examples and do not fully showcase the potential of the proposed approach in more complex, real-world scenarios. The paper lacks a discussion of the limitations of the approach and its applicability to more challenging problems. Finally, the submission is not according to the guidelines (missing line numbers).

### Questions
- Page 3 (Quotients): $\bar{\pi}([|q|]) = [\pi(q)]$ (?)
- Page 3 (Quotients): $\bar{\tau}([|q|], \sigma) = [|\tau(q, \sigma)|]$ (?)
- Page 4: What is sift? The paper would generally benefit from relying less on [6] as a reference.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors consider the problem of learning a probabilistic deterministic finite automaton (PDFA) by interacting with a constrained sequence model with a special sampling scheme, such as a large language model constrained with a given property and sampled with a top-k selection scheme. The main challenge to learn a PDFA in such a setting is that the distribution over strings by the constrained LLM with a particular sampling scheme may assign non-zero probabilities to infinite sequences; in order to even describe an ideal PDFA to learn, one has to come up with an appropriate notion of equivalence on strings that are induced by the constraint and the sampling scheme. In the paper, the authors indeed propose such a notion in a clean general way, define the induced quotienting operators on language models (formalised as maps from finite strings to probability distributions over characters and EOS), and PDFAs, and analyse the properties of these operators. Based on this formal development, they propose an algorithm for learning a PDFA from interactions with a constrained language model with a special sampling scheme formalised by an equivalence relation on distributions over characters and EOS. Their algorithm is applied to simple language models which are based on randomly generated DFAs, and also to the constrained GPT-2 model with a special sampling scheme. The results of these experiments show the promise of the algorithm in the paper.

### Strengths
1. This paper describes the issue of a constrained language model assigning non-zero probability to infinite sequences. My understanding is that this is not one of the commonly discussed issues on language models (and their distillations which seem to be related to the work in the paper). Asking an unusual question, I think, is good for the research area.

2. The formal development in the paper is thorough and rigorous. Here I mean Section 2 of the paper, which I liked and learnt a lot from. But as I will mention in the weakness box below, I found Section 3 of the paper confusing and hard to follow. 

3. The authors' learning algorithm is derived from a solid theory.

### Weaknesses
1. My main reservation is that Section 3 was very difficult to follow. It is the part that describes the main contribution of the paper, namely, the algorithm for learning a PDFA from the interactions with a teacher model (formalised via the EQ query). But the section assumes the familiarity with QNT, and does not describe what sift, build, EQ, update, and InitializeHypothesis do, and how their learning algorithm works . Also, I couldn't understand what path means (which is used in (8)). Illustrating the run of the algorithm with a concrete example may be helpful.

2. The next point is not really a weakness, but it partly explains why I am not a strong supporter of the paper. While I read the paper, one question kept popping up to me: what can one do if she or he has a quotiented PDFA that models a given constrained language model with a special sampling scheme (such as top-k)? The abstract says that such a quotiented PDFA can be used to analyse the statistical properties of the language model. Elaborating on this and giving some concrete examples would make the paper more appealing to someone like me.

### Questions
If the authors can respond to the two points that I mentioned in the weakness box, that would be helpful for me to understand the paper more. But they don't have to do so.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Many automata theoretic techniques have been introduced to analyse neural sequence-processing recognizers  by composing them with automata theoretic formalisms with the purpose of verifying properties on-the-fly. In this work the authors propose an approach to combine automata theoretic formalisms with language generators, such as neural language models, in order to guide the generation process or constrain the text generation with some common sampling strategies. In this context, the occurrence of symbols that have zero probability of appearing is a problem. For example, the generation may not terminate, or the model may not define a probability distribution over finite strings. 

In this paper, the authors define a notion of  Myhill-Nerode-like congruence over strings which takes into account the occurrence of zero-probabilities, that provides an underlying formal basis for learning of probabilistic deterministic finite automata (PDFA) from neural language models constrained both by by automata and sampling strategies. Another contribution is that they propose a new algorithm for learning the quotient with respect to this congruence. The authors provide experimental evidence that the new approach has some advantages with respect to existing approaches. Finally, the authors providea framework to analyze statistical properties of LLMs.

### Strengths
In my opinion, the paper is quite interesting. There is currently an impending need to understand the behavior of LLMs when their operation is controlled by external such as automata and more general formalisms. In this work the authors provide a contribution in this direction.

### Weaknesses
The paper as a whole is a whole is a fair contribution of the topic of LLMs. Nevertheless, the results follow by extending and adapting known constructions within automata theory. In this sense, I did not find the results of the paper particularly surprising.

### Questions
I do not have questions.

### Soundness
3

### Presentation
3

### Contribution
3
