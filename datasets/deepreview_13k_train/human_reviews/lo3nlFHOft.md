# From Promise to Practice: Realizing High-performance Decentralized Training

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Decentralized training of deep neural networks has attracted significant attention for its theoretically superior scalability over synchronous data-parallel methods like All-Reduce. However, realizing this potential in multi-node training is challenging due to the complex design space that involves communication topologies, computation patterns, and optimization algorithms. This paper identifies three key factors that can lead to speedups over All-Reduce training and constructs a runtime model to determine when, how, and to what degree decentralization can yield shorter per-iteration runtimes. Furthermore, to support the decentralized training of transformer-based models, we study a decentralized Adam algorithm that allows for overlapping communications and computations, prove its convergence, and propose an accumulation technique to mitigate the high variance caused by small local batch sizes. We deploy the proposed approach in clusters with up to 64 GPUs and demonstrate its practicality and advantages in both runtime and generalization performance under a fixed iteration budget.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates decentralized training of DNNs. This used to be a fairly hot topic a few years ago (e.g. Lian et al 2017 and follow-up work), but has to some extent cooled down recently as models and workloads have changed, and model-parallelism has become more standard. 
The paper focuses on the classic data-parallel setting; its contributions are as follows: 

- An analytical model to understand what are the conditions under which decentralized training can bring gains.

- A decentralized version of Adam, which decouples computation from communication and provides convergence guarantees under fairly standard assumptions (for Adam) 

- An implementation of the algorithm and its technical evaluation. This is done fairly thoroughly, on systems with up to 64 GPUs, showing the method’s potential.

### Strengths
Strengths:

1. new perspectives on an “old” problem by today’s standards (decentralized training), from the point of view of modeling and adaptive optimization

2. analytical results are a plus

3. the experiments are fairly thorough

### Weaknesses
Weaknesses:

1. unfortunately the paper seems to be completely missed some important related work in the area, which makes it very hard to position the paper properly in terms of its contribution

2. more broadly, the experimental results are in a system parameter range that has been rendered somewhat obsolete by current-day systems, which are able to e.g. train ImageNet in minutes on a single node https://github.com/libffcv/ffcv



### Questions
Detailed comments and questions:

Q1. The paper seems to ignore work on the decentralized setting since late 2020 to early 2021. Here are some of the many references that are missed:

- There is a lot of nice work by Anastasia Koloskova and co-authors on analyzing Gossip variants of SGD, many of which are missed:

1. Koloskova, Anastasia, et al. "A unified theory of decentralized sgd with changing topology and local updates." International Conference on Machine Learning. PMLR, 2020.

2. Koloskova, Anastasiia, Tao Lin, and Sebastian U. Stich. "An improved analysis of gradient tracking for decentralized machine learning." Advances in Neural Information Processing Systems 34 (2021): 11422-11435. 

See also:

Zhang, Jiaqi, and Keyou You. "Fully asynchronous distributed optimization with linear convergence in directed networks." arXiv preprint arXiv:1901.08215 (2019).

"SQuARM-SGD: Communication-Efficient Momentum SGD for Decentralized Optimization" by Navjot Singh et al. (2020)

In addition: 

- Nadiradze, Giorgi, et al. "Asynchronous decentralized SGD with quantized and local updates." Advances in Neural Information Processing Systems 34 (2021): 6829-6842.

This paper seems to be trying to do something similar to what is done here–decoupling communication from computation–but in some sense goes further since it also supports quantization and completely non-blocking reads. Even the experimental setup is very similar to the one presented in this paper, so I am surprised to see that there is no mention of this work whatsoever. 

- Similar work: 
 Li, Shigang, et al. "Breaking (global) barriers in parallel stochastic optimization with wait-avoiding group averaging." IEEE Transactions on Parallel and Distributed Systems 32.7 (2020): 1725-1739.

I would therefore recommend that the authors go over related work more thoroughly, and provide more complete positioning of their work relative to prior art. I don’t think the paper can be accepted in the absence of this. 

Q2: Are the loss improvements quoted in L488 (2.841 vs 2.846) actually statistically significant?

Q3: Is your setup really faster than just setting up large-batch SGD using e.g. FFCV on a single 4-GPU system?

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
This paper investigates the gap between decentralized training of DNN and data parallel (DP) methods. 
In particularly, although decentralized training is theoretically superior to DP, certain network topologies make the use of this technique challenging. 
The present propose to quantify such gap through the use of a "runtime model".
Moreover, the author introduce a decentralized version of Adam particularly suited to the training of transformer based models.
Extensive numerical experiments illustrate the speedup investigation.

### Strengths
- This paper proposes to study an important, impactful problem (practical gap between DP and decentralized training)
- the accuracy of the model (ie how it captures real time speed discrepancies) is well illustrated
- the numerical experiments are extensive and thorough. There is a clear focus on transformer based architectures, making it relevant to challenges posed by modern LLMs.
- the version of decentralized Adam optimizer is thoroughly compared to other decentralized adam based methods
- the papers lists 3 factors that could explain the aforementioned discrepancy  1) overlapping communication and computation 2) heterogeneous communications costs 3) sensitivity to varying computation times. For each factor, an extensive investigation is proposed supported by numerical experiments.

### Weaknesses
 - the explanation/details of the runtime model in Appendix A.5 could be stated more clearly 
(the reviewers would like to respectfully suggest an explanation similar in spirit to the way Algorithm 1 is stated, although this is relatively minor)
- there is no clear link to the reviewer between the decentralized adam optimizer and the runtime model (please correct me if missed anything).

### Questions
The reviewer is curious about the intuition behind the runtime model: were the assumptions behind the model proposed previously by some other work or is this coming solely from the author?

### Soundness
3

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
3

### Summary
The paper explores decentralized training of deep neural networks (DNNs) as an alternative to synchronous data-parallel methods like All-Reduce, which are known for their scalability issues. The authors identify three key factors that can lead to speedups in decentralized training: overlapping communication and computation, respecting heterogeneous communication costs, and reducing sensitivity to varying computation times. They propose a runtime model to optimize decentralized training configurations and design a decentralized variant of the Adam optimizer, called DAdam, which supports overlapping communications and computations. Additionally, they introduce an accumulation technique to mitigate the high variance caused by small local batch sizes.

### Strengths
1. The authors provide a runtime model that quantifies key environmental parameters and estimates potential speedups, offering valuable insights into the conditions under which decentralized training is advantageous.
2. There is theoretical analysis to support the proposed algorithm.
3. The experiment consists of 64 GPUs, which is a suitable scale.
4. There is detailed hyper-parameter settings for reproducibility.

### Weaknesses
1. Some important related works in MLsys [1,2] are missed, in which the dynamic gossip communication topologies are also discussed, and the communication compression is utilized.
2. The novelty of the DAdam is limited. There is no improvements on the Adam itself. The proposed method can be seen as a system optimization instead of the optimizer itself. However, the systematic optimization including the overlapping between communication and computation is largely used in many ML systems [3,4].
3. While the paper presents extensive experiments, it lacks detailed ablation studies to isolate the impact of individual components of the proposed approach. For example, it is unclear how much performance gain comes from the overlapping of communication and computation, the accumulation technique, and the decentralized Adam optimizer itself. A more granular analysis is needed to understand the contribution of each component.
4. The tested topologies are limited. The paper only considers a few specific topologies like complete and alternating-exp-ring. It is unclear how the proposed method would perform on other topologies, such as torus or expander graphs, which may exhibit different communication characteristics. The generalization of the results to different network structures is therefore limited.
5. For training GPT-2 on OpenWebText, it is unclear whether the final convergence of DAdam can match the All-Reduce Adam when training with more iterations. The convergence curves of training on OpenWebText are not provided. Without these curves, it is difficult to assess the practical effectiveness of the proposed approach for large-scale language model training.
6. There lacks enough details of how the decentralized training is implemented built upon PyTorch. Specifically, the paper does not describe how the communication is launched (e.g., using torchrun or MPIRUN), how synchronization between nodes is implemented (e.g., using distributed.barrier()), how the overlapping between communication and computation is achieved, and how the communication topology is managed. These implementation details are crucial for reproducibility and understanding the practical challenges of the proposed approach.

### Questions
Please refer to the weaknesses. 

It would be better to provide training convergence curves of using DAdam and the All-Reduce Adam on OpenWebText. 

Also, it is important to illustrate how the decentralized training is implemented, as the Pytorch and DeepSpeed have conducted many system optimizations on the All-Reduce, there should be some convincing illustrations to show that the implemented decentralized training can outperform the All-Reduce. Specifically, how the communication is launched, using torchrun or MPIRUN or something else? how the synchronization between different nodes is implemented, is there a distributed.barrier()? how the overlapping between communication and computation is implemented? How do you manage the communication topology? The source code with a document may be very helpful.

If these questions are addressed, I'd like to increase my score.

### Soundness
3

### Presentation
3

### Contribution
2
