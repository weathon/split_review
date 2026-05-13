# DIFUSCO-LNS: Diffusion-Guided Large Neighbourhood Search for Integer Linear Programming

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Integer Linear Programming (ILP) is a powerful and flexible framework for modeling and solving a variety of combinatorial optimization problems. This paper introduces a novel ILP solver, namely DIFUSCO-LNS, which combines the strengths of carefully engineered traditional solvers in symbolic reasoning and the generative power of a neural diffusion model in graph-based learning for the Large Neighborhood Search (LNS) approach. Our diffusion model treats the destroy policy in LNS as a generative problem in the discrete $\{0, 1\}$-vector space and is trained to imitate the high-quality Local Branching (LB) destroy heuristic through iterative denoising. Specifically, this addresses the unimodal limitation of other neural LNS solvers with its capability to capture the multimodal nature of optimal policies during variable selection.  Our evaluations span four representative MIP problems: MIS, CA, SC, and MVC. Experimental results reveal that DIFUSCO-LNS substantially surpasses prior neural LNS  solvers.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an ML-guided LNS framework for MIPs. It uses a diffusion model to guide variable selection in the destroy step of LNS. The variable selection is treated as a generative task, and is learned by imitating the Local Branching expert policy. In the experiment, the new method DIFUSCO-LNS is compared against a variety of ML-guided approaches and heuristic approaches. The presented results show that the proposed method finds better solutions at a faster speed on most benchmarks.

### Strengths
1. Applying diffusion is a novel idea and an interesting direction for LNS mip solving.

2. Experimental results show promise for the approach.

### Weaknesses
1. The results are promising on some benchmarks but overall not super impressive. Also, could you highlight the innovation in diffusion models from this paper that enables its application for LNS? 

2. It would be interesting to see the comparison prediction accuracy / per-iteration improvement to confirm that difusco-LNS is indeed making better predictions.

3. Related to the previous point, It would be good to report the ML inference time overhead during testing. My understanding is that diffusion requires a more expensive denoising process than the other ML approaches using the same architecture.

4. It seems DIFUSCO-LNS is sensitive to hyperparameters. It is not discussed how the best hyperparameters were chosen in the paper.

### Questions
1. You mentioned that you were not able to reproduce results for some baselines due to differences in hardware/compute resources. Can you elaborate more on this? For LB-RELAX there seems to be quite a huge difference. From my own experience, sometimes it is due to different software versions (like SCIP or Gurobi). The other time it might be due to hardware differences: a slower machine computes different heuristics at the BnB nodes and thus produces different results if the wall-clock time budget is fixed.

2. Difusco-LNS also takes advantage of multiple good solutions following previous work. I wonder if a contrastive learning component can be built into the diffusion model so that you can leverage bad solutions from LB?

3. I realize the green curve in Figure 4 has an increasing trend at around 500-600 seconds. What happens there?

4. From the ablation studies, it seems that DIFUSCO-LNS is sensitive to a couple of hyperparameters. I wish to understand whether you need to fine-tune them for different benchmarks.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a diffusion-based approach for learning a large neighborhood heuristic for solving integer linear programming problems (ILPs). Large neighborhood primal heuristics can be used to quickly find high-quality solutions to ILPs using commercial ILP solvers. They do so by iteratively destroying (using a destroy heuristic) and repairing (using the ILP solver) a given starting solution. In recent years, a number of machine learning approaches have been proposed that aim to learn good destroy heuristics. The proposed method builds upon earlier works (using the same model architecture, features, and data collection) but uses a diffusion-based learning scheme. The authors evaluate their approach on 4 problems and observe that it outperforms earlier approaches.

### Strengths
- The idea to use a diffusion model for learning destroy heuristics is novel. Furthermore, the use of a diffusion model is well motivated and straightforward.
- The proposed approach shows good performance and outperforms all other evaluated approaches.

### Weaknesses
- In my opinion, the paper is lacking additional ablation studies or experiments that evaluate the influence of the different hyperparameters. The authors only conduct one experiment that analyzes the effect of the number of diffusion steps. They report results for the values 5, 10, 20, 50 and find that 50 steps lead to the best results. This raises the question if the performance of the approach can be further improved by selecting an even higher number of steps. Overall, the relationship between number of diffusion step, prediction time, and prediction quality could be explored further. Fig. 4, which shows the results for the existing experiments, is also a bit difficult to read. Furthermore, the influence of other hyperparameters (e.g., destroy size) could be evaluated further.
- The novelty of the paper is very slightly limited by the fact that the authors use the same model architecture, features, data collection etc. as earlier work. The main contribution of the authors is that they replace the imitation/contrastive learning approach of earlier works with a diffusion-based approach.
- The quality of Fig. 1 and Fig. 2 could be improved. For example, by using the same font for all Figures. Both figures are also not mentioned or explained in the text. For Fig. 2 it is not clear what elements are added and why only x_1 and x_n are considered on the right hand side (and not x_2, x_3, …). 
- It is not clear based on which (near-)optimal values the primal gap is calculated. Ideally, the authors would also report the primal bound in the Appendix to make comparisons for future works easier.
- There are some minor spelling mistakes etc. (LSN instead of LNS (page 2), Arechitecture (Fig. 2), unnecessary comma at the end of the baselines paragraph. etc).

### Questions
- The approach uses a larger number of hyperparameters (often different parameters for different problems). How have these been selected?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose using a diffusion model for generating neighborhoods for use in large neighborhood search. The diffusion model is trained to imitate local branching, an oracle method that is supposed to find the best local neighborhood to search. The authors present results comparing their approach against other learning-based approaches, heuristics, and branch and bound. They demonstrate mixed results with learning approaches tending to outperform fixed heuristics.

### Strengths
The main strengths of the work are that it evaluates against several baselines, using several metrics, and in several ILP settings including generalization to larger instances. Additionally, the paper overall gives a reasonable explanation of the model architecture, data collection, and settings.

### Weaknesses
The main weakness of the work is that it seems to just be application of a diffusion model to improve LNS solving without further developing or integrating any of the ideas in diffusion or LNS to get improved performance. For instance, previous approaches generally consider directly predicting the neighborhood. However, given a generative diffusion model one might consider generating several neighborhoods, evaluating them, and selecting the best. Otherwise, you might also consider integrating optimization-based objectives in the diffusion model to guide the diffusion model towards generating better solutions. 

Additionally, while the authors do evaluate many metrics, the performance difference between the proposed approach and previous work seems to be quite small and within the uncertainty intervals. It seems unclear that the proposed approach does improve over previous work but in the case that it generally does improve just within a small margin, you might consider evaluating win rate across instances or computing an average rank across instances to understand which algorithm generally solves the problem the fastest.

The problem instances also seem to be effectively solved quite quickly with the primal gap quickly reaching below 10-3. It would help to explain what level of primal gap is reasonable for these instances to be considered solved.

### Questions
The authors should consider some rephrasing to better situate their work within the context of optimization.
Positioning of the work:
1st paragraph, last sentence
Our work … belongs to the category of approximate solvers.
It seems that this work doesn’t give approximation guarantees and also doesn’t give indication of how close to optimality a solution is so instead should be considered a primal solver.

3rd paragraph
It is unclear why the referenced LNS approaches require domain-expert knowledge. It seems that they all readily take the ILP formulation as input without much tuning (other than selecting the neighborhood size which is needed in this work as well).
In the same paragraph, it is not obvious why a data-driven approach is necessarily a better alternative as it assumes access to a distribution of problem instances and requires offline training. Here it might be helpful to give a high-level explanation of why learning-based methods should work well. 

It would be helpful to explain why local branching is something we desire to learn, does it give performance guarantees for LNS? Does it empirically work well but is just too slow?

Average rank seems to be computed using the summary statistics. However, it might be informative to include a metric measuring the average rank that averages over problem instances. This would help give an idea of whether a given algorithm was generally solving problems faster overall. 

Small errors:

2nd paragraph
Heuristics … is called … -> heuristics are called
3rd paragraph
Hand-craft destroy -> hand-crafted destroy
P3 local branching paragraph
“Can we” -> delete this, or missing rest of sentence?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
