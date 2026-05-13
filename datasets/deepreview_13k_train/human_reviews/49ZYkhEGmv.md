# Scalabale AI Safety via Doubly-Efficient Debate

- Decision: Reject
- Scores: 6, 6, 8, 6

## Abstract
The emergence of pre-trained AI systems with powerful capabilities across a diverse and ever-increasing set of complex domains has raised  a critical challenge for AI safety as tasks can become too complicated for humans to judge directly.
 \citet{irving2018ai} proposed a debate method in this direction with the goal of pitting the power of such AI models against each other until 
the problem of identifying (mis)-alignment is broken down into a manageable subtask. While the promise of this approach is clear, the original framework was based on the assumption that the honest strategy
is able to simulate \textit{deterministic} AI systems for an \textit{exponential} number of steps, limiting its applicability. In this paper, we show how to address these challenges by designing a new set of debate protocols where the honest strategy can always succeed using a simulation of a \textit{polynomial} number of steps, whilst being able to verify the alignment of \textit{stochastic} AI systems, even when the dishonest strategy is allowed to use exponentially many simulation steps.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a doubly-efficient debate, where two polynomial-time provers compete to convince a significantly more efficient verifier that they have correctly solved a computational problem that depends on black-box access to human judgments.

### Strengths
See question part

### Weaknesses
This paper proposes two efficient-debate protocols for large language model debate. The paper is out of my research domain and it is hard for me to follow the paper. It would be appreciated if the authors could answer the question below.

1. Could authors give an example to show the difference between the proposed debate method and existing works such as Irving et al. (2018)? Why the proposed method could get a better bound intuitively?

2. How to implement the method in practice to help researchers to train an LLM?

### Questions
This paper proposes two efficient-debate protocols for large language model debate. The paper is out of my research domain and it is hard for me to follow the paper. It would be appreciated if the authors could answer the question below.

1. Could authors give an example to show the difference between the proposed debate method and existing works such as Irving et al. (2018)? Why the proposed method could get a better bound intuitively?

2. How to implement the method in practice to help researchers to train an LLM?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies interaction protocol for the debate framework introduced by Irving et al. 2018, focusing on computational complexity aspects. More specifically, the main motivation of this work is that the original framework assumes that the honest strategy can simulate AI systems for an exponential number of steps. The paper introduces new debate-based protocols, where this  dependence is polynomial.  Inspired by interactive proofs, the debate framework is modeled as a triple $(A, B, V)$, where $A$ and $B$ are provers and $V$ is a verifier, modeled as oracle Turing machines -- oracle models a human evaluator. The paper systematically studies the problem at hand, considering both deterministic and stochastic debate protocols. The results show that the proposed protocols are complete and sound, and that the prover that argues for the correct decision and the verifier run in a polynomial number of steps. Moreover, the number of oracles quires that the verifier requires is constant.

### Strengths
- The paper is well written and enjoyable to read. It introduces all the relevant content important for understanding the formal framework and the results. The practical examples provided throughout the main paper clearly motivate the protocols studied in this work, and are helpful for understanding technical details.  
- To my knowledge, these results are novel, and provide a different perspective on the debate framework. The protocols are relatively simple, but yield guarantees which appear to improve those from prior work. 
- The paper provides rigorous analysis of the protocols, proving that they are sound and complete, and show that the protocols are efficient in relevant parameters of the problem setting. The proofs appear to be relatively simple, and at the first glance, they seem correct.  
- These results would be of an interest to researchers working on alignment problems in AI, and could spark interesting discussions on the practicality of the debate based framework in large language models.

### Weaknesses
 - The paper primarily provides a theoretical treatment of the protocols it considers. Given that there is a concrete practical scenario that motivates these protocols, and since the protocols appear to be relatively simple, it seems that the authors could have conducted an experimental evaluation akin to the one in (Irving et al. 2018), but focusing on LLMs. Experiments that compare this work to prior debate-based approaches would be useful. 

- Although the work relaxes some requirements/assumption compared to prior work, more specifically (Irving et al. 2018), it doesn't fully address all the challenges related to utilizing the debate-framework in practice. For example, the protocols rely on a relative restrictive assumption that the oracle representing human judgment is correct/unbiased. That said, these limitations are clearly discussed in the conclusion section.

### Questions
I don't have specific clarification questions. However, it would be great if the authors could provide a discussion related to my comments about the weaknesses of their work. More specifically, some discussion on whether it would be possible to set up an experiment based on LLMs which showcases the utility of their framework.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript contributes to the 'scalable oversight' literature, presenting results for an environment in which two adversarial provers argue in favor of and against a result, for human review.

### Strengths
**originality**

The paper seems to make improvements to an existing literature.

**quality**

The work seems to be of good quality.

**clarity**

The paper is well written and clear.

**significance**

AI models are becoming larger and more capable, making AI safety an increasingly important topic.  It seems to me that this approach - adversarial provers and human oversight - is promising.

### Weaknesses
Caveat: I've given myself a low confidence score as this literature is not one that I know or have worked in.  Thus, I would have benefitted from a very simple running example through the paper.  I understand that space is tight, and expect that readers actually working in this area would benefit from that less than I would, so would certainly not make including one a strong recommendation.

My main concern about this approach is that it relies on unsound reasoners, overseen by an unsound human.  While I agree that, ultimately, there are turtles or elephants all the way down, we can choose how to position the elephants/turtles.  The autoformalization project (e.g. Jiang et al.'s Draft, Sketch, Prove) relies to a greater extent on sound reasoners.  While I think that each of these approaches has distinct strengths and weaknesses, I think that they should at least be compared.

Minor typos: 
1. "makes progress both" -> "makes progress on both"
1. "currently know for delegating" -> "currently known for delegating"
1. the final sentence on p.3 ("For a real number $p$...") is a fragment
1. "for it's correctness" -> "for its correctness"

### Questions
Can you present a simple example of a false proof that survives the protocol, because of inconsistencies or errors in the (human) oracle?  An ideal example, from my point of view, would display a subtle oracular error (e.g. a minor, buried assumption on real numbers) that spirals into a clearly false result.  Perhaps an easy way to do this would be to show the $(A, B)$ machines yielding both True and False, due to the oracle's replies.

The probabilities in Definition 3.2 stood out: are these merely illustrative (so that any result could be replaced by arbitrary constants  $a$ and $b$), or would even qualitative results derived be overturned by use of different fractions (e.g. are there critical values for these numbers)?

Definition 6.1: can you provide an example of an oracle that is not $K$-Lipschitz?

**FYI**

Not questions re: the reviewing of this paper, but the sort of questions I would ask if talking to the authors about the research more generally. 
 Thus, these do _not_ need to be answered here:
1. is the argumentation procedure in Dewatripont and Tirole's "Advocates" a special case of this framework in any way?  Their approach to efficiency is different from that taken here, but may be complementary?
1. the economic theory literature also contains models of 'cheap talk' and 'long cheap debate' (like a 'debate' in the current paper), in which two biased but informed advisors make comments to a decision maker, who tries to determine the true state of the world from their comments.  In the canonical version, the comments are intervals, rather than the present probabilities.
1. Foster & Vohra's chapter on calibration, in which a decision maker attempts to identify whether or not a purported expert has true expertise, by means of repeated questioning, also seems generally related.
1. Dung's abstract argumentation framework also came to mind, explicitly considering arguments and their attacks/refutations.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a model called the doubly-efficient debate. Here, two competing provers attempt to convince a verifier of a computation's correctness, relying on black-box judgements (like human feedback). This method ensures that any polynomial-time computation can be confirmed with just a few queries to the human judgment black-box. The model promises efficient verification, but it requires the AI models to produce comprehensive reasoning traces that can stand up to rigorous human analysis.

The researchers formalize a scenario where two AI models compete to convince a verifier, who can consult human judgment, of a solution's accuracy. The aim is to ensure the right solution is reached without excess computation and that human queries remain limited regardless of the complexity of the task. Protocols developed demonstrate success in various settings: deterministic human judgment, stochastic human judgment, and settings with witnesses.

### Strengths
The introduction of the "doubly-efficient debate" model is an innovative way to approach the challenge of training and oversight in AI, particularly for Large Language Models (LLMs). By pitting two models against each other to verify the correctness of their outputs, the paper seeks to streamline and make efficient the process of verification, which is a unique proposition.

The paper emphasizes real-world issues, such as the potential high-stakes consequences of language models used for drafting laws or contracts. This grounding in practical applications elevates its relevance and appeal to practitioners in the field.

The paper explores various scenarios, including deterministic and stochastic human judgment. This comprehensive approach ensures that the proposed models and protocols are tested under diverse conditions, enhancing their reliability.

### Weaknesses
The paper poses questions about how the model would deal with errors from the oracle, either due to incorrect judgments or stochastic nature. The mere existence of these questions signifies a lack of clarity or solution in the paper about handling such errors effectively.
Models where the oracle might make errors, either randomly or on a limited set of queries, introduce an element of unpredictability into the verification process. The paper does not seem to offer robust strategies to mitigate or address these potential errors.

Although the paper introduces a theoretical model, the practical implementation of such a model and its real-world viability are not deeply explored. The proposed model's scalability, robustness, and efficiency in real-world applications remain an open question.

### Questions
Could the authors clarify the connection between their protocols and the framework introduced in [1]?
[1] Du Y, Li S, Torralba A, et al. Improving Factuality and Reasoning in Language Models through Multiagent Debate[J]. arXiv preprint arXiv:2305.14325, 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
