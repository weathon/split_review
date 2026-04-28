# Climate-sensitive Urban Planning through Optimization of Tree Placements

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 6, 3, 5

## Abstract
Climate change is increasing the intensity and frequency of many extreme weather events, including heatwaves, which results in increased thermal discomfort and mortality rates. While global mitigation action is undoubtedly necessary, so is climate adaptation, e.g., through climate-sensitive urban planning. Among the most promising strategies is harnessing the benefits of urban trees in shading and cooling pedestrian-level environments. Our work investigates the challenge of optimal placement of such trees. Physical simulations can estimate the radiative and thermal impact of trees on human thermal comfort but induce high computational costs. This rules out optimization of tree placements over large areas and considering effects over longer time scales. Hence, we employ neural networks to simulate the point-wise mean radiant temperatures--a driving factor of outdoor human thermal comfort--across various time scales, spanning from daily variations to extended time scales of heatwave events and even decades. To optimize tree placements, we harness the innate local effect of trees within the iterated local search framework with tailored adaptations. We show the efficacy of our approach across a wide spectrum of study areas and time scales. We believe that our approach is a step towards empowering decision-makers, urban designers and planners to proactively and effectively assess the potential of urban trees to mitigate heat stress.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an optimization algorithm for tree placement in urban environments to reduce the impact rising temperatures. The optimization algorithm uses a combination of greedy heuristics, genetic algorithm and hill climbing to find optimized placement locations for trees. The optimization relies on accurate thermal modeling of the urban environment, which is typically a physics based simulator. The paper proposes an ML approach to approximate the simulator and speed up optimization.

### Strengths
- The paper is well presented, problem statement is clearly stated, and the results are easy to follow
- Use of real-world data
- Claims are backed by theoretical analysis and detailed experiments.

### Weaknesses
 - Lack of technical description of the algorithm. It is not clear how the hill-climbing algorithm works. Methods use domain-specific terminology that have not been adequately explained for an ML conference reader.
- Application of standard ML methods, novelty is in a narrow application area
- 500m x 500m is not a "large neighborhood". Prior state-of-the-art is not stated.
- No details on the size of the training data, separation of train-test split details is provided. 
- It is unclear how the hyper-parameters are tuned. Is there a separate held-out dataset? 
- It would be good to see a cost comparison of planting a new tree vs transferring existing tree.
- What is the correlation value between mean radiant temperature and mortality? 
- What is area covered by prior state-of-the-art in tree placement? 
- I did not understand how the aggregated performance is worse than point prediction, the absolute number is lower
- Isn't it a good thing that the temperature increases during nights and winters when the environment is colder? 
- How can you plant a big tree wherever you want in the city? Won't they need to be small and grow over time? The size of the trees considered is unrealistic. 
- How do you ensure the distribution of training data is sufficient? The optimization algorithm can potentially shift the distribution away from the training set. 
- Why is a reduction of 0.83K substantial? Please provide sufficient domain context for an average ML scientist can follow. 
- Did not understand how you got 20% reduction for 60C T_mrt. No details have been provided.

### Questions
- What is the correlation value between mean radiant temperature and mortality? 
- What is area covered by prior state-of-the-art in tree placement? 
- I did not understand how the aggregated performance is worse than point prediction, the absolute number is lower
- Isn't it a good thing that the temperature increases during nights and winters when the environment is colder? 
- How can you plant a big tree wherever you want in the city? Won't they need to be small and grow over time? The size of the trees considered is unrealistic. 
- How do you ensure the distribution of training data is sufficient? The optimization algorithm can potentially shift the distribution away from the training set. 
- Why is a reduction of 0.83K substantial? Please provide sufficient domain context for an average ML scientist can follow. 
- Did not understand how you got 20% reduction for 60C T_mrt. No details have been provided.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of optimizing the placement of trees in an urban environment such as to maximize a proxy metric of human thermal comfort. Given that this quantity is expensive to evaluate using e.g. physical simulations, the authors propose training a convolutional neural network to estimate the quantity instead. Furthermore, the estimation is performed in an aggregated fashion, which can yield substantial speed-ups while sacrificing an acceptable amount of accuracy. 

The authors pair this estimation of the objective with a heuristic local search technique comprising several components. The method is applied to the optimization of tree placements within a city, and shows improved performance over either component in isolation. Furthermore, there are interesting insights regarding the impact of tree cover on temperature as a function of time, the diminishing impact of additional trees, and the "what-if" scenario concerning the impact of an alternative, optimized placement over the one that currently exists.

### Strengths
**S1**. The work addresses a relevant, practical problem of potential societal impact. I found the analyses in 4.3 and 4.4 particularly interesting and insightful.

**S2**. The paper is very well-written, clear, and easy to follow.

### Weaknesses
 **W1**. In my opinion, the methodological contributions of the paper are thin, and essentially boil down to 1) estimating the aggregated radiant temperatures directly instead of individually and 2) integrating this estimation in a standard local search procedure. These are both fairly straightforward. The "theoretical analysis" in Section 3.1 is extremely tenuous and, in my opinion, should not be branded as such.

**W2**. The evaluation does not include error bars and confidence intervals, which are a must for drawing reliable conclusions from the results, given the stochasticity of the methods (bar greedy search which is deterministic; but given the estimation itself is learned, one could consider an experimental design where the "seed" for the estimation varies in a paired fashion).

**W3**. There is a potential fundamental limitation in the considered objective, which does not include any measure of population density, traffic, or footfall for the areas. 

- In my opinion, this is potentially problematic as the optimization procedure may find solutions where trees are placed in places that yield good deltas in the temperature metric, and yet are comparatively less (or not at all) populated. 
- Hence, the placements may trivially not lead to decreases in thermal comfort experienced by individuals, given that an area is not actually frequented by people. 
- This is potentially alluded to in the text (bottom of page 8) and acknowledged in Section 5, but I think it deserves to be addressed in more depth. 
- For example, it may be that the density is sufficiently uniform in the considered grid that this is not an issue. Evidence that the approach does not "game" the objective would also counteract this point.

### Questions
**C1**. Another means of strengthening the evaluation is to include other, more competitive baselines from the literature. Is there no such method? Given the improved scalability attained by your method, what is the point at which prior methods (e.g. that estimate the temperature in a more granular fashion) are too slow? Some more extensive benchmarking than the figures quoted in the text in 4.1 would help.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To improve urban planning and reducing temperature stress from inhabitants, a U-Net is trained to predict mean radiant temperature from various meteorological and surface inputs, including vegetation. This vegetation input is optimized with an evolutionary algorithm to reveal ideal tree positions that minimize mean radiant temperature. The model runs several orders of magnitudes faster than conventional models but produces slightly deteriorated results.

### Strengths
_Originality:_ This work does not seem to be of particular originality in terms of ML methods. Hence, the manuscript might be better suited for a journal about application of ML to environmental processes. I do like the topic of research and see its importance, though, and would like to encourage the authors to submit the work to an according journal.

_Quality:_ The manuscript is sound. Results of the experiments support the claims.

_Clarity:_ I had some difficulties in understanding what kind of data was used in this work (see questions below).

_Significance:_ Even though the results are important, they do not seem to bring new insights, nor do they seem to be of particular novelty. Replacing physical models with surrogate ML methods has been demonstrated widely to result in substantial speed-ups.

_Further comments_:
- The section about limitations is well structured and captures relevant aspects. Most concerning to me is the restriction to a single study area, which means that results cannot be expected to hold for different climatic regions. Extending the experiments to different cities would be of great value for the manuscript.

### Weaknesses
1. Unclear what data has been used. Does the CityGML data come from [this](https://www.ogc.org/standard/CityGML/) homepage and is this all simulation data, or real observations? As far as I know, ERA5 data is only available on 30m resolution; how do you get to 1m resolution? Where do your digital elevation and surface models, your land cover, wall aspects and height, and sky view factor maps come from? The lack of clarity regarding the source and preprocessing of the input data makes it difficult to assess the reproducibility and generalizability of the results. Specifically, the method for downscaling ERA5 data to 1m resolution is not described and is a crucial step that needs to be detailed. Furthermore, the origin of the high-resolution spatial data (digital elevation models, surface models, land cover, etc.) needs to be explicitly stated, as these are not standard datasets.
2. Benchmarking traditional physical model would be highly appreciated to understand the performance of your U-Net in terms of accuracy. That is, does your method incur a trade-off between accuracy and efficiency, and, in particular, how accurate is your U-Net to approximate $T_{mrt}$? The manuscript should include a more rigorous comparison of the U-Net's predictions against the ground truth (i.e., the output of the physical model) to quantify the approximation error. A simple comparison of L1 error is insufficient; a more detailed analysis, perhaps including spatial error maps and error distributions, would be beneficial. It is also not clear if the U-Net is trained on a single location or multiple locations; this needs to be clarified.
3. Is SOLVEIG a traditional model and do you benchmark this? Please help readers by clarifying this more thoroughly. What does an `L1 error of 1.93K` mean, is it computed between U-Net output and ground truth, or between U-Net output and SOLVEIG output? It is critical to explicitly state that SOLVEIG is a physical model and to provide a brief description of its workings, especially for readers who may not be familiar with it. The evaluation should clearly define what the L1 error of 1.93K represents. Is it the error between the U-Net predictions and the SOLWEIG outputs, or is it with respect to some ground truth measurements? If the latter, where do these measurements come from? If the former, it needs to be explicitly stated that the U-Net is approximating the physical model and not necessarily the real world.
5. Given that the solar incoming radiation $I_g$ has the biggest impact, how does the tree position make a difference? An ablation comparing the effect on $T_{mrt}$ caused by number of trees vs. the positioning of the trees would be interesting. Also, seing Figure 4, I do not quite agree that the number of trees saturates (although it certainly will at some point). In short: Does the number of trees or their position contribute more to a better $T_{mrt}$? (I have seen your comment `Notably, the improvement by relocation of existing trees is significantly larger than the effect of 50 added trees [...]`, but I could not quite understand the quantitative effect of each treatment, i.e., #trees vs position). The claim that tree position is more important than the number of trees needs to be substantiated with a more rigorous analysis. A proper ablation study should quantify the individual contributions of tree number and tree position, perhaps by comparing the performance of the evolutionary algorithm against a random placement of trees.

### Questions
1. In Figure 1: What does the legend show, is it difference in $T_{mrt} [K]$ compared to a no-trees condition? Where are the trees placed (maybe indicate with opaque green circles)?
2. Have you considered other tree positioning approaches, such as projecting error gradients in the U-Net's $T_{mrt}$ prediction on the positions of the trees? That is, somewhat similarly to [[1]](https://arxiv.org/abs/1904.09019), where optimal node-positioning was optimized via gradients in a GNN.
3. What type of trees have been investigated? To what kind of tree does $t_g$ used in your experiments relate?
4. Why does your algorithm suggest to populate east-to-west passages more densely? Wouldn't this prevent wind to transport hot air out of the city in summer? And following up on this, what tree positions does your algorithm predict when exclusively optimizing for winter or summer months?

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses a spatial optimization problem - how a certain number of items (in this case trees) can be distributed over a spatial grid system to optimize a particular objective (in this case Mean Radiant Temperature-MRT). For this task, they discuss a genetic algorithm based approach to identify the optimal distribution. A neural network (U-Net) is used to estimate the impact of placement of each tree on aggregate MRT. This U-Net is used to approximate a process-based model that estimates point-wise MRT based on meteorological and vegetation features. A counterfactual-based analysis is also carried out, where optimal placement of even existing trees are considered in addition to new ones.

### Strengths
1) The paper considers a novel spatial optimization problem with a very relevant application - climate-sensitive urban vegetation planning.
2) The paper develops a neural network surrogate for an existing process-based model (Solweig), this can be an useful contribution to the growing subfield of ML-based surrogates for process models

### Weaknesses
1) No technical contribution in ML. Even the considered surrogate model is a simple U-Net. It is not used for anything other than approximation of Solweig. If it gives computational benefits, this aspect is never discussed, nor is the quality of approximation evaluated
2) The optimization seems to be done one tree at a time, rather than jointly over an entire configuration. This need not be a weakness, but the approaches need to be compared
3) The problem is solved in rather artificial settings, without considering many realistic effects (as mentioned by the authors themselves, in the limitations section)
4) The proposed approach seems to be too specific to one application to be of sufficient interest to the ICLR audience in general

### Questions
1) Algorithm 1 suggests that the MRT seems to have been pre-computed for placing each tree separately. But in each iteration of the GA, the existing tree placements are partially perturbed. Do we not need to recompute the MRT once again for each perturbation?
2) Is U-Net the best model for generating the spatial maps? Have different architectures been compared? I didn't see much discussion about this
3) Several limitations have been mentioned in the paper itself. Can those be overcome within the proposed framework itself, or do they need completely different approaches?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
