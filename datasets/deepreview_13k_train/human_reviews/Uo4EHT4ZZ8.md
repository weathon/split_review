# LeanAgent: Lifelong Learning for Formal Theorem Proving

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Large Language Models (LLMs) have been successful in mathematical reasoning tasks such as formal theorem proving when integrated with interactive proof assistants like Lean. Existing approaches involve training or fine-tuning an LLM on a specific dataset to perform well on particular domains, such as undergraduate-level mathematics. These methods struggle with generalizability to advanced mathematics. A fundamental limitation is that these approaches operate on static domains, failing to capture how mathematicians often work across multiple domains and projects simultaneously or cyclically. We present LeanAgent, a novel lifelong learning framework for formal theorem proving that continuously generalizes to and improves on ever-expanding mathematical knowledge without forgetting previously learned knowledge. LeanAgent introduces several key innovations, including a curriculum learning strategy that optimizes the learning trajectory in terms of mathematical difficulty, a dynamic database for efficient management of evolving mathematical knowledge, and progressive training to balance stability and plasticity. LeanAgent successfully proves 155 theorems previously unproved formally by humans across 23 diverse Lean repositories, many from advanced mathematics. It performs significantly better than the static LLM baseline, proving challenging theorems in domains like abstract algebra and algebraic topology while showcasing a clear progression of learning from basic concepts to advanced topics. In addition, we analyze LeanAgent's superior performance on key lifelong learning metrics. LeanAgent achieves exceptional scores in stability and backward transfer, where learning new tasks improves performance on previously learned tasks. This emphasizes LeanAgent's continuous generalizability and improvement, explaining its superior theorem-proving performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents LeanAgent, a framework that aims to improve automated theorem proving through lifelong learning across multiple mathematical domains. The key contributions include a curriculum learning strategy, progressive training of retrieval models, and management of evolving mathematical knowledge. The paper claims significant improvements over baselines, particularly in proving "sorry" theorems previously unproved by humans.

### Strengths
- LeanAgent introduces an interesting approach to adapting theorem provers across evolving repositories. And it uses curriculum learning strategy provides a systematic way to handle increasing mathematical complexity and demonstrates potential for improving retrieval models through continuous training
- This paper provides a framework that could be practically useful for filling in "sorry" theorems and it demonstrates ability to work across diverse mathematical repositories, shows promise for developing maintainable theorem provers that can adapt to changes-
- This paper has detailed ablation studies examining different components

### Weaknesses
 # Evaluation Methodology Concerns
- TPPS metric (with 10x multiplier) may artificially inflate improvements over baseline
- Unclear separation between "during" vs "after" lifelong learning results
- Combined statistics from multiple 10-minute runs may give unfair advantage over baselines
# Results Reproducibility Issues
- Some reported baseline numbers appear inconsistent with other evaluations (ReProver's results)
- Need clearer accounting of which theorems are proved and how
# Technical Limitations
- Only updates retriever model, not tactic generator
- Unclear why curriculum learning is necessary vs training on all data
- Long training times (4-9 days) may limit practical applicability

### Questions
1. Could you provide separate statistics for theorems proved during vs after lifelong learning?
2. Why not update both retriever and tactic generator during training?
3. Have you compared to simple pre-training on all available data?
4. How do you ensure reported improvements aren't just from running multiple model checkpoints?
5. What are the key computational requirements for practical deployment?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes LeanAgent, a lifelong learning framework for formal theorem proving in Lean. LeanAgent alleviates the catastrophic forgetting issue in life-long learning of formal language provers via retrieval-augmented generation, with progressive training on the retriever.

Four main techniques are adopted to reduce the difficulty of training or proof search, including
  * **Curriculum learning** based on quantifiable complexity measured by the number of reasoning steps, allowing the model to learn from easy to difficult repositories
  * **Dynamic database management** that manages existing proofs and incorporates new proof steps generated by LeanAgent
  * **Progressive training** which limits the number of epochs to 1 to improve stability for mitigating forgetting, and choose the iteration with the highest validation recall on top-10 retrieved premises to improve the plasticity of absorbing new information.
  * **_sorry_ Theorem proving** via best-first search, similar to Dijkstra's algorithm in the graph, where each node/state is an incomplete proof, each edge is a proof step, and the path length is measured by the negative log-likelihood.

Experiments are conducted on two aspects, 1) comparing the quantity and quality of newly discovered proofs, and 2) ablation over different setups to further strike a balance between stability and plasticity. The main result shows that LeanAgent significantly outperforms ReProver and discovers 162 new theorems across 23 Lean repositories.

### Strengths
The main strength of the paper is its significance, especially for the Math community. A method capable of automatically discovering new theorems/proofs can lead to powerful tools to accelerate the development of mathematics and expedite relevant scientific fields such as physics and machine learning.

Although each proposed technique alone is not novel, showing the effectiveness of the combined systems is non-trivial, demonstrating the novelty of the proposed methods.

### Weaknesses
The main concern centers around its quality. The provided demos are impressive and great, but the code availability and adopted benchmarks are questionable, specifically,

  * **Code availability**: for LeanAgent to be truly accessible for mathematicians, the code and corresponding inference pipeline are necessary. I am wondering if the authors intend to release the code soon.
  * **Adopted benchmarks**: a standard metric for evaluating Lean-based systems is the success rate on the miniF2F test set. I am wondering if the authors can provide the number, along with comparisons to baselines other than retrieval-based methods. Just including the reported success rates in the previous literature would be fine, e.g. [1][2][3][4][5].

Other detailed comments are listed as follows,
  - [Clarity] lines 262-263, typo: "We sorry theorem theorem proving performance between..." -> "We compare sorry theorem proving performance between..."
  - [Clarity] lines 373-374: terms like "masters" may not be sufficiently rigorous and objective. It would be recommended to provide some numbers to improve the objectivity of the statement.
  - [Clarity] lines 366-387: Better provide redirections to the corresponding section in the Appendix, e.g. line 2050 of HairyBallDiff. This improves the objectivity of the paper.
  - [Clarity] line 437, Table 4: it is recommended to add up/down arrows in metrics to indicate whether the lower or higher values are better
  - [Clarity] Appendix section A.5: the figures for different theorems can be rescaled to make the fonts similar in size.
  - [Quality] lines 316, 430-431: several metrics adopted in the paper are computed based on heuristics, where further justification is encouraged to be added. For example, under the proposed metrics, the rank order of modern LLMs, o_1 > GPT-4o> ChatGPT, would provide evidence that the chosen coefficient is proper.

### Questions
* I am wondering if the code will be released, and when it is expected to be released.
* I am wondering if it is possible to report the miniF2F success rate of the proposed method, given this is the conventional benchmark for Lean-based methods.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces LeanAgent, a framework that augments LLM-guided formal theorem proving with lifelong learning and retrieval from a dynamic database. Evaluations on several real-world Lean GitHub repos and miniF2F demonstrate the advantage of the framework over a baseline with only retrieval from a static database (ReProver).

### Strengths
1. Demonstrates the utility of curriculum learning with retrieval from a dynamic database in the application of neural-guided formal theorem proving.
2. Evaluation on real-world repos shows real-world applicability of the framework (although this also has caveats – see Weakness 5 below).

### Weaknesses
1. The way the abstract describes the results is very misleading. For example, “LeanAgent successfully proves 162 theorems previously unproved by humans” is understood to mean that LeanAgent solved 162 unsolved problems in math, whereas in reality many of these just happened to not have their proofs filled in because the authors of the repositories hadn’t gotten to them yet, or the proofs are intentionally left blank because they are exercises from Lean tutorials/textbooks. For example, there are 0 = 1 placeholder theorems and theorems that simply involve expanding definitions (thus proven by just “refl”). The main metric of comparison with the baseline is also misleading, where the “11x” improvement actually refers to 3 repos where ReProver proved nothing and LeanAgent proved 1 theorem – see my next point.
2. The metric of comparison with the baseline (“TPPS”) appears to be designed to inflate the result of LeanAgent. The metric’s definition depends on the model/framework – already not a good sign. For LeanAgent it is (# ReProver Theorems Proved) + 10 * (# New Theorems Proved) + 1, and for the baseline ReProver it is (# ReProver Theorems Proved) + 1. Notably, the metric for LeanAgent is defined as the metric for the baseline plus a non-negative number, so by the very definition of the metric it is impossible for LeanAgent to perform worse than the baseline. Furthermore, the extra factor of 10 in the definition of the metric for LeanAgent (that doesn’t appear in the definition of the metric for the baseline) appears arbitrary and requires more justification than just saying it is “relatively modest considering the large difficulty gap between basic arithmetic and abstract algebra”.
3. The paper only showed results of the LeanAgent framework with the ReProver retriever and tactic generator. The paper would be stronger if it also showed consistent improvements from LeanAgent applied on top of well-known math LLMs such as Llemma and DeepSeek-Prover and/or other search strategies such as Hypertree Proof Search.
4. While the paper frequently emphasizes its curriculum learning strategy, it does not appear to make a technical contribution in this regard (simple rule of training for 1 epoch on each successive repository) and its application to formal math has already been explored (see, e.g., https://arxiv.org/abs/2202.01344).
5. The evaluation datasets (with the exception of miniF2F) appear to be various Lean GitHub repos with no guarantee of cleanliness. Indeed, the authors point out themselves that one of the repos has several “0 = 1” placeholder “sorry” theorems. Even among actual “sorry” theorems, there’s significant variation in difficulty, e.g., there are some proven by just “refl” and others that are more involved. This makes it more difficult to contextualize and interpret the results. (See also question 5 below for a suggestion to possibly improve this.)
6. In terms of presentation, there’s a decent amount of repetition (e.g. curriculum learning was explained an excessive number of times)

### Questions
(Questions 1-3 are about typos and wording issues)
1. Line 262: Missing word in “We sorry theorem proving performance…”?
2. Lines 227-228: “Before validation, we precompute embeddings for all premises in the corpus to ensure these embeddings are consistent with LeanAgent’s current state.” What does this mean?
3. Lines 318-324: Not sure what “formalize” means here, since if I understood the paper correctly, LeanAgent doesn’t do auto-formalization and MiniF2F is not an auto-formalization benchmark. It is also unclear to me what “in parallel” in line 323 means.
4. It would help the reader to show some basic statistics about each repo, namely, the number of sorry theorems in each repo, the number/percentage proven by LeanAgent, and the number/percentage proven by ReProver. Some statistics regarding the dynamic database would also help, such as the number of theorems/premises from each repo and their breakdown into difficulty categories.
5. (Related to the TPPS metric) It would be helpful to see a more informative metric than the TPPS metric (see criticisms above). For example, it would be ideal to have difficulty estimates for all the “sorry” theorems (based on e.g. ground truth proof length), and then for each repo, show (with e.g. a histogram) for each difficulty category, how many “sorry” theorems there are, how many were proven by ReProver, and how many by LeanAgent.
6. How is it ensured that the proofs do not involve circular reasoning? In other words, how did you make sure you’re not proving a sorry theorem A using another sorry theorem B while using sorry theorem A in the proof of sorry theorem B? (The Alternate PFR Commit case study on pages 30-31 seem to suggest that circular reasoning did occur, using 0 = 1 placeholder theorems to prove other 0 = 1 placeholder theorems.)
7. The coefficients in the definition of the Composite Score obtained (lines 429-431) seem arbitrary – how were they determined? How sensitive are the results to these coefficients?

### Soundness
3

### Presentation
3

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
This paper studies the topic of automated theorem proving in Lean language. It primarily builds on the method proposed by LeanDojo and considers the problem that a trained LLM may consider catastrophic forgetting when it is fine tuned on a new dataset. To address this issue, it suggests that LLMs should be trained for lifelong learning, where they learn new material after being fine-tuned without forgetting what they had learned before. It then considers several Lean repositories and tries to prove the unsolved theorems in those repositories. It reports vaguely some successes in solving some of the theorems.

### Strengths
The topic is very interesting and the experiments are on a diverse set of problems and repositories.

Literature review considers both the ML literature and math literature.

### Weaknesses
## Review

### summary:
 This paper studies the topic of automated theorem proving in Lean language. It primarily builds on the method proposed by LeanDojo and considers the problem that a trained LLM may consider catastrophic forgetting when it is fine tuned on a new dataset. To address this issue, it suggests that LLMs should be trained for lifelong learning, where they learn new material after being fine-tuned without forgetting what they had learned before. It then considers several Lean repositories and tries to prove the unsolved theorems in those repositories. It reports vaguely some successes in solving some of the theorems.

### soundness:
 2

### presentation:
 2

### contribution:
 2

### strengths:
 The topic is very interesting and the experiments are on a diverse set of problems and repositories.

Literature review considers both the ML literature and math literature.

### weaknesses:
 I found the presentation of results very disorganized and rather unusual in the context of the ML literature. Overall, the presentation seems to be a stream of consciousness.

I try to view the contribution from different perspectives, and I explain the shortcomings from each perspective.

1. The task of automated theorem proving: 

    1.a. I tried for some time to find out what is the achieved accuracy of the proposed system on the miniF2F validation and test sets. I was shocked to see in the main body of the paper, in Tables 1 and 2, the paper provides the number of theorems in the datasets that it has proved without giving the total number of theorems nor the accuracy. I was expecting these tables to provide the accuracy of the proposed model on each of the datasets. I was only able to find somewhere deep in the appendix that the paper has been able to prove 99 theorems from the miniF2F dataset (not clear whether it is for the test set or valid set) which translates to accuracy of about 40%. It is as if the paper is trying to hide the accuracy on the known benchmark miniF2F.

    1.b. The accuracy of 40% on miniF2F does not appear to be an improvement in the recent literature. For example, the accuracy of Hypertree Proof Search from 2022 is 41% on the miniF2F.

    1.c. Table 2 does not show how many sorry theorems exists in each repository. For the Coxeter, I believe there are hundreds of sorrys, but paper only indicates the numbers 1 and 11, the number of sorry's it has been able to address without mentioning how many sorry have remained unproved. Table 2 has large margins of empty space, so I don't see why those numbers are not provided.

    1.d. Paper does not mention how many of those sorrys can be proved using native methods in Lean such as apply?, hint, or exact?. 

     1.e. Many of the statements in the paper seem imprecise and perhaps trying to exaggerate the contributions of the paper. For example, the paper claims: “For the Coxeter repository, LeanAgent proves a complex lemma about Coxeter systems, showcasing its proficiency in group theory.” While the paper claims “proficiency” of its model in group theory, it is useful to note that its proof only has three lines of code, and the model fails to prove all other theorems in that repository. So the claim of “proficiency in group theory” seems overblown and unjustified.

2. Lifelong learning: 
    
    2.a. The paper does not establish how its LLM suffers from the issue of forgetting when it comes to ATP. It seems that the paper has struggled with this, and has tried to find the best setting for training the LLM on multiple datasets in sequence, but it is not clear what the baseline was, what kind of accuracy was obtained, how the LLM was suffering from forgetting, and how the issue can be addressed. 

    2.b. The paper keeps talking about the trade-offs between the stability and plasticity, but these two terms remain undefined and unquantified.

    2.c. It seems that, ultimately, paper has just performed trials and errors to eventually find the setting that yields the highest accuracy. Is that the case? I hope authors can clarify this, and explain their exact contribution. Is the contribution a method on how to train LLMs on multiple datasets while avoiding the issue of catastrophic forgetting, or is their contribution just an improvement on the task of ATP? If the former is the case, it would make sense to formalize the method, perform ablation studies, and demonstrate the generalization ability of the method. By ablation study, I mean reporting the accuracies in each configuration of lifelong learning and on each of the datasets. By accuracy for each dataset, I mean the number of proved theorems divided by the total number of theorems in a dataset.


Some other comments

The discussion about lifelong learning, and the claims about how mathematicians work seems like an incoherent opinion piece without much evidence, and not even necessary for the experiments of the paper.

The claim that “mathematicians often formalize across multiple domains and projects simultaneously or cyclically”, and giving Terry Tao as an example, seems a bit out of context. Terry Tao is famous for his unusual ability to work on multiple domains. Overall, I think the paper makes claims that are not even necessary. Paper can simply review the list of problems in miniF2F that it has failed to prove, perhaps showcase one of the more easier problems that it has not been able to prove, and be more grounded in reality when claiming “proficiency” in topics such as group theory.

### questions:
 Please see weaknesses.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 6

### confidence:
 5

### code_of_conduct:
 Yes

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
