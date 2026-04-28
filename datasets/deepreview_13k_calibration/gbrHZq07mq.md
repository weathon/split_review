# Logical Languages Accepted by Transformer Encoders with Hard Attention

- Decision: Accept
- Avg Score: 5.60
- Scores: 6, 3, 3, 8, 8

## Abstract
We contribute to the study of formal languages that can be recognized by transformer encoders. We focus on two self-attention mechanisms: (1) UHAT (Unique Hard Attention Transformers) and (2) AHAT (Average Hard Attention Transformers). UHAT encoders are known to  recognize only languages inside the circuit complexity class ${\sf AC}^0$, i.e., accepted by a family of poly-sized and depth-bounded boolean circuits with unbounded fan-ins. On the other hand, AHAT encoders can recognize languages outside ${\sf AC}^0$), but their expressive power still lies within the bigger circuit complexity class ${\sf TC}^0$, i.e., ${\sf AC}^0$-circuits extended by majority gates.
We first show a negative result that there is an  ${\sf AC}^0$-language that cannot be recognized by an UHAT encoder. On the positive side, we show that UHAT encoders can recognize a rich fragment of ${\sf AC}^0$-languages, namely, all languages definable in first-order logic with arbitrary unary numerical predicates. This logic, includes, for example, all regular languages from  ${\sf AC}^0$. We then show that AHAT encoders can recognize all languages of our logic even when we enrich it with counting terms. We apply these results to derive new results on the expressive power of UHAT and AHAT up to permutation of letters (a.k.a. Parikh images).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Review
======

As a non-IA specialist but a circuit-complexity and automata specialist,
I found those connection amusing but slightly artificial.
I will not express myself on the pertinence of analizing the expressivity
of those models from IA-perspective but provides a bit of insight about
the automata/circuit complexity side.

First I found some claim dubious:

In a footnote you claim that only rational numbers where used in Hao (2022)
but generalize it real numbers.  It is known in complexity theory  that going from rational to real number is always complicated. Even
calculability theory can become weird when considering real numbers.

While it is rather clear that computation performed by UHAT can be computed
in AC0 when restricted to rational numbers, it is much less clear when going
within rational numbers. If it holds, it by the sake of some continuity and
approximation by real numbers arguments, but it deserves some details...
I believe it should be explained.

Because I don't really get that, I have assumed that the remaining where
done on rational numbers;

About the question about "what fragment of AC0, UHAT can belongs to", since it
contains all regular languages in AC0, it is improbable that you can find
a sound answer for that since it is already wide open for regular languages.
Indeed:
- regular language are complete for each level of the depth hierarchy AC0, 
- regular language are in quasilinear AC0 and proving that they are linear AC0
is a long standing open problems (see the survey of Koucky on the topic).

About Proposition 1. I believe a much simpler argument can be used using
a simple padding argument: 

>AC^0 recognized all languages up to exponential padding. 
>That is, Pad(L) = { u #^{2^|u|} \mid u in L } is always in AC^0 whatever is L. 
>Your UHAT shouldn't be able to capture all Pad(L) as it only can remember a small
>piece of information and convolute it. Basic information theory/pigeon hole might
>help to conclude without a hammer of sensitivy of circuits within AC0.

About proposition 5: I don't really understand why the Parikh
closure/permutation closure of languages is meaningful here. Sounds like an
arbitrary property to me.


Logic with counting operators has been introduced in the past (Majority logic)
and a study of its expressivity with respect to circuit classes.
See for instance (https://link.springer.com/chapter/10.1007/978-3-642-02737-6_7)
Is there a connection?

### Strengths
The paper contribute to a fun connection between formal language theory in order to analyze the expressivity of transformers. This line of research sounds more like research performed in TCS than in IA tracks but since it is apply to IA-defined model it makes some sense. Understanding the expressivity of those model might be enlightening to people actually playing with them.

### Weaknesses
First I found some claim dubious:

In a footnote you claim that only rational numbers where used in Hao (2022)
but generalize it real numbers.  It is known in complexity theory  that going from rational to real number is always complicated. Even
calculability theory can become weird when considering real numbers.

While it is rather clear that computation performed by UHAT can be computed
in AC0 when restricted to rational numbers, it is much less clear when going
within rational numbers. If it holds, it by the sake of some continuity and
approximation by real numbers arguments, but it deserves some details...
I believe it should be explained.

Because I don't really get that, I have assumed that the remaining where
done on rational numbers;

About the question about "what fragment of AC0, UHAT can belongs to", since it
contains all regular languages in AC0, it is improbable that you can find
a sound answer for that since it is already wide open for regular languages.
Indeed:
- regular language are complete for each level of the depth hierarchy AC0, 
- regular language are in quasilinear AC0 and proving that they are linear AC0
is a long standing open problems (see the survey of Koucky on the topic).

About Proposition 1. I believe a much simpler argument can be used using
a simple padding argument: 

>AC^0 recognized all languages up to exponential padding. 
>That is, Pad(L) = { u #^{2^|u|} \mid u in L } is always in AC^0 whatever is L. 
>Your UHAT shouldn't be able to capture all Pad(L) as it only can remember a small
>piece of information and convolute it. Basic information theory/pigeon hole might
>help to conclude without a hammer of sensitivy of circuits within AC0.

About proposition 5: I don't really understand why the Parikh
closure/permutation closure of languages is meaningful here. Sounds like an
arbitrary property to me.

### Questions
Comments 
========
- The last sentence of the second paragraph of section 2.2 makes no sense.
f is a function from Sig -> R^d, T: Sig^+ -> R et the last sentence
says that T get an input sequence that type as a sequence of vectors of R"e.
The value of T(w) = (t, v0) only depending of t and v0 which is plain weird
as it gives the impression it depends of a constant (t) and v0 which is f(a_0) + p(0, n).
The whole paragraph is thus buggy.

- You can have some feelings on what is going on with logic extended with monadic
predicates through this paper.

https://dl.acm.org/doi/10.1145/3091124

- About your open question: 
Additionally, does there exist a language in the circuit complexity class TC0, the
extension of AC0 with majority gates, that cannot be recognized by AHATs

I would go for Dyck language. Sounds hard for a AHATs.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates whether circuit language can be accepted by existing transformer encoders with hard attention. Specifically, this work concludes that UHATs cannot accept all languages in $AC^0$, but they can still accept all languages in a ’monadic’ version. Besides, 
this work finds out that AHATs, other transformer encoders, can express any language definable in a powerful counting logic. Moreover, this work provides sufficient theoretical justifications to support their findings and conclusions.

### Strengths
1. The study about whether circuit language can be accepted by existing transformer encoders is interesting and impressive. 
2. The paper offers comprehensive theoretical justification to demonstrate and validate their findings.

### Weaknesses
1. The structure of this paper is very messy, which is very hard to follow. Let me take the Section Introduction as an instance:

1.a In Section 1 Introduction, the paper claims that "the expressive power of transformer encoders
has not been fully elucidated to date.". I am curious about that. What do you mean they are not fully elucidated? Specifically, what limitations or open questions exist regarding the expressive power of different transformer architectures with hard attention, and how does this work aim to address these gaps? The introduction lacks a clear articulation of the specific challenges in characterizing the expressive power of these models, making it difficult to understand the motivation for the study.

1.b I am very confused about the challenges of studying the circuit language. I could not find any information to discuss the existing challenges and related works, which makes it hard to understand the motivation for this work. The paper should explicitly state why analyzing circuit languages is relevant to understanding transformer expressivity. What are the known limitations of existing approaches in relating circuit complexity to transformer capabilities, and how does this work overcome them? The connection between circuit complexity classes (like AC0 and TC0) and transformer encoders needs to be clearly defined and motivated.

1.c What are your contributions to this work? I could not find any conclusions about contributions after reading this section, or even the whole manuscript. The introduction fails to clearly state the specific contributions of this work. What are the novel results or techniques introduced, and how do they advance the understanding of transformer expressivity? The paper should highlight the significance of these contributions in the context of existing research.


2. The paper has a very weak introduction to related works, making this work hard to understand and compare. The related work section should provide a comprehensive overview of the existing literature on the expressivity of transformer encoders, specifically focusing on works that connect transformer architectures to circuit complexity classes. The paper needs to discuss the limitations of existing approaches and clearly position this work in the context of the current research landscape.

3. I would suggest that an illustration figure be provided to clearly show the main idea of this work. A visual representation of the key concepts and results would greatly improve the clarity and accessibility of the paper. This figure should illustrate the relationship between the different transformer architectures, the circuit complexity classes, and the specific languages considered in the paper.

### Questions
Please refer to the weakness of the questions that I proposed.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the expressiveness of Transformer encoders by establishing their relation with a class of formal languages called circuits. Based on prior work, the main theoretical claims of the paper are:

Previous works have demonstrated that UHAT transformers (similar to Transformers with hard attention) cannot recognize languages beyond AC^0 (informally: circuits of polynomial size and constant depth). This paper further finds an example problem class within AC^0 that cannot be recognized by UHAT, which demonstrates that AC^0 is not a “lower bound” of UHAT.

The paper further establishes a class of problems that can be recognized by UHAT.

Results are then extended to AHAT (Transformers with averaged head attention).

### Strengths
Justifying the expressiveness of Transformers through the length of formal language is a very important topic and could lead to better understanding of the working mechanisms of Transformers. This paper strengthens prior theoretical results and better bounds the expressivness of UHAT and AHAT.

### Weaknesses
Although the theoretical results themselves sounds interesting, I found some definitions and assumptions are not approprately stated, which potentially leads to incorrect results. While it is possible that the theoretical results still hold after fixing all the problems, I think the paper needs a major revision to ensure its validity.

Missing important restrictions when defining the transformer model. 

- Precision of the number processed by the transformer. The paper does not include any restriction on the precision of the numbers processed by the transformer. This could make the model unrealistically expressive as discussed in many related work (e.g., proving Turing completeness of RNNs require relaxations on the numerical precision). In related works, a realistic assumption could be log-precision transformers, i.e., the number of floating/fixed-point bits scale logarithmically with the sequence length.

- No assumptions have been made about the number of transformer layers. Prior work usually assume constant depth or logarithm depth (w.r.t. sequence length). Related to this assumption, it seems that the proof of Proposition 2 constructs a Transformer whose number of layers depends on the form of input LTL. This makes it particularly important to make the correct assumption.

- Structure of the model. The model does not include residual connections and only uses single-head attention. Also the ReLU layer only applies ReLU to a single element of the input vector. Although these might be able to adapt in the proof, it would still be nice to make these assumptions as practical as possible.

Many related works are missing. The paper states that “there has been very little research on identifying logical languages that can be accepted by transformers”. However, with a quick google scholar search, I found the following highly-related papers not cited in the paper. It would be nice to discuss the relation of this paper’s results with these prior works.

[1] Merrill, William, Ashish Sabharwal, and Noah A. Smith. "Saturated transformers are constant-depth threshold circuits." Transactions of the Association for Computational Linguistics 10 (2022): 843-856.

[2] Merrill, William, and Ashish Sabharwal. "The parallelism tradeoff: Limitations of log-precision transformers." Transactions of the Association for Computational Linguistics 11 (2023): 531-545.

[3] Strobl, Lena. "Average-Hard Attention Transformers are Constant-Depth Uniform Threshold Circuits." arXiv preprint arXiv:2308.03212 (2023).

### Questions
Some important assumptions seem to be missing.

It would be nice to discuss the relation between this paper and the missed related work mentioned in the weaknesses section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The papers is a contribution to the exciting and challenging domain of characterizing expressivity of transformers. The authors focus on the  Unique Hard Attention Transformers (UHAT). Previous results have shown that $UHAT \subseteq AC^{0}$, where $AC^{0}$ is the circuit complexity class of circuits with constant depth, with unlimited fan-in  $AND$, and $OR$ gates. The author's first result is to show that  $UHAT \subset AC^{0}$. The key contribution of the paper is that First Order Logic on words with unary numerical predicates (i.e. unary boolean functions on positions of the symbols in a word, and the length of the word) is readable by UHAT. They denote this fragment with FO(Mon), the proof strategy used by authors relies on a classic result in logic known as the Kamp's theorem, which says that FO(Mon) is equivalent to another type of logic, known as the Linear Temporal Logic (Mon) i.e. the extension of LTL with unary numerical predicates. The authors then design vector encodings and positional encodings that allow evaluation of any LTL (Mon) formula using a UHAT. Finally, they show the applications of their results by comparing them to other types of formal languages.

### Strengths
Formal properties of transformers are not very well-understood, and analyzing them w.r.t. the formal languages they accept is a very exciting and challenging direction. The author's provide significant contributions in this direction, and the paper contributes many new results and ideas that can contribute to theoretical investigation of transformers. Writing is quite clear, the proof though hard, seems to consist of clear arguments (I mention my confusions in the questions).

### Weaknesses
The proof on Page 6 and Page 7 could be further clarified. Although, the structural induction arguments are clear, but I am not sure how this is consistent with the meaning of accepting a word as part of the language --- which authors define earlier (See questions)

- In my understanding, in section 2.2 paragraph 2, it is unclear to me why you set $T(\bar{w})$ to $\langle \mathbf{t},\mathbf{v}_{0}\rangle$. 
- [Minor Comment] Page 6, "reverses the third coordinate" is not a very precise statement. 
- When is the notion of $T(\bar{w}) > 0$ (as introduced in section 2.2), used as the criterion in proof on page 6 and page 7. From this proof, I just see that you can perform LTL operations on input strings, but I am not sure how this shows that a string in the language will never be mapped to a string outside the language?
- Does Kamp's theorem give any bounds on the length of equivalent FO(Mon) equivalent formula in LTL(Mon)?

### Questions
- In my understanding, in section 2.2 paragraph 2, it is unclear to me why you set $T(\bar{w})$ to $\langle \mathbf{t},\mathbf{v}_{0}\rangle$. 
- [Minor Comment] Page 6, "reverses the third coordinate" is not a very precise statement. 
- When is the notion of $T(\bar{w}) > 0$ (as introduced in section 2.2), used as the criterion in proof on page 6 and page 7. From this proof, I just see that you can perform LTL operations on input strings, but I am not sure how this shows that a string in the language will never be mapped to a string outside the language?
- Does Kamp's theorem give any bounds on the length of equivalent FO(Mon) equivalent formula in LTL(Mon)?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper theoretically analyses the formal languages that transformer encoders can recognize. 
The paper analyses two classes of transformers depending on the attention mechanism. The first class is 
unique hard attention transformers (UHAT), and the second class is average hard attention transformers (AHAT). 
It is known that UHAT encoders can only recognize languages inside the circuit complexity class $AC^0$. AHAT
can recognize languages outside $AC^0$, but its expressive power still lies in the circuit complexity class $TC^0$.

This paper gives new theoretical results on the topic. The main findings of the paper are:
- There is a language in $AC^0$ that UHAT cannot recognize.
- UHAT can recognize all languages definable in first-order logic with arbitrary unary numerical predicates. The class includes all regular languages in $AC^0$.
- AHAT can recognize all languages definable by LTL(C, +), which is an extension of the logical language acceptable by UHAT with counting terms.

### Strengths
**Important topic, impressive results:**
 Since the transformer is one of the most important neural architectures, understanding its expressiveness in a formal way seems an important topic. This paper brings progress on this topic by relating the expressive power of transformers with logical languages.
This connection results in identifying some important language classes that can be acceptable by UHAT, e.g.,  all regular languages in $AC^0$.

**A clearly written paper:** The paper is very clearly written. I feel no difficulty in reading the paper. 
The background needed to understand the contribution is concisely explained in the paper. 
Proofs of important theorems are shown in the main body of the paper, and they are easy to follow.

**New approaches for proofs.**
The paper uses the relationship between first-order logic and linear-time logic to prove the main results. This technique seems not
used in the previous papers analyzing the expressive powers of transformer encoders.

### Weaknesses
Currently, I have no clear reason to reject the paper.


On p.6, the paper says, "Observe that $(\bar{w}, i) \models \phi U \psi $ if and only if $(\bar{w}, j_i) \models \psi$". I wonder what happens if there exists $i \leq j^\prime < j_i$ such that $(\bar{w}, j^\prime) \models \psi$"? Following the definition on page 5, I think $(\bar{w}, i) \models \phi U \psi$ holds if there exists such $j^\prime$.


**Minor comments:**
- **Abstract:** outside AC^0) -> AC^0 ?
- **page2, before related work:** it have been shown before that parity can be accepted by an AHAT -> it has not been shown before that parity can be accepted by an AHAT?
- **p.5, first paragraph:** at at least 2n/3 -> at least 2n/3
- **Appendix, proof of lemma1:** max{0, x_i + i - (n+1)} -> max{0, x_i + 1 - (n-1)}?

### Questions
On p.6, the paper says, "Observe that $(\bar{w}, i) \models \phi U \psi $ if and only if $(\bar{w}, j_i) \models \psi$." I wonder what happens if there exists $i \leq j^\prime < j_i$ such that $(\bar{w}, j^\prime) \models \psi$"? Following the definition on page 5, I think $(\bar{w}, i) \models \phi U \psi$ holds if there exists such $j^\prime$.


**Minor comments:**
- **Abstract:** outside AC^0) -> AC^0 ?
- **page2, before related work:** it have been shown before that parity can be accepted by an AHAT -> it has not been shown before that parity can be accepted by an AHAT?
- **p.5, first paragraph:** at at least 2n/3 -> at least 2n/3
- **Appendix, proof of lemma1:** max{0, x_i + i - (n+1)} -> max{0, x_i + 1 - (n-1)}?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
