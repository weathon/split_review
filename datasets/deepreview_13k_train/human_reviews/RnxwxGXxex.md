# CLDyB: Towards Dynamic Benchmarking for Continual Learning with Pre-trained Models

- Decision: Accept
- Scores: 5, 6, 6

## Abstract
The emergence of the foundation model era has sparked immense research interest in utilizing pre-trained representations for continual learning~(CL), yielding a series of strong CL methods with outstanding performance on standard evaluation benchmarks. Nonetheless, there are growing concerns regarding potential data contamination within the massive pre-training datasets. Furthermore, the static nature of standard evaluation benchmarks tends to oversimplify the complexities encountered in real-world CL scenarios, putting CL methods at risk of overfitting to these benchmarks while still lacking robustness needed for more demanding real-world applications. To solve these problems, this paper proposes a general framework to evaluate methods for Continual Learning on Dynamic Benchmarks (CLDyB). CLDyB continuously identifies inherently challenging tasks for the specified CL methods and evolving backbones, and dynamically determines the sequential order of tasks at each time step in CL using a tree-search algorithm, guided by an overarching goal to generate highly challenging task sequences for evaluation. To highlight the significance of dynamic evaluation on the CLDyB, we first simultaneously evaluate multiple state-of-the-art CL methods under CLDyB, resulting in a set of commonly challenging task sequences where existing CL methods tend to underperform. We intend to publicly release these task sequences for the CL community to facilitate the training and evaluation of more robust CL algorithms. Additionally, we perform individual evaluations of the CL methods under CLDyB, yielding informative evaluation results that reveal the specific strengths and weaknesses of each method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper evaluates the existing CL approaches based on pre-trained foundation models over dynamic benchmarks, raising an important question of whether the existing methods benefit from data contamination, thereby resulting in higher overall continual learning performances, thus inducing less forgetting in the network over the sequential learning tasks.

### Strengths
1. The paper is well written and the problem setup is mostly clear.
2. This paper raises an interesting question involving the evaluation strategy of the recently proposed continual learning approaches exploiting pre-trained foundation models to mitigate catastrophic forgetting in the network while learning from sequentially arriving data.

### Weaknesses
While I find the paper interesting, questioning the existing evaluation strategy and raising a possibility that the recently proposed continual learning approaches involving pre-trained foundation models may benefit from data contamination, thereby suffering less from catastrophic forgetting over sequential learning, I have a few concerns about this paper.

1. This paper considers that the foundation models are pre-trained on large-scale datasets, like ImageNet-1k or ImageNet-21k, thereby, considers creating a dynamic benchmark with various datasets ranging across various types. However, the authors failed to consider that there are other large-scale datasets, such as JFT-300M, which might be the superset of the datasets considered by the authors in this paper, thereby raising a crucial question of what would happen in such a case. Furthermore, it is very much possible to train a foundation model with no supervision by scraping all images from the internet, thereby pre-training with a superset of these considered datasets, which raises the same question.

2. This paper does not consider online continual learning setup [1], which I believe is a crucial variant of continual learning research. However, I believe this paper cannot handle such a scenario.

### Questions
Please refer to weaknesses section.

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
This paper proposes a “dynamic” framework for evaluating continual learning algorithms in a way that addresses two issues: i) the potential data contamination inherent in the methodology of using pretrained models as a starting point for continual learning, and ii) lack of realism in prior benchmarks due to their static nature. 

Specifically, the proposed benchmark is dynamic in that it forms sequences of tasks using M CL algorithms. These algorithms are used to determine 1) the most challenging tasks, and 2) the most challenging ordering of them. For the former, the authors use a Markov Random Field construction with pairwise potentials encoding the similarity between pairs of classes (using their prototypes in embedding space). They employ a greedy algorithm for picking K classes that are most similar (higher pairwise potentials), starting with a randomly-chosen class, to ensure enough diversity. They then perform additional clustering and sample uniformly from clusters, to ensure enough diversity in the set of K-way classification problems that are chosen. Then, for picking the hardest sequence, they formulate an online sequential decision-making problem where the reward is defined based on a notion of difficulty (increased forgetting and decreased task accuracy). They solve the problem using Monte-Carlo Tree Search (MCTS). To mitigate the expensive nature of MCTS (due to the rollouts, which in this case require training models on different sequences of tasks), they use a look-ahead variation that is more compute-efficient at the expense of an approximation bias.

They propose two modes of using their dynamic benchmark: the first finds task sequences that are “commonly challenging” for a pool of considered CL algorithms / backbones, while the second finds task sequences that are individually challenging for a given CL algorithm / backbone. They perform several analyses with different CL algorithms on different task sequences.

### Strengths
- The paper is for the most part well written and easy to follow (see some exceptions in Weaknesses and Questions below)

- The proposed benchmark is well motivated and well-thought out (though see some questions below regarding some exceptions) and seems like a useful contribution to the CL community.

- Empirically, the authors show that the proposed approach for finding “generally challenging” sequences leads to task sequences that are challenging for “held out” CL methods too (that weren’t used during the sequence selection), making it a meaningful benchmark for measuring progress of new algorithms. 

- On the other hand, the sequences generated by the benchmark individually for different CL algorithms can lead to an understanding of that algorithm’s limitations, and capture similarities between different CL algorithms in terms of their failure modes, which is very interesting.

- Several interesting and thorough analyses are considered, including the ability to expand the benchmark using generated data, and ablation studies of various components.

### Weaknesses
 - Some clarity issues. For example, under Equation 2, certain symbols (e.g. the set of algorithms and models A, and F) are defined that aren’t used in Equations 1 and 2, but become relevant later and it’s not clear how they are integrated into the quantities AFM and ALA – is there an average missing?

- Related to the above, in Section 4.1, the authors discuss the metrics used for evaluation and mention AA, AR and ALA, but not AFM. Why are there different metrics considered here now? Why is AFM excluded from evaluation? 

- Another important clarity issue regarding the experimental setup: the authors mention CL algorithms and backbones, and for the former, discuss that they were selected to ensure high performance and sufficient diversity / coverage. But how were the backbone selected? Are all CL algorithms applied on the same pretrained backbone, or are there different pretrained models and architectures considered? This feels like a very important aspect that is not discussed.

- When defining intra-class difficulty, it’s not clear that the proposed operationalization of “difficulty” corresponds with the issue of data contamination, which the authors use as motivation for choosing difficult tasks. Instead, the chosen approach seems to correspond to capturing difficulty as the difficulty to discriminate between pairs of classes based on their embedding-space prototypes, which isn’t *directly* related to having seen those classes at pretraining time (it is to some extent of course since what is seen at pretraining time influences the embedding function). It would be great to add some discussion about this. An alternative approach would be to independently choose the K “hardest” classes, rather than picking based on pairwise relationships (this might be seen as more directly capturing potential data contamination). This could be done e.g. by picking the classes whose examples are predicted with the smallest possible confidence in a classification task containing all classes. Have the authors considered such alternative approaches?

- Regarding the results and experimental setup in Table 1, can’t one claim that “Heldout” isn’t truly held-out due to potential data contamination issues that the authors have pointed out elsewhere in the paper? Has care been taken to alleviate this concern here? If not, can these results regarding the correlation of performance between Heldout and other benchmarks be confounded by potential data contamination?

- In the caption of Figure 1, the authors claim that the figure shows the insufficient sensitivity to performance differences, but I don’t see how this argument can be made without knowing whether the evaluated methods do in fact perform differently. If we knew that, we could say it’s a limitation of the benchmark for not capturing this. But if we don’t know that, we can’t rule out that these methods are actually indistinguishable from one another in terms of their performance. Could you comment on this?

- Insufficient discussion / description of the chosen CL algorithms (and families of CL algorithms in general). It is hard to follow the discussion of e.g. the trade-offs of different algorithms (based on Fig 4) without any description of those algorithms. Consider swapping the order of section to have Related Work appear before the experiments to address this.

- Insufficient discussion of other benchmarks. While the authors describe some in the related work, they don’t discuss what blind spots of those benchmarks (that are also dynamic), the proposed benchmark addresses. Further, in analyses like the one in Table 1, it would have been great to compare against such dynamic benchmarks rather than static ones like CIFAR-100 and ImageNet-R.

- Related work: it would be great to also discuss Nevis’22 (see References below) which also is motivated by building a more realistic benchmark for continual learning.

- Relationship to related work: are the trade-offs observed in Figure 4 between different families of methods novel? Have prior work pointed out similar trade-offs? What are the new findings here?

- In Equation 4, why are these objectives chosen in particular, and why with that particular weighting? 


Minor:

“While continue learning approaches” → “While continual learning approaches” (line 062)

### Questions
- The authors argue (at the start of Section 3.1) that when there is data contamination in the context of a pretrained model, the resulting high performance on CL tasks does not provide a meaningful comparison between CL algorithms. Why is this the case? I agree of course that if there is data contamination, this may lead to overall inflated performance (compared to had there not been data contamination), but why are the relative differences between the performance of different CL algorithms not meaningful?

- There seems to be a hypothesis that “hardest” task sequences are more realistic. But this isn’t always in the case: many practical sequences of interest may not be adversarially difficult. And it might not be the case that the relative ranking between CL methods at the “hardest” sequences is the same as that for average-case / realistically-occurring sequences. Is there some empirical evidence that hardest tasks align best with realistic scenarios (in terms of relative ranking of CL methods)? It may make sense to offer different levels of difficulty (e.g. easy, medium and hard), and observe how the relative rankings of CL methods vary across these?

- How compute intensive is it, overall, to find the hardest tasks and hardest sequence? Is the computational cost required a function of M? What are the relevant trade-offs to consider?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper benchmarks different approaches in CL. The main contribution of this work is the use of optimization and tree search to come up with more challenging tasks.

### Strengths
Dynamic benchmarking seems like a novel idea. 
The evaluation methodology is scalable
The metrics make sense
A well written paper
The graphics are very nice.

### Weaknesses
Why do we talk about benchmarking pre-trained models on CiFAR100, not even a CL dataset, nor an LLM dataset.

The training can only work with Pre-trained models, no starting from scratch.

The difficulty of choosing tasks is based on  some clustering approach, I would have thought that using some directional gradient to pick a task that pushes the cost in a particular direction to be much more reasonable for selecting the new tasks. .

How does the approach ensure that the CL methods is not biased by the choice of the training sample. If uniform random is being used, I would understand it, however, in this case, there seems to be some form of search and it is easy to derail this search.

The metric is confusing, a smaller average accuracy seems to be the best choice, why? should it not be the other way round.

### Questions
How does the approach ensure that the CL methods is not biased by the choice of the training sample. If uniform random is being used, I would understand it, however, in this case, there seems to be some form of search and it is easy to derail this search.

The metric is confusing, a smaller average accuracy seems to be the best choice, why? should it not be the other way round.

### Soundness
3

### Presentation
3

### Contribution
3
