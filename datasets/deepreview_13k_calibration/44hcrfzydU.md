# FedTMOS: Efficient One-Shot Federated Learning with Tsetlin Machine

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
One-Shot Federated Learning (OFL) is a promising approach that reduce communication to a single round, minimizing latency and resource consumption. However, existing OFL methods often rely on Knowledge Distillation, which adds a training phase and increases server-side latency. Their performance can also be compromised by the quality of generated data or public datasets, resulting in sub-optimal server models. To address these challenges, we proposed One-Shot Federated Learning with Tsetlin Machine (FedTMOS), a novel data-free OFL framework built upon the low-complexity and class-adaptive properties of the Tsetlin Machine. FedTMOS first clusters then reassigns class-specific weights to form models using an inter-class maximization approach, generating balanced and efficient server models without requiring additional training. Our extensive experiments demonstrate that FedTMOS significantly outperforms its ensemble counterpart by an average of $6.16\%$, and the leading state-of-the-art OFL baselines by $7.22\%$ across various OFL settings. Moreover, FedTMOS achieves at least a $2.3\times$ reduction in upload communication costs and a $75\times$ reduction in server latency compared to methods requiring server-side training. These results establish FedTMOS as a highly efficient and practical solution for OFL scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents FedTMOS, a compute efficient one-shot Federated Learning (FL) algorithm that leverages Tsetlin Machines. Tsetlin Machines present an alternative to DNNs, known for their low complexity, compute and storage efficiency along with good performance. FedTMOS learns client-specific TMs and derives an aggregated server side TM that enhances class distinction. The aggregation procedure is significantly cheaper than traditional KD based methods while being data-free. The authors show comprehensive empirical results on standard OFL benchmarks under non-IID data.

### Strengths
- The application of Tsetlin Machines to OFL is novel and offers an interesting alternative to standard KD based methods which are compute intensive
- The method is data-free
- The authors provide comprehensive evaluations on communication and compute efficiency alongside accuracy which showcase the strength of the approach

### Weaknesses
- It is unclear whether the performance improvement in Table 1 comes from the performance gap between the CNNs and CTM. It is suggestted to report the performance of CNNs and CTM in a centralized(non-federated learning) setting.
- My main concern with this work is its applicability, as it is limited to a specific machine learning model. In my view, machine learning models and tasks should primarily serve as a testbed for evaluating federated learning algorithms. They should not be restricted to particular models, unless exploring new applications of federated learning in emerging areas, such as diffusion models or large language models. However, this paper addresses a well-established image classification task and is effective only for the Tsetlin Machine, which limits its practical application. The lack of exploration with more complex models or tasks raises concerns about the generalizability of the proposed approach.
- The readability of this paper can be further improved. For instance, in line 146, what does the $j$ of $L_j$ stand for, and how to get the definition of the $L_j$ from the definition of $L$?

### Questions
1) The authors mention using a standard compute node for evaluating server side latency. Does this mean that the node was GPU equipped? It would be unfair to measure the latency of DNN based approaches without using a GPU equipped node.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors leveraged Testlin Machine to resolve the bottleneck in one-shot federated learning, saving the communication cost and reducing the necessity of using a public dataset. The proposed solution views the one-shot federated learning in a different prospective, in the form of automation machines.

### Strengths
1. The idea of introducing Testlin Machine into one-shot federated learning is innovative, aiming to solve the bottleneck of using public datasets.

2. The authors clearly described the background, laying emphasis on Testlin Machine, making the paper self-contained.

3. The authors evaluated the solutions over client numbers of a certain scale, e.g. 20, 50, 80, which is a critical factor in one-shot federated learning.

### Weaknesses
1. The reviewer acknowledges the innovation of introducing Testlin Machine, however the motivation for doing so is not well explained. The authors spent certain paragraphs describing  Automation Machine and the mechanisms in machine learning. Nevertheless, how such a mechanism can benefit machine learning and federated learning is not illustrated. Moreover, why the key bottleneck in one-shot federated learning can be resolved is not explained. In other words, the current solution looks like converting a conventional question into a mechanism of a automation machine. For example, it likes a task converting a coding task into Moore Machine in algorithm lectures.

2 Many choices of approaches are not well justified. See more details in the reviewer's questions.

3. The empirical evaluation can be improved. The authors claimed that they used various datasets. However, these are very basic datasets like MNIST,SVHN, and CIFAR10. The reviewer suggested using more complex datasets such as Tiny-ImageNet. For datasets like MNIST, even if we are not doing one-shot federated learning, few epochs and communication rounds are needed to achieve convergence. The effectiveness, particularly in terms of convergence and accuracy, can be correctly justified by using a more complex dataset. 

Other minor writing issues:
1. The acronym in the paper is not of common use. OFL is not a common usage for one-shot federated learning. Directly saying one-shot FL is fine. TM is usually referred to Turing Machine.
2. Table 1 and Table 4 are out of bounds.

### Questions
1. Why do authors typically introduce Testlin Machine, which is an automation machine rather than leveraging a general reinforcement learning scheme where penalty, reward, and stage changing are involved? What is the motivation for doing so? How different is the solution with general reinforcement learning based one-shot FL? e.g. 

2 It is not common to use Gini index to measure data distribution. There are more common solutions. For example, the simplest way is Gaussian Model. But it is possible that clients data are non-i.i.d. In that case, a simple solution is to do some sampling. In some semi-supervised federated learning, uploading hard or soft labels is also fine.  Choosing Gini index is neither a straightforward nor a trivial option. How did you come up with that? And why can authors benefit from that?

### Soundness
2

### Presentation
2

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
This paper propose FedTMOS for efficient one-shot federated learning (FL). FedTMOS employs Tsetlin Machine instead of DNNs to reduce upload costs and presents a novel data-free solution to generate server model. Experimental results show that FedTMOS outperforms existing one-shot FL methods.

### Strengths
- Employing Tsetlin Machine in one-shot federated learning is interesting.
- The proposed FedTMOS significantly reduce the communication costs.

### Weaknesses
- It is unclear whether the performance improvement in Table 1 comes from the performance gap between the CNNs and CTM. It is suggestted to report the performance of CNNs and CTM in a centralized(non-federated learning) setting.
- My main concern with this work is its applicability, as it is limited to a specific machine learning model. In my view, machine learning models and tasks should primarily serve as a testbed for evaluating federated learning algorithms. They should not be restricted to particular models, unless exploring new applications of federated learning in emerging areas, such as diffusion models or large language models. However, this paper addresses a well-established image classification task and is effective only for the Tsetlin Machine, which limits its practical application.
- The readability of this paper can be further improved. For instance, in line 146, what does the $j$ of $L_j$ stand for, and how to get the definition of the $L_j$ from the definition of $L$?

### Questions
- Since FedTMOS uses a non-DNN model, is its scalability being limited by Tsetin Machine? Can it achieve comparable performance when other baseline methods employ stronger networks (e.g., ResNet) on challenging datasets (e.g., Tiny-ImageNet)?

### Soundness
2

### Presentation
1

### Contribution
2
