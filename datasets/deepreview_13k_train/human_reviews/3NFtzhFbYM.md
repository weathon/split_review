# Dolphin: A Programmable Framework for Scalable Neurosymbolic Learning

- Decision: Reject
- Scores: 8, 8, 5, 3

## Abstract
Neurosymbolic learning has emerged as a promising paradigm to incorporate
symbolic reasoning into deep learning models.
However, existing frameworks are limited in scalability with respect to both
the training data and the complexity of symbolic programs.
We propose \tool{}, a framework to scale neurosymbolic learning at a fundamental level by mapping both forward chaining and backward gradient propagation in symbolic programs 
to vectorized computations.
For this purpose, \tool{} introduces a set of abstractions and primitives 
built directly on top of a high-performance deep learning framework like 
PyTorch, effectively enabling symbolic programs to be written as PyTorch modules.
It thereby enables neurosymbolic programs to be written in a language like Python that is familiar to developers and compile them to computation graphs that are amenable to end-to-end differentiation on GPUs.
We evaluate \tool{} on a suite of 13 benchmarks across \numbenchmarks\ neurosymbolic tasks that combine deep learning models for
text, image, or video processing with symbolic programs that involve multi-hop 
reasoning, recursion, and even black-box functions like Python {\tt eval()}.
\tool{} only takes $\speedupminperc$\%-$\speedupmaxperc$\% of the time (and $\speedupavgperc$\% on average) to train these models on the largest input per task compared to baselines  Scallop, ISED, and IndeCateR+, which time out on most of these inputs.
Models written in \tool also achieve state-of-the-art accuracies even on the largest benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes DOLPHIN, a scalable neurosymbolic learning framework that integrates symbolic reasoning efficiently within deep learning models. Unlike existing frameworks that struggle with CPU-GPU data transfer bottlenecks, DOLPHIN enables symbolic programs to operate as a set of inheritanted PyTorch nn.module, allowing efficient GPU-based differentiation.

### Strengths
1. The authors propose an end-to-end neurosymbolic framework that makes all progress differentiable.
2. With a glance at the provided code, the DOLPHIN is a lightweight implementation of the framework integrated with PyTorch, having a potential opportunity to support the neurosymbolic community.
3.  The evaluation on 13 benchmarks across 5 neurosymbolic tasks show the advantage of the proposed DOLPHIN.

### Weaknesses
1. It seems DOLPHIN only supports neurosymbolic programs with deterministic symbolic processes. For example, if HWF task requires the neural part to predict both numbers and operators (+,-,*,/), the symbolic part cannot be programmed with the Apply function. How DOLPHIN deal with this situation?


### Questions
Please refer to weaknesses 1.

Other questions:

1. What is the limitation of the proposed DOLPHIN?
2. Are lambda functions fast enough? Do we require doing some acceleration for the proposed operations, such as designing some specific CUDA kernel or triton functions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce Dolphin, which is a pytorch-friendly framework for performing neuro-symbolic computations.  The neural component of a computation is assumed to be a model, such as an MNIST digit classifier, which outputs a discrete set of symbols (e.g the digits 0-9), with a probability attached to each of them.  The symbolic component is a python program which runs a computation over the symbols.  The result of symbolic execution is a pytorch tensor, representing final output probabilities for each possible result, which is end-to-end differentiable with the neural components.  The authors apply Dolphin to several of neuro-symbolic benchmarks, and show that it is faster than competing frameworks.

Dolphin essentially works by running the symbolic program for every possible combination of input symbols, and tracking the probability of each combination.  The symbolic program is executed on CPU, but Dolphin evaluation will merge different traces of the program which have the same output into batches.  The probabilities can then be computed using batch operations that are GPU-friendly, as well as being end-to-end differentiable with pytorch.

The authors also provide two different mechanisms, which they call provenances, for tracking probabilities.  The DAMP provenance tracks all probabilities, while DTKP tracks only the top-K proofs.

### Strengths
The paper is very well written, and describes the basic execution and batching mechanism clearly, at least for the DAMP provenance.  The Dolphin framework does seem to be an improvement over SOTA in terms of basic usability for certain classes of neuro-symbolic programs.

### Weaknesses
 The authors spend a lot of time talking about the easy parts of the problem, and fail to adequately discuss the hard parts.  As a result, they gloss over two glaring weaknesses that I see with using this approach to solve anything other than cherry-picked trivial problems.  

The first issue is the combinatorics.  When evaluating a function f(A,B), where A and B are distributions over symbols, evaluation must evaluate f(a,b) for every possible combination of symbols { a | a \in A }, and { b | b\ in B }.  Depending on the exact problem, this can easily lead to an combinatorial explosion in the number of possible outputs.  The authors test their code on the "sum of MNIST digits" problem, where the combinatorics are reasonable; even given 20 digits, there are at most 181 possible answers.  If they were to instead try the "product of MNIST digits", which is a tiny change to the code, then the number of possible outputs would balloon, and the technique would likely fail.  

The second issue is control flow.  As a symbolic computation, the "sum of digits" has no loops or branches, and thus is trivially easy to batch.  The authors mention that they support recursive computations, but those generally require a branch to terminate the recursion, and often have divergent control flow.  In the presence of branches, different traces of the program take different paths, and no longer cleanly batch together.  

The usual solution (e.g. in CUDA programs) is that when evaluation encounters a branch, it splits the batch of traces into a then-branch and an else-branch, and then merges the traces together again afterwards.  Without merging, the traces will continue to diverge on subsequent branches, until each trace is operating independently at batch size 1, and the benefits of parallelism are lost.  

Merges happen at the join points in a control-flow graph, which requires the underlying library to build a control-flow graph.  Alternatively, since there are only two batched operations (conjunction and disjunction), the authors could first construct an (unbatched) DAG of operations, and then merge/batch together independent nodes of the DAG after the fact, in the style of Looks et al. "Deep learning with dynamic computation graphs," or Neubig et al. "On-the-fly operation batching in dynamic computation graphs." 

However, the authors make no mention of any machinery to analyze control-flow, build control-flow graphs, or otherwise auto-batch in the presence of divergent control flow.  In fact, they do not even provide a discussion or examples of how to write recursive computations with their library at all, despite claiming that it is possible.  

My main objection with both of these issues is that the authors simply don't discuss these problems at all, when IMO they are very clearly major limitations that affect the kind of programs that Dolphin is able to run.   

A further weakness of the writing itself is that the authors do not do a good job of explaining the DTKP provenance, which seems like it's quite important.  I have several criticisms here.  First, it is possible that choosing only the top-K proofs after each operation will address the combinatorics issue, which would be a big deal.  However, I'm uncertain, because the authors gloss over combinatorics problem altogether without discussion.  Second, the authors claim that their mechanism for merging DTKP tags is equivalent to weighted model counting, but this claim is wholly unsubstantiated.  I didn't really understand the formula in Table 1 at all, including how infinities get into the tags.  At the very least, the authors should provide a detailed discussion of DKTP in the appendix, ideally with a proof of how it relates to WMC, if space within the paper itself is an issue.  

Finally, the authors mention that wrt. to the HWF task, "the DTKP-AM provenance is more effective than DAMP since the tags in DAMP provenance lack the structure needed to capture the semantics of the symbolic program."  This statement seems important, but really requires further explanation; I don't understand it at all.  Providing HWF as a worked example (perhaps in the appendix) would be valuable to anybody who actually wants to use Dolphin.  

Errors:

Line 310: "Its conjuction operation is defined as the addition of probabilities, and its disjunction is defined as the multiplication of probabilities."  Unless my understanding is way off base, shouldn't this be the other way around?  For independent observations, p(A and B) means multiplying p(A) and p(B)?  That's what the authors show in Table 1.

### Questions
Please see "weaknesses" above -- in particular my confusion with the DTKP provenance.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work presents Dolphin, a brand new framework designed to enhance the scalability of neurosymbolic learning. Dolphin allows developers to write differentiable symbolic programs in Python, utilizing PyTorch for end-to-end GPU acceleration. The framework conveys flexible programmability, end-to-end differentiability, scalability, and tunability, which are essential to handling complex programs and large datasets effectively. Experimental results demonstrate that Dolphin significantly outperforms existing frameworks.

### Strengths
- A new framework for neurosymbolic learning, namely Dolphin, is developed.
- Dolphin shows superior performance compared to existing frameworks.

### Weaknesses
My major concern is that the paper is not well structured and hard to follow. In the introduction section, the authors criticized existing frameworks that they must use a separate CPU-based backend and suffer from the slow inter-process data transfers. For me, this is implementation-specific, and it does not drive me to the reasons why we should redesign the entire framework. Although the authors further discuss the challenges in lines 52-67, I find it rather irrelevant to the aforementioned limitation of slow inter-process data transfers.

Moreover, as a new framework, there lacks an overview to depict the layered structures. This prevents readers from having a general picture. It is hard to tell why the designs/implementations could realize the core principles. Additionally, I cannot map the core principles to the challenges discussed in the introduction, either.

### Questions
- It would be better to provide a breakdown of the training time (e.g., according to Figure 1) to justify the major efficiency improvement of Dolphin.
- In Figure 5, for small tasks that all competitors could converge within the time limit, why Dolphin has a better accuracy?
- In Figure 6, there is a trade-off between accuracy and training time for different provenances (DAMP vs. DTKP-AM). How should we select the most suitable one in practice?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Many neurosymbolic frameworks have been introduced in recent years, which typically execute their symbolic component on the CPU. This limits their scalability, due to the inferior CPU performance and data transfer latency between the CPU and GPU. The paper introduces Dolphin, a neurosymbolic framework that is fully implemented by parallel tensor operations, and hence can be run on the GPU using conventional deep learning libraries such as PyTorch. The experiments indicate that Dolphin exhibits considerable speed-ups compared to existing frameworks such as Scallop.

### Strengths
- The problem tackled in the paper (scalable and efficient neurosymbolic learning) is relevant and an important issue for the broader neurosymbolic community. 
- Overall, I feel that the paper is rather well-written and includes several useful figures and examples, resulting in a clear presentation of the ideas. 
- The design of Dolphin seems more accessible to a deep learning audience compared to many existing neurosymbolic systems. Notably, it does not require knowledge of e.g. ASP or Prolog (as is the case for NeurASP or DeepProbLog) and can be integrated easily into a deep learning library such as PyTorch or Tensorflow.

### Weaknesses
 **Novelty**. The key contribution of the paper - speeding up a neurosymbolic framework by tensorizing it and running on GPUs - is certainly not a new idea. One example of prior work is the LYRICS framework by Marra et al. (2019), which also uses tensor operations to perform the symbolic operations in parallel on the GPU (see e.g. Figure 1 in their paper). Logic tensor networks (Badreddine et al., 2022) and Tensorlog (Cohen, 2020) are some additional examples. These frameworks often also support different provenances / semirings / t-norms. The parallelization of neurosymbolic methods with expressive probabilistic semantics is more challenging, but also here there is plenty of existing work (see e.g. Darwiche (2020) or Dang et al. (2021)). Unfortunately, the paper does not mention prior work on parallelized neurosymbolic learning, nor how it is different from these existing methods.

**Semantics**. It is not clear to me what exact semantics Dolphin aims to achieve. The first provenance (DAMP) is essentially fuzzy semantics (which already has been shown to be easily parallelizable, e.g. Badreddine et al. (2022)). On the other hand, “Apply” mostly brute-force enumerates models meaning the necessary independence assumptions for probabilistic sematics can often hold. (c.f. the MNIST-experiment). The second provenance is the top-k semiring, which is less trivial to parallelize. However, the proposed solution of adding the different proofs destroys the top-k semantics (lower-bounding the WMC). This also results in the introduction of clamp operations, which could lead to zero gradients.

**Language**. A distinction from existing methods is that Dolphin introduces its own set of programming primitives (apply, filter, etc.). Previous neurosymbolic frameworks have typically built on an existing language, e.g. Datalog for Scallop, ASP for NeurASP, ProbLog for DeepProbLog, etc. However, there is no justification for the choice of programming primitives. How does its expressivity relate to existing systems such as Scallop? Why wasn’t an existing language chosen? In my opinion, a lot of different choices could have been made (e.g. why do you need ApplyIf instead of just Apply + Filter?).

**Experiments**. I was surprised that the IndeCateR baseline achieved such low accuracy, given that the experiment seems to be the same as in the IndeCater paper, where the reported results are much better. I just tried out the original IndeCateR implementation myself, and I could replicate the MNIST-addition (L) on my machine in 2 minutes. In contrast, the paper reports a timeout after 10 hours. The accuracy also reaches 86.8%, as opposed to less than 10% in the paper (I'm not sure how the paper reports accuracy if it times out). As the code for the baselines is not included in the supplementary material, I hope the authors can clarify these discrepancies. There are additional issues in the experimental section, e.g. there is no mention of hyperparameter tuning, c.f. the questions section. 

Lastly, the performance of Dolphin is claimed to be state-of-the-art but I’ve seen several systems get better results on the considered benchmarks (the comparison is hard as actual numbers are not reported, and only bars). To give just some examples, Orvieto et al. (2023) report 94% for Pathfinder, and Manhaeve et al. (2021) report near-perfect accuracies for CLUTRR. I want to stress that I don’t think state-of-the-art results are necessary, but if they are claimed this should be properly supported.

In summary, the concerns about the novelty of the paper combined with the experimental evaluation issues unfortunately mean I cannot recommend acceptance.

### Questions
- Line 213: “Tags are tensors that represent relative likelihoods”. Relative with respect to what? Relative likelihoods (as I understand it) represent a fraction between two likelihoods.
- The experimental section doesn’t really explain how the CLUTRR and Mugen tasks are solved by Dolphin. E.g. what are the Dolphin programs used here? I think it could be useful to at least include these in the Appendix.
- I found the naming of “Distribution” unclear. Unless I misunderstand it, a “Distribution” isn’t a probability distribution? (E.g. the Filter operation can remove probability mass.)
- How did you perform hyperparameter tuning? Did you tune the baselines in a similar fashion? Given that Table 2 compares total training time, better hyperparameters also affect the reported runtime.
- Why is there such a pronounced accuracy difference between Dolphin and Scallop in some experiments? From what I understand, the provenances like DAMP are essentially inherited from Scallop, so similar accuracy in Scallop should be possible (although not with the same runtime of course).

Minor comments:

- The paper mentions that an “NVIDIA GeForce RTX 4352” was used for the experiments for all experiments (besides CLUTRR). Is this a typo? I’m not aware of the existence of this specific model, and could not find anything about it on the internet. In contrast, the Appendix mentions that a GeForce RTX 2080 Ti was used.
- For Table 2, what is the unit of time? I assume this is in seconds, but I couldn’t find this anywhere.
- For Table 2, what is the provenance used for Dolphin? I assume this is DTKP-AM, but I couldn’t find this anywhere.
- Line 518: “these methods are point solutions”. What do you mean by "point solution"?
- The brackets on the citation on line 107 are wrong.
 - Figure 6 bottom would be more clear with a log y-scale.
- Several citations refer to the arXiv preprint instead of the conference publication (e.g. for neurASP, CLUTRR, and NeuralLog).

### Soundness
1

### Presentation
3

### Contribution
2
