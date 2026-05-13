# EReLELA: Exploration in Reinforcement Learning via Emergent Language Abstractions

- Decision: Reject
- Scores: 5, 3, 1

## Abstract
The ability of AI agents to follow natural language (NL) instructions is important for Human-AI collaboration. 
Training Embodied AI agents for instruction-following can be done with Reinforcement Learning (RL), yet it poses many challenges.
Among which is the exploitation versus exploration trade-off in RL. 
Previous works have shown that NL-based state abstractions can help address this challenge. 
However, NLs descriptions have limitations in that they are not always readily available and are expensive to collect. 
In order to address these limitations, we propose to use the Emergent Communication paradigm, where artificial agents learn an emergent language (EL) in an unsupervised fashion, via referential games. 
Thus, ELs constitute cheap and readily-available abstractions. 
In this paper, we investigate (i) how EL-based state abstractions compare to NL-based ones for RL in hard-exploration, procedurally-generated environments, and (ii) how properties of the referential games used to learn ELs impact the quality of the RL exploration and learning.
We provide insights about the kind of state abstractions performed by NLs and ELs over RL state spaces, using our proposed Compactness Ambiguity Metric.
Our results indicate that our proposed EL-guided agent, entitled EReLELA, achieves similar performance as its NL-based counterparts without its limitations. 
Our work shows that RL agents can leverage unsupervised EL abstractions to greatly improve their exploration skills in sparse reward settings, thus opening new research avenues between Embodied AI and Emergent Communication.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an algorithm for augmenting reinforcement learning
algorithms with emergent communication-derived rewards that aid in tasks where
exploration is a difficult part of the task.  This algorithm works by training
agents to play a referential game with observations from the environment; the
speaker agent is then able to generate abstracted descriptions of the
observations for the RL agent which can encourage the agent to make new
observations that are not trivially different.  This algorithm is validated
with a handful of experiments and new metric "Compactness Ambiguity Metric" (CAM)
which quantifies the way in which the speaker agent generates abstract
descriptions of the environment observations.

### Strengths
The major strength of the paper is that the EReLELA algorithm itself is
presented clearly and is well motivated by (1) the success of language-based
abstraction methods for RL-based exploration and (2) the potential of emergent
communication to produce learned, human language-like communication.  I think
this contribution is especially important on the emergent communication side of
things because the field lacks practical applications of emergent languages,
and integrating it into an algorithm such as the one this paper introduces
could not only be effective in its own right but be an effective demonstration
of the applicability of emergent communication methods.

### Weaknesses
The major weaknesses of this paper are two fold.  First, CAM is not clearly
defined and/or justified.  It seems like it is a key analytical tool in the
empirical work of this paper, but its presentation did not give me a clear
picture of what it was doing either in theory or in practice. The description of the metric lacks detail regarding the specific mathematical operations involved in computing the histogram. It is unclear how the time intervals are precisely mapped to histogram bins, and the role of the hyperparameters $(\lambda_i)$ in this mapping is not sufficiently explained. The justification for using a histogram of compactness counts as a measure of abstraction quality is also weak, lacking a clear connection to established measures of information content or representational similarity.

The second also relates to clarity, namely the lack of clarity of the
experiments themselves.  The graphics themselves are quite noisy and refer to
settings that are not described in detail (e.g., "Agnostic STGS-LazImpa-10-1
ELA+AccThresh=90+Distr=256+UnifDSS").  Since the experimental settings are not
established at the beginning of the experiments section, I have very little
idea as to how to interpret the empirical results.  Is there a baseline?  Which
one is the proposed method?  Which other settings am I supposed to compare it
to?  Since I cannot easily answer these questions reading this section of the
paper, I cannot determine what is learned about the proposed algorithm.
I think it could be the case that the experiments themselves already contain
the requisite data for presenting an effective analysis of the algorithm, but
those things would need to be presented more simply and methodically. The experimental results are presented in a way that makes it difficult to discern the relative performance of different methods. The plots are too cluttered, and the specific configurations being tested are not clearly defined, making it hard to understand the impact of different design choices. The lack of a clear baseline for comparison makes it challenging to assess the effectiveness of the proposed approach. The paper would benefit from a more structured presentation of the experimental results, with clear definitions of the experimental conditions and a more focused comparison of the different methods.

### Questions
My main questions derive from the _Weaknesses_ section above: What are the
experiments showing?  Less is more when it comes to these graphics and
presenting these results.  Regarding CAM: what exactly is the metric?  What are
the inputs and outputs, precisely?  Once this is clarified, is it the case the
CAM is actually measuring the things we want to measure?  How do we validate
this?

It is possible I could be convinced to raise my review scores if the authors
are able to streamline the presentation of the experiments (especially the
graphics) _and_ the results are still substantive enough for the paper's
claims.  While I appreciate the thoroughness of the introductory sections,
I think they could be compact to make room for a more extensive explanation of
each experiment.  If the CAM and experiments sections of the paper had as much
clarity as the introduction, related work, and EReLELA sections, I easily
recommend acceptance.

### Minor Comments

- (Abstract) "done ne" -> "done"
- (1 Introduction) Typo at the very beginning?
- (1 Introduction) "NLs oracle" -> "NL oracle"
- (1 Introduction) In a sentence or two, why is it necessary to use
  language-based abstractions?  Wouldn't it be easier to represent things as,
  say, an embedding or more formal structure?  (I have an inclination as to
  what the answer to this question is, but I think it should be touched on in
  the text for clarity.)
- (Line 055) "NLs, that are" -> "NLs, which are"
- (Line 058) "hard-exploration" -> "hard exploration"
- (Line 065) What does "aligned by not similar to" mean?
- (Line 067) "advantages _over_ their NL"?
- (Line 090) The discussion of intrinsic versus extrinsic reward is a little
  unclear (partially on the writing level).  I can see what is being
  communicated, but someone with slightly less RL background might have a more
  difficult time.
- (Line 105) This is a good distinction to make.
- (Line 114) Extra space before ";"
- (Line 122) "entail to good exploration": Not sure what this means.
- (Line 138) "constraint" -> "constrain"
- (Line 160) Space after end quote
- (Line 161) Use `\citep`
- (Line 216) Extra space before ","
- (Line 228) Does "may not be passed" mean "is not passed with a certain
  probability"?  The phrasing "may not" is not clear here since it makes it
  sound like it is "not allowed to be passed".
- (Line 276) This paragraph is difficult for me to follow.
  - $i\in[0,N-1]$ suggests that $i$ is a real number, but I believe it is
    discrete.  Using $i\in{0, 1, \dots, N-1}$ would be clearer.
  - What is $\lambda_i$?
  - What is a "time interval threshold"?
  - Using pseudocode might be clearer here (I don't think I follow it enough to
    say this for sure, though).
  - (Sec 3.2) What is the input and output of CAM?  I get that it is creating
    a discrete distribution based on utterances used to describe observations,
    but what is the metric itself?  Is the distribution the metric itself or is
    it the entropy or the divergence from some baseline metric?
- While I appreciate explicitly naming the hypotheses, they are not stated with
  enough clarity and precision to be testable.  That is, how do we know
  precisely when the hypothesis as been validated or not?
- (Sec 4.1, Fig 2) These are difficult to follow, especially with the colors
  and the names which have not been well specified.  For example, I do not know
  what "shared" or "agnostic" refers to in the architecture.
  - Unless it is necessary, it would be good to reduce the number of
    referential game settings that you report so as to minimize confusion.
- The "natural language" baseline should be called a "synthetic language" since
  it is just programmatically generated and not gathered/derived from human
  language in a meaningful way.
- The different text colors for the experimental settings is a bit distracting.
  I think it would be better to come up with simple, easy-to-remember names for
  each setting and use those without worrying about colors (aside from the
  lines/legend on the plots themselves.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors hypothesize that emergent languages can benefit RL agent exploration, to the same extent as expensive natural lanaguge descriptions. They propose a method to learn such emergent languages via reference games to induce intrinsic rewards jointly with the RL objective (EReLEA). They provide evidence that the learned emergent language is as useful, even more compact than natural language oracles.

### Strengths
1. Interesting method. The proposed CAM metric made a decent attempt at measurnig the quality of abstractions as far as I can understand its definition.
2. Contextualization of the problem is clearly articulated in sec 1 and 2.
3. The analysis about Zipf's Law of Abbreviation and the learned emergent langauge is insightful.
4. The ablation studies seem thorough (if only I can interpreate how they precisely differ in context).

### Weaknesses
My primary concern is presentation quality. Improved clarity can significantly benefit readability of this paper, as well as my understanding of the main method.
1. Typo/abbreviation mistakes: line 3 of the abstract "be done ne(?) with Reinforcement Learning", start of the first paragraph of introduction, line 42 "in effect" (?), single quotes in line 43, "it dynamics" -> "its dynamics" in line 98, and so on.
2. What's the superscript -1 on line 271?
3. Figure readability is sadly discounted by low resolution, small font size, and the lack of in-figure legends. Personally I find it hard to parse the results without clear legend names and matching color coding, even with captions.
4. Undefined H3.1 and H3.2 in lines 337-338
5. $\beta_1$ and $\beta_2$ in Figure 2 captions seem out of blue. Are they defined anywhere in the main text? Why do they imply "shared" and "anogostic"? Perhaps a table comparing configurations of parallel runs?
6. I appreciate the intuition, but I struggle to understand the formulation of the proposed CAM in sec 3.2. I think neither eq 4 nor the relative ambiguity of a language are CAM, but I cannot find exactly how CAM is computed in the main paper.

### Questions
1. What is the precise definition of CAM?
2. How do parallel experiments (i.e., different curves in Figure 2) differ exactly?

I am happy to raise the score if these questions are addressed with clarity.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper investigates to what extent referential games, and the resulting emergent language abstractions, can be used to derive intrinsic rewards in hard exploration problems of reinforcement learning agents.

### Strengths
The research question of the paper is creative: can emergent language abstractions be used to help RL agents in hard exploration problems.

### Weaknesses
A) I don’t see empirical gains of using emergent language abstractions: Looking at Figure 2, it seems to me that the performance of the natural language abstraction agent (gray) and the emergent language abstraction agent (green) are within noise levels of each other. Thus, I find it difficult to conclude from the experiment that emergent language abstractions are important, in particular since both the natural language abstraction agent and the emergent language abstraction agent are using count based exploration terms as well. These should be ablated.

B) Even if there were empirical gains, I would want to see a comparison to state-of-the-art intrinsic reward methods for hard exploration problems based on natural language abstractions to see the point empirically proven that emergent language abstractions are supposedly preferable. In particular, I would expect comparisons to 
- Mu et al. Improving Intrinsic Exploration with Language Abstractions. NeurIPS 2022. https://doi.org/10.48550/arXiv.2202.08938
- Klissarov et al. (2023). Motif: Intrinsic Motivation from Artificial Intelligence Feedback. arXiv. https://doi.org/10.48550/arXiv.2310.00166
- Zhang et al. OMNI: Open-endedness via Models of human Notions of Interestingness. ICLR 2024. https://arxiv.org/abs/2306.01711 

C) Related to the above, I believe the authors need to evaluate on harder exploration problems, such as MiniGrid’s KeyCorridor-S3-R3 and MultiRoom-N10-S10, or MiniHack (Samvelyan et al. MiniHack the Planet: A Sandbox for Open-Ended Reinforcement Learning Research. NeurIPS 2021. https://doi.org/10.48550/arXiv.2109.13202). Moreover, I would like to see experiments beyond gridworlds, e.g., on Vizdoom (c.f. Henaff et al. Exploration via Elliptical Episodic Bonuses. NeurIPS 2022. https://doi.org/10.48550/arXiv.2210.05805).

D) I believe it would be important to add a tabula-rasa RL agent, as well as only RND baseline to Figure 2.

E) p8 Figure 3 looks to me like the experiments did not finish in time.

### Questions
- Abstract: It’s not entirely clear to me what limitations of NL-based counterparts you are referring to here.
- p1: “RND … which can be difficult to deploy” — Why are they difficult to deploy? RND is a very straightforward intrinsic reward method. 
- From Figure 1 it looks like the intrinsic reward is only generated from the speaker. Why shouldn’t one also derive the intrinsic reward from the listener?

Comments
- p4 Figure 1 is too small to read. Same goes for other figures in the paper (e.g. Figure 2)
- p7 Figure 2 caption: explain the different methods variants in more detail.

What the authors would have to demonstrate to see an improved rating from me:
Demonstrate clearer gains of emergent language abstractions over natural language abstractions (A) on harder exploration problems (C) while also comparing to state of the art natural language abstraction methods (B) and adding tabula-rasa RL, as well as RND, baselines (D). Present results of finished experiments where each method is ran for the same number of steps (E).

### Soundness
1

### Presentation
1

### Contribution
1
