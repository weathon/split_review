# Searching for Optimal Solutions with LLMs via Bayesian Optimization

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Scaling test-time compute to search for optimal solutions is an important step towards building generally-capable language models that can reason. Recent work, however, shows that tasks of varying complexity require distinct search strategies to solve optimally, thus making it challenging to design a one-size-fits-all approach. Prior solutions either attempt to predict task difficulty to select the optimal search strategy, often infeasible in practice, or use a static, pre-defined strategy, e.g., repeated parallel sampling or greedy sequential search, which is sub-optimal. In this work, we argue for an alternative view using the probabilistic framework of Bayesian optimization (BO), where the search strategy is adapted dynamically based on the evolving uncertainty estimates of solutions as search progresses. To this end, we introduce Bayesian-OPRO (BOPRO)—a generalization of a recent method for in-context optimization, which iteratively samples from new proposal distributions by modifying the prompt to the LLM with a subset of its previous generations selected to explore or exploit different parts of the search space. We evaluate our method on word search, molecule optimization, and a joint hypothesis+program search task using a 1-D version of the challenging Abstraction and Reasoning Corpus (1D-ARC). Our results show that BOPRO outperforms all baselines in word search (≥10 points) and molecule optimization (higher quality and 17% fewer invalid molecules), but trails a best-k prompting strategy on program search. Our analysis of this failure case reveals that despite the ability to sufficiently balance exploration and exploitation using BOPRO, failure is likely due to the inability of code representation models in distinguishing sequences with low edit-distances.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors are interested in answering whether the LLMs can search for optimal solutions and reason in the planning problems. They extend the prior works which either attempt to predict the task difficulty to select the optimal solution or greedy sequential search, both of which are not always optimal. More specifically, the authors propose Bayesian-OPRO, that integrates Bayesian optimization with LLMs, which iteratively samples from new proposal distributions by prompting the LLM with a subset of its previous generations selected to explore different parts of the search space. They evaluated their method on two language-based search tasks.

### Strengths
Strengths:

1.	The paper is clear and well-written, with all the relevant works cited. 

2.	The authors provide a thorough analysis of BOPRO’s exploration and exploitation capabilities and acknowledge that the proposed method fails to exploit.

3.	I like that this paper discusses the limitations and future work openly. These insights can help future researchers to build and improve upon the current methodology.

### Weaknesses
Weaknesses:

1.	The proposed methodology is dependent on the access to an external verifier.

2.	BOPRO is not able to balance exploration and exploitation and might not be ready for practical use of the reasoning in the LLMs.

3.	BOPRO might not be ready for practical use yet as it still consistently trails behind the greedy baseline.

### Questions
Questions:
1.	How does the number of warm-start prompts W influence the final performance of the model? Is there a specific range of W that balances exploration and exploitation effectively?

2.	In row 248, how do the authors sample a batch of candidates for each z’t+1? Could alternative sampling methods impact the diversity and quality of solutions generated? 

3.	I am wondering if the choice of other dimensionality reduction technique can  help improve the performance of BOPRO?

4.	Do authors have any insights on what specific strategies can be introduced to improve BOPRO’s ability to balance exploration and exploitation?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposed a method leveraging LLM to perform optimization, named Bayesian-OPRO (BOPRO). This work can be seen as a generalization version of recent work OPRO. Their method is to intergrate bayesian optimization into LLM-based search, to be more specific, they use BO to determine the search direction for LLM by constructing a surrogate function on the latent space for value assignment. The experiment is performed in two tasks, however, the performance of this method underperforms OPRO in both tasks, although the authors have provided some in-depth analysis in terms of exploration capability and adaptbility.

### Strengths
1. The proposed method is novel, although there have been works focusing on combining LLM and BO to perform optimization tasks, the specific method of this work is different from other works. They perform BO process in latent space and design a reasonable encoding-decoding method. 
2. The presentation is good, statements and visual presentation in the paper is clear. 
3. Apart from main experiments, more in-depth analysis about adaptability and exploration are provided.

### Weaknesses
1. The experimental tasks in this works look easy and insufficient, which could not be enough for examine the performance.
2. The performance of this method is not good in the main experiment, as shown in Figure 2. Although the authors argue that this method could have stronger exploring capability and adaptability to different tasks, this kind of advantage isn't verified by the final performance which we should pay more attention to.

### Questions
1. The author mentioned in the introduction section that "Despite moderate success, these solutions are either too expensive, not performant enough, or impractical in offering a general solution for search.". How does this method resolve these issues? There seems no clear explanation of this aspect in the paper.
2. The authors mentioned in the Section 6 that " However, we find that our baseline of repeated sampling (RS) using a weaker Mistral-Large-2407 model is able to trivially surpass that score with an accuracy of 81.48%". I don't really get this statement, could the author please provide more detailed information of this? Using weaker model with less generations surpass the stronger model with more genrations go against my instincts.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces BOPRO, a novel search method designed to improve the identification of optimal solutions by combining Bayesian Optimization with an LLM-based search strategy. BOPRO operates through an iterative search process, in which Bayesian Optimization is applied over a latent-space embedding derived from the LLM-generated prompts. 

An empirical evaluation of BOPRO is performed on two benchmark tasks for language-based search, wherein it is found that BOPRO is outperformed by a greedy baseline approach. 

Further investigation of the search behaviour of BOPRO is performed, revealing that it has strong exploration capabilities and can adapt to problem difficulty, but that it fails to effectively exploit promising regions of the search space.

### Strengths
The paper is well-written and relatively easy to follow. The proposed method has many details and "moving parts" but these are clearly outlined and their significance explained. The same goes for the experimental setup and results. 

The paper is open and forthright about the limitations of BOPRO. 

The paper includes nice big figures that are intuitive and easy to understand. 

Despite the essentially negative results, the paper does a good job of clearly outlining the experimental investigation of BOPRO. 

Given the popularity of LLMs and the effectiveness of Bayesian Optimization, I think the investigation described in this paper can be seen as a valuable contribution and could be a helpful starting point for future research.

### Weaknesses
The results are essentially negative (i.e., BOPRO is beaten by the greedy baseline and/or repeated sampling), which must be considered a weakness.

Figure 2: It would be easier to read the plots if they indicated somehow which lines were the three BOPRO variants (e.g., with different line styles and/or legend labels) and which were the baselines.

I think the related work would be nice to see earlier in the paper, particularly the part about other ways that Bayesian Optimization and LLMs have been combined.

Some minor issues not affecting my recommendation:

- Line 120 and elsewhere:  "For e.g.," this reads as too informal. Use "For example,".

- Figure 3 caption: There is maybe a word missing? "... random sampling with low due to ..."

- Section 7.2 Heading and elsewhere: "v/s" -> "vs."

### Questions
I wonder if the authors could explain the importance/significance of separating the solved from the unsolved cases in the various figures. 

There seem to be a number of heuristics that were used. For example normalizing scores between 0.1 and 0.8, and the use PCA for dimensionality reduction (over other methods). It is stated that these improved performance. Was the performance improvement large? Is it expected that this will hold for other search tasks, or will these heuristics need to be adjusted in general?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces BOPRO, a novel Bayesian optimization-based search methodology for LLM-driven tasks, showing its exploratory capabilities and adaptability to task difficulty. Despite BOPRO’s strengths, it underperforms compared to a greedy baseline. The paper also identifies its limitations and suggests directions for future improvement.

### Strengths
- Combining the search capabilities of BO and the language capabilities of LLM is a research direction worth exploring.
- Plotting the search path (e.g., Fig.1 and Fig.5) is a great way to illustrate the trade-off between exploration and exploitation.
- The experiment conducted a detailed analysis of BOPRO underperforming.

### Weaknesses
 - The claimed generality is not well demonstrated. The abstract states that a key issue in this field is the lack of "a one-size-fits-all approach" (line 14), and the introduction provides several examples that highlight the importance of a general search strategy. I initially believed that generality would be a major highlight of the proposed algorithm. However, it is disappointing to see that the experiments were conducted on only "two representative language search tasks" (line 110), which clearly does not showcase BOPRO as a general method. As shown in Appendix A.6, the prompts are specifically tailored to the given tasks and are not generalizable.
- The innovation is questionable. Bayesian optimization has proven its utility and been extensively explored due to its strong performance and wide applicability. If this paper simply applies LLMs to the BO framework in the context of two specific tasks, the novelty is doubtful. There are already numerous search algorithms combining LLMs with BO.
- The experiments are insufficient. The experiments only compare BOPRO with three basic search strategies: greedy, repeated sampling, and random. These methods are too simple to demonstrate the superiority of BOPRO. The author should include current state-of-the-art methods, such as those mentioned in [1-4], and conduct more comprehensive experiments with different background.
- The reproducibility is questionable. I intended to test the performance of the algorithm, but I could not find any code or materials to support reproducibility. For example, the author claims that BO is described in Appendix A.2, but the expressions for the acquisition functions and related parameters are not provided. Similarly, in the LLM section, there is no explanation for why the Sematle task uses the T5-base model while the 1D-ARC task uses the Qwen1.5 model. ICLR has clear expectations regarding reproducibility (https://iclr.cc/Conferences/2025/AuthorGuide), and the author is encouraged to include such information at the end of the paper. Perhaps a reproducibility statement is not necessary, but at least it should ensure that key parameters are covered in the paper. 
- Expression. The entire manuscript should be carefully proofread; otherwise, it is not ready for publication. For instance, "warm-start" and "warmstart" are used interchangeably (lines 685 and 689).

### Questions
1. Why doesn't the author provide an overall framework diagram of the BOPRO or use the "Algorithm" environment in LaTeX to fully describe the BOPRO process? The current description is quite unclear, making it difficult for readers to form a comprehensive understanding of the relationship between BO and LLM.
2. Why are Qwen-1.5 and T5-base used as the base models? Specifically, (a) why are different models used for the two tasks? (b) why are other models (such as Llama) not evaluated, or why hasn't an ablation study been conducted on the base models? (c) If BOPRO is based on prompts, why not consider using the GPT-4 series as the base model (especially since the original paper on the 1D-ARC dataset also evaluated performance on GPT-4)?
3. As mentioned under "weaknesses", if the goal is to show the generality, comprehensive experiments on multiple search tasks are needed. The following problems could serve as useful references: combinatorial optimization (e.g., traveling salesman problem, knapsack problem), path planning and navigation, game problems (e.g., in reinforcement learning environments, Go, or chess), and program synthesis. While it may be challenging for the author to cover all types of tasks, covering too few problem scenarios is insufficient to demonstrate the generality of BOPRO. Why hasn't the author attempted more tasks?
4. The comparison methods are not strong enough; simple greedy strategies represent very basic approaches. In the introduction, the author lists a series of highly relevant methods and highlights their shortcomings. Why doesn't the author conduct comparative experiments to demonstrate these shortcomings (as mentioned in lines 51-52, "too expensive, not performant enough, or impractical in offering a general solution for search")?
5. Regarding exploration and exploitation, the author mentions that "we are interested in answering whether search with large language models (LLMs) can handle this trade-off"(line 43). Although the trajectory demonstrates a good balance, is this really the capability of the LLM? Most BO-based frameworks specifically balance exploration and exploitation, typically related to the choice of acquisition function. The BO acquisition functions used in the experiments all include sufficient exploration components, so is this balance due to them? This question is not well addressed and may require ablation studies to clarify. 
6. The author mentioned that "BOPRO trails a strong greedy baseline in aggregate"(line 26-27). Is this due to the prompt design? Can better performance be achieved by modifying the prompt?

### Soundness
3

### Presentation
2

### Contribution
2
