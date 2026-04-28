# Beyond Squared Error: Exploring Loss Design for Enhanced Training of Generative Flow Networks

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
Generative Flow Networks (GFlowNets) are a novel class of generative models designed to sample from unnormalized distributions and have found applications in various important tasks, attracting great research interest in their training algorithms. 
In general, GFlowNets are trained by fitting the forward flow to the backward flow on sampled training objects. 
Prior work focused on the choice of training objects, parameterizations, sampling and resampling strategies, and backward policies, 
aiming to enhance credit assignment, exploration, or exploitation of the training process. 
However, the choice of regression loss, which can highly influence the exploration and exploitation behavior of the under-training policy, has been overlooked. 
Due to the lack of theoretical understanding for choosing an appropriate regression loss, most existing algorithms train the flow network by minimizing the squared error of the forward and backward flows in log-space, i.e., using the quadratic regression loss.
In this work, we rigorously prove that distinct regression losses correspond to specific divergence measures, enabling us to design and analyze regression losses according to the desired properties of the corresponding divergence measures.
Specifically, we examine two key properties: zero-forcing and zero-avoiding, where the former promotes exploitation and higher rewards, and the latter encourages exploration and enhances diversity.
Based on our theoretical framework, we propose three novel regression losses, namely, Shifted-Cosh, Linex(1/2), and Linex(1). We evaluate them across three benchmarks: hyper-grid, bit-sequence generation, and molecule generation.
Our proposed losses are compatible with most existing training algorithms, and significantly improve the performances of the algorithms concerning convergence speed, sample diversity, and robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel framework for GFlowNet objective functions, unifying existing training algorithms and clarifying key components. By establishing a connection between objective functions and divergence measures, it offers valuable insights into designing effective training objectives. The authors investigate key regression properties—zero-forcing and zero-avoiding—and propose three new loss functions (Linex(1), Linex(1/2), and Shifted-Cosh) to balance exploration and exploitation. Extensive experiments on benchmarks, including hyper-grid, bit-sequence, and molecule generation, show that these losses outperform the common squared loss in convergence speed, diversity, quality, and robustness.

### Strengths
This paper introduces a systematic framework for designing regression losses in GFlowNet training, linking each loss to specific divergence measures for targeted properties. Resulting in three new losses—Shifted-Cosh, Linex(1/2), and Linex(1)—that enhance exploration and exploitation balance.

### Weaknesses
Broader exploration of other potential divergence-based losses would offer a more comprehensive understanding of the effects of different divergence properties on GFlowNet training. Although the novelty lies in extending GFlowNet loss functions, there are similar attempts in reinforcement learning and generative models. Although the paper derives theoretical properties of zero-forcing and zero-avoiding, it lacks direct theoretical comparison with existing GFlowNet training algorithms.

### Questions
Could the authors clarify if they’ve noticed stability shifts in higher-dimensional or complex tasks and if adjustments might bolster robustness? Additionally, what drives the choice of a limited set of losses—are there theoretical or practical reasons for omitting other f-divergences, like Hellinger? Lastly, insights into each loss function’s hyperparameter sensitivity and effects on convergence guarantees would further clarify their resilience and adaptability.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel theoretical finding for GFlowNets regarding their objective function. Using f-divergence theories, they connect existing objectives of GFlowNets and show that they are special cases of the squared loss. They design a new loss structure that combines both properties together: (1) zero forcing (as considered in existing losses) and (2) zero avoiding, which compensates for exploration. Their new loss function seems to have empirical benefits.

### Strengths
1. The paper is well-written and easy to follow.


2. The theories are insightful.

### Weaknesses
1. The empirical results seem to be weak; they are only varied in synthetic tasks

### Questions
Areas for improvement and suggestions:

1. Making a literature connection with f-GAN, which also uses f-divergence in GANs, might be insightful to readers.


2. Include a discussion connecting with off-policy exploration methods. Are your loss and off-policy search orthogonal? Which means, is your loss function combined with an off-policy method (e.g., local search) better than the TB loss combined with an off-policy method?


3. It's good to see the categorization of prior GFlowNet works. Can you include this recent work [1] that uses genetic search as an off-policy method for training GFlowNets and provide some discussion?



[1] Hyeonah Kim et al., "Genetic-guided GFlowNets for Sample Efficient Molecular Optimization," NeurIPS 2024.

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
3

### Summary
The authors propose to modify the loss function of Gflownet (which has been completely overlooked by prior work). They show that dinstinct losses lead to different divergences. They propose three new loss functions, evaluate them extensively on diverse benchmarks.

### Strengths
Contributions:
- generalizing the objective function of gflownet
- derive impact of loss function on the gradient
- define zero-forcing (encourage epxloitation) and zero-avoiding (encourage exploration) as two key properties induced by certain loss functions
- They create 3 new losses (alonside the existing quadratic loss) to tackle all 4 possible combinations (with/without zero-avoiding, with/without zero-forcing)
- Linex(1) corresponds to the KL divergence
- experiments on 3 datasets
	- Non-zero-forcing losses (Linex(1) and Linex(0.5)) converge faster on hyper-grid
	- Linex(1) obtains all the modes almost always the fastest, but spearman corr between train and test is highest for shifted-cos on bit-sequence
	- Linex(1) tends increase diversity while quadratic and shifted-cos give higher quality (high average rewards) on molecule generation

Paper is well written.

### Weaknesses
 - it would be nice to have a few more choices of losses, taking inspiration let say from f-divergences (Reverse-KL, JSD, etc.)
- there may be more than just zero-forcing and zero-avoiding to the key properties of loss functions hence why studying more losses would be helpful
- it would be nice to let say consider hybrid methods with some kind of annealing. For example, why not use Linex(1) for its fast convergence to a large number of nodes, before then transitioning to shifted-cos for higher rewards around those now-discovered modes.

So to me, the paper is great, but its kind of stopping too quickly, it feels like its only just tapping the surface. These kinds of ideas would be easy to test out and add to the papers. 

If the authors add bit more meat to the paper, i.e. extra loss functions and hybrid-annealing (as discussed above), I would likely increase my score. Like I said, its just missing a little bit of filling to make it a great paper.

### Questions
See Weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3
