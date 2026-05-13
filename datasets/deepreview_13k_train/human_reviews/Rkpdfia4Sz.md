# Learning Discrete Latent Models from Discrete Observations

- Decision: Reject
- Scores: 3, 3, 6, 5

## Abstract
A central challenge in machine learning is discovering meaningful representations of high-dimensional data, commonly referred to as representation learning. However, many existing methods lack a theoretical foundation, leading to unreliable representations and limited inferential capabilities. In approaches where certain uniqueness of representation is guaranteed, such as nonlinear ICA, variables are typically assumed to be continuous. While recent work has extended identifiability to binarized observed variables, no principled method has been developed for scenarios involving discrete latent variables. In this paper, we show how multi-domain information can be leveraged to achieve identifiability when both latent and observed variables are discrete. We propose general identification conditions that do not depend on specific data distributional assumptions or parametric model forms. The effectiveness of our approach is validated through experiments on both simulated and real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a set of conditions for model identifiability in the binary data case. The authors have developed separate conditions for both local and global identifiability. The paper also addresses identifiability under very strict assumptions regarding the mapping between latent factors and observed variables. While similar results exist under similar frameworks, the authors' multi-domain approach represents a novel contribution to the field. The authors also conduct a set of experiments designed to prove the paper's main claims.

### Strengths
* The paper tackles an important issue, as model identifiability is crucial.
* The paper's introduction is well-constructed, explaining concepts clearly and providing appropriate illustrations
* The problem is well-defined, and the derivations appear correct under the stated assumptions

### Weaknesses
 * While the section ordering is logical, the paper's writing is confusing, and lacks a well-defined summary of conditions for each type of identifiability. Some assumptions are stated redundantly (e.g., latent factors being mutually independent within each domain, positive free parameters), and some results appear unnecessary, adding to the confusion.

* The assumptions, which are central to the paper as they constitute the conditions for identifiability, require more explanation and discussion of their practicality:
  - Assumption 1.2 is unrealistic in medicine, for example (although admittedly common in the field)
  - Assumption 2 creates a degenerate model as described earlier
  - Assumptions 4.2 and 5.2 appear particularly rushed and unclear; for instance, would a redundant (always 1) observed variable break model identifiability?
  - Assumption 6, which is core to the proof, is almost identical to the target proposition, making it seemingly circular


* The paper claims in the abstract: 'In this paper, we show how multidomain information can be leveraged to achieve identifiability.' However, it's not clear from the paper how the multidomain setup "leveraged" identifiability. Moreover, given that identifiability is a model property, it's unclear how a 'multidomain' setup can be 'leveraged.' Furthermore, the need for a new work for the multi-domain setup isn't well explained, which is problematic given this is the paper's claimed novelty.

* There is insufficient explanation of how the provided experiments prove the claimed identifiability.
While the paper derives sufficient conditions for identifiability, there is no discussion about whether these conditions are necessary and to what extent, thus limiting the paper's contribution.

* The paper's title focuses on discrete distributions, although the content appears to address only binary distributions.

* Section 3 appears redundant as no other sections rely on it, and its results are trivial under such strict assumptions, leading to a degenerate model. The same applies to Theorem 2.

### Questions
* Lines 036-038: Citation needed?

* Lines 050-051, '...deep learning techniques to ensure identifiability': This requires clarification, as identifiability is a model property rather than an algorithmic one. How can deep neural networks 'ensure' identifiability?

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
This paper investigates the problem of identifying meaningful representations in high-dimensional data, a central objective in representation learning. While some methods offer unique representations, such as nonlinear independent component analysis (ICA), these approaches generally assume continuous variables, with recent work extending identifiability to binarized observed variables. However, there has been no established framework for cases involving discrete latent variables. In response, the authors propose a method to leverage multi-domain information for achieving identifiability when both latent and observed variables are discrete. They present general identification conditions that do not rely on specific data distributions or parametric models. Experimental results, conducted on both simulated and real-world datasets, are used to validate the effectiveness of the proposed approach.

### Strengths
To the best of my knowledge, the paper studies a scenario (discrete observed variables + discrete latent variables) that has not been explored so far.

### Weaknesses
I find the paper extremely unclear in terms of motivation, intuition behind results/assumptions, and overall presentation. This severely hinders the readability of the article and the credibility of its claims. Here are some more specific concerns of mine:

1. The introduction of $K$ domains is not justified. What are these domains modeling? Why are they necessary in the analysis? The paper does not provide a clear explanation of the role of these domains in the identifiability framework. It is unclear why multiple domains are needed instead of a single domain with more data.

2. Definition 1 is not precise, it needs to be mathematized in order to be relied on to follow proofs; The definition lacks a formal mathematical description, making it difficult to verify the claims and follow the proofs. The concept of 'state-level identifiability' is not rigorously defined.

3. The proof of Theorem 3 is unclear. Also, assuming that the proof is correct, given how trivial it is, does this result really deserve the name of "Theorem"? The proof lacks detailed steps and explanations, making it hard to follow. The significance of the result is questionable given its apparent simplicity.

4. The definition of local identifiability needs to be (1) mathematized, (2) moved to the main text, as it seems pretty central to the paper's focus; The concept of local identifiability is crucial for the paper's claims, yet it is not formally defined in the main text. This makes it difficult to understand the scope and limitations of the results.

5. The explanation after Theorem 3 is unsatisfactory (e.g., why is it ok to assume that the columns of the Jacobian are linearly independent?); The justification for assuming linearly independent columns in the Jacobian is not well-explained. It is unclear under what conditions this assumption holds and what its implications are.

6. In Lemma 2, the two $\otimes, \tilde \otimes$ notations are unclearly differentiated; The distinction between the two outer product notations is not clearly defined, leading to confusion in the mathematical derivations.

7. The experiments, especially the real world ones, do not seem to match the goals of the paper. One of the points made at the beginning is that, in some applications, it may be crucial to model latent variables as discrete rather than continuous, especially when they may have a certain interpretation for the science domain in question. However, here the authors don't really justify their choice of data through this lens (at some point, they even discretize originally continuous data) nor do they compare the performance of their method with continuous latent variable alternatives. This casts doubt on the ability of these experiments to validate the author's claims; The experimental setup does not align well with the motivation of the paper. The choice of datasets and the lack of comparison with continuous latent variable models raise concerns about the practical relevance of the proposed method.

8. More broadly, while it may be true that no previous work looked at this categorical-categorical setting, I wonder if this is because such a setting has no peculiarity of its own. Indeed, looking at the proofs, no new interesting technique seems to have been introduced. Nevertheless, I would be happy to hear what the authors may have to say to disprove this feeling of mine.

### Questions
As I mentioned above, the paper has many unclear points (at least to me). Here are some questions that could help the authors clarify those points:

1. In Assumption 2, do the authors mean for all $k$?

2. In Assumption 4, why is it reasonable to assume that the derivatives wrt all free parameters are positive?

3. In Definition 2, wouldn't a $2^D$ vector suffice (once you know $P(X_i = 0 \mid \boldsymbol Z = \boldsymbol z_l)$, you also know $P(X_i = 1 \mid \boldsymbol Z = \boldsymbol z_l) = 1 - P(X_i = 0 \mid \boldsymbol Z = \boldsymbol z_l)$)?

### Soundness
2

### Presentation
1

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
This paper studies mathematical conditions to achieve identifiability in discrete-discrete latent variable models. I think this is an interesting paper with good theoretical results. I am happy to raise my score should the authors respond thoughtfully to my comments and questions.

### Strengths
- Clear presentation
- Closes a clear gap in the literature
- Relevant overall topic (latent variable models in representation learning)

### Weaknesses
 - The empirical examples are both not really discrete but rather discretized, which of course is not ideal. Since the paper is primarily theoretical and just has some empirical examples as a “nice addition”, I think this is fine.
- Still I would like to see real examples, where we *actually* have both discrete observed and discrete latent variables. The authors argue with the cases where we would, for example, discretize personality traits, which as a psychologist by training originally, I have to reject as not a good (oversimplifying) approach.

- The authors often state the inequalities involving N, K, D as weak, e.g Assumption 4.1 and similar. Can the authors explain a bit more on why they think these are weak? I.e. can we expect these to be justified in most real world cases?
- Can the authors comments on the major difference between Theorem 3 and 4. I.e. in which way does the independence assumption relax the other requirements?
- Results simulation study: When the authors say that they show empirically that the assumptions of Theorem 6 can be strongly weakend, can they say which idendifiablilty constraints the theorem would imply in this concrete case (3 latent variables, 7 or 8 observed variables)?

### Questions
- The authors often state the inequalities involving N, K, D as weak, e.g Assumption 4.1 and similar. Can the authors explain a bit more on why they think these are weak? I.e. can we expect these to be justified in most real world cases?
- Can the authors comments on the major difference between Theorem 3 and 4. I.e. in which way does the independence assumption relax the other requirements?
- Results simulation study: When the authors say that they show empirically that the assumptions of Theorem 6 can be strongly weakend, can they say which idendifiablilty constraints the theorem would imply in this concrete case (3 latent variables, 7 or 8 observed variables)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper establishes a theoretical foundation for scenarios involving both discrete latent variables and observations. The author(s) discuss one-to-one and flexible mappings, as well as local and strict identifiability under flexible mappings. The results of experiments conducted on both simulated and real-world datasets confirm the required number of domains of identifiability as derived from the theorems.

### Strengths
1. The author's use of multiple domains relaxes certain conditions, enabling flexible modeling without imposing restrictive assumptions. 
2. It identifies marginal distributions based on specific assumptions.

### Weaknesses
1. I find that Assumption 1.2 appears to be too general. For instance, in the example illustrated in Figure 1, it's possible that X3 could be a cause of X1.
2. I'm not an expert in ICA and found myself waiting for an explanation of both ICA and the term `domain` as I read. It would be helpful for the author to inform readers early on that Appendix A1 contains the necessary background knowledge.

### Questions
1. For the abstract, providing the full name of ICA could be better.
2. For assumption 1.1, should it be P(X,Z|k)=P(X|Z)p(Z|k)?
3. For Theorem 2, you said after taking the log on both sides of 2. What is 2? And why do the linear equations have unique solutions if and only if $2^{D-1} \ge D$?
4. For line 652, please add more examples.
5. For line 231-232, why for $\alpha$, the l ranges to $2^D-1$?

### Soundness
3

### Presentation
2

### Contribution
3
