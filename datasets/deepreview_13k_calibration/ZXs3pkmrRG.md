# Test-Time Learning of Causal Structure from Interventional Data

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 3, 6, 5

## Abstract
Inferring causal structures from interventional data remains a challenging task, especially when the intervention targets are unknown. *Supervised Causal Learning (SCL)* demonstrates strong empirical performance in predicting causal structures by training on datasets with known causal relations and applying the learned models to unseen test data. However, existing *SCL* methods often face inherent generalization challenges and struggle with the diverse intervention settings encountered in the *interventional causal discovery* problem. 

In this work, we propose _**TICL**_ (**T**est-time **I**nterventional **C**ausal **L**earning), a novel approach that follows the *Test-Time Training (TTT)* + *Joint Causal Inference (JCI)* paradigm to address these challenges of generalization and versatility, respectively. Specifically, _**TICL**_ employs a self-augmentation technique that generates training data at test time, tailored to the characteristics of the test data, enabling the model to adapt to the inherent biases in the test distribution. Additionally, by integrating the *JCI* framework with *SCL*, _**TICL**_ replaces the rule-based logic of the standard PC algorithm with a learning-based approach, effectively leveraging self-augmented training data. 

Extensive experiments on bnlearn benchmarks demonstrate _**TICL**_'s superiority in multiple aspects of causal discovery and intervention target detection.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors focus on the setting where we have multiple datasets describing the same system, but each dataset was collected under a different set of interventions, whose targets may be unknown.  This problem setting matches that of the joint causal inference framework proposed by Mooij et al., which provides a framework for combining such a collection of datasets and conceptualizing them with a single graph.  The authors propose a novel method, TICL, that first generates semi-synthetic data from from a graph structure learned from the unified JCI datasets, producing a training dataset.  TICL then uses this data to in a two-phase PC-like supervised causal learning process, using classifiers to determine first edge existence and then V-structure orientation.  The authors compare TICL to a variety of other methods on bnlearn baselines and find that it consistently performs the best.

### Strengths
I think this is a good paper.  The authors take two existing techniques (JCI and SCL), describe both of them well, and provide an interesting combination that both feels intuitive and clever.  The writing is, for the most part, clear throughout, with consistent terminology and notation.  The experimental results, while only semi-synthetic (due to the lack of real-world interventions), are thorough and compelling, comparing against a solid range of competitive methods in multiple categories.

### Weaknesses
I appreciate the attempt at a "When", "What", "How" framing in the introduction, but the framing of "We create training data after accessing the test data" is strange and over-complicates what you're actually doing.  If I understand correctly, your approach is a two-stage process, using the input data $D$ to generate augmented semi-synthetic data, which is used to train a model that to classify $D$ in your second stage.  I think part of the confusion is the use of the term "test data" here, since in ML, tests data is usually a dataset that is used at the very end of a pipeline to assess model performance, which doesn't really match the standard causal inference setting.  I didn't understand the text of the "When" section in the introduction at all until I had nearly finished the paper, and even then it took multiple times reading it to understand what you were trying to say.  Rewording that section to focus on how the data that is typically use for SCL training differs from what you use, and how that allows you to train an SCL model that is far more tailored to your specific problem.

Not being very familiar with the JCI framework before reading this paper, I found the organization around Sections 3.1 and 3.2 confusing.  Figure 2, and the discussion of it at the end of 3.1, is very helpful, but it makes use of the JCI framework (referencing intervention families and showing how intervention targets are present in the graph).  This figure makes a lot of sense after reading Section 3.2, but since it's presented and discussed in 3.1 (even using terms like "intervention family" before they are defined), it mostly serves to confuse and force the reader to try to understand the JCI framework from context clues.  Moving the final paragraph of 3.1 until after Section 3.2 would help a lot.

While I generally like the experimental results, some of the discussion there feels a bit disingenuous.  The authors state one of their key advantages  over other recent methods is that you tested on "real causal graph datasets with over 100 nodes", and in the "Benchmarks & Baselines" section, you say that you "use discrete datasets of 14 real-world datasets collected from the bnlearn repository".  This implies that all 14 of the datasets are "real-world datasets", many of which are over 100 nodes.  However, unless I'm missing some experiments or missing something about the bnlearn datasets, the only one of the 14 you list that has over 100 nodes is Pathfinder, which has 104, and some of the bnlearn datasets you chose (Asia, Insurance, Alarm, Hailfinder) are synthetic, so calling them "real-world datasets" is strange. 
You definitely test on a broader array of datasets than "only synthetic with 10-30 nodes", so I think that's a fine distinction to highlight, but it would be helpful, when describing the datasets you used in the "Benchmarks & Baselines" section, to be clearer about the range of nodes and realism of the datasets you chose.

I understand your reasoning, but it's a bit strange to call AVICI and ENCO "unfair baselines".  While they are told the intervention targets and other methods are not, TICL and the other JCI-based methods also have the distinct advantage that the data you are testing on is data from bnlearn that you modified (via interventions) to exactly match the problem setting for the JCI framework, upon which TICL is based, so it's not surprising that methods designed to work on data with multiple interventions with unknown targets perform better than methods intended to work on data with either a single intervention or known intervention targets.  You of course should make it clear to the reader that AVICI and ENCO had access to that information, since the fact that TICL doesn't need it to be competitive is a clear advantage, but I would drop the language about them being unfair baselines because of it.

A real-world example would help a lot towards showing the value of this method.  While the method seems interesting, the setting of "We have both observational and interventional data that measures the same variables, but the targets of each intervention are unknown" comes across as very niche and not very applicable.  I don't think that's necessarily the case, but providing even a simple motivating example in the introduction would help explain to the readers why we should care about your method.

In Table 1, the meaning of blue/bold and red/underlined should be included in the Table 1 caption, rather than in the "Training Datasets & Metrics" section, so the table can be at least somewhat stand-alone.  I would also put Footnote 1 on the table, rather than at the beginning of the list of methods (especially since you don't actually use the * until the table).

A minor point, but in Table 1, it would be good to use some other indicator for "JCI-Improved baseline", "Unfair baseline", and "classic baseline" besides a light background color.  As is, it's impossible distinguish when printed in black and white and even in color, the light yellow for "classic baseline" blends in far too much with the background and looks too similar to the pale green.  Similarly, in the two right plots of Figure 4, it's odd to use different symbols and colors for the points, but only include the colors (and not the symbols) in the legend.  You should make the legend show the shapes as well.

### Questions
Can you clarify the loop structure of Algorithm 1?  The parallelization loop index, $i$, is not used in the algorithm pseudo-code, and if that loop is being done in parallel, then presumably there's no looping back to step 1 from step 7, right?  But then step 1 starts with us already having $G^{t-1}$.  Where is $t$ initialized?  I wondered if maybe steps 1-7 were being done iteratively until IS-MCMC converges, but then I'm not sure what's happening with the $D^{(t)}$ that's sampled in step 7, since if we're making a list of each $D^{(T)}$ dataset for each variant of $G^{(t)}$ we see, then we'd probably want some sort of burn-in period, which isn't part of the algorithm.  But if we're just keeping the final $D^{(t)}$, then there's no reason for it to be in a loop... Clearly there's something I'm missing with how this algorithm is set-up.

You mention that you consider soft-interventions for your experiments.  Can you give an example of the type of soft intervention you simulated?  Did you try experiments with hard interventions, and, if so, were the results essentially the same?

Did you try comparing against generating $D^{(t)}$ from Algorithm 1 and then just using standard PC on it, rather than your custom PC-like approach?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an algorithm that performs causal discovery from observational and interventional data while adapting to test-time training. It is built upon the joint causal inference and supervised causal learning frameworks. The authors provide their performance results on a variety of causal graphs.

### Strengths
The authors address a very interesting and important problem. The experiments are extensive, and the necessary background to understand the paper is provided.

### Weaknesses
## Minor Weaknesses:
* The introduction discusses many contributions, which might be a little distracting.
* Figure 2's caption should mention what the numbers in the curly brackets refer to.
* $X_2 \to X_1 \leftarrow \{1\}$. It is unclear why $\{1\}$ is considered a node here.
* Assumptions such as Markovian, faithfulness, sufficiency, etc. should be defined and explained.
* I-CPDAG is not discussed in detail, although it is used many times.
* JCI considers data samples under interventions as observations under imposed conditions — this statement appears repetitive.
* $D_i$ is likely to be in the neighborhood of the original augmented dataset. It is unclear what "neighborhood" means.
* It is unclear what "high-quality training data" means. This should be made precise.
* It is not properly defined what $G^{(t-1)}$ refers to in the mutation step.
* The numbers 1-6 in the key steps could be shown in Figure 3 for better mapping.

## Major Weaknesses:
* It is hard to focus on the main contribution: Is it I-CPDAG discovery, finding the intervention target, test-time adaptation, PC+SCL, prior knowledge, etc.?
* The presentation of the paper needs to improve a little more. It feels like too many things are going on. The description needs to be clearer.
* Although test-time adaptation was the main motivation of the proposed approach, it is discussed very little.
* Are the authors proposing to train a classifier for each possible triplet to detect if it forms a v-structure? That would be very computationally inefficient. How is that better than using the PC algorithm? The training procedure needs more detailed discussion.
* The Asia graph from bnlearn is not a real-data graph. Please check its reference.

### Questions
## Questions:
* If the $\text{score}(G^{\text{cand}}) < \text{score}(G^{(t-1)})$ and $\frac{\text{score}(G^{\text{cand}})}{\text{score}(G^{(t-1)})} = 0.9$, does that mean $G^{\text{cand}}$ is chosen with probability 0.9 even if its score is lower? Doesn't that mean we will gradually move toward incorrect graphs?
* To my knowledge, the 14 graphs from bnlearn are mainly observational (except Sachs). How are the authors generating observational and interventional datasets from these graphs?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors tackle the problem of inferring causal structures from interventional data with unknown targets, where standard Supervised Causal Learning (SCL) often fails due to distribution shifts. They introduce TICL (Test-time Interventional Causal Learning), which leverages self-augmentation at test time to adapt the model to test data biases. TICL integrates the Joint Causal Inference (JCI) framework, transforming rule-based logic into a learning-based approach that better utilizes augmented data. Extensive experiments show TICL's effectiveness in causal discovery and target detection.

### Strengths
The main contribution of the authors is their proposal of a novel JCI+SCL paradigm for causal discovery under unknown interventions from discrete data. Their TICL approach significantly advances the state of the art in discovering causal relations and interventional targets, achieving an average F1-score improvement across diverse real-world datasets. The authors introduce self-augmentation within SCL, enhancing training instances from the test data, and implement the IS-MCMC algorithm, which effectively samples graphs from the posterior distribution and generates compatible data for training. Their systematic study highlights JCI as a promising direction for interventional causal discovery, with TICL offering flexibility and requiring fewer assumptions in various intervention settings.

### Weaknesses
Although the paper is a well-contributed effort on empirical and experimental sides, showing significant advancements over the state of the art, I still believe the paper can improve with some theoretical justification on key steps involved in the proposed approach. For instance, the claim that the algorithm IS-MCMC samples $G$ from the posterior estimation $P(G|D)$ and that the data $D_i$ is compatible with $G_i$ is made. However, the authors do not justify how the stationary distribution of the constructed Markov chain matches the posterior distribution of graphs given the data. Specifically, the Metropolis-Hastings algorithm requires careful design of the proposal distribution to ensure ergodicity and convergence to the target distribution, and this aspect is not sufficiently addressed. Similarly, there is a lack of discussion on the sampling convexity for convergence of the Markov chain. The authors should provide a more rigorous analysis of the conditions under which the Markov chain converges to the desired posterior, including a discussion of the mixing time and the properties of the proposal distribution that guarantee convergence. If the authors can clarify these issues, I would be willing to revise my score for the paper and see it as a more valuable contribution to the field.

### Questions
I have few question for the authors:

* Can the authors provide some justification on how the stationary distribution of the constructed Markov chain(s) in IS-MCMC matches the posterior distribution of graphs given the data?
    
* What is a good criterion (or number of samples) to ensure proper convergence for the constructed Markov chain(s)?
    
* The authors claim that a binary classifier enables us to replace heuristic searches and potentially erroneous conditional independence (CI) tests with a robust classification mechanism. Do the authors have any empirical evidence for this claim in their set of experiments?
    
* In experiment section 5.1, the authors mention that they sample, or forward-sample, 10,000 samples for both observational cases and each intervention. I wanted to ask how one would choose this number. Is there a risk of overfitting if the chosen sample size is too large? If not, can you explain why it is generally better to use a larger number of samples?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a supervised causal discovery framework that is composed of three steps. First, they convert the given interventional data collection into an augmented observational data samples. Then, they generate simulation training data from the augmented samples. Finally, they tune a supervised PC algorithm for identifiying the causal graph.

### Strengths
**1**. The paper is clearly written and easy to read.

**2**. The authors conduct extensive experiments to validate their method.

### Weaknesses
 **1.** The novelty of this paper is limited. The first step, pooling interventional data into observational data samples, was introduced by Joint Causal Inference (Moiij et al., 2020). The second step, generating simulated trainning data via a proxy algorithm and Maximum Likelihood Estimation (MLE) for estimating the conditional probability, has been proposed by ML4S (Sec. 5; Ma et al., 2022). This paper is just a trivial combination of existing methods.

**2**. The supervised PC algorithm (Step 3) is problematic. Now that you already test conditional independence from data (Sec. 4.1, Freaturization step), why do you use a supervised classifier to determine the v-structure, instead of adopting the orientation rules that enjoy the theoretical identifiability? The approach costs more computations (to train the classifier) and meanwhile loses the identificiation guarantee.

### Questions
See the weakness above.

### Soundness
2

### Presentation
2

### Contribution
2
