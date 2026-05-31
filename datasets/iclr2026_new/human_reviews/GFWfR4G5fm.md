## Human Reviewer 1

### Summary
This paper introduces TTT-SCL (Test-Time Training for Supervised Causal Learning), to address the poor out-of-distribution generalization of current supervised causal discovery methods.

The authors first show through experiments that current supervised methods suffer from fragility to distribution shifts, failure in compositional generalization, and a significant performance gap between synthetic benchmarks and real-world data.  They highlight the need of "diversity" in training data.

The authors then propose to generate training data at test time that is aligned closer to test instances.  The underlying causal model is assumed to be additive noise models.  Under this, the candidate causal graph is regressed against the test data, and ones with high regression consistency are admitted into training set, together with their forward sampled data.

Experiments show that TTT-SCL achieves stronger and more consistent performance than other pre-trained supervised methods.

### Strengths
1. The goal is well-motivated and timely.  The authors correctly identify a real gap in the supervised causal discovery literature: the strong in-distribution performance but poor robustness under realistic domain shifts.

2. Their diagnosis through controlled experiments (mechanism/graph/noise shifts) is thorough and convincing to reveal the above issues.

3. The whole method procedure and the graph refinement strategy are simple and heuristic.  They seem to perform well though, via the experimental results reported by authors.

### Weaknesses
1. **The work lacks any kind of formal theoretical analysis:** 
- While it is understandable that their identifiability results are rooted back to the additive noise models setting, the key arguments in this paper itself still need more justification.
- For instance, at line 281, ".. if.. closely aligned.. (Dk≈Dtest), then .. is likely a close approximation.. (Gk≈Gtest)."  The authors need to discuss the scale of "≈":  Do same levels graph differences (e.g., measured by structural hamming distance) always lead to the same levels of differences in the sampled data?  Should this "alignment of distribution" score, as well as the sparsity constraint, be normalized by the sample size of data or graph size?  These problems need to be addressed to ensure the supervised method is grounded.
- Moreover, within the scope of this work the unique identification of the DAG is guaranteed by ANM.  Then what about other cases where only an equivalence class is identifiable?  How to characterize the "Gk≈Gtest" in that case?  These should be discussed.

2. **Search space for training instances can be improved to prevent from overfitting:**  Currently only the new graphs are generated for test-time training, together with the data forward sampled from them using the parameters regressed on data.  However, these regressed parameters can be arbitrarily complex, leading to overfitting issues.  Could the authors please explain why new data generating functions are not generated together with graphs, and in a way similar to regularize the sparsity for graphs, regularize the complexity of these functions?

3. **Search strategy for training instances can also be improved for efficiency:**  Currently the "optimal new training graphs" are searched through stochastic graph refinement.  It seems that many existing optimization based causal discovery methods can be incorporated as a component to directly optimize the AD score.  Existing unsupervised causal discovery methods may also be used to get some "base graphs" to modify from.  Following this, some existing supervised causal discovery methods may also be viewed as "test-time training".

4. **The overall presentation and writing is poor:**  For instance,
- The authors introduce unnecessary technical notations even in the start of the first introductory paragraph.  
- The whole section 3.1 is hard to read, where more natural language are expected to explain the experimental setup.
- The term "low sparsity" in Figure 2 can be ambiguous.
- Too much abbreviation abuse throughout the paper.  What is the authors' proposed method, TTT-SCL or TACTIC?  The abbreviation for AD seems unnecessary, and subscripts with ("G", "U") noise notations only make section 3.1 hard to parse.  At the same time, many abbreviations are used before explaining them, e.g., the "DAG" is used at line 37 but only declared at line 104.

### Questions
see "weaknesses"

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
This work firstly shows that traditional methods for Supervised Causal Learning (SCL) based on pretrained models that map a dataset $D$ to a graph $G$ fail to generalize to out-of-distribution data.  To address this issue, the Test Time Training for Supervised Causal Learning (TTT-SCL) framework is introduced - along with an algorithm, TACTIC, that implements it. In a nutshell, TACTIC generates a set of graph candidates that maximize a sparsity-regularized goodness-of-fit score for the test data. Then, it produces datasets $\{D_{t}\}_{t}$ for each graph by regressing a predefined causal mechanism into the test data. Finally, it fine-tunes an existing SCL algorithm (AVICI) on the sampled graph-data. 

Overall, the introduced approach is seemingly sound, clearly positioned in the realm of SCL algorithms, simple, and demonstrably effective through well-executed experiments. However, I have a few concerns regarding exposition and reproducibility (listed below), and I will be happy to give a positive review for the work in case they are addressed.

### Strengths
1. Both TTT-SCL and TACTIC are clearly described and properly evaluated.

2. Limitations of prior works are nicely discussed and experimentally assessed.

3. The method has clear advantages over existing, test-data-independent, approaches, which are confirmed by comprehensive experiments.

4. Figures 1 and 2 are quite helpful in understanding the TACTIC.

### Weaknesses
1. Code has not been publicly released, which is a major drawback for reproducibility  - especially given the empirical nature of the work. Will the authors release the code?

2. As I understand, the generated graph-data pairs are either used for training a SCL from scratch or fine-tuning an existing SCL, although I am not sure which approach is undertaken. Could the authors clarify this? I believe this is a major component for the work that lacks a clear description.

3. If it is only training from scratch, the optimization problem could be formulated as

$$
	\min\_{G} \mathbb{E}\_{G \sim P\_{test}} [ L(G, D\_{test}) | D\_{test}], % . % .
$$

for whichever (empirical) distribution $P\_{test}$ is induced by the score function in Equation (5) and a loss function $L$ that defines the training of the underlying SCL model (AVICI). Is this correct (Otherwise, how can we compare fine-tuning vs. training the SCL model from scratch?) In this case, TACTIC is equivalent to score-based Causal Discovery algorithms - with a specific, stochastic score - and I believe that the distinction in Figure 1 is inaccurate. 

4. Out of the three presented issues (lack of robustness to distribution shift, failure to perform compositional generalization, and mismatch between real and synthetic tasks), only two of them have been assessed on the experiments, as far as I understand. Could the authors elaborate on how TACTIC addresses compositional generalization (perhaps through experiments)?

### Questions
Please refer to the section above.

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
The authors illustrate limitations of supervised causal discovery, and propose a framework (TTT-SCL) and a method (TACTIC) to overcome these limitations. In particular, given that the main issue is the inability of SCL methods to generalize out of distribution, they propose to generate data at test time for fine tuning/training of an SCL method.

### Strengths
The studied problem is important and timely. An interesting contribution is the empirical evidence of failure of AVICI to generalize to Sachs nd Syntren, two (pseudo) real datasets.

### Weaknesses
1. **Novelty.** The first two issues identified in the paper about SCL are known e.g. from Montagna et al., 2024, which the authors fail to mention and discuss in relation to their work. The third issue is nice to be observed, but it is a corollary of the other two: if we show that SCL fails OOD  in synthetic settings, the same should happen in real settings (but it is nice to see! Not sure somebody showed it before)
2. **Novelty.** In relation to Issue 2: the same problem is observed in Montagna et al., 2024 (figure 4 in their paper). However, they show that the performance gap is closed as you increase the number of training datasets (see figure 12 in Montagna et al., 2024). In your setting, it is unclear how many datasets from each SCM type (eg RFF_G_ER is one SCM type) are used in the mixed setting, so it’s also unclear whether the conclusions in Montagna et al., 2024 would apply here. This requires discussion.
3. Given that the novelty in the identified issues in SCL is at best only partial, the main contribution is the algorithm to mitigate distribution shifts. I see two big issues here
    1. **Statistical significance of experiments**. Conclusions of improved performance of TACTIC on (pseudo) real data can not be drawn only from two datasets (Sachs and Syntren)
    2. **Methodological/conceptual.** TTT-SCL/TACTIC, in order to work, requires training/fine-tuning on the test data **assuming they were generated according to an identifiable SCM;** in the paper, an additive noise model. Then (as already discussed in Montagna et al., 2024), this is equivalent to restricting the space of solutions under the assumptions of an additive noise model: if we are willing to make this assumption, why use SCL in the first place? I can use any of the known methods for causal discovery on additive noise models (SCORE, RESIT, NOGAM, GranDAG, …). The clear advantage of these methods is that they do not require a training procedure, so there is not even the problem of distribution shifts: e.g., there is no issue of noise distribution shift, as most of these methods simply don’t need assumptions on the noise distribution. In this light, I don’t see the improvement that TTT-SCL/TACTIC brings to the table of algorithmic causal discovery.
4. Other issues
    1. **Reproducibility.** The authors fail to provide sufficient specifications on the training
        1. In the TACTIC procedure, how do you choose the noise distribution of the SCM
        2. In TACTIC, how do you choose the algorithm to sample the graph?
        3. In section 3.2, how many datasets do you use for training, each one with how many samples?
        4. In section 3.2, what are the specifics for AVICI training
    2. I am not sure NOTEARS, GES, and PC are the most probing methods to compare to. Since this is mostly an algorithmic paper, many more comparisons are needed (SCORE, CAM, NoGAM, RESIT provide good baselines for ANM causal discovery — these are just some of my picks, feel free to change/expand)
    3. **Clarity**. 
        1. In section 3.2, the choice of presenting the results with a table, no highlights, doesn’t really help to deliver the message. Please consider using figures?
        2. L212: “Each specific training data setting is indicated above the result”. I assume this refers to tables? Please clarify this, and also consider making this explicit in the tables’ captions.
    4. L222: “AVICI can be considered the strongest model of open source under the SCL paradigm”: any evidence for this?

### Questions
Please refer to the weaknesses section

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 4

### Summary
This paper argues that the standard static pre-training paradigm for Supervised Causal Learning (SCL) is flawed, demonstrating its fragility to distribution shifts and failure to generalize from synthetic to real data. It proposes a new paradigm, Test-Time Training for SCL (TTT-SCL), which generates a small, bespoke training set for each test instance on-the-fly. The core idea is to search for training graphs that maximize an "Alignment of Distribution" (AD) score with the test data, penalized by a sparsity term to ensure causal minimality. The paper's implementation, TACTIC, uses stochastic graph refinement to generate this data. Experiments show TACTIC substantially outperforms established SCL and traditional baselines in challenging OOD and real-world settings.

### Strengths
The primary contribution is significant and original: it introduces the first test-time adaptation framework for SCL, fundamentally reframing the problem from seeking universal diversity to achieving targeted concentration. Apart from that, I highlight the following points:
- Principled test-time framework for causal discovery; clear link between distributional alignment and causal minimality.
- Rigorous OOD diagnostics (shift, composition, synthetic-real gap).
- Comprehensive experiments with two backbones and multiple metrics.
- Insightful sparsity ablation showing dense graphs mimic data yet harm causal accuracy.

### Weaknesses
1) Scalability: results ≤ 20 vars; K = 200 graphs + SIM fitting may be heavy; no runtime or complexity analysis.
2) Initializer dependence: performance drops sharply without NOTEARS seed; robustness unclear.
3) Theory: no guarantees that AD optimization recovers true graph or stable minima.
4) Evaluation breadth: only Sachs as real dataset; no interventional or large benchmarks.

### Questions
1) How is the runtime breakdown vs. AVICI for d >= 20, K = 200?
2) How sensitive is λ across datasets; any adaptive tuning needed?
3) How does performance scale with poorer or random seeds?
4) Could hybrid fine-tuning of pretrained SCL with TTT-SCL reduce cost?
5) Is AD robust under misspecified mechanism regressions?
6) Recent works explore adaptive or amortized causal graph generation via generative sampling and refinement (e.g., [1,2]). How does TACTIC relate to these frameworks that also perform dynamic graph generation, and could TTT-SCL benefit from such generative sampling instead of heuristic refinement?

[1] Bayesian Structure Learning with Generative Flow Networks. https://proceedings.mlr.press/v180/deleu22a/deleu22a.pdf
[2] Expert-Aided Causal Discovery of Ancestral Graphs. https://arxiv.org/abs/2309.12032

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
4