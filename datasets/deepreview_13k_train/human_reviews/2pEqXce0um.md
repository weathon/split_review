# Root Cause Analysis of Failure with Observational Causal Discovery

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Finding the root cause of failures is a prominent problem in many complex networks. Causal inference provides us with tools to address this problem algorithmically to automate this process and solve it efficiently. The existing methods either use a known causal structure to identify root cause via backtracking the changes, or ignore the causal structure but rely on invariance tests to identify the changing causal mechanisms after the failure. We first establish a connection between root cause analysis and the \textit{Interactive Graph Search (IGS)} problem. This mapping highlights the importance of causal knowledge: we demonstrate that any algorithm relying solely on marginal invariance tests to identify root causes must perform at least $\Omega(\log_{2}(n) + d\log_{1+d}n)$ many tests, where $n$ represents the number of components and $d$ denotes the maximum out-degree of the graph. We then present an optimal algorithm that achieves this bound by reducing the root cause identification problem as an instance of IGS. Moreover, we show that even if the causal graph is partially known in the form of a Markov equivalence class, we can identify the root-cause with linear number of invariance tests. Our experiments on a production-level application demonstrate that, even in the absence of complete causal information, our approach accurately identifies the root cause of failures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors provide a method for identifying the root cause based on marginal invariance tests. The proposed method includes two steps: first, recovering the skeleton of the underlying causal model using normal (pre-failure) data, and second, constructing an augmented graph using invariance tests to identify the root cause by computing conditional mutual information. The authors demonstrate that, if the underlying causal model is known, the root cause can be identified using $O(\log(n))$ marginal invariance tests, where $n$ is the number of observed variables. Additionally, given observational data, the root cause can be recovered using $O(n)$ invariance tests according to the proposed algorithm.

### Strengths
1. The organization of the paper is easy to follow, although some technical parts are not clear (see Weakness 3).
2. The authors provide detailed simulation results to demonstrate the performance of the proposed algorithm. In particular, the authors present multiple variants of the proposed RCG algorithm with different graph inputs.

### Weaknesses
1. The main theoretical results in Sections 4 and 5 are based on the implicit assumption of atomic intervention (i.e., only one variable is affected by the failure mode). This is a very strong assumption, and existing methods such as RCD do not rely on this assumption. For example, in Figure 5, given that $F$ is not independent of $X_2$, it might be the case that both $X_2$ and $X_3$ are directly affected by $F$. This assumption limits the applicability of the proposed method in real-world scenarios where failures can have cascading effects, impacting multiple variables simultaneously. The theoretical guarantees provided are thus contingent on a rather restrictive condition.

2. Section 5 lacks a theoretical guarantee of the recovery output, which may make the comparison with RCD unfair. It has been shown in RCD that the true root cause can be uniquely identified given infinite data (without knowing the graph structure or the number of root causes), although it may require an exponential number of invariance tests. The authors claim that only $O(n)$ invariance tests are needed in the RCG algorithm. However, there is no guarantee of recovery accuracy; that is, it is unclear under what conditions the true root cause is the only variable adjacent to $F$, as stated in Lemma 5.3. The paper does not provide a clear theoretical justification for why the proposed algorithm would converge to the true root cause, especially in cases with multiple potential causes or complex causal structures.

3. Some technical details are either missing or provided in the appendix; including them in the main text would improve the presentation. For example, Lemma 5.3 relies on the possible parent set $PossPa(X)$, which is defined in Definition A.4 without explanation. Further, it appears that not all actual parents are possible parents (see Q1 below), which may lead to incorrect theoretical results. The definition of possible parents is crucial for the theoretical results, and its lack of clarity in the main text makes it difficult to assess the validity of the claims. The reliance on appendix material for core definitions hinders the readability and accessibility of the paper.

### Questions
1. Consider a causal model with three variables $(X_1, X_2, X_3)$ with edges $X_1 \to X_2 \to X_3$ and $X_1 \to X_3$. Following the definition of possible parent in Definition A.4, $X_2$, which is an actual parent of $X_3$, is not a possible parent of $X_3$. Is this correct?

2. Given that the output of Algorithm 2 is a partially oriented DAG, is the definition of possible parent set the same as in Definition A.4?

3. Should the faithfulness assumptions be defined on the augmented graph?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Using causal analysis, the authors provide and review methods to determine the root cause(s) of failure for up to 100 nodes.

### Strengths
An attempt is made here to give an algorithm for root cause analysis that considers some of the literature. Preliminary results are promising.

### Weaknesses
This paper needs more work. There are claims throughout that seem like they're not quite thought through. I will list a few, but generally, the paper needs to focus more on comparing the best available methods in the literature and be rewritten with this in mind. That requires a bit more work than was taken up here.

For example, the reference to Chickering 2004 as evidence that causal search algorithms are slow is a bit forced since there are implementations of Chickering 2002 that are quite fast (e.g., FGES). The Lam et al. 2022 paper referenced is pretty slow for 100 nodes, but a follow-up paper to this in Neurips 2023 is quite fast for 100 nodes and scales to 1000 nodes with near-perfect accuracy. Also, whether a causal search algorithm is slow largely depends on the model class. For the linear Gaussian or multinomial cases, algorithms can be quite fast, but general distributions can become very slow, as general tests or scores need to be employed. The speed and accuracy also depend on the density of the graph. FGES (above) is very accurate for sparse graphs (sparsity = 1 - avg degree / # nodes, so for 100 nodes, average degree 4 might be considered sparse). But for dense graphs, its accuracy falls off quickly. PC (and derivatives) tend to have decent adjacency precision, but adjacency recall can be low, and orientation accuracy can be low. The devil is in the details. So those comments were a little too hand-wavy. For the version of PC you're using, you need to cite accuracy statistics not just for adjacency but also for orientation, as you are making claims about whether ancestral paths exist. This is completely missing from the draft.

As a general strategy, one should compare one's novel methods to _the best-performing alternative methods in the literature_, not just a few chosen methods one has on hand. As for the methods compared, these don't seem like the best methods that could be devised in the literature, so more work needs to be done to find what those methods might be (or devise them) and compare them. The PC version you're using should be compared to other plausible alternatives, such as the one mentioned above, or to the R method, BIDAG, which is also quite good. Again, for timing results, just give the _actual timing results_ for the various methods and let the reader decide. If the C-PC method turns out to be the winner, this should be evident from one's figures.

In addition, there are more papers on root cause analysis than are given in the literature review; this could well be expanded.

Some minor comments.

1. The definition of Markov given is for DAGs in particular, not for arbitrary graphs. It doesn't even work for what you're calling "essential graphs."

2. There is a little confusion about soft intervention. If you do a "soft intervention" on a variable X, X can still have parents. The case where it cannot have parents is where you have a "hard intervention," in which case you replace its distribution with a parent-free distribution of your choice. This is a terminological problem that can be fixed.

There is a little confusion between the lemmas given on p. 4 and the algorithms later in the paper. On p. 4, you claim that "The following two lemmas use the fact that there is only one single root cause," leading me to think that you are only considering the case where there is a single root cause of failure in the system. It's a strong assumption, but fair enough. But later, in the algorithms, you say you list the top l root causes. I could not discern any transition between these two ideas.

Typos p. 5 "Algorithm the only" ==> "Algorithm that only"; "C avid" ==> "C to an avid"

You say proofs are to be left to the avid reader, but for a paper for ICML, you should supply the proofs of your claims.

In Algorithm 2, circle endpoints suddenly appear out of nowhere. What are these? Are you dealing with PAGs here?

### Questions
Would you be able to try various other methods besides C-PC for the essential graph search, trying to find the best performers in the literature?

Would you be able to go through the literature more thoroughly and give a more substantive literature review?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an approach for identifying the root cause in a system where we observe anomalies. For this, the authors propose to utilize data from the normal operating regime to infer a (partial) causal graph. The graphical information is then used to reduce the number of independence tests to identify the root cause node based on the assumption of a shift in the underlying data generating mechanism. The approach has been evaluated using artificial and real-world data.

### Strengths
+ Insightful analysis and fair discussion of causal discovery in a large-scale setting
+ Good introduction to the problem
+ Extensive additional information in appendix for certain details

### Weaknesses
 - While the related work section has a fair discussion about different works, it also lacks work involving the direct use of graph structure (see Questions section for more details).
- The proposed method certainly has its novelty, but it seems rather limited as it boils down to the idea of first reconstructing the causal graph using causal discovery and by this, naturally, reducing the search space when running independence tests. The arguments for papers that address the problem without graph knowledge explicitly avoid a causal discovery step.
- Some definitions (like SCMs) are introduced but then not really needed. A shift in the mechanisms can be defined without this.
- The formulation of some of the definitions could be improved (e.g., when introducing a causal graph). However, these are minor issues that could be easily fixed in a revision.
- Some assumptions are not clearly stated and implied. For instance, the assumption that there can only be one root cause.
- The core novelty of the approach is not clearly articulated. While reducing the search space via a causal graph is beneficial, this benefit is also shared by other graph-based RCA methods, and the paper does not clearly differentiate itself from these approaches in a theoretical sense. The paper needs to more clearly articulate the specific theoretical advantages of the proposed approach over existing causal graph-based RCA methods, particularly in scenarios where the causal graph is known beforehand.

### Questions
The work certainly has some novel and great insights. However, I am concerned about the (more high-level) novelty here. The related work that identifies the node with a mechanism shift without assuming a graph naturally needs to run this on a potentially exponential number of combinations. Their main claim is also about not needing the graph structure, as this is an obvious way to reduce the required number of independence tests one needs to perform. Running causal discovery on the normal operation period of a system is a logical first step if a method requires a causal graph or, as in your case, to reduce the search space. In that sense, I am concerned about the novelty claim that one needs fewer tests if the graph is given, as this is obvious. I might be missing a crucial part here in the, admittedly, over-simplification of the idea and hope the authors can comment on this.

Some further remarks:
- The related work focuses on certain types of work in the domain of root cause analysis but lacks discussion about other types of work that utilize a causal graph directly, such as:

"Identifying patient-specific root causes with the heteroscedastic noise model" by Strobl et al.  
"Causal structure-based root cause analysis of outliers" by Budhathoki et al.  
"Counterfactual formulation of patient-specific root causes of disease" by Strobl et al.  
"Root Cause Analysis of Outliers with Missing Structural Knowledge" by Okati et al.  

- The difference between the complexities mentioned on lines 101 and 103 is not clear, and further clarification would be helpful.
- In Definition 2.1, the formal definition of the graph is lacking, which you then later use in Assumption 2.3. You could move this to Definition 2.1 already.
- The notation Z(X, Y ∉ Z) in line 130 is confusing; can you clarify this?
- As mentioned before, the need to introduce SCMs is unclear as a mechanism shift can also be purely introduced using the Bayesian network formulation.
- A clear assumption statement that you assume a single root cause is lacking.
- The faithfulness assumption is important for causal discovery via CIs, but that connection could be emphasized more clearly.
- Applying causal discovery on the 'normal operation' period alone implies the assumption that the causal structure has changed in the anomalous regime. While this is a valid assumption, it is also only made implicitly. In a general setting, anomalous data can even be particularly helpful in identifying cause-effect relationships.
- The introduction of the notation for having multiple metrics for a node over time does not seem to be used afterward. While I am not very familiar with the C-PC algorithm, it is unclear how one would perform causal discovery in such a setting with high-dimensional nodes and temporal dependencies without employing more time-based causal discovery approaches. Does the data you used in the experiments reflect such data?
- A drawback of your approach that lacks further discussion is the requirement of a "sufficiently" large sample size of the anomalous population. Since you argue that the root cause needs to be identified in a timely manner, this would only work in a system that produces a lot of data. If, for example, the system only produces a metric observation every few minutes, you would not have enough samples. This aspect could be discussed further as the works mentioned in the first point would work on single observations.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This research links root cause analysis in network failures to Interactive Graph Search (IGS), establishing a mathematical lower bound for the number of tests needed. With a fully known causal graph, the authors then propose an optimal algorithm that achieves this bound. With a partially known causal graph, they can identify the root-cause with linear number of invariance tests.

### Strengths
1. The motivation of this work makes sense. I totally agree that RCA is time-sensitive only after the failure occurs. We can use the time before a failure to learn the causal graph which can help us to reduce the number of tests of conditional independence in the period of RCA.

2. The authors provide extensive experimental results and detailed discussion. In particular, I very appreciate Appendix I.

### Weaknesses
1. This work relies heavily on previous works. First and foremost, it borrows the idea of modeling a failure as an intervention and transforming RCA into a problem of finding adjacency of the F-NODE from (Ikram et al., 2022). Also, it directly uses the theoretical results in (Shangqi et al., 2023) and C-PC in (Lee et al., 2024). More specifically, (Ikram et al., 2022) has already linked RCA to causal discovery and most causal discovery techniques used in this paper are also proposed by previous works. In my opinion, the major contribution in causal discovery of this paper lies in Lemma 4.1, 4.2, and 5.2. Considering that the authors list "causal discovery" as the first keyword, I think their contribution in this aspect is limited.

2. The organization of this paper should be improved. The discussion on related works is spread across many sections. The authors can use a dedicated section to introduce existing techniques used in this paper and the detailed differences between this work and previous works, rather than giving too many details in Sec. 1, 4, 5, which makes it harder for readers to grasp their contributions. Besides, I strongly suggest the authors move Appendix I to the main text.

3. Some minor concerns are detailed in Questions.

### Questions
1. The authors claim that RCD performs an exponentially large number of CI tests, but I'm not sure this is correct for Hierarchical Learning in (Ikram et al., 2022).

2. Lemma 4.1 and 4.2 are both based on the fact there is only one single root cause, but it is possible that there are multiple root causes in real-world scenarios, limiting applicability of this work.

3. There is too much space between references in page 14.

### Soundness
2

### Presentation
2

### Contribution
2
