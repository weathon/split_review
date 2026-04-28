# A Reasoning-Based Approach to Cryptic Crossword Clue Solving

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 3, 8

## Abstract
Cryptic crossword clues are challenging language tasks for which new test sets are released daily by major newspapers on a global basis. Each cryptic clue contains both the definition of the answer to be placed in the crossword grid (in common with regular crosswords), and ‘wordplay’ that *proves* that the answer is correct (i.e. a human solver can be confident that an answer is correct without needing crossing words as confirmation). This work describes an LLM-based reasoning system built from open-licensed components that solves cryptic clues by (i) hypothesising answers; (ii) proposing wordplay explanations; and (iii) using a verifier system that operates on codified reasoning steps. Overall, this system establishes a new state-of-the-art performance on the challenging Cryptonite dataset of clues from The Times and The Telegraph newspapers in the UK. Because each proved solution is expressed in Python, interpretable wordplay reasoning for proven answers is available for inspection

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a reasoning-based system for solving cryptic crossword clues using fine-tuned LLMs and a Python-based verification process. The model generates candidate answers and wordplay suggestions, formulates these into Python code, and verifies correctness via assertions.

### Strengths
**Originality**
The paper offers a unique approach to solving cryptic crossword clues. Like math proofs, the authors combined LLMs for candidate generation, wordplay suggestions, and formalized Python-based verifiers.

**Quality**
The paper details the fine-tuning of models for clue and wordplay generation and the creation of a domain-specific verifier, including formalization in Python. The experiments demonstrate a clear improvement over previous state-of-the-art results on the Cryptonite dataset, significantly outperforming prior baselines.

**Clarity**
The paper includes figures containing examples that help in understanding.

**Significance**
The paper shows an improvement in the cryptic crossword domain.

### Weaknesses
1. The mention of a 23.5% accuracy on the Cryptonite dataset using GPT-4-turbo in the paper [1] suggests that a more rigorous baseline is possible for this study. Using the same prompting strategy on the Gemini-Flash that is used in the paper could provide better insight into the improvement of the proposed method.

2. The paper's reliance on the Wordplay dataset, gathered from newspapers (The Times, etc.), raises the possibility of data leakage, as The Times also contributes to the Cryptonite test set. If fine-tuning data includes patterns or clues from the test set, results may be artificially inflated.

### Questions
1. Partial correctness metrics, as reported in [1], can provide a more nuanced understanding of model success on cryptic crosswords, where the model might have answered some rows/columns but not the whole crossword.

2. Some minor corrections on line 200 ("from" is repeated twice)

[1] Saha, Soumadeep, et al. "Language Models are Crossword Solvers." arXiv preprint arXiv:2406.09043 (2024).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a method that achieves state of the art performance on cryptic crosswords. The method uses LLMs to solve the subtasks using various strategies. First, Gemma2-9B is fine-tuned using low-rank adapters on answer-candidate generation, which returns a list of answers which match the 'pattern' (the length of the answer). Second, Gemma2-9B is again fine-tuned using low-rank adapters, but this time for 'wordplay suggestion', which takes each answer candidate and generates multiple definition/wordplay pairs, which are meant to explain why the answer is correct. Third, prompting is used in combination with Gemini-Flash to formalise the wordplay into Python 'proofs'. The Python proofs are run and any errors are reported back to Gemini-Flash, which is given a chance to correct its proof (until the answer is valid, or the maximum of 2 rewrites is reached). In the experiments, the formalisation process is shown to be helpful in the general, although for the 'Quick' subset, using the most frequent answer candidate proves too strong a baseline.

### Strengths
- State of the art result on complex task.
- The reported results show that LLMs are very helpful as components in a system to solve complex tasks, while also not sufficient to solve it completely on their own.

### Weaknesses
 - I think more space could be devoted to explaining cryptic crosswords. As someone previously unfamiliar with them, it took quite long for me to understand what exactly was happening in the example given in the introduction. Maybe a table or diagram that explains exactly how each part in the wordplay is related to the parts in the clue?
- A solid motivation for why this work is important is missing. What is the primary reason to be interested in LLM performance on this task? And relatedly, what should be the general take-away after reading it?

### Questions
How were the in-context learning prompts constructed, and how many versions did you try? What is your sense of the sensitivity of the final accuracy w.r.t. the prompt, how important is it?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper identifies the gap that cryptic crosswords, a well-known language-oriented reasoning puzzle, have received little attention from the community. To this end, the authors propose a system that combines LLMs and a Python interpreter to solve cryptic clues. In the paper, they elaborate on the system architecture and run experiments using Gemma and Gemini model family to show better performance than the baselines on Cryptonite benchmark.

### Strengths
Identifying the gap that cryptic crosswords have received little attention from the community, especially post LLM era, the authors propose a framework that combines LLMs and a Python interpreter to solve cryptic clues, and show better performance than baselines on Cryptonite benchmark.

### Weaknesses
1. This paper may lack enough strong baselines and the comparisons with these baselines may not be entirely fair. There are 3 baselines including rule-based, a fine-tuned T5 large, and Gemini Pro 1.0 zero-shot. First, The T5 large model only has 770M parameters while Gemma 9b (which is used in this paper) has 9B parameters. Comparing Gemma 9B-FT with T5, we can see that changing the model with the same training data improved the accuracy from 7.6% to 15.9%. Second, Gemini 1.5 Flash is used in the proposed system while the baseline is zero-shot Gemini Pro 1.0 which shows inferior performance across general benchmarks. Third, while the papers mentions limited computation resource, rows in table 1 are reported based on different number of examples, which make them not comparable.

2. It may not be clearly stated in the paper the reason of following the proposed order: i.e. generating answer candidates first, then generating possible definitions and wordplays, and then doing verification. Reasoning tasks typically generate reasoning steps followed by the final answer and verification, e.g. ReAct format. In this case, possible definitions and wordplays can be followed by the final answer candidates and external verifiers. This is also consistent with line 44 regarding the reasoning steps. Have you tried different variations and concluded that the proposed order is the best?

### Questions
1. Regarding weakness 2, have you tried different variations and concluded that the proposed order is the best?
2. Since the current system combines multiple open source fine-tuned models (Gemma) and a closed source model (Gemini) for different stages, I wonder if you have tried a single model performing all different tasks, either prompting or fine-tuning, which makes the system simpler?
3. The last paragraph in section 2.2 mentions that an apple-to-apple comparison with Rozner et al. (2021) is hard because of different split setting. Could you elaborate more on the challenge of comparing using the same data? Is it because the test split in one approach is used for training of another approach, or their model is not publicly available?

Minor points => Typo(s): 
1. Line 155, T5 large is 770M
2. Line 200, the first sentence in section 3.1 has two “from”
3. Line 344, that -> than

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a novel reasoning approach to generate answers for cryptic crossword clues. It is a multistage approach which does the following:
1. First, a fine-tuned LLM suggests possible answers for the entire clue.
2. Second, for each candidate answer, another LLM generates possible definition/wordplay suggestions.
3. Third, for each suggestion, another few-shot LLM generates python code which wraps their domain-specific language to prove the wordplay. If there's an error in the verifier, it is fed back to the LML in a loop up to K times to improve/correct the proof. If there is no error, the answer is used as the final prediction. 

This system improves overall performance on the Cryptonite dataset from 15.7% to 32.5%, and the authors give some analysis on the benefits and shortcomings of their approach.

### Strengths
* The authors introduce a novel approach to a uncommonly studied task, which has interest to the NLP/reasoning communities for its difficulty and unique reasoning requirements, and to the cryptic crossword hobbyist community. They provide motivation for why this task is relevant and should be worked on. 

* Their approach is effective, more than doubling the previous SOTA performance on the same task. Additionally, it offers several "obvious" avenues for improvement as it breaks the task down into more easily tunable parts.

* Finally, the paper is very clearly written and communicates their relatively unknown task and novel method effectively.

### Weaknesses
 * A full ablation study would make clear the shortcomings of each part of the pipeline. While the authors demonstrate the effectiveness of just using the top candidate answer, it would be helpful to know the benefit of adding the definition/wordplay model (combined with e.g., a simple LLM-based reranker) compared with the full pipeline.


### Questions
- When you say `The Wordplay dataset follows the train, validation, and test split defined by
  Cryptonite`, I assume you mean there is no contamination between the two, i.e., no clue in the
  train dataset for Wordplay will appear in the Cryptonite val/test splits. Is this correct or did
  you have mean something different?
- The performance of your pipeline is of course capped by the recall of the candidate answer
  suggestion model, which seems to be about $40$% at $N=20$. This means that the rest of your pipeline
  can correctly choose about $32.5 / 40 \approx 81$% of the results, which seems promising. Have you
  considered just making N as large as possible? It might be an easy (albeit inefficient) way to
  improve overall performance by a bit, assuming the rest of the pipeline is robust to many wrong
  candidates.
- Also, I'd be curious to know how much the 'verification' system helps. While your system is
  certainly effective, I wonder how much the verification system improves over a "dumb" reranker
  (e.g., scoring the probability of each (answer, definition/wordplay) pair using the LLM and
  choosing the best).

### Soundness
3

### Presentation
4

### Contribution
3
