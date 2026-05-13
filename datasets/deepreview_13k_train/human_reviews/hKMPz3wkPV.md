# Towards a formal theory of compositionality

- Decision: Reject
- Scores: 8, 6, 5, 8

## Abstract
Compositionality is believed to be fundamental to intelligence. In humans, it underlies the structure of thought, language, and higher-level reasoning. In AI, it enables a powerful form of out-of-distribution generalization, in which a model systematically adapts to novel combinations of known concepts. However, while we have strong intuitions about what compositionality is, there currently exists no formal definition for it that is measurable and mathematical. Here, we propose such a definition, which we call representational compositionality. The definition is conceptually simple, quantitative, and grounded in algorithmic information theory. Intuitively, representational compositionality states that a compositional representation is both expressive and describable as a simple function of discrete parts. We validate our definition on both real and synthetic data, and show how it unifies disparate intuitions from across the literature in both AI and cognitive science. We also show that representational compositionality, while theoretically intractable, can be readily estimated using standard deep learning tools. Our definition has the potential to inspire the design of novel, theoretically-driven models that better capture the mechanisms of higher-level human thought.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present a definition for representational compositionality, aiming to turn an old and only vaguely defined concept into a precise mathematical definition. They ground their definition in Kolmogorov complexity and demonstrate that for synthetic datasets, this quantity conforms well with intuitive expectations of how representational complexity should vary with different hyperparameters. They then consider two empirical representations and use an approximation to Kolmogorov complexity to compute their compositionality.

### Strengths
I think this is a generally well-written and thought-provoking paper. Compositionality and compositional generalization is an important topic across a number of different fields and I agree that a better formal understanding of what we mean by it is important. The authors present a conceptual framework that is well thought out and clearly presented and explain the intuitions behind it well --- I really appreciated the clarity of explanation especially given the highly conceptual and theoretical nature of the work. The empirical results demonstrate that this could be a useful metric and provide interesting use cases to think about.

A few other points I liked about the paper:
- I liked that the authors explicitly spelled out what bearing their definition has on various related concepts in the field.
- I appreciated the point of having a useful quantitative point of reference (i.e. compositionality of 1 indicating a complete lack of compositionality).
- I also thought the example of the grammar representations was a compelling argument for this definition.

### Weaknesses
I think the manuscript in its current form has two points that weaken its case for the proposed definition. One concerns discussing how this definition connects to compositional generalization and one concerns further demonstrating its practical usefulness and providing a concrete way for follow-up work to use this definition.

**Relationship to systematic generalization**

As the authors note in their introduction, compositionality is a highly relevant topic in part because it can enable systematic out-of-distribution generalization. This provides a complementary approach towards this question, i.e. compositional representations are representations that enable systematic generalization. There are a number of prior works who have laid out formal or conceptual frameworks relating different representations, architectures, and inductive biases to systematic/compositional generalization (albeit sometimes under different terms) [e.g. 1-4; as well as some papers that the authors already cite, e.g. Ren et al., 2023] and it would be useful to discuss at least some of them in terms of how they relate to this approach, e.g.: Do they get at the same concept of compositionality or do they address a different problem? How specific would you predict your definition to be, i.e. will neural networks that generalize well have highly compositional representations according to your definition?

I note that the authors already discuss systematicity and generalization in p. 252-262, but so far this discussion seems to be more focused on generalization of the functional embedding rather than the entire network of which $Z$ may be a part (or the input).

**Practical usefulness**

I found the authors suggested framework in Appendix B very intriguing and I think having such a concrete method for estimating compositionality could further increase the impact of the authors' proposed definition. I also think empirically evaluating the relationship between representational compositionality and generalization would be really interesting (e.g. across different network architectures that yield better or worse generalization, is there a correlation between compositionality and generalization?). I think adding this kind of practical method or evaluation would further increase the impact of this paper. I also understand, though, that addressing this may not be realistic during the revision period and I think the paper is still interesting and valuable without this --- as the authors note, the primary contribution of this paper is of theoretical/conceptual nature.

### Questions
- See weaknesses.
- To what extent are the changes in topological similarity due to different factors in the lookup tables because that implicitly changes the embedding dimensionality of each individual symbol. For smaller dimensionality (e.g. due to longer sentences), there will be more variance in how correlated different symbols are with each other, leading to lower correlation, whereas for larger dimensionality, most of them will be approximately orthogonal, leading to higher correlation, correct?
- Could you apply the prequential coding method to the synthetic examples in section 4.1, to further validate it?
- Could you specify the numerical values on the y axis in Fig. 2?

Minor comments:
- L. 151: superfluous “a”
- L. 178: “who’s” -> “whose”
- L. 374 “rather” -> “rather than”
- L. 400: “who’s” -> “whose”

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a formal definition of representational compositionality based on Kolmogorov complexity from the perspective of compression. The paper verifies that the definition aligns with human intuition on some examples in synthetic and real datasets.

### Strengths
1.	The motivation of this paper is greatly appreciated. It focuses on proposing a new formal definition of compositionality, which is sometimes a vague notion in previous literature. The definition based on compression is also novel.

2.	Some parts of the definition match well with intuition. For example, if the function $f$ to construct the representation $Z$ has no structure and is very complex to the extent of a look-up table, then intuitively this representation is not compositional. Accordingly, the proposed metric also shows low compositionally.

3.	The proposed metric shows the extent to which the representation is compositional, rather than a binary indicator.

### Weaknesses
1. My biggest concern for this paper is its presentation. Although the notion of compositionality is abstract in nature, I think the presentation in Section 2 and 3 could be clearer if properly accompanied by concrete examples. I was a bit struggled with the abstract words like “representations” “constituents” “semantics” “sentences” “language” “systematicity” “modularity.” They prevented me from reading through the whole section smoothly.

I find the example in Appendix D useful for understanding the proposed definition, and I encourage the authors to move some of them into the main text. On the other hand, however, these examples are still not concrete enough. For example, Example 5 says “$f$ is modular.” Then, what is a modular function? It will look much better if the authors can write out *the specific formula* of the function (maybe in a toy setting) and use *a figure to illustrate* how this function structure contributes to high compositionality.

2.  The assumption that the representation $Z$ follows a normal distribution seems arbitrary. Is there previous work to provide theoretical support for this assumption? Or is there any empirical evidence?

### Questions
1.	In Line 270, what is the definition of *modularity*?  Is modularity a specific form of *systematicity* in Line 253? If so, I think it is not appropriate to put these two terms in parallel.

2.	In the experiment on lookup table representations, are the sentence length and vocabulary size correlate with each other? For example, if vocabulary size is very large, then the sentence length is likely to be 1.

3.	Are there any practical implications of this theoretical definition of representational compositionality. In the conclusion, it says that the compositionality can be used to score tokenization schemes. Could you elaborate on this?

I’m also curious about whether this definition of representational compositionality can be readily applied to vision tasks. There have been some advancements in forcing CNNs to learn compositional parts [c1,c2], and object-centric learning [c3]. I wonder if the definition can be further validated under these settings.

4.	Some recent works studies the compositional generalization in object-centric learning, e.g., the reference [c4]. Although it focuses on a more concrete setting rather than a general definition as in this paper, it provides insight into how we can prove compositional generalization in a formal way. Could you briefly discuss how the definition of compositionality in this paper relates to or differs from that in [c4], and why viewing compositionality from the view of compression is “better”?

[c1] Zhang et al. Interpretable Convolutional Neural Networks. CVPR 2018.

[c2] Interpretable Compositional Convolutional Neural Networks. IJCAI 2021.

[c3] Locatello et al. Object-Centric Learning with Slot Attention. NeurIPS 2020.

[c4] Wiedemer et al. Provable Compositional Generalization for Object-Centric Learning. ICLR 2024.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In machine learning applications, we're often interested in understanding whether
a model has learned to solve a problem using a compositional computation, or
in evaluating whether it has discovered the latent compositional structure underlying
some domain of interest. This paper describes a procedure for answering these questions quantitatively. It
provides tools the compositionality of an
arbitrary collection of vector-valued datapoints $z$, using algorithmic
information theory as a tool.

From a technical perspective: we first posit that data results from a generative
process of the following form:

$$ \textrm{words } w \sim p(w) $$
$$\textrm{statistics } (\mu, \sigma) = f(w) $$
$$\textrm{true data } z \sim N(\mu, \sigma) $$

Next, we optimize $p$ and $f$ to minimize the overall Kolmogorov complexity:

$$K(Z) = K(p) + K(f) + \sum_i \log p(w_i) + \log p(z_i | w_i)$$

where

$$p(z_i | w_i) = N(z_i ; f(w_i))$$

Finally, we measure the compositionality of the representation system as:

$$C(Z) = K(Z) / K(Z | W) = K(Z) / (K(f) + \log p(z_i | w_i))$$

for $p$ and $f$ as chosen above. Intuitively, a representation $z_i$ is "more
compositional" if it is easy to reconstruct given a simple "parts-based"
representation $w_i$.

At a high level: I really like what this paper is trying to do---this is an important topic and I'm 
very excited about the idea
of trying to better ground intuition about compositionality in terms of
algorithmic information theory. However, I think there are a few major issues
with the formulation presented in the current paper, and I don't think this work
is quite ready to publish in its current form.

## RELATION TO EXISTING WORK

The paper claims that nobody has attempted to offer a quantitative, graded
measure of compositionality targeted at modern representation learning
applications. This is not quite right: people were thinking about similar
issues as part of the general late-2010s multi-agent communication fad, and I
would encourage the authors to check out https://arxiv.org/abs/1902.07181 and
follow-ups for some earlier work trying to answer related questions. The
technical approach proposed in the current paper is substantially different from this past work---in
particular, it successfully infers latent compositional descriptions of
data---but many of the experiments are very similar and it
might be informative to discuss some relationships to
representation-reconstruction techniques in addition to the existing discussion of topological similarity.

## DEGREES OF FREEDOM

My primary technical concern with the paper is the following: there's some
symmetry between $p$ and $f$ in the optimization problem described above, and as a
consequence different minima will give very different answers to the question of
whether a given representation system is compositional. Here's an argument that
I think captures the essence of the issue (we could be more precise about some
constant factors, but it wouldn't change the overall conclusion).

Suppose I have a set of $N$ random bitstrings of length $M$. This set is
incompressible, so no matter how I set $p$ and $f$ I'm going to have $K(Z) = MN$.

[For simplicity, let's also assume that $p(z ; f(w))$ isn't Gaussian, but instead a
sequence of $M$ Bernoulli distributions whose parameters are given by $f(w)$. The
choice of Gaussians is described as arbitrary in the paper, and it wouldn't be
too much more work to rephrase the argument below with that parameterization.]

Now consider two different schemes for setting $p$ and $f$.

**Scheme 1**: $p(z)$ is a deterministic distribution that places its mass on a single
word $w$, and $f(w)$ outputs the all-0.5s vector (so both functions are simple, and $K(p)$ and $K(f)$ are both
negligible). Then $K(W | p) = 0$ (it's deterministic), and $K(Z | W, f) =
-\sum_{i=1}^N \sum_{j=1}^M \log p(z_{ij}) = -\sum_{ij} \log 1/2 = MN$ (it's the
log-probability of a sequence of fair coin flips). So $K(Z) = MN$ as expected, and
$C(Z) = 1$ (since all terms but K(Z | W, f) are negligible or zero).

Scheme 2: Each word $w$ is just a copy of its associated bitstring $z$; $p(w)$ places a
uniform distribution over all length-$M$ bitstrings, and $f(z)$ is the identity
function (so a 0 in a bitstring gets turned into a Bernoulli that always outputs
0). $K(p)$ and $K(f)$ are negligible as before. But now $K(W | p) = -\sum_{i=1}^N
\log p(w_i) = -\sum_{i=1}^N M \log 1/2 = MN$, while $K(Z | W, f) = 0$ (since all
decoding is deterministic). $K(Z) = MN$ as before, but $C(Z)$ is **arbitrarily
large** as both terms in the denominator are negligible relative to MN.

So in fact this definition of compositionality allows us to conclude that incompressible noise is either highly compositional, or highly non-compositional.

## CONCEPTUAL CONSIDERATIONS

Taking a step back: there's quite a lot of work---in fields ranging from formal
semantics to category theory---that offers a precise mathematical treatment of
compositionality (just not one that's graded or approximate in the way this
paper and the above work is aiming at). One of the big differences between the
existing literature and current paper is that compositionality is usually
thought of as a property of *interpretation functions*, not *sets of
representations*: if we have a space of "sentences" and "meanings", each
equipped with some algebraic structure, then a mapping from sentences
to meanings is compositional if it is a homomorphism with respect to this
structure (see e.g.  https://plato.stanford.edu/entries/montague-semantics/).

This is closer to the paper's Section 3.1, which fixes the encoding scheme W and
its prior, and just tries to optimize the function f that translates ws into zs.
But in the experiments using this definition, $K(Z)$ is fixed to a constant, so
we're really just estimating something like $1/K(Z|W)$, which is just a measure of
how *predictable* $z$s are from $w$s, without saying anything about the structure
that relates them.

And I think this gets at the fundamental conceptual issue with the current
version of the paper---that the definitions of $C$ and $C^L$ don't actually say
anything about *parts*, or putting them together. They're just measuring a
predictability relationship between $z$s and $w$s, and we can make systems look more
or less "compositional" under these definitions by moving the cost of that
prediction operation into p or f. The brief mention that "structure-preserving
maps have low Kolmogorov complexity" does all the work of relating these
operations to compositionality as usually understood, such that we should maybe
think of the paper as arguing that low Kolmogorov complexity is necessary and
sufficient for high compositionality (which I don't think is what was intended, and
in any case orthogonal to the current experiments and technical presentation).

## NEXT STEPS

So what would it look like to have a definition of compositionality grounded in
algorithmic information theory? I think the answer has to focus on mappings
rather than representations---fixing both $Z$ and $W$ (as in 3.1, and existing work
on the subject). Then plausibly we could introduce a new latent variable that
doesn't describe an encoding of the data, but the structure of the mapping.
Maybe something like:

- Given w, compute $f(w) = w_1, ..., w_n$
- translate each $w_i$ into $g(w_i) = z_i$
- combine all $z_i$ into $h(z_1, ..., z_n) = z$

Then a system is compositional if this decomposition is *useful* for
implementing a low-complexity mapping, which you could characterize by e.g.
finding the most aggressive decomposition that remains close to the
unconstrained complexity $K(Z|W)$. This is of course all speculative! The main
thing I want to communicate is that, while there are issues with the current
proposal, I think the high-level idea is really promising, and could probably be
made to work if re-oriented around a definition of compositionality as a
property of maps rather than sets.

### Strengths
- Very interesting problem formulation and approach

### Weaknesses
My primary technical concern with the paper is the following: there's some
symmetry between $p$ and $f$ in the optimization problem described above, and as a
consequence different minima will give very different answers to the question of
whether a given representation system is compositional. Here's an argument that
I think captures the essence of the issue (we could be more precise about some
constant factors, but it wouldn't change the overall conclusion).

Suppose I have a set of $N$ random bitstrings of length $M$. This set is
incompressible, so no matter how I set $p$ and $f$ I'm going to have $K(Z) = MN$.

[For simplicity, let's also assume that $p(z ; f(w))$ isn't Gaussian, but instead a
sequence of $M$ Bernoulli distributions whose parameters are given by $f(w)$. The
choice of Gaussians is described as arbitrary in the paper, and it wouldn't be
too much more work to rephrase the argument below with that parameterization.]

Now consider two different schemes for setting $p$ and $f$.

**Scheme 1**: $p(z)$ is a deterministic distribution that places its mass on a single
word $w$, and $f(w)$ outputs the all-0.5s vector (so both functions are simple, and $K(p)$ and $K(f)$ are both
negligible). Then $K(W | p) = 0$ (it's deterministic), and $K(Z | W, f) =$
$-\sum_{i=1}^N \sum_{j=1}^M \log p(z_{ij}) = -\sum_{ij} \log 1/2 = MN$ (it's the
log-probability of a sequence of fair coin flips). So $K(Z) = MN$ as expected, and
$C(Z) = 1$ (since all terms but K(Z | W, f) are negligible or zero).

Scheme 2: Each word $w$ is just a copy of its associated bitstring $z$; $p(w)$ places a
uniform distribution over all length-$M$ bitstrings, and $f(z)$ is the identity
function (so a 0 in a bitstring gets turned into a Bernoulli that always outputs
0). $K(p)$ and $K(f)$ are negligible as before. But now $K(W | p) = -\sum_{i=1}^N
\log p(w_i) = -\sum_{i=1}^N M \log 1/2 = MN$, while $K(Z | W, f) = 0$ (since all
decoding is deterministic). $K(Z) = MN$ as before, but $C(Z)$ is **arbitrarily
large** as both terms in the denominator are negligible relative to MN.

So in fact this definition of compositionality allows us to conclude that incompressible noise is either highly compositional, or highly non-compositional.

Taking a step back: there's quite a lot of work---in fields ranging from formal
semantics to category theory---that offers a precise mathematical treatment of
compositionality (just not one that's graded or approximate in the way this
paper and the above work is aiming at). One of the big differences between the
existing literature and current paper is that compositionality is usually
thought of as a property of *interpretation functions*, not *sets of
representations*: if we have a space of "sentences" and "meanings", each
equipped with some algebraic structure, then a mapping from sentences
to meanings is compositional if it is a homomorphism with respect to this
structure (see e.g.  https://plato.stanford.edu/entries/montague-semantics/).

This is closer to the paper's Section 3.1, which fixes the encoding scheme W and
its prior, and just tries to optimize the function f that translates ws into zs.
But in the experiments using this definition, $K(Z)$ is fixed to a constant, so
we're really just estimating something like $1/K(Z|W)$, which is just a measure of
how *predictable* $z$s are from $w$s, without saying anything about the structure
that relates them.

And I think this gets at the fundamental conceptual issue with the current
version of the paper---that the definitions of $C$ and $C^L$ don't actually say
anything about *parts*, or putting them together. They're just measuring a
predictability relationship between $z$s and $w$s, and we can make systems look more
or less "compositional" under these definitions by moving the cost of that
prediction operation into p or f. The brief mention that "structure-preserving
maps have low Kolmogorov complexity" does all the work of relating these
operations to compositionality as usually understood, such that we should maybe
think of the paper as arguing that low Kolmogorov complexity is necessary and
sufficient for high compositionality (which I don't think is what was intended, and
in any case orthogonal to the current experiments and technical presentation).

Realized I didn't respond to the point about predictability vs compositionality in sec 3.1. Suppose I have some highly compositional data with an extremely transparent encoding scheme, e.g. data are pairs of letters (e.g. $(a, b)$) and encodings $E$ are ASCII representations of these pairs (e.g. $[01100001, 01100010]$). Now suppose I take my letter pairs and pass them through a hash function, such that it's not possible to look at any individual part of the hashed data and say that it corresponds to the $a$ or the $b$. I would think of the hashed data as a canonical set of representations that is "predictable, but non-compositional" (and we can make $K(Z|W)$ really small / $\mathcal{C}^L(Z)$ really big). Is the intuition in the paper that this data is in fact compositional? If so, is there any difference between compositionality and predictability? If so, what do the separating cases look like?

OK, but just to clarify---should I interpret this comment as adding additional stipulations to the definition that aren't present in the paper? Either:

- Models "aren't overfit". What makes scheme 1 overfit and scheme 2 not overfit? More generally, what does "overfitting" mean here, given that none of the definitions presently make any reference to generalization?

- The particular programming model with which respect to which we're measuring $K$ complexity happens to have a short program for Dirac deltas and a long program for Gaussians. Kolmogorov complexity is typically only defined up to a constant factor, so if these constant factors are really important for choosing solutions to Eq 1, we're not really talking about Kolmogorov complexity in a general sense---we're tied to some specific model of computation, but it's currently not clear what that is (or why it's better than any of the other models that algorithmic information theory generally treats as interchangeable).

Again, I don't think these issues are insurmountable! But they really need to be locked down if the goal is to enable apples-to-apples between different sets of representations. My concern is that, even if we can agree about how to break the tie for this specific hypothetical, I'd be worried that there are other distributions that still have identifiability problems, and we need yet a different set of extra rules to break the tie in the right way.

Given the extensive exchange above, we would be curious to know whether our comments above have addressed your concerns about predictability vs. compositionality with regards to $C^L$ and, more generally, if there are any further points that would increase you support for our paper.

Hi authors! Thank you for the detailed response. Unfortunately, it doesn't address my main concerns---I still think the paper has fundamental technical issues and isn't ready to publish in its current form. Briefly:

The identifiability argument in the original review used discrete distributions to avoid all the complications that come up with entropies of continuous distributions. But if the Gaussian piece of this is important, let's just call $G$ the entropy / average number of bits needed to encode a sample from $\mathcal{N}(0, 1)$. Now suppose my data consists of $N$ i.i.d. draws from $\mathcal{N}(0, 1)$; the Kolmogorov complexity of this set is $NG$. Now as above we have two choices:

We can let $p = \mathcal{N}(0, 1)$ and $f(x) = (x, \epsilon)$

or we can let $p = \mathcal{N}(0, \epsilon)$ and $f(x) = (0, 1)$

In the former case compositionality scales with $NG$, and you pay $NG$ to represent the encodings $E$. In the latter case compositionality is constant, and you pay $NG$ to account for prediction noise. Both choices achieve the same value of the objective in Equation 1. As the author response notes, these two implementations are morally "the same". This is exactly the problem with the proposed definition---a useful definition of compositionality should be invariant to these implementation details. The constraints given in the first part of the author response don't actually help us break the tie here: we can implement both ps above as trivial transformers (constraint 1), the matrix of discrete representations $E$ contains either the binary encoding of all points or the trivial all-zeroes matrix in the two constructions above (constraint 2), $f$ outputs the parameters of a normal distribution in both constructions (constraint 3), and $p(z; f(w))$ is a Gaussian (constraint 4).

And despite the (helpful!) conceptual scaffolding in the author response, I'm genuinely unsure which of these two schemes the authors would consider to be the "right" one for encoding a bunch of unstructured noise. Is high-dimensional noise compositional or non-compositional? And given how much intuition / discretion seems required to compute $\mathcal{C}$, it seems a bit premature to refer to this as a "formal" definition. For something as fundamental as compositionality, it seems a little worrying for that definition to depend on things like transformers and even Gaussians rather than more basic computational primitives like Turing machines---in this sense, the version presented in the first paper draft seemed closer to the right answer than the revised one.

### Questions
- Did I miss something in the argument above?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a novel metric to measure representational compositionality from the perspective of algorithmic information theory. Specifically, by estimating the Kolmogorov complexity of the representations (Z) and the corresponding message matrix (W), the paper defined compositionality as the ratio of K(Z) to K(Z|W). Compared with earlier colloquial definitions of compositionality, the proposed metric is well-founded on algorithmic information theory. It has the potential to inspire a more detailed analysis of different practical systems. Compared with existing metrics like topological similarity, the proposed metric aligns better with our intuitions of compositional generalization, and also has the potential to be extended to more general scenarios. The paper also showcased how to estimate such a metric using standard deep-learning tools. The experimental results all support the analysis well. To the best of my knowledge, this is the first paper that formally defined compositionality using Kolmogorov complexity and the authors did a good job of practically estimating this metric in different scenarios. I hence suggest an acceptance.

### Strengths
- The paper is well-written and easy to follow.
- The discussion of limitations of colloquial compositionality highlights the necessity of a formal definition.
- Reaching the definition of compositionality step-by-step makes it easier to understand how different components of the final metric are formulated.
- The experiments are conducted at different levels (i.e., synthetic representations, emergent communication, and natural language).

### Weaknesses
 - The practical experiments can be more practical. It might be helpful to consider some LLMs. For example, if we can obtain the representations of some LLMs, how would the compositionality of these representations evolve during finetuning?
- Although the authors discussed it in the conclusion part, more discussions on how the proposed metric can inspire the new algorithm design can make the paper stronger. For example,  are there particular machine learning tasks or model architectures where you believe optimizing for this compositionality metric could lead to improvements?
- The role played by W and Z might be a bit confusing. It might be more helpful to draw a system diagram combining representation learning (i.e., how Z is estimated) and the sentence W together. IIUC, if we call our high-dim input X, consider an unsupervised representation learning as an example, our system should be X→Z→X’. We then have the hidden representation of input signals. After that, when we evaluate how good Z is, we introduce the messages W and f to evaluate the corresponding Kolmogorov complexity.

- For the first line of equation (1), if $p_w, W, f$ are all empty strings, then the right-hand side is still minimized. The equation is degenerated to be K(Z)=K(Z). Is that the case?
- Is there any particular reason to define C(Z) as the ratio of two K terms? What about the K(Z)-K(Z|W)? What’s the difference between these two options?
- It might be more helpful to provide a more formal definition of topological similarity. It appears in Figures 2 and 3. But defining them in the main context might be helpful.
- Still about topsim. This metric is notoriously known for its high complexity because we must calculate the pair-wise distance of all the examples. What about the complexity of the proposed method?
- Figure 3 caption: iterated learning is an inductive bias … I guess it should be “iterated learning amplifies the inductive bias of model’s learning that more compositional mappings are learned faster”?
- In section 4.2, the last paragraph, what is the “normal language” system trained without iterated learning?
- Results in section 4.3 demonstrate that different languages have different compositionality. Are there any results in linguistics that can verify this claim? Furthermore, the experiments show that Japanese has a negative topsim, is there any intuitive way to understand what this means?

### Questions
- For the first line of equation (1), if $p_w, W, f$ are all empty strings, then the right-hand side is still minimized. The equation is degenerated to be K(Z)=K(Z). Is that the case?
- Is there any particular reason to define C(Z) as the ratio of two K terms? What about the K(Z)-K(Z|W)? What’s the difference between these two options?
- It might be more helpful to provide a more formal definition of topological similarity. It appears in Figures 2 and 3. But defining them in the main context might be helpful.
- Still about topsim. This metric is notoriously known for its high complexity because we must calculate the pair-wise distance of all the examples. What about the complexity of the proposed method?
- Figure 3 caption: iterated learning is an inductive bias … I guess it should be “iterated learning amplifies the inductive bias of model’s learning that more compositional mappings are learned faster”?
- In section 4.2, the last paragraph, what is the “normal language” system trained without iterated learning?
- Results in section 4.3 demonstrate that different languages have different compositionality. Are there any results in linguistics that can verify this claim? Furthermore, the experiments show that Japanese has a negative topsim, is there any intuitive way to understand what this means?

### Soundness
4

### Presentation
4

### Contribution
3
