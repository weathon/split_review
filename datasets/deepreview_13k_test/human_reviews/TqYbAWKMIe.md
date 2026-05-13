# LILO: Learning Interpretable Libraries by Compressing and Documenting Code

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
While large language models (LLMs) now excel at code \textit{generation}, a key aspect of software development is the art of \textit{refactoring}: consolidating code into libraries of reusable and readable programs. In this paper, we introduce \lilo, a neurosymbolic framework that iteratively synthesizes, compresses, and documents code to build libraries tailored to particular problem domains.
\lilo\ combines LLM-guided program synthesis with recent algorithmic advances in automated refactoring from \stitch: a symbolic compression system that efficiently identifies optimal $\lambda$-abstractions across large code corpora. To make these abstractions \textit{interpretable}, we introduce an auto-documentation (AutoDoc) procedure that infers natural language names and docstrings based on contextual examples of usage. In addition to improving human readability, we find that AutoDoc boosts performance by helping \lilo's synthesizer to interpret and deploy learned abstractions. We evaluate \lilo\ on three inductive program synthesis benchmarks for string editing, scene reasoning, and graphics composition. Compared to existing methods---including the state-of-the-art library learning algorithm DreamCoder---\lilo\ solves more complex tasks and learns richer libraries that are grounded in linguistic knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
LILO is a system for library learning that leverages large language models. It iterates through a series of modules that allow it to automatically discover a collection of interpretable and documented abstraction functions that help solve held-out tasks across three domains: string regexes, turtle graphics, and visual-question answering. First, given the current version of a DSL, LILO asks an LLM to infer programs that solve prompted input tasks (this step is augmented by an enumerative search). Then, an abstraction discovery algorithm (STITCH) is employed to identify and refactor common patterns of code use into abstraction functions that are added to the base DSL to form a new library. These abstractions are then presented to an LLM, so that they can be given interpretable names and a doc-string description. Compared with prior library learning techniques (DreamCoder) LILO is able to solve more held out tasks with its discovered abstractions.

### Strengths
The paper is well-written and proposes a compelling method for a difficult and important problem. The methodology employed is sound and clearly described, even without a reference implementation much of the system seems reproducible. On the whole, the experimental design is reasonable and comprehensive, modulo a few missing conditions (detailed in the next section). I was pleasantly surprised by the detailed computational efficiency analysis at the end of the appendix, it was a well-formulated and interesting addition to the paper.

In terms of contribution, the paper situates itself as a complete system that offers an improvement over DreamCoder across a varied collection of tasks; I think the evidence the paper presents on this point is compelling. There are two main insights/observations that support this improvement. (1) Given a task description, LLM’s can usefully solve inductive programming tasks and (2) the success of (1) is dependant on operating over a DSL with “good documentation”, e.g. without semantic names, even otherwise helpful functions can contribute to model obfuscation. However, in some ways the most surprising results from the paper are that, even without library learning, LLMs can solve these domain-specific tasks much better than prior works (e.g. for regex, comparing DreamCoder to and LLM Solver that infers with respect to a base DSL offers a large improvement).

The paper notes that invoking an LLM at inference time can actually be more computationally efficient than enumerative search, which is an interesting observation. That said, I think the strongest experimental evidence in favor of the proposed method is in the bottom half of Table 1, which shows that LILO produced libraries outperform other libraries when only enumerative search is used. This is a clever, although not perfect, way of evaluating how well-suited each discovered library is for a particular domain.

### Weaknesses
My main concern is that while LILO does offer an improvement over DreamCoder, I’m not convinced the claimed reasons for the improvement are conclusive based on the experimental design. 

For instance, the version of LILO without enumerative search actually does worse than only using LLM solver for all three of the listed domains, even though LILO has access to an abstraction discovery method (i.e. STITCH). So then, is the evidence that LILO w/ search outperforms LLM Solver+search related to LILO’s use of LLMs (to infer programs and document abstractions) or its use of STITCH to identify common patterns of code-use. On this note, the comparisons between the LLM solver+search variant and LILO appear a bit more murky than the narrative reads; based on the listed standard deviation numbers it’s unclear if there are statistically significant differences in any of these cases. 

To better separate out how the contributions of LILO (LLM program induction in the context of iterative library learning, along with auto-documentation of abstractions) affect system performance, I think the following conditions should be considered:

- (A) Base DSL + STITCH
- (B) LLM Solver+Search+STITCH

Condition (A) would be an ablated version of LILO, where no LLM calls are made. “Wake” would be performed through enumerative search, and STITCH would still be used to generate new libraries. This would be similar to a DreamCoder + STITCH integration, where STITCH replaces DreamCoder’s sleep phase. From my perspective, this ablation condition is critical to supporting the claims of the paper – at present, its possible that the delta improvement between LILO and Dreamcoder is due entirely to LILO’s use of STITCH, and ablating out of the use of LLMs in this manner would provide a definitive answer on this point.


Condition (B) would first employ the LLM Solver+Search for a set amount of iterations, and then would run STITCH over the final set of inferred programs to output a new library. This would be important to support the implicit claim of the method that library learning needs to be performed in the intermediate stages of the algorithm. If LILO outperforms this ablation on offline search performance (e.g. bottom half of Table 1), then it would be a strong mark in favor of the method.

### Questions
While I think the paper does a good job of validating that AutoDoc is really helpful in getting the LLM to be able to employ the discovered abstractions, I’m a bit curious to know more about how mistakes in documentation might affect performance (as a few mistakes from AutoDoc were noted). Would it be possible to compare AutoDoc generated documentation versus “oracle” documentation (e.g. expert provided)? Even if done just once, it could provide some useful insights into how close the AutoDoc module is to human performance, and whether the LLM solver that gets “expert” documentation would be any better than the one generated by AutoDoc.

# Minor comments

While I appreciate the goals of the system are to work for 'real-world’ domains, I would consider reframing the introductory statement of the results section, as I wouldn’t consider any of the domains studied in this work to match that description.

I think a bit more effort should be made into clarifying that STITCH is not a contribution of this work – this is clear to a careful reader, but should be made obvious. Additional citations to STITCH in Figure 1 and the respective paragraph in Section 3 would seem appropriate. 

It looks like Table 1 has a minor bolding issue in the CLEVR mean column, bottom half. More generally, I’m unsure if bolding only the highest number is the right thing to do in this table, when the standard deviations have a great deal of overlap in many cases.

Maybe I’m misunderstanding this, but the standard inductive program synthesis problem statement at the beginning of Section 2, doesn’t seem to match the problem setting that LILO uses. Instead of being conditioned on a specification with a set of input/output examples that come from the same program, my understanding is that the LLM is conditioned on task-description/program examples (e.g. the in-context examples), and then is prompted with a single new task-description. Is there a reason for this disconnect?

While the performance differences between LAPS and LILO are discussed in A.5, is there a reason that this comparison isn’t put directly into either Table 3 or Table 4?

### Soundness
4 excellent

### Presentation
4 excellent

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
The paper introduces a neurosymbolic framework 'LILO' for learning interpretable libraries of reusable code abstractions. 
* A dual-system synthesizer that uses both LLM-guided search and enumerative search.
* A compression module based on 'STITCH' that extracts common abstractions from synthesized programs.
* An auto-documentation module that adds human-readable names/descriptions to make abstractions more interpretable.

### Strengths
**Originality**:
* The integration of LLMs and symbolic program compression is a novel approach toward library learning.
* Propose auto-documentation for improving abstraction interpretability.

**Quality**:
* Well described architecture.
* The analysis and experiments are comprehensive.
* Comparision to multiple baselines on 3 program synthesis benchmarks demonstrate the advantages of the proposed framework.

**Clarity**:
* The overall framing and individual components of LILO are well motivated.

**Significance**:
* The proposed 'LILO' provides a generalizeable blueprint for integrating language models with formal program synthesis.

### Weaknesses
* In Table 1, the proposed 'LILO' framework has substantially higher standard deviation than the baseline across three domains. It indicates LILO's performance varies more widely across different runs, suggesting less stability in this field. 
* The dual-system search module combines LLM-guided and enumerative search, yet the tradeoff and relative contributions are not deeply analyzed.
* The proposed 'LILO' is strongly based on LLM and it mentions using different models like Codex, gpt-3.5-turbo, gpt-4, but did not provide direct comparison of the their performance.

### Questions
* Please address my concern in the above weakness section.
* In Figure 10 caption D, the authors mentions LLM output are sampled without clearly specify the filtering/selection standard.  I advise the author can give a more detailed explanation.

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
The paper presented a dual strategy system utilizing LLM and symbolic systems for program synthesis. Unlike conventional programming synthesis models, which implicitly learn the common program fragment (library), the proposed LILO explicitly generates a library with human-readable function names. The code generator is informed with the library and is able to generate potentially more concise program. 

The experimental results show its improvement against the straightforward LLM + search approach and the LLM free baseline, DreamCoder.

### Strengths
The work demonstrated a successful combination of LLM and symbolic tools to efficiently generate a library and set of programs given a DSL and program synthesis tasks.

### Weaknesses
As the author also mentioned, the pipeline needs an additional self-verification step for the auto-documentation. The validity and conciseness of the language-guided program synthesis is enforced by input-output pairs and the stitch compression, while the library auto-doc has no verification or feedback loop to update the LLM or other trainable part of the pipeline. 

The application of the method is limited in functional programming with relatively simple DSL. Though it's almost a common limitation of program synthesis models/systems.

### Questions
1. Could the author elaborate on algorithm 1 and Dual-system program search? The relationship between the enumerate search and LLM-guided search is quite unclear. Are they parallel? cascaded? or combined in another manner?

2. What does PCFG stand for? Could the author describe the input-output, architecture, and training of this multi-layer perceptron? Is this model pre-trained? DSL-specific? 

3. In the Table 1, only in LOGO, the LILO method significantly outperforms the LLM solver + search. Could the author explain the performance difference among the different DSLs? If the reason is that LLM is not pre-trained on only LOGO, it could be an interesting and promising observation about the generalization capability of both LLM and LILO.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a neuro-symbolic framework for learning "code libraries" for lambda-calculus code.
The idea is to iteratively synthesize code using an LLM, compress it using an existing approach ("Stitch") and then document it using an LLM.
By repeating this approach multiple times, the overall framework learns repetitive "libraries" that can be further useful in the next iteration.

The overall framework, called Lilo, is evaluated on three tasks: CLEVR (visual scene reasoning), REGEX (string editing with regular expressions), and LOGO (graphics composition in the 2D Logo graphics language), and shows improvements over a vanilla LLM and over DreamCoder (Ellis et al., 2021).

### Strengths
1. The idea is interesting, combining both LLMs and traditional program synthesize.
2. It is refreshing to see tasks and approaches in which using vanilla LLMs still works much worse than a clever approach.

### Weaknesses
1. The tasks are a quite contrived, and it feels like the problem definition is tailored exactly to this kind of solution. All the tasks are synthetic and based on lambda calculus. What practical problems can the proposed approach be helpful for? Who is expected to use the proposed approach? 
2. Evaluation - I am not sure that it is fair to compare that proposed approach to a *prompted* LLM as a baseline when this baseline is prompted with the lambda-calculus language, which it probably was not trained on. Since the task is defined in a domain-specific-language (DSL), a prompted LLM is expected to fail. Can the task be "translated" to Python? If the LLM would be allowed to use Python, that would be a more fair comparison. Alternatively, a more fair baseline could be fine-tuning an LLM on the language, rather than just prompting, since the proposed approach also does kind-of training within its compression step. 
3. Novelty - I am not familiar with the directly related work, and I am thus not sure about the novelty: the paper claims that the framework consists of three modules: 
    1. A synthesis module - which is a prompted LLM
    2. A compression module ("Stitch"), which is adopted as is from [Bowers et al., 2023](https://mlb2251.github.io/stitch_jul11.pdf).
    3. An "auto-documentation module" which uses a prompted LLM to document the resulting code pieces, for better interpretability and improvement of the next iteration.

   It seems like steps (1) and (3) are standard code generation using LLM prompting, and the heavy lifting is done by the 2nd step. Since the 2nd step is identical to Bowers et al. (2023), I am not sure how novel is this paper compared to Bowers et al. (2023).

### Questions
### Questions

1. What practical problems can the proposed approach be helpful for? Who is expected to use the proposed approach? 
2. Can the task be "translated" to Python, and then tested on an LLM?
3. Can an LLM such as LLaMA be finetuned on the training examples, to better understand their language? Prompting an LLM with a language it was not trained on is a bit unfair.

### Comments
1. Regarding the AutoDoc module - more than *having* an auto-documentation module, the interesting part to me is that this generated documentation improve the next iteration, when fed to the LLM. That is, the self-improvement part (the fact that the LLM generated doc improves the LLM itself in the next iteration) is the interesting from an ML perspective, to me, while the paper mostly emphasizes the "existence" of this module to generate documentation, which is not significantly novel or interesting on its own.

### Summary
The main weaknesses of the paper are its lack of practicality, the tasks are quite synthetic, and I believe that an LLM-based baseline can perform better than presented, if given fair chances.
Nonetheless, the paper proposes a simple approach (simpler than DreamCoder, which is good), it is well written, easy to follow, and the ideas are conceptually pleasing, and I thus vote for acceptance.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
