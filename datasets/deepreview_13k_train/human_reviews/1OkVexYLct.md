# Revisiting the Othello World Model Hypothesis

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
\citet{li2023emergent} used the Othello board game as a test case for the ability of GPT-2 to induce world models, and were followed up by \citet{nanda-etal-2023-emergent}. We briefly discuss the original experiments, expanding them to include more language models with more comprehensive probing. Specifically, we analyze sequences of Othello board states and train the model to predict the next move based on previous moves. We evaluate seven language models (GPT-2, T5, Bart, Flan-T5, Mistral, LLaMA-2, and Qwen2.5) on the Othello task and conclude that these models not only learn to play Othello, but also induce the Othello board layout. We find that all models achieve up to 99% accuracy in unsupervised grounding and exhibit high similarity in the board features they learned. This provides considerably stronger evidence for the Othello World Model Hypothesis than previous works.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, authors evaluate the Othello World Model hypothesis using different types of language models. This study is based on the previous works Li et al. (2023) and Nanda et al. (2023). The goal of this study is to reevaluate the hypothesis over multiple language models and see common representations they learnt.

### Strengths
This work is based on previous studies on Othello World Model Hypothesis. It's an interesting study because it tries to see if language models can model the rules of the Othello game from a large amount of transcripts data. Although the hypothesis has been probed in the previous studies, authors propose to reevaluate the hypothesis with more language models and different settings.

From the reevaluation, authors provide more evidence on the hypothesis and try to provide cross-language model latent representation on the Othello World model.

As a result, the paper could support the previous work's claims with new evidence.

### Weaknesses
The weak point of this study is to see the contribution claimed by authors as an important new contribution or extension of the previous work's claims. Although the authors tried to use multiple language models to see the difference of the modeling capability, it's not a new problem formulation because it's based on the previous works.

It's unclear why two-hop move generation is introduced as a new benchmark problem. Authors need to explain how two-hop generation provides insights beyond one-hop prediction, or to discuss potential limitations of the one-hop approach.

### Questions
* Why is the two-hop move generation an important benchmark in the Othello World Modeling?
* Could you please provide detailed analysis on the difference of each language model on the Othello world modeling? Why do they show different behaviors on the task?
* Please discuss potential implications for particular fields or research areas that might benefit from insights into how language models learn structured world representations.
* What is the reason to revisit this hypothesis using more language models and comprehensive probings? Is the previous work not enough to show the hypothesis's validity?
*Please discuss specific types of problems or domains where your approach might be applicable, and what challenges you anticipate in extending beyond Othello.
* Could you show that the Othello world model encodes the rules of Othello (to determine the validity of moves) or strategy of game playing?

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
This paper aims to add additional evidence to the Othello World Model Hypothesis by training a variety of different LLMs for predictive tasks in the game of Othello.

### Strengths
Highly topical area of research, and I think the experiments are carried out well.

### Weaknesses
## Review

### summary:
 This paper aims to add additional evidence to the Othello World Model Hypothesis by training a variety of different LLMs for predictive tasks in the game of Othello.

### soundness:
 2

### presentation:
 1

### contribution:
 2

### strengths:
 Highly topical area of research, and I think the experiments are carried out well.

### weaknesses:
 Under strengths above, I wrote that I **think** experiments are carried out well. Here is my main issue with the paper: many crucial details are not described in sufficient detail, and/or are too vague. I can make reasonable guesses as to the exact work that was done, and based on this, I do genuinely believe there is good work in here. But I shouldn't have to guess, and this state is not acceptable for a research paper.

I will elaborate on some specific points:
1. The entire paper revolves around the hypothesis that LLMs trained on Othello move sequences can induce a "relevant world model". But... I'm missing a definition of world model. I cannot judge with full certainty whether the experiments adequately support the claims, when I don't even have a crisp, clear, unambiguous definition of the hypothesis that the entire paper revolves around. I understand that "world model" is a relatively common phrase, but it is still crucial to define it clearly and unabmiguously.
2. The paper does not make it clear exactly what the models are trained to do. Combined with the lacking definition of world model above, this makes things very problematic. It is not clear to me whether the models are trained to:

    - Given current state (implied by sequence of previous moves), predict what the next played move is / should be.
    - Given current state (implied by sequence of previous moves) and a next move, predict what the next state will be.
    - A combination of the above, or anything else.

The caption of Figure 1 talks about "predict the next move". The caption of Table 1 is talking about "game state generation". These two are two very different things. Much of the rest of the paper talks about "move generation", which could be predicting next move again, but could also be about predicting which moves are legal, for instance.

3. There are no details whatsoever on how the SYNTHETIC dataset was generated. Which agents were used to play these games? This requires complete details on these agents (what algorithms, how much search time if they used search, on what hardware, any kind of randomisation used to ensure variety in the data, ... we need to know everything, but now we know nothing at all).

Other comments:
- Section 2 says that the work of Takizawa (2024) also looked at "whether LLMs adopt similar ones [strategies]", but as far as I can see, they did not do anything even remotely like that at all.
- line 159 PLMs should be LLMs?
- Section 3.2 refers to Tables 2 and 3, but this should be 1 and 2?
- Caption of Figure 2 vaguely mentions "performance". This is not precise enough (could be accuracy, could be error rate, would lead to very different interpretations). There's also no label on the y-axis, which also does not help in this regard.
- Line 263/264 talks about performance plateauing, but I don't see it as plateauing at all. Therefore, I also disagree with much of the analysis in the rest of the bottom of page 5. Sure, the decline in error rate becomes less steep at the end for the non-pretrained models. But they didn't fully plateau yet, and are **still** outperforming the Pretrained models **also at the very end of your x-axis**. These observations disagree with much of your conclusions here.
- Line 462/463 mentions "the policy of the game". There is no such thing as a "the policy" of any game. We can play according to many different policies.

### questions:
 1. Please define world model.
2. Please describe very precisely what the models are actually trained to do.
3. Please provide details on how the SYNTHETIC dataset was generated exactly.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 3

### confidence:
 4

### code_of_conduct:
 Yes

### Questions
1. Please define world model.
2. Please describe very precisely what the models are actually trained to do.
3. Please provide details on how the SYNTHETIC dataset was generated exactly.

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
4

### Summary
In 2023 Li et al. (and subsequently Nanda et al. (2023)) formulated the Othello World Model Hypothesis (OWRH), claiming that GPT-2, based purely on Othello move sequence analysis, was able to infer the principles of the game, including its 64-square board representation. This paper revisits OWRH with 6 Large Language Models (LLMs) and enhanced research protocol, providing stronger evidence supporting the hypothesis than the two above-cited articles.

### Strengths
1) The paper is clearly written and easy to follow.
2) The experiments are well-thought and lead to several new insights.
3) The topic should be of interest to some of the ICLR community.

### Weaknesses
1) The novelty of the paper is limited. The underlying research concept of verifying the OWMH is not new and even though the paper leads to certain new observations, they are not surprising and do not significantly expand the existing knowledge.
2) The selection of LLMs is somewhat outdated, since there are quite a few stronger LLMs available these days.
3) In the era of MLLMs (Multimodal LLMs) the rationale behind the proposed research is disputable.

### Questions
1) What qualitatively new observations related to the internal representation of Othello games in LLMs result from the presented study? What are the high-level novel implications of the presented experiments and conclusions?
2) Why this particular set of models has been selected? There are quite a few newer models available at the moment, both proprietary and open access.
3) How the presented study relates to the representation abilities of MLLMs?

### Soundness
3

### Presentation
3

### Contribution
3
