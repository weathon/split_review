# SWE-bench: Can Language Models Resolve Real-world Github Issues?

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Language models have outpaced our ability to evaluate them effectively, but for their future development it is essential to study the frontier of their capabilities.
We find real-world software engineering to be a rich, sustainable, and challenging testbed for evaluating the next generation of language models.
To this end, we introduce \benchmark{}, an evaluation framework consisting of $\num{2294}$ software engineering problems drawn from real GitHub issues and corresponding pull requests across $12$ popular Python repositories.
Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue.
Resolving issues in \benchmark{} frequently requires understanding and coordinating changes across multiple functions, classes, and even files simultaneously, calling for models to interact with execution environments, process extremely long contexts and perform complex reasoning that goes far beyond traditional code generation tasks.
Our evaluations show that both state-of-the-art proprietary models and our fine-tuned model \swellama{} can resolve only the simplest issues. The best-performing model, Claude 2, is able to solve a mere $1.96$\% of the issues. 
Advances on \benchmark{} represent steps towards LMs that are more practical, intelligent, and autonomous.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper primarily describes a benchmark (Swe-Bench) for evaluating language models. The benchmark consists of issues reported in github python repositories. The authors give a detailed description of the criteria they used for constructing the benchmark. They also describe the inputs to the benchmark for evaluation. They finetune the CodeLlama model for the benchmark, and then evaluate this model and others using the benchmark.

### Strengths
The paper addresses a practically relevant issue, that of a benchmark for evaluating language models. The paper is clearly written, and quite a lot of work seems to have been done to support the material in the paper.

### Weaknesses
It seems that none of the models is doing well when the benchmark is used. It would be nice if the benchmark can be used to more clearly indicate where the problem in the language model lies. The results of the model evaluation e.g. difficulty correlates with context length or difficulty correlates with output length are expected and thus do not seem very interesting

### Questions
1) It would be nice if the exact contributions of the paper are stated more clearly.

2) In section1, the authors point out that there is a need for a challenging benchmark that can be used to check the abilities of language models. Although the results have been reported, I am not sure how far they evaluate the specific abilities or weaknesses. The results are general, and seem to apply to all the models without discerning the strengths/abilities or weaknesses of a particular model

3) At this stage, since all the models are performing poorly, perhaps there is a need for a benchmark that is neither too simple, but not as general as SWE-bench? Wouldn't this allow some aspects of the models to be better tested and reported?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce a new benchmark and dataset for testing the abilities of LLMs to edit large code bases.  Previously existing test suites typically involve asking the LLM to generate a small self-contained function when given a natural language description.  In contrast, the new dataset requires the LLM to create a patch, which potentially affects many files across an entire repository, when given a bug report.

Bug reports and repositories were scraped from Github.  Ground truth is a human-written pull request, along with additional unit tests.  Success is determined by whether the patched repository passes additional unit tests that were supplied with the pull request.

The authors conduct numerous experiments with various LLMs, and discover that existing LLMs are (unsurprisingly) very bad at this task.  They analyze and discuss a number of issues as the cause of this failure, such as limited context length, difficulty in retrieving the relevant files from large datasets, poor test coverage, and the requirement that the model output a correctly-formatted patch, rather than ordinary code.

### Strengths
The primary contribution of this paper is the creation of a new dataset and methodology for evaluating the performance of LLMs on real-world software engineering tasks.  The benchmark is well-designed, and can be continually updated and expanded moving forward.  The experiments with existing models are interesting, but they mainly serve to illustrate that this is a difficult and unsolved problem.  

I fully expect this to be a high-impact paper, because other practitioners working in this area can now measure the performance of their models against the new benchmark.  In addition, the analysis and discussion provided by the authors provides a good starting point for guiding future research in this area. 

The qualitative analysis, which compares LLM-generated patches against human-generated patches was also quite insightful.

### Weaknesses
Generating a patch file, and generating code, are two very different tasks.  Existing models are pretrained on code, not patch files, so at least some of the poor performance could simply be due to the fact that the models are operating out of distribution on this data set.  (The authors mention this issue in the paper.)

There is an additional issue with the way pretraining for code LLMs is typically done.  Due to context length limitations, the LLM often does not even see a complete file, much less a complete repository.   Moreover, the code fragments that are used for pretraining do not indicate what file they come from.  

In contrast, in order to generate a good patch file, the model must be able to see the file and directory structure of the repository.  How do you handle file names and directory structure in your experiments?

### Questions
There is an additional issue with the way pretraining for code LLMs is typically done.  Due to context length limitations, the LLM often does not even see a complete file, much less a complete repository.   Moreover, the code fragments that are used for pretraining do not indicate what file they come from.  

In contrast, in order to generate a good patch file, the model must be able to see the file and directory structure of the repository.  How do you handle file names and directory structure in your experiments?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors aim to determine if LLMs can resolve real world software issues (vs constructing or fixing toy programs). Authors propose SWE-bench, a benchmark based on GitHub issues. They apply LLMs to try and fix these real-world issues and discover very poor performance.

### Strengths
- Authors present a good real-world problem benchmark based on real product sized GitHub repositories and real issues fixed in them.
- Fine tune CodeLlama 7B and 13B models to get at least somewhat positive performance on repository-wide code edits
- Propose retrieval methods to compose input for LLMs to fit into LLM context size.
- Evaluate LLMs on the benchmark and present general lessons from the results.

### Weaknesses
 - Although benchmark and LLM evaluation on it are valuable, the paper does not present any novel solutions to the task in the benchmark. This limits the contribution.
- Please reorganize the paper so tables and figures are collocated with the text. Currently, it is hard to read when tables referenced out of order and explained very far from their location in the paper.
- This sentence, especially its last part, is unclear: "We compare the BM25 retrieval results against the oracle retrieval setting in Table 3, where we see that BM25 retrieves a superset of the oracle files in about 40% of instances with the 27,000 token context limit but only also excludes all of the oracle files in over half of instances.". I think this is trying to explain the results in Table 3 and trying to say that in around half cases BM25 does not retrieve any of oracle files. Is this what you are trying to say? Please explain or rephrase.

### Questions
This sentence, especially its last part, is unclear: "We compare the BM25 retrieval results against the oracle retrieval setting in Table 3, where we see that BM25 retrieves a superset of the oracle files in about 40% of instances with the 27,000 token context limit but only also excludes all of the oracle files in over half of instances.". I think this is trying to explain the results in Table 3 and trying to say that in around half cases BM25 does not retrieve any of oracle files. Is this what you are trying to say? Please explain or rephrase.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new benchmark, SWE-bench, which collects code and issues from 12 Python repositories. This benchmark also considers the convenience of subsequent evaluation, and the test code for relevant issues is included. Moreover, this paper also finetunes Code Llama with SWE-bench training data. Experimental results show that there are still many challenges for existing LLM to solve real-world issues.

### Strengths
1.	The paper is generally well-written.
2.	This paper introduced a new dataset SWE-bench that contains 2294 GitHub issues and related test scripts. The dataset can be used to evaluate the methods for resolving real-world GitHub issues.

### Weaknesses
1.	Some of the comparison is not very fair. As Claude 2 is trained on data up to early 2023, GPT's knowledge cutoff is September 2021 and there is no specific time for Code Llama’s training data, evaluating these models on the dataset that contains instances before 2023 is not fair enough.
2.	The contribution of SWE-Llama is not significant, especially for an AI conference. The paper could better target a software engineering/programming conference.
3.	This method is mainly based on Code Llama while there is no comparison between Code Llama and SWE-Llama.
4.	Some of the experimental analysis is not solid enough. For example, in the “Difficulty correlates with output length” (Section 5), Table 8 only presents all successfully applied patches, and does not show the correlation between difficulty and output length. The length of other patches needs to be taken into account.
5.	There are a lot of work on automated bug fixing, including LLM-based ones and traditional ones. The authors could discuss and compare. For example:
Jiang et al., Shaping Program Repair Space with Existing Patches and Similar Code, Proc. ISSTA 2018.
D. Sobania, et al., An analysis of the automatic bug fixing performance of Chatgpt,arXiv:2301.08653, 2023.

### Questions
1.	As the experimental results of GPT-4 are on a 20% random subset of SWE-bench while there is no comparison of other models on the same subset. If we only look at this part of the subset, are all the conclusions in the paper still valid/consistent?
2.	Why are these 12 Python repositories chosen as the source of the benchmark? Does the selection of the programming language and repository influence the results of the comparison?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
