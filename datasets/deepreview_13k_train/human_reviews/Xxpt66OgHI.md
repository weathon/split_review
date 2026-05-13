# LEGACY: A Lightweight Adaptive Gradient Compression Strategy for Distributed Deep Learning

- Decision: Reject
- Scores: 3, 5, 5

## Abstract
Distributed learning has demonstrated remarkable success in training deep neural networks (DNNs) on large datasets, but the communication bottleneck reduces its scalability. Various compression techniques are proposed to alleviate this limitation; often they rely on computationally intensive methods to determine optimal compression parameters during training and are popularly referred to as adaptive compressors. Instead of the hard-to-tune hyperparameters for adaptive compressors, in this paper, we investigate the impact of two fundamental factors in DNN training, the layer size of the DNNs and their training phases, to design a simple yet efficient adaptive scheduler for any compressors to guide the compression parameters selection. We present a **L**ightweight **E**fficient **G**r**A**dient *C*ompression strateg**Y** or LEGACY that, in theory, can work with any compression technique to produce its simple adaptive counterpart. We benchmark LEGACY on distributed and federated training, involving 6 different DNN architectures for various tasks performed on large and challenging datasets, including ImageNet and WikiText-103. On ImageNet training, by sending similar average data volume, LEGACY's adaptive compression strategies improve the Top-1 accuracy of ResNet-50 by 7%-11%, compared to the uniform Top-0.1% compression used throughout the training. Similarly, on WikiText-103, by using our layer-based adaptive compression strategy and sending similar average data volume, the perplexity of the Transformer-XL improves $\sim$26% more than the uniform Top-0.1% compression used throughout the training. We publish anonymized code at: https://github.com/LEGACY-compression/LEGACY.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces LEGACY, an adaptive framework for gradient compression in distributed deep neural network training. This framework dynamically adjusts compression parameters based on layer size or training phase, depending on the user choice, to leverage the observation that smaller layers and the initial stages of training are more sensitive to aggressive compression. The authors provide theoretical intuitions to justify the adaptive scheduling approach, showing that it aligns with the convergence behavior of compressed stochastic gradient descent. The authors benchmarked the proposed algorithm across six DNN architectures and five datasets with different parameters against Top-k and random-k sparsification.  In summary, the paper presents a novel and practical approach to adaptive gradient sparsification, offering a scalable and efficient solution for distributed deep learning training across various applications.

### Strengths
The paper touches upon a very important challenge in training neural networks. To make training more efficient and scalable, there has been tremendous work on gradient compression to tackle the communication bottleneck in the distributed setup. However, over the past few years, some solutions have been proposed beyond the one-fits-all strategy, and ways have been developed to identify the compression adaptively during the training and for each layer. Further exploring this direction would allow us to exploit gradient compression's power to accelerate fully.

The paper looks into two different properties of neural network training, the importance of layer size and training stages in gradient sparsification, aiming to make gradient compression even more efficient. 

One of the main strengths of the proposed method is its lightweight design, allowing for easy integration with NCCL, a popular library for distributed training. This accessibility means that the method could be widely adopted in practice without adding significant complexity, a crucial advantage in large-scale applications.

Moreover, the authors offer valuable theoretical insights, explaining why higher compression might be especially effective in the later stages of training. This theoretical perspective strengthens the overall argument and adds a layer of rigor to the paper’s contributions, making it both informative and practical.

### Weaknesses
 - The paper lacks benchmarking against a closely related work, the L-GreCo method by Markov et al. (2024), which also aims to find optimal parameters per layer at each iteration. For instance, Markov et al. reported that L-GreCo achieves 76.85% accuracy on ResNet50 on ImageNet with a 45.6x compression ratio. Including a comparison with this approach would provide a stronger baseline and help clarify the performance gains offered by LEGACY.

- Although the paper suggests that the method can integrate with other compression techniques like quantization and low-rank decomposition, all experiments focus solely on sparsification. Additional experiments with various compression methods would demonstrate the flexibility and versatility of LEGACY in handling different compression techniques.

- The experiments focus primarily on a single compression regime. Testing LEGACY across different compression levels—both high and low—would help evaluate its performance against uniform sparsification and adaptive compression methods in varied regimes.

- The motivation behind the framework relies on two observations: increasing compression towards the end of training and applying higher compression to larger layers. However, the framework allows only one of these settings to be chosen at a time. A combined approach that integrates both strategies could offer a more comprehensive solution.

- A potential way the method can be improved is by considering the sequential order in which gradients are sent during backpropagation. Since gradients are transferred layer by layer from the last to the first, adjusting compression based on this order, in addition to layer size and training phase, might further enhance efficiency. For instance, prioritizing higher compression on gradients for earlier layers could optimize transfer times, as these gradients are sent later in the process.


Updates after the rebuttals:

Legacy introduces a framework that adaptively selects compression ratios during training and across layers by specifying compression parameters for different training phases or layer groups. However, two closely related works leverage similar ideas.

The first is Accordion by Agarwal et al., which adjusts compression levels during training based on critical training regimes. Accordion uses gradient norms as a proxy for the importance of the training phase, practically leading to less compression at the start of training or after learning rate reductions—aligning closely with Legacy's first mode. When comparing the two, Legacy offers more granular training phases and compression levels (which could be integrated into Accordion via multiple gradient thresholds). Legacy is computation-free, whereas Accordion accumulates gradients, a process with minimal overhead. However, Legacy requires manual specification of training phases, offering flexibility at the expense of additional hyperparameter tuning.

The second is L-GreCo by Markov et al., which employs low-overhead dynamic programming to optimize layer-wise parameters during training. This method leverages varying sizes and layers' sensitivities. In comparison, Legacy enables grouping layers by size and assigning compression parameters per group, while L-GreCo requires a range of possible compression choices and a uniform baseline for error bounds to find each layer's compression level optimally. L-GreCo also accumulates gradients and uses an efficient dynamic programming step, which, as reported in Table 1 of their paper, typically adds less than 0.5% to training time.

Moreover, as shown in Figure 6.a. of L-GreCo, it is possible to combine the approaches of L-GreCo and Accordion for a training-phase- and layer-aware adaptive compression method that outperforms previous adaptive techniques. Legacy could also combine these observations with additional parameter choices. 

While the authors emphasize that Legacy is computation-free and preferable in low-bandwidth federated settings, to my understanding, prior methods have negligible computational overhead, making this advantage less compelling.

Regarding scalability, I acknowledge the computational demands of large-scale experiments and wouldn't penalize the paper for lack of such experiments. However, I question whether trends observed on ResNet18 with CIFAR-100 are generalizable to more complex tasks and datasets.

In conclusion, Legacy builds on two previously explored observations and introduces additional hyperparameter requirements. Given this, I find the paper's contribution unclear and will maintain my score (not due to a lack of large-scale experiments). I welcome further discussion if needed and encourage the authors to refrain from personal remarks towards reviewers.

### Questions
- How should the parameters for defining the "begin" and "end" training stages, or "small" and "large" layers, be chosen, potentially to match a specific uniform sparsification baseline? How does the proposed method decide between different compression parameter sets?

- Have the authors considered incorporating factors beyond layer size, such as layer type, into their compression framework? Certain layers may have varying sensitivity to compression; for instance, in CNNs, initial convolutional layers are likely less sensitive than later layers that capture finer features. Would accounting for these sensitivity differences enhance the framework's adaptability and performance?

- There is limited guidance on how to select parameters for defining the "begin" and "end" training stages or for distinguishing between "small" and "large" layers, as both of these could vary for different models and training purposes. How the following parameters would be chosen for a new task?

- How does the model distinguish between different sets of parameters and decide which set is better? Should these parameters be treated as hyperparameters that require tuning?

- In Figure 1, smaller layers are described as having less compression, yet the figure indicates a higher compression ratio for these layers. Is there a specific reason for this or a possible mismatch between the figure and the intended interpretation?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel adaptive gradient compressor named LEGACY, to improve the communication efficiency of deep neural networks in distributed training. The performance of LEGACY in different models and tasks is verified by experiment, and its advantages over existing compression methods are demonstrated. Based on the information of layer size and training stage, this study provides a framework for dynamically selecting compression parameters, thus reducing the communication overhead while ensuring model performance

### Strengths
The LEGACY strategy combines the dynamic adjustment of the layer size and training phase, providing a new idea for adaptive compression, and has some innovation.

This paper provides sufficient empirical data to support the effectiveness of the proposed method through experiments on a variety of DNN architectures and tasks.

LEGACY is compatible with a wide range of compression technologies and is adaptable to different DNN models and data sets

### Weaknesses
Introduction part seems to describe to much details about the experiment. Though I understand that the author wants to show the finds of two key factors, it’s better to write in the later section instead of the Introduction section. Overall, the organization of the whole article needs to be improved.

The author seems to have identified only two key factors and tried to apply them. But in fact, no specific algorithm has been proposed to achieve true adaptive mechanism, so the innovation point is not enough.

Although the paper introduces two key factors for adaptive compression (training phase and layer size), it lacks a rigorous theoretical foundation to support their combined effects.  Without a deeper theoretical framework, it is challenging to determine whether these factors are universally applicable across diverse model architectures and datasets.

How is the list of LEGACY compression factors selected? It doesn't seem to be adaptive. 

In line 323, the author give the point that “LEGACYcan be used for uplink and downlink bidirectional compression”. However, the principle of upstream compression and downstream compression is not exactly the same, how to prove that this method can be applied to downstream compression?

Whether this method can be integrated with hard threshold compressors and how it works? The selection of threshold is different among different models and it’s hard to define.

### Questions
How is the list of LEGACY compression factors selected? It doesn't seem to be adaptive. 

In line 323, the author give the point that “LEGACYcan be used for uplink and downlink bidirectional compression”. However, the principle of upstream compression and downstream compression is not exactly the same, how to prove that this method can be applied to downstream compression?

Whether this method can be integrated with hard threshold compressors and how it works? The selection of threshold is different among different models and it’s hard to define.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper focuses on the problem of gradient compression in distributed learning. The main contribution is an adaptive scheduler for any compressors to guide the compression parameters selection. By taking into account the layer size of the DNNs and the training phases, the schedule is able to reduce communication overhead in an adaptive fashion. The approach can work with any compression technique. Experimental evaluation is performed on different models and datasets and shows very good results.

### Strengths
The paper is very clearly written and gives an excellent review of related work in the field. It very clearly states where its main contributions lie and back up the methodological contributions by theoretical analyses. I very much like the structure of the paper and the incorporation of the theoretical analysis. 
The paper is original in the sense that it targets a very specific question, newly training epoch and layer size dependency in distributed training. Although the experimental evaluation is performed on different datasets and models, it is difficult to say how generalisable the proposed approach really is and how impactful it is in practice.

### Weaknesses
The approach focuses on two aspects, namely training epoch and layer size dependency. Are these the only two aspects which are important or are there more aspects, such as layer type or activation function, which are not included but which are relevant in practice? It is unclear if the proposed adaptive schedule would generalize to other factors beyond these two. 
The practical impact of the proposed approach is not 100% clear. While the paper shows compression results, it does not clearly articulate what these results mean in practice in terms of actual training time or resource savings. What are the limitations of the approach in terms of the types of models or training scenarios where it might not be effective? The method uses Top-k as the base compressor, but there are many more methods in the field, such as quantization or low-rank approximation. How does the approach compare to these other compression techniques, and under what conditions might they be more suitable? 
Since the technical contribution of the paper is rather limited, proposing a heuristic adaptive scheduling approach, the experimental evaluation could contain more in-depth analyses. For example, it would be beneficial to see a breakdown of the communication overhead reduction and the impact on training time, as well as analyses showing the real practical benefits of the approach in different distributed training settings.

### Questions
Are other aspects beyond training epoch and layer size dependent relevant, which are not considered here?
What are the limitations of the approach?
What are the practical benefits?

### Soundness
3

### Presentation
3

### Contribution
3
