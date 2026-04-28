# Emergent Communication with Conversational Repair

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 6, 8

## Abstract
Research on conversation has put emphasis on the importance of a multi-level communication system, in which the interlocutors aim to establish and maintain common ground. In natural conversations, repair mechanisms such as clarification requests are frequently used to improve mutual understanding.
Here we explore the effects of conversational repair on languages emerging in signaling games. We extend the basic Lewis signaling game setup with a feedback channel that allows for the transmission of messages backwards from the receiver to the sender. Further, we add noise to the communication channel so that repair mechanisms become necessary for optimal performance.

We find that languages emerging in setups with feedback channel are less compositional.
However, the models still achieve a substantially higher generalization performance in conditions with noise, putting to question the role of compositionality for generalization.
These findings generalize also to a more realistic case involving a guessing game with naturalistic images.

More broadly speaking, this study provides an important step towards the creation of signaling games that more closely resemble the conditions under which human languages emerged.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper explores the effects of conversational repair mechanisms on emergent communication in signaling games. The basic Lewis signaling game setup is extended to allow bidirectional communication through an interleaved feedback channel from receiver to sender. Noise is added to the communication channel by replacing tokens at random. Models trained with a feedback channel are found to achieve higher generalization performance under noisy conditions, even though the resulting languages are less compositional.

### Strengths
The experiments are interesting, testing multiple game configurations and noise levels. The code is open-sourced. Results are robust across settings and replicated in two different game paradigms. The paper clearly explains the methods, results, and implications. Allowing conversational repair is clearly an important step towards better models of human language evolution.

### Weaknesses
Methods: The most significant concern is that the apparent lack of compositionality (arguably the 'headline' result) is an artifact of the specific choice of how to inject noise (via random i.i.d. replacement with a special token). Modeling *misunderstanding*, uncertainty over *meaning* or *interpretation* at the message level, rather than uncertainty over the literal content of each message token, would better reflect the cases where repair arises in real-world communication. For instance, instead of replacing tokens with a generic noise token, a more nuanced approach would involve perturbing the message by substituting tokens with semantically related or confusable alternatives, which might better capture how misunderstandings actually occur. This could involve using a confusion matrix derived from human language data or a model of semantic similarity to guide the token replacement process, which would provide a more realistic simulation of communication breakdown. 

Originality: While some details of the specific implementation here is novel, a number of prior works have also introduced interactive repair mechanisms into signaling games and are not discussed. Even the classic Steels (1995) simulations included a form of (binary) repair. Here are some salient examples from the more recent literature. 

- van Arkel, Woensdregt, Dingemanse, & Blokpoel. (2022). A simple repair mechanism can alleviate computational demands of pragmatic reasoning: simulations and complexity analysis. CoNLL.
- Tria, Galantucci, & Loreto (2012). Naming a structured world: A cultural route to duality of patterning. Plos ONE. 
- de Ruiter & Cummins. (2012). A model of intentional communication: AIRBUS (Asymmetric Intention Recognition with Bayesian Updating of Signals). SemDial. 
- Silva & Roberts. (2016). Exploring the role of interaction in the emergence of linguistic structure. EVOLANG.
- White, Poesia, Hawkins, Sadigh, & Goodman. (2022). Open-domain clarification question generation without question examples. EMNLP. 

Additional weaknesses:

* The feedback channel only allows binary signals. It's unclear how the results would be affected by a higher-dimensional space of feedback. For example, a richer feedback channel could allow the receiver to provide more specific information about what part of the message was unclear, or even offer a hypothesis about the intended meaning. This could lead to more efficient repair strategies and potentially different emergent communication systems.
* Noise is only added to sender messages, but realistically noise would affect receiver feedback too, possibly shrinking the gap between the feedback vs. no-feedback models. This is a significant limitation since in real-world communication, the feedback channel is often just as susceptible to noise as the primary communication channel. Ignoring this factor may lead to an overestimation of the benefits of the feedback mechanism.
* No comparison to recent related work like van Arkel et al. is provided to situate the advances here.

In summary, while this work provides a good first investigation, the contributions are somewhat modest and incremental given prior exploration of feedback channels. It's difficult to know which aspects of the findings are general consequences of repair mechanisms, and which aspects are artifacts of specific choices about how noise is injected in this task setup. Addressing the above limitations would strengthen the novelty and significance of the study.

### Questions
* Typo: “defined by the number of symbols in the vocabulary V” — the vocabulary was previously denoted by X; V was defined was the set of possible values the attributes may take.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduced a new Lweis signaling game setup with a noisy communication channel for emergent communication. Through experiments in logical and pixel-level input, they showed that setups with the receiver’s feedback can achieve better generalization performance in a noisy environment. By reporting the topographical similarity, it also points out that a better generation does not usually mean a higher compositionality.

### Strengths
1. This paper considers a novel setup with multi-step communication with the receiver’s feedback. It changes the original unidirectional communication to bidirectional communication, which can better resemble realistic human communication scenarios.

2. The experiments designed multiple evaluation groups to test how a feedback channel helps alleviate the effects of noise, influence generalization, and compostionality. The experiments introducing realistic image referential tasks with objects in the same visual background also look interesting. The performance contrast between compositionality and generalizability and the potential cause of the receiver’s feedback is worth further investigation.

### Weaknesses
The current experiments only show that communication with the receiver’s feedback will generalize better in a noisy environment. It would be more comprehensive to understand this feedback behavior with further analysis:

    a. The semantics of the feedback token: for example, is it more related to interaction regulation (continue to talk, no need to talk) or the attribute of the objects (clarification on some attributes)? It is unclear how the feedback token is encoded and what specific information it conveys back to the sender. A more detailed analysis of the feedback vector's content is needed, perhaps by examining its correlation with different aspects of the input or the sender's message.

    b. The messages updated by the sender: based on the receiver’s feedback, how the sender’s messages vary across different time steps. It's crucial to understand how the sender adapts its message based on the feedback. Does the sender refine its initial message, or does it switch to a completely different strategy? Analyzing the changes in the sender's message vector over multiple iterations could reveal the underlying communication dynamics.

    c. Through multiple iterations, will the receiver provide less feedback or less informative feedback while they gradually build their common ground? It would be beneficial to investigate whether the receiver's feedback becomes more concise or less frequent as the agents establish a shared understanding. Does the feedback signal converge to a stable state, or does it continue to evolve throughout the interaction? Analyzing the entropy or information content of the feedback signal over time could provide valuable insights.

    d. Will the emerged languages with additional feedback make the sender’s messages of different objects more separatable? While improved generalization is observed, it is not clear if this is due to the sender's messages becoming more distinguishable for different input objects. A visualization of the sender's message embeddings for different objects, with and without feedback, would help to clarify this point.

### Questions
1. How does the game end? Will they communicate a fixed number of time steps?
2. How does the receiver generate the feedback token, through another MLP layer besides the one used in the final target selection?
3. The drops in the compositionality are interesting. Since the sender’s message now depends on both the symbolic input and the receiver’s feedback, the semantic spaces could be disturbed. Have you tried to let the sender and the receiver share the same vocabulary?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a basic notion of communication failure and opportunity
for recovery into the standard emergent communication signalling game.
Communication failure occurs when one of the sender's tokens is replaced with
a special noise token, and the listener is provided with a binary feedback
channel that could be used to indicate the need for recovery.  The empirical
results show that the binary feedback channel provides an increase in
performance in the presence of such noise but is not necessary in the noiseless
cases.  This effect is robust across different hyperparameters as well as with
both symbolic and image embedding-based observations.

### Strengths
The paper is coherent: it has a simple, well-defined scope that is explained
well, pursued with reasonable methods, and has empirical data with supports the
main contribution with appropriate ablations.  While the contributions are not
extensive or revolutionary, I do not see this as a problem because the
contributions are sufficient and the quality of the paper as a whole makes
a good building block in the field's body of literature.

### Weaknesses
 I do not see any major weaknesses in the paper as a whole.  Any specific areas
that could be improved upon are mentioned in "Questions".  What puts my rating
at an 8 instead of 10 is primarily the modest significance of the
contributions.

A minor weakness is that there is no robust/empirical explanation for the cause
of the drop in topographic similarity in the feedback-enabled agents.

### Questions
- Page 2:
    - Section 2.2: [Travis LaCroix's paper](https://www.semanticscholar.org/paper/Biology-and-Compositionality%3A-Empirical-for-LaCroix/6422d5e83caec99487936035cfbb2b0d18f2a76d) on reflexivity could be relevant
- Page 5:
    - "instable" -> "unstable"
    - It would be better to use 95% confidence intervals instead of raw standard error
    - Discussion: "jointly co-constructing" seems pretty relevant to Kottur et al. (2017), maybe a sentence connecting the two works would be appropriate
    - "lack vision-and-language" -> "lack of vision-and-language"?
    - Would it be possible to give a sense of what the correlation between the
      presence of the noise token and the feedback request from the receiver
      is?  It's not necessary for all of the experiments, maybe just the
      initial basic ones.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
