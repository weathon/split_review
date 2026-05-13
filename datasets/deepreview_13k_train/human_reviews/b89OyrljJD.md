# How Well Can LLMs Synthesize Molecules? An LLM-Powered Framework for Multi-Step Retrosynthesis

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
Predicting retrosynthesis routes is a fundamental challenge in chemistry, involving the design of a sequence of chemical reactions to synthesize a target molecule from commercially available starting materials. With a rapidly
growing interest in using large language models for planning, this work introduces an LLM-powered framework for multi-step retrosynthesis. Our framework employs molecular-similarity-based retrieval-augmented generation (RAG) to generate an initial retrosynthesis route, which is then iteratively refined through expert feedback. The use of molecular-similarity-based RAG improves reaction round-trip validity from 24.42\% to 51.64\% compared to GPT-4 with representative routes. With further refinement, the validity increases to 89.81\%, resulting in an overall route validity of 79.5\% with a perfect query success rate, comparable to traditional methods. Our framework offers a flexible, customizable approach to retrosynthesis, and we present a comprehensive analysis of the generated routes along with promising future research directions in LLM-driven multi-step retrosynthesis.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the potential of pretrained LLM models to engage in in-context learning of synthesis routes when the context includes related reactions from a RAG database.

### Strengths
The paper provides a baseline for a straightforward approach to use modern pre-trained AI models in a retrosynthesis context.  The authors explored a variety of different models, demonstrating the practical utility of this approach.

### Weaknesses
Given the rapid pace of development, the pretrained models used by the authors are not state-of-the-art at this point in time.  The authors chose not to finetune any model, which limits the exploration of the true potential of the underlying concepts once the models are adapted to handle small molecule chemistry in a reliable fashion.

The price tables listed in this paper for the models are outdated.  GPT-4o mini costs $0.075 per million input tokens and $0.3 per million output tokens, and GPT-4o also costs significantly less than GPT4-turbo cost at the time the authors used it. Providing updated pricing information and evaluation with latest models would improve the evaluation.

The primary metrics of the paper presented in table 1 are not particularly effective in evaluating if the method works in practice.  In particular, the query success rate only indicates if the model learns to copy the target smiles from the prompt and then produce a series of plausibly looking text.  Since the relevance of the reactions is not evaluated, it may be possible that the round-trip validity can be iterated to become accurate by reference to valid SMILES and purchaseable molecules in the database. It remains unclear if the authors ultimately answer the question they posed in their title.

### Questions
Could the authors elaborate on why fine-tuning is considered to require substantial resources?  Finetuning of 4o-mini cost $0.15 per million input tokens and was free up to a daily token limit for a couple of months until end of October.  Moreover, finetuning using LORA for publicly available LLMs can be performed with manageable compute costs (the FLOPS required during training without LORA are 6 * params * datatokens, and modern H100 GPU can theoretically reach 1e15 FLOPS/s).  Have the authors considered finetuning on their training set, possibly including additional small molecule SMILES (as others have done), to create a chemically aware LLM and then repeat their current setup?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the challenge of computer-aided synthesis planning (CASP), i.e. finding viable synthetic routes to a given target molecule. For this purpose, the authors introduce a two-step LLM-centric pipeline: First, a full route is proposed through retrieval-augmented generation from the LLM. In the second step, this route is refined using feedback from multiple specialist models. This method is benchmarked against a “classical” tree search approach using a neural-network-enhanced A* algorithm. The paper also discusses empirical insights gained from model evaluation.

### Strengths
-	Most current CASP methods rely on iteratively navigating the retrosynthesis tree, which struggles with with strategic multi-step planning. Against this background, the idea of generating an initial complete route, followed by route refinement, is promising. 
-	Empirical results indicate that retrieval-augmented generation enhances the quality of initial route proposals. 
-	The paper is generally well-written, and its logic is easy to follow.

### Weaknesses
-	Benchmark results do not demonstrate a performance advantage over the baseline strategy – even given that the problems are relatively simple (see below). Therefore, application to real-world problems is still distant. A broader evaluation, potentially including MCTS-based methods, might yield more comprehensive insights. 
-	The significance of the benchmark set is doubtful for two reasons: 1) The problems are relatively simple – average route lengths of <5 steps do usually not require advanced, multi-step strategic thinking. 2) The problems are extracted from the patent literature, which faces well-known data quality issues. For example, a rapid visual inspection of the “ground truth” routes in Figure A.3 reveals synthesis-relevant chemical errors in two out of three examples, further questioning the reliability of these benchmarks. 
-	The discussion of literature precedence, particularly regarding computer-aided synthesis planning, is incomplete, and omits a number of pioneering contributions: The seminal retrosynthesis works by Corey; the first demonstrations of retrosynthesis with ML / AI (Segler, Coley), and the state-of-the-art in CASP (Grzybowski) – which is, as of today, not based on AI technology.

### Questions
-	The discussion of “expert models” in the main text implies that they provide ground-truth information. However, the reaction-wise feedback models are subject to severe limitations themselves, especially due to the data they are trained on. This should be discussed in the main text. 
-	The RAG model retrieves reference syntheses based on a hard-coded notion of “chemical similarity” (fingerprint similarity), assuming that similar molecules exhibit similar synthetic routes. However, there are many examples that violate this assumption, especially when stereochemistry comes into play. At minimum, this limitation should be acknowledged. In the long term, the RAG should be based on similarity measures which are more meaningful to the similarity of synthetic routes. 
-	Is the “query success rate” a meaningful metric, especially in comparison to the non-LLM-based baseline model?  
-	Chapters 3 and 4.1 have overlapping content. A single, consolidated section that discusses the experimental setup, particularly with respect to expert models and knowledge databases, would improve readability.
-	The term “round-trip validity” is confusingly applied. The original definition from Schwaller et al. only defines it for single reaction steps (target molecule –(retro-direction model)–> starting material(s) –(forward-direction model)–> target molecule). The authors later use the term for scoring full synthetic routes (but without defining what a “round-trip valid route” is). This should be clarified. Moreover, the limitations of their method to determine round-trip validity (p.5) should acknowledged.

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
The authors present a framework for automated retrosynthesis using large language models. Contrary to the commonly employed strategy of obtaining a synthesis plan by iteratively expanding a tree of reactions and reactants, this approach takes a more holistic view, generating and iterating over the entire sequence as a whole. In the proposed framework, the user inputs a target molecule as query to the retrosynthesis planner. The system then starts by performing a fingerprint-based similarity search in a database of known reaction plans to use the synthesis route of a similar molecule as starting point. This example is fed to the LLM which generates a route for the query molecule, and format it in a structured JSON file. This response then goes into an interative loop which (1) checks the validity and commercial availability of reactions and building blocks (using expert models and other databases) and in case of invalid steps, feeds-back the route and the validity check results to the LLM for further refinement. The authors experiment with three different LLM models (GPT4-Turbo, Claude-Haiku and Deepseek) and compare against Retro*, a well-known retrosynthesis model. They show that the proposed framework effectively combines all of these components and allow to propose valid synthesis routes for about 80% of the tested query molecules.

### Strengths
Overall, I found the paper of good quality and very well written. I think it addresses an important challenge (automatic retrosynthesis) from a modern perspective (in combination with LLM and integrating workflows and specialised tools / user feedback). In particular:

- The Introduction and Preliminary sections are well written and effectively guide the reader into the subject matter.
- The presentation of the proposed framework is also very clear (Figure 2).
- I believe that the integration of both specialized models and human feedback (Section 4.1) is a flexible and powerful combination. In particular, Table A2 provides a clear and helpful list of scenarios which could be handled by the framework.
- The experiments section is well structured and clearly support the claims made earlier in the paper.
- The authors clearly identify drawbacks of the proposed methods (lines 333-343, 371-377) showing scientific integrity and motivating future work.

### Weaknesses
#### Main weaknesses:
1. My main comment is on the motivation of this line of work. I believe the authors could present more clearly the potential benefits of an eventual transition from traditional synthesis planners to LLM-powered planners in a more effective way. While I have some intuitions about what potential gains in accessibility and ease-of-use such approaches could yield, after reading the paper, I am still left somewhat unclear about which precise drawbacks from traditional planners LLM-based planners aim to address.

2.  The validity-availability iterative loop (steps 3-7 in Figure 2) should be explained in more details before the experimental section. For example, on line 199 it is mentioned that "The synthesis tree is evaluated by a series of expert models for feedback" but no concrete example of such models is given. Although more details are given in pages 5-6, adding more details about expert models in the methods section would make that part better standalone and enhance clarity.

3. The availability of the code to reproduce experiments is not discussed.

4. The quality of several figures could be enhanced -- e.g. very thinly rendered molecular bonds, drafty layout (table 3) etc. In Figures 1 and 5, some elements in the "LLM" box are unreadable. The pseudocode presented in appendix is hard to read (too many different text styles).

#### Minor comments:

1. Broken link in footnote of page 3 ("s" is not in the \url).
2. Figure 4 is missing the caption.

### Questions
1. On lines 270-272, the authors describe how predictive models are used for RT assessment on the proposed synthesis plan. Why can't the framework simply employ traditional tools like rdkit to run the proposed reaction and reactant? (why employing ML models here?)
2. I am not sure to understand exactly what is meant by Query Success Rate (line 252). How exactly is that evaluated and how can the model fail to produce any sort of synthesis path when the quality is not taken into account? I believe this could be made clearer with an example.
3. How reliant is the framework on the success of the similarity-based search? Can the model successfully propose synthesis routes for molecules that are synthesizable, but far outside the known synthesis routes database? Results are presented for similar v.s. representative starting points in Table 3, but how about without providing any starting point (just the query molecule)?
4. Regarding scalability with the number of queries: synthesis plans can be designed by hand by chemists on a case-by-case basis. On the automated side, one of the most important applications of automated synthesis planning is to feed high throughput screening (HTS) platforms with hundreds or thousands of molecules that are guaranteed to be synthesizable in a timely fashion (without human involvement). Where do LLM-based planners fit on this scale? Apart from operational costs listed in lines 290-293 (which were helpful), it would be interesting to discuss these limitations and the exact use-cases for the presented framework.
5. Have any experiments been carried out using user feedback in the refinement loop? User feedback is mentioned as a possibility for this framework in the text but no explicit experiments are presented.

### Soundness
3

### Presentation
2

### Contribution
3
