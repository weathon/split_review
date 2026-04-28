# Understanding In-Context Learning from Repetitions

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
This paper explores the elusive mechanism underpinning in-context learning in Large Language Models (LLMs). 
  Our work provides a novel perspective by examining in-context learning via the lens of surface repetitions. 
  We quantitatively investigate the role of surface features in text generation, and empirically establish the existence of \emph{token co-occurrence reinforcement}, a principle that strengthens the relationship between two tokens based on their contextual co-occurrences.
  By investigating the dual impacts of these features, our research illuminates the internal workings of in-context learning and expounds on the reasons for its failures. This paper provides an essential contribution to the understanding of in-context learning and its potential limitations, providing a fresh perspective on this exciting capability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper quantitatively investigates in-context learning in terms of surface patterns. 
It shows that there is an inherent correlation between surface patterns, self-reinforcement, iterative generation and their important role in text generation.
In particular, it shows the role of surface surface patterns in text generation and the existence of token co-occurrence reinforcement that strengthens the relationship between two tokens based on their contextual co-occurrences.
The experiments on MMLU and GSM8K show that the reinforcement helps to constrain the output space and format the output according to a  demonstration such as ‘Let’s think step by step’ .

### Strengths
This paper provide a novel framework to understanding in-context learning via  the notion of token co-occurrence reinforcement.
Through various experiments, the authors have shown how token reinforcement causes spurious correlations in in-context learning.

### Weaknesses
Althogh  there is a novelty in showing experimentally that token reinforcement can cause some problems in in-context learning,
the paper lacks the important perspective of analyzing why token reinforcement exists and causes problems. 
For example, the following paper, which is only briefly mentioned in this paper, analyzes the impact of repetition structures in a corpus on in-context learning from an information-theoretic perspective.
A Theory of Emergent In-Context Learning as Implicit Structure Induction
Michael Hahn, Navin Goyal
They showed that the performance of in-context learning is represented by a complexity that repetition structures can be represented by a small PCFG tree, and  experimentally investigated theoretical finindings.

### Questions
Is it possible to provide hypothesis about the reason for the token reinforcement phenomenon and check it, even experimentally?
The authors may argue that analyzing reasons is the next step, i.e., outside the scope of this paper; however, it is fandamental in machine learning research.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the emergent in-context learning (ICL) ability of LLM. The authors try to probe the ICL performance through surface repetitions, and establish a theory called token co-occurrence reinforcement, which explains the reasons for possible failures.

### Strengths
- This work provides meaningful explanations on the possible failures of ICL. 
- The experiments seem comprehensive and convincing.

### Weaknesses
 - This work tries to understand the inherent ICL behavior of LLMs, yet is in lack of theoretical analysis. For example, how is such token co-occurrence reinforcement established? This may involve the detailed interactions between prompts and self-attention mechanism, etc., which I would like the authors to delve into.
- As an experiment-oriented work, the authors should examine their assumptions on more LLMs; otherwise, it's hard to reach a common conclusion.
- The findings of this work are not completely new. As far as I'm concerned, the findings are based on the distributional bias in the demonstrations. The impact of spurious correlations are widely discussed in out-of-distribution generalization literature. In this regard, more insights are welcome. Also, the authors could discuss on how to address such (inevitable) distributional bias in the demonstrations.

### Questions
As mentioned above, how could me mitigate the biased effect in ICL demonstrations?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
The authors delve into an investigation of the impact of token repetition on in-context learning (ICL) performance, revealing both beneficial and detrimental effects through empirical analysis. On the positive side, repetition aids in narrowing down the output space, fostering consistency in subsequent predictions. However, the downside is evident when non-informative or incorrect messages are repeated in the demonstrations, resulting in diminished prediction accuracy.

### Strengths
The authors conducted extensive experiments to explore the nuances of token repetition and its effects on ICL.

### Weaknesses
1.  **Lack of Clear Motivation**: The rationale behind investigating token repetition patterns is not adequately clear, leaving the reader uncertain about the study's purpose. Specifically, it's unclear what gap in our understanding of in-context learning this work aims to fill. The abstract does not effectively capture the paper's core idea, necessitating further clarification to provide a concise summary of the work. It needs to articulate why token repetition is a relevant factor to study in the context of ICL, beyond a simple observation that it exists.
2.  **Need for Enhanced Clarity**: The manuscript's presentation is complex, making it challenging for readers to navigate through the content. A more detailed explanation of certain terms and concepts, such as *surface pattern*, *self-reinforcement effect*, and *token reinforcement*, would significantly enhance comprehension, particularly if these have been previously established in prior literature. The paper should define these terms operationally, explaining how they are measured or identified in the experiments. It's not enough to simply state that these effects exist; the reader needs to understand the mechanisms behind them.
3.  **Specificity of Experiments**: The experiments are overly specific and do not sufficiently connect to real-world applications. The paper needs to provide a more compelling argument for the relevance of the chosen experimental setups. Demonstrating how the findings on repetition patterns can be applied in practical scenarios would strengthen the paper's relevance and impact. For example, if the authors are studying a particular type of repetition, they should explain why that specific pattern is relevant to real-world use cases of ICL.

### Questions
While I do not have any specific questions at this moment, I would appreciate it if the authors could address the concerns raised in the Weakness section, particularly regarding the need for clearer motivation and enhanced clarification of certain terms and concepts.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper examines the phenomenon of token co-occurrence reinforcement, whereby tokens occurring in the context have a higher chance of being predicted by an LM.
An interesting consequence is that In-Context Learning (ICL) can go wrong when a label that is different from the target label is repeated often in the in-context examples, potentially helping explain some failure modes of ICL.

It first shows that self-reinforcement occurs with randomly constructed sequences of words. The longer the repeated part, the stronger the reinforcement effect (Figure 3).
It then shows that even discontinuous repeated subsequences give rise to the reinforcement effect.
Section 4 studies the effect of the reinforcement effect on ICL. The effect can help constrain the output space and the desired pattern, but it can also lead to incorrect results.

### Strengths
- systematic study using openly available LLM family

- interesting results about the factors impacting the success and failure of ICL. For instance, in Figure 7, the authors seem to show that that in a specific CoT prompting setup (GSM8K), replacing the questions and CoT answers in the demonstrations with random tokens does not hurt ICL performance nearly as much as replacing a separator with random tokens.

### Weaknesses
 - The paper remains somewhat unclear regarding the overall contributions and implications. The paper argues that the results helps understand both limitations of ICL and the inner workings of ICL.
 To the extent that the paper aims to illuminate the "inner workings" of ICL, the contribution is left somewhat unclear. Do the authors argue that co-occurrence reinforcement is implicated in LMs' ability to pick up input-label mappings? And what "inner workings" are responsible for the co-occurrence effect? A range of recent research discussed in Section 5 aims to explain how ICL works, and observations on the self-reinforcement effect could help shed light -- and indeed the paper hints at this repeatedly (e.g., end of page 4, "In the context of ICL, this pattern corresponds to demonstrations like" -- it seems that the experiment is understood as some kind of simple prompt-like structure, but this idea and its implications are then not made explicit).

 - Clarity: Section 3.1 uses the term "sentence" for the examples, but in the experiment they are "randomly generated". How are they sampled -- just as random sequences of symbols sampled i.i.d. from the vocabulary? Are all symbols in the vocabulary equally like to appear? The same question about how masked subsequences are resampled also applies to the other experiments.

- Section 4.1, "Learning to follow patterns" -- when masking the Question, does this mean that the questions in the demonstrations are masked (i.e., replaced with random word sequences) but the question in the final element of the prompt (the one to respond to) is not masked?

### Questions
- Clarity: Section 3.1 uses the term "sentence" for the examples, but in the experiment they are "randomly generated". How are they sampled -- just as random sequences of symbols sampled i.i.d. from the vocabulary? Are all symbols in the vocabulary equally like to appear? The same question about how masked subsequences are resampled also applies to the other experiments.

- Section 4.1, "Learning to follow patterns" -- when masking the Question, does this mean that the questions in the demonstrations are masked (i.e., replaced with random word sequences) but the question in the final element of the prompt (the one to respond to) is not masked?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
