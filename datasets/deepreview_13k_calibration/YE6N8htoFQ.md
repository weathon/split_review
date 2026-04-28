# Vocabulary In-Context Learning in Transformers: Benefits of Positional Encoding

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8, 6

## Abstract
Numerous studies have demonstrated that the Transformer architecture possesses the capability for in-context learning (ICL). In scenarios involving function approximation, context can serve as a control parameter for the model, endowing it with the universal approximation property (UAP). In practice, context is represented by tokens from a finite set, referred to as a vocabulary, which is the case considered in this paper, i.e., vocabulary in-context learning (VICL). We demonstrate that VICL in single-layer Transformers, without positional encoding, does not possess the UAP; however, it is possible to achieve the UAP when positional encoding is included. Several sufficient conditions for the positional encoding are provided. Our findings reveal the benefits of positional encoding from an approximation theory perspective in the context of in-context learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents several theoretical results on the expressivity of
individual transformer models with fixed weights implementing different
functions by changing their context.

* The paper considers transformers that make predictions given a sequence of
  embedded $x$/$y$ pairs as tokens in context.
* The transformer architecture has a single-layer, single-head, attention-only
  (no MLP) transformer (that is, essentially just a single attention
  mechanism). In detail, the architecture computes query--key affiliation
  scores based on the $x$-components of the tokens, processes these using
  either a softmax transformation or element-wise ReLU activation, followed
  by multiplication by a value score based on both $x$s and $y$s, after which
  they extract the prediction corresponding to the final output.
* The paper considers several settings and whether or not a transformer with
  arbitrary fixed (full-rank) attention matrices achieve the universal
  approximation property, in the sense that for any continuous function on a
  compact domain there exists a context of some length that causes the
  transformer's prediction of the next $y$ as a function of the next $x$ is
  arbitrarily close to the continuous function.
  1. If any real vectors are allowed as $x$/$y$ tokens in the context, the
     paper shows that the transformers have the universal approximation
     property in the above sense.
     * The proof relies on constructing a context of length $n$ that makes
       the transformer implement a given MLP with a single hidden layer of
       width $n$, and the classical result that such MLPs have the universal
       approximation property.
  2. If the $x$/$y$ tokens that are allowed are restricted to a finite set of
     pairs, then the paper argues that transformers lack the universal
     approximation property.
     * The argument proceeds by constructing a similarly constrained set of
       MLPs that are constructed using a finite collection of hidden units,
       and showing that these families of functions lack the universal
       approximation property, then arguing that the connection between MLPs
       and transformers from the previous setting shows that this is also the
       case for transformers.
  3. If the $x$/$y$ tokens are restricted to a finite set containing at least
     certain irrational basis vectors, *and* the transformer's inputs are
     augmented with an additive positional encoding that, when added to the
     $x$-component of the finite tokens, creates a set of tokens that are
     dense in the input space (or, in the case of ReLU networks, dense in at
     least the unit hypercube), then the transformers again achieve the
     universal approximation property.
     * I have tried to understand the statement of this theorem but given my
       expertise is not in approximation theory, I was unable to review this
       proof in detail. A superficial summary is that the proof involves an
       application of Kronecker's Theorem on approximating real vectors with
       integer multiples of irrational vectors.
* The paper motivates the importance of the above results with the
  observation that transformers used in natural language processing involve a
  finite vocabulary, which gives rise to a finite set of embedded token
  vectors. Therefore, an informative analysis of the in-context expressivity
  of transformers should involve such a finiteness constraint. In this
  context, the paper's results demonstrate that the inclusion of a positional
  embedding is crucial to retaining the universal approximation property.

I also include a summary of my review as follows.

* While functional approximation is not my area of expertise, I found the
  paper interesting and thought-provoking, and relatively clearly written and
  relatively easy to follow. I particularly liked the framework for studying
  transformers implementing different functions in context, and the neat
  construction of how to implement an arbitrary MLP using the attention
  mechanism.
* Unfortunately, I found what appears to be a potentially serious gap in the
  argument that the finite-vocabulary transformer architecture does not have
  the universal approximation property, and I was not able to see an easy way
  to close this gap. If I am correct and the authors are unable to close this
  gap then this would appear to undermine one of the major results of the
  paper.
* Aside from this, my overall impression of the novelty and significance of
  the paper was weakened by the strength of some of the assumptions and a
  lack of detailed comparison to what appears to be a closely related work
  (the cited work of Petrov et al., 2024b).
* While studying the paper I also noted a number of what seem to me to be
  minor technical errors that would probably be easy to fix, I list these
  along with questions to the authors I encountered while studying the paper.

**EDIT TO ADD:** Summary of discussion:

* The authors' revision fixed the gap I had noted in my initial review, but when looking at the paper in more detail during the discussion period I noticed another major gap in the proofs for the non-universality of finite-vocabulary prompting for softmax attention (see comment ['Response to Rebuttal Part 1'](https://openreview.net/forum?id=YE6N8htoFQ&noteId=fYd5DD26co)). Unfortunately due to this remaining gap I am still recommending that the paper should be rejected.
* The authors' revisions and rebuttals somewhat addressed the other concerns I listed, by clarifying the relationship with prior work and the role of the various assumptions.
* The authors' revisions addressed all of the minor technical errors and the authors answered all of my questions from my initial review. During the discussion period I noticed some additional minor technical issues in the revised paper which I have communicated to the authors.

**EDIT TO ADD:** Summary of further discussion and score updates.

* The authors outlined how to address the new gap I noticed. I am satisfied that their proposed fix will work. I am aware of no further gaps in the proofs for sections 2 and 3. I haven't been able to verify the proofs in section 4.
* The revised paper made explicit that section 4 does not apply to softmax attention, which I think is a significant limitation.
* The revised paper has improved the presentation, but various non-trivial presentation issues remain and I believe that resolving them requires further review, which is now impossible.
* Overall, while I am no longer aware of any major flaws in the argument, I still don't think the paper should be accepted. But I am less sure about this, so I am raising my score from 3 (reject) to 5 (borderline reject).

### Strengths
I think understanding the expressivity of neural architectures is an
interesting and important theoretical problem in deep learning. It is
important to have a clear understanding of the theoretical limits of our
models, and, while in my opinion there is often a disconnect between positive
expressivity results and the way that neural networks learn to implement
functions in practice, we can still derive qualitative insights about how
neural networks might implement certain kinds of functions using features
such as depth, or, in this case, an attention mechanism, which can be
informative in practice.

Within this topic, the current paper presents an analysis of the problem not
of the expressivity of transformers as a neural architecture, but of the
expressivity of an arbitrary transformer model with fixed weights through
changes to the prompt alone. This is an ambitious undertaking and has the
potential to shed light on one of the most important topics in modern deep
learning, namely the nature of in-context learning.

In this setting the authors have put forward an elegant notion of the
in-context expressivity of a fixed transformer through the provision of a
particular context. While as I have mentioned functional approximation is not
my area of expertise, it appears to me that this framework is novel and I
believe it has been well done.

A neat example of the in-context framework is the link the authors have
achieved between single-hidden-layer neural networks and their in-context
transformer (captured in Lemma 2 for the case of ReLU attention and embedded
in the proof of Lemma 3, though I have not reviewed the latter). I found this
connection interesting and thought-provoking, and it leads to a very elegant
proof of the universal approximation property of prompting a fixed
transformer in the setting with arbitrary token vectors.

### Weaknesses
 **Gap in Theorem 6:**
Theorem 6 is accompanied by a very brief proof that says the result
immediately follows from the connection between FNNs and transformers plus
Lemma 5. I couldn't see how this conclusion follows from these results, and
in fact I have come to suspect that it might not follow from them at all.

Consider the case of ReLU networks. By "the connection between FNNs and
Transformers" I take it you are referring to Lemma 2. As far as I can tell,
the Lemma is one-directional, showing the existence of a context for every
FNN but *not* the existence of an FNN for every context. At the very least,
the reverse direction would require further justification.

Given this, in Theorem 6 it is not sound to reason that because there are
some functions that cannot be approximated as an FNN with ReLU activation
these same functions must not be approximable by the transformer with any
context. It seems to me that you also have to rule out the existence of
another context which might approximate the function.

In the case of softmax networks the same issue may apply, however the status
is not clear to me because there is no separate Lemma for "the connection
between FNNs and Transformers" for the case of softmax activation, with the
details apparently to be found in the proof of Lemma 3 and involving
reasoning via a custom architecture involving exponential activation.

I don't immediately see how this argument can be recovered, and I invite
clarification from the authors. If I am not mistaken about this problem with
the proof of Theorem 6, and it is not able to to be resolved, then I can't
recommend the paper for acceptance.


**Inadequate discussion of closely related work:**
The authors state in the introduction "Meanwhile, Petrov et al. (2024b)
explored the role of prompting in Transformers, proving that prompting a
pre-trained Transformer can act as a universal functional approximator." I
was not previously familiar with this cited work, but from the authors' own
description it sounds quite closely related in scope to the present work,
which is also about proving that under certain conditions a transformer can
act as a universal function approximator.

Could the authors please clarify the relationship between the contributions
of Petrov et al. (2024b) and their contributions?

**Some implausible assumptions:**
I believe the authors are interested in finding universal approximation
results that will eventually speak to the limitations of architectures
used in practical deep learning settings. Given this motivation, I was made
uncomfortable by the following features of the setting and assumptions.

1.  **The use of ReLU attention.** Of course, ReLU is a very commonly used
    activation function, including with transformer architectures. However, I
    have never seen it used in place of softmax for the post-processing of the
    query--key affiliation scores (usually it would be used, for example, as
    part of an MLP step after the attention step in a transformer block).

2.  **The reliance on a dense positional encoding.** In Theorem 8 the
    universal approximation property is achieved under the assumption that the
    positional encoding essentially turns the finite input token vocabulary
    into a set that is dense in $\mathbb{R}^{d_x}$.

These features are apparently in a kind of trade-off: In Corollary 10, the
authors give a universal approximation result requiring the positional
encodings are merely dense in the unit hypercube, not the whole input space.
This is also a tall order but seems much more plausible. However, this
Corollary is only given for transformers with ReLU attention, not the more
standard softmax attention.

Finally, I appreciate that the authors have acknowledged the strong
assumption that the positional encoding is dense, and pointed out that they
can be addressed with future work. However, I would have liked to see a more
in-depth discussion around this topic: do the authors have any reasons to
believe that this assumption could be relaxed, or does it appear to be
fundamental to the entire diophantine approximation approach pursued here?

### Questions
I studied the technical results up to and including the statement of Theorem
8, and I noticed the following potential minor errors, all of which I expect
would be easy to fix (if I am not mistaken about them in the first place). I
would be happy to clarify any of my questions in further detail as needed.

Definition of transformer and feed-forward architectures:

1. In the definition of attention, $Q$ and $K$ have undefined shapes (only the
   shape of $B$ and $C$ are defined). One can infer from usage that $Q$ and
   $K$ have $d_x + d_y$ columns, but the number of rows could be any number
   greater than or equal to $d_x$ and the equations could come out the same.
   I invite the authors to consider removing the zero rows entirely such that
   $Q = [B\ 0]$ and $K = [C\ 0]$.

2. In the definition of attention, $V$ is described with shape $d_y$ by $d_y$.
   This must be a mistake since:
   * $V$ is multiplied by $Z$ of shape $d_x+d_y$ by $n+1$ implying it should
     have $d_x+d_y$ columns.
   * The shape of the output of attention has the same number of rows as $V$,
     and needs to be added to $Z$ (equation 10), suggesting that $V$ should
     have $d_x+d_y$ rows too.
   * Indeed later (line 266) the authors partition $V$ into blocks such that
     the shape is $d_x+d_y$ by $d_x+d_y$.

3. In Equation 10 there is an undefined symbol $h$ which, from context,
   appears should be the activation function $\sigma$.

4. Equation 10 uses input $x; Z_{:, 1:n}$ whereas later invocations of
   $T^\sigma$ use $x; X, Y$ (and the RHS of equation 10 is expressed in terms
   of $Z$).

5. I invite the authors to consider promoting some assumptions on the
   transformer architecture from later in the text to section 2.1 where the
   architecture is introduced, so that they are all in one place.
   * This applies to the decomposition of $V$ into four parts.
   * Also the assumption that $B$, $C$, and $F$ are non-singular would then
     make sense in section 2.1.

6. As written, the definition of feed-forward networks does not appear to
   allow for the use of softmax activation, which is not an element-wise
   function due to normalisation.

    This led me into some confusion later in the paper when the authors talk
    about how softmax FNNs with a finite vocabulary of units leads to an
    infinite-dimensional family of functions. Could the authors please clarify
    the definition of FNNs with softmax activation and the definition of the
    finite-vocabulary family of softmax networks, if they indeed intend for
    these networks to have normalisation?

7. Finally, in equation (11) (the definition of the finite-vocabulary family
   of transformers), $n$ is fixed, but I think the authors intended for it to
   be any positive integer. This would make more sense by analogy to
   classical FNN approximation results for unbounded width (see also the
   correspondence between FNN width and context length of Lemma 2), and
   in Theorem 8 the authors explicitly allow unbounded context length.

   It seems important that the definition of the family should allow
   unbounded context length, because the authors want to say, for example in
   Theorem 8, that "[the family] can achieve the UAP", and in Theorem 6, that
   it cannot, but, trivially, if the family uses a finite context length then
   (given the tokens are also finite) it is a finite family of functions and
   therefore it trivially cannot have the UAP.

Lack of universal approximation properties for finite vocabulary setting:

8. What norms are being used in the approximation property statements?
   Starting with Lemma 1, which I think is the norm used throughout, but then
   also for Theorem 6, there is a norm with subscript $C(K)$ (is that the
   same?)

9. What do the authors mean on line 308 by "the case of non-softmax
   activation"? I think they simply mean ReLU activation, but I am left
   uncertain as to whether they are trying to make a more general claim.

10. What do the authors mean on line 309 by "It is well known that
   finite-dimensional spaces are compact"? This is false in the generality
   stated. Am I missing an assumption? It seems to me that the span would be
   unbounded and therefore it is not compact. Nor does the family of networks
   appear to be a closed and bounded subset of the span, which would ensure
   compactness given that the span is finite-dimensional.
   Actually, I am not immediately sure how to resolve this, but I hope the
   authors might be able to address it.

    As an aside, I invite the authors to consider stating the ReLU case as a
    numbered lemma and giving a formal proof, even if turns out to be a short
    proof.

11. On line 312 the authors state that "the dimension of the span of [the
   finite set of softmax networks] might be infinite". I didn't immediately
   understand this claim, and I wanted to check my understanding. Is is due
   to the presence of normalisation between units that even though the softmax
   networks are each comprised of weighted units from a fixed finite
   collection of basic units, the normalisation means that these networks
   won't generally be linear combinations of each other?

12. In Lemma 5, the statement must hold for any $\epsilon_0 > 0$. Intuitively
   I thought the choice of inapproximable function should have to depend on
   $\epsilon_0$, but I don't see such a dependence in the proof sketch, and
   in the proof it is stated that $\epsilon_0 = 0.1$. I am concerned that the
   proof does not go through for $\sin(m \pi x)$ if $\epsilon_0$ is large
   enough since the approximation will no longer have to distinguish between
   zeros and peaks.

    Perhaps the constructed function should be something more like
    $\frac{10}{\epsilon_0}\sin(m \pi x)$? (I'm not sure what norm is being
    used but I chose $10$ based on the decision to use $\epsilon_0 = 0.1$ in
    the proof).

Restoration of universal approximation property through positional encoding:

13. Theorem 8: In the statement, there is no introduction of the function $f$,
   which I assume should be introduced as a continuous function from the
   compact domain to $\mathbb{R}^{d_y}$.
14. Line 383: In the definition of $S$, you want $j \in \mathbb{N}^+$ rather
    than $i \in \mathbb{N}^{+}$.
15. Line 431: The same error again, you want $j \in \mathbb{N}^+$.

Typos:

16. Line 58: "Transformersin" missing space.
17. Line 111: "for for".
18. Line 283: "Propriety" in title of section 2.4.
19. Line 383: "and ,"

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper is about the approximation properties of transformers in ICL: The authors fix the transformer
weights V ,Q,K, then given a target function f, they aim to adjust the content of the context so that the output of the Transformer network can approximate f. The claim is that when there is no restriction on the size of the vocabulary, single layer transformers have the universal approximation property in ICL. But when the size of the vocabulary is limited, single layer transformers do not have the
universal approximation property in ICL, which is remedied by allowing for position encodings.

### Strengths
ICL is poorly understood, and this paper makes a step towards understanding the capacity that transformers have for ICL and the role of positional encodings.

### Weaknesses
A lot of the paper is spent setting up notation. However, many statements are imprecise and opaque. For example, the proof sketch of theorem 8 is quite hard to follow, particularly the jump from the finite nature of the vocabulary to the limitations on UY and X⊤B⊤C. The connection between the density of set S and the density of X⊤T B⊤C is not well explained, especially considering that the position encoding is fixed after being learned. Furthermore, the statement in line 424 regarding the unboundedness of positional encoding is unclear and requires further elaboration.

Logically, the idea of fixing the network weights and "adjusting the content of the context so that the output of the Transformer network can approximate f" doesn't commonly arise in practical scenarios. For example, Lemma 3 finds a vocabulary matrix X, Y to fit an arbitrary function f. But after the model is trained, in a typical ICL setting the model has to learn to adapt to the arbitrary function f on the fly given the fixed vocabulary matrix and weights V, Q, K. That is, one does not optimize over the context to find the function. This raises concerns about the practical relevance of the theoretical framework presented. The paper would benefit from a more thorough discussion of how this framework relates to real-world ICL scenarios.

No experiments or simulations to illustrate the result -- not a serious problem for a theory paper but does take away the significance of this work. The lack of empirical validation makes it difficult to assess the practical implications of the theoretical findings.

### Questions
Theorem 8: However, in natural tasks, we don't have a choice over the content of the context, we are
given sequences and yet the network must fit the target function f in-context. Could the authors please elaborate on why this is a reasonable setting?

Line 398: "From previous work" -- which one?

Is there a missing hypothesis in line 383/theorem 8: "If S = \{x_i + P^{(j)}_x ∣ x_i \in Vx, i \in N_+\} is
dense in R^{dx} , and" 

Line 409 "The contradiction arises from the finite nature of the vocabulary, which limits the finiteness of UY and X⊤B⊤C". What does finiteness mean here?

Line 410 "We invoke the density of the set S = {xi + P(j) x ∣ xi ∈ Vr, j ∈ N+} in Rdx ,
which ensures the density of X⊤T B⊤C." But don't we learn a particular position encoding which is then fixed for the
transformer, so for a particular transformer S can't be dense -- doesn't this defeat their paper's goal?

Line 424 "The finiteness and boundedness of V impose stringent requirements on
positional encoding, which, to some extent, necessitates unbounded positional encoding" It's unclear what this statement means.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper provides a mathematical theory of how adding positional encoding information to input tokens affects a transformer's ability to exhibit the Universal Approximation Property (UAP). 
This is the study of when a simple, single-layer transformer can function as a universal approximator - that is, it can model any continuous function with arbitrary precision. The researchers showed that positional coding plays a crucial role: without it, single-layer transformers fall short of universal approximation. 
A key aspect of the mathematical proof is the use of the Kronecker Approximation Theorem to establish conditions that ensure the density of the sum of the positional encoding and the input tokens. This theorem allows us to show that positional encoding provides a sufficiently rich sum of tokens.
 This result underscores that positional encoding is not only helpful, but essential for transformers to effectively model complex patterns, especially when working with limited, discrete vocabularies, from a UAP perspective.

### Strengths
-The paper advances the theoretical understanding of in-context learning and its relation to positional encoding in transformers, especially under finite vocabulary constraints, by mathematically proving that positional encoding allows transformers to achieve UAP.
- The mathematical proof is based on the effective f use of the Kronecker Approximation Theorem, and the rational formulation of the theory.
- The paper provides clear conditions for UAP: The study defines explicit mathematical conditions and sufficient criteria for positional encoding to enable UAP, providing a basis for further theoretical and applied research in NLP.

### Weaknesses
 - Although the theoretical contribution is clear, the practical insights for practitioners are limited.
- This paper lacks experimental validation. While the mathematical differences are qualitatively clear, there are no experimental demonstrations to show how these theoretical differences translate to actual differences in model performance.

### Questions
- Is it possible to provide some numerical demonstration that clearly shows that the difference suggested by this theory in positional encoding actually produces different performance? 
- In the discussion, it may be better to describe a bit more about the theoretical insights based on the understanding gained through the proof for practitioners who will be designing positional encoding or just using Transformer.

### Soundness
3

### Presentation
4

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
The most important contribution of this work is theoretic: In (single-layer) Transformer,s (vocabulary) in-context learning can only (possibly) achieve UAP when positional encoding is there. I am not an expert in this field, but compared to the most known Transformer ICL+UAP research to my knowledge (e.g., Yun et al., Luo et al., Petrov et al.), this work emphasizes the positional encoding in Transformer.

### Strengths
- The theoretical insight and contribution: The promise of this work is intriguing to me, as it’s the first time I’ve seen research attempting to bridge the theoretical understanding of in-context learning from positional encoding through the lens of universal adversarial perturbations.
- The proofs (especially Theorem 6). With a finite vocabulary and no positional encoding, the authors prove that single-layer Transformers cannot achieve universal approximation properties (UAP) for ICL tasks.
- The discussion of ReLU is a plus to me.

### Weaknesses
This paper makes a good number of assumptions.
- I accept most of the assumptions made as valid, but...
- I would prefer the authors mention all assumptions more clearly in bullets or “Assumption $n$” like the Theorems. For example, Lines 378-379 state an important assumption of the density property using Diophantine approximation. I almost missed it…
- The part I am a bit concerned about is that this work only studies absolute positional encodings and single-layer transformers. The latter is fine, but I think the authors should discuss (at least on a higher level) how the results of this work could potentially generalize to other PEs like RPE and RoPE.

[Minor] In Sec 1.2 where positional encodings are discussed, I believe that the Rotary Position Embedding (RoPE) [1] should be mentioned.

### Questions
**Question 1**: In line 160 “Unlike the setting in Ahn et al. (2024); Cheng et al. (2024), in this paper, we do not assume a correspondence between $x^{(i)}$ and $y^{(i)}$” Are you suggesting that there is **independence** between  $x^{(i)}$  and $y^{(i)}$, or that they are **unpaired data** in a **weakly supervised setting**? Or do you mean there may be **false** or **unmatched pairs** of $x$ and $y$? 

**Question 2**: Can the results generalize to RPE and RoPE? Could authors include a discussion section on how their results might extend to or differ for other types of positional encodings like RPE and RoPE.

### Soundness
3

### Presentation
3

### Contribution
3
