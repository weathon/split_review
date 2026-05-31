## Human Reviewer 1

### Summary
LLMs excel at math final-answer tasks (e.g., AIME) but struggle with rigorous proof generation—critical for research/theorem proving. Existing proof benchmarks are small, outdated, or closed, leaving 3 key questions unaddressed: (1) natural vs. formal proof gap, (2) final-answer vs. proof correctness link, (3) best-of-n strategy impact. Several findings are elaborated in the paper:
- Natural language proofs outperform formal ones (GEMINI-2.5-PRO solves 4x more PutnamBench problems than top formal model).
- Final-answer accuracy is not equal to proof correctness (O3 loses ~30% accuracy when proofs are required, vs. 8% for GEMINI-2.5-PRO).
- Best-of-n pairwise ranking boosts accuracy significantly.
- LLMs match humans in proof judging.
- LLMs rarely admit uncertainty and struggle to judge their own work.

### Strengths
- Rigorous proof generation/evaluation pipeline.
- First large, open, human-validated LLM-proof dataset (OPC).
- High-Quality Data: Expert judges (IMO background) ensure reliable labels; diverse, competition-sourced problems.
- Actionable Insights: Quantifies critical gaps (natural vs. formal proofs) and validates best-of-n strategies.
- Openness: OPC and code are open-sourced; transparent methodology for reproducibility. I think this will be a good resource in theorem proving area.

### Weaknesses
- Narrow Problem Scope: Most problems are high school-level (IMO/USAMO); few undergraduate/research-level tasks.
- Outdated Provers: GROK-4/GPT-5 are only used as judges, not prover, which misses latest LLM proof capabilities.
- Lack of analysis of why formal theorem provers lag behind natural language counterparts. This is an interesting comparison, it would be great if there can be some deeper analysis.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
In this work the authors curated a new dataset called the open proof corpus, which contains 5,062 LLM-generated proofs of 1,010 distinct problems from math contests. These proofs are all incorporated with manual reviews from human experts. They have also done a lot of researches around this dataset, especially on the proof judging capabilities of different LLMs.

### Strengths
* This work answers a lot of interesting questions in this area.  

* This paper provides a comprehensive study on the proof evaluation capability of LLM, fulfilled an important blank in the research of AI4Math.

### Weaknesses
* The evaluation of proof judgement may be heavily dependent on the judger’s prompt or criteria, so neither the judging accuracy nor the alignment with human graders are accurate enough.  

* This work did not cover problems from advanced math or research-level math, where proof problems weigh more importance than math competitions. This limits the contribution of OPC.  

* The creation of this OPC heavily depends on manual annotation from experts, which limits the scalability of this work.

### Questions
* How are the results in Table 2 (Section 5.2) evaluated actually? I did not find any further descriptions of the settings of these experiments around this chapter. If the performance of LLM judges is evaluated by comparing with human labels, then are they directly comparable with human baselines?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper presents large-scale dataset of high-difficulty math problems which includes both correct/incorrect proofs and profound annotations which are represented via human-expert judgements. Based on the dataset, some exciting insights are proposed.

### Strengths
1. A fairly large dataset of math problems is proposed, with its core value lying in expert annotations. Furthermore, both correct and incorrect proofs are included. It is quite unusual for modern math benchmarks and datasets to contain such annotations, making this contribution valuable to the community.
2. Some exciting empirical insights are provided. While I do not feel that the exploration of performance differences between natural and formal proof generation is particularly valuable, since the performance degradation in formal setups is largely expected, the examples illustrating the discrepancy between final-answer correctness and proof correctness are important.
3. The performance of the fine-tuned, moderately sized LLM judge is impressive.

### Weaknesses
It might be somewhat subjective, but the presentation quality is low, even considering the number of figures included in the manuscript. While it is understandable that the authors tend to include more content rather than placing all figures in the Appendix, the text in each section is highly granular. I think this weakness could be addressed by rethinking the overall structure. The main focus should be on the dataset itself, which is valuable, while the incremental contributions in the form of interesting observations should either be explored more deeply or moved to the Appendix.

### Questions
1. Can you clarify the guidelines used by judges for borderline proofs? How are omissions or shortcuts treated when deciding correctness?
2. Could you provide more insight into common errors when models give correct answers but incorrect proofs? Are these mostly algebraic mistakes, logical gaps, or misapplied theorems?
3. Does this discrepancy vary systematically by problem type or difficulty?

### Soundness
3

### Presentation
2

### Contribution
4

### Rating
8

### Confidence
5

---

## Human Reviewer 4

### Summary
This paper introduces the Open Proof Corpus (OPC), a dataset of 5,062 LLM-generated mathematical proofs across 1,010 problems from prestigious competitions (IMO, USAMO, Putnam), each evaluated by human judges. Using the OPC, the authors demonstrate: (1) informal proof generation outperforms formal by 4x on PutnamBench, (2) significant gaps exist between final-answer accuracy and proof correctness (especially for o3, dropping from 87.6% to 59.5%), and (3) ranking-based best-of-n strategies achieve 47% accuracy versus 26% pass@1. They also fine-tune an 8B model that achieves 88.1% accuracy in judging proofs, approaching GPT-5's performance.

### Strengths
- Addresses critical need: First large-scale dataset of human-evaluated LLM proofs, filling a major gap since existing benchmarks focus only on final answers (e.g., AIME, HMMT).
- Methodology: Well-designed grading pipeline using 13 former IMO participants, clear guidelines, double-grading (90.4% agreement), and clever use of LLM-generated issue summaries to aid grading efficiency.
- Significant empirical findings: The 4x gap between informal/formal proof generation and the divergence between answer accuracy and proof correctness are important insights. The ranking-based best-of-n showing 21% absolute improvement is practically valuable.
- High-quality dataset design: Thoughtful splits (MathArena, PutnamBench, best-of-n, generic) enable targeted analyses while preventing test set contamination.

### Weaknesses
- Binary evaluation loses information: The "5+/7 points counts as correct" threshold is arbitrary and discards nuanced quality differences that partial credit scoring would capture.
- Unfair formal/informal comparison: Comparing specialized formal proof models against general-purpose LLMs isn't apples-to-apples. The brief mention of Seed-Prover's 50% formal accuracy suggests the gap may be overstated.
- Missing statistical analysis: No confidence intervals, significance tests, or error bars despite sufficient sample sizes.
- Insufficient contamination analysis: Section C.2's comparison of "Standard" vs "Non-standard" competitions is suggestive but not conclusive. The performance differences could be explained by difficulty alone.

### Questions
- Why binary labels? Could you release the raw judge feedback to enable partial credit analysis? This would be valuable for understanding proof quality gradients.
- Model failure modes: The observation that only 114/1700 incorrect proofs acknowledged uncertainty is striking. Could you analyze whether this varies by problem difficulty or type?
- Formal proof training: Have you considered fine-tuning informal models on formal proof data to better understand the performance gap?
Competition selection rationale: Was there systematic criteria for choosing these specific competitions over others (e.g., Putnam over Mathcounts)?
- Extending beyond competitions: Have you considered including undergraduate textbook problems or research-level lemmas? What would be needed to extend OPC to these domains?

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 5

### Summary
The authors introduce a set of approximately 1000 contest math problems, drawn from existing competitions, whose LLM proof is humanly rated (binary), to be used both as an eval set and training set. They use the dataset to assess how correct the proof is compared to the (correct) final answer. The dataset, as a training dataset, is validated by fine-tuning an 8B R1-Qwen model, which is claimed to match GPT5.

### Strengths
The problem assessment pipeline is rigorous. 

The single fine-tuned model on OPC is a welcome addition that supports OPC. 

The dataset size is sufficiently large to allow finetuning.

### Weaknesses
- misleading statement: my biggest issue is that apparently not the full dataset was shared, as only USAMO and BMOSL seem to appear in the zipped supplementary (and also for these, not the full dataset? seems quite small), contrary to the claim: "We have included our dataset in the supplementary material, along with detailed descriptions of our methodology and experimental setup to ensure full reproducibility."

- ambiguous claim: "The OPC was specifically designed for broad applicability and downstream usage in proof generation research and is the first to include a substantial number of correct, LLM-generated solutions to problems from prestigious mathematics competitions such as the USAMO and IMO."
As it reads, it is unclear if the authors claim to be the first ever to create such a dataset, or the first to create such a dataset in the more narrow domain of contest math problems (only the latter is correct). Since this is from the **appendix**, I would urge the authors to rewrite.

- missed important prior literature: Probably the first paper on "pure" autograding was https://arxiv.org/abs/2406.10268, and there is (rather similar) follow-up work by these authors https://arxiv.org/html/2502.13337v1  (it would be good to include this in the related work section). But much earlier work exists implicitly in ML even if not marked as autograding, e.g. in 2024 https://arxiv.org/abs/2402.11111 a more detailed methodology for "LMs as evaluators" was derived (see also more papers on prior such literature), or **2021** in the well-known paper https://arxiv.org/abs/2110.14168, which used what they called "verifiers" All this points to an existing body of work on proof judging that is missing from this paper.

- Wrong claim: "Data contamination poses only a minor risk for proof judging, since generated proofs cannot be present in the training data."
I am unsure on what information this claim rests - who is to say that the main LLM companies don't exactly do this? They have their LLMs generate outputs on contest-level problems to ensure that their LLMs can potently act as judges, which can be of use for subsequent pipelines that the companies might use, or in case the public wants to use LLMs as judges, and companies are interested in having their LLMs perform well on publicly known problems. This seems entirely plausible to me, so I believe this statement should be retracted.

- in terms of the results, with some exceptions, the paper seems to reinforce known folklore beliefs about how models performance on mathematics.

- Almost no details are given about fine-tuning on R1 Qwen3-8B. In particular, rivalling the performance on GPT-5 is a dubious claim (presumably a heldout subset of OPC was used for this on which R1 Qwen was not train? details are missing)

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
4