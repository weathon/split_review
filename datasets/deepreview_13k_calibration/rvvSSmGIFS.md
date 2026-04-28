# From Probability to Counterfactuals: the Increasing Complexity of Satisfiability in Pearl's Causal Hierarchy

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 3, 5, 8

## Abstract
The framework of Pearl's Causal Hierarchy (PCH) formalizes three types of reasoning: probabilistic (i.e. purely observational), interventional, and counterfactual, that reflect the progressive sophistication of human thought regarding causation. We investigate the computational complexity aspects of reasoning in this framework focusing mainly on satisfiability problems expressed in probabilistic and causal languages across the PCH. That is, given a system of formulas in the standard probabilistic and causal languages, does there exist a model satisfying the formulas?  

Our main contribution is to prove the exact computational complexities showing that languages allowing addition and marginalization (via the summation operator) yield NP^{PP}-, PSPACE-, and NEXP-complete satisfiability problems, depending on the level of the PCH. These are the first results to demonstrate a strictly increasing complexity across the PCH: from probabilistic to causal and counterfactual reasoning. On the other hand, in the case of full languages, i.e.~allowing addition, marginalization, and multiplication, we show that the satisfiability for the counterfactual level remains the same as for the probabilistic and causal levels, solving an open problem in the field.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the computational complexity of the satisfiability problems of queries under different causal layers. In particular, it considers queries that may involve marginalizations ($\sum$) and proves that the sat problems with basic and linear terms under L1, L2, L3 layers belong to the complexity classes of $NP^{PP}$, PSPACE, and NEXP. Moreover, it completes the open problem in Van der Zander et al. to show that the sat problem with polynomial term under L3 also belongs to succ-$\exists R$.

### Strengths
- I checked the proofs and most of them make sense to me. The proofs are also quite rigorous in my opinion.
- The paper is succinct and clearly structured. 
- The results are novel and are important contributions to the complexity of casual satisfiability problems.

### Weaknesses
I think the main challenge is for the readers to process the complexity results.

Here are some suggestions:
1. I think providing more background on the complexity classes in the preliminaries section can be very helpful. Currently the paper points to [Arora & Barak 2009] textbook for more background about the complexity classes. If the page limit permits, it's better to summarize the definitions for each complexity class considered in this paper along with some complete problems in each class. This should make the paper more self-contained.
2. A lot of contents in Appendix C should be moved to Section 2.1. For example, I got lost in the definitions of base, lin, and poly, etc.. Also, please provide some concrete examples so that we know immediately their differences.
3. I think it is worth stressing that the satisfiability problem does not assume anything about SCMs, nor does the causal structure. In the classical work on the complexity of probabilistic inference, it is often assumed that both the structure and parameterizations are known (Remark 5 in the paper). In causal effect identification, the causal structure (graph) is often assumed to be known.

### Questions
1. Are there any (potential) applications of the satisfiability problems mentioned in this work? For example, do they have any implications in causal identifiability or causal discovery (structure learning)? I can see the applications of the validity problems but not sure about the satisfiability problems.
2. Why/when do queries with marginalization become important? How does this relate to existing works on marginalizing (forgetting) variables from causal models?
3. In Appendix A.2 proof of Lemma 14: "A small model property follows that there are only polynomial many, rational probabilities $p_u$" I don’t know what "small model property" is.

Minor typos:
- Line 816: "the second sums" -> "the second sum"
- Line 863: "$\frac{P(\delta)}{P(\delta')}$" -> "$\frac{P(\delta)}{P(\delta, \delta')}$", maybe?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies the complexity issues of the satisfiability and validity problems of formulas and shows an increasing complexity within the framework of Pearl’s Causal Hierarchy of reasoning: observational, interventional and counterfactual.

### Strengths
(1)The paper studies an important theoretical problem for causal reasoning and answers some open problems in this field. 
(2)The paper provides a good motivation and detailed literature.

### Weaknesses
(1)The paper is very technical, condensed and very hard to understand. Hence it is difficult to check the mathematical soundness and evaluate the contributions. But the mathematical proofs turns out to more important than anything else including originality and insights in this paper. The main text consists of a list of theoretical results. The topic is also very limited. Since the paper is mainly about the pure complexity results, probably it is more appropriate as a journal submission or a pure theory conference.   
(2)Some important results in the paper are related to some uncommon complexity classes like succ-ExistentialR-completeness. The paper fails to provide a clear explanation of this class and some motivation of the relationship. 
(3)There is no a concrete example which demonstrates the increasing complexity results. Such an example would help understand the motivation behind the complexity results for different levels of languages.
(4)The introduction in Section 2.1 of Pearl’s PCH is very messy. It would take some hard time to understand the main components and the structure of the hierarchy.  It would be better to illustrate the graph structures of SCMs and give some examples to illustrate the increasing structures.

### Questions
(1)There are several operations in the structure: sum, marginalization, conditioning. What are their roles in the increasing complexities of the hierarchy?
(1)Could you give nontrivial examples to demonstrate different levels of reasoning and to illustrate the corresponding increasing complexities?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies the complexity of the satisfiability problem of various logics for describing properties of structural causal models. The logics incorporate probability comparisons of statements including interventional counterfactuals. The authors give a very rigorous study on the complexity of the satisfiability problem of fragments of the logics they consider.

### Strengths
The paper is very rigorous, and the results are surely interesting for the community of researcher working on logics for causal reasoning.

### Weaknesses
While the call for papers mentions causal reasoning as one of it's topics knowing, I do not think that a paper whose main contributions are pure complexity results for logics for causal reasoning is suitable for ICLR. Though the precise complexity results obtained might have some impact on the algorithmic aspects of causal reasoning. The paper is an almost pure logic paper studying computational complexity landscape of the logic they consider and as such is a valuable contribution that should be carefully reviewed and published in a more suitable venue. I would urge the authors to resubmit the paper to a venue that can better appreciate the results There are numerous conferences of this kind, including A* conferences such as LICS and KR, but also JELIA, CSL, and many other.

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the complexity of satisfiability in three increasingly complex probabilistic frameworks: purely probabilistic, interventional, and counterfactional. They build on previous work which does not allow for marginalisation, and the authors add results that allow for marginalisation.
Their findings are interesting: for each of the three frameworks, they find to which complexity class it belongs, and interestingly the three classes differ (under widely accepted assumptions).
The authors motive their approach well, and cite the relevant literature, at least so far as I can see. The paper gives proofs for all the claimes in an appendix, so the findings are well supported.
This paper adds to the field of causality in probability theory, which is becoming increasingly more relevant, with new results that have the potential to influence further studies in this field.

### Strengths
In my opinion, this paper studies a very relevant question, which naturally arise. The current interest in causality in probability theory makes this paper even more relevant. The results obtained are important on its own right, and may well influence further research.

This paper is well written. The authors took great care in explaining the concepts, and generally succeeded with this (but not everywhere in their paper – see my "questions" section).

One particular thing I appreciated, was the use of 'proof ideas'. In my opinion, this is great to convey the idea, at the same time reducing the risk that the reader loses themselves in details. This seems a nice way for conferences, to my taste.

In all, I am very positive about this paper. I identify later a small number of points where minor improvements are possible. Note that this field is not my expertise, so while I am rather confident that this is a good paper, I am open to arguments against this.

### Weaknesses
In general, I am positive about this paper, and I only identify a small number of weaknesses.

While the authors generally motivate their approach, and introduce the necessary concepts, well, at some points there is improvement possible. 
- For instance, in Table 1 the authors should make more clear that the languages L1, L2 and L3 refer to their introduction on the next page in Section 2.1. The authors do not refer there to L1, L2, and L3, which makes it more harder to make this link.
- An instance where the motivation could be improved, is Section 3, the sentences following that of Equation (3). There, the authors remark that adding marginalisation to a language does not change the expressivenes of it. It comes to wonder, then, why the authors are particularly interested in the questions they answer: if adding marginalisation does not change the expressivenes, why is it important to add this? The authors expand a bit on this in the Introduction, but I would rephrase the sentence here, or expand on it, in order to make the paper feel better motivated.
Also, how do we know that adding marginalisation to a language does not change the expressivenes of it? It may be a well known fact, but I would add a reference.

I end this section with a small list of small remarks and typos:
- Abstract, last sentence: Please be more specific about which open problem in which field. Ideally, give a reference that states that the problem you describe is open.
- Page 2, line 065: add a space between "see, e.g.," and "(Pearl, 1988;".
- Page 6, line 314:  I would write that the sum "ranges" over all values, instead of "sums" over it.

### Questions
Here are three questions that would increase the readibility in my opinion:
1. Page 4, line 182: The basic term P( [ X_1=x_1] X_2=x_2 ) does not belong to T_1^base, if I understand it correctly. The way it's written now, seems to suggest that it does. Please clarify this.
2. Page 6, line 289: What does it mean for a sum to be "equivalent" to another sum? Does the author(s) mean "equal"?
3. Theorem 9: The proof idea only seems to (informally, but I like this here, as I mentioned in the "strengths" section) show that the satisfiability problems are NEXP-hard instead of NEXP-complete. The proof in the appendix does, however, prove the desired result. I suggest that the authors rephrase this, or (if I'm mistaken here) explain why the current proof idea (informally) shows that they are NEXP-complete.

### Soundness
3

### Presentation
3

### Contribution
4
