# Lemur: Integrating Large Language Models in Automated Program Verification

- Decision: Accept
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
The demonstrated code-understanding capability of LLMs raises the question 
of whether they can be used for automated program verification, a task that %typically 
demands high-level abstract reasoning about program properties that is challenging for verification tools. We propose a general methodology to combine the power of LLMs and automated reasoners for automated program verification. We formally describe this methodology as a set of transition rules and prove its soundness. We instantiate the calculus as a sound automated verification procedure and demonstrate practical improvements on a set of synthetic and competition benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an interesting way to use LLMs and automated program verification tools synergistically to prove properties of programs that may otherwise be difficult to prove by the verification tools themselves.  The core idea consists of using an LLM to generate potential assumptions that may help an automated program verifier discharge the proof goal.  Once such assumptions are found, the effort of the program verification tool is directed to proving the assumptions themselves.  The authors present a set of sound rules to transform "configurations" of the proof process involving LLM calls and program verifier calls.  The authors also present some heuristics for LLM prompt generation, and for deciding how to prioritize multiples responses that may be provided by the LLM.  Finally, the authors present experimental results that show the promise of the proposed technique vis-a-vis state of the art program verification tools.

### Strengths
The paper is clearly written, modulo some typos.  This helps in taking the reader along with the flow of the presentation.  The core ideas are illustrated with a running example -- this helped me follow the ideas without much difficulty. The idea of using an LLM to propose assumptions that can then be used to simplify a verification task is promising and the experiments demonstrate this.  Being able to out-perform the winning entries in SV-COMP is a significant achievement, and I believe this sufficiently demonstrates the promise of the approach.

### Weaknesses
The set of rules formulated by the authors doesn't add much value to the paper.  Algorithm 1 could itself have been presented directly, with explanations for the different steps.  In my opinion, the rules are kind of a force-fit to the paper.
It is good that the authors try to show that the proof rules are sound; however the soundness proofs are simple and not very insightful.  Indeed, finding a sound set of rules for simplifying/decomposing program verification is often not the difficult part of the process.  The more technically challenging part is to have completeness results for some subclass of programs/properties.  Unfortunately, the authors don't even try to do this.
Since there are practical limits to prompt lengths for an LLM like GPT or GPT-4, this sets limits to how large a program can be verified using the proposed technique.  This is highly undesirable.  It would have been better if the authors attempted decomposition of the problem (perhaps guided by an LLM) and then applied the proposed technique to each decomposed part, and then stitched the results back together.  Unfortunately, the authors completely avoid any such attempt/discussion.
SV-COMP has several tracks for verification.  The total count of programs in SV-COMP is significantly larger than that reported by the authors. It is not clear whether some cherry-picking was done in selecting the examples.
An LLM like GPT-4 makes use of immense computational power at the server end to come up with proposals/suggestions quickly.  It is not fair to discount this computational effort completely when comparing with the performance of other solvers that do not make LLM calls.  As a consequence, I believe the time comparison is not fair.
A method like the one proposed, without any considerations of how the LLM is trained, may give dramatically different results based on what LLM is being used.  Therefore, a discussion on training the LLM should have been included.

### Questions
1.  What actual value does the set of rules provide to this work?  Wouldn't it have sufficed to have Algorithm 1 directly, along with an explanation of the steps?
2.  SV-COMP contains many, many more benchmarks.  How does LEMUR compare with UAutomizer or other tools on the other benchmarks?  Why are so few benchmarks chosen for comparison?
3.  For what kinds of <program, property> combinations do LLMs fare badly as far as suggesting assumptions is concerned?  In some sense, this ought to depend on what kinds of data it has been trained on.   I didn't see any discussion in this regard -- I would tend to think that there are <program, property> combinations for which LLMs will have a very difficult time generating good assumptions.
4. An LLM like GPT-4 makes use of immense computational power at the server end to come up with proposals/suggestions fast.  How do you propose to factor this in your comparisons for an apples-to-apples comparison.  Neither ESBMC not UAutomizer were provided access to such computational power; so how is the comparison fair?
5. What are the assumptions on the training of the LLM that are being used?  Will the proposed method work with one's privately trained LLM?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes a system for program verification that queries CHATGp4 for axioms.
The idea is interesting and the results excellent,  
The main problem of the paper is that it is written in a way that is much more suitable fior a CAV venue  than fior ICLR. The authors carefully and fomally describe the program  analysis framework, but they take a loose approach about GPt

### Strengths
The main strength of the paper are the results in Section 5\

.

### Weaknesses
Presentation

Only good results are shown? How likely is the fail case? ChatGPT seems a magic box, Above al, the way you present your work makes it unnecessarily hard to understand ypur ideas.

### Questions
A small point: there is another lemur system in LLMs

"An important research question is whether modern AI models are capable of understanding ." .. indeed, but can you claim you do that?

Are you the first to ask LLMs to propose sub-goals?

I'd much prefer a better survey that would make your contributions clear, and a graphical descriotion of the system that would allow me to position the different componrrntd

I understand the process is fully automated?

 "  -Finally, if the verifier V proves that the original property is not an invariant" -> is the verifier cmplete?

Arguabythe prompts are what makes everything else worthwhile. Yet, they are in appendix?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an approach to reachability verification, dubbed Lemur, which combines the invariance generation capabilities of LLMs with standard verification tools. The resulting procedure, which is sound albeit incomplete, comes with theoretical guarantees.
Lemur equipped with GPT4 can solve benchmarks that are currently out of reach of state-of-the-art standard reachability verification tools.

### Strengths
- Clear presentation
- Reachability is a pivotal problem in program verification
- Promising preliminary results
- (To the best of my understanding) Lemur's calculus and template algorithm can accomodate different combinations of invariant generators and verifiers

### Weaknesses
My main concerns are related to the empirical evaluation of Lemur.
The combination of LLMs and standard verification procedures is indeed promising, but I am left wondering how much the results are reliant on the specific LLM GPT4.

This is particularly important considering the economic cost of reproducing the experiment, which can be prohibitive for some.

If I understand correctly, Lemur is a template algorithm. I would then expect to see results for LEMUR(X, Y), where X = {GPT4, other free LLMs, other invariant generation techniques (Code2INV maybe?), and Y = {UAUTOMIZER, ESBMC}.

### Questions
- How much is Lemur performance reliant on the invariant generator quality?
- How does Lemur fare without GPT4 as an invariant generator? 
- Can Lemur be used with non-LLM invariant generators such as Code2Inv?

--------
Minors:

The derivation rules in Fig.1 are not 100% clear to me. What is the semantic of operator ": :"?

Figures 3 and 4 should have different (and self-explanatory) captions, i.e. explicitly mention the referred benchmarks.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a principled approach for combining LLMs with automated reasoning tools to perform automated program verification. Automated program verification typically proceeds by breaking down the overall proof goal into simpler proof sub-goals---each sub-goal establishes some invariant of the program which can help in proving/disproving the overall program assertion. The proposed technique uses LLMs to suggest candidate invariants as proof sub-goals; whether the suggested invariants hold or not is posed as a query to existing automated program reasoning tools. While the general paradigm of guessing and then checking invariants is well-known in the program verification literature, the paper presents a proof calculus that cleanly formalizes this style of reasoning and develops an algorithm based on this calculus. The calculus is proven sound and the algorithm is shown to be terminating under suitable conditions. Most importantly, the presented algorithm outperforms state-of-the-art automated program verification tools on standard benchmarks.

### Strengths
1. This is a very well-written paper and presents a nice, clean formalization of the guess-and-check style of program reasoning via the Lemur calculus.

2. The algorithm that operationalizes the calculus is elegant and easy to understand.

3. Use of LLMs to suggest candidate program invariants is an obvious idea but it has been very well manifested into practice, both mathematically and algorithmically,  by this work.

4. Some of the prompting tricks used to get the invariants from the LLM, such as placeholder lines, are interesting in their own right.

5. Most importantly, the empirical results are very promising and suggest that LLMs and verification tools can be fruitfully combined.

### Weaknesses
1. This is a relatively minor comment but the formalization and the algorithm seem geared towards imperative languages where the notion of associating a property/invariant with a line number makes natural sense. It would be helpful to acknowledge that the proposed calculus might not necessarily be applicable to all programming languages.

2. There has a large body of literature on data-driven techniques for learning loop invariants [1,2]. Unlike Code2Inv and Lemur, these past works use dynamic values of loop variables. Adding references to this body of work would help paint a fuller picture about this area.

3. For the benchmark of difficult programs from SV-COMP, where are the placeholder lines added? Is it after every line in the program? If not, doesn't the location of the placeholder leak information, potentially aiding Lemur?

4. It seems like the text and the formal expression for the second bullet point of Proposition 2.1 do not line up. Shouldn't the implication in the formal expression go the other way?

5. I don't think the last line on Page 2 is correct. A program without loops can have an unstable property because the program can still have multiple paths due to branches. Also, how can a property that is not an invariant be stable? Is this the case where stability is due to the property always being false?

6. Is the time in Table 1 in seconds? When you say timeout of 1 hr or 10 minutes, is that the timeout for the entire dataset or each program?

7. Does each bar in Figure 4 correspond to a single value for the number of proposals or a set of values? It seems like it is the latter case. It would help to clarify the figure.

### Questions
1. For the benchmark of difficult programs from SV-COMP, where are the placeholder lines added? Is it after every line in the program? If not, doesn't the location of the placeholder leak information, potentially aiding Lemur?

2. It seems like the text and the formal expression for the second bullet point of Proposition 2.1 do not line up. Shouldn't the implication in the formal expression go the other way?

3. I don't think the last line on Page 2 is correct. A program without loops can have an unstable property because the program can still have multiple paths due to branches. Also, how can a property that is not an invariant be stable? Is this the case where stability is due to the property always being false?

4. Is the time in Table 1 in seconds? When you say timeout of 1 hr or 10 minutes, is that the timeout for the entire dataset or each program?

5. Does each bar in Figure 4 correspond to a single value for the number of proposals or a set of values? It seems like it is the latter case. It would help to clarify the figure.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
