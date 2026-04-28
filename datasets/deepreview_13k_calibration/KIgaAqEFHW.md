# miniCTX: Neural Theorem Proving with (Long-)Contexts

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
Real-world formal theorem proving often depends on a wealth of context, including definitions, lemmas, comments, file structure, and other information. We introduce $\texttt{miniCTX}$, which tests a model's ability to prove formal mathematical theorems that depend on new context that is not seen during training. $\texttt{miniCTX}$ contains theorems sourced from real Lean projects and textbooks, each associated with a context that can span tens of thousands of tokens. Models are tasked with proving a theorem given access to code from the theorem's repository, which contains context that is needed for the proof. As a baseline for $\texttt{miniCTX}$, we tested fine-tuning and prompting methods that condition theorem proving on preceding context. Both approaches substantially outperform traditional methods that rely solely on state information. We found that this ability to use context is not captured by previous benchmarks such as $\texttt{miniF2F}$. Alongside $\texttt{miniCTX}$, we offer $\texttt{ntp-toolkit}$ for automatically extracting and annotating theorem proving data, making it easy to add new projects into $\texttt{miniCTX}$ to ensure that contexts are not seen during training. $\texttt{miniCTX}$ offers a challenging and realistic evaluation of neural theorem provers.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces $\texttt{miniCTX}$, a benchmark of 384 problems with context-rich information, e.g., in-file definitions and lemmas, and evaluates the model's theorem-proving ability under new context, which claims to be closer to the real-world scenario when researchers develop the formal repository. The paper further includes the NTP-TOOLKIT that the authors use for data extraction. The authors provide several baseline experiments, including the common practice of state-tactic tuning and prompting methods (which works for standalone problems as presented in $\texttt{miniF2F}$) and file-tuning that works under such a context-rich setup.

### Strengths
1. The $\texttt{miniCTX}$ benchmark fills the gap in the current community: it expands current benchmarks by addressing the limitations of standalone theorem proving and enabling evaluation in real-world scenarios where context is critical.

2. I appreciate the authors' commitment to automatically updating the benchmark and maintaining a temporal split to mitigate the data contamination, given that most LLMs nowadays crawl GitHub and train on it.

3. The authors present details for constructing the benchmark and the sources. The addition of the $\texttt{miniCTX}$ and the NTP-TOOLKIT will be valuable assets to the community. The authors also present solid baselines in Table 3 using inference-time methods with GPT-4o and fine-tuning methods using 1.3b model. An ablation of providing different contexts is also presented in Table 4 to show the source of gain from each context component.

### Weaknesses
1.  $\texttt{miniCTX}$ does not have a valid/test set separation. Though it's not inherently an issue for a benchmark, separating a valid set could make the benchmark less gameable under Goodhart's law.

2. It seems that some problems in $\texttt{miniCTX}$ are with contexts that could be easily "in-lined" and transformed into context-less problems. For example, the example shown in Appendix A.1: one could easily in-line the square function $s$ definition into the lemma s\_eq\_pow\_two and make the statement to be $x * x = x ^ 2$ from $s \ x = x ^ 2$. The same in-line transformation seems to be also applied to the example in Appendix A.2 by inlining the Rectangle definition. It would be great for the author to assess how many problems in $\texttt{miniCTX}$ could be transformed into context-free problems under certain efforts.

### Questions
1. Is the 1.3b model in L349 the same as the DeepSeek Coder 1.3b in L343?

2. What is the "Environment" in Table 4? Does it stand for the import statements / open namespace statements or something else?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new benchmark called miniCTX for evaluating a model's context-dependent theorem proving abilities, i.e., a model's ability to maximize Expectation_{(theorem, context) ~ repository} Expectation_{proof ~ model(. | theorem, context )} [theorem is valid proof in context]. In-file context includes the source code that precedes the theorem in the file while cross-context includes the in-file context and relevant premises from imported modules. The authors argue that this is a more realistic evaluation of a model's theorem proving abilities. Additionally, the paper introduces NTP-toolkit, a tool for constructing/extending miniCTX with future repositories and running baseline evaluations.

### Strengths
- The paper introduces a useful tool (NTP-toolkit) and benchmark (miniCTX) for evaluating a model's theorem proving capabilities. The Python Lean REPL, provided that it is performant, is another useful component that will enable researchers to more easily evaluate models.
- A benchmark of context-dependent theorem proving and a model that performs well on it could potentially be useful for assisting humans using Lean for formal verification.
- The idea of file tuning, i.e., training model(tactic | theorem, context) is novel.

### Weaknesses
 - The differences between benchmarks shown in Table 1 is, in my perspective, superficial. For example, what fundamental reason is there from preventing other theorem-proving extraction tools from extracting a timestamp or saving the file name that a theorem is extracted from?
- There seem to be a few missing experiments. First, since the temporal split is emphasized, is there any empirical evidence to support the failure of other benchmarks to handle this properly? Second, for file-tuning, have other LLMs / those fine-tuned on Mathlib been tested with file-tuning to see if file-tuning works across different models? Third, In Table 4, I'd like to see context = environment + definition + lemma statement but without natural language comments. This way, we can see just how much having the lemma proof affects file-tuning to better support the claim that models can learn from previous proofs in context.
-  While the paper offers empirical evidence and some analysis, there isn't much in the form of hypotheses to guide the design of the benchmark or experiments. As an example hypothesis, while it might not be surprising that model(tactic | theorem, context) > model(tactic | theorem) since we condition on more information, we hypothesize that the gains come mostly from context = previous proofs since this offers the appropriate context as to when an automated tactic can be most beneficially applied. Such hypotheses would help guide and focus the experiments, and offer more insight into the success and failure cases of neural theorem proving with LLMs.

### Questions
- The weaknesses section contains questions that I'd be curious to hear the answers to.
- Why doesn't the cross-file context include the source code of imported modules as opposed to just the premises? Is this just because of context-length limitations?

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
4

### Summary
This work propose a new formal theorm proving dataset that tests a model's ability to prove formal mathematical theorems that depend on new context that is not seen during training. This work also reports the baseline results of the miniCTX dataset.

### Strengths
* This work provides a new dataset for the theorem proving, which tests the model's ability to prove formal mathematical theorems that depend on new context that is not seen during training. And the ability to use context is not captured by previous benchmarks such as miniF2F.
* The work provides baseline results on miniCTX, telling the difficulty of the proposed miniCTX.
* The work provides detailed analysis on the experiments.
* The work provides details of the miniCTX dataset and samples in the Appendix, which makes it easy to understand what the miniCTX looks like.

### Weaknesses
 * For the Table 3, how do you test the File tuning Model result on miniF2F, as the miniF2F only has the formal statement? You may: 1) only give the formal statement for File tuning Model and get the result; 2) Or, you provide addtional context information by any way?; 
* For Table 3, you do not report the result of GPT-4o (full proof), could you explain why? Previous works (DSP, LEGO-Prover or Lyra) all reports the results GPT-4 on miniF2F.

### Questions
Please check the weakness

### Soundness
4

### Presentation
3

### Contribution
4
