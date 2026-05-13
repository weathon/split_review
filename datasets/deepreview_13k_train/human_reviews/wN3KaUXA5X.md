# Diffusion On Syntax Trees For Program Synthesis

- Decision: Accept
- Scores: 8, 8, 6, 6, 8

## Abstract
Large language models generate code one token at a time. Their autoregressive generation process lacks the feedback of observing the program's output. Training LLMs to suggest edits directly can be challenging due to the scarcity of rich edit data. To address these problems, we propose neural diffusion models that operate on syntax trees of any context-free grammar. Similar to image diffusion models, our method also inverts ``noise'' applied to syntax trees. Rather than generating code sequentially, we iteratively edit it while preserving syntactic validity, which makes it easy to combine this neural model with search. We apply our approach to inverse graphics tasks, where our model learns to convert images into programs that produce those images. Combined with search, our model is able to write graphics programs, see the execution result, and debug them to meet the required specifications. We additionally show how our system can write graphics programs for hand-drawn sketches. Video results can be found at \videourl.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a program synthesis method based on "tree diffusion". They randomly corrupt programs (with some constraints) and learn to invert the corruptions, conditioned on the output of the corrupted program and the target output (an image rendering in their case).

### Strengths
The method is simple but non-obvious
The more general problem of program synthesis conditioned on desired outputs is very relevant
The authors use randomly generated programs as a dataset which sidesteps dataset curation in favor of just a specification of the language
The paper is well-written, easy to understand, and has nice and (mostly) clear figures

### Weaknesses
The paper is somewhat limited in scope (simple problem setup) in ways that make it not entirely obvious how the method "scales" to more complex relevant tasks like code generation.

Some minor things covered in Questions

Fig 3 is confusing. v(x) is the value function or the pre-trained image encoder? if its pretrained, why is there a _phi subscript?

Where do the initial problems come from? It seems like they are generated randomly, but how?

Do the fuzzing and edit algorithms generalize easily to non-context-free grammars (e.g. general programming languages)?

How many steps did you train for? I don't think this is covered in the appendix.

### Questions
Fig 3 is confusing. v(x) is the value function or the pre-trained image encoder? if its pretrained, why is there a _phi subscript?

Where do the initial problems come from? It seems like they are generated randomly, but how? 

Do the fuzzing and edit algorithms generalize easily to non-context-free grammars (e.g. general programming languages)?

How many steps did you train for? I don't think this is covered in the appendix.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces an innovative approach to inverse graphics tasks by combining diffusion models with transformers. The authors present the first application of diffusion to program synthesis using explicit syntax tree updates, validating their method on CSG2D and TinySVG environments.

### Strengths
- Innovative Approach: The paper presents a novel combination of autoregressive, diffusion, and search methodologies, which, despite being applied to a specific domain, holds potential for broader applications. The reverse mutation path algorithm also provides an efficient way to generate training targets. 
- Clarity and Replicability: The manuscript is well-written and easy to follow, providing sufficient detail to enable replication of the experiments.
- Comprehensive Ablation Studies: The authors conduct thorough ablation studies on key hyperparameters and the impact of integrating search, enhancing the understanding of their method's efficacy.

### Weaknesses
 - Literature Coverage: The authors should consider citing "Outline, Then Details: Syntactically Guided Coarse-To-Fine Code Generation" in the Neural program synthesis section since this work also takes multiple passes of the program and edits the program. 
- The value network (vϕ) training and effectiveness aren't thoroughly evaluated. Alternative approaches to edit distance estimation, including direct calculation from syntax trees, are not explored or compared. Specifically, the paper lacks a detailed analysis of the value network's architecture, training procedure, and its impact on the overall performance. The paper does not explore the impact of different loss functions or training data sizes on the value network's ability to accurately predict edit distances. Furthermore, the paper does not discuss the computational cost associated with training the value network, nor does it compare its performance against simpler heuristics for estimating progress during the search process.

### Questions
- In the limitations section, you mention that your syntax tree currently supports only a limited set of operators. What are the bottlenecks in expanding support to other operators and generalizing to broader coding problems?
- What is the cost of training the value network that predicts the edit distance?
- Given the recent advances in vision-language models, how does your approach compare against contemporary models like VILA or LLaMA? The current baselines only include older models (4+ years old), and evaluating against recent state-of-the-art would provide a more helpful comparison.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a program synthesis framework using mutations on syntax trees via a neural diffusion model for inverse graphic tasks. These tasks aim to convert images that can contain free hand-sketches of shapes or a set of computer-generated colored shapes into images depicting a computer-generated rendering matching the input. The authors defend the claim that the approach presents the ability to edit trees generated using a base model as opposed to incrementally autoregressive approaches that fail to narrow down the search space. The authors apply their method to inverse graphics tasks and present results in two settings (CSG2D and TinySVG) and show improved performance in the number of problems solved compared to baselines (REPL VLM and VLM) along with an ablation study to investigate the individual contributions of constituent components.

### Strengths
1. The main strength of this paper is the design of a neurosymbolic framework to evaluate the automated (i.e. diffusion-based) conversion of images into context-free grammar. This formal evaluation ensures that the desired specifications are met through iterative observation of the execution results and verification.

2. The authors extend the approach to accept hand-drawn sketches and illustrate examples in the appendix confirming the applicability of the approach in several real-world settings.

3. The supplementary videos illustrate the overall problem that the authors are attempting to solve and showcases the "edits" made by the framework.

### Weaknesses
There are three main weaknesses I would like to bring up. The authors are encouraged to rebut and provide legitimate explanations, if any, against these and the review decision may be adjusted accordingly.

1. A claim made by the author states that the proposed method focuses on editing the program synthesized from the image, unlike prior works that autoregressively generate programs that are incrementally better. In doing so, the authors propose adding random noise to modify a base syntax tree generated from CSG2D. Despite the illustrative example shown in Figure 2, enabling the approach to modify node types rather than shape, the base syntax tree structure is governed by the initial generated program. It remains unclear (at least it has not been proven) that diffusion + base tree always yields the optimal syntax tree (a statement regarding suboptimal steps in section 4.3 is thus not justified). An analysis and example to demonstrate this is lacking and should be included. Specifically, the claim that the method can escape local minima by editing the tree is not sufficiently supported. The method's ability to explore the search space beyond the initial structure is not rigorously demonstrated. The authors should provide a more thorough analysis of how the diffusion process and tree editing interact to achieve global optimality, or at least, escape local minima.

2. The overall architecture presented in Figure 3 is difficult to understand at first glance. In addition, the descriptions provided in section 3.4 (the model architecture) do not present enough detail to understand Figure 3.  Specifically, it is not clear how replacing the "(" denoted by the edit position token and replacing it with the grammar constrained autoregressive decoding yield valid syntax (i.e. are there low-level implementations in play that ensure that entire blocks from “(“ to “)” are parsed out during replacing? How are varying input lengths handled? ). Replacing "(" with "(Quad 8..." seems to break the pairing of parenthesis. In addition, it is not clear what the purpose of "EOS" is in this context. The figure needs to be revised to clearly show that the entire subexpression is replaced, not just the opening parenthesis. The text description should also be expanded to clarify how the grammar constraints are enforced during the replacement process, and how the model handles variable-length sequences and the role of the EOS token.

3. The fraction of problems solved by the method trained with "no reverse path" is nearly the same as that of the control after about 60 expanded nodes. The control reaches the same performance at about 50 nodes. Is this a "significant" efficiency gain when the maximum node expansion budget was two orders of magnitude higher (i.e. 5000)? There are no computational or time-related metrics presented which help put this into context. The authors should provide a more detailed analysis of the computational cost, including the time taken for each node expansion and the overall time to reach a solution. The claim of efficiency gain needs to be supported by concrete metrics, and the authors should clarify the practical implications of the observed performance difference.

### Questions
Here are some of the main points I would like to make:

1. The edit distance introduced by Pawlik & Augsten is narrowed to allow only small changes. If there are big changes, the change that reduces the distance between the trees the most is chosen. While this can be used as a training signal, it is assumed and was mentioned in section 3.3.2 that access to the ground-truth mutations is available. However, access to this ground truth may not be readily available in most cases. How is this ground-truth data obtained? If not automated, the authors must comment on the limited scalability of the approach.

2. In section 4.2 under evaluation, it is not clear what the criteria for considering a match between the synthesized and true plan is. Re: “In TinySVG, we accepted an image if 99% of the pixels were within 0.005 ≈ $\frac{1}{256}$.” Is this “within 0.005” a tolerance on the 8-bit pixel color intensity? If so, please state explicitly and explain how this metric is applied to the RGB images in TinySVG.

3. The difference between tree diffusion search and tree diffusion rollouts is not explicitly stated or defined in section 4.

4. There were references to computational demand and efficiency, yet no time-related metrics were reported to demonstrate gains in this regard, despite claims about improving performance efficiency. It is unclear as to just how much improvement the proposed approach affords.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents an algorithm to train a diffusion model on the abstract syntax tree (AST) of programs written in a simple procedural language. That language produces 2D images by combining geometric shape primitives, and the resulting image is used to guide the denoising process.

Using an additional network estimating the distance from a rendered image to the target image, beam search is applied to generate a sequence of AST edits (node replacements) that produce a predicted program, approximating the target image. That approach transfers to generating geometric images from noisy sketches.

### Strengths
Originality
-------------
The paper takes inspiration from existing ideas and benchmarks, but they are clearly cited, and the novel aspects are well described. For instance, a backward edit path that's better than reversing the corruption path, removing the need of a partial renderer, and relying on beam search rather than full-fledged reinforcement learning.

Quality
----------

Experiments demonstrate the advantages of the proposed approach, and properly ablate the different aspects and contributions.

Clarity
---------
The paper is overall clear and straightforward to follow. With the additional details of the appendix, the approach should be re-implementable by a different team.

Significance
-----------------
Using ML models to directly manipulate and modify programs, rather than either generate a whole program autoregressively, or emit edition instructions (which could be invalid or result in an invalid program) could make iterative program generation better or easier.
The fact that no reinforcement learning is required, but observation of the output of intermediate programs can simply be combined with beam search is also an interesting result.

### Weaknesses
Originality
-------------
No major weakness here, the work is in the continuation of previous cited work.

Quality
----------
Comparison with baselines might have been more extensive, specifically the RL-based algorithms from previous work, which could have better shown how "brittle" they were.

Clarity
---------
A few things were not clearly defined in the experiments and ablation sections (see "questions" below).

Significance
----------------
Overall, the CSG2D and TinySVG languages are a small-scale benchmark, but it's unclear whether the proposed approach would scale to large, structured programs in general purpose languages.
For instance, it might not be possible to find a sequence of valid programs created by short mutations between two relatively close programs. For instance, going from recursion to a loop, from an implicit lamda to a declared function, or from a for loop to a list comprehension. Even splitting a function into smaller pieces may require either large edits, or intermediate unparseable states.

### Questions
1. In the ablations, there is one about training only on the last mutation step. It's illustrated by Fig. 12 by only showing the transition from z_5 to z_4. Do I understand correctly that the other reverse transitions (e.g., z_4 -> z_3, ..., z_1 -> z_0) are not used for training?
2. If so, why not use that (training on all denoising steps) as a baseline?
3. Can you define the "Rollout" method, and the differences with the "Search" one?
4. What's the relationship between "Number of nodes expanded" and the "number of compilations needed"?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper addresses the edge of visual symbolic reasoning and code generation. It addresses the important task of generating code (symbolic sequence) to depict images with visual feedbacks. It applies diffusion model-like approaches to permute the program syntax tree and guarantee the correctness of the generated code. Through iterations, the model is able to recover the image with high fidelity using discrete preset symbols.

### Strengths
- This paper proposed a novel solution to the reverse CG field, to synthesis programs for visual symbolic reasoning. The proposed method address the hard task through the unique lens of syntax tree, and achieves notably better results.

- The idea of permuting on syntax tree allows for more efficient model, with better performance.

- The efforts to make demo video makes the paper easier to understoand and spread.

### Weaknesses
This is a good paper, with minor weakness points below.

- It is better to mention the size of the decoder model in the architecture section rather than in the appendix, so that readers with LLM background can quickly understand the edge of the model on this task.

- It is better to discuss the number of steps in the diffusion procedure, and the model's potential ability limit in terms of output sequence length or number of symbols. Specifically, how does the performance of the model scale with the complexity of the target program, measured by the number of symbols or the depth of the syntax tree? Does the diffusion process require more steps for more complex programs, and what is the practical limit on the complexity of programs that can be generated effectively?

- Two highly related work should be cited and discussed:

"Outline, Then Details: Syntactically Guided Coarse-To-Fine Code Generation" in ICML 2023, which explore the possibility of syntax tree to generate code, and via coarse-to-fine multi-round generation approach.

"Symbolic Visual Reinforcement Learning: A Scalable Framework with Object-Level Abstraction and Differentiable Expression Search" in TPAMI, which also learns visual symbolic programs, not to depict the image but to interact with the environments. Rainbow environment is also leveraged in their experiments.

### Questions
See discussions above.

### Soundness
3

### Presentation
4

### Contribution
3
