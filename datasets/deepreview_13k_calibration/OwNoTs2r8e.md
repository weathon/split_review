# No Free Lunch: Fundamental Limits of Learning Non-Hallucinating Generative Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 1, 8, 8, 8, 5

## Abstract
Generative models have shown impressive capabilities in synthesizing high-quality outputs across various domains. However, a persistent challenge is the occurrence of ``hallucinations", where the model produces outputs that are plausible but invalid.
While empirical strategies have been explored to mitigate this issue, a rigorous theoretical understanding remains elusive. In this paper, we develop a theoretical framework to analyze the \emph{learnability} of non-hallucinating generative models from a learning-theoretic perspective. Our results reveal that non-hallucinating learning is statistically \emph{impossible} when relying solely on the training dataset, even for a hypothesis class of size two and when the entire training set is truthful. To overcome these limitations, we show that incorporating \emph{inductive biases} aligned with the actual facts into the learning process is essential. We provide a systematic approach to achieve this by restricting the facts set to a concept class of finite VC-dimension and demonstrate its effectiveness under various learning paradigms. Although our findings are primarily conceptual, they represent a first  step towards a principled approach to addressing hallucinations in learning generative models.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
-This paper is rather strange, because it seems to be about hallucination as a specific problem, but the theoretical claims just treat hallucination as a subset of examples.  It seems like the claims are about a more general phenomena of trying to learn examples which belong to a set.  In this case, set is characterized as a set of factual claims, but this property isn’t used.  In the technical results, it’s just a set.  

Notes from reading the paper: 
 -Hallucinations are outputs which are plausible but invalid.  
  -Impossible to stop hallucinations using data, but need to leverage inductive biases about facts.  
  -Paper is purely conceptual, but if claim is valid, seems very striking.  
  -Let X be the set of sentences, while T is the set of facts, or sentences that describe true statements that are relevant.  The hallucination rate is the rate hall(p, T) of sentences generated which aren’t facts.  
  -A demonstrator q is faithful wrt T if hall(q,T)=0.

### Strengths
The issue of conceptualizing and theorizing about hallucinations seems like an important and useful problem to address.

### Weaknesses
The paper seems extremely flawed.  First, it is a purely theoretical paper, with no analysis or experiments, even on toy models.  I think this is dubious, especially when the theoretical framework is speculative and not well established.  For example, even a small illustration on a real toy dataset would help to clarify the ideas of the paper.  Second, it doesn't seem like the analysis actually uses the nature of hallucinations in proving the result, which leads me to think that the paper could be written with a more general claim. The core issue is that the paper's theoretical claims do not engage with the specific properties of hallucinations but rather treat it as a general set-membership problem. The analysis does not leverage the fact that hallucinations are plausible but incorrect statements; instead, it treats them as any arbitrary set of incorrect statements. This significantly weakens the connection between the theoretical results and the motivating problem of hallucination in language models. The paper could be reframed to address a more general problem of learning from sets, but then the connection to hallucinations would be lost. This lack of specificity makes the theoretical claims less impactful and relevant to the intended domain. The paper's framework also neglects the nuances of contextual understanding and the fact that the truth value of a statement can be highly dependent on the context in which it is made.

### Questions
Couldn’t a statement simply be non-factual, but not a hallucination.  Context also seems important. For example, a claim may be factual in a story but not in general.  Additionally, a question seems like a sentence which is non-factual but not a hallucination.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors examine the problem hallucinations in generative models from a learning theory perspective. They provide a formal setup for the problem, define the hallucination rate formally (as the probability mass assigned to samples not in some true fact subset) and characterize the importance of distinguishing between proper/improper learning for this paradigm. They then provide three main theoretical results:
- Proper learning (i.e. restricted to a hypothesis class) without hallucination is impossible.
- Non-hallucinating learning that generalizes is possible given an improper learner and restrictions on the VC-dimension of the fact set $\mathcal{T}$. They provide sample complexity bounds for this case.
- Proper learning with a VC concept class is possible as long as $q$ (the data generating process) is sufficiently informative.

### Strengths
- The work provides a novel and important contribution that addresses a particularly relevant problem (namely that of hallucinations in generative models) which has not been thoroughly studied from a theoretical perspective.
- The paper is generally well-written and structured.
- The construction of the counter-example for Theorem 1 is interesting and clear.
- Section 4.1 is particularly valuable studying the case of a model that can generalize without hallucinating.

### Weaknesses
 - The work could benefit for a more in-depth comparison with Kalai & Vempala (2024). Specifically, the authors should elaborate on how their definition of generalizability via information measure maximization relates to the concept of "calibration" used in Kalai & Vempala (2024). A more detailed analysis of the similarities and differences in the theoretical frameworks would strengthen the paper's contribution.
- The impossibility results in section 3 seem to rely on the pathological case of an uninformative $q$. While Theorem 1 demonstrates that proper learning without hallucination is impossible, it hinges on a specific construction where the data generating process $q$ does not provide sufficient information to distinguish between different hypotheses. It would be interesting to investigate the case where $q$ is sufficiently informative as per definition 4. In particular, the authors should discuss whether proper learning with a VC concept class is possible if $q$ satisfies the conditions outlined in Definition 4, and if so, how the sample complexity bounds might change.
- As acknowledged by the authors, the work is mostly conceptual and a first step in this research direction. 
- The messaging on the key takeaways from the paper could be improved (especially for practitioners not particularly interested in learning theory). The authors should consider adding a section that clearly summarizes the practical implications of their findings.

Nitpicks:
- The work could do with less italicized words (feels like there's at least 1-2 every sentence).
- Some typos such as:
  - Line 245: For the -> the
  - Line 294: Complited -> Completed
  - Line 326: Leaner -> Learner

### Questions
- Theorem 1 is written as specifically for the case of a hypothesis class of 2, do you think the result would still hold for hypothesis classes of arbitrary sizes?
- I'm a bit confused by how exactly Example 3 differs from Example 1?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers the problem of hallucinations in generative models from a learning theory lense. The authors highlight that avoiding hallucinations poses a fundamental problem: On the one hand, a model should generalize beyond its training distribution, but on the other hand, undesired implausible artefacts (hallucinations) have to be avoided without a strict characterization of what is implausible. The authors formalize this issue and are able to show that without inductive biases that restrict the set of plausible samples, it is impossible to avoid hallucinations. This is an important result that will be of interest to the wider community, especially also for practicioners who attempt to avoid hallucinations via empirical means. The authors go on to explore how inductive biases can facilitate learning without hallucinations, but highlight that this problem remains challenging.

### Strengths
The paper, to the best of my knowledge, introduces a novel take on hallucinations in generative models and is the first to show such a strong impossibility result. While the paper remains purely theoretical and doesn't offer an implementation for cases in which hallucination-free learning is in principle possible (as the authors also admit), I believe this result will nontheless be informative for the community. Theorem 4 and §4.2 in general make a first step in understanding when avoiding hallucinations is possible.

The paper is thorough in setting up the problem and does a good job of elucidating the importance of its results.

### Weaknesses
The paper is quite dense and might be inaccessible to a larger audience, especially to practitioners for whom this result might be very relevant. I would highly suggest the authors to add, e.g., a short paragraph after each theorem that translates the abstract results into specific examples and gives a higher-level intuition. E.g. consider a simple sample task using real data: Which assumptions of the theorem will be met? Are there some implications the theorem makes that would be violated but can be considered to be not very impactful in practice? I believe some of the proofs could be moved to an appendix to make space for this.

Specifically, the introduction is overly technical and lengthy, delving into formal definitions before establishing the core problem and its significance for a broader audience. This makes it difficult for readers unfamiliar with the specific learning theory concepts to grasp the motivation behind the work. The paper would benefit from a more intuitive introduction, deferring the technical details to later sections. The lack of an introductory figure further compounds this issue, as a visual overview of the problem setup and the proposed approach could greatly enhance accessibility.

Furthermore, the paper assumes a level of familiarity with PAC learning that may not be universal among the target audience. While the concept is mentioned, it is not adequately explained, which could hinder understanding of the subsequent theoretical results. The frequent use of abbreviations, while common in some subfields, also detracts from the readability and accessibility of the paper, particularly for those outside the immediate area of expertise. For instance, terms like 'w.p.' and 'w.h.p.' are used without explicit definitions at their first appearance, which adds to the cognitive load for the reader.

### Questions
# Questions
- LL178: Is point (ii) even always possible in principle, i.e., will the learned model always generalize given sufficient training samples?

# Minor suggestions
- LL65: What is $\mathcal X^*$?
- LL130: typo "being" → "been"
- LL151: while it is technically correct to call $\mathrm x^n$ a "sample", this might confuse readers to assume $\mathrm x^n$ is a single point rather than a set of points. I recommend using a slightly different terminology
- Eq. 3: $\| \cdot \|_\text{TV}$ what does this notation mean? I assume based on the paragraph below it is "total variation distance"?
- §1, §2: as far as I can see, the term PAC learning is never introduced
- LL167: What does "w.p." stand for?
- LL195: What does "w.h.p." stand for?
- LL336: Should be "note that, here, ..."

Generally, I recommend double-checking that abbreviations and notations used are introduced whenever they first appear. Where not absolutely necessary, avoiding abbreviations increases readability and makes the paper more accessible to readers from other subfields.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper studies learning hallucination-free models from a learnng theory perspective and provides multiple negative and positive results, the latter for cases when inductive biases are present.

### Strengths
**I am by far not an expert in learning theory, so my theoretical understanding of this paper is limited. Still, I can appreciate the authors' contributions:**

- the paper's topic is highly relevant, interesting, and the results (seem to be) strong
- the setup is clear from the introduction (though it's maybe too technical to be placed into the introduction)
- the technical results have nice intuitive explanations (even for someone who is not an expert in learning theory)

### Weaknesses
 **My main point is that the presentation lacks clarity and detailed explanations of the steps taken. Note, however, that I am no expert in learning theory. Due to this fact, I choose a conservative score, but I am willing to reconsider during the rebuttal.**

### Major points
- several details are deemed "simple/clear/easy to verify" and left out, and non-standard abbreviations are not resolved (even though the reader might be able to guess them)
- the proofs could have been moved to the appendix, for the main text providing proof sketches would have been sufficient (and this would provide space to elaborate on intuition/notation) - by sketch I mean an intuitive description of the steps, not as technical as the one provided for Theorem 4.

### Minor points
- a Figure 1 for an intuitive overview would improve the paper
- L55: what is an instance space?
- the introduction is too long and already contains technical details (and readers probably won't expect to find these in the introduction), please consider restructuring the paper
- also, though the contributions list is helpful, it is too long to be considered as a "summary"
- L117: "Our results demonstrate"
- Eq (3): please specify what the subscript TV stands for.
- L160: what does 3-agnostic mean? Does the "3" relate to Eq (3) or something else?
- Fact 1: 
	- please don't call this a "simple fact."
	- what is "w.p."?
- L195: what is "w.h.p."?
- Example 1: I appreciate that you provide an example, though skipping steps by writing "It is easy to verify" doesn't help the reader. Please elaborate.
- L317: what do you mean by "measured competitively?"

### Questions
- You use plausibility, validity, and factuality (and their negations) to describe hallucinations. Though for me the definition of hallucination rate was very clear, the definition in the abstract _("plausible but invalid")_ seems not to capture all aspects of hallucinations. I'd argue that implausible (and false) outputs also belong to hallucinations. Could you please clarify which one you mean?
- Out of curiosity, how does your intuition relate to impossibility results in the identifiability literature (eg,  http://proceedings.mlr.press/v97/locatello19a.html), which also state that some further assumption ("inductive bias") is needed for identifiability?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper develops a theoretical framework to explore the limitations of training generative models that do not hallucinate. It finds that learning non-hallucinating models based purely on truthful training data is statistically impossible without incorporating inductive biases. The study further introduces scenarios where non-hallucinating learning is achievable by using improper learners or by restricting the hypothesis space with finite VC-dimension concept classes.

### Strengths
1. The paper explores the inherent challenges and limitations of achieving non-hallucinating learning, introducing the theoretical impossibility of agnostic proper learning.
2. Through Theorems 1-4, the paper offers new theoretical insights, such as the impossibility of agnostic guarantees and the role of concept classes with finite VC-dimension in enabling non-hallucinating learning.
3. The paper provides upper and lower sample complexity bounds to balance model generalization and non-hallucination.

### Weaknesses
The framework proposed is primarily conceptual, and may need practical guidance for deploying non-hallucinating generative models in real-world applications.

### Questions
1. Your framework assumes that inductive biases can be introduced through concept classes. How is it applied to generative models in real-world scenarios?
2. The VC-dimension plays a key role in characterizing non-hallucinating learnability, but for complex models like transformers, estimating the VC-dimension is challenging. Are there alternative complexity measures or proxies you considered?
3. Can the framework be extended to evaluate hallucinations across multimodal generative models, such as vision-language models? If so, how would you do that?

### Soundness
3

### Presentation
2

### Contribution
2
