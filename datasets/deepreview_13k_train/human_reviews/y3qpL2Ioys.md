# Towards Neural Architecture Search through Hierarchical Generative Modeling

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Neural Architecture Search (NAS) is gaining popularity in automating designing deep neural networks for various tasks. 
A typical NAS pipeline begins with a manually designed search space which is methodically explored during the process, aiding the discovery of high-performance models.
Although NAS has shown impressive results in many cases, the strong performance remains largely dependent on, among other things, the prior knowledge about good designs which is implicitly incorporated into the process by carefully designing search spaces.
In general, this dependency is undesired, as it limits the applicability of NAS to less-studied tasks and/or results in an explosion of the cost needed to obtain strong results.
In this work, our aim is to address this limitation by leaning on the recent advances in generative modelling -- we propose a method that can navigate an extremely large, general-purpose search space efficiently, by training a two-level hierarchy of generative models.
The first level focuses on micro-cell design and leverages Conditional Continuous Normalizing Flow (CCNF) and the subsequent level uses a transformer-based sequence generator to produce macro architectures for a given task and architectural constraints.
To make the process computationally feasible, we perform task-agnostic pretraining of the generative models using a metric space of graphs and their zero-cost (ZC) similarity.
We evaluate our method on typical tasks, including CIFAR-10, CIFAR-100 and ImageNet models, where we show state-of-the-art performance compared to other low-cost NAS approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed efficient hierarchical generative modelling for neural architecture search using zero-cost proxies. NAS as a field often relies strongly on well-designed search spaces. Design of such search spaces is non-trivial especially in new domains and research areas. This paper addresses this disadvantage by  exploiting an extremely large, general-purpose search space efficiently, by training a two-level
hierarchy of generative models. First level of the conditional generative process focusses on micro-cell design using conditional continuous normalizing flow and the second level uses an transformer to sequentially model the macro architecture. What makes this approach effective in these larger spaces is the ability to exploit task-agnostic zero cost proxy scores to pre-train the generative model. The method is evaluated on the cifar10, cifar100 and the imagenet1-k dataset.

### Strengths
Originality: I find the main contribution of the paper of modelling a 2-level hierarchical search space (which is very expressive) novel and interesting. Furthermore this paper effectively avoids the expensive training cost of generative nas models by relying on zero-cost proxies for pre-training

Clarity: I found the presentation clear in most parts (refer to questions for things that are unclear)

Significance: This paper in my opinion proposes an interesting way to exploit zero cost proxies to search in a large and expressive search spaces. The results in my opinion are competitive and significant

### Weaknesses
 - Given the search space design and inability to construct a supernet, fair comparison with effective nas strategies becomes challenging in this case. For example the OFA search space in table 3 is very different from the search space of GraphNet. Hence it becomes difficult to understand if the gains are attributed to search space design itself or the NAS approach. I recommend comparison with black box nas methods on exactly the GraphNet space(eg: regularized evolution [1], hierarchical nas [2])

- The method uses a pretrained GPT-Neo-125M model. Hence the actual search cost also implicitly inclues the pre-training cost of this model, which should ideally be added to the search cost computation (table 1,2,3). 

- Study is limited to convolutional spaces. It becomes natural to question the robustness of the proxies to the recent transformer baeed search spaces in NAS

- Performance on Imagenet is still dominated by methods like Once-For-All which models a simple chain structured space  in Table-3 (contrary to the more expressive space here).

- I encourage the authors to release code to foster reproducibility in NAS

### Questions
- Refer points in weaknesses

- Could the search space design and search methodology be extended to transformer spaces like AutoFormer [1] or HAT [2]?

- Could the authors ablate the choice of T-CET as a proxy in macro architecture generation across different proxy choices? How robust/sensitive is the search to different choices of (strong) zero-cost proxies?

- Could the authors ablate the gains from each of the two phases of hierarchical generative modelling? ie fixing the cell and only performing macro search and vice-versa. 

- Could the authors study insights derived from NAS method? Which architectural designs tend to be more impactful than the others?

[1] Chen, M., Peng, H., Fu, J. and Ling, H., 2021. Autoformer: Searching transformers for visual recognition. In Proceedings of the IEEE/CVF international conference on computer vision (pp. 12270-12280).

[2] Wang, H., Wu, Z., Liu, Z., Cai, H., Zhu, L., Gan, C. and Han, S., 2020. Hat: Hardware-aware transformers for efficient natural language processing. arXiv preprint arXiv:2005.14187.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies a zero-cost NAS that navigates an extremely large, general-purpose search space to produce network of good quality. The proposed schema considers micro level cell designs at first, then leverages a transformer generator to produce macro architectures for a given task and architectural constraints. Numerical experiments on CIFAR and ImageNet validate the efficacy of the method.

### Strengths
- The paper is written well and technically sound. 
- The topic of using generative model into ZC NAS is interesting.

### Weaknesses
 - The design conflicts the target pain point. The target pain point raised in the introduction is to eliminate the need of designing search space manually. However, this paper still manually designs a search space and develop an algorithm upon it, see page 4. 

 - The proposed method seems not generic and time-consuming. The proposed methods require a transformer generator to produce macro architectures which seems require time-consuming pretraining, fine-tuning, and may be task and search space specific.

### Questions
See the weakness.

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
This paper aims to reduce the dependency of NAS on the search space design to improve NAS's applicability to less-studied tasks. The core technique is a new hierarchical generative model pretrained using a metric space of graphs and their zero-cost similarity. Experiments are conducted on several standard benchmark datasets, including CIFAR and ImageNet.

### Strengths
1. This paper is well-motivated. 
2. Improving the applicability of NAS to less-studied tasks is a fundamental challenge for NAS and has large practical values.

### Weaknesses
1. The proposed method still heavily depends on human prior knowledge (e.g., reference design, zero-cost metric). I do not see any improvements in improving NAS's applicability to less studied domains. The use of cluster centers as reference points, while automated, still relies on the initial choice of clustering algorithm and its parameters, which can be considered a form of prior. Furthermore, the selection of zero-cost metrics, such as FLOPs or parameter counts, is not an objective choice but rather a design decision based on assumptions about what constitutes a good proxy for performance. This reliance on pre-defined metrics limits the method's ability to adapt to novel tasks where such proxies may not be valid.
2. The generalization of the proposed method is a big question. As far as I know, the generalization ability of zero-cost metrics is a bit limited. As the proposed method is based on zero-cost metrics, I think it is necessary to verify the proposed method's generalization ability. The performance of zero-cost proxies is known to vary significantly across different architectures and tasks. Therefore, a method that relies heavily on these proxies may not generalize well to tasks that differ significantly from those used to train the generative model. The paper lacks a thorough analysis of the sensitivity of the proposed method to the choice of zero-cost metric and the diversity of tasks.
3. The idea of using a hierarchical design to reduce the space is not novel.
4. I feel the current experiment design is not a good fit for this paper. I am more interested in seeing experiments on less studied domains instead of these standard benchmark datasets. If the author can show one practical case where their method can clearly outperform conventional NAS, this paper will be much stronger.

### Questions
Please check my comments above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose an efficient method of constructing and searching through neural architecture search spaces. Their method consists of multiple stages. In the first stage, a graph variational autoencoder is trained to produce embeddings of different architectures on the cell level. The authors add a margin loss comparing architectures using zero-cost proxies to encourage the architectures to cluster. The resulting latent space is clustered using a gaussian mixture model. 
In order to sample architectures given a well-performing reference architecture in the high dimensional latent space of the VAE, the authors employ a conditional, continuous normalizing flow model. In order to create the macro architectures, the authors propose to fine-tune a decoder-only generative transformer model on architectures found via evolutionary optimization, which uses a zero-cost proxy for its search. 
The authors demonstrate competitive performance with both aligned methods on CIFAR-10 and CIFAR-100 as well as overall NAS methods on Imagenet.

### Strengths
- The method is well motivated, each problem encountered in the architecture generation process is clearly explained and their approach to solve it makes sense to me.
- The authors openly state the limitations and assumptions made by their framework, I appreciate the level of detail.
- Overall clearly written paper.

### Weaknesses
 - CIFAR-10, CIFAR-100 and Imagenet are benchmarks which the community has collectively overfit on. If time permits do you think you could provide results on a different modality, e.g. an NLP task?
- To better understand the variance of your method, could you rerun the architecture selection multiple times and also report conf. intervals over the variance of each architecture when run for 3-5 random initializations?
- As stated in their limitations, the method largely relies on ZC proxies for both G-VAE and the generation of the macro architecture. The reliance on zero-cost proxies, while computationally efficient, introduces a potential bias towards architectures that perform well under these proxies, which may not always correlate with actual performance after training. This is a crucial limitation, as the method's effectiveness is directly tied to the reliability of these proxies.
- Code was not submitted alongside the submission.

### Questions
- How do you estimate the number of components for the GMM?
- Why is the cost of the ES for training the SG such a major bottleneck when using ZC proxies? Did you parallelize ES?


Typos (only minor, just listing them for completeness):
- 'even the best searching algorithm' -> 'even the best search algorithm'
- '... impressive results for modelling highly-dimensional conditional ...' -> '... impressive results for modelling high-dimensional conditional ...'
- 'to a continues latent space' -> 'to a continuous latent space'

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
