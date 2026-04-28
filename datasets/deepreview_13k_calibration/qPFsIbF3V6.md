# Guess & Sketch: Language Model Guided Transpilation

- Decision: Accept
- Avg Score: 7.00
- Scores: 5, 8, 8

## Abstract
Maintaining legacy software requires many software and systems engineering hours. Assembly code programs, which demand low-level control over the computer machine state and have no variable names, are particularly difficult for humans to analyze.
Existing conventional program translators guarantee correctness, but are hand-engineered for the source and target programming languages in question. 
Learned transpilation, i.e.  automatic translation of code, offers an alternative to manual re-writing and engineering efforts.
Automated symbolic program translation approaches guarantee correctness but struggle to scale to longer programs due to the exponentially large search space. Their rigid rule-based systems also limit their expressivity, so they can only reason about a reduced space of programs. 
Probabilistic neural language models (LMs) produce plausible outputs for every input, but do so at the cost of guaranteed correctness. In this work, we leverage the strengths of LMs and symbolic solvers in a neurosymbolic approach to learned transpilation for assembly code. 
Assembly code is an appropriate setting for a neurosymbolic approach, since assembly code can be divided into shorter non-branching basic blocks amenable to the use of symbolic methods. 
\ourmethod\ extracts alignment and confidence information from features of the LM then passes it to a symbolic solver to resolve semantic equivalence of the transpilation input and output. We test \ourmethod\ on three different test sets of assembly transpilation tasks, varying in difficulty, and show that it successfully transpiles 57.6\% more examples than GPT-4 and 39.6\% more examples than an engineered transpiler. %better than both engineered transpilation methods and pure neural language modeling methods. 
We also share a training and evaluation dataset for this task.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an approach for machine language translation. They attempt to utilise a generative language model with a confidence score to identify uncertain blocks or "guesses" which can then be symbolically solved using a neuro-symbolic solver. They rely on Sketch (Solar-Lexama  et al)  prior work for handling the expansion/completion of the uncertain tokens. The authors perform experiments on other three datasets (Unix, Euler, Benchmarks) outperforming or equal (in rare cases) in all test settings.

### Strengths
- While a simple concept, the method outperforms prior work
- The concept of uncertainty is a good mapping to identify holes in the generated program
- Evaluation is robust and thorough, providing analysis of failure cases
- Authors identify a setting for Neuro-symbolic approaches to work stably and outperform prior works

### Weaknesses
 - Novelty within this approach is quite limited the translation is a standard approach the confidence is simple (see below), and they use an existing neuro-symbolic solver therefore, it is more on the sole idea of putting these together. This is the main criticism. However, they outperform prior work, and the idea is interesting and technically sound. 
- Confidence is very trivially explained. In general, deep models are very confident even when they are wrong. It isn't clear how this was implemented and is critical to the method. As the author's rely on this to identify potential errors for solving.
- The parameter lambda is not ablated on as the threshold for identifying blocks. It is unclear if this is set low to allow more errors i.e. false negatives but to make the result more robust.

### Questions
- Explain more how the confidence is applied and used is it based on prior work as there is significant literature in this area
- Does the Lamda hyper-parameter effect the output, was this ablated on, but not included?
- Why do you choose only the region of error to be solved? Did you consider using a buffer before and after as well to increase the consistency across the section and provide context?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an approach for translating low-level assembly programs into higher-level code for the purpose of analysis and human understanding. The approach is based on a combination of neural processing and symbolic program translation. The proposed approach,  called GUESS & SKETCH, extracts alignment information from features of the neural language model and passes it to a symbolic solver to perform "transpilation". The paper also presents experiments illustrating the benefits of GUESS & SKETCH as compared to GPT-4 and an engineered "transpiler".

### Strengths
The paper is well written and presents a clear contribution. The combination of generative language models and program synthesis by sketching is new and it is shown to be effective as compared to state of the art techniques.

### Weaknesses
I could not understand the correctness guarantee provided by the approach. The authors say "the correctness of GUESS & SKETCH is always lower-bounded by the correctness of the initial guess" -- the authors should explain what they mean by lower bound here. If the translation is incorrect, how can it be useful in practice?

The scalability is unclear.  What s the largest program that has been translated using the approach presented here?

### Questions
Please see above?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
this work presents a way of transpilation: turning one assembly code into another functionally equivalent assembly code.

the main techniques consists of: using a LM to generate candidate programs. from the internal values of the LM 1) alignment/attention and 2) uncertainty, generate localized sketches with holes for the candidate program. this localized sketch is then solved, with the holes resolved to values that are provably equivalent to the source code's corresponding fragments. the fragments are then stitched together, finishing the transpilation process.

results show the proposed method beats a reasonable set of baselines -- a heuristic based transpiler, and few-shot using gpt4.

### Strengths
## the good part of quality: that it worked
The presented method works, on a domain of highly structured translation task (i.e. highly stylized texts), something a language model should perform very well at, and it shows. The extra care taken to correct the translation locally is a reasonable yet good idea to complement the weakness of the language model.

The benchmark is thorough, and the evaluation (on what is being shown) is solid. 

## clarity
I am very grateful how this work is able to encapsulate the domain specific aspects of compiler and assembly, so that the top level algorithm remains accessible to the ML audience. Thank you!

## novelty : fair
I think it is a straight forward paper, and it outlined reasonable decompositions of the transpiling tasks to LLM and a symbolic solver.

### Weaknesses
## the not so good part of quality:

### evaluation set is small 
This work can be significantly beefed up with a synthetic test set. Evaluation on mere 100s of programs is likely not sufficient. Since it is possible to compile C into both architectures, and since test generation / fuzzing is a well established approach, this work can benefit from an artificial/synthetic test set consists of about ~1k programs, to evaluate the correctness of the transpiler more thoroughly. 

### lack of statistic tests
At least we should see confidence intervals of the results, or some kind of t-test to make sure that the proposes method is better than the baseline not due to noise. Kindly ask your colleagues in statistics to look over your tables and give recommendations on how it could be made bullet proof.

I would love to see this update in the rebuttal period.

## fit of venue
While I think this is a good paper, it might be a better fit at PLDI. As I am unsure what is the AI/ML lessons gained from this work, other than it is possible to build such a system, and some relatively detailed finding on how well language models are at learning over a highly stylized text (assembly code) when compared to English sentences.

However, as other application papers of the compiler flavour has a precedence of appearing at ICLR, this is not a major concern.

### Questions
## program equivalence?

As I understand program equivalence is an undecidable problem. If I recall correctly, synthesis systems like sketch does not have a way to fully verify the SKETCH and the SPEC are identical over all input-outputs, but only over a bounded domain?

Is this an issue for your work? Or is it because everything is bounded to begin with, as we're working over assembly and we only need to account for, for instance, 16 bits integers or similar ? Or is it some Z3 theory magic that allows for a DSL which programs can be reasoned for full equivalence?

At any rate, this should probably be clarified in the paper.

## successfully compile = ?

If I read correctly, success is measured over a set of input-output test cases to see if the input code runs the same as the compiled output code. Is this related to the program equivalence problem above somehow? Is this comprehensive enough to make sure the transpiling is not mistaken?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
