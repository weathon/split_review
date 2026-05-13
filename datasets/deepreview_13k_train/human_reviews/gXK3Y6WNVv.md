# Defects4C: Benchmarking C/C++ Faults to Assess LLM-Based Program Repair

- Decision: Reject
- Scores: 6, 6, 5, 3

## Abstract
Automated Program Repair (APR) plays a pivotal role in ensuring the quality and reliability of software. However, most existing APR research focuses on Java programs, primarily due to the well-established benchmark such as Defects4J. Despite the significant prevalence of C/C++ vulnerabilities, the field lacks extensive research on the automated repair of such vulnerabilities, primarily attributed to the absence of high-quality open-source benchmarks in this domain.

To address the critical gap in available datasets for C/C++ program repair, this paper introduces Defects4C, a comprehensive and high-quality executable benchmark designed to improve defect detection and repair. The dataset includes a vast collection of bug-relevant commits (e.g., **9M** in total), **248** high-quality buggy functions and **102** vulnerable functions paired with test cases for reproduction. These datasets can be used to evaluate repair techniques and to retrain learning-based methods for improved performance. Using this expanded dataset, we evaluate the performance of state-of-the-art LLM-based automated program repair techniques in addressing C/C++ faults. Specifically, we conduct an extensive empirical study with **24** leading LLMs. Our findings provide valuable insights into the capabilities and limitations of existing APR approaches for C/C++ programs, underscoring the necessity for novel APR techniques and the significance of Defects4C. This dataset marks a significant advancement in the field, offering a robust and comprehensive C/C++ dataset that is instrumental for future research on program repair.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper develops a benchmark for Automated Program Repair (APR) in C/C++ programs. The authors curate a dataset of C/C++ bug-fixing commits, apply systematic filtering, and use human annotations to ensure data quality. The benchmark is evaluated through various experiments using multiple large language models (LLMs), with a comprehensive analysis of the results. The main contribution is providing training set and a benchmark for C/C++ APR task, which can be used for evaluating code LLMs.

### Strengths
- The authors introduce a new benchmark for APR with C/C++ with human annotation.
- The benchmark has been well-categorized. 
- A training set for APR tasks in C/C++ is available.

### Weaknesses
 - Human Annotation Process: More details about the human annotation process should be discussed in Section 3.3. Please refer to Questions for suggestions.

- Experimental Results: The authors only represent the performance of LLMs. The performance of traditional APR methods is missing. The authors also miss some of the latest LLMs with the most competitive performance on other benchmarks. Please refer to Questions for suggestions.

- Presentation: Some contents should be relocated to make the paper more organized. The paper contains some issues on grammar and style of writing.

  - The introduction is lengthy; some contents could be relocated to Related Work or Benchmark Construction. For example, paragraphs describing the dataset collection could be made more concise (line 81 to 103).

  - Line 83: Change “vulnerability functions” to “vulnerable functions.”

  - Line 241: Explain CWE upon its first use.

  - Line 383 in Table 3: Correct “GPT-35-Turbo” to “GPT-3.5-Turbo.”

### Questions
- Human Annotation Process:
  - In lines 248-249, you mention that half of the bugs were reviewed in the third round. What about the other half? Does this imply that some parts of the dataset received two rounds of annotation, while others received only one? Additionally, is the reported Cohen’s Kappa calculated based on only the reviewed half or all annotated commits?
  - In line 255, it’s noted that 248 commits were identified for Defects4C_bug. This is a significant reduction from the original 3,785 commits. Does this reduction imply that the remaining commits in the 3,785 were deemed non-bug-related, which could affect training set quality, or were only a portion of the 3,785 commits annotated by human experts?

- Experimental Results:
  - Could you include some traditional APR methods as baselines in Table 3? The paper frequently claims that LLMs perform well, and a traditional baseline would strengthen the claim.
  - For close values in Table 6, standard errors are needed to support the claim that fine-tuning improves model performance.
  - Including evaluations of the latest general-purpose LLMs, like GPT-4o(-mini), Claude3, Gemini 1.5, or even o1-preview, would be helpful. Testing one or some of these models could demonstrate how recent models perform on C/C++ APR tasks. 
  - Given that Defects4J is an older dataset, it’s possible that knowledge contamination is affecting model performance. Conducting a case study on this potential contamination could provide valuable insights. Furthermore, are there methods to prevent your benchmark from contaminating future LLM knowledge?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents Defects4C, a dataset of defects in C/C++ mined from open-source repositories using specific commit messages. Defects4C first collects bug-relevant commits, verifies the repositories and commits still exist, and performs certain filtering (e.g., making sure the commits address a single function). Then, it further splits the collected commits into Defects4C_bgcommit, Defects4C_bug, and Defects4C_vul. The datasets Defects4C_bug and Defects4C_vul are rigorously verified by real-life human experts. To understand the effectiveness of LLMs in Automated Program Repair (APR), the authors perform an inference-only and fine-tuning experiments on 24 widely used LLMs. The experimental results indicate LLMs fall behind in fixing C/C++ bugs compared to Defects4J (Java bugs). The authors further introduce a tool for better interacting and reproducing bug datasets.

### Strengths
- Mining software repositories to collect C/C++ bugs
- Human analysis of collected bugs and creating bug taxonomy
- Open-sourcing a tool to better interact with the collected bugs
- Large scale study of the effectiveness of multiple LLMs in APR on collected bugs
- Fine-tuning existing LLMs to understand the effectiveness of Defects4C_bgcommit

### Weaknesses
 - No comparison with other C/C++ bug datasets in the task of APR.
- Some results in Table 3 does not make sense. For instance, why Magicoder result is all 0s. Is there any analysis to root cause this problem because Magicoder is a good model

### Questions
Q1. Given that most people are interested in migrating to Rust (because of memory safety features), and there has been research on code translation between C to Rust (https://arxiv.org/pdf/2404.18852), why do you think a dataset of bugs for C/C++ would be worthwhile?

Q2. Have you performed some more analysis on why a model like Magicoder produces 0.0 as result? Do you think the right prompt is not used when inferencing with Magicoder?

Q3. Why didn't the authors perform APR on existing C/C++ datasets. What if overall LLMs are bad on all existing C/C++ datasets including Defects4C? If that is the case, what is the one thing that makes Defects4C stand out?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Defects4C, a new benchmark dataset for C/C++ program repair, derived from a substantial collection of GitHub commits (9M). The benchmarks consists of 350 defects in total. The authors detail a careful filtering and human verification process. The focus on real-world projects enhances its applicability for assessing program repair methods in practical scenarios. The authors also evaluate the effectiveness of LLM-based APR (automated program repair) on this benchmark.

### Strengths
- A new automated program repair (APR) benchmark for C/C++.
- Extensive experiments with 24 LLMs on the benchmark.

### Weaknesses
 - The novelty and contributions are limited. In recent years, a lot of APR benchmarks have been proposed, covering a variety of programming languages, types (real-world, programming assignments, competitions), difficulty levels, and so on. Table 1 of the paper shows some existing APR benchmarks. There are some more, such as DebugBench (Tian et al., 2024) , EvalGPTFix (Zhang et al., 2023), FixEval (Haque et al., 2023), QuixBugs (Lin et al., 2017b), etc. Therefore, the contributions of this paper are rather incremental.
- The categories of bugs as listed in Table 2 are too rough. I suggest to categorize bugs using finer-grained taxonomy of bugs, which would help reflect the capability of models more comprehensively. 
- Lack of evaluations on sub-tasks: The paper only evaluate models on the entire program repair task, without describing the effectiveness of each step, such as bug localization and patch generation. Particularly, given the challenges in identifying the exact location of faults in C/C++ code, the paper could evaluate of LLMs’ capabilities in bug localization, which is important for real-world program repair.

### Questions
- What are the novel contributions of this work?
- The dataset includes a large collection of bug-relevant commits (e.g., 9M in total), 248 high-quality buggy functions and 102 vulnerable functions paired with test cases for reproduction. How do you ensure adequate quality control through the human annotation process?

### Soundness
3

### Presentation
3

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
This paper proposes a defect dataset for C/C++ languages.

### Strengths
+ This could be a valuable dataset

### Weaknesses
 - Overall, I think this paper is a dataset paper that could fit MSR dataset track well. However, it would not be qualified for a ICLR technical paper cause it contais little technical contribution.

- The description of the collection process of the vulnerability dataset is rather vague. I did not clearly understand how it was constructed. From the Introduction, it seems that this sub-dataset is directly reused from the official CVE database. Later, in the human annotation part, it seems that it was collected by humans, which makes me very confusing. Another point is that 248 bugs were chosen from 3,785 candidates, but 102 vulnerabilities were chosen from 102 condidates. What leads to such a big difference in this ratio?

- The manual annotation leads to Cohen’s Kappa values like 0.48 and 0.60 which are very low. This means that the annotation quality is rather low.

- In the annotation process, CWE types were used to help participants decide whether each commit is bug-related. It is well known that bugs and vulnerabilities are different concepts. Why use this type of information for bug identification?

- The prompts used for evaluation are simply wrong. Before fixing a bug, we would never know how many code entities we need to modify. That means what we can do is only providing a unified prompt for fixing. We cannot ask LLMs to perform modifications at a specific level because we do not have this prior knowledge. The experiments conducted in this study were thus totally wrong.

### Questions
1. What is the technical contribution of this paper?

2. Why we can use prompts of different levels for fixing bugs?

### Soundness
2

### Presentation
2

### Contribution
1
