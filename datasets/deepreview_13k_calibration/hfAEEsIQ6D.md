# Perceptual Metrics for Video Game Playstyle Similarity and Diversity

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5

## Abstract
In gaming, decision-making diversity reflects the broad spectrum of styles that players can adopt. Despite the importance of this diversity, finding a universally applicable metric for it is challenging. To address this, a previous approach introduced the $\textit{Playstyle Distance}$—a method for gauging similarity between datasets using game screens and their corresponding action pairs. This method identifies comparable states in discrete representations and then computes action distribution distances. Building on it, we introduce several new techniques. These include multiscale analysis with varied state granularity, perceptual kernels rooted in psychology, and the utilization of the intersection over union method for efficient data assessment. These innovations advance playstyle measurement and offer insights into human cognition of similarity. In experiments across two racing games and seven Atari games, our metric achieves over 90\% accuracy in playstyle classification. Remarkably, this requires fewer than 512 observation-action pairs, less than half an episode in all tested games. We also develop an algorithm for assessing decision-making diversity using this metric. Our findings illuminate promising avenues for real-time game analysis and the evolution of AI with diverse playstyles.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of discerning similarities among datasets containing state/action pairs derived from video games. This aids in pinpointing distinct playstyles and understanding the diversity of human behaviors within these games. The work enhances existing methods, particularly the Playstyle Distance technique, by modifying this approach. This traditional method involves an initial discretization of the state space, followed by a comparison of action distributions based on these discrete states using a wasserstein distance. The authors propose three advancements. Firstly, they introduce multiscale states, a refined discretization technique that uses a combination of mappings rather than just one. Secondly, they use the Bhattacharyya distance as an alternative to the Wasserstein distance, arguing that the former aligns more with human perception. Lastly, the authors use the Jaccard index to weight the distance when comparing conditional action distributions across intersecting states in both reference and analyzed datasets, ensuring a more accurate assessment of the intersection's significance. The researchers conducted experiments on three distinct games: two racing games and a collection of Atari games. When compared with various versions of the Playstyle Distance, their proposed methodology appears more proficient. It more effectively captures similarities, leading to a more accurate identification of players.

### Strengths
The proposed variations over existing approaches sound interesting and grounded on human cognition. By building upon the foundations laid out by prior research, this paper takes strides in refining and enhancing what has been previously suggested in the domain. It is a simple approach that performs well on the described datasets and that extends the possible playstyle identification set of methods.

### Weaknesses
I find it challenging to grasp the exact task the authors aim to address, even though I recognize it's based on prior work. The paper's objective seems to be playstyle identification based on a few gameplay samples by comparing them with reference datasets,, but the experiments are more about player identification. While understanding the need for reference datasets for different playstyles, the creation and existence of these references remain ambiguous. A discussion on this would be beneficial.
Moreover, the assumption is that the more the distributions of actions are different, the further the playstyles are. But is it really waht defines playstyle? What about identifying playstyles that are only different in very few states (for instance, two chess players that are using two different openings). Since the definition of palystyle provided here is not grounded on any concrete application, it is difficult to understand the relevance of the work.

Second, the approach hinges on discretizing the state space. While states are assumed to be continuous and actions discrete, how would this apply when actions are also continuous, as seen in many games? The method's efficacy seems tied to the state discretization's capability to reflect genuine state distances. This might work for pixel-based games, but what about more structured observations, like chess? The multiscale approach's specifics, including the number of mapping functions and their selection, are unclear, yet these details likely influence the outcome significantly.

Last, the approach is an unsupervised method and is evaluated on very few use-cases. It makes it difficult to understand if the proposed approach is good 'in general' or if the choices made by the authors have been 'over-fitted' on the three single use cases they propose. The paper lacks a real dataset captured from real video games, with complex states, actions, and many more players than what is in the article. 

If the contribution sounds right and improves over existing publications, the validation does not allow us to conclude if the approach is really good for identifying playstyles or not. The article lacks a clear definition of what a playstyle is, and why identifying playstyles is interesting. While the subject may appeal to a niche audience, particularly those in the video game research community  (e.g Cog conference), it might not meet the broader criteria for acceptance at ICLR

### Questions
* What are the real use-cases that the identification of playstyle is targeting? Why is it an unsupervised problem and not a supervised one ? How the playstyle references dataset are built and is it realistic?
* What is the effect of the state discretization technique that is used ? How do you tune the multiscale approach ? Since you are only using few datasets, the way you tune it may be overfitting the datasets, isn't it ?
* How do you deal with continuous actions since your work focuses on discrete action spaces?

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a novel playstyle similarity metric, based on several extensions to the work of Lin et al. (2021). These modifications entail a multiscale metric, an exponential scaling, justified by psychophysics research and a probabilistic interpretation of the Jaccard index. The resulting variants are evaluated on two racing games and 7 Atari games, in a playstyle classification scenario.

### Strengths
The paper is well structured, explaining each modification in turn. Each modification is reasoned for and realized using proven concepts. The range of evaluation domains is diverse and all modifications are evaluated independently, showing that each is contributing to the whole.

### Weaknesses
Several statements are not clear to the reviewer or hard to parse:
- It is worth noting that Lin et al. (2021) were able to distinguish intersection states even with unprocessed screen pixels in Atari games. - Seems to state "In two different datasets, Lin et al. (2021) did find pixel-identical screens"? This is unclear, as it's not obvious how pixel-identical screens would arise in different game trajectories, especially given the stochastic nature of many games. The statement needs further clarification regarding the conditions under which such identical states were observed.
-  In a different scenario, when treating each state as equivalent, we can invariably pinpoint an intersection state. - Relates to identical, not just equivalent? The distinction between 'equivalent' and 'identical' states is crucial here, and the statement needs to be more precise about what constitutes an 'intersection state' when states are treated as equivalent. Does this mean that any two states are considered intersecting, or only those that map to the same discrete representation?
- Unclear what exactly is new in Sec. 3.1 and what was introduced as part of HDS (Lin et al. (2021)). The specific novel contributions of this section need to be clearly delineated from the existing HDS framework. It's not apparent what aspects of the multiscale metric are entirely new versus extensions of previous work.
- While distance is a common metric for determining similarity, a larger distance value conveys primarily that two entities are different, without giving much insight into the degree of their similarity - Why doesn't a larger distance relates to a smaller degree of similarity? The reasoning behind this statement is not clear. In most distance metrics, a larger distance directly implies less similarity. The authors need to explain why their metric behaves differently.
- Drawing from the concept of similarity, we can infer that a smaller distance provides more definitive information about the similarity - Needs to be explained. This statement is also not intuitive. A smaller distance usually implies greater similarity, but the claim that it provides 'more definitive information' needs further justification. What specific properties of the metric make smaller distances more informative?
- General wording: "intersecting states/samples" suggest a partial equivalence of a single state/sample. E.g. "intersecting set of states/samples" could be more appropriate. This is especially relevant, because the HSD model can be used to defined a intersection over (single) states (based on the hierarchy), and therefore the concepts are not clearly distinguishable. The terminology needs to be more precise to avoid confusion, especially given the hierarchical nature of the HSD model. The current wording implies a partial overlap within a single state, which is not the intended meaning.
- Sec 4.2.: "Space size" seems not to be introduced - probably number of discrete states? The term 'space size' is ambiguous and needs to be clearly defined. It's unclear whether it refers to the number of discrete states, the dimensionality of the state space, or some other measure.
- To evaluate the efficacy of the proposed multiscale state space and to compare it fairly with Playstyle Distance, we primarily focus on the TORCS and RGSK platforms - Needs to be explained. The rationale for focusing on these specific platforms for this particular evaluation needs to be clarified. Why are these platforms more suitable for evaluating the multiscale state space compared to others?
- In this section, we perform a comprehensive evaluation of various metrics, including leveraging full data with union operations. - Seems to state, that state samples from all games are used as a single set? It's unclear how the 'union operations' are performed and whether this involves combining state samples from different games into a single dataset. This needs to be explicitly stated.

Besides these clarity issues, the experimental Section could use some improvements:
- This is based on the assumption that variations in game content can be interpreted as different states - This statement was not empirically evaluated? The assumption that variations in game content correspond to different states needs empirical validation. It's not clear if this assumption holds true in all cases.
- The "game-merging" study in Sec 5.3. is an interesting piece of additional information, but the per-game results are potentially more relevant. The results should be added to the main paper and in case of space constraints, one may think about rank metrics or a table with just the most interesting dataset sizes. The lack of per-game results limits the insights gained from the game-merging study. Including these results would provide a more detailed analysis.
- Why was Playstyle Similarity not evaluated in Sec. 5.2? The absence of Playstyle Similarity evaluation in Section 5.2 is not justified. It's unclear why this metric was excluded from this particular analysis.
- Most importantly, additional comparison baselines from related work should be added. E.g. clustering or supervised methods should be applicable. The lack of comparison with existing methods limits the evaluation of the proposed metric. Including baselines from clustering or supervised learning would provide a more comprehensive analysis.
- The evaluation is only performed via classification, but a similarity metric should preserve a distance relation beyond "Top-1". Therefore, a ranking/continuous study should be performed. E.g. by creating or ordering existing playstyles along a continuous spectrum (like passive/aggressive driving) and evaluating the correlation. The evaluation should go beyond classification and include a ranking or continuous study to demonstrate the metric's ability to preserve distance relations.
- Sec 5.2 a, b has nearly indistinguishable intervals. A tabular presentation or non-linear graph scaling should be used to improve clarity. The presentation of results in Figure 3(a)(b) is not clear due to indistinguishable intervals. A tabular presentation or non-linear scaling would improve clarity.

Overall, the evaluation is still strong, but additional baselines and per-game results would greatly contribute to its value. The contribution was only deemed fair, mostly because the work does only modify an existing idea and the topic is quite niche.

### Questions
See confirmative questions above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose extensions of a previous approach, "Playstyle Distance," which attempted to quantify different playstyles by DRL agents in applications such as video game play. The authors argue why different modifications to this approach are needed for improvement, such as multi-scale state encoding and incorporating other metrics. They provide experiments showing the improvements in playstyle accuracy classification attributable to these modifications.

### Strengths
- The authors do a good job of explaining previous work.
- The authors provided code to recreate the experiments.
- The derivations in the paper seem correct.

### Weaknesses
 - The theoretical contribution is marginal, including the connection to video game play. The concept of "Playstyle Distance" itself does not seem to be specific to game play---it is a straightforward distance between policies using encoded state/action pairs [while "straightforward" is a feature (and not a bug) here, it raises the question as to why this paper needs to be framed in this language at all].
- As "Playstyle Distance" and related concepts are previous work, the additional theoretical contributions are minimal. Incorporating the Bhattacharyya distance is fine, but the connections made to human psychology are a bit flimsy. Additionally, the "Playstyle Similarity" metric is ad-hoc (which is isn't inherently bad); it's also not immediately clear to me (or at least it wasn't argued) if it's a metric, as the product of two metrics isn't a metric in general.
- Given the above points, the experimental section is not substantive enough. While the authors compare Playstyle Distance against their various improvements, they use classification accuracy to compare. However, taking a step back---this is now just a supervised learning problem. Why are any of these needed at all? If the _actual_ task is playstyle classification, then algorithms need to be compared against supervised learning approaches. The authors should at least provide some justification for why a distance-based approach is needed over a more standard supervised learning approach.
- While I appreciate the fact that code was provided, there weren't good instructions in the supplementary material zip file. Clicking the PapersWithCode link in the paper then brought me to a page that clearly has the author names and affiliations listed.

### Questions
- Is Playstyle Similarty a metric?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of defining a metric for comparing the similarity of playtraces from videogames (sequences of video frames and actions). The work improves the prior method called Playstyle Distance in three ways:
1) use of multiple encodings of states
2) use of an exponential kernel to scale the distance metric and treat it as a probability
3) use of the Jaccard index to improve assessment of overlap compared to the prior intersection

The evaluations assess each of these changes in isolation (to the degree possible), along with an overall assessment. Evaluations primarily used two datasets (one from humans, one from AI agents), with a third dataset used to evaluate the complete set of techniques. Results show the full metric improves over the prior Playstle Distance metric.

### Strengths
# originality
The paper focuses on a problem with limited prior work - developing ways to quantify similarity of playstyles. The originality of the work lies in the three improvements made to the Playstyle Distance metric. These are all reasonable incremental improvements.

# quality
Experiments vary single elements of the proposed changes to evaluate their efficacy; this provides some rigor in the evaluation of the overall method. The technical improvements are motivated by limitations of the Playstyle Distance and employ theoretically well-motivated adjustments.

# clarity
The paper articulates the insight behind each of the three core extensions to the previous algorithm and describes the changes clearly.

# significance
Playstyle metrics working from video (and action) data are valuable tools for a variety of applications including assessing "human-likeness", characterizing reinforcement learning algorithm behavior diversity, to stylometry work to model how humans play games. The paper targets a problem with wide reuse, while building on core components of a prior model.

### Weaknesses
 # originality
The original contribution is limited to extending a previous model. This is in line with the intended contribution of the paper, and remains in line with the broader objective of behavioral playstyle metrics that require little manual tuning. Thus it is not a major weakness.

# quality
The experiments are only weakly supportive of individual components of the changed method. Section 5.3 (the full model) provides the clearest results showing superiority of the new technique over prior efforts. Results in section 5.1 and 5.2 seem to show improvements for only 1 domain (of 2 tested), where the two domains are quite similar in structure (though one uses humans and one AI agents). Below are more detailed questions on the evaluation.

# clarity
No substantial issues with clarity. Only minor clarification questions (below).

# significance
The primary weakness is the technique is only compared to a single prior effort. Thus there is no sense of how this technique compares to the state of the art in performance. This makes it hard to claim the technique has major significance, beyond the clear feature that it depends on very little manual tuning (of features, heuristics, thresholds, or other parameters).

### Questions
- What other baselines could be used for comparison in these games?
	- The empirical evaluations focus on ablations of the existing metric, but do not compare against any other metrics. This makes it difficult to assess how the current approach fares compared to alternative ways of conceptualizing playstyle measurement.
- Table 1:
	- Can multiple seeds or variations of the method be run to quantify uncertainty in the performance?
	- The text claims multiscale features ("mix") are superior. Looking at RGSK this result is not clear: the $2^20$ result for t=1 is quite close to mix for t=1. For TORCS the mix results are more clearly better (modulo the lack of any estimate of uncertainty).
	- Better results on 1 of 2 cases evaluated (TORCS) is not very strong evidence for superiority of the method. Perhaps this would be stronger with evidence from Atari as well?
- Figure 3:
	- As with table 1, is it possible to add uncertainty estimates to the results presented?
	- The results on probabilistic similarity again show clear results for TORCS, but more ambiguous outcomes for RGSK. Lacking any confidence intervals, the results in RGSK look very close to one another for all methods.
	- Is it possible the dataset is the root cause of these issues? TORCS is from AI agents, which may be easier to classify in style than humans (though it's not obvious a priori why this would be true).
- Figure 4: What are the shaded areas?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
