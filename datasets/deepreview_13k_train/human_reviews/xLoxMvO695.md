# Decomposing the Enigma: Subgoal-based Demonstration Learning for Formal Theorem Proving

- Decision: Reject
- Scores: 5, 6, 8

## Abstract
Large language models~(LLMs) present an intriguing avenue of exploration in the domain of formal theorem proving. Nonetheless, the full utilization of these models, particularly in terms of demonstration formatting and organization, remains an underexplored area. In an endeavor to enhance the efficacy of LLMs, we introduce a subgoal-based demonstration learning framework, consisting of two primary elements: Firstly, drawing upon the insights of subgoal learning from the domains of reinforcement learning and robotics, we propose the construction of distinct subgoals for each demonstration example and refine these subgoals in accordance with the pertinent theories of subgoal learning. Secondly, we build upon recent advances in diffusion models to predict the optimal organization, simultaneously addressing two intricate issues that persist within the domain of demonstration organization: subset selection and order determination. Through the integration of subgoal-based learning methodologies, we have successfully increased the prevailing proof accuracy from 38.9\% to 44.3\% on the miniF2F benchmark. Furthermore, the adoption of diffusion models for demonstration organization can lead to an additional enhancement in accuracy to 45.5\%, or a $5\times$ improvement in sampling efficiency compared with the long-standing state-of-the-art method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a method of improving the performance of LLM-based guidance to the formal prover Isabell for the Isabell problems in MiniF2F.  The reported results are an improvement on previous results for this dataset.  The primary method involves the constructions of in-context examples to serve as a prompt to an LLM in finding a proof of a desired theorem x.  The prompt consists of a set of "demonstrations" each of which is a kind of "lemma" consisting of the statement proved by the lemma and the sequence of steps (subgoals) in the proof of the lemma. The method of constructing the demonstrations in the prompt appropriate for a specific goal x is quite complex involving a heuristic solution to a Hamiltonian graph problem.

### Strengths
This paper described an considerable effort in improving the performance of LLM-based support for formal verification.  The ideas are nontrivial and provide experimental results that may be of value to future efforts in this area.

### Weaknesses
The writing is unclear.  For example does the term "demonstration-based proof" in the subgoal refinement section correspond to graph nodes (demonstrations) in section 2.2?  Reviewers cannot be expected to read appendices and the technical meaning of terms needs to be clear from the body of the paper.

A serious ambiguity is whether the "manually written" seed demonstration-based proofs are biased to the test set.  If so, this would constitute training on the test set.  The process of manual annotation needs to be discussed.  A related issue is source of the training data for the "diffusion model" (it is not really a diffusion model as the latent variables are not in R^d and no Gaussian distributions are involved).
In the section on evaluation they say

   Given the absence of a training split in the miniF2F
   dataset, we leverage optimal organizations that yield successful proofs from the miniF2F-valid set
   to train the diffusion model.

I find this very unclear.  Why is training on the validation set ok?

It seems to me that the complexity of the system allows for an over-fitting of the system design to the test data. I worry that the results would not generalize to a test set that was unavailable to the authors before testing.

### Questions
Questions are asked in the weakness section.

### Soundness
2 fair

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
This paper looks at using LLMs to provide formal proofs from an initial human-provided proof sketch, where the formal proofs are verifiable by an external automated theorem prover. The proposed method consists of two parts. First, the authors propose generating subgoal based proofs from human-provided proof sketches. This is inspired by the subgoal generation literature in reinforcement learning--specifically, that a good sequence of subgoals should preserve the property that each subgoal is reachable from the start state, and that the goal state is reachable from the subgoal. Second, the authors propose using diffusion models to select and order the demonstrations provided to the LLMs, for generating the formal theorem sketches.

### Strengths
- Using LLMs for theorem proving is an interesting problem. The proposed method follows prior work in breaking down the problem into two in-context  learning problems: first, providing a subgoal proof, and second, providing a formal proof based on the subgoal proof. The paper proposes novel methods to order in-context learning examples for the in-context learning problems. 
- Well written and clear. 
- Experiments are described clearly and sufficient baselines are used. Experiments show ~7% improvement of proposed method over baselines.

### Weaknesses
Experiments: 
- No std deviations or measurement of uncertainty in Tbl 1 &2. 
- The improvement brought by using the diffusion models is very minor (about 1% in the Table 2). This is potentially not statistically significant. However, in Figure 2a, there seems to be a clear  advantage of using diffusion models + subgoals over using subgoals alone (about 2-5 additional problems solved for each # of LLM calls). These two results seem slightly contradictory. In any case, the result of Table 2 shows that the main innovation of the method seems to be the subgoal generation itself, which I feel the authors should state clearly. 

Experimental setup is not fully justified. 
- Why are words like "sorry" and "oops" used to determine that the proof is not valid? The provided justification is that these words indicate that the proof has been prematurely terminated, but I'm not quite sure I understand this justification.

### Questions
How does the quality of the human provided proof sketch influence the performance of the proposed method?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work aims at using LLMs to assist formal proof generation. Previous attempts decompose the generation process into two phases, where the LLMs first generate an informal proof given the statement and then build a formal proof given the informal proof. The authors argue that LLM-generated informal proofs are prone to be invalid while human-written ones could be incompatible with the formal proof. To bridge the gap, the authors propose to replace the informal proof with a sequence of subgoal proofs, where each step of the subgoals can be verified. The subgoal proofs are iteratively generated with LLMs and existing automated theorem prover as the verifier.

The authors also claim that the order and selection of demonstrations are vital to the performance of LLM-based generations. To automate this selection process, the authors utilize a diffusion model to generate conditional demonstration organizations.

Empirically, the proposed method can outperform previous baselines in the MiniF2F dataset or match the performance while significantly reducing the number of LLM calls.

### Strengths
- The paper is well-written and easy to follow.
- The idea of using subgoal-based proofs to bridge the gap between formal proofs and LLMs is well-motivated.
- There is a clear empirical improvement over previous baselines.

### Weaknesses
 - For the diffusion model-based reorganization, it would be nice to show the correlation between the generated optimal demonstration organization and the input statement. I am curious if the diffusion model would collapse into generating a generic organization that works decently well with most statements. On roughly the same note, it would also be nice to show some examples where the order of the demonstrations greatly affects the performances. Another interesting baseline to compare would be to search the optimal organization for each tested statement.
- It seems that previous LLM-based algorithms do not utilize formal proof generation tools such as Sledgehammer. I am wondering if it's possible to add a comparison of the number of usages of such tools (or their resource consumptions), aligning with the LLM calls comparison.

### Questions
I don't have any questions for the authors.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
