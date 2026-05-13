# AST-T5: Structure-Aware Pretraining for Code Generation and Understanding

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Large language models (LLMs) have made significant advancements in code-related tasks, yet many LLMs treat code as simple sequences, neglecting its structured nature. We introduce \model, a novel pretraining paradigm that leverages the Abstract Syntax Tree (AST) for enhanced code generation, transpilation, and understanding. Using dynamic programming, our AST-Aware Segmentation retains code structure, while our AST-Aware Span Corruption objective equips the model to reconstruct various code structures. Unlike other models, \model avoids complex program analyses or architectural changes, so it integrates seamlessly with any encoder-decoder Transformer. Evaluations show that \model consistently outperforms similar-sized LMs across various code-related tasks including HumanEval and MBPP. Structure-awareness makes \model particularly powerful in code-to-code tasks, surpassing CodeT5 by 2 points in exact match score for the Bugs2Fix task and by 3 points in exact match score for Java-C\# Transpilation in CodeXGLUE.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a pretraining paradigm for code models consisting using AST-aware methods. Specifically, it presents two main techniques: (1) A method of segmenting examples to minimize AST breakage and (2) a span corruption technique that minimizes AST subtrees cutting instead of randomly choosing.

Update: My score has been adjusted to reflect the concerns addressed by the authors.

### Strengths
While AST information use in code LLMs is not novel, the combination of using this information in segmentation and T5-style span corruption in pretraining is original and interesting.

### Weaknesses
 - Performance comparisons to other models require more supporting evidence
  - Given the lack of models for comparison at this scale (in particular for generation tasks with more N/A than results in the chart), showing these results at a scale with more models to compare directly against would have made the performance differences more abundantly clear and understanding the scaling characteristics would make for a much more compelling argument.
  - HumanEval has been known to have been in public datasets (such as Github Archive) commonly used for training code LLMs (https://arxiv.org/abs/2306.11644) and being that it is an incredibly small dataset of questions and only Python, it would a stronger argument for performance to show the Pass@1 vs Model Size graph for other common reported downstream evaluations to support the claim of "competitiveness against larger models". I understand that there are not many code generation evaluations that are common between most models, but I would suggest at least adding MBPP (present in Llama, PaLM, GPTs, etc) and consider showing performance across more languages through benchmarks such as MBXP and Multilingual HumanEval (https://arxiv.org/abs/2210.14868).
- This sentence in the abstract: `Structure-awareness makes it particularly powerful in code-to-code tasks, surpassing CodeT5 by 2 points in Bug Fixing and 3 points in Java-C# Transpilation.` needs to be contextualized better or a different summary of results should be presented. The significance of these results are ambigious.
- Typo: "avilable" typo in page 9 last line of first paragraph

### Questions
1. What are some potential limitations of using this method? 

2. Were masking ratios tested between 25% and 100%? If 25% showed no degradation in understanding tasks, why not go higher?
From paper: 
```
we observed that raising the mask ratio from 15% to 25% significantly improved generation capabilities without noticeably compromising performance in understanding tasks. Thus, we settled on a 25% mask ratio for our AST-T5 model.
```
3. Code completion (generation with both prefix and suffix context) has become a very common capability in code models and the span corruption objective is effectively code completion. Was there work done on evaluating this model for code completion tasks? Why or why not?

4. The abstract mentioned anonymized model + code, where is this available?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors introduce a new way of pre-training generative models for code which has two innovations:

First, when dividing long source code files into smaller segments for training purposes, the authors choose segmentation boundaries that align, as much as possible, with the abstract syntax tree (AST) for the code.

Second, when masking out spans of text, where the model is trained to reconstruct the masked spans, they mask out spans that correspond to nodes in the AST.

Experiments show that these two changes to the training task result in significant improvements in model quality.  No changes are made to the transformer model architecture, or to the training data set.

The authors compare the performance of a single model which is pretrained with AST-aware segmentation and masking to the performance of the same sized model which is pretrained with conventional segmentation and masking.  They also compare their model against other models (with different sizes and architectures)  in the literature.

### Strengths
The paper is well written and the ideas are presented clearly.  The experiments also seem to be well-designed, and adequately support the authors conclusions.  

The most interesting thing about this paper is that the authors are able to achieve significant improvements, just by changing segmentation and masking.  There are no changes to the actual training data or to the transformer architecture.  The use of code structure has, IMO, been underutilized in code LLMs to date, so this paper outlines a simple and effective technique that other practitioners can implement.

### Weaknesses
The main weakness of the paper is that it only investigates these two simple changes.  There are many other previously published ways of utilizing AST structures in a transformer architecture, e.g. tree-position embeddings, augmenting the attention matrix with tree/graph structure, etc.  Many of these changes would not be hard to implement.  I would have been very interested to see a more comprehensive comparison of various techniques.  E.g. how does masking (in this paper) compare against providing tree-position embeddings for the AST?  Does AST-aware attention eliminate the benefit of AST-aware masking, or do they compliment each other?

Experimentally, this paper uses a context length of 1024 tokens, which is very small for code.  The benefit of AST-aware segmentation will diminish with increasing context length, so some of these results may not apply to larger models.   

The related work section also needs to be fleshed out, in particular with regards to "leveraging code structure in pretraining."

### Questions
There is less need for good segmentation boundaries when training with longer contexts.  Have you attempted to see whether your results still hold for model that are trained on longer contexts, e.g. 8k or 32k tokens?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- This work proposes AST-aware segmentation of code into chunks to smartly chunk code into contexts causing the least disruption of syntax trees.
- Building on top of AST-aware segmentation, this work proposes an AST-aware subtree corruption pre-training objective instead of the standard random corruption objective to mask well-formed code segments.
- Using this sole pre-training objective, this work pre-trains a T5 model of 226M parameters on code data from GitHub and NL data from Wikipedia and OpenWebText.
- Evaluating AST-T5 on downstream tasks such as code transpilation, code generation, and code understanding, the work shows better performance of the AST-T5 model as compared to other comparable models.
- Through ablation studies, the work demonstrates the benefits of AST segmentation and AST subtree corruption separately.

### Strengths
The proposed method is a simple yet useful way of utilizing code syntax trees in model pre-training that results in better performance. I do believe that utilizing AST to better design pre-training objectives code has a lot of merit, and this paper presents an interesting approach to how to think about code segmentation and masking, and how it affects model performance.

### Weaknesses
 - The work refers to trees created by the tree-sitter library as ASTs, but the tree-sitter library actually creates a Concrete Syntax Tree and not AST. While the two are related, CSTs are precursors to ASTs and are more verbose. See [1], [2], [3] for more details.
- What is the rationale behind including explicit NL data in the pre-training corpus? Prior works in this space such as CodeT5, PLBART, and GraphCodeBERT all have only code data in their pre-training mix. Is this a side-effect of the AST-aware masking strategy, where comments in code are not masked, and thus rather than including a new task - such as the Bimodal dual generation task in CodeT5 - this work requires NL data?
- I have the impression that the AST Subtree Corruption objective is more important than AST-aware segmentation because, for the defined objective, the model is learning to unmask spans masked in an AST-aware manner through the AST Subtree Corruption. The remaining context (code), even if incomplete from an AST point-of-view might not be affecting the learning significantly. Is it possible to do an ablation study with base T5 + AST Subtree Corruption to assess the performance? Since this work utilizes tree-sitter, which is an incremental parsing library, it is possible to parse even incomplete code.
- For Concode, Bugs2Fix, and Java-C# translation tasks, the work reports the Exact Match (EM) score alone. EM is not an ideal measure for code as it measures string equivalence. Other fuzzy evaluation metrics such as CodeBLEU [4] or CodeBERTScore [5] scores might be a better fit for these tasks.
- While the work does a good job of covering a decent number of downstream tasks, any specific reason why Code Summarization tasks were not included? The pre-training dataset for the model does include explicit NL data, so I expected to see code-to-text tasks included as well.
- In section 4, the authors mention utilizing PromptSource to create prompt templates for fine-tuning. I might be wrong, but it is my understanding that prompts are more useful in zero/few-shot settings. If the authors are fine-tuning the model, why is a prompt required? Why can't the model be fine-tuned on input-output pairs directly?

### Questions
mentioned above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
