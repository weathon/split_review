# Training Language Models on Synthetic Edit Sequences Improves Code Synthesis

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Software engineers mainly write code by editing existing programs. In contrast, large language models (LLMs)  autoregressively synthesize programs in a single pass. One explanation for this is the scarcity of open-sourced edit data. While high-quality instruction data for code synthesis is already scarce, high-quality edit data is even scarcer. To fill this gap, we develop a synthetic data generation algorithm called LintSeq. This algorithm refactors existing code into a sequence of code edits by using a \emph{linter} to procedurally sample across the error-free insertions that can be used to sequentially write programs. It outputs edit sequences as text strings consisting of consecutive program \textit{diffs}. To test LintSeq, we use it to refactor a dataset of instruction + program pairs into instruction + program-diff-sequence tuples. Then, we instruction finetune a series of smaller LLMs ranging from 2.6B to 14B parameters on both the re-factored and original versions of this dataset, comparing zero-shot performance on code synthesis benchmarks. We show that during repeated sampling, edit sequence finetuned models produce more diverse programs than baselines. This results in better inference-time scaling for benchmark coverage as a function of samples, i.e. the fraction of problems ``pass@k'' solved by any attempt given ``k'' tries. For example, on HumanEval pass@50, small LLMs finetuned on synthetic edit sequences are competitive with GPT-4 and outperform models finetuned on the baseline dataset by +20\% ($\pm$3\%) in absolute score. Finally, we also pretrain our own tiny LMs for code understanding. We show that finetuning tiny models on synthetic code edits results in state-of-the-art code synthesis for the on-device model class. Our 150M parameter edit sequence LM matches or outperforms code models with twice as many parameters, both with and without repeated sampling, including Codex and AlphaCode.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes LintSeq, which is a synthetic data generation algorithm that generates edit sequences from raw code to construct training datasets for LLMs. Specifically, to let LLMs learn to write code by editing existing programs like human developers, LintSeq first refactors existing code into a sequence of code edits, where each edit is an error-free insertion, and then outputs edit sequences as text strings consisting of consecutive program diffs. Evaluation shows that, after training LLMs on the synthetic edit sequences, the inference-time scaling performance of LLMs on HumanEval and MBPP improves significantly.

### Strengths
- The paper explores an interesting and important research direction.
- The idea of constructing fine-tuning datasets that mimics human developers’ behavior by synthesizing edit sequences is novel.

### Weaknesses
 - The synthesized edit sequences may not be reasonable. While LintSeq ensures that the program at each step of the edit sequence does not contain any static error, it does not necessarily guarantee that this edit sequence is reasonable because a valid edit sequence should reflect the reasoning/thinking process of human developers, which is not guaranteed by LintSeq. Furthermore, edit sequences synthesized by LintSeq only contain insertions, which is also different from real-world edit sequences. The lack of deletions or modifications limits the diversity of the generated data and may not fully capture the complexity of code evolution.
- The comparison between “LintSeqInstruct” and “Instruct” may not be fair enough. While authors have controlled the number of optimizer steps the same, it is also important to make sure that “LintSeqInstruct” and “Instruct” share the same valid training tokens (i.e., the number of tokens in the training sequences that are not padding tokens). Although sharing the same number of optimizer steps, it is still possible that each training sequence in “LintSeqInstruct” is much longer than that in “Instruct” and thus more training tokens are provided for “LintSeqInstruct”. This discrepancy in training data volume could lead to an overestimation of the benefits of LintSeq.
- Evaluation is not comprehensive enough. Apart from HumanEval(+) and MBPP(+), more benchmarks should be included to further demonstrate the effectiveness of “LintSeqInstruct”, such as DS-1000, APPS, and LiveCodeBench. The current evaluation is limited to relatively simple code generation tasks, and it is unclear how well LintSeq would perform on more complex or specialized coding challenges. The absence of results on datasets that test different aspects of code understanding and generation limits the generalizability of the findings.

### Questions
- What are the computational resources required to synthesize edit sequences using LintSeq? If it is cost friendly, will it also be able to improve pre-training performance?

### Soundness
2

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
The paper introduces LintSeq which is a proposed method to tune LLMs for programming tasks. Data preparation consists of representing code generation as a sequence of edits. To construct the edits, there is a 2 step process broadly, first deleting lines from an existing program to create potential intermediate states, and using a linter to reject intermediate states that are syntactically incorrect or fail other kinds of static linting tests. The authors demonstrate the merits of this approach for small language models and large language models, comparing LLMs tuned with LintSeq to plain instruction-tuned models. The authors also ablate the importance of the linter-based filtering step, showing that this step is important to its success. The authors also demonstrate and explain that LintSeq-tuned models may sacrifice inference-time compute in exchange; however, in turn for higher performance on program synthesis benchmarks.

### Strengths
The results speak for themselves: the authors demonstrate LintSeq is capable of substantial performance improvements over instruction-tuned models. The authors are transparent that LintSeq may sacrifice inference-time compute for improvements in the efficient use of parameters and its strong program synthesis abilities. And the authors' ablation demonstrates that the use of a linter (to reject poorly formatted code edits) is important to the success of LintSeq. 

In terms of intellectual merit, LintSeq is not the first work to suggest leveraging edit sequences for training language models for programing tasks. However, LintSeq is notable for getting these ideas to work at scale. To my best knowledge, much prior work may have focused on using human edits such as github commits, which is limited by the number of demonstrations available. Here: the authors introduce a procedure that is not bounded by the number of human demonstrations available, but rather the availability of a linter or even more loosely, a static-analysis based tool for checking the well-formedness of programs (e.g. tools often found in a compiler). 

In terms of significance, the authors are able to demonstrate LintSeq's ability to improve over instruction tuning for a series of code LLMs. However, LintSeq also may have significance for real-world coding applications. The authors mention that commercial code assistants like Cursor deliberately do not use edits; however, the case study of LintSeq may inspire new approaches for code-editor assistants (it could also potentially have issues as well). Additionally, the set-up of LintSeq may also motivate applications for incremental generation of natural langauge responses, especially for tasks that may be intensive in reasoning.

### Weaknesses
The authors' work is very strong, however, there are some important points that need discussion. Overall, my largest concerns are with transparency, clarity, and integrity in presentation. I myself felt mislead multiple times while reviewing this paper, and that concerns me greatly. 

1. Misleading Presentation of Models >1B parameters / Transparency + Clarity 

I found figure 1 to be misleading. It compares leading LLMs on Human Eval with K=1 to LintSeq with K=50. Personally I didn't catch this until I glanced over the paper after at least multiple passes, I would fear other readers may fall into the same trap and overestimate how strong LintSeq is. In reality, LintSeq Pass@1 is can equal to or even significantly worse than an instruction-tuned variant of the same base model. 

It is only in the appendix in Tables 10 and 11 where the authors clearly present LintSeq vs Instruciton-Tuning pass@1, pass@5, etc rates; although similar information is presentated in figure 4. With pass@50 LintSeq is significantly better than instruction-tuned models; whereas, it is negligible or worse with few or one/fewer samples. I believe there is no thorough discussion of this phenomenon in the main manuscript and this is an extremely important point. For example, the authors could offer an explanation that LintSeq increases the generation diversity which is highlighted in the higher pass@50. The authors must be more forthcoming about the tradeoffs of LintSeq when model size is scaled up. I urge the authors to reframe the presentation and discussion to clearly reflect this.  

I would also appreciate a comparison with other top LLMs for code (e.g. LLama3 or LLama3.1; CodeLLama, DeepSeekCoder, Gpt3.5) and comparisons with equal pass@1, pass@5, pass@10 to show how these other LLMs scale with more samples. I feel very mislead by Figure 1 comparing Pass@1 for big models vs. pass@50 for LintSeq and I am left feeling such a presentation is problematic. I feel uncertain about  the motives in presenting Pass@1 vs. Pass@50 without a fair like-to-like comparison between other LLMs and putting tables 10 and 11 deep in the appendix. The authors must present a more forthcoming picture of the strengths and weaknesses of LintSeq when scaled up >1B parameters. I think the paper requires a significant revision to reflect this in language. I believe the technical contributions could already be there, but the presentation feels very misleading to me and the discussion should center much more on the tradeoffs that LintSeq introduces.

2. Framing and Explanation of LintSeq

I find the framing of LintSeq or the explanation of it is not easily clear, and even after section 2.2 where it is broken down into phase 1 and phase 2, it is still unclear to me. This led me to inspect the artifact `lintseq` in the supplementary materials which is >300 lines of code and mentions sampling weights, computing fitness, and "children." Perhaps there's something going on where in the paper "affected lines" are the indented lines of a code block. The description is not sufficiently clear, and I recommend more clarity in the presentation of the algorithm for both transparency and reader understanding. I would not call this "recursively lint" as shown in figure 2, as linting doesn't edit code, so the recursive process needs to be combined with some editing process as menitoned in section 2.2: "(2) run a linter or other
verifier on the remaining code; (3) if the deletion induced new errors, remove all affected lines; and (4) repeat steps 2 and 3 until no errors are caught by the linter." To me, the "remove all affected lines" is unclear to me and I'm not sure if all writers of the paper fully understood the procedure either. I recommend trying to formulate a more thorough explanation both in the main manuscipt and also if this is not sufficient to add an appendix section explaining the procedure in more detail. Pseudocode / pythonic pseudocode may also help to demonstrate this procedure. 

2. Claims of Tiny LMs is Misleading 

I'd recommend the authors walk back the claims on their Tiny LMs. I find the statement "Our 150M parameter edit sequence LM matches or outperforms code models with twice as many parameters" misleading: the 150M parameter model underperforms CodeT5+ 220M at Pass@10 HumanEval and underperforms Codex 300M at Pass@1. 

3. Discussing Prior Work

The authors only mention 2 works from 2023 and 2024 on fine-tuning on edits. Some papers that came to my mind while reading this were: 
https://arxiv.org/abs/1810.13337
https://arxiv.org/pdf/1905.11006 (much less related)

This makes me inclined to think that there may be more works that I have not included here that should be discussed to highlight the history of thinking on this issue. 

4.  Choice of Language 

The term `static program verifier` makes a loose use of the word "verify." I recommend using a different word from "verify" to not conflate it with [formal verification](https://en.wikipedia.org/wiki/Formal_verification) of programs. 

Also in the abstract "small LLMs" is a contradiction of sorts "small Large Language Models."

### Questions
Generally, this is a re-hashing of the weaknesses

1. Could you please describe the algorithm for LintSeq more clearly, and I'd strongly also recommend updating the paper to reflect a more clear explanation (e.g. PseudoCode or a more lengthy explanation in natural language in an appendix section). 

2. Did I misrepresent or misunderstand your claims? Please feel free to disagree if I have missed something.

3. Could you provide comparisons to other commercial LLMs (e.g. Gpt4o, the updated Sonnet 3.5, Gpt4o-mini, Haiku 3) and open LLMs (e.g. the most recent LLama3-Instruct 70b, Llama3-Instruct 8b, DeepSeekCoder 7b instruct, DeepSeekCoder33b Instruct) on MBPP and HumanEval with higher samples, and demonstrating pass @N as you did in tables 10 and 11. 

4. For the models in tables 10 and 11, is it possible to also compare lintseq best@50 to instruction-tuned models best@50, except with Top p = 1.0 and temperatures [1.0, 1.1, 1.2]? This is important to also establish if the increase in diversity of lintseq cannot be matched by modulating the temperature for sampling. 

5. Are there other ways to calculate estimated FLOPs as you have? Would it be possible to also tell me the wall clock time of running inference using the instruction-tuned models and compare that to the wall clock time of using the LintSeq models (e.g. both 14b models compared) just for more transparency.

### Soundness
3

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
5

### Summary
This paper looks at the problem of code generation. The corpus trains LLMs to generate code from left to right. Yet, this paper proposes to generate synthetic code edits that train the model to construct code in a step-by-step fashion, while encouraging each step to preserve the syntax validity of the code. This technique is evaluated to be effective for SLMs esp. when doing inference scaling.

### Strengths
- This paper looks at an important domain in generative AI -- code generation.
- The overall idea of processifying code generation makes sense to me -- decomposing the code generation task into code insertions allows the model to construct the generated code with more diverse context possibilities in addition to the simple left-to-right context

### Weaknesses
 - **Novelty & related work**: LintSeq reminds me of the code sketch paper [1] which generates code via syntax-validity-preserving edits (i.e., filling grammar holes). This paper should be discussed (and compared if applicable).
- **Technique**: One theoretical limitation of LintSeq is the lack of naturalness of synthetic edits. The data trains the model on random trajectories which might (if not always) not be meaningful.
- **Technique**: Code edits in LintSeq are *insertion-only* -- I can imagine cases deletion/rewriting can be used, such as writing a bunch of `def f(): pass` when planning the code skeleton and replacing the "pass" when real implementation starts.
- **Evaluation**: overall I feel the evaluation focuses on function-level code generation, which might look a bit contradictory to "inference scaling" -- as I'd expect to use inference scaling for solving much more challenging tasks, e.g., those in SWE-Bench.
- **Presentation**: "Open-source edit data with good coverage over the distribution of all error-free code “diffs” is nonexistent" is debatable given high-quality code-edit datasets such as EditPackFT.
- **Presentation**: The terminologies in this paper can be made more precise (detailed comments below).

----
Comments on writing:

- Fig 1: "HumanEval Coverage" and its use in many other places: maybe just explicitly say pass rate or pass @ k -- "coverage" by default means code coverage in the code generation domain and it might be confusing to refer it to pass rate.
- L065: authors should explicitly explain what "static-error-free" means -- is it program syntax error? or the error of the diff syntax, etc.
- L080 "static program verifier" and "error-free program states": how is it possible to verify an arbitrary program state "error-free" statically? :) -- Similar to the comment above, some basic concepts need to be explicitly clarified and defined.
- L084 "verifier ... is also referred to as a linter": linters and verifiers are very different concepts. linters mostly do static syntax-based checks on certain surface-level program properties. Verifiers are way more ambitious as they assure the existence/absence of program properties given all possible inputs/states (nonetheless, the meaning of verifiers has been extended to validators to assure behaviors over "certain" rather than "all" inputs/states). 
- L107 "A linter is a type of standard code analysis tool that verifies the correctness of program" -- the statement is too strong to be right. Linters cannot verify program correctness but just check a few syntactical issues.

**Actionable suggestions**: for these "linters", "correctness", and "verifiers" terms, it's more precise to say "apply linters to make sure each edit can preserve the program's syntactical validity/well-formedness".

### Questions
- Novelty-wise what is the paper's main difference compared to the code sketch paper? 
- Code diff is more than just insertion -- why deletion and rewriting are not considered?
- Why disabling chain-of-thought data?
- Why pre-training TinyCodeLM instead of reusing existing pre-trained SLMs?
- Can you try sampling the model using min-p rather than top-k?
- What's the intuition on why LintSeq can improve pass@1? It makes sense to me it can improve pass@ big K as the approach optimizes code generation diversity but it's interesting to me that it also gets higher pass@1 (i.e., higher-quality first sample).

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a new algorithm, LintSeq, which generates synthetic code editing sequences from existing programs. It reframes code generation as a sequence of edit generation tasks, mimicking human coding. They applied the method to create instruction + program-diff-sequence to train smaller LLMs for code synthesis. Models finetuned on these edit sequences generate more diverse programs and improve performance on benchmarks, achieving up to +20% higher scores on HumanEval pass@50 compared to baseline finetuning. Additionally, a 150M parameter model fine-tuned on these edits achieves state-of-the-art performance in code synthesis for on-device models, competing with larger models like Codex and AlphaCode.

### Strengths
- The idea is novel. While existing models often separate code generation and editing tasks, this paper presents a perspective to unify them into sequence of editing tasks. It's an interesting directions researchers can explore in the future.
- To prepare the training data, the authors proposed LintSeq, which refactors existing programs into sequences of static error-free code edits. This is a smart combination of program analysis and LLM.
- The pretraining experiment gives a better understanding of the effectiveness of the technique.

### Weaknesses
 - The authors only evaluated the models on HumanEval and MBPP. While these two benchmarks are popular for most general-purpose LLMs, they are biased toward simple programs and do not cover practical coding scenarios.
- The paper used a Python-specific linter `pylint` to construct pretraining data, but it's unclear how this approach can be easily applied to other languages and be applied at scale. Specifically, the reliance on `pylint` introduces a strong bias towards Pythonic coding styles and may not generalize well to languages with different paradigms or linting rules. The paper lacks a discussion on how the specific rules enforced by `pylint` might influence the generated code edits and the resulting model behavior.
- There is not enough justification for the base models used for finetuning. Why no base code LLMs? The choice of base models seems arbitrary and the paper does not provide a clear rationale for why these specific models were chosen over other available options, especially those pre-trained specifically for code. This lack of justification makes it difficult to assess the true impact of the proposed method.
- There is an overemphasis on pass@k when k is large. While a better pass@ larger k shows the LLM can cover a broader code distribution,  by definition, pass@1 is more practical and is what people care about more.

### Questions
1. See the weaknesses above.
2. Besides simple code generation tasks on HumanEval and MBPP, does this approach work for practical coding such as BigCodeBench? Also, does training on edits improve code editing tasks, say CanItEdit?
3. How does this approach handle a code file that depends on other files in a repository? In such cases, applying the linter only to the code file will raise an error.
4. For code generation tasks requiring multiple programming languages, does the same methodology still work?

Open to increase the score if the above concerns are properly addressed.

### Soundness
3

### Presentation
3

### Contribution
2
