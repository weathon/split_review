# Lewis's Signaling Game as beta-VAE For Natural Word Lengths and Segments

- Decision: Accept
- Avg Score: 6.00
- Scores: 3, 8, 8, 5

## Abstract
As a sub-discipline of evolutionary and computational linguistics, emergent communication (EC) studies communication protocols, called emergent languages, arising in simulations where agents communicate.
A key goal of EC is to give rise to languages that share statistical properties with natural languages.
In this paper, we reinterpret Lewis's signaling game, a frequently used setting in EC, as beta-VAE and reformulate its objective function as ELBO.
Consequently, we clarify the existence of prior distributions of emergent languages and show that the choice of the priors can influence their statistical properties.
Specifically, we address the properties of word lengths and segmentation, known as Zipf's law of abbreviation (ZLA) and Harris's articulation scheme (HAS), respectively.
It has been reported that the emergent languages do not follow them when using the conventional objective.
We experimentally demonstrate that by selecting an appropriate prior distribution, more natural segments emerge, while suggesting that the conventional one prevents the languages from following ZLA and HAS.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper attempts to reframe the conventional Lewis's signaling game within the context of beta-VAE and ELBO, with a focus on the impact of prior distributions on emergent languages. The authors argue that selecting appropriate prior distributions can lead to the emergence of more natural language segments, while the conventional prior may hinder adherence to linguistic properties like Zipf's law of abbreviation (ZLA) and Harris's articulation scheme (HAS).

The weak points of this paper include:
(1) The paper is hard to read. The theoretical section includes symbols and equations without full explanation.
(2) The experiments are weak. The compared methods lack descriptions, and the performance improvement is not well explained.
(3) The studied problem lacks of enough audience.

### Strengths
1. The author well introduces the problem, which is well motivated.
2. The authors provide a deteailed proof in supplementary material.

### Weaknesses
 (1) The paper is hard to read. The theoretical section includes symbols and equations without full explanation.
(2) The experiments are weak. The compared methods lack descriptions, and the performance improvement is not well explained.
(3) The studied problem lacks of enough audience.

### Questions
I suggest the authors address my concerns mentioned in Weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new perspective on Lewis’s signaling game as beta-VAE and reformulates the game’s objective as ELBO. Based on this modification, it analyzes the influence of the implicit prior function on the properties of word lengths and segmentation of the emergent languages. It also shows that a learned prior distribution of the emergent languages can help evolve a language following Zipf’s law and Harris’s articulation scheme while the previous conventional objectives do not encourage meaningful segments.

### Strengths
1. The originality of this paper is good. The authors propose a generative point of view of the signaling game and analyze the possible causing factors of the current problems of the emerging less meaningful linguistic properties using the conventional objectives. This can provide a fresh study framework for emergent communication. The rigorous formalization and mathematical equations can integrate previous designs of regularizers and help with future objective design, offering a valuable contribution to the field.

2. The quality of the experiments and analysis is good. They compare different baselines controlling different priors of the objectives. The properties of word lengths, segments, and compositionality are carefully checked. 

3. This paper is of good clarity. It is easy to follow the argument of this paper.

### Weaknesses
No obvious weaknesses.

### Questions
Based on the current formulation, it seems that the distractors on the receiver’s side are not considered. How would you incorporate the context of the distractors and their corresponding influences [1,2] into the prior design? 

[1] Lazaridou, Angeliki, Alexander Peysakhovich, and Marco Baroni. "Multi-agent cooperation and the emergence of (natural) language." arXiv preprint arXiv:1612.07182 (2016).

[2] Evtimova, Katrina, et al. "Emergent communication in a multi-modal, multi-step referential game." arXiv preprint arXiv:1705.10369 (2017).

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper reanalyzes an emergent communication-signalling game in terms of
a VAE.  Within this analysis, the optimization of a signalling game is using an
"implicit prior" which leads to statistical properties of the emerging language
which do not match human languages.  Introducing linguistically-inspired priors
into signalling game by way of the VAE framework improves the resulting
emergent languages' statistical properties (i.e., adhering Zipf's Law of
Abbreviation and Harris's Articulation Scheme more closely).

### Strengths
- (major) The paper aims at re-analyzing a common EC setting in a more
  formalized way, yielding the potential for theoretical insights that would
  not otherwise be possible.
- (major) Furthermore, I think this analysis is largely in the correct
  direction with analyzing the signalling game as a VAE, looking at inductive
  biases, and tying in linguistic concepts like Zipf's Law of Abbreviation and
  Harris's Articulation Scheme (although this wide scope is also a bit of
  concern; cf. "Weaknesses").
- (minor) The experiments partially satisfy HAS which is known to hold for
  human languages.

### Weaknesses
 - (major) A critical part of the paper is the "prior" within a VAE or
  signalling game, but I did not get a concrete sense of what this prior
  actually is in the context of a signalling game with neural network-based
  agents (I expand on this in "Questions").  As a result, it makes me unsure
  how well the theoretical claims actually apply to a real setup.
- (major) The paper, I think, tried to do too much, and ends up not spending
  enough time on the core claims, namely, the signalling game can be
  re-analyzed as a VAE.  I think the paper would benefit greatly from cutting
  away all but the essential claims and going through those more slowly and
  thoroughly.
    - For example, this shows up in the experiments which seem more concerned
      with evaluating the existence of ZLA/HAS in the newly proposed setting
      rather than establishing empirically that the signalling game behaves
      like a VAE.
- (minor) The notation and the proofs are not very clear, and it made it
  slow/difficult to work through the equations.

### Questions
- What exactly is the "prior" in the emergent language game?  I understand that
  it is implicit, but does that mean that is embedded in the objective function
  (i.e., the $D_\text{KL}$ term is constant)?  Or is it instead the case that
  the sender's architectural biases represent the prior?
- In addition to the theoretical analysis, what else can the authors point to
  to support the claim that an EC signalling game is analogous to a VAE?


### Other comments

- If the authors are assuming a REINFORCE objective for the signalling game,
  that should be mentioned earlier than Sec 4.1.
- What is $A_t$ in Eq 3?
- In Sec 2.2, I do not think the section compositionality is relevant or
  important; it should removed, in that case.
- Before Eq 5, what is $\mathcal A^*$?  Is it supposed to be a Kleene star?
- What exactly is the uniform prior?  Is it just a constant probability mass
  over every possible sequence?  If so, how do we know that is the "implicit
  prior" and not something like a uniform _unigram_ prior instead, for example.


- Sec 3.1: It is not clear to me how (9) is derived from (2).  I looked at Section
  B.1, but it was very unclear what was happening because rather than starting
  with (2) and going to (9), it talks about "transforming" different sides of
  the equation.
  - It would also be helpful to give an indication of what from Schulman et al.
    (2015) is being applied (i.e., the what the "stochastic computation
    approach" is).
  - As a result, I'm not convinced that the reconstruction game, absent
    modifications to the traditional object (e.g., length penalty), assumes
    a uniform prior of messages.
  - It seems like the $P(m) = \mathbb E_{x\sim{}P_\text{obj}}[S(m|x)]$ should be the
    prior over messages.  I very well might be misunderstanding something here
    due to terminology.  Am I conflating here that "prior" as the distribution
    of messages the receiver produces given the distribution over inputs with
    "prior" in the sense of our objective function which we are optimizing
    against (in which case "prior" does not refer to anything concrete in the
    EC environment but rather only to the optimization process by analogy to
    a VAE's optimization)?
- Sec 3.2: what is a "heuristic variant of [a] VAE"?
- Sec 3.4:
  - The very first paragraph of this section, I think, is glossing over
    critical question in the paper: what is the connection between the "prior"
    and the actual EC setup.  I understand that the EC setup is analogous to
    a VAE, but what exactly is the analog of the VAE's prior?
  - I think the use of "approximately" is dangerous when trying to make
    theoretical claims; I understand that it is unavoidable in something as
    messy as EC, but it still needs to be accompanied by some justification in
    order to keep the theoretical claims strong.


### Minor notes

- "they are not" reproduced emergent lanuaguages   has awkward phrasing
- Right after Eq. (1), it should be $\log(|\mathcal A| - 1)\ge0$ in the case
  that $|\mathcal A| = 2$.
- Sec 3.3:
  - what is $\mathcal M$ -- the set of all messages? 
  - What is $\mathcal A$, again?
  - Eq 15 limit notation here would be more appropriate

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors discuss connections between classic emergent communication in Lewis signalling games and Beta-VAEs.

In some traditional EC works, a speaker and listener must coordinate such that the listener can reconstruction a speaker's "target" observation, given communication. In many ways, this mirrors classic reconstruction training. Prior works have often found that the resulting communication from such training is often "unhumanlike" in several ways, including ZLA and HAS metrics. This work argues that such undesireable properties are likely a result of implicit priors that most EC works encode. 

By connecting EC to Beta-VAE methods, the authors uncover theoretical interpretations of different terms in EC and open up the important directions for experiments (such as varying prior distributions or Beta).

In experiments, the authors show that, by using a learnable prior in training agents, they appear to achieve greater separation of EC into "word-like" units.

### Strengths
## Originality
I'm am somewhat torn about the originality of this work. On the one hand, I think connection EC literature to other theoretically-rich approaches like beta-VAE is a very good idea. On the other hand, the authors note that some prior literature appears to have considered a generalization of this problem ("Section 6: Tucker et al. defined a communication game... based on VIB, which is known as a generalization of beta-VAE."), which makes me think this work is not proposing novel ideas.

## Quality
Overall, the work seems quite careful and sound in discussing the mathematical underpinnings of many EC methods.

## Clarity
Some aspects of this paper were quite clear (in particular, the introduction and conclusion are very good), but I found other aspects harder to read. I suspect this is somewhat due to having a fair amount of notation is not immediately interpretable without remembering definitions from earlier pages (e.g., "monkey typing model" or n_bou).

## Significance
I think this work falls within an important (and significant) field of connecting EC to other training methods and objects. I remain somewhat confused about the relationship to prior art, however, so I am unsure of the significance of this individual work.

### Weaknesses
Overall, I like aspects of this work, but there are a few important unresolved questions or weaknesses that I would want to see addressed before accepting, in particular about relations to prior art.

## Relation to prior art
The authors do a good job noting related prior literature, but I remain somewhat confused by the position of this paper relative to such literature. In particular, the authors write that:

> Moreover, Resnick et al. (2020) explicitly formulated the objective as ELBO, though it is not directly applicable to this paper...

> Tucker et al. (2022) defined a communication game called VQ-VIB, based on Variational Information Bottleneck (VIB, Alemi et al., 2017) which is known as a generalization of beta-VAE. Also, Chaabouni et al. (2021) formalized a color naming game with a similar motivation.

If prior art has used the same formulation and considered a generalization of the problem this paper is considering, what are the contributions of this paper? Honestly, I suspect there are many unique contributions made in this paper, but the contrast relative to prior art should be made much more obvious. Even just adding a sentence at the end of each related works section saying, e.g., "While Tucker et al., Alemi et al., and Chaabouni et al. consider similar frameworks to us, we introduce novel metrics and results" or something to that effect would help a lot. Ideally, the authors would run experiments comparing to Resnick's method.

## Presentation of results
I found the results somewhat difficult to read. Figure 2 contains the main results, and with enough flipping between pages, I could eventually figure out how to interpret them, but generally I encourage authors to make figures more self-contained. For example, listing a baseline as BL1 is not as informative as using a name/label that actually describes characteristics of the baseline (e.g., conventional + entropy).

## Why did segments become more meaningful.

The analysis in this section, while addressing a very important question, is slightly unsatisfying. First, parts of the writing are very casual (e.g., The receiver must be surprised several times..." ), whereas in reality the receiver just needs to receive, over multiple timesteps, enough bits to reconstruct the input. It is unclear what it means to "be surprised" as a binary term.

Second, I question the fundamental conclusion of this paragraph. The authors appear to suggest that the competing terms for entropy and reconstruction are what give rise to word boundaries. In other words, communication wants to often be predictable (because of the entropy term), which creates word-like clumps. However, as the authors note, the speaker needs to communicate some information in at least some timesteps to convey the meaning to the listener. Is there any mathematical basis, given the training terms used, for why that information should be concentrated in just a few timesteps (which would match word-like clumps) as opposed to evenly distributed across time? For example, in a simple four-timestep case conveying 4 bits, is there any advantage (as measured by decreased loss) to transmitting [2 bits, 0 bits, 2 bits, 0 bits] vs. [1 bit, 1 bit, 1 bit, 1 bit]?

## Minor:
Appendix D would greatly benefit from a little bit more text explaining what the graphs present. There are also some sentences that need editing (e.g., "threshold is set to 0.25.")

### Questions
1. In the Weaknesses section, I raised questions about why an entropy term would actually increase word segmentation. To repeat it here: is there any mathematical reason that the losses used during training should concentrate surprisal in just a few timesteps (which would induce word-like clumps) instead of spreading the surprisal loss more evenly across time?

2. I struggled to understand Figure 5. What is it depicting? What do the legend entries/different lines correspond to?

3. Just a clarifying question about the results for Criterion C3: the authors' proposed method is worse than baselines, correct? I recognize that topsim values for the proposed method improved generally, but for the narrow metric of the difference between topsim values, there is a decrease, right?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
