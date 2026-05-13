# Bayesian Optimization of Antibodies Informed by a Generative Model of Evolving Sequences

- Decision: Accept
- Scores: 5, 8, 8, 8

## Abstract
\let\thefootnote\relax\footnotetext{* Equal contribution}
    To build effective therapeutics, biologists iteratively mutate antibody sequences to improve binding and stability. Proposed mutations
    can be informed by previous measurements or by learning from large antibody databases to predict only typical antibodies. Unfortunately, the space of typical antibodies is enormous to search, and experiments often fail to find suitable antibodies on a budget. We introduce Clone-informed Bayesian Optimization (CloneBO), a Bayesian optimization procedure that efficiently optimizes antibodies in the lab by teaching a generative model how our immune system optimizes antibodies. Our immune system makes antibodies by iteratively evolving specific portions of their sequences to bind their target strongly and stably, resulting in a set of related, evolving sequences known as a \emph{clonal family}. We train a large language model, CloneLM, on hundreds of thousands of clonal families and use it to design sequences with mutations that are most likely to optimize an antibody within the human immune system. We propose to guide our designs to fit previous measurements with a twisted sequential Monte Carlo procedure. We show that CloneBO optimizes antibodies substantially 
    more efficiently than previous methods in realistic \textit{in silico} experiments and designs stronger and more stable binders in \textit{in vitro} wet lab experiments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper treats antibody design from pure sequence view, using clonal family to guide the model. The paper shows CloneBO can optimize antibody sequences better than former methods. Outstandingly, some experiments in vitro also support the effectiveness, which is often ignored in similar works.

### Strengths
1. The idea of applying martingale in antibody optimization is novel, and surprisingly fits the nature of evloving process of antibody.
2. Wet lab experiment is a highlight.

### Weaknesses
1. The experiment seems weak. Many influential works in recent years are not taken into comparison, such as[1][2]. They authors claim that structure based de novo design cannot make use of previous measurements and must have access to structure so they are not suitable for this task, which I highly suspect. Antibody is a specific protein type that highly reliable on its structure to perform. Even though stucture data are scarse, authors should demonstrate CloneBO’s supriority by showing that using massive sequence data can lead to higher performance only using sequence.
2. The representation is vague. Without any specific table, it’s hard to comprehend directly. This could also be a potential problem for following works to follow.

### Questions
1. Does the optimization process in Fig. 3a converge? It seems that fitness is still rising in the end.
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In this paper authors propose CloneBO - a procedure which aims at streamlining the antibody sequence optimisation. The approach relies on a language model which training is heavily inspired by the evolutionary mechanisms present in the immune system and allows for iterative guidance of generation by taking into the account previously measured samples. Authors validate their approach both in silico and in vitro demonstrating significant improvements over other methods.

### Strengths
This paper focuses on antibody sequence optimisation, an important problem of multi-objective nature that is encountered in every drug discovery project. Approaches that improve this drug pipeline stage have a potential of streamlining development of antibody-based therapies by shortening the development process and decreasing its costs.
The main original contribution of this paper lies in jointly modelling the clonal families (groups of evolutionarily connected antibody sequences that are computationally inferred from large scale sequencing data). 
Authors validate their approach on several benchmarks and showcase potential of improving individual relevant traits of antibodies like binding affinity, humanness and thermal stability. Reported results significantly outperform state-of-the-art methods. Improvements are reported both in silico (through better predicted scores of trained oracles) and with in vitro experiments, which significantly strengthens the contribution.

### Weaknesses
Method requires initial, viable sequence i.e. the starting point from which the optimisation begins. This limits the applicability in some design scenarios where such sequence is not known and therefore hinders the impact of the approach compared to parallel lines of research that focus on e.g. structure based binder design and optimisation.



### Questions
Training of CloneLM relies on a data pre-processing step (grouping of sequences into clonal families) done with FastBCR. Since this is a critical initial step I wonder if the authors examined the effects of different preprocessing tools or hyperparameters on downstream performance or at least, given the large resource demands of LM training, the changes in distribution of processed data.

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
The paper introduces a method, termed CloneBO, for optimizing antibody sequences for stability and binding. Their approach uses an LLM to model the distribution of a collection of clonal populations of antibodies, drawing inspiration from the evolutionary trajectories of antibodies in the body to predict beneficial mutations. The authors introduce several ideas to improve sampling quality from their LLM, including sampling from a martingale posterior and constructing a twisted MC scheme that biases towards observed antibodies. Their approach is tested both on in silico benchmarks and in vitro experiments and shows outstanding performance in the design tasks they’ve attempted.

### Strengths
* Context sharing and placement of the solution: The exposition is strong (on the antibody design problem), code is shared, well-organized and readable. The paper targets an important problem and is lucid about how to get to impact in that domain. 
* Innovation: Multiple interesting and recent ideas have been introduced together for this problem domain (Simulating clonal evolution, Martingale posteriors, combining twisted Montecarlo and LLMs), and the results are convincing in silico and in vitro. 
* Benchmarking: multiple relevant design approaches have been benchmarked, and the method performs well comparatively. 
* In vitro validation: The authors conduct extensive validation, both in silico and in vitro. In vitro validation is rare among ML papers but absolutely crucial in evaluating whether the method has practical use. The authors have done ablation studies on the effects of their sampling scheme and show each individual component helps the performance of the optimizer.

### Weaknesses
 * The experimental data are not shared. This is not disqualifying for an ML paper in my view, but should be noted as a weakness. 
* The paper is well structured but somewhat hard to read, partly due to the many ideas that it tries to cover in the main text. I suggest moving some of the mathematical exposition into the SI and describe the intuition more concisely but clearly.

* I’m not clear on the exchangeability claim, evolutionary processes have a clear arrow of time, with sequences ordered in a way that can be predicted, unless we are only looking at the final leaves of the tree, which in my understanding is not necessarily true for immune populations. I appreciate a clearer exposition here.  
* I’m unsure why the authors have chosen to model the light chain and heavy-chains separately. A clear explanation would be helpful. 
* Line 39: “up to thousands of previous iterations” this is somewhat misleading, not all iterations are the same as in many cases these are done in batches (“measurements” are always done in batches), and batch-iterations rarely exceed 10. In silico iterations can reach thousands but the description here is blurry and especially “measurements” is best reserved for real world queries rather than oracle queries.

### Questions
* I’m not clear on the exchangeability claim, evolutionary processes have a clear arrow of time, with sequences ordered in a way that can be predicted, unless we are only looking at the final leaves of the tree, which in my understanding is not necessarily true for immune populations. I appreciate a clearer exposition here.  
* I’m unsure why the authors have chosen to model the light chain and heavy-chains separately. A clear explanation would be helpful. 
* Line 39: “up to thousands of previous iterations” this is somewhat misleading, not all iterations are the same as in many cases these are done in batches (“measurements” are always done in batches), and batch-iterations rarely exceed 10. In silico iterations can reach thousands but the description here is blurry and especially “measurements” is best reserved for real world queries rather than oracle queries.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new way to design antibodies using Bayesian optimisation. In contrast to most closely related existing aproach (Lambo) the authors propose a different way to capture the prior antibody distribution. They train a PLM on clonal families, to capture how the imune system diversifies antibodies. They also introduce a twisted sequential Monte Carlo procedure to better incorporate previous lab measurements (sucessful designs). The in silico and in vitro results show that the proposed procedure improves upon Lambo in terms of antibody synthesizeability and stability.

### Strengths
I find it quite a unique and nice idea to try to produce local diversification around the seed that matches diversification our body produces during imunization and it's implementation is going a bit of the beaten path with for example the martingale posterior. The experiments are quite thorough and convincing, with a strong baseline. The paper itself is well written and easy to follow.

### Weaknesses
This is not a big weakness, but I'd say that the CloneLM model makes more Fv mutations than one would expect. Also, in appendix the clonal familly does not fix the missing starting gap '-' in some cases, which is not ideal as it would always be a 'Q' for human Ab with the given subsequent amino acids.

The melting temperature and binding oracle experiment uses VHHs, which I would say is not ideal. While humanized VHHs do look kinda like human VH chain, they are still different, even in trivial ways (e.g. they often have much longer CDR H3). It's nice that the proposed method deals with this distribution shift, but it's not entierly fair to compare to the baselines, that were only developed for 'normal' Abs.

In the paper you write "de novo design method DiffAb", but DiffAb it's not de novo, it needs a co-crystal structure as a starting point.

Figure 4 (b) second plot, only 1 point beats best point of Lambo, the average of Lambo also looks better so I'm not fully convinced that the proposed method produces more stable antibodies. Of course, the KD results are quite convincing.

### Questions
When training the ClonalPLM are the clonal families (their order) re-mixed (e.g. for Light chain as it uses many epochs) if not, how is the ordering chosen?

What is the edit distance distribution for the in-vitro designs? In the method description (Section 6.4) you state "iteratively optimize F(X) over the top substitution for up to 3 substitutions", does this mean that designs can only have maximum edit distance of 3 in your experiments? If yes were the baselines constrained to the same edit distance?

### Soundness
3

### Presentation
3

### Contribution
3
