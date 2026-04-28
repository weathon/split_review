# Towards Automated Knowledge Integration From Human-Interpretable Representations

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
In noisy and low-data environments, a significant challenge in machine learning lies in effectively incorporating inductive biases that enhance data efficiency and robustness. Despite many success of informed machine learning methods, designing algorithms with explicit inductive biases based on prior expert knowledge remains largely a manual process. In this work, we explore how prior knowledge represented in its native formats, e.g. in natural language, can be integrated into machine learning models in an automated manner. Inspired by the learning to learn principles of meta-learning, we consider an approach of learning to integrate knowledge via conditional meta-learning, a paradigm we refer to as informed meta-learning. We introduce and motivate theoretically the principles of informed meta-learning enabling automated and controllable inductive bias selection. To illustrate our claims, we implement an instantiation of informed meta-learning--the Informed Neural Process, and empirically demonstrate the potential benefits and limitations of informed meta-learning in improving data efficiency and generalizing to novel knowledge representations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper provides a theoretical framework around conditional meta-learning, oriented toward conditioning neural processes on natural language info about temporal processes.

### Strengths
Nice concrete examples through the theory; good explanations and clear notation.

### Weaknesses
Overall an interesting and well-written paper, but  seems like it's maybe missing references to conditional metalearning, and doesn't compare to the baselines it discusses early on. The theory seems like a lot of math to say things that are kind of vacuous, but such is math, and it's well explained with nice concrete examples. The biggest criticism I have is that the way K is given to the model, concretely, is very unclear, and in my experience (conditioning physics-informed neural nets, which come to think of it is another area that should be cited as relevant lit) this kind of 'technical detail' makes a huge practical difference.

Detailed comments by section:

- I would add "particularly" to the first sentence of the abs
	- almost very nice first fig, but caption could be improved (what are the different indices on Ks and how do they relate to K

2.
- nice concrete examples of K in the problem setting
- not sure exactly how to phrase this, but it seems worth mentioning how strong the assumption of an underlying stochastic process is. e.g. in the nice explanatory figure, in the observable data space you have a sine and a line, and these are clearly different, but what we actually have in real life is often a bunch of high-D points that you could fit a sine or a line to with equal error and it doesn't mean that either of them is properly the "underlying" function. I'm not trying to say this assumption isn't fine to make, but I think it's worth emphasizing how abstracted it is from "real" data
	- similarly for the assumption of conditional independence of K and D that is necessary for the proof; it seems to me like it's a lot of math to say something pretty obvious; that if we add new necessarily true and relevant information that will improve things ... it would be nice to give an idea of how much the proof relies on those properties.

3.
	- nice concrete examples but man the formatting is hard to read; please make it not all in italics!
	- the remarks section is a bit random and take up a lot of room relative to what they provide; suggest moving to appendix to make more room for easier to read formatting and extra concrete examples/explanations of experimental results and connections from theory to experiments.

4 
- the arrangement of the sections makes sense, but it does mean all the theory and acronyms about neural processes are really far from the empirical results; it would be nice to tie them together better with cross-references
- unclear how the aggregator operator works

5 
- definitely nice to have the empriical results but because of the synthetic setting it's hard to take anything from the results without the discussion being more concrete -- it would be nice to continue the concrete example pattern you had from the theory section (e.g. for the dist shift experiments, what was the K you provided?). 
	- why not use real weather forecasts?? introducing a LLM adds an unnecessary layer of complexity and potential for hallucinations 
- again unclear how the K is actually informing the NP -- are you encoding it with a pretrained LLM and appending that to the input of the neural process? adding? something else? these details are the technical core of the paper and it's important to make them clear.

### Questions
Detailed comments by section:

- I would add "particularly" to the first sentence of the abs
 - almost very nice first fig, but caption could be improved (what are the different indices on Ks and how do they relate to K

2.  
- nice concrete examples of K in the problem setting
- not sure exactly how to phrase this, but it seems worth mentioning how strong the assumption of an underlying stochastic process is. e.g. in the nice explanatory figure, in the observable data space you have a sine and a line, and these are clearly different, but what we actually have in real life is often a bunch of high-D points that you could fit a sine or a line to with equal error and it doesn't mean that either of them is properly the "underlying" function. I'm not trying to say this assumption isn't fine to make, but I think it's worth emphasizing how abstracted it is from "real" data
  - similarly for the assumption of conditional independence of K and D that is necessary for the proof; it seems to me like it's a lot of math to say something pretty obvious; that if we add new necessarily true and relevant information that will improve things ... it would be nice to give an idea of how much the proof relies on those properties.

3. 
 - nice concrete examples but man the formatting is hard to read; please make it not all in italics!
 - the remarks section is a bit random and take up a lot of room relative to what they provide; suggest moving to appendix to make more room for easier to read formatting and extra concrete examples/explanations of experimental results and connections from theory to experiments.

4 
- the arrangement of the sections makes sense, but it does mean all the theory and acronyms about neural processes are really far from the empirical results; it would be nice to tie them together better with cross-references
- unclear how the aggregator operator works

5 
- definitely nice to have the empriical results but because of the synthetic setting it's hard to take anything from the results without the discussion being more concrete -- it would be nice to continue the concrete example pattern you had from the theory section (e.g. for the dist shift experiments, what was the K you provided?). 
 - why not use real weather forecasts?? introducing a LLM adds an unnecessary layer of complexity and potential for hallucinations 
- again unclear how the K is actually informing the NP -- are you encoding it with a pretrained LLM and appending that to the input of the neural process? adding? something else? these details are the technical core of the paper and it's important to make them clear.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The work proposes a viewpoint on how to integrate prior knowledge into the learning process via informed meta-learning. The idea is to incorporate knowledge that is conditioned on the generative function, but is not a unique representation of the function. The meta-learning algorithm can then be applied to incorporate this knowledge. Neural Processes are used for empirical studies of the approach, demonstrating the advantages of prior knowledge in three specific cases.

### Strengths
The paper can potentially be applied to a lot of domains, where the expert knowledge and priors are presented.

The paper is overall clearly and well-written.

The proposed viewpoint is clearly illustrated based on a set of examples.

### Weaknesses
One of the core ideas of the paper’s perspective is to use prior knowledge K to guide the learning system. To assess how applicable this viewpoint is to different problems and domains, more discussion is needed on how to construct K for different scenarios, as the examples provided in the paper are very specific and not necessarily realistic. More discussion is also needed on how the properties of K influence the viewpoint. For example, in 5.1.1, more knowledge corresponds to a stronger prior. Can this be formalized for a general viewpoint?

Could you please comment on whether it is possible to have a stronger statement in Theorem 1 with a strict inequality?

Minor:

Line 245: "mete-training" -> "meta-training"

Please name the axes in Figure 6.

### Questions
For the MAML Example 1, how similarity between tasks is measured?

Could you please comment of how number of shorts or context points should be chosen while using the framework?

### Soundness
3

### Presentation
3

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
This paper studies a meta-learning setup in which a learner tries to adapt to a new environment given only a few samples. 

The paper's main idea is to endow the learner with additional domain knowledge about the specific task (\mathcal{K} in the paper).

The key research question is whether, in the era of LLMs, we can provide the learner with human-interpretable domain knowledge in the form of text, e.g. the human provides the learner with the information that the function "is monotonically decreasing". 

The paper first develops a formal framework for meta-learning with additional information (Section 3).

The paper then provides different empirical applications of the new paradigm using Neural Processes (Section 5).

The paper states that *"our work primarily focuses on putting forward the idea of informed meta-learning with the introduced
class of INPs serving mainly as an illustration."*

Overall, this is an interesting and well-written paper with limited empirical evaluation (which makes the currently submitted paper a marginal paper in my view).

I'm not very familiar with the meta-learning literature, and I decided to give this paper the benefit of the doubt with a score of 6.

### Strengths
I find the research question quite interesting. It connects a classic topic in machine learning research—how to integrate human domain knowledge into the algorithm's inductive bias—with recent developments (LLMs). 

The paper is well-written, and the appendix documents the different experiments in detail. The paper illustrates key ideas and results with well-designed figures. 

The paper's theory seems sound (though I did not check the details), and the experiments are well-designed. 

Overall, this paper makes some interesting suggestions for how novel developments in LLMs can inform existing work in knowledge integration / meta-learning.

### Weaknesses
The paper's main weakness is the empirical applications. Specifically, it does not provide a real-world application in which providing additional information in natural language improves upon other approaches (running somewhat contrary to the motivation as outlined, for example, in Figure 3). While the authors claim that the aim of the work is not to surpass existing baselines, the lack of a compelling real-world demonstration limits the impact of the proposed method. The experiments in section 5.2.1, while using real-world data, still rely on synthetic knowledge representations. The textual descriptions used are not derived from actual expert knowledge or real-world scenarios, which weakens the argument for practical applicability. The paper should have included an experiment where the knowledge is derived from actual expert knowledge, not just synthetically generated text. 

**Section 5.1:** The experiments in section 5.1 are all for the synthetic function y_i = ax_i + sin(b x_i) + c + epsilon_i. For this reason, the results in this section (while convincing) read like a case study, not a systematic assessment of the pro's and con's of the proposed method. The choice of this specific function limits the generalizability of the findings. A more diverse set of synthetic functions should have been considered to demonstrate the robustness of the approach. The experiments do not explore the limitations of the proposed method when the provided knowledge is noisy, incomplete, or even contradictory.

**Missing baselines:** I find the usefulness of the proposed method hard to gauge because the paper does not compare it with other existing methods. For example, the authors mention that Bayesian linear regression would be a natural method to use in the setup of Section 5.1. Then why does the paper not compare performance with Bayesian linear regression? The absence of such a comparison makes it difficult to assess the relative performance of the proposed method compared to established techniques. The paper should have included a comparison with Bayesian linear regression, especially given the simplicity of the function used in Section 5.1.

### Questions
**Question 1:** Figure 3 contains nice examples, e.g. K = "This function is sharply decreasing." However, there seems to be no exmpirical application with K = natural language for a regression problem in the paper. Why not? Did the authors not try this, or did they try it, and it did not work? I would be quite interested to see if this can work well in practice. 

**Question 2:** Figure 4(b): I do not understand how the plot value for {a,b} can be in between {a} and {b}? should {a,b} not be strictly better than {a} and {b}?

**Question 3:** What exactly are the research contributions in Section 3? To me, this Section mostly reads like a summarization of different possible approaches, laying out the strategy the authors want to employ in the paper. 

**Question 4:** Concerning the general motivation, it is a bit strange to read some of this in 2024. For example, from the introduction: *"with the knowledge integration step often forming the core contribution of many ML papers"*. Do the authors actually believe that "the knowledge integration step" will be a core part of many ICLR'25 papers?

**References:** Some of the references need updating. e.g. 

"Chelsea Finn, Kelvin Xu, and Sergey Levine. Probabilistic Model-Agnostic Meta-Learning, 2019.
eprint: 1806.02817."

was published at neurips 2018.

### Soundness
3

### Presentation
3

### Contribution
3
