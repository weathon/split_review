# The Good, the Bad and the Ugly: Watermarks, Transferable Attacks and Adversarial Defenses

- Decision: Reject
- Scores: 3, 5, 6, 6

## Abstract
We formalize and extend existing definitions of backdoor-based watermarks and adversarial defenses as *interactive protocols* between two players. The existence of these schemes is inherently tied to the learning tasks for which they are designed. Our main result shows that for *almost every* discriminative learning task, at least one of the two — a watermark or an adversarial defense — exists. The "*almost*" refers to the fact that we also identify a third, counterintuitive but necessary option, i.e., a scheme we call a *transferable attack*. By transferable attack, we refer to an efficient algorithm computing queries that look indistinguishable from the data distribution and fool *all* efficient defenders.

To this end, we prove the necessity of a transferable attack via a construction that uses a cryptographic tool called homomorphic encryption. Furthermore, we show that any task that satisfies our notion of a transferable attack implies a *cryptographic primitive*, thus requiring the underlying task to be computationally complex. These two facts imply an "*equivalence*" between the existence of transferable attacks and cryptography. Finally, we show that the class of tasks of bounded VC-dimension has an adversarial defense, and a subclass of them has a watermark.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates the relationship between watermarks (planted in trained ML models) and adversarial defenses for noiseless classification tasks over a finite set $\mathcal{X}$. For clarity, let us focus on *binary* classification tasks. Here, a learning task (or equivalently, full data distribution) can be represented by a pair $(D, f^*)$, where $D$ is the marginal distribution over $\mathcal{X}$ and $f^*: \mathcal{X} \to \\{0,1\\}$ is the true labeling function.

For any given learning task $(D, f^*)$, consider an interactive protocol in which Alice (ML service provider) interacts with Bob (client). As a service provider, Alice trains a classifier $f: \mathcal{X} \to \\{0,1\\}$ which achieves $\epsilon$-error on $D$, and sends it to Bob. However, Alice is motivated to secretly plant a “watermark” into her trained classifier $f: \mathcal{X} \to \\{0,1\\}$ by making it susceptible to pre-designed adversarial examples. Bob, on the other hand, is motivated to neutralize any backdoors in the classifier f he received from Alice.

The opposing objectives of Alice and Bob in this framework can be formulated as a *zero-sum two-player* game. Furthermore, by modeling Alice and Bob to be circuit classes of fixed size, the pure strategy space for both Alice and Bob become finite, with explicit bounds on their cardinalities. This setup allows previous results on approximate equilibria [Lipton and Young, 1994] to be applied. Using the zero-sum two-player game formulation, the authors show that any “efficiently learnable” classification task $(D, f^*)$ falls into at least one of the following three cases:

1. **Watermarking.** There exists a watermarking scheme for Alice can compute a classifier f and sequence of adversarial (randomized) queries $x_1, …, x_q$ such that for any circuit (”Bob”) whose size is significantly smaller than hers (i.e., y computed by any such small circuit incurs $\mathrm{err}(x, y) \ge 2\epsilon$) the watermark is *unremovable* and the distribution of her queries $x_1, …, x_q$ is indistinguishable from $D$.
2. **Adversarial Defense.** There exists a watermark neutralizing (i.e., adversarial defense) scheme for Bob such that either Alice’s queries $x_1,…,x_q$ are non-adversarial (the avg loss of $f$ on $x_1, …, x_q$ is $\epsilon$-small) or the distribution of Alice’s queries $x_1, …, x_q$ and $D^q$ are distinguishable by small circuits.
3. **Transfer Attack.** A third possibility not covered by the previous two cases, which has left me confused. Please refer to the Questions section for further details.

### Strengths
The paper attempts to formalize an intriguing relationship between two phenomena recently studied in machine learning: watermarking (i.e., planting undetectable backdoors [Goldwasser et al., 2022]) and adversarial defense [Cohen et al., 2019]. A watermark for a classifier attempts to hide specific signatures in its error patterns, while an adversarial defense attempts to maintain performance of a given untrusted classifier f across distributions that are “close to” D, which can be formalized via a weakened notion of statistical distance. Intuitively, there is tension between these two objectives, which the authors attempt to formalize as a zero sum game. Addressing these natural questions would be of wide interest to the ML community.

### Weaknesses
The main weakness of this paper lies in the **lack of clarity and precision in its definitions and framework**, which significantly undermine the credibility of any theorems that follow. The presentation of key definitions and interactive protocols are “hand-wavy”, leaving substantial ambiguity in how the results should be interpreted and applied. This vagueness makes it difficult to assess the validity of the theoretical claims and fully appreciate the significance of the results.

While the authors give more formal specifications in the Appendix (especially, Appendix B), significant gaps still remain to be filled. In addition, the appendix should provide further technical details after the basic setup and key insights have been presented in the main text, rather than serving as a teaser for readers left confused by the unclear presentation in the body of the work. 

One significant issue is that the modeling of Alice and Bob with size-bounded circuit classes seems to fail a basic type check. In the interactive protocols, Alice and Bob face different tasks that involve different input and output spaces. For instance, in a watermarking scheme for binary classification, Alice is expected to output a representation of a classifier $f: \mathcal{X} \to \{0,1\}$ along with queries $ x_1,\ldots,x_q \in \mathcal{X}$ (a separate issue here is Alice's inputs are not specified and the dependence on the input domain’s cardinality doesn't appear anywhere in the quantitative results, which raises concerns). On the other hand, Bob’s inputs are sequences $x_1, \ldots, x_q$ and needs to output $y \in \{0,1\}^q$. Without further clarification, it’s unclear how a size $s$ circuit for Alice compares to a size $s$ circuit for Bob since even the input and output domains do not match. This is one of several issues with the paper's framework that, collectively, call into question the overall rigor and applicability of the approach. Please refer to the **Questions** section for additional issues.

Moreover, the paper **incorrectly applies previous results from cryptography**, which indicates a lack of understanding of the field. In particular, the interpretation of the results based on [Goldreich, 1990] in Section 5.2 is incorrect. Goldreich’s result applies to an *ensemble* of random variables, i.e., a *sequence* of distributions, whereas the EFID pairs the authors define in Section 5.2.1 are particular instances of distributions. Moreover, the ensembles used by Goldreich are *uniformly constructible*, meaning that there exists a single Turing machine generating random samples from X_n given the input 1^n. This contrasts with the non-uniform circuits used in this work. Given this misunderstanding, the title of Section 5,  *Transferable Attacks are “Equivalent” to Cryptography* is misleading and unnecessarily provocative. Even if Goldreich’s equivalence result could be applied here (which I find unlikely), the only concrete implication for cryptography is the existence of pseudorandom generators (PRGs), which are basic cryptographic primitives but do not represent the entire research field.

In addition, the restriction to succinct circuits feels somewhat ad hoc, seemingly added specifically to prevent Alice and Bob from hardcoding outputs. It seems likely that the approximate equilibria results (Theorem 1) would still hold without the succinctness assumption, albeit with different bounds, as the key requirement is simply that the pure strategy space remains finite with explicitly known bounds on its cardinality. This raises concerns about the integrity of the formulation, with the succinctness restriction serving more as a workaround than an integral component of the setup.

Overall, the paper would benefit greatly from prioritizing clarity over excessive generality, focusing on straightforward, concrete setups and presenting mathematical results clearly and precisely, without the informal remarks.

**Editorial comments**
- (Abstract) The phrase "almost every" learning task is misleading. Terms like “almost every” carry strong connotations in measure theory. The mere fact that a mathematical object is “irregular” or "very complex" does not imply that it is rare (e.g., from a measure-theoretic perspective). For instance, with respect to the uniform measure on [0,1], “almost every” real number in the unit interval is uncomputable.
- (Line 214) Advantage should be an equal sign.
- (Line 243) The unremovability condition, as stated, is clearly incorrect. Bob can simply respond with random y and the realized error can be 0 with small but non-zero probability. Even if this is intended as an informal simplification of the definitions in Appendix B, it should not be so obviously wrong.
- (Line 248) The term "defender" is used inconsistently alongside other terms like "player", "prover", and "Bob". It would be better to choose a single term for the recurring entities and use it consistently throughout the paper.

### Questions
Many issues appear to stem from portraying Alice (and Bob) in an “active” or “anthropomorphic” manner, as if she dynamically performs tasks, which is inconsistent with the static nature of non-adaptive computation models like circuits. Circuits compute a fixed function based purely on their inputs.

**Formal specification of Alice and Bob**
1. What mathematical objects represent Alice and Bob? If they are fixed-size circuits, then what is the input and output space of these circuits? How are the input spaces structured, and how are random source bits, which are necessary for a circuit to output a random variable, represented within these spaces? Do they count towards the size of the circuit?
2. Circuits themselves are not formally defined anywhere in the text, so it’s unclear what the authors mean by a “size $s$ circuit” in mathematically. The closest reference is [Appendix B, Definition 4] which defines "succinct circuits" but leaves "width" and "depth" undefined. For instance, what would be the width and depth of a circuit shaped like a pyramid? In addition, are input gates counted as part of the circuit size?

**Specification of the interactive protocol (Section 3.2)**
1. How does the interactive protocol proceed? Does Alice send $(f, x_1,…, x_q)$ to Bob in a single round? Are there multiple rounds?
2. If there are no assumptions on the hypothesis class, how does Alice represent her classifier $f: \mathcal{X} \to \\{0,1\\}$? The only reasonable choice in the absence of structural assumptions on the labeling function seems to be the truth table, i.e., an element of $\\{0,1\\}^{\mathcal{X}}$.
3. It seems weird to compare Alice’s budget $T_A$ and Bob’s budget $T_B$. Within the protocol, they have different inputs and different outputs. Alice must output $(f, x_1, …, x_q)$ which could be potentially much longer than Bob’s $q$ bits to represent $(y_1,…,y_q)$.
4. In the *Transfer Attack* setting, what access does Bob have to the learning task $(D, f^*)$? Figure 4 suggests that Bob is only provided with Alice’s queries. Is it reasonable to expect Bob to achieve low error on Alice’s queries without any access to the labeling function? Moreover, what is the significance of this setup if Bob is not given any information about the learning task itself?

**Other confusions**
1. In [Section 4] (also [Appendix C, Theorem 5]), what is meant by a “learning task $(D, f^*)$ is learned by a circuit up to error $\epsilon$”? How does a circuit solve a learning task? What are its inputs? What is the output? How is the output represented? What kind of “access” does a circuit have to the learning task $(D, f^*)$?

2. If $\mathcal{X} = [N]$, where $N=2^{100}$, $D$ is uniform over $[N]$, $f^* = 1$ everywhere, then what case does the learning task $(D, f^*)$ fall into? If the circuit class size bound for both Alice and Bob are small, say less than $10$, then Alice cannot even write down a description of a single sample from $\mathcal{X}$, which makes the *Watermark* and *Adversarial Defense* schemes ill-defined. On the other hand, the learning task is technically "learnable" since a constant circuit that is not connected to any input gates and outputs $1$ realizes $f^*$.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper explores the relationship between backdoor-based watermarks and adversarial defenses in machine learning.  These concepts are formalized as interactive protocols between two players and proved that for almost every discriminative learning task, at least one of the two exists. The main contribution is the identification of a third, counterintuitive option: a transferable attack.  This term describes an algorithm capable of generating queries that are indistinguishable from the data distribution, yet can deceive even the most effective defenses.  The authors demonstrated the necessity of a transferable attack using homomorphic encryption and proved that any task susceptible to such an attack implies a cryptographic primitive.

### Strengths
- Formalization of the relationship between backdoor-based watermarks and adversarial defenses is useful.

### Weaknesses
 - I take umbrage with the following claim: “Along the way to proving the main result, we identify a potential reason why this fact was not discovered earlier.”. There are multiple prior works that have investigated the trade-off between adversarial robustness and backdoors/watermarks [Weng et al,  Sun et al, Gao et al, Niu et al., Fowl et al., related work in Tao et al. is a good summary]. Although most of these papers are more empirical, this paper completely ignores an entire line of work. The paper primarily focuses on theoretical results without providing clear guidance on how these results can be translated into practical applications, and I find it difficult to assess if this paper is saying anything profound beyond what has already been discussed in the referenced papers. This is my main concern. Some suggestions:
    * (1) Include a detailed discussion of how their theoretical results relate to or extend the empirical findings in the papers you cited.
    * (2) Explicitly state what novel insights their work provides beyond the existing literature.
    * (3) Add a section on potential practical applications or implications of their theoretical results.

- In Definition 2.3. Why is the coefficient before epsilon, 7?

- The paper primarily deals with discriminative learning tasks, like classification. These tasks assume a clear relationship between input data (e.g., images) and distinct output labels (e.g., "cat" or "dog").  How can the trade-offs be captured for generative models?

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors provably identify the following trichotomy - for every learnable task there is an adversarial defence and/or a watermarking scheme, while for learning tasks which have associated cryptographic hardness results, there is a transferable attack.

### Strengths
The most important contribution of this manuscript is the proof that the notions adversarial robustness and watermarking schemes is complementary to the notion of cryptographically hard learning schemes. The authors use a lot of existing results across various fields creatively, to arrive at this result, which makes the technical part of the paper interesting in its own right.

### Weaknesses
My main concern with the paper is that the definitions (especially the two player games) is too carefully constructed to be readily used in conjunction with existing results from game theory, cryptography, and learning theory. There is lack of justification / discussion on several fronts, which should be addressed for the paper to be useful to the community at large.

A secondary but related weakness is the lack of a technical discussion section. A detailed overview of proof techniques section is much required. I have detailed a list of my questions in the next section.

A better related works section is also warranted. For example, there are certain confusions arising in the discussion containing the comparison with the Christiano et al. (2024) paper. See the questions section.

*Note to the authors:* Regardless of the acceptance results at this conference, I believe the authors should prepare a longer version of this manuscript and submit it to a journal like TMLR. It would be of immense value to the community.


--------
After the rebuttal period, I have decided to raise my score to indicate my positive opinion of the paper. 

*Note:* At this point I cannot justify raising the score any higher due to numerous missing definitions and discussions (detailed in the reviews by myself and other reviewers, and mostly agreed upon by the authors) that should have been included in a theoretical paper in the first place.

### Questions
# Main points to be addressed

1. In section 3.1 (line 202), why do we need to define $\perp$, given the fact that $x\sim D$ and $\text{dom}(h)=\text{supp}(D)$? It seems to me that we are never really using the fact (at least in the vicinity of said definition) that $h$ is a partial function? This is causing unneeded confusion at this point. This subtlety can be separately introduced in appendix F and H, where it is actually required.


2. The definition of indistinguishability which forms a cornerstone of most of the concepts in this paper is both _informal_ and _incomplete_.  The authors define the distinguishing game, but abruptly end the definition with $\text{Pr}\left[A\text{ wins}\right]$. 
     - More concretely, the authors should explicitly state what the probability in line 215 is over, and connect the winning probability to the distinguishing game?


3. In definitions 5,6, and 7, it seems to be a straightforward requirement that $t<T$. The authors should include this in the paper.

4. Line 150 onwards: I request the authors for certain clarifications:
   - "_A major difference between our work and that of Christiano et al. (2024), is that in their approach, the attacker chooses the distribution, whereas we keep the distribution fixed._" Does this not imply that the related work proves a *stronger result*? (Note: this does not influence my score. I simply wish to understand this point in some more detail.)

   - "_A second major difference is that our main result holds for all learning tasks, while the contributions of Christiano et al. (2024) hold for restricted classes only._" Earlier, it was stated that the related work "_show(s) an equivalence between their notion of defendability (in a computationally unbounded setting) and PAC learnability._" So what do the authors mean by *restricted classes* in the work of Christiano et al. (2024)?

5. The notions of zero-sum games and Nash equilibria are absent from the main paper. This makes the proof sketch of Theorem 1 highly unreadable without jumping back and forth from appendix C, which defeats the whole purpose of having a simplified main theorem and a proof sketch in the first place.
   - Why do we need to restrict ourselves to zero-sum games instead of focusing on more general interactive protocols? Is it simply because the proof framework demands a certain kind of assumption? In this case, such a setup should be clearly mentioned as an assumption (which is still fine). 
   - The authors should also address why they have only considered Nash equilibria instead of in their setup, if not for other reasons, for the sake pedagogy alone.

6. Succinctly representable circuits are not well-motivated in Appendix C. One the referenced papers uses the notion of Stackelberg equilibrium which is different from Nash equilibrium used in this paper. There needs to be a longer/better discussion on this point.

7. It seems to be that FHE is superfluous in the proof of Theorem 2. Any reasonable encryption task seems to suffice for the purposes of the proof. 
   - On this note, I have the following question for the authors: Consider the Learning with Errors problem (Regev, 2005), where the learner has to figure out if samples are drawn from the LWE distribution or the uniform distribution. The adversary in LWE can be taken as Alice, while the learner, i.e., Bob has to figure out if the samples were drawn from uniform or the LWE distribution.

## Typos
  - Line 1599: "For instance in ? the existence of PRGs secure against time and space bounded adversaries was considered." *Missing reference*.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper gives formal definitions of “watermarks” through backdoor (not for LLM’s output, but rather for models themselves) and “adversarial robustness” and “transferable attacks” in their own way. Meaning that the definitions do not necessarily match what is the common usual way of defining them, but the definitions make sense in their own way.

Then, the paper observes that these three notions are complementary for a “learning task”. A task is modeled using a distribution D (on instances) and a function h (to label them) and differs from the method of using a family of h (as hypothesis class). In particular, the paper shows that for each learning task, at least one of the following holds: either we can watermark models that predict that task, or that we can resist backdoor, or that transferability attacks work.

Intuitively, the main result is proved by observing that a watermark through a backdoor aims to plant a backdoor and later use specific queries to detect it (using wrong answer) and this is exactly what a defense against backdoor wants to avoid. So the two notions are rather complementary. Once the paper aims to prove this formally, they show that a third case is also possible, which in their formalism is referred to as the transferability attack.

The paper then shows that “transferability” attacks could probably exist assuming fully homomorphic encryption, and that transferability attacks *require* one-way functions (they say PRG, but that is the same as OWFs), and hence it implies secret key crypto.

Finally, the paper claims that PAC learnable families (ie., those with bounded VC dimension) always can have adversarial robustness and “watermark against fast adversaries”.

### Strengths
A formalism of the intuition behind the duality of watermarks (for models through backdoor) and adversarial robustness is interesting. 

Also, the paper realizes that formal definitions are needed for such results and takes an effort in that direction.

### Weaknesses
The new formalisms for the 3 notions of watermark, robustness and transferability need a lot more scrutiny and discussion. For example, there are limits on the time of the adversary that are needed to make these definitions non-vacuous, but these definitions are different from previously established definitions in this regard (e.g., about adversarial examples) and I see no real effort to compare them. (see my question below)

Also, due to the number of results in the main body, their proofs are deferred to the appendix, and perhaps the most exciting result (saying that bounded VC dimension means we can have adversarial robustness) is pushed to the appendix.

### Questions
Regarding the differences in definitions (for adversarially robust learning): please provide a detailed comparison between your time-limited adversary definitions and established definitions in adversarial examples literature, and highlight the key differences and justify your choices.

Related to the question above: are you claiming that any PAC learnable problem has adversarially robust learners? This seems to be a very important and technical problem, e.g., see:
https://proceedings.mlr.press/v99/montasser19a/montasser19a.pdf
https://arxiv.org/pdf/1806.01471
I guess the devil is in the details and differences in definitions, but that needs to be much more openly discussed.

Having a comparison of the definitions (yours and previous literature on adversarial examples and adversarially robust learning) partially addresses this issue, but please also make an explicit comparison with the results of the papers above (particularly, the impossibility result of the first paper and how it does not contradict yours).

### Soundness
3

### Presentation
3

### Contribution
3
