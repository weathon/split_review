# Transformer Encoder Satisfiability: Complexity and Impact on Formal Reasoning

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 3, 5, 8

## Abstract
We analyse the complexity of the satisfiability problem (SAT) for transformer encoders (TE), naturally occurring in formal verification or interpretation tasks. We find that SAT is undecidable when considering TE as they are commonly studied in the expressiveness community. Furthermore, we identify practical scenarios where SAT is decidable and establish corresponding complexity bounds. Beyond trivial cases, we find that quantized TE—those restricted by fixed-width arithmetic—lead to the decidability of SAT due to their limited attention capabilities. However, the problem remains difficult, as we establish scenarios where SAT is NEXPTIME-hard and others where it is solvable in NEXPTIME for quantized TE. To complement our complexity results, we place our findings and their implications in the broader context of formal reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proves several hardness results on the satisfiability of encoder-only Transformers. These results demonstrates the hardness of preforming formal verification of satisfiability over Transformers Encoders, which is undecidable for unbounded-length, log-precision Transformer Encoders, NEXPTIME-Hard for bounded-length inputs and bounded precision.

### Strengths
Overall, the theoretical contributions of this work can be impactful as formalizations of impossibility results of general formal verification over Transformers. The theoretical contribution of implementing a tiling system within Transformer Encoders can also be useful for further theoretical work, whereas prior works on expressiveness on Transformer Encoders mostly focused on upper bounds with circuit complexity. As such, I recommend for Acceptance (assuming the authors make appropriate clarifications as mentioned below).

### Weaknesses
The paper tries to make arguments that connects the satisfiability theorems proven in the paper to “formal reasoning” (i.e, model verification and interpretation), which I believe is not sufficiently justified. In the section 3.1 “Satisfiability as a baseline formal reasoning problem” the author makes 2 examples: robustness verification and formal interpretation. However, both examples require the input to satisfy certain properties and decides satisfiability on the set of inputs with the given properties. It is unclear whether the how hardness results still hold when input space is constrained as in the given examples. As such, this connection between the theorems proven in the paper and “formal reasoning” should be accurately characterized.

The naming in the paper can cause much confusion. SAT typically refers to the Boolean Satisfiability problem in computational complexity, and using SAT to also refer to Transformer Encoder Satisfiability can be confusing to many readers, especially the claim that “SAT is undecidable” in the abstract. It is recommended to use a different acronym for the specific problem. Similarly, “Formal Reasoning” also has specific meanings referring to reasoning over formal systems with well-defined inference rules and axioms. The “formal reasoning” in this paper can be directly stated as “verification and interpretation”.

At the current state, the paper’s conclusions are not fundamentally surprising given the recent line on work on the expressiveness of Transformers (although, as mentioned, formalizing such statements and providing a concrete construction is a sufficient contribution). From a practicality perspective, both NP-Hard and NEXPTIME-hard are both infeasible, and it would be more impactful if the work shows interesting classes of Transformers/properties that can be verified in polynomial time.

### Questions
Please address the concerns raised in the Weaknesses section.

### Soundness
3

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
The paper studies the decidability of the emptiness problem of the language recognized by a transformer encoder classifier,  that is, whether there exists a string w in the input domain for which the given transformer will return true. It also studies the complexity of such problem in contexts where it is found to be decidable.

### Strengths
The main interest of the paper is to try to define bounds on the complexity of decidable classes of problems related to languages recognized by transformes.

### Weaknesses
The paper itself is quite a high-level description of a list of results. The necessary definitions, such as the tiling problem, and other key aspects of the proofs are in the appendix or completely missing. The absence of important definitions makes the paper difficult to follow.

Besides, the structure of the paper with a preview of the results does not enhance readability but quite the contrary. It would be much readable if the results were shown, proved and explained once, providing reasonably detailed proofs that put forward the important issues (while the much technical details are put in the appendix).

Pg. 2. L 54-54. I disagree with this comment. Programming languages are Turing Complete, still formal reasoning and verification has been a very active, productive and necessary field of computer science. Nevertheless, it is worth knowing	the boundaries of decidability and complexity to figure out methods to cope with that.  Please comment.

Pg. 2. L 66-69. What do you mean by “formal interpretation”? The term is not common in the field of formal verification and you do not define it here nor provide references to definitions or related work. An example is provided later in Pg. 4, Sec. 3, which reduces to a verification problem. There is missing related work regarding formal methods and tools for extracting automata-based models from different kinds of neural classifiers (including transformers) and language models that should be cited here. Such methods can accomplish verification and generate explanations. Good sources of references for this matter are the Proceedings of the International Conference on Grammatical Inference 2023 and the last two LearnAut workshops. That line of relevant work is not referenced by the cited papers.

Pg. 3. L 169-174. What part of the TC proof of Pérez et al made you believe that languages recognized by the class T_udec could possibly be decidable?

Pg. 4. Could it be possible that softmax rather than hardmax change the decidability result?

Pg. 5. L 251. The 3. Clearly, bounded satisfiability is decidable if T(w) is computable because you can enumerate all words up to length n. The important result here is the complexity bound. Also, the way this theorem is written  here is different from Sec. 5. You should rewrite this.

Pg. 5. L. 265. In what sense fixed-width arithmetic has a similar effect to bounding the input length? Besides, why not considering then T^FIX only?

Pg. 6. L. 302. Why is it the case that T_udec is the weakest class in terms of expressivity? 

Pg. 6. L. 306. The name “octant” tiling problem does not seem to be standard. It is not mentioned as is in the provided reference. Also it is not clear why it is necessary to distinguish between “tiling” problem and “tiling word” problem. The definitions in the appendix do not make this clear. Could you explain it?

Pg. 8. L. 401. It reads “one can reasonably assume the size of a syntactic representation of T to be polynomial on |T|”. It is not clear to me that this assumption is reasonable. Please provide arguments.

Pg. 8. L. 402. The so-called polynomial evaluation property is not discussed in Section 3 nor elsewhere in the paper. Why is it reasonable?

Pg. 8. It seems that the proof sketch of The 3 does not take into account the representation of w. Please comment on this.

Other comments

Pg. 3. L. 138. k should be L since i is a layer, and layers go from 1 to L.

Pg. 3. L. 157. different rational number”s”

### Questions
Pg. 2. L 54-54. I disagree with this comment. Programming languages are Turing Complete, still formal reasoning and verification has been a very active, productive and necessary field of computer science. Nevertheless, it is worth knowing	the boundaries of decidability and complexity to figure out methods to cope with that.  Please comment.

Pg. 2. L 66-69. What do you mean by “formal interpretation”? The term is not common in the field of formal verification and you do not define it here nor provide references to definitions or related work. An example is provided later in Pg. 4, Sec. 3, which reduces to a verification problem. There is missing related work regarding formal methods and tools for extracting automata-based models from different kinds of neural classifiers (including transformers) and language models that should be cited here. Such methods can accomplish verification and generate explanations. Good sources of references for this matter are the Proceedings of the International Conference on Grammatical Inference 2023 and the last two LearnAut workshops. That line of relevant work is not referenced by the cited papers.

Pg. 3. L 169-174. What part of the TC proof of Pérez et al made you believe that languages recognized by the class T_udec could possibly be decidable?

Pg. 4. Could it be possible that softmax rather than hardmax change the decidability result?

Pg. 5. L 251. The 3. Clearly, bounded satisfiability is decidable if T(w) is computable because you can enumerate all words up to length n. The important result here is the complexity bound. Also, the way this theorem is written  here is different from Sec. 5. You should rewrite this.

Pg. 5. L. 265. In what sense fixed-width arithmetic has a similar effect to bounding the input length? Besides, why not considering then T^FIX only?

Pg. 6. L. 302. Why is it the case that T_udec is the weakest class in terms of expressivity? 

Pg. 6. L. 306. The name “octant” tiling problem does not seem to be standard. It is not mentioned as is in the provided reference. Also it is not clear why it is necessary to distinguish between “tiling” problem and “tiling word” problem. The definitions in the appendix do not make this clear. Could you explain it?

Pg. 8. L. 401. It reads “one can reasonably assume the size of a syntactic representation of T to be polynomial on |T|”. It is not clear to me that this assumption is reasonable. Please provide arguments.

Pg. 8. L. 402. The so-called polynomial evaluation property is not discussed in Section 3 nor elsewhere in the paper. Why is it reasonable?

Pg. 8. It seems that the proof sketch of The 3 does not take into account the representation of w. Please comment on this.

Other comments

Pg. 3. L. 138. k should be L since i is a layer, and layers go from 1 to L.

Pg. 3. L. 157. different rational number”s”

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This technical paper tackles the decidability of satisfiability for Transform encoders (TE), namely, does there exists an input such that the output of the TE is a given constant, say 1. This problem is a generic problem which can encode pattern recognition, etc. The results by the authors are as follows:

1) in general, the satisfiability problem is undecidable. The proof is by reduction to a tilling system, or equivalently to halting problem - a correct input of the TE leading to output 1 corresponds one to one to a (correct) halting unfolding of a run of the machine. The encoding requires a number of bits for each neuron computation logarithmic in the size of the input, and also that the embeddings are *not* periodic.

2) If the input is bounded by size n, then the problem is NP-complete(n) (leading to a usual NExptime-complete complexity if n is written in binary), the upper bound being trivial and the lower bound being the same reduction than for undecidability.

3) Alternatively, if the input is unbounded but the number of bits for each neuron computation is bounded by a number of bits part of the input, then the problem is also NEXPTIME-hard using the exact same encoding, although no upper bound, is provided in this case, not even decidability.

4) The most interesting decidability result is that if the number of bits for each neuron computation is bounded and the embedding periodic, with both the period and number of bits are part of the input (in unary), then the problem is decidable in NEXPTIME (but no lower bound is provided).

### Strengths
1. The paper explores the complexity of Transform encoders. Understanding the theoretical complexity of this hot topic is very timely.

2. The proofs seem solid. 2 constructions are non-trivial (one lower bound encoding (1) and one decidability & (upper bound) complexity proof (4), the other being direct application of the first construction).

### Weaknesses
1. The paper could be written in a more reader-friendly way, it is very technical. Statements of the theorems are unnecessarily complicated. The number of Theorems is also inflatted. E.g. theorem 2 should just be a note at the end of theorem 1: "undecidable in general, even when restricted to log-precision transformers." At the end of the day, there are 2 main results in this paper (1 and 4 listed above).

2. (edit: partially improved, but the solution does not fundamentally change the usability landscape, which is in practice somehow still restricted to bounded input) The biggest weakness is that the complexity landscape has a serious gap. The authors need 2 restrictions together to get decidability (see 4.), and the proof of undecidability needs both restriction lifted. So what happens if only one of this restriction? Even more problematic, the authors focus heavily on one of these restrictions (bounded-precision, which is arguably a very reasonable restriction to consider), leaving the other (periodicity, a much stronger restriction) as a technical factor that can be easily overlooked by an inattentive reader (for instance, the notation is using a small '_o'). The proof in appendix C reveals that its actually periodicity that is the main driver for decidability, and fix-precision only seems to be accessory to simplify the proof, and may be useful for the Nexptime upper bound complexity.

### Questions
1. Where is the fix-precision used in the proof of lemma 3? Is it necessary?
 
2. Do you have proof of decidability for fix-precision (*without* periodic embeddings)?

In all cases, you cannot draw Sat[T^fix] on the Nexptime ball (in figure 2), as there is no proof it is *in* Nexptime. (edit: fixed)

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper studies the complexity of deciding whether a transformer accepts a given input sequence. This problem of satisfiability (SAT) is studied on encoder-only transformers. Encoder-decoder transformers are not considered, as they are Turing complete and hence the SAT problem is immediately undecidable. Firstly, the SAT problem is proven to be undecidable for hardmax encoder-only transformers using a reduction to tiling problems, even when the transformer has log precision. Secondly, decidable restrictions are achieved using bounded length sequences or fixed precision in combination with periodic embedding results. However, in these cases, the SAT problem still remains NEXPTIME.

### Strengths
Although the content is very theoretical, the authors take care to first give a general overview of the results (Section 3), after which proof sketches are given (Sections 4 and 5) and more detailed proofs follow in the appendices. This presentation kept the paper relatively digestible, despite the fact I’m not very familiar with this subject matter. From a theoretic viewpoint, I found the results interesting. The practical usefulness seems somewhat limited to me, but as the authors note the presented SAT problem is foundational in relation to safety and verification of model properties and this work provides a useful start in its study.

### Weaknesses
As I am not really familiar with the computational complexity study of neural networks, I do not feel very confident to judge the significance of the findings. However, some of the assumptions seem to limit the practical usefulness of the results.
-  As the authors mention themselves, the distinctions between the considered transformer models fall away when a bounded word length is assumed. Given that transformers almost always have a (fixed) context window, such a bounded length assumption seems quite reasonable to me, and the results for unbounded length seem less relevant.
- The $\mathcal{T}_{udec}$ class for transformers (and its further restrictions) uses hard-attention instead of soft-attention. Previous works have indicated that soft-attention can achieve significantly different results compared to hard-attention (Strobl et al. 2024).
- The decidability results of e.g. Theorem 3 are based on naive enumeration, which is not realistic except for very short word lengths.

### Questions
- Do any of the proven results change if satisfiability is defined as exceeding a given threshold instead of just being equal to 1? This could be a more realistic condition for acceptance.

- Do the authors have an intuition on to what extent their results could generalize to soft-attention?

- It was not clear to me if the definition of SAT on transformers is new, or has been proposed before.

- This perhaps a bit of a broad/vague question, but seeing the many undecidability and hardness results proven in the paper, do the authors think that there is hope for formal verification techniques on transformers? Or should the verification efforts focus on more tractable and less expressive classes of models than the transformer?

*Some small nitpicks*

- Brackets for citations are not used properly. The paper consistently cites transformers Vaswani et al. (2018) instead of transformers (Vaswani et al., 2018).

- The font in Figure 2 is too small for me to be readable without zooming.

### Soundness
3

### Presentation
3

### Contribution
2
